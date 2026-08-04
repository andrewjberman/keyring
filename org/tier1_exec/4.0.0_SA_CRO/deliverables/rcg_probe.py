"""rcg_probe -- ad-hoc single-file RCG evidence card.

For ANY tracked path, prints on demand: the 27-column feature vector (newest vintage
that carries it), the label chain at last-row-wins (label / confidence / source /
evidence), the latest model's p_archive, and the ACTIVE-axis read (reachability +
mechanical-reference features, the computed half of the PRD s.3 quadrant; the RELEVANT
half stays judgment, which is the point of the probe -- it feeds the judge, it does
not replace them).

Usage: python org/tier1_exec/4.0.0_SA_CRO/deliverables/rcg_probe.py <path> [<path> ...]
Reads committed artifacts only; writes nothing.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve()
WS = HERE.parents[4]


def newest_vintage_with(path: str) -> tuple[str, dict] | tuple[None, None]:
    scans = sorted((d for d in (WS / "rcg" / "scans").iterdir() if d.is_dir()),
                   reverse=True)
    for vd in scans:
        fp = vd / "features.jsonl"
        if not fp.exists():
            continue
        for line in fp.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                if r.get("path") == path:
                    return vd.name, r
    return None, None


def label_chain(path: str) -> list[dict]:
    chain = []
    for line in (WS / "rcg/ledger/LABELS.jsonl").read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            if r.get("path") == path:
                chain.append(r)
    return chain


def latest_prediction(path: str) -> dict | None:
    scans = sorted((d for d in (WS / "rcg" / "scans").iterdir() if d.is_dir()),
                   reverse=True)
    for vd in scans:
        fp = vd / "predictions.jsonl"
        if not fp.exists():
            continue
        for line in fp.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                if r.get("path") == path:
                    return r
    return None


def main() -> int:
    for path in sys.argv[1:]:
        print(f"\n=== {path} ===")
        vintage, feats = newest_vintage_with(path)
        if feats:
            print(f"[features @ vintage {vintage}]")
            for k, v in feats.items():
                if k != "path":
                    print(f"  {k:24s} = {v}")
            active_signals = {
                "reach_from_root": feats.get("reach_from_root"),
                "reach_hops": feats.get("reach_hops"),
                "ref_mech_in_live": feats.get("ref_mech_in_live"),
                "lex_out_live": feats.get("lex_out_live"),
            }
            mech_active = (feats.get("ref_mech_in_live", 0) or 0) > 0 or \
                          (feats.get("reach_from_root", 0) or 0) > 0
            print(f"[ACTIVE axis -- computed] mechanically-referenced/reachable: "
                  f"{'YES' if mech_active else 'NO'} {active_signals}")
            print(f"[recency] last touch {feats.get('t_last_touch_days')}d, "
                  f"age {feats.get('t_age_days')}d, {feats.get('t_commits')} commits / "
                  f"{feats.get('t_author_count')} authors")
        else:
            print("[features] NOT IN ANY VINTAGE (untracked at scan time, or post-scan file "
                  "-- a fresh scan run would compute it)")
        chain = label_chain(path)
        if chain:
            last = chain[-1]
            print(f"[label @ last-row-wins] {last.get('label')} / "
                  f"{last.get('confidence')} / {last.get('source')} "
                  f"({len(chain)} row(s) in chain)")
            if last.get("evidence"):
                print(f"  evidence: {str(last['evidence'])[:220]}")
        else:
            print("[label] UNLABELED")
        pred = latest_prediction(path)
        if pred:
            print(f"[model] p_archive={pred['p_archive']} uncertain={pred['uncertain']} "
                  f"(model {pred['model_version']}) -- ADVISORY: the E-0004 finding stands, "
                  f"the score mirrors training labels; it triages, never decides")
    return 0


if __name__ == "__main__":
    sys.exit(main())
