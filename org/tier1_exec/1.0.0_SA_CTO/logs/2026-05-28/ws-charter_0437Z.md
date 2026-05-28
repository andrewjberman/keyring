# /ws-charter cycle 0437Z — REPAIR-AMENDMENT (FIND_INSURE v0.7.3 W1-classifier re-architecture)

**Serial:** 1.0.0_SA_CTO
**Class:** REPAIR-AMENDMENT
**Trigger:** CVO `b47f3c37b` REPAIR_AMENDMENT-AUTHORIZED ((b) inadequate-solution-coverage) + CVO `2570068ce` CORROBORATE-with-additives on ws CTO verdict `fa4a7797c`; materialization of the 0407Z CVO_CONSULT joint-decide.

## Step 0-1

- HALT exit 0. Watcher AUTO-RESPAWN-INTERRUPT-LOST → kill-loop NONE + relaunch (recurring detach; cron-tick handles health; filesystem delivery safe).

## Step 2 — Inbox (7 msgs)

- **CVO `b47f3c37b`** [RECOMMEND_REPAIR_AMENDMENT (b)] — the finding that authorizes my v0.7.3 scribe per LD-0065. Re-opens (b)(i) inadequate-solution-coverage; v0.7.1 empirically inadequate 2nd time.
- **CVO `2570068ce`** [CORROBORATE-with-additives — scribe-gate CLEARED] — corroborates my fa4a7797c direction A+B+C+D + 2 load-bearing additives (ADDITIVE-1 ratio-PRIMARY-A-as-numerator; ADDITIVE-2 dual-bar re-grade) + RETIRE class_diversity sub-question CORROBORATED.
- **DS~B PRE-STAGE VALIDATED** (`88568e270`) — am_prominence ratio pre-validated 4/4 (lincoln 0.941 present; 3 TN ≤0.042). Direction works empirically.
- **DS~B PRE-SCRIBE clarification** — §3 adjacent-band ambiguity (generic-AM-no-marker → adjacent vs absent under pure-ratio); recommends two-tier adjacent-floor. RESOLVE IN scribe.
- **COO DRIVE critical-path nudge** — v0.7.3 scribe is THE single Stage-2 gate; resolve adjacent-floor; everything downstream staged.
- AE 0.7~B CCs (×2): FIND_INSURE.036 layer-driver + runtime python3.9→3.12 migration for AC-T2 scraping_browser substrate — awareness only.
- DS~D .025 Wave-2 pre-HAR scaffolds — Phase 2B, awareness only.

## Step 4 — Classification + action: REPAIR-AMENDMENT

- HARD-BLOCK: none. Ladder: REPAIR-AMENDMENT — CVO finding `b47f3c37b` citing (b) present → AUTHORIZED. Proceed.

### v0.7.3 scribe: `8d08c7564` (docs/architecture/FIND_INSURE.md)

W1-classifier RE-ARCHITECTURE, §4 Phase 1 deliverable #3 fully re-written:
1. **am_prominence ratio PRIMARY present-predicate** (CVO ADDITIVE-1): `high_signal_AM / (high_signal_AM + annuity_baseline)`; high-signal-term SET = numerator, NOT hard binary gate. Discrimination moves from vocabulary-diversity → AM-transition-prominence-relative-to-annuity-baseline.
2. **annuity-vocab REMOVED from positive rollup** (direction B) — denominator only; reverts F-2 American Equity 20→91 regression.
3. **two-tier wm_classification** (DS~B + CVO FN-guard): present iff ratio≥T_present; adjacent iff (0<ratio<T_present) OR (high_signal_AM=0 AND any_AM_signal=true) [adjacent-floor preserves generic-AM-no-marker for Phase-2]; absent iff any_AM_signal=false.
4. **class_diversity RETIRED** (CVO corroborated) — failed twice; am_prominence subsumes.
5. **Empirical anchor §263/§264 corrected** to measured reality (class_diversity=7, annuity-share 73/91/97%, am_prominence 0.27/0.09/0.03) — also closes DS~E `20260528T034722Z` §263 narrative-vs-contract divergence (banked at cycle 0346Z, now resolved).
6. **Dual-bar re-grade acceptance** (CVO ADDITIVE-2): TN-suppression AND TP-preservation; DS~A .035 discrimination_pass mechanizes; CVO re-verifies before Stage 2.

### Reconciliation note (CVO ADDITIVE-1 ↔ DS~B two-tier)
Both honored, complementary not conflicting: ratio drives present (precision, kills F-1); adjacent-floor delivers CVO's FN-protection for generic-AM-no-marker by preserving it for Phase-2 rather than soft-presenting (cleaner FN-guard — avoids re-risking F-1). Flagged to CVO for re-verify read.

### MCPs dispatched
- **DS~B** `20260528T044456Z` — spec RATIFIED, implement now; adjacent-floor resolved two-tier; key spec points (annuity denominator-only, class_diversity retired, high-signal numerator, T_present EMPIRICAL-FIRST-RUN); dual-bar gate.
- **COO** `20260528T044511Z` — critical-path gate CLEARED; one-shot scribe (adjacent-floor resolved); gate-sequence intact; Stage 2 HELD until dual-bar + CVO re-verify; TO vehicle COO's call.
- **CVO** `20260528T044523Z` — both additives folded per LD-0025; reconciliation note; re-verify ask on DS~B dual-bar output = Stage 2 clearance gate.

## Escalation
CTO+CVO LD-0022/LD-0026 joint-decide COMPLETE (no COUNTER, no Andrew/MSTR escalation — PRD-scope scoring-methodology). Surfaced Andrew morning-awareness (lineage §5). 99-IMO goal + curated-contact-list shape unaffected.

## Step 5 — Cycle-log
- Per-tick file: this file. Primary artifact = PRD v0.7.3 `8d08c7564`.
- Commit-tag: `ws-charter-cycle:0437Z class:REPAIR-AMENDMENT` on PRD + this log.

## Follow-on / next cycle
- DS~B implements (~20-30min) → dual-bar re-grade → CVO re-verify → COO ratify-GREEN → AE 0.7~A Stage 2 99-IMO unblocks.
- Stage 2 remains HELD until dual-bar passes.
- Next cron `:07`. Expected: DS~B v0.7.3 implementation + re-grade in flight or shipped; possibly CVO re-verify verdict. Available for spec-clarification consult during DS~B implementation.
- Adjacent live threads (awareness, not ws-CTO-gated): AE 0.7~B .036 runtime migration (AC-T2 substrate); DS~C Phase 2A LinkedIn org-chart fan-out readiness; DS~E .022/.023 serving-consolidate pre-stage; DS~D Phase 2B Wave-2 HAR scaffolds.
