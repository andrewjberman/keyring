#!/usr/bin/env python3
"""Generate BUNDLE_IDENTITY.json for the ISCK contract bundle at a cited commit.

Round-3 target 5 (GPT memo Appendix C): the contract identifies ITSELF with the rigour it demands of
other immutable versions. Every field here is DERIVED from git at the cited commit -- no digest is
typed. A human label such as "v0.2-candidate" resolves to exactly one bundle id; a later amendment
gets a new candidate id even when the doctrine is behaviourally unchanged.

    python org/standards/isck/bundle_identity.py <commit> [--write]   # print (or write) the record
    python org/standards/isck/bundle_identity.py <commit> --check     # exit 1 if the written record
                                                                      # does not match the derivation
    python org/standards/isck/bundle_identity.py <commit> --freeze --boundary <commit>
                                                    # SCHEMA-ONLY freeze of the label derived at <commit>
                                                    # (C4); recorded in BUNDLE_LABELS.json; immutable after
    python org/standards/isck/bundle_identity.py <commit> --receipt <kind> --value <v>
                                                    # append an OPERATIONAL receipt to the FROZEN label's
                                                    # registry entry (R3-CRO-28): idempotent on the same
                                                    # value, REFUSED on a conflicting one; bundle bytes and
                                                    # id untouched, so it is NOT a new candidate_id

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
         f"{REL}/isck_coverage_probes.py", f"{REL}/ARM4_ADJUDICATION.json",
         # R3-CRO-13: a sidecar that changes probe disposition is a bundle member, or the trust
         # decision moves without entering the hash
         f"{REL}/ARM1_ADJUDICATION.json"]
LABELS = HERE / "BUNDLE_LABELS.json"
VOCAB = [f"{REL}/vocab/entity_classes.json", f"{REL}/vocab/identity_spaces.json",
         f"{REL}/vocab/identity_policies.json"]
BOUNDARIES = {"round_1_boundary_commit": "21d6fc7325", "round_2_boundary_commit": "ece1ac0f41",
              "round_3_boundary_commit": None}
# R3-CRO-28: the operational receipts are REGISTRY facts on the frozen label (append-only, keyed by
# the immutable candidate_id + bundle id), never a member byte -- so recording one is not a new
# candidate. Each kind is set at most once; a second, different value is a conflict, not an update.
RECEIPT_KINDS = ("clean_clone_gate_receipt", "wp3_certification_receipt", "vertical_slice_receipt")


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True).strip()


def blob(commit, path):
    # a member ABSENT at the cited commit is part of the bundle's identity (R3-CRO-13: the member
    # set is fixed by this script, not by what happened to exist) -- never a crash, never skipped
    try:
        return git("rev-parse", "--verify", "-q", f"{commit}:{path}")
    except subprocess.CalledProcessError:
        return "ABSENT"


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
    # R3-CRO-12: the human label must resolve to exactly one bundle. The FAMILY label stays
    # semantic_version; the injective handle is candidate_id = family + the post-boundary amendment
    # count on the package path (monotone along the path, so two byte-distinct bundles never share
    # it), and BUNDLE_LABELS.json records every binding -- a rebinding is a failure, not an update.
    candidate_id = f"v0.2-candidate+{len(post_boundary)}"
    # C4 (CVO~X 20260828T040820Z): a FREEZE is a registry fact, so it is derived here like every
    # other field -- the label's registry entry carries frozen_at + round_3_boundary_commit; a frozen
    # label emits status=frozen and --check stays deterministic. The freeze is SCHEMA-ONLY: the three
    # operational receipts stay null BY DEFINITION until WP-3 / the live slice / replay land.
    labels = json.loads(LABELS.read_text(encoding="utf-8")) if LABELS.exists() else {}
    fz = labels.get(candidate_id, {}).get("frozen") or {}
    receipts = labels.get(candidate_id, {}).get("receipts") or {}
    return {
        "contract_bundle_id": bundle_id,
        "semantic_version": "v0.2-candidate",
        "candidate_id": candidate_id,
        "schema_$id": schema_id,
        "status": "frozen" if fz else "candidate",
        "freeze_scope": "schema-only (contract vocabulary + conditionals + battery); operational certification is a SEPARATE gate and its receipts are null" if fz else None,
        "frozen_at": fz.get("frozen_at"),
        "round_3_boundary_commit_frozen": fz.get("round_3_boundary_commit"),
        "derived_at_commit": full,
        "doctrine_commit": full, "doctrine_blob_sha": blob(full, DOCTRINE),
        "schema_commit": full, "schema_blob_sha": blob(full, SCHEMA), "schema_sha256": sha256_at(full, SCHEMA),
        "validator_commit": full, "validator_blob_sha": blob(full, VALIDATOR),
        "gate_suite_commit": full, "gate_suite_blobs": {p: blob(full, p) for p in GATES},
        "vocabulary_digests": {p: sha256_at(full, p) for p in VOCAB},
        **BOUNDARIES,
        "post_boundary_amendments": post_boundary,
        **{k: receipts.get(k) for k in RECEIPT_KINDS},
        "supersedes_bundle_id": None,
        "$comment": "every field is derived by bundle_identity.py -- re-run it, never edit it. status: candidate -> frozen is a SCHEMA-ONLY freeze (C4, CVO~X 20260828T040820Z) recorded in BUNDLE_LABELS.json by --freeze <commit> --boundary <commit>; it requires round 3 CLOSED and does NOT require the operational receipts, which stay null until WP-3 / the live slice / historical replay land (that is 'not operationally certified', not a contradiction). The operational receipts are appended to the frozen label's registry entry by --receipt <kind> --value <v> (R3-CRO-28): registry-side, never a member byte, so the bundle id and candidate_id do not move. A frozen label is immutable: any byte change on the package path derives a NEW candidate_id; --write under a frozen label with different bytes REFUSES",
    }


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    commit = sys.argv[1]
    if "--receipt" in sys.argv:
        rec = derive(commit)
        try:
            kind = sys.argv[sys.argv.index("--receipt") + 1]
            value = sys.argv[sys.argv.index("--value") + 1]
        except (ValueError, IndexError):
            sys.exit("REFUSED: --receipt <kind> needs --value <v>")
        if kind not in RECEIPT_KINDS:
            sys.exit(f"REFUSED: receipt kind {kind!r} is not one of {RECEIPT_KINDS}")
        # R3-CRO-31: a receipt slot is set ONCE, so an invalid first value poisons it permanently --
        # validate BEFORE any mutation. Every kind is commit-bearing (the run that produced the
        # receipt): the value must be a hex commit-ish that RESOLVES in this repository. An empty
        # or malformed value, or a commit that does not exist, is refused and nothing is written.
        import re
        if not re.fullmatch(r"[0-9a-f]{7,40}", value or ""):
            sys.exit(f"REFUSED: receipt value {value!r} is not a hex commit (7-40 chars); nothing written")
        try:
            value = git("rev-parse", "--verify", "-q", f"{value}^{{commit}}")
        except subprocess.CalledProcessError:
            sys.exit(f"REFUSED: receipt value {value!r} does not resolve to a commit in this repository; nothing written")
        labels = json.loads(LABELS.read_text(encoding="utf-8")) if LABELS.exists() else {}
        bound = labels.get(rec["candidate_id"])
        if not bound or bound["contract_bundle_id"] != rec["contract_bundle_id"]:
            sys.exit(f"REFUSED: {rec['candidate_id']} is not bound to {rec['contract_bundle_id']} in the registry")
        if not bound.get("frozen"):
            sys.exit(f"REFUSED: {rec['candidate_id']} is not frozen; a receipt certifies a FROZEN bundle")
        receipts = bound.setdefault("receipts", {})
        if kind in receipts and receipts[kind]["value"] != value:
            sys.exit(f"REFUSED: {kind} already recorded as {receipts[kind]['value']!r} at {receipts[kind]['recorded_at']}; "
                     f"a conflicting receipt is not an update -- a different certification is a different candidate")
        if kind not in receipts:
            import datetime
            receipts[kind] = {"value": value, "contract_bundle_id": rec["contract_bundle_id"],
                              "recorded_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
            LABELS.write_text(json.dumps(labels, indent=2) + "\n", encoding="utf-8", newline="\n")
        rec = derive(commit)
        OUT.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(f"RECEIPT {kind} = {value!r} on {rec['candidate_id']} ({rec['contract_bundle_id'][:24]}...); bundle id unchanged")
        return
    if "--freeze" in sys.argv:
        # freeze the label derived at <commit>, citing the round-3 boundary record commit; refuses
        # unless the label is bound in the registry to exactly this bundle (no freezing a stranger)
        rec = derive(commit)
        labels = json.loads(LABELS.read_text(encoding="utf-8")) if LABELS.exists() else {}
        bound = labels.get(rec["candidate_id"])
        if not bound or bound["contract_bundle_id"] != rec["contract_bundle_id"]:
            sys.exit(f"REFUSED: {rec['candidate_id']} is not bound to {rec['contract_bundle_id']} in the registry; --write it first")
        if bound.get("frozen"):
            sys.exit(f"REFUSED: {rec['candidate_id']} is already frozen at {bound['frozen']['frozen_at']}")
        try:
            boundary = sys.argv[sys.argv.index("--boundary") + 1]
        except (ValueError, IndexError):
            sys.exit("REFUSED: --freeze needs --boundary <commit of BOUNDARY_ROUND3.md>")
        git("rev-parse", "--verify", "-q", f"{boundary}^{{commit}}")
        import datetime
        bound["frozen"] = {"frozen_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                           "round_3_boundary_commit": git("rev-parse", f"{boundary}^{{commit}}"),
                           "scope": "schema-only"}
        LABELS.write_text(json.dumps(labels, indent=2) + "\n", encoding="utf-8", newline="\n")
        rec = derive(commit)
        OUT.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(f"FROZEN (schema-only): {rec['candidate_id']} = {rec['contract_bundle_id']} @ {rec['derived_at_commit'][:10]}, boundary {bound['frozen']['round_3_boundary_commit'][:10]}")
        return
    rec = derive(commit)
    if "--check" in sys.argv:
        cur = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
        same = {k: v for k, v in cur.items() if k != "$comment"} == {k: v for k, v in rec.items() if k != "$comment"}
        print(("OK" if same else "STALE") + f": {OUT.name} vs derivation at {rec['derived_at_commit'][:10]}")
        sys.exit(0 if same else 1)
    text = json.dumps(rec, indent=2) + "\n"
    if "--write" in sys.argv:
        labels = json.loads(LABELS.read_text(encoding="utf-8")) if LABELS.exists() else {}
        bound = labels.get(rec["candidate_id"])
        if bound and bound["contract_bundle_id"] != rec["contract_bundle_id"]:
            sys.exit(f"REFUSED: label {rec['candidate_id']} is already bound to {bound['contract_bundle_id']} "
                     f"@ {bound['derived_at_commit'][:10]}; a byte-distinct bundle needs a new label (R3-CRO-12)")
        if not bound:
            # a NEW binding only; an existing (matching) entry is left untouched -- rewriting it
            # dropped the `frozen` sub-record on the first --write after --freeze (measured
            # 2026-08-28 04:1xZ: record said frozen, registry said candidate, --check said STALE)
            labels[rec["candidate_id"]] = {"contract_bundle_id": rec["contract_bundle_id"],
                                           "derived_at_commit": rec["derived_at_commit"]}
            LABELS.write_text(json.dumps(labels, indent=2) + "\n", encoding="utf-8", newline="\n")
        OUT.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {OUT.name}: {rec['candidate_id']} = {rec['contract_bundle_id']} @ {rec['derived_at_commit'][:10]}")
    else:
        print(text)


if __name__ == "__main__":
    main()
