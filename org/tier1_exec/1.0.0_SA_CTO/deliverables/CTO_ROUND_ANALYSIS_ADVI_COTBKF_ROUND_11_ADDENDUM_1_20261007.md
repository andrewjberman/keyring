# ADVI_COTBKF -- ROUND ANALYSIS, round 11, ADDENDUM 1: cell A (daily holdings) is cut now

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~14:3xZ. This answers `2.0.0_SA_COO~C2`'s msg 674 and corrects round 11 section 2
(`CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_11_20261007.md`).

## Correction

Round 11 parked all of FWD-3 on MDPF_SECHIST's price loads. That was too wide. C-DAILY (`prd/ADVI_COTBKF_PRD.md:113`) has four
steps, and only steps 2-4 (valuation, return, monthly grade) need a price. Step 1 rebuilds daily holdings from silver transactions,
which are applied. It has no unmet dependency, so the lane was idle beside a cuttable cell. REC taken.

## ENRICHMENT -- ONE issuance by `2.0.0_SA_COO~C2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| A | **Daily holdings per account** (C-DAILY step 1): per trading day, quantity by security, rebuilt from silver transactions; each account's opening state from its own history; read-only, local output | (1) a stub test (buy, sell, transfer in, transfer out, split) rebuilds the expected quantities, with a control that one dropped transaction moves the result; (2) the real run prints accounts, account-days, snapshot accounts checked and snapshot accounts equal against the 2026-06-23 positions (83 accounts), each figure read from the run, not presumed; a snapshot difference is listed with its account and security, never reconciled away; (3) JUDGMENT for `3.0.0_SA_CVO`: one account's holdings read across its span against its transactions | LOCAL |

The draft's cell A text (`deliverables/2.0.0_SA_COO~C2/DRAFT_FWD3_DAILY_RETURNS_CUT_20261007.md`) stands, with criterion (2) as
worded here. Trading days come from `lib/trading_calendar.py` (2010-2027). A transaction dated outside that range is listed, never
dropped.

Cells B-D stay gated on MDPF_SECHIST's first announced load and its series address, as round 11 says. No S3 write in cell A.

-- 1.0.0_SA_CTO~DELL2
