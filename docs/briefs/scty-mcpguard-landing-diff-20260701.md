# SCTY_MCPGUARD — Live-Path Landing Diff (for 0.7.0 owner-ack + CTO landing-gate)

**Build-lane:** 0.5.0_AE_OpalETL | **Deploy-lane (owner):** 0.7.0_AE_CloudOps (Rule 12: my diff → their ack → deploy-to-ec2.sh S3→SSM) | **Landing-gate:** 1.0.0_SA_CTO | **Live-cert:** 3.0.0_SA_CVO
**GO-LIVE HOLD:** (b) 0.8.0 independent no-bypass corroboration MUST clear first (CTO). This doc is the DRAFT to circulate in parallel — NOT a deploy.
**Chain:** spec ae651397e → CTO Part-A PASS → tier_resolve 13b4cdcee (gate-c PASS) → registry af26eadbf → guard (this) → landing.

## Scope of THIS landing
The tier + G2 **foundation** wired into `_run()` with the two fail-closed denials + tier-in-audit. **G3 confirm-on-irreversible / G1 recipient-cap / B2 / full-G6 layer ON TOP next** (this landing is the seam they extend). Everything here is built + tested (47/47): `tier.py` (18) + `destructive_ops.py` (16) + `guard.py` (13).

## Files ADDED to `app/` (built + tested, drop-in)
- `app/tier.py` — user-type resolution (fail-closed root-of-trust + ADD-1/2/3).
- `app/destructive_ops.py` — the G2 `destructive_ops` registry (5 send-class mutating + 20 SAFE + fail-closed unknown).
- `app/guard.py` — the `_run`-entry gate (`enforce`/`resolve_and_enforce`).
- (+ their `test_*.py`.)

## DIFF 1 — `app/config.py`: add 3 SECURITY-CRITICAL config vars (NO new boot-guard)
```python
# --- SCTY_MCPGUARD tier config (SECURITY-CRITICAL; changes AUDITED per CTO gate-c Q1) ---
# EXACT-match sets (tier.py uses == , never substring/pattern). Sovereign pin + opt-in write.
MASTER_ADMIN_EMAILS: tuple = tuple(e.strip().lower() for e in
    os.environ.get("MASTER_ADMIN_EMAILS", "andrew@opalinvest.com").split(",") if e.strip())
WRITE_CAPABLE_EMAILS: tuple = tuple(e.strip().lower() for e in
    os.environ.get("WRITE_CAPABLE_EMAILS", "").split(",") if e.strip())   # EMPTY default (opt-in)
VA_SIGNATURE_VERIFIED: bool = os.environ.get("VA_SIGNATURE_VERIFIED", "0") == "1"  # flips on PREMCP P1b
```
**ANCHOR, NOT REINVENT (grounded catch):** `config.validate()` lines **177-196 ALREADY implement the boot-guard** the tier root-of-trust needs — it raises in prod unless `IDENTITY_PROVIDER == alb_oidc` OR configured-cloudflare (SCTY.W2 M365-2). So the ADD-3 boot-gate is **already live**; I add NO parallel `validate_identity_provider_for_prod` (would drift). `tier.py._provider_is_verified` is the per-request runtime BELT to that boot-time SUSPENDERS. **Forward-note (P1b):** when P1b lands VA signature verification, BOTH must update together — config.validate:184-188 to allow `verified_access`, AND flip `VA_SIGNATURE_VERIFIED=1` — or master-admin stays read-only under VA (fail-closed, safe). `tier.py.validate_identity_provider_for_prod` is left as an OPTIONAL standalone assertion (redundant w/ the existing boot-guard; do NOT double-wire).

## DIFF 2 — `app/audit.py`: add `tier` to the audited record (G6, every call)
```python
def log_call(email, tool, args, outcome, detail="", tier=""):   # + tier param
    _emit({
        "ts": ..., "user": email, "tool": tool, "args": _safe_args(tool, args),
        "outcome": outcome, "detail": detail[:500],
        "tier": tier,            # + SCTY_MCPGUARD: the resolved user-type on EVERY call
    })
```
(Additive; existing callers unaffected — `tier` defaults "".)

