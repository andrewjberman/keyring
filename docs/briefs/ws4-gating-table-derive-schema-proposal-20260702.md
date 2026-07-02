# WS-4 gating_table DERIVE-schema proposal — replace hand-set frontier_page magic-numbers with grounded, derived values

**Author:** 0.4.0_DS_ClientPlatform~C (cot lane) · **Date:** 2026-07-02 · **Origin:** ADVI_COTETL WS-2b fast-follow (COO /drive redirect 230633Z; DE flagged the derive as the durable supersede)
**Pairs:** 0.4.0_DE_ClientPlatform (WS-4 served config + comp-freshness resolver), 0.5.0 (MDPF aggregate gating), 0.x_DS~B (bd/inf per-table cadences). RAVC: COO+CTO.

## Problem
The per-surface freshness PAGE thresholds are HAND-SET magic numbers, one per served entry across 4 firm configs:
- bd (`data/black_diamond/.../gold_freshness_config.yaml`): frontier_page_trading_days = **2** ("bd T-1 cadence +1, DS~B-grounded")
- inf (`data/inf/.../gold_freshness_config.yaml`): **2** ("Orion T-1 cadence +1")
- cot (`data/cot/.../gold_freshness_config.yaml`): **3** ("holdings T+2 cadence +1, WS-2b-grounded, PROVISIONAL")
- mdpf (`data/served_freshness_config.yaml:33`): **2** provisional ("aggregate-of-partners; gated by slowest partner surface -- **DS~C per-table cadence refine pending; may raise to 3**")

Two problems: (1) the numbers carry no machine-readable grounding -- the WHY lives in a comment; (2) a cadence change (e.g. cot holdings tightening to T+1 on the re-confirm) means hand-editing every gated surface, with drift risk vs the AE alarm.

## The finding (grounded, this is the key)
**Every hand-set value is already `gating_cadence + 1`** -- the rule is IMPLICIT in the comments:
| firm | gating feed | normal cadence (td behind frontier) | page = cadence+1 | grounded? |
|---|---|---|---|---|
| bd  | holdings/served (T-1) | 1 | 2 | YES (DS~B) |
| inf | Orion (T-1)           | 1 | 2 | YES (DS~B) |
| cot | holdings (T+2 vendor snapshot) | 2 | 3 | YES (DS~C, WS-2b; PROVISIONAL) |
| mdpf | slowest partner surface | ? | 2 (prov, may be 3) | **NO -- ungrounded, assigned to DS~C** |
So the derive-schema doesn't invent a rule -- it makes the EXISTING `page = cadence+1` rule explicit and removes the magic numbers. It also surfaces that mdpf's cadence is the one un-grounded value (the ":33 DS~C refine").

## Proposed schema
### (A) Per-firm, per-table cadence registry (the ONE grounded source)
```yaml
# one block per firm config (or a shared data/table_cadence.yaml)
table_cadence:
  cot:
    transactions: 0     # lands T-0
    realized: 0
    allocations: 0      # point-in-time; when present
    unrealized: 0
    holdings: 2         # T+2 vendor snapshot -- GROUNDED WS-2b (07-02->06-30, 07-01->06-29, 06-30->06-26); PROVISIONAL re-confirm-after-5
  bd:  { holdings: 1, transactions: 0, ... }   # T-1, DS~B-grounded
  inf: { orion: 1, ... }                        # T-1
```
### (B) Per served-surface: declare the gating table(s), drop the magic number
```yaml
- artifact_id: cot_platinum_timeseries_overview
  gating_tables: [holdings]        # snapshot-first -> holdings gates the AUA frontier
  # frontier_warn_trading_days: DERIVED   (report-tier; see WARN note)
  # frontier_page_trading_days: DERIVED = max(table_cadence[firm][gt] for gt in gating_tables) + 1
```
### (C) Resolver (comp-freshness / the config loader, at load-time)
```
page = max(table_cadence[firm][t] for t in gating_tables) + 1
```
- **WARN tier:** currently a FLAT 2 across all firms (a report-tier "2td-behind is worth noting" convention, NOT cadence-derived -- cot warn=2=cadence, bd/inf warn=2=cadence+1). Design choice for DE: keep WARN flat-2 (report convention) OR also derive it (= cadence, warn-at-floor). Recommend keep flat-2 for now (report-only, no page harm) and revisit.
- **Override escape hatch:** an explicit `frontier_page_trading_days: N` still wins over the derive -- for a PROVISIONAL/manual value pending cadence-grounding (e.g. cot=3 until the re-confirm, mdpf until my refine). Derived-by-default, override-when-needed.

## MDPF (aggregate-of-partners) -- the DS~C refine assigned at served_freshness_config.yaml:33
MDPF's served surfaces aggregate N partner surfaces, so mdpf's gating cadence = **max over its contributing partner surfaces' OWN gating cadences** (the slowest partner gates the aggregate). Concretely: if MDPF aggregates cot (holdings T+2) + others (T-1), the aggregate is gated at T+2 -> page=3, NOT the current provisional 2. This is exactly 0.5.0's MDPF-derive increment; I bring the grounded cot/bd/inf per-table cadences as the calibration set + ground the mdpf partner set.

## Migration (coordinated, no big-bang)
1. Seed `table_cadence` per firm (cot grounded now; bd/inf DS~B-grounded; mdpf = DS~C refine).
2. Add `gating_tables` to each served entry.
3. DE extends comp-freshness/loader to DERIVE frontier_page (+ optionally frontier_warn); explicit values become overrides.
4. Remove the hand-set frontier_page where a grounded cadence exists (keep override only where provisional).
5. AE alarm reads the DERIVED frontier_page (the existing one-source drift-guard, now grounded).

## Status of the grounding (update 2026-07-02, e513cdde4)
- **mdpf cadence -- GROUNDED + LANDED (was the open ":33 refine").** schwab_custody=2 (the slowest feeder), from BD_MAX_LAG_TRADING_DAYS=2 SOURCE-CONFIRMED (mdpf-daily-trigger lambda:69 + mdpf-pipeline/lambdas.tf:35; 0.5.0_AE_OpalETL pairing + DS~C verify). => mdpf frontier_page 2->3 folded into served config. table_cadence.yaml seeded (all 4 firms). DE building resolve_page_threshold().
- **cot holdings=2** -- PROVISIONAL, re-confirm-after-5-clean-nightlies (post-06-22-AUAFIX baseline thin). Override held until lock.
- **STILL OPEN:** bd/inf cadences are DS~B-grounded (recorded in table_cadence.yaml as cited) -- confirm the basis is a real cadence-confirm (like WS-2b), not an assumed T-1 (route to DS~B). Add gating_tables to the bd/inf served entries (DS~B lane). DE's resolve_page_threshold() (lib/served_vintage.py) is the remaining build.

## Ownership
DS~C leads the schema + the cot & mdpf cadence grounding. DE owns the comp-freshness/served-config resolver + folds into the MDPF-derive increment. 0.5.0 owns MDPF aggregate gating. AE consumes the derived frontier_page. RAVC COO+CTO.
