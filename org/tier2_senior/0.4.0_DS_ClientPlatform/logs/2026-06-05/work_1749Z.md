# 0.4.0_DS_ClientPlatform — /work work_1749Z (MDLP I1+I2 Global producer BUILT + VALIDATED)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

## MDLP_DISTFIX I1+I2 re-source — Global producer authored + validated; helper-triple foundation

Fully unblocked this cycle (COO Option-(b) owned-paths ruling + Andrew's 3 literals: SMA=EXCLUDE,
partner-set=union{49F,INF}, Global=MIGRATE). base-DE contract confirmed (parity=model-only).

### Helper-triple foundation (built + gate-tested)
- 3rd byte-identical floored_percentiles.py in data/smartx/scripts/ (bd+orion+smartx).
- ds-precommit-check sync-guard generalized PAIR -> N-way GROUP (tested: pass on 3-identical,
  fail naming all 3 on divergence, restored). Guard-triple commit HELD until AE commits the
  smartx helper in-lane (COO sequencing — avoid referencing an uncommitted copy).

### Global producer (compute_account_distribution.py) — re-pointed, gate-clean, VALIDATED
- SOURCE: dead opal-data-smartx-v2/smartx_allocations.parquet -> live
  s3://opal-data-mdpf/mdpf/feeds/model_aua_positions/{firm}/{latest}.parquet, UNION across
  {49financial, inflection}. Per-account = groupby(account_id).model_value.sum() on
  cohort_class=='model' (SMA excluded). Dropped obsolete Period/AllocationStatus/funded-month.
  Percentiles floored >=$1K via the shared helper. Output shape UNCHANGED.
- FUNCTIONAL SMOKE vs LIVE feed (local, no --upload, read-only): both firms' 2026-06-05 (TODAY)
  partitions; true-Global union **7,301 funded / $1.49B** (vs old 49F-only 6,838/$1.38B = I1 fix;
  fresh = I2 fix); total.min=$1,037 / p10=$7,987 (dust GONE, was $8.42); shape + TO-B + by_model
  (5 base + 2 INF blends) all correct.
- HANDED to 0.7.0_AE (174924Z) for in-lane commit + scheduled-job deploy (Option-b).

### Per-firm twin — SCOPE-Q to COO (held)
compute_per_firm_account_distribution.py has TWO builders: 49F (dead smartx_allocations, needs
re-point) + INF (already eclipse-gold). Surfaced A-vs-B to COO (174950Z): re-point BOTH onto MDPF
(reconcile-consistency w/ Global, my rec) vs just 49F. Awaiting COO/base-DE source ruling.

### Owned-paths blocker (resolved)
data/smartx/** = SHARED_OPAL_ETL (AE lane); DS not permitted. Did NOT --force; routed to COO ->
Option-(b): I author, AE commits in-lane. (.tools guard = DS-committable, sequenced post-AE-helper.)

## Other workstreams
- R2: DONE (tail = storage-trend read next CloudWatch cycle).
- MDLP I3: deployed+accepted (close = scheduled-nightly served-verify + visual smoke, next-day).
- GLDINC §5: reconcile-correctness co-owner; review in PRD v0.2 §5a; P0 reconcile-gate (0.6.0-lead).

## Compiler Tools
| Tool | Run | Result | Notes |
|---|---|---|---|
| ds-commit-gate | compute_account_distribution.py + smartx helper + ds-precommit-check | exit 0 | py_compile + undefined-name + sync-guard(triple) + ruff |
| (functional smoke) | python compute_account_distribution.py (no --upload) vs live MDPF feed | PASS | true-Global 7,301/$1.49B, dust gone (min/p10>=1000), shape preserved — the right validation for a re-sourced producer (read-only, no upload, no gold-runner) |

work-cycle:0015
