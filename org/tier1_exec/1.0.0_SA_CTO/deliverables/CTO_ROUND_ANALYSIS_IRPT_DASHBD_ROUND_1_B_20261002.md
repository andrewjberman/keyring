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

## ADDENDUM 1 -- 2026-10-02 ~05:2xZ (self-drive tick 1): the gold has no clock; two compile findings placed

**Input:** `2.0.0_SA_COO~P` msg 104057 (row IRPT_DASHBD-S13 @76a5e50ed3); `3.0.0_SA_CVO` msg 104058 (compile 13 of 13 @662953e505,
ADJUDICATION_v1, REMEDIATION_v1). Round 2 is issued (@97eaff05ff: DB-b-5 the issuer's served act, DB-b-6 the residual read).

A1. **CORRECTION.** Section 3's "the gold it reads is T-1" is WRONG. `account_return_daily` ends at 2026-09-28 (559 partitions) and no
    clock fires its producer (row S13). An 08:15 ET publisher over it would republish the same 09-28 series every weekday: a
    scheduled job over an unscheduled input.
A2. **ROUND 2, RULED: DB-b-5 applies the READ root only** (8 resources, read-only on the platinum prefix). The publisher root stays
    planned and unapplied. FWD-1's real run is workstream F's signed-in fetch of the platinum series already served (as of
    2026-09-28), its as-of date shown with it. The issuer narrows its own act's packet; the decomposition is not re-cut.
A3. **ROUND 3, FIRST: DB-b-7, the adapter's scheduled fire** on the holdings-performance pattern (its own root, its own ledger,
    firing before the publisher), **then the publisher root with its 08:15 ET schedule**, in that order. Not added to round 2:
    mid-round the decomposition is frozen (Rule 27). Production pipelines are scheduled (CLAUDE.md section 5); ad hoc gold is QA.
A4. **IRPT_DASHBD-S6 limb (e), PLACED.** Foreign tax paid is not an external flow. The shared classification
    (`org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json`) puts FTP/FC/WD (2,449 rows) and
    FTR/FC/WD (4 rows) in EXTERNAL, and the served 49F engine reads it through `a05_ref_txn_classification.py`. The two codes move to
    internal (tax) in the file's owner's edit (`4.0.0_SA_CRO`), the served engine's read moves with it under its own packet with both
    halves (a served NNA change, about 15 USD a row), and the IRPT adapter's own override retires in the same act. A round-3
    enrichment line the issuer cuts with the CRO. INERT until then.
A5. **IRPT_DASHBD-S8, CARRIED.** `fact_trn` has no per-event key; the remedy is upstream in the Schwab ingest silver. The
    1,099-row upper bound on duplicates (0.034 percent) stays disclosed where it is. PARKED: owner the Schwab silver lane
    (`0.5.0_AE_OpalETL`, the 49-schwab-conv lane, not live); un-parks when that silver next changes, which then adds a per-event key.
