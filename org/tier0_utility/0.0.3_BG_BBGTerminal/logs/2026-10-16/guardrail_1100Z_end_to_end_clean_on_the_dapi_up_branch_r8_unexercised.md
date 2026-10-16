# Guardrail 2026-10-16 11:00:01Z -- END-TO-END CLEAN, on the DAPI-UP branch, so R8 is still UNEXERCISED

**archetype:** VALIDATE

The one dated obligation carried from 10-15: read the 11:00Z fire and report. Done. **The pull,
publish and every downstream leg are green, and the dashboard is fully current at T-1.** The fire
took the DAPI-UP branch, so it graded the organic negative arm and NOT R8's settle loop -- which is
ruling 34925 item (1), recorded as such.

## 1. The branch was called BEFORE the fire, and the log confirms it verbatim

At **10:46:14Z**, 14 minutes early, `bloomberg_health` read `ok:true` and I read the precondition out
of `scheduled_daily_pull.cmd` rather than inferring it: the cmd runs `bbg_fallback.ps1`
unconditionally and the fallback's own rc decides (`:68` -- `if (Dapi-Up) { Say "DAPI UP -- proceed
with pull, no sign-in needed."; exit 0 }`). Flagged to `1.0.0_SA_CTO~Z` (msg 34924) **before** the
fire, not explained after.

The log at 11:00:01Z, verbatim:

```
[fallback] checking DAPI availability...
[fallback] DAPI UP -- proceed with pull, no sign-in needed.
DAPI FALLBACK EXIT: 0
PRECONDITION: PASS -- DAPI UP, an entitled session answered a real refdata request.
```

**So the GUI sign-in phase never ran and R8's settle loop was never reached.** Per ruling 34925: this
is the organic negative arm; the live settle-loop grade stays at the next DAPI-down morning.

## 2. What ran, with its own numbers

| leg | result |
|---|---|
| pull notebooks | `market_indices_data_pull` **148s**, `model_portfolio_regression_analysis` **139s**, both OK |
| target | **20261015** (today - 1 business day) |
| tripwire (pull leg) | **PASS**, vintage 20261015, as-of 2026-10-15 matches expected business day |
| tripwire (publish leg, as-of-scoped) | **PASS** again, independently re-run by the publisher |
| PULL EXIT | **0** |
| publish | no-backward guard read *"portal currently serves 2026-10-14 -- 2026-10-15 is newer, safe to advance"*; uploaded data **8,737,361 B**, model **18,032,257 B**, manifest **LAST** |
| served check | *"served data_as_of 2026-10-15 (generated_at 2026-10-16T11:07:38Z)"*, *"served 1D matches the PKL for all five models"* |
| PUBLISH EXIT | **0** -- *"PUBLISHED 2026-10-15 -- verified by content, not by self-report"* |
| ETF leg | **0**, 7 objects under `bbg/2026-10-15/` |
| constituents leg | **0**, 9 objects |
| price leg | **0**, 188 of 188 rows, 2 of 2 pointers |
| rivalfunds Bloomberg | **90** -- landed, batch whole, marker written |
| rivalfunds enrichment | **94** -- landed |

## 3. I verified the SERVED artifact myself, because rc=0 is the producer's self-report

The publisher verifies its own served content, which is good engineering -- **and still the
producer's claim.** Read independently through the gateway:

| source | at 02:3xZ (my own earlier read) | after the fire |
|---|---|---|
| `data_pkl` | 2026-10-14, **1** trading day behind T-1 | **2026-10-15, 0 behind, stale false** |
| `model_pkl` | 2026-10-14, **1** behind | **2026-10-15, 0 behind, stale false** |

Both under `pipeline_execution_id b1a9569c-b9aa-4927-bedd-8b65d254c46b`, `updated_at
2026-10-16T11:05:31Z`. **The delta against my own pre-fire read is the evidence** -- a single
post-hoc reading could not distinguish "advanced" from "was already there".

**The aggregate trap, restated because it is one line from a false alarm:** the endpoint's top-level
`stale: true` / `as_of: 2026-09-30` is a MINIMUM across five mixed-cadence sources and is driven
entirely by `attribution_excel` and `peer_excel`, both `frozen: true` at the last month-end. A
monthly artifact 11 trading days after 09-30 is on-cadence. **Nothing I own is stale.**

## 4. R7's -TraceTest, run per ruling 34932 -- and what it does NOT prove

Ruling 34932 withdrew item (3) of 34925 (its premise was false: `-ForceDown -DrySubmit` cannot reach
submit while signed in -- see
`deliverables/R8_OFFLINE_PROOF_NOT_EXECUTABLE_WHILE_SIGNED_IN_20261016.md`) and asked for the R7
trace run instead, stated as proving the trace and not the loop.

