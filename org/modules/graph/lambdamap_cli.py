#!/usr/bin/env python3
"""comp-lambdamap -- derive/verify the Lambda source-map against ground truth.

Phase 1 (this file): `check` -- read-only drift detection. Compares
the function map (infra/aws/lambda/ci/function-map/, one file per function; CT-ca-1) against the two real sources of
truth (Terraform function->source_dir + the on-disk lambda dirs) and reports
drift classes. NO map mutation (zero blast radius). CI-gate friendly: exits 1
on any drift, 0 when clean.

Drift classes:
  WRONG_SOURCE_DIR   source-map source_dir != TF source_dir, or the dir is absent
  MISLOCATED         entry is a TOP-LEVEL key (outside functions{}) -> no sha-refresh/provenance
  INCOMPLETE_SCHEMA  functions{} entry missing source_dir (build-and-upload can't build it)
  MISSING_ENTRY      TF-backed lambda with NO functions{} entry (CI-drift-blind)
  ORPHAN_ENTRY       functions{} entry with no TF resource AND no on-disk dir

Phase 2 (this file): `sha` -- live CodeSha256 drift detection. Compares each
functions{} entry's recorded artifact_sha256 against the LIVE AWS CodeSha256
(one paginated list-functions call, us-east-1). Read-only. Catches the
half-landed / out-of-band-update class the source-map records but the live
function diverged from. Exits 1 on any SHA_DRIFT or NOT_LIVE.
Phase 2 remaining (next increments, CVO-gated): `derive --write` map-regenerate
+ provenance fold; multi-region/multi-runtime enumeration.

Origin: BMKAUD source-map audit (CVO 359375d87) + CTO charter (f9e70457a).
Author: 0.7.0_AE_CloudOps.
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys

# the one reader of the function map (CT-ca-1): lib/opal_lambda_map.py, found from this file's location
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
import opal_lambda_map as olm  # noqa: E402

FUNCTION_MAP_REL = "infra/aws/lambda/ci/function-map"
TF_ROOT_REL = "infra/aws/terraform"
LAMBDA_ROOT_REL = "infra/aws/lambda"
# top-level source-map keys that are metadata, not function entries
META_KEYS = {"_description", "_updated", "_note", "functions", "_last_deploy_recorded"}


def workspace_root() -> str:
    # this file lives at <root>/org/modules/graph/lambdamap_cli.py
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def load_srcmap(root: str) -> dict:
    """The function map as {"functions": {name: entry}}, read whole from the per-function folder. Read-only;
    a missing or empty folder raises (olm.load_all). Writers use write_function_files, never the whole folder."""
    return {"functions": olm.load_all(root)}


def write_function_files(root: str, entries: dict) -> None:
    """Rewrite ONLY the files of the named functions: <folder>/<name>.json holds the entry object alone. A name with
    no existing file raises (a new function is a new file, written by the cell that adds it, never by this tool)."""
    d = os.path.join(root, FUNCTION_MAP_REL)
    for name, entry in sorted(entries.items()):
        path = os.path.join(d, name + ".json")
        if not os.path.isfile(path):
            raise FileNotFoundError("no function-map file for %r: %s" % (name, path))
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(entry, indent=2, sort_keys=False, ensure_ascii=True) + "\n")


def _strip_interp(val: str) -> str:
    # normalize "${local.lambda_base_dir}/x" -> "infra/aws/lambda/x"
    val = val.replace("${local.lambda_base_dir}", "infra/aws/lambda")
    val = re.sub(r"\$\{[^}]+\}", "", val)
    return val.strip().strip("/")


def parse_tf(root: str) -> dict:
    """Return {function_name: {'source_dir': <rel or None>, 'tf_file': <rel>}}.

    Matches both `module "x" { ... function_name=.. source_dir=.. }` (yang-lambda
    module pattern) and raw `resource "aws_lambda_function" "x" { function_name=.. }`.
    Regex-based (mirrors comp-iam's HCL approach) -- sufficient for these stanzas.
    """
    out: dict = {}
    tf_root = os.path.join(root, TF_ROOT_REL)
    block_re = re.compile(
        r'(?:module|resource)\s+(?:"aws_lambda_function"\s+)?"[^"]+"\s*\{', re.M)
    for dirpath, dirnames, filenames in os.walk(tf_root):
        if ".terraform" in dirpath:
            continue
        for fn in filenames:
            if not fn.endswith(".tf"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, root).replace("\\", "/")
            try:
                text = open(path, encoding="utf-8").read()
            except Exception:
                continue
            # split into top-level brace blocks (greedy-safe: scan by stanza start)
            for m in block_re.finditer(text):
                start = m.end()
                depth = 1
                i = start
                while i < len(text) and depth:
                    if text[i] == "{":
                        depth += 1
                    elif text[i] == "}":
                        depth -= 1
                    i += 1
                blk = text[start:i - 1]
                fnm = re.search(r'function_name\s*=\s*"([^"$]+)"', blk)
                if not fnm:
                    continue
                name = fnm.group(1)
                sdm = re.search(r'source_dir\s*=\s*"([^"]+)"', blk)
                sd = _strip_interp(sdm.group(1)) if sdm else None
                # last writer wins is fine; dedupe by name, prefer one with source_dir
                if name not in out or (sd and not out[name].get("source_dir")):
                    out[name] = {"source_dir": sd, "tf_file": rel}
    return out


def compute_findings(root: str):
    """Return (findings, stats). findings = [(class, name, detail)]. Pure (no print) -- testable."""
    sm = load_srcmap(root)
    funcs = sm.get("functions", {})
    top_level = {k: v for k, v in sm.items() if k not in META_KEYS}
    tf = parse_tf(root)

    findings: list[tuple[str, str, str]] = []  # (class, name, detail)

    # MISLOCATED: any non-meta top-level key
    for name in top_level:
        findings.append(("MISLOCATED", name,
                         "top-level key outside functions{} -> no sha-refresh/provenance"))

    # per functions{} entry: WRONG_SOURCE_DIR / INCOMPLETE_SCHEMA / ORPHAN_ENTRY
    for name, e in funcs.items():
        sd = e.get("source_dir")
        if not sd:
            findings.append(("INCOMPLETE_SCHEMA", name, "no source_dir"))
        elif sd == "EXTERNAL":
            # intentional sentinel: code lives outside the repo (not drift)
            continue
        else:
            abs_sd = os.path.join(root, sd)
            if not os.path.isdir(abs_sd):
                findings.append(("WRONG_SOURCE_DIR", name,
                                 f"source_dir absent on disk: {sd}"))
            elif name in tf and tf[name].get("source_dir") and \
                    tf[name]["source_dir"].rstrip("/") != sd.rstrip("/"):
                findings.append(("WRONG_SOURCE_DIR", name,
                                 f"source-map={sd} != TF={tf[name]['source_dir']}"))
        # ORPHAN: not TF-backed and dir (if any) absent
        if name not in tf:
            if not sd or not os.path.isdir(os.path.join(root, sd)):
                findings.append(("ORPHAN_ENTRY", name,
                                 "no TF resource and no on-disk source_dir"))

    # MISSING_ENTRY: TF-backed lambda with no functions{} entry
    for name in tf:
        if name not in funcs:
            findings.append(("MISSING_ENTRY", name,
                             f"TF-backed (in {tf[name]['tf_file']}) but no functions{{}} entry"))

    findings.sort(key=lambda f: (CLASS_ORDER.index(f[0]) if f[0] in CLASS_ORDER else 99, f[1]))
    stats = {"functions": len(funcs), "top_level": len(top_level), "tf": len(tf)}
    return findings, stats


CLASS_ORDER = ["WRONG_SOURCE_DIR", "MISSING_ENTRY", "INCOMPLETE_SCHEMA",
               "MISLOCATED", "ORPHAN_ENTRY"]


def check(root: str) -> int:
    findings, stats = compute_findings(root)
    print("comp-lambdamap check -- source-map vs TF + on-disk dirs (read-only)")
    print(f"  source-map functions: {stats['functions']} | top-level non-meta: {stats['top_level']} "
          f"| TF lambdas: {stats['tf']}")
    if not findings:
        print("  CLEAN: no drift. source-map matches TF + dirs.")
        return 0
    counts: dict = {}
    for cls, _, _ in findings:
        counts[cls] = counts.get(cls, 0) + 1
    print("  DRIFT: " + ", ".join(f"{counts[c]} {c}" for c in CLASS_ORDER if c in counts))
    for cls, name, detail in findings:
        print(f"    [{cls}] {name}: {detail}")
    return 1


def live_code_shas():
    """Return {function_name: CodeSha256} from live AWS (us-east-1), or None if
    unavailable. ONE paginated list-functions call covers the whole account --
    far cheaper than a get-function per entry, and CodeSha256 comes back inline.
    None (not {}) signals 'could not read live' so sha_check reports UNAVAILABLE
    rather than mis-flagging every function as NOT_LIVE."""
    try:
        import boto3  # noqa: PLC0415 -- optional dep; tool degrades gracefully without it
    except Exception:
        return None
    try:
        cl = boto3.client("lambda", region_name="us-east-1")
        out: dict = {}
        for page in cl.get_paginator("list_functions").paginate():
            for fn in page.get("Functions", []):
                out[fn["FunctionName"]] = fn.get("CodeSha256", "")
        return out
    except Exception:
        return None


def _parse_lambda_mtime(s):
    """list-functions LastModified ('2026-06-09T15:15:50.000+0000') -> aware
    datetime, or None. Used by the parity settle-guard."""
    if not s:
        return None
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f%z")
    except Exception:
        try:
            return datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except Exception:
            return None


def live_lambda_modified():
    """{name: aware-datetime of last code update} from one list-functions call,
    or None if unavailable. Feeds the parity settle-guard (an in-flight deploy
    makes live momentarily != S3 -- a transient, not a half-landed break)."""
    try:
        import boto3  # noqa: PLC0415
        cl = boto3.client("lambda", region_name="us-east-1")
        out = {}
        for page in cl.get_paginator("list_functions").paginate():
            for fn in page.get("Functions", []):
                out[fn["FunctionName"]] = _parse_lambda_mtime(fn.get("LastModified"))
        return out
    except Exception:
        return None


# A valid AWS CodeSha256 / artifact_sha256 is base64-encoded SHA-256: 32 bytes
# -> 44 base64 chars ending in '='. Anything else recorded in the field is a
# CORRUPT record (e.g. a Windows path leaked by record-terraform-deploy), NOT a
# real deploy-drift -- distinguishing the two routes to different fixes.
_B64_SHA256 = re.compile(r"^[A-Za-z0-9+/]{43}=$")
# An entry whose `_note` documents an INTENTIONAL artifact-vs-live divergence
# (e.g. live = a bundled package, the S3 artifact is a stale re-zip NOT to apply,
# TF lifecycle ignore_changes) is NOT drift. Recognize the dispositioned class
# and suppress it -- a recorded artifact_sha256 that intentionally != live
# CodeSha256 must not false-flag as SHA_DRIFT (and must not mislead a re-record).
# Conservative-correctness, same discipline as the comp-iam condition-fix.
_DISPOSITION_RE = re.compile(r"intentional-leave|ignore_changes|not[\s-]?to[\s-]?apply",
                             re.IGNORECASE)


def compute_sha_findings(funcs: dict, live):
    """Pure classifier (no print, no AWS) -- testable. Given the source-map
    functions{} and a {name: live_CodeSha256} map, classify each recorded entry.
    artifact_sha256 and AWS CodeSha256 are BOTH base64 SHA-256 -> directly ==.

    CORRUPT_RECORD (recorded value not a valid base64 sha) is split from
    SHA_DRIFT (a data bug isn't a deployed-code divergence); DISPOSITIONED (a
    divergence the entry's _note documents as intentional) is also split out so
    it neither false-flags nor invites a wrong re-record."""
    drift, not_live, corrupt, dispositioned = [], [], [], []
    match = no_record = 0
    for name, e in sorted(funcs.items()):
        rec = e.get("artifact_sha256")
        if not rec:
            no_record += 1
            continue
        if not _B64_SHA256.match(str(rec)):
            corrupt.append((name, str(rec)))
            continue
        if name not in live:
            not_live.append(name)
        elif live[name] == rec:
            match += 1
        elif _DISPOSITION_RE.search(str(e.get("_note", ""))):
            dispositioned.append((name, rec, live[name]))
        else:
            drift.append((name, rec, live[name]))
    return {"match": match, "no_record": no_record, "drift": drift,
            "not_live": not_live, "corrupt": corrupt, "dispositioned": dispositioned}


def sha_check(root: str) -> int:
    sm = load_srcmap(root)
    funcs = sm.get("functions", {})
    print("comp-lambdamap sha -- recorded artifact_sha256 vs LIVE CodeSha256 "
          "(Phase 2, read-only, us-east-1)")
    live = live_code_shas()
    if live is None:
        print("  UNAVAILABLE: could not read live CodeSha256 (boto3 or AWS creds "
              "absent). Install boto3 / configure creds and re-run.")
        return 2
    r = compute_sha_findings(funcs, live)
    recorded = len(funcs) - r["no_record"]
    print(f"  functions: {len(funcs)} | recorded-sha: {recorded} | no-record: {r['no_record']} "
          f"| live-fns-in-acct: {len(live)}")
    print(f"  MATCH: {r['match']} | SHA_DRIFT: {len(r['drift'])} | NOT_LIVE: {len(r['not_live'])} "
          f"| CORRUPT_RECORD: {len(r['corrupt'])} | DISPOSITIONED: {len(r['dispositioned'])}")
    for name, rec, liveh in r["drift"]:
        print(f"    [SHA_DRIFT] {name}: source-map={rec[:16]}.. != live={liveh[:16]}.. "
              f"(live running a DIFFERENT artifact than recorded -- half-landed / out-of-band update)")
    for name in r["not_live"]:
        print(f"    [NOT_LIVE] {name}: recorded (with artifact_sha256) but NOT found live in us-east-1 "
              f"(deleted out-of-band, renamed, or non-us-east-1)")
    for name, rec in r["corrupt"]:
        print(f"    [CORRUPT_RECORD] {name}: artifact_sha256 is not a base64 sha: {rec[:40]!r} "
              f"(source-map data bug -- record-terraform-deploy wrote a non-sha value; re-record)")
    for name, rec, liveh in r["dispositioned"]:
        print(f"    [DISPOSITIONED] {name}: recorded != live, but _note documents an intentional "
              f"divergence (e.g. bundled pkg / ignore_changes / S3-artifact not-to-apply) -- NOT drift")
    if not (r["drift"] or r["not_live"] or r["corrupt"]):
        extra = f" ({len(r['dispositioned'])} dispositioned divergence(s) suppressed)" if r["dispositioned"] else ""
        print(f"  CLEAN: every non-dispositioned recorded artifact_sha256 matches the live CodeSha256.{extra}")
        return 0
    return 1


ARTIFACT_BUCKET = "opal-313476888478-lambda-artifacts"


def s3_artifact_sha(s3_key):
    """The deploy artifact's base64 SHA-256 = the `content-sha256` metadata the
    builders store at upload. The cheap evidence (head-object, no download) for
    the live-vs-S3 parity check. None if unreadable (boto3/creds/object absent)."""
    if not s3_key:
        return None
    try:
        import boto3  # noqa: PLC0415
        h = boto3.client("s3", region_name="us-east-1").head_object(
            Bucket=ARTIFACT_BUCKET, Key=s3_key)
        return (h.get("Metadata") or {}).get("content-sha256")
    except Exception:
        return None


def classify_reconcile(drift, key_of, sha_of_s3):
    """Split drift proposals into SAFE (STALE-RECORD: live == the current S3
    deploy artifact -> recorded sha just went stale, reconcile is correct) vs
    UNSAFE (POSSIBLE-HALF-LANDED or UNVERIFIABLE: live != S3 artifact, or the S3
    sha can't be read -> reconcile-to-live would LAUNDER a wrong deployed
    artifact + silence the detector). Pure (sha_of_s3 injected) -> testable.

    This is CVO's binding gate condition baked into the tool (verdict ed13b714a):
    --write must only touch entries where live == the S3 deploy artifact."""
    safe, unsafe = [], []
    for name, rec, liveh in drift:
        s3sha = sha_of_s3(key_of(name))
        if s3sha and s3sha == liveh:
            safe.append((name, rec, liveh))
        else:
            reason = "POSSIBLE-HALF-LANDED (live != S3 artifact)" if s3sha else "UNVERIFIABLE (S3 sha unreadable)"
            unsafe.append((name, rec, liveh, reason))
    return safe, unsafe


def derive(root: str, write: bool = False, only=None) -> int:
    """Reconcile the source-map artifact_sha256 to the LIVE CodeSha256 for
    DRIFTED entries -- the durable record-writer fix (record the DEPLOYED sha).
    Dry-run by default; --write mutates the source-map (CVO-gated).

    SAFE-BY-CONSTRUCTION on two axes: (1) disposition-aware -- only the
    classifier's real `drift` is a candidate (a DISPOSITIONED/CORRUPT entry is
    never written); (2) anti-launder -- each candidate is split STALE-RECORD
    (live == current S3 deploy artifact, reconcile correct) vs POSSIBLE-HALF-
    LANDED / UNVERIFIABLE, and --write touches ONLY the STALE-RECORD class. So
    --write can only move a confirmed-stale sha to the deployed truth; it can
    never launder a half-landed deploy or clobber a disposition."""
    sm = load_srcmap(root)
    funcs = sm.get("functions", {})
    print("comp-lambdamap derive -- reconcile source-map artifact_sha256 -> LIVE CodeSha256 "
          "(Phase 2; dry-run unless --write)")
    live = live_code_shas()
    if live is None:
        print("  UNAVAILABLE: could not read live CodeSha256 (boto3/creds absent).")
        return 2
    r = compute_sha_findings(funcs, live)
    drift = [d for d in r["drift"] if d[0] in only] if only else r["drift"]
    if only is not None:
        print(f"  scoped --only: {len(drift)} of {len(r['drift'])} drift candidate(s) in the named "
              f"set (post-apply deployed scope)")
    safe, unsafe = classify_reconcile(
        drift, lambda n: funcs[n].get("artifact_s3_key"), s3_artifact_sha)
    print(f"  drift candidates: {len(r['drift'])} -> STALE-RECORD (safe): {len(safe)} | "
          f"POSSIBLE-HALF-LANDED/UNVERIFIABLE (HOLD): {len(unsafe)} | "
          f"dispositioned (LEFT): {len(r['dispositioned'])} | corrupt (builder): {len(r['corrupt'])}")
    for name, rec, liveh in safe:
        print(f"    [STALE-RECORD] {name}: {rec[:16]}.. -> {liveh[:16]}.. (live == S3 artifact; safe to reconcile)")
    for name, rec, liveh, reason in unsafe:
        print(f"    [HOLD] {name}: recorded != live, but {reason} -- do NOT reconcile; investigate (could be half-landed)")
    if not write:
        print("  DRY-RUN: no changes written. `derive --write` reconciles ONLY the STALE-RECORD class "
              "(CVO-GATED per-entry confirm of live==S3, verdict ed13b714a).")
        return 1 if unsafe else 0
    print("  CVO-GATED WRITE: mutating the function-map folder (one file per changed function) -- CVO sign-off WITH live==S3 evidence required "
          "per entry (NFRA_COMPAWS.LAMBDAMAP-P2). Writing ONLY the STALE-RECORD class; HOLD entries skipped.")
    if not safe:
        print("  nothing safe to re-record.")
        return 1 if unsafe else 0
    for name, rec, liveh in safe:
        funcs[name]["artifact_sha256"] = liveh
    write_function_files(root, {name: funcs[name] for name, _rec, _liveh in safe})
    print(f"  WROTE: reconciled {len(safe)} STALE-RECORD entr(ies) to live CodeSha256 "
          f"({len(unsafe)} HOLD left for investigation). Re-run `comp-lambdamap sha` to confirm.")
    return 1 if unsafe else 0


# Parity verdicts -> tri-state exit class (CTO arch-gate refinement, mirrors
# comp-validate PASS/ADVISORY/UNVALIDATED). 0 = non-actionable, 1 = true
# integrity break, 2 = could-not-verify.
_PARITY_EXIT = {
    "MATCH": 0, "STALE-RECORD": 0, "DISPOSITIONED": 0, "NO-RECORD": 0,
    "POSSIBLE-HALF-LANDED": 1, "CORRUPT-RECORD": 1, "NOT-LIVE": 1,
    "UNVERIFIABLE": 2, "SETTLING": 2,
}
_PARITY_ORDER = ["MATCH", "STALE-RECORD", "DISPOSITIONED", "SETTLING",
                 "POSSIBLE-HALF-LANDED", "CORRUPT-RECORD", "NOT-LIVE",
                 "UNVERIFIABLE", "NO-RECORD"]
_SETTLE_SECONDS = 180  # an in-flight deploy < this old = SETTLING, not a break


def compute_parity(funcs, live, key_of, sha_of_s3, modified=None, now=None,
                   settle_seconds=_SETTLE_SECONDS):
    """Pure 3-leg deploy-parity classifier -- record (source-map) x live
    (CodeSha256) x s3 (artifact content-sha256). Returns {name: (verdict,
    detail)}. COST GUARD: sha_of_s3 is invoked ONLY for the non-MATCH divergent
    subset (MATCH/NO-RECORD/CORRUPT/NOT-LIVE never touch S3). Spec 9ebcbb49f.

    SETTLE-GUARD (CVO race finding): if `modified` ({name: aware-datetime of
    last code update}) and `now` are supplied, a live!=S3 divergence whose live
    was updated < settle_seconds ago is an in-flight deploy (live moved, S3/
    record not yet) -> classified SETTLING (transient could-not-verify, exit 2),
    NOT POSSIBLE-HALF-LANDED -- so a CI gate doesn't flap red during normal
    deploys. Omit modified/now to disable (pure-test default)."""
    out = {}
    for name, e in sorted(funcs.items()):
        rec = e.get("artifact_sha256")
        note = str(e.get("_note", ""))
        if not rec:
            out[name] = ("NO-RECORD", "no artifact_sha256 (not sha-tracked)")
        elif not _B64_SHA256.match(str(rec)):
            out[name] = ("CORRUPT-RECORD", f"record not base64: {str(rec)[:32]}")
        elif name not in live:
            # orphan record -- DISPOSITIONABLE (decommissioned-but-mapped = hygiene, not a break)
            out[name] = (("DISPOSITIONED", "not-live, intentional _note")
                         if _DISPOSITION_RE.search(note)
                         else ("NOT-LIVE", "recorded but absent in live (orphan / wrong region)"))
        elif live[name] == rec:
            out[name] = ("MATCH", "")
        elif _DISPOSITION_RE.search(note):
            out[name] = ("DISPOSITIONED", "intentional divergence (_note)")
        else:
            # divergence -> leg 3 (the ONLY S3 read)
            s3 = sha_of_s3(key_of(name))
            if not s3:
                out[name] = ("UNVERIFIABLE", "content-sha256 metadata absent on S3 artifact")
            elif s3 == live[name]:
                out[name] = ("STALE-RECORD", "live == S3 artifact; record stale (safe derive --write)")
            else:
                mt = (modified or {}).get(name)
                age = (now - mt).total_seconds() if (mt is not None and now is not None) else None
                if age is not None and age < settle_seconds:
                    out[name] = ("SETTLING",
                                 f"live updated {int(age)}s ago (deploy in flight) -- transient, re-check after it lands")
                else:
                    out[name] = ("POSSIBLE-HALF-LANDED", "live != S3 artifact -- deploy problem, investigate")
    return out


def parity(root: str, as_json: bool = False) -> int:
    sm = load_srcmap(root)
    funcs = sm.get("functions", {})
    live = live_code_shas()
    if live is None:
        if as_json:
            print(json.dumps({"error": "UNAVAILABLE", "reason": "no boto3/creds"}))
        else:
            print("comp-lambdamap parity -- UNAVAILABLE: could not read live CodeSha256 (boto3/creds absent).")
        return 2
    modified = live_lambda_modified()  # settle-guard input (None -> guard off)
    now = datetime.datetime.now(datetime.timezone.utc)
    verdicts = compute_parity(funcs, live,
                              lambda n: funcs[n].get("artifact_s3_key"), s3_artifact_sha,
                              modified=modified, now=now)
    counts = {v: 0 for v in _PARITY_ORDER}
    for _name, (verdict, _d) in verdicts.items():
        counts[verdict] = counts.get(verdict, 0) + 1
    exit_code = max((_PARITY_EXIT.get(v, 0) for v, _ in verdicts.values()), default=0)

    if as_json:
        print(json.dumps({
            "summary": counts,
            "exit": exit_code,
            "verdicts": {n: {"verdict": v, "detail": d} for n, (v, d) in verdicts.items()},
        }, indent=2))
        return exit_code

    print("comp-lambdamap parity -- 3-leg deploy-parity (record x live CodeSha256 x S3 artifact), read-only")
    print("  " + " | ".join(f"{v}: {counts[v]}" for v in _PARITY_ORDER))
    # only actionable / notable verdicts get per-Lambda lines; MATCH + NO-RECORD
    # are bulk non-actionable states -> summarized in the counts (full per-Lambda
    # detail is in --json).
    for name, (verdict, detail) in verdicts.items():
        if verdict not in ("MATCH", "NO-RECORD"):
            print(f"    [{verdict}] {name}: {detail}")
    # COVERAGE PROMINENCE (CVO P3): exit-0 must not read as whole-estate-verified.
    total = len(funcs)
    unchecked = counts["NO-RECORD"] + counts["UNVERIFIABLE"] + counts["SETTLING"]
    checked = total - unchecked
    bits = []
    if counts["NO-RECORD"]:
        bits.append(f"{counts['NO-RECORD']} NO-RECORD")
    if counts["UNVERIFIABLE"]:
        bits.append(f"{counts['UNVERIFIABLE']} UNVERIFIABLE")
    if counts["SETTLING"]:
        bits.append(f"{counts['SETTLING']} SETTLING")
    cov = f"  COVERAGE: {checked}/{total} functions verified" + (f"; UNCHECKED: {', '.join(bits)}" if bits else "")
    print(cov)
    verdict_word = {0: "IN-PARITY (no integrity break)", 1: "INTEGRITY BREAK",
                    2: "UNVERIFIABLE / SETTLING (could-not-verify)"}[exit_code]
    print(f"  => {verdict_word} over the {checked} verified (exit {exit_code})")
    return exit_code


_RECONCILE_AUDIT = "infra/aws/lambda/ci/source-map-reconcile-audit.jsonl"


def reconcile_deployed(root, only, settle_retry_seconds=0, deployed_commit="",
                       audit_rel=_RECONCILE_AUDIT) -> int:
    """Post-apply DURABLE source-map reconcile (CVO gate b56df0083 -- C1/C2/C3).
    For the just-deployed function set `only`, reconcile STALE-RECORD (live==S3)
    -> record the LIVE CodeSha256, so the source-map tracks deployed truth and
    the drift class cannot recur.

      C1 (HOLD + ALERT, exit 1): a just-deployed fn that is PERSISTENTLY
         POSSIBLE-HALF-LANDED / UNVERIFIABLE after settle = the deploy didn't
         fully land -> NOT reconciled, alerted (the caller SNS-notifies).
      C2 (settle-aware): live is seconds old + S3 can lag -> a SETTLING (live!=
         S3 within the deploy window) entry is retried once after
         settle_retry_seconds, reconciled if it settles, alerted only if
         persistent. Reuses compute_parity's settle-guard.
      C3 (audit): every reconcile + every HOLD is appended to a durable JSONL.

    FAIL-SAFE: an empty/unknown deployed set is a NO-OP (never reconcile-all)."""
    sm = load_srcmap(root)
    allf = sm.get("functions", {})
    funcs = {n: allf[n] for n in (only or []) if n in allf}
    if not funcs:
        print("  reconcile-deployed: empty/unknown deployed set -- fail-safe NO-OP (never reconcile-all)")
        return 0

    def classify():
        live = live_code_shas() or {}
        modified = live_lambda_modified()
        now = datetime.datetime.now(datetime.timezone.utc)
        v = compute_parity(funcs, live, lambda n: funcs[n].get("artifact_s3_key"),
                           s3_artifact_sha, modified=modified, now=now)
        return v, live

    verdicts, live = classify()
    settling = [n for n, (vd, _) in verdicts.items() if vd == "SETTLING"]
    if settling and settle_retry_seconds > 0:
        print(f"  C2 settle: {len(settling)} in-flight ({', '.join(settling)}) -- waiting "
              f"{settle_retry_seconds}s then re-checking")
        import time  # noqa: PLC0415
        time.sleep(settle_retry_seconds)
        verdicts, live = classify()

    reconciled, held, first, unrecorded = [], [], [], []
    for n, (vd, detail) in sorted(verdicts.items()):
        if vd == "STALE-RECORD":
            old = funcs[n].get("artifact_sha256")
            funcs[n]["artifact_sha256"] = live[n]
            reconciled.append((n, old, live[n]))
        elif vd in ("POSSIBLE-HALF-LANDED", "UNVERIFIABLE", "SETTLING"):
            held.append((n, vd, detail))
        elif vd == "NO-RECORD":
            # FIRST RECORD (AMGT_RESAPP-D1-S6): a just-deployed fn with no sha yet takes the live
            # CodeSha256 under the STALE-RECORD proof (live == S3 artifact). live != S3 is the
            # half-landed shape -> HOLD. No S3 key or no content-sha256 metadata (a local-zip
            # deploy) cannot be proven -> left unrecorded and said so, never alerted.
            s3 = s3_artifact_sha(funcs[n].get("artifact_s3_key")) if n in live else None
            if n not in live:
                unrecorded.append((n, "not live"))
            elif not s3:
                unrecorded.append((n, "no S3 artifact content-sha256 to prove live against"))
            elif s3 == live[n]:
                funcs[n]["artifact_sha256"] = live[n]
                first.append((n, None, live[n]))
            else:
                held.append((n, "POSSIBLE-HALF-LANDED", "no record, and live != S3 artifact"))
        # MATCH/DISPOSITIONED/CORRUPT: not this hook's job -> leave.

    if reconciled or first:
        # only the deployed function(s) that were reconciled or first-recorded: one file each, nothing else
        write_function_files(root, {n: funcs[n] for n in [r[0] for r in reconciled] + [f[0] for f in first]})
    # C3 audit -- durable, append-only. ONLY on an actual reconcile/HOLD (a
    # no-op run must not touch the file -- keeps the tracked audit clean).
    if reconciled or first or held:
        try:
            ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
            with open(os.path.join(root, audit_rel), "a", encoding="utf-8") as fh:
                for action, rows in (("reconcile", reconciled), ("first-record", first)):
                    for n, old, new in rows:
                        fh.write(json.dumps({"ts": ts, "trigger": "automated-post-apply", "fn": n,
                                             "action": action, "old_sha": old, "new_sha": new,
                                             "deployed_commit": deployed_commit}) + "\n")
                for n, vd, _ in held:
                    fh.write(json.dumps({"ts": ts, "trigger": "automated-post-apply", "fn": n,
                                         "action": "HOLD", "verdict": vd,
                                         "deployed_commit": deployed_commit}) + "\n")
        except Exception as e:
            print(f"  WARN: audit append failed ({e}) -- reconcile still applied")

    parity_n = len(funcs) - len(reconciled) - len(first) - len(held) - len(unrecorded)
    print(f"  reconcile-deployed: {len(reconciled)} reconciled, {len(first)} first-recorded, {len(held)} HELD, "
          f"{len(unrecorded)} left unrecorded, {parity_n} already-in-parity")
    for n, old, new in reconciled:
        print(f"    [RECONCILED] {n}: {(old or '')[:16]}.. -> {new[:16]}..")
    for n, _old, new in first:
        print(f"    [FIRST-RECORD] {n}: none -> {new[:16]}.. (live == S3 artifact)")
    for n, why in unrecorded:
        print(f"    [NO-RECORD] {n}: left unrecorded -- {why}")
    if held:
        print("  !!! ALERT (C1): post-apply HALF-LANDED -- the deploy did NOT fully land for "
              "(record HELD, NOT reconciled -- investigate):")
        for n, vd, detail in held:
            print(f"    [{vd}] {n}: {detail}")
        return 1
    return 0


def census(root: str, out=None) -> int:
    """Vintage-stamped APPLIED lambda census -- descriptor row #2 of the census substrate
    (2026-08-05 extraction, Andrew-present; comp-iam is row #1). The whole mode is a
    DESCRIPTOR CONSUMPTION: transport, failure classes, _meta stamp, field projection all
    come from census_substrate; this function only picks the output path and prints the
    summary. THAT is the scaling thesis measured: row #2 cost ~this function.

    DISTINCT from `sha`: sha is the LIVE-PRIMARY sweep (boto3, no artifact, compares now
    against the source-map now). A census is a DATED SNAPSHOT the vintage gate can
    adjudicate -- the substrate's FRESH/STALE/NO_VINTAGE/FUTURE applies to it, and future
    reconcile-style consumers resolve newest-by-vintage exactly like comp-iam does."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from census_substrate import build_descriptor_census
    snap = build_descriptor_census("aws.lambda", tool="comp-lambdamap census")
    date_tag = snap["_meta"]["generated_utc"][:10].replace("-", "")
    out_path = os.path.join(root, out) if out else os.path.join(
        root, "docs", "briefs", "cmpaws-lambda-census-%s.json" % date_tag)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(snap, fh, indent=2)
    m = snap["_meta"]
    print("OK: APPLIED lambda census written -> %s" % out_path)
    print("  generated_utc : %s   account: %s" % (m["generated_utc"], m["account"]))
    print("  api           : %s" % m["api"])
    print("  functions     : %d" % snap["summary"]["item_count"])
    print("  scope         : %s" % m["scope"])
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="comp-lambdamap")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("check", help="read-only source-map vs TF/disk drift detection (Phase 1)")
    sub.add_parser("sha", help="read-only recorded-sha vs LIVE CodeSha256 drift (Phase 2)")
    d = sub.add_parser("derive", help="reconcile artifact_sha256 -> live CodeSha256 (dry-run; --write CVO-gated)")
    d.add_argument("--write", action="store_true",
                   help="apply the reconcile to the function-map folder, one file per changed function (CVO-gated mutation)")
    d.add_argument("--only", default=None,
                   help="comma-separated function names to scope the reconcile to "
                        "(e.g. the post-apply deployed set, for the record-terraform-deploy hook)")
    p = sub.add_parser("parity", help="read-only 3-leg deploy-parity classifier (a.k.a. comp-derivedrift); "
                                      "tri-state exit 0=in-parity 1=break 2=unverifiable")
    p.add_argument("--json", action="store_true", help="machine-readable output for CI/piping")
    rd = sub.add_parser("reconcile-deployed",
                        help="post-apply durable reconcile of the just-deployed set to live "
                             "(settle-aware, HOLD+ALERT on persistent half-landed, audited)")
    rd.add_argument("--functions", required=True,
                    help="comma-separated just-deployed function names (the record-terraform-deploy set)")
    rd.add_argument("--settle-retry-seconds", type=int, default=0,
                    help="C2: wait this long then re-check SETTLING entries before alerting (post-apply: ~45)")
    rd.add_argument("--deployed-commit", default="", help="commit sha for the audit record")
    c = sub.add_parser("census",
                       help="vintage-stamped APPLIED lambda census via the descriptor substrate "
                            "(census_substrate.py aws.lambda row; 2026-08-05 extraction). "
                            "Writes docs/briefs/cmpaws-lambda-census-<date>.json. DISTINCT from "
                            "`sha` (live-primary sweep, no snapshot): a census is a dated "
                            "artifact the vintage gate can adjudicate.")
    c.add_argument("--out", default=None, help="output path (default docs/briefs/cmpaws-lambda-census-<date>.json)")
    args = ap.parse_args(argv)
    root = workspace_root()
    if args.cmd in (None, "check"):
        return check(root)
    if args.cmd == "census":
        return census(root, out=args.out)
    if args.cmd == "sha":
        return sha_check(root)
    if args.cmd == "derive":
        only = (set(filter(None, (s.strip() for s in args.only.split(","))))
                if args.only else None)
        return derive(root, write=args.write, only=only)
    if args.cmd == "parity":
        return parity(root, as_json=args.json)
    if args.cmd == "reconcile-deployed":
        fns = set(filter(None, (s.strip() for s in args.functions.split(","))))
        return reconcile_deployed(root, fns, settle_retry_seconds=args.settle_retry_seconds,
                                  deployed_commit=args.deployed_commit)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
