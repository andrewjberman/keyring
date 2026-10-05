# TO MDPF_SECCLASS.TO-SC-e19 -- round 7 SC-e-19: FWD-10 -- the scheduled producer for stocks newly entering through the Opal ETFs' and the rival ETFs' trading

<to_id>MDPF_SECCLASS.TO-SC-e19</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~16</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-10-05</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-19` (`decompositions/MDPF_SECCLASS_DECOMP_R7.md`) |
**outcome_ref:** FWD-10 | **depends_on:** MDPF_SECCLASS.TO-SC-e17 (imports its module; starts after it drains)

---

## WORKER FACE

### THE CELL

`SC-e-19`. FWD-10: "when a stock first appears in the holdings of an Opal ETF or a rival ETF, the routine adds its entry and
fills its history back three years without a person starting it; where it asks an outside source or model, that use has
Andrew's word, never a default" (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.3).
- 1.0.0_SA_CTO RULINGS batch 257 Q5
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md`): a SCHEDULED PRODUCER, not an alert
  or monitor (CLAUDE.md moratorium).
- **Measure which Opal ETFs the rival canonical_shape already carries. Read the Opal silver holdings only for the rest.**
- History is site Z's input (Q2). This producer writes no price series. It writes the day's new-stock list to a
  builder-addressed artifact, so the gap is visible and routable.

**Inputs:**
- Rival and possibly Opal ETFs: `s3://opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/date=<d>/holdings-<rev>.parquet`
  (13 funds measured, `fund_ticker` column). Refreshed Monday to Friday at about 07:10 ET, with a 09:00 ET sweep.
- Opal ETFs: `s3://opal-data-etfs/silver/holdings/{run_date}.parquet` (`holding_ticker`, `cusip`, `security_name`), written by
  `infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py:1501-1508` on `cron(0 22 * * ? *)`.
- The mapping: `infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py` `classify_canonical_row()` from cell
  `SC-e-17` (Q1 keys, Q3 sub-class, Q4 domain).
  - For an Opal-silver row, which has no Bloomberg id or GICS, build the same item through the module's US-ticker path.
  - Where nothing resolves a sub-class, set `low_confidence: true`.
  - No vendor call and no model: Andrew's word is required and none is given.
- The writer: `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` `write()` (put on absence only).

**Build (code, tests, dry run and declared infra; NO apply and NO table write: the apply is the issuer's act under its own
half):**
1. **Measure first.** Which funds in the canonical_shape are Opal ETFs? Compare against the Opal silver holdings' fund ids.
   Print the split. The producer reads silver only for the Opal ETFs canonical_shape lacks.
2. **The producer.** `infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py`. For the run day:
   - A stock is NEW when it is in today's holdings (either source) and was not in the previous available day's.
   - Plan each new stock through the module, skip any key the table already has (consistent get), and write through
     `write()`.
   - Write the day's new-stock list (key, source, fund, `security_bloomberg` or ticker, planned/written/present) to an
     S3 address from `lib/opal_naming.py address()`.
   - `dry_run` is the default when invoked without `{"write": true}`.
   - ASCII only.
   - Tests in `infra/aws/lambda/mdpf-secclass/new-security-classifier/tests/test_new_security_classifier.py`, with S3 and
     DynamoDB stubbed: new versus carried stocks; a present key is skipped; an Index future or cash line is ignored; the
     dry run writes nothing.
3. **Rule 30 / LGIC.** Every resource name comes from `lib/opal_naming.py name()` and every S3 address from `address()`.
   - A builder REFUSAL is a missing registry row: add it to `infra/logic/registry/resources.json` or `systems.json`, and
     never hand-type a name.
   - Homes and tenancy follow `infra/logic/02_DOCTRINE.md`.
