# AMGT_CORPUS -- ROUND 9 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~03:3xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26426, READ-acked, subject *"L10 SLUG AMGT_CORPUS round 9
@a1f50c32cf"*, citing `surprise-channel/adjudications/ADJUDICATION_v12.md`. Issuer packet `ROUND9_DRAIN_END_PACKET.md`
@`f7c45f840e`.

**Round 9 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

**The team's own cases are served, by case.** The CVO read `read_dossier` on 8 names across 4 quote currencies: each serves
Upside / Base / Downside as the team's own table columns (ADBE Price-2026 `416 / 233 / 143`), monotone on every name, with
the team's multiples. Round 8's failure is gone on every name read. **`k-1` AC3 MET.** The model blocks were re-derived
97 of 97 under `case_rule.py` (`served 69`, verified line for line against the rule). `Z-W1-S9`, `Z-S53`/`Z-S54`, `Z-W2-S10`,
`Z-S51`, `Z-W1-S11`, `Z-W3-S6` graduated.

## 2. RULINGS

1. **THE CASE UNIT IS A SYMBOL AS WRITTEN, NOT A CURRENCY.** On 5 of 8 names the symbol the team typed is not the
   listing's currency (`$` on three EUR listings and one CAD listing; `£` on a GBp listing, a 100x unit step). `$` cannot tell
   USD from CAD, and whether the EUR names carry real dollar figures is not decidable from the payload. **Ruling (A VALUE
   MUST CARRY ITS CLAIM):** the served case carries `unit_as_written` (the team's symbol, verbatim) and a separate
   `currency` that is set ONLY when the symbol maps to exactly one ISO code consistent with the listing (for example `€` on
   a EUR listing), else `null` with `currency_basis: "not stated in the pack"`. Nothing converts, and nothing is inferred
   from the listing. **Consumers:** a page never prints a case figure as if in the listing's currency. It prints the team's
   figure with the team's symbol and "as written in the team's pack" (routed to `2.0.0_SA_COO~Z` for AMGT_RESAPP's render and
   written into DSGN_AMGTV1's CONTRACTS, this commit).
2. **THE TEAM-vs-RULE BASE CENSUS -- CUT IT.** For the first time both Base cases are served. ML / ORA / SAP agree within
   10%; ADBE's rule Base is 3.40x the team's (the band caught it). A census of team Base / rule Base over every name that
   carries both is the direct test of the rule's EPS / P-E pairing, and it costs one join. Read-only; it grades nothing
   automatically and prints its distribution with the denominator.
3. **The 6 unreadable tables (`Z-W1-S12`: 8035_JP, BZLFY_US, HEI_US, SNPS_US, TSM_US, V_US)** -- a round-10 cell: read each
   layout and extend the rule, or serve ABSENT with a per-name reason, stated.
4. **`Z-S55` (cases-report grades an underscore key ABSENT instead of refusing)** -- a small round-10 cell: the CLI refuses a
   key that resolves to no landed stamp.

## 3. FWD GRADES

- **`FWD-12`: NOT REALIZED -- the data half is MET, the render half is not this project's.** The team's cases are served,
  cited and split by case; "render as the team's ... in the slot" happens on AMGT_RESAPP's page (and DSGN_AMGTV1's).
- The others stand as `i-5` recorded them.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 10 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **Case unit carries its claim** (ruling 1) | `unit_as_written` + `currency` / `currency_basis`; the dossier rewrite under a pair |
| 2 | **Team-vs-rule Base census** (ruling 2) | read-only; distribution + denominator; ADBE named |
| 3 | **The 6 unreadable tables** (ruling 3) | per-name layout read; extend or ABSENT with reason |
| 4 | **`cases-report` refuses an unresolvable key** (`Z-S55`) | a planted underscore key is the positive control |

Cells 1 and 3 share the dossier write surface and one pair; 2 and 4 are LOCAL and independent. Cap 8 not pressed.

## Compiler Tools

The CVO's own `read_dossier` reads over 8 names and 7 block reads taken as the measurement; `r9_k2_blocks_after.txt`
(`served 69`) read against this seat's own pre-act `cases-report` diff (0 lines, @`0fbb50e84e`).
