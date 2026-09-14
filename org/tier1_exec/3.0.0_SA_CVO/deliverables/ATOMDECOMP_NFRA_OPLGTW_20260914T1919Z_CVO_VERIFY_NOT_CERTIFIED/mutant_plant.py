"""Plant two mutants in SCRATCH copies of the committed rectangle and SEAL their coordinates.
Prints only the seal hash and the mutant file names, never the coordinates. Never writes the repo."""
import hashlib
import json
import os
import secrets
import shutil
import sys

ROOT = sys.argv[1]
SCR = sys.argv[2]
SRC = os.path.join(ROOT, "workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/rectangle.c1.json")
base = open(SRC, "rb").read()
print("committed c1 sha256:", hashlib.sha256(base).hexdigest(), "bytes:", len(base))
shutil.copyfile(SRC, os.path.join(SCR, "scratch.base.json"))

# Mutant S (semantic, coherence-violating): a plausible digit transposition in one footer record.
s_old, s_new = b'"rows": 105074', b'"rows": 150074'
assert base.count(s_old) == 1, base.count(s_old)
# Mutant M (mechanical): rename the 6th occurrence of one field key -> rectangularity break.
m_old, m_new = b'"unverified_boundary": {', b'"unverified_boundarY": {'
assert base.count(m_old) == 6, base.count(m_old)
idx = -1
for _ in range(6):
    idx = base.index(m_old, idx + 1)
mut_s = base.replace(s_old, s_new)
mut_m = base[:idx] + m_new + base[idx + len(m_old):]
open(os.path.join(SCR, "scratch.mutantA.json"), "wb").write(mut_s)
open(os.path.join(SCR, "scratch.mutantB.json"), "wb").write(mut_m)
seal = {
    "sealed_by": "3.0.0_SA_CVO (worker fork)",
    "nonce": secrets.token_hex(16),
    "mutantA": {"file": "scratch.mutantA.json", "class": "SEMANTIC coherence-violating",
                "cell": "S3-data.recorded_observation footer_objects[master=08335338,dataset=dim_position].rows",
                "old": s_old.decode(), "new": s_new.decode(),
                "expected": "validator 0 violations (blind by design); semantic lens MISMATCH at this cell"},
    "mutantB": {"file": "scratch.mutantB.json", "class": "MECHANICAL rectangularity",
                "cell": "S6-operations.unverified_boundary key renamed (6th occurrence, byte offset %d)" % idx,
                "old": m_old.decode(), "new": m_new.decode(),
                "expected": "validator RECTANGULARITY violation (MISSING + EXTRA) on S6-operations"},
}
blob = json.dumps(seal, indent=2, sort_keys=True).encode()
open(os.path.join(SCR, "SEAL.json"), "wb").write(blob)
print("SEAL sha256:", hashlib.sha256(blob).hexdigest(), "(coordinates withheld until detection output exists)")
for f in ("scratch.mutantA.json", "scratch.mutantB.json"):
    b = open(os.path.join(SCR, f), "rb").read()
    print(f, "sha256:", hashlib.sha256(b).hexdigest(), "differs-from-committed:", b != base)
