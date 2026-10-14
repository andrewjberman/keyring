# NFRA_OPLGTW task order -- `OG-ec-2` -- APPLY: deploy the Eclipse converter fix and drive the silver sweep until the guard reads PASS (row Z-S117, CTO msg 34152)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ec-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ec-2</to_id>
<issued_to>0.7.0_AE_CloudOps~ZS</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-APPLIER at the act (`comp-schedule --drift`) on the Eclipse silver sweep (`cron(0 16 * * ? *)`, `infra/aws/terraform/opal-assets/silver.tf`): record what it scanned and any hold or moratorium naming the converter; none is known at the cut.
comp-iam: DECLARED-NOT-APPLICABLE -- the converter's role and policies do not change; this order redeploys its code only.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's ruling (msg 34152, PRD v3.5) on row NFRA_OPLGTW-Z-S117 (0.7.0_AE_CloudOps~Z), and `OG-ec-1` (merged `d2ad76dd24`) is the reviewed schema edit it deploys.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ec-2` (decomposition addendum R3-T.58, workstream G2-ECLIPSE, FWD-22 client data)

Since 2026-10-10 the vendor's Eclipse `portfolios_simple.json` carries one extra column, `defaultTradingEngineId`. The converter's drift check raised `VendorDriftError` for it and, because the check fires during a run that converts the folder, 12 bronze keys failed
(`eclipse/inflection/bronze/2026-10-14/`: `model_composition_{3,5,6,7,8,9,10,28,29}.json`, `models.json`, `portfolios_full.json`, `portfolios_simple.json`; the DLQ was drained, nothing retries them). The silver guard reads FAIL: `expected 552 landed 547 matched 547 missing 5 alien 0`
(`eclipse/inflection/meta/backfill-status.json`). `OG-ec-1` edited `mirror_schemas.py` to admit the column and re-vendored the eclipse converter copy byte-identical (merged `d2ad76dd24`). THIS order deploys that code and drives the sweep that fills the gap.

### PHASE A: measure, plan, ask. NOTHING applied

1. Read the live converter's deployed code hash against the repo's at HEAD (the converter lives under `infra/aws/lambda/opal-assets/opal-assets-silver-eclipse/`; the Terraform root is `infra/aws/terraform/opal-assets`, `silver.tf`). Write `W/EC2_PLAN.json` with `live_code_sha256` and `repo_code_sha256`
   (64 hex each; they must differ, else STOP and a BLOCKING row), the converter's Terraform resource address, `tf_plan_summary` from a targeted `terraform plan` of that one resource (`0 to add, 1 to change, 0 to destroy`; `-lock=false`, no `-out`, no apply; any other change is a STOP),
   and `missing_silver_count` (the integer from the guard's own `missing`, and the list of the missing silver keys, counted not guessed). Find out HOW the scheduled sweep converts a missing key (read `silver.tf` and the sweep code) and record the manual invoke that drives it once, so the act is a deliberate drive and not a wait for 16:00Z (`sweep_invoke`).
2. **The ask**, `W/NEVER_WIDEN_ASK_OG-ec-2.md`, for TWO halves (`1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~O`): the converter's output reaches pages and tools, so the act moves served data (NEVER-1). Each under a heading containing its word: (1) the `diff` (the code delta by file, hashes); (2) the `widening`, stated plainly (no new reach: the converter writes the same silver prefixes it always did,
   now also for the 12 keys; list the silver keys the sweep will write and the prior state of each, absent or present); (3) the `order` of acts (ledger, apply the one resource, drive the sweep once, read the guard); (4) `both branches` (the drift check still refuses a column that is NOT admitted: zero silver writes and the same error; an admitted file converts); (5) the `rollback` per key (delete the newly written silver objects; redeploy the prior code from its recorded hash); (6) the `triggers` (guard verdict PASS with expected = landed, missing 0, alien 0; deployed hash = repo hash).
   Commit, run AC1, REPORT, STOP.

### PHASE B (only on the issuer's GO, which names both halves signed)

3. (A1) Ledger `nfra-oplgtw-eclipse-converter`, entry AND sentinel first (name every Lambda or task family that shares the converter code, one `describe`/`get-function` sweep). BEFORE the apply, build the converter package from the repo's bytes and upload it to the artifact bucket key the module reads (`data.aws_s3_object.artifact`, `s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-silver-eclipse/...`), exactly as the prior eclipse release did; record the prior object's version id and sha256 in the ledger as the rollback. Then apply the ONE resource through `safe-apply` targeted. Read the deployed hash back and compare it with the repo's.
4. Drive the sweep once with the recorded manual invoke. Read `eclipse/inflection/meta/backfill-status.json`. If the guard does not read PASS, STOP: do not invoke again; file an ARMED row naming `2.0.0_SA_COO~O` with the guard's own numbers and the converter's log lines (no data content).
5. Write `W/EC2_PROOF.json` = `{"deployed_code_sha256": "<64 hex>", "sweep_driven_by_applier": true, "guard": {"verdict": "PASS", "expected": N, "landed": N, "missing": 0, "alien": 0}, "freshness_td": N}` where `freshness_td` is the Eclipse silver's newest partition in TRADING days behind T-1 (`lib/trading_calendar.py`). Close the ledger, commit, run AC2, report once to `2.0.0_SA_COO~O`.

## 2. BOUNDS

- ONE resource applied (the converter's code) and ONE object written, the converter's package at its artifact key (A1); nothing else in any bucket. No IAM, schedule, queue, bucket or other Lambda change; `aws lambda update-function-code` is never used (Terraform only). No object is written by you; the sweep writes the silver it always wrote.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform apply`; print a person's name, an account number or an object's content.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-assets/silver.tf
infra/aws/terraform/opal-assets/.terraform.lock.hcl
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-eclipse-converter.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZS/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZS/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ec-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ec2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)live converter differs from the repo's: yes; plan '0 to add, 1 to change, 0 to destroy.*is one change: yes; missing silver count [1-9]\d*; ask headings 6 of 6.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ec-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ec2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0.*deployed code equals the repo's: yes; sweep driven by the applier: yes; guard PASS \(expected (\d+) landed \1 missing 0 alien 0\); Eclipse silver freshness [01] trading day\(s\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the live converter lacks the fix, the plan is exactly one change, the gap is counted, and the ask is complete. `AC2`: the fix is deployed from the repo's bytes, the sweep was driven by you, and the guard reads PASS with Eclipse silver fresh in trading days.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ec-2.eclipse-converter-deploy.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G2-ECLIPSE (decomposition addendum R3-T.58). The eclipse tables are G2 (Orion/Inflection) client data; they are reached only after this lands. Z-S110 (the 49F producer's OutOfMemory) follows the same route once its cause is read: a separate order.
- Seat: `0.7.0_AE_CloudOps~ZS` (idle at the cut). Never-widen halves: CTO and COO (the sweep writes served silver). The GO is the issuer's message citing this order.
- Pre-cut: ec2.AC1 and ec2.AC2 base FAIL as expected (the records are absent).


- A1 (issuer, 2026-10-14 ~23:1xZ, row Z-S131, msg 34274): Phase B had no artifact-upload step, so an apply alone moves only the pin. Ruled IN: the package is built from the repo's bytes and uploaded to the module's artifact key before the apply, as the prior eclipse release did; the prior object's version and sha256 are the rollback; the ask (section order, rollback) names the upload. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>G2-ECLIPSE</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
