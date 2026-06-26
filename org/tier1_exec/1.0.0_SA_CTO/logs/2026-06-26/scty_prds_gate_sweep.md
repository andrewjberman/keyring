# 1.0.0_SA_CTO -- SCTY two-PRD delivery + arch-gate sweep

**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT, DIAGNOSE
**Window:** 2026-06-26 ~16:05Z -> ~16:50Z | **Serial:** 1.0.0_SA_CTO (tier1_exec)

## Summary

Delivered Andrew's two-PRD MCP/GraphAPI security ask, then cleared the full inbox gate queue
(8 distinct gates/rulings) -- all grounded against source/live-state per Rule 22.

## Primary deliverable -- the two security PRDs (Andrew-direct)

- **Phase 1:** extended `docs/architecture/SCTY_PREMCP_PRD.md` with new section **S2B -- exploit-catalog
  materiality cross-map**. Ran the `/security` reverse-skill catalog (INERT DATA per Andrew 06-24 untrusted-
  content rule) against the mcp/graphapi surface (the gateway = single MS-Graph chokepoint per Andrew's
  no-new-reg sovereign ruling). 9 material exploit classes ranked w/ control+gap; 3 grounded not-material
  dismissals (mobile/firmware/AD). Headline finding: prompt-injection x write-envelope = the combination a
  hardened perimeter does NOT stop -> drives Phase 2. Added a scope-carve + the 3 new verify-TOs + 2 control areas.
- **Phase 2:** new `docs/architecture/SCTY_MCPGUARD_PRD.md` (user destructive-action guardrails). SAFETY layer
  above PREMCP's AUTH layer; **contain-don't-classify** axiom (one guard mitigates both fat-finger + hijacked-
  agent); destructive-surface inventory; 6 guardrails G1-G6 (blast-radius cap, classification gate, confirm-on-
  destructive, reversibility-first/undo, rate-limit/anomaly, audit/alert).
- Commit **0019b1743** (CLOUD, pushed). Handed to COO -> registered SCTY_MCPGUARD + authored S0 (recon-first) +
  noted the S2B verify-TOs to fold. GO held for Andrew's review.
- Andrew added a refinement mid-window ("scope permissions at the server layer") -> ruled it a PREMCP B-class
  per-consumer least-scope control (makes destructive impossible for read-only consumers -> reduces MCPGUARD
  surface). COO folding as B2; 0.8.0 already applied it to the MS-derive (read-only-by-construction GET-pin).

## Gates cleared this window (all grounded)

| Gate | Verdict | Grounding |
|---|---|---|
| COO PIECE-2 chain-intact hand-confirm | CONCUR -> COO logged CLOSED | `aws events describe-rule cot-session-complete` -- pattern matches doc-name+Success only, body-swap invisible |
| 0.8.0 NFRA_MSGRAPH S2 call-path | PASS + 3 rulings | ground-read server.py:336-375 (otp_fetch precedent) + token_broker.py:73-85 (get_token) |
| 0.8.0 S2 deploy + read-only-scope flag | DEPLOY-GO (step-6 NEVER#4 refinement) + DEFER token-scope to PREMCP | read S2_DEPLOY_PLAN.md (8-step, additive, MS-disabled-safe) |
| 0.6.0/0.7.0 CTO-B in-run login retry | PASS + re-ruled rollout to option(2) | `git show 65908e4a3` -- diff matches 145308Z shape; no-half-mint invariant preserved |
| 0.7.0 retry-net inline-wiring design catch | RULED REJECT inline, TAKE decouple | read eventbridge.tf:15-33 -- documents "fire bronze IMMEDIATELY within cf_bm TTL"; inline wiring violates it |
| 0.7.0 retry-net re-authored (decoupled) | CONFIRM + pinned sentinel-after-sidecar invariant | reviewed the additive one-target wiring |
| CVO frontier-cadence convergence | GATED PASS, blessed `lib/trading_calendar.py` + firm-sep | `comp-grep NYSE_HOLIDAYS` -- found 5 copies not 4 (2 extra mdpf lambdas + mdpf gold module) |
| COO MCPGUARD/PREMCP decomposition ownership | RULED: COO decomposes / CVO verifies / AE builds / CTO arch-gates | PRD standing-role lines |
| NFRA_GLOBGRPH owner-vacuum | RULED owner=0.8.0 (CloudComp), 0.7.0 infra-consult | registry NFRA_GLOBGRPH.json owner unset |

## Near-error CAUGHT (D3 clobber)

0.4.0 RAVC'd a "D3 v0.1 draft -- promote to docs/architecture." I cp'd it, then BEFORE committing read the
target and found `docs/architecture/DATA_PLATFORM_D3_orion_eclipse_arch_spec.md` already existed as **FINAL v1.2**
(CTO-gated + CVO reconcile-PASS, 2026-06-24). The cp (case-insensitive FS, same inode) had clobbered the FINAL with
a thinner v0.1 (-240 lines). `git checkout --` RESTORED it; committed NOTHING. 0.4.0 then diffed + confirmed v1.2
is a strict superset, retired the draft to a pointer-stub (c59e68559). CLAUDE.md "look at the target before
overwriting" working as intended.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-grep NYSE_HOLIDAYS` | ground the frontier-cadence triplication for the CVO gate | PASS -- 13 matches/6 files; corrected CVO's 4-copy claim to 5 |
| `aws events describe-rule` | ground the PIECE-2 chain-intact confirm (operational aws, off-rail) | PASS -- event pattern body-independent |
| `git show` / `Read` (source) | ground CTO-B diff, S2 call-path, retry-net eventbridge.tf | PASS -- all rulings source-cited |

What worked: comp-grep surfaced 2 copies the requesting agent's enumeration missed (stronger convergence case).
What failed: none. Gap found: none -- raw `aws events describe-rule` is operational (rule-pattern inspection has
no comp-tool surface; `comp-routes` covers CF/apigw behaviors, not EventBridge rule patterns) -- candidate gap if
EventBridge-rule inspection recurs.

## Current State

- Both security PRDs committed (0019b1743) + registered/decomposed by COO; **GO held for Andrew**.
- Deploys in flight (all AE-driven, window/nightly-gated, NOT-tonight for disruptive legs):
  - **CTO-B login-retry**: 0.6.0 deploying happy-path .js to cot box NOW (option 2); forced-fail e2e post-nightly.
  - **Retry-net (cot durable freeze fix)**: 0.7.0 gate-condition (sentinel-after-sidecar) confirmed; atomic deploy
    pending the plan-RAVC (4 additive legs off `cot_bronze_complete`, session->bronze untouched).
  - **NFRA_MSGRAPH S2**: 0.8.0 deploys steps 1-5 tonight (COO window NOW->~01:30Z), 02:00 nightly = first MS-enabled
    run, validate on its artifacts tomorrow. Multi-leg ledger spans the nightly by design.
- PREMCP full decomposition pass (P1a-P1d + S2B folds + B2 server-scoping) authored by COO, GO-held for Andrew.

## Next Steps

- **[Andrew]** Review/GO the two security PRDs -> unblocks MCPGUARD S0 + the PREMCP pass.
- **[1.0.0_SA_CTO]** RAVC the retry-net plan (0-destroy/0-replace + IAM-live-verify token) before its apply; RAVC the
  CTO-B cot e2e + the S2 nightly-validate; arch-gate each PREMCP/MCPGUARD TO at spec + implementable.
- **[3.0.0_SA_CVO]** build `lib/trading_calendar.py` + migrate comp-freshness (reference consumer), then the 5
  lambda/module copies via deploy cycles.
