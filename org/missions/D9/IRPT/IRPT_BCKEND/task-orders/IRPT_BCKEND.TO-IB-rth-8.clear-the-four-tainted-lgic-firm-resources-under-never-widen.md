# TO IRPT_BCKEND.TO-IB-rth-8 -- CLEAR THE FOUR TAINTED `lgic_firm` RESOURCES UNDER NEVER-WIDEN: `IB-rth-7`'s worker measured real drift, exactly the contingency its own order anticipated -- a fresh Terraform plan on `shared-infra` reads `4 to add, 0 to change, 4 to destroy` (NOT `0/0/0`), naming `aws_s3_bucket_policy.lgic_firm["inflection"/"cottonwood"]` and `aws_s3_bucket_versioning.lgic_firm[same]` as TAINTED, leftover from the 2026-09-18 half-landed apply (row W3-S45). The live bucket policy is already correct (CRO's console PUT, msg 99124) and both buckets are empty (0 keys) -- but a policy-resource replace is a destroy-then-create, and this project's own doctrine (`IB-rtf-5`'s task order) names exactly this ordering hazard. CTO+COO halves sign BEFORE any apply.

<to_id>IRPT_BCKEND.TO-IB-rth-8</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~8</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 8 (mid-round addition) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` (no addendum) | **Decomp cell:** `IB-rth-8` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.12, s.R8.9) | **outcome_ref:** FWD-11 (the bucket program) | **Prior context:** `IB-rth-7`'s result @`cabb11ced3` (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~7/reconcile-terraform-state-against-the-recovered-bucket-policy.result.md`), row `IRPT_BCKEND-W7-S2`, `IB-rtf-5`'s own task order (the proven packet shape for this exact resource family)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~8`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~8;`.
- **Worktree:** the issuer creates `/c/tmp/wk-irpt-8-8` on branch `wk-irpt_bckend-8-8`, cut from CLOUD HEAD AFTER this order's own commit lands (learn from `IB-rth-7`'s first attempt: the issuer verifies this file is present in the worktree BEFORE spawning), `.tools/terraform.exe` provisioned there. First act: `cd /c/tmp/wk-irpt-8-8`, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN CONFIRM THIS FILE ITSELF IS PRESENT (`test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rth-8.clear-the-four-tainted-lgic-firm-resources-under-never-widen.md`) -- if absent, STOP and file a row exactly as row `IRPT_BCKEND-W7-S1` did, never proceed on content read from outside the worktree; write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing `/c/tmp/wk-irpt-8-8/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~8 <0.9.0_WK_IRPT_BCKEND~8@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`. Capture `safe-commit.sh` output to a file, never `| tail`, never with `$( )`.
- Python `py -3.12`; AWS via `.tools/aws`; a recursive grep/find is rail-DENIED -- use Read/Grep tools, a gated read in its own call.

## THE CELL

