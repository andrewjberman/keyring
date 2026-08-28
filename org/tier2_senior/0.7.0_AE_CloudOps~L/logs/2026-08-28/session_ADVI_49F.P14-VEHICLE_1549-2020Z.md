# The campaign resumed and ran 117 dates clean; every one of my four errors was caught by an instrument that was not mine — 0.7.0_AE_CloudOps~L

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, COORDINATE, VALIDATE

**Date:** 2026-08-28
**Task Order:** ADVI_49F.P14-VEHICLE (the 534-date backfill campaign)
**Status:** IN PROGRESS — campaign live, 120 of 534 ARTIFACT-COMPLETE at 20:18:45Z

---

## Objective

Resume the P14-VEHICLE backfill campaign at a fresh seat: read the campaign oracle FIRST (dates
done, last artifact ts, HARD-STOP rows), report to `2.0.0_SA_COO` + `1.0.0_SA_CTO`, then re-invoke
the driver per its own contract. The campaign repairs 534 trading dates of 49 Financial ADVI gold
history that the scheduled path produced wrongly; the backfill's writes take the named
ad-hoc/backfill boundary and BECOME production history.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | XXX.md A.3 EXERCISE half — proved a forwarder RAN (own banner), not merely resolved |
| comp-state | `comp-state --self-test` | PASS | 4/4, its own N/N line; gated the drift read below |
| comp-state | `comp-state --project ADVI_49F` | PARTIAL | BEHIND/POST-CLOSE rows are lexical false positives — every evidence commit is about a different project (KEYFILL, PERFRP, DAILY_SPRINT). No real drift on this thread. |
| audit-archive-invoker | `python .tools/audit-archive-invoker.py` | WARN | rc=1, 2 findings, snapshot deferred (non-exec lane). Surfaced, not chased. |

**What worked:** `comp-state --self-test` as a gate is the right shape — it discriminates (4/4) before
its report is allowed to mean anything. The A.3 EXERCISE line earned its place: `PATH: 105 of 105`
resolves is the reading that went 100% healthy while every forwarder was dead on 2026-07-29, and only
running one distinguishes those worlds.

**What failed:** nothing in the comp rail. The instrument failures this session were mine, in raw AWS
CLI reads, and are recorded under Work Completed §5.

**Gap found:** none new. AE role minimum (`comp-pipescript io` + `comp-routes trace`) SKIPPED with
cause: this session changed no Lambda, no CloudFront, no gold script — the only artifact written was a
JSONL ledger, and the only AWS acts were `ssm send-command` through an already-deployed document plus
read-only `describe-*` / `lookup-events` / `filter-log-events`.

---

## Deployment Sequence

Not a Terraform/Lambda deploy. The AE sequence for this session is the campaign vehicle's own
dispatch loop, run 117 times; the table records the SESSION's shape, not one date's.

| Step | Action | Result |
|------|--------|--------|
| 1 | `/watcher` — register + arm persistent inbox Monitor | task `bax1pidoy`, banner `parent-tied: pid 1099778` (armed, not orphan-capable) |
| 2 | Read the oracle BEFORE any send | 3 JSONL lines -> 2 DATES; HARD-STOP rows blocking a resume: 0 |
| 3 | Commit the uncommitted row found at §1 | `0a41580505` |
| 4 | Driver `--status` then default `--plan` (read-only) | 534 re-derived; blackout CLEAR on the nightly's OWN artifact |
| 5 | Judge V14-4c(e) at this seat's face read | FINAL, not provisional (three inputs + 77146 V14-2 sequencing) |
| 6 | `--run --confirm-campaign-start` (background) | pid 1168780, 16:06:23Z; 62 dates before the halt |
| 7 | Halt at 2024-10-04; diagnose; re-invoke | `7c6aa7cea7`; second driver 18:32Z; date re-drove clean |
| 8 | Per-100 boundary report + ledger vintage | `0bc0e8e588` |

## Verification

Actual output, campaign ledger, tree read `2026-08-28T20:18:45Z`:

```
TREE: 122 lines -> 120 dates | COMPLETE 120 of 534 | newest 2024-12-24 | remaining 414
```

Push state of the ledger vintages, measured by `ls-remote` + `merge-base --is-ancestor` with a
negative control that discriminates:

