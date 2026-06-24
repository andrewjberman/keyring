# DATA_ANALYTICS A1 — Transformation Ledger (v0.1: framing + method + bd-tree start)

**Deliverable:** DATA_ANALYTICS.A1 — the end-to-end transformation ledger (every gold-script → output → ADVI/MDPF consumer(s), tagged ESSENTIAL / AGNOSTIC-core / FIRM-SPECIFIC / DEAD-cruft). Foundation for the clean analytics-rebuild that kills the 49F-overfit (A2 distills → A3 firm-parameterized archetype → A4 parity-gated rebuild).
**Lead:** 0.4.0_DS_ClientPlatform · **Verify:** 3.0.0_SA_CVO (tags + FULL-census completeness) · **Arch-gate:** 1.0.0_SA_CTO (A3/cutover) · **Issued:** 2.0.0_SA_COO (DATA_ANALYTICS_PRD.md, sibling of DATA_PLATFORM)
**Status:** v0.1 — framing + method + bd-tree ledger START (reverse-ETL findings folded). The full multi-tree ledger + the load-bearing full-consumer-census = the build-out (paced for rigor).
**Inputs folded:** the DATA_PLATFORM reverse-ETL proof-of-method (BD-gold = mostly-repackaging; lots-FIFO = 49F-overfit-redundant [chunk-1 data-confirmed]; perf = self-owned-standard) + pipescript advi-bd/advi-cot/advi-inf/mdpf threads.

---

## 1. Method (rail-grounded; the load-bearing census is the high-stakes part)

- **Thread-analysis per gold-runner → ADVI/MDPF path, script-for-script:** `pipescript <thread>` (estate traversal) + `comp-pipescript io <script>` (per-script reads/writes + portal consumers) + `comp-blast <fn/artifact>` (downstream blast) + `comp-transform`/the graph for the FE consumers. NOT raw grep (rail).
- **Per script → output(s) → consumer(s) → TAG.**
- **The CONSUMER-CENSUS is LOAD-BEARING (the cot-C_02 destructive-removal lesson):** a FULL census — running-chain consumers (comp-blast) + DORMANT consumers (no running edge) + cross-val/validate scripts + dynamic/late-bound reads (grep ALL refs, classify hard/soft/fallback/dormant). The running-chain graph ALONE misses dormant consumers; a wrong DEAD-tag → a drop-list that silently degrades a LIVE served surface. **A DEAD tag requires a re-census = 0 consumers (incl dormant), not a 0-running-edge.**
- **Rule-22:** the v0.1 bd-tree tags below are INFERRED-from-the-reverse-ETL (hypotheses); each is CENSUS-GROUNDED before it can authorize an A2 drop. Tag = INFERRED until the full-census confirms.

## 2. Tagging schema

| Tag | Meaning | A2 disposition |
|---|---|---|
| **ESSENTIAL** | core analytics every firm's served surface needs (the value) | keep + generalize |
| **AGNOSTIC-core** | the firm-AGNOSTIC transformation (the reusable engine) | keep as the parameterized core (A3) |
| **FIRM-SPECIFIC** | legitimately per-firm (a firm declares a real dimension/need) | keep behind a per-firm capability flag |
| **DEAD-cruft** | redundant / overfit / superseded / unconsumed (the 49F-overfit class) | DROP (after full-census = 0 consumers) |

## 3. Scope inventory (the gold-runner threads to ledger — pipescript)

| Thread | Tree | Gold scope |
|---|---|---|
| advi-bd (19 threads) | bd / 49F | A_00..A_03 dims/positions, B_00..B_03 holdings/lots, C_00..C_04 canonical perf/nna, D_00..D_04 publishers, **26 E_* diagnostics** |
| advi-cot | cot | the cot fork (snapshot-native; A/B/C/D, no lots-FIFO) |
| advi-inf (14 threads) | inf | INF_* gold (Orion snapshot pass-through; the best-shape set) |
| mdpf | mdpf | the model-AUA convergent-feeder |

## 4. bd-tree ledger START (reverse-ETL-folded; INFERRED tags, census-pending)

