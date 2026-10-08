# NFRA_OPLGTW Z-S67: a grace window for the previous refresh-token generation -- how it is bounded in practice, and what `oauth_as.py` records today

**From:** 4.0.0_SA_CRO~Z. **For:** 1.0.0_SA_CTO~Z (msg 31446, round 29 analysis, remedy 2).
**Written:** 2026-10-07 ~22:5xZ. Read-only: the code at site-Z HEAD
(`infra/aws/ec2/opal-gateway/app/oauth_as.py`, 1,000-plus lines; lines cited were printed) and
`surprise-channel/adjudications/ADJUDICATION_v21.Z.md`. No table was read and nothing was changed.

## Read this first: two evidence classes

- **Section 2 (what the estate records) is measured** from the code.
- **Section 1 (industry practice) is this seat's recall.** I fetched nothing from the web: egress off Opal
  infrastructure is not this seat's to take without a word. Vendor defaults and ranges below should be treated as
  approximately right and re-read from the vendors' own pages before a number is ratified from them.

## Answer in four lines

1. **Practice bounds the window in seconds, not minutes:** 0 to 60 seconds, with defaults of 0, 10 or 30.
2. **A window alone does not give up theft detection if the chain keeps ONE live head.** A replay inside the window
   gets a new token that supersedes the lost one; whoever holds the superseded token trips the reuse rule on its next
   refresh. Detection is delayed by at most one refresh cycle, not lost.
3. **This estate cannot return "the same answer again".** It stores only the SHA-256 of each refresh token, so the
   lost successor cannot be re-sent. A grace here must mint a new successor.
4. **Whether seconds are enough for a restart is measurable from records that already exist**, and should be read
   before any window length is chosen (section 3).

## 1. How rotation leeway is bounded in practice (recall)

### The standards

| Source | What it says | What it does not say |
|---|---|---|
| RFC 6749 section 6 and 10.4 | A server may rotate refresh tokens; the old one is then invalid | Nothing about retries |
| RFC 6819 section 5.2.2.3 | Rotation as the countermeasure: a reused old token reveals a theft, so revoke | Nothing about a window |
| RFC 9700, the OAuth 2.0 Security Best Current Practice (2025) | For a public client, refresh tokens are either sender-constrained (bound to a key the client holds) or rotated with reuse detection. On reuse the server cannot tell which party is the thief, so it revokes the active token | **No grace window is defined.** A window is a vendor practice, outside the specification |
| RFC 9449 (DPoP), RFC 8705 (mutual TLS) | Sender-constraint: a stolen token is useless without the client's key | - |

The point that matters for the ruling: **the standard's stronger remedy is sender-constraint, and rotation is the
fallback for clients that cannot do it.** A grace window is a tolerance added to the fallback.

### What vendors do

| Vendor | Name of the setting | Bound | Inside the window, a replay of the previous token returns |
|---|---|---|---|
| Auth0 | reuse interval ("leeway") | seconds; default 0 | a new token pair |
| Okta | rotation grace period | 0 to 60 s; default 30 | a new token pair |
| Amazon Cognito | retry grace period on rotation | 0 to 60 s | a new token pair |
| Supabase Auth | refresh token reuse interval | default 10 s | the session's CURRENT token again (it can, because it stores tokens readable) |
| Keycloak | refresh token max reuse | a COUNT, default 0, not a time | the token works that many extra times |
| Ory Hydra | refresh token rotation grace period | a duration, default 0 | a new token pair |

Three patterns come out of that:

1. **Length.** Sized for a lost HTTP response and an immediate retry: tens of seconds. Nobody defaults above 30.
2. **What a replay returns.** Either the same successor again (idempotent retry; needs the token stored readable) or
   a freshly minted successor (needs a rule for the fork).
3. **Outside the window** every one of them falls back to the strict rule: revoke the family.

### Same-client binding

In practice the grace is given to the same client the family was issued to, at the least:

