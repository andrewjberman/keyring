# `0.0.3_BG_BBGTerminal` -- 2026-09-24 09:32Z-10:45Z -- THE LEAD PANEL PRICE PRODUCER

**Session purpose:** startup, then the `BG_BBGTERMINAL_PRICE_PRODUCER` mandate (Andrew-direct R-21 call 3
@`b390c36444`, this seat named owner of the terminal-box schedules).
**Current-state file (not this log):** `deliverables/LEADPANEL_PRICE/STATUS.md`.

## THE HEADLINE

⭐ **THE PRODUCER ALREADY WORKED. ONLY THE TRIGGER WAS ABSENT.** No producer code was written. The mandate's
own closing line made that the first question and the build ladder's second rung is the whole answer.

## STARTUP

Inbox first per the launch prompt. Two messages, both read and acked: **25199** (R-21, the Andrew-direct
egress grant) and **25383** (the mandate exists). `/watcher` armed; `org/XXX.md` A.1/A.3/D/E run; B.0
delivery ledger clean at 2 of 2 READ. Identity gate PASSED -- `whoami` on `opal-gateway-bbg` returns
**Opal Bloomberg**, not Andrew. `bloomberg_health` `ok: true`.

⚠ **THE `/watcher` CENSUS REGEX READS ZERO FOR A LIVE WATCHER ON THIS BOX, AGAIN.** The skill's
`CommandLine -match 'inbox-watch\.sh {serial} stream'` cannot match, because the workspace path contains a
space and is therefore QUOTED -- a `"` sits between `.sh` and the serial. `script rows: 0` while the watcher
was healthy at **PID 35932**. This is already banked; recording the re-hit because a ZERO gets believed
where a wrong number gets re-run. Watcher expired and was re-armed twice on its own `[WATCHER-EXPIRED]`
notice, same turn each time (tasks `bbuzztuir` -> `bz0btwlvg` -> `b0tjw9nl3`).

⚠ **BROKER REGISTRATION DROPPED TWICE** (~09:47Z, noticed by `0.0.0_AB_MSTR~Z`; again ~10:41Z, caught by a
`heartbeat` returning *"is not registered"*). Re-registered both times. The heartbeat-death this fabric has
banked.

## WHAT WAS MEASURED, IN ORDER

1. **Frontier first**, before any staleness claim: `prev_trading_day(2026-09-24)` = **2026-09-23**.
2. **Served state:** last PRICE generation **2026-09-15**, written 09-17 -- and its own `coverage_vintage`
   says it was a RE-PUBLISH of already-crossed bare partitions, *"NO NEW VENDOR CALL, NO RECOMPUTE"*, so the
   last actual box-side pull was older still. `2026-09-22/23/24` ABSENT on both axes.
   **A guessed key shape returned empty first and was NOT accepted as absence** -- the pointer contract was
   read (`axis_date = "<AXIS>#<date>"`, `ticker = "_CURRENT"`) and the query re-run.
3. **Schedule census:** no price task on this box. `OPAL_BBGTML_daily_pull` 07:00 ET, `LastResult 50`.
4. **Dry run:** 34 universe names, 32 usable PX_LAST (2 insufficient: `Enel IM`, `ROG SW`), 31 of 32
   identity-resolved, both axes COMPLETE. **The producer works.**
5. **QA fire, guarded.** Both target pointers re-read ABSENT immediately before the write, **with a positive
   control on the identical command shape** (09-15 PRESENT) so ABSENT could not be instrument failure; the
   fire aborts on either. Landed 64 of 64 rows, 2 of 2 pointers, run `R20260924T095217Z`.
6. **NEVER-1 discharged by measurement:** writer census **N=2** (`price_axis_pull.py`,
   `backfill_legacy_generation.py`), both scripted, neither scheduled. After the fire the 09-15 pointer
   re-read **byte-identical** -- same `generation_id`, same `written_at`. **DELTA=0, so no hold.**
   Checked before firing that no live seat was writing that key: `2.0.0_SA_COO~Z` holds a price-review
   worktree and was live, mid an unrelated crosswalk incident -- **the exact overwrite class this guard
   exists for, in flight on a neighbouring surface.**

## THE TRIGGER

A **fourth ISOLATED leg** in `scheduled_daily_pull.cmd`, not a new Scheduled Task -- R-21 says *"like the
existing pull"*, so this **is** the existing pull; a sibling task would be a second path to the same
loopback DAPI. `RC_PRICE` never touches `%RC%`/`%RC_ETF%`/`%RC_CONS%`; codes **80-83** disjoint.
Control flow re-derived **from the saved file**, and **6 of 6 arms exercised** in a stub harness with the
models-chain `%RC%` sentinel preserved 6 of 6. File integrity: 17702 -> 21406 bytes, CRLF preserved, bare
LF 0, non-ASCII delta 0.

⛔ **THE HARNESS'S FIRST CUT WAS WRONG AND IS WORTH THE LINE.** `index(":price_leg")` matched the substring
inside `goto :price_leg` ~45 lines earlier, so the extract began mid-constituents-leg and **contained its
own entry goto** -- it self-looped and printed nothing. **The search SUCCEEDED and returned a real offset.**
Anchored on the line-start label plus two asserts, it passes. Banked as
`a-label-anchor-is-a-substring-of-every-reference-to-that-label`.

