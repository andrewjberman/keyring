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

⛔ **AND HALF OF IT IS ALREADY BUILT — DO NOT CUT THIS AS GREENFIELD.** `comp-iam-usage`'s
`self-test` asserts **`never-used != cold`** and the tool carries an explicit **`UNKNOWN` band**
(F5 corrected). **That is exactly this outcome, already implemented on the ROLE axis.** What is
missing is the same discipline at **permission** grain. An O7 cell written as new work would re-buy
passing, self-testing code.

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
⚠ **VINTAGE, and it bounded the claim as first written:** materialized graph at
**2026-09-03T02:00:31Z, 158.5h old**, flagged STALE, incremental pipe UNVERIFIED, population
cross-check UNAVAILABLE. **The tool calls itself a DETECTOR, not an oracle**, and evaluates no
Deny/boundary/condition/SCP.

### ⭐ F2a — CONFIRMED 2026-09-09 ~17:5xZ: **THE 16 IS A SETTLED COUNT AND A SETTLED SET**

The brief first said *"16 is a strong signal to confirm, never a settled count."* **It has now been
confirmed** — by a second instrument, on a different substrate, at a different vintage, once
`comp-find --corpus aws` was repaired (D1).

| | roles | DECLARED | LIVE-no-DECLARED |
|---|---|---|---|
| `comp-iam live` — materialized graph, **158.5h stale** | **208** | 192 | **16** |
| `comp-find --corpus aws IAM_ROLE` — served projection, **vintage 2026-09-09T14:59:48Z** | **216** | 200 | **16** |

⭐ **AND THE SETS ARE IDENTICAL, NOT MERELY THE SAME SIZE.** Measured by this author: the 16 names
from the fresh projection diffed against the 16 named in the commissioning handoff — **intersection
16 of 16, symmetric difference EMPTY.** `1.0.0_SA_CTO~Z` correctly warned that an agreeing
cardinality is not an agreeing set and that the comparison had not been run; it has now been run and
it holds.

**Two instruments, two substrates, two vintages, two different total populations — one identical
undeclared set.** That is corroboration in CLAUDE.md's strict sense, not repetition.

⚠ **AND THE 8-ROLE DELTA IN THE TOTALS IS UNEXPLAINED AND NOT CHASED.** 216 − 208 = 8, and the
DECLARED bucket moves by exactly the same 8 (200 − 192). Consistent with *eight Terraform-declared
roles appearing in the 158.5h between vintages*, and equally consistent with *the two instruments
scoping the population differently*. **Not measured.** It does not disturb the undeclared set, which
is what this project is about — but nobody should quote 208 and 216 as the same number.

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

## F5 — ⭐ CORRECTED 2026-09-09 17:1xZ. THE INSTRUMENT IS BUILT — BUT NOT AT THE GRAIN THE QUESTION NEEDS

> ⛔ **THIS FINDING PREVIOUSLY READ "DESIGNED AND PROTOTYPED SEVEN WEEKS AGO, AND NEVER BUILT." THAT
> WAS FALSE.** Falsified by `1.0.0_SA_CTO~Z` at L2 (msg 20532) before outcomes were cut, and
> re-measured independently by this author before amending. The wrong version is quoted here rather
> than deleted, because the reason it was wrong is itself a finding — see the tell at the end.

**`.tools/comp-iam-usage` EXISTS, IS TRACKED, AND RUNS.**
**Measured independently by this author, 2026-09-09**, using the instrument the first census should
have used:

- `comp-find --name 'comp-iam-usage*'` → **1 hit across 54,558 files** — `.tools/comp-iam-usage`
- `--help` **RUNS**, five subcommands: `role-cold`, `who-can-reach`, `reach-check`, `limits`,
  `self-test`
- **NEGATIVE CONTROL:** an unrecognised flag errors *differently* from `--help`
  (`error: unrecognized arguments: …`), so the parser is real and `--help` is not a static banner
- `self-test` **PASSES**: *"never-used!=cold, break-glass-guard-not-debris, UNKNOWN-band, hold-aware,
  22a limits NAMED (fix-or-carry) — all held"*