| Binding | Strength | Available here |
|---|---|---|
| Same `client_id`, same resource, scope no wider | weak: a thief with the token usually knows the client id | yes, all three are on the family head |
| Client authentication (a confidential client's secret or key) | strong | not for a public client; this server accepts a missing `client_id` (`oauth_as.py:916`) |
| Sender-constraint (DPoP key or TLS certificate) | strongest; makes the window nearly moot | not implemented; depends on what the connecting client supports |
| Same network address or user agent | a heuristic, easily wrong both ways | not recorded today |

## 2. What `oauth_as.py` records per rotation (measured)

**The family head** (`:847-866`, updated at `:943-944`):

| Field | Meaning |
|---|---|
| `generation`, `token_hash` | the current generation number and the SHA-256 of its token |
| `status`, and on revocation `revoked_at`, `revoked_reason` (`:784-787`) | `refresh_token_reuse`, `authorization_code_replay` or `operator_revocation` |
| `last_used_at` | time of the latest rotation |
| `client_id`, `resource`, `scope`, `granted_scope` | the bindings |
| `principal`, `tid`, `oid`, `email` | who the family belongs to |
| `created_at`, `absolute_expires_at` (30 days), `idle_expires_at` (7 days) | lifetime |

**One record per generation** (`:867-874`, `:948-957`): `family_id`, `generation`, `token_hash`, `scope`, `issued_at`,
and `consumed_at`, which is set in the same transaction that installs the next generation (`:962-964`).

**How a presented token is judged** (`:908-915`, `:970-973`):

| Case | Result |
|---|---|
| It is the head's current token | rotate: one conditional transaction consumes generation n and installs n+1 |
| Two requests race on the same token and one loses the transaction | `invalid_grant`, "already used by a concurrent request". **The family is NOT revoked** |
| It matches an OLDER generation's stored hash | `revoke_family(..., "refresh_token_reuse")`, at any age, even one second |
| It matches nothing | `invalid_grant`, no revocation |

Five properties that bear on a grace design:

1. **The leeway today is zero, with one exception already built in:** a true race is forgiven (row 2 above). The
   restart case is not a race: the first request committed, so the retry lands in row 3.
2. **`consumed_at` and `issued_at` are recorded, so the age of a replay is computable** with no new field: now minus
   the presented generation's `consumed_at`.
3. **Only hashes are stored.** The server cannot re-send the lost successor.
4. **The reuse branch runs BEFORE the client and resource checks** (`:910-915` precede `:916-919`). So a replay
   revokes whatever client presents it. A grace has to do its own binding check; it does not inherit one.
5. **Nothing records who asked.** No address, user agent or client key is stored per rotation, and nothing records
   whether the successor was ever USED: `validate_access_token` reads the head on every call (`:329`) and writes
   nothing.

## 3. The measurement to take before choosing a length

The r28 incident's own records give the number the window must cover. For the one family revoked in that hour:

- generation n's `consumed_at` (the rotation whose answer was lost), and
- the head's `revoked_at` (the retry that tripped the rule).

The difference is how long after the lost rotation the client came back. If it is a few seconds, the vendors' range
fits. If it is the length of the restart plus the client's back-off, a 30 to 60 second window would not have saved
this session, and the drain (remedy 1, already ruled) is the whole fix. The issuer, `2.0.0_SA_COO~O`, has already
scanned these records read-only; this is two more fields from the same scan.

## 4. Options for the fork (recommendation; the ruling is the CTO's)

| Option | What changes | What it costs in detection | New state needed |
|---|---|---|---|
| A. No grace; the drain only | nothing in the security rule | nothing | none |
| B. Time-bounded grace, new successor, one live head | inside W seconds of `consumed_at`, the previous generation may rotate again; the head moves to a NEW generation and the lost one is marked superseded, so presenting it later is reuse | a thief replaying inside W is not caught at once; caught at the next refresh by either party | a `superseded` mark on the generation record; W |
| C. B, plus "the successor was never used" | as B, and only if the lost successor's access token was never presented | closes B's gap when the real client DID receive its token: then a replay of the old one is always theft | one conditional write, the first time a family's access token validates |
| D. Sender-constraint (DPoP) | the token is bound to a client key | none; the window stops mattering | client support, which is not this estate's to assume |

**Recommendation:** rule A now and take the section 3 measurement. If the measured gap is seconds and the drain
does not remove the case, B with the binding check from section 1 (same `client_id` where one is presented, same
resource, scope no wider) and W at the low end, 10 to 30 seconds. C is the tighter version and the one I would
choose if a write on the validate path is acceptable. I would not go above 60 seconds on any option: beyond that the
window is no longer "a lost response" and starts to be a second valid token.

Two cautions on B and C as they meet this code:

- The successor's key is written with an if-absent condition (`:965`). A grace rotation cannot reuse generation n+1's
  key; it has to mint n+2 and mark n+1 superseded in the same transaction.
- The grace check must come before the reuse branch at `:912-914` and must itself check client and resource, because
  that branch runs ahead of the existing checks.

## 5. What this does not establish

- The cause of the r28 revocation (a rotation committed while its answer was lost) is the issuer's inference, as the
  CVO's adjudication says. The records show the revocation, its reason and its minute.
- How the connecting client retries after a failed refresh (how soon, how many times, with which token) is not
  known here. It decides whether any window helps.
- `REFRESH_ENDPOINT_SECONDS = 30` (`:91`) was not traced; I do not know what it bounds.
- I did not read `revocation.py` or `access_state.py`, so what the kill path or the state layer adds to a grace
  transaction is not covered.
- Vendor figures in section 1 are recall.
