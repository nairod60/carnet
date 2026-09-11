# -*- coding: utf-8 -*-
"""Génère CONTEXTE.md : profil, décisions, repas et entraînements en clair pour Claude Code.
Les repas et séances sont lus dans plan/gen.py et plan/prog.py (jamais recopiés à la main).
Relancer après toute modification du plan :  python gen_contexte.py"""
import importlib.util, io, os, re, contextlib

HERE = os.path.dirname(os.path.abspath(__file__))

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):  # gen.py écrit ses planches A4 au chargement
        spec.loader.exec_module(m)
    return m

g = load("gen", os.path.join(HERE, "plan", "gen.py"))
p = load("prog", os.path.join(HERE, "plan", "prog.py"))

L = []
w = L.append
w("# Contexte — Dorian et son Carnet")
w("")
w("Ce fichier donne à Claude Code ce que le code ne dit pas : qui est l'utilisateur, ce qui a été décidé et pourquoi.")
w("Les tableaux de repas et de séances sont générés depuis `plan/gen.py` et `plan/prog.py` par `gen_contexte.py` ;")
w("si le plan change, relancer ce script plutôt que d'éditer les tableaux à la main.")
w("")
w("## Profil")
w("")
w("- Dorian, 40 ans, 1,84 m, 70 kg (pesée de début septembre 2026). Charpente fine (« ectomorphe ») : jusqu'à 40 ans il ne")
w("  grossissait pas quoi qu'il mange ; depuis peu, un peu de gras au ventre. Le suivi du tour de taille (dimanche) sert à ça.")
w("- Matériel : haltères, banc inclinable, barre de traction. Séances chez lui, environ une heure.")
w("- **Une épaule douloureuse** : c'est la contrainte numéro un du programme. Pectoraux une seule fois par semaine, prises neutres,")
w("  pas de développé militaire, pas d'écartés, pas de pull-over, pas de prise large aux tractions ; échauffement de la coiffe")
w("  avant chaque séance haut du corps ; jamais à l'échec sur les poussées. Échelle de douleur ci-dessous.")
w("- Prend du Dafalgan codéiné à l'occasion (maux de tête) : sans effet sur le muscle, pas d'interaction avec la créatine.")
w("- Préférences : les salades de riz au thon plutôt qu'au poulet ; pas de sardines, pas de courgettes ; le steak haché seulement")
w("  le soir ; trouve les assiettes volumineuses, d'où les calories du surplus mises dans le shake plutôt que dans l'assiette.")
w("")
w("## Objectif et décisions")
w("")
w("- **Prise de masse propre d'abord, sèche ensuite** (sèche envisagée vers février). Cible : **+200 à +350 g par semaine**")
w("  sur la moyenne hebdomadaire des pesées du matin. Le verdict de l'appli (onglet Suivi) applique les règles de pilotage ci-dessous.")
w("- Énergie : Mifflin-St Jeor à 70 kg × 1,35 (sédentaire) + 300 kcal les jours d'entraînement ; le plan vise environ")
w("  +250 kcal par jour au-dessus de la dépense. Moyenne du plan : voir les totaux par jour ci-dessous.")
w("- Protéines ~2,7 g/kg (marge volontaire : un steak un peu léger ou un repas raté ne change rien). Lipides ~80 g/jour, choisis")
w("  et dosés (jaunes d'œufs, huile d'olive pesée, amandes, poisson) — on achète maigre et on ajoute le gras soi-même.")
w("- Glucides autour des séances, sans sucre ajouté (avoine, riz, pâtes, pommes de terre, pain complet, fruits).")
w("- **Créatine monohydrate 5 g par jour, repos compris**, dans le shake de 10 h. Pas de phase de charge. Pendant les 14 premiers")
w("  jours la balance monte d'eau (+1 à 2 kg) : l'appli met le verdict en pause et exclut ces pesées du comparatif.")
w("- Whey : Isostar, 30 g par prise, dans 250 ml de lait demi-écrémé.")
w("- Poids toujours donnés **crus** (avant cuisson). Table cru → cuit dans l'appli (onglet Repas).")
w("- Substitutions admises sans changer le plan : légumes interchangeables à poids égal (haricots verts, concombre, tomate,")
w("  poivron, courgette) ; steak plus léger que prévu → un œuf en plus ; une cuillère à café (10-15 g) de crème de marrons dans")
w("  le fromage blanc du soir, pas plus. Ce qui est fixe : les protéines, les féculents pesés et l'huile.")
w("- Sommeil 7-8 h et 20-30 min de marche par jour sont considérés comme faisant partie du programme (pas de 5e séance).")
w("- Semaine allégée toutes les 6 à 8 semaines (2 séries au lieu de 3, charges à 70 %).")
w("")
w("## Règles de pilotage (verdict hebdomadaire)")
w("")
for cond, texte, alerte in g.PILOTAGE:
    w(f"- **{cond}** — {texte}" + (" *(alerte)*" if alerte else ""))
