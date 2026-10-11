# ADVI_FIRMBKTS task order -- `FB-g-25` -- THE ACT-0 GRANT GAINS ONE NARROW `s3:DeleteObject` STATEMENT (THE CTO'S ACT-0 ADDENDUM 1, ITEM 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-25</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~48</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one repository file; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: RUN by the issuer -- this cell WRITES one statement of a role policy and applies none of it. The permitted set (one action, two directories printed from the code), the writers counted and both branches are in the act-0 pair's addenda (`org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT0_GRANT_CTO_HALF.md` ADDENDUM 1, signed; the COO addendum is written beside this cell). The act that applies the policy is a separate staged order.
comp-adversary: RUN by the issuer -- at base `r4_delgrant.py` reads 3 of 5 (G3 delete roots read from the code, G4 module directories and G5 dormant PASS as controls; G1 and G2 FAIL as expected: no Delete statement). Blindness: the check reads iam.tf as text and the module through `terraform console`; it does not plan the bd-pipeline root (the act's own first step).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-25` (round 4, workstream `DELGRANT`; row D1-S29; the CTO's act-0 ADDENDUM 1, msg 3931)

The producers' role holds an inline policy (act 0, applied) that allows Put, Get and List on the canonical platinum prefix and
no Delete. `D_04` (`platinum/advisors/<id>/`) and `D_02` (`gold/entities/advisors/<id>/`) delete a DEPARTED advisor's files
under exactly two directories. Add ONE statement to the same policy resource granting `s3:DeleteObject` on those two
directories and nothing else. The directories come from the module's `class_prefix` output (`FB-g-24`), never typed.

### 1a. Behavior (the whole spec)

1. In `infra/aws/terraform/bd-pipeline/iam.tf`, in the `aws_iam_role_policy.bd_exporter_advi_49f_platinum_canonical` resource's statement list, append a
   THIRD statement after `AdviPlatinumCanonicalList`:
   - `Sid = "AdviPlatinumCanonicalDelete"`, `Effect = "Allow"`, `Action = ["s3:DeleteObject"]`;
   - `Resource` exactly two entries, in this order, each
     `"arn:aws:s3:::${module.opal_name_platinum_grant.bucket}/${lookup(module.opal_name_platinum_grant.class_prefix, "<legacy prefix>")}*"`
     for the legacy prefixes `platinum/advisors/` and then `gold/entities/advisors/`;
   - no `Condition`, no other key, no other action.
2. Update the comment block above the resource: replace its "No DeleteObject" claim with one sentence saying the third
   statement is the stale-advisor cleanup's narrow delete (row D1-S29, the CTO's act-0 ADDENDUM 1), two advisor directories,
   generated through `class_prefix`. Comment lines only.
3. Everything else in the file, and every other file, stays byte-identical. `terraform fmt` must read clean on the file.

## 2. BOUNDS

1. One file changes: `infra/aws/terraform/bd-pipeline/iam.tf`. No other file, no module change, no apply, no plan in the bd-pipeline root, no AWS call.
2. No key literal is typed in the statement except the two legacy-prefix arguments of `lookup()`. If the commit is refused by
   the naming gate, do not override or force: file a BLOCKING row with the gate's lines.
3. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
infra/aws/terraform/bd-pipeline/iam.tf
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~48/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~48/ADVI_FIRMBKTS.TO-FB-g-25.delete-grant-statement.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-25"><invocation>cd /c/dev/wk-firmbkts-48 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_delgrant.py --arms grant --root /c/dev/wk-firmbkts-48 --base ab97247bd3; echo "exit=$?"</invocation><expect>ROUND 4 DELETE GRANT: 5 of 5 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-25"><invocation>cd /c/dev/wk-firmbkts-48 &amp;&amp; timeout 60 terraform fmt -check infra/aws/terraform/bd-pipeline/iam.tf; echo "fmt_rc=$?"</invocation><expect>^fmt_rc=0$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-25"><invocation>cd /c/dev/wk-firmbkts-48 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-48 --allow infra/aws/terraform/bd-pipeline/iam.tf --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~48/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/terraform/bd-pipeline/iam.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the policy's three statements (the two base statements unchanged, one new Delete statement), its two generated
resources, that the two legacy prefixes are the directories the code deletes under, the module's resolved directories and
that nothing else of the root changed. AC2 is the formatter. AC3 is the write-surface bound. Each invocation terminates
inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-25.delete-grant-statement.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~48`.
Commit the file and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains it).
Row ids: `ADVI_FIRMBKTS-D1-W48-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs and the
commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut after `FB-g-24` merged (ab97247bd3) and `FB-g-26` merged (b3a1f43daa). The apply is the act-0
addendum's act (`FB-f-16`, `0.7.0_AE_CloudOps~FB1`, scoped plan `1 to change` on the one policy) and must land before act 2.
The directories, read from the code and printed: `D_04.client_portal_summary.py:789-812` lists `platinum/advisors/<id>/`;
`D_02.advisor_client_detail.py:3252-3265` lists `advisor_book_key('_').rsplit('/', 2)[0] + '/'` = `gold/entities/advisors/`.
Workstream `DELGRANT`. Class WORLD by the path floor, inert until applied.

<status>pending</status>
<round>4</round>
<workstream>DELGRANT</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-25</to_id>
<slot>~48</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
