# 0.7.0_AE_CloudOps~IR -- IAM-w-1 PHASE B applied, three gates that nearly left it half-landed, and w-2/w-3 PHASE A

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE, SCRIBE

**Date:** 2026-10-10
**Task Order:** `NFRA_IAMROLES202609.TO-IAM-w-1` (PHASE B, now `complete`),
`NFRA_IAMROLES202609.TO-IAM-w-2` (PHASE A + step 1a) and `NFRA_IAMROLES202609.TO-IAM-w-3` (PHASE A) --
the last two stopped at step 3 as their orders direct
**Status:** **ALL FOUR ORDERS TERMINAL. FIVE ROLES NOW IN CODE across four modules**, every one applied
and verified live. w-1, w-2 and w-3 PHASE B complete this session; w-4 was complete earlier. Zero ledger
entries of this lane open or held. The one sovereign item, `Z-S34`, was answered by Andrew mid-session and
the act it blocked then landed.

**Lane:** `0.7.0_AE_CloudOps~IR` (no `~IR` agent folder exists; filed under the base folder with the
lane in the title, per `/log` Step 0)
**Window:** re-seat ~21:16Z -> 23:4xZ, 2026-10-10. Second log of this lane; the first is
`2026-10-09/ir_lane_iamroles_r6_w1_phase_a_and_w4.md`.
**Device:** site Z. **Branch:** `box/sitez`. **Workspace root:** `C:/Users/Opal Bloomberg/Desktop/ajb_workspace`.

---

## Objective

