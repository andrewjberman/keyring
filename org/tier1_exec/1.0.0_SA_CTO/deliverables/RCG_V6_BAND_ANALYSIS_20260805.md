# v6 (465f15ce) uncertainty band — what is actually in it, and what it asks you to rule

**Author:** `1.0.0_SA_CTO~B`, 2026-08-05 ~00:5xZ. **Ordered:** Andrew-direct ~002xZ ("*then can
look into v6*"). **Basis:** predictions.jsonl @ scan vintage `20260804T174531Z_f919615b`, all
14,947 scoreable rows, model_version 465f15ce on every row (verified — single-version file, no
mixed-vintage contamination). Re-derived here, not read from the retrain record.

## Headline: the band is 172 files; your decision surface is 30

| Slice | Count | What it means |
|---|---|---|
| Band total (`uncertain: true`) | **172** of 14,947 (1.15%) | p_archive 0.350–0.645 |
| — already seeded **KEEP** | **142** | model is unsure; the ledger is not. No decision needed — these are model-calibration data, not questions |
| — seeded **ARCHIVE_CANDIDATE** | **8** | model doubts an archive-side label → **over-archive check** |
| — **no seed at all** | **22** | **the genuinely undecided set** |

**So the sitting rules on ~30 files, not 172.** The 142 KEEP-seeded members are the band doing
its job (flagging where the model's confidence is weakest) without asking anything of you.

## The 22 genuinely undecided, and they fall into 4 coherent cohorts

Adjudicate as cohorts, not per file — three of the four are structurally uniform:

1. **`org/modules/perceive/` + `org/modules/act/` (8 files, p_archive all exactly 0.465)** —
   identical scores mean an identical feature vector: the model sees these as ONE object.
   `corpus_aggregator`, `corpus_indexer`, `filesystem_scanner`, `vector_index`, `key_generator`,
   `registry_writer` + two `__init__.py`. **One cohort verdict; splitting them is meaningless to
   the model and would fracture a package (the click/C7 lesson).**
2. **`infra/aws` step-functions + rollback + scripts (7 files, 0.462–0.638)** — includes the
   three `bd-gold-*` Step Function definitions (foundation / stage2 / pipeline-complete). **These
   are pipeline-shaped: verify live-vs-dead before any archive verdict** — a Step Function
   definition that still backs a live state machine is deploy-coupled, and cohort-A routing
   applies (prepared handoff, not RCG execution).
3. **`tools/market_update/components/news_recap/` (4 files, 0.536–0.605)** — the model's
   top-candidate locus across BOTH v5 and v6. Generator + component + prompt.
4. **Singletons (3):** `infra/security/policies/README.md` (0.640 — highest in the band),
   `infra/testing/smoke/critical-paths.sh`, `infra/orchestration/config/.bashrc.agents`,
   `timeseries/vix.json` (0.396).

## The 8 archive-seeded doubts — and the convergence worth noting

Five sit under `docs/architecture/`, and **three were re-adjudicated to KEEP hours ago on the
label-vs-LAW ruling** (`GOLD_PERF_PRD.md`, `ADHC_TMSTEL_PRD.md`, `YALP_ATTRBN.md` — now
CTOB-RCG-002 / exact-path VERDICTS rows). **The model independently doubted the same files the
law pinned.** Two instruments, different derivations, same class — that is the tie that counts
(a shared-derivation tie would not).

The remaining 5: `COMPILER_IAM_LAMBDA_PARSER.md` + `PORTAL_DESIGN_NORMALIZATION_AND_COMPILER_TOOLS.md`
(both still MIGRATE under R-0020; both in CRO's open per-file list),
`opal-assets-absence-check/lambda_function.py` (0.430 — **teardown residue I dispositioned in the
cycle-3 board; the model doubting its archive label is the model being wrong here, and that is a
useful calibration fact**), plus two dated briefs already on the `docs/briefs/archive/` move-list.

## Band widening 151 → 172 is CORRECT, and the reason matters

v5 trained on 4,103 wrong-side labels at **max weight 5.0** — that artificially *sharpened* the
decision boundary (a large block of confidently-wrong training mass pushes the model to false
certainty). The repaired v6 is honestly less certain. **A wider band on a repaired ledger is the
instrument recovering, not degrading** — the number to distrust was 151.

**Robustness check that passed:** top-candidate locus (`data/seeking-alpha` + `tools/market_update`
+ `seeking-alpha-ui`) is **unchanged v5 → v6**. The contamination did not manufacture the signal —
so the model's actual finding survives its own repair. That is the strongest evidence yet that
the archive signal is real rather than an artifact of label bookkeeping.

## What I recommend at the sitting

- Rule the **4 cohorts** (not 22 files) + the **2 open per-file architecture docs**.
- Before any verdict on cohort 2, require the **live-vs-dead check on the three bd-gold Step
  Functions** — deploy-coupling makes them prepared-handoff class regardless of label.
- Treat the 142 KEEP-seeded band members as **calibration data for cycle-5**, not agenda items.
- The `opal-assets-absence-check` doubt is a **known-wrong model call with a known-right answer** —
  it is a free planted-control specimen for E-0005's calibration set.
