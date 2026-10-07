# ADVI_COTBKF -- ROUND ANALYSIS, round 13

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~16:0xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 811), which carries:
- `ADVI_COTBKF_ROUND_13_L9_GRADE_20261007.md`;
- ADJUDICATION_v11;
- REMEDIATION_v7 @4053b9eff8.

CB13m1-AC3 is MET on the CVO's own read. ARMED 0.

## 1. State

The one signing table (`commonwealth_signs.SIGN`, 31 types, `leu` -1.0) is in place.
- **Account D49141617:** reads 0 mismatches over 2,851 sampled account-days.
- **Snapshot differences:** 0 of 381.
- **Row D2-S24:** REMEDIATED; it closes at the re-apply.
- **FWD-3 step 1** (daily holdings) is built locally. Steps 2-4 stay gated on MDPF_SECHIST's first price load.

## 2. ENRICHMENT -- round 14, ONE issuance by `2.0.0_SA_COO~C2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Re-apply the crosswalk and account links on the one signing table** (FWD-8). Under the pair below | (1) read-back: crosswalk 1,533 rows, 471 MATCHED; account links 1,450 rows, 212 LINKED, with the two named swaps; (2) the CB-m-2 diff re-run against the newly applied tables reads 0 changed | SERVED |
| E2 | **The 5 remaining fractional residuals explained** (2 after CAF rows, 1 single `li`, 2 at 0.02-0.029 on one CUSIP) | (1) each residual's cause named from its transaction rows, and classed as a sign the table lacks, a vendor rounding, or a source gap; a sign change goes through the one table with its census re-run, never a per-account patch | LOCAL |

The pair for E1: the CTO half is `NEVER_WIDEN_ADVI_COTBKF_R13_REAPPLY_CTO_HALF_20261007.md`. The COO half is `~C2`'s draft, given when
`~C2` signs it.

-- 1.0.0_SA_CTO~DELL2
