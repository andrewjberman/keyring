# 0.4.0_DS_ClientPlatform -- DATA_ANALYTICS canonize-gold (A->C) + ETFS AVGCAP correction
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE, SCRIBE, COORDINATE

## Summary

Drove the DATA_ANALYTICS canonical (Schwab-raw-native) build to a milestone: completed the SILVER
layer (14 facts + 5 dims), built + served GOLD-B `account_gains` (the AUA decomposition that
replaces the misguided 90-day flag), documented the whole architecture (8-doc suite), and executed
Andrew's A->B->C: (A) investigated the gold-B residual, (B) engaged CVO, (C) built + verified the
daily-incremental cadence. Also: owner-reviewed the 49F W2 ETF-ownership producer (PASS), and
caught + corrected an ETFS AVGCAP overstatement (inf June blend) before it served -- served clean
May + June rollups on fully-canonical inf data.

## Work done (this window = whole session)

### Silver dims completed (the 3 non-custodian dependencies)
- `dim_advisor_fee` (a897b6c0b) -- advisory-RATE dim, account_id PK, `annual_fee_bps` from the BD
  fees feed, xref-bridged (4,899 accts; 501 unbridged REPORTED not dropped). Completes the trio:
  household (`dim_relationship`) + advisor-role (`dim_advisor_role`) + fee.
- Silver layer now 14 facts + 5 dims, all materialized `opal-data-bd/canonical/schwab/silver/`.

### Gold-B `account_gains` (the AUA decomposition)
- build_gold_account_gains.py (1de75d0c0). Identity `d_aua = nna_cash + nna_in_kind + income -
  fees_tax + market_growth`, closes EXACT. Flows classified by `fact_transaction.sb` (Schwab's
  native txn-class code; FI/FO proven to sign MoneyLink both ways). NNA split cash/in-kind
  server-side. Aberration-excise via `is_aberration`. 30-day window basis.
- Served `account_gains/period=2026-05-18_2026-06-18` -- d_AUA +$31.28M (NNA +$31.2M dominates;
  49F in acquisition). Backfilled the window: fact_position 05-18/06-17 + 22 fact_transaction
  partitions.

