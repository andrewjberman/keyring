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
   `python .tools/deploy_ledger.py open --slug mdpf-stratid-r2-global-fold --title "MDPF_STRATID round 2 + ST-w-7: Cottonwood OUTSIDE, held-out stated, unidentified list on the slice" --author 0.7.0_AE_CloudOps~DELL1 --leg "L1|s3-prefix|data/mdpf/scripts/gold/mdpf_gold_consolidator.py|s3 sha256 == git show ff1a8867a6" --leg "L2|s3-prefix|data/mdpf/scripts/gold/mdpf_category_registry.py|s3 sha256 == git show ff1a8867a6" --leg "L3|s3-prefix|data/assets/scripts/gold/build_cottonwood_mdpf_slice.py|s3 sha256 == git show ff1a8867a6" --lambda mdpf-gold-lambda --leg "L4|verify|next scheduled mdpf-scheduled-floor fire|issuer's r2_run_read.py prints R2-RUN-READ PASS"`.
   Commit it, then tell `2.0.0_SA_COO~S1`, citing this order, that the entry is open. Do nothing more until step 2 lands.
2. **The issuer merges** both chains into box/dell1 and names the merge commit to you. `0.0.0_AB_MSTR~DELL1`'s box push then carries
   the three files through the push gate (D1).
3. **After the push**, read back each D1 key: the S3 object's sha256 must equal `git show ff1a8867a6:<path>`'s, and its LastModified
   must be after the entry's open time. Close legs L1, L2 and L3 with that proof.
4. **D2:** `build_package.py` at `--pin ff1a8867a6`, the upload, and a targeted `safe-apply` on the function per the package's own
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


## AMENDMENT (issuer, 2026-10-09 ~19:3xZ) -- leg L4 re-pointed at `55c3cc4642` (CloudOps~DELL1 msg 3048)

- **The trigger.** MDPF_CANON's order 2 redeploys `mdpf-gold-lambda` at `55c3cc4642`, which descends from this order's pin
  `ff1a8867a6`.
- **The consolidator diff between the pins.** It is additive only: 0 lines removed and 4 hunks (an import, a helper after `a4_key`,
  and parquet/backfill emits in `build_all`). No round-2 function changes. `mdpf_category_registry.py` and the slice are the same
  blob.
- **Re-run on that consolidator.** `st_u1_seam` SEAM-OK, `st_u2_seam` SEAM-OK, `st_r2_muni_seam` R2-MUNI-SEAM-OK, U1-OK, U2-OK.
- **Ruling.** L4 reads the 2026-10-10 13:30Z fire on the lambda live then, `55c3cc4642` included, and order 2 is not held. The read
  records the live CodeSha256 and the pin it was built from.

Gate limb: GATE viii on the modification (placeholders NONE).

## AMENDMENT (issuer, 2026-10-09 ~20:3xZ) -- FORWARD FIX NOW: `opal_unidentified.py` is missing from both homes (CloudOps~DELL1 msg 3129, row MDPF_CANON-D1-S3 @7ce182e0ca)

- **The defect (the issuer's).** ST-w-7 made `build_cottonwood_mdpf_slice.py` import `opal_unidentified` at module level
  (`:130-136`). The CTO half's condition-3 closure was read for the consolidator and the registry only, not for the slice. The
  module is in neither home:
  - `build_package.py` does not list it, so the qa_local invoke at 20:14:51Z read `SCOPE FAILED (isolated): cottonwood --
    ModuleNotFoundError`, and global was skipped behind it;
  - it is absent at `s3://opal-data-mdpf/code/scripts/{silver,assets_gold,gold}/` (3 of 3 head-object 404, read 20:2xZ). The
    runner's step 6d (`mdpf-daily-dispatch.sh:547-556`) imports the slice, so the next dispatch (12:52Z or any accelerator
    trigger) fails there too.
- **Its own closure:** `opal_unidentified.py` imports only `__future__` and `re`. Nothing further is missing.
- **ONE act, now, in this order** (rollback is not needed: nothing reads the new key yet, and both fixes are additive):
  - **F1, runner home:** first-mint `git show ff1a8867a6:data/assets/scripts/silver/opal_unidentified.py` (sha256 `6b9c1d7f..`,
    unchanged to HEAD) to `s3://opal-data-mdpf/code/scripts/silver/opal_unidentified.py`. This one manual `aws s3 cp` is
    authorized for this one key (safe-deploy SKIPs a first-mint). Read back sha256 equal.
  - **F2, lambda package:** add `("opal_unidentified.py", "data/assets/scripts/silver/opal_unidentified.py"),` beside the
    `opal_strategy_matcher.py` line (`build_package.py:170`), rebuild at that commit, and run the targeted safe-apply.
    - Coordinate with `2.0.0_SA_COO~D1`: its MDPF_CANON build is the live one, so F2 rebuilds on top of `55c3cc4642` plus this
      line.
    - Read back: the deployed manifest carries `opal_unidentified.py`.
    - Re-run the qa_local invoke: errors `[]`, 16 of 16.
  - Record F1 and F2 as legs on entry `mdpf-stratid-r2-global-fold`.

Gate limb: GATE viii on the modification (placeholders NONE).

## AMENDMENT (issuer, 2026-10-09 ~21:1xZ) -- F3/F4: ship the ST-w-8 key-set pad at `88e974ca10` (row D1-S7 follow-on; CloudOps~DELL1 msg 3151)

- **The pin.** `88e974ca10` (box/dell1 merge of `wk-MDPF_STRATID-w2-8`) pads `unidentified_strategies` to every scope in
  `apply_sma_sleeve_overlay`, so the L-1 key-set identity holds once the Cottonwood slice carries the key.
- **Issuer re-run on the merged tree:**
  - `w2_8_tests` W28-OK; `w2_8_keyset` W28-KEYSET-OK (control reproduces the failure; with the pad, 4 of 4 scopes carry the key and
    identity passes).
  - `w2_7_seam` W27-SEAM-OK; `st_u2_regress` U2-REGRESS-OK; `st_r2_muni_seam` R2-MUNI-SEAM-OK.
  - stratid+taxsma+wiring: 267 passed.
- **The two acts:**
  - **F4, first:** `mdpf-gold-lambda` rebuilt at `88e974ca10` (carries F2's `opal_unidentified.py` line and MDPF_CANON's
    `55c3cc4642`), targeted safe-apply.
    - Read back: the manifest's `mdpf_gold_consolidator.py` equals `88e974ca10`.
    - Then qa_local: errors `[]`, 16 of 16.
  - **F3:** name `data/mdpf/scripts/gold/mdpf_gold_consolidator.py` at `88e974ca10` on entry `mdpf-stratid-r2-global-fold`, so the next
    box/dell1 push safe-deploys it to `code/scripts/gold/` (code homes agree). Read back sha256 equal.
- **Deadline:** before the 2026-10-10 12:52Z dispatch writes the keyed slice. **Fallback** if F4 is not live by 11:00Z: restore
  `code/scripts/assets_gold/build_cottonwood_mdpf_slice.py` to VersionId `Xki2TZ7vXhS6btiNeg3Hl5ASuf3Fq89i`.
- **Leg L4** stays on the 13:30Z fire on the build live then.

Gate limb: GATE viii on the modification (placeholders NONE).

**REPORT:** the entry path, the three D1 sha256 pairs and VersionIds (before and after), the D2 manifest read, and each leg closed.
</task_order>
