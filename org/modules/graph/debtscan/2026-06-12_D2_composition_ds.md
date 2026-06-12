# NFRA_DEBTSCAN TO-D2 — DS lane composition battery (pipescript / cache / postdeps)

**Lane:** DS (0.4.0_DS_ClientPlatform) | **Companion lane:** AE (0.7.0_AE_CloudOps, comp-iam — files `_D2_composition_ae.md`)
**Run:** 2026-06-12 ~18:33–18:46Z | **Posture:** READ-ONLY (zero mutations; Rule 13 untouched)
**Binding doctrine:** freshness-bound; CVO ≥0.8 precision gate before promoting above ADVISORY.

## Provenance / freshness header
| Pipeline | Freshness source | Result | Filing class |
|---|---|---|---|
| bd-gold (67) | `comp-pipescript deployed` | **43/43 MATCH** (A_00 transient-TIMEOUT → retried MATCH) | FRESH → fileable |
| bd-silver (incl. compact-realized) | `comp-pipescript deployed` | MATCH | FRESH |
| inf-gold (50) | (none — see Finding D2-DS-01) | **UNKNOWN-VINTAGE** | ADVISORY (caveated) |
| cot-gold (43) | (none — see Finding D2-DS-01) | **UNKNOWN-VINTAGE** | ADVISORY (caveated) |

`comp-pipescript deployed` enumerates bd-rooted scripts only; it cannot confirm inf/cot/mdpf S3 vintage. Per CVO guidance (184549Z, via Andrew): file inf/cot caveated — "a caveated finding beats a held sweep; the caveat class auto-clears when the tool extends."

## Findings ledger  {family, tool, script, finding, verdict, owner-lane}

### Family: comp-pipescript io — COLUMN GAPS ($0-metric class; geo_drill / fee_earning_aua pattern)
| Tool | Scope | Scripts | Finding | Verdict | Owner |
|---|---|---|---|---|---|
| comp-pipescript io | bd-gold | 67 | 0 column gaps | CLEAN | — |
| comp-pipescript io | inf-gold | 50 | 0 column gaps | CLEAN (UNKNOWN-VINTAGE) | — |
| comp-pipescript io | cot-gold | 43 | 0 column gaps | CLEAN (UNKNOWN-VINTAGE) | — |

Estate-wide: **0 column gaps / 160 gold scripts.** Detector scope-bound: fires only on `_load_parquet(KEY, columns=[explicit list])` sites; dynamic column lists (`columns=SOME_VAR`) are not analyzed (tool limitation, not a clean-claim on those sites).

### Family: comp-cache collisions (cache-corruption class: same key, DIFFERENT response type)
5 shared keys surfaced; the bug class is same-key-**different-type**. All 5 are same-fetcher-**same-type** → intentional shared cache, NOT corruption. **5/5 verified-FP (suppressed with reason):**
| Cache key | Components | Fetcher / type | Verdict |
|---|---|---|---|
| advisor-book-view/advisorId/firmOverride | AdvisorBookView, AdvisorPublicProfile | getPlatinumAdvisorSummary → PlatinumAdvisorSummary | FP (same type) |
| advisor-intelligence/advisor-nna-canonical/firmOverride | AdvisorPublicProfile, AdvisorAnalytics, DistributionTab | getAdvisorNnaCanonical → AdvisorNnaCanonicalResponse | FP (same type) |
| advisor-intelligence/timeseries-overview/firmOverride | PartnerAnalytics, DistributionTab | getTimeseriesOverview → TimeseriesOverviewResponse | FP (same type) |
| firm-leaderboard/firmOverride | index×3, AdvisorsTab, ClientsTab | getFirmLeaderboard → PlatinumLeaderboardResponse | FP (same type) |
| partner-analytics/granularity/firmOverride | PartnerAnalytics, DistributionTab | getPlatinumPartnerAnalytics | FP (same fetcher) |

Real cache-corruption findings: **0.**

### Family: comp-pipescript postdeps (missing post-step class: $22M phantom-override pattern)
5 post-dep guards configured + present (`gold_pipeline_deps.yaml`):
- `build_canonical_prices_v2.py → inject_scoped_overrides.py` [BLOCKING] — **the $22M BNP-override class: PROTECTED.**
- `B_03.account_gains.py → C_00.canonical_performance.py` [BLOCKING] (AUAGAP.002).
- Preconditions: `B_00.hybrid_price_fill` needs canonical_prices.parquet (+coverage>80 WARN); `D_00b`/`D_01` need dim_advisor_office.csv on S3.

Missing-config gaps: **0** (the tool's static view; a producer/consumer cross-ref for *un*configured post-deps is out of this tool's scope — noted as a deeper-analysis candidate).

### REAL FINDING (CVO-verified)
**D2-DS-01 [tooling-debt / freshness-binding gap] — `comp-pipescript deployed` is bd-only.**
inf/cot/mdpf gold scripts have **no freshness-verification path** → every non-bd gold sweep is structurally UNKNOWN-VINTAGE, so the freshness binding cannot be satisfied for those legs. CVO-acknowledged (184549Z); fix routed to CTO as Andrew-direct: the deployed engine already carries inf/mdpf/cot bucket overrides (`pipeline_cli.py:1450-1466`) — the gap is bd-rooted script *enumeration*, so the fix is `--firm` scoping / PIPELINE_MAP auto-detect, not bucket plumbing. **Verdict: REAL.** Owner: CTO (tool) / AE-or-CTO (impl). Caveat class auto-clears when the tool extends.

## Precision sample (CVO gate)
| Candidate set | Surfaced | Verified-REAL | Verified-FP (suppressed) | Promoted |
|---|---|---|---|---|
| comp-cache collisions | 5 | 0 | 5 (same-fetcher-same-type) | 0 |
| comp-pipescript io column gaps | 0 | 0 | 0 | 0 |
| postdeps missing-config | 0 | 0 | 0 | 0 |
| tooling-debt (freshness binding) | 1 | 1 | 0 | 1 |
| **Total** | **6** | **1** | **5** | **1** |

**Promoted-set precision = 1/1 = 1.00** (≥0.80 gate PASS). **Suppression accuracy = 5/5** (every FP correctly filtered; 0 false promotions). 

## Verdict
Estate composition-debt for the DS families (column gaps / cache corruption / missing post-steps) is **CLEAN** — 0 real bugs of those classes across 160 gold scripts + the portal cache graph. The one REAL finding is tooling-debt (D2-DS-01, freshness-binding coverage gap), already routed to CTO. Filing class: bd legs gate-passed; inf/cot legs ADVISORY/UNKNOWN-VINTAGE pending the `--firm` tool extension.
