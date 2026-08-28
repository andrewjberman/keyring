# /self-drive D2 & D3 — tick 15 (2026-08-28 18:49Z) — state: ARMED

Covers tick 15 (tick 14 logged @28ed06b53d; row 15 @26077ca5df). Cron bde882a4 (:07/:37; ran on
idle). Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: the tick-14 verdict
executed (round 2 cut, a DS lane seating), the plan-gate discharged, a halt-class campaign row
closed at three seats with the trigger honestly unresolved, two corrections owned by their authors.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs **30**
(D2 23 — +1 = ADVI_PERFRP.TO-R2-DS; D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342,
0 claimed-not-member. Live roster 13 (D2 lanes: DE~D release-eligible, AE~K applying, AE~L campaign,
DS~V seating; CVO base live).

## Calls (§1-2)

**Zero.** No new adjudicable call; no RESERVED. GATE A on PERFRP unchanged (source-gap half open —
round 2 now cut against it).

## Verdicts / rulings since tick 14 (§3)

- **Row 15 CONSUMED by COO — EXECUTED 3 of 3:** `ADVI_PERFRP.TO-R2-DS` CUT @700fc7d53b from the
  advi-perfrp decomp cells PRF-b-2..b-7 (round 2 = the b-series leaves RE-EMITTED on the
  campaign-corrected upstream; build-only cap; CVO's conditions (i)/(ii) verbatim on the face);
  BDPARITY's arming predicate stated on its face (first post-campaign emission, or
  manifest-carries-campaign-state); `0.4.0_DS_ClientPlatform~V` seating; DE~D's re-seat target named.
- **PLAN-GATE DISCHARGED — GO @18:4xZ (78677) on ~K's TO-A4-AEC saved plan** (3 add / 2 change /
  0 destroy, 5 targets). Read at this seat on the DESIRED plane: `git diff a57461f191^ f526a00753`
  over the two committed files — `InvokeRunner` gains exactly the data-lookup ARN (no action, no
  wildcard); env gains `INSURANCE_RUNNER_FUNCTION_NAME` only; rule/target/permission = the fees
  template with `runner=insurance`, `cron(35 4)` ENABLED; `_PAYLOAD_BY_TARGET` adds the `Payload`
  kwarg only for a mapped target, so main/fees keep their exact two-kwarg call (structural);
  `_RUNNER_BY_TARGET` is the marker vocabulary. ~K adopted both CVO P2s before the gate (cross-root
  ARN via `data.aws_lambda_function`; the "cot 02:00Z" stagger note was STALE — cot refreshes at
  07:30 America/New_York on the Scheduler plane; 04:35Z is ≥4h35m from every mint on both planes).
  ~K applies under a NEVER#6 ledger; acceptance = counts == plan, 0-diff re-plan, three IAM arms as
  separate invocations, live read-backs; **AC4 = the first scheduled fire 2026-08-29T04:35Z** (the
  same day's main run as the negative control). `INSURANCE_EGRESS=1` was re-read live by ~K and by
  CVO (CodeSha256 changed) — the deploy order holds.
- **~K 78680 — hold disclosure, ACCEPTED:** `a57461f191` landed 49 s inside window 17's hold
  because the OPEN arrived mid-`safe-commit`; blast radius none (an unapplied `.tf`). Mechanism
  recorded, NO gate built: a commit-side window-state check is a RAIL PROPOSAL for MSTR (window
  owner) + 0.8.0 (rail owner), obligations row 7 item (j), for Andrew's word at the sitting.
  Relayed to MSTR (LD-0116). Memory: `reference_an_inbox_hold_binds_only_between_tool_calls`.
- **Campaign halt-class row (~L 78662/78674/78697; COO 78670/78682/78694; CVO 78633):** the runner
  host stopped ~17:58:2xZ between dates (OS-level "User initiated"); 2024-10-04 ARTIFACT-INCOMPLETE
  from a never-started invocation — NOT a HARD-STOP; ~L cancelled the dead command (disclosed) so the
  driver's own oracle wrote the row, re-drove clean; **65 of 534**, 0 non-complete. Trigger
  **UNRESOLVED with every candidate excluded on a measured plane**: the idle enforcer (its own log
  spared the box 17:56:17Z); an API stop (CloudTrail 0 events on the instance 17:50-18:05Z, two
  indexes); the document's self-halt (the 2024-10-03 send's `Parameters` carry NO
  `StartedByDispatcher` key — my +2-minute hypothesis EXCLUDED at the plane that carries the
  parameter); the driver's own halt path (the driver started this host, so its guard read TRUE —
  censused unbounded over 469 lines of its stdout: `halting host` 0, controls both ways). CVO's row
  adds a `StateReason.Code` pre-registered read for a recurrence. **Two corrections owned by their
  authors:** ~L's "other lanes are driving the runner TODAY" was WRONG on when (a `%H:%M:%SZ`
  format dropped the DATE — the sends were 08-26/08-27) and on who (all 7 = Andrew's own aws-cli
  probes); withdrawn; the shared-runner hazard stays STRUCTURAL on the substrate card's owner row,
  not ARMED. ~L's first control failed on backticks in a shell-parsed JMESPath (the banked class).
  **RULED:** pin `DocumentVersion="3"` on the send at the 12:45Z blackout pause (the next natural
  boundary), not mid-run; per-100 reports print the SSM send count beside the row count. Memory:
  `reference_a_timestamp_without_its_date_is_not_a_timestamp`. **CVO 78705 (row landed
  @968090b2fc):** a SIXTH candidate excluded on the platform plane (0 scheduled events, not spot,
  status ok; CloudTrail by ResourceName 17:40-18:10Z = 2 routine AssumeRole events) — and **the
  discriminator existed and the resume destroyed it**: a STOPPED instance's `StateReason.Code`
  (`Client.InstanceInitiatedShutdown` vs `Client.UserInitiatedShutdown` vs `Server.*`) is CLEARED
  once it runs again; `ensure_host_running` erased the one field that answers "who" as its first
  act. PRE-REGISTERED for a recurrence: any resume that finds the host stopped unexpectedly reads
  and records `StateReason.Code` + `StateTransitionReason` BEFORE `start_instances`. Both SSM
  planes corroborate 0 foreign sends today (98 of 98 ids on both). **Correction owned here:** my
  78683 item 1 relayed ~L's "the nightly fires the document TWICE at 12:45:41Z" — the same date-less
  `strftime` (b3ff218d and 7b814f8e are 08-27 and 08-26); it is once per day, and a relay of a
  detail inherits the instrument that produced it.
