# Cottonwood Supervised Retroactive Filter + Book Split (G2-G6 legs) — 0.2.0_DS_PortfolioAnalytics

**archetype:** IMPLEMENT

**Date:** 2026-08-20
**Task Order:** COT_SUPERVISED.G1-G7.retroactive-filter-and-portfolio-group (joint with 0.6.2_AE_PartnerETL)
**Status:** IN PROGRESS (my legs G2/G3/G5/G6 + G4-gold complete; G4/G4b behavioral acceptance rides tonight's scheduled run; G7 rides CTO arch-gate)

---

## Objective

Land the Andrew-sanctioned Cottonwood supervised/unsupervised retroactive filter +
portfolio_group advisor-book split per CTO design 63310 (CTO_COT_SUPERVISED_FIELD_TRACE_20260820.md):
my legs = the A_00 silent-drop class fix + dim columns (G2), the retroactive dim join +
HAR tie-out (G3), the gold aum toggle + book split emission (G5), the artifact-stated
caveat (G6), the daily invariant's gold half (G4), and the G4b ingest promotion (re-ruled
to my lane, CTO 63352 / COO 63353).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pipescript io | io A_00.accounts_dimension.py --pipeline cot | PASS | 15 downstream consumers enumerated before touching the dim |
| comp-pipescript deployed | deployed {A_00, cot_silver_merge, cot_bronze_ingest, D_05, B_00} --pipeline cot-* | PASS | STALE->deploy->MATCH cycle per script (Rule 13) |
| comp-find | collapse_relationship_grain / timeseries_overview / --name patterns | PASS | located the grain gateway + serving chain with denominators |
| comp-validate | A_00 + D_05 vs served bytes (downloaded artifacts) | PASS | 5/5 PASS each after authoring the two new stanzas |
| comp-which | "where do comp-validate configs live for cot gold artifacts" | PARTIAL | no curated rule; fuzzy list still pointed at comp-validate, comp-find closed it |
| comp-blast | timeseries_chart.json | WARN | AMBIGUOUS-SUBJECT refusal (4 nodes, bd/inf only) — correct refusal; cot instance absent from graph (gap noted) |
| comp-pulse | diff (via safe-commit risk-reflex) | PASS | HOLD on cot_silver_merge.py -> read the cited T+1 pricing/retry-net memory before proceeding (it validated the design) |

**What worked:** comp-pipescript deployed drove the full Rule-13 deploy-verify loop; comp-validate stanzas turned two acceptance criteria into standing machine checks.
**What failed:** nothing silently; comp-blast refused correctly on ambiguity.
**Gap found:** cot's gold/artifacts/timeseries_chart.json is not a comp-blast node (bd/inf instances are); cot D_05's new artifact will need graph registration on the next graph refresh.

---

## Work Completed

### 1. G2 — silent-drop class fix + dim columns (@386a3f6d94, @a2723b89b7)
- `_select_declared()` loud-prints any declared-but-undelivered column at all three
  narrowing sites of A_00. Phase-1 enumeration: served dim was 943x23; drop set
  measured **10 of 30** declared cols (trace named 6; +closed_date, account_is_open,
  relationship_sec_client_type, additional_advisor — surfaced to COO, not chased).
- Silver: `account_attributes` TABLE_CONFIG entry (dedup on (account_id, portfolio_group)
  deliberately — a two-book account is two real rows; Rule 17). Ran for 2026-08-19,
  verified served bytes match 0.6.2's bronze measurements exactly.
- Gold: `load_account_attributes()` (cross-row flag agreement assert, DC1 pattern;
  multi-book loud note) + `join_account_attributes()` (authoritative for its 4 columns).
  Incremental path: "current" is now a schema claim — a no-new-txn day still refreshes
  when declared attribute columns are missing.
- **Served-dim re-read (acceptance): 943 x 27, all 4 columns present** (819 Supervised /
  123 Unsupervised / 1 disclosed null z0927448761).

### 2. G3 — tie-out battery + the plane finding (@03d818c1e8, @62e0b77055)
- `tests/test_cot_supervised_tieout.py`: oracle constants pinned to their HAR JSON paths;
  join-key control 942/942; mutant (un-collapsed) FAILS correctly.
- **Grain pin vindicated from the vendor's own numbers:** naive-minus-collapsed =
  $205,070.77 = BD's own sum-of-books-minus-firm exactly.
- **Plane finding:** our collapsed holdings == allocations export == $480,056,488.78 to
  the penny (DataMining plane internally consistent) vs BD Dashboard $488,753,694.26.
  The -$8.70M gap is BD-internal, ~99% supervised-side; unsupervised delta only -$79,367
  (0.26%). Accrual self-test (CTO 63363): $220,718.17 = 2.5% of the gap — does NOT close.
- CTO ruled acceptance REBASE (63363): (i) internal exact TIE (penny), (ii) split parity
  PASS (0.26% <= 0.5%; share gap 0.10pp <= 0.25pp — the business ask achieved),
  (iii) plane gap DECLARED. **Battery VERDICT: ACCEPT** (two same-input runs identical).
