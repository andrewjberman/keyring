# `/closer propose` -- AMGT **Lead Panel** (B01 · L1-L4, W1, F1)

`1.0.0_SA_CTO~Z`, 2026-09-24 ~02:4xZ, on Andrew's word at this terminal with
`4.0.0_SA_CRO~Z`'s brief `LEAD_PANEL_END_TO_END_GAP_BRIEF_20260923.md` (+ `.evidence.json`).
**Andrew's word is needed for THREE things (§4). One item in the brief is REFUSED (§5).**

## 1. The propose gate -- satisfied, re-measured this hour

| condition | measured |
|---|---|
| **>= 2 rounds** | **12 distinct round families over 191 orders** on `AMGT_RESAPP` |
| **0 live journeys** | `E0 NOT_EVALUATED`; and `2.0.0_SA_COO~Z` filed a **blocker at 02:30Z** -- no browser connector, CDP 9222/9223 unreachable, no accessible admin+Dev session. **Confirmed by the owning seat, minutes ago.** |

## 2. The trace -- deployed bytes, 13 live invocations, nothing written

**10 hops: 4 WORKS** (2 route, 3 edge, 4 generation read, 10 watchlist read) · **3 INCOMPLETE** (1 = E0
unexercised, 5 chatter producer, 6 price producer) · **3 MISMATCHED** (7, 8, 9). Both deployed digests verified;
the chatter Lambda's bytes compared member-by-member against HEAD; a complete 22-pointer scan; the pull route,
function and queue depth read live. **Neither write route was called.**

⭐ **THE FINDING, AND IT IS THE OPPOSITE OF "BROKEN": "WHAT IS UNFINISHED IS THE WATER, NOT THE PIPES."** The
read path WORKS end to end for all four crosses, the series, the watchlist read and the firm gate. The panel
resolves, verifies row counts, refuses SHORT_READ/OVER_READ, and serves in producer order with identity on
every row.

## 3. ⛔ ONE DATED DEADLINE, AND IT IS FIVE DAYS OUT

**The price generations are 2026-09-15 and are served ONLY through the 14-day dated fallback. That fallback
stops finding them on 2026-09-29, after which Trending x Price AND Breakout x Price read ABSENT with NO ROWS.**
⛔ **AND THE SCREEN CANNOT SAY SO TODAY:** `dated` and `requested_as_of` are **not in `RankingSet`**, and the
panel's timestamp is `generated_at` -- *the adapter's clock at read time* -- so **a reader sees a fresh
timestamp over a list computed for 2026-09-15.** That is the worst of the five gaps because it is silent.

**The six steps, in the brief's order, with ownership measured against `CONTRACT.md`:**

| # | step | owner | granted? |
|---|---|---|---|
| 1 | **Live thread** (hops 1-4, 8 on today's data) | `2.0.0_SA_COO~Z` | yes; **identity is Andrew's input** |
| 2 | **Water in the chatter pipe** -- the H03 gold cutover (hop 5) | `2.0.0_SA_COO~Y` | **yes** (`metrics/{chatter_axis,generation_writer}.py`, `pool_reader.py`) |
| 3 | **`dated` on screen + overlay fallback** (hops 6b, 8) | `2.0.0_SA_COO~Z` | yes (portal rows + `scoped_amgt.py`) |
| 4 | **Price producer owner + run** (hop 6a) -- **before 09-29** | ⛔ **UNOWNED** | **no -- the terminal box's schedules are not a contract row** |
| 5 | **Refresh wired to its carrier** (hop 9) | `2.0.0_SA_COO~Z` for client+route; ⛔ **consumer trigger UNOWNED** | partial |
| 6 | **ABSENT beside EMPTY** (hop 7) | `2.0.0_SA_COO~Z` | yes |

⭐ **FOUR OF SIX STEPS ARE ALREADY OWNED AND CAN START ON "GO".** Only the **terminal-box triggers** are
unowned, and they block steps 4 and 5's proof.

## 4. What needs Andrew's word -- three items

**(a) THE BROWSER SESSION ENDPOINT** -- already filed as `~Z`'s blocker. Unchanged and shared with Peers/E0.
**An accessible permitted session or connection endpoint, NOT credentials.**

**(b) AN OWNER FOR THE TERMINAL BOX'S SCHEDULES** (the price pull, and `pull_consumer.py`'s drain).
**REC: `0.0.3_BG_BBGTerminal`**, the seat that owns that machine's Bloomberg surface -- the existing
`OPAL_BBGTML_daily_pull` family already lives there, so this is one more task beside its own, not a new
surface. ⚠ **The first scheduled fire is a PRODUCTION SCHEDULE and goes through the deploy ledger**
(`org/critical_paths/change_management/`), opened before and closed after.

