# LT/ULT scatter trace + typing canon (Pod4) + acct-dist render leg — 0.4.0_DE_ClientPlatform

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, COORDINATE, VALIDATE

**Date:** 2026-08-04 (~19:10–21:20Z)
**Task Order:** ad-hoc (Andrew-direct chain) + CTO 203147Z typing-canon MCP work order + DS acct-dist render leg
**Status:** COMPLETE (all three threads closed in-window)

---

## Objective

(1) Track down LT/ULT missing from the Return-vs-Volatility scatter (Andrew report); (2) roll
the fix knowledge out to the new 0.2.0_DE seat + 0.2.0_DS producer half (Andrew-assigned);
(3) execute the hyphen display-typing canon on Pod4 (Andrew via Yang, CTO relay); (4) run the
acct-dist heal render-verify leg (DS ping).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-routes | `comp-routes behaviors` | PASS | resolved /api/general/* origin (S3 opal-data-portal-v2, public-data-router rewrite) + cache-control-injector chain |
| comp-grep | `comp-grep "cache-control-injector" infra --files` | PASS | located the origin-response injector source |
| comp-grep | `comp-grep "max-age" infra/aws/lambda/edge` | WARN | 0-scanned FAILED-RETRIEVAL warning fired correctly (wrong pathspec: lambda-edge); re-aimed by hand |
| tsc (portal gate) | `bun x tsc -b` (x2) | PASS | exit 0 at both commits |
| ui-smoke | 4 renders (benchmark fixture x2, acctdist fixture, plain) | PASS | the exercised proof for all three threads; --click Benchmark + --fixtures live-artifact pattern |

**What worked:** fixture-render (REAL served bytes through REAL FE code) settled both "is it
fixed" questions without touching PROD; comp-routes answered the cache question in one call.
**What failed:** nothing silently; the comp-grep 0-scan warning did its job.
**Gap found:** none.

---

## Work Completed

### 1. LT/ULT scatter trace (DIAGNOSE — no FE defect)
Andrew reported LT/ULT missing from Return-vs-Volatility. Traced BOTH halves: FE mapping chain
verified sound at source (canonicalModelCode/getCanonicalModelName idempotent, colors present);
served artifact pulled S3-direct — regenerated 19:51:03Z by DS's producer fix with all five
canonical codes + full YTD volatility quartet. Fixture render through deployed FE code: all 5
model circles + ULT/LT split-diamond + 5 legend chips OBSERVED. Root cause of Andrew's
observation: he looked minutes BEFORE DS's 19:51Z land (pre-fix artifact honestly had 3 usable
models); /api/general/* carries max-age=60 so the serve self-healed. PROD deploy confirmed
shipped: v2.1.157 @6398630a (0.2.0_DT, CI success). Phase-3 benchmarks verify reported to DS
(200116Z) — closes the benchmarks TO acceptance criterion 4.

### 2. LT/ULT rollout handoffs (Andrew-assigned, recorded @fe42f2e6bc)
Andrew-direct: same closure rolls to Positioning/Attribution/FactorTilts, owner NEW seat
0.2.0_DE_PortfolioAnalytics; my leg = execution recipe. Pre-scouted the ground: positioning +
factor-tilts artifacts still emit legacy LTC/LTA; attribution artifact MISSING LT/ULT rows
entirely (silent-drop class live); producer file:line pointers for all 3 yang_pipeline lambdas.
Recipe sent to 0.2.0_DE (202936Z) + producer-half view to 0.2.0_DS (203310Z, per Andrew
follow-up). COO closed both dispatch notes (owned-paths already enumerated; split worded:
FE=0.2.0_DE now, producers=0.2.0_DS morning-wave).

### 3. /watcher — Monitor was ABSENT all session
Crash killed the predecessor's Monitor; no orphan existed; filesystem inbox unwatched with 5
unread top-level messages (broker channel masked the gap). Armed task b8d5qeawq
(/cygdrive/c/ prefix), TaskOutput-confirmed running, 9-message backlog drained and acted.

### 4. Display typing canon, Pod4 (Andrew via Yang, CTO relay 203147Z) — portal DEV @02b7f351
displayModelName() added to modelPortfolioColors.ts as THE render-boundary resolver (canon:
Ultra Short-Term / Short-Term / Intermediate-Term / Long-Term / Ultra Long-Term); identity
keys untouched per scope; applied at all Pod4 emission sites; Rolling Sharpe/Capture/Drawdown
local display tables DELETED (net-negative on maps). HAZARD closed en route: getModelColor
partial-match resolved 'Long-Term' into 'Long-Term Aggressive' (wrong color) — exact-match
aliases added for all five canon strings; getCanonicalModelName accepts display strings.
Verified: tsc -b clean + fixture render observed (canon strings exact, colors correct).
SURFACE_ACK audited. 0.2.0_DE unblocked on the shared lib (they held it pending my word) and
consumed it same hour — their Pod2 half landed DEV @604101df atop mine. CTO ACCEPTED 210613Z
(one-mapping execution named the model shape; hazard close ratified).

### 5. Acct-dist heal render leg (DS ping 191048Z) — PASSED
Healed artifact pulled independently: account_count 7925, total_aum 1,694,070,546.01, mean
213,762.84, median 73,299.37, meta.cottonwood_fold (295) — all DS-bound predictions EXACT.
Fixture render: bell renders (histogram sums 7,925), median chip $73.3K exact, unfunded-49
footer exact. "Total Holdings 8,108" GROUNDED as correct: the Andrew-ruled sleeve-level
headline (7,925 + 183 blend rows), formula in-code at ModelPortfolios.tsx:1154. Reported to DS
210525Z — closes the heal ledger's last open verification leg; noted their producer-side
sleeve_level_count retirement path is now unblocked.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Traced the artifact BEFORE FE mappings on the scatter report | The benchmarks lesson same-day: missing models = producer drop until proven otherwise |
| Display map at render boundary, not re-keyed canonical targets | CTO scope said keys NOT re-keyed; identity strings double as data-match keys — re-keying cascades |
| Deleted local MODEL_NAMES tables instead of re-valuing them | One-mapping law executed, not just honored (CTO ratified this shape) |
| 8,108 vs 7,925 investigated to mechanism before reporting | A discrepancy report OR a pass without grounding would both have been wrong; it is the ruled sleeve-level grain |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| portal: lib/modelPortfolioColors.ts + ModelPortfolios.tsx + ReturnVolatilityScatter + BenchmarkHeatmap + 3 Rolling/Drawdown charts | typing canon (see commit message) | Yes — portal DEV `02b7f351` |
| org/.../deliverables/ANDREW_DIRECT_20260804_20xxZ_LTULT_ROLLOUT_TO_020DE...md | verbatim record + measured states | Yes — `fe42f2e6bc` |

---

## Blockers

None.

---

## Current State

- PROD = portal v2.1.157 @6398630a (the 45e5843f slate). Typing canon (02b7f351) + 0.2.0_DE's
  Pod2 half (604101df) are DEV-only — **promote bar: CTO says it waits on Pod2's confirm; Pod2
  landed 604101df ~2127Z, so the joint promote is ready on Andrew's word.**
- Benchmarks thread CLOSED (Phase-3 verified on real artifacts). Acct-dist render leg CLOSED
  (DS holds the ledger pen with my evidence). CI-R6R closed-superseded (COO morning
  bookkeeping).
- LT/ULT on Positioning/Attribution/FactorTilts: 0.2.0_DE executing FE half (their lane);
  0.2.0_DS holds the 3 producer lambdas morning-wave (attribution silent-drop is the priority).
- Watcher: Monitor task b8d5qeawq live. Registered PID 20548.
- Screenshots: portal/.frontend-dev/screenshots/{benchmark-tab-live-artifact, benchmark-tab-
  display-typing, acctdist-heal-render}.png. Fixtures: portal/.frontend-dev/testing/.
- Stray junk noted, not mine, unhandled: portal/portal/ dir (org/, public/) in the portal
  working tree.

## Next Steps

- [Andrew] word on cutting the joint typing-canon promote (02b7f351 + 604101df) — then
  [0.2.0_DT_PortfolioAnalytics] or the seat Andrew names runs /prod-deploy.
- [0.2.0_DS_PortfolioAnalytics] tomorrow's scheduled 6b = acct-dist production-evidence leg;
  their sleeve_level_count producer field retires the ModelPortfolios.tsx:1154 interim reduce.
- [0.2.0_DE_PortfolioAnalytics] Pod2/LT-ULT continues in their lane; I answer questions on the
  recipe/helper as they come.

— 0.4.0_DE_ClientPlatform
