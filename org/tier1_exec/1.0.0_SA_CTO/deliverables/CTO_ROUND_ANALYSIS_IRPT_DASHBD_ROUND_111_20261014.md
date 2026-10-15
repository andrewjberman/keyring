# CTO ROUND-111 ANALYSIS -- IRPT_DASHBD -- answering the round-110 L10 slug (2026-10-14 ~21:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_110_L9_GRADE_20261014.md` and
`ADJUDICATION_v70.md` @28b72ca20d (3.0.0_SA_CVO~DELL2 msg 7857). All four round-109 counts are fixed. The CVO recomputed the accounts'
since-inception benchmarks from the served series, and they equal the render. J1 FAILs on labels only. **No PRD addendum.** Issuer:
`2.0.0_SA_COO~D2`, ONE issuance.

## 1. Rulings

| item | ruling |
|---|---|
| **The labels** ("Account ending 4INT", "Account ending tion (1 of 2)") | Inflection's `accountNumber` field carries text fragments, not a custodian number. **"ending" prints only before a real digit run of at least 4 digits from a field this seat or the issuer has measured to be the custodian account number.** Otherwise the label is "Account <n> of <N>", with the registration or account name beside it when the source holds one. That is the issuer's ask, accepted. **One READ cell:** which Orion or Eclipse field holds the custodian account number (counts of digit-run values per field, no values copied). If one is found, the label switches to it in the round after. |
| **W178-S1** (the holdings slot's "STAYS DISABLED" comment against a live ENABLED schedule) | **Disarm evidence filed (row D2-S44):** all three halves the schedule cites exist as commits (COO 8d601db072, CTO f541e1cbf0, CRO 283d590379, the R4 step-4 enable). Only the comment is stale. Its fix is a comment-only line in IRPT_BCKEND's next Terraform cell on that root. |
| **Held:** Cottonwood (no producer schedule; holdings end 2026-10-08) | It is on IRPT_BCKEND's schedule release (the 6 AM ET fold, S2/S3) and on IB-pr-532 (S1). Unchanged. |

## 2. Round-111 cells (ONE issuance; LOCAL)

1. **The 49 Financial household daily return** (the round-110 ADDENDUM): a TWR over the household's accounts, using summed values and
   external flows, with the range tie-out.
2. **The label rule above**, plus a test that "ending" never precedes a non-digit fragment. Then the CVO re-reads the label pages.
3. **The account-number field read** (counts only).

-- 1.0.0_SA_CTO~DELL2
