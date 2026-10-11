# ADVI_FIRMBKTS task order -- `FB-g-27` -- ACT 3c: THE EXEC-SUMMARY GENERATOR'S FENCE ROW FOR THE CANONICAL ADVISORS DIRECTORY (REGISTRY ROW ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-27</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~49</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one registry file; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: RUN by the issuer -- this cell WRITES one row of a bucket-policy change and applies none of it. The permitted set, the writers counted and both branches are in `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT3C_EXECSUM_FENCE_COO_HALF.md` (COO half; the CTO half `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT3C_EXECSUM_FENCE_CTO_HALF.md` precedes the apply, not this commit). The Put the row exempts is granted identity-side in the writer's root (`FB-g-28`); the module renders no Allow for a write.
comp-adversary: RUN by the issuer -- at base `r4_exec.py` reads 2 of 4 (E3 other buckets unchanged and E4 clean plan PASS as controls; E1 and E2 FAIL as expected: no row). Blindness: the check reads the registry as JSON and the module through `terraform console`; it cannot see an SCP and does not plan the shared-infra root.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-27` (round 4, workstream `EXECROW`; the CTO's round-3 ADDENDA 10 and 11)

Act 4b moves the exec-summary generator to the canonical home: it READS the advisors directory there and PUTS
`exec_summary.json` under it. The fence must exempt that one role for those actions on that one directory, so the Get and
List are rendered by the module as a bucket-policy Allow beside the Deny row (ADDENDUM 10), and the Put is exempted on the Deny
side only (ADDENDUM 11, `FB-g-23`; the Allow for it is identity-side, `FB-g-28`).

### 1a. The row (the whole permitted set -- add this and nothing else)

In `infra/logic/registry/exemptions.json`, bucket `opal-data-49financial`, append ONE scoped row after the existing ones (the last row now is the OAI's):
- `principal` `exec-summary-generator-role`; `arn` `arn:aws:iam::313476888478:role/exec-summary-generator-role`;
- `reason` one sentence naming act 3c, act 4b and the CTO's ADDENDUM 11;
- `signoff_ref` the two pair paths `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT3C_EXECSUM_FENCE_COO_HALF.md` and `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT3C_EXECSUM_FENCE_CTO_HALF.md` followed by "unsigned at this write";
- `actions` `["s3:GetObject", "s3:ListBucket", "s3:PutObject"]` (no `s3:PutObjectAcl`, no Delete, no `s3:*`);
- `prefix` `["advi/49financial/platinum/advisors/"]` (one directory, ending `/`: the module's `class_prefix` for the legacy class `platinum/advisors/`;
  copy it, it is not a new value).

Existing rows, every other bucket's rows and the `grants` object stay byte-identical; keep the file's own indentation.

## 2. BOUNDS

1. One file changes: `infra/logic/registry/exemptions.json`. No module file, no shared-infra file, no apply, no AWS call.
2. No other row, key or prefix. Anything outside section 1a is a surprise row, not an edit.
3. ASCII only; LF endings. If the commit is refused by a gate, do not override or force: file a BLOCKING row with the gate's
   lines.

## 3. SURFACES

<paths>
infra/logic/registry/exemptions.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~49/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`, the two pair files named in the preflight.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~49/ADVI_FIRMBKTS.TO-FB-g-27.exec-summary-fence-row.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-27"><invocation>cd /c/dev/wk-firmbkts-49 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_exec.py --arms row --root /c/dev/wk-firmbkts-49 --base 44e7a3f712; echo "exit=$?"</invocation><expect>ROUND 4 EXEC ROW: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-27"><invocation>cd /c/dev/wk-firmbkts-49 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-49 --allow infra/logic/registry/exemptions.json --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~49/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/logic/registry/exemptions.json; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the registry against the base (one scoped row added, the grains, the actions), the module's render (the Get and
List Allows, the Put on the Deny side, no write Allow, one new exemption) and that every other bucket renders unchanged. AC2 is
the write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-27.exec-summary-fence-row.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~49`.
Commit the file and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains it).
Row ids: `ADVI_FIRMBKTS-D1-W49-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 and AC2 outputs and the
commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the exec-summary's rows, deferred from act 3b by the CTO's ADDENDUM 11. The apply is act 3c (`FB-f-17`, one
bucket policy again), inert like 3b, before act 4b. Workstream `EXECROW`. Class WORLD by the path floor.

<status>pending</status>
<round>4</round>
<workstream>EXECROW</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-27</to_id>
<slot>~49</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
