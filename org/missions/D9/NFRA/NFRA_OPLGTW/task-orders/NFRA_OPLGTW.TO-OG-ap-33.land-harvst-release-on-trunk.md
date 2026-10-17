# NFRA_OPLGTW task order -- `OG-ap-33` -- APPLY (repository only): land the AMGT_HARVST gateway release `319c9413a2` on trunk after `OG-ap-32` closes (CTO ruling msg 35311, resolving row Z-S336)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-33</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-33</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a repository merge; no schedule, trigger or deploy is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM is applied; the one Terraform file in the merge (`advi_billing_gateway_iam.tf`) is merged as text and NOT applied.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (msg 35311): "~NFRA1 resolves the 319c9413a2 landing AFTER OG-ap-32 Phase B closes, on a small order COO~O cuts"; the released bytes are already live.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ap-33` (decomposition addendum R3-T.105, round 40, workstream ENRICH-R40-L)

CONTEXT. `0.7.0_AE_CloudOps~SC1` deployed `319c9413a2` (`AMGT_HARVST` `HVST-cc-7`) to the gateway host on 2026-10-17 from the local branch `rel-amgt-harvst-cc7b` (also `origin/rel-amgt-harvst-cc7b`), a release line cut on the live ref and never merged to trunk. `OG-ap-32` (release `b124377b41`, cut on `4be300110e` with the three harvest files taken from trunk) deploys on top of it. This order lands that release line on the box trunk (`box/sitez`) so trunk and the live host agree, WITHOUT changing a live byte.

START ONLY on the issuer's GO, which names `trunk_base_sha` (the `box/sitez` HEAD at the GO) and states that the ledger `nfra-oplgtw-gateway-release-batch4` is CLOSED. Do not start before it.

DO, in your own worktree (`C:/tmp/og-land-hvst`, branch `land-hvst-cc7b-nfra1`, created from `trunk_base_sha`; a sparse cone holding every path in `<paths>` and the gateway and Terraform folders):
1. Merge `319c9413a20895a63517c5ca1b9ced0f78a5573a` into the branch with `.tools/safe-merge.sh` (its `--continue` limb keeps a conflicted merge inside the guards; never rebase, never `git stash`, never reset a shared branch). `git merge-tree --write-tree --name-only trunk_base_sha 319c9413a2` lists the conflicted paths (18 when this order was cut; print your count as the denominator).
2. Resolve per the CTO's rules, exactly:
   - every conflicted path under `infra/aws/ec2/opal-gateway/app/`, `lib/`, `dashboard/` and `deploy-to-ec2.sh` resolves to the bytes LIVE after `OG-ap-32`, which are the blobs at `release_sha` `b124377b41caf5665b999378fd0ca08ad8a1fb7d` (the host md5 walk of `OG-ap-32` Phase B equals them);
   - `infra/aws/ec2/EC2_MANIFEST.json`: the `services.opal-gateway` block stays EXACTLY as trunk has it at `trunk_base_sha` (the live `deployed_commit` after the `OG-ap-32` close); the rest of the file merges as git merges it;
   - the six `org/critical_paths/change_management/*nfra-mcportal-*` entries keep BOTH sides (every non-blank line of each side is present);
   - `infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf`: keep both only if the two sides' hunks are disjoint and additive; otherwise STOP, file a BLOCKING row naming the file and the hunks, create no merge commit, and write the record with `stop_row`. It is Terraform and not the gateway lane's.
   - the conflicted gateway TEST files take trunk's side (they are not on the host); if the other side's change in one touches the harvest code, STOP and file a row naming it.
   - STOP, file a BLOCKING row and create no merge commit if resolving any gateway path to the live blob would drop a trunk change that is not deployed (the trunk blob differs from the live blob and a trunk order since the merge base changed it): name the path and the commit.
3. Run the five conflicted gateway test files and `tests/test_og_en18.py` together in both orders on the merged tree: the passed count equals trunk_base's for the same files, none fails only here (record both counts; this is a report item, not a criterion).
4. Write `W/ap33_landing.json` = `{"trunk_base_sha", "hvst_sha": "319c9413a20895a63517c5ca1b9ced0f78a5573a", "release_sha": "b124377b41caf5665b999378fd0ca08ad8a1fb7d", "merge_sha", "branch"}` (40-character shas; `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/`). Commit the record and run the criteria. Do NOT push: `0.0.0_AB_MSTR~Z` carries the merge to origin after the issuer's word.

## 2. BOUNDS

- Only the paths in `<paths>`. No deploy, no `terraform apply`, no IAM, no push, no change to a live byte, no object or item written to any bucket or table.
- Never: `git stash`, rebase, `checkout --`, `clean`, `HALT_OVERRIDE`; print a credential or an account number.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and stop.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/tests/test_admin_gateway_breakdown.py
infra/aws/ec2/opal-gateway/tests/test_admin_people.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
infra/aws/ec2/opal-gateway/tests/test_og_cp1.py
infra/aws/ec2/opal-gateway/tests/test_og_en15.py
infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf
org/critical_paths/change_management/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The tree convention grants `W`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-33"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap33.AC1.sh; echo "exit=$?"</invocation><expect>(?s)conflicted paths \(merge-tree of trunk_base and hvst, the denominator\): (\d+).*merge parents are exactly trunk_base and hvst: yes; hvst is an ancestor of the merge: yes; conflict markers in 0 of \1 paths \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-33"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap33.AC2.sh; echo "exit=$?"</invocation><expect>(?s)gateway live-byte paths (\d+) of \1 equal the release blobs; gateway test paths (\d+) of \2 equal trunk's; manifest opal-gateway block equals trunk's: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-33"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ap33.AC3.sh; echo "exit=$?"</invocation><expect>(?s)mcportal change_management entries (\d+) of \1 carry both sides; billing IAM Terraform carries both sides' added lines: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: a true merge of the HVST release on the trunk head, no conflict marker left in any conflicted path. `AC2`: the gateway bytes equal what is live, the manifest block equals trunk's. `AC3`: the mcportal ledger entries and the billing IAM file keep both sides. A STOP on the Terraform file or on a dropped trunk change leaves the order `staged`, with the BLOCKING row and no merge commit.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-33.land-harvst-release-on-trunk.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (merge_sha, the conflict denominator, the AC lines, the test counts).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 40, workstream ENRICH-R40-L (decomposition addendum R3-T.105). The CTO's four rules (msg 35311) are quoted in step 2; the test-file rule and the dropped-trunk-change STOP are the issuer's.
- Pre-cut: `ap33.AC1/AC2/AC3` base FAIL as expected (record absent). Dry-run on git-plumbing merge commits built on the current trunk head: the PASS arm passes all three (18 conflicted paths: 5 gateway live-byte, 5 gateway test, the manifest, 6 mcportal entries, the Terraform file); controls FAIL (conflict markers left; the adapter at the HVST bytes; the mcportal entries trunk-side only; a one-parent commit).
- The merge pulls the release line's own commits (including release commits cut on the live ref in earlier rounds); the review of those is the conflicted-path list above. The conflict set may differ at the GO (the `OG-ap-32` close adds a manifest change and a ledger entry on trunk); the criteria recompute it from the record.
- Staged: the GO is the issuer's message citing this order, naming `trunk_base_sha`, sent after `nfra-oplgtw-gateway-release-batch4` closes.

<status>staged</status>
<round>40</round>
<workstream>ENRICH-R40-L</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
