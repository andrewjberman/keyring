# Commission 1+2: adversarial review of the 49F A/B/C/D specs + the INFLECTION A/B/C/D shape spec

**Author:** `4.0.0_SA_CRO~A` · 2026-08-11 ~0725-0745Z · **archetype:** VALIDATE + IMPLEMENT (design)
**Authority:** Andrew-direct instruction 7 + the CVO handoff block (committed). Reviewed state =
the RULED specs (A @9c294bbf15+@6fba62393b · B @d57bbf7229+@39c41163cd · C @f882b91ce2 ·
D @1e11389af8). **Grounding: live state measured this session; every number re-derived where my own
deliverables are cited (seam e), never trusted from the relay.**

---

# COMMISSION 1 — ADVERSARIAL FINDINGS (ranked; each with its grounding and its remedy shape)

## F-1 · THE DEFAULT PRODUCT ROOT COLLIDES WITH RATIFIED LAW (Group A §3.1) — the author's seam (a), answered with LAW not preference
Group A's default mints `opal-data-assets/portal/gold/advi/49financial/`. **Rule 17b's ratified
canonical form is `{vendor}/{firm}/{medallion}` under opal-data-assets, with SERVING in
opal-data-portal-v2/platinum — and the existing top-level `portal/` tree inside opal-data-assets is
MEASURED NON-CONFORMING RESIDUE** (17b's own 2026-08-05 census: "top-level gold/ json/ portal/
code/ OUTSIDE the {vendor}/{firm}/{medallion} grammar"). The default therefore EXTENDS a
known-non-conforming root with new structure — minting fresh grammar debt under atom-1's flag.
The spec's own alternative (`schwab/08335338/gold/`) IS grammar-conformant. **Remedy: flip the
default to the vendor-tree home, or route the root as a NAMING ACT to Andrew (Rule 24 — a new root
is a taxonomy act; 17b explicitly ratified direction WITHOUT migration authority, and minting a new
non-grammar root is the stronger violation).** Every contract survives either way, as the spec says.

## F-2 · THE SEQUENCE HAS NO SCHEDULING-ATOM GROUP — and tonight's INF freeze is the measured cost of exactly that omission
All four specs defer dispatch/trigger topology to "the runner wiring" (A §4). **The INF chain is a
fork of this same archetype family, and it froze for nine days tonight precisely at the atoms no
spec carried: universe definition, write cardinality, Sunday-rebuild semantics, dispatch-path
census, mode-homing** (my 01_STOP_MECHANISM + CTO's remedy ruling + CVO's own dispatch-path-census
suggestion). A shape transposed without its scheduling atoms is the shape-cloned-without-atoms
failure re-armed. **Remedy: a GROUP W (wiring) spec BEFORE build decomposition — pack 01's A1–A5
declared per leg (write cardinality, label semantics, trigger predicate, re-delivery policy,
settle window) + the dispatch-path census cell + the host-mutex/mode-homing rows CTO ruled tonight.
One page; it is the page the INF post-mortem says was missing.**

## F-3 · B_02's RATE-BEARING PREDICATE UNDER-COVERS AMORTIZING INSTRUMENTS (the author's seam (c), sharpened)
The 112-asset predicate is `interest_rate` nonzero. **Zero-coupon/OID instruments accrue with
interest_rate = 0 — their accrual rides AMORTIZATION, and the estate's own tables prove the class
exists in the book: fact_rld/rlu/rly carry `ytd_amortization`, `cost_basis_unamortized`,
`adjusted_cost_basis_amortized` as populated schema** (my RECON-2 schema census). The materiality
gate as specced can read IMMATERIAL while amortizing paper accrues outside its denominator.
**Remedy: B_02's census gains a second predicate leg — assets with nonzero amortization activity in
the attribution families — unioned into the materiality read. One extra groupby; the gate's
verdict then covers the whole accruing class.**

## F-4 · EXTERNAL-BY-DEFAULT SERVES TWO MASTERS WITH OPPOSITE CONSERVATISM (the author's seam (d), answered structurally)
C_00's unmatched-pair default is EXTERNAL — conservative FOR TWR (the standard's safe direction).
**But C_01 re-bases NNA on the SAME ledger, and for NNA the same default is ANTI-conservative: every
unmatched intra-book transfer read as external INFLATES net-new-assets** — the client-facing flow
number the fabric spent tonight protecting to the dollar. The r(t) sensitivity quantification the
CVO asks for is necessary but not sufficient; the structural fix is per-consumer treatment.
**Remedy: the flow-ledger's class enum stays as specced, but C_01 consumes `resolution_provenance`
and books EXTERNAL-BY-DEFAULT rows into a SEGREGATED NNA line (`nna_unresolved_direction`) rather
than the headline — the headline carries matched+code-resolved flows only, the segregated line
carries the residual with its census.** TWR keeps the conservative default; NNA stops inheriting
its bias. (Also closes the review question with a design rather than a measurement debt.)

