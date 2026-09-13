# POSN_ASTTAX -- ROUND 1 ANALYSIS, ADDENDUM A (L10, 1.0.0_SA_CTO~Z)

**archetype:** SCRIBE (ledger) · **written by** `1.0.0_SA_CTO~Z` · **2026-09-11**
**Supersedes:** the ROUTING of sections 2, 4 and 6 in `ROUND_ANALYSIS.round1.md` @`1eb5f44a2c`.
**Cause:** an Andrew-direct PURPOSE ruling (~07:1xZ, at the CVO~Z terminal) that landed AFTER the round-1
grade was committed, carried to me as `3.0.0_SA_CVO~Z` C-S3 @`4275402ec2` (msg 21257) -- a NEW channel row,
not an edit to C-S2, per append-only.

---

## A1. WHAT ANDREW RULED (a statement of PURPOSE, verbatim via C-S3)

> "ETFClassifier is basically a developing list of how we tag securities we own. We do not trade really
> fast or move through so many securities, so we basically just add things there as we need to in order to
> keep securities with proper capitalization, proper sub asset class, etc etc"

The registry is a CURATED TAGGING LIST -- low-churn by design, extended by a PERSON as the firm acquires a
security. It is NOT the single-source-of-truth ARCHITECTURE that both the CVO's slug and my round-1 grade
measured it against. ⚠ The correction is to the FRAME, not the measurements: every set figure stands
(DICT 136 / TABLE 285 / BOTH 116 / dict-only 20 / table-only 169 / union 305 / disagreement 189), the ZERO
value-level mismatches stand, and C-S1 stands entirely.

## A2. WHAT COLLAPSES -- do NOT route these to round 2; neither is a defect

- **"Give the seed a trigger" -- STRUCK.** For a list a person extends on acquisition, THE PERSON IS THE
  MECHANISM; there is nothing to schedule. My round-1 line "an instruction addressed to a person is not a
  mechanism" (carried from the slug) invents a requirement the purpose excludes.
- **"Account for the 169" -- STRUCK.** The 169 are NOT unexplained. The `updated_by` field attributes all
  285 with ZERO unattributed: 169 `seed-etf-constituents (1.0.0_SA_CTO~Z, Andrew-direct 2026-08-25)`, 59
  placeholder-name-sweep, 55 attr-restore-from-_shared, 1 vug-naming-fix, 1 canonical_si_seed. The dict
  (`etf_classification.py`, 136 entries) is a SUPERSEDED seed input that fell behind the table (285) -- not
  a competing "one place." **So round-1's headline "NEITHER end is one place" is wrong in emphasis: the
  TABLE is the one place** (the curated list serving reads via ETFClassifier); the dict is a retired input.

## A3. WHAT SURVIVES AND IS ROUND-2 WORK -- the corrected routing (replaces round1.md s.4)

Additive to a curated list, not a migration of something broken -- smaller and safer than round 1 framed it:
1. **Make UNKNOWN distinguishable from `equity` -- PRIMARY.** `equity` is both a real class AND the
   positioning lambda's unknown-default (`lambda_function.py:359`). Under Andrew's purpose (the registry
   exists to keep securities PROPERLY TAGGED), a bucket where "properly tagged equity" and "not recognised"
   are the SAME STRING is precisely what cannot be audited. The CVO would still cut this, and it matters
   MORE under his framing, not less. (Touches the positioning lambda's default, not only the registry --
   an implementation note for the decomp.)
2. **The additive vocabulary reconciliation (ratified FIVE vs stored THREE).** ADD Commodities and
   Alternatives to the stored vocabulary and move the SEVEN currently-`hedge` served tickers to ratified
   classes: SIX -> Commodities (DBC, GLD, GSG, IAU, SLV, USO); VIXY -> Structured (VXX likewise, per
   C-VOL-HEDGE-STRUCTURED, if it is ever a holding -- it is not one of the served seven today). ADDITIVE to
   the list, not a migration.
3. **`is_hedge()` reconciliation (C-S1, still ARMED, still mine).** Resolve as part of (2) -- populate or
   retire `HEDGE_TICKERS` per the reconciled vocabulary; the two access paths must stop disagreeing.
   Unchanged by this addendum; disarm still keyed to the reconciliation settling.
4. **Fill the THREE blank `sub_asset_class` rows -- the REAL coverage gap.** `sub_asset_class` is populated
   on 282 of 285 (31 distinct values: Information Technology 32, Financials 29, US Large Cap 25 ...); THREE
   blanks are the actual gap in what the registry exists to do. A five-minute job, not an architecture
   programme.

## A4. FWD-5 RE-GRADE (verdict UNCHANGED, rationale corrected)

FWD-5 ("The classification is defined in one place and flows everywhere") stays **NOT_REALIZED** -- but NOT
because no one place exists. The one place EXISTS: the table. It is NOT_REALIZED because its DONE WHEN bar is
EXERCISED ("someone changed where a class boundary sits and it flowed everywhere") and that has not been
exercised, and because the dict is a stale competing input still to retire and the equity/unknown collision
undermines "properly tagged." FWD-1..4 and FWD-6 grades in round1.md s.3 are UNCHANGED.

## A5. CHANNEL

C-S3 @`4275402ec2` (`3.0.0_SA_CVO~Z`, OBSERVATION) is the correcting row, filed append-only rather than as an
edit to C-S2 -- the correction is to reasoning, not measurement. C-S1 (is_hedge, BLOCKING, ARMED, disarm
mine) is untouched and carries forward exactly as round1.md s.5 records.

## A6. TO THE PRD

Andrew's purpose ruling lands as a PRD constraint at v0.4 so round-2 cells cut against the right frame -- the
same discipline that fixed C-VOL-HEDGE-STRUCTURED (a ruling that lives only in a message is reproduced wrong
by a cell author who reads only the PRD). The v0.4 bump re-opens the two L4-R sign-offs; the six
classification cells are UNCUT, so nothing is blocked -- the fix lands before they cut, which is the point.

**Push state:** LOCAL at write time. `0.0.0_AB_MSTR~Z` pushes.
