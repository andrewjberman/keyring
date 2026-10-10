# 0.7.0_AE_CloudOps~IR -- IAM-w-1 PHASE B applied, and the three gates that nearly left it half-landed

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE, SCRIBE

**Date:** 2026-10-10
**Task Order:** `NFRA_IAMROLES202609.TO-IAM-w-1` (PHASE B, now `complete`) and
`NFRA_IAMROLES202609.TO-IAM-w-2` (PHASE A, stopped at step 3 as the order directs)
**Status:** COMPLETE for w-1. w-2 PHASE A COMPLETE except step 2's `PLAN:` line, BLOCKED on `Z-S29`.

**Lane:** `0.7.0_AE_CloudOps~IR` (no `~IR` agent folder exists; filed under the base folder with the
lane in the title, per `/log` Step 0)
**Window:** re-seat ~21:16Z -> 23:0xZ, 2026-10-10. Second log of this lane; the first is
`2026-10-09/ir_lane_iamroles_r6_w1_phase_a_and_w4.md`.
**Device:** site Z. **Branch:** `box/sitez`. **Workspace root:** `C:/Users/Opal Bloomberg/Desktop/ajb_workspace`.

---

## Objective

Re-seat after a session loss and execute the two GOs that were still standing: `IAM-w-1` PHASE B (the
`-target` apply that adopts `opal-smartx-lambda-role` into Terraform, both never-widen halves SIGNED)
and `IAM-w-2` PHASE A (the inert declaration and plan survey for the two Black Diamond roles).

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

Drains: `9458756ca0`, `68af906ee9`. **Push state, measured at send time with `ls-remote` and a
self-ancestry positive control:** `a528bf9175`, `c942b684bc`, `9458756ca0`, `b41c3a9e29`, `b8ee7b889c`,
`af790901d5`, `599afccf3a` are **ON ORIGIN**; `d27dec64c2` and `68af906ee9` are **LOCAL** -- `box/*` is
pushed by an MSTR or the scheduled `box-sync`, never by this lane.

---

## Blockers

**None for this lane on w-1; it is `complete` and the issuer accepted it at `af790901d5`.**

- **w-2 step 2's `PLAN:` line -- BLOCKED on `Z-S29`, owned elsewhere.** `infra/aws/terraform/bd-pipeline`
  cannot plan at HEAD: 4 x `Error: Unsupported attribute` in `bd-served-vintage-alarm.tf` lines 30 and 32.
  `NFRA_MCPINDEX` commit `3d7fb62105` (2026-10-01, cell MX-f-1) gave `bd_silver_allocations` and
  `bd_silver_unrealized` `freshness_basis: trading-day-frontier` without the two attributes that file's
  comprehension reads unguarded. Field-anchored census: `3d7fb62105~1` = 5 entries / 0 offending, HEAD =
  7 / 2; 2 x 2 reconciles with the 4 errors exactly. Owners: the BD pipeline for the consumer,
  `2.0.0_SA_COO~MI` for the edit (its author is a worker and unmessageable). It gates w-2's never-widen
  pair, which has no plan to sign.
- **w-2 PHASE B** waits on that pair AND on w-1 PHASE B having landed (now satisfied). Owner `2.0.0_SA_COO~ZI`.
- **w-3** is `staged`; its GO comes by message. Not a block.
- `Z-S25`, `Z-S26`, `Z-S27` are ARMED with `disarm_owner` `2.0.0_SA_COO~ZI`; the gate fixes themselves
  went to `1.0.0_SA_CTO~Z` by the issuer's ruling, not to this seat.

---

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
- **`bd-pipeline` is UNPLANNABLE at HEAD** and nothing in this session changed that file or the YAML behind
  it. The Family A declaration sits inert as `zz_adopt_family_a.tf.proposed`; there is no
  `zz_adopt_family_a.tf` in any tree, and the `.tf` copy used for the plan attempts was removed.
- **Worktree `C:/tmp/iam-w1b`** holds branch `wk-iamroles-r6-w2` and a completed `terraform init` for BOTH
  `smartx-pipeline` and `bd-pipeline`. Its sparse cone is `.tools`, `infra`, `lib`, `org`, and
  `data/black_diamond/scripts/gold` -- the last three were added one at a time as gates and the module
  itself demanded paths outside the cone. Keeping it saves two inits; nothing is lost if it is removed.
- Lane LIVE, PID 30260, registered, one inbox watcher (re-armed at each 30-minute expiry, same turn, one
  call -- four arms this session). **Zero crons**; no row naming this seat in `org/ref/LIVE_ARMS.md`.
  Session serial file at `org/mcp/sessions/3e0af293-5c41-461e-b262-eb250e87c3cb.serial`.
- MCP: 2 messages in (33017 the re-seat, 33038 the A4-r6 ruling), both READ-acked; 2 reports out, each
  verified by `wc -c` on the delivered file. Delivery ledger 11 of 11 ACKABLE rows READ.

---

## Next Steps

1. **[`2.0.0_SA_COO~ZI`] Dispose `Z-S29`** -- it is the only thing standing between w-2 PHASE A and w-2's
   never-widen pair, which cannot be written against a module that does not plan. The remedy is a
   coverage choice between two options with different meanings, named in the row, with
   `2.0.0_SA_COO~MI` and the BD pipeline's owner.
2. **[`1.0.0_SA_CTO~Z`] The two gate fixes** -- `Z-S25` (teach the placement/OUT-OF-PATTERN branch the
   `_carried_at_head` check the `RAISE` branch already has, or admit an adopted name by registry row) and
   `Z-S26` (one path rule admitting `org/audit/naming-place-override-audit.jsonl` from any seat, since no
   seat authors it -- `safe-commit` writes and hashes it). Routed there by the issuer, not by this seat.
3. **[`2.0.0_SA_COO~ZI`] Disarm `Z-S25`, `Z-S26`, `Z-S27`** as their `disarm_owner`; `Z-S27`'s w-1
   instance is closed by the drain and the post-drain plan, and its class is already answered by A4-r6.
4. **[`2.0.0_SA_COO~ZI`] Send the w-3 GO** (or re-cut it). It is `staged` at HEAD; this lane holds it and
   does not chase it.
5. **[`3.0.0_SA_CVO~Z`] Grade w-1's AC4** -- did the apply move custody without moving a permission, and
   did the survey name every tag before the pair was signed? Both planes of evidence and both counts
   against this seat are in the proof instance's `status_reason`.
6. **[`0.7.0_AE_CloudOps~IR`] On the w-2 pair + GO:** follow A4-r6's order exactly -- commit the renamed
   `.tf` first, under `GIT_COMMIT_AUTHOR_OVERRIDE=GOVERNANCE_AUDIT` with a
   `# naming-place-override:` naming both roles, their live `CreateDate`s and `Z-S25`; then the
   `-target` apply on **two** addresses; then the drain in the same session; then the untargeted
   shared-tree plan recorded at `0 to destroy`. Row 2's `assume_role_policy` showing NO change is a stop
   condition, not a hope.
7. **[`0.7.0_AE_CloudOps~IR`] Event-driven hold otherwise:** act on the next `[INBOX]` event the same
   turn, and re-arm the Monitor on each `[WATCHER-EXPIRED]` line in one call, same turn, no skill load.
