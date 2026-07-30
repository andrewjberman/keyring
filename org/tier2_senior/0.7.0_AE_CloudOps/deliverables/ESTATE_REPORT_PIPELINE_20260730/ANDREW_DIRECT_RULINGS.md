# ESTATE REPORT pipeline -- Andrew-direct rulings received at the 0.7.0_AE_CloudOps~B terminal

Recorded per `org/XXX.md` ("RECORD DURABLY AND BROADCAST -- SAME TURN"; the phrasing IS the ruling,
never a paraphrase). Rulings 1-3 were received at the **CVO terminal** and are recorded by CVO in
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_RULING_SEMANTIC_EVOLUTION_PIPELINE_20260730.md`
(commits `438d1c98da`, `a83cf57bdb`). **This file records what arrived at MY terminal**, so the
compute-shape ruling is not carried only in one agent's session context.

---

## RULING 4 -- COMPUTE SHAPE (Andrew-direct, **0.7.0_AE_CloudOps~B terminal**, 2026-07-30 ~2205Z, VERBATIM)

> WE could have an EC2 do this with autostart implementation, that may be more logical

**Channel:** direct to `0.7.0_AE_CloudOps~B`, mid-turn, while I was grounding the compute shape.
**Status:** ARCHITECTURE DIRECTION, and it CONVERGES with what the estate independently says.
**Scope discipline:** I do not adjudicate scope. Recorded as received; surfaced to CTO + CVO + MSTR.

### Why this is not merely a preference -- the measurement that agrees with it

I was, at the moment this arrived, grounding whether an "existing kimi lambda structure" exists.
**It does not, in the form the phrase suggests.** Measured:

| Claim | Ground truth |
|---|---|
| A Lambda that calls Kimi | **ZERO.** Every `.tf` file in the estate mentioning `kimi` carries `aws_lambda_function` count = **0** (7 files: astn-pipeline iam/secrets, bd-49f-auto-login iam/instance/main, cot-pipeline ec2/iam). |
| Where Kimi is actually called | **On EC2, in Node.js.** `infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js:64-91` -- `https://api.moonshot.ai/v1/chat/completions`, model default `kimi-k2.6`, key from Secrets Manager `astn/kimi/api-key`. |
| What the "BD API setup" actually is | EventBridge Scheduler (DST-native) -> **orchestrator Lambda** -> start EC2 -> SSM run -> **always stop** -> fail-loud. `infra/aws/terraform/astn-pipeline/orchestrator.tf`. |

**So "the exact same as the BD API setup" and "an EC2 with autostart" are THE SAME ARCHITECTURE, not
two competing ones.** The Lambda in that pattern is the *orchestrator*; the Kimi call lives on the
transient EC2. Ruling 4 does not overturn ruling 1's "likely a lambda" -- it names which half of the
existing pattern does the work, and the estate's own wiring already answers it that way.

**Consequence for the spec:** clone the `astn-pipeline` orchestrator shape. Do NOT invent a
Kimi-in-Lambda path that has no precedent in this estate.

### RULING 4a -- the RATIONALE, same terminal, ~2210Z, VERBATIM

> in the event that it takes a meaningful amount of time (>900s) to scan the graph, analyze
> changes/co-changes, kimi analyzes the changes, etc.

**This is the correct constraint and the estate has already paid for it once.** `900s` is Lambda's
**hard** ceiling -- not a tunable. `astn-pipeline/orchestrator.tf:120-124` carries the scar in its
own comment: *"900s is Lambda's HARD MAX -- there is no bigger number available. The scrape already
needs >744s and is creeping, so the orchestrator can no longer reliably outlive its own job... Do
not 'fix' a future overrun by raising this -- it cannot be raised."*

**And it changes the design, not just the host.** The astn orchestrator **polls its EC2 job to
completion**, which re-imports the 900s ceiling into the orchestrator even though the work moved to
EC2. astn's mitigation is a compromise: derive the poll deadline from remaining Lambda time and, on
overrun, **leave the box running** for a separate 04:00 sweep to reap.

**I am NOT cloning that half.** See `SPEC.md` -- the orchestrator is **fire-and-forget** (start the
instance, return in seconds, never poll), and the EC2 **self-drives and self-stops**. The 900s
ceiling then binds nothing: an 8-minute run and an 80-minute run are the same architecture.
Andrew's constraint is satisfied structurally rather than by a deadline calculation that gets
tighter every month.

---

## CARRIED CONSTRAINT -- the pattern contains a BANNED component; clone the compute, NOT the alerting

`astn-pipeline/orchestrator.tf` -- the exact file I am cloning -- declares:

- `aws_sns_topic.astn_alerts` (line 13)
- `aws_cloudwatch_metric_alarm.orchestrator_errors` (line 139)
- an `sns:Publish` IAM grant (line 72)

These are **precisely** what the standing **2026-07-28 moratorium** forbids building
(*"We need to establish a moratorium on blindly creating alerts and SES and so on unless I
explicitly ask for it"*). Andrew asked for the **report** by name; he did **not** ask for an alarm.

**A pattern-clone is the single most likely way a moratorium gets violated by an agent acting in
good faith** -- the banned resource arrives as a side effect of "copy the working thing," and the
copier can point at a live precedent. Recorded here so the omission is a DECISION with a reason,
not a gap someone later "fixes" by restoring parity with the source module.

**Replacement (already design-canon, CVO 215615Z):** miss-detection is the **per-day manifest
ledger** -- each date born `PENDING`, flipped by the `/estate-pull` loop, any un-flipped prior day
loud at every CVO load. **A gate whose default state is the alarming one.** No SNS, no CloudWatch
alarm, no SES anywhere in this build.

---

## Standing authorizations for this build (recorded so no future agent re-litigates)

- **Moratorium:** does not bite -- Andrew asked for this report BY NAME. Build carries
  `# andrew-asked: "...that report is surfaced to a queue that is updated every day at 9a Eastern" (Andrew-direct 2026-07-30 ~2135Z)`.
- **Vendor egress (Kimi/Moonshot):** Andrew-direct **per-use** designation, **THIS pipeline only**.
  Not a blanket Kimi lift. Same shape as the arxiv precedent.
- **Schedule:** production pipeline => MUST have a schedule (NEVER-rule). Satisfied by construction
  via `aws_scheduler_schedule` + `schedule_expression_timezone = "America/New_York"`.

-- `0.7.0_AE_CloudOps~B`
