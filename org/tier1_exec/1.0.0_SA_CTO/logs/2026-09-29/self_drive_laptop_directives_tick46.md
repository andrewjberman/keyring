# /self-drive laptop directives -- ticks 44-46 (2026-09-29 20:03Z-21:12Z)

**archetype:** COORDINATE

Arming record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_230xZ_SELF_DRIVE_LAPTOP_FABRIC.md`
@`9549fd3b32`; cron `f02c52db`. **state: ARMED**

## Landed

- **MDPF_SECCLASS** (one canonical security table), in D8 under the existing MDPF macro:
  - L3 register `dc175119ab`;
  - L4 PRD v0.1 `b9680cfe86`, with FWD-1..8 verbatim, data contract `org/standards/MDPF_SECCLASS_CONTRACT.json`, and
    ~M as owner of the FWD-7/8 backend.
  - Owed: the CVO's ratified-text half. The brief half is accepted, since the CRO wrote the brief. Sequence: UNPLACED
    (only Andrew orders it).
- **Seating is not an issue:** 2.0.0_SA_COO lives in tier1_exec, and rule 27's seating limit does not reach Tier 1.
- **Gate hole closed** `3f33315632`: to-decomp-ref-lint never graded NEW tree task orders (`task-orders/`), so the
  `<decomp_ref>` and seating checks skipped all 25 tree projects. Census of the fixed lint over the 34 tree TOs added
  since 09-28: findings=0.
- The transcripts ledger is CLOSED (AE `66c5fb3844`). Step 3 is on CLOUD `f13d9e9222`.
- The INF raw writer is named (~P `0b5cdb06f9`): EC2 inf-bronze-runner. A launch-monitor '' pattern suppresses the
  retry, and the on-instance failure goes uncaptured.

## Decisions

- **Walk-2 backend placed** (103025-28): the W2-11/15 page fold is NOT legal, so ~M serves the aggregates. W2-04/05/06/07
  go to ~Y, W2-01 to ~P, and W2-12..14/19/20/21 to ~M.
- **W2-04/05:** no substitution to bd-securities (~Y 103033). etf-classifications covers 285 securities against about
  10.8k in bd-securities (cot 21%, bd 16% of holdings). A missing ticker shows verbatim. The backfill is MDPF_SECCLASS's
  first need, through the FWD-7 scheduled path, with bd-securities as reviewed input only.
- **W2-13 industry:** a new canonical field beside O8, filled by the scheduled path, with Bloomberg GICS as an input
  only (~M 103034).
- **Pre-commit hook hang** (2nd, CVO session): owned by the CTO. MSTR's capture is armed for the next hang (103031).

## At Andrew

- None open. Worth knowing: Andrew said the canonical table "also has all the individual securities". It holds 285
  rows. The backfill is the first MDPF_SECCLASS work.
