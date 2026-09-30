# NEVER-WIDEN HALF REQUEST -- Holdings Narrowed Canonical Release (IB-mr-291, CTO RULING 103169)

**Cell:** IB-mr-291. **Issuer:** `2.0.0_SA_COO~M`. **Built by:** `0.9.0_WK_IRPT_BCKEND~93` (TO
`IRPT_BCKEND.TO-IB-m29-291.holdings-narrowed-canonical-release.md`). **Class:** SERVED (a published
Holdings classification value changes for real securities in production once applied and drained).

Andrew, ~05:0xZ: "PHYS is Commodities / Metals but it continues displaying in Alternatives." This is
the NARROWED release the CTO ruled admissible while the full canonical migration (IB-mr-251..272)
stays HELD.

## The act

Change `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`'s security classifier from
a single source (`data/black_diamond/scripts/gold/lib/etf_classifier.py`, reading `bd-securities`) to
TWO, tried in order, for every SECURITY node on every firm's Holdings build:

1. **CANONICAL FIRST.** `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`'s
   `ETFClassifier`, reading the cross-firm `etf-classifications` table (2,309 rows measured
   2026-09-30). A ticker the table holds is served EXACTLY as the row holds it (`asset_class`,
   `sub_asset_class`), no hedge fold, no guess.
