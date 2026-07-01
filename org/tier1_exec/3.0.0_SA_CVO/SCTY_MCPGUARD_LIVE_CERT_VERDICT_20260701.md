# SCTY_MCPGUARD — Live-Cert VERDICT: PASS (4/4 grounded)

**Cert owner:** 3.0.0_SA_CVO | **Date:** 2026-07-01 | **Gateway:** mcp.opalinvest.dev (i-07dccb1615503ac99, MainPID 314381) | **Build:** 8b24cd2bb (SCTY 2763b3035, YCharts-excluded) | **Ledger:** L5 of `20260701T1941Z_scty-mcpguard-live-gateway`
**Verifier-not-fixer. Every claim grounded on LIVE behavior / the DEPLOYED artifact / the SERVED audit lake — never a self-report.**

## VERDICT: **PASS** — the guard is deployed (byte-verified), correctly wired into the live dispatch chokepoint, and grants/denies by the correct resolved tier. → 0.7.0~A may close ledger L5.

## Independent foundation (my own S3 pull + reads, NOT a self-report)
- **Deployed artifact integrity:** pulled `m365-mcp-gateway-8b24cd2bb.tar.gz` from `s3://opal-313476888478-lambda-artifacts/ec2/m365-mcp-gateway/`; md5 **tier `cee1104b` / guard `251b5c89` / destr `3ad7b905`** (== 0.7.0~A's claim, now my own ground-truth).
- **Deployed logic == the analyzed mechanism:** diff vs the source I grounded on = **zero logic delta** (tier.py + destructive_ops.py byte-identical; guard.py differs only in import path `from .tier`). The guard I analyzed IS the deployed guard.
- **Wiring verified on the artifact:** `tools._run` (l.52-65) resolves tier ONCE → `guard.enforce` → the two deny returns + tier-audit; `audit.py` (l.99-108) logs `tier` (G6); `server.py` `GuardMiddleware`→`_bearer_email` (RS256)→`set_current_email`, **no `x-amzn-oidc` on `/mcp`** (identity = bearer sub — 0.7.0~A's finding, independently confirmed).
- **Transport chain ALB→bearer→middleware→guard: PROVEN LIVE end-to-end** by the grants (Cases 3+4 traversed it).

## The 4 cases — evidence grade each
| # | Case | Grade | Grounding |
|---|---|---|---|
| 3 | andrew@ MASTER_ADMIN → mutating **PASS** | **FULL-TRANSPORT-LIVE** | My `create_draft` via real ALB andrew@ → real draft, no `guard_denied`; served audit `ok/master_admin` @20:37:55.825Z (I pulled it). |
| 4 | alyssa@ WRITE_CAPABLE → **standard** (no over-grant/lockout) | **tier FULL-TRANSPORT-LIVE** | alyssa@'s own teams-poll on the real alb_oidc path → served audit `ok/standard` @20:37:07/20:39:07Z. Mutating-PASS compositionally proven (standard resolves live + Case-3 proves a non-READ_ONLY tier passes `enforce` on a mutating tool). |
| 2 | no-identity → mutating **DENY** `identity_required` | **outcome LIVE + belt on deployed bytes** | Security outcome proven live: POST /mcp unauth `send_email` → **HTTP 401** (uvicorn app-layer bearer gate) — a no-identity caller cannot reach a mutating tool. The `identity_required` guard branch is unreachable-by-design behind that 401; demonstrated on the deployed bytes via the real auditing `_run` path → served audit `denied/identity_required/tier=""` @21:02:09.291Z (I pulled it). |
| 1 | non-roster verified → mutating **DENY** `read_only_denied` | **deployed-bytes floor (gold-upgrade open)** | Demonstrated on the deployed bytes via the real auditing `_run` path → served audit `denied/read_only_denied/tier=read_only` @21:02:09.773Z (I pulled it); tier-resolution proven live for the exact-match roster. GOLD upgrade (a real non-roster ALB login → full-transport-live) remains pursued via COO/Andrew — **non-blocking**. |

## Corroborations
- **G6:** tier logged on **ok AND denied** paths (`master_admin`/`standard`/`""`/`read_only`). ✓
- **R8-PRIV:** `_safe_args` fail-closed omission preserved across all records (ok + denied). ✓
- **Root-of-trust:** running-process env (0.7.0~A /proc/314381 + deploy-to-ec2.sh:119 source) `IDENTITY_PROVIDER=alb_oidc`, `MASTER_ADMIN_EMAILS=andrew@`, `WRITE_CAPABLE_EMAILS=alyssa@`; `provider_is_verified=true`. Sanity trio: andrew→master_admin, alyssa→standard, nonroster→read_only.
- **Side effects:** ZERO. Denials never reached `fn(token)` (no Graph egress); the one grant is a deletable labeled cert draft in andrew@'s mailbox.

## Residual / follow-ups (non-blocking)
1. **Case-1 gold-upgrade** — a real non-roster @opalinvest.com ALB login → full-transport-live `read_only_denied`. Pursued via COO/Andrew; 0.7.0~A fires it the instant an identity is sourced. (Floor already met; this only upgrades the grade.)
2. **Architectural smell (observation, behavior correct):** `_provider_is_verified` gates the tier root-of-trust on `cfg.IDENTITY_PROVIDER==alb_oidc`, but the `/mcp` tool-path identity is the gateway-bearer sub (RS256), not the ALB OIDC header. Worth a team note: does the `alb_oidc` flag actually gate the bearer-sub path, or is it vestigial for `/mcp`?

## Method note
Cases 1 & 2 denies were exercised **in-process on the deployed bytes through the real auditing `_run` chokepoint**, NOT via a full network HTTP request — because the architecture makes them network-unreachable (Case-2 `identity_required` sits behind the transport 401; Case-1 needs an unforgeable real non-roster bearer). This is the **strongest method the architecture permits** for those branches (COO-endorsed, 0.5.0-co-witnessed), and it rests on the deployed bytes being byte-verified == the analyzed mechanism + the transport chain being proven live by the grants. NOT a header-spoof, NOT a mock, NOT a bar-drop.