| Gold script | Output | Consumer(s) (census-PENDING) | Tag (INFERRED) | Basis |
|---|---|---|---|---|
| A_00 accounts_dimension | gold/dimensions/accounts_dimension | ~all B/C/D | **AGNOSTIC-core** | the account dim — every firm |
| A_03 positions_cube | gold/timeseries/positions_cube | B_00/B_01 | **AGNOSTIC-core** | positions from custodian (Schwab-direct) |
| B_00 canonical_holdings | gold/canonical/holdings | B_02/B_03/C_02/D_04 | **AGNOSTIC-core** | the snapshot value (the reference shape) |
| **B_01 holdings_lots** | gold/timeseries/holdings_lots | **CENSUS-DONE: WIDELY CONSUMED** — D_00b/D_02/D_03/D_04 (publishers), C_01.canonical_nna, C_05.client_tax_liability, E_18/E_25 (diag), B_01b, A_03, + cross-val (validate_sl_nightly_gate, diag_gold_silver_recon, diag_sleeve_fix), + gold_validate/freshness_config, + dormant STAUDT diag | **AGNOSTIC-core — SUPPLANT-REROUTABLE (NOT dead)** | **TAG CORRECTED from v0.1 DEAD-candidate (the census caught the cot-C_02 trap).** chunk-1 proved the reconstruction is REDUNDANT-vendor-IP (its lot-tax data is re-sourceable from Schwab-direct), but it is LOAD-BEARING in the live graph → NOT droppable as-is; the clean rebuild RE-SOURCES its consumers from Schwab-direct lots, it is not deleted. **redundant-IP ≠ dead-unconsumed.** |
| B_02 canonical_lots | gold/canonical/lots_{realized,unrealized} | C/D tax intel | **AGNOSTIC-core** | Schwab-direct lots passthrough (chunk-1: essential, not overfit) |
| C_00 canonical_performance | gold/.../performance | C_03 | **AGNOSTIC-core** | standard Dietz-family, self-owned (chunk-4) |
| C_01 canonical_nna | gold/canonical/nna | D_* | **AGNOSTIC-core** | NNA (the trn_nna Schwab-flow now wired post-cutover) |
| C_02 client_performance | gold/timeseries/client_performance.parquet (+ cert/lock JSON) | **CENSUS-PENDING** (consumer-trace of the .parquet) | **PENDING (NOT dead)** | TAG CORRECTED from v0.1 DEAD-candidate: source has NO frozen/deprecated marker -- it's an ACTIVE assembler; my session-1 "frozen-06-09" was DATA-STALENESS, not script-death. pipescript --resource client_performance hits an IN-SCOPE inf thread (cross-tree). Needs the .parquet consumer-census before any tag. |
| C_03 account_performance | served firm-AUA keyer | D_00/D_01/D_04 + ADVI | **ESSENTIAL** | the served-AUA producer |
| D_00..D_04 publishers | platinum/firm/* + platinum/{advisors,clients,accounts} | ADVI portal | **ESSENTIAL** (firm-routing = FIRM-SPECIFIC-thin) | the served contract |
| **ALL bd E_* (the whole E_* group, ~E_18..E_25+)** | (manifests / diagnostics-prefix / DDB / dry-run-only) | **NONE — undispatched** | **DEAD-cruft (CONFIRMED, whole group)** | **DECISIVE (Andrew-direct test): `gold_dispatch.sh` invokes ZERO E_* (line 797: "Other ad-hoc diagnostic scripts live outside the dispatch") + no .sh/cron/systemd invoker anywhere (only own-docstring --dry-run self-refs). The E_* NEVER run in the live pipeline -> never feed the frontend.** Supersession note: the live new-securities classification is **B_01b** (dispatched), NOT E_18; E_18's bd-securities write doesn't happen nightly. The E_* are the accreted 49F-overfit diagnostic debt = the A1 clean-rebuild DROP-SET (retained only as ad-hoc manual diagnostics, irrelevant to the served analytics). |

## 4b. DECISIVE FINDINGS (rigorous trace, Andrew-direct 2026-06-24)

1. **The frontend-feeding gold-script set = exactly `gold_dispatch.sh`'s invocation list** (~30): A_00–A_04, B_00, B_01, B_01b, B_02, B_03, C_00–C_08, D_00, D_00b, D_00c, D_00f, D_01–D_04. These are the live nightly pipeline → portal. Everything not in this list does not feed the frontend.
2. **The ENTIRE bd E_* group is DEAD (undispatched).** `gold_dispatch.sh` runs ZERO E_* (explicit line 797: "Other ad-hoc diagnostic scripts live outside the dispatch"); no other .sh/cron/systemd invokes them. The E_* are ad-hoc manual diagnostics (run with --dry-run), the accreted 49F-overfit debt = the **clean drop-set** for the A1 rebuild. (Andrew called this; confirmed.)
3. **The PRIMARY essential-vs-dead test is the DISPATCHER, not per-script blast.** "Is the script in `gold_dispatch.sh`'s invocation list?" decides live-vs-dead in one query — simpler + more decisive than per-script comp-blast/DDB-tracing. Per-script census is for the SECOND question (among dispatched scripts, who consumes whom = essential/agnostic/firm-specific). Two-question method: (Q1 dispatcher) live-or-dead → (Q2 census) role-among-the-live.
4. **comp-tool GAP (Andrew predicted): no tool flags undispatched gold scripts as orphans.** comp-blast gives a running-chain lower-bound; pipescript threads don't even LIST the E_* (they're not threads). Nothing says "these N gold .py exist in the tree but `gold_dispatch.sh` never invokes them = orphan." **Proposed: a `comp-*` orphan-detector = (gold .py in tree) MINUS (gold_dispatch.sh invocation list) → the dead-script list.** Routes to CTO (comp-tool owner). This would have surfaced the whole E_* group in one call.

## 5. Build-out (the deep deliverable)
1. **Full bd-tree ledger** — every script comp-pipescript io'd + comp-blast'd; the DEAD-candidates (B_01, C_02, the 26 E_*) get the LOAD-BEARING full-consumer-census (dormant + cross-val + dynamic) before any A2 drop authorization.
2. **cot + inf + mdpf trees** — same ledger (cot is snapshot-native = inherently leaner; inf is the best-shape reference; mdpf the feeder).
3. **A2 hand-off** — the essential-transformation spec + the census-confirmed DEAD/cruft drop-list.

*v0.1 = framing + method + the bd-tree INFERRED-tag start (reverse-ETL-folded). The tags are hypotheses until census-grounded (Rule-22); the full-census is the high-stakes deliverable (a wrong DEAD-tag degrades a live surface — cot-C_02 lesson). RAVC2 COO+CTO; CVO verifies the tags + census-completeness.*