- Semantic pin: the TO's "$455,532,550 named-books" is
  `$.firmAggregateResult.activeRelationshipAggregateResult.supervisedEmv` (active-rel
  supervised); named-books supervised actually sums to $451,918,881.59. CTO owned the
  trace correction.

### 3. G4b — ingest promotion (@f03ec88563)
One commit per the ruled form: TABLE_QUERY_TYPE "account_attributes": 4 + TABLE_DATE_MODE
("Custom", 14) + SNAPSHOT_TABLES membership (ratified) + 0.6.2's thin template envelope
folded verbatim (templateId 270648). Enumeration-proven live: `:1266` derives the nightly
table set from TABLE_QUERY_TYPE.keys(). Behavioral acceptance = tonight's scheduled run.

### 4. G5+G6+G4-gold — D_05 emitter + B_00 invariant (@8d19ea52a3)
- `D_05.supervised_split.py` -> `gold/artifacts/supervised_split.json`: firm_daily
  98-date history {aum_all, aum_supervised, aum_unsupervised, aum_unflagged} (MECE
  partition asserted per date) + book split at PAIR grain (two-book account in both
  books, firm counts once — COO 63346) + G6 meta.notes (caveat, plane gap, semantic pin,
  unflagged disclosure) verifiable off the artifact.
- **Cross-derivation control:** D_05 (account_performance) vs battery (fact_holdings+dim)
  penny-identical. **Book unsupervised ties BD to the penny on all three named books.**
- B_00: daily holdings-internal G4 invariant (guarded; LOUD FINDING on disagreement,
  SKIP printed on pre-G4 partitions); flags passthrough into canonical holdings.
- Validate stanzas: A_00 (4 columns as standing checks) + D_05; both 5/5 PASS vs served.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Silver dedup key includes portfolio_group | Rule 17: dropping a real two-book row is a business decision; gold adjudicates with an agreement assert + loud note |
| Dim refresh via INCREMENTAL path only | Full rebuild is window-degraded (73 daily txn files -> 942 accounts, tax data lost); incremental preserves the 943-account universe |
| G5 as new D_05 artifact, not D_00b extension | D_00b is a complex cohort artifact with real blast radius; a dedicated artifact lands the acceptance with zero existing-consumer risk; platinum wiring is serving-tier follow-on |
| Book split at pair grain, firm at account grain | Mirrors BD exactly (their book rows double-count the dual account; their firm row does not) |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/cot/scripts/gold/A_00.accounts_dimension.py` | _select_declared + attributes join + schema-aware incremental | Yes — 386a3f6d94, a2723b89b7 (deployed MATCH) |
| `data/cot/scripts/silver/cot_silver_merge.py` | account_attributes TABLE_CONFIG | Yes — a2723b89b7 (deployed MATCH) |
| `data/cot/scripts/bronze/cot_bronze_ingest.py` | G4b dict entries | Yes — f03ec88563 (deployed MATCH) |
| `data/cot/scripts/bronze/templates/account_attributes.json` | thin envelope (0.6.2-authored) | Yes — f03ec88563 (deployed) |
| `data/cot/scripts/gold/tests/test_cot_supervised_tieout.py` | G3 battery (rebased) | Yes — 03d818c1e8, 62e0b77055 (deployed) |
| `data/cot/scripts/gold/D_05.supervised_split.py` | G5/G6 emitter | Yes — 8d19ea52a3 (deployed MATCH) |
| `data/cot/scripts/gold/B_00.canonical_holdings.py` | G4 daily invariant | Yes — 8d19ea52a3 (deployed MATCH) |
| `data/cot/scripts/gold/gold_validate_config.yaml` | A_00 + D_05 stanzas | Yes — 8d19ea52a3 (deployed) |

Served artifacts written: accounts_dimension_latest.parquet (dim refresh, its own producer's
normal key — 943x27), gold/artifacts/supervised_split.json (new), silver/account_attributes/2026-08-19.parquet (new).

---

## Blockers

None hard. Two acceptance events ride tonight's scheduled cot run (external time gate,
stated plainly): G4 invariant first fire + G4b behavioral acceptance (bronze sentinel +
silver consuming). G7 rides CTO arch-gate acceptance.

---

## Current State

G2/G3/G5/G6 complete and verified on served bytes; G4-gold + G4b enabling acts landed and
deployed MATCH. Proof-of-spec instance next, then RAVC close to COO cc CTO. Surprises
surfaced same-turn throughout (10-of-30 drop set; all-taxable dim tax_status — banked at
COO; full-rebuild degradation; the plane finding — which CTO folded into the acceptance).

## Next Steps

1. [me] Proof-of-spec instance + validator rc=0; RAVC close to COO cc 1.0.0_SA_CTO.
2. [me] After tonight's run: verify G4 invariant fired + run silver merge for the new
   attributes date + G4b behavioral evidence.
3. [1.0.0_SA_CTO] Arch-gate acceptance (G7 cite).
