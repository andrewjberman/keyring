# ANDREW-DIRECT 2026-09-09 ~21:4xZ, at the `1.0.0_SA_CTO` terminal -- VERBATIM

After this seat's per-project close-out read (OUTSET, CLDGRPH, COMPEFFICACY, ETFS_GUARDRAIL), his words, entire:

> "Ok we need to not be "waiting" on anything, anything that we'd be waiting for needs a manual trigger of some kind depending on
> the test type. ETFS GUARDRAIL is a perfect example, we are not going to just wait for October and hope it works, that needs to be
> closed out and proven. PLease go through each of these, assess anything that is "pending" some future date run, and include
> addedndums for each that mandate the requirement is contingent on a relevantly structured manual/test run."

Recorded 21:4xZ; broadcast the same turn to `2.0.0_SA_COO`, `2.0.0_SA_COO~A`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`, `4.0.0_SA_CRO`.
Scope, at the width of his words: the four projects named at this terminal; every acceptance that today reads on a FUTURE
SCHEDULED FIRE gains a manual form and the grade is contingent on that manual run. Acted on as four L4 addendums (below), each on
his 2026-09-03 scope-change word (the PRD adjusts mid-round; the loop cycles).

## THE MANUAL-TRIGGER RULE (how every addendum is structured, so the manual run PROVES rather than pretends)

A manual run is accepted as the EXERCISED form of an outcome only when it keeps the discriminator the scheduled fire exists to
produce. Five conditions, all five on every row:
1. **Same target, not a copy.** The manual run invokes the SAME target the schedule invokes (the rule's target: the state machine,
   the CodeBuild project, the ECS task definition, the instance's own boot units, the scheduled task's action) with the scheduled
   event's payload shape. Never a re-implementation, never a local script standing in for the cloud runner.
2. **Real plane.** Real keys, real catalogs, real inboxes, real devices. An artifact written to a QA key is a TEST; it grades an
   outcome only where the outcome is about the mechanism, never where the outcome is about what the estate READS. Writing to a
   SERVED key by hand is a served-output move: its own NEVER-2 entry, never-widen sign-off (CTO+COO), rollback named.
3. **Told apart on the artifact.** The manual run carries a run-id / trigger field (`trigger=manual`, the initiator in the build
   record, the state-machine execution name) so the grader can tell it from the scheduled fire on the artifact itself, never by
   the clock.
4. **The schedule's own firing is proven separately and from HISTORY, never by waiting:** the rule's prior rule-initiated
   executions (CloudTrail / `batch-get-builds` initiator / the state machine's execution list / the instance's start events)
   show the trigger fires; the manual run shows the code succeeds; the outcome is the conjunction. Where a rule has NEVER fired,
   a one-off near-term schedule expression on the SAME rule (an `at()` expression, then restored) is the manual form of the trigger.
5. **The next scheduled fire is confirmation, never a gate.** It is read if it is already there when the grader reads; nothing
   waits for it, and a grade never carries "pending the fire" again.

What this does NOT change: a bar that is APPLIED stays APPLIED; a real-world event no manual run can make (a market holiday that
has not happened yet) is read on the first one that HAS happened, and the record says which.

## THE FOUR ASSESSMENTS (what was pending a date, and its manual form)

### ETFS_GUARDRAIL (round 1, 1 of 8 REALIZED; every other grade was "10-01 or a rare real event")
- **FWD-3 (coverage on the served face) + FWD-5 (both inboxes receive) + FWD-6's alignment check:** the AUGUST 2026 report
  re-rendered by the SAME monthly orchestrator (`etfs-reports-monthly-run`'s target, started by hand with `month=2026-08`),
  published to the served key WITH the coverage line, delivered to aj@ and andrew@. A served-output move: NEVER-2 entry +
  never-widen sign-off (CTO+COO), the prior August artifact archived first; rollback = restore the archived object.
- **FWD-2 (cannot go out over incomplete data), FWD-7 (a surviving gap reaches Andrew), FWD-8 (ask-the-provider stays a
  stop-and-ask, 0 egress):** the SAME orchestrator started by hand for `month=2026-09` TODAY -- a partial month is incomplete
  by construction, so the refusal ladder runs for real: the HTML lands under `refused/`, the alert text is produced, the terminal
  email reaches andrew@ (the ONE send the SES carve-out authorizes, on the terminal path, on a real refusal), `coverage_egress_ask.json`
  is written and NO vendor is called (CloudTrail / the gateway's egress log read 0). The publish key is untouched by a refusal.
- **FWD-4 (a legitimately empty day is left alone):** the SAME September run reads `coverage_verdict.json` for 2026-09-07 (Labor
  Day, a real closed-market day that has ALREADY HAPPENED): class A, in no partner's holes list, no `daily/<partner>/2026-09-07.json`
  slice written for cottonwood or 49financial. No waiting for 10-01; the discriminator exists today.
- **FWD-1 (a missing day gets filled in):** the daily producer (`cot-etf-ownership-daily` / `bd-49f-etf-ownership-daily`) invoked
  by hand with the scheduled event's payload against a REAL hole -- the September coverage read names one, or the run's own
  `catchup_processed` on a date the producer missed; if the estate holds no real hole, a controlled one: one slice archived to a
  quarantine key under a NEVER-2 entry, the producer fired, `catchup_processed` naming the date, the slice's restore verified byte-equal.
- **The schedule's firing** (`cron(0 10 1 * ? *)` and the two daily crons) is proven from history: the executions that produced the
  published August artifact and the daily slices, listed with their initiators. 10-01 confirms; nothing waits for it.

### NFRA_OUTSET (round 3, every open accept "on a served day")
- **OS-s-19/20/21(cloud half)/22/23:** a MANUAL SERVED DAY -- the report host started by the SAME mechanism the 13:00Z rule
  uses (the rule's target invoked by hand, or `start-instances` on the replaced host, whose creation-boot units run the report by
  design), after the cloud-side freshness publisher (`opal-outset-freshness`'s CodeBuild) is started by hand (`start-build`, same
  project, same role, same keys); the report published to the SAME served key with the run's own `run_id`/`trigger=manual` on the
  propagation stratum; every OS-s accept read on THAT run. The 13:00Z fire tomorrow is confirmation (today's 13:00:45Z run already
  proves the schedule fires).
- **OS-s-21 (laptop drift half) + OS-s-22 (per-device consumer):** the drift publisher's scheduled task installed on this laptop NOW
  (his word here is the heads-up S25 asked for -- stated in this record so no seat waits on a second one) and run on demand
  (`schtasks /run`, the same action the schedule runs), then a second manual served day reads the device row with that vintage.
  No 09-11.

### NFRA_CLDGRPH (round 6, three accepts read "the next rule-initiated nightly")
- **S23 (the stitch producer), S30 (comp-aws deprecation), S31 (the vocabulary unified):** "a rule-initiated nightly SUCCEEDED" is
  satisfied by (a) an ad-hoc `start-build` of the SAME CodeBuild project SUCCEEDED with `producer=stitch-codebuild` (S23 has this:
  build daaedf78 / fe7ff348) or the SAME derive task run by hand (`ecs run-task` on the pinned task definition) for the nightly
  derive, AND (b) the rule's prior rule-initiated executions listed from `batch-get-builds` / CloudTrail (the stitch rule has 67 of
  them; the derive rule its nightly history). The 03:00Z fire is confirmation the CVO reads if present. Nothing in round 6 waits
  for a night.
- **S22 (the site-Z exercise):** already manual (two seats, three instants); no change.

### NFRA_COMPEFFICACY (ROUND_CLOSE; nothing date-gated -- gated on two of his acts and one seat's)
- **FWD-4:** his read of the packet is a MANUAL SITTING at any terminal at any time he names -- no roadmap dependency; the CVO's
  `/estate-pull` runs on his "go".
- **FWD-9 (the Codex-rail exercise CE-g-4):** runs on ANY Codex seat; `1.0.0_SA_CTO~X` is one, READY -- his word allocates it and
  the exercise runs the same day.
- **FWD-8:** the CVO's second-cut list is written now (not after the sitting; the sitting reads it), and one seat starts one piece
  of work from the ratified fourteen the same day -- the COO names the seat.

## RULE CLARIFICATIONS, 22:1xZ, on `2.0.0_SA_COO`'s four cut-shaping facts (94739; measured by `0.7.0_AE_CloudOps~W`) -- appended, never silently

- **(4) for a schedule that has NEVER fired** (the 08:30 ET freshness CodeBuild rule: 0 rule-initiated executions; the laptop drift
  task: 0 runs): "prove the rule fires from prior firings" cannot be met on day one, and an unsatisfiable rule gets satisfied
  dishonestly. The form is: the CONFIGURATION READ (state ENABLED, expression, timezone, target ARN, next fire in UTC) at the manual
  run, plus the schedule's FIRST fire recorded as the history the NEXT accept cites; the manual run on the same target grades the
  mechanism now. Where the platform allows it (an EventBridge rule), a one-off near-term `at()` on the SAME rule, then restored, is
  the alternative -- the initiator then reads the rule, not a person. A Windows scheduled task has no `at()` short of editing its
  trigger: configuration read + first fire is the form there.
- **(2)'s scope:** "real plane" and the served-output clause cover the OUTPUT THE ESTATE READS (for OUTSET: `daily/` and `manifest/`
  on the report bucket). A producer's seam prefix (`outset/`) is producer artifacts under each face's standing QA clause ("a hand
  publish is QA, permitted, never the exercise"): a hand publish there stays QA, no accept is ever read on one, and this is NOT
  retroactive -- today's five hand-written seam keys stand as the QA their faces said they were.
- **(3) needs a carrier, not a clock:** where the served artifact carries no trigger field (OUTSET's `run_bundle` = {coverage, run_pin,
  stages, started_at}; a manual and a scheduled run differ only by `started_at`), a cell ADDS the field -- the orchestrator writes a
  trigger token before it starts the host, the runner stamps `run_bundle.trigger` / `run_bundle.run_id`, and the field distinguishes
  UNKNOWN from SCHEDULED so an absent token never reads as a scheduled claim. Instance tags (a stale tag reads fresh) and CloudTrail
  inference (a second system, lagging) are not the carrier.
- **A manual run never overwrites the only proof of a prior act:** its date decides its keys; where today's keys hold the artifact that
  proves an earlier row (OUTSET's 15:32Z creation-boot report proving OS-s-20), the manual run waits for the next UTC day's keys --
  hours, not a scheduled fire -- and its NEVER-2 entry names the pins and the rollback.

## Push state
LOCAL on commit; origin/CLOUD @`c6bcb7b12b` (this seat's ls-remote 20:53Z; re-read at send).