**(c) THE PER-USE VENDOR WORD** for the two runs that call Bloomberg: the price pull, and the Refresh proof to
`LANDED`. See §5 -- this is broader than the brief states.

## 5. ⛔ REFUSED: the brief's reading that the price pull needs no vendor word

**The brief states:** *"Andrew's per-use word is not needed for a producer that already exists and pulls only
PX_LAST for the landed universe."*

⛔ **THAT IS REFUSED AND THE REFUSAL IS NOT DISCRETIONARY.** CLAUDE.md, hard stop: **"NEVER call an external
vendor API without Andrew's explicit per-use word -- availability is not authorization."** The price pull
reaches **Bloomberg DAPI at 127.0.0.1:8194**. It is an external vendor API call. **That the producer already
exists, is narrow, and pulls only `PX_LAST` are all arguments about MAGNITUDE, and the rule is not about
magnitude -- it is about AUTHORITY.** ⭐ **"It already exists" is the precise shape of "availability is not
authorization," which is the clause's own wording.**

**So BOTH Bloomberg-touching runs need his per-use word:** the price pull (step 4) and the Refresh proof
(step 5). The brief is right about Refresh and wrong about the price pull, in the **permissive** direction,
which is the direction that matters. **Nothing else in the brief is disturbed** -- this is one sentence, and
the hop it sits in is otherwise correct and useful.

⚠ **AND STEP 2's DEPLOY CARRIES THE NEVER-WIDEN PAIR** (CTO + COO halves) because it **moves served output**.
The brief says so and it is right.

## 6. Parked, on the record, not worked

The description source (a Bloomberg header field the block does not carry -- **Andrew's data-source call**) ·
`bloomberg_session_state UNKNOWN` (the terminal box's report, off this thread) · the **SLB** unresolved identity
(1 row of 32) · the chart's density, which follows from steps 2 and 4.

## 7. If Andrew says go

**No new contract:** Lead Panel is already **B01** in `CONTRACT.md` v1.0 with IDs `L1`-`L4`, `W1`, `F1`, and
`closer_contract` is now on all three D5 rows. The delta is **one ownership row** (the terminal-box schedules,
to whoever he names) plus **two MANDATEs** -- one for `2.0.0_SA_COO~Y` (step 2, the H03 cutover, its first
Lead-Panel-scoped mandate) and one refreshing `2.0.0_SA_COO~Z` (steps 1, 3, 5, 6) -- and one for
`3.0.0_SA_CVO~Z` carrying the acceptance matrix. **No task orders, no rounds, no recut.**

**Acceptance is the brief's, unchanged:** CROSSES {4} x VIEWS {list, chart, starred-only} x **HOURS {before
10:00Z, after 10:00Z}** -- ⭐ **the hour axis is load-bearing, because the producer runs at 10:00Z and the same
unchanged fact renders two different screens either side of it** -- plus SECURITY MODE {BA, PBR, **a null
`security_key` row (SLB) that must NOT navigate**} plus ACTIONS {star/unstar = W1, Refresh to LANDED = F1, his
word} plus FAILURE CASES {expired session, a SHORT_READ refusal, `read_completeness.complete false`, the
no-firm 401}.
