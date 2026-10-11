# ADVI_FIRMBKTS task order -- `FB-g-22` -- ACT 3b'S REGISTRY ROWS AND THE SHARED-INFRA WIRING: THE READERS' ADMISSION TO `opal-data-49financial` (THE CTO'S ADDENDA 8 TO 10)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-22</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~44</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two repository files; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: RUN by the issuer -- this cell WRITES the rows of a bucket-policy change and applies none of it. The permitted set, the writers counted (1 writer of the bucket policy, 1 generator, 1 registry file), both branches and what the act does not know are in `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT3B_ADMISSION_COO_HALF.md` (COO half; the CTO half `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT3B_ADMISSION_CTO_HALF.md` precedes the apply, not this commit). Identity side read for all 11 principals (`IDENTITY_CENSUS_20261011.txt`: no permissions boundary on any). The act that applies the policy is a separate staged order under that pair.
comp-adversary: RUN by the issuer -- at base `r4_policy.py` reads 1 of 6 (P6 clean plan PASS as the control; P1 to P5 FAIL as expected: no row, no grant, no wiring). Blindness: the check reads the registry as JSON, the module through `terraform console`, and the shared-infra file as text; it cannot see an SCP, and it does not plan the shared-infra root (that plan is the act's own first step).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-22` (round 4, workstream `FENCEREG`; the CTO's round-3 ADDENDA 8 to 10)

Act 3b admits the readers of act 4 to the canonical home. `FB-g-19`, `FB-g-20` and `FB-g-21` made the module able to say
it; this cell SAYS it, in the registry, and wires the module's Allow into the bucket's policy file. You write two files and
apply nothing. The module already renders, from `infra/logic/registry/exemptions.json`, a Deny per scoped row, and (FB-g-21) an Allow beside each scoped
row and an Allow-only `grants` row.

### 1a. The rows (the whole permitted set -- add these and no other)