## F-5 · A_01's FAMILY MAP LEAVES ~53 ACCOUNTS UNMAPPED, UNNAMED (grounded in the specs' own numbers)
fact_acc = 7,239 accounts (re-derived tonight: 7,239 rows, all 10-digit); fact_fam ≈ 7,186 rows
~one-per-account (feasibility cell 2). **The ~53-account delta has no stated disposition in A_01's
contract — household composites will silently exclude them.** Remedy: an explicit unmapped-census
column + disposition enum (SELF-FAMILY default vs EXCLUDED-LOUD), acceptance row: mapped +
unmapped == 7,239, denominators printed.

## F-6 · D_00's FE LEG YIELDS TEMPLATES, NOT KEYS — reconcile at the right grain (the author's seam (b), refined)
The deployed-bundle extraction returns PATH TEMPLATES (`clients/{clientKey}`,
`advisors/{advisor_key}/book`) while legs 2/3 return CONCRETE KEYS — a per-key three-way
reconciliation structurally cannot tie for dynamic families. Also one 49F-specific surface the
bundle CAN'T show as S3: the per-client detail rides API-GW→Lambda (bd-client-detail), so leg-1
must capture FETCH ROUTES, not only S3-key reads. **Remedy: reconcile at FAMILY grain (template ×
live-instance-set), and the census row contract gains `route_class: s3-direct | apigw-lambda`.**
Everything else in D_00's design holds — the three-leg predicate structure is right.

## F-7 · VERIFIED CLEAN (seam e executed — numbers re-derived, no drift found)
A_00's 7,239/10-digit ✓ (my fact_acc read) · A_04's 525 partitions 2024-07-08..08-07 ✓ (my
census) · A_03's 112/2,313 + the sentinel-maturity trap ✓ (base's run, my schema census
corroborates the fact_sec coupon fields) · C's four estate-truths ✓ (@a876ee6ae9/@5bb3b2626d,
whose form my transposition map already inherited) · A_06's 99.86/99.65 carry DIFFERENT
denominators than my 99.8% form-bridge (feed-side vs map-side vs end-to-end) — **not a
contradiction; the spec's carry-both-denominators clause is exactly the right guard, keep it.**
The C_04 "Schwab-native return tie UNAVAILABLE-BY-MEASUREMENT" cell ✓ (my 20-table census).

**Net verdict on the four specs: APPROVE-WITH-FINDINGS — F-1/F-2 are pre-build blockers (one
routing act + one page); F-3/F-4/F-5/F-6 are spec amendments of a paragraph each. The sequence's
architecture (frame → valuation → flow/TWR → frozen serving), its law-citation discipline, and
its acceptance batteries are sound and I attack nothing in them.**

---

# COMMISSION 2 — THE INFLECTION A/B/C/D SPEC (same shape, Orion fields; a MODEL, never a port)

