# DATA_ANALYTICS A1 -- the PATCH / OVERFIT REGISTER (v0.1)

**Purpose (Andrew-direct 2026-06-25):** the 49F gold layer is full of **defensive patches** -- broad-strokes downstream heuristics bolted on to work around sketchy 49F-migration data. DATA_ANALYTICS exists to **canonize the gold process properly, once and for all, WITHOUT these patches.** The correct data-quality strategy is to **excise the clear aberrant transactions at the SOURCE** (e.g. a $4B withdrawal is a data error to remove, not a signal to dampen) so every downstream calc is clean and needs no defensive logic. This register is the first-class A1 output that feeds A2/A3: the explicit "do NOT carry forward; fix the data at root instead" list.

**Author:** 0.4.0_DS_ClientPlatform, 2026-06-25 (A1 layer-walk). **Status:** v0.1 -- backfilled from the A/B/C-tier walk so far (A_00..A_04, B_00..B_03, C_00, C_01); extends as the walk continues (C_02..C_08, D-tier). The aberration-excision FIX SPEC is held pending Andrew's steer (curated known-bad-txn excise-list vs rule-based sanity-bound filter vs both).

---

## The classification doctrine (the load-bearing distinction)

Not every defensive flag is a bad patch. The register splits findings into two classes -- conflating them would wrongly strip honest labeling:

- **INAPPROPRIATE PATCH (excise-at-source candidate):** a downstream heuristic that works AROUND dirty/aberrant data instead of fixing it. The clean rebuild REMOVES it and fixes the root (chiefly: excise aberrant transactions; re-source from the custodian). 
- **LEGITIMATE (KEEP):** honest provenance/completeness labeling, or a genuine correctness fix. The clean rebuild PRESERVES it.

## The register

| # | Layer | The patch / flag | What dirty-data it dodges | Class | Clean root-fix |
|---|---|---|---|---|---|
| 1 | A_04 client_dimension | **90-day `active_accounts` flag** (full-scans all silver/transactions for a recent-activity heuristic) | sketchy 49F-migration accounts/txns -- broad-strokes "is this account real" | **INAPPROPRIATE (Andrew's named example)** | **Excise the aberrant transactions at source** (the $4B-withdrawal class); then the active-flag heuristic is unnecessary and is deleted (not optimized). |
| 2 | A_04 client_dimension | **inferred-tax-status keyword fallback** (`infer_tax_status_vectorized`: 401k/ira/roth string-match) | silver missing/blank `tax_status` | PATCH (mild) | Fix tax_status completeness in silver (the dimension source), not a gold keyword-guess. |
| 3 | A_00 accounts_dimension | **`Olivia Shin` hardcode** (single-entity hack) | one entity's broken record | **INAPPROPRIATE** | Fix the entity's source record / a general rule; no single-name hardcodes in gold. |
| 4 | B_00 canonical_holdings | **`NAME_ALIASES` hardcode** (3 ETF rebrand name->name maps) | vendor ETF name-history (rebrands) | PATCH (mild, but real aliases) | A silver name-canonicalization map / config, not a gold hardcode dict. |
| 5 | B_00 / B_01 / C_01 | **`bd_stale` FIFO-ghost handling + `is_ghost` flag** (zero-out / flag positions the custodian doesn't confirm) | BD FIFO reconstruction INVENTS positions the custodian denies | **INAPPROPRIATE (dissolves at root)** | **Re-source lots from the custodian-direct feed** (Schwab ULN/RLD, already read by B_02) and RETIRE the BD FIFO reconstruction (B_01) for custodian-covered books -- then there are no ghosts to flag. |
| 6 | C_01 canonical_nna | **`is_excluded` account-exclusion flag** | (TRACE PENDING -- legit business exclusion vs dirty-data dodge) | UNCLASSIFIED -> trace upstream | TBD on the trace. |
| -- | C_01 canonical_nna | `nna_clean` completeness-provenance flag | n/a -- honest "is the residual trustworthy" labeling | **LEGITIMATE (KEEP)** | none -- this is the honest-provenance the rebuild WANTS. |
| -- | C_01 canonical_nna | the `how='left'` join bugfix (Andrew 2026-04-14) | newly-opened accounts silently dropped | **LEGITIMATE correctness fix (KEEP)** | none -- a real bug fix, not an overfit patch. |
| -- | A_02 fee_rate_history | the `basis_points_1` dup-suffix column resolver | BD denormalized dup-suffixed columns | borderline (silver-belongs) | move the de-dup-suffix resolution to silver (the BD-denorm cleanup). |

## The headline: aberration-excision is the keystone root-fix

The single highest-leverage root-fix -- the one that dissolves multiple patches at once -- is **excising clearly-aberrant transactions at the source**:
- It removes the NEED for the **90-day active flag** (#1): clean txns -> the activity heuristic is moot.
- It makes the **NNA residual trustworthy** (C_01): `aua_residual = AUA_change - growth` is acutely sensitive to a single $4B-withdrawal aberration; excise it once and the residual NNA is clean without defensive `is_excluded`/flagging.
- It is distinct from business-row-filtering (Rule 17 / silver-no-field-slimming): excision targets PROVABLE data errors (clear aberrations / sanity-bound violations), with a documented + auditable rule -- NOT judgment-laden relevance filtering.

**Open decision (Andrew's Q2 -- shapes the A2 spec):** is the excision a **curated known-bad-transaction excise-list** (conservative, fully auditable, manual-add), a **rule-based sanity-bound filter** (magnitude/sign thresholds, e.g. |txn| > $Nbn or > X% of account AUA), or **both** (rules surface candidates -> curated list confirms)? This choice is the first A2 deliverable once chosen.

## Next (as the walk continues)
- Finish the C-tier (C_02..C_08) + D-tier walk, appending patch-register rows.
- Trace `is_excluded` (#6) upstream to classify it.
- On Andrew's Q2 steer: spec the aberration-excision step (the keystone fix) as the first A2 candidate.