```
origin/CLOUD @ f41fdaa7e7 (ls-remote 19:11:11Z)
  0a41580505  ON ORIGIN
  4db6ee10b3  ON ORIGIN
  7c6aa7cea7  ON ORIGIN
  control: origin NOT ancestor of 7c6aa7cea7 -- test discriminates
0bc0e8e588  LOCAL at close (rides the next integrator window)
```

Blackout verdict, read from the NIGHTLY'S OWN PRODUCED ARTIFACT rather than from the schedule
having fired (the driver's rule 4):

```
advi-49f-gold-floor   ENABLED   cron(45 12 * * ? *)
advi-49f-publisher    DISABLED  cron(15 13 * * ? *)
verdict 16:04:28Z     CLEAR -- POST-FIRE cleared: twr_daily date=2026-08-27
                      written 2026-08-28T12:47:23Z > anchor 12:45:00Z
```

---

## Work Completed

### 1. An uncommitted ledger row — the oracle was one row short on every other device

`git show HEAD:<ledger>` returned 2 lines against a 3-line worktree. Date 2's S3 writes had landed at
00:52Z; only the RECORD was device-local. This is the identical failure `2.0.0_SA_COO` 77114 item 4(i)
named on the FIRST row, recurring on the third, and it is the one failure the driver's contract cannot
absorb — a successor resumes from the ledger and would have re-driven a completed date while reading
its denominator one low. Committed `0a41580505`.

### 2. The campaign resumed and ran 117 dates

`--run --confirm-campaign-start`, strictly sequential, from date 3. Observed end-to-end cadence
109.8 s/date over the 49-date uninterrupted stretch after the 18:32Z re-invoke (ledger write
timestamps, not the SSM command wall median of 105.6 s — the gap is verify + ledger overhead).

### 3. Halt-class row 1: the runner host DIED mid-flight (trigger UNRESOLVED, six candidates excluded)

At ~17:58:2xZ the box went down between `2024-10-03` completing (17:58:23Z) and `2024-10-04`'s command
being dispatched (17:58:25Z). That command NEVER STARTED — `ResponseCode -1`,
`ExecutionStartDateTime` NULL, stdout empty. The driver halted IN PLACE with `ARTIFACT-INCOMPLETE`,
exit 0, exactly as designed.

| Candidate | Verdict | Instrument |
|---|---|---|
| `ec2-auto-shutdown-enforcer` | EXCLUDED | its OWN log SPARED the box at 17:56:17Z ("up 1.8h < 3.0h ceiling") |
| an EC2 API stop | EXCLUDED | CloudTrail, TWO indexes: my EventName sweep + COO's ResourceName index (0 events 17:50-18:05Z) |
| the document's `shutdown -h +2` self-halt | EXCLUDED | cmd `82ff84fb` Parameters = {Date, DeclaredHistorical}; `StartedByDispatcher` key ABSENT |
| a foreign SSM send | EXCLUDED | zero non-campaign sends in today's window (see §5) |
| the driver's own `halt_host()` | EXCLUDED | unbounded census of its 469-line stdout: `halting host` = 0, exceptions = 0, `nothing to halt` = 1 at line 466 |
| a platform scheduled event | EXCLUDED | `3.0.0_SA_CVO`: `describe-instance-status` 0 events, not spot, sys/inst ok |

An OS-level halt with no API event, no scheduled shutdown, no driver act and no foreign command.
UNRESOLVED, honestly, on one occurrence. I cancelled the dead command at 18:30Z so the driver's own
oracle could write the row rather than poll a dead host to its 3600 s deadline — disclosed in the
commit and accepted by both seats; it changed one field (`ssm_status`) and bought back 28 minutes.

`3.0.0_SA_CVO` 78704 then named the discriminator I had destroyed: on a STOPPED instance
`StateReason.Code` separates `Client.InstanceInitiatedShutdown` from `Client.UserInitiatedShutdown`
from `Server.*`, and `ensure_host_running` CLEARS it on resume. I read the ADJACENT field
(`StateTransitionReason` = "User initiated") at 18:19:46Z and stopped there; the 18:32:49Z resume
erased the one that answers "who". Pre-registered for any future unexpected-stopped resume.

### 4. Per-100 report #1, and the control that earned its place on first run

Printing the SSM send plane BESIDE the ledger row count found `2c8385ec` — a 00:53:16Z send for
`2024-07-10` that produced NO LEDGER ROW AT ALL. "Zero non-COMPLETE rows" read from the ledger alone
was structurally silent about it. A row count answers "what did I WRITE"; only the send count answers
"what did I DO". `3.0.0_SA_CVO` 78631 called this and was vindicated by its own instrument.

### 5. Four errors, mine, each caught by someone else's instrument

| Error | Mechanism | Caught by |
|---|---|---|
| "other lanes are driving this document TODAY" | rendered epochs `%H:%M:%SZ` — DATE discarded; every cited send was 08-26/08-27 and the principal was Andrew's own aws-cli | `2.0.0_SA_COO` 78681/78693 |
| "the nightly fires TWICE at 12:45:41Z" | same date-less render; it is ONCE PER DAY | `3.0.0_SA_CVO` 78704 |
| per-100 #1 stated 103 lines / 101 dates | counted the TREE, then committed, then cited the COMMIT — the live writer appended a row in between; the pin holds 104/102 | `2.0.0_SA_COO` 78917 |
| "arrives at the pause with 100-150 dates outstanding" | computed the duration and never SUBTRACTED it from the time to the anchor | me, while building `/exec-sum` |

A fifth, self-caught before it reached anyone: a JMESPath positive control written with inline
backticks returned `[]` on data containing two matching rows — the shell EXECUTED the backticks and
handed SSM an empty comparison. I reported the control failure instead of the answer it gave.

**The common shape, and it is the transferable half: in every case the citation and the measurement
came from different places, and my own output could not contradict me** — the date-less stamp had
deleted the disagreeing field, the emptied filter had deleted the rows, the tree count was never
compared to the object cited. Each needed an instrument I did not hold.

### 6. Startup, integration windows, law edit

`/watcher` + XXX.md Step 1b A.1/A.2/A.3/B/B.1/C; `/cloud-ops` one-shot; `CronList` empty (zero crons,
matching the Step 1b-F Tier-2/3 row). Rode five integrator windows (MSTR 15-18 + the leg-2 merge)
without a commit landing mid-window. `1.0.0_SA_CTO` law edit `@5fc6086005` marks the A.2
STALE-BASELINE + UNCOVERED-AUDIT-LOG pair OWNED-UNTIL-`rv0057-f001` — my 78274 was one of four
independent filings of that pair today; CVO corrected my "an exec startup remedies it" as FALSE on
measurement (exec A.2 also defers, DEVICE-CHAIN-PENDING).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Re-drive `2024-10-04` rather than halt for judgment | HARD-STOP means the ENUMERATION is wrong (never retried); ARTIFACT-INCOMPLETE from an invocation that NEVER STARTED is an infrastructure interruption. Re-driving re-tests nothing answered. CONCURRED by CTO 78667 + COO 78669; validated by outcome — the row superseded in place. |
| Cancel the dead SSM command at 18:30Z | 32 min InProgress against a host down 32 min; the driver would have polled to its 3600 s deadline. Cancelling made the invocation terminal so the DRIVER'S OWN oracle wrote the row. Disclosed, not silent. |
| Do NOT send the OS-journal read during a live date | Read-only does not make it safe; CONCURRENCY does. A non-campaign send competes for the same SSM agent and a stuck one becomes the next ARTIFACT-INCOMPLETE — the inbound hazard I had just filed. Routed to CTO, who ruled GO at the boundary. |
| Do NOT edit the running driver for the `DocumentVersion` pin | No mid-campaign driver change (CTO 78261 / COO 78669). Proposed the next natural boundary and asked CTO to rule. |
| Report the projection error immediately rather than let it stand | Two senior seats had built sitting clocks on it; the 534-of-534 triggers moved from "tomorrow afternoon" to ~09:00Z. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.7.0_AE_CloudOps~L/deliverables/ADVI_49F.P14-VEHICLE_CAMPAIGN_LEDGER.jsonl` | 4 vintages of the live-appended campaign oracle | Yes — see commit messages: `0a41580505`, `4db6ee10b3`, `7c6aa7cea7`, `0bc0e8e588` |

No code, no infra, no `.tf`, no gold script touched this session.

---

## Blockers

**NONE at this seat.** Nothing held, nothing stranded. The four-item bundle is GATED, not blocked —
`1.0.0_SA_CTO` 78961 set its boundary at CAMPAIGN COMPLETION with the 12:45Z pause as fallback, and
the executor names which boundary arrived.

Not blockers, listed so they are not read as mine:
- The halt trigger stays UNRESOLVED with six candidates excluded. A second occurrence is the next
  data point; the ledger is the instrument that produces it.
- The shared-runner inbound hazard is STRUCTURAL with ZERO instances today, owned on the substrate
  card's owner row by `2.0.0_SA_COO`'s disposition — no live actor to disarm.

---

## Current State

The P14-VEHICLE campaign is LIVE and unattended: driver pid 1168780 (second invocation, 18:32Z),
`org/tier2_senior/0.7.0_AE_CloudOps~L/deliverables/ADVI_49F.P14-VEHICLE_CAMPAIGN_DRIVER.py
--run --confirm-campaign-start`, dispatching `advi-49f-chain-dispatch` (riding `$DEFAULT`, currently
v3) to `i-01003b035d2988dfb` (bd-gold-layer-runner) one 2024 trading date at a time, ~110 s each. The
ONLY durable resume point is `ADVI_49F.P14-VEHICLE_CAMPAIGN_LEDGER.jsonl` — 122 lines / 120 dates /
120 ARTIFACT-COMPLETE / 0 non-COMPLETE at 20:18:45Z, newest `2024-12-24`, last committed vintage
`0bc0e8e588` (LOCAL; `0a41580505` / `4db6ee10b3` / `7c6aa7cea7` are on origin @`f41fdaa7e7`). The
driver re-derives the 534-date set at every invocation and completion is read from PRODUCED S3
ARTIFACTS (LastModified > send time AND `attestation_basis` matching the driven branch), never from
rc — so a successor resumes by re-invoking the same command with no arguments changed and re-drives
only dates lacking an ARTIFACT-COMPLETE row. Projected completion `2026-08-29T08:56:46Z` at
109.8 s/date (COO's independent window gives ~09:10Z); both land 3.5-3.8h BEFORE the 12:45Z pre-fire
pause, so the pause is the FALLBACK boundary, not the expected one. Two Monitors are armed: inbox
`bax1pidoy` and campaign-progress `b6zgwgop2` (per-100 boundaries, halt-class rows, 20-min stalls).

---

## Next Steps

1. **File per-100 report #2 at date 200 (~23:00Z)** — in the CORRECTED form: commit first; derive
   every ledger number from `git show <hash>:<ledger>`; JOIN on LINES not the date-keyed dict
   (date-keying drops superseded rows' `command_id`s — exactly 2 today); print each remainder with
   the INSTANCE it was counted on; print the send-plane snapshot's own timestamp.
2. **Land the four-item bundle at CAMPAIGN COMPLETION** (CTO 78961; fallback = the 12:45Z pause,
   name which arrived): (a) pin `DocumentVersion="3"` on the send, committed as protection for
   FUTURE runs and SAYING SO — it cannot cover this campaign; (b) `StateReason.Code` +
   `StateTransitionReason` read BEFORE `start_instances` in `ensure_host_running`; (c) substrate-card
   row-6 scope edit (ListBucket is prefix-scoped `AdviChain49fListScoped`, plus the borrowed
   identity's 8 further statements as the owner row's blast radius); (d) the OS-journal read as ONE
   bounded read-only `AWS-RunShellScript`, boot table printed BEFORE the boot read, dead boot by
   BOOT ID (the host has rebooted since — `-b -1` reads the wrong one), and the volatility caveat
   stated BEFORE the read so an empty journal is scored UNMEASURABLE, never a seventh exclusion.
3. **Report ACTUAL completion from the ledger, never from the projection** — `534 of 534` on a
   measured read.
4. **[2.0.0_SA_COO]** The base `0.7.0_AE_CloudOps` re-seat is a COO spawn act keyed on the measured
   534/534 read, projected ~09:00Z 08-29; this seat stays through the bundle and its completion
   report, release ruled then.
5. **[3.0.0_SA_CVO]** Date-200 acceptance read (~23:00Z) and the four-plane certifying read of the
   04:35Z INSURE fire — different host, no interaction with this campaign.