w("")
w("## Repas de la semaine (poids crus)")
w("")
for d in g.DAYS:
    w(f"### {d['nom']} — {'entraînement' if d['train'] else 'repos'} · {d['kcal']} kcal · {d['p']} g P · {d['g']} g G · {d['l']} g L")
    w("")
    w("| Repas | Aliments | kcal |")
    w("|---|---|---|")
    for nom, plat, kcal, items in d["meals"]:
        parts = []
        for it in items:
            a, q, c = it[0], it[1], it[2] if len(it) > 2 else ""
            s = a + (f" {q}" if q else "") + (f" ({c})" if c else "")
            parts.append(s)
        titre = nom + (f" — {plat}" if plat else "")
        w(f"| {titre} | {', '.join(parts)} | {kcal} |")
    w("")
    if d.get("batch"):
        w(f"*Organisation : {d['batch']}*")
        w("")
w("## Liste de courses (une semaine, dérivée des repas)")
w("")
for rayon, items in g.construire_courses(g.DAYS):
    w(f"- **{rayon}** : " + ", ".join(f"{a} {q}" for a, q in items))
w("")
w("## Cru → cuit")
w("")
w("| Aliment | Cru | Cuit | Facteur |")
w("|---|---|---|---|")
for a, cru, cuit, f in g.CONVERT:
    w(f"| {a} | {cru} | {cuit} | {f} |")
w("")
w("## Entraînement : 4 séances par semaine")
w("")
w("Lundi J1, mardi J2, jeudi J3, vendredi J4. Mercredi et week-end : repos (marche bienvenue). Haltères + banc + barre de traction.")
w("")
for s in p.SEANCES:
    tot = sum(int(re.match(r"(\d+)", e[2]).group(1)) for e in s["exos"])
    w(f"### {s['id']} · {s['jour']} — {s['titre']} ({tot} séries)")
    w("")
    w(f"*{s['focus']}*")
    w("")
    w("| Muscle | Exercice | Séries × reps | Repos | Consigne |")
    w("|---|---|---|---|---|")
    for muscle, nom, series, reps, repos, consigne in s["exos"]:
        w(f"| {muscle} | {nom} | {series} × {reps} | {repos} | {consigne} |")
    w("")
w("### Échauffement de l'épaule (avant J1 et J3)")
w("")
for nom, dose, note in p.ECHAUFFEMENT:
    w(f"- **{nom}** ({dose}) — {note}")
w("")
w("### Règles de progression")
w("")
for titre, texte in p.PROGRESSION:
    w(f"- **{titre}** — {texte}")
w("")
w("### Échelle de douleur (épaule)")
w("")
for situation, consulter, texte in p.DOULEUR:
    w(f"- **{situation}** — {texte}" + (" *(consulter)*" if consulter else ""))
w("")
w("## Historique des décisions")
w("")
w("- Août 2026 : premier plan « sécher et prendre du muscle » à 75 kg supposés, 5 séances.")
w("- Début septembre : la balance dit 70 kg → tout recalibré ; épaule douloureuse → 4 séances, pectoraux une fois par semaine ;")
w("  déficit remplacé par une **prise de masse propre** (+250 kcal) avec un shake à 10 h, parce que les assiettes paraissaient grosses.")
w("- 7 septembre : appli Carnet (PWA puis APK Android), design « Papier », créatine suivie dans l'appli, mise à jour automatique.")
w("- 11 septembre : `plan/prog.py` corrigé (la règle « En déficit » devient « En prise de masse »). Ce fichier créé.")
w("")
w("## Comment travailler avec Dorian")
w("")
w("- Il écrit souvent en dictée vocale (fautes et mots approximatifs) : comprendre l'intention, ne pas relever.")
w("- Réponses courtes et concrètes, en français, avec les chiffres qui comptent (kcal, grammes, séries). Pas de listes à rallonge.")
w("- Ne jamais inventer une valeur nutritionnelle : les kcal viennent de `plan/recalc.py` (tables CIQUAL/USDA) qui réécrit `plan/gen.py`.")
w("- Toute modification du plan passe par `plan/gen.py` / `plan/prog.py`, puis `.\\publish.ps1` — et relancer `gen_contexte.py`.")

out = os.path.join(HERE, "CONTEXTE.md")
io.open(out, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print(f"CONTEXTE.md : {len(L)} lignes, {os.path.getsize(out)//1024} Ko")