4. **Declared infra (not applied).** `infra/aws/terraform/mdpf-secclass/new-security-classifier/`:
   - the Lambda, sourced from the S3 artifact pattern the other modules use
     (`infra/aws/terraform/investor-reporting/holdings/lambda.tf`);
   - an EventBridge Scheduler or rule firing Monday to Friday after the canonical_shape refresh plus its sweep. Pick the
     time from the measured refresh times and say why;
   - its IAM role:
     - `s3:GetObject` and `s3:ListBucket` on `opal-data-etfs/rivalfunds/etfs/gold/canonical_shape/*` (the CTO's "read
       grant ... is a laptop cell") and on `opal-data-etfs/silver/holdings/*`;
     - `dynamodb:GetItem` and a conditional `dynamodb:PutItem` on `etf-classifications`;
     - `s3:PutObject` on the new-stock list's address only.
5. **The dry-run check.** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd10_dry_run.py --packaged`.
   - It assembles the files the Lambda would ship (the handler plus every `_shared` module it imports) into a temp dir, and
     imports the handler from that packaged layout. That is DECISION 103371's deployed-layout import.
   - It runs the handler in dry run against the live inputs for the latest day that has a previous day, and prints
     `FWD10-DRY-RUN day=<d> previous=<d> sources=<n> new_stocks=<n> planned_writes=<n> present=<n>`.

### ACCEPTANCE

<criterion id="SC7-e19-AC1" cell_refs="SC-e-19"><invocation>python -m pytest -q infra/aws/lambda/mdpf-secclass/new-security-classifier/tests/test_new_security_classifier.py</invocation><expect>passed</expect></criterion>
`SC7-e19-AC1` -- the producer detects new stocks, skips present keys, ignores non-stocks and writes nothing in a dry run.

<criterion id="SC7-e19-AC2" cell_refs="SC-e-19"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd10_dry_run.py --packaged</invocation><expect>FWD10-DRY-RUN day=</expect></criterion>
`SC7-e19-AC2` -- imported from its packaged layout, the producer dry-runs the latest real day end to end.

<criterion id="SC7-e19-AC3" cell_refs="SC-e-19"><invocation>.tools/terraform.exe -chdir=infra/aws/terraform/mdpf-secclass/new-security-classifier validate -no-color</invocation><expect>The configuration is valid</expect></criterion>
`SC7-e19-AC3` -- the declared infra validates. Before `validate`, run `init -backend=false -plugin-dir=C:/Users/AndrewBerman/.terraform.d/plugin-cache`, so no registry egress.

<expected_criteria>SC7-e19-AC1,SC7-e19-AC2,SC7-e19-AC3</expected_criteria>

Dry-run at the base 2026-10-05: all three FAIL as expected (no producer, check or module).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No apply, no table write, no S3 write.** The dry run reads live inputs only. `terraform apply`, the artifact upload and
  the first real fire are the issuer's act under a half.
- **No vendor or model call** (Andrew's word is required for any).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W16-S<k>`), and do not weaken the test.

<paths>
infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py
infra/aws/lambda/mdpf-secclass/new-security-classifier/tests/test_new_security_classifier.py
infra/aws/terraform/mdpf-secclass/new-security-classifier/main.tf
infra/aws/terraform/mdpf-secclass/new-security-classifier/lambda.tf
infra/aws/terraform/mdpf-secclass/new-security-classifier/iam.tf
infra/aws/terraform/mdpf-secclass/new-security-classifier/schedule.tf
infra/logic/registry/resources.json
infra/logic/registry/systems.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd10_dry_run.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. The two registry files are for a builder refusal only. Everything else named here you READ and
never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R7.md</decomp_doc> (round 7), cell `SC-e-19`.
<owned_cells>SC-e-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC7-e19-AC1, SC7-e19-AC2, SC7-e19-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~16/MDPF_SECCLASS.TO-SC-e19.fwd10-new-security-producer.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC7-e19-AC1,SC7-e19-AC2,SC7-e19-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the Opal-ETF split, the dry-run line, the builder names and addresses used (or the registry rows added), the
schedule and why, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the gate ledger read 2026-10-05 ~06:5xZ (python .tools/comp-schedule): no armed gate names MDPF_SECCLASS FWD-10 or a new-security schedule. The cell DECLARES one new schedule after the canonical_shape refresh; it is applied only under the issuer's half.
comp-iam: RUN -- read 2026-10-05 ~06:5xZ (comp-iam service dynamodb; comp-iam resource-sweep): the existing etf-classifications writer role is yang-pipeline-lambda-role (the seed path). The cell DECLARES a new role (reads two opal-data-etfs prefixes, conditional put on etf-classifications, one S3 put); it is applied only under the issuer's half.
comp-adversary: RUN -- the moratorium (a scheduled producer, not a monitor), the vendor rule (none), the FWD-7 writer (put on absence, no LLM: etf_classification_scheduled.py:30-31, :506), LGIC rule 30; BLIND: which Opal ETFs canonical_shape carries (step 1 measures it), the refresh time spread (step 4 reads it).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.3 FWD-10 @ffb329af49; RULINGS batch 257 Q5 @a272c26a75; intake @320b02aa6b.
