"""RCG stage-E packet assembler: the review session, built from the scored vintage.

W1 stage E (PRD s.9). Deterministic assembly of what Andrew sees at stage F: cohort-
ordered candidate groups with evidence-card data, DISAGREEMENTS FIRST, planted controls
checked before anything ships. The packet is a MEASUREMENT (scans/<vintage>/packet.md,
local-only); RATIFIED outcomes -- not the packet -- land in the ledger.

Sections, in order:
  S1 DISAGREEMENTS  -- instruments contradict each other (model-vs-activity,
                       dead-marker-vs-marked, seed-vs-score). Highest review value.
  S2 UNCERTAIN BAND -- the stage-D grader queue, cohort-grouped.
  S3 ARCHIVE COHORTS-- non-seed high-confidence archive proposals, cohort-grouped.
  S4 CONTROLS       -- >=2 known-cruft + >=2 known-canonical planted; A MISGRADED
                       CONTROL QUARANTINES THE PACKET (rc=2, nothing ships) -- W1 HALT
                       rule, the known_negative law in executable form.

BOUNDARY DECLARATION (printed every run):
  address_space      the newest vintage's scored rows; cohorts are directory-prefix
                     groups (first 3 path components) -- a MECHANICAL prior, not a
                     semantic one; the grader may split/merge cohorts at stage D.
  traversal_residue  cards carry up to 3 citing referrers per file (cap, declared);
                     control selection is deterministic (md5 order), so a control set
                     is stable per vintage -- an adversary who reads the code can name
                     the controls (acceptable: the operator IS the grader in R-0001
                     solo posture; revisit at multi-agent staffing).
  presentation       packet.md is the session document; this print is the assembly log.
  failure_direction  a packet ships ONLY on 4/4 controls -- fail direction is a LOUD
                     quarantine, never a silently thinner packet.
"""
from __future__ import annotations

import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

WS = Path(__file__).resolve().parents[2]
BAND = (0.35, 0.65)


def newest_scan() -> Path:
    scans = sorted((WS / "rcg" / "scans").glob("*/predictions.jsonl"))
    if not scans:
        print("BLOCKED: no scored vintage -- run model.py first")
        sys.exit(3)
    return scans[-1].parent


def load_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", errors="replace") as h:
        return [json.loads(line) for line in h]


def cohort_key(path: str) -> str:
    return "/".join(path.split("/")[:3])


