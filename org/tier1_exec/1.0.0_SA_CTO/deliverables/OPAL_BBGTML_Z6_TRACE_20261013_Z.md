# Z6 Bloomberg agent trace -- site Z, 2026-10-13 (read-only)

Box clock: Windows time zone "Eastern Standard Time" (EDT, UTC-4). Scheduled-task times below are LOCAL ET; the
freshness log and escalation files stamp UTC (Z). Trace taken ~15:40-16:00 ET (19:40-20:00Z). Last boot
2026-10-13 14:57:31 ET = 18:57:31Z (MEASURED, Win32_OperatingSystem.LastBootUpTime). Nothing was run, edited,
committed or sent; no blpapi session was opened.

## Summary (one blocker per leg)

1. PULL: 07:00 ET exit 50 = DAPI down and the unattended sign-in aborted at submit ("focus lost before submit", rc=4, 0 attempts spent); a supervised sign-in at 10:28 ET + re-run at 10:32 ET went END-TO-END OK (vintage 2026-10-12 published, served verified).
2. PULL, NOW: the 14:57 ET reboot left no wintrv.exe (Terminal shell) running, only bbcomm.exe, started 15:07 ET by the BG seat's Bloomberg MCP server; INFERRED signed out. With 8194 listening, the fallback's P0 gate refuses to sign in ("8194 not sustained-absent"), so tomorrow 07:00 ET is expected to exit 50 again unless someone signs in first.
3. FRESHNESS: the 07:30 ET exit 2 is a correct STALE verdict on the missed pull, not its own defect; a manual re-run at 19:14Z read PASS (data_as_of 2026-10-12). Blocker = the pull.
4. INTAKE: exits 2 every 5 min because runner_config.json:11 pins identity "opalbloomberg", which is substring-matched against the token `sub` ("<tid>/<oid>") and can never match; the fix is the oid 517aa5ee-... (the BG skill already uses it). Last exit 0: 2026-09-03 04:29.
5. TEAMS: the watcher IS live now (python pid 17484, armed 15:38:57 ET with the oid pin, which matches the one live opal-gateway-bbg record). Blocker: it lives 1770 s (dies ~16:08 ET) and only the live BG session re-arms it. No process persists it, and a successful arm prints nothing the agent can see.
6. OTHER: TO-GUARD-4 is `pending`; its branch rv-bbgtml-guard4 @3b65362444 is built and PASS, LOCAL only, not merged, waiting on Andrew's word. amgt-induction-daily rc 4 = DAPI refused at 09:00 ET (AMGT_CORPUS).

---

## Q1. Scheduled tasks

MEASURED: `Get-ScheduledTask | Where TaskName -like 'OPAL_*' -or 'BBG*' -or -match 'bloomberg' -or -like 'amgt*'`
+ `Get-ScheduledTaskInfo`, read 15:41 ET. Every task runs as user `Opal Bloomberg`, LogonType Interactive (a task
fires only while that user is logged on). Times are local ET.

