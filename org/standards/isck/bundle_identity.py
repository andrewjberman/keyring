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
# R4-CTO-3 (1.0.0_SA_CTO~X 2026-08-28 18:0xZ, on DT~X 78538): the doctrine's $comment names THREE operational
# receipts -- WP-3 ledger, live vertical slice, HISTORICAL REPLAY -- and the WP-3b decomp/TO (11 tracked files)
# cut a `historical_replay_receipt` cell on that reading, but this tuple never carried the kind: the CLI refused it
# by enum while receipt_problem() returned None for it (the kind gate lived only in main()). APPEND, never remove
# (R3-CRO-31: a slot is set once; `clean_clone_gate_receipt` stays as the declared slot it is, consumer or not).
# Rule-24 record: domain = operational receipt kinds appended to a FROZEN label's registry entry; grain = one kind,
# one slot; intent = one (which certification a value attests); MECE over the doctrine's three named receipts +
# the pre-existing gate slot; state = each slot moves once, independently. Word-boundary census at the edit:
# `historical_replay_receipt` 11 tracked files (all WP-3b), 0 in this tool or the doctrine.
RECEIPT_KINDS = ("clean_clone_gate_receipt", "wp3_certification_receipt", "vertical_slice_receipt",
                 "historical_replay_receipt")


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


RECEIPT_PATH = f"{REL}/receipts/{{kind}}.json"
RECEIPT_FIELDS = ("kind", "candidate_id", "contract_bundle_id", "manifest_path", "manifest_digest", "result",
                  "evidence_path", "evidence_digest", "run_commit")


