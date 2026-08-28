#!/usr/bin/env python3
"""Recompute a round's sealed-claim digest from EXACT bytes (COO~X 77360 / CVO~X condition on C4).

    python org/standards/isck/verify_seal.py [--round 3|4] [--commit <sha>]

Composition, byte-exact, the same for every round:
    sha256( utf8(register row <planted id> "claim") + b"|" + bytes(ROUND<N>_ANSWER_KEY.txt) )
where the key file is read RAW (no trailing newline; CRLF would change the digest -- the file is
LF-only and read in binary). --commit reads both inputs from that commit's object database
(git show), never the tree. --round defaults to 3 so every earlier citation of this script keeps
its meaning. Rounds and their expected seals (each printed in the charter that sealed it):
    3  row R3-CTO-2, ROUND3_ANSWER_KEY.txt, ROUND3_CHARTER.md sec 7
    4  row R4-CTO-1, ROUND4_ANSWER_KEY.txt, ROUND3_CHARTER.md sec 11 (OPENING)
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent
REL = "org/standards/isck"
ROUNDS = {
    "3": {"row": "R3-CTO-2", "key": "ROUND3_ANSWER_KEY.txt",
          "expected": "402da6e06c5d813b1350e9a1c4a01fd860945e11b8dfa84fb0cf065217f839af"},
    "4": {"row": "R4-CTO-1", "key": "ROUND4_ANSWER_KEY.txt",
          "expected": "e092b98a74019218325ec8cc97c74bb9a59ac3ccdc4cb548e1febe4a3144d3d1"},
}


def read(path, commit):
    if commit:
        return subprocess.check_output(["git", "-C", str(ROOT), "show", f"{commit}:{REL}/{path}"])
    return (HERE / path).read_bytes()


def main():
    commit = sys.argv[sys.argv.index("--commit") + 1] if "--commit" in sys.argv else None
    rnd = sys.argv[sys.argv.index("--round") + 1] if "--round" in sys.argv else "3"
    if rnd not in ROUNDS:
        sys.exit(f"REFUSED: --round must be one of {sorted(ROUNDS)}")
    spec = ROUNDS[rnd]
    reg = json.loads(read("ROUND3_FINDING_REGISTER.json", commit).decode("utf-8"))
    claim = next(r["claim"] for r in reg["findings"] if r["finding_id"] == spec["row"])
    key = read(spec["key"], commit)
    seal = hashlib.sha256(claim.encode("utf-8") + b"|" + key).hexdigest()
    print(f"round         = {rnd} (row {spec['row']}, {spec['key']})")
    print(f"sha256(key)   = {hashlib.sha256(key).hexdigest()}")
    print(f"seal          = {seal}")
    print(f"expected      = {spec['expected']}")
    print("MATCH" if seal == spec["expected"] else "MISMATCH")
    sys.exit(0 if seal == spec["expected"] else 1)


if __name__ == "__main__":
    main()
