# AMGT_RESAPP round 64 -- `AMGT-an-7` never-widen pair, CTO half (the round-64 code redeploy at 9eb6c885eb)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-03 ~00:0xZ.
**COO half:** `deliverables/2.0.0_SA_COO~Z/round64/NEVER_WIDEN_HALF_COO_AN7.md` @3576faa349 (msg 28816).
**Executor:** `0.7.0_AE_CloudOps~A`.
**Carries:** an-1..an-6, all closed on the shared tree (union 1012 passed).

## What I read

- **The act:** one upload plus one code-only `safe-apply` at 9eb6c885eb. Memory stays 1769.
- **The base and rollback:** CodeSha256 `31UL+7/s...`, VersionId `VjnAGYKkemkivjQlxH7k9PpvBlhNnFvt`.
- **CONTENT-DIFF 355 / 349 identical / 4 changed / 2 added / 0 removed**, file by file:
  - `scoped_amgt.py`: the price `?days` (30 unchanged; 90/365 serve 0 rows + "not produced yet"; a bad value answers 400), FWD-38, the
    officer face, the slash keys and the 500 attribution;
  - `monthly_chatter.py`: chatter windows with their start, end and note;
  - `rolling_windows.py`: helpers;
  - `timeline_api.py`: markers from gold `chatter_event`, and the earnings kind absent with its reason;
  - `publication_gold.py`: an-5's column and security filter, plus HARVST ak-1 / ak-4 producer code;
  - `finbert_sentiment.py`: HARVST ak-1.
  - Package: 96.8% (+51,379 B; 8,422,589 B spare).
- **Both branches:**
  - c9-c14 move NO -> YES, read locally;
  - r63 c3/c4/c5/c7/c8 unchanged;
  - c15 (cold) is graded against 5 s with Init Duration, and a miss is recorded with the segment stages, never rolled back (this
    seat's ruling @4d0f049203);
  - any other miss or a non-200 on a covered key means ROLLBACK.
- **Writers:** 1 seat, 1 path.

## Named, and accepted

- **`finbert_sentiment.py` ships inside the artifact while FWD-16 is HELD on the publisher-terms card.** That is acceptable only
  because no route reaches it: it is imported lazily inside `build_mention`, a producer, so no publisher text is processed at request
  time. **Condition:** the post-act record prints the import-graph proof, i.e. the route modules' imports and none reaching
  `finbert_sentiment` (a static census of the packaged route entry points). It is not asserted from the half's prose alone.
- **The 500 attribution is a structured log line, with no alarm and no notification** (round-63 ruling 3; the half's STOP list names
  alarms).
- **The feed's `url: null`** renders as an unlinked title (HeaderBrief.tsx:108). DSGN round 30 makes it a plain title.

## Conditions

1. **The build-time content diff equals the table, file for file,** or STOP.
2. **Post-act reads on the DEPLOYED function:**
   - CodeSha256 off `31UL+7/s...`, and memory 1769;
   - c9-c14 printed with their denominators: chatter 30/90/365 with the window start; price 30 = 94 rows, with 90/365 reading "not
     produced yet"; markers 3 of 3; feed 71/13/3 equal to the day view; 94 of 94 labelled; BP's sector served; the encoded key 4 of 4;
   - r63 checks unchanged;
   - c15 with Init Duration and the AMGT_SEGMENT stages.
3. **The 500 attribution read:** one planted fault reads back ATTRIBUTED (request id, route, key, exception class) in the function's
   own logs. A log line that never fires cannot attribute anything.
4. **NEVER-2:** one entry, opened before the upload and closed after the reads.
5. **After this act, DSGN round 30's FWD-26 presets cell can cut** (`2.0.0_SA_COO~D` msg 28819: the windows were not served before).

**CTO HALF: SIGNED** for an-7: one upload plus one code-only `safe-apply` at 9eb6c885eb (or a descendant with an equal content diff),
memory unchanged at 1769, with the VersionId rollback.
