# -*- coding: utf-8 -*-
import os, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fiches")  # fiches A4 générées ici
os.makedirs(OUT, exist_ok=True)

ACCENT, ACCENT_TINT = "#45682F", "#EDF1E5"
CLAY,   CLAY_TINT   = "#9A4E2C", "#F6E9E1"
INK, INK2, MUTED    = "#1A1D14", "#4C5243", "#7B8071"
LINE, LINE_SOFT     = "#D6D7CB", "#E9E9E0"

SANS = "'IBM Plex Sans', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
DISP = "'Bricolage Grotesque', 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "'IBM Plex Mono', ui-monospace, 'SF Mono', Menlo, Consolas, monospace"

FONTS = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..700"
         "&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap")

# ---------------------------------------------------------------- donnees
# (libelle, poids, mention)  -- mention = "cru" / "crues" / "" / note libre
DAYS = [
 dict(file="Main.dc.html", nom="Lundi", num=1, train=True, kcal="2889", p="193", g="333", l="81",
      meals=[
        ("Petit-déjeuner","","545", [("Œufs entiers","3","150 g"),("Pain complet","90 g",""),
            ("Banane","120 g","")]),
        ("Collation 10 h","whey + avoine, au shaker","380", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Flocons d\'avoine","40 g","")]),
        ("Déjeuner","Salade de riz au thon","690", [("Thon au naturel égoutté","130 g",""),("Riz basmati","90 g","cru"),
            ("Tomates","150 g",""),("Concombre","150 g",""),("Œuf dur","1","50 g"),("Huile d'olive","12 g",""),
            ("Vinaigre, moutarde","","libre")]),
        ("Avant la séance","≈ 90 min avant","105", [("Banane","120 g","")]),
        ("Après la séance","dans l'heure","335", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Banane","120 g","")]),
        ("Dîner","Poulet aux poivrons, riz","715", [("Blanc de poulet","150 g","cru"),("Poivrons","250 g",""),
            ("Riz basmati","100 g","cru"),("Huile d'olive","15 g",""),("Ail, paprika, cumin","","libre")]),
        ("Avant de dormir","","115", [("Amandes","20 g","")]),
      ],
      batch="Cuis 300 g de poulet et 190 g de riz crus (100 pour ce soir, 90 pour la salade). La moitié se mange chaude ce soir, l'autre moitié refroidit pour la salade de riz de mardi midi."),

 dict(file="Mardi.dc.html", nom="Mardi", num=2, train=True, kcal="2774", p="187", g="304", l="82",
      meals=[
        ("Petit-déjeuner","","515", [("Œufs entiers","3","150 g"),("Pain complet","90 g",""),("Pomme","150 g","")]),
        ("Collation 10 h","whey + avoine, au shaker","380", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Flocons d\'avoine","40 g","")]),
        ("Déjeuner","Salade de riz au poulet","635", [("Blanc de poulet","150 g","cru"),("Riz basmati","90 g","cru"),
            ("Tomates","150 g",""),("Concombre","150 g",""),("Huile d'olive","12 g",""),("Vinaigre, herbes","","libre")]),
        ("Avant la séance","≈ 90 min avant","105", [("Banane","120 g","")]),
        ("Après la séance","dans l'heure","335", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Banane","120 g","")]),
        ("Dîner","Steak, pommes de terre, haricots","685", [("Steak haché 5 %","160 g","cru"),
            ("Pommes de terre","350 g","crues"),("Haricots verts","200 g",""),("Huile d'olive","15 g","")]),
        ("Avant de dormir","","115", [("Amandes","20 g","")]),
      ],
      batch="Le steak reste une portion unique : il ne passe jamais au déjeuner. Fais juste cuire 90 g de riz cru en plus ce soir pour la salade au thon de demain."),

 dict(file="Mercredi.dc.html", nom="Mercredi", num=3, train=False, kcal="2618", p="204", g="267", l="76",
      meals=[
        ("Petit-déjeuner","","485", [("Œufs entiers","3","150 g"),("Pain complet","80 g",""),
            ("Kiwis","150 g","")]),
        ("Collation 10 h","whey + avoine, au shaker","380", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Flocons d\'avoine","40 g","")]),
        ("Déjeuner","Salade de riz au thon","715", [("Thon au naturel égoutté","130 g",""),("Riz basmati","90 g","cru"),
            ("Tomates","150 g",""),("Concombre","150 g",""),("Œuf dur","1","50 g"),("Huile d'olive","15 g",""),
            ("Vinaigre, moutarde","","libre")]),
        ("Collation","milieu d'après-midi","230", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml","")]),
        ("Dîner","Poulet, pâtes complètes, tomates, poivrons","715", [("Blanc de poulet","150 g","cru"),
            ("Pâtes complètes","100 g","crues"),("Tomates","150 g",""),("Poivrons","150 g",""),("Huile d'olive","15 g","")]),
        ("Avant de dormir","","70", [("Fromage blanc 0 %","150 g","")]),
      ],
      batch="Jour de repos. Cuis 300 g de poulet et 190 g de pâtes crues (100 pour ce soir, 90 pour la salade) : la moitié chaude ce soir, l'autre moitié refroidit pour la salade de pâtes de jeudi midi."),

 dict(file="Jeudi.dc.html", nom="Jeudi", num=4, train=True, kcal="2916", p="195", g="318", l="85",
      meals=[
        ("Petit-déjeuner","","505", [("Œufs entiers","3","150 g"),("Pain complet","90 g",""),("Orange","150 g","")]),
        ("Collation 10 h","whey + avoine, au shaker","380", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Flocons d\'avoine","40 g","")]),
        ("Déjeuner","Salade de pâtes au poulet","650", [("Blanc de poulet","150 g","cru"),("Pâtes complètes","90 g","crues"),
            ("Tomates","150 g",""),("Poivrons","100 g",""),("Olives","20 g",""),("Huile d'olive","10 g","")]),
        ("Avant la séance","≈ 90 min avant","105", [("Banane","120 g","")]),
        ("Après la séance","dans l'heure","335", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Banane","120 g","")]),
        ("Dîner","Steak, riz, haricots","815", [("Steak haché 5 %","160 g","cru"),("Riz basmati","110 g","cru"),
            ("Haricots verts","250 g",""),("Huile d'olive","15 g","")]),
        ("Avant de dormir","","115", [("Amandes","20 g","")]),
      ],
      batch="Steak en portion unique. Cuis 90 g de riz cru en plus pour la salade au saumon de demain midi."),

 dict(file="Vendredi.dc.html", nom="Vendredi", num=5, train=True, kcal="2776", p="185", g="310", l="81",
      meals=[
        ("Petit-déjeuner","","545", [("Œufs entiers","3","150 g"),("Pain complet","90 g",""),("Banane","120 g","")]),
        ("Collation 10 h","whey + avoine, au shaker","380", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Flocons d\'avoine","40 g","")]),
        ("Déjeuner","Salade de riz au saumon","660", [("Saumon en boîte égoutté","150 g",""),("Riz basmati","90 g","cru"),
            ("Tomates","150 g",""),("Concombre","150 g",""),("Huile d'olive","10 g",""),("Citron, aneth","","libre")]),
        ("Avant la séance","≈ 90 min avant","105", [("Banane","120 g","")]),
        ("Après la séance","dans l'heure","335", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Banane","120 g","")]),
        ("Dîner","Poulet, pommes de terre, haricots","630", [("Blanc de poulet","150 g","cru"),
            ("Pommes de terre","350 g","crues"),("Haricots verts","200 g",""),("Huile d'olive","15 g","")]),
        ("Avant de dormir","","115", [("Amandes","20 g","")]),
      ],
      batch="Poulet en portion unique ce soir. Cuis 650 g de pommes de terre crues : 350 chaudes ce soir, 300 refroidissent pour la salade au thon de samedi midi. Le saumon en boîte du midi remplace le poisson gras : c'est lui qui apporte tes oméga-3."),

 dict(file="Samedi.dc.html", nom="Samedi", num=6, train=False, kcal="2521", p="204", g="234", l="78",
      meals=[
        ("Petit-déjeuner","","490", [("Œufs entiers","3","150 g"),("Pain complet","80 g",""),
            ("Pomme","150 g","")]),
        ("Collation 10 h","whey + avoine, au shaker","380", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Flocons d\'avoine","40 g","")]),
        ("Déjeuner","Salade de pommes de terre au thon","640", [("Thon au naturel égoutté","130 g",""),
            ("Pommes de terre","300 g","crues"),("Haricots verts","200 g",""),("Tomates","100 g",""),
            ("Œuf dur","1","50 g"),("Huile d'olive","12 g",""),("Moutarde, vinaigre","","libre")]),
        ("Collation","milieu d'après-midi","345", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Amandes","20 g","")]),
        ("Dîner","Cabillaud, pommes de terre, haricots","590", [("Cabillaud ou colin","200 g","cru"),
            ("Pommes de terre","300 g","crues"),("Haricots verts","200 g",""),("Huile d'olive","15 g","")]),
        ("Avant de dormir","","70", [("Fromage blanc 0 %","150 g","")]),
      ],
      batch="Pendant que le poisson cuit, fais aussi cuire 150 g de poulet et 90 g de riz cru : ils refroidissent pour la salade de dimanche midi."),

 dict(file="Dimanche.dc.html", nom="Dimanche", num=7, train=False, kcal="2488", p="183", g="244", l="80",
      meals=[
        ("Petit-déjeuner","","505", [("Œufs entiers","3","150 g"),("Pain complet","80 g",""),
            ("Orange","150 g","")]),
        ("Collation 10 h","whey + avoine, au shaker","380", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Flocons d\'avoine","40 g","")]),
        ("Déjeuner","Salade de riz au poulet","635", [("Blanc de poulet","150 g","cru"),("Riz basmati","90 g","cru"),
            ("Tomates","150 g",""),("Concombre","150 g",""),("Huile d'olive","12 g",""),("Vinaigre, herbes","","libre")]),
        ("Collation","milieu d'après-midi","320", [("Whey Isostar","30 g",""),("Lait demi-écrémé","250 ml",""),("Fruit au choix","150 g","")]),
        ("Dîner","Omelette aux tomates","600", [("Œufs entiers","4","200 g"),("Tomates","150 g",""),
            ("Pain complet","80 g",""),("Huile d'olive","10 g","")]),
        ("Avant de dormir","","70", [("Fromage blanc 0 %","150 g","")]),
      ],
      batch="Fais juste cuire 90 g de riz cru pour la salade au thon de lundi midi. C'est aussi le moment des courses."),
]

E = html.escape

def item_row(label, poids, note, last):
    bb = "" if last else f"border-bottom: 1px dotted {LINE}; "
    right = ""
    if poids:
        right += f'<span style="font-family: {MONO}; font-size: 15px; font-weight: 500; color: {INK}; font-variant-numeric: tabular-nums; white-space: nowrap;">{E(poids)}</span>'
    if note:
        right += f'<span style="font-family: {MONO}; font-size: 12.5px; color: {MUTED}; letter-spacing: 0.03em; white-space: nowrap;">{E(note)}</span>'
    return (f'<div style="display: flex; justify-content: space-between; align-items: baseline; gap: 14px; '
            f'{bb}padding-bottom: 2px;">'
            f'<span style="font-size: 15px; line-height: 1.25; color: {INK2};">{E(label)}</span>'
            f'<span style="display: flex; align-items: baseline; gap: 7px;">{right}</span>'
            f'</div>')

def meal_block(nom, dish, kcal, items, accent):
    rows = "".join(item_row(l, p, n, i == len(items) - 1) for i, (l, p, n) in enumerate(items))
    sub = ""
    if dish:
        sub = (f'<div style="font-size: 14px; font-style: italic; color: {MUTED}; line-height: 1.3;">{E(dish)}</div>')
    return f'''<div style="display: grid; grid-template-columns: 172px 1fr; gap: 0 26px; border-top: 1px solid {LINE}; padding-top: 8px;">
  <div style="display: flex; flex-direction: column; gap: 3px;">
    <div style="display: flex; align-items: center; gap: 9px;">
      <span style="width: 13px; height: 13px; border: 1.2px solid #B7BDAC; border-radius: 2px; flex-shrink: 0;"></span>
      <span style="font-size: 16px; font-weight: 600; color: {INK}; line-height: 1.2;">{E(nom)}</span>
    </div>
    <div style="padding-left: 22px; display: flex; flex-direction: column; gap: 2px;">
      {sub}
      <div style="font-family: {MONO}; font-size: 13px; color: {accent}; font-weight: 500; font-variant-numeric: tabular-nums;">{E(kcal)} kcal</div>
    </div>
  </div>
  <div style="display: flex; flex-direction: column; gap: 3px;">{rows}</div>
</div>'''

def macro_cell(k, v, unit):
    return f'''<div style="background: #FFFFFF; padding: 8px 14px; display: flex; flex-direction: column; gap: 1px;">
  <div style="font-family: {MONO}; font-size: 10px; letter-spacing: 0.13em; text-transform: uppercase; color: {MUTED};">{E(k)}</div>
  <div style="font-family: {MONO}; font-size: 23px; font-weight: 600; color: {INK}; font-variant-numeric: tabular-nums; line-height: 1.1;">{E(v)}<span style="font-size: 12px; font-weight: 400; color: {MUTED}; margin-left: 3px;">{E(unit)}</span></div>
</div>'''

def build(d):
    accent = ACCENT if d["train"] else CLAY
    tint   = ACCENT_TINT if d["train"] else CLAY_TINT
    chip   = "Entraînement" if d["train"] else "Repos"
    whey   = "Whey 30 g à 10 h et 30 g après la séance" if d["train"] else "Whey 30 g à 10 h et 30 g l'après-midi"

    meals = "".join(meal_block(n, ds, k, it, accent) for n, ds, k, it in d["meals"])
    macros = (macro_cell("Total", d["kcal"], "kcal") + macro_cell("Protéines", d["p"], "g")
              + macro_cell("Glucides", d["g"], "g") + macro_cell("Lipides", d["l"], "g"))

    return f'''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="{FONTS}">
  <style>
    body {{ margin: 0; }}
    * {{ box-sizing: border-box; }}
    a {{ color: {ACCENT}; }}
    a:hover {{ color: #2F4A1F; }}
  </style>
</helmet>
<div style="width: 794px; height: 1123px; background: #FFFFFF; font-family: {SANS}; color: {INK}; display: flex; flex-direction: column;">

  <div style="height: 6px; background: {accent}; flex-shrink: 0;"></div>

  <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 12px; padding: 28px 50px 24px;">

    <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 20px;">
      <div style="display: flex; flex-direction: column; gap: 5px;">
        <div style="font-family: {MONO}; font-size: 10px; letter-spacing: 0.16em; text-transform: uppercase; color: {MUTED};">Prise de masse · 70 kg · semaine type</div>
        <h1 style="margin: 0; font-family: {DISP}; font-size: 36px; font-weight: 700; letter-spacing: -0.02em; line-height: 1; color: {INK};">{E(d["nom"])}</h1>
      </div>
      <div style="font-family: {MONO}; font-size: 10.5px; letter-spacing: 0.11em; text-transform: uppercase; color: {accent}; border: 1px solid {accent}; padding: 5px 11px; white-space: nowrap;">{E(chip)}</div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1px; background: {LINE}; border: 1px solid {LINE};">
      {macros}
    </div>

    <div style="display: flex; flex-direction: column; gap: 9px; flex-grow: 1; justify-content: space-between;">
      {meals}
    </div>

    <div style="background: {tint}; padding: 10px 16px; display: flex; flex-direction: column; gap: 3px;">
      <div style="font-family: {MONO}; font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; color: {accent};">À préparer ce soir</div>
      <div style="font-size: 14.5px; line-height: 1.45; color: {INK2};">{E(d["batch"])}</div>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; border-top: 1px solid {LINE}; padding-top: 9px; font-family: {MONO}; font-size: 11px; color: {MUTED}; letter-spacing: 0.02em;">
      <span>Tous les poids sont CRUS, avant cuisson · {E(whey)}</span>
      <span style="font-variant-numeric: tabular-nums;">{d["num"]} / 8</span>
    </div>

  </div>
</div>
</x-dc>
</body>
</html>
'''

for d in DAYS:
    with open(os.path.join(OUT, d["file"]), "w", encoding="utf-8") as f:
        f.write(build(d))
    print("ok", d["file"])

# ---- canvas.json : 7 planches A4, 4 + 3
import json
W, H, GX, GY = 794, 1123, 80, 130
boards = []
for i, d in enumerate(DAYS):
    col, row = i % 4, i // 4
    boards.append({"file": d["file"], "x": col * (W + GX), "y": row * (H + GY),
                   "w": W, "h": H, "title": d["nom"], "print": "fixed"})
canvas = {"artboards": boards, "launch": {"view": "canvas"}}
with open(os.path.join(OUT, "canvas.json"), "w", encoding="utf-8") as f:
    json.dump(canvas, f, ensure_ascii=False, indent=2)
print("ok canvas.json")

# ============================================================ planche 8
# La liste de courses est CALCULEE a partir des repas : elle ne peut plus diverger du plan.
RAYON = {
 "Blanc de poulet":("Protéines","g"),"Steak haché 5 %":("Protéines","g"),
 "Maquereau ou sardines":("Protéines","g"),"Cabillaud ou colin":("Protéines","g"),
 "Thon au naturel égoutté":("Protéines","boîte"),"Œufs entiers":("Protéines","oeufs"),
 "Fromage blanc 0 %":("Protéines","g"),"Whey Isostar":("Protéines","g"),"Lait écrémé":("Protéines","ml"),"Lait demi-écrémé":("Protéines","ml"),"Flocons d'avoine":("Féculents et gras","g"),
 "Riz basmati":("Féculents et gras","g"),"Pâtes complètes":("Féculents et gras","g"),
 "Pommes de terre":("Féculents et gras","g"),"Pain complet":("Féculents et gras","g"),
 "Amandes":("Féculents et gras","g"),"Huile d'olive":("Féculents et gras","ml"),
 "Courgettes":("Légumes et fruits","g"),"Haricots verts":("Légumes et fruits","g"),
 "Tomates":("Légumes et fruits","g"),"Tomates et courgettes":("Légumes et fruits","g"),
 "Concombre":("Légumes et fruits","g"),"Olives":("Féculents et gras","g"),
 "Saumon en boîte égoutté":("Protéines","g"),"Œuf dur":("Protéines","oeufs"),
 "Poivrons":("Légumes et fruits","g"),"Banane":("Légumes et fruits","fruits"),
 "Pomme":("Légumes et fruits","fruits"),"Kiwis":("Légumes et fruits","fruits"),
 "Orange":("Légumes et fruits","fruits"),"Fruit au choix":("Légumes et fruits","fruits"),
}
def _g(poids, note):
    import re as _re
    for t in (poids, note):
        m = _re.search(r"(\d+)\s*(?:g|ml)", t or "")
        if m: return float(m.group(1))
    return 0.0

def construire_courses(days):
    from collections import defaultdict
    tot = defaultdict(float)
    for d in days:
        for _, _, _, items in d["meals"]:
            for lab, poids, note in items:
                if lab not in RAYON: continue
                if lab == "Tomates et courgettes":
                    tot["Tomates"] += _g(poids, note)/2; tot["Courgettes"] += _g(poids, note)/2
                elif lab in ("Œufs entiers", "Œuf dur"):
                    tot["Œufs entiers"] += float(poids)
                elif lab == "Thon au naturel égoutté":
                    tot[lab] += _g(poids, note)
                else:
                    tot[lab] += _g(poids, note)
    def fmt(lab, v):
        u = RAYON[lab][1]
        if u == "oeufs":  return f"{v:.0f}"
        if u == "boîte":  return f"{-(-v // 100):.0f} boîtes"
        if u == "fruits":
            unite = {"Banane":120,"Pomme":150,"Kiwis":75,"Orange":150,"Fruit au choix":150}[lab]
            return f"{max(1, round(v/unite)):.0f}"
        if v >= 1000:     return f"{v/1000:.1f}".replace(".", ",").replace(",0", "") + (" kg" if u == "g" else " L")
        return f"{v:.0f} {u}"
    rayons = {}
    for lab, v in tot.items():
        if v <= 0: continue
        rayons.setdefault(RAYON[lab][0], []).append((lab, fmt(lab, v)))
    ordre = {"Protéines":0, "Féculents et gras":1, "Légumes et fruits":2}
    out = [(r, rayons[r]) for r in sorted(rayons, key=lambda x: ordre[x])]
    out[2][1].append(("Ail, citron, épices", "—"))
    return out

CONVERT = [("Riz basmati","90 g","≈ 260 g","× 2,9"),("Pâtes complètes","100 g","≈ 230 g","× 2,3"),
 ("Pommes de terre (eau/vapeur)","400 g","≈ 380 g","× 0,95"),("Blanc de poulet","180 g","≈ 135 g","× 0,75"),
 ("Steak haché 5 %","180 g","≈ 135 g","× 0,75"),("Poisson blanc","200 g","≈ 160 g","× 0,80"),
 ("Maquereau","150 g","≈ 120 g","× 0,80")]
PILOTAGE = [("+200 à +350 g / semaine","Tu es dans la cible. Ne touche à rien : c'est du muscle avec un peu de gras, la proportion normale.", False),
 ("Moins de +150 g pendant 3 semaines","Le surplus est trop petit pour ton métabolisme. Ajoute 150 kcal : 40 g de riz cru au dîner, ou 20 g d'avoine dans le shaker.", False),
 ("Plus de +500 g / semaine","Trop vite, c'est du gras. Retire 150 kcal : 40 g de riz cru en moins au dîner.", True),
 ("Tour de taille +2 cm en un mois","Tu stockes plus que tu ne construis. Retire 150 kcal et vérifie que les charges montent vraiment.", True),
 ("Balance à 17-18 % ou fin janvier","Fin de la prise de masse. On passe à la sèche : −450 kcal, protéines à 2,3 g/kg, dix semaines.", False)]

def build_annexe():
    A, T = ACCENT, ACCENT_TINT
    cols = "".join(f'''<div style="display: flex; flex-direction: column; gap: 3px;">
      <div style="font-family: {MONO}; font-size: 10px; letter-spacing: 0.13em; text-transform: uppercase; color: {MUTED}; border-bottom: 1px solid {LINE}; padding-bottom: 6px;">{E(cat)}</div>
      {"".join(f"""<div style="display: flex; justify-content: space-between; align-items: baseline; gap: 10px;"><span style="display: flex; align-items: center; gap: 8px;"><span style="width: 11px; height: 11px; border: 1.2px solid #B7BDAC; border-radius: 2px; flex-shrink: 0;"></span><span style="font-size: 14.5px; color: {INK2};">{E(n)}</span></span><span style="font-family: {MONO}; font-size: 14px; font-weight: 500; color: {INK}; font-variant-numeric: tabular-nums; white-space: nowrap;">{E(q)}</span></div>""" for n, q in items)}
    </div>''' for cat, items in construire_courses(DAYS))

    rows = "".join(f'''<tr>
      <td style="padding: 5px 12px; border-bottom: 1px solid {LINE_SOFT}; font-size: 14.5px; color: {INK2};">{E(a)}</td>
      <td style="padding: 5px 12px; border-bottom: 1px solid {LINE_SOFT}; font-family: {MONO}; font-size: 14px; color: {INK}; font-variant-numeric: tabular-nums;">{E(b)}</td>
      <td style="padding: 5px 12px; border-bottom: 1px solid {LINE_SOFT}; font-family: {MONO}; font-size: 14px; font-weight: 600; color: {A}; font-variant-numeric: tabular-nums;">{E(c)}</td>
      <td style="padding: 5px 12px; border-bottom: 1px solid {LINE_SOFT}; font-family: {MONO}; font-size: 13px; color: {MUTED}; font-variant-numeric: tabular-nums;">{E(d)}</td>
    </tr>''' for a, b, c, d in CONVERT)

    regles = "".join(f'''<div style="display: grid; grid-template-columns: 210px 1fr; gap: 0 20px; border-top: 1px solid {LINE_SOFT}; padding: 4px 0;">
      <div style="font-family: {MONO}; font-size: 12.5px; font-weight: 500; color: {CLAY if warn else A}; line-height: 1.35;">{E(cond)}</div>
      <div style="font-size: 14px; color: {INK2}; line-height: 1.45;">{E(txt)}</div>
    </div>''' for cond, txt, warn in PILOTAGE)

    return f'''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <link rel="stylesheet" href="{FONTS}">
  <style>
    body {{ margin: 0; }}
    * {{ box-sizing: border-box; }}
    table {{ border-collapse: collapse; width: 100%; }}
    a {{ color: {ACCENT}; }} a:hover {{ color: #2F4A1F; }}
  </style>
</helmet>
<div style="width: 794px; height: 1123px; background: #FFFFFF; font-family: {SANS}; color: {INK}; display: flex; flex-direction: column;">
  <div style="height: 6px; background: {A}; flex-shrink: 0;"></div>
  <div style="flex-grow: 1; display: flex; flex-direction: column; gap: 11px; padding: 30px 50px 24px;">

    <div style="display: flex; justify-content: space-between; align-items: flex-end; gap: 20px;">
      <div style="display: flex; flex-direction: column; gap: 5px;">
        <div style="font-family: {MONO}; font-size: 10px; letter-spacing: 0.16em; text-transform: uppercase; color: {MUTED};">Prise de masse · 70 kg · semaine type</div>
        <h1 style="margin: 0; font-family: {DISP}; font-size: 41px; font-weight: 700; letter-spacing: -0.02em; line-height: 1; color: {INK};">Courses &amp; repères</h1>
      </div>
      <div style="font-family: {MONO}; font-size: 10.5px; letter-spacing: 0.11em; text-transform: uppercase; color: {A}; border: 1px solid {A}; padding: 5px 11px; white-space: nowrap;">Une fois / semaine</div>
    </div>

    <div style="display: flex; flex-direction: column; gap: 11px;">
      <div style="font-family: {MONO}; font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase; color: {A};">La liste de courses · 7 jours, une personne</div>
      <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 26px;">{cols}</div>
    </div>

    <div style="display: flex; flex-direction: column; gap: 9px;">
      <div style="font-family: {MONO}; font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase; color: {A};">Cru vers cuit · si tu pèses dans l'assiette</div>
      <table>
        <thead><tr>
          <th style="text-align: left; padding: 5px 12px; background: {T}; font-family: {MONO}; font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: {MUTED}; font-weight: 500;">Aliment</th>
          <th style="text-align: left; padding: 5px 12px; background: {T}; font-family: {MONO}; font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: {MUTED}; font-weight: 500;">Poids cru</th>
          <th style="text-align: left; padding: 5px 12px; background: {T}; font-family: {MONO}; font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: {MUTED}; font-weight: 500;">≈ cuit</th>
          <th style="text-align: left; padding: 5px 12px; background: {T}; font-family: {MONO}; font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: {MUTED}; font-weight: 500;">Facteur</th>
        </tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>

    <div style="display: flex; flex-direction: column; gap: 4px;">
      <div style="font-family: {MONO}; font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase; color: {A}; margin-bottom: 5px;">Pilotage · une pesée par jour à jeun, moyenne de la semaine, et le tour de taille le dimanche</div>
      {regles}
    </div>

    <div style="flex-grow: 1;"></div>

    <div style="background: {T}; padding: 13px 16px; display: flex; flex-direction: column; gap: 5px;">
      <div style="font-family: {MONO}; font-size: 10px; letter-spacing: 0.14em; text-transform: uppercase; color: {A};">Hors assiette</div>
      <div style="font-size: 14.5px; line-height: 1.45; color: {INK2};">Eau : 2,5 à 3 L par jour. Sommeil : 7 à 8 h — c'est la nuit que le muscle se construit. Et note tes séries : en surplus, une charge qui ne monte pas est un surplus qui part en gras.</div>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 16px; border-top: 1px solid {LINE}; padding-top: 9px; font-family: {MONO}; font-size: 11px; color: {MUTED}; letter-spacing: 0.02em;">
      <span>Tous les poids sont CRUS, avant cuisson · Whey 30 g à 10 h + 30 g l'après-midi, dans 250 ml de lait demi-écrémé</span>
      <span style="font-variant-numeric: tabular-nums;">8 / 8</span>
    </div>
  </div>
</div>
</x-dc>
</body>
</html>
'''

with open(os.path.join(OUT, "Courses.dc.html"), "w", encoding="utf-8") as f:
    f.write(build_annexe())
print("ok Courses.dc.html")

boards.append({"file": "Courses.dc.html", "x": 3 * (W + GX), "y": 1 * (H + GY),
               "w": W, "h": H, "title": "Courses & repères", "print": "fixed"})
with open(os.path.join(OUT, "canvas.json"), "w", encoding="utf-8") as f:
    json.dump({"artboards": boards, "launch": {"view": "canvas"}}, f, ensure_ascii=False, indent=2)
print("ok canvas.json (8 planches)")
