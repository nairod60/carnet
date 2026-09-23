# -*- coding: utf-8 -*-
"""Pictogrammes des exercices de rééducation (séance R), dessinés en SVG : bonshommes, pointillé = départ,
trait plein = arrivée, flèche terre cuite = mouvement, vert = élastique. Couleurs en variables CSS de l'appli
(thème clair/sombre). Clé = nom exact de l'exercice dans prog.py ; build_data.py les attache à data.json.
Même dessin que la fiche A4 plan/fiches/Mercredi-posture-epaule.png."""
import html as H

INK, MUTED, CLAY, GREEN, GREEN_T, LINE = "var(--ink)", "var(--muted)", "var(--clay)", "var(--green)", "var(--green-tint)", "var(--line)"
MONO = "JetBrains Mono, Consolas, monospace"

S = f'stroke="{INK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"'
SD = f'stroke="{MUTED}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" fill="none" stroke-dasharray="5 6"'
SA = f'stroke="{CLAY}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" fill="none"'
SP = f'stroke="{MUTED}" stroke-width="3" stroke-linecap="round" fill="none"'  # décor (mur, banc)

def head(x, y, r=12, dashed=False):
    return f'<circle cx="{x}" cy="{y}" r="{r}" {SD if dashed else S}/>'
def line(pts, dashed=False, style=None):
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    return f'<path d="{d}" {style or (SD if dashed else S)}/>'
def arrow(pts, curve=None):
    """flèche terre cuite ; curve = (cx, cy) point de contrôle quadratique"""
    if curve:
        (x0, y0), (x1, y1) = pts
        d = f"M{x0} {y0} Q{curve[0]} {curve[1]} {x1} {y1}"
    else:
        d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    return f'<path d="{d}" {SA} marker-end="url(#ar)"/>'
def dumbbell(x, y, ang=0):
    return f'<g transform="translate({x} {y}) rotate({ang})"><path d="M-9 0 L9 0" {S}/><rect x="-13" y="-6" width="6" height="12" rx="1.5" fill="{INK}"/><rect x="7" y="-6" width="6" height="12" rx="1.5" fill="{INK}"/></g>'
def band(pts):
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    return f'<path d="{d}" stroke="{GREEN}" stroke-width="3" stroke-linecap="round" fill="none"/>'
def wall(x, y0, y1):
    return f'<path d="M{x} {y0} L{x} {y1}" stroke="{MUTED}" stroke-width="7" stroke-linecap="butt"/><path d="M{x} {y0} L{x} {y1}" stroke="{LINE}" stroke-width="3" stroke-dasharray="4 8"/>'
def floor(y=138):
    return f'<path d="M6 {y} L194 {y}" stroke="{LINE}" stroke-width="2"/>'
def bench(x0, x1, y):
    return f'<rect x="{x0}" y="{y}" width="{x1-x0}" height="9" rx="2" fill="{MUTED}"/><path d="M{x0+8} {y+9} L{x0+8} {y+30} M{x1-8} {y+9} L{x1-8} {y+30}" {SP}/>'
def label(x, y, t, col=CLAY):
    return f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="11" font-weight="600" fill="{col}">{H.escape(t)}</text>'

def svg(body):
    """Le marqueur de flèche est renommé après coup (id unique par pictogramme, voir PICTOS)."""
    return (f'<svg viewBox="0 0 200 145" xmlns="http://www.w3.org/2000/svg">'
            f'<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{CLAY}"/></marker></defs>{body}</svg>')

# ------------------------------------------------------------ pictogrammes
P = {}

# 1. Rentré de menton (profil, buste) : tête avancée en pointillé -> tête reculée, flèche vers l'arrière
P["menton"] = svg(
    head(128, 42, 15, dashed=True) + line([(122, 56), (112, 80)], dashed=True)
    + head(108, 42, 15) + line([(105, 57), (104, 80)])
    + line([(70, 82), (145, 82)]) + line([(104, 82), (104, 125)])
    + arrow([(165, 42), (128, 42)]))

