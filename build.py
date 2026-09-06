# -*- coding: utf-8 -*-
"""Assemble l'appli : data.json est injecté dans app.template.html -> dist/index.html
Relancer après toute modification du plan (build_data.py) ou du template.
Produit aussi dist/version.json (numéro de build croissant) : l'appli Android compare ce numéro
à celui qu'elle a déjà pour se mettre à jour toute seule, et le service worker l'utilise comme nom de cache."""
import json, os, re, subprocess, sys, time
os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.run([sys.executable, "build_data.py"], check=True, capture_output=True)
data = open("data.json", encoding="utf-8").read()
tpl = open("app.template.html", encoding="utf-8").read()
assert "__DATA__" in tpl
build = int(time.strftime("%Y%m%d%H%M"))  # ex. 202609061030 : croît à chaque build
os.makedirs("dist", exist_ok=True)
open("dist/index.html", "w", encoding="utf-8", newline="\n").write(tpl.replace("__DATA__", data, 1))
for f in ("manifest.json", "icon-192.png", "icon-512.png"):
    if os.path.exists(f): open(os.path.join("dist", f), "wb").write(open(f, "rb").read())
sw = open("sw.js", encoding="utf-8").read().replace('"carnet-v1"', '"carnet-%d"' % build, 1)
open("dist/sw.js", "w", encoding="utf-8", newline="\n").write(sw)
def pages_url():
    """Adresse où dist/ est publié : variable CARNET_URL, sinon déduite du dépôt GitHub (GitHub Pages)."""
    u = os.environ.get("CARNET_URL")
    if u: return u if u.endswith("/") else u + "/"
    try:
        r = subprocess.run(["git", "remote", "get-url", "origin"], capture_output=True, text=True, check=True).stdout.strip()
        m = re.search(r"github\.com[:/]([^/]+)/([^/\s]+?)(?:\.git)?$", r)
        if m: return "https://%s.github.io/%s/" % (m.group(1).lower(), m.group(2))
    except Exception: pass
    return ""
url = pages_url()
json.dump({"build": build, "version": json.loads(data)["version"], "url": url}, open("dist/version.json", "w", encoding="utf-8"))
if not url: print("(pas d'adresse de publication : la mise à jour automatique du téléphone est inactive)")
print("dist/index.html :", os.path.getsize("dist/index.html") // 1024, "Ko — build", build)
