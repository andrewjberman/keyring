"""E-0004: the first honest prospective eval. Scores BOTH frozen prediction sets
(prior c4259ace + v3 a35ac7af, committed in this dir) against cycle3_adjudication
outcomes -- labels neither model saw at train time. Three denominators, declared:
  FULL      all adjudicated paths both models scored (agreement measure -- models
            trained on the PRIOR labels of most of these, so this is partly fit)
  FLIPS     paths whose adjudicated BINARY differs from the pre-adjudication binary
            (strictly new information -- the honest improvement cut)
  BAND      each model's own uncertain-band members among adjudicated paths (did
            adjudication resolve what the model flagged uncertain)
Adjudicator blinds: NOT administered this cycle (a blind known to the adjudicator is
not a blind; retrofit impossible) -- commissioned to 3.0.0_SA_CVO~B for cycle 4.
Rerun anytime: python eval_e0004.py  (reads only committed artifacts; writes stdout)
"""
from __future__ import annotations
import json
from pathlib import Path

HERE = Path(__file__).parent
WS = HERE.parents[4]
LABELS = WS / "rcg" / "ledger" / "LABELS.jsonl"

adj = {}
for line in LABELS.read_text(encoding="utf-8").splitlines():
    if line.strip():
        r = json.loads(line)
        if r.get("path") and r.get("source") == "cycle3_adjudication":
            adj[r["path"]] = r  # last-row-wins within the source
# pre-adjudication binary = last row BEFORE the cycle3 rows, per path
pre = {}
for line in LABELS.read_text(encoding="utf-8").splitlines():
    if line.strip():
        r = json.loads(line)
        p = r.get("path")
        if p in adj and r.get("source") != "cycle3_adjudication":
            pre[p] = r.get("binary")
print(f"[denominator] cycle3_adjudication outcomes: {len(adj)} paths")

models = {
    "prior_c4259ace": HERE / "predictions_prior_c4259ace.jsonl",
    "v3_a35ac7af": HERE / "predictions_v3_a35ac7af.jsonl",
}
results = {}
for name, fp in models.items():
    preds = {r["path"]: r for r in
             (json.loads(x) for x in fp.read_text(encoding="utf-8").splitlines() if x.strip())}
    common = [p for p in adj if p in preds]
    flips = [p for p in common if pre.get(p) and pre[p] != adj[p].get("binary")]
    band = [p for p in common if preds[p].get("uncertain")]

    def score(paths: list) -> dict:
        tp = fp_ = fn = tn = 0
        p_arch_pos, p_arch_neg = [], []
        for p in paths:
            truth = adj[p].get("binary") == "ARCHIVE_CANDIDATE"
            prob = preds[p]["p_archive"]
            call = prob >= 0.5
            (p_arch_pos if truth else p_arch_neg).append(prob)
            if call and truth:
                tp += 1
            elif call and not truth:
                fp_ += 1
            elif not call and truth:
                fn += 1
            else:
                tn += 1
        n = len(paths)
        return {"n": n, "tp": tp, "fp": fp_, "fn": fn, "tn": tn,
                "accuracy": round((tp + tn) / n, 3) if n else None,
                "mean_p_when_ARCHIVE": round(sum(p_arch_pos) / len(p_arch_pos), 3)
                                        if p_arch_pos else None,
                "mean_p_when_KEEP": round(sum(p_arch_neg) / len(p_arch_neg), 3)
                                     if p_arch_neg else None}

    results[name] = {"FULL": score(common), "FLIPS": score(flips), "BAND": score(band),
                     "flip_paths_n": len(flips), "band_n": len(band)}
    print(f"\n{name}:")
    for cut, s in results[name].items():
        if isinstance(s, dict):
            print(f"  {cut:5s} {s}")

print("\n[declared] FULL is agreement-partly-fit; FLIPS is the honest new-information "
      "cut; blinds deferred to CVO~B at cycle 4.")
if __name__ == "__main__":
    (HERE / "e0004_results.json").write_text(json.dumps(results, indent=1),
                                             encoding="utf-8")
    print(f"results written: {HERE / 'e0004_results.json'}")
