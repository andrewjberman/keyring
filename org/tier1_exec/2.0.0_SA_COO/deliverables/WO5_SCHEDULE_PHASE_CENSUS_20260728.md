# WO-5 -- SCHEDULE / PHASE CENSUS

**Author:** `2.0.0_SA_COO` · **run 2026-07-28T225228Z -> T225xZ** · CTO spec @`3fa042158b` (Amendment 5)

**PREDICATE (the criterion, stated before the result):**
> **Does the consumer fire AFTER the source's DECLARED cadence window closes?**
> Criterion = `partner_roster.json` `cadence` (`trading_day_offset`). **Measured arrival times are
> CORROBORATION that the declaration is honoured -- never the criterion.** (A census keyed on observed
> clock times would flag T-1-at-D+1 forever, and WO-4c makes that state CORRECT -- the instrument would go
> stale under its own remediation.)

**DENOMINATOR: 8 declared feeds** (`partner_roster.json` -> `partners[].legs{}.feeds[]`), enumerated not
constructed. **Plus 2 feeds with NO declared cadence, carried as UNKNOWN rather than inferred.**
**Authority:** `MDPF_CHANNEL_INDEPENDENCE_PRD.md` §2.6 (closure row 7) + §2.5 (row 8); roster key amended
@`f642948889`.

---

## PART 1 -- DO THE PRODUCERS HONOUR THEIR DECLARED CADENCE? **8 of 8 YES.**

Times measured via `aws s3 ls` (renders **LOCAL, UTC-4**); UTC conversion stated. Today = Tue 2026-07-28,
expected last trading day = **07-28**; T-1 frontier = **07-27**; D+2 frontier = **07-24**.

| feed_id | declared | newest partition | written (UTC) | expected frontier | verdict |
|---|---|---|---|---|---|
| `smartx_model_aum_daily` | same_day | **2026-07-28** | 13:38Z | 07-28 | **HONOURED** |
| `smartx_model_allocation_roster` | same_day | **2026-07-28** | 13:38Z | 07-28 | **HONOURED** |
| `schwab_rps_s2` | T-1 | **2026-07-27** | 10:16Z (D+1) | 07-27 | **HONOURED** |
| `eclipse_portfolios_full` | T-1 | **2026-07-27** | 07-28 03:30Z | 07-27 | **HONOURED** |
| `orion_assets` | same_day | **2026-07-28** | 14:16Z | 07-28 | **HONOURED** |
| `bd_model_roster` | same_day | **2026-07-28** | 06:00Z | 07-28 | **HONOURED** |
| `bd_holdings_s2` | D+2 | **2026-07-24** | 07-26 03:30Z | 07-24 | **HONOURED** |
| `bd_allocations_s2` | D+2 | **2026-07-27** | 07-28 03:30Z | 07-24 | **HONOURED (ahead)** |

>> **ZERO PRODUCER DEFECTS. Every declared feed is delivering on contract.** This is the census's most
>> important negative result: **the estate does not have an ingestion problem.** <<

**⚠ AND IT CORRECTS A STANDING RECORD.** `bd_allocations_s2` is at **2026-07-27**, *ahead* of its D+2
contract. The memory-index caveat that cot `allocations`+`unrealized` are frozen has been superseded twice
today; **allocations is now the FRESHEST cottonwood feed.** Only `bd_holdings_s2` sits at its D+2 frontier,
which is **lag 0, by design** -- the roster is explicit: *"Cottonwood at D+2 is lag 0; Cottonwood at D+4 is
lag 2, and THAT is the signal."*

---

## PART 2 -- THE PHASE TABLE: consumer firing vs declared window close

| consumer | applied schedule | reads | source's declared window closes | PHASE |
|---|---|---|---|---|
| `opal-assets-daily-emitter-daily` | `cron(15 17 * * ? *)` = **17:15Z** | `schwab_rps_s2` (T-1) | D+1 ~10:16Z | **OK for T-1** ✔ |
| " | " | `eclipse_portfolios_full` (T-1) | D+1 ~03:30Z | **OK for T-1** ✔ |
| " | " | `orion_assets` (same_day) | D ~14:16Z | **OK** ✔ (2h59m margin) |
| " | " | `smartx_*` (same_day) | D ~13:38Z | **OK** ✔ (3h37m margin) |
| " | " | ETF partner files | **UNDECLARED** | **UNKNOWN** |
| `etfs-netassets-daily` | `cron(0 22 * * ? *)` = **22:00Z** | TrueShares / Filepoint | **UNDECLARED** | **UNKNOWN** |
| WS-A aggregate (in-chain) | **inherited, no own rule** | ETF feeder | -- | **INVERTED** ✖ |
| `mdpf-daily-refresh-trigger` | **`ScheduleExpression: None`** | INF completion marker | n/a | **NO SCHEDULE** ✖ |
| `opal-assets-mdpf-portal-publisher` | **zero rules target it** | canonical gold | n/a | **NO SCHEDULE** ✖ |
| `bd-49f-etf-ownership-daily` | **no rule AND no resource policy** | `opal-data-bd` rps | n/a | **UNINVOKABLE** ✖ |
| `cot-etf-ownership-daily-schedule` | `cron(30 10 * * ? *)` | cot gold holdings | -- | OK ✔ |
| `inf-etf-ownership-on-gold-complete` | event-only (INF gold) | INF gold | n/a | **NO SCHEDULE** (accelerator w/o floor) ✖ |

