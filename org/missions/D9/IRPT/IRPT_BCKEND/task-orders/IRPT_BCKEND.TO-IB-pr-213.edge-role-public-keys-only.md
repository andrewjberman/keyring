# TO IRPT_BCKEND.TO-IB-pr-213 -- The Lambda@Edge role reads only the public verification keys (row S132)

<to_id>IRPT_BCKEND.TO-IB-pr-213</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~69</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ROUND-19 ANALYSIS section 3 (S132 P2 to
2.0.0_SA_COO~P, shared auth, writer table) | **Decomp cell:** `IB-pr-213` (decomposition section 18) | **outcome_ref:**
PRD item 1 (a separate signing key; least privilege for verifiers) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-pr-213` -- Row S132: the Lambda@Edge role (`lambda-edge-execution-role`, policy `lambda-edge-secrets-logs`,
`C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/terraform/portal-auth/iam.tf` around lines 287-298) grants
`secretsmanager:GetSecretValue` on `arn:aws:secretsmanager:us-east-1:${local.account_id}:secret:opal/auth/*`. That
includes BOTH private signing keys (`opal/auth/jwt-private-key` and `opal/auth/irpt-render-jwt-private-key`).

The edge validator reads only two public keys:
- `opal/auth/jwt-public-key` (`infra/aws/lambda/lib/authkeys/jwtPublicKeys.mjs:57`, imported by
  `infra/aws/lambda-edge/auth-validator-edge/index.mjs:78`);
- `opal/auth/irpt-render-jwt-public-key` (`infra/aws/lambda-edge/auth-validator-edge/render_auth.mjs:17`).

**Build:** narrow that statement's `Resource` to exactly those two secrets, each as
`...:secret:opal/auth/<name>-*` (Secrets Manager appends a 6-character suffix to an ARN). Leave every other
statement unchanged. Run `terraform fmt` on the file and `.tools/terraform.exe plan` in the portal-auth root. Report
the plan's resource lines: expected ONE in-place update, to `aws_iam_role_policy.lambda_edge_secrets_logs`.

Do NOT apply. The apply touches the shared edge validator: it is the issuer's served act, under both never-widen
halves, with a live before/after of the human-token path.

### ACCEPTANCE (run from your worktree root)

<criterion id="P21-3-AC1" cell_refs="IB-pr-213"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r21/p21_3_ac1_edge_policy_source.py" .</invocation><expect>P21-3-AC1 PASS</expect></criterion>
`P21-3-AC1` -- the GetSecretValue statement names exactly the secrets the edge code reads, all public keys, none a
bare wildcard. Base: FAIL (`opal/auth/*`). Positive control, run at the cut: a copy narrowed to the two names PASSES.

<expected_criteria>P21-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **No apply.** `terraform plan` only, with `-lock=false`; never `apply`, never `safe-apply`.
- **Refusal clause.** If the edge code reads a secret beyond these two, stop, write it in your report and a surprise
  row, and do not widen the check.

<paths>
infra/aws/terraform/portal-auth/iam.tf
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 18 (round 21, workstream ~P), cell `IB-pr-213`.
<owned_cells>IB-pr-213</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P21-3-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~69/IRPT_BCKEND.TO-IB-pr-213.edge-role-public-keys-only.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P21-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, the criterion's last line, the plan's resource lines, and any surprise
row id (`IRPT_BCKEND-W69-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: RUN -- denominator: 1 role (lambda-edge-execution-role), 1 of its statements narrowed; live grant read at the cut: GetSecretValue on opal/auth/* (p21_3_live_after_read.py FAIL at base).
comp-blast: RUN -- the edge validator's secret reads (2 names, census above); the issuer's served act carries the human-token before/after.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- the edge's key cache is unchanged.
comp-adversary: RUN -- P21-3-AC1 dry-run at the base: FAIL; positive control (a copy narrowed to the two names) PASS.
lane: the <paths> block IS the grant.
</preflight>
