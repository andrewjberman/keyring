# TO POSN_AGGFIX.TO-C1-1 -- THE EDGE REFUSES THE AGGREGATE TO ANYONE OUTSIDE OPAL: every URL that reaches the Opal-only key censused, the refusal built into the viewer-request function right after the JWT verify, deployed under both never-widen halves, and exercised live for Opal staff, a Dev user, an advisor and a client (AF1-s-4, AF1-s-11; FWD-7, FWD-2)

<to_id>POSN_AGGFIX.TO-C1-1</to_id>
<project>POSN_AGGFIX</project>
<issued_to>0.9.0_WK_POSN_AGGFIX~2</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D4 - **Macro:** POSN - **Fabric:** site-z - **PRD:** `org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md` **v0.2**
@`cbd85e5cff` (C-OPAL-ONLY-DATA, C-EXISTING-PREDICATE, C-NEVER-WIDEN) - **Decomp cells:** `AF1-s-4`, `AF1-s-11` - **Issuance:** round 1,
slot `~2`, the only order in this slot's queue; runs in PARALLEL with slots `~1` and `~3`, whose files are disjoint from yours.
THIS ORDER CHANGES SERVED BEHAVIOUR ON EVERY PORTAL REQUEST THE FUNCTION SEES.

---

## IDENTITY AND THE FIRST ACT

You are `0.9.0_WK_POSN_AGGFIX~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_POSN_AGGFIX~2;`. Your worktree is
`/c/tmp/wk-aggfix-1-2` (branch `wk-posn_aggfix-1-2`, a sparse cone cut by the COO from SITEZ; do NOT re-create it). First act:
`git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`. Commit ONLY via
`bash .tools/safe-commit.sh --author "0.9.0_WK_POSN_AGGFIX~2 <0.9.0_WK_POSN_AGGFIX~2@opal.agent>" -F <msgfile> -- <paths>` (msgfile by
the Write tool, PURE ASCII). Never push, merge, rebase, `checkout --`, `clean`. Scratch in `/c/tmp/wk-aggfix-1-2/.scratch/` only.
**Immediately before your first `safe-apply`**, run
`printf '%s\n' 0.9.0_WK_POSN_AGGFIX~2 > "/c/Users/Opal Bloomberg/Desktop/ajb_workspace/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"`.
**Secrets:** the ONLY secret this order reads is `opal/auth/jwt-private-key`, through `comp-secrets get opal/auth/jwt-private-key
--reveal`, captured inside the process that signs; the key and every token are NEVER printed, written to a file, placed in argv or
committed. Tokens are short-lived (`exp` no more than 300 s after `iat`) with `sub` = `qa-posn-aggfix-<class>`. If the key cannot be read
that way, the live token arms are REFUSED with a row, never replaced by another route.

## THE CELLS (verbatim from the decomposition @`605c03f81f`)

**`AF1-s-4` -- where a tier refusal runs, and every URL that reaches the key (S4, C-OPAL-ONLY-DATA).** Read in order
`infra/aws/lambda-edge/shared-advisor-router/index.mjs`, `infra/aws/lambda-edge/auth-validator-edge/index.mjs` (the handler :210 onward
whole) and `infra/aws/lambda-edge/public-data-router/index.mjs`; list every CloudFront behaviour whose path pattern and rewrite can reach
`json/positioning/opal_aggregate.json` (`comp-routes behaviors` / `rewrites`, denominator printed) and which of them associate
`auth-validator-edge` at viewer-request; record whether the proxy docstring's "blocks client tier" for
`/api/general/positioning/model.json` (`portal-proxy.ts:1419-1426` @edf85ce503) is true by exercising that URL live with a client token. A
live exposure found elsewhere is a surprise row, not this project's fix.