## SURFACED, NOT FIXED -- `AMGT_RESAPP-Z-S248`

`%PY_AWS%` is assigned at `:166` **inside the SEND leg**, but the pull-failed/DAPI-up branch at `:145` does
`goto :etf_leg` from **above** it -- so on that one path the ETF and constituents legs invoke an **empty
interpreter**, and that branch **is** the 2026-09-04 leg-isolation fix's own protected path.
**EXPOSURE not INCIDENT, discriminator RUN:** 0 hits across the 30 retained run logs (2026-08-25..09-23);
`RESULT: PULL FAILED` appears once (09-04) in a run with no `ETF LEG` line, so it predates the fix.
**That denominator is bounded by the .cmd's own 30-log prune** and is silent about earlier runs.
Another owner's leg; the price leg resolves `PRICE_PY` itself and cannot inherit it (`rc=83`, one of the 6
arms). **The gate refused `class="EXPOSURE"` (ratified enum is `OBSERVATION|BLOCKING`); corrected to
OBSERVATION rather than taking the audited override** -- EXPOSURE-vs-INCIDENT is the hazard axis, carried in
`hazard_standing=ARMED`, and the row's notes say so.

## THE READER -- and it reframes B2 and B4

`read_rankings` exercised in-process against the live store: **resolves to THIS seat's generation**
(`as_of_date 2026-09-23`, `generation_id 20260924T095217Z-...`, SERVED, 32 rows), not the 09-15 one.

⛔ **But it arrives `dated: true` -- THROUGH the fallback branch -- because the reader asks `_today()`
(09-24) while the producer writes `prev_trading_day` (09-23).** So the mandate's B2 clause *"rather than the
14-day dated fallback"* is **structurally unreachable** on any ordinary day. What changed is the fallback
**DISTANCE: 9 days -> 1 day.** **B4 is therefore held open by the SCHEDULE, not by the QA fire** -- closing
it on the ad-hoc would have been a false close. Neither remedy is in this seat's write surface.

## RECORD

| | |
|---|---|
| `8d235eadb1` | the leg + ledger + STATUS.md, committed by `0.0.0_AB_MSTR~Z`, this seat's **named integrator**. `safe-commit` refused this seat correctly (no OWNPATHS lane, by README design); **`GIT_COMMIT_AUTHOR_OVERRIDE` was NOT used** -- the designed route was available. |
| `b867e362b6` | the S248 row + ledger L1/L2 closes, this seat's own commit (lane ANY). **Verified an ancestor of `origin/CLOUD`, with a bogus-hash negative control.** |
| ledger | `leadpanel-price-producer-schedule`: **L1, L2 CLOSED. L3, L4 OPEN on the 07:00 ET fire.** |

⛔ **THE INVERTED DEPLOY HAZARD, now resolved but worth carrying as a device property:** site-Z Scheduled
Tasks run the **WORKING TREE**, so the `.cmd` edit was the deployed state the moment it touched disk, before
any commit. An uncommitted edit here is **not** "not yet deployed" -- it IS the deployment, and a
checkout/reset would have silently reverted a landed deploy while the ledger read OPEN. `1.0.0_SA_CTO~Z`
ruled on this in R-52 at 10:37Z; **its premise was already 16 minutes stale** (the commit landed ~10:21Z),
and that correction was sent rather than held, because the ruling had left a standing "no seat resets this
tree" constraint on other seats.

## TEAMS DUTY

Watch armed (`bllxyi2nx`). **Banner: `cursor=2026-09-15T18:25:20.883Z`.** This seat's own 09-11 log
(`72aeee47ce`) establishes that under the harness **`C:\tmp` IS the live home** -- native Windows Python
resolves `/tmp` there because the harness does not export `TMPDIR` -- so **the arm took the LIVE cursor**,
not the stale `%LOCALAPPDATA%` one (which is newer by mtime and still the wrong file; *which file is live is
not a property of the file*). ⚠ **A prediction made from this shell was WRONG and the banner corrected it:**
the Bash tool's shell DOES export `TMPDIR`, so reasoning from it picked the other home. **The banner is the
only statement of which cursor was armed, exactly as `TEAMS_DUTY.md` says.**
**That cursor is still 8 days behind the newest thread daily file (2026-09-23), so every emit from this arm
is SUSPECT-REPLAY until RECALL clears it individually.** Cursor not hand-edited (forbidden); engine defect
owned by `0.5.0_AE_OpalETL~Z` and already documented -- not re-surfaced as new.

## NEXT PROOF -- the one gate

The **07:00 ET fire** (~18 min after this write). A bounded background watcher is armed on all terminal
markers, not just the happy one. Close **L3** on the run log's `PRICE LEG EXIT CODE` + `LastRunTime`/
`LastTaskResult`; close **L4** on a pointer whose `run_id` is **distinct from `R20260924T095217Z`**.
⚠ **B3 cannot be graded on a calendar:** on 2026-09-23 the 07:00 precondition FAILED (rc 50, DAPI down) and
every landing leg correctly skipped. DAPI is up now.

## PUSH STATE

`8d235eadb1` on `origin/CLOUD` (integrator's `ls-remote` read). `b867e362b6` verified an ancestor of
`origin/CLOUD`. This seat pushed nothing itself.
