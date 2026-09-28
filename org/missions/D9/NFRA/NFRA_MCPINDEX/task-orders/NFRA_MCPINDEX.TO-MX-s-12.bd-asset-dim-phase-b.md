# NFRA_MCPINDEX task order -- `MX-s-12` -- MX-s-10 PHASE B: the ported asset-dim document goes DEFAULT, the dead Playwright scripts and fees leg retire, and the 22:10Z weekday fire is the acceptance

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~8</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN -- no schedule is added. EventBridge `bd-asset-dim-pipeline-trigger` cron(10 22 ? * MON-FRI *) -> Lambda `bd-asset-dim-trigger` -> SSM `opal-bd-asset-dim-download` stays the ONE asset-dim producer; only the document's DEFAULT version changes. The fees schedule leg `bd-fees-pipeline-trigger` cron(15 22 ? * MON-FRI *) is REMOVED; `bronze/fees` stays current through `bd-49f-fees-runner` (22:20Z), which this order does not touch.
comp-iam: RUN -- no grant changes. `bd-exporter-ec2-role` reads `blackdiamond/49f/session` (MX-s-10 A5, applied; re-read live by 3.0.0_SA_CVO~O at 9ff8aaf1ef).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is bounded by two SIGNED never-widen halves.
EGRESS CLASS, declared: NONE ad hoc. The only vendor call is the scheduled 22:10Z fire, the same vendor at the same cadence.
</preflight>

## 1. THE CELL -- `MX-s-12`

**What.** PHASE A of MX-s-10 is done and graded. The document `infra/aws/ssm/opal-bd-asset-dim-download.json` is ported
to the REST pull plus the dim rebuild (Playwright 0, BD_PASSWORD 0), and an ad-hoc run measured DELTA=0 on content. This
order makes that document the served DEFAULT and retires the dead Playwright scripts and the fees schedule leg.

Both never-widen halves are SIGNED. They ARE your GO, and their guards bind you. Read all three files IN FULL before
step 1:
- CTO half: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/RULING_MX-s-10_NEVER_WIDEN_CTO_HALF_20260928.md`
- CVO half, with guards G1-G3: `org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NFRA_MCPINDEX_MX-s-10_NEVER_WIDEN_SECOND_HALF_20260928.md`
- The ask both halves sign: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_MX-s-10_20260928.md`

**TIME.** Tonight's fire is 22:10Z. Steps 1-3 must be DONE before 22:05Z. Step 4 may follow, but never between 22:05Z
and 22:40Z.

1. **Ledger.** Open the NEVER-2 ledger `nfra-mcpindex-bd-asset-dim-rest-schedule`:
   - `org/critical_paths/.open_deploys/nfra-mcpindex-bd-asset-dim-rest-schedule.json`;
   - an entry in `org/critical_paths/change_management/`.
   COMMIT it before any change.
2. **G1: the rollback targets, READ live and never typed from memory.** Record in that ledger:
   - (a) the current DefaultVersion of SSM document `opal-bd-asset-dim-download` (`aws ssm describe-document`);
   - (b) the served dim's current VersionId, from `aws s3api list-object-versions --bucket opal-data-bd --prefix silver/bd_assets_dim.parquet`.
     The CVO names `kittUyy.WHGfmKRaAag.p4TqGFycZ3eA` (12:22:57Z). If the live LATEST differs, record the live one and
     say so.
   - (c) that version's asset_id count, its non-null `cusip` count, and the sha256 of its sorted asset_id set. These
     are the G2 baseline. Read them into a scratch dir outside the repo.
3. **Publish and set DEFAULT, through the existing deploy path.**
   - First check that the repo file is byte-equal to `git show 0ff972bc38:infra/aws/ssm/opal-bd-asset-dim-download.json`.
     The signed bytes are those.
   - Then run `aws ssm update-document --name opal-bd-asset-dim-download --content file://<file> --document-version '$LATEST'`.
   - Then run `aws ssm update-document-default-version` to the new version.
   - Read back with `aws ssm get-document --name opal-bd-asset-dim-download`, which returns DEFAULT. Compare it to the
     file as parsed JSON objects; the version number alone does not count. Confirm the DEFAULT content carries the rc 92
     no-OUTPUT_KEY refusal and `--union-bronze` on the builder call.
   - Run s10.AC1. If any check here fails, restore the (a) DefaultVersion and report.
4. **G3: retire, through Terraform.** In `infra/aws/terraform/bd-pipeline/`, remove the fees schedule leg:
   `bd-fees-pipeline-trigger` (`aws_cloudwatch_event_rule.bd_fees_pipeline`), its target, its Lambda permission, and
   the `bd-fees-trigger` Lambda, with any resource that exists only for them. Delete these files:
   - `infra/aws/lambda/bd-pipeline/bd-fees-trigger/`;
   - `infra/aws/ec2/bd-exporter/src/stepwise/download-daily-asset-dim.ts`;
   - `infra/aws/ec2/bd-exporter/src/stepwise/download-daily-fees.ts`;
   - the asset-dim script's `_ts_source` entry in `infra/aws/ec2/EC2_MANIFEST.json`.
   How to apply:
   - `.terraform` is absent, so run `terraform init` first. Then apply with `.tools/safe-apply.sh`, never a bare apply.
   - GRADE THE PLAN BEFORE APPLYING. It destroys ONLY the fees-leg resources above, and adds or changes NOTHING.
   - The plan must NOT name `aws_instance.bd_fees`, `bd-49f-fees-runner`, its session-chain rule, `bd-silver-merge`, or
     any asset-dim resource. If it does, the cell STOPS: do not apply, and report with the plan text.
   - After apply, `terraform plan -detailed-exitcode` returns 0.
   - The SSM document `opal-bd-fees-download` is not Terraform-managed. It stays registered, inert with no trigger.
   - Run s10.AC2. Close the deploy legs.