| Task | State | Last run (ET) | LastTaskResult | Next run (ET) | Action | Trigger |
|---|---|---|---|---|---|---|
| OPAL_BBGTML_daily_pull | Ready | 10-13 10:32:43 | 0 | 10-14 07:00 | `cmd.exe /c "...\integrations\bloomberg\pipeline\scheduled_daily_pull.cmd"`, WD none | daily 07:00 |
| OPAL_BBGTML_freshness_check | Ready | 10-13 07:30:01 | 2 | 10-14 07:30 | `cmd.exe /c "...\integrations\bloomberg\pipeline\freshness_check.cmd"` | daily 07:30 |
| OPAL_D7_ticket_intake | Ready | 10-13 15:39:46 | 2 | 10-13 15:44:45 | `...\integrations\ticketing\intake\run_intake.cmd` (no args) | every 5 min (PT5M) |
| amgt-induction-daily | Ready | 10-13 09:00:02 | 4 | 10-14 09:00 | `cmd.exe /c "set OPAL_INDUCTION_FIRE=1&& ...\Python311\python.exe -m lib.research.corpus.induction_scheduled --mode fire"`, WD `C:\Users\Opal Bloomberg\Desktop\opal-pinned\amgt-induction-daily\7580fe909cf3` | daily 09:00 |
| OPAL_vendor_watch | Ready | 10-13 15:09:01 | 0 | 10-13 16:09 | `cmd.exe /c "...\workflows\vendor_watch\run_vendor_watch.cmd"` | hourly (PT1H) |
| OPAL_restore_etf_daily_pull_20261009 | Ready | 10-09 08:00:00 | 0 | (none) | `git.exe -C "<repo>" checkout HEAD -- integrations/bloomberg/pipeline/etf_daily_pull.py` | one-shot 2026-10-09 08:00 |
| OPAL_DEMQUE_bbg_ledger_upload | Ready | 10-13 08:30:02 | 0 | 10-14 08:30 | powershell -EncodedCommand; decoded: `C:\Program Files\Python314\python.exe data\mdpf\scripts\demque\bbg_ledger_upload.py --day <UTC yesterday> --apply`, WD repo | daily 08:30 |
| OPAL_BLOOMBERG-FreezeTripwire | Ready | 10-13 15:40:55 | 0 | 10-13 15:41:54 | `wscript.exe "...\Desktop\OPAL_BLOOMBERG_freeze_investigation_2026-07-30\tripwire\Run-TripwireHidden.vbs"` | logon + every 1 min |
| OPAL_autolaunch_agents | Ready | 10-13 14:58:19 | 0 | (logon) | `powershell.exe -File "C:\opal-elev\autolaunch-agents.ps1"` | at logon |
| Bloomberg Updater (vendor's) | Ready | 10-12 18:26:02 | 3221225786 (0xC000013A, STATUS_CONTROL_C_EXIT) | 10-13 18:26 | `C:\blp\Wintrv\clientratermgr.exe` | daily 18:26 |

Note: the daily pull's task record reads 0 because the LAST run was the 10:32 ET re-run. The 07:00 ET run's exit 50 survives only in its own log (Q2).

## Q2. The daily pull and freshness check

Scripts (MEASURED, read): `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` logs to
`%USERPROFILE%\opal_bbg_logs\bbg_tplus1_<stamp>.log` (cmd :57,:63); exit 50 = DAPI precondition failed, pull not
attempted (cmd :46-49, :124-132). `freshness_check.py` logs to `C:\opal-elev\freshness_check.log` (py :71).

07:00 ET run, `C:\Users\Opal Bloomberg\opal_bbg_logs\bbg_tplus1_20261013_070001.log` (MEASURED):
- `[fallback] DAPI DOWN.` / `P0 gate: transport sustained-down, network OK -> sign-in warranted.` / `fire-once ledger clear (0 in 6h).`
- FILL ok: login window found, focus VERIFIED, password dots 9 of 9, username OCR similarity 100%, `VERIFY: PASS`.
- `[fallback] ABORT: focus lost before submit.` -> `ESCALATE: submit aborted pre-click (rc=4; ...) -- NO Bloomberg attempt spent, ledger untouched`.
- `DAPI FALLBACK EXIT: 2`; the re-check `dapi_check.py` failed: blpapi `Failed to connect to 127.0.0.1:8194 ... connect event failed`, `DAPI: DOWN (session.start() failed -- no listener/transport on 8194)`.
- `PRECONDITION: FAILED -- DAPI DOWN and not self-healed. PULL NOT ATTEMPTED.` -> RC 50. The rivalfunds legs then ran: 93 and 97 (blpapi unreachable).
- So the failure is exactly: no listener on 8194 (Terminal not running or signed in), and the unattended sign-in lost window focus between verify and the Login click. INFERRED cause of the lost focus: another window took the foreground in that interval. NOT MEASURED which window.

Recovery (MEASURED): the sign-in ledger `%USERPROFILE%\.bbg_signin_attempts.json` (35 entries) has its last entry at
`2026-10-13T14:28:30Z outcome=SUBMITTED-SUPERVISED`; `C:\opal-elev\bbg_login_shot.png` and `bbg_win.txt` are stamped 10:24 ET.
`bbg_tplus1_20261013_103245.log`: `DAPI UP`, `PRECONDITION: PASS`, both notebooks OK, tripwire PASS, `PUBLISHED 2026-10-12 --
verified by content`, ETF leg 0, constituents 0, price leg 0, rivalfunds 90 and 94.
The BG seat's log (`org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-10-13/relaunch_1900-1920Z_...md` :32-53) gives
the same account and says the freshness summons led to the re-fire.

Pattern (MEASURED, 30 retained pull logs 2026-09-16..10-13): the first DAPI check read DOWN on 16 of 30; the
fallback self-healed 8 of those 16; `PRECONDITION: FAILED` on 8 of 30 (09-23, 09-27, 09-28, 10-05, 10-06, 10-08, 10-11,
10-13). `C:\opal-elev\bbg_fallback_ESCALATION.txt` lists, for the same dates: "fill did not verify after 3 attempts" (09-28,
10-06, 10-08), "sign-in submitted (1 attempt used) but DAPI still down" (09-23, 09-27, 10-11), "8194 not sustained-absent
(0/3)" (10-05), "focus lost before submit" (10-13). So unattended sign-in is the chronic weak link, not one day's fault.

Freshness (MEASURED, `C:\opal-elev\freshness_check.log`):
- `2026-10-13T11:30:02Z STALE: served data_as_of=2026-10-09, expected_frontier=2026-10-13, trading_days_behind=2` -> summons written to
  `C:\opal-elev\freshness_ESCALATION.txt` and the BG and MSTR~Z inboxes; "BG session LIVE -- no spawn". Exit 2 is correct.
- `2026-10-13T19:14:10Z PASS: data_as_of=2026-10-12 ... trading_days_behind=1 ... series graded=10`. This was a manual run
  (the task's LastRunTime is still 07:30 ET), so the task record still reads 2 while the served artifact is fresh.

Terminal / DAPI processes NOW (MEASURED, Get-Process + Win32_Process, ~15:45 ET):
- `bbcomm.exe` pid 17756, `c:\blp\DAPI\bbcomm.exe`, started 15:07:29 ET; `blpcrashmon.exe` (its child) 15:07:29.
- 127.0.0.1:8194 LISTEN, owned by pid 17756.
- NO `wintrv.exe` and no window titled BLOOMBERG / Login / Launchpad. No bplus process.
- bbcomm's parent is python pid 17380 = `Python311\python.exe integrations/bloomberg/mcp/server.py`, child of the
  0.0.3_BG_BBGTerminal claude.exe (pid 9376, started 14:58:29 ET by the logon autolaunch). So bbcomm was started by the
  BG seat's MCP server, not by a Terminal sign-in.

Signed in? INFERRED NO. The Terminal shell (wintrv) is not running after the reboot, and the only sign-in since the
reboot-free window is the 14:28Z one, which the reboot ended. The BG seat's post-reboot checks (`bloomberg_health ok:true`;
cma `Session.start()/openService` True/True, BG log :24-26) do not settle it: `blp_client.health()` only opens a session
(`integrations/bloomberg/mcp/blp_client.py:133-140`), and `dapi_check.py`'s own header (:6-11) records that
"8194 listening + openService OK" was measured on 2026-08-18 WHILE the Terminal was logged out. Only a real refdata
request can tell, and that was not run (hard rule).

HAZARD for tomorrow (INFERRED from code + live state): `bbg_fallback.ps1:55-56` refuses to sign in unless 8194
is absent on 3 of 3 samples. bbcomm now holds 8194, so if the Terminal is logged out at 07:00 ET the fallback escalates
"8194 not sustained-absent" (the 10-05 shape), does NOT sign in, and the task exits 50.

## Q3. OPAL_D7_ticket_intake

Row (MEASURED): `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md:1646-1667`, id
NFRA_OPALAI-Z-S40, OBSERVATION / INERT / UNDER_INVESTIGATION, owner named in notes as OPAL_TICKET_VNEXT (no live COO lane).
It says the probable cause is the `--identity` pin, "not verified".

Chain (MEASURED, read): task -> `integrations/ticketing/intake/run_intake.cmd` -> `python -m integrations.ticketing.intake.runner`,
log `%USERPROFILE%\opal_ticket_intake\runner.log`. `runner.py:118-123` loads `.claude/skills/teams-assist/teams-watch.py` and
sets `PIN_SERVER`/`PIN_IDENTITY` from config; `read_token()` exits 2 on an unsatisfiable pin (`EXIT_IDENTITY = 2`, runner.py:73).

Exact refusal (MEASURED, last lines, 15:44:46 ET):
`[TEAMS-IDENTITY-FAIL] no-token-for-identity: no mcpOAuth record matches the pin (--server=opal-gateway-bbg --identity=opalbloomberg)` -> `intake pass exit 2`.
Log totals (MEASURED, whole retained log since 2026-08-20): exit 0 = 613, exit 1 = 650, exit 2 = 12,895, exit 5 = 843;
`no-token-for-identity` lines 13,302; last exit 0 `[Thu 09/03/2026 4:29:48]`. Before 09-18 the exit 2s were a different
reason ("pinned gateway token expired"); the identity refusal starts 2026-09-18 01:59 ET.

Expected vs got (MEASURED):
- Pin set at `integrations/ticketing/intake/runner_config.json:11` `"identity": "opalbloomberg"` (server pin :10
  `opal-gateway-bbg`), last changed ab4f76c878 (2026-08-20). Also stated in the runner.py docstring :10-11.
- Matching: `teams-watch.py:238-239` keeps a record only if the pin is a substring of `self_id(accessToken)`, and
  `self_id` (:271-285) returns the JWT `sub` claim lowercased.
- Token store census (`~/.claude/.credentials.json`, redacted script, values never printed): 4 mcpOAuth records, 3 for
  opalinvest.dev. `opal-gateway-bbg`: sub shape `6810043e.../517aa5ee...`, NOT expired, contains "opalbloomberg" = False,
  contains "517aa5ee" = True. `opal-gateway` (expired) and `opalgateway` (live) carry oid `2e21f8e5...`, Andrew's
  identity (the `opalgateway` whoami answers Andrew Berman).
- So the store has the right record and the pin can never select it. Commit 16fb949b5b (1.0.0_SA_CTO~Z, 2026-10-09)
  applied the same correction to the BG Teams skill only; the intake config was not changed.

## Q4. The Teams path

Path (MEASURED from `org/tier0_utility/0.0.3_BG_BBGTerminal/prompt.md:30-63` and `.claude/skills/bbg-teams-assist/SKILL.md:24-49`):
colleague message to opalbloomberg@opalinvest.com -> the gateway `opal-gateway-bbg` (M365 Graph, delegated as Opal
Bloomberg) -> `teams-watch.py`, run under the BG session's Monitor tool, polls `poll_addressed_teams_messages` (DM + group
chats) plus the 1 channel in `.claude/skills/teams-assist/channels.json`, and prints one `[TEAMS]` stdout line per new
message -> the Monitor wakes the BG session (claude.exe, seat 0.0.3_BG_BBGTerminal, launched at logon by
`C:\opal-elev\autolaunch-agents.ps1`) -> `/bbg-teams-assist` serve loop: ACK in-thread, research (Bloomberg MCP and others),
reply with vintage, record to `threads/`. Launch prerequisites: prompt.md step 2a whoami gate, step 3 arm the Monitor.
Arm line, SKILL.md:35: `timeout 1770 python .claude/skills/teams-assist/teams-watch.py --server opal-gateway-bbg --identity 517aa5ee-b4d0-425a-b493-5a22ff77ac4f --channels .claude/skills/teams-assist/channels.json`.

