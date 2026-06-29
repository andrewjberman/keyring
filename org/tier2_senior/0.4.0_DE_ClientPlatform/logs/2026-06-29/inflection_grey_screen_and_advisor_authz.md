# Inflection Wealth — first-login grey screen + advisor-identity + advisor-scoping authz

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE
**Serial:** 0.4.0_DE_ClientPlatform · **Date:** 2026-06-29 · **Window:** session start (ad-hoc spawn) -> now

## Summary

Andrew-direct ad-hoc spawn on an Inflection Wealth FE issue (noel@ + patrick@inflectionwealth.com,
newly provisioned). Diagnosed + shipped fixes for two distinct symptoms, then scoped + (after live
verification) RIGHT-SIZED a backend advisor-scoping concern that turned out to be a false positive.
All FE changes live on DEV (opalinvest.dev), CI green.

## What shipped (portal DEV, all CI=success; workspace pointer bumps on CLOUD)

| portal commit | CLOUD bump | what |
|---|---|---|
| `dcb5d227` | `67d88936d` | **Grey-screen fix.** `firmAccess.ts`: exempt `/change-password` from the per-firm path matrix (`FIRM_EXEMPT_PATHS`). |
| `adda3e0e` | `99827bc83` | **noel = bookless firm-viewer.** `inflection/index.tsx`: gate non-admin Profile tab on a resolved `advisorId`; bookless users get Distribution-only. |
| `6089c7a6` | `ff33ce04d` | **FE regression guard.** dev-only non-throwing assert: a non-admin is never offered an Advisors/Books tab. |
| (brief) | `fb93fc189` | `docs/briefs/ADVI_PARTNER_AUTHZ_backend_enforcement_scope_20260629.md` — backend authz scope. |

## Current State (zero-context handoff)

**Symptom B — grey screen (ROOT-CAUSED + FIXED).** Root cause = redirect loop in
`portal/src/components/ProtectedRoute.tsx`: the `mustChangePassword` guard (line 34) sends a
newly-provisioned partner user to `/change-password`; the firm path-matrix guard (line 57) found
`/change-password` absent from every partner allowlist in `src/lib/firmAccess.ts` and bounced them
back to `/market` -> infinite loop -> React bails -> blank grey screen. Internal `opal-capital`
users never hit it (short-circuit true). Affected all 5 new users (`mustChangePassword=true`). Fix:
added `FIRM_EXEMPT_PATHS={'/change-password'}` short-circuited in `isPathAllowedForFirm`. tsc clean.

**Symptom A — "Advisor Identity Unavailable" (AE-owned, coordinated).** FE renders that panel when
`claims.advisorId` is null (`inflection/index.tsx`). advisorId is minted into the JWT from
`opal-partner-{firm}` DynamoDB `advisorKey` at token-mint. patrick@ — AE backfilled
`advisorKey=patrick_scanlan` (live, JWT-verified); needs a full re-login. noel@ — Andrew ruled he is
a firm-level VIEWER with no book; handled by the `adda3e0e` Profile-tab gate (no advisorKey -> no tab).

**Backend advisor-scoping (ADVI_PARTNER_AUTHZ) — G1 FALSE POSITIVE, retracted.** I flagged a "G1
own-book IDOR" off reading the `opal-partners-data` route handlers (`:1791/:1846`) without the
pre-branch guard. It was wrong: the own-book gate is ALREADY enforced two-layer — the Lambda L1
`ADVI_ROLGAT.DT1` guard at `lambda_function.py:1682-1694` (`not admin_bypass and required_tier=='L1'`,
keys on JWT advisorId, 401 'Advisor scope mismatch'; fires on edge AND direct-API-GW) + edge
`auth-validator-edge .004a`. AE live-PoC confirmed: patrick->own=200, patrick->peter_lee=401/403, no
leak. COO closed G1; G2 (authorizer firmRole/advisorRole claim-parity) + G3 (advisorRole is a 49F-only
concept, drop from Inflection provisioning) downgraded to low-pri hygiene folded into AE/DT lanes.
Memory banked: `reference_partner_advisor_ownbook_scoping_already_twolayer.md`.

**Deploy:** opalinvest.dev serving HEAD `6089c7a6` (CI run 28400285169 success @ 20:23Z). DEV only —
no PROD promote done. Users must hard-refresh / re-login to pick up the new bundle (patrick's re-login
also mints his advisorId claim).

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-which` | route to auth token-mint lambda | FAIL (mis-match) | matched on "handles"; fell back to Grep/Read of authorizer + lambda |
| `comp-transform schema-check` | AdvisorPublicProfile, PartnerAnalytics | PASS | no MISSING introduced (only pre-existing UNUSED); my tab-gating change adds no data prop |
| `comp-transform ternary-audit` | InflectionAdvisorIntelligence | FAIL (not found) | component not in the index by that name; change is tab-visibility, not a data ternary |

**What worked:** schema-check confirmed the Profile-tab change introduced no runtime-undefined risk.
**What failed:** comp-which mis-matched on a common word ("handles"); ternary-audit didn't resolve the
page component by export name. **Gap:** comp-which keyword scoring matched prose "handles" over the
auth-lambda intent — a routing-precision gap for natural-language lambda lookups.

## MCP traffic

~10 messages. Significant: AE coordination on symptom A (confirm backfill + re-login) and the live
IDOR PoC (AE ran it, falsified G1); COO GO'd the PoC, relayed Andrew's authz-policy rulings (A-narrow,
keep Distribution, benign threat model), accepted my G1 retraction + closed the leg. RAVC closes:
symptom-A coord (AE), PoC retraction (COO), regression-guard land (COO).

## Blockers

None. Symptom A (patrick) is event-gated on his re-login (user action, not an agent block). G2/G3 are
low-pri folded into AE/DT lanes.

## Next Steps

- **[Andrew]** confirm whether the Inflection users need this on PRODUCTION (a DEV->PROD promote, DT lane) — DEV is live now.
- **[patrick@inflectionwealth.com]** log out + back in once -> clears grey screen + resolves advisor profile.
- **[0.7.0_AE_CloudOps]** fold G3 (drop `advisorRole` for Inflection) into the provisioning-contract scripts; G1 = nothing to build (closed).
- **[0.4.0_DE, me]** back to IDLE/event-gated lane (NFRA_TSGRAPH P2-1 + COTMVP B remain on prior gates).
