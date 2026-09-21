# TO IRPT_BCKEND.TO-IB-rth-7 -- RECONCILE TERRAFORM STATE AGAINST THE MANUALLY-RECOVERED BUCKET POLICY: `4.0.0_SA_CRO` recovered `opal-data-inflection`/`opal-data-cottonwood` access by a console break-glass IAM-role PUT (msg 99124, @a0097b1ef4), bypassing Terraform entirely -- the live bucket policy now (probably) matches what `s3-lgic-firm-buckets.tf` renders, but Terraform's own STATE never saw the apply and the deploy ledger (`org/critical_paths/change_management/20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md`) has three legs (L1, L3, L4) still OPEN. This cell VERIFIES the reconciliation; it does not create anything and applies nothing unless a plan shows genuine drift, in which case it STOPS and carries the finding rather than resolving it ad hoc.

<to_id>IRPT_BCKEND.TO-IB-rth-7</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~7</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending -- RE-HANDED by 2.0.0_SA_COO~B 2026-09-21 ~18:2xZ on worktree wk-irpt_bckend-8-7b (issuer's own sequencing error on the FIRST hand-off: that worktree, wk-irpt_bckend-8-7, was cut from CLOUD@93790c036e BEFORE this order's own commit (@7427e805de) landed, so the worker correctly found this file absent and STOPPED honestly -- row IRPT_BCKEND-W7-S1, drained clean @9779e226e0, disarmed by this re-hand). Originally HANDED 2026-09-21 ~18:0xZ (round 8, mid-round addition v0.11, s.R8.8), superseding IB-rth-6 (closed superseded s.R8.7) on 4.0.0_SA_CRO msg 99124 (@a0097b1ef4) and 1.0.0_SA_CTO msg 99128. VERIFY-CLASS: no apply unless arm (a) finds drift, and even then only under a fresh never-widen packet -- never in this cell.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 8 (mid-round addition) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` (no addendum) | **Decomp cell:** `IB-rth-7` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.11, s.R8.8) | **outcome_ref:** FWD-11 (the bucket program) | **Prior context:** `IB-rte-3`'s ledger, `IB-rtf-5` (round 6, superseded/parked -- read for the FULL original mechanism this cell is now verifying converged, never re-executed), CRO msg 99124, CTO msg 99128

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~7`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~7;`.
- **Worktree:** `/c/tmp/wk-irpt-8-7b` on branch `wk-irpt_bckend-8-7b`, cut from CLOUD HEAD @`9779e226e0` by the issuer (a re-cut -- the first worktree, `wk-irpt-8-7`, was cut before this order's own commit landed and is removed), `.tools/terraform.exe` already provisioned there. First act: `cd /c/tmp/wk-irpt-8-7b`, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN CONFIRM THIS FILE ITSELF IS PRESENT AT THAT PATH before anything else (`test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rth-7.reconcile-terraform-state-against-the-recovered-bucket-policy.md`) -- if absent, STOP and file a row exactly as row `IRPT_BCKEND-W7-S1` did, never proceed on content read from outside the worktree; write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing `/c/tmp/wk-irpt-8-7b/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~7 <0.9.0_WK_IRPT_BCKEND~7@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`. Capture `safe-commit.sh` output to a file, never `| tail`, never with `$( )`.
- Python `py -3.12`; AWS via `.tools/aws`; a recursive grep/find is rail-DENIED -- use Read/Grep tools, a gated read in its own call.

## THE CELL

- **(a) THE PLAN -- leg L3.** Locate the Terraform root managing these buckets (`infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` -- confirm the root path, do not assume). `init` with the vendored binary (every provider cache was purged estate-wide -- init every root you plan). Run a plan WITH refresh, no `-target`. Read the result for `aws_s3_bucket_policy.lgic_firm["inflection"]` and `["cottonwood"]` (or however the resource is keyed) specifically, and for the rest of the root generally.
  - **`0 to add / 0 to change / 0 to destroy`, printed in full** -> the manual PUT converged exactly with what Terraform would render. Record this as the discriminating evidence for leg L3's closure.
  - **ANY drift** -> STOP. Print the diff verbatim. Do NOT `apply` to force convergence, do NOT hand-edit state, do NOT treat this as your own error to silently patch. File a BLOCKING row with the diff and what it implies (did the CRO's manual PUT differ from the renderer's current output? has the registry changed since 99124's apply? something else?). This is a carry to the COO, not a fix landed by this cell.
  - Also check: does the plan show TAINTED resources for `versioning`/`bucket_policy` on either firm, left over from the original 2026-09-18 half-landed apply (W3-S45)? If so, that is itself drift and falls under the STOP branch above.

- **(b) THE NEGATIVE CONTROL -- leg L4.** `describe-instances` on host `i-02448edb624a7a7cf`, print its state.
  - RUNNING: from the host, via read-only SSM, exercise: the host role's attempt to write `opal-data-inflection/irpt/inflection/gold/directory/zz-negative-control`, and the 49f principal's attempt to read `opal-data-cottonwood/irpt/cottonwood/gold/directory/` -- both must be DENIED, 2 of 2. Print the SSM command id and the verbatim AccessDenied error for each. If either is NOT denied, that is a FAIL and a BLOCKING row -- the fence is not actually live and no grant widened by this cell.
  - STOPPED: do NOT start it (another owner's resource, an EC2 state change outside this cell's grant). Record the control UNEXERCISED under its own criterion (`R83-AC2`, non-verdict status, host state + reason + owner named) -- never a FAIL for a control nobody ran, following `IB-rtf-5`'s own `R62-AC3` precedent exactly.
  - `simulate-principal-policy` is NEVER a substitute (this estate's own catalogue records it returning FALSE ALLOW).

- **(c) LEG L1 -- STATE THE JUDGMENT QUESTION, do not rule it.** L1's proof requirement was "apply output + resource list" from an actual `safe-apply.sh` run; none ran here (the CRO's fix was a direct role-level `put-bucket-policy`, not a Terraform apply). Write, for the CVO's `R83-AC3` judgment row: does a clean 0-change plan (arm a) mean L1 is satisfied BY CONVERGENCE, or does closing L1 properly require an actual (no-op) `safe-apply.sh` run so the state file itself reflects reality, e.g. via `terraform import` of the two policy resources or a deliberate no-op apply? State both readings' consequences (what breaks later if state is never reconciled -- the next real plan on this root, a future `terraform destroy` scoping, etc.) and your own read, but do not flip anything to `complete` on your own say.

- **(d) THE FENCE-PATTERN FINDING -- row `IRPT_BCKEND-S116`, carried not re-derived.** Measure, do not assume: does ANY IAM role this project's own Lambdas/pipelines actually hold (search this estate's Terraform for `aws_iam_role` resources with a name matching `*inf-*` or `*cot-*` that are NOT already `opal-inf-*`/`opal-cot-*`/`bd-cot-*` shaped) need write/read access to `opal-data-inflection`/`opal-data-cottonwood` going forward? Print what you find, denominator included. Report to the COO; do NOT edit `fence_patterns()` in `s3-lgic-firm-buckets.tf` -- that function is a shared-infra module outside this project's lane, and a fix there is a carry, never landed by this cell.

## DELIVERABLE
The plan output (full, both resources named); the ledger's L3/L4 rows closed (or left OPEN with a filed BLOCKING row and reason, if arm (a) or (b) found a real problem); the L1 judgment write-up for the CVO; the S116 measurement.

## BOUNDS
- **VERIFY ONLY.** No `terraform apply`, no `terraform import`, no state mutation of any kind, regardless of what arm (a) finds -- a STOP with a filed row is the only response to drift, never a same-cell fix.
- No change to `fence_patterns()`, any other firm's bucket policy, any IAM role or user (the CRO's break-glass roles stay as-is -- deletable later once L3 reads clean, not this cell's to touch).
- The host is never started by this cell.
- No object written to either bucket (the negative-control writes are DENIED attempts by construction -- if one unexpectedly succeeds, that is itself the FAIL condition in arm (b), not a green light to continue).
- The forward-looking-criterion bar; R-40 (content hash per run/artifact read AT the event); S56 vintage pins `path:line @ <commit-ish>`.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W7-S<k>` starting at 1 (append INSIDE the first fence's array or as a new fenced block matching this file's established practice, PREVAILING EOL [CRLF], UTF-8 explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); then keep working. Never edit this face, never widen the order.

