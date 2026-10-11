# NFRA_IAMROLES202609.TO-IAM-z-3 -- opal-market-data-v2 (ruled deleted 2026-07-30, tombstoned): remove its Terraform declaration (TF-debt A7) and its one live Allow, ONE pair (round-8 analysis E3; row Z-S43)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R9.md</decomp_doc>
<owned_cells>IAM-z-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (ROUND_ANALYSIS.round8.md @d14162158d, E3)

```
IAM-z-3. ACT: one pair, one module (infra/aws/terraform/market-overview), two removals:
  (1) the declaration of the deleted bucket: market-overview/s3.tf, resources
        aws_s3_bucket.market_data_v2 (:5), aws_s3_bucket_versioning.market_data_v2 (:10),
        aws_s3_bucket_server_side_encryption_configuration.market_data_v2 (:17),
        aws_s3_bucket_public_access_block.market_data_v2 (:26)
      -- these are round 7's "4 to add": Terraform trying to resurrect a bucket Andrew ruled deleted. TF-debt A7, which your
      lane declined in July as unauthorized, is now authorized by the CTO's E3 ruling.
  (2) the Allow on market-data-generator-lambda-role (market-overview/iam_legacy.tf): the ARN "arn:aws:s3:::opal-market-data-v2/*"
      in Sid S3MarketDataWrite (:50) and "arn:aws:s3:::opal-market-data-v2" in Sid S3MarketDataList (:59). The opal-data-portal-v2
      ARNs and all actions stay.
  and mark the tombstone's `declaration_removed` done in infra/aws/terraform/tombstones.json (the opal-market-data-v2 entry, ~:69),
  citing the apply commit.

PHASE A -- read-only, no AWS write:
  1. `terraform state list` in market-overview: do the four market_data_v2 addresses exist in STATE? (If they do, removing the
     declaration plans a DESTROY of an absent bucket: say what the plan does with it, verbatim.) Re-read the bucket live
     (get-bucket-location -> NoSuchBucket). Save the as-live inline policy to
     org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round9/market_data_v2/ROLLBACK_<policy>.json.
  2. In YOUR OWN worktree: make both removals; plan the module UNTARGETED and targeted, and record exactly:
       PLAN: market-overview: <the plan summary, verbatim>
     The expected shape: the four adds vanish; the role policy is 1 change losing exactly the two ARNs; nothing else. Any other
     planned change is named and is a reason to target. Grade the naming with `git diff --cached --no-renames`. Write
     .../market_data_v2/MDV2_SURVEY.md holding the state read, both plans, and the per-attribute grade. Commit the survey and
     the rollback only, never the edit.
  3. STOP. Report to 2.0.0_SA_COO~ZI. The pair ledger/NEVER_WIDEN_ROUND9_Z-3_{COO,CTO}_HALF.md is written against your survey.

PHASE B -- only on the issuer's GO after both halves are SIGNED:
  4. Read .open_deploys/ for market-overview; open a NEVER-2 entry `iamroles-r9-market-data-v2`.
  5. Commit the edit and the tombstone line on your worktree branch, `safe-apply` as signed, drain the same session.
  6. Verify LIVE: the policy differs from the rollback by exactly the two ARNs; the bucket still reads NoSuchBucket (nothing
     re-created). Record in .../market_data_v2/POST_APPLY.md, exactly:
       POST-APPLY-PLAN: market-overview: <the untargeted shared-tree plan summary after the drain, verbatim>
     Then close the entry.
```

## DEPENDENCIES

None. PHASE A runs beside IAM-z-1 and IAM-z-2; PHASE B serializes with them on `.open_deploys/`.

## BOUNDS

```
ONLY the four market_data_v2 declarations and the two dead ARNs leave. Nothing is added; NEVER create the bucket.
The market-data-generator role itself stays (its orphan status, RoleLastUsed null and no function, is a row, not this act).
safe-apply only (NEVER-9); the NEVER-2 entry opens first and closes last.
STANDING (Z-S40): the survey names its read time; the act re-reads its baseline before it applies.
G-21: no alert, monitor or schedule.  G-25: no Access Analyzer.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/terraform/market-overview/s3.tf
infra/aws/terraform/market-overview/iam_legacy.tf
infra/aws/terraform/tombstones.json
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round9/market_data_v2/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-z-3.market-data-v2-declaration-and-allow.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-z-3).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-z-3"><invocation>bash -c "f=org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round9/market_data_v2/POST_APPLY.md; test -f \$f || { echo MISSING:\$f; exit 2; }; echo decl=\$(grep -c 'market_data_v2' infra/aws/terraform/market-overview/s3.tf) plan=\$(grep -c -E '^POST-APPLY-PLAN: market-overview: .*0 to add, 0 to change, 0 to destroy' \$f)"</invocation><expect>`decl=0 plan=1` -- the declaration is gone and the module plans clean after the drain (no resurrection pending)</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-z-3"><invocation>bash -c ".tools/aws iam get-account-authorization-details --output json > /c/tmp/z3_auth.json && python 'org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/2.0.0_SA_COO~ZI/checks/round9/allow_names.py' /c/tmp/z3_auth.json opal-market-data-v2 opal-data-portal-v2"</invocation><expect>`opal-market-data-v2=0`, and `opal-data-portal-v2=` 30 or more beside a `DENOMINATOR:` line (a failed read exits 2, never a zero)</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-z-3"><invocation>bash -c "echo open=\$(ls -a org/critical_paths/.open_deploys/ | grep -c 'iamroles-r9-market-data-v2') closed=\$(grep -l '^\*\*Status:\*\* CLOSED' org/critical_paths/change_management/*iamroles-r9-market-data-v2* 2>&1 | grep -c '\.md\$')"</invocation><expect>`open=0` and `closed=1`</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-z-3" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): is the ruled
  deletion now complete on every plane (declaration, state, grant, tombstone), with nothing re-created?

Every invocation runs under `timeout 120`, except AC2, whose account-wide read takes up to 300 seconds.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>9</round>
<slot>0.7.0_AE_CloudOps~IR</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-z-3</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 9) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** row Z-S43 -> round-8 slug (msg 33357) -> `ROUND_ANALYSIS.round8.md` @d14162158d E3 (msg 33361) -> L5 round-9 decomp -> this issuance.
**Risk WORLD:** a Terraform declaration removal plus a permission narrowing, under one never-widen pair.
<preflight>
comp-schedule: RUN -- PARTIAL_OR_BLIND at the round-7 read; the assignee reads .open_deploys/ for market-overview before its entry opens.
comp-iam: RUN -- live read at the cut (checks/round9/allow_names.py): opal-market-data-v2=1 (market-data-generator-lambda-role); control opal-data-portal-v2=38.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 3 of 3 (tombstones.json ~:69 reads deleted 2026-07-30, declaration_removed NOT YET; s3.tf :5/:10/:17/:26 declare the four adds; iam_legacy.tf :50/:59 hold the two ARNs).
</preflight>

**Preflight disposition:** checks dry-run at the base: AC1 base FAIL as expected (`MISSING:` POST_APPLY.md); AC2 base FAIL as expected (opal-market-data-v2=1); AC3 base FAIL as expected (`open=0 closed=0`).
