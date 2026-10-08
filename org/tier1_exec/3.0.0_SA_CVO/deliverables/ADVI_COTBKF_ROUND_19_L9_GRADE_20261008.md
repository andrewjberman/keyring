# ADVI_COTBKF round 19 -- L9 grade of CB19s1-AC3 (the sweep list)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~17:5xZ. **Order:** `ADVI_COTBKF.TO-CB-s-1` (drained @bf424e274b).
**Criterion (verbatim):** "the sweep list reads as a declared list: every CUSIP on it is a bank sweep by its stated source, and no
rejected candidate should have been on it." **Ruling it applies:** `1.0.0_SA_CTO~DELL2` round-18 analysis @04b347e9ea section 1
("A bank sweep is the account's cash parked in an interest-bearing vehicle ... sweep vehicles are cash ... a declared, versioned
list: each listed CUSIP is named with its source ... A security not on the list is never treated as cash").

## Verdict: MET

1. **Declared list.** `commonwealth_sweeps.py` `SWEEP_LIST_VERSION` sweeps-v1-20261008; two CUSIPs, each with its source
   (vendor `Security_Description` as delivered): FDIC66606 "Bank Deposit Sweep Program", FDIC66853 "Advisory Retirement Sweep
   Program". Both are bank deposit sweeps by their own description. CFNCASH stays cash, not a sweep.
2. **Rejected candidates.** 520 flagged CUSIPs: 2 SWEEP, 1 CASH_BALANCE, 517 REJECTED, 0 UNACCOUNTED. The 8 classes sum to 517
   (CD 385, MERGER 52, BANKISSUER 32, MMF 23, UITCASH 18, INSURED 4, CASHMGMT 2, FUNDNAME 1). No rejected CUSIP is a bank deposit
   sweep by a stated source. The two classes the issuer asked me to read:
   - **CASHMGMT (2).** 262006836 and PER999676: 30 transaction rows across 4 accounts, 2023-03 to 2024-11; PER999676 carries only
     `dv` rows. Neither description names a bank deposit program, and neither trades like a sweep. Correctly rejected.
   - **MMF (23).** Money-market fund shares are NAV-priced funds, not bank deposits. Under the ruling as written they stay off.
     **One finding beyond the criterion:** 316067107 (Fidelity Government Cash Reserves) trades like a custodian CORE sweep, not an
     elected fund: 8,768 rows across 232 accounts since 2023-03-17, monthly `dv`/`dvr` (3,410 / 3,292), and 91% of its rows fall
     on an account-day that also traded another CUSIP (the two listed sweeps read 75% and 78% on the same measure). The criterion
     is met because the ruling covers bank sweeps by stated source and this one has neither. Whether a money-market core position
     is a "sweep vehicle" under the ruling's headline is the CTO's call, and it is wider than the packet's enrichment item 2
     (6 months): it touches 232 accounts.

## This seat's reads

- `.scratch/advi_cotbkf/cache/transactions.parquet` (1,416,497 rows; dell2, 2026-10-08 ~17:5xZ): per-CUSIP rows, accounts, type
  counts and the same-account-day pairing share for FDIC66606, FDIC66853, PER999676, 262006836, 316067107, 31617H102, 922906300.
- `deliverables/0.9.0_WK_ADVI_COTBKF~40/sweep_regrade.md` lines 5-20 (list and class definitions), 545-555 (census by status),
  and a recount of the class table.

## Discrepancy in the L8 packet (prose only)

The drain-end packet's class counts (CD 279, cash-merger 61, bank issuer 33, money-market 22) do not match the report it cites
(CD 385, MERGER 52, BANKISSUER 32, MMF 23). The report is self-consistent: its classes sum to 517. The packet prose is wrong; no
artifact is affected.
