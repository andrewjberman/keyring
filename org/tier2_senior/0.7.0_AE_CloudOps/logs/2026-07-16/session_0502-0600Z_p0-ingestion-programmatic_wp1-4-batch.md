# 0.7.0_AE_CloudOps -- Andrew P0 (ingestion-programmatic): WP1 mechanism named + honest holes, WP2 reduced-to-one-pull, WP4 census-corrected + retry fix, bd49f converter SCHEDULED, twins ARMED

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, VALIDATE, COORDINATE
**serial:** 0.7.0_AE_CloudOps | **date:** 2026-07-16 | **window:** ~05:02Z (CTO P0 dispatch, Andrew-direct "backfill first, incremental pulls scheduled henceforth") -> ~06:00Z

## Summary

1. **WP1-READ: the eclipse death NAMED end-to-end, every layer grounded.** Rule fired 6/6 days
   (TriggeredRules) -> trigger Lambda clean (starts the box) -> box (inf-bronze-runner t3.small,
   i-083ad9ae297f88e9f) launched daily and SELF-STOPPED LANDING NOTHING (AMEND 49's shape) -> mechanism =
   the boot code-sync FATAL on the 07-10T23:37Z basename collision ("the collision that broke bronze IS
   the collision protecting gold"); first dead boot 07-11 13:30Z, the morning after. REPAIR = my 22:57Z
   Door-5 de-collide; proven by the window run's own pulls (~B's TZ correction: the "22:04Z" raws were
   EDT renders of 02:04-03:03Z TODAY, run through the box's boot path DOWNSTREAM of the de-collide).
2. **WP1-FIX per CTO ruling (a) HONEST HOLES** (labeled-copies REJECTED -- eclipse vendor API is
   current-state-only; --date labels the partition, never the fetch): ruling-16 manifest LANDED at
   s3://opal-data-inf/bronze/eclipse/_meta/holes.json (5 dates, mechanism + census reading; repo
   a8600b645). C2 mirror read: ALIVE-STARVED-INNOCENT (ENABLED cron(15 14), fired 07-14/15 over a dead
   source; first loaded walk 14:15Z today). Eclipse twin = the EXISTING paused registry row -- arms ONLY
   on ~B's hold-lift + first post-release landing verify (today's 13:30Z + 14:15Z reads), per the row's
   own written condition.
