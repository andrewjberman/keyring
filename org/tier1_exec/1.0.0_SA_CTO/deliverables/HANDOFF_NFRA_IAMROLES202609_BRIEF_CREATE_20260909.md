# HANDOFF -- `NFRA_IAMROLES202609` -> `4.0.0_SA_CRO~Z` for `/brief-create`

**From:** `1.0.0_SA_CTO~Z` · **For relay by:** Andrew · **Date:** 2026-09-09 ~16:5xZ
**Project code (Andrew-direct):** `NFRA_IAMROLES202609` · **Directive (Andrew-direct):** `D12`
**archetype:** SCRIBE

⛔ **THIS IS A COMMISSIONING HANDOFF, NOT A BRIEF AND NOT AN ENDPOINT.** It exists so `4.0.0_SA_CRO~Z`
does not re-derive measurements this seat already took, and so it knows what was NOT measured. The
L1 brief is that seat's to write; the L2 endpoint is this seat's and comes after.

---

## THE SUBJECT, in Andrew's frame

*"Is there anything there for assessing all IAM roles and making sure we are properly adhering to
least privilege?"* -- asked of `NFRA_OPSEC202609`, measured, and the answer was **no**. This project
is the answer to the question that exposed.

## WHY IT IS NOT `NFRA_OPSEC202609`'s

Measured at PRD v0.14: all nineteen of that project's outcomes are about **request-path front doors**
-- who can reach an endpoint, what is logged, what is blocked. IAM appears only INSTRUMENTALLY, for
resources that project itself builds:

| Existing coverage | Its actual scope |
|---|---|
| `TO-OP-S-22` (complete) | its own deliverable says *"least privilege is this cell's entire subject"* -- **for the sentinel chain only** |
| `C-1` | least privilege on **the identity tables** |
| `C-2` | swept 231 principals, but only for **one action** (`wafv2:UpdateIPSet`) on **4 IP sets** |
| `TO-OP-S-9C` | one residual grant cleanup on `opal-users` |
| `C-13`/`C-14` | the project CMK's key policy, scoped to 3 roles |

So least privilege is done there **four times, narrowly, on things that project owns.** Nothing
sweeps the estate. Adding a 208-role sweep to it would have made it instantly the largest thing in a
project whose nineteen outcomes are coherent without it.

---

## WHAT THIS SEAT MEASURED, so it is not re-derived

**1. THE POPULATION.** `comp-iam live`: **208 live roles. 192 declared in Terraform. 16 governable
and completely undeclared** --
`bd-merge-daily-lambda-role`, `bd-pipeline-task-role`, `codebuild-semantic-clustering-role`,
`ecsTaskExecutionRole`, `finbert-ec2-backfill-role`, `lambda-ec2-runtime-monitor-role`,
`lambda-test-role`, `opal-data-refresh-lambda-role`, `opal-smartx-lambda-role`,
`portal-auth-lambda-role`, `portfolio-management-lambda-role`, `rds-monitoring-role`,
`seeking-alpha-scraper-role`, `sentiment_query_api-role`, `vpc-flow-logs-role`,
`workspace-sync-lambda-role`.

⚠ **VINTAGE, AND IT LIMITS THE NUMBER:** that is the materialized graph at **2026-09-03T02:00:31Z --
158.5h old**, flagged STALE against its own 24h cadence, incremental pipe UNVERIFIED, population
cross-check UNAVAILABLE. The tool calls itself **a DETECTOR, not an oracle** and evaluates no
Deny/boundary/condition/SCP. **Treat 16 as a strong signal to confirm, never a settled count.**

⛔ **WHY THE 16 MATTER MORE THAN THEIR NUMBER: they are invisible to the estate's own analysis.**
`comp-iam` parses Terraform, so a role with no Terraform declaration is outside every DESIRED-plane
check that runs here. `portal-auth-lambda-role` is among them.

**2. THE TOOLING IS POINTED THE OTHER WAY -- and this is the brief's central problem.**
`comp-iam gaps` answers the **UNDER-grant** question: *does this role have what its code needs?* It
is finding **12 missing permissions** right now. **Least privilege is the OVER-grant question, and no
comp-iam surface answers it.** The fourteen surfaces are `gaps, roles, services, service, role,
stats, reconcile, attach-census, resource-sweep, gaps-filtered, simulate, refresh-census, live,
investigate-candidates`. The closest is `investigate-candidates`, and it is explicitly labelled
**TRIAGE ONLY, RoleLastUsed-based, never "unused", NOT SCHEDULABLE as a routine sweep.**

**3. PRIOR ART THAT MUST NOT BE RE-BOUGHT (build-ladder rung 2).**
- `infra/security/remediation/active/iam-least-privilege-rollback-plan.md` -- *"Replace 40 overly-
  permissive IAM policies with least-privilege custom policies."* **Last touched 2026-02-17**, by
  Andrew, in a directory reorganisation. Still in `active/`, never moved to `completed/`, and it
  carries **no completion record**. ⚠ **A stale document is NOT evidence the work did not land** --
  establishing which is a first-order task for this project, not an assumption for this handoff.
