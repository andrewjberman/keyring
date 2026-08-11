# INF gold-script audit + the raw-endpoint refactor spec (P9/P10 of the atom_decomp run)

**Authority:** Andrew-direct instruction 2 (@097ba43959 record) + the north-star generalization
(CTO relay 045513Z, corrected 045806Z): **raw-from-endpoint is the default; every derivation is
guilty-until-proven; the must-calculate exception list is Andrew's to fix** (provisional members:
NNA [flow], cross-account rollups). · **Author:** `4.0.0_SA_CRO~A` · 2026-08-11 ~0525Z
**Endpoint ground:** `docs/architecture/INFLEC_API_ENDPOINTS_CATALOG.md` (the file Andrew
remembered — CTO-consolidated 2026-04-28, four endpoint families, 130+ verified column paths in
`data/orion/manual_api/PATH_DISCOVERY.md`). Egress granted for live probes; where a claim below
rests on the catalog's own verified pulls + daily-landing bronze rather than a fresh probe, its
evidence class says so.

---

## 1 · THE HEADLINE, MEASURED: THE RAW DATA IS ALREADY LANDING; THE SERVED SURFACE DERIVES ANYWAY

`silver/api_dims/performance/` — **account-grain vendor TWR + risk metrics, pulled DAILY** (Envision
Performance dim, 27 cols, LIVE; bronze `performance_dim.csv` landed 2026-08-10 14:28Z, 744KB —
DATA). Meanwhile the served performance surface (`INF_C_02.client_performance` →
`gold/timeseries/client_performance.parquet` → every D-chain publisher) computes
`aua_change, growth` **from canonical AUA deltas net of NNA flows — performance as a residual —
and C_02 ITSELF reads the vendor TWR dim nowhere** (SOURCE: C_02 inputs are canonical_performance +
canonical_nna + accounts_dimension only, docstring + import graph). *(CORRECTED per CVO cert
@08215b39a3 refusal: the original "reads it NOWHERE" swept the D-chain publishers — FALSE there:
D_00c/D_02/D_04 have loaded silver/api_dims/performance since 04-28, and D_00c reads BOTH the
C_02 residual base (:705) AND the TWR dim (:302). The claim is C_02-scoped only. W-B's scope
absorbs the 3 existing readers, and its acceptance must first answer the CVO coherence question:
does any served surface present vendor TWR beside C_02-residual growth SIMULTANEOUSLY?)* Andrew's "performance is not a
residual" is not a future aspiration; the raw feed his refactor wants is already in silver, daily,
unconsumed by the serving chain.

## 2 · THE THREE-BUCKET FIELD MAP (north-star decision rule applied)