# 2. Extension du haut du dos sur le banc : allongé en travers, bord du banc sous les omoplates, on se laisse aller
P["thoracique"] = svg(
    floor() + bench(58, 118, 100)
    + line([(170, 138), (160, 112), (140, 108)])          # jambes pliées, pieds au sol
    + line([(140, 108), (100, 98)])                       # bassin -> omoplates (sur le bord du banc)
    + line([(100, 98), (72, 112)], dashed=False)          # buste qui bascule en arrière
    + head(56, 122, 12)
    + line([(72, 108), (60, 104), (52, 112)])             # mains derrière la tête
    + arrow([(112, 70), (78, 92)], curve=(88, 66)))

# 3. Étirement trapèze supérieur : tête inclinée, main sur la tête, épaule opposée basse
P["trapeze"] = svg(
    head(96, 40, 13) + line([(104, 52), (108, 70)])
    + line([(72, 72), (140, 72)]) + line([(108, 72), (108, 128)])
    + line([(140, 72), (146, 48), (118, 28), (100, 30)])  # bras qui passe sur la tête
    + line([(72, 72), (66, 100)])                          # bras opposé relâché vers le sol
    + arrow([(86, 22), (74, 40)], curve=(76, 28))
    + arrow([(66, 104), (66, 120)])
    + label(118, 118, "30 s"))

# 4. Rotation externe couché sur le côté : coude collé au flanc, avant-bras du sol vers le plafond
P["rot_ext"] = svg(
    floor(126) + head(38, 108, 12)
    + line([(50, 104), (150, 100)]) + line([(150, 100), (178, 112), (176, 126)])
    + line([(46, 122), (40, 130)], style=SP)                   # bras du dessous replié
    + line([(78, 104), (104, 100)])                            # bras du dessus : épaule -> coude
    + line([(104, 100), (108, 122)], dashed=True) + dumbbell(110, 126, 90)   # départ : vers le sol (pointillé)
    + line([(104, 100), (106, 62)]) + dumbbell(106, 54, 90)                  # arrivée : vers le plafond
    + arrow([(126, 118), (128, 64)], curve=(142, 92)))

# 5. Rotation interne à l'élastique : face, coude au corps, l'avant-bras vient vers le ventre
P["rot_int"] = svg(
    head(100, 26, 12) + line([(100, 38), (100, 60)]) + line([(68, 60), (132, 60)])
    + line([(100, 60), (100, 118)]) + line([(100, 118), (88, 140)]) + line([(100, 118), (112, 140)])
    + line([(68, 60), (62, 100)])
    + line([(132, 60), (136, 88)])                                   # épaule -> coude (collé au corps)
    + line([(136, 88), (178, 88)], dashed=True)                      # départ : avant-bras vers l'extérieur
    + band([(178, 88), (196, 86)]) + f'<rect x="192" y="70" width="6" height="34" fill="{MUTED}"/>'
    + line([(136, 88), (98, 92)])                                    # arrivée : avant-bras devant le ventre
    + band([(98, 92), (196, 86)])
    + arrow([(172, 100), (110, 104)], curve=(140, 118)))

# 6. Abaissement à l'élastique : élastique en haut (barre de traction), bras tendu poussé vers le bas et l'arrière
P["abaissement"] = svg(
    floor() + f'<path d="M90 12 L196 12" stroke="{MUTED}" stroke-width="7" stroke-linecap="round"/>'
    + head(100, 46, 12) + line([(100, 58), (100, 108)]) + line([(100, 108), (90, 138)]) + line([(100, 108), (112, 138)])
    + line([(100, 66), (150, 50)], dashed=True)                       # départ : bras tendu devant
    + band([(150, 50), (150, 12)])
    + line([(100, 66), (104, 118)])                                    # arrivée : bras tendu le long du corps, un peu en arrière
    + band([(104, 118), (150, 12)])
    + arrow([(158, 66), (118, 122)], curve=(160, 108)) + label(150, 134, "5 s"))

# 7. Isométriques contre le mur : coude à 90°, dos de la main contre le mur, on pousse sans bouger
P["iso"] = svg(
    floor() + wall(166, 20, 138)
    + head(96, 26, 12) + line([(96, 38), (96, 60)]) + line([(64, 60), (128, 60)])
    + line([(96, 60), (96, 112)]) + line([(96, 112), (86, 138)]) + line([(96, 112), (108, 138)])
    + line([(64, 60), (58, 100)])
    + line([(128, 60), (132, 90), (163, 90)])                          # coude au corps, avant-bras vers le mur
    + arrow([(140, 104), (160, 104)]) + label(126, 124, "10 s"))