Running now? MEASURED YES (Win32_Process command-line census ~15:45 ET): `timeout.exe 1770 ...` pids 14892/18940 and
`C:\Program Files\Python314\python.exe .claude/skills/teams-assist/teams-watch.py --server opal-gateway-bbg --identity 517aa5ee-b4d0-425a-b493-5a22ff77ac4f --channels ...`
pid 17484, all created 15:38:57 ET. Its parent bash has exited. A bash under the BG claude.exe (pid 30424) was created
the same second, so INFERRED: the BG session armed it. Exactly one teams-watch python is live.

Would the live arm match? MEASURED YES: the pin `517aa5ee-...` is a substring of the `opal-gateway-bbg` record's sub,
exactly one opalinvest.dev record matches server+identity, and it was not expired at census time. The memory note
("`--identity opalbloomberg` can never match") is TRUE of the name pin and is now the intake runner's defect (Q3), not
this watcher's.
The BG session's MCP config (`org/mcp/sessions/861ca766-...mcp.json`) carries `opal-gateway-bbg`, `opal-agent-comms`
and `bloomberg`. So the session that refreshes the token is the same session that consumes it.

Weak points (MEASURED from code/logs; consequences INFERRED):
- Lifetime: `timeout 1770` kills the watcher ~16:08:27 ET. Re-arm is the BG agent's act on the Monitor-end notice
  (SKILL.md:29-31, :150-154). No OS task or service keeps it alive, so a busy, compacted or dead BG session leaves Teams
  deaf until someone re-arms it.