3. **WP2 REDUCED TO ONE PULL by the pullers' own window math:** txn healed by run-7's --since default
   (pull_date-7 covers 07-09..16; 1,409,666 rows full-table continuity) + perf healed by TRAILING_DAYS=30
   ("a short outage is one gap-free window"). CTO ruled DATA-PARITY BINDS (event-shaped rows carry their
   own dates; per-date keys would fabricate a pull cadence + duplicate rows); WINDOW-COVERAGE MANIFESTS
   landed at bronze/{transactions,performance}/_meta/window-coverage-20260716.json. Positions = the one
   TRUE-VENDOR-VINTAGE dated pull (the API's own --backfill-days design proves time-travel): JWT ad-hoc
   refresh (approved; issued 05:40Z, 10h TTL), mode=backfill marker (HISTBF precedent -- suppresses
   boot-pull + self-shutdown, no race), box up, SSM 5898c94c dispatched
   (--start 2026-07-11 --end 2026-07-15 --upload-bronze), watcher b6wewuv88 armed (5-key landing +
   SSM-failure + timeout alarms). ~B converts behind the landings.
4. **WP4 CENSUS-CORRECTED (CTO accepted "the census instrument working on its own author"):** the smartx
   scheduler EXISTS -- smartx-assets-daily-pull-daily ENABLED cron(30 9) America/New_York, live-verified;
   it FIRES daily and the producer errors 100% (6/6 + 3/3): DirtyRunError = the fail-loud landing guard
   WORKING over ONE vendor-500ing feed (models_summary, platform=27d20c6b). Defect pair ruled: the feed +
   artifact swap = 0.5.0's lane; the Scheduler's DEFAULT RetryPolicy (185 attempts/24h hammering a 500ing
   vendor) = MINE, fixed: explicit retry_policy 2/3600s applied + live-read (smartx-pipeline-v1.6.0;
   stray mis-versioned v0.9.1 on the same commit surfaced-not-deleted).
5. **bd49f D1 CONVERTER SCHEDULED (WP-add, ~B contract @ 82b527d8b):** Lambda vehicle (single-file
   pandas+pyarrow converter = silver-family shape; SSM-to-runner rejected -- couples a daily schedule to
   the gold box's ~80min/night uptime), shim preserves the contract verbatim (--date fire-minus-1,
   forwarded-not-dropped event override, nonzero rc -> raise -> Errors metric), scope-exact role, applied
   8/0/0 + 0-diff (opal-assets-v0.22.0, sha uepzt0eC live-tied), cron(5 3) retry 2/3600s. 22a BATTERY on
   the landed role 9/9 discriminating (4 pos + 5 fence neg incl. bronze-write 17a + DeleteObject).
6. **PHASE-3 TWINS ARMED (the arm-window commit at its designed moment):** checker module APPLIED
   (opal-assets-absence-v0.1.0, 5/0/0) + cot-mirror 05:00Z / bd49f-pull 06:00Z / NEW bd49f-dims 05:00Z
   twins 3/0/0 (opal-assets-v0.23.0), registry-driven input. INF mirror twin deliberately absent per its
   paused row.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-grep / comp-glob | ~15 sweeps (producers, args, jwt, TF grants, twins) | PASS | located every mechanism source-side |
| comp-pipescript deployed | pull_inflection_positions_daily | SKIP (stale sovereign-block guard) | TOOL GAP: still enforces the LIFTED 07-14 49F block -- routed in evidence |
| terraform plan/validate/apply (safe-apply) | 4 applies: retry-fix 0/1/0, checker 5/0/0, converter 8/0/0, twins 3/0/0 | ALL 0-diff after | targeted throughout |
| commit-gate.sh | shim + vendored converter | PASS 2/2 | |
| build-and-upload.sh | opal-assets-bd49f-dim-convert | write-VERIFIED sha uepzt0eC | |
| simulate-principal-policy | 9-arm battery on the landed converter role | 4 allow / 5 implicitDeny | one --resource-arns per call, positives isolated |
| aws primitives | TriggeredRules x3, scheduler get/list, lambda get-config x4, logs filter x3, s3 listings, SSM x3 | grounded every claim | rail-checked markers on gated calls |

**What worked:** the layered read (rule metric -> trigger log -> box state -> record timeline) naming the
death without touching anything; the pullers' own docstrings collapsing WP2 from 15 pulls to 1; the
import-closure lesson applied preemptively (converter vendored with closure verified). **Gaps found:**
comp-pipescript's stale sovereign-block guard (lifted 07-14, still enforced); the Scheduler 185-retry
default (now a named class -- check every existing schedule at natural touches); my lingering-CWD defect
recurred twice more (module-dir cd not returned) -- root-cause habit fix: absolute paths + explicit cd back.

## MCP traffic
~8 in / ~8 out. CTO P0 dispatch + queue-add + rulings x4 + batch GO; ~B contract + vehicle-TZ answer;
0.5.0 C5 contract. Out: WP1-read evidence + roll-up + batch evidence; ~B vehicle note + WP2 pairing;
0.5.0 contract ask.

## Blockers
None stranded. OPEN WATCHES (a successor picks these up if the session ends):
- WP2 watcher b6wewuv88 (expires ~06:42Z): on 5/5 -> ping ~B for silver conversions, RESTORE the mode
  marker to bronze-pull (or delete) + stop the box (the backfill marker suppresses the daily pull -- a
  forgotten marker = tomorrow's 13:30Z boot skips its pull; the WP2 ledger does NOT close with the marker
  in backfill state). On FAIL/timeout -> read SSM invocation output, box state, escalate.
- 13:30Z box natural fire read (WP1 close instrument) + 14:15Z C2 mirror first loaded walk read -> on
  both green + ~B hold-lift signal: UNPAUSE the inf-mirror registry row + arm its twin schedule.
- 03:05Z tomorrow: bd49f converter maiden fire (~B reads as contract author; twin 05:00Z backs it).
- Batch-3 answers (portal-calc + infrastructure_monitor) to MSTR; aws_access.py renormalize; Door-5
  revert.sh armed untouched until the AoR window closes.

## AMEND (07:00Z) -- WP2 CLOSED: 5/5 landed on dispatch 3; both failures loud-and-caught

Dispatch 1: box role 403 on code/manual_api/ (reads code/bronze/ only) + MY OWN SSM harness swallowed the
rc through a tail-pipe (ssm=Success over a dead pull -- the watcher's expiry alarm caught it; the
watcher's own key-query was ALSO malformed -- two broken instruments, one working alarm leg). Dispatch 2:
import closure (rate_limiter -- third closure-class catch tonight). Dispatch 3 (full 3-file closure from
code/bronze/, pipefail + explicit rc): bronze/positions/2026-07-{11..15}.jsonl.gz ALL LANDED 06:50-06:58Z
(2.178-2.188MB each, true vendor vintage, ONE ranged invocation). Mode marker RESTORED to bronze-pull
shape + box STOPPED (ledger-close conditions). ~B's dated conversions firing. CTO evidence 070042Z.
WP1+WP2 acceptance census waits only on the 13:30Z box fire + 14:15Z mirror walk reads + eclipse twin arm.
