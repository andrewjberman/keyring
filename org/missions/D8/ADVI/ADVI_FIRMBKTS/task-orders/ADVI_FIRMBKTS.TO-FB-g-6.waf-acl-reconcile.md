# ADVI_FIRMBKTS task order -- `FB-g-6` -- THE WAF ACL RECONCILE: A `portal-auth` PLAN THAT READS NO ACL CHANGE (row D1-S12)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed; the cell edits one Terraform file and reads a plan. Nothing is applied.
comp-iam: RUN by the issuer -- the plan reads under the identity the round-3 act-1 plan ran under (refresh and read of the portal-auth root); the cell creates no grant and writes nothing to AWS.
comp-adversary: RUN by the issuer -- at base the live plan names `aws_wafv2_web_acl.opal_cloudfront_protection` (row D1-S12: three managed groups differ in `managed_rule_group_statement.version`, '' before and null after); `r4_waf.py` reads 2 of 3 at base (A1 FAILS: no file changed; A2 and A3 PASS as controls). Blindness: the text check cannot see the provider's plan; the plan criterion is the oracle and is yours to run.
EGRESS CLASS, declared: NONE (read-only AWS describe calls inside the account).
</preflight>

## 1. THE CELL -- `FB-g-6` (round 4, enrichment item 4; the CTO's S12 ruling, `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round3.md` section 2)

`infra/aws/terraform/portal-auth/waf-cloudfront.tf` declares `aws_wafv2_web_acl.opal_cloudfront_protection`. Its plan lists the ACL as an update on
every run: the three managed rule groups (`ip-reputation` p3, `common-rule-set` p4, `known-bad-inputs` p5, all
`override_action count`) differ only in `managed_rule_group_statement.version`, `""` in state and `null` in config. A
`-target` plan cannot exclude it because the CloudFront distribution depends on the ACL, so every apply in this root has
carried it as a named rider (row D1-S12; act 1's ADDENDUM 1). The CTO ruled the ACL reconciled in Terraform so that a
`portal-auth` plan reads NO ACL change: `lifecycle { ignore_changes }` on the three groups' `version`, or an explicit
`null`. **You make the plan read no ACL change by the smallest edit inside that one resource, and you prove it with the
plan.**

### 1a. Steps

0. Work in `/c/dev/wk-firmbkts-30` (a linked worktree the issuer provisioned from the dell1 branch). Begin every shell call with
   `cd /c/dev/wk-firmbkts-30 &&`. Initialise the root once: `cd /c/dev/wk-firmbkts-30/infra/aws/terraform/portal-auth && terraform init -input=false -no-color` (a read of the
   backend and providers; it changes no infrastructure).
1. Take the plan as it stands: `terraform plan -input=false -lock=false -refresh=true -no-color
   -target=aws_wafv2_web_acl.opal_cloudfront_protection`. Record that it shows the ACL update and which attributes.
2. Edit `waf-cloudfront.tf` inside the ACL resource only. Try, in this order, reading the plan after each: (i) the
   CTO's first form, `ignore_changes` naming the groups' `version` (note: Terraform cannot index a SET of nested blocks,
   and a comment in this file records that `ignore_changes = [rule]` on the whole array was refused earlier, so if the
   provider rejects the path say so and move on); (ii) the CTO's second form, an explicit `version = null` on each of
   the three `managed_rule_group_statement` blocks; (iii) if neither clears the plan, the smallest third form that does
   while changing no rule name, priority, action, override or statement, and say which in the report.
3. When the targeted plan reads `No changes`, run the FULL root plan (no `-target`) and record its resource-change
   list: the ACL must not appear in it. (Other resources may appear for their own reasons; list them.)
4. `terraform fmt` the file. Commit with `.tools/safe-commit.sh` under your own serial. Do NOT run `apply`.

## 2. BOUNDS

1. One file changes: `infra/aws/terraform/portal-auth/waf-cloudfront.tf`. No other Terraform file, no variable, no state operation, no `import`, no
   `apply`, no AWS write. A plan writes only its local `.terraform` working directory and `-out` file (keep any plan file
   under your deliverables folder, uncommitted).
2. No rule is added, removed, renamed, re-prioritised or moved from `count` to `block`: the ACL's behavior at the edge
   does not change by one request. If the only clearing form changes behavior, stop and file a BLOCKING row.
3. ASCII only; LF endings.

## 3. SURFACES

<paths>
infra/aws/terraform/portal-auth/waf-cloudfront.tf
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-g-6.waf-acl-reconcile.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-6"><invocation>cd /c/dev/wk-firmbkts-30/infra/aws/terraform/portal-auth &amp;&amp; timeout 118 terraform plan -input=false -lock=false -refresh=true -no-color -target=aws_wafv2_web_acl.opal_cloudfront_protection 2&gt;&amp;1 | tail -n 8</invocation><expect>No changes</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-6"><invocation>cd /c/dev/wk-firmbkts-30 &amp;&amp; timeout 100 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_waf.py --arms waf --root /c/dev/wk-firmbkts-30; echo "exit=$?"</invocation><expect>ROUND 4 WAF: 3 of 3 arms</expect></criterion>
</proof_of_spec>

AC1 is the oracle (the provider's own plan, read-only). AC2 is the bound: only `waf-cloudfront.tf` changed, the six rule
blocks are identical apart from `version` lines, and the file is formatted. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-6.waf-acl-reconcile.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1`. Commit
the file, then the instance second; flip this order's `<status>` to `complete` in the SAME commit as the instance only
when AC1 and AC2 pass. Row ids: `ADVI_FIRMBKTS-D1-FB1-S<k>` from the next unused number, `surfaced_at` from
`date -u +%FT%TZ`. Report once to `2.0.0_SA_COO~B1`: the form that cleared the plan, the full-root plan's resource-change
list, AC1 and AC2 outputs, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** a seat order, not a worker spawn: the plan needs the CloudOps identity and judgment about the provider's
behavior (the task order's own AC1 is the provider, not a text read). Class WORLD by the path floor; the cell applies
nothing, and if the cleared plan is a no-op the later `portal-auth` apply carries no ACL rider. The CVO's packet of
round 3 recorded the rider as ruled in act 1's ADDENDUM 1; this cell retires it.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-11 ~12:4xZ, WITHDRAWN):** `0.7.0_AE_CloudOps~FB1` (msg 3847, row D1-S22) read the
provider's own plan for each form the ruling named: `ignore_changes` on the three `version` paths errors ("Cannot index a set
value"), an explicit `null` has no effect, `version = ""` is refused by the schema; only `ignore_changes` on the whole `rule`
array reads No changes, which this file's comments record as refused. The CTO ruled (msg 3854, round-3 ADDENDUM 5): keep the
named rider; S12 closes "not reconcilable; standing rider"; it reopens only if the provider can ignore a set member. The order
is withdrawn with nothing changed (the file is byte-identical to base; nothing was applied). Gate limb: a status change on an
existing order is graded by no limb (GATE viii reads `<placeholders>` at HEAD: `NONE`).

<status>withdrawn</status>
<round>4</round>
<to_id>ADVI_FIRMBKTS.TO-FB-g-6</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
