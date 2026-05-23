# CVO Priority-Corroboration Verdict — LD-0024 — 2026-05-23 ~18:01Z — **CORROBORATE Path B** with one operational footnote

**Charter:** MSTR LD-0024 (active), supersedes LD-0023. VALFIN-001 Phase B three-branch reclassified OPERATIONAL → ARCHITECTURAL per v1.6. Andrew sovereign surfacing in flight; if Andrew non-responsive past CY-0042, CVO becomes priority corroborator under LD-0022 + v1.6.

**MSTR's draft recommendation to Andrew:** **Path B (fee-STATUS bools post LD-0018 F1 fix)**. Rationale: best signal-availability tradeoff; Path A months-block exceeds D-001 throughput; Path C forecloses fee dimension without product justification.

**CVO verdict:** **CORROBORATE Path B.** One operational footnote (FN-1) for the materialization TO; one META consideration for Andrew's call (M-1).

---

## Verify-channel under MECHANICAL / NOVEL / META

### MECHANICAL

Path B requires INF_C_09 audit table consumable by Phase B/C portal type swap, post LD-0018 F1 fix:
- INF_C_09 audit table EXISTS / FRESH / SCALED / NOT-FROZEN per direct probe today 2026-05-23T15:30Z (LD-0018 verify-channel; `s3://opal-data-inf/gold/views/fee_status_audit.parquet`, 16,073 bytes, 867 rows × 8 cols, last refresh 10:31Z, in `CHAIN_GOLD_C` + `CHAIN_FULL` per `orion-gold-dispatch.sh:163,219,228`).
- F1 fix in flight via VALFIN.010 (DS, COO charter `9f68a6cd3`, GO'd 15:16Z). Required for correctness.
- Consumer wiring required: zero downstream consumers today per grep (`fee_status_audit` / `first_known_fee_status` across `data/`, `infra/aws/lambda/`, `portal/src/`); Phase B/C consumer is the materialization scope.

**MECHANICAL: GREEN** — viable post-F1-fix + consumer-wiring.

### NOVEL

Empirical state today (LD-0018 probe results):
- 867 accounts in audit. 532 (61%) carry false `first_known_fee_status_date=2023-05-25` due to F1 placeholder-zero pollution. Post-F1-fix expected: those 532 either shift to a real first-known date (e.g., 2026-04-01) OR get filtered out as never-billed.
- **Post-fix audit population may shrink** (sharpest-test-bind): the 532 placeholder accounts include both genuinely-never-billed and "I haven't seen them yet in real data" — depending on F1's filter shape, the audit may settle at ~535 accounts (only those with `fee_amount > 0` ever observed) or stay at 867 with corrected dates. Either is acceptable for Path B; consumer must handle either.
- 69% of accounts (598/867) have `has_state_changes=True`. Path B's hold-status assumption violates for the majority of the audited population — meaning the pre-Apr-2026 hold-backward is a known approximation. This is acceptable for Phase B/C **only if** the portal type swap displays an explicit "since [date]" floor OR explicit "imputed" flag for pre-`first_known_fee_status_date` periods.

**NOVEL: GREEN with caveat** — viable; consumer-side display contract must acknowledge the hold-backward imputation explicitly.

### META

Three META layers tested:

1. **D-001 throughput discipline:** Path A months-block fails; Path B hours-block passes; Path C unblocked. Path B = minimum-block satisfying throughput discipline. **PASS.**

2. **Andrew product invariant — minimum-viable-fee-dimension:** Path C forecloses the fee dimension entirely (no fee signal anywhere in Phase B/C). MSTR's framing "without product justification" is correct: defaulting to forecloseure is over-shrink in the opposite direction. Path B keeps fee STATUS without committing to fee VALUES. **PASS** for minimum-viable-fee-dimension respecting Andrew's chartered fee-data product surface.

3. **Reversibility ordering:**
   - Path B → Path A: forward-extensible when Orion Advisory Fees feed lands. Add fee VALUES to existing fee STATUS consumer; consumer schema extends, no destructive change.
   - Path B → Path C: reversible — drop the fee-status consumer wiring later if product invalidates.
   - Path A → Path B: NOT reversible without strong reason (downgrading richer signal to coarser is product-debt).
   - Path C → Path A or B: reversible but requires net-new consumer build.
   
   Path B has **the best reversibility position** of the three. **PASS.**

**META: GREEN.**

---

## Footnote FN-1 (operational, for materialization TO)

When LD-0024 materializes (whichever lane: DS or AE picks up the consumer-wiring scope for Phase B/C), the materialization TO should explicitly include:
- Sequencing: F1 fix MUST land before consumer goes live (else 61%-wrong-data ships). VALFIN.010 closure is the gate; CVO will signal when re-probe confirms.
- Display contract: consumer must surface "imputed" flag OR "data since [first_known]" floor for pre-`first_known_fee_status_date` periods. The 69% has-state-changes population means silent display of the hold-backward bool would mislead.
- Audit-table population shift on F1-fix-landing day: documented expectation so consumer doesn't trip on count drop.
- INF_C_09 docstring update from F2 (c) PHASE-2-STAGED materialization TO already in COO's lane: should now reference the Phase B/C consumer as the planned wiring (no longer purely Phase-2-staged-for-future).

## META M-1 for Andrew (one consideration the recommendation should surface)

Whether Phase B/C **actually consumes** fee-status bools is an empirical question the recommendation chain hasn't answered. The LD-0018 META-3 framing was "DS or COO should clarify which class Phase B/C falls in." If Phase B/C is empirically fee-independent (a possible case nobody has verified), Path B materializes unnecessary work. Suggested addition to Andrew's surface: "Confirm Phase B/C portal type swap consumes fee-status bools — or charter empirical-consumption-probe before materialization."

Andrew may know this already (he has end-to-end product context); this is the META check, not a counter to Path B.

---

## Verdict

**CORROBORATE MSTR's Path B recommendation** under verify-channel discipline. GREEN at MECHANICAL / NOVEL (with caveat) / META layers. Footnote FN-1 + META M-1 as enhancement, not counter.

Standing by for either (a) Andrew adoption + materialization, OR (b) Andrew overruling with Path A/C — corroboration ready for either case.

— 3.0.0_SA_CVO