---

## PART 3 -- ⚠⚠ THE FINDING THAT CHANGES THE DIAGNOSIS

>> **THE EMITTER'S PHASE IS CORRECT. AT 17:15Z IT FIRES *AFTER* EVERY ONE OF ITS FOUR DECLARED SOURCES HAS
>> DELIVERED ON CONTRACT.** The T-1 feeds closed that morning (10:16Z, 03:30Z); the same-day feeds closed
>> that afternoon (13:38Z, 14:16Z). **There is NO phase error at the emitter.** <<

**So the Group A/B failures are NOT a phase defect. They are a PREDICATE defect.** The emitter fires at the
right time and then asks the wrong question -- `date == run_date` -- of feeds whose contract is `D+1`.

**This sharpens Andrew's diagnosis rather than contradicting it.** He said *"backwards ingestion versus
consumption trigger schedule."* Measured: **the ingestion/consumption ORDER is right; the consumption
PREDICATE ignores the declared offset.** WO-4c (accept latest partition <= run_date, judged per declared
cadence) is therefore **the whole fix for Groups A/B** -- **no re-phasing of the emitter is required, and
re-phasing it would be a change made against a non-existent defect.**

**GENUINE PHASE INVERSION EXISTS IN EXACTLY ONE PLACE:** the ETF chain -- puller **22:00Z**, WS-A consumer
**~16:45Z**. **5h15m inverted, permanently.** That is Andrew's "backwards" in its literal form, and it is
**ETF-only** -- which lands it in the E-queue, below MDPF, exactly where he ranked it.

---

## PART 4 -- SCHEDULE ABSENCES (4, all consumer-side)

1. **`mdpf-daily-refresh-trigger`** -- `ScheduleExpression: None`, event-only on the INF marker. **The
   NEVER#4 instance already in CLAUDE.md; re-confirmed on the applied plane.**
2. **`opal-assets-mdpf-portal-publisher`** -- **zero EventBridge rules target it.** Being fixed under
   WO-4/AE tonight.
3. **`bd-49f-etf-ownership-daily`** -- no rule **and no resource policy**; uninvokable. E1.
4. **`inf-etf-ownership-on-gold-complete`** -- event-only, **no scheduled floor.** Works today because INF
   completes daily; **it is one upstream failure away from the 07-18 six-day freeze.**

---

## PART 5 -- DECLARED UNKNOWNS (not inferred)

- **ETF vendor feeds (TrueShares, Filepoint)** -- not in the roster. **No declared cadence.** Their
  behaviour (22:00Z draw, forward-dated Filepoint labels) is measured but **uncontracted**. E2 closes this
  by DECLARING the cadence rather than re-phasing the clock.
- **The emitter itself as a producer** -- it writes the gold DDB on `cron(15 17 * * ? *)` but has **no
  declared cadence of its own**. Per CTO: when the ETF feed is declared, **add the emitter's own row -- it
  is a consumer with a schedule and belongs in the table it feeds.**
- **What FIRES each silver producer** -- I measured arrival TIMES for all 8; I did **NOT** establish the
  producing job, its trigger, or its schedule for **any** of them. **This is the genuinely open half of
  WO-5** and it is what would let a slip be attributed rather than merely detected.

---

## VERDICT

| axis | result |
|---|---|
| Producers honouring declared cadence | **8 / 8** |
| Consumer phase errors (fires before its source) | **1** -- ETF chain only |
| Consumers with NO schedule | **4** |
| Feeds with no declared cadence | **2** (+ the emitter itself) |
| **MDPF Group A/B root cause** | **PREDICATE, not phase** -- WO-4c is the whole fix |

**The estate does not have an ingestion problem. It has four unscheduled consumers, one inverted ETF chain,
and one consumer asking a question its own roster already answers.**

-- `2.0.0_SA_COO`, 2026-07-28
