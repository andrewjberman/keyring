# 0.6.0_AE_PartnerETL — work cycle 2026-06-11 2150Z

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

GLDINC segment 3: A_01 oracle-fix engineered + proven + handed to DS (option-1
split per DS proposal). Second pre-existing defect caught live during the
determinism proof. B_03 classified.

## A_01 oracle-fix (standalone, CTO fix-oracle-first ruling)
Split: AE engineers + proves; DS reviews/commits/deploys + owns CTO never-widen
review. Incremental WIP parked .runtmp/gldinc_a01_incremental_wip/ (restored
A_01+s3_layout to HEAD for an A_01-ONLY minimal fix).

Fix (gate-clean): (1) _load_one tags _file_date+_intra_pos; (2) txn_id dedup
total-order sort-before; (3) (account,date) dedup provenance-extended
sort-before (THE attribution-flipping dedup); (4) load-completeness guard
(failed read -> RuntimeError, was WARN-and-continue). + Rule-15 future-import,
2 gate-forced lint nits (f-string, unused sys import).

PROOF (all local, 6 full builds total, no c6i):
- DETERMINISM: 4/4 complete-load builds byte-identical (14,847 rows, 0/0).
  Pre-fix: never 2 alike (14,733-14,742).
- b3 anomaly root-caused = DEFECT #2 caught live: transient S3 read failure
  silently dropped a file (3,068,324 vs 3,068,516 post-dedup rows = 192 raw
  rows) -> 18 shifted SCD keys. Swallowed-exception load path = even a
  deterministic oracle non-reproducible under transient errors. Guard added.
- DELTA: 122 keys/60 accounts vs pre-fix sample; account-level containment in
  the 79-key/72-account tie-population = TRUE (SCD-chain manifestation > causal
  ties, expected). Artifacts /tmp/a01_oraclefix_*.parquet.
- TXN_ID: NOT a no-op — 32,277 cross-file txn_ids dataset-wide (3-pair probe
  had undersampled); sort is load-bearing + correct there.
- A_02 equivalent-fix NOT needed (fees: no cross-file ties). 
- build_history_for_account confirmed dead -> flagged, untouched (DS routes).

Handoff to DS 2146Z. After DS deploy: rebase incremental, mirror ordering in
cache-union dedup, re-shadow 1/3/10d vs stabilized oracle, hand off A_01.

## B_03 classified (5/7)
Pure arithmetic on canonical outputs, per-date grain, ALL inputs dated (no
latest-refs). Incremental = per-date input etag fingerprint; shares machinery
with B_02. (Identical re-uploads keep the same etag -> valid even before
B_02's redundant-rewrite fix lands.)

## Compiler Tools
| Tool | Result |
|------|--------|
| ds-commit-gate A_01 (x3 iterations) | CLEAN final |
| (proof harness) full-vs-full x5 + delta + tie-enum | determinism 4/4; defect #2 evidence |

## Open / next
1. DS review/commit/deploy of A_01 oracle-fix -> CTO never-widen review.
2. B_02 implementation (input-fingerprint; share with B_03) — next work item.
3. Tonight 22:00Z: A_02 night-1 shadow + post-fix load_flows scorecard -> AM review.
4. AM: COTETL verify (checklist staged) + PRTORG AC-closeout.