### A -- residual investigation (00cad7ef5)
- 236 accounts flag |market_growth|>25% bmv. NOT timing lag (refuted: 5% recent). Root cause:
  account closures/full transfers-OUT generate NO TRN transaction (positions vanish from RPS),
  + model rebalancing. Built + REJECTED a position-derived transfer-out fix ($718M securities
  "disappear" between snapshots = rebalancing, doesn't reconcile -> spurious -$116M). Kept honest
  pure-residual v1 + flags; transfer-out split needs a trade/allocation feed TRN lacks.

### B -- CVO engaged
- Validation request to 3.0.0_SA_CVO: methodology + sb taxonomy + Item-A handling + co-scope the
  transfer-out reconciliation gap. Async, non-blocking.

### C -- daily-incremental cadence (fcafc5164, 4913aa6b9)
- build_canonical_daily.py -- one idempotent command rolls silver (5 facts + 5 dims) + gold
  (holdings + trailing-30d account_gains). Verified LIVE 12/12 steps OK. COO concurred Option A
  (49-schwab-conv tail); coordination sent to 0.5.0_AE post-P0. Hardened: missing periodic-form
  raw -> SKIP not ERROR.

### 49F W2 producer owner-review -- PASS
- bd-49f-etf-ownership-daily metric-correct (faithful W1 mirror); schema-safe; no shared-account
  inflation (all-ticker total $1.59B ties canonical) -> discharged the 49F half of DE's tie-out AC.

### ETFS AVGCAP (the catch + correction)
- AVGCAP _stage_ double-count allowlist (5dea9da91, COO GO). list_partner_dates strict-ingest
  (3380a45f6) -- skips a stray holdings_2026-06-24.json that crashed the rollup.
- HELD the June rollup after verifying the SERVED inf slices were a BLEND (some dates still
  old-raw ~$78-82M, 2x). Pinned the completeness-floor decision = VALUE-BASED (RAVC'd COO);
  0.5.0 implemented + re-backfilled all 41 inf slices canonical.
- Grounded the early-canonical residual: $12M is the TRUE fully-priced ramp (0 held-but-unpriced;
  only PFDE+PFOE migrated by 06-01, DIVZ+IDVZ arrive 06-08 -- the genuine Inflection->Opal
  migration, started 05-15). SERVED clean: monthly/2026-06.json (inf $38.81M) + monthly/2026-05.json
  (inf $12.46M PARTIAL).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-which | "where is the ETF ownership dashboard renderer w/ CANONICAL_PARTNERS allowlist" | PASS | routed to comp-grep (no rich tool fit); found etf_ownership_dashboard.py:70 to mirror the guard |
| ds-commit-gate.sh | every .py commit (dim_advisor_fee, gold-B, orchestrator, build_fact_schwab, avgcap) | PASS | py_compile + ds-precommit (padded-string marker honored) + ruff; 1 F401 + 1 E731-class fixed |
| safe-commit.sh (surface-check) | all commits | PASS | no critical surface touched |

**What worked:** comp-which dead-ended gracefully into comp-grep and located the renderer guard to
mirror. ds-commit-gate caught a ruff F401 (unused `date` import) in the orchestrator before commit.
**What failed:** none.
**Gap found:** none new. (Most data-build inspection was direct boto3 parquet reads = data-plane
/ no-graph-presence, off-rail per the graph-presence principle; comp-tools don't model row-level
canonical data.)

## DS Briefs / Docs Written

| Doc | Path | Purpose |
|---|---|---|
| Architecture suite (8 files) | data/canonical/schwab/docs/{README,00..07}.md | overview, silver contract, 14 facts, 5 dims, sb taxonomy keystone, NNA decomposition, diagrams, productionization (ee0521608, 00cad7ef5, fcafc5164) |

## MCP traffic

~10 messages handled. Significant: AVGCAP re-run done -> 0.5.0; CANONICAL_PARTNERS RAVC done ->
COO; gold-B VALIDATION REQUEST -> CVO (3.0.0); orchestrator scheduling RAVC -> COO (concurred
Option A); W2 owner-review PASS -> 0.5.0 (cc DE tie-out); floor decision (value-based) RAVC -> COO;
ETFS June HELD + blend evidence + CORRECTION (06-01/02 = raw not ramp) -> 0.5.0; ETFS CLEARED
(both months served) -> 0.5.0. Inbound: DE ETFS_CANON tie-out cc; COO floor-mis-fire DRIVE;
0.5.0 floor-DONE + grounded raw-vs-canonical correction.

## Blockers

None BLOCKED. Open items are async on other lanes (not blocking my work):
- 0.5.0_AE: add orchestrator tail to /49-schwab-conv (post their inf P0); clean up stray
  holdings_2026-06-24.json object (S3-delete needs human-confirm gate).
- 3.0.0_SA_CVO: validate gold-B methodology (async).

## Current State (handoff surface)

- **Silver** (opal-data-bd/canonical/schwab/silver/): 14 facts + 5 dims materialized. Builders in
  data/canonical/schwab/silver/. Universal Silver Contract v1 (docs/01).
- **Gold** (opal-data-bd/canonical/schwab/gold/): canonical_holdings (date=2026-06-18, $1.63B) +
  account_gains (period=2026-05-18_2026-06-18, identity exact). Builders in .../gold/.
- **Cadence:** data/canonical/schwab/build_canonical_daily.py (verified 12/12). Scheduling =
  Option A (49-schwab-conv tail), pending 0.5.0 post-P0.
- **Docs:** data/canonical/schwab/docs/ (8-file suite). sb taxonomy = docs/04 (keystone).
- **ETFS AVGCAP:** monthly/2026-05.json + monthly/2026-06.json served clean (fully-canonical inf).
  avgcap_monthly_average.py has CANONICAL_PARTNERS allowlist + strict-ingest lister.
- **Memory banked:** project_canonical_schwab_path, _nna_decomposition, project_inflection_assets_
  migrating_to_opal (canonical ramp ~$12M, raw ~2x -- always read canonical).
- **Known residual (documented, not blocking):** gold-B market_growth conflates true price move +
  uncaptured transfer-out + rebalance; needs a trade/allocation feed for the clean split (CVO).

## Next Steps

1. [0.4.0_DS] Serve refresh of ETFS monthlies if 0.5.0 adjusts any inf slice; re-run on AE confirm.
2. [0.5.0_AE_OpalETL] Add build_canonical_daily tail-step to /49-schwab-conv post-P0 -> ping me ->
   I RAVC COO to close the cadence loop. Implement value-based floor across inf/49f/cot at
   contract-lock. Clean up stray holdings_2026-06-24.json.
3. [3.0.0_SA_CVO] Validate gold-B account_gains methodology + co-scope the transfer-out
   reconciliation feed.
4. [0.4.0_DS] DE ETFS_CANON tie-out AC: 49F verified clean; COT clean-by-construction; inf now
   canonical -- confirm the all-ticker producer-total == partner Total AUA for inf when its
   producer-total mode lands (co-own w/ CVO).
5. [0.4.0_DS] (optional) tighten the 161 unvalued in-kind legs via dim_asset pricing (hold for
   CVO); bring the declared-dtype gate generalization to CTO to ratify.