## DIFF 3 — `app/tools.py` `_run()` (line 47): resolve tier ONCE → gate → audit-with-tier
```python
def _run(tool, args, fn):
    try:
        email, token = _user_token()
    except NeedsLogin as nl:
        audit.log_call(get_current_email(), tool, args, "needs_login")
        return {"needs_login": True, "message": str(nl), "login_url": nl.login_url}
    except RuntimeError:                              # CTO Q3(i): no verified identity -> DENY (not 500)
        audit.log_call(get_current_email() or "", tool, args, "denied", "no verified identity")
        return {"error": "no verified identity established", "guard_denied": True, "code": "identity_required"}
    from . import guard, tier as _tier               # SCTY_MCPGUARD
    _t = _tier.resolve_tier(email, get_config())      # resolve ONCE (-> audit + gate)
    try:
        guard.enforce(tool, email, _t)                # G2 + fail-closed (Q3 (i)+(ii))
    except guard.GuardDenied as gd:
        audit.log_call(email, tool, args, "denied", gd.reason, tier=_t.value)
        return {"error": gd.reason, "guard_denied": True, "code": gd.code}
    try:
        result = fn(token)
        audit.log_call(email, tool, args, "ok", tier=_t.value)
        return result
    except graph.GraphError as ge:
        audit.log_call(email, tool, args, "error", str(ge), tier=_t.value)
        return {"error": str(ge)}
```
SAFE reads: `guard.enforce` returns immediately (OpClass.SAFE bypass) — the only added read-path cost is one dict lookup + one tier resolve (both O(1)); acceptable. Mutating: READ_ONLY→deny, no-identity→deny; write-capable tiers pass (G3/G1 next).

## DIFF 4 — `/teams/poll` G6-audit fold (the read-only audit gap 0.7.0 flagged)
`server.py:teams_poll` (grounded READ-ONLY) skips `audit.log_call`. Fold it + its MCP twin `poll_addressed_teams_messages` into one audited path — add after the `poll_addressed_impl` call:
```python
    result = poll_addressed_impl(token, since)
    audit.log_call(email, "teams_poll", {"since": since}, "ok")   # + G6 coverage (read-only)
```
(Declare `teams_poll`/`poll_addressed_teams_messages` in audit `_ARGS_ALLOWLIST` with `{"since"}` metadata-only.) Read-only → audit-only fold, NOT a G2/G3 guard.

## Wiring-tests (CTO Q3 (i)+(ii)) — DONE (test_guard.py, 13/13)
(i) no-identity + mutating → DENY(identity_required); (ii) READ_ONLY + mutating → DENY(read_only_denied); SAFE bypass; write-capable pass; resolve_and_enforce end-to-end. + tier 18/18 + registry 16/16 (47 total, ds-commit-gate clean).

## Landing-gate checklist (CTO verifies at this diff before GO-live)
| Item | State |
|---|---|
| merged config.validate raise-path | ANCHORED — existing boot-guard (config.py:177-196) IS the raise; +3 config vars only; P1b forward-note |
| the 2 wiring-tests pass | DONE (test_guard.py 13/13) |
| registry fail-closed | DONE (af26eadbf 16/16, unknown→destructive) |
| /teams/poll real capability | GROUNDED read-only → G6 audit-fold (DIFF 4) |
| **0.8.0 no-bypass corroboration** | **PENDING — GO-LIVE HOLD** (independent check of 0.7.0's enum) |

## Coordination / deploy (owner rules, confirmed)
1. 0.7.0 owner-ack this diff → 0.7.0 deploys via deploy-to-ec2.sh S3→SSM (Rule 12; they own the box + deploy-ledger). I do NOT deploy.
2. No change to the 29-tool surface / token scope / REST routes here (B2 read-only mint is a SEPARATE change needing App-2 consent + CTO).
3. CVO live-cert AFTER deploy: an actual READ_ONLY-tier mutating call is DENIED live; a no-identity mutating call is DENIED live — proven on the running gateway, not asserted.

*Grounded 2026-07-01 against config.py:155-201, audit.py, tools.py:47, server.py:310. Build-lane deliverable (docs/briefs). Author: 0.5.0_AE_OpalETL.*
