#!/usr/bin/env python3
"""
comp-surface-check -- commit-time guard for the critical client-facing surfaces
(NFRA_GRAPHS D8). Sibling of comp-manifest-check (D6).

Maps changed files -> the critical-surface(s) whose carve names them, and emits a
per-surface verdict: SEV1 = block-with-ack, SEV2 = warn, NONE = clean. Severity
resolution (critical-surfaces.yaml monitor.severity_resolution): a file carved into
MULTIPLE surfaces takes the MAX severity (block-with-ack wins over warn) -- the
SEV1 headline + SEV2 aum surfaces share the aum.ts chain, so a shared-file touch
must alarm at SEV1.

Mechanism = direct file-watching derived from each surface's carve prose (which
names the files: frontend_root + backend_chain). This is deliberate, not a fallback:
D8-findings.md shows comp-platinum cannot carve several of these subgraphs
(BenchmarkHeatmap not registered, PeersTab prop-drilled, double-wrapped aum fetches),
so the registry-carve would be blind exactly where it matters. comp-diff backend
deepening is a best-effort future enhancement; the file-watch is the reliable core.

Best-effort: any tooling failure (yaml unparseable, no surfaces) -> ADVISORY pass,
never a hard block on the tool's own failure.

Subcommands:
  comp-surface-check check [--file PATH ...] [--mode blocking|advisory]
      No --file -> uses `git diff --name-only HEAD`. SEV1 touch exits non-zero
      (blocks the commit) UNLESS SURFACE_ACK="<reason>" is set (audited).
  comp-surface-check list        # surfaces + severity + watched files
  comp-surface-check selfcheck   # AC8 synthetic SEV1/SEV2/clean demonstration
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
# org/modules/graph -> modules -> org -> workspace root (3 levels up)
_WS = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
SURFACES_YAML = os.path.join(_HERE, "critical-surfaces.yaml")
ACK_AUDIT = os.path.join(_WS, "org", "surface-check-ack-audit.log")

SEV_ORDER = {"SEV1": 1, "SEV2": 2}          # lower number = higher severity
# bare filenames too generic to match on basename alone (need a full path)
_GENERIC = {"index.tsx", "index.ts", "index.js"}
# tokens that look like file paths/names inside the carve prose
_PATH_RE = re.compile(r"[\w./@-]*?[\w@-]+\.(?:tsx|ts|jsx|js|py|json|yaml|yml)\b")


def _norm(p: str) -> str:
    """forward slashes; drop a leading portal/ so submodule-relative and
    repo-relative paths compare (portal/src/x.tsx  <->  src/x.tsx)."""
    p = p.replace("\\", "/").lstrip("./")
    if p.startswith("portal/"):
        p = p[len("portal/"):]
    return p


def _segsuffix(a: str, b: str) -> bool:
    """True if one normalized path is a segment-aligned suffix of the other."""
    sa, sb = a.split("/"), b.split("/")
    n = min(len(sa), len(sb))
    return n > 0 and sa[-n:] == sb[-n:]


def load_surfaces() -> list[dict]:
    import yaml
    with open(SURFACES_YAML, encoding="utf-8") as f:
        doc = yaml.safe_load(f)
    out = []
    for s in (doc.get("surfaces") or []):
        carve = s.get("carve", {}) or {}
        blob = " ".join(str(v) for v in carve.values()).replace("\\", "/")
        tokens = sorted(set(_PATH_RE.findall(blob)))
        out.append({
            "id": s["id"],
            "severity": s.get("severity", "SEV2"),
            "firms": s.get("firms", "all"),
            "watched": [t for t in tokens if t],
        })
    return out


def _file_touches(changed: str, watched: list[str]) -> list[str]:
    """Return the watched tokens a changed file matches."""
    cf = _norm(changed)
    hits = []
    for t in watched:
        nt = _norm(t)
        if "/" in nt:
            if _segsuffix(cf, nt):
                hits.append(t)
        else:  # bare filename: basename match, excluding too-generic names
            if nt not in _GENERIC and os.path.basename(cf) == nt:
                hits.append(t)
    return hits


def _changed_files(args) -> list[str]:
    if args.file:
        return args.file
    try:
        r = subprocess.run(["git", "diff", "--name-only", "HEAD"],
                           cwd=_WS, capture_output=True, text=True, check=True)
        return [ln.strip() for ln in r.stdout.splitlines() if ln.strip()]
    except Exception as e:
        print(f"ADVISORY: could not read git diff ({type(e).__name__}: {e}); pass --file", file=sys.stderr)
        return []


# ---------------------------------------------------------------------------
# NFRA_GCONTR (TO-2): the contract advisory layer (Q1/Q2). ADDITIVE + ADVISORY.
# A SEV1 contracted-surface commit runs Q2-at-HEAD; an UNSANCTIONED result WARNS
# (advisory) -- it NEVER changes the exit code (the existing file-gate verdict is
# untouched), mirroring the comp-manifest-check D6 advisory ramp. The hard-block
# flip (exit 2 + audited SURFACE_ACK) is a LATER one-line CTO ramp-flip gated on
# low-FP evidence once CVO's SEV1 contracts (TO-3) exist + are tuned. Engine:
# contract_engine.py. Best-effort: any failure -> silent skip, never a block.
# ---------------------------------------------------------------------------

def _contract_advisory(sev1_surface_ids: set) -> None:
    """Print the NFRA_GCONTR Q2 contract advisory for the touched SEV1 surfaces.
    PURELY ADDITIVE -- emits advisory lines only, returns None, and the caller's
    exit code is unaffected. Opt out with GCONTR_SKIP_CONTRACT_CHECK=1."""
    if not sev1_surface_ids:
        return
    if os.environ.get("GCONTR_SKIP_CONTRACT_CHECK", "").strip() in ("1", "true", "yes"):
        return
    try:
        import contract_engine as ce  # lazy: dev-box only; not COPY'd into the derive container
    except Exception:
        return  # engine absent (e.g. in-container nightly) -> contract layer inert

    try:
        contracts, cstatus = ce.load_contracts()
    except Exception:
        return
    print("\n-- NFRA_GCONTR contract layer (Q2, ADVISORY) --")
    if cstatus == "absent":
        print("CONTRACT-ADVISORY: globgrph.graph_contracts not created yet "
              "(NFRA_GCONTR TO-2 in-VPC stand-up pending) -- contract layer inert.")
        return
    if cstatus.startswith("unavailable"):
        print(f"CONTRACT-ADVISORY: graph_contracts unreachable ({cstatus}) -- skipping (never blocks).")
        return

    # only pay the snapshot read when a TOUCHED SEV1 surface is actually CONTRACTED
    contracted = {}
    uncontracted = []
    for sid in sorted(sev1_surface_ids):
        c = ce.contract_for_surface(sid, contracts)
        if c:
            contracted[sid] = c
        else:
            uncontracted.append(sid)

    for sid in uncontracted:
        # false-clean discipline pushed to the value layer: an uncontracted SEV1
        # surface reads LOUD unreviewed, never silently "fine".
        print(f"CONTRACT-ADVISORY: SEV1 surface {sid} is UNCONTRACTED (LOUD: unreviewed) -- "
              f"no graph_contracts row governs it yet (CVO TO-3 authoring).")

    if not contracted:
        return
    try:
        import datetime as _dt
        cur = ce.load_graph_snapshot("latest")
        today = _dt.date.today()
        clist = list(contracted.values())
        q1 = ce.q1_writes_diff(None, cur, clist)
        q2 = ce.q2_join(clist, q1, window=(today, today))
    except Exception as e:
        print(f"CONTRACT-ADVISORY: could not evaluate Q2 ({type(e).__name__}: {e}) -- skipping (never blocks).")
        return
    for sid, c in contracted.items():
        v = q2.get(c["contract_id"])
        if not v:
            continue
        st = v["status"]
        if st == "UNSANCTIONED":
            print(f"CONTRACT-ADVISORY [WARN]: SEV1 surface {sid} contract={c['contract_id']} -> "
                  f"UNSANCTIONED. {v['reason']}")
            print("  (ADVISORY ramp: this WOULD hard-block once the CTO flips the ramp on low-FP "
                  'evidence; set SURFACE_ACK="<reason>" then. Warning only today.)')
        elif st == "SANCTIONED":
            print(f"CONTRACT-ADVISORY: SEV1 surface {sid} contract={c['contract_id']} -> SANCTIONED "
                  f"(ratified contract edit in window; never-widen sign-off recorded).")
        elif st == "WATCH":
            print(f"CONTRACT-ADVISORY: SEV1 surface {sid} contract={c['contract_id']} -> WATCH "
                  f"({len(v['intruders'])} non-canonical, non-forbidden writer(s); shared-bucket "
                  f"capability noise, advisory only).")
        else:
            print(f"CONTRACT-ADVISORY: SEV1 surface {sid} contract={c['contract_id']} -> CLEAN "
                  f"(only canonical_writer={v['canonical_writer']}).")


def cmd_check(args) -> int:
    # best-effort load
    try:
        surfaces = load_surfaces()
    except Exception as e:
        print(f"ADVISORY: comp-surface-check could not load critical-surfaces.yaml "
              f"({type(e).__name__}: {e}) -- passing (never hard-block on tooling failure).")
        return 0
    if not surfaces:
        print("ADVISORY: no surfaces registered -- passing.")
        return 0

    files = _changed_files(args)
    if not files:
        print("OK: no changed files to check.")
        return 0

    # collect touches: file -> {surface_id: severity}
    touches = []   # (file, surface_id, severity)
    for f in files:
        for s in surfaces:
            if _file_touches(f, s["watched"]):
                touches.append((f, s["id"], s["severity"]))

    if not touches:
        print(f"OK: {len(files)} changed file(s) touch no critical surface.")
        return 0

    # effective severity per file = MAX (severity_resolution); overall = max of all
    sev1 = [t for t in touches if t[2] == "SEV1"]
    # de-dupe display
    def _firms(sid, surfaces=surfaces):
        fm = next((x["firms"] for x in surfaces if x["id"] == sid), "all")
        return "bd/inf/cot" if fm == "all" else str(fm)

    for f, sid, sev in sorted(set(touches)):
        tag = "CRITICAL" if sev == "SEV1" else "WARN"
        print(f"{tag}: change touches {sid} ({sev}) [firms: {_firms(sid)}] via {f}"
              + (" -- confirm + justify" if sev == "SEV1" else ""))

    # severity_resolution note when a file hit both tiers
    shared = sorted({f for f, _, sv in touches if sv == "SEV1"}
                    & {f for f, _, sv in touches if sv == "SEV2"})
    for f in shared:
        print(f"  severity_resolution: {f} is in BOTH a SEV1 and a SEV2 surface -> alarms at SEV1.")

    if sev1:
        # NFRA_GCONTR (TO-2): additive contract advisory (Q2). Prints WARN/WATCH/
        # SANCTIONED/CLEAN/uncontracted notes for the touched SEV1 surfaces but
        # NEVER alters the exit code below. Off during selfcheck (synthetic files,
        # no live S3 reads). Best-effort -- never raises.
        if getattr(args, "contract_layer", True):
            try:
                _contract_advisory({t[1] for t in sev1})
            except Exception:
                pass
        if args.mode == "advisory":
            print("\nADVISORY MODE: SEV1 touch would BLOCK in blocking mode "
                  "(ramp not yet flipped) -- warning only.")
            return 0
        ack = os.environ.get("SURFACE_ACK", "").strip()
        if ack:
            _audit(ack, sev1)
            print(f"\nSEV1 ACKNOWLEDGED (SURFACE_ACK={ack!r}) -- audited to "
                  f"{os.path.relpath(ACK_AUDIT, _WS)}. Proceeding.")
            return 0
        print("\nBLOCKED (SEV1, block-with-ack): a critical client-facing surface backend is touched.")
        print('  To proceed deliberately: set SURFACE_ACK="<reason>" and re-run (audited).')
        return 2

    # SEV2 only -> warn, never block
    print("\nWARN: SEV2 surface(s) touched -- review, not blocked.")
    return 0


def _audit(reason: str, sev1_touches: list[tuple]) -> None:
    try:
        from datetime import datetime, timezone
        ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        ids = ",".join(sorted({t[1] for t in sev1_touches}))
        os.makedirs(os.path.dirname(ACK_AUDIT), exist_ok=True)
        with open(ACK_AUDIT, "a", encoding="utf-8") as f:
            f.write(f"{ts} SURFACE_ACK surfaces={ids} reason={reason!r}\n")
        # B1 D8-AE Part B: durable ledger entry in org/critical_paths/change_management/
        _write_ledger_approval(ts, ids, reason, sev1_touches)
    except Exception:
        pass


def _write_ledger_approval(ts: str, ids: str, reason: str,
                            sev1_touches: list[tuple]) -> None:
    """B1: write a durable .md approval entry to org/critical_paths/change_management/.
    Best-effort -- never raises (called from inside except-swallowed _audit)."""
    try:
        commit = ""
        try:
            r = subprocess.run(["git", "rev-parse", "HEAD"], cwd=_WS,
                               capture_output=True, text=True, check=True)
            commit = r.stdout.strip()[:12]
        except Exception:
            pass
        first_surface = sorted({t[1] for t in sev1_touches})[0].replace(".", "-")
        ledger_dir = os.path.join(_WS, "org", "critical_paths", "change_management")
        os.makedirs(ledger_dir, exist_ok=True)
        fname = os.path.join(ledger_dir, f"{ts}_{first_surface}_all_approval.md")
        touched = "\n".join(
            f"- `{f}` ({sid}, {sev})" for f, sid, sev in sorted(set(sev1_touches))
        )
        with open(fname, "w", encoding="utf-8") as fh:
            fh.write(
                f"# SURFACE_ACK approval -- {ts}\n\n"
                f"**class:** approval\n"
                f"**surfaces:** {ids}\n"
                f"**firm:** all\n"
                f"**commit:** {commit or '(unknown)'}\n"
                f"**reason:** {reason}\n\n"
                f"## Touched surfaces\n\n{touched}\n\n"
                f"Durable record (D8-AE B1, NFRA_GRAPHS). "
                f"See org/surface-check-ack-audit.log for the one-line summary.\n"
            )
    except Exception:
        pass


def _load_graph(path: str) -> dict:
    import json
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# Layer-2 (D8-AE Part B, CTO Q1; format LOCKED by COO 180558Z): the signed
# watched-file-SHA baseline lives IN critical-surfaces.yaml under
#   baseline.portal_commit_at_sign + baseline.watched_file_shas.{surface}[{path, sha}]
# DE writes it at re-sign (capture-at-re-sign-only); the scan only READS it. SHAs
# are `git hash-object` blob SHA-1s.


def _git_hash_object(path: str) -> str | None:
    """`git hash-object <file>` blob SHA-1 -- via git so line-ending normalization
    (.gitattributes / autocrlf) matches DE's signed SHA exactly (a raw-bytes hash
    diverges on Windows CRLF). Portal files run in the portal submodule."""
    p = path.replace("\\", "/")
    if p.startswith("portal/"):
        cwd, rel = os.path.join(_WS, "portal"), p[len("portal/"):]
    else:
        cwd, rel = _WS, p
    try:
        r = subprocess.run(["git", "hash-object", rel], cwd=cwd,
                           capture_output=True, text=True, check=True)
        return r.stdout.strip()
    except Exception:
        return None


def _watched_sha_baseline() -> dict | None:
    """Read the signed watched-file-SHA baseline from critical-surfaces.yaml."""
    try:
        import yaml
        with open(SURFACES_YAML, encoding="utf-8") as f:
            doc = yaml.safe_load(f) or {}
        b = ((doc.get("monitor") or {}).get("baseline") or {})
        if b.get("watched_file_shas"):
            return {"portal_commit": b.get("portal_commit_at_sign", ""),
                    "shas": b["watched_file_shas"]}
    except Exception:
        pass
    return None


def cmd_list_watched(args) -> int:
    """The DE handoff (CTO Q1): the exact full-path watched-file list per surface
    that DE SHA-captures + anchors to the portal submodule commit at re-sign."""
    import json
    wm = {}
    for s in load_surfaces():
        for w in s["watched"]:
            if "/" in w:
                wm.setdefault(w, []).append(f"{s['id']}({s['severity']})")
    if args.json:
        print(json.dumps({"watched_files": {k: sorted(v) for k, v in sorted(wm.items())},
                          "note": "DE: capture sha256 of each + the portal submodule commit at re-sign -> "
                                  "org/modules/graph/baseline_watched_files.yaml"}, indent=2))
    else:
        print("Watched files for DE SHA-capture (single source of truth = critical-surfaces.yaml):\n")
        for f, surfs in sorted(wm.items()):
            print(f"  {f}")
            print(f"      surfaces: {', '.join(sorted(surfs))}")
        print("\nDE: capture sha256(each) + the portal submodule commit at re-sign -> "
              "baseline_watched_files.yaml (CTO Q1 conditions 2+3).")
    return 0


def cmd_scan(args) -> int:
    """D8-AE Part B Layer-1 (graph-diff): diff the current graph vs the signed
    baseline and attribute each change to the critical surface(s) whose carve
    names the changed node's file -> SEV-routed findings (SEV1=page / SEV2=digest).

    LAYER-1 ONLY: this sees nodes that ARE in the graph (frontend/API/backend
    Lambda+S3+gold). The 3 coverage-gap surfaces (BenchmarkHeatmap / portal-proxy /
    PeersTab) are NOT graph nodes -> a Layer-2 watched-file-SHA diff (CTO baseline-
    extension ruling pending) is required to cover them; flagged loud below.
    Best-effort: missing snapshots -> ADVISORY, never crash a nightly scan.
    """
    import json
    base_p = args.baseline or os.path.join(_WS, ".comp-graph", "baseline.json")
    cur_p = args.current or os.path.join(_WS, ".comp-graph", "graph.json")
    try:
        surfaces = load_surfaces()
        base = _load_graph(base_p)
        cur = _load_graph(cur_p)
    except Exception as e:
        print(f"ADVISORY: comp-surface-check scan could not load inputs "
              f"({type(e).__name__}: {e}) -- skipping (never crash the nightly).")
        return 0

    bn, cn = base.get("nodes", {}), cur.get("nodes", {})
    # node-level diff
    added = [k for k in cn if k not in bn]
    removed = [k for k in bn if k not in cn]
    changed = [k for k in cn if k in bn
               and (cn[k] or {}).get("source_sha") != (bn[k] or {}).get("source_sha")]

    def _node_file(graph_nodes, k):
        return str((graph_nodes.get(k) or {}).get("file_path") or "")

    findings = []   # (severity, kind, surface_id, node)
    for kind, keys, src in [("ADDED", added, cn), ("REMOVED", removed, bn),
                            ("CHANGED", changed, cn)]:
        for k in keys:
            fp = _node_file(src, k)
            if not fp:
                continue
            for s in surfaces:
                if _file_touches(fp, s["watched"]):
                    findings.append((s["severity"], kind, s["id"], k))

    sev2 = [f for f in findings if f[0] == "SEV2"]

    print("comp-surface-check scan (Layer-1 graph-diff)")
    print(f"  baseline: {os.path.relpath(base_p, _WS)}  ({len(bn)} nodes)")
    print(f"  current:  {os.path.relpath(cur_p, _WS)}  ({len(cn)} nodes)")
    print(f"  node delta: +{len(added)} / -{len(removed)} / ~{len(changed)}")
    if not findings:
        print("  OK: no critical-surface graph node changed since baseline (Day-0 clean).")
    else:
        for sev, kind, sid, node in sorted(set(findings)):
            route = "PAGE" if sev == "SEV1" else "digest"
            print(f"  {sev} [{route}]: {kind} node in {sid} -> {node}")
    # ---- Layer-2: watched-file-SHA diff (per-surface; covers non-graph surfaces) ----
    l2_findings = []   # (severity, file, surface_id, kind)
    l2_status = "unknown"
    wb = _watched_sha_baseline()
    if not wb:
        print("  Layer-2 (file-SHA-watch): HEAD-ORACLE UNKNOWN -- no signed "
              "baseline.watched_file_shas in critical-surfaces.yaml yet (DE re-sign pending; "
              "`comp-surface-check list-watched-files` is the DE handoff).")
    else:
        l2_status = "active"
        sev_by_id = {s["id"]: s["severity"] for s in load_surfaces()}
        nfiles = 0
        for sid, entries in (wb["shas"] or {}).items():
            sev = sev_by_id.get(sid, "SEV2")
            for ent in (entries or []):
                nfiles += 1
                fpath, base_sha = ent.get("path"), ent.get("sha")
                cur = _git_hash_object(fpath) if fpath else None
                if cur is None:
                    l2_findings.append(("SEV1", fpath, sid, "MISSING"))
                elif cur != base_sha:
                    l2_findings.append((sev, fpath, sid, "CHANGED"))
        print(f"  Layer-2 (file-SHA-watch): baseline portal@{str(wb['portal_commit'])[:12]} "
              f"-- {nfiles} watched (surface,file) pair(s)")
        if not l2_findings:
            print("    OK: no watched-file SHA changed since the signed baseline.")
        for sev, fpath, sid, kind in sorted(set(l2_findings)):
            route = "PAGE" if sev == "SEV1" else "digest"
            print(f"    {sev} [{route}] [file-SHA-watch]: {kind} {fpath} ({sid})")

    if args.json:
        print(json.dumps({
            "layer1_graph_drift": {
                "node_delta": {"added": len(added), "removed": len(removed), "changed": len(changed)},
                "findings": [{"severity": s, "kind": k, "surface": sid, "node": n, "coverage": "graph-drift"}
                             for s, k, sid, n in sorted(set(findings))],
            },
            "layer2_file_sha_watch": {
                "status": l2_status,
                "findings": [{"severity": s, "file": fp, "surface": sid, "kind": k,
                              "coverage": "file-SHA-watch"}
                             for s, fp, sid, k in sorted(set(l2_findings))],
            },
            "sev1_total": len({(k, sid, n) for s, k, sid, n in findings if s == "SEV1"})
                          + len({fp for sev, fp, _sid, _k in l2_findings if sev == "SEV1"}),
            "sev2_total": len(set(sev2)) + len({fp for sev, fp, _sid, _k in l2_findings if sev == "SEV2"}),
        }, indent=2))
    # scan is a REPORT (the nightly publishes/alarms); exit 0 always (advisory),
    # SEV-routing is in the payload, not the exit code.
    return 0


def cmd_list(args) -> int:
    surfaces = load_surfaces()
    print(f"comp-surface-check -- {len(surfaces)} critical surface(s) "
          f"(from {os.path.relpath(SURFACES_YAML, _WS)}):\n")
    for s in surfaces:
        print(f"  {s['id']}  [{s['severity']}]  firms={s['firms']}")
        for w in s["watched"]:
            print(f"      watch: {w}")
        print()
    print("severity_resolution: a file in multiple surfaces alarms at the MAX (SEV1 wins).")
    return 0


def cmd_selfcheck(args) -> int:
    """AC8 demonstration: synthetic SEV1 file-touch blocks; SEV2 warns; unrelated passes."""
    surfaces = load_surfaces()
    # SEV1-exclusive set vs SEV2-exclusive set, so the demo cases are unambiguous
    # (a file shared across tiers correctly resolves SEV1 -- that's the aum.ts case,
    # not a clean SEV2 demo). Pick a path-form file from each exclusive set.
    sev1_tokens = {w for s in surfaces if s["severity"] == "SEV1" for w in s["watched"]}
    sev2_tokens = {w for s in surfaces if s["severity"] == "SEV2" for w in s["watched"]}
    sev1_file = next((w for w in sorted(sev1_tokens) if "/" in w), None)
    sev2_only = sorted(sev2_tokens - sev1_tokens)
    sev2_file = next((w for w in sev2_only if "/" in w), sev2_only[0] if sev2_only else None)
    cases = [
        ("SEV1 synthetic touch (expect BLOCKED rc=2)", [sev1_file], 2),
        ("SEV2-only synthetic touch (expect WARN rc=0)", [sev2_file], 0),
        ("unrelated file (expect clean rc=0)", ["README.md"], 0),
    ]
    fails = []
    for label, files, want in cases:
        print(f"\n--- {label} : {files} ---")
        ns = argparse.Namespace(file=files, mode="blocking", contract_layer=False)
        # selfcheck must not honor a real ack
        saved = os.environ.pop("SURFACE_ACK", None)
        rc = cmd_check(ns)
        if saved is not None:
            os.environ["SURFACE_ACK"] = saved
        ok = rc == want
        print(f"  -> rc={rc} (want {want}) {'PASS' if ok else 'FAIL'}")
        if not ok:
            fails.append(label)
    print("\nSELFCHECK:", "ALL PASS" if not fails else f"FAIL {fails}")
    return 0 if not fails else 1


def cmd_contract_selfcheck(args) -> int:
    """NFRA_GCONTR Phase-3 mandate: synthetic BMKAUD T1 replay. Inject a fake
    `+smartx -> json/benchmarks` WRITES edge into the live graph snapshot with NO
    ratified graph_contracts edit, run Q1+Q2 against a synthetic SEV1 benchmark
    contract, and assert Q2 marks it UNSANCTIONED and WARNS (advisory) -- exit 0,
    NOT exit 2 (advisory ramp). Also asserts the CLEAN baseline (pre-injection)
    does NOT spuriously fire UNSANCTIONED (the WATCH/forbidden distinction). This
    proves the JOIN fires without needing the real (empty) table. Offline-degrade:
    if the live snapshot is unreachable, runs against a fully synthetic graph."""
    import copy
    import datetime as _dt
    try:
        import contract_engine as ce
    except Exception as e:
        print(f"SELFCHECK: contract_engine unavailable ({type(e).__name__}: {e}) -- cannot run.")
        return 1

    SEED = {
        "contract_id": "benchmark-model-portfolios",
        "surface": "critical-surfaces:model_portfolios.benchmark (SEV1)",
        "artifact_keys": ["s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json"],
        "canonical_writer": "yang-pipeline-lambda-role",
        "forbidden_writers": ["smartx-model-monthly-pull", "opal-generate-benchmark-returns",
                              "smartx-ingestion-role", "news-pipeline-role"],
        "ratified_at": "2026-06-15", "active": True, "models": [], "period_defs": {},
        "enforcement": {}, "ratified_by": ["1.0.0_SA_CTO", "2.0.0_SA_COO"],
    }
    try:
        base = ce.load_graph_snapshot("latest")
        src = "live snapshot (latest)"
    except Exception as e:
        print(f"  (live snapshot unreachable: {type(e).__name__}: {e} -- using synthetic graph)")
        base = {"edges": [{"source": "arn:aws:lambda:us-east-1:313476888478:function:yang",
                           "target": "arn:aws:s3:::opal-data-portal-v2", "edge_type": "WRITES",
                           "via_role": "yang-pipeline-lambda-role", "semantic": "capability"}]}
        src = "synthetic graph"
    today = _dt.date.today()

    # T1: inject the +smartx forbidden writer, NO ratified edit in window
    cur = copy.deepcopy(base)
    cur["edges"].append({"source": "arn:aws:lambda:us-east-1:313476888478:function:smartx-monthly",
                         "target": "arn:aws:s3:::opal-data-portal-v2", "edge_type": "WRITES",
                         "via_role": "smartx-model-monthly-pull", "semantic": "capability"})
    q1 = ce.q1_writes_diff(base, cur, [SEED])
    q2 = ce.q2_join([SEED], q1, window=(today, today))
    v = q2["benchmark-model-portfolios"]

    print(f"--- BMKAUD T1 replay (source: {src}) ---")
    print(f"  Q1 +added writers: {[r for r, _ in q1['benchmark-model-portfolios']['added']]}")
    print(f"  Q2 status: {v['status']}  added_forbidden={v['added_forbidden']}")
    fails = []
    # AC1: T1 injection -> UNSANCTIONED
    if v["status"] != "UNSANCTIONED":
        fails.append(f"T1 expected UNSANCTIONED, got {v['status']}")
    # AC2: a contracted SANCTIONED case (ratified edit today) -> SANCTIONED
    SEED_S = dict(SEED, ratified_at=today.isoformat())
    vS = ce.q2_join([SEED_S], q1, window=(today, today))["benchmark-model-portfolios"]
    if vS["status"] != "SANCTIONED":
        fails.append(f"ratified-in-window expected SANCTIONED, got {vS['status']}")
    print(f"  ratified-in-window -> {vS['status']} (expect SANCTIONED)")
    # AC4: the Q2 advisory NEVER changes the surface-check exit code. Prove the
    # contract layer is rc-invariant: cmd_check with contract_layer on vs off must
    # return the SAME rc for the same inputs. Use a SEV1 file in ADVISORY mode (rc
    # 0 without ack -> no SURFACE_ACK audit / ledger writes, i.e. no test
    # pollution) while still exercising the on-path contract layer.
    sev1_file = next((w for s in load_surfaces() if s["severity"] == "SEV1"
                      for w in s["watched"] if "/" in w), None)
    saved_ack = os.environ.pop("SURFACE_ACK", None)  # ensure no real ack leaks in
    try:
        rc_off = cmd_check(argparse.Namespace(file=[sev1_file], mode="advisory", contract_layer=False))
        rc_on = cmd_check(argparse.Namespace(file=[sev1_file], mode="advisory", contract_layer=True))
    finally:
        if saved_ack is not None:
            os.environ["SURFACE_ACK"] = saved_ack
    if rc_off != rc_on:
        fails.append(f"contract layer changed exit code (off={rc_off} on={rc_on}) -- MUST be additive")
    print(f"  rc-invariance (advisory-mode SEV1): contract layer off={rc_off} on={rc_on} (must match)")

    print("\nCONTRACT-SELFCHECK:", "ALL PASS" if not fails else f"FAIL {fails}")
    return 0 if not fails else 1


def main() -> int:
    ap = argparse.ArgumentParser(prog="comp-surface-check")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--file", action="append", default=[])
    c.add_argument("--mode", choices=["blocking", "advisory"], default="blocking")
    c.set_defaults(fn=cmd_check)
    sc = sub.add_parser("scan")
    sc.add_argument("--baseline", default=None, help="baseline graph snapshot (default .comp-graph/baseline.json)")
    sc.add_argument("--current", default=None, help="current graph snapshot (default .comp-graph/graph.json)")
    sc.add_argument("--json", action="store_true")
    sc.set_defaults(fn=cmd_scan)
    lw = sub.add_parser("list-watched-files")
    lw.add_argument("--json", action="store_true")
    lw.set_defaults(fn=cmd_list_watched)
    sub.add_parser("list").set_defaults(fn=cmd_list)
    sub.add_parser("selfcheck").set_defaults(fn=cmd_selfcheck)
    sub.add_parser("contract-selfcheck",
                   help="NFRA_GCONTR Phase-3: synthetic BMKAUD T1 replay -> Q2 UNSANCTIONED + rc-invariance"
                   ).set_defaults(fn=cmd_contract_selfcheck)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