**Pattern parameters swapped per @6e180df78e:** `{scope}` = inflection · A-layer source = Orion
(endpoints catalog + the INF_ATOMDECOMP substrate) · intermediate fan-out = the INF medallion in
`opal-data-inf` (the firm-tree law; product-root question inherits F-1's routing verbatim).
**Every field verdict below is RAW / MANUFACTURABLE / ABSENT-with-shape, grounded in tonight's
measurements (GIPS transposition map + P1 probe + the stop-mechanism run). The 49F group
boundaries, acceptance batteries, provenance/manifest/boundary-version machinery, policy blocks,
and port protocol TRANSPOSE VERBATIM — only the field sourcing below differs.**

## INF GROUP A — dimensions/reference/boundary (all seven artifacts instantiate)
| Artifact | INF source + verdict |
|---|---|
| A_00 dim_account | **RAW:** `silver/api_dims/accounts_v2` (NewPortfolio endpoint, daily; account_id native int; 98.0–100% identity legs per RECON-4). Universe = W-C's DERIVED PREDICATE, never `INFLECTION_REP_IDS` (the 28-site allowlist is the fork's measured breaker — its retirement is a Group-A precondition, not an option) |
| A_01 dim_relationship | **RAW:** `household_rep_mapping` (endpoint-landed daily) — INF's family map needs NO fact_fam-style parse; unmapped-census per F-5 applies (the 07-13 household-rescue class is the INF specimen of the same gap) |
| A_02 dim_boundary | **MANUFACTURABLE (named):** IN_CLIENT_BOOK from the predicate universe; COLLECTION_ACCOUNT — the FRM-leg discriminator does NOT transpose (Orion is not Schwab's ledger); INF's named computation = advisory-fee flow classes (`Advisory Fees Paid`, 15,193 rows measured) → fee-receiving-account detection, ELSE the boundary carries `collection_detection: ABSENT-with-shape` (the shape: a per-account fee-credit ledger from Orion billing — the billing dim carries payee-side rows) — REFUSE-not-guess per the doctrine |
| A_03 dim_security | **RAW:** assets_v2 + the asset dim surfaces; accrual inputs NOT needed (see B_02) |
| A_04 dim_calendar | **VERBATIM:** the same `lib/trading_calendar.py` JOIN — against the canonical-holdings partition tree (2,450 daily partitions 2019-09-17.., re-derived tonight) — the amendment transposes unchanged |
| A_05 ref_txn_classification | **MANUFACTURABLE (named, mostly built):** the 46-code transTypeId universe (ZERO nulls, full 1.43M-row series — NOT a window sample) × `activityCategory` (explicit external/internal) × the existing 47-entry dict + `orion_cashflow_taxonomy.yaml`, rebuilt in the task-1 FORM @a876ee6ae9 (full-series census, first-match rules, dual materiality; the `Other` class 1,793 rows = the residue row). The four estate-truth priors apply (find the real money column FIRST: verify `transAmount` vs any gross/net twin at build) |
| A_06 identity_crosswalk | **RAW, simpler than 49F:** account_id is NATIVE across txn/positions/perf/billing dims (RECON-4: 98.0% spine join; 100.0% real-account). The crosswalk artifact still exists (uniformity of shape) but is near-identity; smartx allocation machinery is NOT in INF's path |

## INF GROUP B — valuation plane (the one structural transposition decision, stated openly)
**49F's sec3 preferred branch used an AUTHORITATIVE account-level total (`net_mv_plus_cash`). INF's
measured equivalent is TWO-SOURCE:** (1) the position plane — `positions_mv` → canonical holdings,
**100% raw vendor `pmv_only` in every sampled era, 2,450 daily partitions** — SUM(account) = V(t)
candidate; (2) the vendor's own account-level total — `unified_account_dim` **Ending MV via
Activity Option 1 explicitly** (catalog Gotcha #1: the $140M-vs-$199.4M lesson — the option id IS
the contract). **B_00 (INF): V(t) = the Ending-MV authoritative total (RAW, endpoint-attested,
historically pullable per the P1-proven Custom-window machinery); the positions SUM becomes B_03's
integrity tie** — same authoritative-over-reconstructed law, sources swapped by measurement.
**B_02 accrual: N/A-BY-CONSTRUCTION** — Orion positions are vendor-valued (accrual embedded in
marks); the artifact still lands, carrying the N/A verdict + grounding (uniform shape, honest
cell). **B_01**: positions passthrough with the same quality flags (`nav_price` staleness vs the
canonical price... NO — F-1-of-instruction-4 applies: the interpolated price tier is DISCARD-class;
B_01's flags derive from vendor fields only). **B_03**: SUM(B_01) vs Ending-MV per account-day,
1bp-class ex-ante tolerance with the ruled-recalibration clause verbatim.

## INF GROUP C — flow ledger / TWR engine / validation
| Artifact | INF instantiation |
|---|---|
| C_00 flow_ledger | fact-source = the txn snapshot (1.43M rows, dates+amounts 100%); classes from A_05; **the debit_credit amendment transposes as a SEMANTIC-VERIFICATION row for `transTypeId`×`activityCategory` consistency** (INF's trap-equivalent: Exchange In/Out pairs ~718K rows are share-class internal — pair-verified, not assumed); pair-matching for Journal In/Out (1,566/1,071) via the same engine pattern; **F-4's segregated-NNA treatment is BUILT-IN from v1** |
| C_01 nna_canonical | re-based on C_00; **the INF C_01 EXISTS and its guard battery is tonight's proven quality structure (F7 coverage guard, no-residual-advisor, time-lock) — EXTRACT the guards verbatim, re-base the flow input, and the point-in-time/W-D invocation axis from the refactor spec applies** (the daily run computes forward; full re-derive = deliberate maintenance) |
| C_02 twr_engine | **TRANSPOSES UNCHANGED** (the GIPS forms are source-agnostic) — EOD convention, geometric linking, REFUSE-on-no-BMV, gross/net via the fee classes (`Advisory Fees Paid` = the management-fee family; admin-fee split per the A_05 census) |
| C_03 twr_lineage | verbatim; method = TRUE_TWR-daily; USD boundary same |
| C_04 validation_battery | all nine checks — **with the star difference: the "vendor-native return tie" check, UNAVAILABLE at 49F, is AVAILABLE-AND-PROVEN at INF** — the Envision Performance Dim ships account-grain TWR with `CalcMethod=TWR` in-band, daily since 04-28 AND for arbitrary historical windows (P1 probe: 99.8% as-of-consistent). **INF's battery gains the strongest possible independent-derivation cross-check: our computed TWR vs the vendor's, two genuinely different derivations** (the shared-derivation law satisfied better than 49F's monthly-aggregate tie). P&L-identity check uses realized/unrealized from the tax dims (validation-only, decision 4) |
| C_05 (INF-only, small) | **vendor-TWR verification series**: the daily perf-dim snapshot + on-demand historical windows land as `verification_twr` (RAW) — the input C_04's tie consumes; never served as OUR return (provenance separation) |

## INF GROUP D — frozen-shape serving
**The census discipline transposes VERBATIM; the INF census universe is already half-enumerated
(comp-estate advi-inf, believed-state):** `platinum/firm/{dashboard, timeseries_overview,
cumulative_chart, header_metrics_fresh, timeseries_chart, mix_summary, client_directory,
fee_efficiency, partner_analytics_*}.json` + `platinum/firm/snapshots/aua_by_*.json` +
`platinum/advisors/{advisor_key}/{book,summary,top_holdings,timeseries,composition,mix}.json` via
`inf-portal-publisher` + `inf-portal-advisor-publisher`, consumed by
`portal/src/pages/AdvisorIntelligence/_partners/inflection` through `/api/scoped/
advisor-intelligence/*`. **D_00 measures this as its first act (three legs, F-6's family-grain
reconciliation + route_class), and the D_04 fee fields land per the CPR-4 succession: the
unreconciled bucket is part of the frozen shape going forward (it shipped tonight).** Emitters:
one per family, C-canonicals only, byte-schema identity, spelling law, schedule floors — verbatim.
**Port protocol: verbatim, with the INF-specific note that the publisher chain (pipeline-complete
sentinel → inf-portal-publisher) is the LIVE delivery mechanism and stays untouched in v1.**

## INF GROUP W — the scheduling-atom page (F-2 applied to my own derivation, so the fork's lesson is structural)
One table, five atoms × every leg (pull/silver/gold/serve), pre-filled from tonight's
measurements: the Sunday full-pull union-preserve semantics (landed), the aggregator mode-homing
(CTO-ruled remedy), the dispatch-path census (CVO's cell), the 13:47Z floor + event accelerators,
first-write-wins vs multi-write declarations per key family. **The INF spec is not complete
without this page, by its own fork's post-mortem.**

## SEQUENCING + PROTOCOL
Same review protocol: each group to CTO; certification returns to `3.0.0_SA_CVO` (Rule 14e). Build
decomposition = COO. The COT derivation follows this same file's shape once RECON-5a's endpoint
inventory + the BD catalog question (P2's named instrument) close its A-layer cells — its
transposition seed rows are already in GIPS_TRANSPOSITION_INF_COT_20260811.md.

-- 4.0.0_SA_CRO~A
