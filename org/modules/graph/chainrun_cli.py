"""ADHC_VALGATE.007 -- comp-chainrun: the Class-B chain-run pre/post sentinel-diff gate.

Class B of the VALGATE four-class acceptance-gate taxonomy catches
PARTIAL-REFACTOR LEAKS: a helper signature changes and a consumer is not
updated; an atomic-bundle ship drops a sibling. The chain-run A/B/C/D-stage
SHAPE sentinels (artifact-exists / columns-present / row-count > 0) already
exist as worker-discipline checks -- but there was no structural fire and no
pre/post diff. The GATE did not exist. comp-chainrun formalizes it (PRD
section 4.B, N7).

Mechanism:
  comp-chainrun snapshot --label pre     capture the stage sentinel set BEFORE
                                         an atomic-bundle ship
  < ship the bundle; re-run the chain >
  comp-chainrun snapshot --label post    capture it AFTER
  comp-chainrun diff pre.json post.json  a sentinel that flipped green->absent,
                                         lost a column, or went row-count>0->0
                                         is a partial-refactor leak -> WARN

Verdict policy (PRD section 7 Q1, reused verbatim from the .001-.003 Class-C
suite -- do NOT fork the conventions): v1 ships WARN-not-BLOCK. The WARN->BLOCK
ratchet, after ~1-2 weeks of empirical false-positive data, is a one-line flip
of GATE_VERDICT_POLICY in this module. The verdict -> exit-code mapping mirrors
valgate_gate.py (WARN/PASS/SKIP -> 0, BLOCK -> non-zero) so any future
dispatcher / hook wire is exit-code-gated from day one.

The stage-sentinel set is the in-code curated CHAIN_MANIFEST -- the same
in-code declared-registry convention as the Class-C valgate_baseline.py
registries (ARTIFACT_CONFIG / SENTINEL_REGISTRY / CROSS_SOURCE_REGISTRY): a
small set of known-stable per-stage artifacts, not an exhaustive scan. A new
sentinel is a CHAIN_MANIFEST edit; an external JSON manifest may be supplied
via --manifest for offline / test use.

Anchor: DWSPLT chain #26 partial-refactor leak -- a consumer signature mismatch
surviving an atomic-bundle ship; forward-fix dd1206258 validated by chain #27.

PRD: docs/architecture/ADHC_VALGATE.md v0.1 -- section 3.2 (gate anatomy),
section 4.B (Class-B formalization, N7), section 7 Q1 (verdict policy).
Author: 0.7.0_AE_CloudOps~B (ADHC_VALGATE.007)
"""
from __future__ import annotations

import argparse
import datetime as dt
import io
import json
import os

# ---------------------------------------------------------------------------
# Verdict model -- reused verbatim from valgate_gate.py (the .001-.003 Class-C
# suite). v1 policy = "warn": a partial-refactor leak -> WARN, never BLOCK.
# The WARN->BLOCK ratchet is exactly the GATE_VERDICT_POLICY arm of
# verdict_for(). SKIP = the diff had nothing to compare.
# ---------------------------------------------------------------------------

GATE_VERDICT_POLICY = "warn"          # v1; ratchet to "block" post-FP-data

VERDICT_EXIT = {"PASS": 0, "WARN": 0, "SKIP": 0, "BLOCK": 1}
_VERDICT_RANK = {"PASS": 0, "SKIP": 0, "WARN": 2, "BLOCK": 3}


def verdict_for(finding: str) -> str:
    """Map a diff finding (leak / no-leak) to a verdict under the current
    policy. The WARN->BLOCK ratchet is exactly this function's `policy` arm."""
    if finding != "leak":
        return "PASS"
    return "BLOCK" if GATE_VERDICT_POLICY == "block" else "WARN"


# ---------------------------------------------------------------------------
# Gate anatomy -- the PRD section 3.2 six-field contract for the Class-B gate.
# Filled here in-code so the gate's contract travels with the gate (the same
# pattern as valgate_gate.py GATE_SPEC).
# ---------------------------------------------------------------------------

