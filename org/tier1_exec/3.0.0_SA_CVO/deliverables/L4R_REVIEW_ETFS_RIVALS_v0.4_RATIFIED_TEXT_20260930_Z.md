# L4-R ratified-text review -- ETFS_RIVALS v0.4 @7aba7bcc4d (CONTRACTS only: C-HOME-PRODUCER)

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~20:4xZ - **Asked by:** CTO~Z msg 27364
**Span:** from this seat's own signed bytes (v0.3 @`3027a47dc0`) to `7aba7bcc4d`. The ENDPOINT hash is `6015445bf712` at both, so there
is **no ENDPOINT change**. One hunk, in C-HOME-PRODUCER.
**Andrew's record read:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_202xZ_ETFS_RIVALS_LEAVE_POSITIONING_PULL_ALONE.md`
@`6bd8185eb6`, in full.

## THE CHANGE

- **v0.3:** "If not, the fund joins this pipeline's Bloomberg request and the old pull stops writing that fund in the same window." and
  "**Never two producers of one fund's holdings** (CLAUDE.md, no duplicate output path)."
- **v0.4:**
  - the Positioning pull is not modified and keeps landing IDVZ and PFOE;
  - where it is short of the grain, "this pipeline lands its own copy";
  - each pipeline reads only its own landing;
  - "This v0.4 line replaces v0.3's 'the old pull stops writing' and **'never two producers of one fund's holdings' on his word.**"

## THE GROUND -- a relay that lifts a hard stop the relayed words do not lift

1. **His words, verbatim:** "Ignore RVs comment about ETFS pull for positioning, their idea is stupid, **we're leaving the existing
   pull alone**." The record's own scope section says the pull is not modified, "no stop and no narrowing", and that the "old pull
   stops" clause is superseded.
   - **That supports removing "the old pull stops writing".** This seat agrees with that part.
2. **His words do not address a second producer of IDVZ and PFOE holdings.**
   - "Never two producers of one fund's holdings" is the PRD's own citation of a CLAUDE.md HARD STOP: "NEVER stand up a
     shadow/build-alongside pipeline, duplicate output path, or standing parity comparator (Andrew complete veto)".
   - v0.4 lands a second copy of the same two funds' holdings, from the same vendor. v0.3 itself named that a duplicate output path.
3. **Striking that line "on his word" attributes to Andrew the lifting of his own veto.** His quoted words contain no such lifting.
   - CLAUDE.md section 2(b): "verbatim scope; relay, never adjudicate wider or narrower; **if wider seems plausible, ASK**."
   - Wider is plausible here. He may well accept two landings at different grains for different consumers. But the veto is his to
     lift, and the text cannot record it as lifted before he says so.

**What is not in dispute:**
- the one-writer-per-landing and read-only-your-own-landing clauses are sound design;
- the ENDPOINT is untouched;
- the rest of the CONTRACTS half stands as signed at v0.3.

## VERDICT: REFUSE (one clause)

**Remedy: one of two.**
- **(a) Put one question to Andrew:** "IDVZ and PFOE would land twice: the Positioning pull as is, and ETFS_RIVALS's own daily
  holdings at its grain, each read only by its own consumers. Does that stand under your no-duplicate-output veto?" On his yes, v0.5
  quotes it, and this seat signs from this review.
- **(b) Drop the second landing:** ETFS_RIVALS reads the Positioning pull's landing for IDVZ and PFOE and accepts its grain for those
  two funds. The shortfall RIV-m-1 measured is then stated as a limit on FWD-2/3 for the home funds.

Either way, the text must not attribute the veto's lifting to words that do not contain it.
