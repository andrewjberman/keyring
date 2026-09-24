# AMGT Lead Panel B01 -- PRE-10:00Z HOUR-AXIS CAPTURE + the `dated` type-boundary measurement

**`3.0.0_SA_CVO~Z`, 2026-09-24 02:39-02:42Z.** **NOT a grade.** No mandate has issued for Lead Panel and
no pinned candidate exists; the proposal `CLOSER_PROPOSE_LEADPANEL_20260924.md` @`d2bbf82b3f` awaits
Andrew's word.

## WHY CAPTURED NOW

`1.0.0_SA_CTO~Z` flagged the acceptance matrix's **HOUR AXIS** as *"load-bearing and the part a grader
would most likely collapse"*: the chatter producer runs at **10:00Z**, so the same unchanged fact renders
two different screens either side of it. **This capture is the BEFORE half.** It was taken at 02:39Z and
cannot be retaken -- the window closes at 10:00Z each day and the underlying generation moves.

Same reasoning as the Peers pre-build baseline (`99f8d35d37`): a before-state not measured before the
change can only be taken on the changing party's word afterward.

**INSTRUMENT:** direct `lambda invoke` against deployed `opal-amgt-scoped-api`
(`CodeSha256 DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`), synthetic API Gateway v2 event, firm header
present.

## THE CAPTURE, 2026-09-24T02:39:48Z

| route | HTTP | `dated` | `requested_as_of` | rows | `generated_at` |
|---|---|---|---|---|---|
| `lead-panel/rankings/trending/chatter` | 200 | **TRUE** | `2026-09-24` | 2 | `2026-09-24T02:39Z` |
| `lead-panel/rankings/breakout/chatter` | 200 | **FALSE** | `2026-09-24` | 0 | `2026-09-24T02:39Z` |
| `lead-panel/rankings/gainers/securities` | **400** | -- | -- | -- | refused: *"movement must be one of TRENDING, BREAKOU..."* |

⭐ **The 400 is the control**: the instrument refuses an invalid movement rather than answering 200 to
everything, so the two 200s are answers and not artifacts.

**Full served key set on both 200s:** `as_of_date`, `axis`, `coverage_vintage`, `dated`, `empty_reason`,
`generated_at`, `generation_id`, `generation_row_count`, `payload_hash`, `ranking_reason`,
`ranking_status`, `read_attempts`, `requested_as_of`, `resolution`, `row_count`, `rows`, `rows_read`,
`run_id`, `state`.

## THE `dated` GAP IS A TYPE-BOUNDARY DROP, NOT A ROUTE GAP

The proposal states *"`dated` and `requested_as_of` are absent from `RankingSet`"*. **That is correct.**
The mechanism measured here is sharper than absence:

- **THE ROUTE EMITS BOTH** -- `dated` and `requested_as_of` are on the served payload above.
- **THE CLIENT TYPE OMITS BOTH.** `types.ts:181` `RankingSet extends Partial<GenerationFields>` declares
  `axis`, `resolution`, `as_of_date`, `rows`, `row_count`, `ranking_status?`, `ranking_reason?`,
  `rows_read?`, `read_attempts?`, `generated_at`. `GenerationFields` at `:93` declares `generation_id`,
  `coverage_vintage`, `payload_hash`, `state`, `generation_row_count`, `run_id?`, `empty_reason?`.
  **Neither carries `dated` or `requested_as_of`**, and a search over 986 files finds no ranking-payload
  use of either name.

⛔ **So the information a reader needs in order not to be misled by a fresh `generated_at` IS ALREADY
COMPUTED, SERVED AND PAID FOR, and is discarded because the client never models it.** The remedy is
client-side -- extend the type, render it -- not a producer or route change. **The 2026-09-29 fallback
expiry can therefore be made VISIBLE without touching anything that serves.**

⭐ **`empty_reason` IS in `GenerationFields`**, so the 189-of-191 `NO_SIGNAL_IN_WINDOW` reason **can**
reach the client even though `dated` cannot. That asymmetry matters when the hour-axis case is graded:
one half of the explanation is modelled and the other is not.

## LIMITS -- STATED BECAUSE I OVERRAN THIS EXACT BOUNDARY EARLIER TONIGHT

- I measured **(a)** that the deployed route emits both fields and **(b)** that the type declarations at
  HEAD omit them. ⛔ **I did NOT trace the adapter or the panel.** So this does **not** show the panel
  would render them if the type carried them, and does **not** show the type is the ONLY place they are
  lost. **ROUTE-PROOF IS NOT RENDER-PROOF; this is not render evidence.**
- **The edge is not exercised.** Direct invoke bypasses CloudFront and `auth-validator-edge`.
- **The after-10:00Z half is NOT captured** and is the other half of every hour-axis case.
- **Two observations, explicitly NOT findings:** `trending/chatter` returned **2** rows where the
  proposal's SLB note speaks of **32** -- different axis-date and window, so this is not read as a
  discrepancy and is not raised as one. And the null-`security_key` SLB row that **must not navigate** is
  **render-level and outside anything this instrument can reach**.

## WHAT THIS IS FOR

If a Lead Panel mandate issues, the after-10:00Z half is graded **against this capture**, not against
recollection, and no case exercised at one hour only is credited.
