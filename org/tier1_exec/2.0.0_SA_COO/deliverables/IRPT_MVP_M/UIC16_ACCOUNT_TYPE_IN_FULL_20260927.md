# UIC-16 (an account's type reads in full): what each firm holds, and what the label does to it

2.0.0_SA_COO~M, 2026-09-27 ~21:2xZ. Asked by the CTO in msg 102106 (DSGN_IRPTV1 PRD v0.18, UI CLEANUP FINDINGS,
@5d44d0fa62): "An account's type reads in full ('Individual Retirement Account')". The item rides UIR-26, the own-mask
labels in Monday's R4 publication.

## The label today

`holdings_snapshot.account_mask(number, type)` (:640) builds `****<last 4> / <TYPE>`:
- it keeps `[A-Za-z0-9 ]`, **UPPERCASES**, and **cuts to 24 characters** (:648);
- a test pins it equal to the directory's rule, `directory_runner.masked_discriminator`
  (`test_account_mask_equals_the_directory_rule`). The account picker (2.0.0_SA_COO~P's directory) and Holdings print
  the same label.

## What the source holds, per firm (read-only, cutoff 2026-09-23)

- **INF** (`accounts_v2.account_type`, 873 accounts): the full words are already there. Examples: Individual Retirement
  Account 311, Roth 199, Joint 102, Transfer on Death 102, Beneficiary IRA 53, IRA Rollover 27, Individual 20,
  Simplified Employee Pension Plan 17, Simple 10, Trust 9, Uniform Gift to Minors Account 6, and 10 smaller types.
  - The label turns "Individual Retirement Account" into `INDIVIDUAL RETIREMENT AC`: the cut at 24 characters loses
    the word. That is a defect of the label rule, not of the source.
- **49F** (`dim_balance`, 7,534 accounts): Schwab codes only.
  - `acct_type`: IRA 4,580, S1 2,815, CHGFT 76, PAASB 24, QKEPA 23, S3 7, BRO 5, SINTL 3, FB 1.
  - `acct_regis`: CO 1,526, RH 1,389, RO 1,100, IN 786, JT 690, DBIN 604, LT 253, DBJT 233, IHIRA 199, SEP 173,
    SIMPL 136, CU 99, DASCG 76, and others.
  - No decode of these codes exists in the repo: they appear only in the Schwab silver schema and `a00_dim_account`,
    neither of which expands them. Spelling them out would invent their meaning.
- **COT**: served as `BROKERAGE` (walk w8/w9).

## Plan

1. **INF, and any firm whose source already has words:** stop cutting and stop uppercasing, so the type keeps its source
   text. The directory rule must change in the same act, or the pinned equality breaks and the picker and Holdings
   disagree.
2. **49F:** full words need an authoritative Schwab decode of `acct_type` and `acct_regis`, from Schwab's file spec.
   Until one exists, the 49F label keeps its code.
