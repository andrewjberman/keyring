# NFRA_OPLGTW task order -- `OG-ap-21` -- APPLY: the per-person record reader, the news and published-analysis role moves, and the published-analysis tool (FWD-22, PRD v2.9 C-PERSON, v3.1, v3.9)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-21</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-21</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; the applier still runs `comp-schedule --drift` at the act and records what it scanned.
comp-iam: RUN-BY-ISSUER at the cut: three Terraform changes. (1) NEW `news_read_internal_iam.tf`: ONE `aws_iam_role_policy` on `aws_iam_role.int_reader`, `dynamodb:Query` and `dynamodb:GetItem` on the four resources `gw_news_read` names; (2) `harvest_published_invoke_iam.tf` retargeted from `aws_iam_role.gw` to `aws_iam_role.int_reader`, `lambda:InvokeFunction` on the ONE function ARN it names; (3) AFTER the served read, `gw_news_read` (`news_read_iam.tf`, the instance-role statement PRD v3.9 admitted for one release) destroyed BY NAME. The person reader needs no grant: the gateway role already holds `dynamodb:GetItem` on the access-state table.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is PRD v2.9 C-PERSON (`NFRA_MCPORTAL` F2 waits on it), PRD v3.9 ("one cell moves the news readers onto the internal reader and destroys the instance-role statement by name") and v3.1 (reads go through the internal reader).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-21` (decomposition addendum R3-T.67, workstream PERSON-ROLES, FWD-22)

APPLY on the live ref that `OG-ap-20` (and the catalog release `MX-r-13` before it) leave. The builds are merged: `OG-cp-1` (`fa9d18e692`; both identity-scope floors), `OG-cp-2` (`ec442b8827`; one test repaired), `OG-nw-2` (`1f556dbc16`), `OG-gt-13` (`3042e6d2d3`), `OG-gt-5` (`640c8a55f7`) and its hookup `OG-gt-11` (`a03a9d2fa2`; pins +1).
NOTHING is a new tool but `harvest_get_published_analysis`; the rest changes WHICH identity the code uses and ADDS the per-person record reader (no record = today's behaviour exactly).

### PHASE A (only when `OG-ap-20`'s ledger `nfra-oplgtw-gateway-release-g5a` is CLOSED): files, plan, re-cut, ask. NO deploy, NO apply IN ANY FORM (a negative check is a plan; its output is kept)

1. **Live ref.** Read `services.opal-gateway.deployed_commit` at HEAD and one SSM md5 read of the host against it over `app/`, `deploy/`, `dashboard/` and `lib/`. A mismatch is a STOP and a BLOCKING row.
2. **Terraform.** (a) Write `infra/aws/terraform/opal-gateway/news_read_internal_iam.tf`: the policy of `news_read_iam.tf` re-created on `aws_iam_role.int_reader` (name from `lib/opal_naming.py name("gateway","global","news-read-internal","policy")`, written as a literal). (b) Retarget `harvest_published_invoke_iam.tf` from `aws_iam_role.gw` to `aws_iam_role.int_reader`.
   (c) `news_read_iam.tf` STAYS in this commit (the old statement is destroyed in Phase B AFTER the served read, never before): do not delete the file in the release commit. Targeted plan of (a) and (b), `-lock=false`, no `-out`, no apply: the plan must read `1 to add, 1 to change, 0 to destroy` (the new policy; the invoke policy's role). Save as `W/P21_PLAN.txt`. Any other change is a STOP. The prefixes and resource names carry no new legacy literals; if the naming limb asks for one, route it to `4.0.0_SA_CRO~Z` as before.
3. **Re-cut** in `C:/tmp/og-rel-p21`, branch `rel-nfra-oplgtw-p21`, at the live ref, with `infra/logic/` and `org/missions/DIRECTIVES.yaml` in the cone. **First enumerate the seams** (every app module the taken files import; `app/typed_scope.py`, `app/harvest_typed.py` are in the base since ap-18/ap-19; check the rest) and **read the closure of the contract**: `build_package.py` stages the contract from `git show <deployed_commit>`, so the new contract reaches the host only through THIS release.
   Take WHOLE from `box/sitez` HEAD: `app/harvest_published.py`, `app/internal_role.py`, `app/news_typed.py`, `app/access_state.py`, `tests/test_og_cp1.py`, `tests/test_og_nw2.py`, `tests/test_og_gt5.py`, `tests/test_og_gt13.py`, `tests/test_access_state.py`, `tests/test_admin_people_access.py`, `infra/aws/ec2/opal-gateway/deploy/NFRA_OPLGTW_CONTRACT.json` and `org/standards/NFRA_OPLGTW_CONTRACT.json` (byte-equal copies).
   Take BY HUNK (3-way against the base; never a whole file from trunk): `app/data_entitlement.py` (the person reader, `person_widens`, the published-analysis name), `app/tools.py` (the person hook at `_run`, the published-analysis registration), `app/integrations/base.py` (the person hook), `app/destructive_ops.py` (the name in `SAFE_TOOLS`), `tests/test_entitlement_admin.py` and `tests/test_data_entitlement_family.py` (pins +1 on the base's), and `deploy-to-ec2.sh` (the `AMGT_SCOPED_API_FUNCTION` key, commit `c10c91b797`). Add the two Terraform files. Commit with the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` on the release commit only.
   Write `W/p21_release.json` = `{"base_sha", "release_sha"}` (FULL shas). Run in the release tree the suites of the taken tests, the entitlement suites, `tests/test_og_hv1.py`, the host-shaped import check (all taken modules and `app.tools`), and `tests/test_schwab_host_inputs.py::test_grant_writer_stages_the_contract_only_from_the_standard` (it reads RED here until the release is the deployed commit: record that, expect GREEN in Phase B).
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-21.md`, for THREE halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~Z`), each under a heading containing its word: (1) the `diff` by file; (2) the `tools` (one new, `harvest_get_published_analysis`, class and refused arms) and the reader's rules (stop, narrow, widen only at the identity-scope floors for an Opal principal and a served tool, fail closed);
   (3) the `widening`, stated plainly: the published-analysis tool lets Opal principals invoke ONE named Lambda (research content) through the internal reader role; the person reader can WIDEN a scoped Opal identity to a served tool when `NFRA_MCPORTAL` writes a record (Andrew-only writes) and can narrow or stop anyone; no grant widens (the news and invoke statements MOVE from the instance role to the internal reader role, narrowing the instance role); (4) the `order` of acts (new policies, deploy, served read, then destroy `gw_news_read` by name);
   (5) `both branches`; (6) the `rollback` (redeploy the base; destroy the two new statements; re-create `gw_news_read` if it was already destroyed); (7) the `triggers`. Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

