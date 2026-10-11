# NFRA_OPLGTW task order -- `OG-ap-6` -- APPLY: the E2 `.xlsx` gateway release (OG-rl-16 Phase B), re-cut on the live ref

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-6</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-6</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- host queue: MX-r-9 CLOSED 22:19Z (COO~MI msg 33030), MP-r-2 CLOSED 23:12:37Z (COO~MP msg 33064), live ref 2a5966dfbd; THIS release is next and the only one in flight. Phase B2 window 11:00Z-23:00Z. No cron, alarm or monitor is created.
comp-iam: RUN-BY-ISSUER -- ONE new inline policy, `aws_iam_role_policy.advi_billing_gateway_put` on `opal-gateway-role`: s3:PutObject on `opal-data-assets/smartx/49financial/bronze/fee_statement/*` only (CTO half read it live: 21 inline policies, none an advi-billing put). Applied in Phase B2 under its own ledger, never in B1.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the three signed halves over org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~51/ANNOUNCE_OG-rl-16.md (release a88661b145): CTO org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_OPLGTW_OG_RL16_E2_XLSX_RELEASE_20261009_Z.md @5e258448d2, COO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-rl-16_20261009.md @153e507b79, CVO @9b6003cd3b; CTO C1 requires the three halves re-pinned at the re-cut sha before B2.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-6` (decomposition addendum R3-T.41)

Re-cut dell2's E2 tool (`copy_site_file_to_s3`, `.xlsx` -> bronze `fee_statement` ONLY) onto the gateway's live ref, then
deploy it: first the one PutObject policy, then the gateway. READ the ANNOUNCE and all three halves first; they BIND,
especially CTO C1 (a new sha is a new pair), C2 (env keys), C3 (policy first, whole-root plan) and the COO half's re-cut
condition. Two phases. B1 runs now. B2 runs only on the issuer's GO.

### PHASE B1 (now) -- re-cut, prove it, read the plan; NO AWS write

1. **The live ref.** Read the host's shipped-file md5s through one SSM read, reusing
   `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~51/rl16_md5_host.py` copied to `W/ap6_md5_host.py`.
   Compare them with the shipped files of `2a5966dfbd89be9fe6cc0ef3566831e502b81d42` (MP-r-2's deployed commit,
   on branch `rel-nfra-mcportal-cp2-v2`). The host is a SUPERSET of the artifact: row NFRA_MCPINDEX-Z-S94 names 2 orphaned
   mcportal dashboard assets, `dashboard/assets/index-BP6X9XJd.js` and `index-BqfQgt7G.css`. List every extra by name. Any
   shipped file whose md5 differs, or any extra not named in this step, is a STOP.
2. **Re-cut.** Create a worktree at `C:/tmp/og-rel16c` on a new branch `rel-nfra-oplgtw-r16c`, at `2a5966dfbd`.
   Cherry-pick, in order, the signed release's three commits `e698b10bdc`, `e581384925`, `a88661b145`. The issuer
   dry-applied their combined diff onto this base, and it lands clean: 11 files, +531 -2. Any conflict is a STOP.
   The release commits take the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` (OG-tl-1 A1 precedent), on those
   three commits only. Write `W/ap6_release.json` = `{"base_sha", "release_sha"}`, both as full shas, and commit it on box/sitez.
3. Run E2's suites in the release tree: `test_advi_site_to_s3.py`, `test_advi_site_to_s3_registration.py`,
   `test_og_ab1_carry.py`. Record the output in `W/ap6_tests.out`.
4. **The policy plan, read only.** Run a whole-root `terraform plan` of `infra/aws/terraform/opal-gateway`
   from the release worktree (plan is not gated; never apply here) and save it to `W/ap6_plan.txt`. CTO C3 expects exactly
   `1 to add, 0 to change, 0 to destroy` for `aws_iam_role_policy.advi_billing_gateway_put`. Row Z-W39-S5 records an
   unrelated `mcportal_grant_writer` `source_code_hash` drift in this root. List every planned row by address. Any
   row beyond the one add goes in your report verbatim. It is a STOP for B2, not for B1.
5. Run AC1, commit, REPORT, STOP.
5b. **(A1) The policy plan at box/sitez HEAD, read only.** Step 4's plan read a TF root that is stale against the live
   estate (row Z-S81). Create a DETACHED worktree `C:/tmp/og-tf-e2` at box/sitez HEAD; make no commits there. Check
   that `git rev-parse HEAD:infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf` = `49c420acbce7cfb99c8726f5439b3f2cc6ea9f5a`,
   the signed release's blob. Run the same whole-root plan from that worktree, with step 4's secret and artifact handling
   (TF_VAR_ env only, values redacted), and save it to `W/ap6_plan_head.txt`. List every row by address, and report it
   verbatim.

### PHASE B2 (only on the issuer's GO, which names the three halves re-pinned at `release_sha` and MP-r-2's drain into box/sitez)

6. **Policy act** (CTO C3). Ledger `nfra-oplgtw-e2-put-policy`, entry AND sentinel committed before the act. Run
   `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply` FROM `C:/tmp/og-tf-e2` (A1), on the plan
   step 5b read. Run it only if that plan was exactly 1/0/0, or if the GO names the CTO's ruling on each extra row and the
   form (`-target` or whole-root) it admits. NEVER run a Terraform apply from `C:/tmp/og-rel16c`: its root would destroy
   three live resources (Z-S81). Read back `iam get-role-policy` for the new
   policy: one statement, `s3:PutObject` only, on the fee_statement prefix only. Close the ledger and commit it.