5. **Do NOT fire the served document ad hoc.** The acceptance is the next scheduled 22:10Z weekday fire. Do not run
   the builder by hand at any time: that is the Z-S46 path, and neither half signs it.
6. **G2, at that fire.** When the scheduled run ends:
   - Read the run's uploaded log and the builder's printed `DELTA on the ... already-served rows` block.
   - Compare the written dim with the G1 baseline: ids before and after, added, removed; non-null `cusip` before and
     after; changed values per attribute column; the count of non-null -> non-null cusip changes.
   - IF the id count is below the G1 count, OR ANY row's `cusip` goes from non-null to null: restore the G1 VersionId
     in the same session (`aws s3api copy-object` from that version), and file a row.
   - A cusip changing from one non-null value to another is in radius: report its count, no rollback.
   - If the run FAILED before the builder, the served key did not move: record it and file a row.
7. Run s10.AC3. Then close the ledger in the committed state.
8. Write the proof instance (section 5).

## 2. BOUNDS

1. One producer before and after: no second schedule, no parallel path, no comparator.
2. Nothing under `data/`. Served gold untouched.
3. No private data in the repo: no account ids and no asset rows. Counts and hashes only.
4. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ssm/
infra/aws/terraform/bd-pipeline/
infra/aws/lambda/bd-pipeline/bd-asset-dim-trigger/
infra/aws/lambda/bd-pipeline/bd-fees-trigger/
infra/aws/ec2/bd-exporter/src/stepwise/download-daily-asset-dim.ts
infra/aws/ec2/bd-exporter/src/stepwise/download-daily-fees.ts
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-bd-asset-dim-rest-schedule.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~8/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- row id `NFRA_MCPINDEX-Z-W8-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from the workspace root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3,J1</expected_criteria>
  <criterion id="AC1" cell_refs="MX-s-12" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s10.AC1.sh; echo "exit=$?"</invocation><expect>served document: rest-pull refs>=1 builder refs>=1 playwright refs=0 BD_PASSWORD refs=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-12" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s10.AC2.sh; echo "exit=$?"</invocation><expect>rule state=ENABLED schedule=cron(10 22 ? * MON-FRI *) targets=1 targets bd-asset-dim-trigger=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-s-12" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s10.AC3.sh; echo "exit=$?"</invocation><expect>runs at/after slot>=1 success>=1 dim rewritten after the successful run=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J1" cell_refs="MX-s-12" judgment="true"><!-- s10.J1, CVO-graded at L9 by 3.0.0_SA_CVO~O; the worker RECORDS the G2 delta block and the run log excerpt, no verdict. Question: is the dim written by the 22:10Z fire one a Black Diamond tool may answer from -- ids >= the G1 count, zero non-null->null cusip, and the non-null->non-null cusip-change count explained against MX-s-6's 42. An unexplained jump is a FAIL even when AC3 passes. --></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~8/NFRA_MCPINDEX.TO-MX-s-12.bd-asset-dim-phase-b.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>` above, after the acceptance fire.

Report twice:
- once after steps 1-4, before 22:05Z if you can;
- once after step 8.

Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Cell id: the analysis names `MX-s-10b`; the decomposition grammar (`.tools/to-pipeline-gate.py` CELL_ID_RE) refuses a letter suffix, so the cell is `MX-s-12`. This lifts ROUND_ANALYSIS.round2.md section 1 @e4445020f5 as written. It re-cuts
MX-s-10 PHASE B as its own order; MX-s-10 stays superseded with PHASE A graded (A6 @471c840a0a).
- Paths are MX-s-10's `<paths>` unchanged, minus the closed Z-S44 ledger.
- Criteria: s10.AC1-AC3 unchanged, plus the judgment criterion s10.J1.
- `s10.AC3` keys its slot on the latest `issue(NFRA_MCPINDEX.TO-MX-s-10` commit. `git log --grep` reads the whole
  message, and this issuance's body carries that token, so the slot is the first 22:10Z weekday at or after this issuance.
- Dry-run at base, 20:1xZ: s10.AC1 FAIL (served document v3 of 3: rest-pull 0, builder 0, playwright 1,
  BD_PASSWORD 2); s10.AC2 PASS; s10.AC3 FAIL (slot 2026-09-28T22:10Z, 0 runs).
- `git diff 0ff972bc38 HEAD` is empty on the document, the bd-pipeline Terraform, the builder and the pull, so both
  halves bind the bytes this order publishes.
- Narrowed inside the signed radius: `opal-bd-fees-download` is not Terraform-managed (ANNOUNCE_MX-s-10 step 4), so
  it is left registered and inert.
- Disarms on acceptance, the issuer's: Z-S42 and Z-S47.

# pipeline-override: re-cut of MX-s-10 PHASE B (MX-s-10 carried the same line: supplementary cell ruled by 1.0.0_SA_CTO~O @bf94418eb8 on row Z-S42), lifted from ROUND_ANALYSIS.round2.md s.1 @e4445020f5; the gate's one shape refusal is PRD_HEADER.fabric=laptop vs register site-z, a CTO carrier drift reported to 1.0.0_SA_CTO~O. LIMB 6 still grades.

<status>pending</status>
<direct_act>true</direct_act>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