GATE_SPEC: dict = {
    "B": {
        "name": "chain-run pre/post sentinel-diff",
        "trigger": "any atomic-bundle ship (a multi-commit refactor touching a "
                   "producer + its consumers) -- carried as a Phase-N TO step: "
                   "comp-chainrun snapshot pre-bundle, snapshot post-bundle, "
                   "diff",
        "input": "the chain's A/B/C/D-stage shape-sentinel set -- per the "
                 "in-code CHAIN_MANIFEST artifact: exists / columns / "
                 "row-count",
        "reference": "the pre-bundle snapshot (the pre-refactor sentinel set) "
                     "-- the reference the producer code does not contain",
        "comparison": "set + shape diff -- a sentinel that flips green->absent "
                      "(DROPPED), loses a column (COLUMNS-LOST), or goes "
                      "row-count>0->0 (EMPTIED)",
        "verdict": "WARN on any leak (v1; PASS when the diff is clean; SKIP "
                   "when the two snapshots share no comparable sentinel)",
        "action": "surface the [VALGATE-B] leak report to the session log + "
                  "the TO's Phase-N gate step; route to the bundle author; "
                  "does NOT block the ship in v1",
    },
}


# ---------------------------------------------------------------------------
# Artifact readers -- S3 (production) and local-dir (offline / fixture / the
# selfcheck), the same two-backend split as valgate_baseline.BaselineStore.
# ---------------------------------------------------------------------------

class _NotFound(Exception):
    """The artifact is genuinely absent (S3 404 / missing local file) -- a
    capture records exists=False. Distinct from an error (creds / network /
    parse) which records an `error` so the diff never reads absent-for-an-
    unknown-reason as a clean green->absent."""


def _infer_kind(artifact: str) -> str:
    """Infer artifact kind from extension when the manifest entry omits it."""
    low = artifact.lower()
    if low.endswith(".parquet"):
        return "parquet"
    if low.endswith(".json"):
        return "json"
    return "unknown"


def _s3_reader(bucket: str):
    """Return a reader(artifact)->bytes backed by S3 get_object on `bucket`.
    A 404 / NoSuchKey raises _NotFound (-> exists=False); any other error
    propagates (-> capture records it as an error, not a clean absence)."""
    import boto3
    from botocore.exceptions import ClientError

    client = boto3.client("s3", region_name="us-east-1")

    def read(artifact: str) -> bytes:
        try:
            return client.get_object(Bucket=bucket, Key=artifact)[
                "Body"].read()
        except ClientError as exc:
            code = str(exc.response.get("Error", {}).get("Code", ""))
            if code in ("NoSuchKey", "404", "NoSuchBucket"):
                raise _NotFound(artifact) from exc
            raise

    return read


def _dir_reader(dirpath: str):
    """Return a reader(artifact)->bytes backed by a local directory. The
    artifact key's '/' segments map to nested subdirectories under dirpath."""

    def read(artifact: str) -> bytes:
        path = os.path.join(dirpath, *artifact.split("/"))
        if not os.path.isfile(path):
            raise _NotFound(artifact)
        with open(path, "rb") as fh:
            return fh.read()

    return read


# ---------------------------------------------------------------------------
# Shape extraction -- the (columns, row_count) shape sentinel per artifact kind
# ---------------------------------------------------------------------------

def _parquet_shape(raw: bytes) -> tuple:
    """(sorted column names, row count) for a parquet artifact."""
    import pandas as pd

    frame = pd.read_parquet(io.BytesIO(raw))
    return sorted(str(c) for c in frame.columns), int(len(frame))


