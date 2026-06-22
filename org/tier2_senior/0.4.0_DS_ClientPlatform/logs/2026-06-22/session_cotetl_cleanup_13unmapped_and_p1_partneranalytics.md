# Session 2026-06-22 ~1700-2035Z — COTETL cleanup + 13-unmapped investigation + P1 partner_analytics launch-blocker — 0.4.0_DS_ClientPlatform

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, DEPLOY, VALIDATE, COORDINATE

## Window
Continuation after the C00SNAPSHOT served-AUA fix (prior log session_cotetl_c00snapshot_servedaua_p0.md).
Three threads: (1) Andrew-direct 13-unmapped quantitative investigation; (2) ADVI_COTETL.CLEANUP (Leg-2
ruff + Leg-1 dead-path retire) incl a landed-not-staged correction; (3) the dominant one -- a P1 LAUNCH-BLOCKER
(cot partner_analytics absent) driven to a live, reconciling, ledger-closed artifact. ~40 MCP exchanges
(CTO/COO/CVO/DE/AE). Held verify-on-served + Rule 22 throughout; 0 false-fixes.

## THREAD 1 — Andrew-direct 13-unmapped investigation (quantitative, CVO-verified to the cent)
Hypothesis (Andrew): the served $395.30M(694)-vs-canonical $397.31M(707) gap = a snapshot-vs-transaction
DELAY. VERDICT = DIRECTIONALLY CONFIRMED, mechanism EXACT, one refinement:
- MECHANISM (source-confirmed): relationship_id is TRANSACTION-DERIVED (A_00.accounts_dimension.py:5-7,69,76
  builds accounts_dimension from silver/transactions). The holdings-snapshot (canonical_holdings<-B_00) is a
  SEPARATE feed. C_03 LEFT-joins the dim -> holdings-present + txn-absent = unmapped.
- QUANTIFIED: 13 unmapped ALL first-appeared in the snapshot ~06-11 (680@06-09 -> 707@06-11), ALL absent from
  accounts_dimension (0/13). Composition: 6 newly-entered "Investor Manual Asset" accts (Home $1.3M/LLC $300K/
  Joint $100K/3x IRA = $2,013,374) + 7 newly-opened empty CASH accts ($0) = the EXACT divergence.
- REFINEMENT: NOT a feed-wide lag (silver/transactions current to 06-22, AHEAD of holdings 06-18) -- a
  per-NEW-account recording lag. resolve-vs-persist = INFERRED (forward-watch ~1wk), NOT claimed-proven.
- CVO independently reproduced to the cent (705/$397,313,612.21 - $2,013,374.15 = $395,300,238.06). Closed
  the confirm-the-13 residual. See [[reference_cot_aua_freeze_localization_consolidated_orphaned_holdings_asofdate_keyed]].

## THREAD 2 — ADVI_COTETL.CLEANUP (Leg-2 ruff + Leg-1 dead-path retire)
- Leg-2 (5d43b4304): C_01 per-class ruff cleanup (1 unused import + 7 f-prefix; manual, NOT --fix) -> retired
  the RULE15 gate-note bypass, C_01 ds-gate now clean, byte-identical.
- Leg-1 RETIRE (CTO-ruled RETIRE not WIRE): staged (475d3bcc5) -> AE de-chained C_00/C_02 from opal-cot-gold-run
  (7240a8933, I live-verified) -> DS landed AFTER: D_00/D_00b client_performance fallback -> FAIL-LOUD raise
  (1703ac61d, structurally proven no-silent-return) + DELETE C_00/C_02 scripts (bba478b66). ds-delete leg
  CLOSED (AE 8f1ded9a8).
- **CORRECTION incident:** CTO HALTed the retire believing it was staged-not-committed; I corrected (it was
  LANDED) + ground-truthed harm CONTAINED (artifact gold/client_performance.parquet persists [scripts deleted
  not data] -> C_04 doesn't hard-exit; C_02 was already frozen-06-09). CTO independently verified -> PROCEED-not-
  restore. Census lesson banked: [[reference_destructive_artifact_removal_needs_full_consumer_census_not_running_chain_graph]]
  (the pre-gate missed D_01 dormant + C_04 validate; census > graph for destructive removals). Multi-leg rewire
  (Leg-1 D_01 done; Leg-2 C_04->C_03; Leg-3 cross-vals; Leg-4 re-census + artifact-removal) -- non-urgent.

## THREAD 3 — P1 LAUNCH-BLOCKER: cot partner_analytics (the dominant thread)
Distribution tab rendered EMPTY because cot partner_analytics didn't exist. Scope-confirm (Rule 22, before any
emit) caught it was NOT a path-redirect but a SNAPSHOT-REWIRE + a D_01-never-runnable-for-cot port:
- D_01's PRIMARY AUA input = client_performance (C_02, the cleanup-retired dead path, frozen 06-09); D_01 was a
  DORMANT consumer the running-chain graph missed (the cleanup-coupling). Same bd-fork-shadow root as the
  served-AUA freeze.
- FIX (CTO-confirmed): `_derive_relationship_perf(acct_perf)` aggregates account_performance (C_03 snapshot) to
  relationship-grain, replacing C_02 (78b7b9132). VERIFIED: relationship total_aua=$395,300,238 TIES EXACTLY to
  the certified firm-AUA (correctness proof); ref_date 06-09->06-18; exact-schema drop-in; all-taxable matches C_02.