- Committed **57d9c8fd20**, `1.0.0_SA_CTO`, **2026-07-17** — the same day as its design — registered
  under `NFRA_DECOMTOOL`.

### ⭐ AND THE GRAIN IS THE POINT — this is what replaces the old claim rather than merely negating it

| Grain | State | What exists |
|---|---|---|
| **ROLE** coldness | **BUILT** | `role-cold` ranks roles by last-**assume** coldness. Answers *"is this ROLE cold"* — **never** *"which permissions inside it are unused"* |
| **APPLIED plane** | **BUILT** | `reach-check` gives an `(action, resource)` verdict via `simulate`; `who-can-reach` reads LIVE resource policies |
| **PERMISSION** grain | ⛔ **NOT BUILT** | *Which granted permissions has this principal never used* — the Access-Advisor question. **No code.** |

**So the brief's central claim survives in a SHARPER form:** the over-grant question **at permission
grain** is genuinely unanswered, while the role-coldness and APPLIED-plane halves are already built
and self-testing. **That is a materially different project from either *"the hardest instrument
problem"* (the handoff, which overstated it) or *"designed and never built"* (this brief's first
version). Both were wrong in the same direction.**

**F7 therefore matters MORE, not less:** `accessanalyzer list-analyzers` is `[]`, so the native
instrument for **exactly the unbuilt grain** is still unenabled.

**The three Rule-22a limits are FIXED, not inherited** — read from the tool's own `limits` output:
`(a)` `reach-check` simulates the EXACT `--resource-arns` (comp-iam models `(action)` only, so a
grant on ANY arn falsely reads GRANTED for EVERY arn); `(b)` ONE arn per call, because batching
poisons the control and the positive control is a separate invocation; `(c)` a conditioned statement
with no context is **UNKNOWN, never a false deny**; `(+)` an unreadable policy is **UNKNOWN, never
"no reach"** — an unparsed Deny is not silence.

### ⛔ THE TELL — why the first census returned a false absence, kept because it is reusable

The original search was keyed on the **ANSWER'S vocabulary** (`GetServiceLastAccessedDetails`,
`access-advisor`, …) and searched **CONTENT**. **The tool does not use those APIs**, so it was
invisible to that pattern. A `--name` census on the name **the design document itself gives** returns
it as the single hit.

**The denominator was honest the whole time — 3 of 3 in the `[DOC]` band was TRUE.** The pattern was
wrong, and a true count over a wrong pattern reads exactly like a settled absence. **Keyed on what
the tool would DO rather than what it is CALLED, and the tool's name was sitting in the title of the
document being read.**

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

**D1 — RESOLVED 2026-09-09 ~17:5xZ. `comp-find --corpus aws` is FIXED and exercised.** It was
BLOCKED (`kuzu_cli.py: unrecognized arguments: --mode`) — a caller/callee contract break introduced
when `d060cf9223` removed `--mode` from `kuzu_cli.py` and left its consumers passing it. Diagnosed by
this author to `.tools/comp-find:204`; **repaired by `1.0.0_SA_CTO~Z` at `9b99b49342`, which found a
SECOND broken caller this author missed — `org/modules/graph/comp_trigger.py:107`.**
⛔ **The reason it was missed is a reusable instrument lesson: this author ran
`git log -S'"--mode"' -- kuzu_cli.py`, which searches the CALLEE'S HISTORY and CANNOT ENUMERATE
CALLERS**, and then ran a caller census scoped to two hand-picked files. Right instrument for *"when
did this change"*, wrong one for *"who calls this."* **Declared-vs-live reconciliation (O4) is no
longer blocked.**

**D1a — THE RESIDUAL THE FIX DOES NOT CLEAR, and it is unowned.** `comp-find --corpus aws` now
prints **`VINTAGE: UNREAD (no provenance header on stderr)`**. Rows come back; **their age does
not.** `kuzu_cli` DOES emit the header — this author read it directly and dated the projection at
2026-09-09T14:59:48Z — **so the wrapper is dropping it.** ⛔ **A denominator with no vintage is the
shape this estate refuses**, and every `--corpus aws` census quoted anywhere until this is fixed
must carry an age read from `kuzu_cli` directly rather than from the census output. Needs an owner.

