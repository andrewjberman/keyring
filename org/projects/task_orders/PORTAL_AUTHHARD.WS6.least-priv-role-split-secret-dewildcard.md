<task_order>
<metadata>
  <to_id>PORTAL_AUTHHARD.WS6</to_id>
  <project>PORTAL_AUTHHARD</project>
  <title>Least-privilege role split + secret de-wildcarding -- split opal-portal-lambda-role (isolate the PUBLIC authorizer first), replace secret:opal/* wildcards with explicit per-role allowlists, add dynamodb:LeadingKeys on partner tables. GROUNDING-FIRST -> CTO~B arch-gate + never-widen co-sign. Wave 2.</title>
  <assigned_to>0.7.0_AE_CloudOps~B</assigned_to>
  <issued_by>1.0.0_SA_CTO~B</issued_by>
  <issued_date>2026-07-20</issued_date>
  <status>complete -- SPRING-CLEAN 2026-08-25 (S2): <project> field repaired from "PORTAL_AUTHHARD (Portal Auth/Authz + Abuse-Resistance Harden" to PORTAL_AUTHHARD, which is closed. Closed as a record act, not a work verdict. Prior status: ISSUED -- QUEUED after WS-2b. GROUNDING (the role->Lambda->secret map) is read-only and MAY start in parallel if idle; NO TF change before CTO~B arch-gate + never-widen co-sign on the split.</status>
  <dispatch_held>true</dispatch_held>
  <priority>MEDIUM -- Wave 2 (after WS-2b). The most security-consequential Wave-2 item (a PUBLIC authorizer sharing a secret-reading role).</priority>
  <references>
    <ref type="prd">docs/architecture/PORTAL_AUTHHARD_PRD.md WS-6 (+ S2.4 DynamoDB LeadingKeys transform)</ref>
    <ref type="brief">docs/briefs/PORTAL_AUTH_HARDENING_BRIEF_20260720.md G5</ref>
    <ref type="grounding">terraform/portal-auth/cross-firm-secret-deny.tf:8-18 -- surgical opal/bd/* Deny SHIPPED, but wildcard->allowlist narrowing + per-function split "still being grounded". opal-portal-lambda-role = SHARED behind 11 Lambdas incl the PUBLIC authorizer; other wildcard holders opalinvest-auth-lambda-role + news-ingestion-lambda-role; yang-pipeline-lambda-role region-scoped-safe. The deny.tf grounding already found 0 code paths in the 4 roles read opal/bd/*. -- CTO~B @HEAD 2026-07-20</ref>
    <ref type="proposal">Andrew proposal S6.7/S6.11 (least-privilege Lambda roles; a function that only reads basic info should not hold credentials to all prod data)</ref>
    <ref type="rule">Rule 22a (comp-iam models (action) not (action,resource) + fails GREEN -> raw simulate-principal-policy, one --resource-arns/call, isolated positive control) + never-widen co-sign (CTO~B + COO~Z) on any non-pure-add TF plan</ref>
  </references>
</metadata>

<scope>
The shared opal-portal-lambda-role sits behind 11 Lambdas INCLUDING the PUBLIC API-GW authorizer, and portal/auth/news
roles held secret:opal/* wildcards. cross-firm-secret-deny.tf surgically Denied opal/bd/* (shipped) but the underlying
wildcard->explicit-allowlist narrowing + per-function split is explicitly deferred ("still being grounded").

>> GROUNDING-FIRST (bring me the map before proposing any split) <<
Enumerate, per the deny.tf method extended to the FULL prefix set: for opal-portal-lambda-role's 11 Lambdas +
opalinvest-auth-lambda-role + news-ingestion-lambda-role, which secret PREFIXES each Lambda ACTUALLY reads (env vars,
string literals, get_secret() wrappers, SSM/DDB/S3-sourced ids, constructed ids -- ALL expression forms, as the deny.tf
did). Output = a role -> Lambda -> used-secret-prefix map. THIS IS THE DENOMINATOR the allowlist rests on; a missed
read path = a broken Lambda post-narrowing.

DELIVERABLE (after I arch-gate the map + the split design):
1. SPLIT opal-portal-lambda-role by responsibility, ISOLATING THE PUBLIC AUTHORIZER FIRST -- a public-reachable Lambda
   must not share a role that can read production secrets. The authorizer's role gets ONLY what it needs (verify keys +
   its own table reads); nothing else.
2. Replace the secret:opal/* WILDCARDS on the portal/auth/news roles with EXPLICIT per-role allowlists of the prefixes
   the grounding proved each uses. (The deny.tf Deny stays -- belt; the allowlist is the narrowing it deferred.)
3. Apply dynamodb:LeadingKeys condition keys on the partner tables (the DynamoDB row-level-security analog, PRD S2.4) so
   a role can only read partitions it owns.

DISCIPLINE: NEVER-WIDEN. This changes existing IAM -> a non-pure-add plan -> CTO~B arch-gate + COO~Z never-widen co-sign
BEFORE apply. Terraform-only, safe-apply. Each role narrowing must be exercised against a currently-used prefix
(prove the Lambda still works) AND a now-denied prefix (prove the narrowing bit). Split in small reversible steps, not
one big-bang role swap on 11 live Lambdas.
</scope>

<acceptance>
EXERCISE-based (Rule 22a/22b) -- grounded on APPLIED state + the live primitive:
- [ ] The role->Lambda->secret-prefix map delivered + CTO~B-reviewed BEFORE any split; the split design + TF plan
      arch-gated + COO~Z never-widen co-signed BEFORE apply.
- [ ] After split: aws iam simulate-principal-policy (ONE --resource-arns/call, positive control in ISOLATION) proves
      the ISOLATED authorizer role CANNOT GetSecretValue on a prod secret it shouldn't, and CAN read exactly what it
      must. Live get-role-policy shows the wildcard GONE, replaced by the allowlist. **CVO R-1 LESSON (Wave-1): when a
      simulate result carries a non-empty Missing[], the implicitDeny may be a CONDITION-driven FALSE-deny (Rule 22a
      mode 2), NOT a real policy deny -- pass --context-entries to satisfy the condition and re-confirm the deny is
      real (Missing=[]). A secret-plane role often carries conditioned statements, so this WILL bite here.**
- [ ] Every one of the 11 Lambdas still functions post-narrowing (exercise a real read path per role, or the scheduled
      path that uses it) -- no Lambda broken by an over-narrow allowlist.
- [ ] dynamodb:LeadingKeys exercised: a cross-partition read is denied, an owned-partition read allowed.
- [ ] RAVC to CTO~B (CC MSTR + COO~Z for the co-sign record); CVO independent exercise-verify.
</acceptance>
</task_order>
