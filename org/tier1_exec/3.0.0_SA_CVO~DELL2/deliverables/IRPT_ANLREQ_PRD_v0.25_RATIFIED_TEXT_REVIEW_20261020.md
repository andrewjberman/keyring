# IRPT_ANLREQ PRD v0.25 -- ratified-text half review: SIGNED

**Seat:** `3.0.0_SA_CVO~DELL2`, 2026-10-20 ~16:2xZ. **PRD:** `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` v0.25 @b83ce81b5b
(half_hash `d8647f6134ed...`). Asked by `1.0.0_SA_CTO~DELL2` msgs 11424 and 11426.

## What I read

1. **The diff v0.24 @7b55cfefe1 to v0.25 @b83ce81b5b** (75 lines added, 2 removed):
   - FWD-9 to FWD-12 appended, with FWD-1 to FWD-8 unchanged;
   - the outcome list extended;
   - C-MODEL-SOURCE and C-AUDIT-RECORD added;
   - ADDENDUM v0.25.
2. **The ratified pin.** The approved draft is
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_IRPT_ANLREQ_REPORT_ENGINE_20261020.md` @bffa5709a9, approved through
   `ANDREW_DIRECT_20261020_160xZ_FWD_9_TO_12_DONE_WHEN_APPROVED.md` ("These are approved as written.").
   - Compared by normalised text: FWD-11 and FWD-12 (DONE WHEN and ACCEPT) and the ACCEPT lines of FWD-9 and FWD-10 are verbatim.
   - FWD-9's DONE WHEN adds "It does not hold FWD-10". FWD-10's adds "a model comparable's window starts no earlier than 2024-04-30
     (C-MODEL-SOURCE)".
   - Both clauses are the "two built-in readings" the approval record says were restated to Andrew before his "approved as written".
     They are within his approval.
3. **Overlap with FWD-7.** FWD-7 is the price-source chain: estate, then Yahoo, then YCharts, then C-SWAP. FWD-10 is the comparison
   content: returns, risk, chart and allocation per comparable. They are disjoint axes. FWD-10 consumes FWD-7's prices, and v0.23's "O7
   stays FWD-7's" is now carried by FWD-10 and FWD-11 for content.
4. **The contracts.** C-MODEL-SOURCE names one firm-neutral model series (inception 2024-04-30), which agrees with FWD-10's window clause,
   behind one read grant under a never-widen pair. C-AUDIT-RECORD is a new family beside `ycharts_runs`, with a published schema and
   builder-made addresses (C-NAMES).

## Verdict

**SIGNED.**

**Notes for grading, not conditions:**
- **FWD-9 is Andrew's own verdict by construction**, so it is a wait on Andrew. It is qualified as rule 27 requires: his word ("I just need
  to see that export in a sample run to gauge ...") and his approval of it as written, and it holds nothing else ("does not hold FWD-10").
  It is graded on his recorded verdict, never inferred.
- **The addendum's front-end line** has the form ask for an "Advisor presenting, pre-filled with the filer and required". FWD-2's DONE WHEN
  says "no advisor-email field", and Andrew's 10-19 words were "we should not need to write what email". The grade of FWD-2 reads whether
  that field requires the filer to type or choose anything. Pre-filled and unchanged meets it; a typed email does not.

-- `3.0.0_SA_CVO~DELL2`

## Re-review at v0.26 @62631269b7 (2026-10-20 ~17:2xZ): SIGNED

- Half reviewed: ratified-text, half_hash `ac5cbec71969b8d3b8071b21a800f8378f6af90d555e4a71ec7cfe438246a240`.
- The only change is C-SWAP step 3:
  - the classifier model is `kimi-k3`, not kimi-k2.6;
  - there is no web search until a verified web-search receipt exists;
  - a pick below 0.80 is still FLAGGED, the output is still bound to the live vocabulary, and the model still classifies and never picks.
- Read at the cited lines:
  - `infra/aws/lambda/v2_portal/_shared/etf_classification_model.py:42` is `MODEL = "kimi-k3"`;
  - `infra/aws/lambda/investor-reporting/intake/resolution_kimi.py:160-165` returns `KIMI_WEB_SEARCH_UNVERIFIED` unless the search
    capability is verified with a QA receipt.
- The contract narrows to what the code does, with the same vendor (C-KIMI) and no ENDPOINT change.
- Proportionate sign-off is written for single-round or sub-week projects, and IRPT_ANLREQ is neither. This seat therefore re-binds to the
  current bytes rather than resting on "current by ENDPOINT hash". **SIGNED.**
