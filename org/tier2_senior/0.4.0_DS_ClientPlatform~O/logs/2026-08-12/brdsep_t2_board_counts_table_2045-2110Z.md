# 0.4.0_DS_ClientPlatform~O -- OPAL_BRDSEP.T2 board counts table + two gaps closed (2045-2110Z)

**archetype:** MEASURE
**secondary_archetypes:** VALIDATE

## Window summary

CTO's final ask for the board document: ONE consolidated clients/accounts/AUA-per-client table,
measured on one pass rather than stitched from six messages -- their words, *"that is how I got the
basis wrong twice today."* Delivered. Their population check caught a real error of mine, and
Andrew then closed a gap I had marked UNCOMPUTABLE by telling me where to look.

Two commits: @`7fb8a0f763` (table + population correction), @`ff7a985d3c` (Inflection households).

## The correction CTO's population check caught

**I had reported Cottonwood counts of 680 -> 926 accounts / 206 -> 223 relationships. Those are ALL
COTTONWOOD ACCOUNTS. The ruled AUA of $190,072,187.03 is ALL OPAL-STRATEGY ACCOUNTS ONLY.** Dividing
one by the other puts a $190M numerator over a 926-account denominator of which **602 accounts
contribute none of it** -- the same addition-across-populations error as the basis stitch, one level
down, and it would have produced the per-client figure the board was going to print.

**Corrected, scoped to the AUA population, with the AUA reproducing exactly as the check:**

| as-of | Accounts | Relationships | AUA |
|---|---:|---:|---:|
| 2026-06-09 | 307 | 162 | $166,517,928.12 |
| 2026-08-10 | 324 | 172 | $190,072,187.03 (ties to the ruled figure) |

**THE CONCLUSION INVERTS.** Measured Opal-book growth is **+17 accounts / +10 relationships**, not
+246 / +17. The larger pair was real but measured the WHOLE FIRM's onboarding ramp. On the correct
population the coverage-window change is **+$23,554,258.91 across +17 accounts** -- predominantly
market and inflow, **NOT onboarding**, which is the opposite of what the wrong denominator supported.

## 7,189 vs 7,190 -- resolved, neither stale

Not a row-vs-distinct artifact: in both tables rows equal distinct account ids. They are DIFFERENT
TABLES. `fact_acc` (the account dimension) = 7,189; `dim_balance` = 7,190; `dim_balance` carries
exactly one account absent from the dimension (`0035140799`) whose `net_mv_plus_cash` is **$0.00** --
which is also why the $0.00 AUA tie-out held at either count. **Use 7,189.** At 2026-04-01 both agree
at 6,683, so the divergence is end-endpoint only.

## Inflection households -- the UNCOMPUTABLE gap, closed by Andrew pointing at it

Andrew-direct ~2100Z, verbatim: *"we can definitely figure out inflection clients, just find those
548 accounts and pull HH IDs for all of them"*

**Households: 4 (2026-04-01) -> 266 (2026-08-10), +262. AUA per household $0.00 -> $545,033.45.**

I had marked this UNCOMPUTABLE because platinum -- the ruled AUA basis -- carries no client count.
**That was true and it was not the end of the question.** Orion silver carries `householdName`, and
`clientId` maps **1:1 to `householdName`** throughout (266 = 266 at both endpoints), so clients and
households are the same unit at Inflection.

**What makes this divisible where the Cottonwood count was not** -- the denominator is stable across
every constructible population:

| population at 2026-08-10 | Accounts | Households |
|---|---:|---:|
| all Opal-named | 600 | 266 |
| 7 crosswalked models (the platinum model set) | 595 | 266 |
| crosswalked, currentValue > 0 | 581 | 260 |
| crosswalked, `isActive` | 582 | 260 |

Six households across a 19-account swing.

**WHAT COULD NOT BE CLOSED, AND IT IS STRUCTURAL:** platinum's exact **548**-account set is not
reconstructible from Orion, which shows **595** on the same 7 models. Five filters tested
(`currentValue>0`, `isActive`, custodial-cash, `isFeeExcluded`, `isGlobalExcluded`); best reproduced
**3 of 7** per-model counts. The reason is not a missing filter -- **platinum's counts come from the
ECLIPSE model feed; Orion silver is the CUSTODY/positions feed.** Two sources, not expected to tie.
So numerator and denominator are from different feeds; disclosed rather than divided silently. Unlike
Cottonwood the denominator is insensitive to that choice -- the 260 variant gives $557,611.14, a
**$12,577.69 spread**. Recommended publishing the household COUNT and treating the per-household
dollar as indicative.

