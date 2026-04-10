# .004c Prep Notes — Parallel Scoping Work

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-10
**Status:** Prep only — no code committed, no deploys. Blocks on 0.4.0_DS_ClientPlatform `.004b` landing firm-partitioned `advisor_ownership.json` in S3.
**Purpose:** Pre-scope the edge-side changes for `.004c` so I can move fast once unblocked.

---

## What `.004c` actually has to do

Extend the `.004a` helper in `auth-validator-edge` (NOT shared-advisor-router — `.004a` corrected that TO-level error) to enforce two more path patterns where the URL segment is an account id or relationship id, not an advisor id:

- `/api/scoped/advisor-intelligence/platinum/accounts/{accountId}/*.json` (S3-direct origin)
- `/api/scoped/partners/books/relationship/{relationshipId}/*` (API GW origin)

Rule: non-admin callers are allowed only if `{id}` is in the ownership map entry for `jwt.advisorId`. Admins bypass (Option 3 semantics inherited from `.004a`). Schema version mismatch is a stop-the-line event (500 + ops alert).

---

## Decision 1 -- S3 fetch mechanism

**Pick:** AWS SDK v3 `@aws-sdk/client-s3` GetObject from Lambda@Edge, backed by an in-memory cache keyed by `firmId`.

**Why not CloudFront-subrequest-cached read:**
- Lambda@Edge doesn't have a native subrequest API. You'd have to issue an outbound HTTP request to the distribution itself, which is architecturally gross and creates circular dependency between auth-validator-edge and the distribution it lives on.
- Propagation semantics become muddy — you'd be reading through your own CF cache.

**Why not bundle the map at deploy time:**
- D_00 is daily. Ownership changes propagate within D_00 cadence. Baking the map into the Lambda bundle means every ownership update requires a full .11.x deploy. Unacceptable ops overhead.

**Why AWS SDK v3:**
- Already know the exact S3 key (`opal-data-{firmId-aliased}/platinum/{firmId}/advisor_ownership.json`). Direct GetObject is the simplest viable read path.
- Lambda@Edge Node.js 20.x provides `@aws-sdk/*` at runtime — marking it `external` in the bun build keeps bundle size identical to today's 60KB.
- Existing Secrets Manager fetch (JWT public key) uses the same SDK-v3 pattern, so no new build-toolchain surface.

### Cache shape

```js
// Module-level, lives for the duration of the Lambda@Edge execution environment
// (minutes to tens of minutes across invocations in the same region).
const ownershipMapCache = new Map();  // firmId -> { map: {...}, expiresAt: number }
const OWNERSHIP_MAP_TTL_MS = 60 * 1000;  // 60s, matches .004a JWT pubkey cache pattern but tighter

async function getOwnershipMap(firmId) {
  const cached = ownershipMapCache.get(firmId);
  if (cached && Date.now() < cached.expiresAt) return cached.map;

  // Route to the actual bucket based on FIRM_BUCKET_MAP -- mirror
  // shared-advisor-router's v4 bucket mapping so alias resolution is identical
  const bucket = FIRM_BUCKET_MAP[firmId] || firmId;
  const fullBucket = `opal-data-${bucket}`;
  const key = `platinum/${firmId}/advisor_ownership.json`;

  const resp = await s3Client.send(new GetObjectCommand({ Bucket: fullBucket, Key: key }));
  const body = await resp.Body.transformToString();
  const map = JSON.parse(body);

  if (map.schema_version !== 1) {
    // Stop-the-line event -- emit structured alert, reject with 500
    console.error(JSON.stringify({
      event: "ownership_map_schema_mismatch",
      rule: "004c",
      firmId, expected: 1, got: map.schema_version,
    }));
    throw new Error(`ownership_map_schema_mismatch: ${map.schema_version}`);
  }

  ownershipMapCache.set(firmId, { map, expiresAt: Date.now() + OWNERSHIP_MAP_TTL_MS });
  return map;
}
```

