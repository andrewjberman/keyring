# AMGT_HARVST ROUND 47 -- L8 COMPILE + L9 -- the silver writer keeps every column (at-4 PASS); batched upload PASS; universe widened as Andrew said (43, not 59); the collection outcomes NOT REALIZED (every leg stopped, declared set empty); L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-06 ~02:3xZ
**Input:** `2.0.0_SA_COO~H` `round47/ROUND47_DRAIN_END_PACKET.md` @`11f3af83c1` (54 lines, read to EOF), msg 29865. It was drained on the CTO ruling @`69ce080222` (Z-S89).

## Grades

| cell | read by this seat | grade |
|---|---|---|
| at-4 column union | `store.silver_append` calls `_union_keys` before `pa.Table.from_pylist` (`store.py:423-464`); the article path writes through the shared helper at `uploads.py:35`, so Z-W95-S2's exposure is covered by the same fix; this seat ran `test_at4_silver_union_keys.py` + `test_at4_mixed_prefix_reads.py`: 6 passed; damage census 0 | **PASS** |
| at-1 batched upload | AC2: the silver prefix reads 1 object against 100, rows identical 200/200 (mechanical, accepted) | **PASS** |
| at-5 widening | Andrew's record: "all Opal Securities and the research list being included in the run", then "Yes I do" to adding "the 59". 16 of the 56 were already in the run under fund keys, so 43 added is the faithful count. The scope is not widened, and ft stays held on his separate word | **PASS** |
| collection outcomes | per-leg report: sa 9 (account 402), barrons 145 of 234 (bot_check), ft 0 (held), bbg 104, wsj 154 (bot_check); `publisher_universe_verdicts` every publisher out, so the DECLARED SET is EMPTY | **NOT REALIZED**: FWD-1, 3, 7, 9, 10, 11, 13, 14 and 15 wait on a resume |

**The resume is Andrew's presence, not a seat's act.** Each blocked leg resumes only when he hand-solves its challenge while present, and sa only when the account answers 200 (CTO @`69ce080222`). That is a qualified wait with its reason and owner, so the outcomes read NOT REALIZED, not stalled.

## Rows

- `Z-W95-S2` (ARMED): GRADUATED here and DISARMED in REMEDIATION_v8, on at-4 @`23baacf0e1`.
- `Z-W95-S1` (INERT) is disarmed by the same fix.
- `Z-S87`, `Z-S88` and `Z-S89` are ruled and left for the analysis.

## L10 PRECONDITION

Every cell is terminal. `comp-surprise --armed AMGT_HARVST` read 1 (Z-W95-S2) before REMEDIATION_v8. **MET.**

```json
[
 {
  "id": "AMGT_HARVST-Z-C-S79",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-06T02:30:00Z",
  "one_line": "Round 47 L8/L9: at-4 column union PASS (store.silver_append unions each date group's keys before pa.Table.from_pylist, store.py:423-464; the article path writes through it, uploads.py:35; 6 at-4 tests pass on this seat's run; damage census 0); at-1 batched upload PASS (AC2 1 prefix against 100, rows identical 200/200); at-5 widening PASS against Andrew's word (scope = holdings + research list; 43 added, not 59, because 16 were held under fund keys); collection outcomes NOT REALIZED: every leg stopped (sa 402, barrons/bbg/wsj bot_check, ft held), declared set EMPTY.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "lib/research/harvest/store.py:423-464 _union_keys inside silver_append; lib/opal_data_harvest/uploads.py:35 the shared append helper",
    "pytest lib/research/harvest/test_at4_silver_union_keys.py test_at4_mixed_prefix_reads.py: 6 passed (2026-10-06, run by 3.0.0_SA_CVO~Z)",
    "org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261005_163xZ_HARVST_ADD_RESEARCH_NAMES.md verbatim scope",
    "deliverables/2.0.0_SA_COO_H/round47/ROUND47_DRAIN_END_PACKET.md section 2 per-leg table"
   ]
  },
  "disposition": "GRADUATED",
  "adjudicates": [
   "AMGT_HARVST-Z-W95-S2"
  ],
  "spec_asserts": "The collection outcomes are realized when publishers reach the declared set; every silver writer keeps every column.",
  "world_is": "The writer is fixed and the universe widened as Andrew said; no publisher reached the declared set before every leg stopped.",
  "notes": "Collection outcomes (FWD-1, 3, 7, 9, 10, 11, 13, 14, 15) stay NOT REALIZED until a resume, which waits on Andrew hand-solving each leg's challenge while present and on the SA account answering 200 (CTO @69ce080222)."
 }
]
```

-- 3.0.0_SA_CVO~Z
