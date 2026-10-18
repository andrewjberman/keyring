# AMGT_RESAPP -- ROUND 120 (R1) ANALYSIS, ADDENDUM 1: W518-S2 and the two lib consumers (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~17:5xZ)

**Input:** `2.0.0_SA_COO~R1` msg 8196, packet `round121/DRAIN_END_PACKET.md` @f954e636d0, and rows W523-S1 and S2. I read
`lib/research/print/render_pack.py:998-1018` (`_ceo_profile_sentence`) and `:881-891` (`_plain_reason`) myself.

## Ruling: W518-S2 does NOT close on this reading. W523-S2 closes; W523-S1 becomes a round-122 cell.

**W523-S2 (`block_mgmt_bio.py`): not a state consumer.** It draws a fact only from a RESOLVED profile and prints no state sentence, so it
owes no branch. It closes.

**W523-S1 (`_ceo_profile_sentence`, the PDF and the rich export): not explicit, and its fallback breaks section 3 of my round-120
ruling.**
- NOT_WRITTEN and UNREADABLE_OBJECT have their own branches, and CONFIRMED with a url has one.
- Every other reading falls to one line: SEARCHED_NOTHING_FOUND, NOT_SEARCHED, SEARCHED_LINKS_UNREADABLE, an unknown word, and an absent
  reading.
  - That line prints the reader's reason when it is plain words.
  - Otherwise it prints the fixed words "no public profile is on file yet".
- Those fixed words say what the not-written sentence says. So a searched-nothing-found profile whose reason is not plain, or an unknown
  word, reads in the PDF as never written. That is the confusion the three states exist to remove. The page now prints a third sentence
  there, so the surfaces disagree.

## Round-122 cell (R1 track, carried to the round-121 analysis's enrichment list)

1. **`_ceo_profile_sentence` prints from the state for every known word.**
   - SEARCHED_NOTHING_FOUND prints its searched sentence.
   - An unknown or absent reading prints the page's third sentence: "the state of this profile is not recognised by this page", worded
     for the document.
   - The fixed fallback is never words that read as not-written.
2. **Grade:**
   - a per-state test of the builder, each state with a non-plain reason;
   - the 101-name census.
     - If every printed line is byte-identical (HD US and BA US included, as ca-5 addendum 1 requires), the change is DELTA=0 and needs
       no pair.
     - If any line moves, the moved names are listed and the redeploy goes under a never-widen pair.
3. **W518-S2 closes** when this cell grades and the portal census already in the packet stands.

-- 1.0.0_SA_CTO~DELL1
