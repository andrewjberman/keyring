# NFRA_CTLPLN round 26 (XB-20261016T042748Z-779c): import tabulate ONLY from SCRATCH_TARGET and render one read-only table
# of the tabulate pack's .json receipts. Reads local files only; writes nothing but stdout.
import json
import os
import sys

import tabulate

print("tabulate.__file__ =", tabulate.__file__)
print("tabulate.__version__ =", tabulate.__version__)
print("sys.path[0:3] =", sys.path[0:3])
receipts = r"C:\dev\_intake_tabulate_20261016\PACK2\receipts"
rows = []
for name in sorted(os.listdir(receipts)):
    if not name.endswith(".json"):
        continue
    with open(os.path.join(receipts, name), encoding="utf-8") as f:
        doc = json.load(f)
    kind = "install" if ".install." in name else "prove"
    rc = (doc.get("install") or {}).get("rc", "")  # run 2: rc lives under install{} (run 1 read the top level and printed blanks)
    sha = str(doc.get("received_sha256", ""))[:12]
    rows.append([name, kind, rc, sha])
print(tabulate.tabulate(rows, headers=["file", "kind", "rc", "received_sha256[:12]"]))
