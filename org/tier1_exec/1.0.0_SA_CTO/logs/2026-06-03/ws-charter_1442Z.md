# ws-charter — 2026-06-03 1442Z — bd advisor-timeseries dual-writer hardening ruling

**CLASS:** FIX (latent-bug hardening; architectural producer ruling). AE-domain Lambda fix.
**Trigger:** AE pipeline-ruling CC (`20260603T144140Z`) + DS W2b producer-ambiguity (`144015Z`). Surfaced via ADVI_FEREFI.W2b but threatens shipped functionality.

## Finding (AE root-cause)

Served `platinum/advisors/{id}/timeseries.json` ← D_04 pass-through of `gold/entities/advisors/{id}/timeseries.json`. That **gold key has TWO writers**:
- **D_02** — RICH, authoritative.
- **bd-portal-advisor-publisher `build_advisor_timeseries`** (:1147, async fan-out every publish) — SIMPLE, strict subset of D_02.

**LATENT CLOBBER:** masked today only by cascade ordering (D_04 reads D_02's fresh rich gold before the async publisher clobbers it). Any ordering where the publisher's gold-write precedes a D_04 read → served loses ALL rich fields → kills W2b `total_aua_fee_paying` AND the **already-shipped 49F NNA-mode `nna_canonical_fee_paying` toggle**. This is the ADVI_DWSPLT dual-writer incident class (known failure mode).

## RULING — GO on AE hardening; D_02 sole producer; standalone FIX-class; superset-proof gate

1. **APPROVED (architectural):** remove `build_advisor_timeseries` (:1147 call + fn) from bd-portal-advisor-publisher → **D_02 = sole gold producer** of bd advisor-timeseries; D_04 bridges gold→platinum unchanged. Eliminates the dual-writer. Single-writer principle.
2. **SCOPE = standalone hardening item, NOT folded into ADVI_FEREFI** feature PRD. Rationale: it protects shipped 49F NNA-mode functionality INDEPENDENT of #6, and it's a pipeline-architecture correctness fix (dual-writer elimination), a different class than the FE-refinement batch. FIX-class (latent-bug hardening) — no new PRD, no Andrew direction required. NOT a new project code (avoids HARD-BLOCK #7); AE authors as a hardening TO in AE/CloudOps domain.
3. **SAFETY CONDITION (HARD gate before cutover):** AE must PROVE D_02's `timeseries.json` is a TRUE SUPERSET of the publisher's `build_advisor_timeseries` output for ALL bd advisors — every field/row the publisher writes MUST be present in D_02's, else removing the publisher writer loses data. Field-diff (comp-pipescript io / served-parity) pre-cutover; CVO served-parity verify post-deploy. AE's "strict subset" assertion is the premise — this condition is the structural guard if it's wrong.
4. **DEPLOY DISCIPLINE:** Lambda change via Terraform only (Rule 1/2), safe-apply HALTGT (Rule 18), source-map (Rule 4), comp-pipescript deployed MATCH, comp-iam (expect no IAM delta — AE concurs), tag after 0-diff (Rule 6). 1-file Lambda change + redeploy.
5. **SEQUENCING:** land the hardening BEFORE or WITH W2b so the 49F AUM-split (`total_aua_fee_paying`) is born on the single-writer pipeline — do NOT add a 2nd clobber-vulnerable field. Hardening is justified on its own merits (protects shipped NNA toggle) regardless of W2b. Does NOT touch INF (INF publisher is sole-builder — different topology; DS's INF fix stays correctly in the Lambda; no INF rework).

## Follow-on

- Ruling → AE (authors + ships hardening TO on this GO) + CC COO (W2b sequencing + ADVI_FEREFI coordination).
- W2b (49F) unblocked architecturally: emit on the hardened single-writer pipeline. DS + AE coordinate the dispatch-path; superset-proof is AE's gate.
- INF #6 served-verified PASS (DS RAVC2 144015Z) — INF FE tail = next promote-bundle commit when RD lands the approx-drop.
- Manifest: 548c9d7d + b5d3e923 + 21be552d + (INF #6 tail imminent) + (W2b 49F, post-hardening) + (bd-timeseries hardening — AE, its own deploy). All promote-side HELD for Andrew GO.