Re-seat after a session loss and execute the two GOs that were still standing: `IAM-w-1` PHASE B (the
`-target` apply that adopts `opal-smartx-lambda-role` into Terraform, both never-widen halves SIGNED)
and `IAM-w-2` PHASE A (the inert declaration and plan survey for the two Black Diamond roles). Two more
arrived mid-session and were taken as they landed: the `IAM-w-3` PHASE A GO (two further modules), and
amendment A6-r6's step 1a, which carried another project's ruled fix for the blocker w-2 PHASE A found.
Five of the session's acts were ruled by the issuer in response to findings this session filed, so the
work and the rules moved together rather than one waiting on the other.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| `terraform` (as the GRADING instrument) | `plan -target=... -out=<file>`; `show -json <file>` decomposed per `resource_change` and per attribute; `apply <that saved file>` via safe-apply; targeted re-plan; untargeted plan; `state list`; `state show` | PASS | The `-out`/`show -json` pair is the session's sharpest tool. `1 to import, 0 to add, 1 to change, 0 to destroy` is EXACTLY what a trust-policy rewrite would also print, so the summary line cannot grade the act; the per-attribute decomposition reported one differing attribute (`tags_all`) and zero `aws_lambda_function` addresses. Applying the SAVED plan removes the gap between what was graded and what ran. |
| `terraform` (as a HAZARD instrument) | the same `plan` run from the SHARED tree instead of my worktree | PASS | This is what found `Z-S27`. It only got run because a commit refusal made me ask what the module looked like from somewhere other than my own worktree -- and it read `1 to destroy` on a live role. |
| `safe-apply.sh` (Rule 18) | `-chdir=infra/aws/terraform/smartx-pipeline apply -no-color -input=false <saved plan>` | PASS | `comp-tagauthz` PASSED **over 0 candidate resources** -- recorded with that denominator, because rc=0 over an empty denominator says nothing about this role. `tombstone-gate` CLEAN, 0 creates against 7 tombstones. HALTGT **not cited**: a `~lane` seat is structurally unhaltable and a live Monitor moves the message first, so I read the inbox directly instead (empty). |
| `aws iam` (live reads as the oracle) | `get-role`, `list-role-policies`, `list-attached-role-policies`, `list-role-tags` on three roles, before and after | PASS | "Apply complete! 1 imported, 1 changed" is the producer talking about itself. The post-apply reads are what establish the four tags, the **0 detachments** and the five unchanged attributes. `simulate-principal-policy` deliberately NOT run: no permission moved, so there is no grant to simulate, and its four false-deny modes plus its false-allow mode would have added noise, not evidence. |
| `comp-tagauthz` | `check --default-tags-tree infra/aws/terraform/bd-pipeline` (no plan available) | PARTIAL | ADVISORY mode surfaced a REAL conditional grant -- `i-0643a5bee8a8feabf`, `System=CottonwoodPipeline`, "this tree's default_tags WOULD OVERWRITE THIS". Unlike Family B's empty-denominator pass, this one had to be chased: measured 0 of bd-pipeline's 7 managed instances, with a positive control reading 1. Its `9 tag-conditioned statements` still disagrees with PHASE A's hand count of 4 distinct triples; not re-derived, and the conclusion does not rest on either count. |
| `deploy_ledger.py` | `open` with 3 `--leg` specs; `list`; `close-leg` x3; `close` | PASS | `list`'s own FOREIGN-VIEW line ("measure the artifact, NEVER-2") is what sent me to the sibling entry's artifact instead of the three stale worktree markers. Its auto-commit refused twice and printed the exact two-file `safe-commit` invocation to run instead -- good gate design. |
| `safe-commit.sh` + `naming-gate.py` | 8 invocations: 3 REFUSED, 5 committed | PARTIAL | The refusals ARE two of the session's findings and the gate was right to fire each time; it asks the right question of the wrong population. Rows `Z-S25`, `Z-S26`. |
| `safe-merge.sh` | `wk-iamroles-r6-w1b`, then `wk-iamroles-r6-w2` | PASS | Fast lane both times; tree check "needed N file(s), dropped 0, foreign 0". The first drain is the commit that actually CLOSED the `Z-S27` destroy window, which is why it ran immediately rather than batched with later work. |
| `comp-find` / `comp-read` | ~8 runs; 3 rail denials (F1 blind recursive grep, F4 census into a pipe x2), each re-run as the printed REMAINDER | PASS | `comp-read --for` located the verdict table and the override block in a 2726-line gate in one read, and its UNREAD LEDGER named `override_valid`/`apply_override` as the highest-salience unread sections -- which is exactly where the answer was. Reading that the override converts `PLACE-REFUSE` rows ONLY, and that "the older limb's REFUSE is not affected", is what separated an overridable refusal from an unoverridable one. |
| `proof-of-spec-check.py` | `<instance> AC1,AC2,AC3,AC4 --governing-order <order>` | PASS | INVALID on the first run for three real reasons (two enum values, one escaping divergence in AC3's recorded invocation); VALID rc=0 after. Its `pin-drift` limb caught that I had pinned an artifact at the commit BEFORE its header fix. |
| `comp-iam` | NOT RUN | SKIP | Triggers absent: `gaps` is bound to an `iam.tf` change and `service` to a new boto3 call. This cell changed no `iam.tf` and wrote no code. It also cannot answer the question -- it models `(action)`, never `(action, resource)`, is a FLOOR not a warrant, and no permission moved for it to measure. |
| `comp-blast` | NOT RUN | SKIP | Its trigger is an infra change of unknown blast radius. Here the radius is the signed pair's table and the targeted plan names every resource an apply could touch -- a stronger answer than a static map. |
| `comp-pipescript` | NOT RUN | SKIP | `deployed`/`postdeps` gate gold-run triggers. No pipeline script, no gold run, no data in scope. |

**What worked:** grading the SAVED plan per attribute instead of reading its summary, and then re-reading
the world instead of the apply's own success line. And running the plan from the SHARED tree -- a view I
would not have taken if the commit had simply succeeded.

**What failed:** my own ordering (see Postmortem). Also, a sparse worktree made four separate gates fail
with `FileNotFoundError` on paths outside the cone, and that error is indistinguishable at a glance from a
real refusal -- the cone had to grow three times before a gate verdict was about my diff rather than my
checkout.

**Gap found:** the naming gate has a `_carried_at_head()` mitigation for "these bytes already exist at
HEAD, so this copy mints nothing", reachable only from the `RAISE` branch. The `OUT-OF-PATTERN`/placement
branch -- the one every adoption hits -- has no such check. Row `Z-S25`; the fix is `1.0.0_SA_CTO~Z`'s.

**On another seat's instruments, since this session ran two:** `2.0.0_SA_COO~MI`'s `f1r.AC1.sh` and
`f1r.AC2.sh` are the best-built checks I have been handed. AC1 reads `init` rc, `plan -detailed-exitcode`
rc, AND the counts of `Unsupported attribute` and `^Error` lines, so it cannot pass on a plan that merely
exits oddly; AC2 goes through `terraform console` to enumerate the *evaluated* locals rather than parsing
the config, which is why its pre-fix output independently confirmed my YAML census from a different plane.
Both carry their own expected-FAIL-at-HEAD claim in a header comment, which is what let me use them as a
negative control without writing anything myself.

---

## Deployment Sequence

| Step | Action | Result |
|---|---|---|
| 0 | Re-read the world before trusting the prior session's record | role live-identical to the PHASE A survey; ledger `list` 30 entries, **0** matching `smartx\|iamroles`; the sibling entry on this module CLOSED all-3-legs `20261009T133651Z`; prior worktree `C:/tmp/iam-w1` GONE |
| 1 | Cut a fresh sparse worktree from `box/sitez` HEAD | `C:/tmp/iam-w1b`, branch `wk-iamroles-r6-w1b` @`bc255d2730`, clean |
| 2 | `terraform init` (`smartx-pipeline`) | provider `hashicorp/aws v5.100.0`, backend s3 `smartx-pipeline/tfstate` |
| 3 | Open the deploy ledger FIRST (NEVER-2), 3 legs | `a528bf9175` |
| 4 | Rename `.tf.proposed` -> `.tf` (pure R100, bytes `cmp`-identical to HEAD) | AC1 grep reads `0`; `fmt -check` clean |
| 5 | Targeted plan, SAVED | `Plan: 1 to import, 0 to add, 1 to change, 0 to destroy.` |
| 6 | Grade the saved plan from `show -json`, per attribute | 1 `resource_change`; 1 non-no-op; **exactly 1 attribute differs** (`tags_all` -> the four keys); `assume_role_policy`/`inline_policy`/`managed_policy_arns` absent from the delta; **0** `aws_lambda_function` addresses |
| 7 | `safe-apply` the SAVED plan | `Apply complete! Resources: 1 imported, 0 added, 1 changed, 0 destroyed.` |
| 8 | Live AWS read-back (not the apply's output) | exactly 4 tags; **3 inline policies still attached, 0 detachments**; `AttachedPolicies []`; path/description/max-session/trust/boundary unchanged |
| 9 | Targeted re-plan | `No changes. Your infrastructure matches the configuration.` |
| 10 | Untargeted module plan | `0 to add, 3 to change, 0 to destroy` -- identical to PHASE A's negative-control baseline |
| 11 | Commit the act -- **REFUSED twice**, then landed | naming gate `NAMING-PLACE: REFUSE 2`, then `GOVERNANCE_AUDIT` lane violation; landed `c942b684bc` under two stacked audited overrides |
| 12 | **Drain to `box/sitez`** -- the step that closed the hazard | `9458756ca0`; shared-tree plan re-read `0 to destroy` (was `1 to destroy`) |
| 13 | Close the 3 ledger legs and the entry LAST | `open=0 closed=1` |
| 14 | Correct the now-false header on the live `.tf` | `b41c3a9e29`; module plan byte-identical across it |
| 15 | Rows, proof instance, `<status>` flip | `b8ee7b889c`, `af790901d5` (proof VALID rc=0) |

`pipeline_inventory.xml` NOT updated: the seat prompt binds that to an apply reaching 0-diff on a
pipeline's own resources; this apply adopted one pre-existing IAM role and added no pipeline resource.
Stated rather than silently skipped.

### The three PHASE A cells, which applied nothing

| Step | Act | Result |
|---|---|---|
| w-2.1 | Two BD roles read live; inert declaration written | row 2 trusts `ecs-tasks.amazonaws.com` and has NO description -- both read from the role, not copied |
| w-2.2 | Plan `bd-pipeline` | **BLOCKED** -- 4 x `Unsupported attribute`, cause outside this cell (`Z-S29` @`599afccf3a`) |
| w-2.2 | Deliver everything the plan did not gate | 3 of 4 required lines measured; `PLAN:` recorded BLOCKED **with its cause** rather than invented |
| w-3.0 | GO arrived; `<status>` staged -> pending | `2543076e4b` -- the LAST tag, never the first |
| w-3.1 | Two more roles read live; two inert declarations | row 11 is the program's FIRST role with an **attached managed policy**; row 3 trusts CodeBuild and is the only role here in active use |
| w-3.2 | Plan both modules + a negative control each | `1 to import / 0 / 1 / 0` each; **both controls read "No changes" -- zero pre-existing drift** |
| w-3.2 | Grade both per attribute | 39 and 141 `resource_changes`, 1 non-no-op each, 1 attribute each (`tags_all`); 3 tags vs 4 -- **the modules differ** |
| w-2.1a | A6-r6: apply ~MI's ruled `can()` guard, committed ALONE | `a18b96fd5d`; 1 insertion / 1 deletion; YAML untouched; zero plan delta |
| w-2.1a | Run ~MI's `f1r.AC1.sh` / `f1r.AC2.sh` BEFORE and AFTER | FAIL/FAIL -> PASS/PASS, re-verified in the SHARED tree after the drain |
| w-2.2 | Re-run step 2 | `2 to import, 0 to add, 2 to change, 0 to destroy`; the BLOCKED line replaced |
| -- | Drains | `68af906ee9` (w-2 A), `f219486b2a` (w-3 A), `df0248d4f6` (1a + re-run) |

All four modules in the shared tree at the end: `smartx-pipeline` `0 to add, 3 to change, 0 to destroy`
(three PRE-EXISTING Lambda drifts, not this cell's), and `bd-pipeline`, `portfolio-management` and
`news-pipeline` each `No changes. Your infrastructure matches the configuration.`

### w-2 PHASE B -- the GO arrived, and the act STOPPED before AWS

| Step | Act | Result |
|---|---|---|
| 0 | Both signed halves read at HEAD (COO @`1ad6f36ca2`, CTO @`dadc1ec69a`) | the pair signs `2 import / 0 add / 2 change / 0 destroy`, four keys each, `-target` on two addresses |
| 0 | Preconditions measured myself, not taken from the GO | 0 open `.open_deploys/` entries matching `bd-pipeline\|iamroles` over 33 listed / 29 ledger entries; both roles `Tags []`, one inline policy each, 0 attached |
| 4 | Ledger `iamroles-r6-family-a` opened FIRST, 3 legs | `ae27a5f5f8` -- and it AUTO-COMMITTED, which the lane-ANY fix (`Z-S26`) made possible |
| 5 | Rename to `.tf`, pure R100, AC1 grep 0, fmt clean | staged fine |
| 5 | **Commit the rename -- REFUSED 4x** | `hand-kept carrier of 'bd' outside every permitted context`; `NAMING-GATE: REFUSE 4 graded`, **no `NAMING-PLACE` line**, on two runs with a valid override. Row `Z-S34` |
| -- | Rename reverted; declaration back to `.tf.proposed` | nothing live |
| -- | Ledger HELD-PRE-APPLY on the named gate | `47955fd728`, verified at HEAD not on the working tree |

**NOTHING WAS APPLIED, measured on three planes:** `bd-pipeline` state holds **0 of the 2** roles against a
positive control of 17 `aws_iam_role` entries; both roles still read `Tags []`; and the shared tree carries
no live `zz_adopt_family_a.tf`. The module plans `No changes`.

**THE ORDERING FIX PAID FOR ITSELF ON ITS FIRST REAL EXERCISE.** The same refusal class in w-1 arrived
AFTER the apply and left a live IAM role planned for destruction. A4-r6 put the commit before the import,
so this time the identical gate behaviour cost nothing at all.

### w-3 PHASE B -- two modules, two applies, the round's cleanest cell

A7-r6 @`7c213215bd` released the "w-2 lands first" condition IN PLACE in the COO half and `1.0.0_SA_CTO~Z`
struck it in the CTO half, on the ground that the two acts write different modules with separate state keys
and zero pre-existing drift. So w-3 landed while w-2 stayed held.

| Step | Act | Result |
|---|---|---|
| 0 | Both halves read at HEAD; both sequencing releases verified in place, not taken on the GO's word | COO @`9586e0106b`, CTO @`8453026444` |
| 0 | Preconditions measured | 0 open entries matching `portfolio\|news\|family-e` over 34 listed; both roles `Tags []`; row 11 **1 attached managed**, row 3 codebuild trust |
| 4 | **TWO** ledger entries opened, one per module, 3 legs each | each module's own stop condition is its middle leg: MANAGED / TRUST |
| 5 | Both renames committed FIRST, pure R100, placement override, **no author override** | `1df69456eb`; 4 rows OVERRIDDEN, WARN 4 graded |
| 5 | Two targeted plans saved, then graded per attribute | 1 `resource_change` / 1 non-no-op / 1 attribute each; **0 other addresses** |
| 5 | **The sharp check: each module's tags against its OWN provider block** | **3 keys** for portfolio-management with `System` confirmed ABSENT; **4** for news-pipeline |
| 5 | Two applies of the saved plans | `1 imported, 0 added, 1 changed, 0 destroyed` each |
| 5 | **Stop conditions, read LIVE** | row 11: `AWSLambdaBasicExecutionRole` **still attached**; row 3: trust still `codebuild.amazonaws.com`, description still absent |
| 5 | Drain in the SAME session (A4-r6) | `763f3934c9` |
| 5 | **Required post-drain untargeted plans in the SHARED tree** | **"No changes" in BOTH modules** -- the Z-S27 window never opened |
| 6 | `POST_APPLY_family_e.md`, both ledgers closed, proof VALID rc=0 first pass | `8cf6951908`, `fc8da02312` |

**Why this was the round's easy cell, which is the instructive part:** all three mechanisms that cost w-1
and w-2 real trouble had been fixed by the time it ran -- the ordering (A4-r6, after w-1 left a live role
planned for destruction), the override's own lane (`b7c27ef5b0`, after it refused the commit it had just
authorised), and the override's scope (A5-r6 dropping the stacked author override). The work left was
grading two modules without letting either one's numbers contaminate the other.

### w-2 PHASE B -- held, unblocked by Andrew, then landed; the round's hardest cell

| Step | Act | Result |
|---|---|---|
| -- | **First attempt**: ledger opened, rename committed... | **REFUSED 4x** on the carrier limb; `Z-S34`; **nothing in AWS** |
| -- | Ledger HELD-PRE-APPLY on the named gate | `47955fd728`; hold re-run after the first write was discarded |
| -- | Reported the hold as correctly standing, on a MEASURED zero | `comp-find` over `infra/logic`: 0 hits across 29 files |
| -- | **Surfaced Andrew's dropped qualifier** | relay said "yes"; record says `YES, the exception, "for now"` |
| -- | CTO landed R20 X17 entries, **cutoff 2026-12-31** -- carrying his qualifier | `bd2cacee69`, ancestry verified here with a positive control |
| 4 | Hold RELEASED, committed in the same step as the mutation | `b0fdae1419` |
| 5 | Rename committed, **NO override of any kind** | `869c01686c`; **DECLARED-EXCEPTION at all 4 sites**, WARN 4 graded |
| 5 | Two-address targeted plan, saved, graded per attribute | 2 non-no-op, 1 attribute each, 4 keys exact-match, **0 other addresses** |
| 5 | Apply | 2 imported, 2 changed, 0 destroyed -- **confirmed from live reads + `state list`**, not from the producer |
| 5 | Drain, same session | `401e211747` |
| 5 | **Post-drain untargeted plan, SHARED tree** | **"No changes"** |
| 6 | `POST_APPLY_family_a.md`, ledger closed, proof VALID rc=0 | `ee46dead92`, `beeb07f26c` |

**THE ROUND'S SHARPEST PIECE OF EVIDENCE sits in this cell: two step-5 commits on IDENTICAL BYTES.**
The first, carrying a valid audited placement override, read `NAMING-GATE: REFUSE 4 graded`. The second,
carrying **no override at all** but with register entry X17 at HEAD, read `DECLARED-EXCEPTION` at all four
sites. Same file, same seat, one variable -- which is what makes `Z-S34` a finding and the R20 route a
demonstrated remedy rather than an inference.

**Three external unblocks, none of them this lane's to grant, each resolved by its owner once named:**
`Z-S29` (the module could not plan for nine days; ruled by `2.0.0_SA_COO~MI`, carried as A6-r6 step 1a,
landed here with zero plan delta), `Z-S34` (Andrew's R20 word plus the CTO's register entry), and in
between, my own first ledger hold failing to persist.

---

## Postmortem -- I proved the apply was safe and did not prove the commit was possible

**Root cause.** The cell's step order (4 open the ledger, 5 rename and apply, 6 re-plan and record) reads
as though the apply is the only irreversible moment, and I followed it literally. The apply writes the
import to the **shared remote state** immediately; the declaration that justifies it lives only in my
worktree until a commit and a drain. Terraform's rule is that a resource in state with no configuration
is a planned **DESTROY**.

| what I verified before acting | what I did not verify |
|---|---|
| the plan equals the signed pair, per attribute | that the renamed `.tf` could be COMMITTED at all |
| both never-widen halves are files and SIGNED | that the naming gate admits an adopted pre-existing name |
| no open ledger entry on this module | that my lane may write the override's own audit row |
| the live role matches the survey | what the module plans from the SHARED tree |

**Consequence, measured on both sides rather than inferred from the fix:** with the declaration absent
from the shared tree, `terraform plan` in `smartx-pipeline` read `Plan: 0 to add, 3 to change, 1 to
destroy` -- `aws_iam_role.opal_smartx_lambda_role will be destroyed (because it is not in
configuration)` -- on a live role carrying three inline policies, in a module that already holds three
pending Lambda changes its owner may apply at any time. After the drain, `0 to destroy`.

**Resolution.** Landed the declaration (the act that removes the hazard) rather than rolling back a
correctly-signed act, then filed `Z-S27` with the prescription. The issuer ruled it the same hour:
amendment **A4-r6** @`7af7a24e9f` rewrote step 5 of w-2 and w-3 -- commit the rename FIRST, on the worker
branch, then import, then drain in the same session, then an untargeted shared-tree plan recorded at
`0 to destroy`. So the ordering is now mechanism, not discipline.

**What I would do differently in one line:** run the real `safe-commit` invocation on the renamed `.tf`
before touching AWS; it costs one command and it is the whole of the fix.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Land the declaration under two stacked audited overrides rather than roll back | The alternatives were worse. Rolling back would discard a correctly-signed act AND leave the gate defect undiagnosed; leaving it uncommitted left a live IAM role staged for deletion. Landing it is the act that removes the hazard. Both overrides are in their audit logs, the `--author` line stayed this lane's, and `Z-S26` records the stacking as a WORSE control rather than a solved problem. |
| Do NOT rename the role to the canonical `smartx-lambda-role` | An IAM role cannot be renamed in place, so it is a create-plus-delete WORLD act outside the cell's BOUNDS and outside the signed pair. Rule 30's own non-application clause routes an existing resource to its own migration project. The issuer confirmed this in A4-r6. |
| Fix the file's header in a SEPARATE commit, after the act | The act's commit is a pure R100 rename of bytes already at HEAD -- the minimum possible diff for a WORLD act. The header said "DO NOT RENAME THIS FILE TO `.tf`" under the name `.tf`, which is a trap for the next reader, but it is not worth enlarging the signed commit. |
| Record AC2's canonical line as a DECLARED DEPARTURE | Terraform renders a clean plan as a sentence, not a count, so the line AC2 greps is my canonical form of its result. Its verbatim output is quoted beside it so a reader can judge the translation instead of taking it. |
| Do NOT propose a fix for `Z-S29` | The two candidates differ in MEANING -- a `try()` default silently drops two tables from the alarm's served-key coverage, which is a freshness-coverage decision, not a syntax fix. That choice belongs to the two owners. |
| Hold w-3 | Its `<status>` is `staged` at HEAD and no GO has arrived. A3-r6's message mentions w-3 but the amendment flipped only w-2; I asked rather than adjudicating the issuer's scope wider. |
| Record w-2's `PLAN:` line as BLOCKED **with its cause** rather than inventing a value or reporting the whole cell blocked | The cell's other three required lines, the live reads, both censuses and the entire tag-authorization read did not depend on a plan, so they were delivered. Scaling the deliverable down is the issuer's call; my job was to finish everything not gated and say precisely what was. |
| Propose NO fix for `Z-S29`, although the one-line candidate was obvious | The two candidates differ in MEANING: a `can()`/`try()` default silently drops two tables from the alarm's served-key coverage. That is a freshness-coverage decision belonging to two other seats, and an AE proposing it as a "syntax fix" would have smuggled a coverage change past its owners. `2.0.0_SA_COO~MI` ruled it in about forty minutes. |
| Run `2.0.0_SA_COO~MI`'s two checks BEFORE the step 1a edit, not only after | A check that only ever runs after a fix cannot distinguish a working recognizer from one that always passes. Both FAILed before and PASSed after, and `f1r.AC2`'s BEFORE output turned out to be a third independent confirmation of `Z-S29`'s count -- from evaluated Terraform locals rather than from my parse of the YAML. |
| Re-run both checks in the SHARED tree after the drain, not just in the worktree | The worktree is where I made the change, so a pass there measures my copy. The claim that matters is about the repository every other seat reads. |
| Keep section 4 of the Family A survey -- the full record of why the module could not plan -- after the fix landed | A survey showing only the working plan would hide that `bd-pipeline` was unplannable for nine days, which is the evidence behind `Z-S29` and the reason step 1a exists. |
| Do NOT fix the five pre-existing `terraform fmt` failures I found in three modules | Outside the orders' `<paths>`, and formatting unrelated files is a rider on a WORLD cell. Surfaced in both surveys instead, with the note that a later module-wide `fmt -check` will fail on them and the adoption will not be the cause. |
| Chase comp-tagauthz's ADVISORY instance rather than dismissing it as another empty-denominator pass | Family B's collision was answerable by scope alone; this one named a LIVE instance whose tag authorizes `ec2:StartInstances` and said this tree's `default_tags` would overwrite it. The tool states its own limit, so the question had to be measured: 0 of bd-pipeline's 7 managed instances, with a positive control reading 1, later corroborated by the tool's own GATE-mode denominator. |
| Build the w-3 tag check as an EQUALITY TEST against a per-module expected dict, not an eyeball of the printed keys | The two modules write 3 and 4 keys. Families A and B both wrote four, so four is the number I arrived with, and a glance at module 1's output would have read "looks right" against the wrong target. The script compared each module's `tags_all` to a dict written from THAT module's provider block and separately asserted `System` absent from module 1. |
| Open TWO ledger entries for w-3 rather than one covering both modules | The cell says "one per module" and AC3 expects `closed=` 2 or more. One entry would have made a single close cover two independent applies, so a half-landed second module would have read as fully closed. |
| Record that AC3's `closed=` limb cannot prove closure, rather than quoting `closed=2` as if it did | `deploy_ledger.py open` writes the completion file at OPEN time, so the limb read 2 before either apply. Noticing that cost one read of the count at the wrong moment; not noticing it would have put a false corroboration in the proof instance. w-1's AC3 had the mirror-image defect and the same treatment. |
| File `Z-S35` against myself in the channel, rather than leaving the probe error in a commit message | The ambiguity that caused it is in MY OWN row `Z-S27`'s prescription, which w-3 PHASE B then had to follow. A lesson that lives only in a revert message is not available to the next cell that reads the row. |
| Release the hold on w-2 rather than close-and-reopen, when `Z-S34` clears | The entry was opened before the act, as NEVER-2 requires, and nothing was applied. Closing it NOT-APPLIED and opening a fresh one would lose the fact that the act was authorised, prepared and stopped at a named gate. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `infra/aws/terraform/smartx-pipeline/zz_adopt_family_b.tf` | renamed from `.tf.proposed` (R100), then header corrected | Yes -- `c942b684bc`, `b41c3a9e29` |
| `org/critical_paths/.open_deploys/iamroles-r6-family-b.json` | opened then removed at close | Yes -- `a528bf9175`, `c942b684bc` |
| `org/critical_paths/change_management/20261010T2144Z_iamroles-r6-family-b_deploy_completion.md` | 3 legs opened and closed | Yes -- `a528bf9175`, `c942b684bc` |
| `.../deliverables/0.7.0_AE_CloudOps~IR/round6/POST_APPLY_family_b.md` | new -- the act's record | Yes -- `c942b684bc` |
| `org/audit/naming-place-override-audit.jsonl` | created by `safe-commit` itself (the override's own row) | Yes -- `c942b684bc` |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | rows `Z-S25`, `Z-S26`, `Z-S27`, then `Z-S29` | Yes -- `b8ee7b889c`, `599afccf3a` |
| `.../task-orders/...TO-IAM-w-1...md` | LAST `<status>` -> `complete` | Yes -- `af790901d5` |
| `.../deliverables/0.7.0_AE_CloudOps~IR/...TO-IAM-w-1....proof_of_spec.json` | new -- VALID rc=0 | Yes -- `af790901d5` |
| `infra/aws/terraform/bd-pipeline/zz_adopt_family_a.tf.proposed` | new -- inert, 2 roles | Yes -- `d27dec64c2` |
| `.../round6/PLAN_SURVEY_family_a.md` | new -- 3 of 4 lines measured | Yes -- `d27dec64c2` |

| `infra/aws/terraform/bd-pipeline/zz_adopt_family_a.tf.proposed` | new -- inert, 2 BD roles | Yes -- `d27dec64c2` |
| `.../round6/PLAN_SURVEY_family_a.md` | new, then the BLOCKED `PLAN:` line replaced with the real one | Yes -- `d27dec64c2`, `a1667d4af4` |
| `infra/aws/terraform/bd-pipeline/bd-served-vintage-alarm.tf` | step 1a -- the `can()` guard, ONE clause, committed ALONE | Yes -- `a18b96fd5d` |
| `infra/aws/terraform/portfolio-management/zz_adopt_family_e.tf.proposed` | new -- inert, row 11 | Yes -- `8361e51c56` |
| `infra/aws/terraform/news-pipeline/zz_adopt_row3.tf.proposed` | new -- inert, row 3 | Yes -- `8361e51c56` |
| `.../round6/PLAN_SURVEY_family_e.md` | new -- all four lines for BOTH modules | Yes -- `8361e51c56` |
| `.../task-orders/...TO-IAM-w-3...md` | LAST `<status>` staged -> pending at the GO | Yes -- `2543076e4b` |
| `.../logs/2026-10-10/ir_lane_iamroles_r6_w1_phase_b_and_w2_phase_a.md` | this log | Yes -- `9ec3bb4488`, and this commit |

Drains: `9458756ca0`, `68af906ee9`, `f219486b2a`, `df0248d4f6`. **Push state, measured at send time with `ls-remote` and a
self-ancestry positive control:** the session's commits through `68af906ee9` are **ON ORIGIN**
and the later ones are **LOCAL** at the time of writing -- `box/*` is pushed by an MSTR or the scheduled
`box-sync`, never by this lane, so LOCAL here is the expected steady state and not an omission. The
measurement is per commit with `git merge-base --is-ancestor` against the `ls-remote` tip, beside a
self-ancestry positive control that PASSED (a containment check that can never answer yes reads LOCAL
identically to a true LOCAL).

---

## Blockers

**NONE. All four orders are terminal and nothing of this lane's is open or held.** Every blocker this
session hit was resolved inside it, and the one sovereign item was answered by Andrew mid-session.

- **`Z-S34` -- RAISED AND CLOSED.** The naming gate's OLDER carrier limb refuses a name carrying a firm
  token (`bd` -> `49financial`), and the audited placement override does NOT reach that limb -- measured
  on two runs printing no `NAMING-PLACE` line at all, against the same override text converting four rows
  for w-3 in the same session. Resolved by the route the canon itself names: Andrew answered
  `YES, the exception, "for now"` (@`5e10dd2dc5` item 4) and `1.0.0_SA_CTO~Z` landed R20 entries
  NFRA-IAMROLES-R20-01/02 (@`bd2cacee69`, register X17, **cutoff 2026-12-31**, carrying his qualifier).
  **I surfaced that qualifier** because the relay to me had compressed it to "yes" and an R20 entry carries
  a cutoff; it landed in the cutoff. The act then took no override at all.
- **`Z-S29` -- RAISED AND CLOSED by three seats.** `bd-pipeline` could not plan at all for nine days after
  an `NFRA_MCPINDEX` config edit. I filed it with four controls and its owners named and **proposed no
  fix**, because the candidates differ in meaning. `2.0.0_SA_COO~MI` ruled it, `2.0.0_SA_COO~ZI` carried
  the ruling in as A6-r6 step 1a, and I landed the one clause with a measured zero plan delta.
- **`Z-S26` -- CLOSED AT SOURCE** by `0.0.0_AB_MSTR~Z` (@`b7c27ef5b0`), exactly the one path rule asked for.
- **`Z-S27` -- FIXED AND THEN TWICE VINDICATED.** It became A4-r6's rewritten step 5, and the two PHASE Bs
  that followed both hit refusals at precisely that step with nothing in AWS. The hazard it describes --
  w-1's live IAM role planned for destruction -- never recurred.
- **`Z-S25` -- open and correctly not mine.** The gate fix is `1.0.0_SA_CTO~Z`'s, parked at dell1. Its
  practical effect is now bounded: three of the four names clear via the placement override and the
  fourth pair via R20 X17 until 2026-12-31.
- **`Z-S35` -- my own error, closed.** Reverted, local-only, nothing applied. Its lesson was applied in the
  very next cell: w-2's step-5 commit WAS the probe, run in its proper place in the ruled order, so its
  refusal cost nothing and needed no separate dry run.
- **Owned elsewhere, none stranded:** w-1's, w-2's and w-3's AC4 (`3.0.0_SA_CVO~Z`, judgment); the five
  rows' dispositions and disarms (`2.0.0_SA_COO~ZI`); the three `smartx-pipeline` Lambda drifts
  (`Z-S20`'s route); the pre-existing `fmt -check` failures and `naming-apply-gate` WARNs on unrelated
  files in three modules (surfaced in the surveys and records, outside every order's `<paths>`).

## Current State

Written for a reader with zero prior context.

- **Live in the world, changed by this session:** `opal-smartx-lambda-role` is now MANAGED BY TERRAFORM in
  `smartx-pipeline` (state key `smartx-pipeline/tfstate`) and carries exactly four tags --
  `Environment=Production`, `ManagedBy=Terraform`, `Project=OpalPortal`, `System=SmartXPipeline` -- where
  it carried none. **Nothing else changed:** its three inline policies (`opal-smartx-logs`,
  `opal-smartx-s3-access`, `opal-smartx-secrets`) are still attached, 0 managed policies are attached, and
  its path, description, `max_session_duration`, trust (`lambda.amazonaws.com`) and permissions boundary
  are identical to the pre-act reads. The pair's rollback (`terraform state rm` + `untag-role` + revert the
  rename) stayed available and was never used.
- **The hazard this session opened is CLOSED and re-measured:** the shared tree's `smartx-pipeline` plan
  reads `0 to add, 3 to change, 0 to destroy`, the same as PHASE A's negative-control baseline. The three
  `aws_lambda_function` drifts and three output removals in that line are PRE-EXISTING and belong to
  `smartx-pipeline`'s owner on row `Z-S20`'s route -- this cell's targeted plan contained zero Lambda
  addresses.
- **`bd-pipeline` PLANS AGAIN** -- it was unplannable at HEAD for nine days and step 1a's one-clause
  `can()` guard fixed it (`a18b96fd5d`). Verified in the SHARED tree, not only in the worktree that made
  the change: `No changes. Your infrastructure matches the configuration.`, and both of `2.0.0_SA_COO~MI`'s
  checks PASS there (`f1r.AC1` 0 Unsupported-attribute / 0 Error lines; `f1r.AC2` keys == want, the five
  daily platinum keys). Both FAILed before the edit, so they discriminate rather than always passing.
  The guard's own plan delta is ZERO, which is what confirms ~MI's premise that nothing consumes those
  locals. **The YAML was NOT touched** -- the remedy was ruled to be the guard, not the data.
- **ALL FOUR declarations are live:** `smartx-pipeline/zz_adopt_family_b.tf`,
  `bd-pipeline/zz_adopt_family_a.tf`, `portfolio-management/zz_adopt_family_e.tf` and
  `news-pipeline/zz_adopt_row3.tf`. No `.tf.proposed` of this round remains. Every `.tf` copy used for a
  PHASE A plan run was removed and none was committed.
- **Worktree `C:/tmp/iam-w1b`** holds branch `wk-iamroles-r6-w2-1a` and a completed `terraform init` for
  ALL FOUR modules (`smartx-pipeline`, `bd-pipeline`, `portfolio-management`, `news-pipeline`). Its
  sparse cone is `.tools`, `infra`, `lib`, `org` and `data/black_diamond/scripts/gold` -- the last few
  added one at a time as gates and then the module itself demanded paths outside the cone. Keeping it
  saves four inits; nothing is lost if it is removed, since every branch is drained.
- **FIVE roles are now in code, across four modules, and that is the whole of what this session changed
  in the world:** `opal-smartx-lambda-role` (4 tags), `portfolio-management-lambda-role` (**3** tags, no
  `System` key) and `codebuild-semantic-clustering-role` (4 tags incl. `System=NewsPipeline`). Each was
  imported into its module's state and each carries exactly its module's `default_tags` set, where all
  five carried zero before -- plus `bd-merge-daily-lambda-role` and `bd-pipeline-task-role`, 4 tags each.
  **No permission moved anywhere:** every role's policies, trust, path, description, max session and
  boundary are identical to the pre-act reads; row 11's attached `AWSLambdaBasicExecutionRole` -- the one
  managed attachment in the program -- survived its import; and `bd-pipeline-task-role`'s
  `ecs-tasks.amazonaws.com` trust and absent description are unchanged. **Live tag counts: 4, 4, 4, 3, 4**
  -- the 3 is `portfolio-management`, whose module declares no `System` key.
- **One clause of `bd-served-vintage-alarm.tf` also changed** (step 1a's `can()` guard, `a18b96fd5d`),
  which is what made `bd-pipeline` plannable at all. Zero plan delta, measured. No instance, Lambda,
  alarm, schedule or notification moved in any module.
- **Four ledger entries, ALL FOUR CLOSED with every leg proven** -- `iamroles-r6-family-b` (w-1),
  `iamroles-r6-family-e-portfolio-management` and `-news-pipeline` (w-3), and `iamroles-r6-family-a`
  (w-2), which is the only one that travelled OPEN -> HELD-PRE-APPLY -> OPEN -> CLOSED. Nothing of this
  lane's is open or held. On that last entry:
  HELD-PRE-APPLY on the `Z-S34` gate (`47955fd728`, verified at HEAD rather than on the working tree,
  because my first hold wrote the file and was then discarded by a revert before it was ever committed --
  the tool's OK line described a change that no longer existed). `iamroles-r6-family-b` is CLOSED. Nothing
  of this lane's is open.
- Lane LIVE, PID 30260, registered, one inbox watcher (re-armed at each 30-minute expiry, same turn, one
  call -- four arms this session). **Zero crons**; no row naming this seat in `org/ref/LIVE_ARMS.md`.
  Session serial file at `org/mcp/sessions/3e0af293-5c41-461e-b262-eb250e87c3cb.serial`.
- MCP: **8 messages in, all READ-acked** -- 33017 re-seat, 33038 A4-r6, 33054 w-3 PHASE A GO, 33067 A6-r6
  step 1a, 33097 w-2 PHASE B GO, 33102 w-3 PHASE B GO, 33158 Andrew's R20 answer, 33162 the RESUME;
  **11 reports out**. Every arrival was acted on in the turn it landed, which is why eight rulings and
  amendments could be absorbed mid-round without a restart. Message 33067 is worth noting for a successor: its
  `[INBOX]` event fired while BOTH probes read empty (the LD-0099 ferry case), and it was read from the
  `read/` dir newest-first exactly as `org/XXX.md` Step 1b B directs. Every arrival was acted on in the
  same turn it landed, which is why four separate rulings could be absorbed mid-cell without a restart.

---

## Next Steps

1. **[Andrew, via `1.0.0_SA_CTO~Z`] The R20 declared exception for the two `bd` role names** -- the only
   thing standing between w-2 PHASE B and its apply, and the only sovereign item in this log. Rule 30 makes
   an R20 entry a departure Andrew acknowledges; the pair is already signed and the plan already measured,
   so nothing else is owed once it lands.
2. **[`0.7.0_AE_CloudOps~IR`] Close `iamroles-r6-family-a` NOT-APPLIED at ~06:03Z** if the R20 call is still
   unanswered when its 6-hour window ends -- the issuer's instruction in msg 33102. Nothing is applied, so
   the close is a record of a held act and not a rollback. If the call lands first, the hold releases and
   PHASE B proceeds unchanged against the already-signed pair.
3. **[`1.0.0_SA_CTO~Z`] The `Z-S25` gate fix** -- teach the placement/OUT-OF-PATTERN branch the
   `_carried_at_head` check the `RAISE` branch already has, or admit an adopted name by registry row.
   Parked at dell1 per the issuer. Until it lands, PHASE B of w-2 and w-3 carries the audited placement
   override by ruled instruction. (`Z-S26` needs nothing further -- it was fixed at source @`b7c27ef5b0`.)
4. **[`2.0.0_SA_COO~ZI`] Disarm `Z-S25`, `Z-S27`, `Z-S29`** and dispose `Z-S34` / `Z-S35` as their
   `disarm_owner`. Their substance is answered -- `Z-S27` by A4-r6's rewritten step 5 and now **twice
   exercised** (it cost w-2 nothing and w-3 nothing), `Z-S29` by step 1a's landed guard, `Z-S25` by the
   standing ruling plus the parked fix, `Z-S34` by the sovereign call it is waiting on -- but the disarm is
   the issuer's act and this seat did not touch any row's disposition. `Z-S35` additionally carries a
   suggested re-wording of `Z-S27`'s prescription, which the issuer owns.
5. **[`3.0.0_SA_CVO~Z`] Grade w-1's AND w-3's AC4** -- did the apply move custody without moving a permission, and
   did the survey name every tag before the pair was signed? Both planes of evidence and both counts
   against this seat are in the proof instance's `status_reason`.
7. **[`0.7.0_AE_CloudOps~IR`] When `Z-S34` clears, w-2 PHASE B resumes from step 5 unchanged:** the pair is
   already signed and the plan already measured at `2 to import, 0 to add, 2 to change, 0 to destroy` with
   four keys per role. The ledger entry exists and is held, so releasing the hold rather than opening a new
   entry is the correct move. The stop condition to re-verify live is row 2's `assume_role_policy` -- the
   `ecs-tasks.amazonaws.com` principal -- plus one inline policy each and no detachments.
8. **[`0.7.0_AE_CloudOps~IR`] Event-driven hold otherwise:** act on the next `[INBOX]` event the same
   turn, and re-arm the Monitor on each `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.
