"""RCG stage-C model: CatBoost binary {KEEP, ARCHIVE_CANDIDATE} over the feature matrix.

W1 stage C (PRD s.9; estimator ratified R-0002). Trains on the SEED labels only (v0 --
ratified labels take over as they accrue, W2 stage I), scores every scoreable file, and
emits predictions.jsonl + a model-version stamp. Target space is BINARY by design until
ratifications exist: full disposition classes are never minted from seeds.

EPISTEMIC STATUS (R-0010): every score is OBSERVED (a number from a deterministic run)
wrapping ASSESSED-at-best provenance (seed labels are OBSERVED-derived; future ratified
labels are RATIFIED) -- the stamp carries both, COMPUTED from the run and written to
model_stamp.json beside predictions.jsonl. A score never outranks the grader.

BOUNDARY DECLARATION (printed every run):
  address_space      scoreable rows of the newest vintage carrying features.
  traversal_residue  the model sees ONLY the feature columns -- no content, no context;
                     drift-vs-age caution: age features legitimately inform ARCHIVE
                     probability (dispositions), but the relevance/drift verdict stays
                     the separate computed columns -- read importances, not vibes.
  presentation       predictions.jsonl is the truth; the print is aggregates.
  failure_direction  seed-circularity -- the model learns the seeds' shape, so holdout
                     metrics OVERSTATE real precision until ratified labels arrive
                     (declared; the prospective test at stage F is the honest number).
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

WS = Path(__file__).resolve().parents[2]
CATEGORICAL = ["fs_root", "f_content", "f_class"]
DROP = {"path"}
BAND = (0.35, 0.65)


def newest_scan() -> Path:
    scans = sorted((WS / "rcg" / "scans").glob("*/features.jsonl"))
    if not scans:
        print("BLOCKED: no features vintage -- run the W1 A-B stages first")
        sys.exit(3)
    return scans[-1].parent


def load_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", errors="replace") as h:
        return [json.loads(line) for line in h]


def md5_8(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()[:8]


def main() -> int:
    from catboost import CatBoostClassifier, Pool

    scan_dir = newest_scan()
    rows = load_jsonl(scan_dir / "features.jsonl")
    seeds = {s["path"]: s["label"] for s in load_jsonl(scan_dir / "seed_labels.jsonl")}
    # RATIFIED labels from the ledger DOMINATE seeds (override on conflict, 5x weight):
    # they carry Andrew's rulings / delegation-backed assessments -- the signal seeds
    # structurally lack (E-0001 measured: archive-precision 0.153 on the band without them)
    ratified: dict = {}
    # weights are RULED values, not defaults: andrew 5x (R-0019 authority),
    # delegation 3x (R-0020), cycle3_adjudication 3x (CTO~B ack 20260804T135024Z,
    # parity-with-delegation, revisit at cycle-4 once E-0004 calibration exists).
    # An UNKNOWN source falls to 2.0 AND is reported in the per-source census below --
    # a silent default is how an acked weight fails to reach the trainer.
    # CTO~B ruling 20260804T145728Z -- weight follows the WARRANT'S ORIGIN, not the
    # writing hand: rows that mechanically RESTORE Andrew-ratified verdicts carry his
    # weight class (precedence_correction 5.0); rows that ADD verified agent judgment
    # carry the adjudication class (coherence_correction 3.0). CALIBRATION FLAG: the
    # 4,110-row 2.0->5.0 shift is KEEP-mass -- watch archive-recall at the next eval.
    src_weight = {"andrew_ratification": 5.0, "assessed_ratified_by_delegation": 3.0,
                  "cycle3_adjudication": 3.0, "precedence_correction": 5.0,
                  "coherence_correction": 3.0}
    rat_w: dict = {}
    src_census: dict = {}
    ledger = WS / "rcg" / "ledger" / "LABELS.jsonl"
    if ledger.exists():
        for r in load_jsonl(ledger):
            if r.get("binary") in ("KEEP", "ARCHIVE_CANDIDATE"):
                ratified[r["path"]] = r["binary"]
                src = r.get("source", "")
                rat_w[r["path"]] = src_weight.get(src, 2.0)
                key = f"{src}@{src_weight.get(src, 2.0)}" + \
                      ("" if src in src_weight else " (DEFAULT -- unruled source)")
                src_census[key] = src_census.get(key, 0) + 1
    seeds = {**seeds, **ratified}
    print("[model] per-source label census (weight applied): " +
          ", ".join(f"{k}={v}" for k, v in sorted(src_census.items())))

    # TRAINING POOL: newest features per path across ALL scan vintages -- NOT just the
    # newest scan. Ratified labels on since-deleted files are the best-confirmed
    # positives (the 2026-08-04 sweep removed 2,940 = 34% of the ARCHIVE class), and a
    # post-sweep rescan carries no features for them: training only on the newest
    # vintage would silently drop them, wasting the ratification compute. Later
    # vintages win per path; scoring stays newest-vintage-only (rows) below.
    train_pool_by_path: dict = {}
    n_vintages = 0
    for vd in sorted(d for d in (WS / "rcg" / "scans").iterdir() if d.is_dir()):
        fp = vd / "features.jsonl"
        if fp.exists():
            n_vintages += 1
            for r in load_jsonl(fp):
                train_pool_by_path[r["path"]] = r
    n_resurrected = sum(1 for p in train_pool_by_path
                        if p not in {r["path"] for r in rows})
    print(f"[model] training pool: {len(train_pool_by_path)} paths across {n_vintages} "
          f"vintages ({n_resurrected} retained from older vintages only -- deleted or "
          f"pre-rescan files whose labels stay trainable)")

    # VINTAGE GRAIN (RCG-D4): this read the LIVE head and stamped it on scores computed
    # from a PINNED scan vintage. Caught 2026-09-16 the only way it can be -- another
    # seat committed between the scan and the score, so the stamp read head=6328a6fb
    # over a population measured at af7ee8fc, and every prediction claimed to describe
    # a commit it had never seen. When the two agree the defect is invisible, which is
    # the usual case and why it survived. `head` is now the VINTAGE's -- the repo state
    # the scores actually describe -- and the live head rides beside it as run_head.
    run_head = subprocess.run(["git", "rev-parse", "--short=8", "HEAD"], cwd=WS,
                              capture_output=True, text=True).stdout.strip()
    head = scan_dir.name.rsplit("_", 1)[-1]
    if head != run_head:
        print(f"[model] WARNING: scoring vintage {scan_dir.name} (head {head}) while the "
              f"worktree is at {run_head} -- the scores describe {head}. Re-run "
              "rcg/bin/scan.py to score the current tree.")
    # PROVENANCE (RCG-D3): label_provenance was the HARDCODED STRING
    # "seed-only (OBSERVED-derived; zero RATIFIED yet)" -- true only at cycle 0, and
    # false from the first ratification onward. Measured 2026-09-16 on vintage
    # 20260916T033918Z_af7ee8fc: the SAME run printed "ratified labels folded: 17537"
    # two lines below the stamp claiming zero. The docstring above promises the stamp
    # "carries both"; it carried neither. It is now COMPUTED from the run.
    # Second half of the same hole: labels_md5 hashed seed_labels.jsonl ONLY, so two
    # runs over DIFFERENT ratified ledgers stamped identically. LABELS.jsonl is now
    # hashed on its own line.
    n_ratified = len(ratified)
    version = {"cycle": 0, "head": head,
               "labels_md5": md5_8(scan_dir / "seed_labels.jsonl"),
               "ratified_labels_md5": md5_8(ledger) if ledger.exists() else "ABSENT",
               "n_ratified_folded": n_ratified,
               "run_head": run_head, "head_drifted_from_run": head != run_head,
               "rulings_md5": md5_8(WS / "rcg" / "rulings" / "RULINGS.jsonl"),
               "label_provenance": (
                   "seed-only (OBSERVED-derived; zero RATIFIED)" if not n_ratified else
                   f"MIXED: {n_ratified} RATIFIED rows fold over the seeds and win on "
                   "conflict (weights per the source census above); the remainder is "
                   "OBSERVED-derived seed")}
    # The stamp is PERSISTED beside the predictions it describes -- a stamp that only
    # ever reached stdout could not be read back off the artifact.
    (scan_dir / "model_stamp.json").write_text(json.dumps(version, indent=1),
                                               encoding="utf-8")

    cols = [k for k in rows[0] if k not in DROP]

    def matrix(subset: list[dict]) -> list[list]:
        out = []
        for r in subset:
            vec = []
            for c in cols:
                v = r.get(c)  # older-vintage rows may lack newer feature columns
                if c in CATEGORICAL:
                    vec.append(str(v))
                else:
                    vec.append(float(v) if v is not None else -1.0)
            out.append(vec)
        return out

    n_rat = sum(1 for p2 in ratified if p2 in train_pool_by_path)
    print(f"[model] ratified labels folded: {len(ratified)} ({n_rat} with features in the "
          f"training pool), per-source weights above")
    weights = rat_w
    train_rows = [r for r in train_pool_by_path.values() if r["path"] in seeds]
    y = [1 if seeds[r["path"]] == "ARCHIVE_CANDIDATE" else 0 for r in train_rows]
    cat_idx = [cols.index(c) for c in CATEGORICAL]
    n_pos = sum(y)
    print(f"[model] vintage {scan_dir.name}; version {version}")
    print(f"[model] seeds {len(train_rows)} (ARCHIVE {n_pos} / KEEP {len(y) - n_pos}); "
          f"features {len(cols)} ({len(CATEGORICAL)} categorical)")

    # sanity holdout (stratified 80/20) -- OVERSTATES per boundary declaration
    tr_x, tr_y, ho_x, ho_y = [], [], [], []
    counters = {0: 0, 1: 0}
    for r, label in zip(train_rows, y):
        counters[label] += 1
        (ho_x if counters[label] % 5 == 0 else tr_x).append(r)
        (ho_y if counters[label] % 5 == 0 else tr_y).append(label)
    clf = CatBoostClassifier(iterations=300, depth=6, random_seed=17,
                             auto_class_weights="Balanced", verbose=0)
    clf.fit(Pool(matrix(tr_x), tr_y, cat_features=cat_idx))
    pred = clf.predict(matrix(ho_x))
    tp = sum(1 for p, t in zip(pred, ho_y) if p == 1 and t == 1)
    fp = sum(1 for p, t in zip(pred, ho_y) if p == 1 and t == 0)
    fn = sum(1 for p, t in zip(pred, ho_y) if p == 0 and t == 1)
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    print(f"[model] seed-holdout sanity (n={len(ho_y)}): ARCHIVE precision "
          f"{prec:.3f} recall {rec:.3f} -- OVERSTATES, see boundary")

    # final fit on all seeds; score everything
    clf = CatBoostClassifier(iterations=300, depth=6, random_seed=17,
                             auto_class_weights="Balanced", verbose=0)
    w = [weights.get(r["path"], 1.0) for r in train_rows]
    clf.fit(Pool(matrix(train_rows), y, cat_features=cat_idx, weight=w))
    (WS / "rcg" / "models").mkdir(exist_ok=True)
    clf.save_model(str(WS / "rcg" / "models" / f"rcg_v0_{head}.cbm"))
    probs = clf.predict_proba(matrix(rows))
    n_band = 0
    with (scan_dir / "predictions.jsonl").open("w", encoding="utf-8", newline="\n") as h:
        for r, p in zip(rows, probs):
            p_arch = round(float(p[1]), 4)
            band = BAND[0] <= p_arch <= BAND[1]
            n_band += band
            h.write(json.dumps({"path": r["path"], "p_archive": p_arch,
                                "uncertain": band, "seed": seeds.get(r["path"]),
                                # head-only BY DESIGN: the frozen E-0004 prior
                                # (deliverables/E0004_FROZEN/predictions_prior_
                                # c4259ace.jsonl) keys on this shape, so widening the
                                # field would break that comparison. The full stamp
                                # lives in model_stamp.json beside this file.
                                "model_version": version["head"]}) + "\n")

    imp = sorted(zip(cols, clf.get_feature_importance()), key=lambda x: -x[1])[:8]
    print("[model] top importances: " + ", ".join(f"{c}={v:.1f}" for c, v in imp))
    non_seed = [(r["path"], float(p[1])) for r, p in zip(rows, probs)
                if r["path"] not in seeds]
    hi_arch = sorted(non_seed, key=lambda x: -x[1])[:12]
    print(f"[model] scored {len(rows)}; uncertain band {n_band}; top NON-SEED archive "
          f"candidates:")
    for path, p in hi_arch:
        print(f"    p={p:.3f}  {path}")
    print("[boundary] " + __doc__.split("BOUNDARY DECLARATION", 1)[1].strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