def receipt_problem(commit, kind, rec):
    """Return None when <commit> carries a valid structured receipt of <kind> for <rec>'s label, else
    the first problem as text. Reads ONLY the object database at <commit> (never the working tree)."""
    import re
    # R4-CTO-3: the kind gate lived only in main(), so a Python-level call returned None for a kind the CLI
    # refuses -- a wrong-type call returning the expected shape. Gate here too, so both arms agree.
    if kind not in RECEIPT_KINDS:
        return f"receipt kind {kind!r} is not one of {RECEIPT_KINDS} (a receipt of an unregistered kind certifies nothing)"
    path = RECEIPT_PATH.format(kind=kind)
    try:
        raw = subprocess.check_output(["git", "-C", str(ROOT), "cat-file", "blob", f"{commit}:{path}"],
                                      stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return f"commit {commit[:10]} carries no {path} (a commit that exists is not a certification)"
    try:
        r = json.loads(raw)
    except ValueError:
        return f"{path} at {commit[:10]} is not JSON"
    missing = [f for f in RECEIPT_FIELDS if f not in r]
    if missing:
        return f"{path} at {commit[:10]} lacks {missing}"
    if r["kind"] != kind:
        return f"receipt kind is {r['kind']!r}, asked {kind!r}"
    if r["candidate_id"] != rec["candidate_id"] or r["contract_bundle_id"] != rec["contract_bundle_id"]:
        return f"receipt names {r['candidate_id']} / {r['contract_bundle_id'][:24]}..., label is {rec['candidate_id']} / {rec['contract_bundle_id'][:24]}..."
    if r["result"] != "PASS":
        return f"receipt result is {r['result']!r}, not PASS"
    for f in ("manifest_digest", "evidence_digest"):
        if not re.fullmatch(r"sha256:[0-9a-f]{64}", str(r[f])):
            return f"receipt {f} is not a sha256: string"
    try:
        manifest = subprocess.check_output(["git", "-C", str(ROOT), "cat-file", "blob", f"{commit}:{r['manifest_path']}"],
                                           stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return f"receipt manifest_path {r['manifest_path']!r} is absent at {commit[:10]}"
    if "sha256:" + hashlib.sha256(manifest).hexdigest() != r["manifest_digest"]:
        return "receipt manifest_digest does not recompute from the manifest at the same commit"
    # R3-CRO-36: the two load-bearing evidence fields were decorative -- presence and syntax only.
    # run_commit BINDS: it must resolve, and the bundle DERIVED AT run_commit must be the very bundle
    # this receipt certifies (the run certified these bytes, not some bytes). evidence RECOMPUTES:
    # evidence_path must exist at the receipt commit and hash to evidence_digest.
    try:
        run_full = git("rev-parse", "--verify", "-q", f"{r['run_commit']}^{{commit}}")
    except subprocess.CalledProcessError:
        return f"receipt run_commit {r['run_commit']!r} does not resolve to a commit"
    if derive(run_full)["contract_bundle_id"] != rec["contract_bundle_id"]:
        return f"receipt run_commit {run_full[:10]} derives a different bundle than the one certified ({rec['contract_bundle_id'][:24]}...)"
    try:
        evidence = subprocess.check_output(["git", "-C", str(ROOT), "cat-file", "blob", f"{commit}:{r['evidence_path']}"],
                                           stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return f"receipt evidence_path {r['evidence_path']!r} is absent at {commit[:10]}"
    if "sha256:" + hashlib.sha256(evidence).hexdigest() != r["evidence_digest"]:
        return "receipt evidence_digest does not recompute from the evidence at the same commit"
    # R4-CVO-5 (3.0.0_SA_CVO~X 123534Z): run_commit was bound to the BUNDLE (derive) and to nothing
    # else -- a receipt could name any commit deriving the label while its evidence witnessed a
    # different run. The evidence is the runner's own stdout and prints the full clone commit
    # ("CLEAN CLONE of BUILD commit <40 hex>"), so the binding is: the evidence must NAME run_commit.
    # Negative control at the fix: e8d3326bd5 (run_commit c557006b0b, evidence naming d11c341f79)
    # is REFUSED here and nowhere above.
    if run_full.encode() not in evidence and run_full[:10].encode() not in evidence:
        return f"receipt evidence does not witness run_commit {run_full[:10]} (the runner's own line names the clone commit; a run_commit the evidence never mentions is a claim, not a run)"
    return None


def derive(commit):
    full = git("rev-parse", f"{commit}^{{commit}}")
    members = [DOCTRINE, SCHEMA, VALIDATOR, *GATES, *VOCAB]
    pairs = sorted((p, blob(full, p)) for p in members)
    bundle_id = "bundle:sha256:" + hashlib.sha256("\n".join(f"{p} {b}" for p, b in pairs).encode()).hexdigest()
    schema_text = subprocess.check_output(["git", "-C", str(ROOT), "cat-file", "blob", f"{full}:{SCHEMA}"])
    schema_id = json.loads(schema_text).get("$id")
    labels = json.loads(LABELS.read_text(encoding="utf-8")) if LABELS.exists() else {}
    # R3-CRO-12: the human label must resolve to exactly one bundle -- and (CVO~X 20260828T043852Z,
    # self-drive D11 ledger row 12) one bundle resolves to exactly one label: a bundle id ALREADY
    # BOUND in the registry keeps its label (content-addressed identity; a second alias on the same
    # bytes is refused by construction), and only an UNBOUND bundle derives a fresh label.
    # FAMILY RULE for an unbound bundle: the +38 freeze is SCHEMA-ONLY, so the family is decided by
    # the SCHEMA blob -- equal to the frozen +38 schema -> still the v0.2-candidate family (a
    # gate-only amendment), N = package-path commits since the round-2 boundary; different -> the
    # v0.3-candidate family, N = package-path commits since the round-3 boundary, and
    # supersedes_bundle_id = the frozen +38 bundle. Never a v0.3 label bound as an alias of a
    # v0.2-candidate+N record. Both counts are monotone along the path (injective handles).
    frozen_38 = next(((k, v) for k, v in labels.items() if (v.get("frozen") or {}).get("scope") == "schema-only"), (None, {}))
    frozen_label, frozen_entry = frozen_38
    round_3_boundary = (frozen_entry.get("frozen") or {}).get("round_3_boundary_commit") or BOUNDARIES["round_3_boundary_commit"]
    schema_blob = blob(full, SCHEMA)
    frozen_schema_blob = blob(frozen_entry["derived_at_commit"], SCHEMA) if frozen_entry else None
    bound = next((k for k, v in labels.items() if v.get("contract_bundle_id") == bundle_id), None)
    supersedes_bundle_id = None
    if bound:
        candidate_id = bound
        family = candidate_id.rsplit("+", 1)[0]
        supersedes_bundle_id = labels[bound].get("supersedes_bundle_id")
    elif frozen_entry and schema_blob != frozen_schema_blob:
        family = "v0.3-candidate"
        since_3 = git("rev-list", "--reverse", f"{round_3_boundary}..{full}", "--", REL).split()
        candidate_id = f"{family}+{len(since_3)}"
        supersedes_bundle_id = frozen_entry["contract_bundle_id"]
    else:
        family = "v0.2-candidate"
        post_boundary = git("rev-list", "--reverse", f"{BOUNDARIES['round_2_boundary_commit']}..{full}", "--", REL).split()
        candidate_id = f"{family}+{len(post_boundary)}"
    post_boundary = git("rev-list", "--reverse", f"{BOUNDARIES['round_2_boundary_commit']}..{full}", "--", REL).split()
    # C4 (CVO~X 20260828T040820Z): a FREEZE is a registry fact, so it is derived here like every
    # other field -- the label's registry entry carries frozen_at + round_3_boundary_commit; a frozen
    # label emits status=frozen and --check stays deterministic. The freeze is SCHEMA-ONLY: the three
    # operational receipts stay null BY DEFINITION until WP-3 / the live slice / replay land.
    fz = labels.get(candidate_id, {}).get("frozen") or {}
    receipts = labels.get(candidate_id, {}).get("receipts") or {}
    return {
        "contract_bundle_id": bundle_id,
        "semantic_version": family,
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
        **{**BOUNDARIES, "round_3_boundary_commit": round_3_boundary},
        "post_boundary_amendments": post_boundary,
        **{k: receipts.get(k) for k in RECEIPT_KINDS},
        "supersedes_bundle_id": supersedes_bundle_id,
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
        # R3-CRO-33: a commit that EXISTS is not a certification -- the pre-ledger +38 pin itself
        # was accepted as a wp3_certification_receipt. The value must CONTAIN a structured receipt
        # of this kind, for this label and bundle, whose manifest digest recomputes from the same
        # commit and whose result is PASS. Everything is checked before the registry is touched.
        problem = receipt_problem(value, kind, rec)
        if problem:
            sys.exit(f"REFUSED: {problem}; nothing written")
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
        # R4-DT-10 (DT~X 77766): the +27 freeze commit wrote its own freeze entry into DOCTRINE, a
        # MEMBER, and moved the bundle it was freezing (87ed7080 -> 103cfd6c); receipt_problem's
        # run_commit binding was then unsatisfiable at every commit with an engine. A freeze's own
        # record lives in BUNDLE_LABELS.json (facts) and FREEZE_LOG.md (prose), never in a member:
        # REFUSE when the working-tree DOCTRINE differs from the DOCTRINE blob at the commit being
        # frozen -- the act that carries this freeze must not also edit the contract's prose.
        wt_doctrine = git("hash-object", str(ROOT / DOCTRINE))
        if wt_doctrine != blob(commit, DOCTRINE):
            sys.exit(f"REFUSED: working-tree {DOCTRINE} ({wt_doctrine[:10]}) differs from its blob at {commit[:10]} "
                     f"({blob(commit, DOCTRINE)[:10]}); a freeze's own record never lives inside a member -- "
                     f"write the prose to FREEZE_LOG.md and freeze from a commit whose DOCTRINE you did not edit")
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
        # R4-CTO-4 (1.0.0_SA_CTO~X 2026-08-28 18:5xZ, on DT~X 78718 / WP-4 AC2): this compared the WHOLE record,
        # provenance pointers included, so it read STALE at every commit except the one the record was derived
        # at -- a check that can pass at exactly one commit says nothing about the bundle, and its STALE was
        # indistinguishable from a real member change (measured: HEAD STALE, 7a44b65f50 STALE, same word).
        # The record is derive(<pin>) by construction (--write / --receipt), so the pointers are EXPECTED to
        # differ from HEAD's. IDENTITY fields decide the verdict; pointer deltas print as INFO, never as a verdict.
        # post_boundary_amendments = rev-list <round-2 boundary>..<commit> -- org/standards/isck: the package-path
        # commit list at that vintage, which grows with every isck commit (registers, receipts, this tool) while
        # the bundle stands still -- provenance, not identity (a bound bundle's candidate_id is the registry's).
        POINTERS = ("derived_at_commit", "doctrine_commit", "schema_commit", "validator_commit", "gate_suite_commit",
                    "post_boundary_amendments")
        cur = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
        def ident(d):
            return {k: v for k, v in d.items() if k != "$comment" and k not in POINTERS}
        cur_i, rec_i = ident(cur), ident(rec)
        diff = sorted(k for k in set(cur_i) | set(rec_i) if cur_i.get(k) != rec_i.get(k))
        moved = [k for k in POINTERS if cur.get(k) != rec.get(k)]
        if diff:
            print(f"STALE: {OUT.name} identity differs from the derivation at {rec['derived_at_commit'][:10]} on {diff}")
            sys.exit(1)
        print(f"MATCH: {OUT.name} identity == derivation at {rec['derived_at_commit'][:10]} "
              f"(bundle {rec['contract_bundle_id'][:24]}..., {rec['candidate_id']})"
              + (f"; INFO pointers differ {moved} -- the record is derived at its pin, not at this commit" if moved else ""))
        sys.exit(0)
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
            if rec["supersedes_bundle_id"]:
                # a v0.3-family binding records the frozen bundle it supersedes (CVO~X row 12)
                labels[rec["candidate_id"]]["supersedes_bundle_id"] = rec["supersedes_bundle_id"]
            LABELS.write_text(json.dumps(labels, indent=2) + "\n", encoding="utf-8", newline="\n")
        OUT.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {OUT.name}: {rec['candidate_id']} = {rec['contract_bundle_id']} @ {rec['derived_at_commit'][:10]}")
    else:
        print(text)


if __name__ == "__main__":
    main()