- `infra/security/remediation/active/SOC2-FULL-REMEDIATION-MASTER-PLAN.md` -- same directory, same
  unknown status.
- `org/projects/task_orders/PORTAL_AUTHHARD.WS6.least-priv-role-split-secret-dewildcard.md` --
  least-privilege Lambda role splitting and secret de-wildcarding. ⛔ **It carries NO `<status>` tag
  at all, and it sits in a project `NFRA_OPSEC202609`'s PRD explicitly marks "not re-opened"**
  (closed 2026-08-25 on membership). Unfinished least-privilege work inside a closed project is
  exactly the shape that never gets picked up.
- `comp-iam`'s own `simulate` surface is the APPLIED-plane instrument and already exists; a
  least-privilege battery should be built ON it, not beside it.

**4. A WORKED EXEMPLAR, measured today, and it reframes the whole question.**
`website-estate-admin` (the external TWLC contractor's policy) is **9 statements**, and the Terraform
at `infra/aws/terraform/website/iam_patricia.tf` declares **9 sids** -- **DESIRED and APPLIED agree,
no drift.** On the RESOURCE axis it is genuinely exemplary: EC2/SSM tag-scoped to
`Project=NFRA_WEBSITE`, exactly one bucket ARN, one log group, and session control scoped to
`${aws:username}`'s own sessions.

⛔ **AND IT IS SILENT ON THE CONDITION AXIS. `MultiFactorAuthPresent` occurs ZERO times in that
Terraform** -- the only two hits are the substring `implicitDeny` inside comments -- and all 9 live
statements are `Allow` with no Deny anywhere. So the policy **grants self-service MFA enrolment and
never requires MFA.** Enrollable, not enforced.

⭐ **THE GENERALISABLE AXIS, AND IT IS THE THING THIS PROJECT IS ACTUALLY ABOUT:**
**least privilege has at least two axes -- WHAT a principal may touch, and UNDER WHAT CONDITIONS.**
This estate's IAM work is strong on the first and largely silent on the second. A policy can be
perfectly resource-scoped and still admit a password-only session from anywhere. **A brief that
frames least privilege as resource-scoping alone will grade this estate as healthy and miss the
entire second axis.**

⚠ **THE INSTANCE IS DISCHARGED AND THE CLASS IS NOT.** Andrew ruled *"Rec approved, remediate now"*
at ~16:3xZ and `4.0.0_SA_CRO~Z` deleted that console login profile (verified with a positive
control), so there is no live exposure today. **But `iam_patricia.tf:172-174` documents the command
to re-provision it when TWLC is onboarded, and the MFA condition still is not there.** The gap
re-arms on onboarding. Discharging one hazard armed another.

---

## BOUNDARY -- what this project should NOT take

- **`NFRA_OPSEC202609`'s nineteen outcomes.** Consumed, never amended. Its four narrow least-privilege
  cells stand as done.
- **The standing moratorium on new alerts/alarms/monitors.** This project ASSESSES and REMEDIATES; it
  does not mint alerting.
- **Retiring or narrowing a grant that serves live production is a change with a blast radius.**
  `CONTROLS_OVER_CARE.md:512` already names the failure mode in terms: *"a future engineer doing
  least-privilege cleanup deleting a needed grant"*. An `AccessDenied` produced by this project's own
  remediation is the thing it must be designed not to cause.
- **Terraform-managed discipline.** The 16 undeclared roles are a GOVERNANCE question (should they be
  in code at all?) as much as a permissions one, and those are two different remedies.

---

## WHAT IS EXPLICITLY NOT KNOWN -- name these as unknowns, do not resolve them here

1. **Whether the 2026-02-17 forty-policy remediation ever executed.** Nothing read either way.
2. **The live fleet was never enumerated.** `comp-find --corpus aws` is **BLOCKED** (`comp-kuzu rc=2`,
   `kuzu_cli.py: unrecognized arguments: --mode`) -- carried in the Global Infra brief as D4. **A
   blocked measurement is not a zero.** Declared-vs-live IAM reconciliation cannot be automated until
   that is repaired, and it needs an owner.
3. **No `simulate-principal-policy` battery was run by this seat.** Every scope statement above is
   read from a DOCUMENT, never exercised. `comp-iam` says it plainly: DESIRED != APPLIED != EXERCISED.
4. **No over-grant census exists at all.** Nobody has measured which roles hold permissions they have
   never used. That is the project's likely first deliverable and its hardest instrument problem.

---

## ONE SEQUENCING NOTE, offered and not imposed

`NFRA_IAMROLES202609` and the Global Infrastructure Reporting project share a substrate: both need to
know what exists in the account and both are blocked on the same broken instrument (item 2 above).
**Repairing `comp-find --corpus aws` serves both**, and whichever project cuts it first should be the
one that owns it. That is an L5 sequencing observation for `2.0.0_SA_COO~Z`, not a ruling.
