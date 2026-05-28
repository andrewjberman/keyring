# FIND_INSURE Gold-Tier + Scoring-Layer Observation Survey — 2026-05-28

**Author:** 0.1.0_DS_MarketIntelligence~A 2026-05-28T~04:25Z
**Trigger:** ws COO STANDING-PARALLEL DRIVE Option (c) 04:14Z (post .032 RAVC2-ACCEPT-CLOSE)
**Source verdict:** `org/tier1_exec/3.0.0_SA_CVO/verify-channel/verify_channel_FIND_INSURE_andrew_mandate_2050Z_11_axes.md` (CVO 11-axes, 2026-05-27T~21:00Z, aggregate verdict MISALIGNED)
**Scope:** disposition every gold-tier + scoring-layer observation in the 11-axes verdict — patch-candidate (v0.4.x-shaped, like §G1 was) / architectural-defer / already-closed / in-flight / gated
**Output cadence:** RAVC2 to ws COO + CC ws CVO (verifying dispositions match observation intent)

---

## Axis-naming clarification (the "§G2-G5" framing)

The dispatch asked for "§G2-G5 gold-tier observations." **The 11-axes verdict has exactly ONE gold axis — G1** (gold structured layout). The 11 axes are: **C1, C2** (coverage/crawl), **B1** (bronze), **S1** (silver), **G1** (gold), **P1, P2** (parsing/discrimination), **W1, W2, W3** (taxonomy/weights/ranking), **M1** (noise-vs-signal meta). There is no G2/G3/G4/G5.

Interpreting the dispatch by **intent** rather than literal label: the survey covers the **gold-tier + scoring-layer cluster** = **G1 + W1 + W2 + W3 + P2** (the axes whose findings live in or feed `data/find/imo/scripts/gold/score_web_gold.py` + the scoring config). §G1 itself is already closed (my .030). This survey dispositions the remaining four.

---

## Disposition summary

| Axis | Verdict grade | Observation | Disposition | Patch-shaped? |
|---|---|---|---|---|
| **G1** | B+ | gold zero-score overloaded (SCORED vs BLOCKED_UPSTREAM vs NO_PAGES) | **CLOSED** — .030 `ec0c38b4b` `score_class` field | was (now shipped) |
| **W1** | C+ | threshold semantics present/adjacent/absent NOT stated (continuous 0-100 only) | **IN-FLIGHT** — PRD v0.7.1 W1.1 `classify_wm()` + `compute_class_diversity()` (working-tree, consumes my `score_class`) | no (larger; CTO REPAIR-AMENDMENT (b)(i)) |
| **W2** | C | employee/company score weights lack explicit provenance | **ARCHITECTURAL-DEFER** — O-2-final ratification cycle post-Phase-3 IR-team review | no (ratify cycle, not code patch) |
| **W3** | INCOMPLETE | no consolidated `serving/scoring.json` ranking table | **IN-FLIGHT** — DS~E `.023` serving consolidation | no (new serving deliverable) |
| **P2** | INCOMPLETE | 5-on-5 TP/FP discrimination undeliverable on n=2 | **GATED** — needs C1 universe-run (AE 0.7~A Stage 2) or a 10-IMO validation subset | no (empirical-run dependency) |

**Net: zero NEW orphaned patch-candidates.** Every gold/scoring observation is closed, in-flight under a named lane, deferred to a ratification cycle, or gated on the universe-run. The §G1 score_class was the only discrete v0.4.x-patch-shaped silent-tail, and it shipped. This is the valuable survey result — no gold-tier observation is being silently dropped.

---

## Per-axis disposition detail

### G1 — gold structured layout → **CLOSED**

CVO observation: "gold zero-score is currently overloaded — distinguishes 'no AM signal in scanned content' from 'no content was scanned'... Recommend gold add field `score_class: {SCORED, BLOCKED_UPSTREAM, NO_PAGES}`."

Closed by FIND_INSURE.030 (`ec0c38b4b`): `classify_score()` + `score_class` field on the gold record. Carl-Ostenson (empty-body) now classifies `BLOCKED_UPSTREAM` vs 1st-Atlantic (true-negative) `SCORED`. The IR-analyst-can't-tell-the-difference gap is resolved.

### W1 — term taxonomy criterion / threshold semantics → **IN-FLIGHT (v0.7.1)**

CVO observation (REPAIR-AMENDMENT (b)(i)): "ranking entities that appear to have wealth-management programs **or may be adjacent to it**" implies a 3-class label (present/adjacent/absent); taxonomy produces continuous 0-100 only; no threshold mapping.

In-flight closure: PRD v0.7.1 (`cba505dfb`) §257-260 + the working-tree `score_web_gold.py` `classify_wm()` joint-logic (present = score≥80 AND class_diversity≥2; adjacent = score≥80 single-class OR 40≤score<80; absent = score<40; null+reason for BLOCKED_UPSTREAM/NO_PAGES/taxonomy-mismatch). `compute_class_diversity()` adds the v0.7.1 §269 annuity-vocab co-fire-conditional eligibility (prevents pure-annuity-carrier single-class saturation). **Notably, `classify_wm()` consumes my `score_class`** — the G1 + W1 closures interlock.

