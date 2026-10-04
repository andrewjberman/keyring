# Daily sprint: every hour reported once, on Eastern time, with each device's unpushed work -- brief and design (L1)

```
BRIEF PATH        docs/briefs/daily-sprint-window-and-device-census-brief-20261004.md
PROJECT           NFRA_SPRINTWIN (D0, site Z), placed by 1.0.0_SA_CTO~Z msg 29152; registered after PARITY CLOSED
ANDREW'S WORD     org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261004_173xZ_DAILY_SPRINT_WINDOW_ET_SCHEDULE_OPTION_A_BUILD.md
RESEARCH          org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/DAILY_SPRINT_PUSH_WINDOW_RESEARCH_20261003.md @c4a1ea0257
SIBLING WORK      0.0.0_AB_MSTR~Z + laptop 0.0.0_AB_MSTR: the /integrate parity
                  (org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261004_172xZ_INTEGRATE_PARITY_BEFORE_FABRIC_RESUMES.md)
EXISTING CODE     infra/aws/lambda/daily_sprint_generator/lambda_function.py; infra/aws/terraform/daily-sprint-generator/main.tf;
                  daily_reports/scripts/{commit_census,project_census}.py; .tools/daily-sprint.py
MEASURED AT       2026-10-03 22:3xZ (research) and 2026-10-04 17:4xZ (code read at CLOUD a2a5cb3a6a)
```

Andrew, verbatim: *"1.) I agree with the covered time, previous report to current report, that is a much better layout. 2.)
Agreed. 3.) I like Option A. Let's proceed with getting this incorporated and designed while the fabric is quiet. I'd like it if
we can get this worked into the /integrate parity that MSTR~Z is working on with the laptop box right now."*

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (FWD-1):** on one weekday, Andrew opens the 4:10 PM page and reads every commit made since yesterday's page.
That includes the work site Z committed at 3 PM and has not pushed, counted once, with the page naming which devices reported.

### O1 -- Every hour of work is in exactly one report
- Each report covers from the previous report's cut to this one's (4:10 PM ET yesterday to 4:10 PM ET today), not 00:00 ET to
  the run.
- Work done in the evening is in the next day's report. Today, 33% of commits are in no report at all (research section 2).
- A missed run does not lose its hours: the next run starts where the last PUBLISHED report ended.

### O2 -- The report runs at 4:10 PM Eastern every day of the year
- The schedule is held in Eastern time, so it stays at 4:10 PM after 1 November.
- Today 20:10 UTC becomes 3:10 PM EST, and two more places in the code assume the summer UTC-4 offset (PART IV, S5).

### O3 -- Work committed on either device counts the day it is done, pushed or not
- Before the run, each device publishes the commits it holds.
- The run counts the union of the pushed history and both devices' censuses. A commit counts once, keyed by its hash, however
  many places hold it.

### O4 -- The page says who reported
- The page's own source line names each device that reported, its census time, and how many of the counted commits were not yet
  pushed.
- A device that did not report is named as missing. Its pushed work still counts. The page never reads zero silently.

### O5 -- Andrew's notes reach the run without a push
- A note written on a device before 4:10 reaches that day's run through that device's census.
- Today a note reaches the run only once CLOUD is pushed (LD-0616, 10-01).

## PART II -- WHERE THE BOUNDARY SITS

| owned here | relied on, owned elsewhere |
|---|---|
| The report window, the schedule, the union and the disclosure (Lambda and census scripts; the deploy is 0.7.0_AE_CloudOps~A via Terraform, per CTO msg 29152). The device-side census emission is owned by each device's MSTR, in its /integrate lane (CTO msg 29152), and run as a scheduled task (MSTR~Z msg 29151). | **The /integrate parity** (MSTR~Z + laptop MSTR). Per MSTR~Z msg 29151, the census is NOT an /integrate step: /integrate pushes only on Andrew's word and needs a live MSTR session, while the census must run every day. /integrate CITES it: its Step 3 bus message names the census file's time. |
| | **Publishing to the served prefix:** `publish_daily_report.py`, unchanged |
| | **Republishing a served day:** the never-widen sign-off (CTO + COO), unchanged |

## PART III -- THE QUALITATIVE BAR

- Andrew never has to ask for a hand re-run because a device had not pushed. On 09-29, 10-01 and 10-03 the scheduled edition was
  replaced by hand.
- Over any stretch of days, the reports' commit counts add up to git's own count for the same span, with no gap and no double.
- When a device is down, the page says so in words, and the number on it is still true for what it covers.

## PART IV -- THE SUBSTRATE (measured in code at CLOUD a2a5cb3a6a)

| # | finding | evidence |
|---|---|---|
| S1 | The cloud run clones the pushed `CLOUD` and censuses it: "THE CLOUD SEES ONLY WHAT IS PUSHED". | `lambda_function.py:38`, `:593-598` |
| S2 | Both censuses cut `00:00 ET -> now` with `--window et`, and share one window function, so they agree. The Lambda refuses to publish if they disagree. | `commit_census.py:39-51`; `project_census.py:122`; `lambda_function.py:279-288` |
| S3 | The schedule is EventBridge `cron(10 20 * * ? *)`, in UTC. | `main.tf:66-68`, `:213` |
| S4 | A dated re-run exists: `{"date": ...}`. | `lambda_function.py:548-550` |
| S5 | **Two more hard-coded summer offsets:** the handler's default day uses UTC-4 (`:549-550`), and `_day_window` for the subjects uses `T04:00:00Z` (`:333-336`). Both are wrong from 1 November. | as cited |
| S6 | The local census already reads all local refs (`git log --all`), worktree branches included. That is the population MSTR~Z's point 2 asks for. | `commit_census.py:188` |
| S7 | A site-Z Scheduled Task runs the working tree, so a mid-edit script would run at 16:00 (MSTR~Z point 3). | MSTR~Z msg 29151 |