**`AF1-s-11` -- the edge refuses the aggregate to anyone outside Opal, deployed and exercised live (S11, C-OPAL-ONLY-DATA).** In
`infra/aws/lambda-edge/auth-validator-edge/`: ONE new pure module `aggregate_gate.mjs` exporting the URI match (both forms, 1.2) and the
admit predicate (`firmId === 'opal-capital' || userType === 'Dev'`), called from `index.mjs` right after the JWT verify, returning
`unauthorized(...)` with one structured log line `aggregate_denied` (no metric filter, no alarm: the moratorium). A unit harness drives
`handler` with synthetic viewer-request events whose JWT verify is replaced in-process: four viewer classes (Opal staff, Dev, advisor,
client) x the two aggregate URLs x a control URL (`/api/general/positioning/positioning_data.json`). Deployed under
`ledger/NEVER_WIDEN_ROUND1_EDGE_GATE_COO_HALF.md` and `..._CTO_HALF.md`: ledger entry; build; plan `-target`ed to the function and the
distribution; `safe-apply`; re-plan; the LIVE distribution association version equals the newly published version on every behaviour that
associates the function (N of N printed); live arms with short-lived tokens for the four classes on both URLs and the control.

**Decomposition s.1.2, the design facts this cell is cut against (MEASURED by the issuer at SITEZ HEAD and portal `edf85ce503`; read each
back):** `public-data-router/index.mjs` (71 lines) rewrites `/api/general/json/*` -> `/json/*` (:45-48) and `/api/general/*` -> `/json/*`
(:63-66) with NO tier branch, so BOTH `/api/general/positioning/opal_aggregate.json` and `/api/general/json/positioning/opal_aggregate.json`
reach the key. `auth-validator-edge/index.mjs` verifies the RS256 JWT (`verifyWithSlots` :234), holds the claims `firmId` and `userType`
(:9-12), denies with 401 not 403 after the verify (:33, :236-260), and its tier gate covers `/api/scoped/advisor-intelligence/*` only
(`tier_policy.mjs:25-26`). The page's predicate (`src/contexts/AuthContext.tsx` @edf85ce503): `isInternal` = `claims.firmId ===
'opal-capital'` (:736-737), `isDev` = `claims.userType === 'Dev'` (:750-751), `userType` normalised to `'Dev'` or null (:118-119). The gate
does NOT use `tier === 'internal'` (the page's own comment :756: "With tier removed, internal = firmId opal-capital"). Terraform:
`infra/aws/terraform/portal-auth/lambda-edge.tf:84-127` (`publish = true`; `ignore_changes = [source_code_hash]` only, the qualified_arn pin
DROPPED 2026-09-09 :106-121), associated through `cloudfront-distribution.tf:65`; build per `lambda-edge.tf:9`; **the post-apply proof is the
LIVE association version (lambda-edge.tf:42-68), never the re-plan**; distribution `EVTSA9VEHNZVH`. Whole-root plan at the cut: `0 to add,
1 to change, 0 to destroy`, the change `aws_wafv2_web_acl.opal_cloudfront_protection` in place -- PRE-EXISTING DRIFT, kept out of your
targeted plan.

**The two halves and the rule they bind you to.** Read both (`git show SITEZ:<path>`) before the first deploy leg and cite both by
path@commit in your instance. **Branch A:** the targeted plan changes only `aws_lambda_function.auth_validator_edge[0]` (a new version) and the
`lambda_function_association` ARNs inside `aws_cloudfront_distribution.portal` -- proceed. **Branch B:** any other attribute or address in
the plan, or any control arm that changes (C1-AC4, C1-AC13) -- STOP, BLOCKING row, and run the rollback the COO half names.

**AMENDMENT 1 (issuer, ~19:2xZ, BEFORE any deploy leg; on the CTO half's three conditions).** The CTO half
(`ledger/NEVER_WIDEN_ROUND1_EDGE_GATE_CTO_HALF.md` @`ae1c985da4`) is SIGNED ONLY ON THREE CONDITIONS, and it states that C1-AC6's two-file
check does not by itself make it signed. The conditions are now criteria of this order; bring this amendment into your worktree
(`git merge --ff-only SITEZ`, or `git merge --no-edit SITEZ` if your branch has commits; never a rebase) before C1-AC6. **The radius is 25
behaviours, not two URLs:** `cloudfront-distribution.tf` carries 25 associations of `local.auth_validator_edge_arn`, so a fault at module load
or before the gate's URI test fails every authenticated API path of the portal.
1. **The gate decides on the path the origin will resolve:** `aggregate_gate.mjs` percent-decodes the URI and ignores any query string before
   it matches either aggregate form. C1-AC4 and C1-AC13 carry the encoded, query and double-slash rows below; an advisor or client row that
   returns the aggregate's bytes is Branch B.
2. **The other 24 behaviours are proven unmoved:** the module has no top-level side effect and the gate's first statement is the URI test
   (C1-AC5); three behaviour families other than `/api/general/*` are requested before the apply (C1-AC17) and after Deployed (C1-AC13) as an
   advisor and as Opal staff, status and body hash equal.
3. **The rollback target is known before the apply:** C1-AC18 prints the version all 25 associations point at, before C1-AC10.
**Run order for the deploy legs: C1-AC6, C1-AC7, C1-AC8, C1-AC9, C1-AC17, C1-AC18, C1-AC10, C1-AC11, C1-AC12, C1-AC13, C1-AC14, C1-AC15.**

**AMENDMENT 2 (issuer, ~20:3xZ, at the partial drain of your Branch B stop; row W2-S4).** `-target=aws_cloudfront_distribution.portal`
pulls in its dependency `aws_wafv2_web_acl.opal_cloudfront_protection` (`cloudfront-distribution.tf:117`, `web_acl_id`), and that WebACL
carries a provider normalization: on its three managed rules `common-rule-set`, `ip-reputation` and `known-bad-inputs`,
`managed_rule_group_statement.version` plans `'' -> null`, with every rule's name, priority, `override_action` (count), statement name and
vendor, and `visibility_config` identical before and after (measured twice: your `terraform show -json` of `c1.tfplan`, and the issuer's
whole-root plan at 18:3xZ). No targeted plan can exclude it, so it is now INSIDE this act, bounded by C1-AC9's leaf check and proved on the
live WebACL by C1-AC19 (before) and C1-AC20 (after). **Both never-widen halves are re-signed for it** (the COO half's AMENDMENT 2 section,
and the CTO half re-requested); C1-AC6 now also requires the CTO half to name the WAF normalization, and without that the legs stop exactly
as before. Your artifact rollback left the latest `portal-auth/auth-validator-edge.zip` at the prior bytes, so **C1-AC8 is re-run (the
rebuild)** before C1-AC9. **Run order on continuation: C1-AC6, C1-AC8, C1-AC9, C1-AC17, C1-AC18, C1-AC19, C1-AC10, C1-AC11, C1-AC20, C1-AC12,
C1-AC13, C1-AC14, C1-AC15.** C1-AC1..C1-AC5 and C1-AC7 stand as recorded.

**AMENDMENT 3 (issuer, ~21:1xZ, on 1.0.0_SA_CTO~Z's msg 23255 as the edge half's signer): C1-AC11's residual is the PERMANENT WAF
normalization, NOT Branch B.** After the apply, the targeted re-plan still reads `0 to add, 1 to change, 0 to destroy` on ONE address,
`aws_wafv2_web_acl.opal_cloudfront_protection`, with exactly the three `managed_rule_group_statement` version leaves `'' -> null`: state holds
`""` and AWS returns the field absent, so the provider re-proposes it after every apply and `No changes` can never pass on this root. Those
three leaves are inside both halves' AMENDMENT 2 radius, and C1-AC20 reads every live rule field equal. C1-AC11 is re-cut to accept either
`No changes` or exactly that one-address, three-leaf residual, read by `<PLAN_LEAF_DIFF_C1>` (the leaf reader you already use for C1-AC9, on
the re-plan's `show -json`). **Live at the amendment, read by the issuer:** 25 of 25 auth-validator-edge associations at version 20
(published 21:00:57Z), distribution Deployed. **Do NOT roll back.** Record C1-AC11 against this expectation, then continue to C1-AC14 and
C1-AC15.

### REFUSAL CLAUSE

A criterion you cannot satisfy as written is REFUSED with its measurement, never repaired, widened or satisfied by another route. A deploy
leg reached without both halves at SITEZ is refused with a row.

## SURPRISE ROWS

ONE row per off-cell finding, id `POSN_AGGFIX-Z-W2-S<k>` (start at S1; class OBSERVATION or BLOCKING only; pure ASCII), inside the fenced
json array of `org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md` per
`org/surprise_channel/schemas/investigation_item.schema.json` (`project` POSN_AGGFIX, `fabric` site-z, `disposition` UNDER_INVESTIGATION;
ARMED needs `disarm_owner` `2.0.0_SA_COO~Z`). Keep working.

## CRITERIA -- structured, one clause each

<criterion id="C1-AC1" cell_refs="AF1-s-4"><invocation>timeout 300 python <EDGE_ROUTE_CENSUS_C1></invocation><expect>every CloudFront behaviour of distribution EVTSA9VEHNZVH listed (from comp-routes behaviors and from `infra/aws/terraform/portal-auth/cloudfront-distribution.tf`, both denominators printed) with its path pattern, its viewer-request and origin-request functions, and whether the pattern plus the rewrite can reach json/positioning/opal_aggregate.json; the reaching behaviours named with both URL forms; a line `REACHING <n> -- AUTH-VALIDATOR AT VIEWER-REQUEST <n> of <n>`.</expect></criterion> `C1-AC1` -- EVERY ROUTE TO THE KEY, AND WHAT GUARDS IT.

<criterion id="C1-AC2" cell_refs="AF1-s-4"><invocation>timeout 120 python <EDGE_TIER_READ_C1></invocation><expect>for each of shared-advisor-router, auth-validator-edge and public-data-router at HEAD: every tier / role / firm / userType branch with its line range and the URI prefixes it applies to; a line per function stating whether any branch applies to /api/general/positioning/ (expected NONE for all three at HEAD).</expect></criterion> `C1-AC2` -- WHERE A TIER REFUSAL RUNS TODAY.

<criterion id="C1-AC3" cell_refs="AF1-s-4"><invocation>timeout 300 node <LIVE_TIER_ARMS_C1> --phase pre</invocation><expect>unauthenticated GET of /api/general/positioning/model.json returns 401 (the reachability control); a short-lived client-class token on the same URL returns a status printed with the first 120 bytes of the body; a line `MODEL-ROUTE CLIENT REFUSAL: TRUE` or `FALSE` (FALSE is recorded and filed as an OBSERVATION row); the claim set used for each class printed with the key and token redacted.</expect></criterion> `C1-AC3` -- THE PROXY DOCSTRING'S CLAIM, EXERCISED.

<criterion id="C1-AC4" cell_refs="AF1-s-11"><invocation>timeout 300 node <GATE_UNIT_HARNESS_C1></invocation><expect>12 rows (Opal staff firmId opal-capital, Dev userType Dev with a non-Opal firmId, advisor, client) x (/api/general/positioning/opal_aggregate.json, /api/general/json/positioning/opal_aggregate.json, the control /api/general/positioning/positioning_data.json), each with the handler's result: Opal staff and Dev PASS-THROUGH on all three; advisor and client 401 on both aggregate URLs and PASS-THROUGH on the control; then the NEGATIVE CONTROL rows from a scratch copy of index.mjs without the gate call: advisor and client PASS-THROUGH on both aggregate URLs (the harness can see a missing gate); and the AMENDMENT 1 rows for advisor and client on /api/general/positioning/opal%5Faggregate.json, /api/general/positioning/opal%5faggregate.json, /api/general/json/positioning/opal%5Faggregate.json, /api/general/positioning/opal_aggregate.json?v=1 and /api/general/positioning//opal_aggregate.json, each 401 or PASS-THROUGH with a forwarded URI that cannot resolve to json/positioning/opal_aggregate.json (the forwarded URI printed), Opal staff and Dev PASS-THROUGH on the same five, and the negative-control copy letting the advisor and client through on the three encoded forms.</expect></criterion> `C1-AC4` -- THE GATE, UNIT-EXERCISED, WITH A HARNESS THAT CAN FAIL.

<criterion id="C1-AC5" cell_refs="AF1-s-11"><invocation>timeout 60 git diff --stat 605c03f81f HEAD -- infra/aws/lambda-edge/</invocation><expect>exactly two files: infra/aws/lambda-edge/auth-validator-edge/index.mjs modified and infra/aws/lambda-edge/auth-validator-edge/aggregate_gate.mjs added; `git diff 605c03f81f HEAD -- infra/aws/lambda-edge/auth-validator-edge/index.mjs` printed and limited to the import and the call after the verify; aggregate_gate.mjs printed whole shows no top-level statement other than imports, constants and function declarations, and the gate function's first statement is the URI test that returns pass-through for every other URI.</expect></criterion> `C1-AC5` -- THE CODE CHANGE IS THE GATE AND NOTHING ELSE.

<criterion id="C1-AC6" cell_refs="AF1-s-11"><invocation>timeout 60 git ls-tree SITEZ -- org/missions/D4/POSN/POSN_AGGFIX/ledger/NEVER_WIDEN_ROUND1_EDGE_GATE_COO_HALF.md org/missions/D4/POSN/POSN_AGGFIX/ledger/NEVER_WIDEN_ROUND1_EDGE_GATE_CTO_HALF.md</invocation><expect>two blob lines, one per half; and (AMENDMENT 2) the CTO half at SITEZ names the WAF normalization inside the radius -- `git show SITEZ:<CTO half>` printed and its WAF passage quoted. One half, none, or a CTO half that does not name it: STOP before any further deploy leg, BLOCKING row (C1-AC1..AC5 stand).</expect></criterion> `C1-AC6` -- BOTH HALVES ARE FILES BEFORE ANY DEPLOY LEG.

<criterion id="C1-AC7" cell_refs="AF1-s-11"><invocation>timeout 120 python .tools/deploy_ledger.py open --slug posn-aggfix-r1-edge-gate --title "POSN_AGGFIX AF1-s-11: auth-validator-edge refuses the Opal-only aggregate outside Opal" --author 0.9.0_WK_POSN_AGGFIX~2 --leg "L1|git|branch carries index.mjs + aggregate_gate.mjs|commit hash" --leg "L2|s3-prefix|opal-313476888478-lambda-artifacts portal-auth/auth-validator-edge.zip|sha256 + VersionId" --leg "L3|verify|plan targeted to the function and the distribution|0 add 2 change 0 destroy" --leg "L4|activation|safe-apply|apply summary + published version" --leg "L5|verify|0-diff re-plan and LIVE association version N of N|No changes + association read" --leg "L6|verify|live tier arms on both URLs and the control|statuses per class" --leg "L7|git|record-terraform-deploy|commit hash"</invocation><expect>the ledger entry and its sentinel created under org/critical_paths/change_management/ and org/critical_paths/.open_deploys/, both committed in your next commit (git show --stat lists both).</expect></criterion> `C1-AC7` -- THE LEDGER ENTRY OPENS FIRST.

<criterion id="C1-AC8" cell_refs="AF1-s-11"><invocation>timeout 900 bash infra/aws/lambda/ci/build-nodejs-lambda.sh portal-auth auth-validator-edge</invocation><expect>printed BEFORE the build: s3api head-object of portal-auth/auth-validator-edge.zip (VersionId, Metadata content-sha256) and `aws lambda list-versions-by-function --function-name auth-validator-edge` last version number -- the ROLLBACK pair; the build completes, uploads, and head-object after prints the new VersionId and content-sha256; infra/aws/lambda/ci/lambda-source-map.json restored to PURE ASCII with only the changed values (detector 0 printed).</expect></criterion> `C1-AC8` -- BUILD AND UPLOAD, ROLLBACK PAIR PRINTED FIRST.

<criterion id="C1-AC9" cell_refs="AF1-s-11"><invocation>timeout 900 bash -c "terraform -chdir=infra/aws/terraform/portal-auth init -input=false -no-color > .scratch/c1_init.txt 2>&1; tail -3 .scratch/c1_init.txt; terraform -chdir=infra/aws/terraform/portal-auth plan -input=false -no-color -target='aws_lambda_function.auth_validator_edge[0]' -target=aws_cloudfront_distribution.portal -out=C:/tmp/wk-aggfix-1-2/.scratch/c1.tfplan"</invocation><expect>init reports success; `Plan: 0 to add, 3 to change, 0 to destroy`: aws_lambda_function.auth_validator_edge[0] updated in place; aws_cloudfront_distribution.portal updated in place with ONLY lambda_function_association ARNs changing; aws_wafv2_web_acl.opal_cloudfront_protection updated in place whose ONLY leaf changes, printed with their count from `terraform show -json` of the plan, are managed_rule_group_statement version '' -> null on the three managed rules common-rule-set, ip-reputation and known-bad-inputs. Anything else: Branch B.</expect></criterion> `C1-AC9` -- THE PLAN, TARGETED, BRANCH A OR B.

<criterion id="C1-AC17" cell_refs="AF1-s-11"><invocation>timeout 600 node <LIVE_TIER_ARMS_C1> --phase families-before</invocation><expect>BEFORE the apply: for the advisor class and the Opal-staff class, one authenticated GET on each of three behaviour families other than /api/general/* -- an S3-backed /api/scoped/advisor-intelligence/* path, an API-Gateway-backed /api/private/* or /v1/* path, and a /api/scoped/satellites/* path (each URL printed) -- with status and body sha256 recorded to .scratch/c1_families_before.json; a line `FAMILIES CAPTURED 6 of 6`; key and tokens redacted.</expect></criterion> `C1-AC17` -- THREE OTHER BEHAVIOUR FAMILIES, CAPTURED BEFORE THE APPLY (AMENDMENT 1, condition 2).

<criterion id="C1-AC18" cell_refs="AF1-s-11"><invocation>timeout 300 python <LIVE_ASSOCIATION_READ_C1> --before-apply</invocation><expect>from the LIVE distribution config of EVTSA9VEHNZVH, before C1-AC10: every lambda_function_association ARN naming auth-validator-edge and a line `AUTH-VALIDATOR ASSOCIATIONS 25 -- AT VERSION <v> 25 of 25` (the config's own count printed if it is not 25); <v> recorded as the rollback target.</expect></criterion> `C1-AC18` -- THE ROLLBACK TARGET, READ BEFORE THE APPLY (AMENDMENT 1, condition 3).

<criterion id="C1-AC19" cell_refs="AF1-s-11"><invocation>timeout 300 python <LIVE_WAF_READ_C1> --phase before</invocation><expect>BEFORE C1-AC10, from wafv2 get-web-acl (scope CLOUDFRONT, us-east-1) of opal-cloudfront-protection: the LockToken printed, and every rule's name, priority, action or override_action, statement (managed rule group name, vendor and version if present) and visibility_config written to .scratch/c1_waf_before.json with a line `WAF RULES CAPTURED <n>` and the three managed rules present.</expect></criterion> `C1-AC19` -- THE LIVE WAF RULES, CAPTURED BEFORE THE APPLY (AMENDMENT 2).

<criterion id="C1-AC20" cell_refs="AF1-s-11"><invocation>timeout 300 python <LIVE_WAF_READ_C1> --phase after</invocation><expect>AFTER C1-AC11, the same read: every rule field listed in C1-AC19 EQUAL to .scratch/c1_waf_before.json (a line `WAF RULES UNCHANGED <n> of <n>`, the managed rules' version fields printed on both sides), the rule count equal, and the LockToken printed beside C1-AC19's. Any rule field that differs is Branch B: the WebACL restore the COO half names runs at once, then the function rollback.</expect></criterion> `C1-AC20` -- THE LIVE WAF RULES, UNCHANGED AFTER THE APPLY (AMENDMENT 2).

<criterion id="C1-AC10" cell_refs="AF1-s-11"><invocation>timeout 1800 .tools/safe-apply.sh -chdir=infra/aws/terraform/portal-auth apply C:/tmp/wk-aggfix-1-2/.scratch/c1.tfplan</invocation><expect>`Apply complete! Resources: 0 added, 3 changed, 0 destroyed.` with the halt-gate checkpoint output pasted above it, and the newly published auth-validator-edge version number printed after it (list-versions-by-function).</expect></criterion> `C1-AC10` -- THE APPLY, THROUGH THE GATE.

<criterion id="C1-AC11" cell_refs="AF1-s-11"><invocation>timeout 900 bash -c "terraform -chdir=infra/aws/terraform/portal-auth plan -input=false -no-color -target='aws_lambda_function.auth_validator_edge[0]' -target=aws_cloudfront_distribution.portal -out=C:/tmp/wk-aggfix-1-2/.scratch/c1_ac11.tfplan && terraform -chdir=infra/aws/terraform/portal-auth show -json C:/tmp/wk-aggfix-1-2/.scratch/c1_ac11.tfplan > .scratch/c1_ac11_show.json && python <PLAN_LEAF_DIFF_C1> .scratch/c1_ac11_show.json"</invocation><expect>(AMENDMENT 3) either `No changes. Your infrastructure matches the configuration.`, or `Plan: 0 to add, 1 to change, 0 to destroy` where the leaf reader prints ONE address with an action, aws_wafv2_web_acl.opal_cloudfront_protection, whose ONLY leaf changes are the three managed_rule_group_statement version values '' -> null (a line `LEAF DIFFS 3`, after_unknown empty); aws_lambda_function.auth_validator_edge[0] and aws_cloudfront_distribution.portal carry NO action. Anything else: Branch B.</expect></criterion> `C1-AC11` -- THE TARGETED RE-PLAN.

<criterion id="C1-AC12" cell_refs="AF1-s-11"><invocation>timeout 1800 python <LIVE_ASSOCIATION_READ_C1></invocation><expect>the distribution's Status polled until `Deployed` (bounded, each poll printed); then from get-distribution-config every lambda_function_association ARN naming auth-validator-edge, with a line `AUTH-VALIDATOR ASSOCIATIONS 25 -- AT NEW VERSION 25 of 25` (the count C1-AC18 printed) naming the version C1-AC10 published and 0 at any other version.</expect></criterion> `C1-AC12` -- THE LIVE ASSOCIATION, THE ONLY PROOF THE EDGE MOVED.

<criterion id="C1-AC13" cell_refs="AF1-s-11"><invocation>timeout 900 node <LIVE_TIER_ARMS_C1> --phase post</invocation><expect>after C1-AC12's Deployed: unauthenticated GET of both aggregate URLs returns 401; advisor-class and client-class tokens on both aggregate URLs return 401 (the gate's message in the body); Opal-staff and Dev tokens on both aggregate URLs return NOT 401 (status and first 120 bytes printed: S3's answer for an absent key, or the JSON once TO-A3-1 has written it); all four classes on the control URL /api/general/positioning/positioning_data.json return 200; the AMENDMENT 1 encoded, query and double-slash forms for the advisor and client classes each return 401 or a body that is not the aggregate's bytes; the three behaviour families of C1-AC17 re-requested as advisor and Opal staff with status and body sha256 EQUAL to C1-AC17's per request (`FAMILIES UNMOVED 6 of 6`); one table with its row count printed, key and tokens redacted.</expect></criterion> `C1-AC13` -- THE LIVE REFUSAL AND THE LIVE ALLOWANCE.

<criterion id="C1-AC14" cell_refs="AF1-s-11"><invocation>timeout 300 bash infra/aws/lambda/ci/record-terraform-deploy.sh portal-auth --plan C:/tmp/wk-aggfix-1-2/.scratch/c1.tfplan --author "0.9.0_WK_POSN_AGGFIX~2 <0.9.0_WK_POSN_AGGFIX~2@opal.agent>"</invocation><expect>the recorder's commit VERIFIED BY GIT and never by its stdout: `git show --stat HEAD` lists infra/aws/lambda/ci/lambda-source-map.json with auth-validator-edge's last_deployed_commit moved; a re-encoded source map restored to pure ASCII in ONE follow-up commit (detector 0 printed); a CHANGELOG entry the recorder's helper cannot write on this device written by hand and cited.</expect></criterion> `C1-AC14` -- THE DEPLOY RECORDED.

<criterion id="C1-AC15" cell_refs="AF1-s-11"><invocation>timeout 120 python .tools/deploy_ledger.py close --slug posn-aggfix-r1-edge-gate</invocation><expect>the entry closed with every leg's evidence filled and the sentinel removed, committed (git show --stat HEAD lists both).</expect></criterion> `C1-AC15` -- THE LEDGER ENTRY CLOSED.

<criterion id="C1-AC16" cell_refs="AF1-s-4,AF1-s-11" judgment="true"/> `C1-AC16` -- **JUDGMENT, GRADED BY `3.0.0_SA_CVO~Z` AT L9:** whether the gate's admit predicate (firmId opal-capital or userType Dev) admits exactly the viewers the page's `isInternal() || isDev()` admits, including any Dev user outside Opal; and whether a route to the key exists that C1-AC1 did not list. Record the readings and offer NO verdict.

<expected_criteria>C1-AC1, C1-AC2, C1-AC3, C1-AC4, C1-AC5, C1-AC6, C1-AC7, C1-AC8, C1-AC9, C1-AC10, C1-AC11, C1-AC12, C1-AC13, C1-AC14, C1-AC15, C1-AC16, C1-AC17, C1-AC18, C1-AC19, C1-AC20</expected_criteria>

<placeholders>EDGE_ROUTE_CENSUS_C1, EDGE_TIER_READ_C1, LIVE_TIER_ARMS_C1, GATE_UNIT_HARNESS_C1, LIVE_ASSOCIATION_READ_C1, LIVE_WAF_READ_C1, PLAN_LEAF_DIFF_C1</placeholders>

<paths>
org/missions/D4/POSN/POSN_AGGFIX/task-orders/POSN_AGGFIX.TO-C1-1.edge-refuses-the-aggregate-outside-opal.md
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~2/
org/missions/D4/POSN/POSN_AGGFIX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda-edge/auth-validator-edge/index.mjs
infra/aws/lambda-edge/auth-validator-edge/aggregate_gate.mjs
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/portal-auth/CHANGELOG.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D4/POSN/POSN_AGGFIX/decompositions/POSN_AGGFIX_DECOMP.md</decomp_doc> round 1 @`605c03f81f`.
<owned_cells>AF1-s-4 AF1-s-11</owned_cells>
Read-dependencies, NOT claimed: the 1.1 contract's URL and key; `AF1-s-3` (TO-B1-1's reading of the page predicate, slot ~3) -- a divergence
between that reading and your admit predicate is a BLOCKING row at the drain. DOWNSTREAM: `AF1-s-16` (TO-B3-1) reads the live key through
your gate as an Opal user.
</decomp_ref>

<preflight>
comp-schedule: RUN at the cut (2026-09-15 ~18:3xZ) -- 7 armed gates, 0 POSN; 6 open deploy-ledger entries, 0 POSN (yours opens at C1-AC7 and closes at C1-AC15); binding NEVER clauses: Terraform through safe-apply only, never-widen halves as files, no monitor or alarm (the structured log line is not a metric filter), secrets through comp-secrets.
comp-iam: DECLARED-NOT-APPLICABLE -- this order changes no role, policy or grant; the function's existing S3 read of the ownership map is untouched. BLIND, stated: `comp-iam service auth-validator-edge` has no record for the edge function (the service listing came back), so the lens could not have read its role even if a grant were in scope.
comp-adversary: RUN on the decomposition. NOT covered, stated: (1) minting tokens with `opal/auth/jwt-private-key` is unexercised by the issuer, and the claim set the auth handler signs (including any `kid`) is unread -- read it from the auth handler source before minting; (2) replacing `verifyWithSlots` in-process for the unit harness is unexercised (index.mjs imports jsonwebtoken and ../../lambda/lib/authkeys/jwtPublicKeys.mjs at :62-65); (3) the portal-auth root has not been initialised in a worktree on this device; (4) CloudFront propagation time on this distribution is unmeasured by the issuer, hence C1-AC12's bounded poll.
</preflight>

<proof_of_spec>
org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~2/POSN_AGGFIX.TO-C1-1.edge-refuses-the-aggregate-outside-opal.proof_of_spec.json
</proof_of_spec>
