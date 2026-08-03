# W2 -- rcg_post_review (procedure contract, v1)

Everything AFTER an Andrew session. Fully deterministic. Runs before the next W1 of the
same sub-scan.

| Stage | Program | Output |
|---|---|---|
| G ingest | bin/post_review.py ingest | ratifications -> LABELS.jsonl; overrides diffed vs model AND grader separately |
| H apply_rulings | bin/post_review.py rulings | each RULINGS entry rendered to machine effects: lexicon delta / charter delta / label overrides / hard rule; non-renderable residue -> grader/INSTRUCTIONS.md delta (versioned) |
| I retrain | bin/model.py train | new model_version = (cycle, labels SHA, rulings SHA, engine SHA) |
| J rescore_eval | bin/model.py score + eval | re-scored root + MODEL_EVAL.jsonl entry (prospective P/R per class, calibration, grader agreement, control results, importance drift) |
| K execute | ratified batches only | git rm batches citing ledger ids (foreign-lane mechanics per the D-0001 CTO ruling); MIGRATE -> change management, never batch-deleted |

Autonomy ladder: L0 (all human-ratified) -> L1 (auto-ARCHIVE in SCRATCH charters only;
earned by >=98% class precision over >=2 consecutive cycles; revoked by any control
failure). MIGRATE and CONTESTED are never automated. Every executed disposition cites
ledger id + scan vintage + model_version.
