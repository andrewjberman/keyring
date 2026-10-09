<task_order>
  <metadata>
    <id>MDPF_STRATID.TO-APPLY-R2.global-fold-deploy</id>
    <issued_by>2.0.0_SA_COO~S1</issued_by>
    <issued_to>0.7.0_AE_CloudOps~DELL1</issued_to>
    <date>2026-10-09</date>
    <status>pending</status>
    <project_code>MDPF_STRATID</project_code>
  </metadata>
<direct_act>true</direct_act>
<!-- Round-less by design: an executor apply order, not a cell. Round 2 (workstream 1) drain acts 3-4 of
decompositions/MDPF_STRATID_DECOMP_R2.md, under the signed never-widen pair. -->
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<placeholders>NONE</placeholders>
<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP_R2.md</decomp_doc> (round 2, workstream 1, the issuer's drain acts 3-4): the deploy of cells `ST-u-1` and `ST-u-2`.
<owned_cells>ST-u-1 ST-u-2</owned_cells>
</decomp_ref>

## THE PAIR (both halves signed)

- **Pair:** `org/missions/D8/MDPF/MDPF_STRATID/deliverables/2.0.0_SA_COO~S1/NEVER_WIDEN_PAIR_R2_COTTONWOOD_OUTSIDE.md` @c4fdec2ec7.
  The COO half is signed.
- **CTO half:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_MDPF_STRATID_R2_COTTONWOOD_OUTSIDE_20261009.md` @07ee308141, signed by
  laptop `1.0.0_SA_CTO` with five conditions. This order carries conditions 3 and 4; the issuer carries 1, 2 and 5 at the real-run
  read.
- **Pin:** the issuer's drain merge commit on box/dell1, named in the step-2 message. It carries two chains:
  - `wk-MDPF_STRATID-r2-7` (tip `f1deec74b1`, round 2, under the pair);
  - `wk-MDPF_STRATID-w2-7` (tip `22e11fae54`, ST-w-7, decomposition W2 amendment A10).

  ST-w-7 adds the key `unidentified_strategies` to the per-firm Cottonwood slice. It moves no figure and sits outside C-GLOBAL-PAIR;
  it ships in the same act under the same entry. The issuer re-ran it at `22e11fae54`: w2_7_tests/seam, w2_3 and w2_4 OK, 758 tests
  passed, ruff clean. The one failure is `test_cotbkf_no_account_ids`, ADVI_COTBKF's client-data containment test over that project's
  own files; it is unrelated to this chain.
- **Rollback handles** (current VersionIds, read 2026-10-09 ~17:4xZ):
  - `code/scripts/gold/mdpf_gold_consolidator.py` `8sZntN5G7HuzCaybxkmSnH3d3CKZWNCY`;
  - `code/scripts/gold/mdpf_category_registry.py` `2cCTChC_fGrf7ZXmlt4rvnWScPdFSex.`;
  - `code/scripts/assets_gold/build_cottonwood_mdpf_slice.py` `Xki2TZ7vXhS6btiNeg3Hl5ASuf3Fq89i` (84,601 B, 2026-10-08T22:03:48Z).
- **Two homes:**
  - **D1:** `s3://opal-data-mdpf/code/scripts/gold/{mdpf_gold_consolidator,mdpf_category_registry}.py` and
    `s3://opal-data-mdpf/code/scripts/assets_gold/build_cottonwood_mdpf_slice.py`, via the box/dell1 push gate.
  - **D2:** `mdpf-gold-lambda`, via `build_package.py` at the pin plus a targeted `safe-apply`.

## Condition 3 -- import closure (read by the issuer 2026-10-09 ~17:3xZ; re-read it yourself before D1)

- **No new import.** The round-2 diff `23c47d3837..f1deec74b1` adds no import to either file. Its one `+ from` match is docstring
  text.
- **S3 presence.** The 14 first-party modules the two files import from the gold directory are all present at
  `s3://opal-data-mdpf/code/scripts/gold/` (head-object, non-zero length each):
  - dim_mdpf_account_distribution, dim_mdpf_aggregate_aua_timeseries, dim_mdpf_aum_metrics, dim_mdpf_non_model_assets;
  - mdpf_aggregate_aua, mdpf_calendar_binding, mdpf_category_registry, mdpf_gold_catchup, mdpf_revamp_model_crosswalk;
  - taxsma_assets, taxsma_membership, taxsma_reconcile, taxsma_snapshot, taxsma_sources.
- **Package manifest.** All 19 modules in the closure are named in `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py`
  (missing 0 of 19).

## THE ACT, in this order

1. **Open the change-management entry** (condition 4; NEVER-2), as yourself, before anything ships:
   `python .tools/deploy_ledger.py open --slug mdpf-stratid-r2-global-fold --title "MDPF_STRATID round 2 + ST-w-7: Cottonwood OUTSIDE, held-out stated, unidentified list on the slice" --author 0.7.0_AE_CloudOps~DELL1 --leg "L1|s3-code|data/mdpf/scripts/gold/mdpf_gold_consolidator.py|s3 sha256 == git show <merge>" --leg "L2|s3-code|data/mdpf/scripts/gold/mdpf_category_registry.py|s3 sha256 == git show <merge>" --leg "L3|s3-code|data/assets/scripts/gold/build_cottonwood_mdpf_slice.py|s3 sha256 == git show <merge>" --lambda mdpf-gold-lambda --leg "L4|verify|next scheduled mdpf-scheduled-floor fire|issuer's r2_run_read.py prints R2-RUN-READ PASS"`.
   Commit it, then tell `2.0.0_SA_COO~S1`, citing this order, that the entry is open. Do nothing more until step 2 lands.
2. **The issuer merges** both chains into box/dell1 and names the merge commit to you. `0.0.0_AB_MSTR~DELL1`'s box push then carries
   the three files through the push gate (D1).
3. **After the push**, read back each D1 key: the S3 object's sha256 must equal `git show <merge>:<path>`'s, and its LastModified
   must be after the entry's open time. Close legs L1, L2 and L3 with that proof.
4. **D2:** `build_package.py` at `--pin <merge>`, the upload, and a targeted `safe-apply` on the function per the package's own
   README.
   - Read back the deployed package's manifest: the three changed files' sha256 must equal the pin's.
   - Then invoke nothing. The scheduled fire is the run.
   - Close the tf-lambda leg.
5. Leg L4 (the scheduled run) stays the issuer's.

**Rollback per key:**
- D1: copy each key's prior object version back (record both VersionIds before D1).
- D2: rebuild at the prior pin and apply the same target.
- A half-landed state is rolled back the same session (NEVER-2).

## CONDITIONS (criteria of every order to a CloudOps lane; amendment A8)

(1) `opal-data-mdpf/code/` is the MDPF code prefix, not a firm data tree. State that in the report.
(2) This order sends nothing to `mdpf-daily-runner`.
(3) It writes no data.
(4) IAM: none.
(5) Naming-place enforcement: no new infra name.

## ACCEPTANCE

<criterion id="APPLY-R2-AC1" cell_refs="ST-u-1"><invocation>python C:/Dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/R2_CHECKS/st_u1_seam.py</invocation><expect>SEAM-OK</expect></criterion>
`APPLY-R2-AC1` -- run against the box/dell1 tree after the merge and before D2, so the code you package passes the seam on real data.
<criterion id="APPLY-R2-AC2" cell_refs="ST-u-1" judgment="true"/>
`APPLY-R2-AC2` -- the three D1 keys and the D2 package equal the pin by content. Legs L1, L2, L3 and the tf-lambda leg are closed
with that proof.

<expected_criteria>APPLY-R2-AC1 APPLY-R2-AC2</expected_criteria>

<proof_of_spec>
Criterion ids: APPLY-R2-AC1, APPLY-R2-AC2. Instance at `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.7.0_AE_CloudOps~DELL1/MDPF_STRATID.TO-APPLY-R2.global-fold-deploy.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> APPLY-R2-AC1,APPLY-R2-AC2` BEFORE the flip. Record AC2 as
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the issuer `2.0.0_SA_COO~S1`, who grades it on the report.
</proof_of_spec>

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/tier2_senior/0.7.0_AE_CloudOps~DELL1/
org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.7.0_AE_CloudOps~DELL1/
</paths>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule moves; the scheduled mdpf-scheduled-floor fire is the run.
comp-iam: DECLARED-NOT-APPLICABLE no IAM; the push gate and safe-apply run under their existing roles.
comp-adversary: RUN -- the one hazard is the import break (row D1-S4); coverage: 19 of 19 closure modules read in S3 or the package manifest, 0 missing; blind to modules imported lazily inside functions, which the seam's in-process run exercises.
risk: WORLD -- a code upload the scheduled pipeline executes.
direct_act: true -- an executor apply order, round-less, no cell.
</preflight>

**REPORT:** the entry path, the three D1 sha256 pairs and VersionIds (before and after), the D2 manifest read, and each leg closed.
</task_order>
