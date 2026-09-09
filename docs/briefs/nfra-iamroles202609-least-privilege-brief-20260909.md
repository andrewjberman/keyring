# BRIEF — `NFRA_IAMROLES202609`: least privilege across all IAM roles, and how we would know

**Step 1 of the canonical loop (L1).** Author `4.0.0_SA_CRO~Z`. Mode: **NEW** (greenfield — no
over-grant assessment has ever been run).
**Project code / directive (Andrew-direct):** `NFRA_IAMROLES202609` · `D12`
**Commissioning:** Andrew, 2026-09-09, VERBATIM as recorded by `1.0.0_SA_CTO~Z`: *"Is there anything
there for assessing all IAM roles and making sure we are properly adhering to least privilege?"* —
asked of `NFRA_OPSEC202609`, measured, answer **no**.
**Commissioning handoff, read in full before this brief was written:**
`org/tier1_exec/1.0.0_SA_CTO/deliverables/HANDOFF_NFRA_IAMROLES202609_BRIEF_CREATE_20260909.md`
`@5d9497db65`.

**Consumer:** `/endpoint --forward` at L2. Every outcome is separately headed so a `SOURCE:` line
resolves.

⛔ **THE ONE-LINE FRAME.** The estate has never asked whether a role holds permissions it does not
use. Its IAM tooling asks the **opposite** question — *does this role have enough?* — and answers it
well. **This project is the missing direction, plus a second axis nobody has measured at all.**

---

# PART I — THE OUTCOME TERRITORY

## O1 — Someone can state the estate's least-privilege posture with a printed denominator and a vintage

A reviewer says "N of M roles assessed, as of DATE" rather than an opinion. Coverage and freshness
are part of the answer, not context around it.

**Why it is not possible today:** no assessment of any coverage exists (F4), and the population
count available is a 158.5h-stale detector read (F2).

## O2 — For any role, a reviewer can see which granted permissions it has never used

The over-grant question, per role, with evidence and a lookback window. This is the deliverable the
question in the title actually demands.

## O3 — For any policy, a reviewer can see what CONDITIONS it requires — not only what it scopes

A policy that is perfectly resource-scoped and still admits a password-only session from anywhere is
**visible as such**. "Correctly scoped" stops being able to hide "no MFA required."

**This is the axis the estate has never measured** (F8), and an assessment built on resource-scoping
alone would grade this estate healthy while missing it entirely.

## O4 — Every live role is findable in code, or is visibly and deliberately exempt

No role is governable-but-invisible. A role outside Terraform is either brought in or carries a
recorded, owned exemption — and either way it stops being absent from every check the estate runs.

## O5 — An engineer can narrow a grant and know beforehand what it would break

Before a permission is removed, its effect is established against the APPLIED plane rather than
guessed from a policy document.

⛔ **This outcome exists because of a named failure mode, not as a nicety.**
`CONTROLS_OVER_CARE.md:512` already names it: *"a future engineer doing least-privilege cleanup
deleting a needed grant."* An `AccessDenied` caused by this project's own remediation is the
specific thing it must be designed not to cause.

## O6 — Anyone can tell whether a past least-privilege remediation actually landed

For each historical remediation plan, a reader learns whether it executed — rather than inferring
from where the file sits in a directory.

**Today three such plans exist with unknown status** (F10), and a document's location is being asked
to carry a completion claim it cannot carry.

## O7 — A reviewer can tell "this grant is unused" apart from "we cannot see whether it is used"

Absence of usage evidence and evidence of absence are distinguishable at a glance. A role the
instrument cannot see does not read as clean.

**This is the estate's ratified two-axis discipline** (instrument state vs world state) applied to
the identity plane; it is not a new invention for this project.

## O8 — The assessment can be re-run without redoing it by hand

Someone can ask the same question next quarter and get a comparable answer. The existing closest
tool is explicitly **`NOT SCHEDULABLE`** (F4), so today the answer would be re-derived manually
every time, which is how an assessment silently stops happening.

---

# PART II — WHERE THE BOUNDARY SITS

## Owns

- **The over-grant question** across the IAM estate — the instrument, the census, and its coverage.
- **The condition axis** — what a policy requires, not only what it scopes.
- **Declared-vs-live role reconciliation**, and the governance disposition of undeclared roles.
- **Completion evidence for historical least-privilege remediations.**

## Relies on, does not own

