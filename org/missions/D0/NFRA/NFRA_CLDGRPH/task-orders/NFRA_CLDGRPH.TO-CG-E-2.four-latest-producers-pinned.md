# TO NFRA_CLDGRPH.TO-CG-E-2 -- CG-s-18 (ADDED at decomposition v0.5 on the CTO's round-4 analysis @707ba2a4c9, PRD addendum v0.5 row S18): THE FOUR `:latest` PRODUCERS PINNED BY DIGEST -- `globgrph-comp-learns-producer`, `globgrph-cse-producer`, `globgrph-fedobs-producer`, `globgrph-resource-summaries-producer` reference the derive-runner image by its digest, applied through `safe-apply` under a NEVER-2 entry naming every family the act touches, read live by `describe-task-definition`: 7 of 7 ACTIVE globgrph families by DIGEST. No image is rebuilt. R13 (PRD v0.5 s.6) is the rule

<to_id>NFRA_CLDGRPH.TO-CG-E-2</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~1</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- GO = the spawn (spine v3 L7): slot ~1 on a fresh worktree from CLOUD at this issuance, with `.tools/terraform.exe` provisioned into it by the issuer (the binary is gitignored and ABSENT in every fresh worktree; the PATH substitute re-pins remote state). ROUND 5 of NFRA_CLDGRPH (the recut as ONE issuance on the CTO's round-4 analysis @707ba2a4c9 / msg 94509). Slot ~1's ONLY order this round. Marked HARD by the issuer (a live Terraform apply on four production task definitions and their launch targets; opus). PREMISE RE-GROUND at hand-off: `infra/aws/terraform/globgrph/serving.tf:22` carries `globgrph_image_digest = "sha256:1b89853f..."`; the four producer `.tf` files reference `opal-globgrph-derive-runner:latest`; `.tools/terraform.exe` is present in your worktree and `bash .tools/safe-apply.sh --help` resolves; if any fails, BLOCKING row + report. The assignee commits its own status flip after a VALID proof-of-spec instance whose mechanical rows ALL read PASS; a FAIL row leaves the order open as the final report; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.5 @`707ba2a4c9` (FWD-2, FWD-4; s.7 row S18; R13) · **Decomp cell:** `CG-s-18` (decomposition v0.5, this recut; the cell text inlined below) · **Lane:** `0.7.0_AE_CloudOps` -- the globgrph Terraform tree and the change-management ledger · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~1`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~1; export PATH="/c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312:$PATH";` (the bare `python` on this box is 3.14 without PyYAML; the commit gate imports yaml). Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~1 <0.9.0_WK_NFRA_CLDGRPH~1@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/`.** A path you need that the block lacks is a BLOCKING row on that criterion, never an override.
- **Scratch:** `<your worktree>/.scratch/` only.
- **Surprise = ONE ROW, never a message.** Append to `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` inside the fenced json array, per `org/surprise_channel/schemas/investigation_item.schema.json`; id `NFRA_CLDGRPH-W1-S<k>`, `<k>` the next unused within W1 (W1-S1..S26 exist at HEAD; start at S27); restate the header denominator line by parsing every fenced block (122 rows at this cut); never edit an existing row; keep working.
- **Every criterion invocation runs under `timeout 120`**; rc 124 IS the recorded output, retried once at most. Deliverable steps that are not criterion invocations (the apply, a polled read) may use `timeout 600` with bounded polling.
- **THE HALT GATE ADMITS YOU** (`.tools/halt-gate-check.sh` @68f22f74f5): a worker holding a NON-TERMINAL order under NFRA_CLDGRPH at HEAD is a real principal; `bash .tools/safe-apply.sh` resolves for you. rc=3 from it is a BLOCKING row quoting its whole output, never a retry with an escape.
- **NEVER:** `terraform apply` bare (use `bash .tools/safe-apply.sh`, read its header first, targeted on exactly the addresses you name); rebuild, push or re-tag any image (a pin is a task-definition revision, nothing else moves -- the cell's own bound); touch a family this order does not name; `aws ecs update-service` / `run-task` / `stop-task`; write the marker, the pointer or any `projection/` object; delete any S3 object; an alarm/monitor; non-ASCII in code/logs/AWS; `2>/dev/null` a read whose emptiness carries a verdict; bare `git commit`.
- **NEVER-2 (deploy ledger) BINDS:** `python .tools/deploy_ledger.py open ...` BEFORE the apply with the complete leg manifest; **AN IMAGE-PIN ACT NAMES IN THE ENTRY EVERY TASK FAMILY THAT PULLS THE TAG IT MOVES AWAY FROM -- all SEVEN globgrph families**, the four it moves and the three already pinned (CLAUDE.md NEVER-2 @b00a69a676: *a shared `:latest` reaches every family at once and no Terraform-plane control can see it*); close every leg with proof; close the entry. The sentinel `org/critical_paths/.open_deploys/<slug>.json` is TRACKED and in your PATHS block: commit it with the entry.
- **Search rail:** `python .tools/comp-read <file> --for "..."` / `--enumerate '<regex>'`; `python .tools/comp-find '<pattern>' <pathspec>`; raw recursive grep/find in Bash is refused; a `cmd | grep` receiver is free. AWS CLI = `.tools/aws` (CLI v1: no v2-only flags; `--output text` rows end in CR -- strip it before a shell field test). Region us-east-1, account 313476888478.

## THE CELL (decomposition v0.5, this recut, s.1a; PRD v0.5 s.7 row S18 verbatim in its accept)

> **CG-s-18** | S18 THE FOUR `:latest` PRODUCERS: `comp-learns-producer`, `cse-producer`, `fedobs-producer`, `resource-summaries-producer` still reference `opal-globgrph-derive-runner:latest` (S31's pins half; 3 of 7 families pinned by CG-s-15) | FWD-2, FWD-4 (acc 2, 4) | claim: measured (the four `.tf` files under `infra/aws/terraform/globgrph/` carry the tag on the DECLARED plane, the CTO's read; 3 of 7 pinned on the APPLIED plane by the CVO's `describe-task-definition`, C-S24) | status: OPEN -- ROUND 5 (recut) | lane `0.7.0_AE_CloudOps` | placement laptop | depends_on: CG-s-15 -> DONE (the image at digest sha256:1b89853f..., three families pinned @c5b54680a9) | **closes on (the PRD's accept, verbatim):** 7 of 7 ACTIVE globgrph families reference the image by DIGEST, read live by `describe-task-definition` after the apply, under a NEVER-2 entry naming every family the act touches; **R13** is the rule. **Bound:** no image is rebuilt by this row -- a pin is a task-definition revision and nothing else moves

**R13 (PRD v0.5 s.6, verbatim):** *"no globgrph task family references a mutable image tag; every image act's change-management entry names every family that pulls the tag it moves."*

## MEASURED BY THE ISSUER AT THE CUT (2026-09-09 ~15:3xZ, HEAD c82df8ce20), so you do not spend a discovery step on it

- **The declared plane** (`comp-find 'opal-globgrph-derive-runner:latest|image\s*=.*globgrph' infra/aws/terraform/globgrph`, 12 hits across 37 files): four task definitions still on the TAG -- `aws_ecs_task_definition.comp_learns_producer` (`comp_learns_producer.tf:72`, image at `:85`), `aws_ecs_task_definition.cse_producer` (`cse_producer.tf:121`, `:137`), `aws_ecs_task_definition.fedobs_producer` (`fedobs_producer.tf:56`, `:69`), `aws_ecs_task_definition.resource_summaries_producer` (`resource_summaries_producer.tf:142`, `:158`); three already on the DIGEST -- `derive_runner` (`item2a.tf:361`), `projection_worker` (`projection.tf:231`), `globgrph_serving` (`serving.tf:125`), all through `local.globgrph_image_digest` (`serving.tf:22`, `sha256:1b89853fe44133f10a60dc2b3e7b463c0d3b68b827a2ddff249bf427ecde2778`, the 2026-09-04T08:03:52Z build of HEAD 5644fee152 carrying the C-3 deriver fix). **The edit is the same shape the three pinned families use:** `image = "${local.account_id}.dkr.ecr.${local.region}.amazonaws.com/opal-globgrph-derive-runner@${local.globgrph_image_digest}"` -- one line in each of four files (plus the comment lines at `:11`, `:8`, `:10`, `:8` that still say `:latest`; correct them). **The digest is the fix's digest, the one the three pinned families already run**; the four producers move to the same bytes they have been pulling as `:latest` since 09-04 (C-S24 measured the applied plane), so the pin changes WHICH REFERENCE, not which bytes.
- **The launch targets that carry a task-definition ARN** (`comp-find 'task_definition_arn|aws_scheduler_schedule|aws_cloudwatch_event_target' infra/aws/terraform/globgrph`, 17 hits): `aws_cloudwatch_event_target.comp_learns_producer_nightly` (`comp_learns_producer.tf:154`, `task_definition_arn = aws_ecs_task_definition.comp_learns_producer.arn` at `:160`); `aws_scheduler_schedule.cse_producer_nightly` (`cse_producer.tf:215`, `:227`); `aws_cloudwatch_event_target.fedobs_producer_nightly` (`fedobs_producer.tf:140`, `:146`). **`resource_summaries_producer` has NO declared launcher in this tree** (only an output at `:186`); measure how it is launched (a Pipe, a schedule in another tree, or by hand) and record it -- a family with no declared launcher is a ROW (OBSERVATION), not a criterion's failure, and its "next launch" is whoever runs it. A task-definition edit produces a NEW REVISION; a target that references `.arn` follows the revision in the SAME apply (Terraform re-points it) -- so the apply set is the four task definitions PLUS every target that references their ARN, and **`-target` pulls dependencies**: state the address list the targeted plan actually carries.
- **The applied plane (the CVO's C-S24 read):** `describe-task-definition` on the ACTIVE revisions -- 3 of 7 by digest. Your E2-AC1 re-reads all seven after the apply; the four ecs families' names are `globgrph-comp-learns-producer`, `globgrph-cse-producer`, `globgrph-fedobs-producer`, `globgrph-resource-summaries-producer`; the three pinned are `globgrph-derive-runner`, `globgrph-projection-worker`, `globgrph-serving`. (`globgrph-nessie` and `globgrph-trino` are OTHER images, not this row's population; say so.)
- **The control that no image moved:** `.tools/aws ecr describe-images --repository-name opal-globgrph-derive-runner --image-ids imageTag=latest --query 'imageDetails[0].imageDigest' --output text` BEFORE and AFTER; equal.
- **The Terraform binary:** `.tools/terraform.exe` is provisioned into your worktree by the issuer at the spawn; verify `ls -la .tools/terraform.exe` and `bash .tools/safe-apply.sh --help` FIRST. A missing binary is a BLOCKING row, never a PATH substitute (v1.14.5 on PATH re-pins the remote state).
- **The plan-from-a-fresh-worktree trap** (memory): a "drift" seen from a fresh worktree on this autocrlf box can be a CRLF artifact -- hash the live bytes and both renderings before calling any foreign diff real; the unscoped plan is a CONTROL asserted BY ADDRESS LIST (the known foreign items: W1-S3's seven stale root outputs; W1-S2's task-definition replacements were D-1's and are now applied), never applied.

## DELIVERABLE -- in this order

1. **Open the ledger** (`cldgrph-cgs18-four-producers-digest-pin`, author your serial) with FIVE legs and ALL SEVEN families in its manifest (the four moved, the three already pinned, each with its ACTIVE revision before the act): L1 activation = the four Terraform edits committed on your branch (`terraform fmt -check` clean); L2 activation = `safe-apply` targeted on the address list the targeted plan carries (the four task definitions + their referencing targets), the plan's add/change/destroy line quoted, and the unscoped-plan control by address list; L3 verify = `describe-task-definition` on all seven families' ACTIVE revisions -> image by digest, with the digest equal to `local.globgrph_image_digest`; L4 verify = every declared launch target references the NEW revision (`list-targets-by-rule` / `get-schedule`), and `resource_summaries_producer`'s launcher recorded; L5 control = the ECR `:latest` digest unchanged before/after (no image moved). Write the entry's path to `ledger_entry_e2.txt` in your deliverables folder (E2-AC5 reads it).
2. **The edits:** one image line per file (four) + the four comment lines; `terraform fmt -check`; the targeted plan saved; the apply through `safe-apply.sh`; the unscoped plan control.
3. **The live reads** (L3, L4, L5) through the scripts below.
4. **The record** `CG-s-18.four-producers-digest-pin.result.md`: one fenced JSON block (per family: before revision/image, after revision/image; the address list applied; the plan lines; the launcher per family; the ECR digest before/after; the seven families named as R13 requires) then prose. Close the ledger (5 of 5). Then the proof instance, validate, and -- ONLY if every mechanical row is PASS -- flip and commit (instance, deliverables, the four `.tf` files, the ledger entry + its sentinel, the flip together).

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="E2-AC1" cell_refs="CG-s-18"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/families_pinned.sh</invocation><expect>PINNED_BY_DIGEST=7 of 7</expect></criterion>
`E2-AC1` -- SEVEN OF SEVEN ACTIVE globgrph FAMILIES REFERENCE THE IMAGE BY DIGEST, read live: `describe-task-definition` on each family's latest ACTIVE revision, `containerDefinitions[0].image` containing `@sha256:` (each family, revision and image printed; the script's denominator is the seven named families).

<criterion id="E2-AC2" cell_refs="CG-s-18"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/producers_digest_equal.sh</invocation><expect>DIGEST_MATCHES_LOCAL=4 of 4</expect></criterion>
`E2-AC2` -- THE FOUR PINS ARE THE FIX'S DIGEST: each producer's live image digest equals `local.globgrph_image_digest` as read from `infra/aws/terraform/globgrph/serving.tf` at your HEAD (a pin to some other digest would pass E2-AC1 and fail here).

<criterion id="E2-AC3" cell_refs="CG-s-18"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/targets_current.sh</invocation><expect>TARGETS_ON_PINNED_REVISION=([0-9]+) of \1 declared launcher\(s\)</expect></criterion>
`E2-AC3` -- EVERY DECLARED LAUNCHER POINTS AT THE PINNED REVISION: for each producer with a declared launch target (three at the cut), the target's `task_definition_arn` read live names the family's new ACTIVE revision; the denominator is the launchers FOUND, and a producer with no declared launcher is printed by name with how it is launched (a ROW, not a miss).

<criterion id="E2-AC4" cell_refs="CG-s-18"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/latest_unchanged.sh</invocation><expect>LATEST_DIGEST_UNCHANGED=true</expect></criterion>
`E2-AC4` -- NO IMAGE MOVED: the ECR `:latest` digest recorded BEFORE the first act (`latest_digest_before.txt`, written at step 1) equals the digest read now (the cell's bound: a pin is a revision, nothing else moves).

<criterion id="E2-AC5" cell_refs="CG-s-18"><invocation>grep -c '^\*\*Status:\*\* CLOSED' "$(cat org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/ledger_entry_e2.txt)"</invocation><expect>^1$</expect></criterion>
`E2-AC5` -- THE LEDGER ENTRY CLOSED, read from the entry's own Status line (`deploy_ledger.py list` cannot print CLOSED, row W2-S5), naming all seven families.

<criterion id="E2-AC6" cell_refs="CG-s-18"><invocation>.tools/terraform.exe fmt -check -diff infra/aws/terraform/globgrph/comp_learns_producer.tf infra/aws/terraform/globgrph/cse_producer.tf infra/aws/terraform/globgrph/fedobs_producer.tf infra/aws/terraform/globgrph/resource_summaries_producer.tf; echo FMT_RC=$?</invocation><expect>FMT_RC=0$</expect></criterion>
`E2-AC6` -- THE FOUR FILES ARE FORMATTED (the estate's Terraform hygiene gate, run with the provisioned binary, never a PATH substitute).

<criterion id="E2-AC7" cell_refs="CG-s-18" judgment="true"/> `E2-AC7` -- THE BLAST-RADIUS READING under R13: which families moved and which did not and why; what the targeted plan's address list carried beyond the four task definitions (dependencies `-target` pulled) and what the unscoped plan's foreign items were and why they were left; whether the change-management entry names every family that pulls the tag; and how `resource_summaries_producer` is launched. A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>E2-AC1, E2-AC2, E2-AC3, E2-AC4, E2-AC5, E2-AC6, E2-AC7</expected_criteria>

## SURFACES

The four producer `.tf` files (the ONE image line + one comment line each) · `infra/aws/terraform/globgrph/serving.tf` (READ: the digest local; `item2a.tf`, `projection.tf` READ: the pinned shape) · the D-1 record `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/CG-s-15.shared-image-digest-pins.result.md` (READ: how the three were pinned, the families table, the launch reads) · `.tools/safe-apply.sh` (READ its header; run) · `.tools/deploy_ledger.py` (run) · the ledger you open.

## BOUNDS

- **Four image lines and four comment lines in four files; nothing else in Terraform.** No variable, no module, no new resource.
- **`safe-apply` targeted on the measured address list; the unscoped plan is a control, never applied.**
- **No image act, no service update, no task run.** The next scheduled launch of each producer is the acceptance the L9 seat reads later; you do not provoke one.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
infra/aws/terraform/globgrph/comp_learns_producer.tf
infra/aws/terraform/globgrph/cse_producer.tf
infra/aws/terraform/globgrph/fedobs_producer.tf
infra/aws/terraform/globgrph/resource_summaries_producer.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-E-2.four-latest-producers-pinned.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.5 (this recut), cell CG-s-18 (s.1a; ADDED on the CTO's round-4 analysis @707ba2a4c9, PRD addendum v0.5 row S18, over rows NFRA_CLDGRPH-S31 and W1-S8).
<owned_cells>CG-s-18</owned_cells>
Read-dependencies, NOT claimed: CG-s-15 (DONE; the digest and the three pins). Siblings this round, NOT yours: CG-s-17 (slot ~2), CG-s-19 -> CG-s-20 (slot ~3).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-09 15:3xZ at this recut: GATES ARMED 25 across 5 carriers (C1 23 -> 7, C2 6 open deploy-ledger entries -> 6, C3 12, C4 20, C5 335); NEEDS-READ 137 prose fields; this order opens a SEVENTH ledger entry and closes it in the same order; the C3 moratoria bind BOUNDS.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or grant is read or changed; the four task roles and execution roles are untouched (a task-definition revision reuses them). Run `python .tools/comp-iam refresh-census` before any APPLIED census read if one is needed (24 h TTL).
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5, 22/22 cited commits VERIFIED; v0.5's rows cited at @707ba2a4c9); the deliverable's validator context is the L9 seat's compose.
comp-blast: DECLARED-NOT-APPLICABLE AT THE CUT -- the blast radius is the seven families named by the row and re-read live by E2-AC1; a graph read would answer the DECLARED plane the CTO already measured.
</preflight>

<proof_of_spec>
Criterion ids minted at the recut by the issuer: `E2-AC1`..`E2-AC7`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/NFRA_CLDGRPH.TO-CG-E-2.four-latest-producers-pinned.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> E2-AC1,E2-AC2,E2-AC3,E2-AC4,E2-AC5,E2-AC6,E2-AC7` (from the worktree root) BEFORE the complete flip; the flip requires rc 0 AND every mechanical row PASS -- a FAIL row leaves the order open and is your final report. `E2-AC2` (the digest equality) and `E2-AC4` (no image moved) are the controls that must be able to FAIL. `E2-AC7` is `judgment="true"`: recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.**
</proof_of_spec>

<compiler_tools_mandate>
BEFORE EDIT: `python .tools/comp-read infra/aws/terraform/globgrph/serving.tf --for "the globgrph_image_digest local and every resource that references it"`; `python .tools/comp-read infra/aws/terraform/globgrph/cse_producer.tf --for "the task definition's image line and the scheduler target that references its ARN"`. BEFORE COMMIT: `.tools/terraform.exe fmt -check` on the four files (E2-AC6); no `.py` is edited by this order.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the spawn (the COO spawns this slot on a fresh worktree from CLOUD at this issuance, with the Terraform binary provisioned).**