def main() -> int:
    scan_dir = newest_scan()
    feats = {r["path"]: r for r in load_jsonl(scan_dir / "features.jsonl")}
    preds = {r["path"]: r for r in load_jsonl(scan_dir / "predictions.jsonl")}
    seeds = {s["path"]: s["label"] for s in load_jsonl(scan_dir / "seed_labels.jsonl")}
    referrers: dict = defaultdict(list)
    for e in load_jsonl(scan_dir / "edges.jsonl"):
        for dst in e["dst"]:
            if len(referrers[dst]) < 3:
                referrers[dst].append(e["src"])

    # S4 first -- controls gate everything (deterministic selection, md5 order)
    def pick(label: str, n: int) -> list[str]:
        pool = sorted((p for p, s in seeds.items() if s == label),
                      key=lambda p: hashlib.md5(p.encode()).hexdigest())
        return pool[:n]

    controls = [(p, "ARCHIVE_CANDIDATE") for p in pick("ARCHIVE_CANDIDATE", 2)] + \
               [(p, "KEEP") for p in pick("KEEP", 2)]
    failures = []
    for p, truth in controls:
        p_arch = preds[p]["p_archive"]
        got = "ARCHIVE_CANDIDATE" if p_arch > 0.5 else "KEEP"
        if got != truth:
            failures.append((p, truth, p_arch))
    if failures:
        print(f"[packet] QUARANTINE -- {len(failures)}/4 planted controls misgraded; "
              f"NOTHING SHIPS:")
        for p, truth, p_arch in failures:
            print(f"    {p} truth={truth} p_archive={p_arch}")
        return 2

    # S1 disagreements -- instruments contradicting each other
    s1 = []
    for p, f in feats.items():
        pr = preds[p]
        if p in seeds:
            if (seeds[p] == "KEEP") != (pr["p_archive"] < 0.5):
                s1.append((p, f"seed={seeds[p]} vs p_archive={pr['p_archive']}"))
            continue
        if f["reach_from_root"] and pr["p_archive"] > 0.8:
            s1.append((p, f"ACTIVE (hops={f['reach_hops']}, in={f['ref_mech_in_live']}) "
                          f"yet p_archive={pr['p_archive']} -- MIGRATE-shaped"))
        elif f["s_dead_marker"] and f["reach_from_root"]:
            s1.append((p, "declared-dead header yet reach-marked -- load-bearing legacy"))

    # S2 uncertain band + S3 high-confidence archive, cohort-grouped
    def cohortize(paths: list[str]) -> list[tuple]:
        groups: dict = defaultdict(list)
        for p in paths:
            groups[cohort_key(p)].append(p)
        return sorted(groups.items(), key=lambda kv: -len(kv[1]))

    band_paths = [p for p, pr in preds.items() if pr["uncertain"] and p not in seeds]
    arch_paths = [p for p, pr in preds.items()
                  if pr["p_archive"] > 0.9 and p not in seeds]
    s2, s3 = cohortize(band_paths), cohortize(arch_paths)

    def card(p: str) -> str:
        f, pr = feats[p], preds[p]
        refs = "; ".join(referrers.get(p, [])) or "none-found"
        return (f"    {p}\n      p_archive={pr['p_archive']} active={bool(f['reach_from_root'])} "
                f"in={f['ref_mech_in_live']} dangling={f['ref_dangling_out']} "
                f"last_touch={f['t_last_touch_days']}d cc_div={f['co_change_divergence']} "
                f"lex_ret={f['lex_retired_ratio']} nonconf={f['lex_canon_nonconform']}\n"
                f"      cited_by[OBSERVED]: {refs}")

    lines = [f"# RCG REVIEW PACKET -- vintage {scan_dir.name}",
             f"model {preds[next(iter(preds))]['model_version']} | controls 4/4 PASS | "
             f"epistemic: all machine columns OBSERVED; proposals arrive ASSESSED at "
             f"stage D; nothing here is RATIFIED until stage F",
             f"\n## S1 DISAGREEMENTS ({len(s1)}) -- review these first"]
    for p, why in sorted(s1)[:40]:
        lines.append(f"  {p}\n      {why}")
    lines.append(f"\n## S2 UNCERTAIN BAND ({len(band_paths)} files, {len(s2)} cohorts)")
    for key, members in s2[:15]:
        lines.append(f"  COHORT {key} ({len(members)} files)")
        lines.append(card(sorted(members)[0]))
    lines.append(f"\n## S3 ARCHIVE PROPOSALS ({len(arch_paths)} files, {len(s3)} cohorts)")
    for key, members in s3[:15]:
        lines.append(f"  COHORT {key} ({len(members)} files)")
        lines.append(card(sorted(members)[0]))
    lines.append("\n## S4 CONTROLS (4/4 PASS, identities logged to assembly output only)")
    (scan_dir / "packet.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[packet] vintage {scan_dir.name}: S1 disagreements {len(s1)} | S2 band "
          f"{len(band_paths)} files / {len(s2)} cohorts | S3 archive {len(arch_paths)} "
          f"files / {len(s3)} cohorts | controls 4/4 PASS "
          f"({', '.join(p for p, _ in controls)})")
    print(f"[packet] wrote {scan_dir.name}/packet.md (LOCAL -- ratified outcomes go to "
          f"the ledger, never the packet)")
    print("[boundary] " + __doc__.split("BOUNDARY DECLARATION", 1)[1].strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