# 8. Anges au mur : dos au mur, coudes/poignets en contact, position W (pointillé) -> Y
P["anges"] = svg(
    f'<rect x="30" y="8" width="140" height="130" rx="4" fill="{GREEN_T}"/>'
    + head(100, 30, 12) + line([(100, 42), (100, 62)]) + line([(70, 62), (130, 62)])
    + line([(100, 62), (100, 116)]) + line([(100, 116), (90, 138)]) + line([(100, 116), (110, 138)])
    + line([(70, 62), (54, 78), (54, 50)], dashed=True) + line([(130, 62), (146, 78), (146, 50)], dashed=True)  # W
    + line([(70, 62), (52, 40), (52, 12)]) + line([(130, 62), (148, 40), (148, 12)])                            # Y
    + arrow([(40, 62), (40, 22)]) + arrow([(160, 62), (160, 22)]))

# 9. Face pull : élastique à hauteur du visage, on tire vers le front, coudes hauts, omoplates serrées
P["facepull"] = svg(
    f'<rect x="4" y="30" width="6" height="40" fill="{MUTED}"/>'
    + head(112, 46, 12) + line([(112, 58), (112, 110)]) + line([(112, 110), (102, 138)]) + line([(112, 110), (124, 138)])
    + line([(112, 66), (60, 52)], dashed=True) + band([(60, 52), (10, 50)])        # départ : bras tendus vers l'ancrage
    + line([(112, 66), (124, 44), (96, 44)]) + band([(96, 44), (10, 50)])           # arrivée : coude haut, main au front
    + arrow([(56, 68), (92, 62)], curve=(74, 84)))

# 10. Pompes au mur + poussée finale : bras tendus, on écarte les omoplates (le haut du dos s'arrondit un peu)
P["dentele"] = svg(
    floor() + wall(28, 20, 138)
    + head(104, 40, 12) + line([(102, 52), (96, 74)]) + line([(96, 74), (110, 96)]) + line([(110, 96), (128, 112)])   # buste incliné
    + line([(128, 112), (150, 138)]) + line([(128, 112), (144, 138)])
    + line([(96, 74), (60, 74)]) + line([(60, 74), (32, 78)])                                                             # bras tendus vers le mur
    + arrow([(96, 56), (116, 56)]) + label(120, 60, "+"))

# 11. Étirement pectoral à la porte : avant-bras sur le montant, coude à hauteur d'épaule, on avance
P["pectoral"] = svg(
    floor() + f'<rect x="150" y="10" width="8" height="128" rx="2" fill="{MUTED}"/>'
    + head(96, 40, 12) + line([(96, 52), (98, 108)]) + line([(98, 108), (88, 138)]) + line([(98, 108), (112, 138)])
    + line([(96, 60), (150, 56)]) + line([(150, 56), (150, 26)])
    + arrow([(112, 84), (134, 84)]) + label(8, 24, "30 s"))


NOMS = {"menton": "Rentrés de menton", "thoracique": "Extension du haut du dos sur le banc",
        "trapeze": "Étirement du trapèze supérieur", "rot_ext": "Rotation externe couchée sur le côté",
        "rot_int": "Rotation interne à l'élastique", "abaissement": "Abaissement à l'élastique",
        "iso": "Isométriques contre le mur", "anges": "Anges au mur", "facepull": "Face pull à l'élastique",
        "dentele": "Pompes au mur avec poussée finale", "pectoral": "Étirement du pectoral à la porte"}
PICTOS = {NOMS[k]: v.replace('id="ar"', f'id="ar-{k}"').replace('url(#ar)', f'url(#ar-{k})') for k, v in P.items()}

# Photos (plan/photos/, JPEG ≤ 1000 px de large, ~40 Ko) : quand une photo existe, elle remplace le dessin dans l'appli.
PHOTOS = {"Rotation externe couchée sur le côté": "photos/rotation-externe.jpg"}
