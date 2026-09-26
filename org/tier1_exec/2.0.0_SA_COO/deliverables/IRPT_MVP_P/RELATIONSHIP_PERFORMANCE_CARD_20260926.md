# Card -- relationship-level (multi-account) Performance: the FWD-1 live-thread defect

**Author:** `2.0.0_SA_COO~P`, 2026-09-26 ~15:1xZ. **Asks:** ONE ruling of `1.0.0_SA_CTO` on the set-level method
(section 4).

## 1. The defect, measured

The page selects whole directory entries, which are relationships and clients, and those hold several accounts. Every
multi-account selection answers `SELECTION_UNSUPPORTED`:
- ~D's admin+Dev walk HAR `prod-uiwalk-20260926.har` (sha256 6b51023c..): 4 of 4 Performance reads at 49F and COT
  answered HTTP 200 `ok:false`, UNAVAILABLE, SELECTION_UNSUPPORTED.
- The refusal is deliberate, at `infra/aws/lambda/investor-reporting/performance/retained.py:77-80` (backend
  @19d8f3038c): "performance computes exactly one selected account".

FWD-1's Performance hop is reachable today only through a one-account entry. Measured from each firm's published
directory at 15:1xZ (not-terminated entries):

| firm | entries | one-account | largest entry | entries > 25 accounts |
|---|---|---|---|---|
| 49F | 4548 | 2609 (57%) | 70 | 1 |
| COT | 258 | 82 (32%) | 24 | 0 |
| INF | 292 | 87 (30%) | 17 | 0 |

So 43% of 49F entries, 68% of COT's and 70% of INF's answer SELECTION_UNSUPPORTED. CTO 101236 names it P's hop, for the
round analysis.

## 2. What already exists

- **The contract carries a set.** `PerformanceReport.returns` has a set-level `summary_returns` / `period_returns` /
  `daily_cumulative_series` and an `account_detail` ARRAY, one row per account. No contract change is needed for a
  multi-account report.
- **49F (Opal engine):** `canonical/twr_daily` holds, per `(account_id, business_date)`, `r_net`, `bmv`, `emv` and
  `cf_net`. That is every input an asset-weighted daily aggregate needs, read and never recomputed. The engine lane's
  linker `parity_period_returns.link_account_period` rules neutral days and the spine for ONE account. No set rule
  exists yet.
- **INF (Orion):** the live-proven Scope body addresses a HOUSEHOLD (entity 5, row S143). A household scope returns the
  household's own aggregate, computed by Orion, beside its Account groups. A relationship that equals one Orion
  household gets a provider-computed set return for free.
- **COT (Black Diamond):** `performancePeriod` is per account today; BD computes aggregates for its own groups, but no
  capture pins that request.

## 3. Options

| | Set-level summary | Per-account detail | New method? | Size |
|---|---|---|---|---|
| **A. Aggregate + detail** | 49F: daily BMV-weighted return, `sum(emv - bmv - cf) / sum(bmv)` over covered accounts, linked by the engine's linker. INF: Orion's household aggregate when the relationship == one household. COT: parked until a BD group request is captured. | each account's own cell (today's one-account path, run per account) | YES for 49F: a set aggregation rule the engine lane has not ruled | 49F about a session; INF small; COT parked |
| **B. Detail only** | none: `summary_returns` stays absent with a named reason ("set-level return not computed") | each account's own cell | no | small, all three firms |
| **C. Keep the refusal** | -- | -- | no | the portal narrows the selection to one account first (a UX change in the portal, not here) |

The missing pieces are always named, never dropped: an account the engine cannot link is an `absence` in
`account_detail`, and the set summary discloses the covered denominator (`k of n accounts, $ covered of $ total`).

## 4. The ruling asked

**Recommendation: B now, A next.**
- B unblocks FWD-1's Performance hop at all three firms this round, with no new methodology. It is the per-account loop
  over today's proven one-account path, with the set summary absent by name.
- A is a METHOD decision: how a set return is formed from accounts. It belongs to the engine lane's ruling, since
  GIPS aggregation needs a stated rule for weighting, intra-day flows and accounts entering or leaving. It should not be
  invented inside the IRPT adapter.

**ONE ASK of `1.0.0_SA_CTO`:** rule B for this round, and route A's aggregation rule to the 49F engine lane (and to
Andrew if it is his to set). Or rule otherwise.

## 5. B, concretely (if ruled)

- **`retained.compute`:** a selection of n > 1 accounts runs the existing one-account computation per account (each
  retained as today, keyed by its own request).
- **Composition:** it composes ONE `PerformanceReport`:
  - `account_detail` = n rows;
  - `summary_returns` / `period_returns` / `daily_cumulative_series` omitted with a named reason in
    `optional_facts`;
  - `dates` = the intersection of the accounts' answered windows, disclosed.
- **Vendor calls:** COT's and INF's one-use plan gates stay per account, so a multi-account COT or INF request
  needs one plan per account. That is named, and no gate is widened.
- **Limit:** n <= 25 accounts per request; more refuses by name. That is 1 entry of 4548 at 49F (its largest holds
  70) and 0 at COT or INF.
- **Tests:** the per-account loop over the real repository; a mixed covered/uncovered set; the refusal above 25.
