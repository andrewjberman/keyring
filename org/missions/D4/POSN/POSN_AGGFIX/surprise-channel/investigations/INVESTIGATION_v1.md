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
  }
]
```
