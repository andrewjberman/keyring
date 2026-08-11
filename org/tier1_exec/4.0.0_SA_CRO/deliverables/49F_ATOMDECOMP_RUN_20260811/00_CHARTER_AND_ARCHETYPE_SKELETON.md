# atom_decomp run 2 — the 49F gold analytics runner as the ADVI canonization archetype

**Run:** 49F_ATOMDECOMP_RUN_20260811 (recon chapter **RECON-2**, collective frame @07c6f68bf4; naming per base CRO ruling @3833ce88d1) ·
**Author:** `4.0.0_SA_CRO~A` · opened 2026-08-11 ~0535Z · **archetype:** EXPLORE + TRACE
**Authority:** Andrew-direct instruction 3 (verbatim in
`ANDREW_DIRECT_20260811_CRO_A_INF_ATOMDECOMP_E2E.md`): the 49F/Schwab **08335338** account as the
base to create *"the perfect gold analytics runner,"* then the archetype for inflection and
cottonwood — *"reverse engineer field for field what we need for the others."*

## P0 charter
- **Objective:** extract the canonical ADVI gold-analytics SHAPE from the 49F estate; specify the
  perfect runner (canonical sourcing × preserved serving contract × north-star derivation rules);
  produce the field-for-field replication map for inf + cot.
- **Decision enabled:** the ADVI canonization program (CTO/COO consuming per the collective frame).
- **Mode:** read-only recon (no mutation in this run).
- **Scope:** `opal-data-assets/schwab/08335338/**` (canonical base) ·
  `opal-data-bd/**` (current serving estate) · `data/black_diamond/scripts/gold/**` (the runner) ·
  the ADVI portal contract (`/api/scoped/advisor-intelligence/*`).
- **Invariants:** two-bucket law (08335338=ADVI, never the 4-digit prefix; 08242234=MDPF is OUT of
  scope) · serving contract preserved (P7) · no shadow paths · note-2a's rigid census
  (field/staging/output/methodology per script) is the program continuation this charter opens.
- **Coordination:** COO's RECON-5 split (cot endpoint inventory parallel; conformance decomp waits for
  this archetype to stabilize) · CTO's unified pattern spec @3272f3c4b0 cited, not re-derived ·
  naming: recon chapters RECON-1..7; my MDPF findings keep C-1/C-2/C-3 verbatim (base CRO ruling @3833ce88d1).

## THE THREE-LAYER ARCHETYPE SKELETON (all layers enumerated tonight, live)

### Layer 1 — the canonical base: `schwab/08335338/silver/` — WHY 49F IS THE BASELINE, MEASURED
**20 tables: 4 dims (asset, balance, position, transaction) + 16 fact tables** (acc, fam, rld,
rlu, rly, rps, rps_s2, rtu, rty, sec, slm, trn, uln, ult, upn, upt), date-partitioned, core set at
**525 daily partitions each, current through Friday 08-07 (T-1 healthy)**. Schemas pulled per
table (extraction in the run scratch; e.g. `fact_trn` 140 cols, `fact_acc` 95, `fact_rld` 86,
`dim_transaction` 44). This is what "complete fact tables" means in the estate's own terms: full
custody depth (positions settled/unsettled, lots, realized/unrealized at daily/monthly/yearly
grains, transactions with settle dates, balances with margin detail) delivered raw by the
custodian — **nothing here is derived by us.**
Early census findings: **(f1)** `fact_fam` + `fact_slm` are UNPARSED positional passthroughs
(`col_1..col_6` + provenance) — schema never applied; **(f2)** period-end variants run their own
cadences (`fact_rlu`/`rtu` 12 partitions → 06-05; `fact_rly`/`rty` 37 → 07-31) — the census
carries cadence PER TABLE, never inherited from the daily core.

