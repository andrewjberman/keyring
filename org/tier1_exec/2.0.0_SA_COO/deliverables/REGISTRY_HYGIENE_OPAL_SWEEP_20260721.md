# Registry-Hygiene Sweep -- OPAL macro (2026-07-21)

**Lane:** 2.0.0_SA_COO~A (Andrew-direct registry-hygiene AUDIT lane; MSTR brief 20260721T154847Z).
**Instrument gate:** `comp-state --self-test` = PASS 3/3 (instrument discriminates BEHIND/CURRENT/QUIET). comp-state is a RECALL linter -- BEHIND = a place to look, not an auto-edit; I am the precision layer.
**Grounding bar (Rule 22, HARD):** "no work remains" grounded on commits + TO status + served/live artifacts, NEVER the registry's own say-so. A close is a real state change; UNCERTAIN/non-obvious closes are FLAGGED, not made.
**Enumeration:** 14 OPAL_* project JSONs (`ls org/projects/OPAL_*.json`), all parse clean.

## Disposition table

| Project | Registered? | TO drift | Remaining work / disposition | Flag |
|---|---|---|---|---|
| OPAL_CONSOLIDATION | OK (active, CTO) | 1 pending TO -- NOT touched (DND) | **DND -- live P0 wave.** Real work remains: nightly #2 read, P0 acceptance census re-run, Wave-3 exec, serve-lift bundle, WP8 schwab decommission. LEAVE ACTIVE. | -- |
| OPAL_TAXSMA | OK (active, DS) | none | **DND.** Remaining: daily-schedule arch decision w/ Andrew, /tax-pt3 write path, Yang 07-01 swap ack. LEAVE ACTIVE. | -- |
| OPAL_TAXSMA_PT2 | OK (active, CTO) | 2 active TOs -- NOT touched (DND) | **DND.** PRD authored, 6 workstreams (WS-1 bronze..WS-6 read) for COO decomposition. LEAVE ACTIVE. | -- |
| OPAL_TAXSMA_REGISTRY | OK (active, CTO) | 5 active TOs -- NOT touched (DND) | **DND.** PRD authored, 5 WS TOs (registry+seed, resolver, ETL-reads-registry, /tax-newacc, gateway IAM). LEAVE ACTIVE. | -- |
| OPAL_ASSETS | OK (complete-as-superseded -> OPAL_CONSOLIDATION; note+field coherent) | **9 open TOs (2 ACTIVE/7 PENDING): C5/C6/C7/C10/C11/V2-5/V2-8/V2-9/P0-A** | These are the LIVE consolidation-wave build items under a superseded code. NOT closed (consolidation-adjacent = DND-adjacent; closing needs per-TO commit grounding). | **FLAG-1** |
| OPAL_ASSETS_49METATABLES | OK (complete-as-superseded -> OPAL_CONSOLIDATION; superseded_by+note coherent) | none open | Correctly superseded. Phase text is historical (D1-in-build) -- authoritative status+superseded_by are clean. No edit. | -- |
| OPAL_RUNNERS | OK (complete-as-superseded -> OPAL_CONSOLIDATION; superseded_by+note coherent) | none open | Correctly superseded. Phase "BUILD OPEN" is historical; work lives under CONSOLIDATION. No edit. | -- |
| OPAL_STNDRD | **FIXED** (superseded-into-OPAL_TAXONOMY) | none open | Status string declared the supersession but structured `superseded_by` was ABSENT + `updated` stale (07-15 vs the 07-17 fold). **EDIT:** added `superseded_by: OPAL_TAXONOMY` + `superseded_note`, bumped `updated`->2026-07-21. Grounded on the record's own `current_phase` (07-17 Andrew-direct fold; ph3/ph4 carried into TAXONOMY DC-queue; driver 0.8.0_AE_CloudComp~B). | FYI-CTO |
| OPAL_GLDRNS | OK (active, CTO) | 1 pending TO | Active build. Remaining: Wave-3 TO cuts at CTO (queued behind P0 census); ~C tax-cell fix + --full rebuild sequenced. LEAVE ACTIVE. | -- |
| OPAL_LCLRPO | OK (active, MSTR) | none open | Active. Remaining: P1 batch execution PARKED on CTO v4 split-runner ruling (commit-gate argv-overflow at 567 files); yang_pkl = ARCHIVE-not-delete rec at Andrew; BBGTML B5 gates retire-with-provenance. LEAVE ACTIVE. | -- |
| OPAL_TAXONOMY | OK (active, CTO) | none open | Active, registered 07-17. Remaining: CTO dispositions on 14 DCs (DC-1..DC-14) -> DC-* lints; awaiting driver spawn. LEAVE ACTIVE. | -- |
| OPAL_TICKET | OK (P0 SHIPPED; owner 0.5.0_AE_OpalETL~A) | none open | **Close candidate -- VERIFIED NOT clean-closeable.** P0 shipped+live (ticket-center-v1.0.0, portal /ticket-center, reachability closed). But the record's own roadmap has **P1 (cutoff/EOD sweeps + Teams/SES claim links + escalations) -> P2 (AI intake) -> P3 (external filer visibility)** as in-scope phases + 3 open human items (cutoff from AJ, bobby@ confirm, external visibility timing). Real scope remains. LEAVE ACTIVE. | **FLAG-2** |
| OPAL_PORTALREFRESH | OK (SHIPPED-LIVE v2.1.137; CTO) | none open | **Close candidate -- build 100% shipped+live** (FE_01 + BE_01 v2.3.0, PROD f11c15a1, CI success). Residual = acceptance tail: F4 formal acceptance (first REAL portal action writing a real-email history row; DT watches) + Andrew's call on attributedTo annotation + DT lane-grant question at COO. LEAVE ACTIVE pending F4. | **FLAG-3** |
| OPAL_BBGTML | OK (active; TOOL FULLY PROVEN LIVE) | none open | **Close candidate -- tool proven-live** (both PKLs staged + ListObjectsV2-verified; substitution closed). Remaining = **B5**: Alyssa's first real /bbg-pull (fresh vintage) + confirm-gated real send + her conda-env/template-path confirms. Human-gated. LEAVE ACTIVE pending B5. | **FLAG-4** |

