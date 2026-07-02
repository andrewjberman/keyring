# ADVI_ETLFIX WS-4 KEYSTONE BUILD -- increment-1: bd+inf served-layer content-vintage coverage

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE

**Workspace CLOUD commit:** `023c1f9d9`
**Trigger:** COO WS-4 KEYSTONE GO (20260702T191409Z, P0 closed -> Phase-1 un-held) + CTO WS-4 arch-strengthening (20260702T192009Z, 3 folds).

## Current State

The WS-4 keystone (firm-wide content-vintage freshness oracle) is arch-gate-RULED; the KEYSTONE GO turned it into a BUILD. **Key reframe from grounding comp-freshness first: the content-vintage oracle ALREADY EXISTS** -- don't rebuild, extend coverage.

### The reframe (avoided a duplicate-tool rebuild)
`.tools/comp-freshness` (DE-editable, comp- basename) already has:
- **CONTENT-MODE** (`as_of_field`): reads the served JSON's internal `data_as_of`, demotes mtime to secondary, emits `MTIME-FRESH-BUT-CONTENT-STALE`.
- **trading-day-frontier** mode (`freshness_basis`, `lib/trading_calendar`): staleness = trading-days-behind the priced frontier -> no flat cry-wolf.
- cot already uses it firm-wide (6 content-mode / 4 frontier served entries).

### R1 audit (the gap)
| firm | content-mode entries | served platinum keys | frontier |
|---|---|---|---|
| cot | 6 | 4 | 4 (template) |
| bd | **0** | **0** | **0** |
| inf | **0** | **0** | **0** |

bd+inf ZERO served-layer content-mode coverage = the EXACT mechanism of both P0 mis-reads (bd false-GREEN mtime-07-02/content-06-29; inf prefix-mtime false-RED). MDPF sits in an orphaned mtime-only `data/served_freshness_config.yaml` (not loaded by the comp-freshness engine).

### Increment-1 SHIPPED (023c1f9d9, DE-permitted config, no engine change)
Registered `bd_platinum_dashboard` + `inf_platinum_{dashboard,header_metrics}` with `as_of_field:data_as_of` + `trading-day-frontier` (mirrors cot). **TESTED LIVE:** content-mode engages, reads served `data_as_of` (bd 07-01 = 1td behind = normal BD T+1 lag -> PASS, no cry-wolf; inf 07-02 = 0td -> PASS) -- NOT prefix-mtime. A 2+td content-freeze now WARNs -> the bd false-GREEN + inf false-RED classes are **structurally closed for the headline served surface**.

### CTO 3 strengthenings folded
1. cot = 3rd firm proof-point -- it's literally the template replicated.
2. NORMALIZER PREREQ (R1-sharpen): Orion forward-labels 07-02=real 07-01 -> the oracle must consume the DS~A+0.6.1 normalized vintage; flagged in-entry (raw label +1 lenient until normalized).
3. SILVER-DIM limb (asset-dim class): comp-freshness ALREADY checks silver dims firm-wide (WARN'd bd_assets_dim) -> the necessary-but-not-sufficient limb EXISTS; make it explicit + a 3rd adversarial AC.

## Compiler Tools
| Tool | Result | Note |
|------|--------|------|
| `comp-which` (freshness interfaces) | routed | located comp-freshness engine + configs |
| Read `.tools/comp-freshness` | grounded | found the existing content-mode + frontier oracle (the reframe) |
| `comp-glob` / `comp-grep` (R1 audit) | gap found | bd/inf=0 content-mode; cot=template; MDPF orphaned |
| owned-paths-check (config lane) | DE-permitted | bd+inf gold_freshness_config.yaml editable |
| `comp-freshness artifact` (bd+inf served) | PASS content-mode | tested: reads data_as_of + frontier, not prefix-mtime |
| safe-commit | PASS | 023c1f9d9 |

## Next Steps
- **[0.4.0_DE, me]** increment-2 (queued, DE-ownable, same pattern): full per-key served coverage per bd+inf (partner_analytics/leaderboard/cumulative_chart/timeseries).
- **[0.4.0_DE + engine decision]** MDPF: wire `served_freshness_config.yaml` into comp-freshness + content-mode (orphaned today).
- **[0.4.0_DS_ClientPlatform~A + 0.6.1_AE]** per-vendor Orion as_of-normalizer (prereq for inf/MDPF true-vintage; dispatched).
- **[AE]** the fail-LOUD outcome-keyed per-DIMENSION alarm wired off this oracle (RED escalation; CW/SNS infra lane).
- **[3.0.0_SA_CVO]** validation ACs incl the 3rd adversarial (fresh top-level + stale joined-dim must fire).
- **[1.0.0_SA_CTO]** arch-gate the firmed WS-4 TO. **[2.0.0_SA_COO]** WS-4 TO decomposition / re-sequence if desired.