### ILLEGITIMATELY-DERIVED — an endpoint gives it raw; the gold script computes it anyway **(RATIFIED as a LAW verdict @d272021791 — W-A/W-B execute against it)**
| what | where derived | the raw source | evidence |
|---|---|---|---|
| **Account/holding VALUATION via a price series** | `INF_build_canonical_prices` (T1 txn-observed medians → T2 yahoo → **T3 linear interpolation → T4 carry-forward**) feeding the B-chain | `GET /api/v1/Portfolio/Accounts/{aid}/Assets/{date}` + `/Clients/{cid}/Assets/{date}` — sync JSON, VALUED asset grain (catalog §Portfolio/Assets; chosen there precisely because Envision asset-grouping timed out) | SOURCE + DECLARED |
| **Performance (growth/aua_change)** | `INF_C_02` residual from AUA deltas − flows | Envision Performance dim: account-grain TWR + risk metrics, already silver-landed daily | SOURCE + DATA |
| **Leaderboard performance metrics** | `INF_D_00c.portal_leaderboard` (33 derivation signatures) recomputes advisor aggregates off the derived C_02 base | same TWR dim, aggregated at advisor grain | SOURCE (base-inheritance: fixing C_02's source fixes D_00c's inputs) |
| **Non-fee AUA** | `INF_D_04:822` residual `total_aua − fee_earning_aua` | Orion Billing classification (`is_fee_earning` per row) — same dim, classified sum | SOURCE; **fix drafted, 02_D04_RESIDUAL_FIX_DRAFT.md** |
| **Ending/beginning MV variants** | assorted D-chain re-additions | Envision Activity Options 1–6 (EndingMV/BeginningMV/±accrual, explicit `activityOptionId`) | DECLARED (catalog Gotcha #1 — the $140M-vs-$199.4M lesson is ITSELF a raw-field mis-pull caught and documented) |

### MUST-CALCULATE — **RATIFIED by Andrew ~0542Z (@d272021791)**: exactly {NNA flow · non-fee residual (TRANSITIONAL — retires when the D_04 fix verifies) · cross-account rollups · the unreconciled bucket}; everything else raw. *(Was provisional at authoring; flipped on ratification per CTO relay 054315Z.)*
| what | why it cannot be raw | note |
|---|---|---|
| **NNA (net new assets)** | a FLOW net of market movement; no endpoint serves it (Andrew-named) | stays calculated — C_01's job survives the refactor; its POINT-IN-TIME form is Wave D |
| **Cross-account/household/advisor rollups** | aggregation grain is ours, not the vendor's | provisional |
| **The unreconciled bucket** (new, F4) | a difference is a difference by construction | deliberately a calculation — it EXPOSES cross-source drift |
| **49F TWR/period-returns from Schwab components** | Schwab ships NO computed returns — only lot-grain gain/loss + cost-basis + flow components (measured over all 20 canonical tables) | **GRANTED Andrew-direct ~0628Z (instruction 5)**; inputs raw, computation explicit — per-firm asymmetry resolved: inf=vendor TWR raw, 49f=computed-from-components, cot=TBD (RECON-5) |

### RAW-AVAILABLE AND ALREADY CORRECTLY RAW (so the audit does not overclaim)
`INF_B_00` canonical holdings is a **positions_mv pass-through** (its own header) — the holdings
values are vendor positions, not price-series products; the A-chain dims (accounts, reps,
households) are endpoint-sourced pass-throughs. **The rot is concentrated in the
price-series→valuation tier and the performance/residual tier, not uniformly "all of gold."**

### UNREVIEWED (marked, not silently covered)
~24 of the ~44 chain scripts got only the signature sweep, not a read (`INF_C_03..C_09`,
`INF_D_02*/D_03/D_05*..D_11`, `INF_09`). The sweep says the heavy derivers are the five named
above; a per-script verdict table for the rest belongs to the refactor program's Wave-0
characterization, not to tonight's record. **An unmarked gap reads as coverage — this one is
marked.**

## 3 · THE REFACTOR WAVES (P10 work-package shape; owners SUGGESTED — CTO+COO staff)

**W-0 · characterize** — per-script I/O + derivation verdict over the full 44 (the method's P2 at
scale; the 20 signature-flagged reads are done). *Owner-suggestion: CRO~A continues.*
**W-A · valuation to raw** — B-chain valuation reads Portfolio/Assets per-account valued JSON;
`canonical_prices` T3/T4 (interpolation/carry-forward) retire from the SERVING path (whether the
price series survives as a QA cross-check is Andrew's call — Build-Ladder default: retire).
*Acceptance: served AUA ties vendor Assets values date-by-date with zero interpolated points;
rollback: the current chain unchanged beside it — NO shadow prefix, staged pre-port per the
no-shadow law.* *DS lane.*
**W-B · performance to raw** — C_02/D_00c consume the TWR dim; `growth` becomes vendor TWR;
`aua_change` stays as a plain balance delta (not presented as performance). *Acceptance: served
performance == vendor TWR to the basis point on a sampled book; Sharpe/Sortino stay EXCLUDED until
the INT-score gotcha (#2) is resolved with Orion.* *DS lane.*
**W-C · universe predicate** — `INFLECTION_REP_IDS` (hand-copied across ~28 sites, already
internally drifted) retires for a DERIVED predicate (the firm's full rep set from the
representatives endpoint, or Andrew's ruled scope) — one definition, one home. NOTE the pull
configs THEMSELVES are rep-scoped (`entityIds [3,11,12]` in the catalog — some copies stale vs the
ruled {3,6,10,11,12}); W-C sweeps those too. *Acceptance: a rep add/reassignment at Orion changes
NO code; the 07-31 event class becomes a no-op.* *DS+AE lanes.*
**W-D · point-in-time daily shape** — the daily run computes TODAY (+ vendor restatement window),
never re-derives history from a current-state snapshot; full re-derive becomes a deliberate,
guarded maintenance op. Kills the Sunday-erase class AND honors the ruled point-in-time semantics;
C_01's own comment has asked for exactly this since it was written. *AE (dispatch) + DS (script
invocation-axis) lanes.*
**W-E · snapshot union-preserve** — already routed to COO as the pre-08-16 durable item (F1) —
W-D's tactical precursor, not a substitute.

Sequencing: W-E before Sunday 08-16 (hard date) → W-0/W-C fast (small, kill the recurring breaker)
→ W-B (raw feed already landed; highest value-to-effort) → W-A (endpoint volume work) → W-D (the
architectural close). Each wave characterize→build-correct→port per the no-shadow doctrine.

## 4 · WHAT THIS SPEC DOES NOT DO

No TOs issued (CRO does not dispatch); no gate proposed beyond those already on record; the
must-calculate exception list awaits Andrew's authoritative set; nothing here touches tonight's
unstick, which stands on its own record (01_STOP_MECHANISM.md).
