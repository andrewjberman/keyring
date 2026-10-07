# IRPT_CUSTDY -- ROUND ANALYSIS, round 4

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~12:2xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. This answers `3.0.0_SA_CVO`'s slug (msg 510):
REMEDIATION_v4 @f29b4eb6e2. 7 rows: 5 dismissed, 2 OPEN; S5, S7 and S8 closed in place; ARMED 0. Suite re-run: 110 passed.

## 1. Where FWD-1 stands -- hops 1-4 run on real data; NOT LIVE

SI is OK on 14 of 14 accounts and 10 of 10 households (the SI branches ruled at msg 422). Hops 1-4 run on real data. What remains:
- **Hop 5 (render):** the template can now be built on dell2 (the portal toolchain landed); the served render waits on IRPT_BCKEND
  E-P9's release, and that waits on the terraform kit.
- **Hop 6:** Andrew's act.
- **W10-S1**, below. FWD-1's ACCEPT is "every client gets a report", so four unkeyed accounts are a FWD-1 gap, not a footnote.

## 2. Rulings

**W10-S1 -- the 4 unkeyed accounts (1,447 firm-wide). MEASURE, then decide by the measurement:**
1. Look up each of the chosen advisor's 4 accounts in Schwab's own accounts file by every identifier it carries (account number with
   and without its leading zeros, the masked last-4 plus the household, the master). Print which identifier, if any, finds it.
2. An account found under another key is mapped through the IRPT_BCKEND seam. That is a seam cell for `~P2`, never a local alias in
   this project.
3. An account Schwab does not hold is shown on the report as "not covered: <reason>", and the advisor's report for that client says
   so. FWD-1's ACCEPT is then read on the clients Schwab holds, with the uncovered ones named.

The firm-wide 1,447 is the same IRPT_BCKEND directory-coverage census routed to `~P2` at round 3.

**IRPT_BCKEND: case-insensitive null-likes.** `ids.py:388`'s guard compares case-sensitively, so `none`, `NaN` and `NULL` would
still reach the mint (0 in the seam today). This joins E-P8 as criterion (4) for `~P2`: the guard matches null-likes
case-insensitively, with a test per spelling.

## 3. ENRICHMENT -- round 5, ONE issuance by `2.0.0_SA_COO~K2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **The 4 unkeyed accounts, measured** (W10-S1) | (1) each account's lookup by every identifier is printed with its result; (2) each is classed found-under-another-key or not-held, with evidence; (3) a not-held account renders "not covered: <reason>" in its client's report data | LOCAL read |
| E2 | **The 49 Financial template** (round 1 E3; un-parked by the portal kit) | (1) a `ClientReportDocument` for 49F renders hops 3-4's figures for one real client of the chosen advisor (not a fixture); (2) no field is named after a Black Diamond field (C-SHAPE); (3) typecheck, eslint and the template's test pass, run as `bun --no-install` inside `portal/` (the HAZARD of msg 490) | LOCAL |

-- 1.0.0_SA_CTO~DELL2
