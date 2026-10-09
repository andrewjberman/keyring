# AMGT_RESAPP -- round 88: mm-3 graded at L9 (dell1)

<sweep_watermark>2026-10-09T21:08Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T21:08:00Z. Asked by 2.0.0_SA_COO~R1 msg 3184 (CTO mm-4 half condition 1). mm-3: MET.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S39",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T21:08:00Z",
    "one_line": "AMGT_RESAPP.TO-AMGT-mm-3.three-repairs-selector-library-root-generated graded at L9 for the mm-4 GO (CTO half condition 1): MET. The code mm-3 ships holds: (1) lib/research/corpus/library.py raises LibraryAbsentError naming the path when OPAL_RESEARCH_LIBRARY_ROOT is SET but is not a directory, and never falls through to the derived candidates (row S3); (2) drafting_build.py sets generated=False exactly when the sentence served is the filing's own (swap is not None), the same branch that sets quote_method 'filing-sentence', and schema.json admits generated=false ONLY under quote_method 'filing-sentence' -- every drafted sentence stays generated true (row D1-W345-S2); (3) part (a), the watchlist selector refusal (D1-S18), stopped under the order's STOP clause (AMENDMENT 1 @b29adf045d) and ships no product change. AC1 24 passed, AC2 863 passed on this seat's run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "NEVER_WIDEN_ROUND88_MM4_CTO_HALF.md condition 1: the GO waits for AMGT-mm-3 graded at L9; spine L9.",
    "world_is": "AMGT_RESAPP.TO-AMGT-mm-3.three-repairs-selector-library-root-generated graded at L9 for the mm-4 GO (CTO half condition 1): MET. The code mm-3 ships holds: (1) lib/research/corpus/library.py raises LibraryAbsentError naming the path when OPAL_RESEARCH_LIBRARY_ROOT is SET but is not a directory, and never falls through to the derived candidates (row S3); (2) drafting_build.py sets generated=False exactly when the sentence served is the filing's own (swap is not None), the same branch that sets quote_method 'filing-sentence', and schema.json admits generated=false ONLY under quote_method 'filing-sentence' -- every drafted sentence stays generated true (row D1-W345-S2); (3) part (a), the watchlist selector refusal (D1-S18), stopped under the order's STOP clause (AMENDMENT 1 @b29adf045d) and ships no product change. AC1 24 passed, AC2 863 passed on this seat's run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran AC1 (three new test files, PYTHONPATH /c/tmp/stubfitz): 24 passed; AC2 (filings, drafting, corpus tests): 863 passed",
        "3.0.0_SA_CVO read git show 8492836089 -- library.py, schema.json, drafting_build.py; drafting_build.py:479-520 (swap and quote_method set on the same branch)",
        "task order AMGT_RESAPP.TO-AMGT-mm-3.three-repairs-selector-library-root-generated @c9610b8669, proof @368b03881c, AMENDMENT 1 @b29adf045d"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard: the code mm-3 ships graded MET by a seat that did none of the work."
  }
]
```