def _json_shape(raw: bytes) -> tuple:
    """(sorted shape keys, row count) for a JSON artifact.

    - A top-level list: row_count is the list length; columns is the union of
      dict keys across the elements.
    - A top-level dict: columns is the sorted top-level key set; row_count is
      the length of the longest list-valued top-level entry (the records
      array a portal emit usually carries), falling back to the key count.
    This makes a vanished records list visible as a row-count>0->0 flip and a
    dropped top-level key visible as a COLUMNS-LOST flip."""
    obj = json.loads(raw.decode("utf-8"))
    if isinstance(obj, list):
        cols: set = set()
        for el in obj:
            if isinstance(el, dict):
                cols.update(str(k) for k in el)
        return sorted(cols), len(obj)
    if isinstance(obj, dict):
        cols = sorted(str(k) for k in obj)
        list_lens = [len(v) for v in obj.values() if isinstance(v, list)]
        return cols, (max(list_lens) if list_lens else len(cols))
    return [], 0


def capture_sentinel(entry: dict, reader) -> dict:
    """Capture the shape sentinel for one manifest artifact: exists, columns,
    row_count -- plus an `error` when the artifact could not be assessed for a
    reason other than genuine absence."""
    artifact = entry["artifact"]
    kind = entry.get("kind") or _infer_kind(artifact)
    out = {"stage": entry.get("stage", "?"), "kind": kind, "exists": False,
           "columns": [], "row_count": 0, "error": None}
    try:
        raw = reader(artifact)
    except _NotFound:
        return out                                  # genuine absence
    except Exception as exc:                        # noqa: BLE001
        out["error"] = f"{type(exc).__name__}: {exc}"
        return out
    out["exists"] = True
    try:
        if kind == "parquet":
            out["columns"], out["row_count"] = _parquet_shape(raw)
        elif kind == "json":
            out["columns"], out["row_count"] = _json_shape(raw)
        else:
            out["error"] = f"unknown artifact kind '{kind}'"
    except Exception as exc:                        # noqa: BLE001
        out["error"] = f"shape-read failed: {type(exc).__name__}: {exc}"
    return out


# ---------------------------------------------------------------------------
# Manifest -- the curated A/B/C/D stage-sentinel set, in-code.
#
# CHAIN_MANIFEST is a Python dict, not a separate file -- the same in-code
# declared-registry convention as valgate_baseline.py (ARTIFACT_CONFIG /
# SENTINEL_REGISTRY / CROSS_SOURCE_REGISTRY). It is a CURATED set of
# known-stable, non-date-partitioned per-stage artifacts -- not an exhaustive
# scan of every chain output. A new sentinel is an edit to the `sentinels`
# list below; no code change. An external JSON manifest (same shape) may be
# supplied via --manifest for offline / test use.
# ---------------------------------------------------------------------------