**D2 — CORRECTED. `comp-iam-usage` is BUILT and RUNNING; what must be established is its COVERAGE at
permission grain.** F5 (corrected) locates it at `.tools/comp-iam-usage`, tracked, executable,
self-test passing. The open question is no longer *"does it exist"* but *"`role-cold` answers the
ROLE axis — what answers the PERMISSION axis?"* **Extending a working, self-testing tool that already
names its Rule-22a limits is a different and much smaller act than building an instrument**, and any
cell written as greenfield here would re-buy working code.

**D3 — `DESIRED ≠ APPLIED ≠ EXERCISED`, and every scope claim so far is DESIRED.** Every statement
in this brief about what a policy permits is read from a **document**. No
`simulate-principal-policy` battery has been run. `comp-iam` states this limit about itself.

**D4 — SETTLED BY ANDREW 2026-09-09 ~17:2xZ. EXTEND `comp-iam-usage` TO PERMISSION GRAIN; AWS ACCESS
ANALYZER IS THE FALLBACK.** ⛔ *This was previously an open fork inviting re-examination; it is now
ruled, and is recorded here so the L2 cut does not treat a settled question as open.*
Basis: `comp-iam-usage` already FIXES comp-iam's three Rule-22a limits rather than inheriting them,
already carries an `UNKNOWN` band, and is free and in-estate; Access Analyzer bills per analyzed role
against ~208 roles. ⛔ **No per-role price has been read by anyone — if Access Analyzer is ever taken
off the fallback shelf, pricing it is the first act, not an assumption inherited from this brief.**
The ruling settles INSTRUMENT DIRECTION only: it authorises no build and cuts no cell.
Record: `ANDREW_DIRECT_20260909_1458Z_INFRA_REPORT_FIVE_RULINGS.md`, ruling 20 (discharging ruling 18).

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
- **`comp-iam-usage`: BUILT, TRACKED AND RUNNING** at `.tools/comp-iam-usage` (committed
  `57d9c8fd20`, 2026-07-17; five subcommands; `self-test` PASSES). ⛔ **CORRECTED 17:1xZ — this line
  previously read "no code in the corpus", which was false.** Coverage: ROLE-coldness and
  APPLIED-plane reach are built; **the PERMISSION grain is not.**
- `website-estate-admin`'s console credential removed 2026-09-09 16:38Z; the MFA-condition gap
  persists in Terraform and re-arms at onboarding.

---

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. ~~**The live IAM fleet was never enumerated by this author.**~~ **DISCHARGED 17:5xZ (F2a).** The
   live plane WAS enumerated once `comp-find --corpus aws` was repaired, and the undeclared SET was
   confirmed identical across both substrates by this author. **The replacement non-claim, narrower
   and real: the 8-role delta between the 208 and 216 totals is UNEXPLAINED** — vintage drift and
   differing population scope are both untested — and `VINTAGE: UNREAD` means `comp-find --corpus
   aws` output carries no age of its own (D1a), so its rows were dated by reading `kuzu_cli`
   directly rather than from the census itself.
2. **No `simulate-principal-policy` battery was run.** Every scope statement — including the
   `website-estate-admin` exemplar — is read from a DOCUMENT and never EXERCISED.
3. **Whether the 2026-02-17 forty-policy remediation executed is unknown.** Nothing was read either
   way, and its directory location is not evidence.
4. ~~**The `comp-iam-usage` prototype was not run or located.**~~ **FALSIFIED AND REPLACED 17:1xZ** —
   it was located and run (F5 corrected). **The replacement non-claim, which is narrower and real:
   the tool was exercised only via `--help`, `limits` and `self-test` (offline). `role-cold`,
   `who-can-reach` and `reach-check` were NOT run against live AWS by this author**, so its coverage
   at role and APPLIED grain is read from its own `--help` and `limits` output, never exercised.
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