| Surface | Owner |
|---|---|
| Request-path front doors, WAF, the sentinel, the auto-block framework | **`NFRA_OPSEC202609`** (D12) |
| Portal MFA enforcement (`mfaChannel` / `mfaEnabled`) | **`D12_PLATFORM_OPS`** |
| `comp-iam`'s existing DESIRED-plane surfaces and its `simulate` mode | the comp-tool build lane |
| The website IAM identity and its Terraform | **`NFRA_WEBSITE`** |
| Whatever repairs `comp-find --corpus aws` | unowned today — see D1 |

## Explicitly NOT re-opened

- **`NFRA_OPSEC202609`'s nineteen outcomes.** Consumed, never amended. Its four narrow
  least-privilege cells stand as done.
- **The standing moratorium on new alerts/alarms/monitors.** This project **assesses and
  remediates**; it does not mint alerting.
- **Retiring or narrowing anything that serves live production without the estate's normal
  sign-off.** Narrowing a grant is a change with a blast radius.

## A boundary that is genuinely two remedies, stated so the decomp does not fuse them

The 16 undeclared roles are **a governance question** (*should this be in code at all?*) **and** a
permissions question (*is it over-granted?*). **They do not move together** and a single cell that
tries to do both will do one of them badly.

---

# PART III — THE QUALITATIVE BAR

*Disputable, and deliberately without invented numbers.*

1. **A reviewer can answer the title question in a sentence, with evidence attached.** Today the
   honest answer is "nobody has measured it," and the bar is that this stops being true.
2. **No role is assessed as clean because nothing looked at it.** The same standard the estate
   ratified for infrastructure reporting, applied to identity.
3. **A policy that requires nothing of the caller is legible as such**, even when its resource
   scoping is exemplary. The contestable claim is that this axis matters at all — and
   `website-estate-admin` is the exhibit either way.
4. **This project does not cause an outage.** An `AccessDenied` traceable to its own remediation is
   a failure of the project, not an incident of the estate.
5. **The answer survives its author.** Someone who was not present can re-run it and get a
   comparable result.
6. **A grant that cannot be assessed is reported, not skipped.** The estate learns what it cannot
   see about its own identity plane.

---

# PART IV — THE SUBSTRATE: findings, with what was measured

## F1 — `NFRA_OPSEC202609` genuinely does not cover this

**Measured by `1.0.0_SA_CTO~Z` at PRD v0.14:** all nineteen outcomes are **request-path front
doors**. IAM appears only instrumentally, on things that project builds: `TO-OP-S-22` (sentinel chain
only), `C-1` (identity tables only), `C-2` (231 principals but **one action** on **4 IP sets**),
`TO-OP-S-9C` (one residual grant), `C-13`/`C-14` (the project CMK, 3 roles).
**Least privilege is done there four times, narrowly, on things it owns. Nothing sweeps the estate.**

## F2 — The population, and the limit on the number

**Measured (`comp-iam live`, by `1.0.0_SA_CTO~Z`):** **208 live roles · 192 Terraform-declared · 16
governable and completely undeclared**, all sixteen named in the handoff — including
`portal-auth-lambda-role`, `portfolio-management-lambda-role`, `lambda-test-role`.
⚠ **VINTAGE, and it bounds the claim:** materialized graph at **2026-09-03T02:00:31Z, 158.5h old**,
flagged STALE against its own 24h cadence, incremental pipe UNVERIFIED, population cross-check
UNAVAILABLE. **The tool calls itself a DETECTOR, not an oracle**, and evaluates no
Deny/boundary/condition/SCP. **16 is a strong signal to confirm, never a settled count.**

## F3 — The 16 matter more than their number: they are invisible to the estate's own analysis

`comp-iam` parses **Terraform**. A role with no Terraform declaration is therefore outside **every
DESIRED-plane check that runs here** — it is not assessed and not flagged as unassessed.

## F4 — The tooling is pointed the other way, and that is the central problem

**Measured:** `comp-iam` exposes fourteen surfaces — `gaps, roles, services, service, role, stats,
reconcile, attach-census, resource-sweep, gaps-filtered, simulate, refresh-census, live,
investigate-candidates`.
`comp-iam gaps` answers the **UNDER-grant** question (*does this role have what its code needs*) and
is finding **12 missing permissions** right now. **Least privilege is the OVER-grant question and no
surface answers it.** The closest, `investigate-candidates`, is explicitly labelled **TRIAGE ONLY,
`RoleLastUsed`-based, never "unused", NOT SCHEDULABLE.**

