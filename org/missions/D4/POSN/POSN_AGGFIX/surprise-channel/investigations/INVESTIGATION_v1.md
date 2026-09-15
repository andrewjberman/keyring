# POSN_AGGFIX -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `2.0.0_SA_COO~Z` at L6, in the round-1 issuance commit, 2026-09-15. **Home:** the project tree's channel. Lane `ANY`; the
gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project). **Append-only during the
round.** Every row goes inside the ONE fenced json array below, per `org/surprise_channel/schemas/investigation_item.schema.json`; a
worker's id is `POSN_AGGFIX-Z-W<slot>-S<k>`, a seat's `POSN_AGGFIX-Z-S<k>`.

```json
[
  {
    "id": "POSN_AGGFIX-Z-S1",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~Z",
    "surfaced_at": "2026-09-15T18:48:41Z",
    "one_line": "PRD v0.2 C-NO-SILENT-EMPTY describes the five books' failure fallback as 'writes aum 0 into each book' (:1798), but on a WHOLLY failed weight read the producer writes no current_holdings at all (load_aum_data returns {} at :1475-1477, and generate_positioning_data's `if aum_data:` gate at :2374-2381 with :2392-2395 omits the block and data_date); aum 0 arises only on a PARTIAL read. TO-A2-1 keeps both arms exactly, so no behaviour moves; the PRD sentence under-describes today's fallback.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D4/POSN/POSN_AGGFIX/prd/POSN_AGGFIX_PRD.md @cbd85e5cff :192-195 (C-NO-SILENT-EMPTY): 'The five model books keep their current failure fallback, which writes `aum` 0 into each book (`:1798`)'.",
        "infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py @605c03f81f :1475-1477: `except Exception as e:` prints WARN and `return {}` (the success return is :1474).",
        "same file @605c03f81f :2374-2381, inside generate_positioning_data (def at :2117): `aum_data = load_aum_data(data_date)`; `if aum_data:` extracts current_holdings, else `current_holdings = None`; :2392-2395 adds current_holdings and data_date to the output only when current_holdings is truthy.",
        "same file @605c03f81f :1796-1799: `'aum': aum_data.get(model_code, 0)` -- the 0 is reached only when aum_data is non-empty but lacks a code (a partial read)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "C-NO-SILENT-EMPTY (PRD v0.2 :192-195): a failed weight read leaves the five books with their current fallback, aum 0 in each book.",
    "world_is": "Two arms: a wholly failed read serves the shared file with NO current_holdings key and no data_date (every Models-mode book disappears for every viewer); a partial read writes aum 0 into the missing book only. The decomposition's AF1-s-6 parenthesis repeated the PRD's one-arm wording; TO-A2-1 states both arms and its A2-AC7/A2-AC8 prove each, and the producer's never-widen COO half names the wholly-failed arm as Branch B with a rollback.",
    "notes": "Carried for 1.0.0_SA_CTO~Z's round analysis: a PRD touch to C-NO-SILENT-EMPTY's sentence would align the text with the measured fallback; nothing in this round waits on it. Filed by the issuer at L6; it also opens this channel, which the row gate refuses to open empty."
  },
  {
    "id": "POSN_AGGFIX-Z-S2",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "1.0.0_SA_CTO~Z",
    "surfaced_at": "2026-09-15T19:10:49Z",
    "one_line": "The shared positioning file has THREE writers, not one: besides the producer, yang-time-machine (Dev-triggered portal restore) and rollback-protocol.sh restore prior S3 versions of every key under json/ by prefix. After TO-A3-1's Branch A, a restore to any execution before the change re-serves current_holdings.AGG and July book aum to every signed-in viewer until the next pipeline run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/v2_portal/yang_pipeline/outputs/yang-time-machine/lambda_function.py @SITEZ HEAD :4-10 restores all captured JSON outputs of the latest execution at or before a target date by CopyObject with CopySourceVersionId; restore_outputs :197-239; only json/portfolios/ is skipped (:52-58).",
        "infra/aws/lambda/v2_portal/yang_pipeline/outputs/capture-output-versions/lambda_function.py :22 JSON_PREFIX = 'json/' and :62 paginate over that prefix: every key under json/, including json/positioning/positioning_data.json and, once written, json/positioning/opal_aggregate.json, is captured per execution.",
        "infra/aws/lambda/data_refresh/lambda_function.py :1756 POST /data-refresh/time-machine, Dev-gated (:24, :140-192); infra/aws/lambda/data_refresh/portal_time_machine/lambda_function.py :4-8 fans out to yang-time-machine.",
        "infra/aws/lambda/v2_portal/yang_pipeline/scripts/rollback-protocol.sh :24-35 lists json/positioning/ among restored prefixes; :170-176 copy_object from a prior VersionId.",
        "Census: comp-find 'positioning/positioning_data.json' over infra and data, 25 hits across 8,112 files, names only the producer as a writer by literal key; the two restore writers address the key by prefix."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The producer never-widen COO half @ed1db8f1db prints 1 writer for json/positioning/positioning_data.json, and PRD v0.2 FWD-7 with C-OPAL-ONLY-DATA asserts the aggregate's figures reach Opal viewers only once the change lands.",
    "world_is": "Two further writers restore that file by prefix. A Dev-triggered time-machine restore, or an operator rollback, to a date before the change puts current_holdings.AGG and July book aum back into the file every signed-in viewer receives, until the next pipeline run. It is not part of TO-A3-1's act and neither half signs it.",
    "notes": "INERT until TO-A3-1 lands Branch A. Carried for 1.0.0_SA_CTO~Z's round analysis: whether a cell carries it (for example, the restore set skipping json/positioning/opal_aggregate.json and a restore of the shared file dropping AGG, or a named operating rule). The CTO halves @ this commit name it: ledger/NEVER_WIDEN_ROUND1_PRODUCER_CTO_HALF.md."
  },
  {
    "id": "POSN_AGGFIX-Z-W2-S1",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~2",
    "surfaced_at": "2026-09-15T19:44:00Z",
    "one_line": "TO-C1-1 drives a 'client' viewer class in its unit and live arms, but the live signer never mints one: generateAccessToken sets tier 'internal' for firmId opal-capital and 'advisor' for every other firm, and no other claim marks a client. The worker constructed the class (tier 'client', firmId 49financial, no advisor identity) and signed it with the live key.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts @240fe36222 :168 (generateAccessToken, :162): const tier = user.firmId === 'opal-capital' ? 'internal' : 'advisor' -- the payload's only tier source.",
        "infra/aws/opalinvest_dev/lambda/auth-handler/src/types.ts @240fe36222 :63: the access payload's tier is commented 'Vestigial -- kept for portal-authorizer compat'.",
        "portal src/contexts/AuthContext.tsx @edf85ce503 :122-140 parseClaims: firmId, userType, advisorId, firmRole, advisorRole; advisorRole levels architect/consultant/local_ops/implementor; no client class.",
        "org/missions/D4/POSN/POSN_AGGFIX/deliverables/0.9.0_WK_POSN_AGGFIX~2/c1_classes.mjs: the client claim set used; printed with the token redacted in C1-AC3's output."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-C1-1 AF1-s-4 and AF1-s-11: exercise /api/general/positioning/model.json live with a client token, and drive four viewer classes (Opal staff, Dev, advisor, client).",
    "world_is": "The signer's tier space is {internal, advisor}; no real login produces a client-class token. The worker's client class carries tier 'client' (the value the proxy docstring names), firmId 49financial and no advisor identity. The gate's predicate reads only firmId and userType, so the class's tier value cannot move a gate row.",
    "notes": "Form only. Not read: portal-authorizer, or any other identity source that might carry a client notion."
  },
  {
    "id": "POSN_AGGFIX-Z-W2-S2",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~2",
    "surfaced_at": "2026-09-15T19:44:00Z",
    "one_line": "The portal proxy docstring for getModelData says the Lambda 'Checks X-User-Tier header (blocks client tier)' on /api/general/positioning/model.json. Exercised live, a client-tier token is NOT refused there: the request reaches S3, which answers 403 AccessDenied because the key is absent, byte-identical to Opal staff's answer. MODEL-ROUTE CLIENT REFUSAL: FALSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal src/api/portal-proxy.ts @edf85ce503 :1419-1426 (getModelData docstring): 'Lambda: Checks X-User-Tier header (blocks client tier)'; 'Access: Internal + Advisor tiers only'.",
        "C1-AC3 live run 2026-09-15T19:41:33Z, node .../deliverables/0.9.0_WK_POSN_AGGFIX~2/c1_live_tier_arms.mjs --phase pre: unauthenticated 401 {error: Missing or invalid Authorization header}; client token 403 len=263 S3 XML <Error><Code>AccessDenied</Code> sha256 b3c16307d6e569c8...; Opal-staff token 403 with the same sha256.",
        "Same run: s3api head-object opal-data-portal-v2 json/positioning/model.json -> 404 Not Found.",
        "C1-AC2 (c1_edge_tier_read.py) at git objects @b29fe4bf48: public-data-router 0 tier/role/firm/userType branches; auth-validator-edge's branches scoped to /api/scoped/advisor-intelligence/ and the advisor/account/relationship scoping regexes; shared-advisor-router not associated with /api/general/*."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-C1-1 AF1-s-4 / C1-AC3: record whether the proxy docstring's 'blocks client tier' for /api/general/positioning/model.json is true by exercising that URL live with a client token; FALSE is recorded and filed as an OBSERVATION row.",
    "world_is": "No function on the /api/general/* path reads the tier: any verified token is forwarded to S3. The URL serves nothing today only because json/positioning/model.json does not exist; were that key written, every signed-in viewer could read it.",
    "notes": "INERT while the key is absent (404 at the run). Not measured: whether anything writes json/positioning/model.json. The docstring describes a check that is not on the path."
  },
  {
    "id": "POSN_AGGFIX-Z-W2-S3",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~2",
    "surfaced_at": "2026-09-15T19:55:00Z",
    "one_line": "C1-AC8 asks for infra/aws/lambda/ci/lambda-source-map.json 'restored to PURE ASCII with only the changed values', but the map at HEAD is not pure ASCII: it carries 23 non-ASCII characters (detector 28) on 8 lines, several of them mojibake, so a pure-ASCII restore also rewrites those 8 unrelated lines as backslash-u escapes. The JSON values are identical; the one semantic change the build made is auth-validator-edge artifact_sha256.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/ci/lambda-source-map.json @9633bb9e7e (last commit touching it; unchanged at b29fe4bf48): 197884 bytes, detector len(b)-len(b.decode('utf-8')) = 28; 23 non-ASCII characters U+009D U+00A2 U+00A7 U+00AC U+00C3 U+00E2 U+2014 U+201A U+20AC; json.dumps(indent=2, ensure_ascii=False) reproduces it byte-for-byte.",
        "A pure-ASCII write (ensure_ascii=True) of the UNCHANGED base differs from it on lines 175, 223, 238, 253, 268, 287, 419, 549 of 3281.",
        "After build-nodejs-lambda.sh portal-auth auth-validator-edge (2026-09-15T19:50Z): 1 semantic leaf change, /functions/auth-validator-edge/artifact_sha256 wRAHCaKdoJ+wGRe95gu0Yh0jcTEeXTAPahEhQ8sRiic= -> fekWqHP2cWuewpfFOnlxa2S5jBhxmKKs8eB4/QccRxs=; the pure-ASCII restore was 197971 bytes, detector 0, differing from the base on 9 lines (the 8 above plus 1503)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-C1-1 C1-AC8: lambda-source-map.json restored to PURE ASCII with only the changed values (detector 0 printed).",
    "world_is": "The base already carries non-ASCII bytes, so PURE ASCII and 'only the changed values' cannot both hold byte-wise: a pure-ASCII write leaves exactly one semantic change and eight escape-only line changes on other functions' entries.",
    "notes": "Form only. The worker's pure-ASCII restore was then returned to the base bytes, because the artifact it described was rolled back under Branch B (row POSN_AGGFIX-Z-W2-S4); the map at the worker's HEAD equals the base. Not measured: which commit introduced the non-ASCII characters, or whether any consumer reads the map in a non-UTF-8 text mode."
  },
  {
    "id": "POSN_AGGFIX-Z-W2-S4",
    "project": "POSN_AGGFIX",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_POSN_AGGFIX~2",
    "surfaced_at": "2026-09-15T20:00:00Z",
    "one_line": "C1-AC9's targeted plan cannot come out as the order expects: -target=aws_cloudfront_distribution.portal pulls in the distribution's dependency aws_wafv2_web_acl.opal_cloudfront_protection (its web_acl_id), so the plan reads 'Plan: 0 to add, 3 to change, 0 to destroy' with the pre-existing WAF drift inside it. Branch B: the worker stopped before C1-AC17 and C1-AC10, applied nothing, and restored the artifact's prior bytes as the latest object version.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/portal-auth/cloudfront-distribution.tf @638492cd7e :117: web_acl_id = aws_wafv2_web_acl.opal_cloudfront_protection.arn inside resource aws_cloudfront_distribution.portal -- Terraform's -target includes a targeted resource's dependencies.",
        "C1-AC9, 2026-09-15T19:52:43Z, the order's invocation verbatim: init succeeded; 'Plan: 0 to add, 3 to change, 0 to destroy.'; terraform show -json of .scratch/c1.tfplan: 14 resource_changes, 3 with an action -- aws_cloudfront_distribution.portal update (25 lambda_arn paths, every before-value auth-validator-edge:19, 0 non-association leaf changes), aws_lambda_function.auth_validator_edge[0] update (s3_object_version GUSk3wpLZE2ElK8it6sOBQeIU0VZASNH -> zNqzzAOFvq1LnTji4BV2_OymHRfr.bXI), aws_wafv2_web_acl.opal_cloudfront_protection update (rule[3], rule[4], rule[5] managed_rule_group_statement version '' -> null).",
        "Rollback per the COO half's artifact row, 2026-09-15T19:58Z: s3api copy-object CopySourceVersionId GUSk3wpLZE2ElK8it6sOBQeIU0VZASNH -> latest VersionId 7AkZ0zQ1ETC.wcttDTxnk3t2s5QT9rh2, metadata content-sha256 wRAHCaKdoJ+wGRe95gu0Yh0jcTEeXTAPahEhQ8sRiic=; get-object of the latest re-hashed to that value (21096 bytes) and its bundle carries aggregate_denied 0 times.",
        "Live re-read 2026-09-15T19:58:26Z (c1_live_association_read.py --before-apply): AUTH-VALIDATOR ASSOCIATIONS 25 -- AT VERSION 19 25 of 25, config ETag E1XYSDYC8UB18L, the same ETag C1-AC1 read at 19:33Z.",
        "Targeted re-plan after the rollback, 2026-09-15T19:59:38Z: still 'Plan: 0 to add, 3 to change, 0 to destroy'; the function now plans s3_object_version GUSk3wpLZE2ElK8it6sOBQeIU0VZASNH -> 7AkZ0zQ1ETC.wcttDTxnk3t2s5QT9rh2 (identical bytes)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-C1-1 C1-AC9 and decomposition s.1.2: the plan -target'ed to the function and the distribution reads 'Plan: 0 to add, 2 to change, 0 to destroy' with aws_wafv2_web_acl absent (the whole-root WAF drift 'kept out of your targeted plan'); anything else is Branch B -- STOP, BLOCKING row, the COO half's rollback.",
    "world_is": "While the WAF drift stands, no plan targeted to the distribution can exclude it, so C1-AC9 as written cannot pass. Not run: C1-AC17, C1-AC10, C1-AC11, C1-AC12, C1-AC13, C1-AC14, C1-AC15. The live function and all 25 associations are at version 19; ledger entry posn-aggfix-r1-edge-gate stays OPEN with L1 and L2 closed.",
    "notes": "INERT: left alone, nothing serves differently. Residual of rolling back by copy: the latest artifact VersionId (7AkZ0z...) differs from the one in state (GUSk3...), so the NEXT portal-auth apply by any seat publishes a new version carrying the OLD code, re-points all 25 associations to it, and applies the WAF drift with it. Restoring the exact prior latest version would need a delete of object versions zNqzz... and 7AkZ0z..., an S3 delete this worker does not make without human confirmation. How the plan is re-cut is the issuer's."
  }
]
```
