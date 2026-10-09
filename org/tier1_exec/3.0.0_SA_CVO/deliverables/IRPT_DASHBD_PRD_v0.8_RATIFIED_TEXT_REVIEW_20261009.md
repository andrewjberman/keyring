# IRPT_DASHBD PRD v0.8 @e8b44a8379 -- ratified-text half review (L4-R)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~03:4xZ, on `1.0.0_SA_CTO~DELL2` msgs 2320 and 2323. **Previous signature:** pin
2cb022f549, ENDPOINT hash f67287ce982d.

## What changed

A section diff against 2cb022f549:
- **ENDPOINT:** one addition, FWD-11 (12 lines).
- **CONTRACTS:** byte-identical (13,882 characters).

## FWD-11 against Andrew's word

Verbatim (record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/ANDREW_DIRECT_20261009_033xZ_ALL_CLIENTS_NOT_ONLY_49F.md`
@9a0a87676b): "You should be doing this not just for 49 Financial, but for all clients, inflection and cottonwood too."

The title, DONE WHEN, the per-firm adapters and the "says so in a sentence" clause for a figure a source cannot supply are faithful.

## Verdict: REFUSE, on one clause

The ACCEPT line states: "Cottonwood's return is tied out against Black Diamond's own return as 49 Financial's is (FWD-8)". That is an
unread fact written into the ratified text as an operative constraint:
1. **Andrew's word names no tie-out source.**
2. **The record of his word lists it as unread.** Under "Not read yet" it says: "what the tie-out comparison source is (49 Financial's is
   Black Diamond)... The first cell per firm reads them."
3. **The evidence points elsewhere.** Cottonwood's reported returns, the ones ADVI_COTBKF has graded against for 26 rounds, are
   Commonwealth's, under `s3://opal-data-assets/commonwealth/cottonwood/`. CLAUDE.md rule 13 also states that cot is a separate firm from
   bd.
4. **Inflection's tie-out is not stated at all.** The ACCEPT is asymmetric.

Signing this would bind the build to compare Cottonwood with a source that may not hold its accounts.

**Fix (one line):** "each firm's return is tied out against that firm's own reported source, as 49 Financial's is against Black Diamond
(FWD-8); the source per firm is named by the first cell's read". On those bytes this seat signs.

## Note, not a refusal ground

FWD-11's SOURCE line cites a record path that contains a seat serial (`deliverables/2.0.0_SA_COO~D2/...`). A file path is a citation, not
a seat annotation, so it stands. The ENDPOINT already carries 'COO~P record "under 2 s"' from the version this seat signed.
