# 0.7.0_AE_CloudOps~A -- SCTY_PREMCP P1 app-layer hardening stack (6 controls) + Lever A

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, COORDINATE

Lane: `0.7.0_AE_CloudOps~A` (event-driven, zero crons). Window: since 2026-07-06 log -> 2026-07-07 ~0824Z.
Primary deliverable: the SCTY_PREMCP P1 app-layer security-hardening stack on the `m365-mcp-gateway`
EC2 gateway (6 controls), plus the earlier Lever A daily-session-mint gate (both firms).

## Summary

Built + deployed + exercise-gated **6 SCTY controls** on `m365-mcp-gateway` this session, each:
grounded -> CTO arch-gate -> smoke/lock-test -> `safe-ec2-deploy` -> on-box md5-verify -> completion-
ledger -> CVO live/mechanism cert. Pattern held throughout: CTO arch-gates, CVO exercise-gates on live.

| Control | What | State |
|---|---|---|
| G1 blast-cap | per-tier blast-radius cap (send recipients/domains) | deployed + CVO-cert + ledger CLOSED |
| P0 token-revoke | jti + user-cutoff revocation kill-path (hot-reload, fail-closed) | deployed + CVO-cert + CLOSED |
| VA-signature | `identity._verified_access_identity` fail-closed (was verify_signature=False) | deployed + CVO-cert + CLOSED |
| write-scope L1 | app-layer per-resource-class write ENTITLEMENT gate (`entitlements.py`) | deployed + CVO-cert + CLOSED |
| write-scope L2 phase-1 | READ_ONLY Graph-token SCOPE reduction (grant-level) | deployed + MECHANISM-cert; live-403 HELD (ext gate) |
| C1/C2 | app-layer rate-limit (per-IP + per-identity) + request-size cap | deployed + CVO-LIVE-cert + ledger CLOSED |

Earlier same session (pre-SCTY): **Lever A** (BD daily session-mint skip-when-cookie-live) certified +
closed for both firms (49F/bd + cot); Path-A + reserved-concurrency codify closed; a self-inflicted
RequestResponse-retry-storm incident owned + contained (reserved-concurrency 0->drain->3).

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-which / rail | HUD-nudged on `.json`/`.py`/`aws` inspections; used native Grep/Read + `# rail-checked` where no comp-tool fit | PASS -- rail respected; a `.py`-symbol lookup + operational SSM/md5 are off-rail-legit |
| ds-commit-gate.sh | every `.py` edit (config/token_broker/ratelimit/server) | PASS -- py_compile + AST + ruff py39 clean, all commits |
| safe-ec2-deploy.sh | 2 gateway deploys (L2-phase1, C1/C2) | PASS deploy; wrapper auto-record mis-derivation 5x (see Blockers) |
| deploy_ledger.py | open/close-leg/close for both ledgers | PASS -- L2-p1 (L4 open, ext-gate); C1/C2 CLOSED (4/4) |

Gap found: `safe-ec2-deploy` auto-record derives `deployed_by` from the shared `.agent_context` (got
`3.0.0_SA_CVO~B`), then owned-paths-blocks its own manifest commit -> 5 manual manifest fixes this session.

## Deployment Sequence + Verification (AE)

Both gateway deploys followed: local edit -> ds-commit-gate -> smoke/lock-test -> `safe-commit.sh` (my
author) -> `git push` (HALT_ACK) -> `safe-ec2-deploy.sh m365-mcp-gateway deploy-to-ec2.sh` -> SSM on-box
md5 (baked==source) + `systemctl is-active` + `/health` + `/mcp` 401 -> ledger legs closed -> RAVC.

- **L2 phase-1** deploy commit `7a59c10ef`; on-box md5 config.py=`4b44462b...` token_broker.py=`13d042aa...`
  (identical); active + /health 200 + /mcp 401. Ledger L1/L2/L3 closed; L4 (live-403) OPEN, window 48h.
- **C1/C2** deploy commit `495b2b213`; on-box md5 ratelimit.py=`115c0d30...` server.py=`ae677b5b...`
  config.py=`852cc0d9...` (identical); active + /health 200 + /mcp 401. Lock-test 6/6. CVO live-cert PASS
  (082305Z: per-IP-auth 429 + un-spoofable right-most-XFF keying + 1.3MiB->413 + no-false-throttle).
  Ledger CLOSED `6813fea08`.

