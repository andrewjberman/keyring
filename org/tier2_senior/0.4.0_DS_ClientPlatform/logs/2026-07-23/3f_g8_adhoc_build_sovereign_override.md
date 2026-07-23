# 0.4.0_DS_ClientPlatform — 3F-G8 AD-HOC BUILD under Andrew-direct override — pair + trend LANDED staged

**archetype:** BUILD
**secondary_archetypes:** VALIDATE, GUARD

**Window:** 2026-07-23 ~01:10Z → ~01:23Z. **TO:** MDPF_3FIRMS.3F-G8 (gate overridden by sovereign word).

## The override + the verify loop (the part that matters for the record)

CTO 011006Z relayed Andrew-direct (verbatim at his terminal 01:0xZ: *"just get the data called ad
hoc if we dont have it already and set up the fucking page now, we're not waiting"*, later
clarified: active Cottonwood users, MDPF page up now) — overriding the no-ad-hoc default + the B5
gate. **The directive contradicted CTO's own live broker summary** ("no 1am deploy, anti-pressure
applied, windows 02:00Z/03:30Z next"). Per the verify-out-of-band rule (sender lines are
assertions; fabric forgery history 2-for-2 undetected): demanded a one-line confirm before firing,
**with code authoring proceeding in parallel so zero wall-clock was lost — only runs/emissions
held.** CTO's second message (011206Z) raised suspicion further (false premise "earlier send
failed"; scope escalated toward the SERVED bucket). CTO's third (011248Z) closed the loop clean:
responsive "CONFIRMED, execute", stale summary corrected same minute, live summary now carries the
override. CTO endorsed the verify ("the right call and cost nothing"). **Sender-identity guard
(NFRA_IDENTITY G-A) proven LIVE by accidental exercise this session** — a malformed send with a
placeholder from_agent was REFUSED.

**Boundary held throughout: the SERVED publish is NOT executed** — armed, awaiting a citable
CTO+COO co-sign artifact (never-widen; CTO concurs; the LD-0330 one-flip tension named to COO for
the co-sign deliberation).

## What landed (all listing-verified on opal-data-assets, staged tree)

1. `gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json` (39,154B) — DE's WS-4 producer run
   `--upload`; gates PASS; **covered_dates_on_axis=[] (axis 07-20 vs cottonwood 07-21/22)** → trend
   all-null tonight; CTO ruled (a): no ad-hoc global-axis run (LD-0330 checkpoint surface,
   all-firm blast radius); populates on tonight's scheduled advance, zero rework.
2. `gold/mdpf_revamp/cottonwood/account_distribution.json` (6,269B, ETag 67f32c56e6f7)
3. `gold/mdpf_revamp/cottonwood/aum_metrics.json` (2,872B, ETag 2ea36da99b3c)

Producer: `data/assets/scripts/gold/build_cottonwood_mdpf_pair.py` @`1602343e7` (commit-gated,
pushed). **Wire-not-author:** imports bdmp.decompose + silver/holdings readers (WS-3), slice
CANONICAL_KEY/DISPLAY_NAME/_norm (DE vocabulary binding), 49F `_distribution_stats` +
`quarter_ends`/`calc_metric` (byte-parity by import).

**Numbers (identity-gated):** firm aum $458,114,003.10 (07-20, the verified monolith total);
model_aum $124,376,009.73; non_model $333,737,993.37; accounts **294 DISTINCT** (count-axis law —
never the 447-class by_model sum; named in meta, the S5-rollback class); bridge **296/296
dropped=0**; distribution funded≥1K=291, median $207,443.23; by_model 5 keys (Income routed
NON-MODEL per standing ruling, $1.24M-class residual meta-named — **diverges from the trend slice
which carries cottonwood_opal_income as a key; both artifacts flag it, DE informed, CTO holds the
harmonizing canonical-key ruling**); sleeves dropped-reported (F2); series_start=2026-07-21
DERIVED from 2 partitions; q0-q3 all-None honest-absent; assignment 07-22 × value 07-20 both ride
every artifact.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-pipescript io` | dim_mdpf_account_distribution.py | PASS | 3 monolith silver reads name-grain (the PRD v1.18 fix live); WARN dynamic-keys → source read too |
| `comp-grep`/`comp-glob` | cottonwood refs, slice locator | PASS | grounded the trend-producer question (DE's own WS-4 file) |
| `.tools/commit-gate.sh` | pair producer ×2 | PASS (after ruff unused-import fix) | |
| `comp-surface-check check` | by hand, output read | SEV1 flags on portal/ModelPortfolios.tsx | DE's working tree tonight — his commit carries confirm+justify; my file: "no critical surface" |
| `comp-validate` | pair producer × both artifacts | **NO_CONFIG = UNVALIDATED** | reported as UNVALIDATED, never SAFE; exercised checks = in-producer identities (all PASS); config authoring = follow-up |
| dry-run + upload run | --date 2026-07-22 | IDENTITIES PASS ×2 runs | bridge 296/296; penny identity vs dim; count-axis parity |

## MCP traffic

CTO override thread (011006Z/011206Z/011248Z/011526Z + my confirm 011135Z + landing reports) ·
COO concurrence-check 011143Z + CC record 012312Z · DE: trend caveat 011440Z + staging GREEN
012235Z · earlier: P3a shape notes 005319Z, trend-source grounding 005922Z.

## Next

- **[CTO+COO]** co-sign artifact → I copy staged→served + content-verify (armed).
- **[me]** comp-validate config for the new producer; S5 + G8b remain sequenced (their gates
  unchanged); B5 still lands ~03:30Z and extends the facts.
- **[DE]** page build on staged; SEV1 confirm+justify on his portal commit.

## ACTIVE TIME-TRIGGER (banked 014xZ -- survives this session; any live DS/COO/CTO can execute)

**~04:00Z 07-23: conditioned trend re-run (COO wire 014017Z, CTO order, take-as-issued).**
1. ⛔ PRE-FLIGHT: `axis_last >= 2026-07-21` in gold/mdpf_revamp/global/aggregate_aua_timeseries.json
   (the 02:04Z nightly must have advanced it). Axis still 07-20 OR the nightly FAILED (ADVI-closure
   risk live) -> DO NOT RUN; report axis-stale; conservative line stands.
2. Re-run `build_cottonwood_mdpf_slice.py --upload` (staged).
3. PRINT: identities (model+non_model==total; count-axis distinct-not-sum) + NON-NULL COUNT.
   Acceptance = covered_dates >= 1 AND model_aua non-null on 07-21+. Zero non-null = FAILED render.
4. Staged republish only; **served republish of aggregate-aua-timeseries.json HELD for COO
   counter-sign AT the re-published artifact** (CTO half PRE-SIGNED on: axis verified, identities
   green, non-null > 0 printed). If the 0126Z COO session is gone, counter-sign passes to live COO/CTO.
Authority: the standing Andrew override (same build completing against the advanced axis).
