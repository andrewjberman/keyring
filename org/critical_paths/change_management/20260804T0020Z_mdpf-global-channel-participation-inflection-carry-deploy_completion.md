# Deploy completion — global fold: channel_participation meta + inflection carry

**Deployer:** 0.2.0_DS_PortfolioAnalytics (Rule-13 DS gold lane) · **Opened/closed:** 2026-08-04 00:12–00:20Z (single-leg, in-session)
**What:** `s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` → repo HEAD @85e7eb3922 (MATCH verified).
**Authority chain:** CTO rider 20260803T221247Z (participation + bounded carry REQUIRED on the global leg) → window RULED 2 TD (CTO 221952Z via AE relay) → schema CONVERGED w/ AE (222302Z) → **shape VALIDATED CTO 20260804T000925Z** (sparse-only; 49financial explicit-null; consumer-contract sentence) → this deploy.
**Hold analysis:** DELTA=0 **verified at value level** (every served field IDENTICAL vs the pre-edit build on identical frozen inputs — dates, opal_aggregate_aua, model_aua, non_model, inflection_non_model, by_model, cohort_provenance, point_class, account_count_total). Meta-only addition ⇒ the never-widen carve-out APPLIES; no serve-hold required. The inflection carry is FORWARD semantics only: the carry map is EMPTY on any healthy build (proven — no carry line fired on current inputs); it first activates on an INF-lag floor day, which is the RULED design.

## The change

1. **Inflection joins the carry mechanism** (mirror of cottonwood's): dates beyond inflection's own
   measured frontier within the roster-declared window (ruled default 2 TD until AE's roster entry
   lands) carry the frontier-dated MEASURED values — headline + by_model value legs; **counts never**.
   Past window: absent-for-real, headline honest-None (unchanged). Carried slots labeled
   `carried_at_declared_cadence(as_of=...)` with `as_of_by_partner` naming the vintage.
2. **`meta.channel_participation`** (validated shape): law text WITH the consumer contract
   ("consumers requiring fully-contributed data MUST check exceptions"), statuses, windows in SERVED
   meta (`49financial: null` + explicit deliberate-absence note), coverage, declared default, SPARSE
   exceptions only ("one representation, one truth"), vocabulary_note (participation vs
   cohort_provenance basis lattice — the count_basis/count_provenance precedent), pre-schema-vintage
   reader note (AE's discipline).

## Exercise evidence

| Check | Result |
|---|---|
| commit-gate | clean |
| Value parity vs pre-edit build (frozen inputs) | **IDENTICAL on all 9 served fields** |
| Composition gate | PASS across 454 dates |
| Inflection carry on healthy data | map EMPTY (zero behavioral delta) — first activates on a lag day |
| Exceptions honesty | 28 sparse dates: 18×49f-absent + 24×inf-absent (real union-axis gaps) + 3 cot carried (ages 1/2/3, `watch` at >1) + **1 cot past-window transition row with `last_carried_as_of`** — all three CTO labeling requirements demonstrated live |
| Deploy verify | comp-pipescript `--pipeline mdpf` → MATCH |

**Downstream:** AE's floor-gate Lambda change (delete hard-DEFER) cuts next per the validated wave;
their seat is under an operator hold since ~23:12Z — resumes on Andrew's word. Served-side
participation appears at the next scheduled 6d cycle (no hand-publish).
