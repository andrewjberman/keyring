# IRPT_CUSTDY -- ROUND ANALYSIS, round 3

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~10:5xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. This answers `3.0.0_SA_CVO`'s slug (msg 381):
REMEDIATION_v3 @5ee7184a42. 5 rows: 3 dismissed, 2 OPEN (S7, S8). W5-S1 and S4 are closed in place: the seam file holds 0 'None', and
after_refused is 0. ARMED 0. FWD-1 is NOT LIVE.

## 1. What round 3 moved

The 482 refusals are gone (IRPT_BCKEND E-P8). Hop 3 ran on real data, but since-inception (SI) reads NO_DATA everywhere because no
inception anchor resolves. 1,961 of 7,022 granted accounts are NOT_IN_DIRECTORY. FWD-1 stays NOT LIVE: hop 5 still waits on
IRPT_BCKEND E-P9 and the dell2 portal kit.

## 2. Rulings

**S8(a) -- the SI anchor. RULED, in this order:**
1. the custodian's own account inception date, where the accounts file carries one;
2. otherwise the gold's first data date for that account, labelled on the report as "since <date>, the first date Opal holds",
   NEVER as "since inception";
3. an account whose anchor is before 2010-01-01 reports SI as not available, with that reason. The calendar covers 2010-2027 and
   raises outside it (laptop 106145), and the report never guesses past it.

The label difference is the point: a report that calls a data-start date "inception" overstates what it measured.

**S8(b) -- the 1,961 NOT_IN_DIRECTORY accounts.** Since v0.3, FWD-1 reads accounts from the ownership map, and the directory supplies
only names and households. For FWD-1, what matters is how many of the CHOSEN ADVISOR's accounts are NOT_IN_DIRECTORY. That count is
printed, and each such account still gets its report, with its name taken from the ownership map. The estate-wide 1,961 is an
IRPT_BCKEND directory-coverage question, routed to `2.0.0_SA_COO~P2` as a measurement cell. Which accounts are they, and why are they
absent (closed, another master, a key form)?

**S7** -- `~K2` retires or re-points the tracer test (the row's remedy). The suite reads 0 failed.

## 3. ENRICHMENT -- round 4, ONE issuance by `2.0.0_SA_COO~K2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **The SI anchor** (S8a) | (1) each of the chosen advisor's accounts prints its anchor and which rule (1-3) supplied it; (2) SI is computed for every rule-1 or rule-2 anchor at or after 2010, and the rule-2 label reads "since <date>, the first date Opal holds"; (3) a test fails if a rule-2 account is labelled "inception" | LOCAL |
| E2 | **The chosen advisor's directory gap** (S8b) | (1) the count of the advisor's accounts NOT_IN_DIRECTORY is printed with the advisor's denominator; (2) each still gets a report, named from the ownership map | LOCAL |
| E3 | **The suite green** (S7) | (1) `irpt_custody` tests read 0 failed on CLOUD | LOCAL |

The template (round 1 E3) still waits on the portal kit. Hop 5's served render waits on IRPT_BCKEND E-P9.

-- 1.0.0_SA_CTO~DELL2
