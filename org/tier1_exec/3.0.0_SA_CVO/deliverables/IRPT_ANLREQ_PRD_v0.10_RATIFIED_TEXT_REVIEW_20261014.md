# IRPT_ANLREQ PRD v0.10 -- L4-R review, ratified-text half

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~16:1xZ. **Delivery:** msg 7741 (and 7743). **PRD:**
`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @c31b76cd19. **Compared against:** v0.9 @c642900a88, which this seat signed
(adffe99ed7).
**Authority read:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_160xZ_COMMENTARY_STANDALONE_BRANDED_PDF_AND_ATTACHMENTS.md`
@98eacceda3, line 12. ADDENDUM v0.10 quotes his answer to part (1) exactly. "2.) Yes do it" approved the CRO's separate read-only offer;
nothing in this half rests on it.

**Verdict: REFUSE. The ENDPOINT carries his word, but CONTRACTS still says the opposite.**

## The ENDPOINT against his word -- carried

- **FWD-1** lists four standalone attachments:
  - the original holdings upload;
  - the form selections as filed;
  - the Opal report;
  - the AI commentary as a STANDALONE branded Opal PDF, marked DRAFT.
- **ACCEPT** says each is its own attachment, and the commentary is not a page inside the report PDF.
- **FWD-3's DONE WHEN** renders the commentary as that standalone PDF and opens it from the ticket.
- **Unchanged:** FWD-2 and FWD-4 to FWD-7 are byte-equal to v0.9.

## Refusal -- C-PACKAGER disagrees with the ENDPOINT

The CONTRACTS row C-PACKAGER (line 107 at v0.10) is unchanged from v0.9. It reads:

"The package is four separate items: the original upload, the form as filled, the Opal report and the commentary draft. Its last hop
attaches them after the commentary; **the branded PDF is a later enrichment, not this hop**."

- **The conflict.** FWD-1 now puts a branded PDF (the commentary) in this hop. A reader of the contract takes "the branded PDF is a
  later enrichment" to exclude it.
- **The missing limit.** ADDENDUM v0.10 item 3 says the combined package PDF (report plus a commentary page) is never posted as a fifth
  item. That limit is the one that shapes the packager's output, and it lives only in the history.
- **Precedent.** This is the same class as v0.6's C-FIRM: the addendum moved the ENDPOINT, and the contract row that binds the hop was
  not restated.

**Fix (one row):** restate C-PACKAGER:
- the four standalone items: the original holdings upload, the form selections as filed, the Opal report, and the AI commentary as a
  standalone branded Opal PDF marked DRAFT;
- the last hop attaches them after the commentary PDF is rendered;
- the combined package PDF is never posted as a fifth item;
- one `package_principal`, firm-bound by its PROFILE row, never ALL.

## Note (not a reason to refuse)

FWD-1 item (1) now reads "the original holdings upload". His word was "the original holdings csv"; the form also takes XLSX, so
"upload" is the right noun.

-- 3.0.0_SA_CVO~DELL2
