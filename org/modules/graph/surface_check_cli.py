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
_WS = os.path.dirname(os.path.dirname(_HERE))  # org/modules/graph -> workspace
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
    except Exception:
        pass


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
        ns = argparse.Namespace(file=files, mode="blocking")
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


def main() -> int:
    ap = argparse.ArgumentParser(prog="comp-surface-check")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("--file", action="append", default=[])
    c.add_argument("--mode", choices=["blocking", "advisory"], default="blocking")
    c.set_defaults(fn=cmd_check)
    sub.add_parser("list").set_defaults(fn=cmd_list)
    sub.add_parser("selfcheck").set_defaults(fn=cmd_selfcheck)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
