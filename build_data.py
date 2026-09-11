# -*- coding: utf-8 -*-
"""Extrait les données du plan (prog.py + gen.py) en un seul JSON pour l'appli.
Une seule source de vérité : modifier le plan = relancer ce script."""
import sys, json, importlib.util, re
sys.path.insert(0, "plan")

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m); return m

prog = load("plan/prog.py", "prog")
gen  = load("plan/gen.py", "gen")
# recalc.py réécrit gen.py quand on l'importe : on n'exécute que ses tables et sa fonction macros()
_src = open("plan/recalc.py", encoding="utf-8").read()
_ns = {}; exec(_src.split("spec = importlib")[0], _ns)
class _R: pass
rec = _R(); rec.macros = _ns["macros"]

JOURS = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]

# --- séances : jour de la semaine -> séance ---
seances = []
for s in prog.SEANCES:
    seances.append({
        "id": s["id"], "jour": s["jour"], "jourIdx": JOURS.index(s["jour"]),
        "titre": s["titre"], "focus": s["focus"],
        "exos": [{"groupe": g, "nom": n, "series": int(ser), "reps": reps, "repos": repos, "consigne": cue,
                  "poidsCorps": any(k in n.lower() for k in ("pompes", "tractions", "gainage", "relevé", "crunch"))}
                 for g, n, ser, reps, repos, cue in s["exos"]],
    })

# --- repas ---
jours = []
for d in gen.DAYS:
    meals = []; jour = [0.0] * 4
    for nom, dish, kcal, items in d["meals"]:
        v = rec.macros(items)
        for i in range(4): jour[i] += v[i]
        meals.append({"nom": nom, "plat": dish, "kcal": int(round(v[0] / 5) * 5), "prot": round(v[1]),  # mêmes arrondis que recalc.py
                      "items": [{"lab": l, "poids": p, "note": n} for l, p, n in items]})
    tot = [round(jour[0]), round(jour[1])]  # total exact du jour, comme gen.py / CONTEXTE.md
    jours.append({"nom": d["nom"], "idx": JOURS.index(d["nom"]), "train": d["train"],
                  "kcal": tot[0], "prot": tot[1], "repas": meals, "batch": d["batch"]})

# --- courses ---
courses = [{"rayon": r, "items": [{"nom": n, "qte": q} for n, q in items]} for r, items in gen.construire_courses(gen.DAYS)]

# --- pilotage + échauffement + douleur ---
data = {
    "version": "2026-09-14",
    "profil": {"poids": 70, "taille": 184, "objectif": "Prise de masse propre", "cible": "+200 à +350 g / semaine"},
    "seances": seances, "jours": jours, "courses": courses,
    "pilotage": [{"cond": c, "texte": t, "alerte": w} for c, t, w in gen.PILOTAGE],
    "echauffement": [{"nom": n, "dose": d, "note": c} for n, d, c in prog.ECHAUFFEMENT],
    "douleur": [{"situation": s_, "consulter": w, "texte": t} for s_, w, t in prog.DOULEUR],
    "conversion": [{"aliment": a, "cru": b, "cuit": c, "facteur": d} for a, b, c, d in gen.CONVERT],
}
json.dump(data, open("data.json", "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print(f"data.json : {len(seances)} séances, {len(jours)} jours, {sum(len(c['items']) for c in courses)} articles, "
      f"{sum(len(s['exos']) for s in seances)} exercices")