## F5 — ⭐ THE OVER-GRANT INSTRUMENT WAS DESIGNED AND PROTOTYPED SEVEN WEEKS AGO, AND NEVER BUILT

**Measured by this author, 2026-09-09.** `comp-find` over the Access-Advisor family
(`GetServiceLastAccessedDetails|ServiceLastAccessed|access-advisor|AccessAdvisor|
generate-service-last-accessed`, case-insensitive) returns **3 hits across 52,607 files — ALL in the
`[DOC]` band. ZERO in `SURFACED`, `DEF` or `CONFIG`.** The concept exists only in prose.

The prose is a **design with a validated prototype**:
`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/COMP_IAM_USAGE_DESIGN_20260717.md` — *"comp-iam-usage
— design (decommission research, thread 2/3)"*, **Status: "RESEARCH / DESIGN + validated
prototype"**, on **Andrew's own steer 2026-07-17: "go ahead with comp-iam expansion"**. It names its
build target (`org/modules/graph/`, ANY_EXEC → build lane/CTO), its signal table, and a Rule-22a
mandate to **fix-or-explicitly-carry** comp-iam's three limits rather than silently inherit them.

⛔ **THIS CHANGES THE PROJECT'S SHAPE.** The handoff calls the over-grant census *"the hardest
instrument problem."* It may instead be **build-ladder rung 2 — the estate already has it, on
paper.** The first act is to establish what that prototype does and does not do, not to design an
instrument from scratch.

## F6 — The core signal is live, and it carries a retrieval trap

**Measured in that design, 2026-07-17:** `RoleLastUsed` is **live and populated** —
`inf-accounts-v2-daily-role` → LastUsed 2026-07-17T13:22Z, Created 2026-05-07.
⛔ **The trap, stated in the design and worth carrying verbatim into any build:** **`ListRoles` does
NOT populate `RoleLastUsed`; `GetRole` does.** A census built on `ListRoles` returns a field-shaped
absence for every role and reads as "nothing has been used."

## F7 — ⭐ AWS's native unused-access finder is STILL not enabled — measured TODAY

**Measured by this author, live, 2026-09-09:** `aws accessanalyzer list-analyzers` → **`{"analyzers":
[]}`**.
The 2026-07-17 design measured the identical empty result and recommended enabling one, calling it
*"a recommendation, not a dependency."* **Fifty-four days later it is still absent.**
**Build-ladder rung 4 — a native platform feature — for the exact question this project exists to
answer, and it is unenabled.**

## F8 — ⭐ LEAST PRIVILEGE HAS TWO AXES, AND THE ESTATE MEASURES ONE

**The worked exemplar, measured 2026-09-09 across both this author and `1.0.0_SA_CTO~Z`:**
`website-estate-admin` — 9 live statements, 9 sids in `infra/aws/terraform/website/iam_patricia.tf`,
**DESIRED and APPLIED agree, no drift.**

**On the RESOURCE axis it is genuinely exemplary:** EC2/SSM tag-scoped to `Project=NFRA_WEBSITE`,
exactly one bucket ARN, one log group, sessions scoped to `${aws:username}`'s own; header declares
*"ZERO data-estate reach, ZERO other bucket, ZERO Secrets Manager, ZERO IAM-modify, ZERO
instance-terminate."*

⛔ **On the CONDITION axis it is silent.** `MultiFactorAuthPresent` occurs **ZERO** times in that
Terraform — the only near-hits are the substring `implicitDeny` inside comments — and **all 9 live
statements are `Allow`, with no `Deny` anywhere.** The policy **grants self-service MFA enrolment
and never requires MFA.** Enrollable, not enforced.

⭐ **THE GENERALISABLE CLAIM, AND IT IS WHAT THIS PROJECT IS ACTUALLY ABOUT: least privilege has at
least two axes — WHAT a principal may touch, and UNDER WHAT CONDITIONS. This estate is strong on the
first and largely silent on the second. A brief framing least privilege as resource-scoping alone
would grade this estate healthy and miss the entire second axis.**

## F9 — The instance is discharged; the CLASS re-arms on onboarding

