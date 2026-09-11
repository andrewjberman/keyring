# 0.0.3_BG_BBGTerminal — session log 2026-09-10T19:42–19:50Z

**archetype:** RAVC REQUEST SERVED (terminal sign-in, this seat's exclusive playbook)

**Serial:** `0.0.3_BG_BBGTerminal`, session `fd87eb7b-…`, PID 6104 — **same session** as the 06:19Z
startup and the 11:30Z freshness entry, woken by inbox Monitor `bh55lbr03`.
**Trigger:** msg **21047** from `2.0.0_SA_COO~ZZZ` — `bloomberg_health ok:false` measured twice
(~18:5xZ, ~19:3xZ); AMGT_RESAPP cell **AMGT-s-1**, head of the longest round-1 chain, cannot spawn
because its worker's first act is `bloomberg_health` and on `ok:false` it files a row and stops.

---

## 1. OUTCOME — SIGNED IN, CONFIRMED BY DATA, ONE ATTEMPT SPENT OF TWO

ACKed at 19:44Z **before any work**, so the requesting lane was never waiting on silence (RAVC 2).
Served and closed at 19:49Z.

| gate | evidence |
|---|---|
| symptom confirmed | third independent reading: `ok:false`, `could not start blpapi session to 127.0.0.1:8194` — READ_HERE §1's most common signature |
| credential | `--check` fingerprint only: `user_len=12 pw_len=9 pw_sha256=b52a0db305ea`. No value printed, none written anywhere |
| **budget read BEFORE submitting** | ledger 12 prior attempts, most recent `2026-09-09T12:38:08Z`, **none in the preceding 6 h** -> fire-once gate clear |
| `-Phase fill` | clean first try — `focus VERIFIED`, hwnd 68786, screenshot written. **Costs nothing, spends no attempt** |
| **screenshot VERIFIED** | login name `alyssaakeith` = 12 chars matching the fingerprint; **NINE masked dots against `pw_len=9`**; genuine `BLOOMBERG: Login` window (S/N 5401234-0, v203.3.81) |
| `-Phase submit` | `ledger recorded (13 attempts total). Clicking Login ONCE.` -> `8194 listener count after submit: 1` |
| ledger after | 13 total, last `{"at": "2026-09-10T19:47:28.6435476Z", "outcome": "SUBMITTED-SUPERVISED"}` |

**ONE attempt spent; one of the two remains.** No lockout risk was taken, because the phase split did
exactly what it exists for — the verify step ran between fill and submit rather than after.

---

## 2. CONFIRMED ON DATA, NOT ON THE PORT — AND THE READ DISCRIMINATES

READ_HERE §2 is explicit that `SUBMIT RESULT: LISTENER UP -- likely success` is **necessary and not
sufficient**, so none of the close-out rests on the listener:

```
bloomberg_health   -> {"ok": true, "endpoint": "127.0.0.1:8194", "service": "//blp/refdata"}
reference_data     -> SPX Index      PX_LAST 7589.71  LAST_UPDATE_DT 2026-09-10  "S&P 500 INDEX"
                      AAPL US Equity PX_LAST 325.28   LAST_UPDATE_DT 2026-09-10  "APPLE INC"
dapi_check.py under C:\Anaconda\envs\cma\python.exe
                   -> "DAPI: UP (session + SPX Index/PX_LAST returned -- entitled session live)" rc=0
```

⭐ **THE DISCRIMINATOR: the value MOVED and the date ADVANCED.** This seat read
`SPX PX_LAST 7636.36 / LAST_UPDATE_DT 2026-09-09` at 11:40Z today; it now reads
`7589.71 / 2026-09-10`. **A listening-but-dead session returns neither a new value nor a new date**,
so the read could have come back false and did not — which is the property a bare `ok:true` lacks
(Rule 22 DISCRIMINATION). Two securities only: the per-lookup cap is respected, and **no field pull
was made** — the request explicitly excluded one and none was needed.

⚠ **BOTH SURFACES ON PURPOSE.** The MCP server and the daily pull run under **different Pythons**, so
a green MCP is not a runnable pull (prompt.md On-Launch step 4). AMGT-s-1 needs the MCP surface;
tomorrow's 07:00 ET vehicle needs the cma one. Green on one would have left the other unmeasured.

---

## 3. DATING THE SIGN-OUT, AND THE PATTERN IT BREAKS

Bounded from this seat's own readings: `ok:true` at **06:20Z**, the 07:00 ET pull logging
`PRECONDITION: PASS -- DAPI UP` and completing END-TO-END OK, a live entitled read at **11:40Z**, and
the L1 brief's `ok:true` at 13:30–16:00Z. So the session dropped **after 16:00Z and before ~18:5xZ**.

⛔ **AND TODAY BROKE THE SHAPE THE FALLBACK WAS BUILT FOR.** The attempt ledger reads:

```
08-26  08-30  09-01  09-03  09-05  09-07  09-09   all ~11:0xZ, all SUBMITTED-UNATTENDED-FALLBACK
09-10  19:47Z                                     SUBMITTED-SUPERVISED   <- today
```

Every prior recovery was the **07:00 ET fallback catching a terminal that signed itself out
overnight**, six for six on a roughly two-day cadence. **Today's sign-out was mid-afternoon, which no
scheduled fire covers**, and the terminal sat down for at least the ~50 minutes between
`2.0.0_SA_COO~ZZZ`'s first reading and this sign-in — **discovered only because another seat happened
to need it.** A mid-session sign-out has **no automatic recovery**, and the seat whose job this is was
live and idle the whole time with no instrument pointed at it.

⚠ **NOT BUILDING ONE.** A watcher/alert on this is squarely inside CLAUDE.md's standing moratorium on
alert/monitor/freshness-checker work absent Andrew's explicit word. **Surfaced to the requesting lane
and recorded here; the route is Andrew.** Told `2.0.0_SA_COO~ZZZ` the operationally useful half
instead: **treat "the terminal is up" as perishable, not as standing for the round.**

---

## 4. COMPILER TOOLS

| Tool | Invocation | Result |
|---|---|---|
| `READ_HERE.md` §1 -> §2 | read BEFORE touching the terminal, per CLAUDE.md's Bloomberg pointer | symptom-matched the exact error string; §2 supplied the phase split and the not-sufficient warning |
| `bbg_credentials.py --check` | fingerprint | `pw_len=9` — the number the screenshot check is scored against; without it the dot count means nothing |
| `.bbg_signin_attempts.json` | read whole, 12 rows printed with denominator | budget state BEFORE the irreversible act, and the two-day cadence in §3 |
| `Read` on `bbg_login_shot.png` | the gate between fill and submit | **the only check that can catch a typo at zero cost**; passed on name length and dot count |
| `reference_data` twice, 8 h apart | 11:40Z vs 19:48Z | the moved value + advanced date — a discriminating read rather than a passing one |
| `dapi_check.py` under cma | the pull's own interpreter | the surface `bloomberg_health` cannot speak for |

---

## 5. STATE AT CLOSE

Registered LIVE PID 6104. Inbox Monitor `bh55lbr03` and Teams Monitor `by8vel475` both live; Teams
cursor unmoved at 2026-08-28T20:07:10.323Z, still zero lapse notes and zero emits. Zero crons.
**Terminal UP and entitled on both interpreters. Portal serving `data_as_of 2026-09-09` = healthy
T-1. Both OS tasks green, next fires 09-11.** One sign-in attempt remains unspent.

**Open, owned elsewhere:** (1) **D7 client-ticket intake, 171.2 h at 07:40 local** — unchanged
escalation, corroborated by `0.0.0_AB_MSTR~Z` from the Task Scheduler plane (msg 20920).
(2) **mid-session terminal sign-out has no automatic recovery** (§3) — new today, route is Andrew.
(3) the `StartWhenAvailable` asymmetry on `OPAL_BBGTML_freshness_check`, with this seat's
transient-alarm qualifier attached (msg sent 11:41Z) — `0.0.0_AB_MSTR~Z` holds the call.
(4) `teams-watch.py` agent-triggered lapse recovery — `0.5.0_AE_OpalETL~Z`; not recurring.
(5) `run_daily_pull.py`'s closing hint still points at the retired m365 gateway.

⚠ **UNCOMMITTED:** this file and the two 2026-09-10 entries beside it, plus `logs/2026-09-05/` and
`logs/2026-09-06/`. No git lane here by design; `0.0.0_AB_MSTR~Z` is the named integrator.
**Push state of every path cited: UNREAD** — no `ls-remote` run this session.
