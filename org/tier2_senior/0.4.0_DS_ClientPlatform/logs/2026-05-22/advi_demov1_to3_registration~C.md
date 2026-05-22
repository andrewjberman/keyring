# Session Log — ADVI_DEMOV1.003 Demo-Tenant Registration (DS-scope)

**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-22
**Task Order:** ADVI_DEMOV1.003 (issued by 2.0.0_SA_COO~C; SCOPED GO 2026-05-22)
**Status:** DS-SCOPE COMPLETE — both DynamoDB records created + verified. RAVC2 to COO~C.

> Log filed under `logs/2026-05-22/` (actual work date). The TO `<scope>` names
> a `logs/2026-05-21/` path — stale, the TO was authored 2026-05-21; work ran
> 2026-05-22.

## Current State

Phase 3 of ADVI_DEMOV1, DS-lane scope. Registered the `demo` tenant's identity
in `opal-users-v2` so a demo login resolves to the `opal-data-demo` bucket. Two
additive DynamoDB records created via an idempotent seed script.

### DS-scope (per COO~C SCOPED GO + the 21:00Z scope correction)

The TO body lists ROUTER_FIRM_SUFFIX as criterion 3, but the SCOPED GO and the
COO~C correction (20:30Z + 21:00Z) bound DS-scope to **criteria 1, 2, partial 4,
9 only**. The three portal items — `ROUTER_FIRM_SUFFIX` in advisor-intelligence.ts,
`firmAccess.ts FIRM_ALLOWED_PATHS['demo']`, `_partners/demo/` — are `portal/**`
= POD_DE_ANY-laned and HELD for a DE lane. They were NOT touched. The
end-to-end demo-login check (criterion 7) waits on the DE lane regardless.

### Artifacts

| Artifact | Evidence |
|----------|----------|
| `scripts/register_demo_tenant.py` | committed `2ea34ba81` (CLOUD) |
| `FIRM#demo` / `META` | created in `opal-users-v2`, verified by independent `get-item` |
| `USER#demo@demo.test` / `PROFILE` | created in `opal-users-v2`, verified; bcrypt credential validated |

### The two records

**FIRM#demo / META** (mirrors the `mockadv` non-real-firm precedent + the
binding `s3Bucket` attribute):
```
PK=FIRM#demo  SK=META  firmId=demo  name="Demo Advisory"
tier=advisor  status=active  domain=demo.test
s3Bucket=opal-data-demo   config={}
createdBy=0.4.0_DS_ClientPlatform@opal.agent  createdAt=2026-05-22T21:03:56Z
```

**USER#demo@demo.test / PROFILE** (mirrors the `opal-users-v2` PROFILE shape
written by `scripts/advi_rolgat_seed_test_accounts.py`):
```
PK=USER#demo@demo.test  SK=PROFILE  email=demo@demo.test  name="Demo User"
firmId=demo  role=user  tier=advisor  status=active
passwordHash + password_hash = bcrypt $2b$12$ (dual-write, legacy readers)
mustChangePassword=false
createdBy=0.4.0_DS_ClientPlatform@opal.agent  createdAt=2026-05-22T21:03:57Z
```

**Demo login credential:** `demo@demo.test` / `OpalDemo2026!` — bcrypt-verified
(`checkpw` PASS for the credential, rejects a wrong password). The auth-handler
verifies against `password_hash`; both `passwordHash` and `password_hash` are
written identically per the seed-script precedent.

### "No Cognito" finding (accepted by COO~C 21:00Z)

The TO says "demo Cognito user." There is **no Cognito user pool**. The deployed
auth substrate is custom RS256 JWT over the `opal-users-v2` DynamoDB table
(`infra/aws/opalinvest_dev/lambda/auth-handler`). The "demo Cognito user" is a
`USER#demo / PROFILE` DynamoDB record. `jwt.js generateAccessToken` derives the
JWT claims directly from the user record:
- `firmId` <- `user.firmId`  → `demo`
- `tier`   <- `user.firmId === 'opal-capital' ? 'internal' : 'advisor'`  → `advisor`
- `role`   <- `user.role`  → `user`

So the `USER#demo` record yields a JWT carrying `firmId=demo` / `tier=advisor`
with no auth-handler code change. The handler emits **no `allowedFirmIds`
claim** — the existing partner users (49financial / inflection) carry none
either, so the demo user mirrors them exactly. The demo user is scoped to ONLY
the demo firm; it carries no firm reference to any real firm.

### Path relocation (owned-paths)

