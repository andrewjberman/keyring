# IRPT_ANLREQ PRD v0.22 -- ratified-text half review (C-FILING-HINT, yfinance first): SIGNED

**Seat:** `3.0.0_SA_CVO~DELL2`, 2026-10-16 ~15:4xZ. **PRD:** `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` v0.22 @d5b6ba40a1.
Asked by `1.0.0_SA_CTO~DELL2` msg 9524. **Half reviewed:** ratified-text, half_hash
`01b1d1ea5352c9e6e6cd5892410739586b4d766da64d43318b52bb72a5c4de69` (was `8961c7ef3c05...` at v0.21 @08a2a01213).
endpoint_hash `f2cdb6557373...` is unmoved, so FWD-7 already said Yahoo first and YCharts second for prices.

## What I read

1. **The whole diff v0.21 -> v0.22** (27 lines added, 2 removed). The only contract text that changes is the one sentence at the head of
   C-FILING-HINT: the door's check asks yfinance first, a holding yfinance keeps at T-1 is KNOWN with no YCharts call, and YCharts is
   asked only for a symbol yfinance does not keep. The (A) and (B) branches, Yes / Replace / No, the retirement of NAME_PROXY and the
   routing of every UNRESOLVED holding to C-SWAP are carried word for word.
2. **The ground.** Andrew's words, quoted in the CRO's record
   `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261016_152xZ_YFINANCE_FIRST_YCHARTS_SECOND_EVERYWHERE_AND_YCHARTS_PACING.md`
   at line 14, match the PRD's quotation exactly. "Any part of this process" covers the door; the sentence does not reach beyond IRPT_ANLREQ.
3. **Coherence with the ENDPOINT.** FWD-7 already orders prices as estate, then Yahoo (cut at T-1), then YCharts, then C-SWAP. The door now
   follows the same order, so the filing check and the report's pricing can no longer disagree about whether a symbol is known. "At T-1"
   is the `lib/trading_calendar.py` frontier (PRD lines 424-425), so a Monday filing reads Friday.
4. **Direction of failure.** Each miss falls toward the existing tree, never past it:
   - A symbol yfinance spells differently (for example a class-share separator) is "not kept", so it falls to YCharts and then to the
     unchanged (A) or (B) branch.
   - A delisted ticker with no T-1 history is not kept either, so it cannot pass as KNOWN on stale history.
   - Nothing that was refused before is now passed without a check by some provider.
5. **No collision with "makes no vendor call at the form".** That clause binds the browser form. The check is the door's, which is
   server-side.

## Verdict

**SIGNED.** One sentence narrows YCharts use, as Andrew asked, and aligns the door with FWD-7's existing price order. Every other clause of
the half is unchanged.

**Notes for grading, not conditions:**
- Items 3 and 4 (no YCharts id for a Yahoo-priced holding; the per-window lease budget) are release work, not contract text. FWD-7's
  "no YCharts call end to end" is their test. The L9 grade reads the release's YCharts call count, never the absence of a WAF trip.
- Over-acceptance is the one new exposure: a typo that happens to be a real Yahoo symbol is now KNOWN at the door. The same was true under
  YCharts, so the exposure is not new. The report's per-holding disclosure is where it surfaces.

-- `3.0.0_SA_CVO~DELL2`
