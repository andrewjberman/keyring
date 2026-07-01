"""
comp-rail-audit -- NFRA_COMPRAIL post-enforce telemetry + broad-grep-tier FP/TP audit (TO-5, the close TO).

The rail (comp-which-first, the FIRES verb) is LIVE + enforcing. This reads the enforce-window rail-log
(org/mcp/comp-which-rail.log) and answers the two COMPRAIL close questions:
  1. TELEMETRY -- are agents finding the rail? Route-vs-on-rails-run-vs-deny-vs-override distribution +
     repeat-override CLASSES (each repeat = a coverage-gap signal -> a tool to build, feeds COMPLEARN).
  2. BROAD-GREP-TIER FP/TP -- the staged broad-repo-grep DENY tier: would it deny LEGITIMATE broad
     searches? Classifies each DENY/OVERRIDE q as rail-FP-overmatch (an echo/cd/comment the matcher
     wrongly caught), legit-raw (a raw-text need no comp-tool replaces), or should-route (a search a
     comp-tool covers = a TRUE positive the tier would correctly catch). Quantifies the FP rate ->
     a GO / HOLD / NO-GO recommendation (the enablement is a COO+CVO call -- this only RECOMMENDS).

The parsed rail rows (tool_activity's parse_rail) drop the class= + q= fields for DENY/OVERRIDE, so this
re-parses the raw log to recover them -- the intent-level signal the class-level audit needs.

Read-only, deterministic, no settings change (the broad-grep enablement is COO+CVO-gated). Lane-portable,
ASCII. Reuses NFRA_COMPLEARN framing (a repeat-override class IS a routing-miss/build-new candidate).

Usage:
    comp-rail-audit                      # the full telemetry + FP/TP report + recommendation
    comp-rail-audit --json               # machine-readable
    comp-rail-audit --window <ISO>       # only rows at/after this timestamp (enforce sub-window)

Author: 0.8.0_AE_CloudComp~E (NFRA_COMPRAIL TO-5). 2026-07-01.
Spec: docs/architecture/NFRA_COMPRAIL_PRD.md + the TO-5 task order.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict

_WS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
RAIL_LOG = "org/mcp/comp-which-rail.log"

_VALID_ACTIONS = {"ROUTE", "ROUTE-SURFACE", "RUN-GREP", "RUN-GLOB", "RUN-LS", "DENY", "RUN-OVERRIDE"}
_LINE = re.compile(r"^(?P<ts>\S+)\s+(?P<action>[A-Z-]+)\s+(?P<rest>.*)$")
_KV = re.compile(r"(\w+)=")

# The broad-repo-grep tier governs a raw repo GREP/FIND INVOCATION -- not aws commands (that's tier-1,
# already live) and not a pipe-CONSUMER (`cmd | grep`, which CLAUDE.md keeps FREE). So the FP/TP is
# scoped to governed-grep commands only.
_GREP_INVOKE_RX = re.compile(r"(?:^|&&|;|\|\||\bthen\b|\bdo\b)\s*(?:sudo\s+)?(grep|egrep|fgrep|rg|find)\b")
_PIPE_CONSUMER_RX = re.compile(r"\|\s*(?:grep|egrep|fgrep|rg|awk|sed)\b")   # filtering output, not a repo search
# A governed-grep that is LEGITIMATE raw (FP if blocked): reads literal file TEXT / format-sampling
# (a comp-tool gives a MODELED view, not the raw bytes) -- the agent's own rail-checked reason confirms.
_RAWTEXT_RX = re.compile(r"rail-checked:.*(raw text|literal|exact string|format|sampl|byte|verbatim|content)", re.I)


def parse_raw_rail(path: str = "", window: str = "") -> list:
    """Re-parse the raw rail-log recovering the class= + q= fields (which parse_rail drops for
    DENY/OVERRIDE). Returns rows: {ts, action, tool, class, q, intent, term}."""
    p = path or os.path.join(_WS, RAIL_LOG)
    rows: list = []
    if not os.path.exists(p):
        return rows
    with open(p, encoding="utf-8", errors="replace") as fh:
        for ln in fh:
            m = _LINE.match(ln.rstrip("\n"))
            if not m or m.group("action") not in _VALID_ACTIONS:
                continue
            ts = m.group("ts")
            if window and ts < window:
                continue
            rest = m.group("rest")
            row = {"ts": ts, "action": m.group("action"), "raw": rest}
            # split rest into key=value fields; q= is greedy-to-end (it can contain spaces + '=').
            qpos = rest.find("q=")
            head = rest[:qpos] if qpos >= 0 else rest
            for kv in re.finditer(r"(\w+)=(\S+)", head):
                row[kv.group(1)] = kv.group(2)
            if qpos >= 0:
                row["q"] = rest[qpos + 2:].strip().strip('"')
            rows.append(row)
    return rows


def is_governed_grep(q: str) -> bool:
    """Would the broad-repo-grep tier govern this command? True iff it INVOKES grep/find/rg over the
    repo (not a pipe-consumer filtering command output, which stays free)."""
    if not q:
        return False
    if not _GREP_INVOKE_RX.search(q):
        return False
    # a command whose ONLY grep is a pipe-consumer (`aws ... | grep x`) is NOT a repo search -> not governed.
    if _PIPE_CONSUMER_RX.search(q) and not re.search(r"(?:^|&&|;|\bthen\b|\bdo\b)\s*(?:sudo\s+)?(?:grep|egrep|fgrep|rg|find)\b", q):
        return False
    return True


def classify_governed_grep(row: dict) -> str:
    """Classify a GOVERNED-GREP DENY/OVERRIDE for the broad-grep-tier FP/TP:
      - 'legit_raw'    : reads literal file TEXT / format (a comp-tool gives a modeled view, not raw
                         bytes) -- the agent's rail-checked reason confirms -> blocking = friction (FP).
      - 'should_route' : a symbol / dependency / resource search a comp-tool covers -> TRUE positive
                         (the tier would correctly redirect it to comp-grep/comp-blast/comp-symbols).
    Conservative: ambiguous -> should_route, so the FP rate is not UNDER-stated (a friction gate must
    not hide friction)."""
    q = row.get("q", "") or ""
    if _RAWTEXT_RX.search(q):
        return "legit_raw"
    return "should_route"


def audit(window: str = "") -> dict:
    rows = parse_raw_rail(window=window)
    acts = Counter(r["action"] for r in rows)
    total = sum(acts.values())
    routes = acts["ROUTE"] + acts["ROUTE-SURFACE"]
    on_rails_runs = acts["RUN-GREP"] + acts["RUN-GLOB"] + acts["RUN-LS"]   # comp-grep/comp-glob (sanctioned)
    denies = acts["DENY"]
    overrides = acts["RUN-OVERRIDE"]

    # coverage-gap signal: repeat DENY/OVERRIDE by CLASS (a class hit many times = a demand cluster).
    by_class = defaultdict(lambda: {"deny": 0, "override": 0})
    for r in rows:
        if r["action"] == "DENY":
            by_class[r.get("class", "?")]["deny"] += 1
        elif r["action"] == "RUN-OVERRIDE":
            by_class[r.get("class", "?")]["override"] += 1

    # broad-grep-tier FP/TP: scope to GOVERNED-GREP commands only (the tier governs repo grep/find, NOT
    # aws inspection [tier-1, already live] and NOT pipe-consumers [free]). nudge-adoption = the RUN-GREP/
    # RUN-GLOB on-rails comp-grep/comp-glob runs (agents already using the sanctioned tool via the NUDGE).
    blocks = [r for r in rows if r["action"] in ("DENY", "RUN-OVERRIDE")]
    governed = [r for r in blocks if is_governed_grep(r.get("q", ""))]
    buckets = Counter(classify_governed_grep(r) for r in governed)
    legit, tp = buckets["legit_raw"], buckets["should_route"]
    fp_rate = legit / (legit + tp) if (legit + tp) else 0.0

    ts = sorted(r["ts"] for r in rows if r.get("ts"))
    return {
        "window": {"from": ts[0] if ts else None, "to": ts[-1] if ts else None, "rows": total},
        "telemetry": {
            "action_distribution": dict(acts.most_common()),
            "route_rate": round(routes / total, 3) if total else 0.0,
            "on_rails_run_rate": round(on_rails_runs / total, 3) if total else 0.0,
            "deny_rate": round(denies / total, 3) if total else 0.0,
            "override_rate": round(overrides / total, 3) if total else 0.0,
            "rail_found_rate": round((routes + on_rails_runs) / total, 3) if total else 0.0,
        },
        "coverage_gaps": sorted(
            [{"class": c, **v, "total": v["deny"] + v["override"]} for c, v in by_class.items()],
            key=lambda d: -d["total"])[:12],
        "broad_grep_fp_tp": {
            "governed_grep_blocks": len(governed),
            "total_deny_override_blocks": len(blocks),
            "scope_note": "repo grep/find INVOCATIONS only -- aws inspection = tier-1 (already live), "
                          "pipe-consumers (`cmd | grep`) = free",
            "legit_raw_FP": legit,
            "should_route_TP": tp,
            "fp_rate": round(fp_rate, 3),
            "nudge_adoption_comp_grep_runs": on_rails_runs,
        },
        "recommendation": _recommend(fp_rate, len(governed), on_rails_runs, by_class),
    }


def _recommend(fp_rate: float, governed_n: int, nudge_adoption: int, by_class: dict) -> dict:
    """GO / HOLD / NO-GO for the broad-repo-grep DENY tier, grounded on (a) the grep-scoped FP rate,
    (b) whether there is ENOUGH broad-grep data to judge, and (c) the NUDGE already working. A HOLD
    (tier stays staged-by-design, gaps -> COMPLEARN) is a VALID close, not a failure."""
    gap_classes = [c for c, v in by_class.items() if (v["deny"] + v["override"]) >= 3 and c != "?"]
    if governed_n < 30:
        rec = "HOLD"
        why = (f"Only {governed_n} governed repo-grep DENY/OVERRIDE events in the enforce window -- the "
               f"broad repo-grep is currently NUDGED, not denied, so there is NO direct broad-tier FP "
               f"evidence. Enabling a hard fabric-wide DENY off <30 data points would be flying blind. "
               f"And the NUDGE is already working: {nudge_adoption} comp-grep/comp-glob on-rails runs -- "
               f"agents adopt the sanctioned tool when nudged, achieving most of the tier's goal WITHOUT "
               f"the hard-deny friction. Keep the tier STAGED-BY-DESIGN; route the coverage-gap classes "
               f"to COMPLEARN as build-next/routing candidates. This is a grounded close.")
    elif fp_rate >= 0.3:
        rec = "HOLD"
        why = (f"grep-scoped FP rate {fp_rate:.0%} -- a broad DENY would block too many legitimate raw-"
               f"text/format reads. Coverage insufficient; keep STAGED, feed gaps to COMPLEARN.")
    else:
        rec = "GO"
        why = (f"grep-scoped FP rate {fp_rate:.0%} is low over {governed_n} governed events -- the tier "
               f"would route far more than it wrongly blocks. Recommend enabling (COO+CVO gate the change).")
    return {"verdict": rec, "rationale": why,
            "gate": "COO+CVO decide the settings-matcher change; this audit is ADVISORY only",
            "gap_classes_to_build": gap_classes}


def render(a: dict) -> str:
    t = a["telemetry"]
    L = ["=== comp-rail-audit -- NFRA_COMPRAIL post-enforce telemetry + broad-grep-tier FP/TP (TO-5) ===",
         f"enforce window: {a['window']['from']} -> {a['window']['to']}  ({a['window']['rows']} rail events)",
         "",
         "TELEMETRY -- are agents finding the rail?",
         f"  rail-found rate: {t['rail_found_rate']:.0%}  (route {t['route_rate']:.0%} + on-rails-run {t['on_rails_run_rate']:.0%})",
         f"  deny rate:       {t['deny_rate']:.0%}    override rate: {t['override_rate']:.0%}",
         f"  actions: {t['action_distribution']}",
         "",
         "COVERAGE GAPS -- repeat DENY/OVERRIDE by class (each repeat = a build-next/routing candidate -> COMPLEARN):"]
    for g in a["coverage_gaps"]:
        L.append(f"  {g['class']:20s} deny={g['deny']:4d} override={g['override']:3d} total={g['total']:4d}")
    fp = a["broad_grep_fp_tp"]
    L += ["",
          "BROAD-REPO-GREP TIER -- FP/TP (would it block legitimate repo searches?):",
          f"  governed repo-grep blocks: {fp['governed_grep_blocks']} of {fp['total_deny_override_blocks']} deny/override",
          f"    ({fp['scope_note']})",
          f"  legit-raw (raw-text/format read -- FP if blocked):      {fp['legit_raw_FP']}",
          f"  should-route (a comp-tool covers it -- TRUE positive):  {fp['should_route_TP']}",
          f"  => grep FP RATE: {fp['fp_rate']:.0%}",
          f"  NUDGE adoption: {fp['nudge_adoption_comp_grep_runs']} comp-grep/comp-glob on-rails runs "
          f"(agents use the sanctioned tool when nudged)",
          "",
          f"RECOMMENDATION: {a['recommendation']['verdict']}",
          f"  {a['recommendation']['rationale']}",
          f"  gate: {a['recommendation']['gate']}"]
    if a["recommendation"]["gap_classes_to_build"]:
        L.append(f"  gap classes -> COMPLEARN: {', '.join(a['recommendation']['gap_classes_to_build'])}")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="comp-rail-audit -- NFRA_COMPRAIL post-enforce telemetry + FP/TP (TO-5)")
    ap.add_argument("--window", default="", help="only rows at/after this ISO timestamp")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()
    a = audit(window=args.window)
    print(json.dumps(a, indent=2) if args.json else render(a))
    return 0


if __name__ == "__main__":
    sys.exit(main())
