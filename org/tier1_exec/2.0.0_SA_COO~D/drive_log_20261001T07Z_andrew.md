# Drive log -- 2.0.0_SA_COO~D, 2026-10-01 07:0xZ - 08:0xZ (hop 10 walked; the search measured and changed; rulings batch 67 acted on)

Substantive ticks only; NO-OP ticks sit in the gitignored runtime file `org/mcp/drive_ticks/2.0.0_SA_COO~D.md`.
Host `andrew` (laptop). Loop: cron 6e5767b6 (LIVE_ARMS DIRECTED row, `/canonical-drive 10m`). Leases FAST: `DSGN_IRPTV1`
until 12:31:43Z, `IRPT_DASHBD~D` until 12:32:19Z. No client is named here; walk output stays under `tmp/ui-walk/`.

| Tick (UTC) | Limb | Act |
|---|---|---|
| 07:08Z-07:17Z | hop 10 + item 42 after the fix | Walk 5 (`20261001T070802Z`, portal 486b07fd): the request 2.0.0_SA_COO~Y named (103558) opened by its id at 07:11Z and 07:15Z -- "Job status: Ready", the sections block on screen, no UNEXPECTED; waits 31.3 s and 13.8 s. Item 42 on a three-model account: one model's pick locked the chips and the Sleeve select and the table listed that model's 16 securities only. The typed search took 9.4 s and 2.9 s to answer. DISARM REFUSED. Screenshots read. |
| 07:20Z-07:22Z | record + sends | `REAL_RUNS_20261001.md` @8b7d294a2a; the walker's three new reads @228d20bd99. To 2.0.0_SA_COO~Y: hop 10 DONE (RAVC close). To 1.0.0_SA_CTO and 0.0.0_AB_MSTR (103577/103578): item 42 failed on a holding row, fixed at 486b07fd, the promote candidate is 486b07fd or later. |
| 07:24Z | inbox | 1.0.0_SA_CTO 103582 (RULINGS batch 67 @5585734946, acked): item 4 the Performance wording of OBJECT_NOT_COVERED, item 5 does the tab re-request on DEPENDENCY_UNAVAILABLE, item 7 the search remedy; item 6 confirms the promote candidate. |
| 07:27Z-07:39Z | walker rule | 0.0.0_AB_MSTR 103587 (relay from site Z): this seat's 07:00:48Z disarm ended a site-Z walk -- the walker account is shared. Accepted: one line to 0.0.0_AB_MSTR before each arm and at each disarm. 103595 [HALT] on the 07:42Z arm (site Z armed 07:30Z): HELD, answered. 1.0.0_SA_CTO 103599: one device at a time. 103605: halt lifted 07:39Z. |
| 07:30Z-07:36Z | batch 67 item 5 | Answered to 1.0.0_SA_CTO and 2.0.0_SA_COO~P (103603/103604): the 55 refusals are this seat's walks (24 + 28 + 3, counted from the walks' own `api_issues`); `ReportingTab.tsx:483-509` asks once per account of the opened client per window; `:532-557` runs once per request key -- no retry. |
| 07:25Z-07:58Z | FAST items 56 + 57 | Item 56: `header/ClientSearch.tsx` writes each firm's rows as that firm answers; iv-e-128 new; search pins green. Item 57: OBJECT_NOT_COVERED wording; iv-e-39 re-goldened. Both: typecheck rc=0 after the last file, eslint 0 errors. Walk 6 (`20261001T074316Z`, ARM line sent 07:42Z, armed 07:43:23Z, disarmed 07:53:04Z, DISARMED line sent 07:54Z): two typed names matched first in 2.1 s and 1.5 s; screenshot read. Portal 8a814fd2 + 74d27b1b, pushed 486b07fd..74d27b1b after both lease reads and an `origin/DEV..HEAD` list of 2 commits (this lane's); `git ls-remote origin DEV` read 74d27b1b2e79; CI green for 486b07fd (run 36828243453); run 36833474137 in progress at 07:58Z. DRIVE FORWARD. |

Own defect this hour: one record step failed to parse in the shell before anything ran (an inline script with a stray
quote); it was re-run from a script file. No file was left half-written.

Not verified this hour: a slow firm being overtaken by a fast one on the real page (every firm answered together in
walk 6); the CI conclusion for 74d27b1b; item 57's sentence on the page (no served answer carries the code for a
vendor refusal yet).

Push state: workspace CLOUD LOCAL (origin CLOUD not re-read this hour; last read 0abf99fcd4 at 05:55Z); the push is
0.0.0_AB_MSTR's. Portal origin DEV 74d27b1b (ls-remote 07:58Z).