### Layer 2 — the runner: `data/black_diamond/scripts/gold/` (69 scripts) + `gold_dispatch.sh` on EC2 `bd-gold-layer-runner`
Production chain A_00..D_04 (~30: dimensions → holdings/lots/gains → canonical perf/NNA/tax/fee →
portal aggregates/leaderboard/partner analytics/client detail) + an E_* diagnostics family (~10) +
legacy. **Load-bearing recognition: the INF chain is ALREADY A FORK of this archetype** — same
letter tiers, same numbering (`INF_A_00…INF_D_04` mirrors `A_00…D_04`). The shape replication
Andrew wants has been done once, and tonight's INF freeze is the measured record of what the fork
got wrong: **the SHAPE was cloned; the per-vendor ATOMS (universe definition, write cardinality,
settle windows, label semantics — pack 01's A1–A5) were not re-derived.** The canonization spec
therefore ships shape + atoms, never shape alone.
**(f3)** The CURRENT 49F runner does NOT read Layer 1 — it reads the legacy `opal-data-bd` silver
(BD DataMining exports, yfinance T2 prices, `interpolated_prices.parquet`) — the same derivation
disease the INF audit flagged (INF run @03). **The perfect runner is therefore NOT the current
runner canonized; it is the current runner's OUTPUT CONTRACT re-sourced onto Layer 1 + raw
endpoints under the north-star rules** (derivation guilty-until-proven; NNA-class calculations
stay; interpolated valuation dies — Portfolio valuation comes from custody-delivered values which
Layer 1 carries natively).

### Layer 3 — the serving contract (the shape inf + cot replicate)
`bd-portal-publisher` artifacts: `gold/artifacts/{timeseries_chart, architect_leaderboard,
clients_tab, summary/header_metrics, filters/dimensions, snapshots/aua_by_{architect,state,
tax_status,region}}.json` · `platinum/firm/{timeseries_overview, partner_analytics,
cumulative_chart, header_metrics_fresh, leaderboard}` · per-client `gold/clients/{relationship_id}.json`
(API-GW served) · gold parquets (positions_cube, holdings_lots, account_gains, canonical_nna,
timeseries/, snapshots/) — consumed by `portal/src/pages/AdvisorIntelligence/` `_partners/49financial`
+ `_shared` tabs via `/api/scoped/advisor-intelligence/*`. **This layer is the CONTRACT: the
archetype's output side is field-frozen here, then each firm's map says which endpoint fills each
input field.**

## THE REPLICATION METHOD (how "reverse engineer field for field" executes)

For each Layer-3 artifact field, walk backward through Layer 2 to the Layer-1 (or endpoint) fields
it consumes → that backward walk IS note-2a's rigid census (field/staging/output/methodology per
script). Then per firm: **inf** fills each required base field from the Orion/Eclipse endpoints
(`INFLEC_API_ENDPOINTS_CATALOG.md` + the INF run's three-bucket map @03 — TWR raw, valued Assets
raw, NNA calculated); **cot** from Black Diamond (endpoint inventory running parallel per COO's
split). A base field with NO endpoint equivalent for a firm is a NAMED GAP (deliverable row), never
a derive-around. **The two runs tonight are the method's two halves meeting: 49F gives the target
shape; the INF audit gives the raw-sourcing discipline the fork must obey this time.**

## RUN STATE + NEXT

Layers 1–3 enumerated live tonight (this record). **CHARTER AMENDMENT (~0540Z, Andrew-direct
oversight frame via CTO relay @3c8418e34b):** this run is the ADVI spine of the CTO-overseen SSOT
matrix (`org/tier1_exec/1.0.0_SA_CTO/deliverables/SSOT_RECON_MATRIX_20260811.md`); deliverables
take the **believed-vs-actual rectangle form (@41692cd3d2)** as the required shape, and the
decomposition grounds **all SIX legs** — explicitly **L2** (what triggers bronze→silver for
schwab/08335338-ADVI today: event/cron/absent, measured) and **L5/L6** (bd-portal-publisher + the
deployed frontend's actual reads) — the archetype claim is empty without upstream trigger and
downstream serve in the rectangle. CVO cross-examines; refused cells are the system working.

NEXT (the program, in order): the six-leg rectangle over 49F-advi (L2 + L5/L6 first — currently
believed-state from census prose, not measured); the note-2a backward walk over the ~30 production
scripts (the rigid census); the perfect-runner spec (contract × Layer-1 sourcing × north-star);
the inf/cot field maps. RECON-3's substance already exists in the INF run records (fills
L2/L3/L4-partial per the matrix; open cells = the ~24/44 UNREVIEWED scripts + L5/L6); conformance
to the rectangle shape follows. RECON-5 flag to base CRO when RECON-2+RECON-3 close.
