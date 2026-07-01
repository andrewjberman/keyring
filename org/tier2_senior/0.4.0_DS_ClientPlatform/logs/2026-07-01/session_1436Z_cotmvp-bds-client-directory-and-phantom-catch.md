# 0.4.0_DS_ClientPlatform -- TAGATTR-gap fill: COTMVP-DS phantom catch + ADVI_COTMVP.B-DS cot client_directory emit

**archetype:** IMPLEMENT (secondary: DIAGNOSE, COORDINATE)
**window:** 2026-07-01 ~1416Z -> 1436Z (delta since session_1356Z)
**serial:** 0.4.0_DS_ClientPlatform | **branch:** CLOUD | **project:** ADVI_COTMVP (+ ADVI_COTETL grounding)
**driver:** COO /drive DRIVE (fill the ~14h TAGATTR external-gate gap with gate-clear cot-DS work; MSTR FOLD).

## HEADLINE
COO FOLD-routed a "COTMVP cot-DS leg" to my session. GROUNDED it = a PHANTOM (Rule 22 catch), then
found + built the REAL cot-DS gap DE surfaced: cot platinum/firm/client_directory.json emit. Code
LANDED + deployed + sha256-verified; artifact on the next cot nightly. Three stale-record catches this
cycle (MSTR + COO + CVO all independently credited).

## Rule-22 catch: the COTMVP cot-DS leg is a PHANTOM
COO's DRIVE (via MSTR FOLD) named a "COTMVP-B cot-DS DATA leg gated on the cutover." Grounded before
running: ADVI_COTMVP's only DS leg (D1, NMNC producer) was STOOD DOWN 2026-06-26 by MY OWN prior
grounding (PRD S5: "no 0.4.0_DS gold work on this PRD; that lane is freed"); "COTMVP-B" = the DE
FRONTEND /books display, not a DS DATA leg. Stale ADVI_COTMVP JSON (pod-0.4 phantom) fed the misread.
MSTR independently verified the grounding (Art. VIII) + fixed the JSON; COO fixed current_phase.
Also caught: ADVI_COTETL.ASSETSDIM-BACKFILL <status>active but footer = RECONCILED-COMPLETE 06-23
CVO-verified -> flipped to complete (stale status).

## The REAL leg built: ADVI_COTMVP.B-DS (cot client_directory.json)
DE took my offer -- COTMVP-B firm-level Clients roster (CottonwoodClientsSection, shipped DEV
07d5887f) renders EMPTY because opal-data-cot has no platinum/firm/client_directory.json. COO
owner-confirmed to me; DE sent the exact schema (TO cf4d23f01).
- IMPL: new build_client_directory() in cot D_04.client_portal_summary.py (main Step 11c, after
  build_clients_tab_slim). Reads gold/artifacts/clients_tab.json clients[] {key,name,aua} -> emits
  platinum/firm/client_directory.json {households:[{household_id,display_name,aua}]}. Folded into D_04
  (already reads clients_tab + writes platinum/firm/* on the nightly chain) -> no new SSM entry,
  firm-separated by construction.
- COMMIT/DEPLOY: bb2d62ef8; deployed opal-data-cot/code/gold/, VERIFIED sha256 cot-S3==HEAD cd1d95bd
  + build_client_directory grep-present in the deployed artifact. cot-tree only (bd D_04 MATCH,
  49F/bd zero-touch). ds-commit-gate clean.
- OFFLINE-VALIDATED vs served clients_tab (06-29): 218 households, 218 unique keys, all real names,
  finite aua, sum $433,839,378.94 reconciles to headline.total_aua $433,839,378.92.
- FLAGS to DE/CVO: count = 218 (not the TO's ~217; emit is faithful to clients_tab headline=218);
  one household aua=0 (finite/valid). GATE: lands on the scheduled nightly; comp-validate Phase-3
  post-nightly; NOT signaling safe yet.

## CLEANUP (ADVI_COTETL.CLEANUP) grounding (parked behind client_directory per COO)
- data/cot is a nested-repo/symlinked subdir of the MAIN repo (NOT a submodule): same branch CLOUD +
  same remote; changes commit via the normal parent cycle. Glob/find don't traverse it; comp-glob/Read do.
- Leg-1 delete targets C_00.py/C_02.py are ALREADY GONE from the cot gold tree (comp-glob C_0* =
  C_01/C_01b/C_01c/C_03..C_08). Leg-1 residual = D_00/D_00b/D_00c fallback-branch removal + de-chain
  (COO-scheduled, stage-only). Leg-2 ruff state still ungrounded (raw ruff hit a submodule path load
  error; use ds-commit-gate which handles it). Deprioritized behind client_directory.

## Compiler Tools
| Tool | Result |
|---|---|
| comp-glob (cot submodule-aware) | located cot gold C_0x scripts Glob/find couldn't (nested-repo) |
| comp-pipescript io D_04 (cot) | confirmed D_04 reads clients_tab + writes platinum/firm/ (insertion point) |
| comp-pipescript deployed D_04 | bd MATCH (defaults bd); cot verified separately by direct sha256 |
| ds-commit-gate.sh D_04 (cot) | clean (submodule path OK via the gate) |
| comp-which HUD | nudged throughout; native Read/Grep used for source-mechanism grounding (Rule 21/22) |
Rail-checked raw aws for served-artifact JSON-shape + cot-S3 code verify (no comp-tool dumps a served
artifact's schema / a bronze xlsx row count). Offline transform unit-tested vs the real clients_tab.