- **(a) MEASURE THE REPLACE SEMANTICS FIRST, before writing anything.** Re-confirm the current state
  independently (do not trust this face's restatement): fresh `terraform plan -input=false -no-color
  -refresh=true -json` on `infra/aws/terraform/shared-infra` (init with the vendored binary first), parse
  the JSON plan for the four named resources' `actions` arrays and any `resource_drift` entries -- print
  each resource's exact planned action sequence (e.g. `["delete","create"]` vs a true in-place replace).
  For `aws_s3_bucket_policy`: does the AWS provider's destroy actually call `DeleteBucketPolicy` (removing
  every Deny) before the create's `PutBucketPolicy` restores the fence -- read the provider source or
  docs if the plan JSON alone does not settle it, and state your confidence. For `aws_s3_bucket_versioning`:
  AWS has no "delete versioning" API -- versioning is binary Enabled/Suspended for the life of a bucket, so
  determine what the provider's destroy step actually does against a live bucket (a no-op reconciliation,
  a Suspend call, or something else) -- do not assume either way. Also independently re-confirm: `get-bucket-policy`
  on both buckets matches the CRO's rendered policy (msg 99124), `list-objects-v2` 0 keys both, applying
  identity's ARN is 1 of 3 exempted in `exemptions.json`.

- **(b) THE PACKET.** Write the never-widen packet naming: the EXACT blast radius (only these four
  resources, both firms, nothing else in the plan); the MEASURED window from arm (a) in plain terms (does
  the bucket sit with NO explicit Deny for some interval during the apply, and for how the provider
  sequences it -- per-resource or all four in one batch); the consequence of that window given both
  buckets hold 0 keys (no data exposure possible, but state plainly that this is a compliance/security
  state regardless of whether data exists); rollback (re-apply the fence policy immediately via a fresh
  `safe-apply.sh` run if anything reads wrong post-replace -- no data can have been lost since none exists).
  Commit the packet. Both never-widen halves (CTO + COO) must SIGN at HEAD naming this packet's blob
  BEFORE arm (c) runs. **If you cannot get both halves this pass, that is an honest STOP** -- exactly
  `IB-rtf-5`'s own precedent: commit the packet, leave the order open, report exactly what's owed. Do NOT
  proceed to arm (c) without both signatures at HEAD.

- **(c) THE APPLY, ONLY once both halves are signed at HEAD, under a change-management ledger update**
  (this reuses `IB-rte-3`'s existing OPEN ledger entry -- do not open a new one; update its Log with this
  act). `.tools/safe-apply.sh` only, never bare `terraform apply`. The plan immediately before applying
  must show EXACTLY the four named resources changing and nothing else -- any other resource in the plan,
  or `demo`/`49financial` appearing, is a STOP, no apply runs. Immediately after: `get-bucket-policy` both
  buckets, verbatim-matching the CRO's already-live policy (sha256 compared); `list-objects-v2` 0 keys
  both, re-measured (never carried from arm (a)); `get-bucket-versioning` Enabled both; a fresh re-plan
  reads `0 to add / 0 to change / 0 to destroy`; `terraform state list` shows no tainted resource. Close
  ledger legs L1 and L3 in `org/critical_paths/change_management/20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md`
  with the apply output + resource list (L1) and the plan output (L3) as proof, committed. Disarm row
  `IRPT_BCKEND-W7-S2` by citation (a new row, per this file's own established pattern -- BLOCKING/
  INVESTIGATION-class rows are never mutated in place). Leg L4 stays exactly as `IB-rth-7` left it
  (UNEXERCISED, host stopped) -- not this cell's to force.

## DELIVERABLE
The plan-JSON measurement from arm (a); the never-widen packet + both signed halves; the apply output,
post-apply verification reads, and closed ledger legs L1/L3 (arm c); the disarm row for `IRPT_BCKEND-W7-S2`.

## BOUNDS
- No resource outside the four named is ever planned or applied; `-target` never; a plan naming any other
  resource, or `demo`/`49financial`, is a STOP.
- No change to `fence_patterns()`, `exemptions.json`, or `scopes.json`.
- The host is never started by this cell; leg L4 is not this cell's to close.
- No `terraform state` verb beyond a read (`list`, `show`) for verification.
- Both halves at HEAD BEFORE the apply, or the apply does not run -- an honest STOP with the packet
  committed is a complete and correct outcome of this cell if sign-off is not obtained same-pass.
- The forward-looking-criterion bar; R-40 (content hash per run/artifact read AT the event); S56 vintage
  pins `path:line @ <commit-ish>`.
- **Surprises:** one row per failed premise / wrong path / absent capability at
  `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W8-S<k>` starting at 1 (append
  as a new fenced JSON block matching this file's established practice, PREVAILING EOL [CRLF], UTF-8
  explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED, `grounding` + `disposition`
  both REQUIRED per the schema); validate every fence still parses before committing; then keep working.
  Never edit this face, never widen the order.

<expected_criteria>R85-AC1, R85-AC2, R85-AC3</expected_criteria>
<criterion id="R85-AC1" cell_refs="IB-rth-8"><invocation>timeout 900 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~8/battery_ib_rth_8.py --arm measure</invocation><expect>IBR85-REPLACE-SEMANTICS-MEASURED-PACKET-WRITTEN</expect></criterion>
**`R85-AC1` -- PASSES BY OUTPUT:** arm (a)'s per-resource action sequence printed for all 4 resources,
policy/keys/identity preconditions confirmed 3 of 3; arm (b)'s packet committed. Token prints once the
packet is committed, regardless of whether sign-off is obtained same-pass -- this criterion covers
MEASUREMENT + PACKET, not the apply.

<criterion id="R85-AC2" cell_refs="IB-rth-8"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~8/battery_ib_rth_8.py --arm apply</invocation><expect>IBR85-FOUR-RESOURCES-CLEARED-LEGS-L1-L3-CLOSED</expect></criterion>
**`R85-AC2` -- GATED ON BOTH HALVES AT HEAD.** No halves signed -> this arm is NOT run, no token, order
stays open on R85-AC1 alone (an honest partial-complete, matching `IB-rtf-5`'s precedent). Both halves
signed -> apply runs, post-apply reads all clean, re-plan `0/0/0`, ledger legs L1+L3 closed, row disarmed
-> token prints, PASS. Anything else in the pre-apply plan, or any post-apply read failing -> FAIL, a
BLOCKING row, no `<status>` flip.

<criterion id="R85-AC3" cell_refs="IB-rth-8" judgment="true"/>
**`R85-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: given the measured
replace semantics from arm (a), was the disclosed window (if any) acceptable given both buckets held 0
keys throughout, or should this class of taint-clear require a different remedy (e.g. `terraform import`
instead of replace) in future. No verdict from the worker.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rth-8.clear-the-four-tainted-lgic-firm-resources-under-never-widen.md
infra/aws/terraform/shared-infra/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.12, cell `IB-rth-8` (s.R8.9).
<owned_cells>IB-rth-8</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: RUN at the hand-off by the issuer -- 3 of 3 operator identities in exemptions.json confirmed as the only principals the fence admits besides the firm's own role pattern; DENOMINATOR: 1 Terraform root (shared-infra) not yet re-planned at hand-off -- BLIND to the exact per-resource action sequence until arm (a) runs, which is this cell's own first job.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R85-AC1, R85-AC2, R85-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~8/IRPT_BCKEND.TO-IB-rth-8.clear-the-four-tainted-lgic-firm-resources-under-never-widen.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim`,
`invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content
hash per produced/served artifact pinned to its commit; the judgment row under `UNVERIFIABLE-BY-INSTRUMENT`
naming `3.0.0_SA_CVO`. Validate `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this
face path>`; rc 0 AND R85-AC2 PASS-by-output, then flip `<status>` to `complete` and commit instance + flip
together. If only R85-AC1 passed (packet committed, sign-off not yet obtained), the order stays OPEN and
that partial state IS the correct final report -- do not fabricate a completion.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its
deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything
you could not do and why, and explicitly: were both halves obtained this pass, or is the order stopping
on the packet alone awaiting sign-off).