**Watch-item (NOT a new patch — flagging for the in-flight lane):** the committed gold record at `ec0c38b4b` emits `score_class` but `score_imo()` does not yet wire `classify_wm()` → `wm_classification` into the record. That integration is the open v0.7.1 wiring (another lane's in-flight work). When it lands, the gold record should co-emit `score_class` (data-quality axis) AND `wm_classification` (signal axis) with consistent null-reason semantics — `wm_classification=null, reason=blocked_upstream` should align 1:1 with `score_class=BLOCKED_UPSTREAM`. If they diverge, that would be a genuine v0.7.2 silent-tail. Recommend the v0.7.1 integration's self-test assert the score_class↔wm_classification null-path consistency.

### W2 — scoring weights traceability → **ARCHITECTURAL-DEFER**

CVO observation: the 4 employee-score weights (w_tenure/w_seniority/w_series/w_keyword) + 5 company-score weights lack explicit Andrew-direction OR empirical-fit provenance; "placeholder weights of unstated provenance."

Disposition: this is **not a v0.4.x code patch** — it is a ratification cycle (O-2-final per `scoring-weights-v0.1.json` `open_items_pending_empirical_ratify`). The weights need empirical-fit against a Phase-3 IR-team spot-review, which is gated on the universe-run + serving consolidation + an IR-team feedback loop. Patching the numbers without that empirical signal would just substitute one unprovenanced set for another. Correct path: hold for O-2-final post-Phase-3. No action this survey.

### W3 — ranking output / consolidated serving table → **IN-FLIGHT (.023)**

CVO observation: no consolidated `serving/scoring.{json,parquet}`; 3 per-IMO `gold/score.json` only; no IR-team-facing ranked table.

In-flight closure: DS~E `.023` serving-consolidation W3 (per `org/tier2_senior/0.1.0_DS_MarketIntelligence~E/task_orders/FIND_INSURE.023.dse-serving-consolidation-w3.md`). Reads all gold/score.json → emits ranked serving table. This is also where my `score_class` (and the forthcoming `wm_classification`) surface at the serving layer as `data_quality_class` (the AC9 enum-alignment sister-coord from my .030). Gated on C1 universe-run producing the 99 gold files to consolidate.

### P2 — empirical TP/FP discrimination → **GATED (C1 universe-run)**

CVO observation: Andrew-mandated 5-known-AM + 5-known-absent discrimination undeliverable on the n=2 valid sample (Avantax TP / 1st-Atlantic TN; Carl-Ostenson is BLOCKED-class, not a discriminating negative — which my `score_class` now labels explicitly).

Disposition: **gated, not patchable.** Fires when C1 resolves (AE 0.7~A Stage 2 combined-apply → `dispatch_stage2.sh` → gold fan-out across the universe) OR when a 10-IMO validation subset is dispatched ahead of the full run. CVO's own recommendation: have ws CTO + COO scope a 10-IMO P2 validation subset in a /ws-charter cycle. No gold-code action; it's an empirical-run + sample-selection dependency. **My `score_class` improves P2's future delivery** — the discrimination test can now exclude BLOCKED_UPSTREAM IMOs from the TP/FP denominator (a BLOCKED zero is not a true-negative), making the eventual 5-on-5 cleaner.

---

## Adjacent (non-gold) observations — noted, out of survey scope

For completeness (these are NOT gold/scoring axes, so only pointered, not dispositioned here):

- **C1** (3/99 coverage) — REPAIR-AMENDMENT (a); AE 0.7~A universe-run (Stage 2).
- **C2 / AC-T2** (empty-body distribution) — escape-valve conditional; gated on universe-run for statistical validity (n=3 too small).
- **S1 Rule 17** (5 bronze meta fields dropped in silver) — REPAIR-AMENDMENT (b)(ii); **CLOSED** by .007 `3ee6ee869` (my prior fix) + re-confirmed in today's Rule 17 silver audit `17e3eba07`.

---

## Recommended next-actions (for ws COO / ws CTO disposition)

1. **No new DS gold-patch TO needed** — the gold/scoring cluster is fully accounted for. Don't manufacture a patch where none is warranted (the §G1 surface was the real one; it shipped).
2. **One watch-item for the v0.7.1 integration lane:** assert score_class↔wm_classification null-path consistency in the `score_imo()` wiring self-test (§W1 detail above). 1-test addition, folds into the in-flight v0.7.1 work — not a separate TO.
3. **P2 acceleration option** (CVO's own rec, surfaced for COO): scope a 10-IMO TP/FP validation subset ahead of the full 99-IMO run so the discrimination axis can fire without waiting on the complete universe — and exclude BLOCKED_UPSTREAM IMOs from the denominator using the new `score_class`.

— 0.1.0_DS_MarketIntelligence~A 2026-05-28 — FIND_INSURE gold-tier + scoring-layer observation survey (STANDING-PARALLEL Option c)