The script was first drafted at `infra/aws/auth/migration/005_create_demo_firm.py`.
The owned-paths pre-commit hook correctly blocked the commit — that path is the
AE `CLOUD_OPS_OR_ETL` lane, not DS. Relocated to `scripts/register_demo_tenant.py`
(lane `ANY`), the home of the user-creation precedent the TO itself cites
(`scripts/advi_rolgat_seed_test_accounts.py`). It is a one-shot tenant seed, not
a schema migration. No `.owned-paths.yaml` change required. COO~C confirmed the
relocation correct (21:00Z).

## firmId-token consistency check (criterion 4 — DS-runnable subset)

The TO's four-point check. Three points are DS-runnable now; the fourth depends
on the DE-laned ROUTER_FIRM_SUFFIX entry and moves to the post-DE track.

| # | Wiring point | Token | Status |
|---|--------------|-------|--------|
| 1 | JWT `firmId` claim (auth-handler `jwt.js` derives from `USER#demo.firmId`) | `demo` | VERIFIED |
| 2 | DynamoDB FIRM# key (`PK=FIRM#demo`) | `demo` | VERIFIED |
| 3 | Edge `FIRM_CONFIG` entry (`infra/aws/lambda-edge/_shared/firm-config.mjs`) | `demo` | VERIFIED (added at TO-1/ADVI_DEMOV1.001; `bucket=opal-data-demo`) |
| 4 | Portal `ROUTER_FIRM_SUFFIX` entry | `demo` | DEFERRED — DE lane; post-DE verification track |

All three DS-runnable points carry the identical token `demo`. Both serving
paths resolve to `opal-data-demo`:
- **Dynamic path:** `opal-partners-data` resolves `FIRM#demo.s3Bucket` = `opal-data-demo`.
- **Static/edge path:** `shared-advisor-router` resolves `FIRM_BUCKET_MAP['demo']`
  = `opal-data-demo` from the JWT-injected `X-Firm-Id: demo`.

## Compiler Tools

| Tool | Phase | Result | What it showed |
|------|-------|--------|----------------|
| `comp-routes auth-map` | 1 (before) | OK | `/api/scoped/advisor-intelligence/*` is EDGE-JWT-gated; confirmed the demo claim path goes through `auth-validator-edge` (JWT `firmId` -> `X-Firm-Id`). Claim shape confirmed directly against `auth-handler/dist/jwt.js`: `{sub,name,role,tier,firmId,...}`, no `allowedFirmIds` emitted. |
| `.tools/ds-commit-gate.sh` | 2 (before commit) | exit 0 | py_compile + AST undefined-name scan + ruff py39 clean on `register_demo_tenant.py` (one F541 f-string fixed pre-commit). |
| `comp-routes trace getPlatinumFirmDashboard` | 3 (after) | OK | Route `/api/scoped/advisor-intelligence/platinum/firm/dashboard.json` -> edge JWT -> `shared-advisor-router` -> S3. The trace shows the static behavior origin `S3-opal-data-bd`; `shared-advisor-router` mutates the origin at request time per `FIRM_BUCKET_MAP[firmId]`, so a `firmId=demo` JWT routes to `opal-data-demo`. |

**Phase-2 mandate `bun run build`:** N/A for DS-scope — the only portal change
in the TO (`ROUTER_FIRM_SUFFIX`) is DE-laned and was not made. No portal build
was run. The Phase-3 `comp-routes trace` end-to-end no-403/no-401 smoke needs a
live demo JWT + the DE items; that is the post-DE verification track.

## Files Modified

| File | Change |
|------|--------|
| scripts/register_demo_tenant.py | CREATED — idempotent demo-tenant seed (`2ea34ba81`) |
| org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-22/advi_demov1_to3_registration~C.md | CREATED — this log |

The TO file is left at `<status>pending</status>` — TO-3 does not fully close
until the DE-laned portal items land. COO~C (the driver) owns the TO status;
this RAVC2 attests the DS-scope only.

DynamoDB writes (`opal-users-v2`) are not git artifacts — they are recorded
above with their `createdAt` timestamps and independent `get-item` verification.

## Next Steps

| Recipient | Item |
|-----------|------|
| **2.0.0_SA_COO~C** | RAVC2 — ADVI_DEMOV1.003 DS-scope COMPLETE. Criteria 1, 2, partial-4, 9 met + verified. Criteria 3/6/7/8 + the 4th token point are DE-laned and HELD (post-DE track). |
| **DE lane (via COO~C)** | The three carved portal items remain open: `ROUTER_FIRM_SUFFIX['demo']='demo'` in `portal/src/api/endpoints/advisor-intelligence.ts`, `firmAccess.ts FIRM_ALLOWED_PATHS['demo']`, `_partners/demo/`. The DS records are in place; the portal wiring is the remaining TO-3 work. |
