# 0.0.3_BG_BBGTerminal — session log 2026-09-02T14:29–14:40Z

**Archetype:** DAILY GUARDRAIL (continuation — no new startup)
**Serial:** 0.0.3_BG_BBGTerminal (base) · broker PID 16328 · device: site Z
**Continuity:** SAME SESSION as `logs/2026-09-01/startup_and_daily_guardrail_1855-1906Z.md`.
Registered 2026-09-01T18:55Z and **continuously live since** — no relaunch, no re-arm, both
Monitors still the ones armed yesterday (`b38eciz71` inbox, `bi6lvvse4` Teams). **The date rolled,
so the guardrail came due again; the session did not restart.** This log covers only the 09-02
delta.

---

## 1. DAILY UPLOAD GUARDRAIL (record @e77bec6e5) — **PASS**, end-to-end, for 2026-09-02

**Trading calendar resolved via the ONE frontier** (`lib/trading_calendar.py`), not by hand:
`calendar_source = NYSE/hardcoded-fallback-2024-2027`; `is_trading_day(2026-09-02) = True`
(Wednesday); `prev_trading_day(2026-09-02) = 2026-09-01`. **T-1 is 20260901.**

| surface | reading |
|---|---|
| `OPAL_BBGTML_daily_pull` | Last **9/2 07:00:01 ET**, Result **0**, Next 9/3 07:00 |
| `OPAL_BBGTML_freshness_check` | Last **9/2 07:30:01 ET**, Result **0**, Next 9/3 07:30 |
| artifacts | `data 20260901 v1.pkl` (8,627,338 B) + `model 20260901 v1.pkl` (17,598,796 B), written 9/2 07:02–07:03 |

**As-of 20260901 IS exactly T-1. Correct, not stale.**

Read at source in `~/opal_bbg_logs/bbg_tplus1_20260902_070001.log` — and the publish leg is
content-verified, so `rc=0` here is not merely the producer's self-report:
```
PRECONDITION: PASS -- DAPI UP, an entitled session answered a real refdata request.
TRIPWIRE: vintage 20260901 ... RESULT: PASS -- both PKLs safe to send
OK:   served data_as_of 2026-09-01 (generated_at 2026-09-02T11:05:56Z)
OK:   served 1D matches the PKL for all five models
RESULT: PUBLISHED 2026-09-01 -- verified by content, not by self-report.
RESULT: END-TO-END OK -- pulled, validated, published, served-content verified.
```
ETF leg EXIT 0, constituents leg EXIT 0. **No fallback `/terminal-upload` needed; none run.**

### 1a. The DAPI fallback did NOT sign in today — and that CORRECTS yesterday's framing
Yesterday I logged the sign-in fallback firing and wrote that *"a fallback that fires silently every
day is a fallback that has become the primary path."* **Today it did not fire in that sense:**
```
[fallback] checking DAPI availability...
[fallback] DAPI UP -- proceed with pull, no sign-in needed.
```
**The block RUNS every day; the SIGN-IN inside it does not.** Yesterday it submitted
(`bbg_signin.ps1 -Phase submit`); today it checked and passed straight through. So the watch I
opened is **1 of 2 days, not 2 of 2** — and the discriminator is the `no sign-in needed` line, not
the block's presence or its `EXIT 0`, both of which are identical in the two cases. ⛔ **My own grep
yesterday would not have separated them**: I filtered on `PRECONDITION|TRIPWIRE|RESULT|EXIT`, none
of which distinguishes a submitted sign-in from a skipped one. **A token census tuned to the
verdict lines cannot see which limb produced the verdict.** Counting this as a trend needs the
`[fallback]` lines specifically, every day, or it is not a count.

---

## 2. Merge window #2 (msg 19330) — acked; posture unchanged, deliberately not restated

`0.0.0_AB_MSTR~Z` opened a second window (inbound leg CLOUD→SITEZ, 8 commits, **overlap 0 of 17 =
0.00%**, merge-tree rc=0, inbound deploy ceiling 0). Acked (`ack_messages("19330")` accepted) and
answered SHORT — the full structural posture was given in the 19274 reply and repeating it would be
noise, not diligence. Same standing: **non-source of the staging hazard, not a complier**; this
seat does no git work.

**Nothing held back.** Yesterday's log was swept clear after the previous CLOSE. This log is the
one new untracked file and is again scoped to AFTER the CLOSE rather than offered mid-merge.

**One datum offered to the integrator, bounded:** msg 19330 repeats the "courtesy, not the control"
caveat, and last night's measured reach was **0 of 7**. This seat has been continuously live since
18:55Z on 09-01 and read all three broadcasts within a minute of send — so a reach figure carried
over from last night would understate by at least this one row. **I asserted no number for the other
six seats and claimed no knowledge of their state.**

---

## 3. Compiler Tools

| tool | use | outcome |
|---|---|---|
| raw `grep`, marked | `~/opal_bbg_logs/bbg_tplus1_20260902_070001.log` verdict lines, then the `[fallback]` limb | **Rule 21 non-application limb (iii)** — a transient run log outside the repo corpus; marked `# rail-checked:` on both calls |
| `python lib/trading_calendar.py` | T-1 frontier | the ONE frontier, queried not recalled |

**Rule 21 limb (i) is DISCHARGED as of the 09-01 merge** (`comp-read --enumerate` landed and is
certified) — a count no longer justifies `grep`. **That did not bind either call above**: both were
outside the repo corpus under limb (iii), which is unchanged. Stating it because the discharge is
one day old and the temptation is to either over-apply a fresh rule or forget it; neither happened,
and the reason is the corpus boundary, not my discipline.

---

## 4. State

- Both Monitors armed and unchanged since 09-01; **ZERO crons**; zero pending task orders.
- Fabric inbox: 3 messages received, read at source and acked this session (19274, 19282, 19330) —
  all `0.0.0_AB_MSTR~Z` integration frames. Nothing else.
- **Nothing owed on Teams** (no emit since the 09-01 arm).
- **Guardrail PASS 2026-09-02**; served vintage 2026-09-01 = T-1, content-verified.
- Holding for the CLOSE frame. **Available.**
