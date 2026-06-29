# Session Log — 0.4.0_DS_ClientPlatform~B — Schwab-SSOT lane (DERISK-2 census + TO-3 G11-G13)

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE (census), IMPLEMENT (G11-G13), VALIDATE
**serial:** 0.4.0_DS_ClientPlatform~B (2nd DS lane) · **date:** 2026-06-29 · **window:** session start -> 1512Z (first log of session)

## Summary

Spawned as the parallel DS lane for the Andrew-top-priority Schwab-SSOT migration. COO confirmed two slices; both COMPLETE:
1. **DERISK-2** non-Schwab/held-away account census (read-only) — commit `31bcb017b`, ACCEPTED by COO + CTO.
2. **DATA_SSOTMG TO-3** — canonical gold G11-G13 thin BD-bridged advisor surfaces — commit `d81ea44a0`.

## Slice 1 — DERISK-2 census (DIAGNOSE)

Bounded the residual BD bridge for the cutover. Method (read-only, live S3):
- Non-Schwab universe = BD accounts not in `gold/dimensions/schwab_bd_account_mapping` -> **998 accts / $253.2M** (06-24; matches prior chunk-2 $244M). 06-26+ BD silver is frozen/empty (PRD §5).
- Cohort split via `rep_code` custodian-inference (no explicit custodian field exists; `8242234` = Schwab master): **FULLY-NON-SCHWAB 513/$166.3M** (vs Andrew ~$156M est, +6.6% — the irreducible BD/Fidelity bridge); **HELD-AWAY-IN-SCHWAB 485/$86.9M** narrow .. **$124.9M** broad (mapped-but-no-RPS-position = 450/$38.0M) — Andrew's ~$109M sits between.
- Last-txn-activity via quarterly-spaced scan of 32 of 1818 daily txn partitions (90d windows @ 75d stride, no gaps), 2020->06-24. LIVE(txn<=365d) $154M/61% vs no-txn $99M/39%.
- **Load-bearing finding (corrects PRD §10):** "no BD txn" for non-Schwab custody is a FEED-COVERAGE artifact (BD never receives held-away/other-custodian txns), NOT economic dormancy. Bridge does NOT shrink to ~nothing; size D5 Fidelity vs full ~$166M. COO surfacing to Andrew's queue; the §10 correction was named the load-bearing finding in the accept.
- Explore subagent confirmed the $156/$109 are Andrew's working estimates (no prior method) -> DERISK-2 defined the split.

## Slice 2 — TO-3 G11-G13 canonical gold (IMPLEMENT)

Built on existing canonical dims (dim_advisor_role/dim_advisor_fee = thin BD bridge) + Schwab-native facts. Materialized `canonical/schwab/gold/{table}/date=2026-06-24/` AES256, parallel/NOT-served; verified by independent S3 read.
- **G11 advisor_attribution** — account->advisor attribution, 5,894 accts/$1.591B (ties canonical_holdings), 100% rel-join. BD architect/manager/money_manager bd-flagged (advisor_source_as_of=2026-04-21).
- **G12 advisor_fee_efficiency** — 55 architects, effective_fee_bps 64-125 (sane); trade-cost from Schwab TCF fact_billing. Fee-rate coverage 8.3% firm AUA (187 accts — xref-bridge gap, surfaced via fee_coverage_aua_pct, not extrapolated).
- **G13 partner_analytics** — ranked leaderboard, 55 partners; sharp-check PASS = G13 AUA ties G11 AUA exactly (clean roll); AUA-wtd return per architect from G4.
- AC#2: every BD-sourced field carries the bd-source flag + source_as_of. NOT daily-wired (PRD D4 open).
- **GAP flagged:** dim_advisor_role lean (architect/manager/money_manager) — implementor/consultant/local_ops/split-% are in BD silver/allocations, not the canonical dim -> follow-on silver enrichment (base-DS lane). Recorded in 08_GOLD_SCOPE.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-which | "which BD tables carry custodian/AUA/last-activity" | PARTIAL | routed to comp-freshness (not the schema-content match); pivoted to pipescript |
| pipescript | `--list`, `advi-bd` | PASS | mapped the BD served estate + artifacts (allocations/transactions/mapping/RPS) |
| comp-grep | docs custodian/156/109/held-away | PASS | located canonical doc (DATA_SSOTMG_PRD) + 49F_RECONCILIATION custodian-inference grounding |
| comp-pipescript io | `build_gold_advisor_attribution` | N/A (expected) | NOT-FOUND — canonical tree not graph-indexed (documented PRD §5 coverage gap); mandate attempted |
| ds-commit-gate | 3 G11-G13 scripts | PASS | py_compile + AST + ruff clean |

- **What worked:** pipescript/comp-grep nailed the estate + the canonical-doc trace fast.
- **What failed:** comp-which mis-routed the schema-content question to comp-freshness.
- **Gap found:** canonical/schwab tree is uncovered by comp-pipescript/comp graph (already a known NFRA item, PRD §5/§57) — re-confirmed.

## Briefs / artifacts written

| Artifact | Path | Note |
|---|---|---|
| DERISK-2 census brief | docs/briefs/DATA_SSOTMG_DERISK2_nonschwab_census.md | the analysis + reconciliation |
| Account-level CSVs (3) | docs/briefs/derisk2_census/ | both cohorts + all (998 rows) |
| G11/G12/G13 builders | data/canonical/schwab/gold/build_gold_{advisor_attribution,advisor_fee_efficiency,partner_analytics}.py | new |

## MCP traffic

~6 messages. Significant: COO slice-GO (both slices); DERISK-2 RAVC -> COO + CC CTO -> both ACCEPTED; TO-3 RAVC -> COO + CC CTO (open). Watcher Monitor armed (task bpzzfyf8t).

## Blockers

None.

## Current State

Both Schwab-SSOT lane-~B slices COMPLETE + RAVC'd. DERISK-2: brief + 3 CSVs committed `31bcb017b`, TO complete `7064d18de`, ACCEPTED COO+CTO. TO-3: 3 gold builders committed `d81ea44a0`, TO complete `fe3c2ef04`; G11(5894 accts/$1.591B)/G12(55 architects)/G13(55 partners) materialized at `s3://opal-data-bd/canonical/schwab/gold/{advisor_attribution,advisor_fee_efficiency,partner_analytics}/date=2026-06-24/`. All pushed to CLOUD. Registered LIVE, summary IDLE.

## Next Steps

- **[2.0.0_SA_COO]** next dispatch; DERISK-2 §10 correction is in Andrew's queue for the D5 Fidelity-scope decision.
- **[0.4.0_DS_ClientPlatform]** (base) owns build_canonical_daily.py — G11-G13 daily-wiring is a follow-on once PRD D4 (advisor-tether cadence) is decided; coordinate then.
- **[0.4.0_DS_ClientPlatform]** (base, silver lane) follow-on: enrich dim_advisor_role with implementor/consultant/local_ops + split-% from BD silver/allocations (G11 currently architect/manager only).
- **[1.0.0_SA_CTO]** PRD inputs delivered (census bounds + G1-G13 complete); fee-coverage 8.3% + implementor-dim gaps noted for the PRD.