CHAIN_MANIFEST: dict = {
    "manifest": "chainrun_manifest_v1",
    "chain": "inf-gold",
    "default_bucket": "opal-data-inf",
    "sentinels": [
        {"stage": "A",
         "artifact": "gold/dimensions/accounts_dimension_latest.parquet",
         "kind": "parquet", "producer": "INF_A_00.accounts_dimension.py",
         "basis": "Stage-A account dimension -- stable named "
                  "(non-date-partitioned) artifact."},
        {"stage": "A",
         "artifact": "gold/dimensions/advisor_assignments.parquet",
         "kind": "parquet", "producer": "INF_A_01.advisor_assignments.py",
         "basis": "Stage-A advisor-assignment dimension -- stable named "
                  "artifact."},
        {"stage": "A",
         "artifact": "gold/dimensions/client_dimension.parquet",
         "kind": "parquet", "producer": "INF_A_04.client_dimension.py",
         "basis": "Stage-A client dimension -- stable named artifact."},
        {"stage": "B",
         "artifact": "gold/lots/lots_latest.parquet",
         "kind": "parquet", "producer": "INF_B_01.holdings_lots.py",
         "basis": "Stage-B canonical lots -- the latest-pointer "
                  "(non-date-partitioned) artifact."},
        {"stage": "C",
         "artifact": "gold/timeseries/account_performance.parquet",
         "kind": "parquet", "producer": "INF_C_03.account_performance.py",
         "basis": "Stage-C account performance timeseries -- stable named "
                  "artifact."},
        {"stage": "C",
         "artifact": "gold/timeseries/client_performance.parquet",
         "kind": "parquet", "producer": "INF_C_02.client_performance.py",
         "basis": "Stage-C client performance timeseries -- INF_C_02 is a "
                  "recurring refactor surface (INFGRO window-TWR)."},
        {"stage": "C",
         "artifact": "gold/views/fee_status_audit.parquet",
         "kind": "parquet", "producer": "INF_C_09.fee_status_audit.py",
         "basis": "Stage-C fee-status audit view -- stable named artifact."},
        {"stage": "D",
         "artifact": "gold/artifacts/cumulative_chart.json",
         "kind": "json", "producer": "INF_D_00d.cumulative_chart.py",
         "basis": "Stage-D portal cumulative-chart emit -- stable named "
                  "JSON artifact."},
        {"stage": "D",
         "artifact": "gold/artifacts/employee_leaderboard.json",
         "kind": "json", "producer": "INF_D_00c.portal_leaderboard.py",
         "basis": "Stage-D portal leaderboard emit -- stable named JSON "
                  "artifact."},
        {"stage": "D",
         "artifact": "gold/artifacts/firm_mix_views.json",
         "kind": "json", "producer": "INF_D_02d.firm_mix_summary.py",
         "basis": "Stage-D firm-mix portal emit -- stable named JSON "
                  "artifact."},
    ],
    "review": "Re-validate this set when a stage's canonical artifact path "
              "changes, when a new stage-representative artifact stabilizes, "
              "or when an atomic-bundle ship reveals a refactor surface no "
              "current sentinel covers.",
}


def load_manifest(path: str | None = None) -> dict:
    """Return the chain stage-sentinel manifest. Default = the in-code
    CHAIN_MANIFEST; `--manifest <path>` loads an external JSON manifest of the
    same shape (offline / test use)."""
    if not path:
        return CHAIN_MANIFEST
    with open(path, "rb") as fh:
        manifest = json.loads(fh.read())
    if not isinstance(manifest.get("sentinels"), list):
        raise ValueError(f"manifest {path} has no 'sentinels' list")
    return manifest


def _utcnow() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Snapshot
# ---------------------------------------------------------------------------

def build_snapshot(label: str, manifest: dict, reader, source_desc: str,
                   manifest_path: str) -> dict:
    """Capture every manifest sentinel into a labelled snapshot."""
    sentinels = {}
    for entry in manifest["sentinels"]:
        sentinels[entry["artifact"]] = capture_sentinel(entry, reader)
    return {
        "snapshot": "chainrun_snapshot_v1",
        "label": label,
        "chain": manifest.get("chain", "unknown"),
        "source": source_desc,
        "manifest": manifest_path,
        "sentinel_count": len(sentinels),
        "captured_at": _utcnow(),
        "sentinels": sentinels,
    }


# ---------------------------------------------------------------------------
# Diff -- the partial-refactor-leak report
# ---------------------------------------------------------------------------

# Status -> is-this-a-leak. The three leak classes are exactly the PRD section
# 4.B comparison: green->absent, shape-changed (column lost), row-count>0->0.
_LEAK_STATUSES = {"DROPPED", "COLUMNS-LOST", "EMPTIED", "COLUMNS-LOST+EMPTIED"}


