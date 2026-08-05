# Deploy-completion ledger: canonical-schwab-runner DECOMMISSION + TERMINATE

**Opened:** 2026-08-05T22:15Z by `0.7.0_AE_CloudOps~C` · **Status:** CLOSED 2026-08-05T22:32Z
**Authority:** Andrew-direct retirement ruling, relayed by `1.0.0_SA_CTO~B` in the instantiating brief
(20260805T204924Z), VERBATIM: *"analyse anything connected to it, see if anything consumes from it;
if not, DECOMMISSION AND TERMINATE."* Condition met (see Evidence). Conditional GO to execute:
CTO~B 20260805T220653Z, five conditions, all carried below.

**Lifecycle law:** RETIRED REQUIRES A RETIREMENT RULING -- "a retirement with no ruling is an outage
with paperwork." The ruling is the Andrew-direct instruction above; this ledger is its record.

## The act

Terraform targeted destroy of **11 runner-only resources** in workspace `canonical-schwab-ec2`,
including EC2 instance `i-0ed92ce2e72f505dc`. **Instance termination is UNRECOVERABLE.**

**S3 DATA UNDER `s3://opal-data-bd/canonical/schwab/` IS PRESERVED AND UNTOUCHED.** This is a
COMPUTE decommission, not a data deletion -- see "compute vs data" below.

## Why the box is dead -- four axes, each with its denominator

| # | Axis | Evidence | Denominator |
|---|---|---|---|
| 1 | **NEVER COMPLETED A RUN** | `run-canonical.sh:30-36` has `trap finish EXIT` shipping a log to `canonical/schwab/_runlogs/` on EVERY exit path incl. failures. That prefix holds **ZERO objects**. | Positive control: recursive list of `canonical/schwab/` = **484 objects**, so the empty read is a real absence, not a broken retrieval. |
| 2 | **NO REACHABLE START PATH** | Nothing emits `opal.canonical-xref`/`XrefRefreshSuccess`; zero `put_events` anywhere. Emitter assigned 2026-06-29, never landed. Prior measurement: 0 invocations/30d vs 33/33/17 for three sibling rules in the same call. | 9 matches / 8 files / 22,354 scanned -- every hit is the rule, a design doc, or a census artifact. |
| 3 | **NOTHING GRANTED READ ON ITS OUTPUT** | Exactly ONE principal references `canonical/schwab/*`: `canonical-schwab-runner-role`, the box's own role. | **1 of 208 roles** (IAM census 2026-08-05). |
| 4 | **NO LAMBDA CONSUMES IT** | Zero functions reference `canonical/schwab` in env. | **0 of 196 functions**, token-walked (NextToken walked; a single `list-functions` call returns a PAGE, not a total). |

**Supersession:** the canonical/schwab logic was RE-HOMED into the monolith --
`data/assets/scripts/gold/runners_49f/a01_dim_relationship.py:4` states it is
`data/canonical/schwab/silver/build_dim_relationship.py` "re-homed to GOLD". The live 49F path is
si2 -> `opal-data-assets`, which is also where CLAUDE.md Rule 17b points the estate. Last write under
`canonical/schwab/` is **2026-07-24 12:37Z**, by something other than this box.

**The rule was applied against its own explicit hold:** `runner-trigger.tf:13-16` carries
*">>> HELD: ... Do NOT apply until the xref bug is fixed + the sentinel emit is wired (CTO 194437Z). <<<"*
and is applied and ENABLED anyway.

## COMPUTE vs DATA -- why the prefix survives

`data/assets/scripts/gold/runners_49f/dryfit_driver.py:51` pins
`canonical/schwab/gold/advisor_attribution/date=2026-07-06/data.parquet`. It is a READ-ONLY,
zero-S3-write dry-fit harness reading a FIXED historical date. **It needs the DATA to exist; it does
not need the PRODUCER to run.** Deleting the prefix would break a live harness and discard parity
history. Terminating the box breaks nothing.

## Two corrections to the brief, established before acting (both CTO~B-accepted 220653Z)

