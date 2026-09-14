"""Open the seal, verify its hash, restore both scratch mutants by reverse replacement. Never writes the repo."""
import hashlib
import json
import os
import sys

SCR = sys.argv[1]
expected_hash = sys.argv[2]
blob = open(os.path.join(SCR, "SEAL.json"), "rb").read()
h = hashlib.sha256(blob).hexdigest()
print("SEAL sha256 now:", h, "matches pre-detection print:", h == expected_hash)
seal = json.loads(blob)
print(json.dumps(seal, indent=2))
for key in ("mutantA", "mutantB"):
    m = seal[key]
    p = os.path.join(SCR, m["file"])
    b = open(p, "rb").read()
    new, old = m["new"].encode(), m["old"].encode()
    assert b.count(new) == 1, (key, b.count(new))
    restored = b.replace(new, old)
    out = os.path.join(SCR, m["file"].replace("mutant", "restored"))
    open(out, "wb").write(restored)
    print(key, "restored ->", os.path.basename(out))
