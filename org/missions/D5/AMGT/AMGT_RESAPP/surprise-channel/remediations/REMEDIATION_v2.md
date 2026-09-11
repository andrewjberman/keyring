# AMGT_RESAPP round 2 L10 slug

From `3.0.0_SA_CVO~Z` to `1.0.0_SA_CTO~Z` only. Vintage: this file's commit. Drain 21308 / `56c755b86a`; reviewed artifacts pinned at `9a2e542c0bea91b87046e243bd5009e310642155`.

**2 PASS / 3 FAIL.** Fiscal sample and SA coverage judgments pass. Check-face salience, identity decision-note coherence, and social predicate judgments fail. The source fix for fiscal alignment also has a future-only boundary defect; its corrected lane is not yet integrated into existing render consumers. All 21 orders are terminal and all 21 proof instances validate; 15 existing tests pass.

This slug carries eight remediation rows, including three dispositions covering all four newly open investigation rows. Full grades and evidence: `../adjudications/ADJUDICATION_v2.md` and `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json`. Round-1 obligations remain; this is not a reset or evidence that prior OPEN rows closed. In particular, all five new lib modules are tracked, but the root ignore rule still hides future untracked source files.

Round 3 remains outside this handoff: Andrew DESIGN_SPEC approval, social/model per-use permission, peer quota and list owners remain prerequisites. No new spending, vendor call, .tsx, fallback implementation, remediation code or round-3 task order is authorized by this slug. CTO analysis/ROE decides the next cut.