5. Ledger `nfra-oplgtw-gateway-release-p21`, entry AND sentinel first. Apply the two policy changes through `safe-apply`, targeted, ONE at a time, each read back from IAM. Deploy from `C:/tmp/og-rel-p21` under the A1 guard (HEAD = full `release_sha`, parent = live `deployed_commit`; no other release in flight). Read back against the triggers.
6. **The served read** through the INSTALLED code on the host, one SSM call writing `W/P21_SERVED.json` = `{"body": {"registry_before": N, "registry_count": N+1, "internal_reader_statements_live": true, "news_and_published_served_through_internal_role": true, "non_opal_refused_zero_reads": true, "person_reader_arms_ok": true, "contract_staging_test_green": true, "old_instance_role_statements_gone": false}}`:
   the five news tools and the published-analysis tool answer an Opal stand-in THROUGH the internal reader role (read the assumed-role identity in the call's audit, not the instance role) and refuse a non-Opal with zero reads and zero invokes; the person reader arms are exercised with a STUB store (no record; `stopped: true` denies a floor-allowed tool; a malformed record fails closed) - write NO real `person_access` record; the contract-staging test reads GREEN at the new deployed commit.
7. **Then, and only then,** destroy `gw_news_read` BY NAME through `safe-apply` targeted (the old instance-role news statement) and confirm from IAM that the old news statement and the old invoke statement on `aws_iam_role.gw` are gone and the role's other statements are IDENTICAL to a capture taken before; set `old_instance_role_statements_gone` to true; re-run one news tool and the published-analysis tool: still served (the internal role carries them).
   On any trigger failing: redeploy the base, destroy the two new statements, KEEP `gw_news_read` (or re-create it), and file an ARMED row naming `2.0.0_SA_COO~O`.
8. **Standing release clauses:** runbook 7.2 names the new live release; EC2_MANIFEST `deployed_commit` and `file_checksums` come from the release blobs. Tell `2.0.0_SA_COO~MI` the live commit. Close the ledger, commit, run AC2, and report once to `2.0.0_SA_COO~O`. Report once per phase.

## 2. BOUNDS

- The release's files and the three Terraform changes only. No other IAM or Terraform change; NO `person_access` record is written anywhere real; no object, item or Lambda configuration is written.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply` or any apply in Phase A; print an `.env` value, a person's name or email, or object or item content; override a gate other than the one audited lane escape in step 3.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
infra/aws/terraform/opal-gateway/news_read_internal_iam.tf
infra/aws/terraform/opal-gateway/news_read_iam.tf
infra/aws/terraform/opal-gateway/harvest_published_invoke_iam.tf
infra/aws/terraform/opal-gateway/.terraform.lock.hcl
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-p21.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-21"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap21.AC1.sh; echo "exit=$?"</invocation><expect>(?s)base [0-9a-f]+ is the live ref before this release: yes.*outside the PERSON-ROLES set 0 \(want 0\); published-analysis tool registered 1, SAFE 1, NATIVE 1; person reader present 1, floors calling person_widens 2 of 2.*terraform: news policy count 1 \(want 1\) on the internal reader 1, Query\+GetItem 1, resources 4 \(want 4\); invoke policy on the internal reader 1, function ARNs 1 \(want 1\); forbidden actions 0 \(want 0\), wildcard resource 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-21"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap21.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0.*landed=(?:current|superseded).*registry [0-9]+ -> [0-9]+ \(\+1\); old instance-role statements gone yes; internal-reader statements live yes; six tools served via the internal role and refused with zero reads yes; person reader arms yes; contract-staging test green yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-21" judgment="true"/>
</proof_of_spec>

- `AC1`: the re-cut is exactly the person reader, the two role moves and the published-analysis tool, with the Terraform confined to the internal reader role. `AC2`: the release landed and closed, the old instance-role statements are gone, the new ones are live, the six tools are served through the internal role, the reader's arms hold, and the contract-staging test is green.
- `AC3` (judgment, `3.0.0_SA_CVO~Z`): a published analysis reads as a research user would want it (the section asked for, its as-of, the 50 KB projection flagged). Graded on a real call.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-21.person-roles-release.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream PERSON-ROLES (decomposition addendum R3-T.67). Release queue: ap-18, yr-1, ec-2, ap-19 (live) -> MX-r-13 (catalog) -> ap-20 -> THIS -> ap-17 (bd-3 re-cut) -> G2. `2.0.0_SA_COO~MP`'s F2 and close run wait on the reader being RELEASED: tell them when this closes.
- The standing Phase A rule (Z-S139): no apply in any form.
- Pre-cut: ap21.AC1 and ap21.AC2 base FAIL as expected (p21_release.json and P21_SERVED.json absent).

<status>pending</status>
<round>37</round>
<workstream>PERSON-ROLES</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