def _classify(pre: dict | None, post: dict | None) -> dict:
    """Classify one sentinel artifact across a pre/post snapshot pair."""
    if pre is None:
        return {"status": "ADDED", "leak": False,
                "detail": "sentinel present only in the post snapshot "
                          "(manifest grew between captures)"}
    if post is None:
        return {"status": "MANIFEST-DROPPED", "leak": False,
                "detail": "sentinel present only in the pre snapshot "
                          "(manifest shrank between captures)"}
    if pre.get("error") or post.get("error"):
        err = pre.get("error") or post.get("error")
        return {"status": "INDETERMINATE", "leak": False,
                "detail": f"shape not assessable ({err}) -- not scored as a "
                          f"leak; re-capture once resolved"}

    pre_x, post_x = bool(pre["exists"]), bool(post["exists"])
    if pre_x and not post_x:
        return {"status": "DROPPED", "leak": True,
                "detail": "present pre, ABSENT post -- artifact flipped "
                          "green->absent"}
    if not pre_x and post_x:
        return {"status": "RESTORED", "leak": False,
                "detail": "absent pre, present post -- artifact appeared "
                          "(not a leak)"}
    if not pre_x and not post_x:
        return {"status": "ABSENT-BOTH", "leak": False,
                "detail": "absent in both snapshots -- nothing to compare"}

    # Both exist -- compare shape.
    pre_cols, post_cols = set(pre["columns"]), set(post["columns"])
    lost = sorted(pre_cols - post_cols)
    added = sorted(post_cols - pre_cols)
    emptied = int(pre["row_count"]) > 0 and int(post["row_count"]) == 0

    notes = []
    if lost:
        notes.append(f"{len(lost)} column(s) lost: {', '.join(lost)}")
    if emptied:
        notes.append(f"row count {pre['row_count']:,}->0 -- emptied")
    if added:
        notes.append(f"{len(added)} column(s) added: {', '.join(added)}")

    if lost and emptied:
        status = "COLUMNS-LOST+EMPTIED"
    elif lost:
        status = "COLUMNS-LOST"
    elif emptied:
        status = "EMPTIED"
    elif added:
        status = "COLUMNS-ADDED"
    else:
        status = "OK"

    if status == "OK":
        detail = (f"shape stable -- {len(post_cols)} column(s), "
                  f"{post['row_count']:,} row(s)")
    else:
        detail = "; ".join(notes)
    return {"status": status, "leak": status in _LEAK_STATUSES,
            "detail": detail}


def diff_snapshots(pre: dict, post: dict) -> dict:
    """Diff two snapshots into a partial-refactor-leak report."""
    pre_s = pre.get("sentinels", {})
    post_s = post.get("sentinels", {})
    artifacts = sorted(set(pre_s) | set(post_s))

    rows = []
    for art in artifacts:
        p = pre_s.get(art)
        q = post_s.get(art)
        cls = _classify(p, q)
        stage = (q or p or {}).get("stage", "?")
        rows.append({"artifact": art, "stage": stage, **cls})

    leaks = [r for r in rows if r["leak"]]
    comparable = [r for r in rows
                  if r["status"] not in ("ADDED", "MANIFEST-DROPPED",
                                          "ABSENT-BOTH", "INDETERMINATE")]
    if not comparable:
        finding, verdict = "no-leak", "SKIP"
    else:
        finding = "leak" if leaks else "no-leak"
        verdict = verdict_for(finding)

    return {
        "valgate_report": "valgate_b_report_v1",
        "chain": post.get("chain", pre.get("chain", "unknown")),
        "pre": {"label": pre.get("label"), "captured_at": pre.get(
            "captured_at"), "source": pre.get("source")},
        "post": {"label": post.get("label"), "captured_at": post.get(
            "captured_at"), "source": post.get("source")},
        "policy": GATE_VERDICT_POLICY,
        "finding": finding,
        "overall_verdict": verdict,
        "sentinel_count": len(rows),
        "leak_count": len(leaks),
        "rows": rows,
        "generated_at": _utcnow(),
    }


