# 1.0.0_SA_CTO — Session 32 Startup Log
**Date:** 2026-04-17 (Eastern)
**Context carryover:** Post-compaction resume of session 31. Full Run-10/11 bond-100x recovery + tiered cap ship + C_08 silent-wrongness saga.

---

## Scope resolved this session

### 1. Cap timing-rule brief review (DS ~ABC)

Reviewed `docs/briefs/ds-brief-b01-cap-timing-rule.md`. DS proposed two layers on top of the tiered B+C cap:
- 5-day introduction ramp (20% -> 100% of target compression over first 5 trading days)
- 3-of-4 persistence gate (cap fires only if account overshot >=5% on 3 of last 4 snapshot dates)

**Call (Andrew + CTO):**
- **KEEP** from the brief: `market_value_uncapped` column (AC #1) + per-account cap log line. Both ship in cap patch. Audit trail + downstream choice.
- **DROP** ramp: publishes deliberately wrong values for 5 days to smooth a one-time chart event. Ship-day step handled via release-note callout in REGISTRY + session log.
- **DROP** persistence gate: chronic overshoot cohort passes 4-of-4 immediately (no value-add for the cohort that matters today); adds 3-day latency for hypothetical future case; fallback `do not fire` on missing parquet is fragile in the cap's first week.
- Andrew correction: CTO idempotency concern was wrong. Tables rebuild from scratch daily with dated S3 keys; reading prior parquets is static lookup, no coupling. Withdrawn.

**Dispatched to DS:** MCP 20260417T174410Z.

### 2. Bond-100x cap ship (cd177553 upstream)

Prior session already landed the bond convention fix (d45fc0dc) — `cost_per_unit <= 2.0` -> bond mask -> `closing_price / 100`. Run 11 confirmed $3.587B -> $1.758B collapse, 916 bond lots repriced correctly. This session shipped the tiered cap on top (cb6d78e2 landed in prior session).

**Artifact evidence (DS manual sanity check, 2026-04-15 B_01):**
- 1,011,807 rows / 10,532 accounts / 3,984 tickers / 37.4 MB
- `market_value_uncapped` column shipped (cap AC #1 in place)
- Cap compression $120.5M, matches ~ABC sim within $1M ($121.2M simulated)
- Post-cap firm total **$1,646.4M** vs silver canonical $1,694.6M -> **-2.9% residual undershoot**, within expected band
- CUSIP non-null 98.3% -> CP-DS1 XYZ key fix holding
- cost_basis non-zero **31.74%** -> confirms Andrew's "Opal models only" whitelist pivot for Top Positions panel (coverage-based approach would have been thin)

### 3. Full chain HALT at C_08 + silent-wrongness recovery

AE fired full chain (mode=full) per Andrew direct ask at 19:12:55Z. B_01 SAFETY HALT cleared (CP-DS1 1db831aa fix held, 544.7s). **C_08 crashed at 19:52:18Z** with KeyError `['aua_current', 'growth'] not in index`.

**DS quick patch 9e537f9f (deployed MATCH):** added both cols to C_08 L644 defensive backfill -> default 0.0 if absent. Unblocks the chain.

**CTO flag — silent-wrongness class, same as bond 100x:**
- Pulled both parquets from S3 and diffed columns.
- `gold/canonical/nna_atomic/2026-04-15.parquet` (C_08 reads this — `CANONICAL_NNA_ATOMIC_PREFIX`): 22 cols, **NO aua_current, NO growth**.
- `gold/canonical/nna/2026-04-15.parquet` (C_01 output — `CANONICAL_NNA_PREFIX`): 14 cols, **HAS aua_current + growth + aua_residual + nna_clean + client_state**.
- DS fix masks real schema mismatch. Zero-fill would complete the chain but zero out `total_aua`, `growth_daily`, `implied_daily_fee` across every advisor in D_04 client_portal_summary.json + advisor_fee_efficiency.json. Crash would have been safer.

**Real fix dispatched:** prefix swap on C_08 + audit of all 7 downstream `CANONICAL_NNA_ATOMIC_PREFIX` consumers (D_00, D_00b, D_00c, D_01, D_02, D_04) -> decide atomic vs canonical per script.

### 4. DS decision matrix (commit cd177553)

| Script | NNA cols read | Decision |
|--------|---------------|----------|
| C_08   | aua_current, growth (L760 hard-select) | **SWAP** |
| D_00   | none — dead import L42; growth/aua_residual come from ACCOUNT_PERFORMANCE | **NO-OP** |
| D_00b  | aua_current + client_state (L407-408) | **SWAP** |
| D_00c  | date, account_id, flows only (L128) — atomic ok | **KEEP** |
| D_01   | aua_current + client_state (L426-427) | **SWAP** |
| D_02   | date, account_id, flows only (L1632) — atomic ok | **KEEP** |
| D_04   | client_state + architect (L1620-1621); atomic has 'state' not 'client_state' -> silent 'Unknown' | **SWAP** |

**Bonus D_04 catch:** second silent-wrongness mode. Before the swap, D_04 was setting `client_state='Unknown'` for every row because atomic has `state` (not `client_state`) and D_04's defensive fallback wrote 'Unknown' when missing. Same failure class as the C_08 zero-fill, masking a different column. Schema-alignment TO (BDPL_NNA.S1) drafted to fix the `state` vs `client_state` naming delta at the schema source.

**cd177553 state:**
- Parent: 9e537f9f | SHA: cd177553 | Push: origin/CLOUD up-to-date
- Diff: +8/-9 lines, 4 files (C_08 + D_00b + D_01 + D_04)
- S3: all 4 scripts uploaded, comp-pipescript deployed 42/42 MATCH
- Defensive backfills retained as insurance (belt-and-suspenders — future schema regression surfaces as WARN, not silent zero)
- C_08 cleanup: dropped unused `canonical_nna_atomic_key` import (L62)

### 5. C_08 -> D_04 re-run fired (SSM d83a1d11)

**Andrew's call:** run C_08 -> D_04 only (A-C artifacts fresh from 19:12Z halted run). QA vs PROD runner equivalent — same scripts.

**AE dispatch choice (smart):** `--single C_08 --no-shutdown` then `--group D --no-shutdown` on bd-gold-qa-runner (i-0090b823a4a0997e3). Rejected `--chain downstream` because it would have re-run C_03/C_05/C_06/C_07 wastefully. `--no-shutdown` on both so QA runner stays up mid-sequence.

- SSM: `d83a1d11-66d7-4bf4-93a7-6fc2fced3461`
- Timeout 3600s, CloudWatch enabled
- Standing by for PERF timeline + D_04 non-zero spot-checks + client_state!='Unknown' verification

### 6. Compiler gap flagged

`comp-validate B_01 --artifact ...` returned exit 0 **but with SKIP** — there is no B_01 config block in `gold_validate_config.yaml`. Validator has been green-by-default for B_01 this whole time. That's a compiler-side gap that hid real signal. DS caught and reported honestly instead of declaring "exit 0 = pass."

**Post-ship TO:** add B_01 config block (required cols, cap-compression bounds, firm MV bounds vs silver canonical, CUSIP non-null threshold). Not blocking current ship.

---

## Key theme: silent-wrongness class

Three incidents in this saga, all same failure mode:

1. **Bond 100x** (Run 10, 53be25d1): RPS closing_price applied directly to bond lots without percent-of-par convention -> $1.83B phantom inflation on 272 lots. Crash-level wrong, but completed quietly. Caught only because firm total visibly blew up.
2. **C_08 zero-fill (9e537f9f):** `aua_current=0.0` / `growth=0.0` defaulted over missing canonical fields -> silently zero advisor fees + growth in D_04.
3. **D_04 client_state 'Unknown':** defensive fallback over missing column (atomic has `state`, not `client_state`) -> every row silently rendering 'Unknown' for state.

Pattern: defensive defaults over missing/misnamed fields mask real data issues. **Crash is safer than zero-fill or label-fill.** Follow-ups:
- Schema-alignment TO (BDPL_NNA.S1) on state vs client_state.
- comp-validate config add for B_01.
- Consider adopting a "WARN-and-halt-if-over-N%-of-rows-default-filled" convention in future defensive backfills.

---

## Still pending (not in scope for tonight)

- **FIFO over-closure 51-account undershoot trace** (~XYZ work — CP-DS1 cusip-keyed merge over-matching vs double-counted bronze sells vs stale `_all_closed` flag). Runs in parallel with tonight's ship.
- **Linear interpolation drift** — RPS dead since 2026-04-08. ~ABC proposed tactical cap (now shipped as tiered cap cd177553 predecessor). Root-cause fix = restore fresh RPS data feed. Not tonight.
- **Asset_class join (Option c)** as hardening TO post-ship — replaces `cost_per_unit <= 2.0` heuristic for bond detection with explicit asset_class from silver/assets.
- **Top Positions "Opal models only" filter** — pivot confirmed by 31.74% cost_basis coverage figure. Separate TO.

---

## Directives I'm carrying forward

- COO GO is not autonomous-execution-authorization when Andrew is absent from chat — AE held correctly on `feedback_andrew_overrides_exec_directives`.
- Defensive defaults over missing fields are silent-wrongness traps — flag and fix the schema, don't absorb.
- QA vs PROD runner is operational, not safety — same scripts run on both.
- DS owns full deploy cycle (commit + push + S3 sync + MATCH check). CTO dispatches; COO coordinates; AE executes dispatch.
- No B_01 re-validates without a real signal question — compiler validator is SKIP-by-default for that script.

---

## Waiting on

- AE SSM d83a1d11 completion report: PERF timeline, D_04 advisor spot-check, advisor_fee_efficiency totals, validator exits, log path.
- DS ABC+XYZ validation battery on C_08 -> D_04 artifacts when landed.
- DS BDPL_NNA.S1 schema-alignment TO draft (for PRD review).
