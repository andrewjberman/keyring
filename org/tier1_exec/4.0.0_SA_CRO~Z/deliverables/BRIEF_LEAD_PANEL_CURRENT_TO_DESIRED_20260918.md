# BRIEF -- the Lead Panel, from current to desired

**From** `4.0.0_SA_CRO~Z`, 2026-09-18, at Andrew's ask: *"write a brief on how to get us from current to desired."*
**To** `1.0.0_SA_CTO~Z`, who owns AMGT_RESAPP from L2 to L4. **Status:** a BRIEF. It creates no gate, cuts no order,
and spends no decision that is Andrew's. Where it names an owner, that owner's limb is unchanged.

> **CORRECTION, 2026-09-18 14:5xZ -- this brief first shipped @`d07d76b1ea` with CARD 5 listed as OPEN. It was not.**
> Andrew answered CARD 5 **YES at 13:09Z, verbatim "yes do it"** (record
> `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260918_1309Z_CARD5_AMGT_RESAPP_YES.md` @`ad2d1253be`),
> about 90 minutes before this brief was committed, and `AMGT-rk-22` was spawned the same turn and is producing.
> Caught by `1.0.0_SA_CTO~Z` (msg 23675) before Andrew acted on it. **The cause is this seat's:** the card's state
> was carried from a 03:4xZ read into a 14:4xZ brief without re-reading the register at write time. A brief that
> re-asks a ruled decision reads as the fabric not listening. Every sentence below that depended on it is fixed
> and marked.

---

## 1. Where the panel stands, measured 2026-09-18

Read from the live table `opal-harvest-security-metrics`, the code at HEAD and the site-Z scheduled tasks.

| list | last committed | state |
|---|---|---|
| Trending x Chatter | 18 Sep | COMPLETE, 10 rows -- **but see UPDATE 1: all ten carry ZERO articles and score 0, ranked alphabetically. The list looks full and carries no signal.** |
| Breakout x Chatter | 18 Sep | EMPTY, 0 rows, every day 15-18 Sep; the pointer carries no reason. UPDATE 1: all 191 names fail the 3-mention floor, because the article store holds almost nothing |
| Trending x Price | 15 Sep | COMPLETE, 32 rows; three trading days stale |
| Breakout x Price | 15 Sep | COMPLETE, 32 rows; three trading days stale. UPDATE 1: 23 of the 32 are FALLING names, down to -9.2%, listed as breakouts |

- **Chatter is scheduled:** EventBridge `cron(0 10 * * ? *)` UTC fires the `chatter-axis-producer` Lambda daily.
- **Price is not:** `integrations/bloomberg/research/price_axis_pull.py` has no leg in
  `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`, so it has run only by hand.
