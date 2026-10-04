#!/usr/bin/env python3
"""Build or verify the deslop.skill bundle from its source files.

    python3 scripts/build_bundle.py          rebuild deslop.skill and SHA256SUMS
    python3 scripts/build_bundle.py --check  verify both match the sources (used by CI)

The zip is deterministic (stored entries, fixed timestamps and modes), so the
same sources always produce the same bytes and the same SHA-256 on any machine.
--check also fails on hidden text in the bundled files: zero-width, bidi and
Unicode tag characters, and HTML comments, which can carry instructions a
reviewer never sees.
"""
import hashlib
import io
import re
import sys
import zipfile
from pathlib import Path

NAME = "deslop"
FILES = ["SKILL.md", "references/kill-lists.md"]
ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / f"{NAME}.skill"
SUMS = ROOT / "SHA256SUMS"
EPOCH = (1980, 1, 1, 0, 0, 0)
HIDDEN = re.compile("[​-‏‪-‮⁠-⁤﻿\U000e0000-\U000e007f]|<!--")


def build() -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_STORED) as z:
        for rel in FILES:
            info = zipfile.ZipInfo(f"{NAME}/{rel}", date_time=EPOCH)
            info.external_attr = 0o644 << 16
            z.writestr(info, (ROOT / rel).read_bytes())
    return buf.getvalue()


def hidden_text() -> list[str]:
    hits = []
    for rel in FILES:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            if HIDDEN.search(line):
                hits.append(f"{rel}:{lineno}")
    return hits


def main() -> int:
    data = build()
    line = f"{hashlib.sha256(data).hexdigest()}  {BUNDLE.name}\n"
    if "--check" not in sys.argv:
        BUNDLE.write_bytes(data)
        SUMS.write_text(line)
        print(line.strip())
        return 0
    problems = [f"hidden text at {h}" for h in hidden_text()]
    if not BUNDLE.exists() or BUNDLE.read_bytes() != data:
        problems.append(f"{BUNDLE.name} does not match the sources: run python3 scripts/build_bundle.py")
    if not SUMS.exists() or SUMS.read_text() != line:
        problems.append("SHA256SUMS does not match the bundle: run python3 scripts/build_bundle.py")
    for p in problems:
        print(f"FAIL {p}")
    if not problems:
        print(f"OK {line.strip()}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