- Silent success: the BG log (`relaunch_1900-1920Z_...md` :59-72) records that the arm banner goes to stderr, which
  the Monitor does not deliver. A healthy arm and a dead one look the same from inside the session; only a process
  census tells them apart.
- Per the same log (:87), the arm-banner cursor rule may make the agent treat the arm's first emits as suspect replay.
  NOT MEASURED whether any message was mis-handled.

## Q5. TO-GUARD-4

MEASURED: `org/tier2_senior/0.7.0_AE_CloudOps~RV/task_orders/OPAL_BBGTML.TO-GUARD-4.tzero-tripwire-cix-recency-port.md`
(issued 0ef06cf632 by 2.0.0_SA_COO~Z, 2026-10-07): one `<status>` tag, `pending -- issued 2026-10-07 ~10:1xZ on CTO
fix-route ADDENDUM 7 @58e472b0b6 (msg 30773), row OPAL_BBGTML-Z-S12`, issued_to 0.7.0_AE_CloudOps~RV, risk WORLD. The
same status is at the branch tip. The order says "BUILDS AND PROVES ON A BRANCH. IT DOES NOT MERGE ... the merge is the
deploy and it waits on Andrew's word".
Branch: `git branch --list` -> `+ rv-bbgtml-guard4 3b65362444` "proof(...): AC1 proof instance and the report -- GUARD-4:
PASS exit 0, five arms, NOT MERGED" (0.7.0_AE_CloudOps~RV, 2026-10-07 06:15 ET). It is checked out in linked worktree
`C:/tmp/rv-guard4`, is 2 commits ahead of HEAD (3 files, +422: `pipeline/tzero/tools/bbg_pkl_tripwire.py` +87, the report,
the proof script), NOT an ancestor of HEAD or origin/CLOUD, and `git ls-remote origin rv-bbgtml-guard4` returns nothing
(LOCAL only, ls-remote read).
Live consequence (MEASURED): in today's 10:32 log the publish leg's tzero tripwire prints no "custom CIX series" line, while
the pull leg's tplus1 tripwire prints "custom CIX series graded: 13 of 84". The gap GUARD-4 closes is still live.

