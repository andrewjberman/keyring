# 0.6.0_AE_PartnerETL — work cycle 2026-06-11 2120Z

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE

GLDINC 7-script conversion, session segment 2: A_02 lifecycle completed through
nightly-evidence wiring; A_01 engineered → shadow FAIL → root-caused to a
PRE-EXISTING oracle non-determinism → CTO fix-oracle-first ruling; B_02
empirically characterized + designed. The "careful one-by-one" discipline
caught a production data-integrity defect that nightly full rebuilds had
been silently exercising.

## A_02 (1/7) — COMPLETE through evidence phase
- Back-dated-row guard amendment (found via A_01 design analysis): any window
  row trade_date <= floor -> full fallback. DS deployed c8ed91949 pre-nightly.
- Nightly shadow wiring: gold_dispatch.sh GLDINC_SHADOW_SET hook (post-chain,
  fail-open, chain:full only, per-script --shadow --shadow-lag 1 --upload).
  Tested standalone (5 behaviors + set -e safe). Commit f78977825; S3 md5 MATCH
  (dispatcher is .sh = AE lane; safe-deploy pre-push only covers .py — uploaded
  + verified explicitly). Night-1 A_02 evidence starts on tonight's 22:00Z run.
- Invariant probes: fees = 0 forward-dated, 0 back-dated>14d across all 1,881
  files (design assumptions now measured, not assumed).

## A_01 (2/7) — engineered; BLOCKED-EXTERNAL on oracle fix (correctly held)
- Probes: silver/transactions 38% of recent files carry rows back-dated >14d
  (worst -519d); txn_id sets DISJOINT across files; intra-file multi-row txns
  ~78%. => change-point cache unviable; engineered v2 DAILY-STATE-GRAIN cache
  (preflt pattern: full (account,date) grain + _file_date provenance,
  eviction-by-provenance, etag restatement guard). Gate clean.
- Offline shadow (3d): PARITY FAIL 61 keys. HELD handoff; root-caused:
  * full-vs-full self-test: oracle NON-DETERMINISTIC (10-36 key wobble/pair;
    4 builds = 14,733/14,735/14,740/14,742 records on identical data).
  * Triple-compare: incr diff = SYSTEMATIC fresh-wins bias vs the oracle's
    RANDOM tie-winner on cross-file (account,date) ties (back-dated rows);
    byte-parity vs a random tie-winner unachievable by construction.
  * IMPACT: served advisor_assignments_history (-> C_08/D_00c/D_02) flips
    attribution keys night-to-night with no data change. Pre-existing.
- ESCALATED DS (co-owner) + CTO. CTO RULED 211102Z: fix-oracle-first APPROVED —
  DS lands deterministic tiebreak (sort (account,trade_date,_file_date,row-pos)
  before dedup) as own reviewed change w/ changed-keys delta; then A_01 re-proves
  vs stabilized oracle. Never-widen honored (I changed nothing in the oracle).
- Worktree holds gate-clean A_01+s3_layout changes (incl. _file_date tagging DS
  can reuse for the tiebreak). Diag artifacts /tmp/a01_diag_*.parquet.

## B_02 (3/7) — characterized + designed (implementation next)
S3-version etag evidence: old-date lots_realized re-uploaded byte-identical
EVERY run (waste + version bloat); lots_unrealized self-limits (~7d). BUT late
realized postings legitimately change old dates -> naive skip/sealing wrong.
Design = per-date INPUT FINGERPRINT (3rd pattern): hash bd_realized rows/date +
prices/date + Schwab/alloc etags/date; recompute exactly changed∪new dates;
ref-hash change -> full fallback. Brief §4e.

## Compiler Tools
| Tool | Result |
|------|--------|
| comp-pipescript io B_02 | 10 reads incl 3 Schwab prefixes + B_00 FUNC-key gate; 2 per-date write families -> B_03 |
| comp-blast positions_cube (A_03, earlier) | 46 consumers — informs A_03-last sequencing |
| ds-commit-gate A_01+s3_layout, A_02 guard | CLEAN (3 runs) |
| aws s3api list-object-versions | B_02 old-date etag-identity evidence (design input) |

## Open / next
1. B_02 implementation (input-fingerprint incremental + shadow) — next segment.
2. A_01: resume on DS tiebreak RAVC2 (mirror ordering in cache-union, re-shadow).
3. Tomorrow AM: COTETL verify (checklist pre-staged) + night-1 A_02 scorecard +
   GLDINC post-fix load_flows scorecard.
4. A_02 cutover: accumulate clean nights -> Andrew nod -> INCREMENTAL_CAPABLE.

## Cost note
All proofs/probes ran LOCALLY against S3 (no c6i runs). Nightly shadow rides
the scheduled chain only.
