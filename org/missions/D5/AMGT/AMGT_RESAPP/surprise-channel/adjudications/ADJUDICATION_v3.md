# AMGT_RESAPP canonical round 3 adjudication (informal round 2b)

CVO `3.0.0_SA_CVO~Z`. Drain 21334 at `bb654d2d4f401e9aa1dea7d59932f50ff6395abc`; mapping ruling CTO~Z 21335. This is the third corrective issuance; the design-gated surface exercise is a later round.

L8: 29 investigations across both roots, one new open row W5-S2. L9: all five rb judgments graded **4 PASS / 1 FAIL**. Mechanical checks: 26/26 proofs VALID, all 26 task orders complete, 23 tests passed. The single new investigation is dispositioned below.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S17",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T11:09:15Z",
    "one_line": "W5-S2 is grounded and its over-scoped criterion is now corrected by the issuer.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND3_CVO_EVIDENCE_20260911.json independently reproduces the old whole-directory sweep: only rot.py matches. The amended three-file predicate scope has zero hits.",
        "The rb-15 order records the issuer amendment; its proof now validates and its six predicate tests pass in the full 23-test run. rot.py was not changed to force green."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "W5-S2 is grounded and its over-scoped criterion is now corrected by the issuer.",
    "world_is": "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND3_CVO_EVIDENCE_20260911.json independently reproduces the old whole-directory sweep: only rot.py matches. The amended three-file predicate scope has zero hits. The rb-15 order records the issuer amendment; its proof now validates and its six predicate tests pass in the full 23-test run. rot.py was not changed to force green.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W5-S2"
    ],
    "notes": "Disarm and remediation are recorded together on the original W5-S2 id in REMEDIATION_v3. No additional task or independent defect is minted for the amended criterion."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S18",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T11:09:15Z",
    "one_line": "Canonical round 3 (informal 2b): five judgments, four PASS and one FAIL.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND3_CVO_EVIDENCE_20260911.json records 26 terminal orders, 26 VALID proof instances, 23 passing tests and independent controls.",
        "CTO mapping msg21335 authorizes r3/v3 for this corrective issuance; rb cell ids stay fixed and surface work remains gated."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Canonical round 3 (informal 2b): five judgments, four PASS and one FAIL.",
    "world_is": "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND3_CVO_EVIDENCE_20260911.json records 26 terminal orders, 26 VALID proof instances, 23 passing tests and independent controls. CTO mapping msg21335 authorizes r3/v3 for this corrective issuance; rb cell ids stay fixed and surface work remains gated.",
    "dismissal_reason": "Grade record, not a separate defect. The consumer failures are graduated as C-S19/C-S20.",
    "grades": [
      {
        "criterion": "AMGTrb10-AC5",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/AMGT_RESAPP.TO-AMGT-rb-10.check-face-salient-warning.proof_of_spec.json@bb654d2d4f401e9aa1dea7d59932f50ff6395abc",
        "verdict": "PASS",
        "reason": "The same 12345 value now reads PASS = 12345, PROVISIONAL = [WARN] 12345 [PROVISIONAL], REFUSE = [BLOCKED] [REFUSED: unit never confirmed against a field map]. In the warned cases the status is encountered before any number; the plain PASS stays distinct. The spec carries the same green/OK, amber/WARN, red/BLOCKED vocabulary and leading placement into the later design. The same-number test now removes the prior confounding value difference. This is a grade of the permitted print fixture, not a claim that the historical worker-8 outputs or a future UI were re-rendered."
      },
      {
        "criterion": "AMGTrb12-AC4",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/AMGT_RESAPP.TO-AMGT-rb-12.identity-decision-note-correction.proof_of_spec.json@bb654d2d4f401e9aa1dea7d59932f50ff6395abc",
        "verdict": "PASS",
        "reason": "The decision note now separates 34 MEASURED from up to 15 INFERRED candidates and observed Nokia-token ambiguity from hypothetical renaming. It distinguishes the existing source-admission rule from render_together: the directory fallback has no authorized write path, while the read gate currently admits INFERRED. An independent INFERRED read-gate control confirms that open design choice. There is no existing read-side INFERRED refusal to claim; the note honestly names that absence and makes its resolution a prerequisite to serving fallback values. The measured universe is unchanged. The wording calling coverage_pass the ONLY MEASURED writer is too broad (build_universe also writes baseline measurements); this does not change the actual fallback decision or the demonstrated read-gate limit."
      },
      {
        "criterion": "AMGTrb15-AC4",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/AMGT_RESAPP.TO-AMGT-rb-15.impostor-predicate-corrected.proof_of_spec.json@bb654d2d4f401e9aa1dea7d59932f50ff6395abc",
        "verdict": "PASS",
        "reason": "The clarified executed contract is company-owned exact-URL link OR (mark present AND bound to THIS company identity). The co-occurrence is now explicit within verification; a copied bio cannot supply missing identity. Independent enumeration of all 16 well-typed combinations matches that contract. A present but identity-blind mark alone is unresolved, with copied bio it is impostor, and a bare boolean check2 raises TypeError. An authoritative company link may admit without a bio because it already attests the company account; this is now stated rather than hidden behind an advertised further-evidence clause. This grades the rule over caller-supplied evidence, not the real-world truth of an unmeasured identity_bound flag. All 267 real handle records and owners remain unchanged; live resolution is still gated."
      },
      {
        "criterion": "AMGTrb1-AC4",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/AMGT_RESAPP.TO-AMGT-rb-1.fiscal-join-direction-correct.proof_of_spec.json@bb654d2d4f401e9aa1dea7d59932f50ff6395abc",
        "verdict": "PASS",
        "reason": "UNRESOLVED is the correct answer when no on-or-before observation exists: a later price cannot truthfully answer as-of period end. The sole resolving branch chooses the maximum date from d <= period_end; the alternative returns None. Independent empty, future-only, exact-day and mixed-date cases pass, including full fiscal_period_join propagation of None for price/date/gap. The signed gap no longer hides a future result with abs. Existing tests exercise the production join across three landed securities, and all six original/corrected sample artifacts are byte-unchanged since round 2. C-S15 source logic is fixed; the separate consumer in rb-2 can still discard this unresolved result, which is C-S19 below."
      },
      {
        "criterion": "AMGTrb2-AC4",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/AMGT_RESAPP.TO-AMGT-rb-2.fiscal-block-wired-to-consumer.proof_of_spec.json@bb654d2d4f401e9aa1dea7d59932f50ff6395abc",
        "verdict": "FAIL",
        "reason": "The populated-sample wiring works: the actual load_model_block returns BABA FY2025 132.23 at 2025-03-31 instead of 146.58, and a CVO scratch run of the actual PDF builder prints that corrected value. The source originals remain unchanged. Full corrected-join propagation fails: load_corrected_price_overlay filters out every price=None row, then apply_corrected_price_overlay silently retains the original calendar-year figure. A synthetic future-only row at BABA period_end 2025-03-31 correctly becomes UNRESOLVED in rb-1 but reaches the renderer as old unmarked 146.58 through rb-2. The claimed end-to-end correction cannot close while it turns absence of valid fiscal evidence back into an apparently valid old price. In addition, the corrected artifact derivation key is dropped; price_date replaces vintage and the renderer prints only Bloomberg, so the test establishes observation date, not the derived vintage its order asks to carry. See C-S19 and C-S20. No live end-user surface was exercised; the worker regenerated provenance fragments and CVO verified the PDF in scratch only."
      }
    ],
    "notes": "Bare order criterion ids remain mapped using the previously disclosed C-S7 convention: cell id stripped to alphanumerics plus bare AC suffix. Four matching v2 remediation rows advance only their clocks. Historical grades are not rewritten."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S19",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T11:09:15Z",
    "one_line": "The corrected-price consumer discards UNRESOLVED fiscal rows and silently resurrects the old calendar-year price.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND3_CVO_EVIDENCE_20260911.json unresolved_overlay_control: fiscal join of period_end 2025-03-31 with only 2025-04-02 price returns price/date/gap None; loader returns {}; rendering then retains the original BABA FY2025 146.58 with no unresolved marker.",
        "lib/research/provenance/render_print.py load_corrected_price_overlay includes only rows whose price is not None; apply_corrected_price_overlay skips missing years. lib/research/print/render_pack.py load_model_block calls both.",
        "The successful live-data sample and scratch PDF give 132.23; this negative control is synthetic and does not claim a current landed row has a missing price."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The corrected-price consumer discards UNRESOLVED fiscal rows and silently resurrects the old calendar-year price.",
    "world_is": "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND3_CVO_EVIDENCE_20260911.json unresolved_overlay_control: fiscal join of period_end 2025-03-31 with only 2025-04-02 price returns price/date/gap None; loader returns {}; rendering then retains the original BABA FY2025 146.58 with no unresolved marker. lib/research/provenance/render_print.py load_corrected_price_overlay includes only rows whose price is not None; apply_corrected_price_overlay skips missing years. lib/research/print/render_pack.py load_model_block calls both. The successful live-data sample and scratch PDF give 132.23; this negative control is synthetic and does not claim a current landed row has a missing price.",
    "disarm_owner": "2.0.0_SA_COO~ZZZ to route to the consumer owner",
    "notes": "Preserve explicit unresolved corrected rows, distinguish missing lane/year from resolved data, and mark or refuse a fiscal price without valid corrected evidence. Test the named consumer from full corrected-join None output through the rendered value; the original calendar price may remain in source storage but cannot silently regain trusted presentation. C-S16 stays OPEN until the end-to-end contract holds."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S20",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T11:09:15Z",
    "one_line": "The consumer substitutes price observation date for vintage and drops the corrected artifact derivation pin.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND3_CVO_EVIDENCE_20260911.json corrected_derived_key records derived/model_block_fye/BABA_US_Equity/20260911T073934Z/model_block_fye.json; current_consumer.wired carries price_date 2025-03-31 and a generic model_block_fye tag, not that immutable key.",
        "apply_corrected_price_overlay replaces fig.vintage with corrected.price_date; load_corrected_price_overlay returns fiscal rows only. render_figure_line hardcodes Bloomberg and does not emit fig.source.",
        "The actual CVO scratch PDF prints the right 132.23 price and 2025-03-31 observation date but no derived/model_block_fye key. test_consumer_wiring checks price_date as vintage rather than the derivation identifier."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The consumer substitutes price observation date for vintage and drops the corrected artifact derivation pin.",
    "world_is": "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND3_CVO_EVIDENCE_20260911.json corrected_derived_key records derived/model_block_fye/BABA_US_Equity/20260911T073934Z/model_block_fye.json; current_consumer.wired carries price_date 2025-03-31 and a generic model_block_fye tag, not that immutable key. apply_corrected_price_overlay replaces fig.vintage with corrected.price_date; load_corrected_price_overlay returns fiscal rows only. render_figure_line hardcodes Bloomberg and does not emit fig.source. The actual CVO scratch PDF prints the right 132.23 price and 2025-03-31 observation date but no derived/model_block_fye key. test_consumer_wiring checks price_date as vintage rather than the derivation identifier.",
    "disarm_owner": "2.0.0_SA_COO~ZZZ to route to the consumer owner",
    "notes": "Carry observation date and derivation/landing identity as distinct fields; retain the exact corrected key (or equivalent immutable artifact pin) through the named consumer and its provenance output. Add a test distinguishing two derived vintages with the same observation date. This is within rb-2 own named-vintage acceptance, not a request for new vendor work."
  }
]
```