`KEY` is `advi/49financial/platinum/49financial/ownership_map.json` (the module's generated `ownership_key` for the firm; copy it, it is not a new value).
`GOLD` is `irpt/49financial/gold/holdings_performance_daily/`.

1. In `infra/logic/registry/exemptions.json`, bucket `opal-data-49financial`, append eight SCOPED rows after the existing ones (a row has `principal`,
   `arn`, `reason`, `signoff_ref`, `actions`, `prefix`; reason one sentence naming act 3b; `signoff_ref` the two pair paths
   `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT3B_ADMISSION_COO_HALF.md` and `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT3B_ADMISSION_CTO_HALF.md` followed by "unsigned at this write"):
   - six rows, one per principal `lambda-edge-execution-role`, `irpt-directory-role`, `irpt-export-render-role`,
     `irpt-narrative-role`, `irpt-status-role`, `irpt-ycharts-generate-role`: `arn` the role ARN in account 313476888478,
     `actions` `["s3:GetObject"]`, `prefix` `[KEY]` (a list holding the one exact key);
   - one row, `irpt-performance-adapter-role`: `actions` `["s3:GetObject", "s3:ListBucket"]`, `prefix` `[GOLD, KEY]`;
   - one row, principal and `arn` both `arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity E139998VWH0PD`,
     `actions` `["s3:GetObject"]` (NO ListBucket), `prefix` the nine canonical served-class prefixes, each ending `/`:
   - `advi/49financial/platinum/accounts/`
   - `advi/49financial/platinum/advisors/`
   - `advi/49financial/platinum/artifacts/`
   - `advi/49financial/platinum/clients/`
   - `advi/49financial/platinum/entities/accounts/`
   - `advi/49financial/platinum/entities/advisors/`
   - `advi/49financial/platinum/entities/clients/`
   - `advi/49financial/platinum/firm/`
   - `advi/49financial/platinum/views/`
2. In `infra/logic/registry/exemptions.json`, add the top-level object `grants` (it does not exist yet; FB-g-21 reads it): `"grants": {
   "opal-data-49financial": [ two rows ] }`, one for `irpt-holdings-role` and one for `irpt-49f-reporting-read-role`, each
   `principal` the role name, `arn` the role ARN, `reason`, `signoff_ref` as above, `actions` `["s3:GetObject"]`, `keys`
   `[KEY]`. Their existing admission (a full row for the first, the scope pattern for the second) is NOT touched.
3. Existing rows and every other bucket's rows stay byte-identical; do not reorder, reformat or re-indent the file beyond
   the lines you add (keep the file's own indentation).

### 1b. The wiring

4. In `infra/aws/terraform/shared-infra/s3-49financial.tf`: remove the three hand statements `DenyPerformanceAdapterAnyOtherAction`,
   `DenyPerformanceAdapterReadsOutsideTheHoldingsGold` and `DenyPerformanceAdapterListingOutsideTheHoldingsGold`, the
   `data "aws_iam_role" "irpt_performance_adapter"` block, the locals `f49_scope` and `f49_adapter_read_prefixes` (and the
   `locals` block if it empties), and the `[data.aws_iam_role.irpt_performance_adapter.arn]` entry of the blanket Deny's
   `ArnNotLike` list (the adapter is a registry row now, so `module.opal_name.fence_exemption_arns` carries it). Keep every
   other line.
5. In `infra/aws/terraform/shared-infra/s3-49financial.tf`: the statement list ends `], module.opal_name.fence_scoped_statements[aws_s3_bucket.opal_data_49financial.bucket])`;
   append `module.opal_name.fence_scoped_allow_statements[aws_s3_bucket.opal_data_49financial.bucket]` as a third argument of
   that `concat`, with a one-line comment above it naming act 3b and ADDENDUM 10. No other change.

## 2. BOUNDS

1. Files that change: `infra/logic/registry/exemptions.json` and `infra/aws/terraform/shared-infra/s3-49financial.tf`. Nothing else: no module file, no consumer root, no apply, no AWS write.
2. No row is typed that is not in section 1a. A principal, key or prefix outside it is a surprise row, not an edit.
3. ASCII only; LF endings in both files. If the commit is refused by the naming gate, do not override or force: file a BLOCKING
   row with the gate's lines.
4. `terraform init -backend=false` and `terraform plan` of the MODULE folder are local and allowed. Do not run a plan in the
   shared-infra root (it needs state and AWS); the check does not need it.

## 3. SURFACES

<paths>
infra/logic/registry/exemptions.json
infra/aws/terraform/shared-infra/s3-49financial.tf
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~44/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`, the two pair files named in the preflight.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~44/ADVI_FIRMBKTS.TO-FB-g-22.act3b-rows-and-wiring.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-22"><invocation>cd /c/dev/wk-firmbkts-44 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_policy.py --arms policy --root /c/dev/wk-firmbkts-44 --base a5637f273f; echo "exit=$?"</invocation><expect>ROUND 4 POLICY: 6 of 6 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-22"><invocation>cd /c/dev/wk-firmbkts-44 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-44 --allow infra/logic/registry/exemptions.json --allow infra/aws/terraform/shared-infra/s3-49financial.tf --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~44/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/logic/registry/exemptions.json --require infra/aws/terraform/shared-infra/s3-49financial.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the registry rows against the base (existing rows kept, the permitted set added), the grains (the generated key,
the gold prefix, the nine served prefixes, the actions), the module's render of the real registry (ten Allow principals, the
new exemptions, every other bucket unchanged), the file's wiring and the adapter's equivalence to its hand statements plus
the key. AC2 is the write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-22.act3b-rows-and-wiring.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~44`.
Commit the two files and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains it).
Row ids: `ADVI_FIRMBKTS-D1-W44-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 and AC2 outputs and the
commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut after `FB-g-21` merged. The exec-summary generator's rows are NOT here: its put
(`platinum/advisors/<id>/exec_summary.json`) is outside the fence grammar's Get and List and is an open call for the CTO at act 4b.
`partners-lambda-role` needs no row (its identity policy allows and the fence admits it). The act that applies this policy is
`FB-f-14`, staged under the act 3b pair; its executor is `0.7.0_AE_CloudOps~FBL` if `PutBucketPolicy` is refused to dell1.
Workstream `FENCEREG`. Class WORLD by the path floor, inert until applied.

<status>complete</status>
<round>4</round>
<workstream>FENCEREG</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-22</to_id>
<slot>~44</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
