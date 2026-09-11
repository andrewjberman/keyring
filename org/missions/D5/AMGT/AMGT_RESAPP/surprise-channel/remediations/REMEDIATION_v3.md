# AMGT_RESAPP canonical round 3 L10 slug (informal round 2b)

From `3.0.0_SA_CVO~Z` to `1.0.0_SA_CTO~Z` only. Mapping authority: CTO ruling 21335; rb cell ids unchanged. Source/review pin `bb654d2d4f401e9aa1dea7d59932f50ff6395abc`. Vintage: this file's commit.

**4 PASS / 1 FAIL.** rb-10 salience, rb-12 decision note, rb-15 identity-bound predicate and rb-1 direction all pass. Their C-S12/C-S13/C-S14/C-S15 v2 remediation clocks advance to DISARMED / REMEDIATED / closed in this commit. Historical evidence and grades remain. C-S10 stays closed from its separately verified source fix.

rb-2 consumer integration fails the full claim: the populated sample and a scratch PDF use 132.23, but an explicitly unresolved corrected fiscal row revives unmarked old 146.58. The corrected derivation pin is also lost when observation date overwrites vintage. C-S16 remains OPEN; new C-S19/C-S20 identify its concrete unresolved mechanisms. This is not a claim of a missing-price failure in the currently landed 30-row sample.

All 26 orders terminal, 26 proofs VALID, 23 tests pass. L8 census: 29 investigations, one new row W5-S2 now dispositioned and closed here. No decomposition-invalidating finding: these are within the already enumerated consumer surface. Full judgments: `../adjudications/ADJUDICATION_v3.md`; independent evidence: `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND3_CVO_EVIDENCE_20260911.json`.

Serving boundary: CVO generated a PDF only in its scratch area to exercise the actual renderer. The worker regenerated three provenance fragments; original model blocks and the historical PDF remain unchanged. Neither this slug nor the canonical number 3 authorizes a .tsx, vendor call, fallback implementation, or surface exercise. Those require Andrew's design approval and the outstanding per-use/ownership decisions, in a later issuance (v4+).

Runtime: canonical surprise-watch once completed rc0 and emitted the 29-row banner; its transient PID/parent was not captured, and no persistent Monitor tool is available. The count and exact human review are independently recorded; a watcher emission is not a claim of reading. L8 stamp names the unstamped predecessor L6 as a ladder warning.

```json
[
  {
    "id": "AMGT_RESAPP-Z-W5-S2",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The rb-15 AC3 whole-directory scan incorrectly counted the pre-existing sibling rot.py DNS lookup against the predicate-only no-network criterion.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND3_CVO_EVIDENCE_20260911.json independently reproduces the old whole-directory sweep: only rot.py matches. The amended three-file predicate scope has zero hits.",
      "The rb-15 order records the issuer amendment; its proof now validates and its six predicate tests pass in the full 23-test run. rot.py was not changed to force green."
    ],
    "remedy": "Issuer narrowed the criterion to impostor.py, build_lists.py and test_impostor.py; independent three-file sweep has zero hits. Criterion repaired and re-exercised; no further remedy owed for this row.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v3",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "3.0.0_SA_CVO~Z",
      "at": "2026-09-11T11:09:15Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-Z-C-S19",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The corrected-price consumer discards UNRESOLVED fiscal rows and silently resurrects the old calendar-year price.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND3_CVO_EVIDENCE_20260911.json unresolved_overlay_control: fiscal join of period_end 2025-03-31 with only 2025-04-02 price returns price/date/gap None; loader returns {}; rendering then retains the original BABA FY2025 146.58 with no unresolved marker.",
      "lib/research/provenance/render_print.py load_corrected_price_overlay includes only rows whose price is not None; apply_corrected_price_overlay skips missing years. lib/research/print/render_pack.py load_model_block calls both.",
      "The successful live-data sample and scratch PDF give 132.23; this negative control is synthetic and does not claim a current landed row has a missing price."
    ],
    "remedy": "Preserve explicit unresolved corrected rows, distinguish missing lane/year from resolved data, and mark or refuse a fiscal price without valid corrected evidence. Test the named consumer from full corrected-join None output through the rendered value; the original calendar price may remain in source storage but cannot silently regain trusted presentation. C-S16 stays OPEN until the end-to-end contract holds.",
    "owner": "2.0.0_SA_COO~ZZZ to route to the consumer owner",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ to route to the consumer owner",
      "round": "v3"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ to route to the consumer owner",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-Z-C-S20",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The consumer substitutes price observation date for vintage and drops the corrected artifact derivation pin.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND3_CVO_EVIDENCE_20260911.json corrected_derived_key records derived/model_block_fye/BABA_US_Equity/20260911T073934Z/model_block_fye.json; current_consumer.wired carries price_date 2025-03-31 and a generic model_block_fye tag, not that immutable key.",
      "apply_corrected_price_overlay replaces fig.vintage with corrected.price_date; load_corrected_price_overlay returns fiscal rows only. render_figure_line hardcodes Bloomberg and does not emit fig.source.",
      "The actual CVO scratch PDF prints the right 132.23 price and 2025-03-31 observation date but no derived/model_block_fye key. test_consumer_wiring checks price_date as vintage rather than the derivation identifier."
    ],
    "remedy": "Carry observation date and derivation/landing identity as distinct fields; retain the exact corrected key (or equivalent immutable artifact pin) through the named consumer and its provenance output. Add a test distinguishing two derived vintages with the same observation date. This is within rb-2 own named-vintage acceptance, not a request for new vendor work.",
    "owner": "2.0.0_SA_COO~ZZZ to route to the consumer owner",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ to route to the consumer owner",
      "round": "v3"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ to route to the consumer owner",
      "at": null
    },
    "closed": false
  }
]
```
