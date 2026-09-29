# IRPT_BCKEND round 25 -- workstream ~Y (Analysis) decomposition

Issuer `2.0.0_SA_COO~Y`, 2026-09-29 ~23:3xZ. **One cell, carried from round 24 by that round's amendment 3.**

## Why this round exists

Round 24's rectangle was two cells. The issuer cut `IB-yr-241` alone and committed it, which closed round 24's
issuance; `.tools/to-pipeline-gate.py` then correctly refused `IB-yr-242` as a SECOND issuance into the same round --
*"ONE ISSUER PER ROUND is keyed to the ROUND, never the serial (Rule 27)"*. Both cells should have been cut in one
issuance. The error is recorded in `IRPT_BCKEND_DECOMP_R24_Y.md` amendment 3; this round is its remedy, not a new
scope. **Nothing about the cell changed** -- only which round issues it.

## The cell

Walk-2 items **W2-04 and W2-05**, placed on this lane by `1.0.0_SA_CTO` 103026. The Analysis composer cannot resolve
or NAME a comparison before Add, so it prints a positional label and refuses only the cap and duplicates; it documents
its own gap at `GenerateComposer.tsx:20-25` -- ResolvedScope v1 *"carries no catalogue of selectable comparisons"*.

Both open questions were ruled before the cut, and neither is the worker's to revisit:

- **Shape -- CTO 103038**, on this lane's measurement that `_contracts/ResolvedScope.schema.json` is
  `additionalProperties: false` with 12 properties and 9 required: **ResolvedScope stays v1**; the catalogue is served
  by a **sibling scoped GET** under the existing `/api/scoped/investor-reporting/` family **behind the same authz guard
  and tenant check**; it gets **its own new `_contracts` schema (v1, `additionalProperties: false`)**; any new resource
  name is **builder output (rule 30)**.
- **Source -- CTO 103035:** the Opal model catalogue plus etf-classifications, and **no substitution to
  bd-securities** -- *"Andrew is retiring bd-securities, so a new reader of it is the fork he named."* A ticker neither
  source names **shows its ticker verbatim, never a positional label.**

| cell | item | outcome served | risk | worker | depends on | checks (base dry-run at CLOUD HEAD) |
|---|---|---|---|---|---|---|
| `IB-yr-242` | a sibling scoped GET serves the comparison catalogue -- the model catalogue's 4 entries joined to etf-classifications for ticker -> name -- behind the existing authz guard and tenant check, against its own new closed v1 `_contracts` schema; an entry named by neither source carries its TICKER VERBATIM | FWD-4 (W2-04/05: the page can resolve and NAME a comparison before Add, and refuse at Add) | WORLD (a new served route) | `~88` | none -- 103038 settled the shape, 103035 the source | `R24_CHECKS/test_r24_y2_catalogue_read.py`: `route_registered_under_the_scoped_family` FAIL, `catalogue_contract_is_closed` FAIL, `unnamed_ticker_is_verbatim` FAIL, `existing_surface_unchanged` **PASS** (control) |

**The battery keeps its `R24_CHECKS` name.** It is already committed and its base dry-run is already measured; renaming
a measured battery to match a round number is churn with no evidential value.

**The verbatim path is the COMMON case, and the cell says so.** `2.0.0_SA_COO~M`'s census
(`deliverables/IRPT_MVP_M/ETF_CLASSIFICATIONS_COVERAGE_20260928.json`) measured `etf_classifications` at **285 items**
covering 179 of 847 cottonwood and 228 of 1,449 bd tickers -- about **one in five**. So roughly four entries in five
take the verbatim path and it must read as deliberate, not broken. The coverage gap is `MDPF_SECCLASS`'s first need,
not this cell's.

**The control is the ruling.** `existing_surface_unchanged` asserts ResolvedScope still has its 12 closed properties
and no `comparison_catalogue` key, and that the existing `POST .../analysis` route still maps to `analysis-requests`.
A cell that put the catalogue on ResolvedScope -- the option 103038 rejected -- fails its own control.

Edges: none; `IB-yr-242` is a single independent cell. **fanout: 1 of 1 chains, cap 8.** Slot `~88`, measured per S197
(highest author 87, order 87, branch 84).