**Side finding on the account side:** two Orion models sit outside the crosswalk entirely --
`90/10 Opal Long Term/Ultra Short Term` (4 accounts) and `90/10 Opal Intermediate/Ultra Short Term`
(1 account), **$4,865,425.91** combined. **That is the same candidate-NEW-Opal-model class T1 found
being folded into `non_model`, now visible on the ACCOUNT side rather than the value side.**

## The delivered table

| Firm | AUA | Accounts | Clients / Households | AUA per client |
|---|---|---|---|---|
| 49 Financial (entire `08242234`) | $1,482,015,684.99 -> $1,736,948,738.65 | 6,683 -> 7,189 | 4,020 -> 4,268 | $368,660.62 -> $406,970.18 (+10.4%) |
| Inflection (Opal models, ruled) | $0.00 -> $144,978,896.75 | 0 -> 548 | 4 -> 266 households | $0.00 -> $545,033.45 |
| Cottonwood (all Opal-strategy) ruled | $0.00 -> $190,072,187.03 | 0 -> 324 | 0 -> 172 relationships | -- (zero denominator) |
| Cottonwood measured | $166,517,928.12 -> $190,072,187.03 | 307 -> 324 | 162 -> 172 | $1,027,888.45 -> $1,105,070.85 |

**Constraints recorded with the table:** do NOT sum the clients column (49F is clients by tax id,
Cottonwood is RELATIONSHIPS, Inflection is households -- three units); the Cottonwood ruled row has a
zero denominator so its per-client cell is arithmetic, not a measurement; and the Cottonwood measured
start applies TODAY's strategy assignment to the 06-09 snapshot, because assignment is only available
from today's bronze.

## Compiler Tools

| tool | call | result | note |
|---|---|---|---|
| none run this window | -- | -- | This window was pure measurement over parquet/JSON already synced in-session, plus arithmetic verification. No new source location, no code or infra change, no deploy. The comp-rail applies to SEARCH and INSPECTION; there was nothing to locate -- every artifact read here was found by comp-tools earlier in the session (`comp-estate` for the positioning key, `comp-find` for the relationship-grain collapse) and was already mirrored locally. |

**What worked:** hypothesis-testing the 548 rather than asserting a cause -- five candidate filters
run and reported as 3-of-7 best match, which is what established the gap is STRUCTURAL (two source
feeds) rather than a filter I had failed to find.
**What failed:** nothing this window. The prior window's `git log --author` artifact did not recur
(used the substring form).
**Gap found:** none new. The platinum-vs-Orion feed split is a property of the architecture, not a
defect, and is recorded as such.

## Current State

- **OPAL_BRDSEP.T2 COMPLETE.** Final deliverable @`ff7a985d3c` at
  `org/tier2_senior/0.4.0_DS_ClientPlatform~O/deliverables/OPAL_BRDSEP_T2_COTTONWOOD_STRATEGY_DECOMPOSITION_20260812.md`.
  Proof-of-spec VALID @`49437033e8`. Committed, NOT pushed (lanes commit, integrators push).
- **CTO has everything for the board document.** AUA table, counts table, per-client figures, and
  every population caveat. Their words: *"this is the last thing I need from you for the doc."*
- **No UNCOMPUTABLE cells remain in the counts table.** Inflection's two were the last, closed this
  window.
- Nothing held, no blockers, no open RAVC loops owed by me.

## Next Steps

- [`1.0.0_SA_CTO`] Board document assembly. Two things still open at Andrew and NOT adjudicated by
  me: whether the two leaf strategies count as Opal (moves the balance between $780,222.16 and
  $7,005,515.33), and whether to publish the per-household dollar or only the household count.
- [unowned, surfaced not claimed] The two `90/10 Opal ...` models outside the crosswalk --
  $4,865,425.91 across 5 accounts, 2 households. Same class as T1's `non_model` folding. Belongs to
  the crosswalk owner.
- [unowned, carried from the prior window] 26.5% of cot `fact_holdings` rows carry NULL Market Value
  with null Units and null accruals; reads as target-allocation template rows. Not diagnosed. Changes
  no figure -- the non-null rows tie exactly to platinum `partner_custody_total`.
