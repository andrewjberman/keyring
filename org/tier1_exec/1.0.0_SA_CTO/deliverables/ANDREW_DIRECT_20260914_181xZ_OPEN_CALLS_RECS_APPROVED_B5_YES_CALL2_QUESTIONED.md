# ANDREW-DIRECT 2026-09-14 ~18:1xZ (~2:1x PM ET) -- /open-calls at 1.0.0_SA_CTO~Z: recs approved; call 2 (the ad-hoc Bloomberg pull) questioned, still open

**Received at:** the `1.0.0_SA_CTO~Z` terminal, in-session, in reply to this seat's `/open-calls` frame (4 cards).
**Recorded by:** `1.0.0_SA_CTO~Z`, same turn.

## HIS WORDS -- VERBATIM AND ENTIRE

> "I am fine with the recs as youve listed them but have questions on call 2. I don't have any issue with recalling
> these, the data should be monotonic anyway; nothing should change aside from two additional data points as I
> understadn."

## THE CARDS HE ANSWERED (as put to him)

1. **POSN_ASTTAX: add a 10th cell, B5, so the edge router serves the two new satellite files?** REC: yes (production
   CloudFront distribution; an API change, not a portal promote; own change record, sign-off, rollback to the prior edge
   version).
2. **Run an extra Bloomberg ETF pull today to capture GLD/VXX a day early?** REC: no (it rewrites this morning's
   `bbg/2026-09-11/` keys for all 170 securities and relabels them ad-hoc).
3. **Should the ASCII check block commits instead of warning?** REC: keep warning; clean the 29 files first.
4. **Should the task-order gate also check edits to existing orders?** REC: hold where Andrew set it.

## READING -- stated narrowly

- **Calls 1, 3, 4: APPROVED as recommended.** B5 is approved as a round-5 cell (`AT5-s-9` in
  `decompositions/POSN_ASTTAX_DECOMP_round5.md` @`f381f6f402`). The ASCII check stays WARN. The task-order gate stays at
  its current scope.
- **Call 2: NOT closed.** He has questions and states an understanding ("monotonic ... nothing should change aside from
  two additional data points"). "I don't have any issue with recalling these" is recorded as his stance, NOT read by this
  seat as the per-use word for a download-class Bloomberg act while the question he raised is unanswered. This seat
  answers the question first; the pull runs only on his word after that answer.

## WHAT IT MOVES

- `2.0.0_SA_COO~Z`: B5 leaves PROPOSED-PENDING-ANDREW. The one issuance of nine cells follows once B5's CTO+COO
  never-widen halves are committed (pre-issuance step 3b).
- `1.0.0_SA_CTO~Z`: writes B5's CTO half; answers call 2.
