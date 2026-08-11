# THE COTTONWOOD A/B/C/D SHAPE SPEC (Black Diamond) — the tri-firm holistic view's remaining leg

**Author:** `4.0.0_SA_CRO~A` · 2026-08-11 ~0740Z · **archetype:** IMPLEMENT (design)
**Authority:** instruction 7 + the CVO handoff's Commission 2 (COT half); completes the tri-firm
packet Andrew's FINAL ratification waits on (@fdae32334f — 49F RATIFIED-TENTATIVE beside INF +
this). **Form:** identical to the INF spec (ADVREVIEW_49F_ABCD_AND_INF_SHAPE_SPEC_20260811.md
Commission 2) — the 49F group boundaries, acceptance batteries, provenance/manifest machinery,
policy blocks, and port protocol TRANSPOSE VERBATIM; only per-firm sourcing differs. Findings
F-1..F-6 apply as adjudicated (root per Andrew's ratified grammar with the Rule-24 note; Group W
per firm; segregated-NNA built in). **Grounding:** tonight's cot measurements (GIPS transposition
map + RECON-4 addenda + the rebalancer ingest census @314689f20a); open cells are MARKED, never
padded — they are exactly what RECON-5a's inventory + the two named probes close.

## COT GROUP A — dimensions/reference/boundary
| Artifact | COT source + verdict |
|---|---|
| A_00 dim_account | **RAW:** the BD account universe — `fact_acc`-equivalent = the custody holdings' account axis (925 accounts, 08-07) + the roster surfaces; the account key is the custody `Account Number` (the fourth key family: 9/11-digit mixed — the key-family table row is LAW here, every join states its family) |
| A_01 dim_relationship | **RAW, native-grain:** `Relationship ID` ships ON EVERY custody row (relationship-grain by construction — Andrew's 08-04 collapse discipline is the A_01 contract: `collapse_relationship_grain()` is the ONE sanctioned aggregation, naive sums double-count). Richer than both sibling firms; no parse needed |
| A_02 dim_boundary | **MANUFACTURABLE (named):** IN_CLIENT_BOOK from the custody universe; COLLECTION_ACCOUNT — **ABSENT-with-shape** at spec time (BD fee-leg discriminator unverified; the shape: fee-transaction payee legs in the BD txn export — `transaction_type` includes fee classes; the discriminator builds from the full-series classification census, not the window sample) |
| A_03 dim_security | **RAW:** custody rows carry AssetID/Symbol/Asset Name + the asset-dim silver (`bd-asset-dim` family); accrual inputs NOT needed (B_02: cot is the BEST-instrumented firm — see below) |
| A_04 dim_calendar | **VERBATIM:** `lib/trading_calendar.py` JOIN × the custody partition tree — **with the honest depth note: 47 daily partitions (2026-06-09..) at rest; the tree deepens as the backfill lands** |
| A_05 ref_txn_classification | **MANUFACTURABLE (named, form proven):** `transaction_type` (14) × `transaction_sub_type` (21) — ⚠ WINDOW-SAMPLE COUNTS (prior 3: the 21-vs-157 class); the build census runs the task-1 form @a876ee6ae9 over the union of all 64 at-rest partitions + backfilled history. Money-column verification FIRST (prior 1) |
| A_06 identity_crosswalk | **THE HARD CELL, honestly:** spine `account_id` (11-digit) vs custody `Account Number` = **MEASURED-NO-DIRECT-JOIN at every tested form** (tonight's structured zero) — the crosswalk REQUIRES an intermediary: candidates ranked (rebalancer_accounts bronze family → custody linkage → BD account-detail surface). **This is COT's one BLOCKING A-cell and it is RECON-5a's first deliverable**; the spec proceeds on the contract, the build waits on the measured bridge |

## COT GROUP B — valuation plane
**The sec3 branch decision, from measurement:** cot's custody rows carry per-position
`Market Value` + `Unaccrued Market Value` + **`Accrual` NATIVE** — vendor-valued positions with the
accrual DECOMPOSED in-row (best of the three firms). No account-level authoritative total surface
is measured yet (the BD balance query type is part of the RECON-5a inventory) — **B_00 (COT) v1:
V(t) = SUM(custody Market Value) per account per day — routed THROUGH the sanctioned
`collapse_relationship_grain()` (AMENDED per CTO review 074437Z: custody rows are
Relationship×Account×Asset grain and a naive per-account SUM DOUBLE-COUNTS — Andrew's 08-04
ruling; the collapse is named IN THIS CONTRACT LINE because B_00 is the row where the
double-count would reach a SERVED valuation). Acceptance gains the mutant control: an account
appearing under 2+ relationships sums ONCE (one duplicated-relationship fixture must fail the
naive sum and pass the collapsed one). CTO's framing note carried verbatim: this SUM is NOT the
sec3-banned reconstruction — it is a NAMED AGGREGATION of vendor-valued rows with native accrual
(the atom-8 rollup exception applied legally); and the swap-on-inventory (BD account-level total
becomes authoritative, SUM demotes to the B_03 tie) is a RULED SPEC-AMENDMENT EVENT when it
happens, never a silent inversion.** The account-level BD total stays the B_03 tie ONCE the
inventory surfaces it (marked OPEN; if BD ships none, B_03's tie is the relationship-grain
collapse identity instead — stated, not assumed).
B_01: custody passthrough + quality flags. **B_02: RESOLVED-BY-CONSTRUCTION — accrual ships
in-row; the artifact lands carrying the RAW verdict** (no materiality gate needed; the 49F/INF
asymmetry table's "cot best" cell, now a spec row). B_03: tolerance + ruled-recalibration verbatim.
**History: the backfill program IS the B-group's initial build** (Custom-window walks, P2b sizes
the floor) — the daily run is the same code at date=T, per the 49F backfill-first rule.

## COT GROUP C — flow ledger / TWR engine / validation
| Artifact | COT instantiation |
|---|---|
| C_00 flow_ledger | source = the BD txn window partitions (union + backfill); classes from A_05's full-series census; **`backdated_date` + `entry_date` ship natively — the reversal/restatement instrumentation 49F had to specimen-hunt is IN-BAND at cot** (the restatement window exists because BD restates; C_00 carries restatement provenance per row); pair-matching verbatim; segregated-NNA (F-4) built in |
| C_01 nna_canonical | re-based on C_00; **relationship-grain rollups via the sanctioned collapse ONLY**; the guard battery pattern (coverage continuity, no-residual, point-in-time) transposes from the INF extraction |
| C_02 twr_engine | **TRANSPOSES UNCHANGED** — with the depth qualifier: period returns compute only where the backfilled valuation series covers the period; pre-floor periods are UNSUPPORTED by construction (the C_03 status enum carries it, never a fabricated BMV) |
| C_03 twr_lineage | verbatim; USD boundary same |
| C_04 validation_battery | all nine; **vendor-native return tie = OPEN-PENDING-P2** (BD may ship a performance queryType — the sixth family found tonight proves the catalog exceeds our five; the discriminating instrument is named). If absent: the check lands UNAVAILABLE-BY-MEASUREMENT exactly as 49F's does — either way the cell closes HONESTLY, not by assumption. P&L identity via the realized/unrealized BD tables (validation-only) |
| C_05 verification series | **CONDITIONAL on P2:** if BD ships computed returns → the INF-style verification series lands; else struck with the measurement cited |

## COT GROUP D — frozen-shape serving
Census discipline VERBATIM (three legs, family grain, route_class). **The cot ADVI serving
universe's believed-state seed:** the `/api/scoped/advisor-intelligence/*` router serves
`opal-data-cot` per the firm-bucket map; the cot gold spine (`gold/dimensions/
accounts_dimension_latest.parquet` + advisor_assignments + client_dimension — same spine shape as
inflection's, identified tonight) feeds whatever publisher family D_00 measures. **D_00 runs
FIRST, as law — cot's served surface is the least-enumerated of the three firms and nothing here
is designed from that believed-state paragraph.**

## COT GROUP W — scheduling atoms (F-2, per firm)
Pre-filled from tonight: the cot-BD session cadence (ce99054e44's 4:30p-ET anchors), the
retry-net's C-2/C-3 fixes (landed R-1 union-preserve; the double-lag remedy in DS's queue), the
mirror 22:30Z leg, first-write-wins vs multi-write declarations per key family — **the custody
leg's write-cardinality atom is the ONE that froze the MDPF chain this week; it is pre-declared
here, not rediscovered.**

## THE OPEN-CELL REGISTER (what FINAL ratification should know it is ratifying around)
1. **A_06 identity bridge** — BLOCKING for account-grain ADVI serving; RECON-5a's first deliverable.
2. **B_00's account-level total** — OPEN (inventory); v1 ships on the named SUM.
3. **History floor** — P2b sizes it; the backfill program is the build's first act.
4. **C_04/C_05 vendor-return branch** — P2's named instrument decides; both outcomes are honest.
None of the four blocks SPEC ratification; 1 blocks BUILD of the account-grain serving legs only.

-- 4.0.0_SA_CRO~A