def format_report(report: dict, verbose: bool = False) -> str:
    """One-screen human summary for the session-log surface. ASCII only
    (no emoji -- CloudWatch / Windows-codec safe), [VALGATE-B] prefixed to
    parallel valgate_gate.py's [VALGATE-C]."""
    lines = [
        f"[VALGATE-B] chain={report['chain']} "
        f"pre={report['pre']['label']} post={report['post']['label']} "
        f"overall={report['overall_verdict']} "
        f"leaks={report['leak_count']}/{report['sentinel_count']}",
    ]
    shown = [r for r in report["rows"]
             if verbose or r["leak"] or r["status"] not in ("OK",)]
    for r in sorted(shown, key=lambda x: (not x["leak"], x["stage"],
                                          x["artifact"])):
        flag = "LEAK " if r["leak"] else "     "
        lines.append(f"  {flag}[{r['status']}] {r['stage']} {r['artifact']} "
                      f"-- {r['detail']}")
    ok_n = sum(1 for r in report["rows"] if r["status"] == "OK")
    if ok_n and not verbose:
        lines.append(f"  ({ok_n} sentinel(s) OK -- shape stable; "
                      f"--verbose to list)")
    if report["overall_verdict"] == "SKIP":
        lines.append("  (SKIP -- the two snapshots share no comparable "
                     "sentinel)")
    elif report["leak_count"] == 0:
        lines.append("  no partial-refactor leak detected -- diff clean")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

def _resolve_reader(args, manifest: dict):
    """(reader, source_desc) for the snapshot backend the args select."""
    if args.from_dir:
        return _dir_reader(args.from_dir), f"dir:{args.from_dir}"
    bucket = args.bucket or manifest.get("default_bucket", "opal-data-inf")
    return _s3_reader(bucket), f"s3:{bucket}"


def cmd_snapshot(args) -> int:
    manifest = load_manifest(args.manifest)
    manifest_path = args.manifest or "in-code:CHAIN_MANIFEST"
    reader, source_desc = _resolve_reader(args, manifest)
    snap = build_snapshot(args.label, manifest, reader, source_desc,
                          manifest_path)

    out = args.out or f"comp-chainrun-snapshot-{args.label}.json"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(snap, fh, indent=2)

    present = sum(1 for s in snap["sentinels"].values() if s["exists"])
    errors = sum(1 for s in snap["sentinels"].values() if s["error"])
    print(f"[VALGATE-B] snapshot label={args.label} source={source_desc} "
          f"sentinels={snap['sentinel_count']} present={present} "
          f"errors={errors}")
    print(f"  written: {out}")
    if errors:
        for art, s in sorted(snap["sentinels"].items()):
            if s["error"]:
                print(f"  WARN: {art} -- {s['error']}")
    return 0


def cmd_diff(args) -> int:
    with open(args.pre, "rb") as fh:
        pre = json.loads(fh.read())
    with open(args.post, "rb") as fh:
        post = json.loads(fh.read())
    report = diff_snapshots(pre, post)
    print(format_report(report, verbose=args.verbose), flush=True)
    if args.json:
        print(json.dumps(report, indent=2, default=str), flush=True)
    return VERDICT_EXIT.get(report["overall_verdict"], 0)


def cmd_spec(args) -> int:
    """Print the PRD section 3.2 six-field gate contract for the Class-B gate."""
    spec = GATE_SPEC["B"]
    print("[VALGATE-B] Class-B gate -- PRD section 3.2 six-field contract")
    print(f"  gate:       B -- {spec['name']}")
    for field in ("trigger", "input", "reference", "comparison", "verdict",
                  "action"):
        print(f"  {field + ':':<12}{spec[field]}")
    print(f"  policy:     GATE_VERDICT_POLICY={GATE_VERDICT_POLICY} "
          f"(v1; ratchet to 'block' post-FP-data)")
    return 0


# ---------------------------------------------------------------------------
# Selfcheck -- offline, dependency-light verification (TO AC3).
# A no-op pre/post pair yields an empty diff (PASS); a synthetic
# dropped / column-lost / emptied sentinel yields the expected leak report
# (WARN). Uses a local fixture directory + a temp manifest -- no S3, no chain.
# ---------------------------------------------------------------------------

