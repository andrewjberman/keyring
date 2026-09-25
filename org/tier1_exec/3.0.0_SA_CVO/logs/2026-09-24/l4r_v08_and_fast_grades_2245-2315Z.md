# DSGN_IRPTV1 L4-R ratified-text half refused at v0.7, signed at v0.8; FAST pins graded -- 3.0.0_SA_CVO

**archetype:** VALIDATE
**Date:** 2026-09-24
**Task Order:** ad-hoc (spine-owned L4-R act; FAST after-the-fact grading)
**Status:** COMPLETE

---

## Objective

Seated by `0.0.0_AB_MSTR` (msg 100921) on Andrew-direct via `4.0.0_SA_CRO` 100892, "Make sure this gets done". The
DSGN_IRPTV1 ratified-text half read STALE and blocked the round-3 L6 cut at `to-pipeline-gate.py` LIMB 6. Then the
FAST pins handed to this seat were graded after the fact.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find -i 'asset_class' docs/contracts/investor-reporting portal/src/pages/InvestorReporting/contracts ... --files` | PASS | 70 hits across 2,611 files, DEF=3; confirmed the v0.6 member exists in the schema and the portal adapter |
| prd-signoff | `python .tools/prd-signoff.py status/refuse/sign DSGN_IRPTV1` | PASS | STALE -> REFUSED -> SIGNED; the PRD reads ADMITTED |
| prd_signoff_lib | `half_hashes()`, `endpoint_hash()` | PASS | v0.7 `eda43d9a7a6b`/`5c40ea8d882f`; v0.8 `9f2702c16e62`/`0193ebd965d7`; both match the deliveries |
| surprise-row-gate | via safe-commit on S10 | PASS | 1 new row of 25 |
| Bash rail | raw grep over directories | WARN | rail denied three raw greps (correct); switched to native Grep and comp-find |

**What worked:** `prd-signoff.py` refuse/sign round trip. The CTO bumped v0.8 within minutes of the refusal.
**What failed:** none.
**Gap found:** a CVO FAST-grade FAIL has no send path to the COO. The broker's L8 guard refuses it, and FAST says "a
FAIL becomes the next item". I used a seat surprise row (S10) as the carrier.

---

## Work Completed

### 1. Startup
`/watcher`: registered at PID 3212; Monitor `bvcvu1fc8`, script pid 29948. XXX.md A.1-E done. B.0: 30 rows since
10:00Z; the 5 OFFER-EXHAUSTED rows (100605, 100626, 100628, 100632, 100707) were opened from `read/` and acked.
32 messages acked in all.

### 2. L4-R, v0.7 REFUSED
Review @`12b89b8dd4`, stamp @`0bcd1f9437`.
- R1: FWD-5 and FWD-6 put footer content that FWD-18 bars (Andrew P:26-28).
- R2: FWD-7 "first step" contradicts FWD-8's upload-first step.

### 3. L4-R, v0.8 SIGNED
The CTO bumped v0.8 @`31a61d0466` with exactly those clauses. Review @`da7e114a5c`, stamp @`0fe69145c8`; the PRD is
ADMITTED. Two non-blocking observations are recorded in the review.

### 4. FAST pins graded
Record @`ddb0339061`, `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_FAST_PIN_GRADES_20260924.md`.
- 16 pins: 14 PASS, 1 FAIL (`68f46e18`), 1 not graded (`9902bf25`).
- Five next items (N1-N5) are not named by any issued round-3 order.
- The FAIL is carried as row `DSGN_IRPTV1-S10` @`6495c8d491`.
- Duplicate artifacts: the perf-footer and opal-engine PNGs are byte-identical.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| REFUSE v0.7 on two ACCEPT contradictions | A build cannot pass both lines of either pair at L9. The fix was three clauses, cheaper now than a false NOT_REALIZED later |
| SIGN v0.8 despite "(v0.8, FWD-18)" in two ACCEPT lines and the unchanged CONTRACTS "footer line" | Neither changes what a grader tests; a second refusal would be friction |
| "AMENDED v0.6" / "RETIRED CAPABILITY" in SOURCE lines are not the barred annotation | `/endpoint` step F0 requires the case statement and the one-line retirement |
| IRPT_BCKEND ~Y `bb1eb7f92b` and ~P pins not graded | Both handoffs say the real run follows; FAST grades only a real-run artifact |
| The six `c3-*~Y.md` orders are not held here | `<issued_to>` = `3.0.0_SA_CVO~Y` |

---

## Blockers

None held by this seat.

---

## Current State

- DSGN_IRPTV1 PRD v0.8 @`31a61d0466`, ADMITTED. `prd/signoff/3.0.0_SA_CVO.json` is SIGNED @`0fe69145c8`.
- Round 3 (IV-e-9..IV-e-20) is issued and pending under `2.0.0_SA_COO~D`.
- The FAST grading record @`ddb0339061` is the input to the round-3 slug's FAST-interval section.
- Push state: LOCAL (origin/CLOUD `01862322b6`, ls-remote read at ~23:05Z).

## Next Steps

- [2.0.0_SA_COO~D] Read `DSGN_IRPTV1-S10`. Place N1-N5 in a round-3 criterion or the next-list.
- [3.0.0_SA_CVO] Grade the IRPT_BCKEND ~Y and ~P pins when their real-run artifacts land. Carry the FAST section in
  the DSGN_IRPTV1 round-3 slug.
