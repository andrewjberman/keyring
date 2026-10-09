# NFRA_IAMROLES202609.TO-IAM-u-3 -- EXERCISE the condition axis: the round-1 exhibit, read live and simulated

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R4.md</decomp_doc>
<owned_cells>IAM-u-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~12</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (outcome FWD-3; the round-3 analysis calls this R4-C)

```
IAM-u-3. ACT: move FWD-3's exhibit from DESIRED (read from policy TEXT) to EXERCISED (read from the live
account and evaluated by AWS's own policy simulator), with a control that proves the scoping is real.

FWD-3, verbatim:
  "For any policy, a reviewer can see what it REQUIRES of the caller, not only what it lets them touch"
  DONE WHEN  EXERCISED -- at least one real policy has been surfaced as perfectly scoped and yet
             requiring nothing of whoever calls it
  ACCEPT     A rule that is careful about WHAT someone can touch but asks NOTHING about who they are
             or how they proved it is visible as such.
  BOUND      Part VII item 5: that the estate is broadly silent on this axis is an INFERENCE from ONE
             policy, never a measured population claim.

WHAT ROUND 1 DID (read: deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/CONDITION_AXIS.md and
condition-axis-reader.py). It surfaced the exhibit from Terraform source
infra/aws/terraform/estate-report/iam.tf, resource aws_iam_role_policy.runner_selfstop, and the reader's
verdict on it was REQUIRES-NOTHING. Its own BOUND section says every finding there is DESIRED and that only
a real `aws iam simulate-principal-policy` battery moves it past DESIRED. That battery was never run.

THE EXHIBIT, read live by the issuer at the cut (2026-10-09):
  role         estate-report-runner-role   (arn:aws:iam::313476888478:role/estate-report-runner-role)
  inline policy estate-report-runner-selfstop
  statement    Sid SelfStopThisInstanceOnly, Effect Allow, Action ec2:StopInstances,
               Resource arn:aws:ec2:us-east-1:313476888478:instance/i-0584e17d283fa7ef4, NO Condition
  simulate, no context: ec2:StopInstances on that ARN -> allowed (rc=0)

WHAT TO PRODUCE, in deliverables/0.9.0_WK_NFRA_IAMROLES202609~12/CONDITION_AXIS_EXERCISED.md:

  (a) THE LIVE READ. `aws iam get-role-policy --role-name estate-report-runner-role --policy-name
      estate-report-runner-selfstop`, its output quoted, and a statement of whether the live statement
      matches the Terraform source round 1 read (action, resource, absence of Condition).

  (b) THE READER, RE-RUN unchanged: `python <~2>/condition-axis-reader.py --policy
      infra/aws/terraform/estate-report/iam.tf`, its verdict line for runner_selfstop quoted.

  (c) THE SIMULATE BATTERY, every call read-only, its raw JSON output quoted in the document so
      `"EvalDecision": "<value>"` appears verbatim for each arm:
        ARM 1  no context entries, ec2:StopInstances on the pinned instance ARN   -> expected allowed
        ARM 2  same, with --context-entries for aws:MultiFactorAuthPresent=false (boolean) -> expected
               allowed: the policy asks nothing about a second factor
        ARM 3  optional, same with aws:SourceIp set to an arbitrary public address -> expected allowed
        CONTROL ec2:StopInstances on a DIFFERENT instance ARN in the same account  -> expected
               implicitDeny: proves the (action, resource) scoping is real, so "allowed" above is about
               the missing condition and not about a loose grant
      Use the live role as `--policy-source-arn`. If any arm returns something other than expected,
      report it as found -- the expectation is a hypothesis, not the answer.

  (d) THE VERDICT, one paragraph: this one real policy is EXERCISED as tightly scoped and requiring
      nothing of its caller, with (c) as evidence -- and the explicit statement that this is ONE policy
      and says nothing measured about any other.
```

## DEPENDENCIES

None.

## BOUNDS

