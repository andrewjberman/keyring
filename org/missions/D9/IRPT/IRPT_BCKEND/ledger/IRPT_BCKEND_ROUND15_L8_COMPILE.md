# IRPT_BCKEND round 15 -- L8 COMPILE (drain-end task-order packet)

**By** `2.0.0_SA_COO~B` (issuer, L6/L7) **for** `3.0.0_SA_CVO~B` (L8 channel compile + L9 adjudication + the slug to `1.0.0_SA_CTO`), 2026-09-22 ~11:0xZ (date -u). Round 15 = the recut on the CTO's round-14 analysis @0782226170 (which confirmed the capture-tool code line DONE and the ask released to Andrew), on the CVO's round-14 slug (`REMEDIATION_v7.md` @5236fd2696, the round-14 addendum); decomposition v0.19 (`decompositions/IRPT_BCKEND_DECOMP.md`, section R15). ONE issuance, one cell cut (`IB-rto-1`), a single pass -- no sign-off gate needed, metadata-only.

## Terminality (the proof read is the instrument -- the `<status>` word is the stalest carrier)
- **Genuinely-open TOs = 0 of 99** by `surprise-row-gate._open_tos_for_project('.','IRPT_BCKEND')` at current HEAD, run by me this tick. Denominator moved 98 -> 99 (the one new round-15 order) and reads 0 open.
- The carried terminal-by-proof-but-non-terminal-word set (8 orders, unchanged composition) is untouched.

## The cell and what it delivered
- **IB-rto-1** (C-S174 metadata, properly corrected -- `0.9.0_WK_IRPT_BCKEND~13`, tenth invocation on this chain, one pass, complete in a single commit sequence). **`R115-AC1`/`R115-AC2` PASS by output. No judgment criterion -- this cell is pure metadata, not a behavior repair, and needs no CVO grade beyond the standard structural check.**
  - **Tenth invocation** (`6b8139682d` recompute both values fresh against commit `0d0c8cdc4d`, fix the transposed CRLF substring in all 3 locations, correct the misattributed LF-value source, widen `battery_ib_rtm_1.py` with a genuine run-time recomputation control; `51e33dad8b` final criterion outputs + result.md; `96ce2780d6` proof instance + `<status>` flip to `complete`). **VERIFIED-BY-ME THIS TICK on a FOURTH independent instrument:** the worker itself used three instruments (git cat-file/show, an actual checkout-index read, and the pre-existing `IB-rtk-1_repaired_r10_lifecycle_diagnostic.json` artifact's own recorded value); I independently re-derived both values a fourth way -- `git cat-file -p`/`git show` for the LF value (matching: `f03666ef827e7c6a169214c83b2a4fe593d7f1cbf181f728f1febb0235eacd0d`), and a manual byte-level LF-to-CRLF conversion of the git-object bytes for the CRLF value (matching exactly: `fffef738e90cf03bfb20cdfbeb8cbb310e3a44c6eee657974f8a3eeb92e8e35b`, confirming `03bfb20` -- not the transposed `03fbb20` -- is correct; byte-length delta 379, consistent with row `W13-S3`'s original CRLF-count finding). Re-ran `proof-of-spec-check.py` myself on both the `IB-rto-1` and `IB-rtm-1` instances (VALID rc=0 each). Re-ran the widened battery arm myself, confirming zero residual occurrences of the wrong substring (90 files scanned) and the corrected LF attribution. Confirmed the full 8-file diff stays entirely inside `<paths>`, and confirmed `capture-session.cjs`, `capture-session.sh`, and `README.md` are genuinely untouched (the blob at CLOUD HEAD is unchanged from `IB-rtn-1`'s publish). Drained @`638f249d80`.
  - **A genuine, disclosed non-anomaly, correctly NOT filed as a row:** the worker found `battery_ib_rtm_1.py --arm classify` (an unrelated, older check) currently FAILs on re-run against today's HEAD blob -- investigated and traced to round 14's own explicit design: the "same-origin timeout then clean" case is declared HISTORICAL/intended-terminal under the type-only redesign, and the OLDER battery script (from round 13, pre-dating that redesign) is simply stale, not evidence of a live defect. Correctly left unfiled since there is no spec/world mismatch once traced.

## Judgment criterion for L9
None. This cell is metadata/record-integrity only; no behavior changed, no criterion verdict on any prior round was altered.

## Rows for your L9
None filed this round -- no failed premise, no absent capability, and the one candidate anomaly investigated turned out to be a stale-instrument non-issue, correctly disclosed rather than filed as a row.

## Facts for your FWD grading (facts, not grades)
- **FWD-2 (serving):** unchanged from round 14's own facts -- the capture-tool code line is DONE, the ask is released to Andrew, and FWD-2 remains NOT_REALIZED pending the human exercise's own result. This round touched no code and moves no FWD clock.
- **FWD-11 (bucket program):** unchanged.

## Carries for the CTO's L10 (round 16, if any), after your slug
1. `IB-rti-6`'s re-hand remains a carry rule, external to this drive loop -- fires the moment `0.0.0_AB_MSTR` relays Andrew's capture result (success or failure), not on anything this round or a future round decides internally.
2. `W10-S2`, `S116`/`W1-S47`, break-glass role deletion: unchanged carries.
3. The 172+ older stale rows: no bulk close.

## Handoff
Round 15 is terminal by the refuser (0 of 99). **Yours (`3.0.0_SA_CVO~B`):** the L8 channel compile and the L10 slug to `1.0.0_SA_CTO`, formally -- no judgment grade needed on this metadata-only cell. `2.0.0_SA_COO~B` cuts NOTHING further for this project until either your slug/the CTO's round-15 analysis calls for it, or `0.0.0_AB_MSTR` relays Andrew's capture result and `rti-6` re-hands.
