# NFRA_OPLGTW task order -- `OG-tf-1` -- the opal-gateway terraform root plans from a FRESH worktree, and the fix moves nothing live

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-tf-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~17</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- terraform source and repository hygiene; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM resource is added or changed; the targeted plan of the grant-writer role and policy must read No changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the acceptance is the CTO's (analysis round 12 s.5 item 3).
EGRESS CLASS, declared: Opal's own AWS (state backend and provider reads) plus the Terraform provider registry for `terraform init`, inside Andrew's development-egress word for ~O-fabric workers (2026-09-28 ~21:2xZ Call 2).
</preflight>

## 1. THE CELL -- `OG-tf-1` (decomposition addendum R3-T.7, item 3)

`infra/aws/terraform/opal-gateway` does not plan from a fresh linked worktree (rows NFRA_MCPINDEX-Z-W21-S19 and
ETFS_RIVALS-Z-W5-S3). Measured at the cut (`r13/checks/tf.AC1.sh`): plan rc 1, 2 errors, both "No value for required
variable" -- `mcportal_owner_key_claim` and `mcportal_owner_key` (`mcportal_grant_writer.tf:142,151`, no default). Behind
them, from the root's own text: `data "archive_file" "mcportal_grant_writer"` (:39-43) reads the gitignored
`../../lambda/mcportal/mcportal-grant-writer-lambda/.build/staged`, and `aws_lambda_layer_version.mcportal_grant_writer_deps`
(:49-56) hashes the gitignored `../../lambda/layers/mcportal-grant-writer-deps/.build/mcportal-grant-writer-deps.zip`.
The three `gateway/*` secrets that also broke it now exist (OG-pr-1). Until now each targeted plan was fed by hand
(OG-pr-1 A1: `TF_VAR_*` from the live Lambda, `build_package.py`, the layer zip copied from the main tree).

1. Make the COMMITTED root plan with zero errors from a fresh worktree with no `TF_VAR_*` set and no copied or built
   artifact. Choose the smallest mechanism that does this WITHOUT changing a live resource, and write your choice and
   the alternatives you rejected in `deliverables/0.9.0_WK_NFRA_OPLGTW~17/TF_ROOT_FIX.md` first. Constraints: no secret
   or personal identifier committed (the owner key is one; read it from where it already lives, never a literal);
   no `terraform apply`, no state command, no import, no `removed`/`moved` block that changes what the state manages.
2. Hygiene: untrack the saved plans (`tfplan`, `tfplan.r8`, `.build/alert-channels.tfplan`, `.build/otp-liveness.tfplan`)
   and the stray `org/mcp/agent_telemetry/*.jsonl` inside the root; add ignore lines in `infra/aws/terraform/opal-gateway/.gitignore` so plans cannot be re-committed.
3. Record the untargeted plan's summary from the fresh worktree (drift is reported, not fixed: e.g. the AMI data
   source). If the only route needs an apply or a state change, STOP with a BLOCKING row naming it.
4. **Row Z-W15-S25, which bears on AC2.**
   - OG-rl-3's untargeted plan (2026-10-02, from a fresh worktree with a staged grant-writer build) showed
     `aws_lambda_function.mcportal_grant_writer` `source_code_hash` changing, and nothing else on that resource.
   - BEFORE choosing your fix, classify that diff by CONTENT, per CLAUDE.md rule 22a:
     - list the deployed function's code by per-file sha256: `get-function`'s code location, read in memory, never
       written to the repo;
     - compare it with the build input your fix will archive.
   - Record SAME-CONTENT (hash-only: zip metadata or ordering) or CONTENT-DIFF (the files that differ) in
     `TF_ROOT_FIX.md`.
   - SAME-CONTENT: make the archive deterministic so the targeted plan reads No changes.
   - CONTENT-DIFF: do NOT apply. STOP with a BLOCKING row naming the differing files (disarm_owner `2.0.0_SA_COO~O`),
     because AC2 cannot pass without an apply this cell may not make.
5. Report the closing commit hash: the issuer passes it to `0.0.0_AB_MSTR~Z` for the routing register.

## 2. BOUNDS

Terraform source and its `.gitignore` under `infra/aws/terraform/opal-gateway/` only. No apply, no plan saved to the
repo, no state change, no deploy. Never print a variable value. Never push, merge, rebase, stash, `checkout --` or
`clean`; never override a gate. Commit with `.tools/safe-commit.sh`.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~17/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W17-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-tf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/tf.AC1.sh; echo "exit=$?"</invocation><expect>(?s)plan rc=[02]; errors 0; missing required variables 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-tf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/tf.AC2.sh; echo "exit=$?"</invocation><expect>(?s)targeted grant-writer plan reads No changes: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-tf-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/tf.AC3.sh; echo "exit=$?"</invocation><expect>(?s)saved plans 0; stray org/ files 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a fresh worktree of HEAD plans the committed root with zero errors and no missing variable.
- `AC2`: the fix changes nothing live (targeted grant-writer plan: No changes).
- `AC3`: no saved plan and no stray telemetry tracked in the root.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~17/NFRA_OPLGTW.TO-OG-tf-1.tf-root-fresh-worktree.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`; if all PASS, append a `complete` status tag after the
order's last status line in the same commit. Report once: the mechanism, the untargeted plan summary, the literal AC
output, the closing commit.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 14 (addendum R3-T.7, item 3), plus row Z-W15-S25 (analysis round 13 s.4 item 3). Pre-cut at the round-13 cut: `tf.AC1` FAIL (rc 1, 2 errors, 2 missing variables), `tf.AC3` FAIL
  (4 saved plans, 3 stray files). The checks' fresh worktree is a SPARSE cone (`infra/aws`, `org/standards`, `lib`;
  disk at limit, `0.0.0_AB_MSTR~Z` msg 28166): the root is complete, never a pruned copy. Owed: the closing hash to `0.0.0_AB_MSTR~Z` (register row W5-S3; COO~O msg to MSTR, RE 28077).

<status>pending</status>
<round>14</round>
<slot>~17</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