1. **A rule DOES target the stopped box.** `canonical-schwab-xref-success` binds it via
   `"InstanceId": ["i-0ed92ce2e72f505dc"]` **inside the target Input payload**, not the target ARN
   (which is `automation-definition/AWS-StartEC2Instance` and names no instance). *"What targets this
   instance", asked at the ARN layer, is structurally blind to payload-bound targets.* This does not
   save the box -- the rule has never fired -- but it means the rule MUST die with it.
2. **The brief's candidate prefixes were the wrong bucket.** The runner WRITES
   `s3://opal-data-bd/canonical/schwab/{silver,gold}/` and only READS `opal-data-schwab`
   (`s8_gate.py:30`). `01_raw_quartz_validation/` is the **LIVE si2 box's** parallel-run landing zone
   (`EC2_MANIFEST.json:511`). Acting on the brief's list would have cleared the wrong prefixes on the
   wrong box.

## Blast radius -- reviewed BEFORE apply (CTO~B condition 1)

⚠ **This workspace also holds the LIVE si2 box's IAM + daily schedules.** An untargeted destroy here
would take down the sole 49F ingest for ADVI + MDPF. Targeting is therefore load-bearing, not
convenience.

- Baseline: plain `terraform plan` = **"No changes. Your infrastructure matches the configuration."**
  (clean 0-diff; no pre-existing drift to ride along).
- Targeted destroy plan: **`Plan: 0 to add, 0 to change, 11 to destroy.`** -- exactly the predicted
  set, nothing dragged.
- `aws_iam_role.events_invoke_ssm` confirmed runner-only (declared + referenced solely in
  `runner-trigger.tf`; si2 has its own `si2_daily_events_ssm`).
- **Untouched:** `aws_cloudwatch_event_rule.si2_daily[*]`, `aws_cloudwatch_event_target.si2_daily[*]`,
  `aws_iam_role.schwab_si2`, `aws_iam_instance_profile.schwab_si2`, all `schwab_si2_*` policies,
  `schwab_monolith_remap`, all KMS + Secrets Manager resources.

### The 11 destroyed

```
aws_instance.canonical_runner                      (i-0ed92ce2e72f505dc)  <-- UNRECOVERABLE
aws_iam_instance_profile.canonical_runner
aws_iam_role.canonical_runner
aws_iam_role_policy.canonical_runner_inline
aws_iam_role_policy_attachment.canonical_runner_ssm
aws_cloudwatch_event_rule.xref_success             (canonical-schwab-xref-success)
aws_cloudwatch_event_target.start_runner
aws_iam_role.automation_start                      (canonical-schwab-automation-start-role)
aws_iam_role_policy.automation_start
aws_iam_role.events_invoke_ssm
aws_iam_role_policy.events_invoke_ssm
```

Rule + start-path IAM die **in the same change** as the instance: an ENABLED rule pointed at a
terminated instance is both a **resurrection hazard** and a **false-green**.

## Open flag -- surfaced, NOT adjudicated

`org/projects/DATA_SSOTMG.json` is `status: active` (held behind ADVI_BREAKS) and this box was its
S4 component. Andrew's retirement instruction is later than that project state and governs the box.
**This ledger states the fact explicitly so an active project does not silently lose a component.**
Per CTO~B condition 5: that project's status is NOT flipped here -- not mine, not CTO~B's.

## Evidence

| | value |
|---|---|
| plan (baseline) | `No changes. Your infrastructure matches the configuration.` |
| plan (targeted destroy) | `Plan: 0 to add, 0 to change, 11 to destroy.` |
| apply | `Apply complete! Resources: 0 added, 0 changed, 11 destroyed.` (via `.tools/safe-apply.sh`, Rule 18) |
| post-apply instance state | `terminated` (live `describe-instances`) |
| post-apply rule existence | `ResourceNotFoundException ... does not exist on EventBus default` |
| post-apply IAM | all three roles absent; **positive control:** the same command shape returns `quartz-si2-spike-role` for a role that exists, so the three empty results are genuine absences, not a broken retrieval |
| **S3 `canonical/schwab/` POST** | **484 objects -- UNCHANGED. Data preserved as required.** |
| EC2_MANIFEST.json | `canonical-schwab-runner` entry removed; 28 -> 27 services; JSON re-validated; CRLF preserved (1 insertion / 24 deletions) |
| rollback | **NONE for the instance (terminate is unrecoverable).** Rule + IAM are re-creatable from `runner-trigger.tf` / `runner-iam.tf` at the parent commit. |