- LAUNCH-EMIT (path a, Andrew-authorized today): added direct platinum/firm write (e71e5a2ae). The emit then
  surfaced 3 D_01 cot-runnability gaps (D_01 never ran for cot), fixed iteratively (244974718): rel_architect_lookup
  absent -> derive from accounts_dimension; account_team fallback missing relationship_id (latent bug); empty-ap_day
  guard for cot's short-history (data starts 04-22) trailing quarters. Emit SUCCEEDED + DS-verified-on-served:
  platinum/firm/partner_analytics_{q,m,a} data_as_of=06-18, metrics tie $395.30M, header firm-AUA UNCHANGED.
- DE render-finding -> geo-reconcile (c5bc7ba49): added explicit "Not state-attributed" donut segment ($24.49M/
  6.2%) + reconciled segment %s + donut.total to the FIRM total. Donut now sums to $395,300,238 on-view (was
  state-only $370.8M); TX=82.0%.
- gate#2 CLOSED (CVO 4-criteria + DE render PASS). Ledger cotetl-d01-partneranalytics-launch-emit CLOSED
  (0d8359230, all 4 legs). Allow-list RULED OUT (index.mjs:179 = S3-status passthrough; the 403 was S3-missing-
  key-AccessDenied). See [[project_cot_served_aua_snapshot_perf_branch_c03_c01_not_lots_fifo]].
- FAST-FOLLOW grounded SIMPLER (Rule 22): D_04.build_partner_analytics (D_04:1878-1922) IS the cot publisher
  (reads gold/artifacts/partner_analytics [D_01] -> writes platinum/firm) + already chained. So fast-follow =
  CHAIN-ONLY (AE adds D_01 BEFORE D_04; no separate publish). In flight (AE-led, time-sensitive <02:00Z).

## Files Modified (see commit messages)
5d43b4304, 475d3bcc5, 1703ac61d, bba478b66, 2485ad4da, 78b7b9132, e71e5a2ae, 244974718, c5bc7ba49, 0d8359230.
Primary: data/cot/scripts/gold/D_01.partner_analytics.py (rewire + 3 cot-runnability fixes + geo-reconcile +
launch direct-write); D_00/D_00b (fail-loud); C_00/C_02 (deleted); C_01 (ruff). 49F/bd UNTOUCHED (firm-sep).

## Compiler Tools
| Tool | Where | Result |
|---|---|---|
| comp-blast | C_00/C_02 (Leg-1 pre-gate) | PARTIAL -- showed D_00/D_00b but MISSED D_01(dormant)+C_04(validate) -> the census lesson |
| ds-commit-gate.sh | C_01/D_00/D_00b/D_01 (per edit) | PASS all (C_01 retired the RULE15 bypass) |
| deploy_ledger.py | open/close-leg/close cotetl-d01-partneranalytics-launch-emit | PASS -- 4 legs proven, CLOSED |
| safe-deploy hook | D_00/D_00b/D_01 -> opal-data-cot/code/gold | PASS -- DEPLOYED [cot] + md5/etag MATCH |
| md5/etag verify | deployed D_01 == c5bc7ba49 (chain-runs-this) + C_02-artifact-present | MATCH (rail-checked; cot comp-pipescript Unknown) |
| Grep/Read (source-ground) | A_00/D_04/index.mjs/D_01 -- mechanism + publisher + allow-list | the Rule-22 groundings (transaction-derived dim, D_04-publisher, S3-403) |

- **What worked:** scope-before-emit (Rule 22) caught the snapshot-rewire + the cleanup-coupling + the stale-emit
  trap before shipping; the $395.30M exact-tie as the rewire correctness proof; reading D_04/index.mjs source to
  simplify the fast-follow (chain-only) + rule out the allow-list.
- **What failed/banked:** the Leg-1 retire pre-gate (comp-blast running-chain graph) missed D_01(dormant)+C_04 ->
  census-not-graph lesson; D_01 was never runnable for cot (3 latent cot-gaps surfaced only on the emit).
- **Gap found:** D_01-for-cot was an unported bd/inf-shaped script; the C_02 artifact must persist until a complete
  re-census (C_04 hard-exits without it).

## Blockers
None. P1 RESOLVED + ledger CLOSED. C_02 artifact-removal GATED on the re-census (hard guardrail, not a blocker).

## Current State (handoff)
- cot partner_analytics LIVE: platinum/firm/partner_analytics_{quarterly,monthly,annual}.json, data_as_of=06-18,
  reconciles to $395,300,238 (geo donut incl "Not state-attributed" $24.49M slice). Header firm-AUA $395,300,238.06.
- D_01.partner_analytics.py (deployed == c5bc7ba49): rewired off C_02 -> derives relationship-perf from C_03;
  still writes the direct platinum path (launch-expedient, to be removed after the chain confirms D_04-publish).
- gold/client_performance.parquet (C_02 artifact) persists frozen-06-09; C_00/C_02 scripts deleted + de-chained.
- Open ledger: cot-cleanup-dechain-deadperf (AE, nightly-verify tomorrow).

## Next Steps
1. **[0.7.0_AE_CloudOps]** chain D_01 into opal-cot-gold-run BEFORE D_04 (<02:00Z); **[self]** verify-on-served the
   chained nightly (D_01->gold/artifacts->D_04->platinum reconciles, fresh date) + remove the redundant D_01 direct-write.
2. **[self/non-urgent]** C_02 multi-leg rewire Leg-2 (C_04.validate_aua -> C_03) + Leg-3 cross-vals + Leg-4 re-census + artifact-removal (ledgered).
3. **[2.0.0_SA_COO]** polish-backlog: Unassigned 0-accounts cosmetic + state-attribution coverage. **[self]** ETFS_AVGCAP-W1 on AE's ETFS-W1 producer signal.
