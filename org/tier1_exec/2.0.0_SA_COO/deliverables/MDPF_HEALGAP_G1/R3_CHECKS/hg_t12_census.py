"""MDPF_HEALGAP round 3, HG-t-12 (FWD-6, PRD v0.3): the re-sweep census of scheduled pulls whose login is kept alive elsewhere.

Reads org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~9/FWD6_CENSUS_RESWEEP_R3.md and requires:
  - a line `DENOMINATOR: <n> scheduled pulls read` and a line `FRESH-COUNT: <m> scheduled pulls via <command>` with
    <n> == <m> (the census is counted against a fresh count of every scheduled pull, not the round-2 figure of 162);
  - a markdown table whose header names `pull`, `schedule`, `login kept alive by`, `answer`, `grounding`, `person's act`, `listed on`;
  - every row's `answer` is exactly `RECOVERS`, `NOT-EXPOSED because <reason>` or `EXPOSED-MANUAL because <reason>`;
  - an `EXPOSED-MANUAL` row names the person's act and where it is listed when owed (both cells non-empty);
  - rows for each of: schwab-canonical-si2-08403355-pull-daily, teams-global-transcripts-pull-hourly,
    canonical-schwab-si2-08242234-daily-pull, canonical-schwab-si2-08335338-daily-pull, astn-wsjft-3am-run,
    bd-asset-dim-pipeline-trigger, cot-rebalancer-runner; the 49F login chain's pull FIRST;
  - every row's `grounding` non-empty and <n> >= the row count.
Last line: CENSUS-OK rows=<r> denominator=<n> exposed_manual=<k>, or CENSUS-BAD <reasons>. Completeness of the population is the
CVO's judgment; this check is the shape.
"""
from __future__ import annotations

import os
import re
import sys

DOC = os.environ.get("HG_T12_DOC") or os.path.join(
    "org", "missions", "D8", "MDPF", "MDPF_HEALGAP", "deliverables", "0.9.0_WK_MDPF_HEALGAP~9", "FWD6_CENSUS_RESWEEP_R3.md")
COLS = ["pull", "schedule", "login kept alive by", "answer", "grounding", "person's act", "listed on"]
NAMED = ["schwab-canonical-si2-08403355-pull-daily", "teams-global-transcripts-pull-hourly",
         "canonical-schwab-si2-08242234-daily-pull", "canonical-schwab-si2-08335338-daily-pull", "astn-wsjft-3am-run",
         "bd-asset-dim-pipeline-trigger", "cot-rebalancer-runner"]


def main() -> int:
    if not os.path.isfile(DOC):
        print("CENSUS-BAD no file " + DOC)
        return 1
    text = open(DOC, encoding="utf-8").read()
    bad = []
    md = re.search(r"^DENOMINATOR:\s*(\d+) scheduled pulls read", text, re.M)
    mf = re.search(r"^FRESH-COUNT:\s*(\d+) scheduled pulls via \S", text, re.M)
    if not md:
        bad.append("no 'DENOMINATOR: <n> scheduled pulls read' line")
    if not mf:
        bad.append("no 'FRESH-COUNT: <m> scheduled pulls via <command>' line")
    if md and mf and md.group(1) != mf.group(1):
        bad.append("denominator %s != fresh count %s" % (md.group(1), mf.group(1)))
    lines = [ln for ln in text.splitlines() if ln.strip().startswith("|")]
    hdr_i = next((i for i, ln in enumerate(lines) if all(c in ln.lower() for c in COLS)), None)
    if hdr_i is None:
        print("CENSUS-BAD " + "; ".join(bad + ["no table header naming " + ", ".join(COLS)]))
        return 1
    hdr = [c.strip().lower() for c in lines[hdr_i].strip().strip("|").split("|")]
    idx = {c: next(i for i, h in enumerate(hdr) if c in h) for c in COLS}
    rows = []
    for ln in lines[hdr_i + 1:]:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):
            continue
        rows.append(cells)
    if not rows:
        print("CENSUS-BAD " + "; ".join(bad + ["table has no rows"]))
        return 1
    manual = 0
    for r in rows:
        if len(r) < len(hdr):
            bad.append("short row %r" % r[:1])
            continue
        name, ans = r[idx["pull"]][:50], r[idx["answer"]]
        if not (ans == "RECOVERS" or re.match(r"(NOT-EXPOSED|EXPOSED-MANUAL) because \S", ans)):
            bad.append("row %r answer %r" % (name, ans[:40]))
        if ans.startswith("EXPOSED-MANUAL"):
            manual += 1
            if not r[idx["person's act"]] or not r[idx["listed on"]]:
                bad.append("row %r is EXPOSED-MANUAL without the person's act and where it is listed" % name)
        if not r[idx["grounding"]]:
            bad.append("row %r has no grounding" % name)
    first = rows[0][idx["pull"]].lower() + " " + rows[0][idx["login kept alive by"]].lower()
    if "49f" not in first:
        bad.append("first row is not the 49F login chain")
    for n in NAMED:
        if not any(n in r[idx["pull"]] for r in rows if len(r) >= len(hdr)):
            bad.append("no row for " + n)
    if md and int(md.group(1)) < len(rows):
        bad.append("denominator %s < rows %d" % (md.group(1), len(rows)))
    if bad:
        print("CENSUS-BAD " + "; ".join(bad))
        return 1
    print("CENSUS-OK rows=%d denominator=%s exposed_manual=%d" % (len(rows), md.group(1), manual))
    return 0


if __name__ == "__main__":
    sys.exit(main())