### The si2 ingest -- verified UNBROKEN after the destroy

| check | result |
|---|---|
| `i-0f3d57a97f14727af` | **running** |
| `canonical-schwab-si2-08242234-daily-pull` | **ENABLED** |
| `canonical-schwab-si2-08335338-daily-pull` | **ENABLED** |
| `quartz-si2-spike-role` | present |

## A NEAR-MISS WORTH RECORDING -- `apply -target` WITHOUT `-destroy` REPORTS SUCCESS AND DOES NOTHING

The first apply was issued as `apply -target=... ` (no `-destroy`). It returned
**`Apply complete! Resources: 0 added, 0 changed, 0 destroyed.`** and **rc=0**.

That is not a failure and not a no-op-by-accident: `apply -target` reconciles toward the CONFIG,
which still declares all 11 resources, so doing nothing was CORRECT behaviour. **A `plan -destroy`
does not carry its intent into the subsequent `apply` -- `-destroy` is a property of the apply, not
of the reviewed plan.**

**The failure mode this would have produced:** an operator who reads `Apply complete!` + rc=0 as
"the destroy landed", closes the ledger, and reports a decommission that never happened -- leaving a
live instance and an ENABLED rule behind a record that says both are gone. **The verdict string
contains the word "complete" and the count that disproves it in the same line.** Caught by reading
`0 destroyed` against the expected `11 destroyed`, which is exactly the
CLAUDE.md "never trust rc=0 -- verify against the served/live artifact" rule doing its job.

## THE SECOND NEAR-MISS, AND IT IS THE SERIOUS ONE -- A TARGETED DESTROY ARMS A RESURRECTION

After the 11 resources were destroyed and verified absent, the `.tf` files still **declared** all of
them. Measured, not assumed -- plain `terraform plan` immediately after the destroy:

```
Plan: 11 to add, 0 to change, 0 to destroy.
  # aws_instance.canonical_runner will be created
  # aws_cloudwatch_event_rule.xref_success will be created
  ...
```

**The next `terraform apply` by ANY agent in this workspace -- for any unrelated si2 change -- would
have recreated the terminated instance and re-enabled the dead rule.** That state is strictly worse
than never having decommissioned: the box is gone from the manifest and from everyone's mental model,
and the mechanism that brings it back is the routine action the workspace exists for.

**`terraform destroy` removes INFRASTRUCTURE; only deleting the DECLARATION removes the INTENT.** A
targeted destroy that is not paired with removing the config is a decommission with a timer on it.

**Closed:** `runner.tf`, `runner-iam.tf`, `runner-trigger.tf` deleted (all runner declarations,
their `locals`, and their three outputs were self-contained in those files -- verified no
cross-file references before deleting). Post-deletion plan showed **no infrastructure changes**, only
three stale state outputs, cleared by a final apply. **Final state: `No changes. Your infrastructure
matches the configuration.`**

## CONVENTION GAP SURFACED (not invented around)

`EC2_MANIFEST.json` has **no retirement/decommission convention** -- 0 occurrences of
`retired`/`RETIRED`/`terminated`, and the schema is a flat `services` map of LIVE services. So a
terminated box has two possible homes and neither is defined: leave it (a manifest asserting a
service that does not exist = false-green) or delete it (loses the retirement record).

**I removed the entry** -- a terminated instance is not a service, and Rule 8's purpose is a true
register of live EC2 that CI/CD depends on. **The durable retirement record is THIS ledger plus the
commit**, cited by path in the commit message.

**I deliberately did NOT invent a `_retired` block.** Adding a disposition axis to a shared schema is
a Rule-24 taxonomy act (MECE / same-grain / intent-coherence / state-coherence), not a
convenience edit, and it belongs to whoever owns that schema. **Routed to CTO as an open item.**

## Closure

**Status: CLOSED 2026-08-05T22:32Z.** All 11 resources destroyed and verified absent on live
primitives; S3 data verified preserved at 484 objects; the si2 49F ingest verified running with both
daily rules ENABLED; `EC2_MANIFEST.json` updated in the same commit. No stranded leg.