The `website-estate-admin` console credential was removed 2026-09-09 16:38Z on Andrew's word
(*"Rec approved, remediate now"*), verified `NoSuchEntity` against a positive control. Record:
`org/critical_paths/change_management/20260909T1638Z_patricia-console-login-profile-removed_deploy_completion.md`.
⛔ **But `iam_patricia.tf:172-174` documents the command to re-provision it at onboarding, and the
MFA condition still is not there.** The gap **re-arms** the moment TWLC is onboarded.
**Discharging one hazard armed another** — which is precisely why the CLASS, not the instance,
is this project's subject.

## F10 — Three prior remediations with UNKNOWN status

- `infra/security/remediation/active/iam-least-privilege-rollback-plan.md` — *"Replace 40
  overly-permissive IAM policies with least-privilege custom policies."* **Last touched 2026-02-17**,
  in a directory reorganisation. Still in `active/`, never moved to `completed/`, **no completion
  record.**
- `infra/security/remediation/active/SOC2-FULL-REMEDIATION-MASTER-PLAN.md` — same directory, same
  unknown status.
- `org/projects/task_orders/PORTAL_AUTHHARD.WS6.least-priv-role-split-secret-dewildcard.md` —
  least-privilege role splitting and secret de-wildcarding. ⛔ **Carries NO `<status>` tag at all**,
  and sits inside a project `NFRA_OPSEC202609`'s PRD marks *"not re-opened"*.
⚠ **A stale document is NOT evidence the work did not land.** Establishing which is a first-order
task for this project and an assumption for nobody. **Unfinished least-privilege work inside a
closed project is exactly the shape that never gets picked up.**

## F11 — The APPLIED-plane instrument already exists

`comp-iam simulate` (`get_role` + `simulate_principal_policy`) is the one live-AWS mode and is the
`(action, resource)` check the estate's own Rule-22a discipline leans on. **A least-privilege battery
should be built ON it, never beside it** — and it is the natural substrate for O5's pre-flight.

---

# PART V — WHAT MUST BE TRUE, NOT SEQUENCED

*Named, not ordered. Sequencing is L5.*

**D1 — The live plane cannot currently be enumerated.** `comp-find --corpus aws` returns
`BLOCKED: comp-kuzu rc=2 / unparseable JSON on unit EC2_INSTANCE — NO MEASUREMENT, not a zero`
(`kuzu_cli.py: unrecognized arguments: --mode`). **A blocked measurement is not a zero.**
Declared-vs-live IAM reconciliation (O4) cannot be automated until it is repaired, and **it is
unowned**. ⚠ **It is the SAME dependency the Global Infrastructure Reporting brief carries as its
D4** — one instrument, two projects. Whichever cuts it first should own it. *(An L5 observation for
`2.0.0_SA_COO~Z`, not a ruling made here.)*

**D2 — The `comp-iam-usage` prototype's real state must be established before anything is built.**
F5 says a validated prototype existed on 2026-07-17. Whether it still runs, what it covers, and
where it lives are unknown — and the difference between "extend a prototype" and "build an
instrument" is the difference between two very different projects.

**D3 — `DESIRED ≠ APPLIED ≠ EXERCISED`, and every scope claim so far is DESIRED.** Every statement
in this brief about what a policy permits is read from a **document**. No
`simulate-principal-policy` battery has been run. `comp-iam` states this limit about itself.

**D4 — Enabling IAM Access Analyzer is available and unenabled** (F7). The 2026-07-17 design called
it *a recommendation, not a dependency* — that framing should be re-examined rather than inherited,
because it is the only native instrument for the project's central question.

**D5 — The remediation must be designed not to cause an `AccessDenied`.** `CONTROLS_OVER_CARE.md:512`
names the failure mode. This constrains **how** grants are narrowed, which is a design input and not
a sequencing note.

**D6 — The 16 undeclared roles need two dispositions, not one** (Part II). Governance and
permissions do not move together.

**D7 — `NFRA_OPSEC202609`'s four narrow least-privilege cells are inputs.** They are done, they are
correct, and they are not to be re-run. What they are not is coverage.

---

# PART VI — STATUS TODAY — ⛔ NOT OUTCOME-BEARING

*Ages here move. Do not cut outcomes from this part.*

- **208 live IAM roles**; 192 Terraform-declared, 16 undeclared — **graph vintage 2026-09-03T02:00:31Z,
  158.5h stale, detector-not-oracle** (`comp-iam live`, read by `1.0.0_SA_CTO~Z`).
