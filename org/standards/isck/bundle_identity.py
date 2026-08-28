#!/usr/bin/env python3
"""Generate BUNDLE_IDENTITY.json for the ISCK contract bundle at a cited commit.

Round-3 target 5 (GPT memo Appendix C): the contract identifies ITSELF with the rigour it demands of
other immutable versions. Every field here is DERIVED from git at the cited commit -- no digest is
typed. A human label such as "v0.2-candidate" resolves to exactly one bundle id; a later amendment
gets a new candidate id even when the doctrine is behaviourally unchanged.

    python org/standards/isck/bundle_identity.py <commit> [--write]   # print (or write) the record
    python org/standards/isck/bundle_identity.py <commit> --check     # exit 1 if the written record
                                                                      # does not match the derivation

Bundle id = sha256 over the sorted (path, blob) pairs of the bundle's member files at the commit
(content-addressed: a bundle at a commit is IMMUTABLE, so LAW 1's hashes-for-immutables rule
applies -- no minted serial). Digests of file CONTENT are taken from `git cat-file blob` (LF as
stored), never from the working tree (CRLF trap).
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent.parent  # org/standards/isck -> workspace root
REL = "org/standards/isck"
OUT = HERE / "BUNDLE_IDENTITY.json"

DOCTRINE = f"{REL}/ISCK_CONTRACT.md"
SCHEMA = f"{REL}/ISCK_CONTRACT.v0.schema.json"
VALIDATOR = f"{REL}/validate_isck.py"
GATES = [f"{REL}/run_gates.sh", f"{REL}/check_rule_ablation.py", f"{REL}/check_enum_collisions.py",
         f"{REL}/check_mutant_isolation.py", f"{REL}/check_postulate_labels.py",
         f"{REL}/isck_coverage_probes.py", f"{REL}/ARM4_ADJUDICATION.json"]
VOCAB = [f"{REL}/vocab/entity_classes.json", f"{REL}/vocab/identity_spaces.json",
         f"{REL}/vocab/identity_policies.json"]
BOUNDARIES = {"round_1_boundary_commit": "21d6fc7325", "round_2_boundary_commit": "ece1ac0f41",
              "round_3_boundary_commit": None}


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True).strip()


def blob(commit, path):
    return git("rev-parse", f"{commit}:{path}")


def sha256_at(commit, path):
    data = subprocess.check_output(["git", "-C", str(ROOT), "cat-file", "blob", f"{commit}:{path}"])
    return hashlib.sha256(data).hexdigest()


def derive(commit):
    full = git("rev-parse", f"{commit}^{{commit}}")
    members = [DOCTRINE, SCHEMA, VALIDATOR, *GATES, *VOCAB]
    pairs = sorted((p, blob(full, p)) for p in members)
    bundle_id = "bundle:sha256:" + hashlib.sha256("\n".join(f"{p} {b}" for p, b in pairs).encode()).hexdigest()
    schema_text = subprocess.check_output(["git", "-C", str(ROOT), "cat-file", "blob", f"{full}:{SCHEMA}"])
    schema_id = json.loads(schema_text).get("$id")
    post_boundary = git("rev-list", "--reverse", f"{BOUNDARIES['round_2_boundary_commit']}..{full}", "--", REL).split()
    return {
        "contract_bundle_id": bundle_id,
        "semantic_version": "v0.2-candidate",
        "schema_$id": schema_id,
        "status": "candidate",
        "derived_at_commit": full,
        "doctrine_commit": full, "doctrine_blob_sha": blob(full, DOCTRINE),
        "schema_commit": full, "schema_blob_sha": blob(full, SCHEMA), "schema_sha256": sha256_at(full, SCHEMA),
        "validator_commit": full, "validator_blob_sha": blob(full, VALIDATOR),
        "gate_suite_commit": full, "gate_suite_blobs": {p: blob(full, p) for p in GATES},
        "vocabulary_digests": {p: sha256_at(full, p) for p in VOCAB},
        **BOUNDARIES,
        "post_boundary_amendments": post_boundary,
        "clean_clone_gate_receipt": None,
        "wp3_certification_receipt": None,
        "vertical_slice_receipt": None,
        "frozen_at": None,
        "supersedes_bundle_id": None,
        "$comment": "status moves candidate -> frozen only when the three receipts are non-null and round 3 is closed; every field is derived by bundle_identity.py -- re-run it, never edit it",
    }


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    commit = sys.argv[1]
    rec = derive(commit)
    if "--check" in sys.argv:
        cur = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
        same = {k: v for k, v in cur.items() if k != "$comment"} == {k: v for k, v in rec.items() if k != "$comment"}
        print(("OK" if same else "STALE") + f": {OUT.name} vs derivation at {rec['derived_at_commit'][:10]}")
        sys.exit(0 if same else 1)
    text = json.dumps(rec, indent=2) + "\n"
    if "--write" in sys.argv:
        OUT.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {OUT.name}: {rec['contract_bundle_id']} @ {rec['derived_at_commit'][:10]}")
    else:
        print(text)


if __name__ == "__main__":
    main()
