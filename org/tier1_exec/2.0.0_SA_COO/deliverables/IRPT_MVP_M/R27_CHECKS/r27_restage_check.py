"""Round 27 (~M) check IBM27-272-AC1: the irpt-holdings Lambda's staged contract copy is current (row W84-S4).

The Lambda resolves infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json FIRST
(holdings/snapshot.py _contract_candidates). Requires: that copy is byte-equal to
docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json at this tree; STAGE_MANIFEST.json's member entry for
the docs path carries that file's current sha256; and the copy admits the CATEGORY node kind, assigned_strategy,
source_vendor_keys, security_aggregates and class_totals.

Run from the repo (or worktree) root. Prints STAGED-CURRENT or NOT-STAGED: <reason>.
"""
import hashlib
import json
import sys

DOCS = "docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json"
STAGED = "infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json"
MANIFEST = "infra/aws/lambda/investor-reporting/holdings/STAGE_MANIFEST.json"


def main():
    docs = open(DOCS, "rb").read()
    staged = open(STAGED, "rb").read()
    if docs != staged:
        print("NOT-STAGED: %s differs from %s" % (STAGED, DOCS))
        return 1
    sha = hashlib.sha256(docs).hexdigest()
    manifest = json.load(open(MANIFEST, encoding="utf-8"))
    text = json.dumps(manifest)
    if sha not in text:
        print("NOT-STAGED: %s does not carry the docs contract's sha256 %s" % (MANIFEST, sha[:12]))
        return 1
    schema = json.loads(staged.decode("utf-8"))
    props = schema.get("properties", {})
    node = props.get("nodes", {}).get("items", {}).get("properties", {})
    kinds = node.get("node_kind", {}).get("enum", [])
    missing = [n for n, ok in (("CATEGORY node_kind", "CATEGORY" in kinds),
                               ("source_vendor_keys", "source_vendor_keys" in props),
                               ("security_aggregates", "security_aggregates" in props),
                               ("class_totals", "class_totals" in props),
                               ("assigned_strategy", "assigned_strategy" in json.dumps(schema))) if not ok]
    if missing:
        print("NOT-STAGED: the staged copy lacks %s" % missing)
        return 1
    print("STAGED-CURRENT sha256=%s" % sha[:12])
    return 0


if __name__ == "__main__":
    sys.exit(main())
