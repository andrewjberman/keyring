# BRIEF for Andrew -- what the estimates data actually looks like for Peers V

**From** `4.0.0_SA_CRO~Z`, 2026-09-18. **Ask:** his own, relayed by `1.0.0_SA_CTO~Z` msg 23656 --
*"vendor egress is authorized, issue that to 4.0.0_SA_CRO~Z to go check out and also we will always be able to find
peers, I will answer that once ive better seen the shape of the data."* **This is that shape.** It recommends no
measure, cuts no cell, writes to no pool and schedules nothing.

---

## 1. The answer in one line

**With egress authorized, Peers V computes today for 30 of the 34 covered names, using the measure exactly as
written.** The binding constraint was never the estimate fields. It was that 224 of the 1,658 landed peer rows carry
a numeric identifier nobody had resolved -- and Bloomberg resolves them directly.

---

## 2. What was run

| | |
|---|---|
| act | ONE ad-hoc `ReferenceDataRequest` per chunk, 313 securities in 8 chunks, read-only |
| when | 2026-09-18, 13:2x-13:4xZ |
| fields | the 16 in `peers_v.FIELDS`, plus `NAME`, `TICKER`, `EXCH_CODE` as identity controls |
| overrides | `BEST_FPERIOD_OVERRIDE=BF` and `EQY_FUND_CRNCY=USD` -- the module's own constants, not this seat's choice |
| subjects | the 34 security keys under `derived/model_block/` in `opal-data-harvest` |
| peers | the newest landed `peers/v1/<key>/` object per subject |
| not done | no producer, no schedule, no pool write, no cadence, no cell. Nothing landed anywhere |

---

## 3. The subject side: the fields are there

Coverage over the 34 covered names, counting a value that came back at all:

| field | of 34 | | field | of 34 |
|---|---|---|---|---|
| `CRNCY_ADJ_MKT_CAP` | 34 | | `BEST_CUR_EV_TO_EBITDA` | 32 |
| `BEST_EPS` | 34 | | `BEST_EBITDA` | 32 |
| `CF_DECR_CAP_STOCK` | 34 | | `EV_TO_T12M_SALES` | 32 |
| `GICS_SECTOR_NAME` | 34 | | `PE_RATIO` | 31 |
| `EQY_FUND_CRNCY` | 34 | | `TRAIL_12M_EBITDA` | 31 |
| `BEST_PE_RATIO` | 33 | | `CURRENT_EV_TO_12M_SALES` | 31 |
| `TRAIL_12M_EPS` | 33 | | `FREE_CASH_FLOW_YIELD` | 30 |
| `TRAIL_12M_DVD_PAID` | 33 | | `CURRENT_EV_TO_T12M_EBITDA` | 30 |

**The three fields that blocked this are all present:** `BEST_PE_RATIO` 33 of 34, `BEST_EPS` 34 of 34,
`TRAIL_12M_EPS` 33 of 34.

**Run through `peers_v`'s own `compute_measures`, the subject's own row supports:**

| measures computable for the subject | names |
|---|---|
| all six | 25 |
| five | 5 |
| four | 1 |
| three | 2 |
| two | 1 |

**Where a measure is missing it is honest, not broken.** Banks and insurers return no free-cash-flow yield and no
EBITDA or sales multiple (HSBC, ICICI, Zurich); Boeing has no trailing P/E because trailing EPS is negative; the two
ADR lines (Petrobras, Roche) refuse several fields with an explicit *"field not applicable to security"*.

---

## 4. The peer side: this was the real blocker, and it is an identity problem

Across 191 landed peer sets there are 1,658 member rows, of which **224 carry a numeric ticker** such as `688910` or
`677172` rather than a symbol. Resolving only the symbol-shaped ones, **Peers V would serve 12 of 34** -- most
subjects fell under the eight-peer floor.

**Those numbers are SEDOL stems, and Bloomberg takes them directly.** Measured, with a positive control:

```
/sedol/688910    -> TAIWAN SEMICONDUCTOR MANUFAC   ticker 2330   exch TT
2330 TT Equity   -> TAIWAN SEMICONDUCTOR MANUFAC   ticker 2330   exch TT     <- same values, both routes
/sedol/6771720   -> SAMSUNG ELECTRONICS CO LTD     ticker 005930 exch KS
```

Re-run with both routes, **258 of 279 distinct peer securities resolved to a named security**, and 2 further rows
were dropped because the returned name disagreed with the name the peer set carried -- the control that stops a peer
being priced as the wrong company.

---

## 5. What serves, and what does not

**30 of 34 covered names would serve a Peers V score today.** The four that would not, each for its own measured
reason:

| name | why not |
|---|---|
| KDDI (`9433_JP`) | its landed peer set has ZERO members |
| ICICI Bank (`ICICIBC_IN`) | zero members, and only two measures compute on its own row |
| NVIDIA (`NVDA_US`) | peer set has 7 members; the floor is 8 |
| BB Seguridade (`BBSE3_BZ`) | 10 peers resolve, but only 2 measures clear the six-peer floor across them |

**None of those four is an estimates problem.** Two are empty peer sets, one is a set one member short of the floor,
and one is an insurer whose peer group does not support the measures. That is a peer-construction question, not a
vendor question.

---

## 6. What this does and does not settle

**It settles the factual half.** *"We will always be able to find peers"* holds: with egress authorized and SEDOL
resolution, the measure as written produces a score for 30 of 34 names, and the substitution the producer's own
source text warns against -- a trailing field standing in for an estimate field -- is not needed for any of them.

**It does not settle what YOU asked to decide.** The measure-definition question is still yours: whether Peers V
should serve on 30 and stay ABSENT on 4, whether a name with fewer measures should carry a narrower labelled score,
and whether an empty peer set is a bug to fix or a genuine ABSENT. This brief deliberately stops there.

**Three things this brief is not.** It is not a producer -- nothing was written to any pool, and the landed
`peers/v1` objects are untouched. It is not a cadence -- one ad-hoc pull, no schedule, and the standing moratorium
plus your own separate reservation on the Bloomberg pull cadence are both intact. And it is not a round-14 cut --
round 13 is still held on CARD 5, and nothing here changes that.

---

## 7. Reproduce

`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/CLAUDE_COST_REPORT_20260917/` holds this seat's other instruments; the
two scripts behind this brief are `peers_shape.py` (peer-set census, S3 only) and `peersv_shape2.py` (the pull and
the measure computation, using `peers_v`'s own functions). Both are read-only and take no arguments. The raw
Bloomberg response is kept in the session scratchpad, not committed: it is vendor data, and this brief carries the
measurements taken from it rather than the payload.
