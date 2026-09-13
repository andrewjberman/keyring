# AMGT_RESAPP round 2 CVO adjudication

Author: `3.0.0_SA_CVO~Z`. Handoff 21308 from `2.0.0_SA_COO~ZZZ`, drain `56c755b86a`; independent review pin `9a2e542c0bea91b87046e243bd5009e310642155`.

L8: both channel roots compiled; 28 investigations, four new undispositioned rows. This vintage dispositions all four, including issuer S4. L9: five judgments, 2 PASS / 3 FAIL. All 21 task orders terminal and all 21 proof instances VALID; 15 existing tests pass. These mechanical results do not override the judgment failures.

Existing round-1 rows and remediations remain append-only historical records. No decomposition-invalidating finding: the new defects sit inside already enumerated surfaces. New findings below are CVO rows only.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S8",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T08:58:51Z",
    "one_line": "The fiscal-period field named by the order is not mapped; the implemented join uses the fundamental row date.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W1-S5 cites the CRO map: FISCAL_YEAR_END is BAD_FLD/INVALID_FIELD; no alternative tested.",
        "integrations/bloomberg/research/fye_join.py reads each fundamentals-bearing row date. org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json independently reads all 30 served fiscal-year records; no future dates in this sample."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The fiscal-period field named by the order is not mapped; the implemented join uses the fundamental row date.",
    "world_is": "W1-S5 cites the CRO map: FISCAL_YEAR_END is BAD_FLD/INVALID_FIELD; no alternative tested. integrations/bloomberg/research/fye_join.py reads each fundamentals-bearing row date. org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json independently reads all 30 served fiscal-year records; no future dates in this sample.",
    "notes": "Correct future order/context text to name the measured row-date carrier. Do not imply a successfully mapped FISCAL_YEAR_END reference field. No new vendor call authorized.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W1-S5"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S9",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T08:58:51Z",
    "one_line": "The SA exercise population is BABA/BA/COST; the order names BABA/RTX/+1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json records a fresh S3 listing: 18 raw keys across BABA_US, BA_US and COST_US only.",
        "Worker 9 sa_ids.json and worker 2 coverage files name that same population. W2-S5 is supported; no RTX substitute was fetched."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The SA exercise population is BABA/BA/COST; the order names BABA/RTX/+1.",
    "world_is": "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json records a fresh S3 listing: 18 raw keys across BABA_US, BA_US and COST_US only. Worker 9 sa_ids.json and worker 2 coverage files name that same population. W2-S5 is supported; no RTX substitute was fetched.",
    "notes": "Correct future cuts and analysis to BABA/BA/COST, retaining the actual security denominator and source pins.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W2-S5"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S10",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T08:58:51Z",
    "one_line": "The sanctioned commit path preserved all five new modules; the root ignore rule still hides future untracked lib source files from ordinary status.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git check-ignore --no-index -v returns .gitignore:47:lib/ for all five named modules. git ls-files --error-unmatch independently finds all five tracked.",
        "W3-S5 and issuer S4 agree safe-commit uses git add -f. The issuer disarmed this round's omission exposure; that does not remove the remaining discovery defect."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The sanctioned commit path preserved all five new modules; the root ignore rule still hides future untracked lib source files from ordinary status.",
    "world_is": "git check-ignore --no-index -v returns .gitignore:47:lib/ for all five named modules. git ls-files --error-unmatch independently finds all five tracked. W3-S5 and issuer S4 agree safe-commit uses git add -f. The issuer disarmed this round's omission exposure; that does not remove the remaining discovery defect.",
    "notes": "Keep the existing round-1 W1-S3 remediation linked; do not count this recurrence as a second independent defect. Route a scoped source-tree ignore correction or explicit tracked-plus-ignored-file enumeration to the repository owner. A bare !lib/research/ exception alone must not be assumed sufficient beneath an ignored parent.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W3-S5",
      "AMGT_RESAPP-Z-S4"
    ],
    "disarm_owner": "1.0.0_SA_CTO~Z to route to repository owner"
  },
  {
    "id": "AMGT_RESAPP-Z-C-S11",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T08:58:51Z",
    "one_line": "Round 2 judgment: 2 PASS, 3 FAIL, zero NOT_EVALUATED; mechanical validation is separate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json records independent workbook, S3 and predicate reads; 15 existing tests passed; all 21 proof instances validated.",
        "All five judgment evidence packages are present at 9a2e542c0bea91b87046e243bd5009e310642155."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "This row records grades rather than a separate investigation finding; substantive failures are graduated as C-S12 through C-S14.",
    "grades": [
      {
        "criterion": "AMGTr1-AC4",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/AMGT_RESAPP.TO-AMGT-r-1.fiscal-year-join-served-correct.proof_of_spec.json@9a2e542c0bea91b87046e243bd5009e310642155",
        "verdict": "PASS",
        "reason": "The requested landed-data comparison passes: independent S3 readback gives BABA FY2025 period_end and price_date both 2025-03-31, price 132.23. The same join serves BA and SAP December FY2025 at 2025-12-31, with maxima 2 days across each ten-year series (BABA 3). This is a grade of the named period-end comparison, not approval of every boundary or downstream consumer; C-S15 and C-S16 carry those limits."
      },
      {
        "criterion": "AMGTr4-AC5",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~2/AMGT_RESAPP.TO-AMGT-r-4.sa-coverage-re-exercise.proof_of_spec.json@9a2e542c0bea91b87046e243bd5009e310642155",
        "verdict": "PASS",
        "reason": "The BABA SA rows say PROVISIONAL because BABA_US is absent from the item tags, so the reader knows that aboutness needs a confirmed tag rather than treating attachment as qualification. Actual ordering places 2026-09-10 15:00 (10 mentions) ahead of 01:14 (102), then older items: recency first, discussion count second. Five existing tests cover the equal-date tie and identity/unscoped controls. The raw content is real; non-SA companion fixtures and unresolved SA subject mapping remain disclosed."
      },
      {
        "criterion": "AMGTr10-AC4",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/AMGT_RESAPP.TO-AMGT-r-10.check-face-marker-in-the-reading.proof_of_spec.json@9a2e542c0bea91b87046e243bd5009e310642155",
        "verdict": "FAIL",
        "reason": "The token-contract limb passes: green/OK, amber/WARN, red/BLOCKED are distinct and transferable. The reading limb does not: the rendered fixture changes 12345 [PROVISIONAL] to 12345 [PROVISIONAL] [WARN], adding another plain suffix word to the same number-first presentation previously rejected. There is still no rendered color, warning glyph, leading status, or equivalent change in visual prominence. The test compares different values (500 versus 12345), so string inequality does not prove a marker makes the difference, much less at-a-glance comprehension. This is a CVO visual judgment, not a measured user-study result; no .tsx is required to demonstrate a salient print fixture."
      },
      {
        "criterion": "AMGTr12-AC4",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/AMGT_RESAPP.TO-AMGT-r-12.identity-coverage-pass.proof_of_spec.json@9a2e542c0bea91b87046e243bd5009e310642155",
        "verdict": "FAIL",
        "reason": "The measured-source limb passes independently: Overview row 2 in each original workbook names Ticker: IMB LN / IMPERIAL BRANDS and Ticker: SAP GY / SAP SE. All 34 measured identifiers are distinct. The decision-document limb fails: DESIGN_QUESTION_identity_fallback.md twice promises MEASURED-or-better coverage 34 to 49 while explicitly limiting all fallback values to INFERRED, never MEASURED. Those categories cannot share the claimed denominator. It also treats hypothetical renaming as a measured failure. Andrew would have to repair the benefit and evidence claims before ruling; correct them to 34 measured plus up to 15 inferred candidates, with downstream admissibility unresolved."
      },
      {
        "criterion": "AMGTr15-AC4",
        "instance": "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~5/AMGT_RESAPP.TO-AMGT-r-15.impostor-and-clause.proof_of_spec.json@9a2e542c0bea91b87046e243bd5009e310642155",
        "verdict": "FAIL",
        "reason": "The copied-bio-only control is refused, but the implementation is strong = check1 or check2 and immediately returns official; it does not enforce the advertised AND with further evidence. Independent eight-case enumeration admits check2 alone and check1 alone. The worker also discloses that a non-identity-bound verification mark plus copied bio still passes; no external platform claim is needed to see that the caller contract never distinguishes identity-bound verification. The two passing fixture arms do not establish real official-versus-impostor discrimination. Preserve UNRESOLVED handles until the predicate and evidence contract are clarified and tested."
      }
    ],
    "notes": "Carrier defect inherited from C-S7: schema requires a compound criterion while these orders use bare AC ids. Deterministic mapping strips nonalphanumerics from cell_ref and prefixes the bare AC id (AMGT-r-12 AC4 -> AMGTr12-AC4). These compound ids are CVO-authored, not verbatim order ids. Round-1 grades remain historical; this file grades only the five round-2 cells.",
    "spec_asserts": "L9 requires CVO judgment grades for all five round-2 criteria; worker proof instances must withhold self-grades.",
    "world_is": "All five proof instances withhold verdicts as UNVERIFIABLE-BY-INSTRUMENT. CVO review supplies two PASS and three FAIL verdicts here, independently of the 15 passing tests and 21 schema-valid proof instances."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S12",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T08:58:51Z",
    "one_line": "A second trailing text tag does not establish the requested at-a-glance PROVISIONAL distinction.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The token-contract limb passes: green/OK, amber/WARN, red/BLOCKED are distinct and transferable. The reading limb does not: the rendered fixture changes 12345 [PROVISIONAL] to 12345 [PROVISIONAL] [WARN], adding another plain suffix word to the same number-first presentation previously rejected. There is still no rendered color, warning glyph, leading status, or equivalent change in visual prominence. The test compares different values (500 versus 12345), so string inequality does not prove a marker makes the difference, much less at-a-glance comprehension. This is a CVO visual judgment, not a measured user-study result; no .tsx is required to demonstrate a salient print fixture.",
        "Worker 3 check_face_fixture.md and SPEC_SECTION_checkface.md at 9a2e542c0bea91b87046e243bd5009e310642155; render_print.py appends icon as bracketed text and does not render colour_token."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A second trailing text tag does not establish the requested at-a-glance PROVISIONAL distinction.",
    "world_is": "The token-contract limb passes: green/OK, amber/WARN, red/BLOCKED are distinct and transferable. The reading limb does not: the rendered fixture changes 12345 [PROVISIONAL] to 12345 [PROVISIONAL] [WARN], adding another plain suffix word to the same number-first presentation previously rejected. There is still no rendered color, warning glyph, leading status, or equivalent change in visual prominence. The test compares different values (500 versus 12345), so string inequality does not prove a marker makes the difference, much less at-a-glance comprehension. This is a CVO visual judgment, not a measured user-study result; no .tsx is required to demonstrate a salient print fixture. Worker 3 check_face_fixture.md and SPEC_SECTION_checkface.md at 9a2e542c0bea91b87046e243bd5009e310642155; render_print.py appends icon as bracketed text and does not render colour_token.",
    "notes": "Provide a visibly salient warning in the permitted print fixture; preserve the value and carry the closed marker contract into the eventual approved design. Compare the SAME number under PASS and PROVISIONAL. Regrade AC4 before treating FWD-10 as realized.",
    "disarm_owner": "2.0.0_SA_COO~ZZZ"
  },
  {
    "id": "AMGT_RESAPP-Z-C-S13",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T08:58:51Z",
    "one_line": "The identity fallback design note mixes MEASURED and INFERRED in its advertised coverage benefit.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The measured-source limb passes independently: Overview row 2 in each original workbook names Ticker: IMB LN / IMPERIAL BRANDS and Ticker: SAP GY / SAP SE. All 34 measured identifiers are distinct. The decision-document limb fails: DESIGN_QUESTION_identity_fallback.md twice promises MEASURED-or-better coverage 34 to 49 while explicitly limiting all fallback values to INFERRED, never MEASURED. Those categories cannot share the claimed denominator. It also treats hypothetical renaming as a measured failure. Andrew would have to repair the benefit and evidence claims before ruling; correct them to 34 measured plus up to 15 inferred candidates, with downstream admissibility unresolved.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json records the two original workbook rows and 34 distinct MEASURED values."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The identity fallback design note mixes MEASURED and INFERRED in its advertised coverage benefit.",
    "world_is": "The measured-source limb passes independently: Overview row 2 in each original workbook names Ticker: IMB LN / IMPERIAL BRANDS and Ticker: SAP GY / SAP SE. All 34 measured identifiers are distinct. The decision-document limb fails: DESIGN_QUESTION_identity_fallback.md twice promises MEASURED-or-better coverage 34 to 49 while explicitly limiting all fallback values to INFERRED, never MEASURED. Those categories cannot share the claimed denominator. It also treats hypothetical renaming as a measured failure. Andrew would have to repair the benefit and evidence claims before ruling; correct them to 34 measured plus up to 15 inferred candidates, with downstream admissibility unresolved. org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json records the two original workbook rows and 34 distinct MEASURED values.",
    "notes": "Correct the decision note to 34 MEASURED and up to 15 additional INFERRED candidates, not 49 MEASURED-or-better. Separate observed ambiguity from hypothetical renaming and state which downstream gates would still refuse INFERRED. Keep the fallback unimplemented pending Andrew's decision.",
    "disarm_owner": "2.0.0_SA_COO~ZZZ"
  },
  {
    "id": "AMGT_RESAPP-Z-C-S14",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T08:58:51Z",
    "one_line": "The advertised impostor AND-clause executes as check1 OR check2, and verification is an untyped boolean.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "The copied-bio-only control is refused, but the implementation is strong = check1 or check2 and immediately returns official; it does not enforce the advertised AND with further evidence. Independent eight-case enumeration admits check2 alone and check1 alone. The worker also discloses that a non-identity-bound verification mark plus copied bio still passes; no external platform claim is needed to see that the caller contract never distinguishes identity-bound verification. The two passing fixture arms do not establish real official-versus-impostor discrimination. Preserve UNRESOLVED handles until the predicate and evidence contract are clarified and tested.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json contains all eight boolean cases, including (false,true,false) -> official and (false,false,true) -> impostor."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The advertised impostor AND-clause executes as check1 OR check2, and verification is an untyped boolean.",
    "world_is": "The copied-bio-only control is refused, but the implementation is strong = check1 or check2 and immediately returns official; it does not enforce the advertised AND with further evidence. Independent eight-case enumeration admits check2 alone and check1 alone. The worker also discloses that a non-identity-bound verification mark plus copied bio still passes; no external platform claim is needed to see that the caller contract never distinguishes identity-bound verification. The two passing fixture arms do not establish real official-versus-impostor discrimination. Preserve UNRESOLVED handles until the predicate and evidence contract are clarified and tested. org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json contains all eight boolean cases, including (false,true,false) -> official and (false,false,true) -> impostor.",
    "notes": "Clarify the intended truth table and the identity meaning of verification; require the stated co-occurrence where intended. Add negative controls for verification without further evidence and for a mark that does not attest company identity. Keep all real handles UNRESOLVED; no social/vendor call or owner assignment is authorized.",
    "disarm_owner": "2.0.0_SA_COO~ZZZ"
  },
  {
    "id": "AMGT_RESAPP-Z-C-S15",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T08:58:51Z",
    "one_line": "The fiscal join can select a future price and report a small absolute gap when no on-or-before observation exists.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json independent control: period_end 2025-12-31 plus only price_date 2026-01-02 returns price 100, gap_days 2.",
        "fye_join._nearest_price falls back to the nearest point in either direction; gap_days uses abs, so the under-45-days mechanical check accepts this direction violation. All 30 actual landed rows have zero such violations at this vintage."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The fiscal join can select a future price and report a small absolute gap when no on-or-before observation exists.",
    "world_is": "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json independent control: period_end 2025-12-31 plus only price_date 2026-01-02 returns price 100, gap_days 2. fye_join._nearest_price falls back to the nearest point in either direction; gap_days uses abs, so the under-45-days mechanical check accepts this direction violation. All 30 actual landed rows have zero such violations at this vintage.",
    "notes": "Return unresolved when no on-or-before price exists; add a future-only negative control and a direction assertion. Preserve the passing three-security sample and its exact pins. This is a bounded source defect, not evidence of a fourth live security failure.",
    "disarm_owner": "2.0.0_SA_COO~ZZZ"
  },
  {
    "id": "AMGT_RESAPP-Z-C-S16",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-11T08:58:51Z",
    "one_line": "The corrected fiscal block is a new engine output; current render consumers remain on the original model_block lane.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Worker 1 r-1 declared_exclusions explicitly excludes replacing model_block artifacts and wiring provenance/print consumers. derive_fye_fixed.py writes derived/model_block_fye/.",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json verifies the corrected S3 lane only; it does not show any consumer switched to it."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "The corrected fiscal block is a new engine output; current render consumers remain on the original model_block lane.",
    "world_is": "Worker 1 r-1 declared_exclusions explicitly excludes replacing model_block artifacts and wiring provenance/print consumers. derive_fye_fixed.py writes derived/model_block_fye/. org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json verifies the corrected S3 lane only; it does not show any consumer switched to it.",
    "notes": "Carry this as integration work for the next authorized cut: name and test the consumer path and its derived-artifact vintage before claiming the served analyst pack uses the corrected join. Do not overwrite peer outputs or implement round 3 from this slug.",
    "disarm_owner": "2.0.0_SA_COO~ZZZ"
  }
]
```