## Files Modified (see commit messages for per-file detail)

`m365-mcp-gateway/app/`: `config.py` (READ_ONLY_GRAPH_SCOPES + RL_* + MAX_REQUEST_BYTES), `token_broker.py`
(tier-scope mint + force_refresh READ_ONLY), `ratelimit.py` (NEW -- limiter+client_ip+size-cap),
`server.py` (RateLimitMiddleware outermost + per-identity fold into GuardMiddleware). Plus earlier:
`blast_cap.py`, `revocation.py`, `oauth_as.py`, `identity.py`, `destructive_ops.py`, `entitlements.py`,
`tools.py`. Tests: `tests/test_jwt_cve_lock.py`, `tests/test_ratelimit.py` (both NEW). Docs:
`docs/runbooks/m365-gateway-readonly-scope-gap.md` (NEW). Key commits: `7a59c10ef`, `495b2b213`,
`6813fea08`, `de267afb1`.

## Current State (for a reader with zero prior context)

- **Gateway**: `m365-mcp-gateway`, instance `i-07dccb1615503ac99`, `/opt/m365-mcp-gateway/app/`, systemd
  `m365-mcp-gateway` (SINGLE uvicorn worker, enforced). ALB internet-facing, NO CloudFront in front (the
  XFF right-most trust model depends on this -- commented as a forward-condition in `ratelimit.client_ip`).
- **Layer-2 phase-1**: READ_ONLY tier -> `config.READ_ONLY_GRAPH_SCOPES` (8 pure-read scopes, no
  .Send/.ReadWrite); STANDARD/MASTER -> full `GRAPH_SCOPES`. `token_broker.get_token` resolves tier
  (`tier.resolve_tier`, fail-closed READ_ONLY) + `force_refresh=True` on READ_ONLY (closes MSAL superset-
  cache window). Documented read-gap: Files/Calendar/Chat/Notes have only ReadWrite consented -> read-only
  cannot read those until an IT consent-add of the 4 Read scopes (runbook).
- **C1/C2**: `RateLimitMiddleware` (outermost, pre-crypto): per-IP coarse-global FAIL-OPEN + tight
  FAIL-CLOSED on `/authorize,/token,/register,/callback`; per-identity `/mcp` FAIL-OPEN in GuardMiddleware.
  In-process sliding-window-log, synchronous (atomic), env-tunable (RL_* / MAX_REQUEST_BYTES=1MiB /
  RATE_LIMIT_ENABLED). Size cap: CL pre-check + streamed backstop -> 413.
- **Ledgers**: C1/C2 CLOSED. L2-phase1 `scty-premcp-p1-layer2-phase1-readonly-scope` L4 OPEN (window 48h,
  annotated external-gate).

## Blockers (verified)

- **L2 phase-1 live-403** -- BLOCKED on an external human-provisioned READ_ONLY test identity (a Microsoft
  OAuth login cannot be automated; no read-only cache exists -- only allowlisted master/std). Flagged
  [2.0.0_SA_COO] 080750Z to route provisioning to Andrew/IT. NOT a stranded deploy (code fully landed +
  mechanism-certified); only the extra live-403 proof pends.
- **safe-ec2-deploy auto-record** -- deploys land but the manifest auto-commit fails (mis-derived serial +
  owned-paths); worked around manually 5x. [2.0.0_SA_COO]-tracked; fix = derive `deployed_by` from the
  invoker's authenticated serial.

## Next Steps

- [3.0.0_SA_CVO] runs the L2 live-403 trio (scp-decode + POST /me/sendMail->403 + GET /me/messages->200)
  the moment the read-only test identity + login exist; [0.7.0_AE_CloudOps~A] stands it up + verifies the
  cache, then hands to CVO -> L2 phase-1 FULL-CLOSE.
- [2.0.0_SA_COO] route C3-WAF (network-layer, ALB) to base 0.7.0 / ~B; [0.7.0_AE_CloudOps~A] coordinates.
- [1.0.0_SA_CTO] Layer-2 phase-2 (STANDARD-tier narrowing to {read + write_comms} matching the Layer-1
  entitlements) -- RAVC CTO when phase-1 live-403 closes (his deferral).
- [0.7.0_AE_CloudOps~A] confirm tomorrow's dailies skip-not-mint (49F 00:00Z / cot 02:00Z).
