# The daily sprint's population: per-device commit tracking vs a scheduled 3:30 PM integrate -- research and recommendation

**Author:** 4.0.0_SA_CRO~Z. **Asked by:** Andrew, directly (record
`ANDREW_DIRECT_20261003_215xZ_DAILY_SPRINT_PUSH_WINDOW_RESEARCH.md` beside this file). **Date:** 2026-10-03 ~22:3xZ.

**Research only.** Nothing is built, scheduled, pushed or changed on the basis of this file without Andrew's explicit directive.

**Method:**
- Read the sprint's code: `infra/aws/lambda/daily_sprint_generator/lambda_function.py`, `infra/aws/terraform/daily-sprint-generator/main.tf`,
  `daily_reports/scripts/commit_census.py`, `.tools/daily-sprint.py`, `.claude/skills/daily-sprint/SKILL.md` and
  `.claude/skills/integrate/SKILL.md`.
- Read the served reports' own `source` lines (`daily_reports/data/`).
- Measured on the site-Z repo with one script: commit times from `git log --all --no-merges`, and landing times from this device's
  reflog of `origin/CLOUD`.

**Limit of the measurement:** the reflog shows when THIS device saw origin move, so "on origin by 4:10" is a LOWER bound. A laptop
push that site Z had not fetched yet counts as late here. 2026-10-01 agrees with the report's own record ("read 0 pushed commits").

## 1. How the sprint works today (measured in code)

- **When:** EventBridge `cron(10 20 * * ? *)`, which is 20:10 UTC (`main.tf`). The `eod_update` job reads the served page about 2
  minutes later (`daily_reports/eod/README.md`).
- **What it reads:** a fresh blobless clone of the `CLOUD` branch from GitHub, so **only pushed commits**. The file says so itself:
  "THE CLOUD SEES ONLY WHAT IS PUSHED" (`lambda_function.py:38`).
- **Its window:** `commit_census.py --window et` counts commits from **00:00 ET to the run**, by commit time
  (`day_window`, `:39-51`).
- **What else it reads from the pushed clone:** Andrew's notes for the day (`daily_reports/notes/<day>.md`), the directive register
  and the day's records. An unpushed note does not reach the run either (LD-0616, 2026-10-01).
- **Re-runs:** the Lambda takes `{"date": "YYYY-MM-DD"}` for a re-run (`handler`, `:548`). Republishing a served day needs the
  never-widen sign-off (LD-0616).
- **Pushing CLOUD:** only the two MSTRs push it, "only on Andrew's word while he is at the terminal" (`org/XXX.md` 1b; LD-0367,
  LD-0368, LD-0522). The push is also a deploy: the pre-push gate uploads every deploy-scope `.py` in the pushed range to S3
  (`/integrate` Step 2).

## 2. What the 4:10 report misses (measured, 2026-09-24 to 10-02, Eastern days)

There are three separate gaps. Andrew's question names the first; the other two came out of the measurement.

**Gap 1: work not pushed by 4:10.**

| ET day | commits 00:00-16:10 ET | on origin by 16:10 (lower bound) | landed later that evening | landed on a later day |
|---|---|---|---|---|
| 09-24 | 746 | 660 | 53 | 33 |
| 09-25 | 349 | 268 | 54 | 18 |
| 09-26 | 635 | 329 | 7 | 294 |
| 09-27 | 488 | 111 | 12 | 364 |
| 09-28 | 359 | 300 | 16 | 14 |
| 09-29 | 829 | 362 | 445 | 12 |
| 09-30 | 1,007 | 926 | 65 | 0 |
| 10-01 | 1,214 | **0** | 1,181 | 4 |
| 10-02 | 1,031 | 913 | 85 | 28 |
| **total** | **6,658** | **3,869 (58%)** | | |

- Two of the ten days measured read zero (10-01 above, and 10-03 so far: 0 of 337).
- The served record confirms it. The 09-29 and 10-01 reports were redone by hand after the push, replacing scheduled editions that
  "saw pushed refs only" and "read 0 pushed commits".

**Gap 2: work after 4:10 PM ET is never reported (new finding).**
- Each report counts 00:00 ET to the run, and the next day starts again at 00:00 ET. So every commit between 16:10 and midnight ET
  falls outside every report, pushed or not.
- Measured: **3,249 of 9,907 commits (33%)**, between 15% and 62% per day. **Neither option in the question fixes this.**

**Gap 3: daylight saving.**
- EventBridge cron runs in UTC, so from **1 November** 20:10 UTC is **3:10 PM EST**. `main.tf` already warns about this.
- After that date a 3:30 PM integrate would run after the sprint, not before it.

Together: about **39%** of the period's work (3,869 of 9,907) reached the 4:10 reports measured here.

## 3. Option A -- track commits on each device