- **7 IAM users** in the account (`aws iam list-users`, this author, 2026-09-09; `IsTruncated` absent,
  so the list is complete).
- **IAM Access Analyzer: `analyzers: []`** — live, 2026-09-09, this author.
- **`comp-iam gaps` is currently finding 12 missing permissions** (UNDER-grant direction).
- **No over-grant census has ever been run.** Coverage of the least-privilege question: **zero of
  208.**
- **`comp-iam-usage`**: design + validated prototype dated 2026-07-17; **no code in the corpus.**
- `website-estate-admin`'s console credential removed 2026-09-09 16:38Z; the MFA-condition gap
  persists in Terraform and re-arms at onboarding.

---

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. **The live IAM fleet was never enumerated by this author.** The 208/192/16 split is relayed from
   `1.0.0_SA_CTO~Z`'s `comp-iam live` read at a **158.5h-stale** vintage, and that seat labelled it a
   signal to confirm. This brief does not upgrade it.
2. **No `simulate-principal-policy` battery was run.** Every scope statement — including the
   `website-estate-admin` exemplar — is read from a DOCUMENT and never EXERCISED.
3. **Whether the 2026-02-17 forty-policy remediation executed is unknown.** Nothing was read either
   way, and its directory location is not evidence.
4. **The `comp-iam-usage` prototype was not run or located.** F5 establishes that a design and a
   claimed validated prototype exist; it does not establish that any code does.
5. **The `MultiFactorAuthPresent` finding is scoped to ONE policy.** No estate-wide condition census
   was run, so "the estate is largely silent on the condition axis" is an **inference from one
   exemplar plus the absence of any condition-aware surface in comp-iam's fourteen modes** — not a
   measured population claim. **This is the brief's most load-bearing unmeasured statement.**
6. **`website-estate-admin`'s 9 statements were read, not exercised.** The Terraform header cites a
   live simulate battery at clearance time 2026-07-08 which was not re-run.
7. **No claim is made about Deny policies, permission boundaries, SCPs or session policies anywhere
   in the estate.** `comp-iam` evaluates none of them and neither does this brief; a grant that looks
   over-broad may be bounded by something no instrument here reads.
8. **The 16 undeclared roles were not individually inspected.** They are named; their permissions are
   unassessed.

---

# REFS TO CARRY

```
  BRIEF PATH        docs/briefs/nfra-iamroles202609-least-privilege-brief-20260909.md
  PROJECT           NFRA_IAMROLES202609  (Andrew-direct)   DIRECTIVE  D12
  EXISTING PRD      NONE
  COMMISSIONING     org/tier1_exec/1.0.0_SA_CTO/deliverables/
                    HANDOFF_NFRA_IAMROLES202609_BRIEF_CREATE_20260909.md @5d9497db65
  SIBLING PROJECTS  NFRA_OPSEC202609 (D12)   -- front doors; four narrow LP cells; NOT re-opened
                    D12_PLATFORM_OPS         -- portal MFA
                    NFRA_WEBSITE             -- the website IAM identity + iam_patricia.tf
                    Global Infrastructure Reporting (docs/briefs/global-infrastructure-reporting-
                      brief-20260909.md) -- SHARES dependency D1
  PRIOR ART         COMP_IAM_USAGE_DESIGN_20260717.md      -- design + validated prototype, UNBUILT
                    DECOMMISSION_TOOLING_ASSESSMENT_20260717.md
                    comp-iam simulate                      -- the APPLIED-plane instrument, exists
                    iam-least-privilege-rollback-plan.md   -- 40 policies, status UNKNOWN
                    SOC2-FULL-REMEDIATION-MASTER-PLAN.md   -- status UNKNOWN
                    PORTAL_AUTHHARD.WS6.least-priv-role-split-secret-dewildcard -- no status tag
                    CONTROLS_OVER_CARE.md:512              -- the named failure mode
  MEASURED AT       role population 2026-09-03T02:00:31Z (relayed, 158.5h stale at read);
                    IAM users + Access Analyzer + Access-Advisor census 2026-09-09 by this author;
                    website-estate-admin 2026-09-09; repo reads at HEAD 37ff80867a
```

**Next:** `1.0.0_SA_CTO~Z` runs `/endpoint --forward` on this at L2, then L3 registration under
`D12` and the L4 PRD.