**TTL rationale:** 60s. Matches the "ownership changes propagate within a minute" expectation. Cost impact: ~1 S3 GetObject per firm per Lambda@Edge execution environment per minute. Each region has maybe 5-10 warm instances. So ~5-10 S3 GETs per firm per minute globally = 100-500 GETs per firm per day. At $0.40/million GET, literally fractions of a cent per firm per month.

**Cost upper bound:** Assume 20 firms eventually, 10 warm instances per region per firm, 14 regions, 60-second TTL = `20 * 10 * 14 * 60/60` = ~2800 GETs/minute globally = ~4M GETs/month per firm = ~$1.60/month per firm = ~$32/month total across 20 firms. Negligible.

### FIRM_BUCKET_MAP duplication

`shared-advisor-router` has `FIRM_BUCKET_MAP = { '49financial': 'bd', 'mockadv': 'bd' }`. `.004c` in auth-validator-edge needs the same map to know which actual bucket to read. Two options:

- **A** (today): Duplicate the constant. Small, easy, but two files must stay in sync as new firms are onboarded.
- **B** (future): Extract both Lambdas to share a config module. Requires build-toolchain change. Not worth doing for two firms.

**Pick A.** Add a one-line comment at each copy pointing at the other, and make the constant a named export in both files for grep discoverability.

### Fail-open vs fail-closed on S3 unreachable

**Rule:** fail-closed for non-admins, fail-open for admins.

- If S3 GET fails (network, IAM, 500, whatever) AND caller is non-admin AND path matches a .004c pattern -> return 503 with structured log event `ownership_map_fetch_failed`. Don't 403 (which would look like a scoping denial in metrics). Don't 200 (which would defeat the purpose).
- If caller is admin, the map is irrelevant -- they bypass before the fetch. Fail-open for admins means "never fetch the map if caller is admin", which is the cleanest short-circuit.

Pseudocode for the enforcement flow:

```js
const accountMatch = uri.match(ACCOUNT_SCOPING_PATH);
const relationshipMatch = uri.match(RELATIONSHIP_SCOPING_PATH);
const resourceType = accountMatch ? "account" : (relationshipMatch ? "relationship" : null);
const resourceId = accountMatch?.[1] ?? relationshipMatch?.[1];

if (resourceType !== null) {
  if (payload.role === "admin") {
    // short-circuit, no S3 fetch
  } else if (!payload.advisorId || !payload.firmId) {
    return forbidden("Advisor scoping: missing identity claims");
  } else {
    try {
      const map = await getOwnershipMap(payload.firmId);
      const entry = map.advisors[payload.advisorId];
      if (!entry) {
        // Distinct log event from id-mismatch — helps diagnose stale map vs attack
        console.warn(JSON.stringify({
          event: "advisor_not_in_map", rule: "004c",
          userId: payload.sub, jwtAdvisor: payload.advisorId, jwtFirmId: payload.firmId,
          requestedResource: resourceId, resourceType, path: uri,
        }));
        return forbidden("Advisor scoping: advisor not in ownership map");
      }
      const allowed = resourceType === "account" ? entry.accounts : entry.relationships;
      if (!allowed.includes(resourceId)) {
        console.warn(JSON.stringify({
          event: "advisor_scoping_denied", rule: "004c",
          userId: payload.sub, jwtAdvisor: payload.advisorId, jwtFirmId: payload.firmId,
          jwtRole: payload.role, requestedResource: resourceId, resourceType, path: uri,
        }));
        return forbidden("Advisor scoping: not authorized for this resource");
      }
    } catch (e) {
      if (e.message.startsWith("ownership_map_schema_mismatch")) {
        return { status: "500", ... };  // stop-the-line, already logged inside getOwnershipMap
      }
      // S3 unreachable, network, throttle, etc. — fail closed for non-admins
      console.error(JSON.stringify({
        event: "ownership_map_fetch_failed", rule: "004c",
        userId: payload.sub, jwtFirmId: payload.firmId, error: e.message,
      }));
      return { status: "503", ... };
    }
  }
}
```

---

## Decision 2 -- IAM grant

