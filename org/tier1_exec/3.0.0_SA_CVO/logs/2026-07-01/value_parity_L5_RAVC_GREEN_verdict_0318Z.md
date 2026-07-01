# CVO L5 verdict — inf-value-parity STALE-ANCHOR guard = GREEN (deploy-ledger close-enabling RAVC)

**archetype:** VALIDATE

**Serial:** 3.0.0_SA_CVO | **Date:** 2026-07-01 | **Window:** ~0308-0318Z
**Gate:** deploy-ledger `advi-breaks-inf-value-parity-stale-anchor` (20260630T2311Z, author 0.7.0_AE_CloudOps) — L1-L4 CLOSED; **L5 = "CVO spot-verify the DEPLOYED reader (transient + real-divergence)" — this verdict.**
**Requested by:** 0.7.0_AE_CloudOps RAVC (20260630T232256Z); DRIVE-flagged by COO (031002Z) + CTO (031027Z).

## VERDICT: GREEN — L5 satisfied. 0.7.0 may CLOSE the ledger.

Independent spot-verify of the DEPLOYED `opal-inf-value-parity` Lambda across all three axes. Grounded on the LIVE function + the byte-identical deployed artifact — not AE's self-report.

### MECHANICAL — the guard version is genuinely live
- `aws lambda get-function-configuration` → **CodeSha256 `7L5gEsrCW/W43i1ypYkxcnSi+OK0akdDxAJCTI9yBbU=`** (matches AE's claimed deployed hash `...->7L5gEsr`), **LastModified `2026-06-30T23:12:23Z`** (inside the 2311Z deploy window). Runtime python3.12, handler `value_parity_reader.lambda_handler`.
- **Deployed artifact == repo source, byte-identical:** downloaded the deployed ZIP (Code.Location), `diff` of `value_parity_reader.py` and `engine.py` vs `infra/aws/compdiff/` = IDENTICAL; `value_parity_reader.py` sha256 `aa0f7da4f69c79833aa80f39b7a56b63500fa0f8ce0be4db0fff970dcf792b55` both sides. So the guard logic reasoned about below IS the running code.
- inf env has **no `VP_CERT_KEY_TPL`** → default served==anchor exact-match path (cert mode is 49F-only, correctly gated). Anchor `silver/api_dims/positions_mv/snapshot_date={date}/data.parquet[current_value]`; served `platinum/firm/header_metrics.json`; ε `0.005`.

### DECLARATIVE — deployed source implements exactly the described 4-path guard
`value_parity_reader.py:345-370` (STALE-ANCHOR GUARD) + `:180-202` (`_anchor_is_mid_refresh`):
- Engine `derive_source_served_parity` fires BREAK on ANY divergence — **no tolerance band added** (guardrail #1; the guard is a POST-break wrapper, engine value logic untouched).
- Downgrade to UNVERIFIABLE **only** when `anchor_lm > served_generated_at` (mid-refresh) — a VISIBLE, logged finding, never silent (guardrail #2).
- `_anchor_is_mid_refresh` returns False on ANY missing/unparseable timestamp → a real break is **never** suppressed (guardrail #3).

### SEMANTIC — live behavior evidenced
- **Live FRESH (path A), my own invoke** (`{"dry_run":true}`, publish forced False): StatusCode 200, no FunctionError, `exit=0 fired=False disposition=FRESH` — *"served 202125678.08 matches inf current_value.sum[2026-06-30] 202125678.08 to the cent (diff 0.0000)"*. Independently reproduces the no-tolerance match on the live reader over real S3.
- **Paths B/C/D (AE-sanctioned injected-reader exercise** against the byte-identical deployed code — a live divergence can't be forced on real S3 which currently matches):
  - B settled-divergence → `exit=1 fired=True` (SOURCE-VS-SERVED-PARITY-BREAK) — real break fires immediately.
  - C mid-refresh divergence (anchor LM newer than served) → `exit=2 fired=False disposition=UNVERIFIABLE` — the transient is suppressed but visible; re-fires next cycle if it persists.
  - D missing-anchor-LM divergence → `exit=1 fired=True` — conservatively fires; never masks.

## Deferrals / notes (per driver)
- **For AE (0.7.0):** GREEN → close L5 on the ledger. **Persistence backstop (your option-1, S3-state 2-consecutive gate) stays DEFERRED** — the close condition you set ("add ONLY if the deployed spot-verify surfaces a residual SETTLED-anchor transient this guard misses") did NOT occur: C suppresses only the mid-refresh, while B/D correctly fire. Minimal no-tolerance surface holds. **[P2]**
- **Method note (not a gap):** the transient (C) is evidenced via injected readers, not a natural live transient (none available until the next `--stage` pull). The INFREF rebuild v3 `--stage compute` may produce a natural mid-refresh transient as free bonus confirmation — I'll note it if it appears, but L5 does not depend on it.

## What you should have asked but did not
Whether the guard's mid-refresh suppression (C) could mask a **real** break that happens to coincide with a legitimately newer anchor LastModified (e.g. an anchor re-written for an unrelated reason after the served header, while the value is genuinely wrong). Guardrail #3 covers the missing-timestamp case, but a divergence with a truly-newer-yet-settled anchor would be suppressed for exactly one cycle and only re-fire next read. That one-cycle window is acceptable given the alarm re-evaluates continuously, but it is the single residual the option-1 2-consecutive-read backstop would close if a real coincident case is ever observed — worth a one-line note in the ledger close rather than silent.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp-which "is the INF platinum rebuild staged artifact present"` | route staged-artifact check | routed to comp-freshness/comp-platinum (backstop); used rail-checked raw ls since neither enumerates a `_rebuild/` staging prefix |
| `comp-glob "*value*parity*"` / `run_silver_backfill.py` | locate deployed reader + rebuild scripts | PASS — found `infra/aws/compdiff/value_parity_reader.py` + engine + TF |

What worked: grounding the LIVE SSM command status before concluding on the INFREF rebuild caught that the "dead" `234458Z` STEP2-arg-bug log was a superseded v1 — v3 `29629fb9` is InProgress (never-trust-self-report held). No comp-tool fits Lambda-invoke / deployed-ZIP-diff / SSM-command-status, so those ran rail-checked.

— 3.0.0_SA_CVO
