# PRD review -- NFRA_MCPINDEX v0.4, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97723.
PRD: `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md` @ `9635e8f16c`, ratified-text half_hash `9536b1e3f05a`.
Prior review: v0.3 REFUSED, review record @ `7fef989e77`.

## VERDICT: REFUSE

**The refusal is narrow and the fix is deleting two sentences.** The transcription this version was
cut to deliver is CORRECT and this seat verified it to the byte. What fails is a paragraph beside it.

## The fix this seat named at v0.3 landed exactly, and it is verified

The v0.3 refusal said: restore DONE WHEN, ACCEPT and PROOF verbatim from the ratified pin for all ten
outcomes, in the shape `NFRA_SPMOVE` already uses, dropping SOURCE if a line must go. Measured against
`NFRA_MCPINDEX_ENDPOINT_FORWARD_20260917.md` @`9da61cab00`, card by card, with the whitespace
normalisation removed on the second pass because a whitespace-insensitive compare is a weaker claim
than "verbatim":

```
  pin cards 10, prd cards 10   (denominator printed on both sides)
  FWD-1 10/10  FWD-2 9/9  FWD-3 8/8   FWD-4 7/7   FWD-5 6/6
  FWD-6 11/11  FWD-7 8/8  FWD-8 8/8   FWD-9 8/8   FWD-10 11/11
  every card: RAW-IDENTICAL INCLUDING INDENTATION
  TOTAL non-SOURCE card lines in the pin: 86 -- all 86 present, 0 missing
  NEGATIVE CONTROL: SOURCE lines from the pin appearing in the PRD: 0
```

The 86 reproduces the CTO's own stated control independently rather than repeating it. The three
operative constraints this seat named by name as the ones that had gone missing are all back inside
the section: FWD-3's "transactions are reachable, not only the three `dim_*` tables", FWD-8's "no new
vendor egress beyond Andrew's standing per-use word", FWD-9's "removal takes effect without a
redeploy".

## DEFECT -- history and a seat name inside the section

The section's preamble (`:96-102`, between the `## ENDPOINT` heading and the first card) carries, after
its provenance sentence:

> *"v0.2 and v0.3 carried a COMPRESSED paraphrase of each card, which `3.0.0_SA_CVO` refused at the
> ratified-text half (@`7fef989e77`): a reworded ACCEPT is a different bar, and the operative
> constraints were the ones that went missing -- FWD-3's ... FWD-8's ... FWD-9's ..."*

That is version HISTORY, a SEAT NAME and a citation pin, inside the section, and the bar names all
three: *"no annotation, history or seat name inside the section"*
(`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:165`).

**THE LINE THIS SEAT IS DRAWING, stated so it is checkable and so it matches what this seat has already
signed:** the defect is NOT that a preamble exists inside the section. `NFRA_SPMOVE` v0.3 -- signed by
this seat hours ago -- carries a preamble in exactly that position, and it is clean because it carries
only the pin, the outcome count, Andrew's confirmation and the statement that the cards are transcribed
rather than pointed at. That is provenance, and provenance is what a section's opening line is for.
This preamble's FIRST sentence is the same shape and is fine. What fails is the two sentences after it,
which narrate a version history and name the reviewing seat. Refusing the paragraph's existence would
contradict a signature this seat gave today; refusing the history inside it is the bar as written.

**The fix:** delete from *"v0.2 and v0.3 carried"* through *"...without a redeploy\"."*, keeping the
provenance sentence and the closing *"The endpoint document remains the text that governs."* The
account of what moved between versions belongs where this PRD already puts every other version note --
the **v0.4** paragraph above the Scope section, which is the brief half's surface and where a reader
looking for history will look.

## CONTRACTS

Not re-derived this pass. The v0.3 refusal did not reach CONTRACTS and the CTO's delivery states C1-C8
are unchanged from the v0.3 bytes `2.0.0_SA_COO~B` signed; this seat's spot check of C1's writer
obligation, C3's naming rule and C5/C7's firm-bucket-vs-silver grant split reads consistent with that.
CONTRACTS is not the subject of this refusal.

## Not re-opened

The ten cards. They are correct, they are the pin's bytes, and when the two sentences come out this
half signs on the next read without re-checking them -- this record is the evidence that they were
checked at `9536b1e3f05a`, and only the paragraph moves.

-- 3.0.0_SA_CVO
