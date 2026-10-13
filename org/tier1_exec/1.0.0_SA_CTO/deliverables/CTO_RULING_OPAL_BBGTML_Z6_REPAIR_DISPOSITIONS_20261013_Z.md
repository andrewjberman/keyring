# CTO ruling -- OPAL_BBGTML Z6: repair dispositions after the read-only trace (`1.0.0_SA_CTO~Z`, 2026-10-13 ~20:1xZ)

**Order:** cross-box ORDER XB-20261013T185926Z-4d72, outcome Z6. Andrew's site Z memo: "We want to make sure that's
functional ... that people can use it." Register home: OPAL_BBGTML, re-opened under D6 @bb8fb3d7b2.
**Trace:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/OPAL_BBGTML_Z6_TRACE_20261013_Z.md`. It is read-only. Nothing was run,
edited or sent, and no Bloomberg session was opened.

## What the trace found, one line per leg

| leg | state | the blocker |
|---|---|---|
| daily pull | 07:00 ET exit 50; recovered by the supervised 10:28 ET sign-in and the 10:32 re-run (2026-10-12 published, verified by content) | the unattended sign-in failed its precondition on 8 of 30 retained runs; after the 14:57 ET reboot there is no `wintrv.exe`, so the Terminal is INFERRED signed out |
| freshness | 07:30 ET exit 2 was a correct STALE; the manual re-run at 19:14Z read PASS | the pull |
| ticket intake | exit 2 every 5 minutes; last exit 0 on 2026-09-03 | `integrations/ticketing/intake/runner_config.json:11` pins identity `opalbloomberg`, which is substring-matched against the token `sub` (`<tid>/<oid>`) and can never match |
| Teams | watcher LIVE with the correct oid pin (armed 15:38:57 ET) | lives 1770 s and only the BG session re-arms it; a successful arm prints nothing the agent sees |
| GUARD-4 | built and PASS on `rv-bbgtml-guard4` @3b65362444, LOCAL only | Andrew's word (open call `sitez-20261013T021538Z-2da6`) |

## Dispositions

1. **Terminal sign-in before 07:00 ET 2026-10-14: Andrew's act.** It is on the site Z open-calls list.
   - Hazard: `bbg_fallback.ps1:55-56` refuses to sign in while 8194 listens. The BG seat's MCP server started `bbcomm.exe`
     at 15:07 ET and holds 8194. So tomorrow's unattended fallback is expected to escalate rather than sign in, and the
     pull exits 50 again. AMGT induction (09:00 ET) has the same root cause.
   - Confirm the sign-in with `dapi_check.py`, which makes a real data request, never `bloomberg_health`.
2. **The 8194 gate vs an MCP-started bbcomm (repair 2): CUT under OPAL_BBGTML.** When 8194 listens but `dapi_check.py`
   fails, classify the state as "listener up, not entitled", which still warrants a sign-in. The file runs from the
   working tree, so the edit is the deploy: the cell carries a change-management entry and one real run.
3. **Unattended sign-in reliability (repair 3): CUT under OPAL_BBGTML, after 2.** Re-assert focus immediately before the
   Login click, and allow one bounded re-fill on rc=4 (an rc=4 abort spends no attempt).
4. **The intake identity pin (repair 4): CUT under OPAL_BBGTML, gated on a backlog read.**
   - The pin becomes the oid `517aa5ee-b4d0-425a-b493-5a22ff77ac4f`, the value 16fb949b5b gave the BG skill.
   - FIRST read the intake cursor and the count of tickets opened since 2026-09-03. The first good pass may post that
     whole backlog into the client ticket channel. If the count is above zero, the cell stops and the call goes to
     Andrew; a post to a client channel is his. The cell lands the fix only on a zero backlog or his word.
5. **Teams arm visibility (repair 5): CUT under OPAL_BBGTML.**
   - One `[TEAMS-ARMED]` stdout line on a successful arm, so the BG session can tell a live watcher from a dead one. Not
     a new standing process.
   - `teams-watch.py` is imported by the intake runner every 5 minutes, so the cell proves the runner unchanged.
6. **GUARD-4:** unchanged; it waits on Andrew. Its branch is LOCAL only, so worktree `C:/tmp/rv-guard4` must not be
   garbage-collected until he answers. `0.0.0_AB_MSTR~Z` should lock it.
7. **Unowned tasks, classed:**
   - `amgt-induction-daily` belongs to AMGT_CORPUS.
   - `OPAL_vendor_watch` is unregistered (author `0.0.0_AB_MSTR~Z`); it stays MSTR's.
   - `OPAL_restore_etf_daily_pull_20261009` is a spent one-shot; MSTR may delete the task.
   - `OPAL_DEMQUE_bbg_ledger_upload` belongs to MDPF_DEMQUE.
   - `OPAL_BLOOMBERG-FreezeTripwire` (outside the repo) is MSTR's to class.

## Issuer

OPAL_BBGTML has no COO lane. Repairs 2-5 are one issuance by a COO lane that `0.0.0_AB_MSTR~Z` seats for OPAL_BBGTML.
Every cell is WORLD risk, because each touches a working-tree production file. Order: 2, then 3; 4 and 5 run in
parallel with them.

-- 1.0.0_SA_CTO~Z
