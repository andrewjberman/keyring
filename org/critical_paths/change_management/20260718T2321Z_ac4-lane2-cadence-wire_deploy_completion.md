# Deploy Completion Record
**Date opened:** 2026-07-18T23:21:02.155106+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260718T234455Z
**Deploy:** AC4 lane-2 co-land: --live-cadence CSE coverage-leg in the nightly derive (additive, no quiesce) -- commit + ONE rebuild (bakes lane-1 cse_schema + lane-2 derive leg)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | derive_runner.py AC4 coverage-leg CLOUD commit | pushed hash + pre-rebuild baked-file git-status clean | b45006995 pushed CLOUD clean FF bfc1af27d..b45006995 (derive_runner.py AC4 coverage-leg). PRE-REBUILD baked-file git-status: ALL 22 Dockerfile-COPY sources + Dockerfile/buildspec CLEAN except the single expected derive_runner.py (now committed) -- cse_schema.py @b7daead4f (lane-1) + summary_corpus.py @784c9a36a (~D PH2) both committed-clean. commit-gate PASS, offline smoke PASS. Image bakes committed code only. | CLOSED 20260718T232235Z |
| L2 | activation | ONE derive-image rebuild | CodeBuild SUCCEEDED + sha-in-container (derive_runner + cse_schema both baked) | ONE rebuild bakes BOTH lanes: CodeBuild globgrph-derive-build:6ff975cd SUCCEEDED -> :latest. SHA-IN-CONTAINER (Rule 22a, task 5abed0aef1d24cccaad0847b31b4adf4 exit 0, no graph write): sha256(/app/derive_runner.py)=5ad5f650...68a9 == local HEAD EXACT (lane-2 AC4 leg); sha256(/app/org/modules/graph/cse_schema.py)=daa5ead2...7e1e == local HEAD EXACT (lane-1 @b7daead4f); CSE_AC4_LIVE_COVERAGE present (3x) + assert_live_coverage def present (1). Both lanes confirmed baked. | CLOSED 20260718T232834Z |
| L3 | verify | exercise the cadence leg in a real derive | controlled derive run -> CSE_AC4_LIVE_COVERAGE line (all mapped, live inventory, lane-1's 4 mappings resolve) | Cadence leg EXERCISED in a real derive (task e82503d0, exit 0 -> NESSIE_COMMIT + MARKER nodes_snap=1690633238494083953 + DERIVE_RUNNER_COMPLETE): CSE_AC4_LIVE_COVERAGE ran against the live in-memory inventory -- node_types ALL MAPPED (lane-1's 4 mappings resolved those), and CAUGHT 2 unmapped edge_types (IN_SUBNET, SENDS_TO) on its FIRST run = the at-appearance detection working. Additive/best-effort (WARN, derive committed cleanly). The leg reads RAW graph_edges semantics (matching cse_emit_graphhead.py:152 which _scan's graph_edges directly), so it is the CORRECT axis -- the 2 edge types are real gaps the CSE producer skips. FOLLOW-ON finding routed to COO (governed edge-mapping + lane-1 projected-vs-raw axis correction). | CLOSED 20260718T234454Z |

## Log

- 20260718T232102Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260718T232235Z LEG L1 closed: b45006995 pushed CLOUD clean FF bfc1af27d..b45006995 (derive_runner.py AC4 coverage-leg). PRE-REBUILD baked-file git-sta
- 20260718T232834Z LEG L2 closed: ONE rebuild bakes BOTH lanes: CodeBuild globgrph-derive-build:6ff975cd SUCCEEDED -> :latest. SHA-IN-CONTAINER (Rule 22a,
- 20260718T234454Z LEG L3 closed: Cadence leg EXERCISED in a real derive (task e82503d0, exit 0 -> NESSIE_COMMIT + MARKER nodes_snap=1690633238494083953 +
- 20260718T234455Z CLOSED -- all 3 legs proven