The `lambda_edge` IAM role (`infra/aws/terraform/portal-auth/iam.tf` — I'll verify when I pick this up for real) currently has grants for Secrets Manager (JWT public key). Needs a new inline policy or attached policy for S3 GetObject:

```hcl
resource "aws_iam_role_policy" "lambda_edge_ownership_map" {
  name = "lambda-edge-ownership-map-read"
  role = aws_iam_role.lambda_edge.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "s3:GetObject"
      Resource = [
        "arn:aws:s3:::opal-data-bd/platinum/*/advisor_ownership.json",
        # Future firm buckets added here as onboarded
      ]
    }]
  })
}
```

Only the specific key pattern. Not `opal-data-*` wildcard (violates least privilege per my role guidance). Not `platinum/**` (too broad — we only want the ownership map, not other platinum artifacts). The `platinum/*/advisor_ownership.json` shape covers all firm-partitioned ownership maps in that bucket.

When new firm buckets are added (e.g., `opal-data-raymond-james`), this policy gets a new resource line. That's a one-line TF edit per firm onboarded.

---

## Decision 3 -- Path patterns

Two new regexes in `ADVISOR_SCOPING_PATH_PATTERNS` (or a new constant `RESOURCE_SCOPING_PATH_PATTERNS` if I want them structurally distinct):

```js
const ACCOUNT_SCOPING_PATH = /^\/api\/scoped\/advisor-intelligence\/platinum\/accounts\/([^/]+)\/.*\.json$/;
const RELATIONSHIP_SCOPING_PATH = /^\/api\/scoped\/partners\/books\/relationship\/([^/]+)\/.*$/;
```

Actually, cleaner to generalize the existing `matchAdvisorScopingPath` helper to return `{ type: "advisor" | "account" | "relationship", id: string } | null`, then the single call site dispatches on `type`. That avoids two separate match passes and keeps the "Phase 1 pattern match" step unified. Refactor task during .004c implementation.

---

## Decision 4 -- Helper extension

Current (`.004a`):
```js
function getAllowedAdvisorIds(payload) {
  if (payload.role === "admin") return null;
  if (!payload.advisorId) return [];
  return [payload.advisorId];
}
```

New (`.004c`) parallel functions:
```js
function getAllowedAccountIds(payload, map) {
  if (payload.role === "admin") return null;
  if (!payload.advisorId) return [];
  const entry = map.advisors[payload.advisorId];
  if (!entry) return null;  // signals "not in map" — caller distinguishes from "empty set"
  return entry.accounts;
}

function getAllowedClientKeys(payload, map) {
  // identical shape, different field
  if (payload.role === "admin") return null;
  if (!payload.advisorId) return [];
  const entry = map.advisors[payload.advisorId];
  if (!entry) return null;
  return entry.relationships;
}
```

Parallel shape to `.004a`, same `null = bypass`, `[] = deny all`, `[ids] = membership check` convention. `.004a`'s helper doesn't change -- `.004c` adds new functions alongside it.

One subtle thing: in `.004a` the `null` return means "admin, skip". In `.004c` it could ALSO mean "advisor not in map". I'm using the convention "null = skip the path check, empty = not-in-map / deny, array = check membership" but that overloads `null` across two cases. Better: return a discriminated object `{ kind: "bypass" | "deny" | "check", ids?: string[] }` or use sentinel strings. Bikeshed during actual implementation — not worth locking in now.

---

## Decision 5 -- Test matrix prep

When `.004b` lands, I'll need:
- An account id owned by Chase (`chase_bertrand`'s `accounts[]` in the map)
- An account id NOT owned by Chase but in 49financial
- A relationship id owned by Chase
- A relationship id NOT owned by Chase but in 49financial
- A fake/nonexistent account id for the "id mismatch" case

DT has Chase + Travis JWTs; they'll run the curls from their side again. I'll monitor CloudWatch for `advisor_scoping_denied{rule=004c}` events + the distinct `advisor_not_in_map` + `ownership_map_schema_mismatch` + `ownership_map_fetch_failed` events.

For the schema-mismatch simulation, I'll either:
- **(a)** Stand up a test bucket with a schema_version=99 file and temporarily repoint the S3 GET, OR
- **(b)** Manually upload a schema_version=99 version of the real ownership map to a versioned prefix, switch to reading that version for a single curl, then revert.

Option (b) is less ops setup; option (a) is cleaner. Decide during implementation.

---

## Decision 6 -- Bundle size sanity check

Current `auth-validator-edge` bundle: 60.32 KB (SHA256 `AsESuygxQAhRzh0eZ0jpoDRGfpO5WdW3DPnLmcZptdk=`).

`@aws-sdk/client-s3` marked external in bun build (Lambda Node.js 20.x provides it at runtime). Expected bundle size growth: <5 KB from the new imports + helper code. Well within Lambda@Edge's 1 MB viewer-request limit (auth-validator-edge runs on viewer-request, not origin-request, so the 1 MB limit applies).

Verified by inspection of `build-nodejs-lambda.sh` logic lines 166-181: any `@aws-sdk/*` in `package.json` dependencies gets a `--external` flag per package. Adding `"@aws-sdk/client-s3": "^3.0.0"` to `package.json` marks it external automatically.

---

## Order of operations once .004b lands

1. Verify prerequisite: `aws s3 ls s3://opal-data-bd/platinum/49financial/advisor_ownership.json` returns non-empty, `aws s3 cp s3://.../advisor_ownership.json -` shows `schema_version: 1` and Chase + Travis entries populated
2. Phase 1 compilers: `comp-routes trace getPlatinumAccountSummary`, `comp-routes trace getPlatinumClientSummary`, `comp-blast auth-validator-edge` (the new dep), `comp-transform` if I touch any portal field contracts (I shouldn't)
3. Add `@aws-sdk/client-s3` to `auth-validator-edge/package.json`, run `bun install` in that dir
4. Add IAM grant to `portal-auth/iam.tf` for `s3:GetObject` on `platinum/*/advisor_ownership.json`
5. Write the code per Decision 4 pseudocode + Decision 1 cache shape
6. Commit source + TF change (one commit, both files)
7. `unset MSYS_NO_PATHCONV && bash build-nodejs-lambda.sh portal-auth auth-validator-edge` (per the gotcha memory)
8. Commit source map [skip ci]
9. `export MSYS_NO_PATHCONV=1 && terraform plan`. Two changes expected: new IAM policy + Lambda@Edge s3_object_version bump. No CF distribution diff UNLESS I also bump `auth_validator_edge_arn` local -- and I will need to, because the published Lambda version will be 12 and CF will still point at 11. Two-step deploy again (same gotcha as .004a).
10. `terraform apply`, verify 0-diff, record deploy, tag `portal-auth-v1.11.10` (first step) and `portal-auth-v1.11.11` (CF rewire). Or if the CF dynamic-local cleanup lands first, single tag `portal-auth-v1.11.10`.
11. Wait for global Lambda@Edge propagation (5-15 min)
12. Curl test (DT runs, I monitor CloudWatch)
13. Session log, pipeline_inventory bump, TO status -> complete, notify DT

---

## Things I will NOT do without explicit re-authorization

- **Write to the ownership map.** Edge Lambda is strictly read-only on this artifact. DS owns writes via D_00.
- **Modify the ownership map schema.** That's `.004b` territory. Schema v1 is frozen.
- **Bypass the schema version check.** A mismatch is a stop-the-line event -- I'll return 500 + ops alert, not "best effort".
- **Use a broader IAM grant than the specific key pattern.** No `s3:*`, no `s3:GetObject` on `opal-data-*/*`.
- **Cache ownership map across firms in a single entry.** Map cache keyed by firmId only.
- **Start `.004c` code before `.004b` is live on S3.** Prep work here is safe because nothing is committed or deployed. Actual code changes block on the map's existence.

---

## Status

Notes only. Zero code committed, zero deploys. Committing this file so the prep context is visible to anyone who picks up `.004c` if I'm unavailable when `.004b` lands.
