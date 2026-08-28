#!/usr/bin/env python3
"""Recompute the round-3 seal from EXACT bytes (COO~X 77360 / CVO~X condition on C4).

    python org/standards/isck/verify_seal.py [--commit <sha>]

Composition, byte-exact: sha256( utf8(register row R3-CTO-2 "claim") + b"|" + utf8(ROUND3_ANSWER_KEY.txt) )
where the key file is read raw (no trailing newline; CRLF would change the digest -- the file is LF-only and
read in binary). --commit reads both inputs from that commit's object database (git show), never the tree.
Expected seal: 402da6e06c5d813b1350e9a1c4a01fd860945e11b8dfa84fb0cf065217f839af (ROUND3_CHARTER.md sec 7).
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
REL = "org/standards/isck"
EXPECTED = "402da6e06c5d813b1350e9a1c4a01fd860945e11b8dfa84fb0cf065217f839af"


def read(path, commit):
    if commit:
        return subprocess.check_output(["git", "-C", str(ROOT), "show", f"{commit}:{REL}/{path}"])
    return (HERE / path).read_bytes()


def main():
    commit = sys.argv[sys.argv.index("--commit") + 1] if "--commit" in sys.argv else None
    reg = json.loads(read("ROUND3_FINDING_REGISTER.json", commit).decode("utf-8"))
    claim = next(r["claim"] for r in reg["findings"] if r["finding_id"] == "R3-CTO-2")
    key = read("ROUND3_ANSWER_KEY.txt", commit)
    seal = hashlib.sha256(claim.encode("utf-8") + b"|" + key).hexdigest()
    print(f"sha256(key)   = {hashlib.sha256(key).hexdigest()}")
    print(f"seal          = {seal}")
    print(f"expected      = {EXPECTED}")
    print("MATCH" if seal == EXPECTED else "MISMATCH")
    sys.exit(0 if seal == EXPECTED else 1)


if __name__ == "__main__":
    main()