7. **Deploy.** Ledger `nfra-oplgtw-gateway-release-e2` (NOT `-r16`: that slug is an old release's, 2026-10-04), entry
   AND sentinel committed first. From `C:/tmp/og-rel16c`, run `infra/aws/ec2/safe-ec2-deploy.sh` with
   `DEPLOY_BASE_REF=2a5966dfbd89be9fe6cc0ef3566831e502b81d42`. Make the halt gate's premise true the way OG-ap-3 A3 did
   (the sparse cone holds your agent home); no `HALT_OVERRIDE`.
8. **Read back immediately** (COO half condition 3 and CTO C2/C5). Use `rl16_verify.py` from W~51, copied to
   `W/ap6_verify.py`, with `before` run at the act on the live base, never with Phase A's 66/52/100. All of these must hold:
   - the tool list is exactly the base's plus `copy_site_file_to_s3`;
   - the `.env` names are exactly the base's plus `ADVI_FEE_STATEMENT_S3_ROOT`;
   - no other value hash moved;
   - `/health` returns 200;
   - the shipped files' md5 equal the release's, with the host's extras named in step 1 unchanged.

   Any trigger: redeploy the base with `DEPLOY_BASE_REF=<release sha>`, destroy the one policy through the same
   Terraform path, and file an ARMED row naming `2.0.0_SA_COO~O`. A revoked concierge family is NOT a trigger: report
   it as re-authentication within the hour.
9. Record the manifest by hand (`EC2_MANIFEST.json` opal-gateway `deployed_commit` = `release_sha`), close the ledger,
   commit, then run AC2. Report once to `2.0.0_SA_COO~O`. You do not run the served read: OG-rl-16's Phase C does.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- E2's `.xlsx` pair only: one tool, one env key, one policy, one restart. Never the `.pptx` pair (`market_update`), and
  never another cell's gateway change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform
  apply`; `aws lambda update-function-code`; override a gate other than the one audited lane escape in step 2.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-e2-put-policy.json
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-e2.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The release commits live on `rel-nfra-oplgtw-r16c` in `C:/tmp/og-rel16c`, never on box/sitez. Rows: id
`NFRA_OPLGTW-Z-S<k>` (the next free number), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` =
`date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after B1, AC2 after B2's ledgers are closed and committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ap6.AC1.sh; echo "exit=$?"</invocation><expect>(?s)is the live ref 2a5966dfbd: yes.*equal=yes.*printf differs only by E2's key and argument: yes.*outside E2's paths 0 \(want 0\); \.pptx-pair tokens in the release gateway tree 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ap6.AC2.sh; echo "exit=$?"</invocation><expect>(?s)nfra-oplgtw-e2-put-policy: entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*nfra-oplgtw-gateway-release-e2: entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*equal=yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the re-cut carries exactly the signed hunks on the live ref, which is the COO half's re-cut condition.
- `AC2`: both acts are landed, neither is half-landed, and the host runs the re-cut release. The served tool is
  OG-rl-16's AC2.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-6.e2-xlsx-release-apply.proof_of_spec.json` and validate it with
`python .tools/proof-of-spec-check.py <instance>`. Flip the ONE `<status>` tag to `complete` only if AC1 and AC2 PASS.
Report once per phase to `2.0.0_SA_COO~O`.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Workstream APPLY-E2, round 33: the applier's half of OG-rl-16 (workstream E2-RELEASE). Cut at MP-r-2's close (COO~MP msg 33064).
- Pre-cut: ap6.AC1 and ap6.AC2 read base FAIL as expected (record absent; 0 entries; manifest d3c31e972e). Positive
  control: a synthetic re-cut from the dry-applied tree on 2a5966dfbd read AC1 PASS (patch-id 041ec0e02b87 equals the
  signed release's). Negative control: a88661b145 on that base read FAIL (15 paths outside, patch-id differs). The
  control record was removed.
- A1 (issuer, 2026-10-11 ~01:1xZ, on rows Z-S81 and Z-S82, after B1 @178b8ecb96, release_sha 6aadf7db37, AC1 PASS):
  - The policy is planned and applied from a box/sitez-HEAD worktree (new step 5b; step 6 amended). It is never
    applied from the release worktree, whose gateway TF root is cut at MP-r-2's deployed commit and lacks box/sitez's
    later Terraform (three live resources would be destroyed).
  - The policy's blob at HEAD equals the signed release's (`49c420ac`), so the act is the same policy.
  - The deploy still ships the release worktree's app code (step 7 unchanged).
  - Option (a) of Z-S81, re-cutting onto HEAD, is refused: it would carry box/sitez's unreleased gateway app changes
    into the deploy.
  - Z-S82: step 1's extras are FOUR dashboard orphans: `index-BP6X9XJd.js`, `index-BqfQgt7G.css`, `index-CrZMj-00.js`,
    `index-a6wjv_wv.css`. Step 8 compares all four as unchanged, and the dashboard/ walk is part of the read-back.
  - Gate limb: to-pipeline-gate grades this modification (placeholders NONE).
- Slug change: the halves' `nfra-oplgtw-gateway-release-r16` is already taken by a 2026-10-04 release, whose CLOSED
  entry would satisfy a count check. The deploy ledger is `-e2`, and this change is named in the re-pin ask.
- Carried from the record: row NFRA_MCPINDEX-Z-S94 (host superset); row Z-W39-S5 (the opal-gateway root's
  grant-writer drift against C3's whole-root plan); row Z-W51-S1 (old `rel-nfra-oplgtw-r16` branch name, hence `-r16c`).

<status>pending</status>
<round>33</round>
<workstream>APPLY-E2</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
