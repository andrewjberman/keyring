# SCTY_MCPGUARD — `_provider_is_verified` vs the `/mcp` bearer-sub identity source (seam note)

**Filed:** 2026-07-01 by 0.7.0_AE_CloudOps~A during the SCTY live-cert.
**Status:** POST-CERT FOLLOW-UP — **behavior is CORRECT, not a cert-blocker.** Banked at the
explicit request of 3.0.0_SA_CVO (cert owner) + 0.5.0_AE_OpalETL (module author). Route: team
note / CTO for a doc line or a small refactor decision.

## The observation

The tier root-of-trust in `tier.py` gates elevation on the *configured identity provider*:

```
# tier.py:41-54
def _provider_is_verified(cfg) -> bool:
    provider = getattr(cfg, "IDENTITY_PROVIDER", None)   # == "alb_oidc" on the box
    if provider in _ALWAYS_VERIFIED: return True
    ...
```

`resolve_tier` returns `READ_ONLY` for everyone if `_provider_is_verified` is False (tier.py:83-84).

But on the **`/mcp` tool-dispatch path** (the only path that runs guarded tools), the identity
that `resolve_tier` keys on does **not** come from the ALB `x-amzn-oidc-data` header. It comes
from the **gateway's own RS256 Bearer token `sub`**:

- `GuardMiddleware` on `_is_mcp_path` calls only `_bearer_email(request)` → `set_current_email(sub)`
  (server.py:118-143). It does **not** call `identity.get_user_email` (the ALB-OIDC extractor).
- `_bearer_email` (server.py:91-106) validates the gateway JWT (RS256 / iss / aud / exp) and takes
  `email = claims["sub"]`; 401 if the bearer is missing/empty or has no subject.
- The bearer's `sub` was minted from a real Microsoft-OIDC login at `callback` /
  `redeem_code_for_email` (server.py:258).

So `IDENTITY_PROVIDER=alb_oidc` describes the **access layer / `/login` GUI path**
(`identity.py._alb_oidc_identity`, ES256 vs the ELB key), whereas the **`/mcp` tier key is the
RS256 gateway-bearer sub**. The `_provider_is_verified` check therefore functions as a
**config/boot-level enable-flag** for elevation (backed by `config.validate()` forbidding
spoofable providers in prod), not as a per-`/mcp`-request signature check of the identity that is
actually used.

## Why it's still CORRECT today (not a vuln)

The chain is doubly sound:
1. **Per-request:** the `/mcp` identity is the RS256-verified gateway bearer sub — always
   signature-verified, never a raw header.
2. **Provenance:** that sub traces to a real Microsoft-OIDC login (callback redeem), and
   `config.validate()` boot-forbids `header`/`tailscale` in prod, so an elevated tier can only be
   enabled behind a signature-verifying access layer.
3. **Live proof:** both roster users resolve correctly on the running service — andrew@→master_admin,
   alyssa@→standard — and a non-roster identity → read_only (verified in the SCTY cert, audit
   records 2026-07-01T21:02:09Z; CommandId 8710fb1f).

No forgeable path was found: a raw ALB header does not reach the `/mcp` tier decision, and a bearer
that validates always carries a non-empty sub.

## The seam worth a decision

`_provider_is_verified`'s `alb_oidc` check is **coupled to the wrong identity source name** for the
`/mcp` path: it reads as "the ALB OIDC header is verified" when the thing actually gating `/mcp`
elevation is "the gateway RS256 bearer is verified (and elevation is enabled at boot)." Two clean
options for the team:

1. **Document** (cheapest): a one-line note in `tier.py` / the SCTY design doc stating that on
   `/mcp` the tier key is the RS256 bearer sub, and `_provider_is_verified` is the
   *config/boot enable-gate* for elevation (not a per-request check of the `/mcp` identity).
2. **Refactor** (clarity): rename/reframe the gate to `elevation_enabled(cfg)` (boot-level) and add
   an explicit, separate assertion at the `/mcp` seam that the identity source is the RS256 bearer —
   so the flag's meaning matches what it actually guards.

Either resolves the "is the `alb_oidc` flag vestigial for `/mcp`, or load-bearing?" question the
CVO raised. Recommendation: option 1 now (doc line), option 2 if the identity layer is next touched.

## Anchors

- `tier.py:41-95` (`_provider_is_verified`, `resolve_tier`), `tier.py:104-129` (boot-gate)
- `server.py:91-106` (`_bearer_email`), `server.py:118-143` (`GuardMiddleware`), `server.py:258` (callback redeem)
- `tools.py:47-77` (`_run` chokepoint) · deployed md5 tier `cee1104b` / guard `251b5c89`
- SCTY cert thread 2026-07-01 (CVO 3.0.0 / author 0.5.0); deny-proof CommandId `8710fb1f`