Runtime limitation: the canonical surprise watcher was exercised in `once` mode; no persistent Monitor facility is exposed to this Codex seat. Its emitted watermark is not evidence of human reading. L8 compilation and the four exact dispositions are independently measured here. The L8 stamp reports the missing predecessor L6 stamp as a ladder warning; no historical stamp is invented.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S8",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The fiscal-period field named by the order is not mapped; the implemented join uses the fundamental row date.",
    "evidence": [
      "W1-S5 cites the CRO map: FISCAL_YEAR_END is BAD_FLD/INVALID_FIELD; no alternative tested.",
      "integrations/bloomberg/research/fye_join.py reads each fundamentals-bearing row date. org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json independently reads all 30 served fiscal-year records; no future dates in this sample."
    ],
    "remedy": "Correct future order/context text to name the measured row-date carrier. Do not imply a successfully mapped FISCAL_YEAR_END reference field. No new vendor call authorized.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-Z-C-S9",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The SA exercise population is BABA/BA/COST; the order names BABA/RTX/+1.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json records a fresh S3 listing: 18 raw keys across BABA_US, BA_US and COST_US only.",
      "Worker 9 sa_ids.json and worker 2 coverage files name that same population. W2-S5 is supported; no RTX substitute was fetched."
    ],
    "remedy": "Correct future cuts and analysis to BABA/BA/COST, retaining the actual security denominator and source pins.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-Z-C-S10",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The sanctioned commit path preserved all five new modules; the root ignore rule still hides future untracked lib source files from ordinary status.",
    "evidence": [
      "git check-ignore --no-index -v returns .gitignore:47:lib/ for all five named modules. git ls-files --error-unmatch independently finds all five tracked.",
      "W3-S5 and issuer S4 agree safe-commit uses git add -f. The issuer disarmed this round's omission exposure; that does not remove the remaining discovery defect."
    ],
    "remedy": "Keep the existing round-1 W1-S3 remediation linked; do not count this recurrence as a second independent defect. Route a scoped source-tree ignore correction or explicit tracked-plus-ignored-file enumeration to the repository owner. A bare !lib/research/ exception alone must not be assumed sufficient beneath an ignored parent.",
    "owner": "1.0.0_SA_CTO~Z to route to repository owner",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z to route to repository owner",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z to route to repository owner",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-C-S12",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "A second trailing text tag does not establish the requested at-a-glance PROVISIONAL distinction.",
    "evidence": [
      "The token-contract limb passes: green/OK, amber/WARN, red/BLOCKED are distinct and transferable. The reading limb does not: the rendered fixture changes 12345 [PROVISIONAL] to 12345 [PROVISIONAL] [WARN], adding another plain suffix word to the same number-first presentation previously rejected. There is still no rendered color, warning glyph, leading status, or equivalent change in visual prominence. The test compares different values (500 versus 12345), so string inequality does not prove a marker makes the difference, much less at-a-glance comprehension. This is a CVO visual judgment, not a measured user-study result; no .tsx is required to demonstrate a salient print fixture.",
      "Worker 3 check_face_fixture.md and SPEC_SECTION_checkface.md at 9a2e542c0bea91b87046e243bd5009e310642155; render_print.py appends icon as bracketed text and does not render colour_token."
    ],
    "remedy": "Provide a visibly salient warning in the permitted print fixture; preserve the value and carry the closed marker contract into the eventual approved design. Compare the SAME number under PASS and PROVISIONAL. Regrade AC4 before treating FWD-10 as realized.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-C-S13",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The identity fallback design note mixes MEASURED and INFERRED in its advertised coverage benefit.",
    "evidence": [
      "The measured-source limb passes independently: Overview row 2 in each original workbook names Ticker: IMB LN / IMPERIAL BRANDS and Ticker: SAP GY / SAP SE. All 34 measured identifiers are distinct. The decision-document limb fails: DESIGN_QUESTION_identity_fallback.md twice promises MEASURED-or-better coverage 34 to 49 while explicitly limiting all fallback values to INFERRED, never MEASURED. Those categories cannot share the claimed denominator. It also treats hypothetical renaming as a measured failure. Andrew would have to repair the benefit and evidence claims before ruling; correct them to 34 measured plus up to 15 inferred candidates, with downstream admissibility unresolved.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json records the two original workbook rows and 34 distinct MEASURED values."
    ],
    "remedy": "Correct the decision note to 34 MEASURED and up to 15 additional INFERRED candidates, not 49 MEASURED-or-better. Separate observed ambiguity from hypothetical renaming and state which downstream gates would still refuse INFERRED. Keep the fallback unimplemented pending Andrew's decision.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-C-S14",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The advertised impostor AND-clause executes as check1 OR check2, and verification is an untyped boolean.",
    "evidence": [
      "The copied-bio-only control is refused, but the implementation is strong = check1 or check2 and immediately returns official; it does not enforce the advertised AND with further evidence. Independent eight-case enumeration admits check2 alone and check1 alone. The worker also discloses that a non-identity-bound verification mark plus copied bio still passes; no external platform claim is needed to see that the caller contract never distinguishes identity-bound verification. The two passing fixture arms do not establish real official-versus-impostor discrimination. Preserve UNRESOLVED handles until the predicate and evidence contract are clarified and tested.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json contains all eight boolean cases, including (false,true,false) -> official and (false,false,true) -> impostor."
    ],
    "remedy": "Clarify the intended truth table and the identity meaning of verification; require the stated co-occurrence where intended. Add negative controls for verification without further evidence and for a mark that does not attest company identity. Keep all real handles UNRESOLVED; no social/vendor call or owner assignment is authorized.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-C-S15",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The fiscal join can select a future price and report a small absolute gap when no on-or-before observation exists.",
    "evidence": [
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json independent control: period_end 2025-12-31 plus only price_date 2026-01-02 returns price 100, gap_days 2.",
      "fye_join._nearest_price falls back to the nearest point in either direction; gap_days uses abs, so the under-45-days mechanical check accepts this direction violation. All 30 actual landed rows have zero such violations at this vintage."
    ],
    "remedy": "Return unresolved when no on-or-before price exists; add a future-only negative control and a direction assertion. Preserve the passing three-security sample and its exact pins. This is a bounded source defect, not evidence of a fourth live security failure.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-Z-C-S16",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The corrected fiscal block is a new engine output; current render consumers remain on the original model_block lane.",
    "evidence": [
      "Worker 1 r-1 declared_exclusions explicitly excludes replacing model_block artifacts and wiring provenance/print consumers. derive_fye_fixed.py writes derived/model_block_fye/.",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_ROUND2_CVO_EVIDENCE_20260911.json verifies the corrected S3 lane only; it does not show any consumer switched to it."
    ],
    "remedy": "Carry this as integration work for the next authorized cut: name and test the consumer path and its derived-artifact vintage before claiming the served analyst pack uses the corrected join. Do not overwrite peer outputs or implement round 3 from this slug.",
    "owner": "2.0.0_SA_COO~ZZZ",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZZZ",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZZZ",
      "at": null
    }
  }
]
```