- **Refresh** is wired end to end and REFUSED by the adapter, because no queue exists to receive it.
- **The security-mode posture line** serves 2 of 33 names today. CARD 5 is ANSWERED (YES, 13:09Z) and
  `AMGT-rk-22` is producing, so this figure is expected to move; it is today's served state, not an open ask.
  ~~(The round's own model-figure denominator is 34 keyed names; 33 is the posture population.)~~ **STRUCK: the
  keyed population is 33 for every line; the 34 was retracted by its author (msg 23693). See section 11.1.**
- **No user can open the page:** DEV builds and deploys nothing, DEV CI is red the same way it was on the previous
  run, and a production promote was never in scope.

**The architecture is sound and should not move.** Producers rank once, commit a generation behind a `_CURRENT`
pointer, and the panel only selects. Every gap below is in RUNNING it, not in its design.

---

## 2. Three decisions still Andrew's (CARD 5, first listed here, is already answered)

Nothing in section 4 that depends on these should be built ahead of his word. Each is a card, not a gate this brief
invents.

| card | the question | what it unblocks |
|---|---|---|
| **A. Price cadence** | May the price puller run DAILY as a leg of the existing Bloomberg job? Law says a production pipeline must be scheduled; his standing reservation on the Bloomberg pull cadence says the cadence is his. The two meet here. | Both price lists going daily; the price half of the chart |
| **B. Price jump floor** | What minimum move counts as a price Breakout? Chatter's floor is 3 mentions; price has NO ratified floor, and `movement_gate.py` refuses to invent one. | A price Breakout list that is not led by trivial moves |
| ~~**C. CARD 5**~~ | **ANSWERED YES by Andrew at 13:09Z** -- not a question for him. `AMGT-rk-22` is producing now. | Posture line moving from 2 toward 33; round 13 now held on rk-22 LANDING (a mechanical gate), with rk-26 behind it |
| **D. Promote** | Put the page in front of users. **Refined per msg 23675:** `3.0.0_SA_CVO~Z` ruled "PUSH DEV NOW. HOLD PROD." (msg 23668). A PROD promote moves served output, so it first needs a CTO+COO never-widen pair naming its blast radius, and none exists yet -- Andrew should not be asked to authorize an act the fabric has not made signable. The DEV push is merged at `625a0888` and waits on the integrator. | The panel existing for anyone |

---

## 3. Measure before building -- four read-only checks, none of them a cell

Cheap, and each one decides what the build is. They can run now, inside the round-13 freeze, because they change
nothing.

1. **Why is Breakout x Chatter empty?** The pointer cannot say, so measure it directly: for the 250-name union
   universe, count each name's daily article history in the pool over the last 30 days, and run the Breakout math
   by hand for one day. Two answers are possible, and they lead to different work. If the baselines are thin, the
   fix is a BACKFILL -- Andrew's own 2026-09-11 ruling said the 30-day window "means we have to backfill". If the
   baselines are full and nothing crossed the floor, the list is HONESTLY EMPTY and the only fix is saying so.
2. **Does starring work?** A star, a read, an unstar and a read on DEV, confirming the firm comes from the
   verified header and never from the browser. **NOT ROUTED (msg 23675):** a real login is a person's credential,
   not something a seat exercises on its own, so this waits on Andrew or on a test identity he names.
3. **Header coverage.** Description and feed were not measured. Read both across the 33 keyed names so the header
   carries a denominator, not just the posture 2-of-33 figure.
4. **Why DEV deploys nothing.** Read the portal DEV pipeline end to end, and separate the red CI (pre-existing, its
   own item) from the deploy step that does not run.

---

## 4. The build, in dependency order

All of this is round-14 material, cut by `2.0.0_SA_COO~Z` after round 13's slug and the round-13 analysis --
except item 1, which is an operations change rather than a cell. Round 13 is now held on `AMGT-rk-22` LANDING,
with `AMGT-rk-26` behind it by its own text -- a mechanical gate, no longer a decision.

1. **Price goes daily** (needs card A). Add a leg to `scheduled_daily_pull.cmd` following that file's own
   leg-isolation pattern: its own exit code, gated on the verified-DAPI flag, and unable to fail a sibling leg.
   **WARN: site-Z scheduled tasks run the working tree, so saving that file IS the deploy.** Open a change-management
   entry before the edit and close it on the first measured daily commit. The as-of date comes from
   `lib/trading_calendar`, T-1, never `BDay`.
2. **Every empty day says why.** One field, `empty_reason`, added to the pointer by BOTH generation writers
   (`chatter_axis.py` and `price/generation.py` share the contract), carried through the adapter, and shown on the
   panel. It separates "nothing jumped" from "not enough history" from "the run refused", which today all read as
   0 rows.
3. **Chatter backfill, IF check 1 says so.** Thirty days of per-name daily article counts from the pool, written as
   the baseline the Breakout math reads. A one-time act with its own co-sign, because it writes to the pool.
4. **Price floor lands** (needs card B) in `movement_gate.py`, the one place the movement math lives, and nowhere
   else. `MIN_ABSOLUTE_JUMP_BASIS` flips from ABSENT to RATIFIED with his citation.
5. **Refresh gets a queue.** An L4 question first, owned by the CTO: what the queue is, what "queue the harvesters
   for one name" means per harvester, and what the panel shows while a refresh is pending. Only then an L5 cell.
   The Andrew-direct of 2026-09-11 already fixed that refresh stays separate from starring.
6. ~~**DEV deploys, and CI goes green** as its own owned item, then a page check on DEV with a real login across all
   four lists, both views and security mode -- and only then card D.~~ **STRUCK: nothing deploys to DEV by design
   (section 9.2), so there is no DEV page to check. Red CI stays its own item; the only path to a user is the PROD
   promote, deferred by Andrew (card D).**

**The chart needs no work of its own.** It shows as many points as there are committed days, so it fills in once
items 1 and 3 have run for 30 trading days.

---

## 5. Done means measured, not merged

| component | closed when |
|---|---|
| Price lists | COMPLETE pointers for both price lists on two consecutive trading days, dated T-1 by the trading calendar |
| Breakout x Chatter | either non-empty rows on a real jump day, or an EMPTY pointer whose `empty_reason` reads "no name crossed the floor" -- both are correct outcomes |
| Empty reasons | an EMPTY pointer on each producer carrying the field, and the panel rendering it |
| Price floor | `MIN_ABSOLUTE_JUMP_BASIS` = RATIFIED with Andrew's citation, and a Breakout list that respects it |
| Refresh | one click on DEV returns `queued: true`, and the harvesters are seen running for that one name |
| Header | description, posture and feed each counted over 33 names, at a named read time |
| Reachable | a user outside the fabric opens the page with their own login |

---

## 6. Traps named in advance

- **Do not cut round 14 before round 13's slug.** The refuser counts open orders per project, so an early cut
  deadlocks round 13's close (LD-0521). Round 13 is held on rk-22 landing today, CARD 5 having been answered.
- **Do not calculate Breakout on the page to fill the empty list.** Re-ranking at render time is what the whole
  design forbids, and it would put an invented list on screen under a real name.
- **Do not call price "stale" without counting trading days.** 16-18 September are trading days, so it is stale
  today; a Monday read of a Friday list is not.
- **Do not transplant the chatter floor of 3 onto price.** Three what -- dollars, percent, points? The module
  refuses exactly this, and it should keep refusing until card B.
- **No monitor, alarm or freshness checker** comes out of this brief. The standing moratorium holds; the daily
  commit IS the signal.

---

## 7. What this brief does not ask for

No seat is re-tasked, no scope is widened, no cadence is set, and no card is answered. The four checks in section 3
are offered to whichever seat the CTO routes them to; this seat will take any of them if asked.

**Evidence:** the 12 `_CURRENT` pointers read from `opal-harvest-security-metrics` on 2026-09-18; the EMPTY pointer
for `BREAKOUT_CHATTER#2026-09-18` read in full (no reason field); `infra/aws/terraform/harvest/chatter-axis-schedule.tf`
at `cron(0 10 * * ? *)`; `scheduled_daily_pull.cmd` with no price leg; `movement_gate.py`'s declared-ABSENT price
floor; the refresh route's stated refusal in `amgt-lead-panel.ts`.


---

## 8. UPDATE 1, 2026-09-18 ~15:1xZ -- the deep dive found the chatter side is hollow, and Andrew decided three cards

Andrew-direct at this terminal, recorded verbatim in
`ANDREW_DIRECT_20260918_15xxZ_LEAD_PANEL_DECISIONS.md`: *"Please update your brief with your updated findings as the
gaps are discovered."* This section is that update. Section 1's first read called Trending x Chatter healthy. **That
was wrong, and it was wrong because it read the pointer's STATE rather than the rows under it.**

### 8.1 The findings

**F1. The chatter article store carries three names.** `publication-links/v1/` in `opal-data-harvest` holds
prefixes for exactly **3** names -- BA, COST, HD. Run through the producer's own reader over the 30-day window, **188
of 191 names have ZERO articles, all reads complete**; the busiest name has 3. For AAPL, NVDA, MSFT, JPM and TSLA the
all-time count is zero and the reader has no lookup key at all. **The chatter subject is not starved of history; it is
starved of SOURCE.** No window, backfill or floor fixes that.

**F2. Trending x Chatter is a tie at zero, presented as a ranking.** The live 18 Sep generation
(`20260918T100026Z-efd7e544dd59`) has ten rows -- 2317 TT, 2602335D US, 9433 JP, 992 HK, AAPL, ABBV, ABT, ADM, AEP,
AIG -- every one with `window_total_count` 0 and `score` 0. They are simply the first ten keys in alphabetical order.
The pointer reads COMPLETE and the panel shows "the ten most talked-about names". **This is the most misleading state on
the panel, because it is the one that looks finished.**

**F3. Breakout x Chatter's empty list has a reason -- the producer computes it and discards it.** Run in dry-run for 18
Sep (writes nothing), the producer excludes **191 of 191** names with the reason `BELOW_MIN_ABSOLUTE_JUMP`. The reason
exists in memory at write time; only the pointer omits it. So build item 2, the `empty_reason` field, is cheaper than
section 4 implied: it writes down what the producer already knows.

**F4. Breakout x Price lists falling names as breakouts.** The 15 Sep generation ranks all 32 names by percentage move
against the trailing mean, with no floor and no sign test: 23 of 32 are NEGATIVE, from -0.05% to -9.2%, and all 32
appear. Each row carries `min_absolute_jump_basis: ABSENT_NOT_RATIFIED`, which is the module telling the truth about
why. Card B below closes this.

**F5. Trending x Price is sound.** It ranks the 30-day window return (`WINDOW_RETURN_PCT`), from +19.3% (PBR) down to
-15.0% (ASML). Staleness is its only gap, and card A closes that.

### 8.2 The decisions

| card | Andrew's word | what it now means |
|---|---|---|
| **A. Price cadence** | "Yes we should just get prices as of prior day on the existing BBG job." | APPROVED. Price joins `scheduled_daily_pull.cmd` as an isolated leg, as-of T-1 by `lib/trading_calendar`. Build item 1 is unblocked; `1.0.0_SA_CTO~Z` sequences it. |
| **B. Price floor** | "go with your rec here." | APPROVED AT THIS SEAT'S RECOMMENDATION, stated here at the moment of adoption: **a price Breakout requires a POSITIVE move of at least +5% above the trailing 30-day mean; anything smaller or negative is excluded, and a day where nothing clears it is an honest EMPTY.** On the one measured day (15 Sep) that leaves 3 of 32 names, at +7.2%, +9.9% and +10.9%, and removes all 23 declines. It lands in `movement_gate.py` as the price entry of `MIN_ABSOLUTE_JUMP`, basis RATIFIED citing the decision record. It is one constant: two weeks of daily price runs will show whether +5% is too tight. |
| **C. CARD 5** | "Card 5 I still don't know what that refrs to." -- then, asked in plain words: **"yes that's what I meant"** | **CONFIRMED ~15:3xZ.** The 13:09Z approval stands; the scope question is closed. Originally recorded here as: NOT RECOGNISED -- put back to him, not treated as confirmed. CARD 5 is: run the two producers that write management commentary and the posture read across all 33 covered names (today 5 and 2). It makes model calls, estimated in the low single digits of dollars. `2.0.0_SA_COO~Z` recorded a "yes do it" at 13:09Z as the answer and `AMGT-rk-22` began producing on it. Whether that yes was meant for this is his to say. |
| **D. Promote** | "the Promote can wait." | DEFERRED. Nothing is prepared toward it. |

### 8.3 What the build list becomes

1. **Price goes daily** -- approved (card A).
2. **Every empty day says why** -- cheaper than first stated (F3): write the reason the producer already computes.
3. ~~Chatter backfill~~ -- **WITHDRAWN.** F1 shows the problem is source coverage, not history depth; a backfill of an
   empty store backfills zeros.
4. **Price floor lands** -- approved at the recommendation (card B).
5. **Refresh gets a queue** -- unchanged, L4 first.
6. **DEV deploys and CI goes green** -- unchanged; the promote itself is deferred (card D).
7. **NEW, and the largest item on the panel: chatter needs a source.** The harvester that writes
   `publication-links/v1/` covers 3 names. Until it covers the universe, both chatter lists are empty or hollow. First an
   L4 question for `1.0.0_SA_CTO~Z`: which harvester is meant to cover these names, why it reaches three, and whether the
   gap is ingestion (nothing fetched) or association (fetched but not keyed to the name -- the empty lookup keys on
   AAPL and NVDA point here).
8. **NEW: Trending must not rank a zero.** A name with no chatter should not appear on a "most talked-about" list, and a
   day where nobody has chatter should read EMPTY with its reason -- the same honesty the Breakout list already has.

**Evidence for this update:** the producer's own dry-run for 2026-09-18 (`compute_chatter_axis`, `write_fn=None`); its
`default_daily_article_counts` over ten sample names; the `publication-links/v1/` prefix listing; the live
`TRENDING_CHATTER`, `BREAKOUT_PRICE` and `TRENDING_PRICE` generations read row by row from
`opal-harvest-security-metrics`.


---

## 9. UPDATE 2, 2026-09-18 ~15:2xZ -- header coverage measured, and DEV was never meant to deploy

The two checks `1.0.0_SA_CTO~Z` routed back to this seat (msg 23675), plus the CARD 5 wording.

### 9.1 Security-mode header coverage, over the 34 keys under `derived/model_block/`

| header line | served or present | source, and why the rest are missing |
|---|---|---|
| **Description** | **12 of 34** served | Measured with the adapter's OWN `read_description`. All 12 come from the drafting document's `company_description` section. The model-block route never serves: `CIE_DES`, the one description scalar the adapter looks for, is on 0 of 34 blocks -- the model-block pull does not request it. |
| **Posture** | **33 of 34** objects in `posture/v1/` | Up from 2 served this morning: `AMGT-rk-22` is landing them now. Served count follows once the adapter reads them; not re-measured on the served plane here. |
| **Management** | **12 of 34** objects in `management/v1/` | Also rk-22, still landing. |
| **News feed** | **3 of 34** | The SAME source gap as chatter (F1): `publication-links/v1/` holds BA, COST and HD only. |

**Two new gaps from this.** (9) The description's primary route is dead: adding `CIE_DES` to the model-block pull's
field list would serve a one-line description for every covered name without any model call -- the cheapest fix on
the whole panel, and it needs only a field added to an existing pull. (10) The news feed and the chatter lists are ONE
gap, not two: both read `publication-links/v1/`. Build item 7 closes both.

### 9.2 Why DEV deploys nothing -- by design, not by fault

Read from `portal/.github/workflows/`: `ci.yml` runs on `DEV` and has NO deploy step; `deploy.yml` runs ONLY on
`PROD` and is the one workflow that syncs to S3 and invalidates CloudFront; `promote-to-prod.yml` prepares the PROD
pull request. **There is no DEV environment to deploy to.** So build item 6 rested on a false premise and is
restated: the red CI on DEV stays its own owned item, and the ONLY path to a user is the PROD promote -- which Andrew
has deferred (card D) and which first needs a CTO+COO never-widen pair. A "page check on DEV with a real login"
cannot happen because nothing serves DEV; the page can be exercised only locally or after a promote.

### 9.3 CARD 5, in the words Andrew actually saw

The label "CARD 5" was fabric shorthand; Andrew met it first in this brief and did not recognise it. The question
`2.0.0_SA_COO~Z` put to him at 13:09Z, read from the commit @`ad2d1253be`, was in plain words:
*"Run the management/posture producers over the full 33-name keyed population? (yes/no)"* -- and he answered
*"yes do it"*. That is the same act this seat re-asked him in plain words. `1.0.0_SA_CTO~Z` (msg 23680) reads it as a
label that did not land rather than an approval not given, and says so as a reading; this seat agrees and still
treats it as his to confirm. **Lesson carried forward in this series: every card is named by its QUESTION, never by
its number, in anything Andrew reads.**

---

## 10. UPDATE 3, ~15:3xZ -- CARD 5 confirmed; state at hand-off to the next panel

Andrew confirmed in plain words that the 13:09Z "yes do it" meant exactly the management/posture run across the
covered names. That run is complete: management 5 -> 14 names, posture 2 -> 33, verified by `2.0.0_SA_COO~Z` on a
fresh instrument (msg 23682). Round 13 now waits only on `AMGT-rk-26` landing. The posture and management lines in
section 9.1 should be re-read on the SERVED plane once rk-22 drains; they are pool counts here.

**Open on this panel, carried forward:** card A (prices daily) with `1.0.0_SA_CTO~Z` to sequence; card B's floor to
land in round 14; the chatter/feed SOURCE question at L4; the `CIE_DES` field; Trending must not rank a zero; the
Refresh queue at L4; the promote deferred. The series moves to the THESIS panel at Andrew's word.

### 10.1 Cards A and B, as sequenced by `1.0.0_SA_CTO~Z` (msg 23684) -- this corrects section 8.3

Section 8.3 called card B round-14 material. **`1.0.0_SA_CTO~Z` takes the opposite view and is right:** both A and B
are direct Andrew words on the same message, neither is a round-13 cell, and LD-0521 bars cutting round N+1 before
round N's slug -- it does not bar a sovereign-authorized direct act. The reason A cannot go first is measured, not
procedural: the price puller writes BOTH price lists from one pull, and `movement_gate.py` returns
`(True, "NO_RATIFIED_ABSOLUTE_FLOOR")` for every name when the price floor is `None`, with no sign test. **A alone
would turn a stale wrong list into a fresh wrong one every trading morning, and freshness lends a wrong list
credibility it did not have when it was three days old.**

The act, in order, as one sequence:
1. **B first:** `MIN_ABSOLUTE_JUMP["PRICE"]` set to the +5% rule with its basis flipped to RATIFIED -- and a SIGN test
   added, because the gate tests magnitude today, so "positive only" is a new clause, not just a number.
2. **The leg:** `:price_leg` after `:cons_leg`, its own `RC_PRICE` that never touches `%RC%`, interpreter `PY_AWS`,
   and **exit codes remapped to 80-83** -- the script's 0-3 collide with the models chain, which owns `1`. The as-of is
   already T-1 via `lib.trading_calendar.prev_trading_day`.
3. **A never-widen CTO+COO pair**, because both halves move served output (rows and the `_CURRENT` pointer).
4. **A change-management entry opened before the edit touches disk** -- on site Z the edit IS the deploy.

The executor is `2.0.0_SA_COO~Z`'s to name; the CTO half is written against the exact diff, not before it.

**One figure carried into round 13's drain:** management went 5 -> 14, posture 2 -> 33. Management may stop short for a
real reason -- it needs officer data not every name has -- but the drain should record WHY the other 19 stayed absent
rather than close the round reading "done".

---

## 11. UPDATE 4, 2026-09-18 ~16:2xZ -- the denominator is 33, and management follows the filing

Carried over from the Thesis panel (`BRIEF_THESIS_CURRENT_TO_DESIRED_20260918.md`), because two of its findings land on
this panel's header.

**11.1 Section 9.1 counted 34; the population is 33.** Its "34 keys under `derived/model_block/`" is the model store's
name set, which holds NVIDIA; the population of record is `crosswalk/v1/2026-09-15.json` `denominators.MEASURED = 33`.
Diffed by this seat against the crosswalk's MEASURED `model_key`s: the only difference is `NVDA_US_Equity`.
`1.0.0_SA_CTO~Z` retracted its own "34" the same hour (msg 23693) and re-measured the header on the SERVED plane, in the
page's own key shape:

| header line | served, over 33 | whose read |
|---|---|---|
| Description | 12 | `1.0.0_SA_CTO~Z` msg 23693 (agrees with this seat's 12 in 9.1, which never included NVIDIA) |
| Posture | **33** | `1.0.0_SA_CTO~Z` msg 23693 -- section 9.1's pool count is now SERVED |
| Management | **12** | `1.0.0_SA_CTO~Z` msg 23693; matches `2.0.0_SA_COO~Z`'s correction of section 10's "14" (@`6366933721`) |
| Any score carrying a value | 0 | `1.0.0_SA_CTO~Z` msg 23693; not re-measured here |
| News feed | 3 (BA, COST, HD, all keyed) | this seat, section 9.1 |

The "14" is explained by the listing: `management/v1/` holds 14 objects, which are 12 names plus two `_pool` files.

**11.2 Why management stops at 12 -- answering section 10.1's last paragraph.** The management roster is read from the
FILING's officer section, by contract C-EXEC-MANAGEMENT (`lib/research/management/roster.py:1-15`, `enrich.py:8`).
Measured today: **the 12 management names are exactly the 12 names with a drafted thesis; neither set has a member the
other lacks.** So the 21 absent names are the 21 with no filing identity, and management's coverage is the Thesis
panel's coverage. The Thesis brief's tier 1 adds six 20-F rosters with no management work, provided each clears one of
the roster's three declared shapes. Bloomberg's `COMPANY_EXEC_OFFICERS` is populated for those 21. **Using it would make
Bloomberg a second roster authority, which changes C-EXEC-MANAGEMENT's ratified text: an L4 question for
`1.0.0_SA_CTO~Z`, not a pull change.** This seat's research note first said otherwise and is corrected.

**11.3 Build item 9 (description), refined.** The adapter reads `CIE_DES` from the model block and finds it on 0
blocks. Bloomberg's long form, `CIE_DES_BULK`, is measured populated for all 21 keyed names without a filing
identity. Either field added to the model-block pull serves the description line for the names Thesis cannot reach;
`CIE_DES_BULK` needs the adapter to read it by that name too. Still the cheapest fix on the panel: no model call, no new
source.
