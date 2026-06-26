# Session Close — 0.2.0_DE_PortfolioAnalytics — 2026-06-26 ~1455-1650Z
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE

Session-spanning summary. Two Yang/Andrew-direct items shipped end-to-end. Per-item depth
lives in the two task logs (this is the index + handoff):
- `index_etf_toggle_fe_wiring.md` — Index/ETF benchmark toggle.
- `peers_missing_models_diagnosis.md` — /Peers missing-models + value bug (incl. corrections).

## Startup
Registered (was NOT REGISTERED), armed persistent inbox Monitor (task bg5w5nd4j). Triaged 9
stale inbox msgs (Apr tooltip/lint = historical; two 06-22 cottonwood re-smokes = already
CLOSED in the launch-emit ledger). Pod 0.2 had been dormant since 2026-04-09.

## Item 1 — Index/ETF benchmark toggle (Yang-direct, DS handoff f3cfe6a4a) — SHIPPED LIVE
The Up/Down Capture, Rolling Sharpe, Max Drawdown sub-views of `ReturnVolatilityScatter` did
not respond to the Index/ETF toggle (they read a single index-only timeseries). Wired
`benchmarkType` + toggle-resolved compositions through `ReturnVolatilityScatter` into all 3
charts; `selectBenchmark()` picks index vs etf with pre-cutover fallback to the legacy
`benchmark_return` alias; null-guards per chart.
- FE: portal DEV `e5029515` -> promoted to PROD `bee2842f`, tag **portal-v2.1.126**, CI
  28248041838 success (DT lane).
- Verify: DS data-verify PASS; my behavior-verify on the live served artifact PASS (all 3
  charts differ index vs etf, model-only control invariant; INT 2026-06-18 ties). Pixel
  screenshot was blocked (shared Playwright browser locked) -> substituted compute-equivalence
  on live data.

## Item 2 — /Peers Model toggle missing ST/LTC/LTA (Andrew-direct) — FIXED LIVE
TWO stacked producer bugs in `yang-generate-peer-performance` (FE was correct throughout —
it renders a toggle per model present in the served data).
1. **Missing models** — `parse_peer_excel` hardcoded section start-cols `[0, 20]`; the wide
   20260618 source (51 cols) has its 2nd block at col 26 -> ST/LTA/LTC silently dropped. My
   fix `d4ae41b84` (dynamic "Return/Risk" header-column scan). Also found a dangling manifest
   pointer (`uploads/...20260618.xlsx` missing, rotated to archive) -> flagged so the rerun
   used the wide source, not stale 202512.
2. **Wrong values** — the same wide layout added leading 1D/MTD periods, shifting period
   columns by 6; fixed period offsets read the wrong period (served "1Y" was actually 1Q, SI
   null). **Andrew caught it.** DS fixed `b72df1095` (header-label period mapping). DT deployed
   **yang-v2.4.13 -> v2.4.14** (wide-file restore + deterministic invoke + CF-invalidate).
- Final verify PASS, SOURCE-grounded: served INT 1Y=14.4275 ties the raw source Excel cell
  exactly; old bogus 6.3888 now correctly served as 1Q; SI populated all 5; cross-model
  1Y risk-ordering sane (UST 3.80 ... LTA 22.40).

## Verification lesson (banked)
My first /Peers value-verify overclaimed: "INT 1Y=6.3888 ties exact" grounded against my OWN
parser's output (self-consistency), which carried the same period-offset bug — not against
independent truth. Retracted; re-verified against the source Excel cell. Memory:
`feedback_verify_semantic_axis_value_not_presence.md`. Verify VALUE-correctness (magnitude/
sign/known ref), not presence or self-consistency.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| `pipescript --resource peer_performance` | PASS | located producer thread model-portfolios/yang-peer-performance |
| `pipescript --fe-reachability` | PASS | thread-tier; used Grep for component-level consumer trace |
| `comp-which "<deps>"` (x2) | PASS | manifest-backstop routing |
| `comp-transform schema-check` (3 chart comps) | FAIL | components not in comp-transform registry (GAP, logged) |
| `.tools/ds-commit-gate.sh` (peer Lambda) | PASS | py_compile + AST + ruff clean |

What worked: `pipescript --resource` nailed the producer instantly; running the actual Lambda
`parse_peer_excel` against the live source Excels was the decisive grounding (reproduced the
2-model + value defects, proved the fixes). What failed / GAP: `comp-transform schema-check`
has no entry for `RollingCaptureChart`/`RollingSharpeChart`/`MaxDrawdownChart` (recharts
presentational chart components) — coverage gap flagged for the comp-transform registry.

## MCP traffic
~30 messages handled (heavy DS/DT coordination across both items). Significant: DS handoff
f3cfe6a4a (ACK->done->verify-split); DT GO->promote portal-v2.1.126; peer fix handoff -> DS
commit d4ae41b84 -> DT yang-v2.4.13/14; the dangling-pointer warning to DT; DS value-bug FYI
+ my retraction/own; final PASS closes to DS+DT. All RAVC loops closed.

## Files Modified
Portal (DEV `e5029515`): see commit message — 6 files (portal-proxy.ts type, ReturnVolatility
Scatter, 3 charts, ModelPortfolios.tsx). Producer fix `d4ae41b84`+`b72df1095` (DS/DT lane;
my patch deliverable `org/.../deliverables/peer_parser_fix.patch`). Workspace logs: see commit
messages 55a148983, 92213fbc5, 9743a99f0, 51794a86b, 875a0e87c, 3bdeb83f1, f58510ec1.

## Current State
Both items LIVE. Index/ETF toggle on PROD (portal-v2.1.126). /Peers fixed on yang-v2.4.14;
served peer_performance.json = 5 models with correct values (generated 16:40:37Z, data_as_of
06-18). FE unchanged for /Peers (period keys stable). CF invalidations propagating (~5-10min
windows) at session-close time.

## Next Steps
- [Operator/Andrew] Final pixel eyeball of live /Peers (5 toggles + corrected values) + the
  Index/ETF toggle on the 3 charts, once CF clears — I could not screenshot (portal /login,
  no creds).
- [0.2.0_DT_PortfolioAnalytics] (info) both deploys complete + ledgers; nothing owed to me.
- Pod 0.2 otherwise IDLE: available; event-driven.

## Blockers
None. Pixel-screenshot residual is a credential/CF-window limitation (handed to operator), not
a blocker — functional correctness verified via served data + source-Excel tie.
