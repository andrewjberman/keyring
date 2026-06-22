# COT go-live P0 -- ROUTER_FIRM_SUFFIX cottonwood->cot fix + stale-bundle second-gap catch
**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT

**Agent:** 0.4.0_DE_ClientPlatform · **Window:** 2026-06-22 ~21:26Z -> ~21:37Z · **Trigger:** CTO+COO P0 (Andrew-direct, all-hands -- "Andrew STILL sees no cot on ADVI despite the display-ready cert") · Portal DEV commit `7d71fbe0` · ~5 significant MCP.

## Current State
P0 root-caused + FE fix SHIPPED to portal DEV (CTO architect-confirmed), pending the DEV->PROD promote (DT lane, CTO driving via COO) which unblocks Andrew. The cert wasn't wrong -- the data + render were fine; the LIVE ?firm= route asked for the wrong bucket name, which my data-injected/scoped smoke bypassed.

## Root (CTO source-confirmed, I confirmed + traced the full mechanism)
`portal/src/api/endpoints/advisor-intelligence.ts:69` ROUTER_FIRM_SUFFIX = {49financial:bd, inflection:inf, demo:demo} -- NO cottonwood. So `bucketSuffix('cottonwood')` falls through to 'cottonwood' (`ROUTER_FIRM_SUFFIX[x] ?? x`, :76-79). The ADVI ?firm= callsites + the shared-advisor-router opal-capital branch (`bucket = opal-data-${firmParam}`, index.mjs) then built `opal-data-COTTONWOOD` (nonexistent) -> Andrew's INTERNAL cot ADVI rendered EMPTY. [SOURCE-CONFIRMED, advisor-intelligence.ts:61-79 + shared-advisor-router index.mjs:190-205]

## Fix (mine, DE/FE -- SHIPPED 7d71fbe0)
Added `'cottonwood':'cot'` to ROUTER_FIRM_SUFFIX (:79) -> FE asks `opal-data-COT` (the real bucket; FIRM_CONFIG cottonwood->opal-data-cot, FIRMSEP.10). Suffix->bucket convention matches 49financial->bd. tsc --noEmit exit 0.

## Adjacent gaps (CTO-flagged -- both GROUNDED CLEAR, no fix)
- (a) FIRM-SELECTOR: cottonwood IS a selectable internal option -- index.tsx ALL_PARTNER_FIRMS + PARTNER_VIEWS['cottonwood'] + showSelector(internal && !locked), all on origin/PROD. Andrew can scope to it. NO GAP. (Refutes the "ADVI 49financial-LOCKED" hypothesis -- the hardcode is the DEFAULT-landing, not a lock.)
- (b) :607 firm-branch (resolvedFirm==='inflection' static-S3 adapter): cottonwood is BD-native -> rides the DEFAULT Lambda path (:610) like 49financial; the branch is inflection-nested-shape-specific; COT Books disabled v1. NO GAP.
- comp-transform schema-check: PartnerAnalytics/DistributionTab clean (no MISSING) per smoke; the fix is endpoint-URL-level not binding-level -> bindings unaffected.

## SECOND GAP (NEW, I caught it -- routed AE/DT)
The DEPLOYED `infra/aws/lambda-edge/shared-advisor-router/shared-advisor-router.zip` is a STALE build -- cottonwood NOT inlined (unzipped + grepped: absent). Source `firm-config.mjs` HAS cottonwood->opal-data-cot (FIRMSEP.10, commit 3e0f224e2) but the .zip wasn't rebuilt+redeployed (bun build inlines firm-config per-function). IMPACT: IRRELEVANT for Andrew (opal-capital branch uses opal-data-${firmParam} directly, bypasses FIRM_BUCKET_MAP) -> my one-liner fully unblocks Andrew. BUT BLOCKS EXTERNAL cottonwood-USERS (partner branch reads FIRM_BUCKET_MAP[cottonwood] -> stale bundle lacks it -> unmapped fallback -> opal-data-cottonwood). FIX: AE/DT rebuild+redeploy shared-advisor-router (+ likely auth-validator-edge, which also inlines firm-config). CTO routed it to AE/DT.

## Blockers
None on my leg (shipped). Andrew-sees-cot gated on the DEV->PROD promote (DT). Prior gates event-pending (TO-2/DS TO-1, P2-1/AE P2-2; COT reconciling-render done).

## Next Steps
- **[1.0.0_SA_CTO / 2.0.0_SA_COO / DT]** portal DEV->PROD promote (carries 7d71fbe0) = the Andrew-unblock.
- **[0.7.0_AE / DT]** SECOND gap: rebuild+redeploy shared-advisor-router Lambda@Edge (cottonwood in the inlined FIRM_BUCKET_MAP) for external cot users.
- **[0.4.0_DE]** available for promote coordination + post-promote served-side verify (deployed-bundle-carries-fix); event-driven otherwise.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| comp-which | locate shared-advisor-router FIRM_CONFIG | -> comp-constants.config.yaml + the lambda-edge source (routed) |
| comp-transform schema-check | PartnerAnalytics/DistributionTab (cot scope, cited from smoke) | clean, no MISSING -- fix is URL-level not binding-level |
| boto3/unzip (not raw-aws) | shared-advisor-router.zip bundle inspection | cottonwood NOT inlined = stale build (the second-gap catch) |
| bunx tsc --noEmit | portal tsconfig.app.json after the fix | exit 0 |
| git (DEV vs PROD) | cottonwood ADVI wiring + firm-config.mjs vs .zip commit history | wiring on PROD; firm-config has cottonwood (3e0f224e2) but .zip stale |

## MCP traffic (this window)
~5 significant: CTO P0 + ROOT-FOUND + architect-CONFIRM; COO P0 + CONVERGE; my ACK + grounded-gap-list report + SHIPPED RAVC (CTO+COO). The CTO/COO 49financial-lock hypothesis was REFUTED by my firm-scope grounding; CTO's source-confirmed ROUTER_FIRM_SUFFIX root superseded + I added the stale-bundle second gap.
