# Session Log — 0.2.0_DS_PortfolioAnalytics — 2026-08-03 23:05–23:25Z (window 6)
**Archetype:** value-correction build under serve-hold (BUILT+EXERCISED+HELD, zero production writes)
**Project:** MDPF_GLOBAL.DC1.relationship-collapse-three-sites @80da654dc8 (CTO grant + serve-hold 230622Z)

## Summary

The urgent cot_total check (23:05Z, answered in ~90s: **fourth naive summer CONFIRMED to the cent** —
`channel_sources.py:446` reads only Market Value so it structurally cannot collapse; 07-31 measured
delta exactly $205,070.77; my own slice self-reported as the fifth) became the formal **DC1 TO**:
collapse to (AccountID, AssetID) at the three sites in my family, equality assert binding,
**BUILT-NOT-SERVED** — Andrew adjudicates the disclosure before any corrected value reaches serve
(DELTA≠0: the never-widen carve-out does not apply).

**Executed @3accc408f8 (DO-NOT-DEPLOY):** ONE mechanism — `collapse_relationship_grain` in
`build_dim_model_portfolio` (+ binding equality assert; NaN and value distinct states) — site 2
collapses before the per-account groupby, site 1 (slice) now reads the identity columns and imports
the helper, site 3 (pair firm_total) documented as pure inheritance (`values` = bdmp.account_values
output). Deployed copies untouched; tonight's cycle serves the status quo.

## Compiler Tools (DC1 mandate rows)

| Mandate `<run>` | Observed | vs `<expect>` |
|---|---|---|
| Read 3 sites @pinned; comp-blast (assets-tree-blind → hand-derived, labeled) | sites confirmed at vintage (slice read-block, dim `account_values` groupby-inside-account, pair `:124` inheritance via `import build_dim_model_portfolio`); consumers = the T1.C-mapped chain (dispatch 6d → accrual → publisher) | PASS — no moved site, no unexpected consumer, emitter site correctly excluded (AE's C1) |
| Scratch exercises (a)/(b)/(c) | **(a)** 07-31 delta **-205,070.77 EXACTLY** at sites 1+2+3 (470,263,647.64→470,058,576.87; z0927448821 410,141.54→205,070.77 == its own clean-day value); **(b)** clean-day 07-20 delta 0.00; **(c)** 07-22 anchor reproduces **457,984,488.00 EXACTLY** | PASS — every cell TIE-EXACT to 0.4.0's measured figures |
| Evidence package to CTO+COO; deploy HELD | delivered 23:24:13/23:24:24Z; TO open at HELD-FOR-ANDREW | PASS — hold in force, no override path |

**Beyond the mandate — the safety scan that made the assert bindable:** the slice iterates every
axis date nightly, so a single unequal historical dual pair would kill every future build. Scanned
ALL 42 live fact_holdings partitions (06-09..07-31): **0 unequal pairs** — every dual in history is
the equal-pair double-count class. Also pre/post captures at function level on 3 dates × all sites
(the C2 mutant-pair discipline, applied third time tonight).

## NEW FINDINGS (widen Andrew's disclosure scope; in the CTO package)

1. **The July window opened 07-21**, not the TO's 07-22 — every value-carrying day 07-21..07-31
   carries exactly +$205,070.77 (one account, two LP assets under two relationships, equal pairs).
2. **A second, LARGER, closed June episode:** 22 positions duplicated 06-10..06-21, value-carrying
   06-15..06-18 at +$338,815.93 / +$338,320.16 / +$336,128.28 / +$337,930.72 — and the LIVE served
   cottonwood artifact carries those naive-summed June custody points. Served-overstatement history
   = TWO episodes, not one.

## Open at my seat

1. **DC1 deploy leg: HELD FOR ANDREW** (fires on his word via CTO/COO; pre-registered read: first
   post-deploy cycle steps DOWN by the dual delta — expected, not regression).
2. Tonight's cycle read (3 pre-registered interpretations, unchanged — it serves the status quo).
3. Dim participation edit on CTO schema validation; T1.C row-12 on clock-v2 apply.
