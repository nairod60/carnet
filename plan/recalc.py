# -*- coding: utf-8 -*-
"""Recalcule les kcal par repas et les totaux du jour à partir des vraies tables,
puis réécrit gen.py. Évite toute valeur saisie à la main."""
import re, importlib.util

F = {"oeuf":(143,12.6,0.7,9.5),"pain_complet":(247,9.0,41.0,3.4),"banane":(89,1.1,20.0,0.3),
 "pomme":(52,0.3,12.0,0.2),"kiwi":(61,1.1,12.0,0.5),"orange":(47,0.9,9.0,0.1),"fruit":(60,0.8,13.0,0.2),
 "poulet_cru":(110,23.0,0.0,1.8),"steak5_cru":(137,21.0,0.0,5.0),"maquereau_cru":(205,19.0,0.0,13.9),
 "cabillaud_cru":(82,18.0,0.0,0.7),"thon_naturel":(116,26.0,0.0,1.0),"riz_cru":(350,7.5,78.0,0.9),
 "pates_comp_cru":(350,13.0,65.0,2.5),"pdt_crue":(77,2.0,17.0,0.1),"haricots_verts":(31,1.8,4.0,0.2),
 "courgette":(17,1.2,3.1,0.3),"poivron":(26,1.0,4.6,0.3),"tomate":(18,0.9,3.9,0.2),
 "huile_olive":(900,0,0,100),"fromage_blanc0":(47,8.0,4.0,0.2),"amandes":(579,21.2,9.0,49.9),
 "whey":(385,72.0,7.0,6.6), "lait_ecreme":(33,3.3,4.9,0.1), "zero":(0,0,0,0),
 "concombre":(12,0.65,1.8,0.1), "olives":(145,1.0,1.0,14.0), "saumon_boite":(140,21.0,0.0,6.0),
 "lait_demi":(46,3.2,4.8,1.5), "avoine":(375,13.5,60.0,7.0)}

MAP = {"Œufs entiers":"oeuf","Pain complet":"pain_complet","Banane":"banane","Pomme":"pomme",
 "Kiwis":"kiwi","Orange":"orange","Fruit au choix":"fruit","Café ou thé sans sucre":"zero",
 "Blanc de poulet":"poulet_cru","Steak haché 5 %":"steak5_cru","Maquereau ou sardines":"maquereau_cru",
 "Cabillaud ou colin":"cabillaud_cru","Thon au naturel égoutté":"thon_naturel","Riz basmati":"riz_cru",
 "Pâtes complètes":"pates_comp_cru","Pommes de terre":"pdt_crue","Haricots verts":"haricots_verts",
 "Courgettes":"courgette","Poivrons":"poivron","Tomates":"tomate","Huile d'olive":"huile_olive",
 "Fromage blanc 0 %":"fromage_blanc0","Amandes":"amandes","Whey Isostar":"whey","Lait écrémé":"lait_ecreme",
 "Ail, paprika, cumin":"zero","Citron, persil":"zero","Concombre":"concombre","Olives":"olives",
 "Saumon en boîte égoutté":"saumon_boite","Œuf dur":"oeuf","Moutarde, vinaigre":"zero",
 "Vinaigre, herbes":"zero","Vinaigre, moutarde":"zero","Citron, aneth":"zero",
 "Lait demi-écrémé":"lait_demi","Flocons d'avoine":"avoine"}
SPLIT = {"Tomates et courgettes": [("tomate",0.5),("courgette",0.5)]}

def grams(poids, note):
    for t in (poids, note):
        m = re.search(r"(\d+)\s*(g|ml)", t or "")
        if m: return float(m.group(1))
    return 0.0

def macros(items):
    v = [0.0]*4
    for lab, poids, note in items:
        g = grams(poids, note)
        parts = SPLIT.get(lab) or [(MAP[lab], 1.0)]
        for key, frac in parts:
            for i in range(4): v[i] += F[key][i]*g*frac/100
    return v

spec = importlib.util.spec_from_file_location("gen", "gen.py")
gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen)

src = open("gen.py", encoding="utf-8").read()
print(f"{'Jour':10} {'kcal':>6} {'P':>5} {'G':>5} {'L':>5}")
tot = [0.0]*4
for d in gen.DAYS:
    jour = [0.0]*4
    for nom, dish, kcal_old, items in d["meals"]:
        v = macros(items)
        for i in range(4): jour[i] += v[i]
        k = str(int(round(v[0]/5)*5))
        pat = f'("{nom}","{dish}","{kcal_old}"'
        assert pat in src, pat
        src = src.replace(pat, f'("{nom}","{dish}","{k}"', 1)
    for i in range(4): tot[i] += jour[i]
    print(f"{d['nom']:10} {jour[0]:6.0f} {jour[1]:5.0f} {jour[2]:5.0f} {jour[3]:5.0f}")
    esp = f'kcal="{d["kcal"]}", p="{d["p"]}", g="{d["g"]}", l="{d["l"]}"'
    new = f'kcal="{jour[0]:.0f}", p="{jour[1]:.0f}", g="{jour[2]:.0f}", l="{jour[3]:.0f}"'
    assert esp in src, esp
    src = src.replace(esp, new, 1)

m = [t/7 for t in tot]
print(f"{'MOYENNE':10} {m[0]:6.0f} {m[1]:5.0f} {m[2]:5.0f} {m[3]:5.0f}   "
      f"({m[1]/70:.2f} g/kg prot, {m[3]/70:.2f} g/kg lip)")
open("gen.py","w",encoding="utf-8").write(src)
print("\ngen.py : kcal par repas et totaux du jour recalculés")

E = [d for d in gen.DAYS if d["train"]]; R = [d for d in gen.DAYS if not d["train"]]
mE = sum(sum(macros(i)[0] for _,_,_,i in d["meals"]) for d in E)/len(E)
mR = sum(sum(macros(i)[0] for _,_,_,i in d["meals"]) for d in R)/len(R)
print(f"\n{len(E)} jours de séance à {mE:.0f} kcal | {len(R)} jours de repos à {mR:.0f} kcal")
for age in (25,32,40):
    mb = 10*70 + 6.25*184 - 5*age + 5
    sem = len(E)*(mE-(mb*1.35+300)) + len(R)*(mR-mb*1.35)
    print(f"  {age} ans : {sem/7:+.0f} kcal/jour -> {sem/7700*1000:+.0f} g/semaine sur la balance (cible +200 à +350)")
