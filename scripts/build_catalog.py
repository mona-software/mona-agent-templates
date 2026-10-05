#!/usr/bin/env python3
"""Sinh catalog.json + templates/<slug>.json (bundle cho monacloud-mcp agent_templates_get qua URL) từ thư mục templates/."""
import json, os, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
TPL = ROOT / "templates"
STD = ["README.md", "AGENTS.md", "SOUL.md", "IDENTITY.md", "tools.json", "deploy.md", "CHECKLIST.md"]
cat = []
for d in sorted(p for p in TPL.iterdir() if p.is_dir()):
    readme = (d / "README.md").read_text(encoding="utf-8") if (d / "README.md").exists() else ""
    lines = [l.strip() for l in readme.splitlines()]
    name = next((l[2:].strip() for l in lines if l.startswith("# ")), d.name)
    ident = (d / "IDENTITY.md").read_text(encoding="utf-8") if (d / "IDENTITY.md").exists() else ""
    desc = next((l.split(":", 1)[1].strip() for l in ident.splitlines() if l.startswith("- vibe:")), "") or next((l for l in lines if l and not l.startswith("#")), "")
    name = next((l.split(":", 1)[1].strip() for l in ident.splitlines() if l.startswith("- name:")), name)
    tools = json.loads((d / "tools.json").read_text(encoding="utf-8")) if (d / "tools.json").exists() else {}
    files = {}
    for f in STD:
        p = d / f
        if p.exists(): files[f] = p.read_text(encoding="utf-8")
    for p in sorted((d / "skills").rglob("SKILL.md")) if (d / "skills").exists() else []:
        files[str(p.relative_to(d))] = p.read_text(encoding="utf-8")
    for p in sorted((d / "sample-data").rglob("*")) if (d / "sample-data").exists() else []:
        if p.is_file(): files[str(p.relative_to(d))] = p.read_text(encoding="utf-8")
    entry = {"slug": d.name, "name": name.split(":")[0].strip(), "description": desc[:300], "products": tools.get("products", []),
             "tags": [t.lower() for t in tools.get("products", [])], "url": f"https://monagent.vn/mau/{d.name}",
             "source": f"https://github.com/mona-software/mona-agent-templates/tree/main/templates/{d.name}"}
    cat.append(entry)
    (TPL / f"{d.name}.json").write_text(json.dumps({**entry, "files": files}, ensure_ascii=False, indent=1), encoding="utf-8")
(ROOT / "catalog.json").write_text(json.dumps({"updated": "2026-09-19", "entity": "MONA Agent thuộc nhóm MONA Cloud (The MONA Group)", "templates": cat}, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"catalog: {len(cat)} template")
