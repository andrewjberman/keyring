# ADVI_FIRMBKTS task order -- `FB-g-28` -- ACT 4b'S IDENTITY SIDE: THE EXEC-SUMMARY GENERATOR'S NARROW PUT AT THE CANONICAL HOME

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-28</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~50</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one repository file; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: RUN by the issuer -- this cell WRITES one new inline policy of a role and applies none of it. The permitted set (one action, one ARN pattern), the writers counted and both branches are in `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT4BC_LAMBDAS_COO_HALF.md` (amended for ADDENDA 10 and 11). Its apply is a separate staged order.
comp-adversary: RUN by the issuer -- at base `r4_execiam.py` reads 3 of 5 (I3, I4 and I5 PASS as controls; I1 and I2 FAIL as expected: no new resource). Blindness: the check reads iam.tf as text and the module through `terraform console`; it does not plan the exec-summary root.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-28` (round 4, workstream `EXECIAM`; the CTO's round-3 ADDENDUM 11)

The CTO's standing rule: generated bucket-policy Allows are read-only, and writes live identity-side in the writer's root. The
exec-summary generator writes `platinum/advisors/<id>/exec_summary.json`; after act 4b it must write the same key under the
canonical home. Add a NEW inline policy to the generator's role granting `s3:PutObject` on exactly that key pattern at the
canonical home. Condition 1 of ADDENDUM 11: no `PutObjectAcl` at the new home (the legacy policy keeps its own).

### 1a. Behavior (the whole spec)

1. In `infra/aws/terraform/exec-summary/iam.tf` add ONE new resource, after the existing policy resource:
   - `resource "aws_iam_role_policy" "exec_summary_canonical_put"` with `role = aws_iam_role.exec_summary_generator.id`;
   - its `name` is `module.<call>.name` of a NEW module call to `../../modules/opal_name` with `system = "advi"`,
     `scope = "49financial"`, `function = "exec-summary-canonical-put"`, `kind = "policy"` (follow
     `infra/aws/terraform/bd-pipeline/iam.tf`'s `module "opal_name_platinum_grant"`, the same shape); never a typed name;
   - ONE statement: `Sid = "ExecSummaryCanonicalPut"`, `Effect = "Allow"`, `Action = ["s3:PutObject"]`, `Resource` exactly one
     entry `"arn:aws:s3:::${module.<call>.bucket}/${lookup(module.<call>.class_prefix, "platinum/advisors/")}*/exec_summary.json"`;
     no `Condition`, no other key, no other action.
2. A short comment above the new resource: act 4b's put at the canonical home, ADDENDUM 11, the bucket policy's Allow for this
   role is read-only. Comment lines only.
3. Everything else in the file and every other file stays byte-identical. `terraform fmt` must read clean.

## 2. BOUNDS

1. One file changes: `infra/aws/terraform/exec-summary/iam.tf`. No other file, no module change, no apply, no plan in the exec-summary root, no AWS call.
2. No key literal is typed except the `lookup()` argument and the `*/exec_summary.json` suffix. If the commit is refused by the
   naming gate, do not override or force: file a BLOCKING row with the gate's lines.
3. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
infra/aws/terraform/exec-summary/iam.tf
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~50/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~50/ADVI_FIRMBKTS.TO-FB-g-28.exec-summary-put-policy.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-28"><invocation>cd /c/dev/wk-firmbkts-50 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_execiam.py --arms iam --root /c/dev/wk-firmbkts-50 --base 44e7a3f712; echo "exit=$?"</invocation><expect>ROUND 4 EXEC IAM: 5 of 5 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-28"><invocation>cd /c/dev/wk-firmbkts-50 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-50 --allow infra/aws/terraform/exec-summary/iam.tf --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~50/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/terraform/exec-summary/iam.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the new resource (named by a module call, one Allow statement, `s3:PutObject` only, one generated ARN), that the
module resolves the canonical directory, that nothing else of the root changed and that the formatter is clean. AC2 is the
write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-28.exec-summary-put-policy.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~50`.
Commit the file and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains it).
Row ids: `ADVI_FIRMBKTS-D1-W50-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 and AC2 outputs and the
commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** act 4b's identity side (ADDENDUM 11: one scoped apply of one new policy in the exec-summary root). It may be
applied before the window: it grants a write at a home nobody writes until 4b, inert like 3b. Workstream `EXECIAM`. Class WORLD
by the path floor.

<status>pending</status>
<round>4</round>
<workstream>EXECIAM</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-28</to_id>
<slot>~50</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