**Structure needed:**
1. **On each device**, a scheduled task at about 4:00 PM ET (Windows Task Scheduler, so it survives a reboot). It writes that
   device's commit census for the window to one S3 key per device per day: hash, author, commit time, subject and files, plus the
   day's notes file if present.
   - It reads `git log` on `CLOUD` and the local worker branches that will merge, not every scratch ref, so abandoned branches do
     not count.
2. **In the Lambda:** read both device files plus the pushed clone, union by commit hash (one commit counts once however many
   places hold it), and state on the page's `source` line which devices reported and when.
3. **Fallback:** a device that did not report falls back to its pushed commits, and the page says so.
4. **Changes outside the code:**
   - a new S3 address and the device tasks' names come from the naming builders (rule 30);
   - Lambda read access to that prefix;
   - a never-widen sign-off, because the served report's population changes.

**Pros:**
- Counts work when it is done, whether or not it is pushed.
- Needs no change to who may push CLOUD, and triggers no deploy.
- Its failure is partial and disclosed: one device missing, named on the page. It never silently reads zero.
- Andrew's notes reach the run without a push.

**Cons:**
- Two new device-side jobs. A device that is asleep, rebooting or out of disk at 4:00 is missed for that day. This week saw a
  reboot, a disk-full wind-down and an 18-hour seat stall.
- A new S3 surface and IAM change to own.
- The page can count work that never reaches the shared trunk (rare: a branch abandoned before merge).
- It does nothing to keep the two devices in sync.

## 4. Option B -- a scheduled cross-device /integrate at about 3:30 PM ET

**Structure needed:**
1. **Andrew's standing word** to push CLOUD on a schedule without him at the terminal. That changes the shared-branch rule in
   `org/XXX.md` (law-locked: an Andrew-direct record plus `ANDREW_LAW_EDIT_ORDER`), with a ledger entry and a `LIVE_ARMS.md` row.
2. **Who runs it:** both MSTR sessions live at 3:30 PM with a daily loop. A plain scheduled script is the alternative, but it cannot
   resolve a conflict.
3. **Order:** one device pushes (3:30), then the other fetches, merges and pushes (about 3:45). The second push carries both devices'
   work.
4. **Merge discipline:** a merge window announced to live seats, the index control, and the tree check before the push
   (`/integrate` Step 1).
5. **Conflict path:** abort and send one agentbus line. Anything louder is a new alert, which needs Andrew's word (standing
   moratorium).
6. **Accept that each push is a scheduled production deploy** of whatever data scripts both devices committed that day.
7. **The DST fix (gap 3) is mandatory.**

**Pros:**
- One truth: the report, the repo and origin agree.
- A daily sync keeps the devices close and the merges small. 10-01 landed 1,181 commits in one evening merge.
- Uses the existing skill; no new pipeline.

**Cons:**
- Needs a change to a law-locked rule.
- The push becomes an unattended daily deploy.
- Large merges take 15-45 minutes in the hooks (`/integrate`). On a 1,000-commit day the second push may not land by 4:10, which is
  the zero day again.
- Depends on both MSTR sessions being alive at 3:30.
- Opens a merge window in the shared tree at mid-afternoon, while seats are working.
- Still misses work committed from 3:30 to 4:10, and all of gap 2.

## 5. Recommendation

**Option A, with two fixes that apply whichever option is chosen:**
1. **Fix the window (gap 2):** each report covers the time since the previous scheduled run (4:10 PM yesterday to 4:10 PM today),
   not 00:00 ET to the run. Then no hour of work falls outside every report.
2. **Fix the clock (gap 3):** run the sprint on EventBridge Scheduler with `America/New_York` as its timezone, so it stays at 4:10
   PM after 1 November.
3. **Then Option A for the push gap.**

**Why A over B:**
- B makes a reporting schedule depend on an unattended production deploy and a law change.
- B's failure cases (a conflict, a slow merge, a dead session) produce exactly today's zero day.
- A's failure case is one device missing, named on the page.
- A also answers the question the sprint exists for, "what got done today", in the time it was done.

Keeping the devices in sync is a separate decision. If Andrew wants a daily integrate for its own sake, it can run on its own
cadence, decoupled from reporting.

**The floor, if A is not built:**
- Make the census count what LANDED since the last run: the git range from the last run's origin hash to now, with the hash stored
  beside the report.
- Then nothing is ever lost. Late-pushed work appears in the next day's report instead of in none.
- This is code-only in the Lambda and the census scripts, and it moves served output, so it needs a never-widen sign-off.

## 6. Not established

- The laptop's own push times. Site Z sees them only when it fetches, so the per-day "on origin by 4:10" figures are lower bounds.
- Whether the laptop is reliably awake at 4:00 PM ET.
- The owner seat of the sprint Lambda for a build. Its history is LD-0574, LD-0588 and LD-0616; the CTO would place it.
- The cost of the never-widen sign-offs each change needs.