<expected_criteria>R83-AC1, R83-AC2, R83-AC3</expected_criteria>
<criterion id="R83-AC1" cell_refs="IB-rth-7"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~7/battery_ib_rth_7.py</invocation><expect>IBR83-PLAN-CONVERGED-LEDGER-LEGS-DISPOSITIONED</expect></criterion>
**`R83-AC1` -- PASSES BY OUTPUT:** arm (a)'s plan reads `0/0/0` on the `lgic_firm` policy resources (printed) AND leg L3 closed in the ledger with that evidence; OR arm (a) found drift, in which case NO token prints, a BLOCKING row is filed, and the order stays open with the diff as the final report. The battery re-derives the plan fresh each run, never caches a prior read.

<criterion id="R83-AC2" cell_refs="IB-rth-7"><invocation>timeout 900 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~7/battery_ib_rth_7.py --arm b</invocation><expect>IBR83-NEGATIVE-CONTROL-DENIED-2-OF-2</expect></criterion>
**`R83-AC2` -- GRADED ON ITS OWN VOCABULARY (matching `IB-rtf-5`'s `R62-AC3`):** host RUNNING -> 2 of 2 DENIED -> PASS, token prints; host RUNNING and anything NOT denied -> FAIL, BLOCKING row; host STOPPED -> UNEXERCISED, non-verdict status recorded with host state + reason + owner, no token, neither PASS nor FAIL.

<criterion id="R83-AC3" cell_refs="IB-rth-7" judgment="true"/>
**`R83-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether ledger leg L1 should close on plan-convergence alone or needs an actual (no-op) apply to reconcile state; what row S116's measurement found and whether it warrants a carry to the shared-infra module owner. No verdict from the worker. Every line citation carries `@<commit-ish>`.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rth-7.reconcile-terraform-state-against-the-recovered-bucket-policy.md
infra/aws/terraform/shared-infra/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.11, cell `IB-rth-7` (s.R8.8).
<owned_cells>IB-rth-7</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: RUN at the hand-off by the issuer -- 3 of 3 operator identities in exemptions.json confirmed as the only principals the fence admits besides the firm's own role pattern; DENOMINATOR: 2 registry rows read (opal-data-inflection, opal-data-cottonwood), 1 Terraform file (s3-lgic-firm-buckets.tf) not yet re-read at hand-off -- BLIND to any drift between the registry and the live-applied policy until arm (a)'s own plan runs, which is exactly this cell's job. Live plane per arm (a)'s plan + arm (b)'s host control.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R83-AC1, R83-AC2, R83-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~7/IRPT_BCKEND.TO-IB-rth-7.reconcile-terraform-state-against-the-recovered-bucket-policy.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hash per produced/served artifact pinned to its commit; the judgment row under `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Validate `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>`; rc 0 AND R83-AC1 PASS-by-output, then flip `<status>` to `complete` and commit instance + flip together. A STOP (drift found, halves needed) leaves the order open with the BLOCKING row as the final report.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
