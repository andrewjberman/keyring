# L4-R review -- IRPT_ANLREQ v0.5 brief half -- REFUSE (three pinned corrections, one coverage gap)

Reviewer `4.0.0_SA_CRO~DELL2`, 2026-10-13 ~19:1xZ, on `1.0.0_SA_CTO~DELL2` msgs 7166 / 7168.
PRD `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @e977af93bf (v0.5, half_hash e8470027de57).
Brief `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_223xZ_ANALYSIS_REQUEST_END_TO_END_ONE_PROJECT_CLOSER_TRACE.md` @2b21a349d1.
Later word read beside it: Andrew's dell2 voice memo, quoted in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md` @4e963d4a12 (section 1.1, :55).

## Denominator

The brief at its pin holds 14 items: 8 in "The journey he names" (step 1: 4, step 2: 1, step 3: 3) and 6 in "What he directs".
BRIEF COVERAGE (:144-161) holds 14 rows, so the heading denominator matches. All 14 rows were read against the brief's text.
11 of them carry their content and stand. 3 do not, and one brief item is now carried by nothing.

## Why REFUSE

v0.5 changes FWD-1 (:28-40) to Andrew's four separate attachments and moves the branded PDF out: "the branded Opal PDF with
the commentary inside is a later enrichment, not FWD-1" (:37). The memo is a sound source for that narrowing. But coverage
row 8 still claims FWD-1 carries the branded PDF, and section 3 has no enrichment item for it. A brief item that is still
open therefore has no carrier in the PRD, and the coverage table says the opposite. The direction file (:152-155) defers the
PDF; it does not drop it.

## Corrections (by pinned line @e977af93bf)

1. **:155, row 8 (the package).** Re-carry the row in two parts:
   - FWD-1 carries the four items the 10-13 memo names: the original upload, the form as filled (J6, a new package kind), the
     Opal report, and the commentary draft. Each is a pointer through `POST /tickets/{id}/package` (C-PACKAGE) by the one
     packager (J5).
   - The brief's "branded Opal PDF with the investment commentary" moves to section 3 as a named enrichment, with its source
     (memo section 1.1; direction :152-155).
   - Proof gap: four pointers set on one ticket and each one opened from the ticket page (direction :145), not the signed-link
     open alone.
2. **:117-123, section 3 (ENRICHMENT BACKLOG).** Add the item the row-8 fix points at: "the branded Opal PDF with the
   commentary inside, rendered by the Opal engine's layout (L4 ruling 1, S4), attached as one more package kind after FWD-1."
   Without it, brief item 8's PDF has no carrier.
3. **:152, row 5 (who files the ticket).** The brief's step 1 reads "an advisor or Opal person opens the ... form". v0.5
   narrows this: "Opal staff do not file in the Ticket Center" (:250, the memo), the driven arm is a synthetic
   partner-firm advisor, and `2e30` is SUPERSEDED (:242-243). The row should carry that narrowing and its source, and its
   proof gap should name the synthetic-advisor filing, never minted or left live outside its never-widen pair.
4. **:151, row 4 (typo check and swap).** The row is stale against C-SWAP (:104). It names `resolution_kimi.py` as the swap
   backend and `KIMI_WEB_SEARCH_UNVERIFIED` as the proof gap, but C-SWAP retires the model-proposed swap. It should carry
   C-SWAP's content: KNOWN, then a yfinance check (KEEP), then classify, then a deterministic proxy from the designated-proxy
   table, then RECORD with `proxy_for` / `method` / `confidence`. It should name the proxy table as MDPF_SECCLASS's (dell1)
   pre-arranged input. The proof gap becomes the C-SWAP path exercised on one unknown holding. This row passed at v0.3; the
   refusal is the time to bring it current.

Rows 1-3, 6, 7 and 9-14 stand as written.

## Outside this half (for `3.0.0_SA_CVO`, the ratified-text half)

Three passages still treat the PDF as FWD-1's last hop, which contradicts the v0.5 ENDPOINT:
- C-PACKAGER (:101): "The package's last hop is the branded PDF render";
- section 1 hop 7 "Package PDF" (:91);
- S4 "and the PDF render" (:139).

The v0.5 addendum's J5 (:257) says the packager runs after the commentary. This is recorded here for the CVO's read and is
not part of this refusal.

## Cost to clear

A coverage-table and backlog edit, with no ENDPOINT change, so the ratified-text half does not re-open on it. Re-deliver and
this seat re-reads only rows 4, 5 and 8 and section 3.
</content>
</invoke>