## PART V -- THE DESIGN (for the PRD; the decomposition and the sequence are step 5's)

### D1. The window (O1)
- On publish, the run writes one small watermark beside the day's pages: `window_start`, `window_end`, `origin_head`, and the
  devices that reported.
- The next run reads the newest watermark and starts there. With no watermark (the first run), it starts 24 hours back.
- A cap of 7 days stops a long outage producing one huge page. Anything beyond the cap is reported as uncovered, in words.
- The census scripts gain explicit `--since` / `--until` (UTC ISO) beside the existing `--window`. The Lambda and local
  `/daily-sprint` both pass the watermark, so a hand re-run and the scheduled run cut the same span.
- **The area chart's axis** becomes "4:10 PM yesterday to 4:10 PM today": 48 bins of 30 minutes, same renderer and same series
  assertion. The report's `date` stays the run's Eastern date, and its `window` label states the span.
- **A dated re-run of an earlier day** reuses that day's stored watermark. It never recomputes "since the previous report"
  relative to now.

### D2. The schedule (O2)
- Replace the EventBridge rule with an EventBridge Scheduler schedule: `cron(10 16 * * ? *)` with
  `schedule_expression_timezone = "America/New_York"`, a scheduler role allowed to invoke the function, and the same target.
- The handler derives its default day with `zoneinfo("America/New_York")`.
- `_day_window` derives its bounds the same way.
- That removes all three summer-offset assumptions (S3, S5).

### D3. The device census (O3, O5)
- **A stdlib script in `.tools/`.** Per device it writes ONE JSON file for the day:
  - `device` (from `.tools/agentbus-sqs.sh device`), `generated_at`, local `HEAD`, the `origin/CLOUD` it last saw;
  - `commits`: the hash, author, author time, commit time, subject and files, from
    `git log --all --no-merges --since=<now - 48h>`. The 48 hours cover the report window plus margin; the union dedupes by hash.
  - `notes`: the content of `daily_reports/notes/<today>.md`, if present.
- **Where it goes:** one S3 key per device per day. The address and the task names are `lib/opal_naming.py` builder output (rule
  30). A refusal means a registry row to add, never a hand-typed path.
- **When:** a Windows Scheduled Task on each device at 15:55 ET, with one retry at 16:02. The second try still lands before the
  16:10 run.
- **Pinned code (MSTR~Z point 3):** the task runs the script as it stands on `origin/CLOUD` (`git show origin/CLOUD:<script>`
  into a temporary file, then run that file), never the working tree.
- **Access:** each device's existing AWS identity is allowed to put the census prefix. The Lambda's role is allowed to get it.
- **Size:** about 1-2 MB on a 1,500-commit day (inferred). The files hold commit metadata only: no file content, no client data.

### D4. The union (O3, O4)
- The Lambda downloads today's device census files after the clone.
- Both census scripts gain an `--extra-commits <file>` input. They union those rows with `git log`'s by hash, drop rows outside
  the window by commit time, and count the result. Both scripts use the same union, so the Lambda's agreement check still holds.
- **Commit subjects for the authoring step** come from the same union.
- **Notes:** the repo's `daily_reports/notes/<day>.md` wins. Otherwise the newest device census's `notes` field is used.
- **The source line** (O4), for example: "4:10 PM yesterday to 4:10 PM today; pushed history plus device censuses from laptop
  (3:55 PM) and site Z (3:55 PM); 212 of 1,031 counted commits not yet pushed". A device with no file for today is named: "site Z
  did not report; its pushed work is counted".
- `team_activity.window` carries the span.

### D5. Where /integrate fits (MSTR~Z msg 29151)
- The census is NOT an /integrate step.
- /integrate Step 3's bus message names the census file's `generated_at`.
- After a parity, both devices' censuses describe the same set, and the hash key makes that harmless.

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-09-24 to 10-02 (research):
- 58% of 00:00-16:10 ET commits were on origin by 4:10 (lower bound), and two of ten days read zero;
- 33% of all commits fall after 4:10 PM ET and are in no report;
- the 09-29, 10-01 and 10-03 editions were redone by hand after a push.

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- The owners by step are the CTO's placement (msg 29152), not this brief's.
- Whether the laptop is reliably awake at 15:55 ET.
- The census file's real size on a heavy day: estimated, not measured.
- Any decomposition or sequence.
- That the window change needs nothing from the renderer beyond its existing bins. That is inferred from `timeline_frame` and is
  to be proven by a render.
- **Governance carried, not decided here:**
  - the never-widen sign-off, because the served page's population changes;
  - the Terraform safe-apply and image build, the deploying lane's;
  - registering each device's Scheduled Task, that device's MSTR.
