# NFRA_SPRINTWIN -- the daily sprint: every hour reported once, on New York time, with each computer's unpushed work

```json
{
 "project": "NFRA_SPRINTWIN",
 "directive": "D0",
 "fabric": "site-z",
 "prd_version": "v0.3",
 "step": 4,
 "brief_ref": "docs/briefs/daily-sprint-window-and-device-census-brief-20261004.md@547af2b735",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~Z` (L2-L4), 2026-10-04.
**Brief:** `4.0.0_SA_CRO~Z`, on branch `croz-sprint-census-20261004` @547af2b735. It drains to CLOUD after PARITY CLOSED.
**Placement:** home D0 (the daily-sprint run's ledger rows LD-0574, LD-0588 and LD-0616 all cite D0), fabric site Z, by this seat
(msg 29152). **Registered** @9f81b531fb (D0/NFRA) after PARITY CLOSED (0.0.0_AB_MSTR~Z msg 29158).
**The ENDPOINT is confirmed by Andrew** (2026-10-04 ~18:0xZ, *"Confirmed, proceed."*, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_18xxZ_NFRA_SPRINTWIN_ENDPOINT_CONFIRMED.md`).
**Sign-off:** proportionate (CLAUDE.md rule 27, single-round scale). `3.0.0_SA_CVO~Z` signs the ratified-text half; the brief half
is accepted because the CRO wrote the brief.
**Seats** (Andrew-direct ~18:4xZ at `4.0.0_SA_CRO~Z`, VERBATIM: *"I want you to drive the full completion of the daily-sprint update
we descirbed. that does not need to go to a new COO/team, you hsould be able to handle that solo on this device."*; record
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261004_184xZ_NFRA_SPRINTWIN_CRO_Z_BUILDS_SOLO.md`):
- build, decomposition and deploy: `4.0.0_SA_CRO~Z`, solo, on site Z. This replaces msg 29152's COO lane and its AE~A deploy owner.
- L8/L9: `3.0.0_SA_CVO~Z`;
- the mechanical gates stand: the never-widen pair, safe-apply, safe-commit and safe-merge, and the NEVER-2 ledger. The pair's CTO
  half is this seat; the COO half is `2.0.0_SA_COO~H` (placement v0.2, CVO~Z review finding 4: the solo change left it unheld).
  COO~H signs a half only. It holds no build, decomposition or deploy step;
- each computer's Scheduled Task: that computer's MSTR, in its /integrate lane (the laptop's on request from site Z).

## ENDPOINT (step 2, /endpoint --forward)

Landed verbatim as Andrew confirmed it. Brief @547af2b735 (174 lines). NOT READ: the TO register, any project JSON, any
decomposition (none exists).

```
  FWD-1  Andrew opens the 4:10 PM page and reads every commit since yesterday's
         page, including work a device committed and has not pushed
         DONE WHEN  EXERCISED -- one live trace: real commits on both devices, each
                    device's list written by its own script, the cloud job run over
                    the union, the page rendered and read (a QA location is enough)
         ACCEPT     The page shows work done today on either computer, counted
                    once, and says which computers reported; anything fed by a
                    made-up sample instead of the real thing fails it
         SOURCE     brief PART I, candidate thread

  FWD-2  Every hour of work is in exactly one report
         DONE WHEN  EXERCISED -- consecutive reports are run on demand, one run is
                    deliberately skipped, and the counts are checked against git's
                    own total for the whole span
         ACCEPT     Over any run of days the reports add up to the true total for
                    those days: nothing missed, nothing counted twice, even when a
                    day's report did not run
         SOURCE     brief O1, D1; PART III bullet 2

  FWD-3  The report runs at 4:10 PM New York time every day of the year
         DONE WHEN  EXERCISED -- the deployed schedule names New York time and has
                    fired at 4:10 PM once; the job, run for a date after 1 November,
                    picks the right day and window
         ACCEPT     The report arrives at 4:10 PM New York time today, and will
                    still arrive at 4:10 PM after the clocks go back
         SOURCE     brief O2, D2, S3, S5

  FWD-4  Work committed on either computer counts the same, pushed or not
         DONE WHEN  EXERCISED -- on one real pushed day, every commit read from a
                    device's list lands in the same kind of work, the same project
                    and the same half-hour as when read from the shared history;
                    a commit held in both places is counted once
         ACCEPT     A commit looks the same on the charts whether or not it was
                    pushed by 4:10 PM, and is never counted twice
         SOURCE     brief O3, D3a (Andrew: "that is crucial"), D4

  FWD-5  The page says which computers reported, and says so when one did not
         DONE WHEN  EXERCISED -- one run with a computer's list deliberately held
                    back names that computer as missing and still counts its
                    pushed work
         ACCEPT     When a computer is down, the page says so in words, and the
                    number on it is still true for what it covers
         SOURCE     brief O4; PART III bullet 3

  FWD-6  Andrew's notes reach the report without a push
         DONE WHEN  EXERCISED -- a note written on a computer and not pushed
                    appears in that day's run
         ACCEPT     A note you write on either computer before 4:10 PM shapes that
                    day's page, whether or not anything was pushed
         SOURCE     brief O5

  FWD-7  Each computer sends its list on its own before the report, from the
         published code
         DONE WHEN  EXERCISED -- each computer's scheduled task fires once and its
                    list is read; a deliberately half-edited copy of the script on
                    that computer does not change what it sends
         ACCEPT     Neither computer needs anyone to remember to push or send
                    anything, and a half-finished edit cannot change what is sent
         SOURCE     brief D3 (pinned code, MSTR~Z point 3); PART III bullet 1
```

## CONTRACTS

**C-ONE-PIPELINE.** This extends `daily-sprint-generator`. There is no second generator, no build-alongside run and no standing
comparator (CLAUDE.md NEVER, shadow pipelines). Classification runs ONCE, in the existing `commit_census.py` and
`project_census.py` (`classify`, `bin_of`, `commits_for`), over the union. No device classifies anything, and no rule is copied
(brief D3a).

**C-WINDOW (brief D1).**
- A published run writes one watermark beside its day's pages, holding `window_start`, `window_end`, `origin_head` and the devices
  that reported.
- The next run starts at the newest watermark's `window_end`. With no watermark it starts 24 hours back. The span is capped at
  7 days; anything beyond the cap is printed as uncovered, in words.
- `window_end` is the EARLIEST census `generated_at` among the devices that reported, and never later than the run. With no device
  reporting it is the run time. A commit made on a device after its census and before the run then falls into the NEXT window,
  where it is counted once; it is never inside a window that no census covers (v0.2, CVO~Z review finding 1).
- A dated re-run of an earlier day reuses that day's stored watermark. It never recomputes "since the previous report" from now.
- Both census scripts take explicit `--since` / `--until` (UTC ISO) beside `--window`. The Lambda and the local `/daily-sprint`
  pass the same pair, so a hand run and the scheduled run cut the same span. The Lambda's existing "the two censuses agree" refusal
  stays.
- The area chart's axis spans the window: 48 bins of 30 minutes, the same renderer, the same "every series sums to its count"
  assertion. The report's `date` is the run's New York date, and its `window` label states the span.

**C-SCHEDULE (brief D2).**
- An EventBridge Scheduler schedule, `cron(10 16 * * ? *)` with `schedule_expression_timezone = "America/New_York"`, targets the
  same function.
- The old EventBridge rule is removed in the SAME apply, so two schedules never both fire.
- The handler's default day and `_day_window` derive from `zoneinfo("America/New_York")`. That removes the three summer-offset
  assumptions (brief S3, S5).

**C-CENSUS (brief D3, D3a).** One JSON file per device per day, written by a stdlib script in `.tools/`. It holds:
- `device` from `.tools/agentbus-sqs.sh device`, `generated_at`, the local `HEAD`, and the `origin/CLOUD` it last saw;
- `commits` from `git log --all --no-merges --since=<now - 8 days> --name-only`, each row carrying exactly git's `%H` (sha), `%aI`
  (author time), `%cI` (commit time), `%an`, `%ae` and `%s`, plus the files. The look-back is the C-WINDOW cap plus one day, so one
  file covers any window the run can cut (v0.2, CVO~Z review finding 2; the brief's 48 hours assumed a 24-hour window);
- `notes`, the content of `daily_reports/notes/<today>.md` if present.

Commit metadata only: no file content and no client data. The scheduled task runs the script as it stands on `origin/CLOUD`
(written to a temporary file with `git show origin/CLOUD:<script>`), never the working tree.

**C-UNION (brief D4).**
- Both census scripts take `--extra-commits <file>`. They union its rows with `git log`'s by sha, keep rows whose commit time is in
  the window, and then classify and bin once.
- The run unions EVERY census file dated inside the window, from every device, deduplicated by sha, not only the run day's files.
  A device that missed today's census still contributes the unpushed commits its earlier files carry (v0.2, finding 2).
- The authoring step's commit subjects come from the same union.
- Notes: the repository's `daily_reports/notes/<day>.md` wins. Otherwise the newest device census's `notes` is used.
- The page's source line names the window, each device that reported with its census time, and how many counted commits were not
  yet pushed. A device with no file for the day is named as not reporting, and its pushed work still counts.

**C-HOMES AND C-NAMES (CLAUDE.md rule 30; `lib/opal_naming.py`).** PINNED by hop H0 (`4.0.0_SA_CRO~Z`, row @4201d79857): the
`sprint` row (class `PLATFORM_SUBSYSTEM`, owner D0, `owner_claim` measured from DIRECTIVES.yaml :39) is in
`infra/logic/registry/systems.json`, and `python lib/opal_naming.py validate` reads OK at 52 system rows. Every string below is
builder output at that registry.
- **The homes:**
  - the device census (v0.3: ONE OBJECT PER CENSUS RUN, never overwritten):
    `address('sprint', 'global', 'bronze', 'device_census', 'date=<D>', '<device>-<generated_at as YYYYMMDDTHHMMSSZ>.json')` =
    `s3://opal-data-assets/sprint/global/bronze/device_census/date=<D>/<device>-<stamp>.json`. Builder output was verified at
    v0.3: `.../date=2026-10-04/sitez-20261004T215100Z.json`. The run unions every census file dated inside the window by sha
    (C-UNION), so several files per device per day change no count. "Who reported" for a day reads the NEWEST file per device. A
    dated re-run reads exactly the files that existed for its stored watermark. (v0.1-v0.2 named one object per device per day,
    `<device>.json`; the 2026-10-04 served re-run overwrote site Z's copy, round-1 analysis ruling 1.)
  - the QA home for FWD-1's trace and the on-demand runs: `address('sprint', 'global', 'platinum', 'qa_page', 'date=<D>')` =
    `s3://opal-data-portal-v2/sprint/global/platinum/qa_page/date=<D>/`. No route serves this prefix. A QA run reads and writes
    its watermark here, never the served one, so a QA run cannot move the scheduled window. `gold` and `state` are refused for
    scope `global` under a non-product source (tiers.json home `source`), so `platinum` is the tier the rule admits.
- **The names.** The H0 row changed them: before it, `name('opal', None, 'sprint', 'daily')` resolved to `opal-sprint-daily`; with
  `sprint` registered the builder refuses it ("opal before 'sprint' reads as a null prefix", GRADING_RULE.md R2).
  - the schedule: `sprint-generator-daily`, from `name('sprint', None, 'generator', 'daily')`;
  - the scheduler role: `sprint-scheduler-role`, from `name('sprint', None, 'scheduler', 'role')`, and its inline policy
    `sprint-scheduler-policy`, from `name('sprint', None, 'scheduler', 'policy')`.
- This is a CONTRACTS edit, so it re-opens no half (the halves bind to the ENDPOINT hash).
- **The existing pipeline keeps its names and homes:** `daily-sprint-generator*` and `opal-data-portal-v2/daily-reports/`
  (rule 30 non-application, R19). The watermark sits beside the day's pages in that prefix (brief D1).

**C-ACCESS.**
- Each device's existing AWS identity is granted `PutObject` on the census prefix only.
- The function's role is granted `GetObject`, plus `ListBucket` conditioned on that prefix only.
- The function's role is granted `PutObject` + `GetObject` on the QA home, plus `ListBucket` conditioned on it (H0 pin: the trace
  publishes there with read-back, and a QA run reads its own watermark there).
- No other grant changes.

**C-SERVED (CLAUDE.md NEVER-1, NEVER-2).**
- **The first scheduled publish under the union changes the served page's population.** It goes under a never-widen pair (COO +
  CTO). The blast radius is that day's page keys plus the watermark. Rollback is a re-publish from the prior image digest, which is
  kept by the keep-last-5 policy.
- **The image move and the schedule swap** take one NEVER-2 entry. The image tag has one consumer, the function.
- **FWD-1's trace publishes to the QA home,** never to the served prefix.

**C-NO-NOTIFY.** No alarm, alert or monitor (the CLAUDE.md standing moratorium). A missing device is stated on the page.

## THE THREAD (FWD-1) -- round 1 builds it end to end

One person, Andrew. One journey: a page covering the span since the last report, with each device's unpushed commits counted once.
Each hop is a real call, and a hop fed by a fixture fails FWD-1.

1. **H0 homes:** the `sprint` systems row lands; the census and QA homes resolve, and are pinned here.
2. **H1 census script:** the `.tools/` stdlib script writes one device's file to its builder home. It runs once on site Z and once
   on the laptop, each from `origin/CLOUD`.
3. **H2 union:** `--since/--until` and `--extra-commits` in both census scripts, classified once over the union.
4. **H3 window:** the function reads the newest watermark, cuts the window (`window_end` per C-WINDOW), downloads every census
   file dated inside the window and runs both censuses on the union.
5. **H4 page:** the run renders the page with the source line, publishes it to the QA home with read-back, and Andrew reads it.

A build cell carries at most THREE mechanical criteria; repo-wide hygiene runs at the drain. The round-1 analysis ends in the
enrichment list.

## ENRICHMENT BACKLOG (off the thread, in order)

- FWD-4: the positive control on one real pushed day (work kind, project and bin agree per commit; one count for a commit in both
  places).
- FWD-2: consecutive on-demand runs with one deliberately skipped, summed against git's total for the span.
- FWD-5: a run with one device's file held back.
- FWD-6: a note written on a device and not pushed.
- FWD-3: the Scheduler swap, the zoneinfo day, and a dated run after 1 November. Then the first 4:10 PM fire, under C-SERVED.
- FWD-7: each device's Scheduled Task at 15:55 ET with one retry at 16:02, registered by that device's MSTR, plus the
  half-edited-copy negative arm.

## PATHS (the write surface)

**Owned:**
- `infra/aws/lambda/daily_sprint_generator/**`;
- `infra/aws/terraform/daily-sprint-generator/**`;
- `daily_reports/scripts/commit_census.py` and `daily_reports/scripts/project_census.py`;
- one new census script in `.tools/` (named by the decomposition);
- `.tools/daily-sprint.py` (it passes the same window);
- one row in `infra/logic/registry/systems.json` (H0).

**Read, never edited:** `daily_reports/scripts/publish_daily_report.py`, `lib/opal_naming.py`, `.tools/agentbus-sqs.sh`.

**Not this project's:**
- each device's Scheduled Task registration (that device's MSTR);
- the `/integrate` skill text (D5: its bus message names the census's `generated_at`, in MSTR's lane);
- the gateway; every other bucket and prefix.

## FIXTURES AND EVIDENCE

- FWD-1's trace is live: real commits on both devices, real files in the builder home, a real function run, the page read at the
  QA home.
- FWD-4's control runs on a real pushed day, never on synthetic rows.
- The CVO grades JUDGMENT criteria at L9, citing the contract clause.

## WHAT THIS PRD DOES NOT CLAIM

- Whether the laptop is awake at 15:55 ET. FWD-5 makes a missing device visible; it does not keep the device awake.
- The census file's real size on a heavy day (the brief estimates 1-2 MB).
- That the renderer needs nothing beyond its existing bins. That is the brief's inference, and H4's render proves or disproves it.

## SURFACE MANIFEST

**WRITES:**
- the census prefix (each device);
- the QA home (the thread);
- the served `daily-reports/` prefix plus the watermark (C-SERVED, after the pair);
- the function's image;
- the Scheduler schedule and its role;
- the removal of the old EventBridge rule;
- one registry row.

**READS:**
- the pushed `CLOUD` clone;
- the census prefix;
- the notes queue;
- the existing OpenAI and GitHub secrets (unchanged).

**NEVER:**
- a second generator, or any notifier;
- any other bucket or prefix;
- any client data.

## PROVENANCE AND AMENDMENT HISTORY

- v0.1 (2026-10-04 ~18:xxZ, `1.0.0_SA_CTO~Z`): first issue, on the brief @547af2b735 and Andrew's endpoint confirmation. Written
  on branch `ctoz-sprintwin-20261004` (@f15b8a86ce) under PARITY HOLD, and landed at its home after registration @9f81b531fb.
- Seats header @bbfd37b595: Andrew-direct ~18:4xZ, `4.0.0_SA_CRO~Z` builds solo.
- L4-R: ratified-text half SIGNED by `3.0.0_SA_CVO~Z` @43b01c88f8 (half 5d3955112dd8; review
  `org/tier1_exec/3.0.0_SA_CVO/deliverables/L4R_RATIFIED_TEXT_SIGN_20261004_NFRA_SPRINTWIN_v0.1_Z.md` @86efca38cb). PRD ADMITTED.
- v0.2 (2026-10-04 ~20:0xZ, `1.0.0_SA_CTO~Z`): CONTRACTS amendments owed before H3, from that review. Finding 1: `window_end` is the
  earliest reporting census. Finding 2: an 8-day look-back, and the run unions every census file in the window. Finding 4: the
  never-widen COO half is placed on `2.0.0_SA_COO~H`. These are CONTRACTS and header edits; the ENDPOINT is unchanged, so no half
  re-opens.
- v0.3 (2026-10-04 ~22:1xZ, `1.0.0_SA_CTO~Z`): CONTRACTS, from round-1 analysis ruling 1 (`ledger/ROUND_ANALYSIS.round1.md`).
  The device census is one object per run (`<device>-<stamp>.json`), never overwritten. The 2026-10-04 served re-run had
  overwritten site Z's day key. The ENDPOINT is unchanged, so no half re-opens.