```
AWS READS ONLY: get-role-policy, get-role, and simulate-principal-policy (an evaluation; it changes
  nothing). Do NOT stop, start or touch the instance; do NOT run ec2:StopInstances for real.
C-NO-ACCESSDENIED: no policy is edited, narrowed or given a Condition. Recommending one is out of scope.
PART VII ITEM 5: one policy, no population claim.
READ, NEVER WRITE: infra/aws/terraform/ and every other worker directory, including ~2's reader, are
  read-only to you. The reader is RUN, not edited.
C-ANALYZER-PRICED-FIRST + G-25: no Access Analyzer.
G-21: no alert, alarm, monitor, schedule or notification of any kind.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
reader pin        condition-axis-reader.py blob 62ff401ce8237a5a148e9873ce9e21e894bd256f at the base.
aws shim          use `.tools/aws`; prefix `MSYS_NO_PATHCONV=1` on calls that carry ARN arguments, or the
                  shell rewrites the leading slash-bearing pieces. The issuer's ARM-1 call, verbatim:
                  MSYS_NO_PATHCONV=1 .tools/aws iam simulate-principal-policy
                    --policy-source-arn arn:aws:iam::313476888478:role/estate-report-runner-role
                    --action-names ec2:StopInstances
                    --resource-arns arn:aws:ec2:us-east-1:313476888478:instance/i-0584e17d283fa7ef4
                  -> ec2:StopInstances allowed, rc=0. Use --output json for the document.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~12/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-u-3.exercise-the-condition-axis-exhibit-live.md
</paths>

Read surfaces (not granted for writing): `infra/aws/terraform/estate-report/iam.tf`, the `~2` reader and
report. Your surprise row id is `NFRA_IAMROLES202609-Z-W12-S<k>`, `"fabric": "site-z"`; `surfaced_at` =
`date -u +%FT%TZ` at filing.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-u-3"><invocation>grep -c '"EvalDecision": "allowed"' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~12/CONDITION_AXIS_EXERCISED.md</invocation><expect>a count of 2 or greater -- ARM 1 (no context) and ARM 2 (MFA absent) both quoted verbatim from the simulator as allowed; a "No such file" error means the deliverable is missing</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-u-3"><invocation>grep -c '"EvalDecision": "implicitDeny"' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~12/CONDITION_AXIS_EXERCISED.md</invocation><expect>a count of 1 or greater -- the CONTROL arm on a different instance quoted verbatim as implicitDeny, which is what makes "allowed" above a finding about the missing condition rather than about a loose grant</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-u-3"><invocation>git hash-object org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/condition-axis-reader.py</invocation><expect>exactly 62ff401ce8237a5a148e9873ce9e21e894bd256f -- the round-1 reader was run, not rewritten (a content pin, because a diff against HEAD reads clean once a change is committed)</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-u-3" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming
  3.0.0_SA_CVO~Z): does a reviewer now SEE, on live evidence, a policy that is careful about what can be
  touched and asks nothing of who touches it -- and does the document keep it to one policy?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>4</round>
<slot>~12</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 4) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-3 slug @36e167a2ea -> `ROUND_ANALYSIS.round3.md` @f8571787db section 7 (R4-C) -> L5 round-4 decomp -> this issuance.
**Chain:** an independent chain of one. **Risk LOCAL:** read and simulate only; the write surface is one deliverables directory.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule`, BUDGET REACHED at 220 s, 1 of 6 carriers, denominator C1=23 (7 gates armed), C2=32 PARTIAL (0 of 32 scanned); PARTIAL_OR_BLIND, not read as clean. G-21 binds as CLAUDE.md law.
comp-iam: RUN -- `bash .tools/comp-iam stats` from the main checkout: 214 TF roles / 196 services / 1154 operations / denominator 338 gaps; the exhibit role is one of them and the cell reads it live instead.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 2 of 2; the exhibit re-read live at the cut and the simulate path exercised once (allowed, rc=0).
</preflight>

**Preflight disposition:** Check dry-run at the base `54c2fd91b6`: AC1 base: FAIL as expected (file absent); AC2 base: FAIL as expected (file absent); AC3 base: PASS as expected (pin equals the base blob).
