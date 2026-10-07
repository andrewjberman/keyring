# Never-widen half request, MDPF_SECCLASS -- the Holdings producer falls back to `CUSIP:<security_id>` after a symbol miss (TO-SC-e56, S27, folds R8 SC-e-39)

**Author:** `0.9.0_WK_MDPF_SECCLASS~38` (worker, L7), 2026-10-07, for `2.0.0_SA_COO~M1` to issue to IRPT_BCKEND's release path and halves (the CTO ruling). **Status: COO half UNSIGNED; CTO half UNSIGNED.**
The ship, the release and any publish are the issuer's and IRPT_BCKEND's acts, never the worker's. The worker edited one shipped gold file on its branch, ran fixture tests and a read-only before-list, uploaded nothing and published nothing.
Records: round-8 analysis section 3 S27 (REMEDIATION_v6): "YES. After a symbol miss the producer falls back to `CUSIP:<security_id>` (C-IDENTITY: the CUSIP rows exist for exactly this). It is a served move under never-widen."; R8 `SC-e-39` folded into R9 `SC-e-56` (laptop 1.0.0_SA_CTO msg 106191, relayed by 0.0.0_AB_MSTR~DELL1 msg 213); surprise rows `MDPF_SECCLASS-W38-S6`, `-S7` (this order's findings, both bear on this half).

## The act

Merge branch `wk-MDPF_SECCLASS-38` (`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` and `tests/test_holdings_cusip_fallback.py`) into a pushed range after both halves sign, then release through IRPT_BCKEND's path. `data/assets/scripts/gold/` is a shared repo home the pre-push deploy gate ships (`.tools/safe_deploy_core.py` `shared_repo_homes`), so the branch stays off every pushed range until both halves sign.

**The candidate diff** (`git diff 5d70aab6c9..wk-MDPF_SECCLASS-38 -- data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`), one file, three changes:
1. `classify_security(ec, clf, ticker, name, description=None, security_id=None)`: after the canonical lookup by symbol misses, a node whose `security_id.namespace` is `CUSIP` is looked up as `CUSIP:<VALUE>` (upper-cased) in the same canonical `etf-classifications` table; a hit is served exactly as that row holds it (`asset_class_basis` TABLE, `class_source` `etf-classifications`); a miss goes to the bd-securities fallback as today. Order: symbol, then CUSIP, then fallback; never the reverse, never blended; a symbol hit never asks for the CUSIP key. The cash rule (checked first) is unchanged. New helper `cusip_key(security_id)`.
2. `annotate_classification` passes each node's `security_id` to `classify_security`.
3. `ASSET_CLASS_VALUES` drops `multi_asset` (the six-class rule: a canonical or fallback answer reading `multi_asset` is now refused loudly with `REFUSED`). Measured on both lookup tables 2026-10-07 by consistent full scans: `etf-classifications` 3,507 rows, 0 `multi_asset`; `bd-securities` 10,965 rows, 0 `multi_asset` (classes: equity 6,135, fixed_income 3,161, alternatives 1,654, cash 15). So the removal refuses nothing that exists today.

Tests: `test_holdings_cusip_fallback.py` 14 passed (the placement, the order, the symbol-hit-never-asks arm, the CUSIP-miss fallback, non-CUSIP ids ask no key, the `multi_asset` refusal, the census). `test_holdings_classification.py` 13, `test_holdings_unclassified.py` 5, `test_holdings_49f.py` 17, `test_holdings_inf.py` 14 passed. **Two older tests fail by design (row `W38-S6`, outside the order's paths, not edited):** `test_holdings_snapshot.py::test_every_published_asset_class_enum_is_the_producers_list` and `test_holdings_narrowed.py::test_a_canonical_multi_asset_row_is_served_not_refused` each assert the `multi_asset` admission this change removes; the release seat must have those two tests (and, for the first, the published contract enum in `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`) put on the six-class rule before the branch merges, or the repo-wide drain fails. `test_holdings_snapshot.py` 29 passed / 1 failed (that one); `test_holdings_narrowed.py` 5 passed / 1 failed (that one); base was 30/30 and 6/6.

## Blast radius

**Keys the act may touch.** The producer writes, per firm and as-of, `irpt/<firm>/gold/holdings/date=<as_of>/<revision>.parquet` and `irpt/<firm>/platinum/holdings/date=<as_of>/<revision>.json` in each firm's own bucket (`opal-data-49financial`, `opal-data-cottonwood`, `opal-data-inflection`), and advances the verified `latest.json` index only after validation (`holdings_snapshot.py` `land()` / `HoldingsPublication`). Revisions are content-addressed and immutable, so a changed classification is a NEW revision object plus the pointer move; no existing revision is rewritten. Which firms a release run covers is the release's own scope: the act names all three; inflection's list below is zero.

**Writers counted (N printed):** per firm, the Holdings snapshot's one writer is `holdings_snapshot.py` through `publication.HoldingsPublication` (N = 1 for each of the three firms; read from `land()`, the producer's one landing function -- other writers of these keys were not swept for). The writer's own rule was read: the lookup order in change 1 above, with the validation and reconcile gates (`validate_snapshot`, `reconcile_before_after`) unchanged.

**The before-list: what the CUSIP step newly places** (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/HOLDINGS_CUSIP_NEWLY_PLACED_20261007.json`, built by `R11_CHECKS/holdings_cusip_newly_placed.py`; **claim `inferred`**: the held set is the Holdings producer's own LOCAL build, run without `--upload`, one parquet per firm, the latest built date per firm, because the firm buckets deny this box's principal; the table reads are DynamoDB consistent reads. `sc_e56_newly_placed_check.py`: `SC-E56-NEWLY ok=True firms=3 of 3 listed=238 false_entries=0 control=present`). A newly placed security is a distinct held SECURITY node (cash line excluded) whose symbol key is absent from `etf-classifications` (or empty) and whose `CUSIP:<value>` key is present.

| firm | build as-of | held securities | newly placed | USD |
|---|---|---|---|---|
| 49financial | 2026-10-05 | 1,941 | 51 | 7,239,921.61 |
| cottonwood | 2026-10-05 | 1,453 | 187 (round 8 held 187) | 22,864,368.78 |
| inflection | 2026-10-02 | 1,601 | 0 | 0.00 |
| total | | | 238 | 30,104,290.39 |

**Value delta, measured with the real classifier** (the same two lookup tables, the symbol-only call against the symbol-then-CUSIP call, for each of the 238; local, no write): of the 238, the class does NOT change for 233 (the fallback already answered the same class; only `class_source` moves from `bd-securities-fallback` to `etf-classifications`, and the sub-class becomes the CUSIP row's). The class CHANGES for five 49financial securities:

| firm | served today | served after | securities | USD |
|---|---|---|---|---|
| 49financial | fixed_income (fallback) | structured (canonical CUSIP row, Hedge) | 1 | 1,922,557.00 |
| 49financial | unclassified (fallback) | equity (canonical CUSIP row) | 3 | 459,369.34 |
| 49financial | fixed_income (fallback) | equity (canonical CUSIP row) | 1 | 3,197.64 |

(Unchanged class, source moves: 49financial alternatives 1 / 610,595.32; equity 5 / 500,742.88; fixed_income 40 / 3,743,459.43; cottonwood fixed_income 186 / 22,864,368.78 and equity 1 / 0.00.) Nothing becomes unclassified.

**Readers of the served Holdings snapshot** (a name census by `comp-find`, then the serving handler read; not every reader read line by line):
- `infra/aws/lambda/investor-reporting/holdings/snapshot.py` (+ `entry.py`, `stage.py`): the handler that serves the projection; it "SERVES; NEVER BUILDS" and validates against the HoldingsSnapshot contract.
- `portal/src/api/endpoints/investor-reporting.ts` and the wire/adapter layer `portal/src/pages/InvestorReporting/contracts/{adapt,validate}.ts`, `contracts/wire/HoldingsSnapshot.ts`.
- The Holdings tab readers of `asset_class` / `sub_asset_class`: `tabs/holdings/{HoldingsTab,HoldingsSummary,HoldingsTreemap,AllocationBars,DrillTree,SecurityList,classTotals,slices}.ts*`; the class-reader tests under `__tests__/dsgn-irptv1/` (including `iv-e-148.multi-asset-class-readers.test.ts`, whose subject the six-class rule retires).
- `portal/src/api/endpoints/advisor-intelligence.ts` (named by the same census; its Holdings use was not read).
- Readers outside the repo: BLIND.

## Branches (both covered)

**Branch A -- the ship lands and a release run publishes:** the next Holdings build per firm serves the 238 above by their CUSIP row, the five class changes as tabled, and nothing else changes: nodes, weights, totals and the reconcile are classification-independent (`reconcile_before_after` gates the publish). The release seat's FIRST step is the local re-run: `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/holdings_cusip_newly_placed.py` (a laptop seat the firm buckets admit may pass `--build`) and `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/sc_e56_newly_placed_check.py` must print `ok=True`; a count far from 238 or any `false_entries` stops the release.
**Branch B -- the ship lands and the branch's two older tests were not put on the six-class rule:** the repo-wide drain fails on those two tests before any publish; nothing is served. This is the ARMED hazard on row `W38-S6`, disarmed by the release seat granting the two tests and the contract enum (or by the CTO ruling the six-class rule off for the enum).
**Branch C -- no release run (the code on `CLOUD` only):** nothing served moves; the held snapshots keep their prior revisions.

## Rollback

Rollback per key: each firm's served snapshot is an immutable revision; the act's only mutable write is the `latest.json` pointer (and the index it verifies). The release seat records each firm's pointer value (`revision`, ETag/VersionId) before the run; rollback re-points `latest.json` at that recorded revision (the prior revision object is untouched), per firm, so a firm that publishes badly rolls back alone. The code rollback is the revert of the merge commit, which restores the symbol-only lookup and `multi_asset` in one unit. No other key is touched.

## Acceptance (after the act, if run)

1. A GET of each firm's served snapshot (through the handler) reads the 238 listed securities with the class and sub-class of their `CUSIP:` row; the five class changes tabled above read as stated; `asset_class_basis` stays in its published enum.
2. `by_class_source` in the producer census counts the newly placed under `etf-classifications` (238 across the three firms at the same as-of).
3. Node count, custody total and the reconcile equal the pre-act revision to the cent.

## COO half -- UNSIGNED

## CTO half -- UNSIGNED