2. **THE DECLARED FWD-6 FALLBACK**, for every other ticker:
   `data/assets/scripts/gold/investor_reporting/bd_securities_fallback.py`, a byte-for-byte copy of
   the pre-SC-t-1 BD library (`git show 1f327f52a2:data/black_diamond/scripts/gold/lib/etf_classifier.py`),
   reading `bd-securities`, unchanged in logic, basis order, mirror-refusal or the cash rule (CTO
   101547).
   - **Owner:** `2.0.0_SA_COO~M`.
   - **Reason:** the canonical table does not yet cover every security the three firms hold (measured:
     1,171 / 9,370 / 3,121 securities per firm below still resolve through the fallback).
   - **Sunset:** retired together with the fallback branch in `classify_security` when MDPF_SECCLASS
     E8 and E9 land (the canonical table's coverage completes) -- tracked as the still-HELD
     IB-mr-251..272 chain, not reopened by this act.
   - Declared in both modules' own headers (see `bd_securities_fallback.py` docstring and
     `holdings_snapshot.py`'s classifier-section comment) and here.

Which table actually answered a given node is tracked ONLY in this producer's own manifest census
(`annotate_classification`'s new `by_class_source` key: `etf-classifications` / `bd-securities-fallback`)
and in this cell's own deliverable census below -- **never served on a node.** The published contract
(`docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`) is `additionalProperties:false`
on every node with a fixed `asset_class_basis` enum with no `CANONICAL` member; widening it is outside
this cell's write grant and is recorded as row `IRPT_BCKEND-W93-S1` (OBSERVATION, INERT, disarmed
same-turn) rather than cut here. A canonical-table hit is therefore served with the EXISTING
contract-legal basis `TABLE` -- the same value a fallback ticker-table hit already used, since both
are, definitionally, a direct ticker-table lookup.

**BOTH BRANCHES, both covered by this half:**
- **Canonical-hit branch:** `asset_class`/`sub_asset_class` change to the table's value for any ticker
  where the table and the old fallback disagreed (the "moves" below). No node becomes `unclassified`
  that was classified before (measured: `to_unclassified` = 0 at every firm, denominator = every
  SECURITY node in that firm's build -- 120,944 / 34,347 / 15,355).
- **Fallback branch:** unchanged behavior, byte-for-byte, for every ticker the canonical table does
  not hold -- same four layers, same mirror-disagreement refusal, same cash rule.

## Pre-release census (condition 2)

Real local builds, all three firms, against the LIVE `etf-classifications` table (2,309 rows at build)
and each firm's normal business date (2026-09-28, the last trading day). File:
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R29_NARROWED_CENSUS_20260930.json`. Verified:
`python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R29_CHECKS/r29_narrowed_census.py` ->
`NARROWED-CENSUS 49financial=6503/1171/120944 inflection=569/9370/34347 cottonwood=1061/3121/15355`
(moved/fallback/securities).

| Firm | Securities | Moved | Fallback | To unclassified | GLD | PHYS | VXX |
|---|---|---|---|---|---|---|---|
| 49financial | 120,944 | 6,503 | 1,171 | 0 / 120,944 | commodities/Metals | commodities/Metals | structured/Hedge |
| inflection | 34,347 | 569 | 9,370 | 0 / 34,347 | commodities/Metals | (not held) | structured/Hedge |
| cottonwood | 15,355 | 1,061 | 3,121 | 0 / 15,355 | commodities/Metals | commodities/Metals | structured/Hedge |

All three carry `class_source: etf-classifications` for GLD/PHYS/VXX -- condition 4 (PHYS, GLD, VXX
read from the table) is met at every firm that holds them (inflection does not hold PHYS).

**Largest moves by weight (fraction of firm total AUM), every move is `alternatives -> {commodities|
structured}` -- the fallback's `hedge`-shaped guess for gold/volatility products, corrected by the
canonical table's direct answer:**
- cottonwood PHYS: weight 0.5820%, 0.3366%, 0.1584%, 0.1244%, 0.1082% (five largest holdings)
- 49financial VXX: weight 0.0321%, 0.0127%, 0.0120%, 0.0105%, 0.0080% (five largest holdings)
- inflection VXX: weight 0.0243%, 0.0218%, 0.0195%, 0.0166%, 0.0150% (five largest holdings)

Every other move in the 8,133 total (6,503 + 569 + 1,061) is the same two tickers (GLD, PHYS, VXX)
repeated across accounts -- no other ticker in the canonical table's 2,309 rows disagreed with the
fallback's answer for a ticker any of the three firms actually holds.

## Blast radius

**WRITERS counted: 1.** `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` is the
ONLY definition of `asset_class_basis` in the estate (comp-find `"asset_class_basis"` DEF band = 1
hit) and the only producer of the Holdings PLATINUM/GOLD artifacts this act changes. One writer, one
rule read: this half.

**READERS, every one:**
- `portal/src/components/holdings/HoldingsBreakdownTable.tsx` (`holding.asset_class`,
  `holding.sub_asset_class`, `subAssetBg(...)`) -- the Holdings UI table Andrew's complaint names;
  groups securities into asset-class buckets (Equity, Fixed Income, Alternatives, Commodities,
  Structured, Cash, Other, Unclassified). PHYS/GLD move OUT of the Alternatives bucket and INTO
  Commodities; VXX moves OUT of Alternatives and INTO Structured.
- `infra/aws/lambda/investor-reporting/_contracts/tests/test_holdings_classification_members.py` and
  the mirrored lambda-tree contract copies (`infra/aws/lambda/investor-reporting/_contracts/` and
  `.../holdings/contracts/HoldingsSnapshot.schema.json`) -- schema conformance readers only, unchanged
  by this act (no new enum value, no new node field).
- No other portal page, Lambda or gold script reads `asset_class_basis`; `comp-find` denominator: 61
  hits total, of which 1 DEF (this producer), the rest are the three mirrored contract copies, QA/diff
  fixtures under this same project's own deliverables, and this cell's own tests.

**LOCAL CANDIDATE DIFF** (the candidate change set in this worktree, uncommitted to the shared branch
until this half signs):
- NEW: `data/assets/scripts/gold/investor_reporting/bd_securities_fallback.py` (the declared fallback)
- NEW: `data/assets/scripts/gold/investor_reporting/tests/test_holdings_narrowed.py`
- CHANGED: `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (classifier section,
  `annotate_classification`), `.../tests/test_holdings_classification.py`,
  `.../tests/test_holdings_snapshot.py` (repaired fixtures, no assertion weakened, one assertion
  added: `class_source`)
- CHANGED: `.tools/safe_deploy_core.py` `_IRPT_HOLDINGS_CLOSURE` (fallback module + shared client
  replace the BD library)
- CHANGED (DESIRED, NOT APPLIED): `infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf`
  (`CanonicalClassifierLookup` statement, GetItem/Query on `etf-classifications` + its two GSIs, for
  each firm's Holdings principal)
- Whole `investor_reporting` test suite: 319 passed (was 30 failed / 268 passed / 16 errors before this
  act -- MDPF_SECCLASS's SC-t-1 thread had broken it, row `MDPF_SECCLASS-S3`)

**What this act does NOT touch:** IB-mr-251..272 (the full canonical migration, still HELD); any
security's classification for a ticker NEITHER table holds (still `unclassified`, unchanged); any
non-Holdings consumer of `bd-securities` or `etf-classifications`.

## Rollback per key

- **Code (`holdings_snapshot.py`, `bd_securities_fallback.py`, `.tools/safe_deploy_core.py`):** `git
  revert` the landing commit. The BD library (`data/black_diamond/scripts/gold/lib/etf_classifier.py`)
  is untouched by this act (read-only via `git show` during this build) and needs no rollback itself.
- **IAM (`holdings_refresh.tf`):** the added `CanonicalClassifierLookup` statement is additive
  (GetItem/Query only, no resource it did not already reach is newly reachable by another actor) --
  rollback is `terraform apply` with the statement removed, or leaving it in place is harmless (no
  Scan, no write) if the code rollback already happened first.
- **Served output (the firm buckets):** rollback is a re-run of the PRE-narrowed code against the same
  `as_of`, re-publishing the same revision-addressed Gold/Platinum keys through the existing
  compare-and-set index (`HoldingsPublication`) -- no delete, no key reused for two different bodies.

## Release order (condition 3's own halves + this one)

1. **This half + the CTO/CRO/COO sign-off** (never-widen class, this document).
2. **The IAM apply** (`holdings_refresh.tf` `CanonicalClassifierLookup`), under its own ledger entry.
3. **The drain** of this worktree's commits into the shared branch.
4. **The Holdings package re-mint** (`2.0.0_SA_COO~M`'s act -- the daily-runner bundle picks up the
   new closure members).
5. **The served after-read** of PHYS, GLD and VXX at all three firms (whichever the firm holds),
   which `2.0.0_SA_COO~D` shows Andrew directly against the LIVE served snapshot, not this local
   census.

This act is separate from IB-mr-251..272's still-HELD halves (condition 3): those cover the full
canonical migration and are not reopened, touched or gated by this release.