- **CVO certs (base, third instrument):** P14-VEHICLE row 6 + V14-2 PASS (78633); INSR1DS-AC1 PASS
  (78635); INS-a-5 re-vehicle + TO-A3-AE + TO-A4-AEC PASS step-zero (78638) with AC3 re-pointed to
  (c′) (COO landed it) and the P2s above. CVO corroborated (c′) live (78655). Surprise-channel items
  4-6 (78645) closed with citations to standing rulings (78645 reply).
- **0.6.0 RELEASED 18:21:51Z** after (c′) completed (`INSURANCE_EGRESS=1` live 18:09:29Z, ledger
  20260828T1807Z 5/5; two provenance one-liners fixed). **DS~R released 17:48Z** (AC1 PASS, silver
  design + digest prep on the record; unmanifested-partition fork ruled: default SKIP-UNVERIFIABLE,
  `--backfill-manifest` once at the stage build with a parquet byte-compare; first-mint = step 0 of
  the build, two imports missing at the prefix; `safe-deploy.sh` header drift → row 7 item (i)).
- **DE~D:** AC10 PASS @537de2bf75 (6/13) on the merge's-second-parent baseline after a false
  confession was averted; ruling transcribed as a harness command with a negative arm that
  reproduces the incident (@a7924a327d); release-eligible; re-seat target = TO-R2-DS's first leaf.
- **Own-lane (quiet window):** `PROOF_OF_SPEC.schema.json` status enum lacks a terminal-by-
  supersession member — a four-postulate proposal before any edit.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @a57461f191, ls-remote read 18:49Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · `to-check --project
  ADVI_PERFRP` (roster: TO-R2-DS PENDING → DS~V) · `get_live_agents` (13) · ledger read · `git diff
  a57461f191^..f526a00753` (the plan-gate's DESIRED-plane read) · `git ls-remote` + MERGE_HEAD.