## FLAGS to MSTR + base COO (+ CTO where noted)

- **FLAG-1 (OPAL_ASSETS, -> CTO):** superseded-into-CONSOLIDATION but still carries **9 open TOs** (C5/C6/C7/C10/C11/V2-5/V2-8/V2-9/P0-A) that ARE the live consolidation-wave build. I did NOT close them (DND-adjacent; per-TO commit grounding required). **Rec:** CTO dispositions these as the consolidation wave completes -- either mark complete-as-superseded per shipped commit or migrate the tracker under OPAL_CONSOLIDATION so a superseded code stops carrying open work.
- **FLAG-2 (OPAL_TICKET, close candidate):** P0 grounded-shipped, but P1-P3 are the project's own in-scope roadmap + 3 human-gated items. **Rec:** keep ACTIVE through P1-P3, OR (cleaner) close the P0 milestone and respawn P1-P3 as a new project code -- MSTR/Andrew's call; I did not close.
- **FLAG-3 (OPAL_PORTALREFRESH, close candidate):** build shipped+live+verified; only the F4 formal-acceptance gate (pending a first real portal action) + 2 human decisions remain. **Rec:** base-COO/DT close it the moment F4's real-email history row lands and Andrew rules the annotation.
- **FLAG-4 (OPAL_BBGTML, close candidate):** tool proven-live end-to-end; close gates solely on B5 (Alyssa's first guided real pull + confirm-gated send). **Rec:** keep ACTIVE until B5; Andrew/Alyssa-paced.
- **FYI-CTO (OPAL_STNDRD):** made the mechanical `superseded_by` + `updated` alignment above; no substantive change (the fold was already declared in status + current_phase). Residual ph3/ph4 already recorded as carried into OPAL_TAXONOMY -- no action needed.

## Net
- **Registry integrity:** 14/14 parse clean; owner-less schema on BBGTML/49METATABLES is by design (pods/authority), not a defect.
- **Edits made:** 1 (OPAL_STNDRD structured-field alignment; grounded, non-substantive).
- **Closes made:** 0 -- the 3 "strong close candidates" each verified to carry a real (mostly human-gated) residual; closing any would violate the grounding bar.
- **Flags raised:** 4 (+1 FYI).
