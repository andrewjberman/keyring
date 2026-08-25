# ANDREW-DIRECT 2026-08-25 ~17:4xZ -- `comp-triggers` should cover the trigger-plane question

**received by:** `0.4.0_DS_ClientPlatform~M` (Andrew wrote directly to this worker seat)
**channel:** the `~M` terminal, mid-turn, during MDPF_COTREMEDIATION execution
**recorded:** same turn, per CLAUDE.md "Andrew-direct instructions -- RECORD + BROADCAST"

## VERBATIM

> **"comp-triggers should be geared for this kind of thing"**
>
> **"if its not already"**

**NOT A PARAPHRASE. The phrasing is the ruling.** Two messages, seconds apart, one instruction.

## CONTEXT HE WAS RESPONDING TO

Immediately prior, three false claims were made across two seats in ~30 minutes, all from the same
blind spot -- **EventBridge *Rules* and EventBridge *Scheduler* are TWO SERVICES and no single AWS
call sees both**:

- `2.0.0_SA_COO` x2: *"the trigger may never fire"* and *"there is no scheduled MDPF gold run --
  not a stale one, NONE"*. Both FALSE, both broadcast to four seats, both overrode MSTR.
- `0.4.0_DS_ClientPlatform~M` (this seat) x1: *"No EventBridge rule targets the MDPF publisher
  directly"*, reasoned from `aws events list-rules` -- 137 rules, auto-paginated, materialised
  client-side, denominator printed. **Every retrieval control was correct and the POPULATION was
  wrong.**

Ground truth: **155 trigger objects, 137 rules + 18 schedules.** `mdpf-scheduled-floor`
cron(30 13 * * ? *) ENABLED targets `mdpf-gold-lambda`; `opal-assets-mdpf-portal-publisher-daily`
cron(50 13) targets the publisher.

## THE ANSWER TO HIS "IF IT'S NOT ALREADY" -- MEASURED, NOT ASSUMED

**The tool EXISTS and is named `comp-trigger` (SINGULAR), not `comp-triggers`.** Its own description:
*"EventBridge/Scheduler trigger-dispatch FORENSICS (read-only): what fires X"*. It resolves via
`comp-which "what triggers this lambda -- schedule or event"` at score 1.50.

**AND IT SCANS BOTH PLANES -- its denominator line proves it:**
`denominator: 137 events-rules + 18 schedules scanned, region us-east-1`

**SO THE COVERAGE IS THERE AND THE ANSWER IS STILL WRONG. MEASURED DEFECT:**

```
comp-trigger mdpf-gold-lambda
  denominator: 137 events-rules + 18 schedules scanned, region us-east-1
  NO MATCH by name or target-ARN substring.
```

**FALSE NEGATIVE.** Ground truth, verified at source this turn:
```
aws scheduler get-schedule --name mdpf-scheduled-floor
  mdpf-scheduled-floor  ENABLED  cron(30 13 * * ? *)
  Target.Arn = arn:aws:lambda:us-east-1:313476888478:function:mdpf-gold-lambda
```
The target ARN contains the literal string `mdpf-gold-lambda`, and the tool advertises matching
"by name or target-ARN substring". It scanned that schedule and did not match it.

### MECHANISM, isolated with two controls

| test | result |
|---|---|
| **CONTROL A** `comp-trigger mdpf-scheduled-floor` (by SCHEDULE NAME) | **MATCHES** -- `matched by: name`, but prints **`schedule: -`** (no cron shown) and **NO `target:` line** |
| **CONTROL B** `comp-trigger mdpf-feeder-trigger` (RULES plane, by TARGET ARN) | **MATCHES** -- `matched by: target-arn`, prints the target ARN, the event-pattern, AND live fired-evidence |
| **the data is available** | `aws scheduler list-schedules` **DOES return `Target.Arn`** in its summary -- verified this turn |

**THREE DEFECTS, ONE ROOT: the Scheduler plane is enumerated but its `Target` is never read.**
1. A Scheduler entry is findable ONLY by its own name -- **never by the lambda it fires.** So
   *"what triggers X?"*, the tool's whole purpose, fails for every Scheduler-driven target whose
   schedule name does not happen to contain X.
2. `ScheduleExpression` is not displayed for schedules (`schedule: -`) though it exists.
3. No `target:` line for schedules, so a matched schedule does not tell you what it fires.

### ⛔ WHY THIS IS WORSE THAN A PLAIN MISS, AND WHY HE IS RIGHT THAT IT MATTERS

**The tool PRINTS AN HONEST DENOMINATOR (`137 + 18 scanned`) AND THAT MAKES THE FALSE NEGATIVE MORE
CONVINCING, NOT LESS.** A reader sees both planes counted and reads `NO MATCH` as authoritative.
This is CLAUDE.md's own named class -- *the denominator certifies the SWEEP, never the PATTERN* --
and here the sweep genuinely covered 18 schedules while the match could not reach their targets.

**The tool's caveat line names S3-notification triggers as its known blind spot and does NOT name
this one** -- so its disclosure points away from its actual failure.

## DISPOSITION

- **`comp-trigger` EXISTS** -- so the answer to *"if its not already"* is **partly yes**: the tool and
  the both-planes scan are there; the **target-resolution for the Scheduler plane is not.**
- **This is a comp-tooling defect and CLAUDE.md is explicit that a comp-tool coverage gap is a
  DEFECT, not an inconvenience** (Andrew-direct, prior: *"the comp-tooling is not additive, it is
  foundational"*).
- **NOT SELF-ASSIGNED.** This seat holds a live P0 (`MDPF_COTREMEDIATION`, one-project-per-instance)
  with global still frozen and NEVER#6 OPEN. Routed to `1.0.0_SA_CTO` as the comp-tooling owner,
  surfaced to Andrew with the measurement so he can direct it wherever he wants. **Surfacing, not
  adjudicating scope.**

**Measured by `0.4.0_DS_ClientPlatform~M`, 2026-08-25, at the seat: the `comp-trigger` invocations
above, both controls, the `aws scheduler get-schedule` ground truth, and the `list-schedules`
Target-field check.**
