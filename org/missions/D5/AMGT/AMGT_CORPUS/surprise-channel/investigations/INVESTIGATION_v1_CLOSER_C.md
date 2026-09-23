# Corpus closer observations, September 23

```json
[
  {
    "id": "AMGT_CORPUS-Z-S5",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~X",
    "surfaced_at": "2026-09-23T16:57:06Z",
    "one_line": "The literal c-11 mixed simple/specific icacls deny mask blocks child traversal; documented specific DE rights support readable write-denied copies.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "evidence/negative_control.log in deliverables/2.0.0_SA_COO~X: deny rc5 after processing root, Access is denied on children; remove-deny rc0; no ingestion attempted.",
        "Local icacls /? separates simple W/D from specific DE,DC,WD,AD,WEA,WA; a disposable control using the latter preserves reading and refuses create/append.",
        "evidence/negative_control_specific_rights.log: deny rc0; create/append PermissionError; ingestion stored123, existed123, put_performed0, read_failed0; actual_s3_puts0."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Original c-11 requests icacls /deny user:(OI)(CI)(W,D,DC,WD,AD,WEA,WA) /T and then read-only ingestion.",
    "world_is": "The original mask prevents the traversal needed by the instrument itself. The corrected specific-rights mask preserves reads; CTO 24818 additionally requires explicit read, write-denial and ingestion controls.",
    "notes": "Retain original failed instrument as NOT_EVALUATED at dependent ingestion level. Final negative_control_root_bound.log prints and asserts resolved copy root plus env source before ingestion, read OK, create/append/overwrite denied, 123 retained byte matches, actual_s3_puts0. CTO 24841 restores C01 PASS on this four-control evidence. Routine review remains pending."
  },
  {
    "id": "AMGT_CORPUS-Z-S6",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~X",
    "surfaced_at": "2026-09-23T17:00:28Z",
    "one_line": "Corpus period sorting and its checker compare raw strings, placing live FY2024/FY2025 reports after 2026-dated reports.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~X",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/research/corpus/typed.py period_order_ok and _order_reports compare raw period strings at base db3267d079.",
        "deliverables/2.0.0_SA_COO~X/evidence/I4_RETAINED_PRE_PERIOD_FIX.json: IMB_LN_Equity prior_reports lists 2026-07-17 before FY2024 and FY2025."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FWD-2 requires a security query to return reports in period order; C02 requires period reconciliation.",
    "world_is": "All 123 admitted lineages match, but the format prefix FY defeats chronological ordering; the checker mirrors the same lexical premise.",
    "notes": "CTO 24824 policy implemented in candidate: declared year and comparable-unit sequence, stable or explicit filing-date rendering for incomparable periods, separate tie evidence, independent all-pairs validator. Five regression controls pass including the planted 2026-before-FY2025 reversal and a Q3/FY/Q1 inversion. Candidate remains subject to independent review; no dates or identities are invented."
  },
  {
    "id": "AMGT_CORPUS-Z-S7",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~X",
    "surfaced_at": "2026-09-23T17:36:00Z",
    "one_line": "H independently reproduced scanner false negatives in lambda/class scopes and parameters shadowing safe globals at d382f2a30e.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~X",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "H review b04336c4d8: REVIEW_C_d382f2a30e.md/json and review_c_candidate.py in AMGT_HARVST_CLOSER_Y_20260923.",
        "New test_nested_scopes_and_parameter_shadowing_fail_closed reproduces the three reports and related closure/argument cases; corrected focused suite38PASS, full corpus149PASS."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The C01 static instrument counts library-directed write calls across corpus Python source, including ordinary lexical scopes.",
    "world_is": "The original scanner skipped lambda and class bodies and inherited safe globals over same-named parameters. Zero reported writes was therefore insufficient evidence despite passing producer tests.",
    "notes": "Original static-census zero-write claim withdrawn. Candidate visits module/function/async/class/lambda scopes, carries lexical closures while skipping class bindings for methods, and treats all parameter kinds as unknown even when defaults/globals are safe. Local assignments start unknown. Thirteen new controls pass. Corrected producer census28files/27write-like/0library requires H re-review; copied-library execution and period-order evidence remain separate. No actual source-library mutation inferred."
  }
]
```
