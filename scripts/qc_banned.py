#!/usr/bin/env python3
"""Quét luật chữ MONA trên mọi .md trong kho: banned-ai-tells + 'ạ' cuối câu + 'Vâng' + mở câu 'Dạ' + em-dash + 'bạn' (ngôi). Exit 1 nếu FAIL."""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
BAN = pathlib.Path.home() / ".claude/skills/mon-taste-qc/catalog/banned-ai-tells.md"
subs, regs = [], []
if BAN.exists():
    for l in BAN.read_text(encoding="utf-8").splitlines():
        l = l.strip()
        if not l.startswith("- ") or l.startswith("- re:") and False: continue
        if l.startswith("- re:"): regs.append(re.compile(l[5:].strip(), re.I))
        elif l.startswith("- "): subs.append(l[2:].strip().lower())
extra = [re.compile(r"[^\w]ạ[.!?,\n]"), re.compile(r"\bVâng\b"), re.compile(r"(^|[.!?]\s+)Dạ\b", re.M), re.compile(r"—")]
fail = 0
for p in sorted(ROOT.rglob("*.md")):
    if "node_modules" in p.parts or ".git" in p.parts or "sample-data" in p.parts: continue
    t = p.read_text(encoding="utf-8"); tl = t.lower(); hits = []
    for s in subs:
        if s and s in tl: hits.append(s)
    for r in regs + extra:
        m = r.search(t)
        if m: hits.append(m.group(0).strip()[:30])
    if p.name in ("README.md", "HUONG-DAN.md") and re.search(r"\bbạn\b", tl): hits.append("bạn (ngôi)")
    if "không đi qua luồng ngoài" in tl and "noi-bo-kin" not in p.parts: hits.append("hứa lố: không đi qua luồng ngoài")
    if "cổng thanh toán mona pay" in tl or "mona pay là cổng thanh toán" in tl: hits.append("entity MONA Pay sai")
    if "thẻ quốc tế" in tl: hits.append("point thẻ quốc tế")
    if hits:
        fail += 1; print(f"FAIL {p.relative_to(ROOT)}: {', '.join(sorted(set(hits))[:8])}")
print(f"{'FAIL' if fail else 'PASS'}: {fail} file lỗi")
sys.exit(1 if fail else 0)