Verified safe before running: `-TraceTest` is handled at `bbg_fallback.ps1:59`, **before** STEP 1's
DAPI check and before the creds check at `:101`; it runs `-TraceOnly`, writes one line, `exit 0`.

Run at **11:02:30Z**, exit **0**:

```
TRACE fgproc=none(0) fgtitle='' loginhwnd=none sess=1 console=3 state=Disconnected locked=y
```

**Live ledger protected and PROVEN so:** `BBG_ESCALATION_PATH` redirected the write to the
scratchpad, and `C:\opal-elev\bbg_fallback_ESCALATION.txt` sha256 is **identical before and after**
(`EF5C4AF2...58FF2`), mtime still 2026-10-15T11:02:37Z.

**SCOPE, stated rather than buried.** The trace reports the foreground of **the session it runs in**.
`query session` shows mine is **ID 1, Disc(onnected)**; the live console is **ID 3, Conn(ected)**.
So `fgproc=none(0) locked=y` is a property of where I ran it, **not** of what the 07:00 task sees --
the historical aborts recorded a real `fg=32116010`, so those ran where a foreground existed.
**This proves the trace renders, parses and exits 0. It proves nothing about the settle loop.**
Worth keeping: the trace's own fields cross-checked correctly against an independent instrument
(`state=Disconnected` and `console=3` both agree with `query session`).

## 5. Flagged, not hidden -- five things in a green run

1. **WARN x4, on the ONE trading-calendar frontier:** `pandas_market_calendars absent; answering
   from the hardcoded NYSE fallback NYSE/hardcoded-fallback-2010-2027 (covers 2010-2027; regenerate
   with lib/tests/gen_nyse_closures.py --write before 2028)`. It answered correctly today and it is
   a fallback on the surface CLAUDE.md NEVER#1 names as the single frontier.
2. **`names: PARTIAL`** in rivalfunds enrichment -- 42 candidates, 34 already named, 8 asked,
   **0 named**, `written: false`, reason *"the fetch returned no usable name"*. Reported as PARTIAL
   by the producer, which is the contract; recorded as PARTIAL here, never as absence.
3. **ETF leg: 1 of 172 securities returned ZERO rows** (`2602335D`).
4. **History backfill EXHAUSTED for PFDE and PFOE since 2026-10-09** (count 2) -- two Opal funds
   whose depth is not being filled, 7 days running.
5. **Constituents leg 1b: `refused:entitlement` on all four funds**, with leg 2 filling from
   `pathfinder:silver/holdings/2026-10-15.parquet`. A working fallback over a standing refusal; the
   refusal is not new and is not mine.

None of these blocked today's run. Items 1, 4 and 5 are standing conditions rather than events.

## Compiler Tools

| tool | result | read |
|---|---|---|
| `bloomberg_health` at 10:46Z (pre-fire) | `ok:true` | **The whole call.** It turned a post-hoc report into a prediction, and the log then matched it verbatim. |
| `grep` of `scheduled_daily_pull.cmd` for the fallback precondition | `:68 if (Dapi-Up) { ... exit 0 }` | Read the branch out of the code instead of inferring it from yesterday's behaviour. |
| `Get-ScheduledTaskInfo` + a background until-loop on `LastTaskResult != 267009` | RUNNING -> **0** after ~150s | `267009` is `SCHED_S_TASK_RUNNING`, not a failure; reading it as an error code would have reported a broken pull. |
| `portal_get_pipeline_freshness` before AND after | 2026-10-14/1-behind -> **2026-10-15/0-behind** | The paired read is the evidence. One reading cannot separate "advanced" from "already there". |
| `Get-FileHash` on the live escalation ledger, before and after `-TraceTest` | identical | Proved the redirect held, rather than assuming the env var worked. |
| `query session` | mine ID 1 Disc, console ID 3 Conn | Explained `fgproc=none(0)` and stopped me reporting it as a statement about the task's context. |

## Owed

- **Nothing dated remains.** The 10-15 obligation is discharged by this file.
- **To Andrew:** a Teams report, which I promised him at 20:10:39Z on 10-15 (*"I will read the result
  after the fire and report"*).
- **Next DAPI-down morning:** the live settle-loop grade, per ruling 34925 item (4).
- **Parked by the CTO, not mine:** the mocked-foreground settle-loop harness and the re-derived glyph
  fixture, both noted as the next R-cell for `2.0.0_SA_COO~ZB`.
