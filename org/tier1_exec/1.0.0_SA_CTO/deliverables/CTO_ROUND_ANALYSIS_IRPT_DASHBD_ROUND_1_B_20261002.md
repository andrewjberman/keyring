# IRPT_DASHBD round 1, workstream B -- the CTO's L10 analysis: round 2 is the served leg of FWD-1

**Author:** 1.0.0_SA_CTO, 2026-10-02 ~04:4xZ. **Input:** `2.0.0_SA_COO~P` msg 104051 and its drain-end record
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/IRPT_DASHBD_ROUND1_B_DRAIN_END_20261002.md` @cdd81865b6 (merge
@9000ce5a08). PRD v0.6 @aabc054e89, both halves current. Issuer `2.0.0_SA_COO~P`.

## 1. Accepted from the drain

Four of four cells are terminal with proofs re-run by the issuer. FWD-1 hop 1 (gold) is served; hop 2 (the platinum series file)
ran for real once, the served object's sha256 equal to a fresh rebuild; hop 3 (the read route) ran locally against the real
objects and is NOT served -- neither root is applied. The thread is NOT live. FWD-8 is not graded on agreement in round 1
(0 of 5 like-day pairs, PRD v0.6 ruling 23).

**The channel's compile is owed, not waived.** All 13 rows carry a disposition by ruling or amendment (the issuer's table), but
their `disposition` fields still read UNDER_INVESTIGATION and no CVO compile exists (watermark 0 of 13). This analysis does not
wait for it: `3.0.0_SA_CVO` compiles the channel in parallel, and any row the compile re-opens comes back to this seat as an
addendum to this analysis.

## 2. Names checked at this seat

The plan's names (`irpt-49f-reporting-publish-lambda`, `-role`, `-policy`, `-daily`) are `lib/opal_naming.name()` output:
`name("irpt", "49financial", "reporting-publish", <kind>)` returns them (the builder abbreviates the scope); the short scope `49f`
is refused by the builder, as row W1-S2 found. Rule 30 holds for the publish root.

## 3. The enrichment list round 2 cuts (ONE issuance, `2.0.0_SA_COO~P`)

| # | item | risk | ruled |
|---|---|---|---|
| E1 | **The served leg.** Apply both planned roots (`reporting-publish`: 7 to add, the schedule `cron(15 8 ? * MON-FRI *)` America/New_York; `reporting-read`: 8 to add, read-only on the platinum prefix) under ONE packet with both never-widen halves and one ledger. Then workstream F's signed-in page fetches one account's series through the route: that fetch is FWD-1's real run. | WORLD | YES, first. The 08:15 ET schedule is the production trigger (a success-of-upstream trigger would be a defect); the gold it reads is T-1. |
| E2 | **The retention family for `series.json.gz`** (row W1-S1). | SERVED | YES, as a registry question to the registry's owner (`infra/logic/registry/`), carried as one row; not a build cell in this round. The served file is not blocked on it. |
| E3 | **The 1,498.38 USD flow residual on 0027265115** (ruling 25; the fee matches to the cent). | LOCAL | YES, one read cell: name the leg (an in-kind leg valued differently, or a leg classed internal here and external at the vendor) from the landed responses; no vendor call. |
| -- | Like-day tie-out windows (ruling 23) | -- | CARRIED, not a cell: Andrew's per-use vendor word. FWD-8's tolerance stays his. |
| -- | Hygiene: empty staging directories in the worker's worktree | -- | At the drain, not a cell. The worktree and branch are removed on Andrew's word (a recursive delete). |

Each build order carries at most three mechanical criteria; E1's acceptance is the page's one fetch, read after the apply.

## 4. Outcome read

| outcome | state after round 1 | round 2 moves it to |
|---|---|---|
| FWD-1 | hops 1-2 real; hop 3 local; NOT live | live end to end on the signed-in page (E1 + workstream F) |
| FWD-8 | not graded on agreement | unchanged; waits on Andrew's vendor word |

-- 1.0.0_SA_CTO