def _selfcheck() -> int:
    import tempfile

    ok = True

    def check(label: str, cond: bool) -> None:
        nonlocal ok
        ok = ok and bool(cond)
        print(f"  [{'PASS' if cond else 'FAIL'}] {label}")

    print("comp-chainrun self-check (ADHC_VALGATE.007)")
    root = tempfile.mkdtemp(prefix="chainrun_sc_")
    pre_dir = os.path.join(root, "pre")
    post_dir = os.path.join(root, "post")

    # Fixture artifacts -- JSON only, so the selfcheck needs no pyarrow. The
    # parquet read path is exercised by the live S3 no-op test (TO Phase 3).
    def write_json(base: str, rel: str, obj) -> None:
        path = os.path.join(base, *rel.split("/"))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(obj, fh)

    arts = {
        "gold/a/stable.json": {"rows": [{"x": 1}, {"x": 2}], "meta": "v"},
        "gold/b/dropme.json": {"rows": [{"y": 1}]},
        "gold/c/cols.json": {"rows": [{"k": 1}], "keep": 1, "drop": 1},
        # A dict with a records array -- emptying the array keeps the
        # top-level key set, so this exercises a PURE EMPTIED flip (the keys
        # are not element-derived, unlike a top-level list).
        "gold/d/emptyme.json": {"rows": [{"z": 1}, {"z": 2}, {"z": 3}],
                                "meta": "v"},
    }
    for rel, obj in arts.items():
        write_json(pre_dir, rel, obj)

    # post = pre, then introduce three synthetic leaks + one benign add.
    for rel, obj in arts.items():
        write_json(post_dir, rel, obj)
    os.remove(os.path.join(post_dir, "gold", "b", "dropme.json"))   # DROPPED
    write_json(post_dir, "gold/c/cols.json",
               {"rows": [{"k": 1}], "keep": 1})                     # COL-LOST
    write_json(post_dir, "gold/d/emptyme.json",
               {"rows": [], "meta": "v"})                           # EMPTIED
    write_json(post_dir, "gold/a/stable.json",
               {"rows": [{"x": 1}, {"x": 2}], "meta": "v",
                "added": 1})                                        # COL-ADD

    manifest = {
        "manifest": "chainrun_manifest_v1", "chain": "selfcheck",
        "default_bucket": "n/a",
        "sentinels": [{"stage": s, "artifact": a, "kind": "json"}
                      for s, a in (("A", "gold/a/stable.json"),
                                   ("B", "gold/b/dropme.json"),
                                   ("C", "gold/c/cols.json"),
                                   ("D", "gold/d/emptyme.json"))],
    }
    mpath = os.path.join(root, "manifest.json")
    with open(mpath, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh)

    pre_snap = build_snapshot("pre", manifest, _dir_reader(pre_dir),
                              f"dir:{pre_dir}", mpath)
    post_noop = build_snapshot("post-noop", manifest, _dir_reader(pre_dir),
                               f"dir:{pre_dir}", mpath)
    post_leak = build_snapshot("post-leak", manifest, _dir_reader(post_dir),
                               f"dir:{post_dir}", mpath)

    check("snapshot captures all 4 sentinels", pre_snap["sentinel_count"] == 4)
    check("snapshot: all 4 present in the pre fixture",
          all(s["exists"] for s in pre_snap["sentinels"].values()))

    # No-op diff -- pre vs an identical capture -> clean, no leak, PASS.
    noop = diff_snapshots(pre_snap, post_noop)
    check("no-op pre/post diff -> 0 leaks", noop["leak_count"] == 0)
    check("no-op pre/post diff -> PASS verdict",
          noop["overall_verdict"] == "PASS")

    # Leak diff -- the three synthetic leaks surface, the benign add does not.
    leak = diff_snapshots(pre_snap, post_leak)
    by_art = {r["artifact"]: r for r in leak["rows"]}
    check("synthetic drop -> DROPPED leak",
          by_art["gold/b/dropme.json"]["status"] == "DROPPED"
          and by_art["gold/b/dropme.json"]["leak"])
    check("synthetic column drop -> COLUMNS-LOST leak",
          by_art["gold/c/cols.json"]["status"] == "COLUMNS-LOST"
          and by_art["gold/c/cols.json"]["leak"])
    check("synthetic empty -> EMPTIED leak",
          by_art["gold/d/emptyme.json"]["status"] == "EMPTIED"
          and by_art["gold/d/emptyme.json"]["leak"])
    check("benign column add -> COLUMNS-ADDED, NOT a leak",
          by_art["gold/a/stable.json"]["status"] == "COLUMNS-ADDED"
          and not by_art["gold/a/stable.json"]["leak"])
    check("leak diff -> 3 leaks", leak["leak_count"] == 3)
    check("leak diff -> WARN verdict (v1 policy)",
          leak["overall_verdict"] == "WARN")
    check("leak diff exit code maps WARN->0 (v1 WARN-not-BLOCK)",
          VERDICT_EXIT[leak["overall_verdict"]] == 0)

    # Indeterminate -- an unreadable artifact is NOT scored a green->absent.
    def _erroring_reader(_artifact):
        raise RuntimeError("simulated creds/network error")

    err_snap = build_snapshot("post-err", manifest, _erroring_reader,
                              "dir:err", mpath)
    err_diff = diff_snapshots(pre_snap, err_snap)
    check("unreadable artifact -> INDETERMINATE, not a leak",
          all(r["status"] == "INDETERMINATE" and not r["leak"]
              for r in err_diff["rows"]))

    print(format_report(leak))
    print(f"=== comp-chainrun self-check: {'ALL PASS' if ok else 'FAIL'} ===")
    return 0 if ok else 1


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="comp-chainrun",
        description="ADHC_VALGATE.007 Class-B gate -- chain-run pre/post "
                    "sentinel-diff. Catches partial-refactor leaks across an "
                    "atomic-bundle ship.")
    sub = ap.add_subparsers(dest="command", required=True)

    sp = sub.add_parser("snapshot",
                        help="capture the A/B/C/D-stage sentinel set")
    sp.add_argument("--label", required=True,
                    help="snapshot label, e.g. pre / post")
    sp.add_argument("--out", default=None,
                    help="output path (default comp-chainrun-snapshot-"
                         "{label}.json)")
    sp.add_argument("--manifest", default=None,
                    help="external JSON manifest override (default: the "
                         "in-code CHAIN_MANIFEST)")
    sp.add_argument("--bucket", default=None,
                    help="S3 bucket override (default the manifest's "
                         "default_bucket)")
    sp.add_argument("--from-dir", default=None,
                    help="read artifacts from a local directory instead of "
                         "S3 (offline / fixture use)")
    sp.set_defaults(func=cmd_snapshot)

    dp = sub.add_parser("diff",
                        help="diff a pre/post snapshot pair -> leak report")
    dp.add_argument("pre", help="pre-bundle snapshot JSON")
    dp.add_argument("post", help="post-bundle snapshot JSON")
    dp.add_argument("--verbose", action="store_true",
                    help="list every sentinel, including the stable ones")
    dp.add_argument("--json", action="store_true",
                    help="also print the full JSON report")
    dp.set_defaults(func=cmd_diff)

    cp = sub.add_parser("spec",
                        help="print the PRD 3.2 six-field gate contract")
    cp.set_defaults(func=cmd_spec)

    scp = sub.add_parser("selfcheck",
                         help="offline no-op + synthetic-leak verification")
    scp.set_defaults(func=lambda _a: _selfcheck())

    return ap


def main(argv: list | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