## Q6. Non-Bloomberg-named tasks: script and owner

- amgt-induction-daily -> `lib/research/corpus/induction_scheduled.py`, run from the PINNED worktree
  `C:\Users\Opal Bloomberg\Desktop\opal-pinned\amgt-induction-daily\7580fe909cf3` (HEAD 7580fe909c, 2026-10-09 00:21 ET). Owner
  (header :1-2): project AMGT_CORPUS, cells CRPS-r-1 / CRPS-t-1 / CRPS-aj-1 (D5/AMGT). It also calls
  `integrations/bloomberg/research/model_block_pull.py admit|refresh`, so it IS a Bloomberg consumer. Today's rc 4 (MEASURED,
  `%LOCALAPPDATA%\opal\amgt-induction-daily\2026-10-13.log`): induction population 7 with 0 Bloomberg calls, admit rc 0,
  `REFUSED: Bloomberg DAPI not reachable -- sign in per integrations/bloomberg/READ_HERE.md section 2`, refresh rc 4. It fires
  at 09:00 ET, before the 10:28 ET sign-in, so same root cause as the pull.
- OPAL_vendor_watch -> `workflows/vendor_watch/run_vendor_watch.cmd` -> `vendor_watermarks.py` (Python311, S3 reads of
  Opal's own buckets, log `%USERPROFILE%\opal_vendor_watch\watch.log`). No project code in the header or path. Origin
  "Andrew-direct 2026-08-05", added f027c46613 by 0.0.0_AB_MSTR~Z. comp-find over org/missions (31 hits / 28,533 files)
  surfaced no owning register row on page 1, only citations. Owner: UNREGISTERED (author MSTR~Z). Healthy, rc 0.
- OPAL_restore_etf_daily_pull_20261009 -> no script; a one-shot `git checkout HEAD -- integrations/bloomberg/pipeline/etf_daily_pull.py`
  that ran 2026-10-09 08:00 ET, rc 0, with no further trigger. Owner 0.0.0_AB_MSTR~Z, record
  `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261008_202xZ_SYNC_PIN_BBG_PULLER_AND_REBOOT_WITH_FULL_ROSTER.md:20-25`
  (temporary pin of the round-1 bytes for dell1's acceptance run). It is spent; `git status` of `integrations/bloomberg/` is clean (MEASURED).
- Also seen (not asked): OPAL_DEMQUE_bbg_ledger_upload -> `data/mdpf/scripts/demque/bbg_ledger_upload.py` (MDPF_DEMQUE), rc 0.
  OPAL_BLOOMBERG-FreezeTripwire -> a Desktop VBS outside the repo (freeze investigation 2026-07-30), every 1 min, rc 0.

---

## Repair candidates

1. Sign the Terminal in NOW, before 07:00 ET tomorrow (pull, freshness, AMGT induction, ETF/constituents/price/rivalfunds
   legs, and BG's Bloomberg answers to colleagues). Touches: no file; READ_HERE.md section 2 fill -> verify the screenshot -> submit.
   Needs a human or a supervised seat at the box. The ledger allows it (last attempt 14:28Z, more than 6h before 07:00 ET).
   Confirm with a real refdata read (`dapi_check.py`), not `bloomberg_health`.
2. P0 gate vs an MCP-started bbcomm: `integrations/bloomberg/auth/bbg_fallback.ps1:55-56` treats a listening 8194 as
   "transient, don't sign in", but on this box bbcomm is routinely started by the BG MCP server whether or not anyone is
   signed in. Option: when 8194 listens but `dapi_check.py` fails, classify as "listener up, not entitled", which is
   still sign-in-warranted. This is a working-tree production file (an edit IS a deploy); needs the owner's ruling
   (OPAL_BBGTML / BG lane), not Andrew's act.
3. Unattended sign-in reliability: 8 of 30 runs failed this precondition; the 10-13 failure was focus lost between verify and
   click. Touches `bbg_signin.ps1` / `bbg_fallback.ps1` (re-assert focus immediately before the click, or one bounded
   re-fill on rc=4 since rc=4 spends no attempt). Owner ruling; production file.
4. Intake identity pin: `integrations/ticketing/intake/runner_config.json:11` `"identity": "opalbloomberg"` ->
   `"517aa5ee-b4d0-425a-b493-5a22ff77ac4f"` (the value 16fb949b5b put in the BG skill). Live-production file under bar A5-A7
   (exercise in the same act). CAUTION (INFERRED): the cursor last advanced around 09-03, so the first good pass may
   buzz every ticket opened since then into the client ticket channel. Read the cursor and the open-ticket count first.
   Then exits 5 (fetch) and 1 may surface (NOT MEASURED). Owner OPAL_TICKET_VNEXT has no live COO lane, so an owner must
   be seated or named. No Andrew act is needed unless the backlog buzz is client-visible (it is a client channel, so ask).
5. Teams watcher persistence: the 1770 s watcher depends on the BG session re-arming it. Options: make the arm success
   reach stdout (a one-line `[TEAMS-ARMED]`) so the agent can verify it, and have the BG session re-arm on every Monitor-end
   notice. Touches `.claude/skills/teams-assist/teams-watch.py` (live production, imported by the intake runner every 5 min,
   bar A5-A7) and `bbg-teams-assist/SKILL.md`. No Andrew act; note the alert/monitor moratorium before adding any new
   standing process.
6. TO-GUARD-4 merge: merge `rv-bbgtml-guard4` @3b65362444 (tzero tripwire CIX limb). Needs ANDREW'S WORD (the order says
   so); the branch is LOCAL only, so push it or keep worktree `C:/tmp/rv-guard4` alive until then.
7. Freshness task record: no fix needed. A manual re-run does not update LastTaskResult; read the log or the artifact,
   not the task record.

## Not measured

- Whether the Terminal is signed in right now. No refdata request was made (hard rule); the inference rests on wintrv.exe being absent.
- Which window took focus at ~07:02 ET (the 10-13 rc=4 abort).
- Whether the live Teams watcher has emitted or served any message since 15:38:57 ET, its cursor value, and whether the
  BG session will re-arm it at ~16:08 ET.
- Whether the intake runner's FETCH leg (svc-analyst-intake token, portal API) works today; after the pin fix it may fail
  with 5 or 1 instead. Also the size of the ticket backlog behind the cursor.
- Who triggered the 10:32 ET pull re-run: the BG log says the freshness summons did; the task history was not read.
- The `Bloomberg Updater` 0xC000013A result (10-12 18:26 ET) was not investigated.
- comp-find pages 2-4 for vendor_watch (only page 1 of 31 hits was read).
