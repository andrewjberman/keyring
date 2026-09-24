# L4-R REVIEW -- AMGT_CORPUS PRD v0.6, BRIEF HALF -- verdict: SIGN

**Reviewer:** `4.0.0_SA_CRO~Z` (the fabric's CRO lane; the two briefs are `4.0.0_SA_CRO~F`'s and `4.0.0_SA_CRO~Y`'s, both named in
the PRD for consultation). **PRD:** `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md` @`031c3a3a3e` (v0.6; HEAD
`bb85c73a75` identical bytes; working tree clean; brief half hash `5bb18cab32d2`). **Vintage note:** the review request (msg
25280) named `8da812bf80`; `031c3a3a3e` (06:18Z) changed exactly two lines of this PRD, `:661` and `:694`, re-heading A.4 and
A.5 as `## CONTRACTS -- A.n ...` so the tool routes them RATIFIED (the CVO's catch, "nine contracts hashing into the brief
half"). The scope and checks below are stated at `031c3a3a3e`; the ratified half is STALE and re-owed to `3.0.0_SA_CVO~Z`. **Briefs:** header `brief_ref`
`docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md` @`6c52138c2f` (unchanged since the v0.3 stamp); ADDENDUM A's
`docs/briefs/amgt-corpus-dossier-fold-brief-20260924.md` @`328e17d5e5` (PRD `:313`, `:594-595`). **Prior brief-half stamp:** v0.3
@`c94a6bb2ef`, half hash `4bdca847a391`, `2.0.0_SA_COO~Z`. **Requested by:** `1.0.0_SA_CTO~Z`, msg 25280, 06:10Z, half hash
`a573ab31ffc4`. **Reviewed:** 2026-09-24 06:2xZ-06:3xZ.

## Scope -- the span runs from the last SIGNED brief bytes

`git diff -U0 c94a6bb2ef 8da812bf80 -- <PRD>`: v0.3 -> v0.4 -> v0.5 -> v0.6, 387 insertions, 13 deletions, twelve hunks.

| hunk (lines at 8da812bf80) | half | what |
|---|---|---|
| `:8`, `:10`, `:20-30` | header | v0.6; the `" (36,007 bytes)"` annotation stripped from `brief_ref` (pin value unchanged); `FWD-10`..`FWD-19` appended; the v0.5 `addendum_a_brief_ref` key added then DROPPED at v0.6 (msg 25284) |
| `:36-37` | brief (preamble) | driver named: `2.0.0_SA_COO~X`, seated 2026-09-23 ~01:5xZ |
| `:111-150` | brief (preamble) | the v0.4 change note: `FWD-4` re-cut to produce the executable induction request, `C-NO-VENDOR-CALL` untouched at that vintage; the header annotation correction |
| `:221-244`, `:312-420` | RATIFIED (ENDPOINT) | `FWD-4` amendment and the ADDENDUM A fence `FWD-10`..`FWD-19` -- `3.0.0_SA_CVO~Z`'s, signed 05:40Z at `b522c794c657`; not graded here |
| `:552` | brief (Rule 28 cards) | card K3 (PDF extractability) struck through and CLOSED by A.2's measurement, 99 of 99 on the control |
| `:586-660`, `:735-777` | brief (ADDENDUM A) | A.1 numbering refused, A.2 the brief's stale O7 passages, A.3 the ten outcomes' reasoning and `FWD-19` by subtraction, A.6 manifest rows and card K6, A.7 what it does not do, A.8 L4-R |
| `:661-734` | RATIFIED | `## CONTRACTS -- A.4` (`C-NO-VENDOR-CALL` amended) and `## CONTRACTS -- A.5` (five new contracts): routed to the ratified half by their headings' first word, exactly as `prd_signoff_lib.top_sections` reads them |

## Content carriage against the dossier brief @`328e17d5e5`, by pinned line

| PRD claim (line) | brief line(s) | result |
|---|---|---|
| A.1: the brief says its `O1` "becomes `FWD-1` of the addendum" (`:606`) | `:46` | verbatim; the collision with the PRD's own `FWD-1` (`:176`) is real, and `:35` does say `FWD-1`..`FWD-9` do not move |
| A.1: `O1`..`O9` become `FWD-10`..`FWD-18` in the brief's order | headings `:48, :57, :63, :71, :77, :84, :91, :108, :115` | order preserved |
| A.2: the O7 amendment and F2 supersession (`:97-106`, `:187-190`) settle extractability at 26 of 30, 29 of 30, 99 of 99 | `:97-106`, `:187-190` | verbatim figures |
| A.2: three later passages still call it unmeasured, two as directives (`:280-282`, `:285-286`, `:404-405`) | `:282` "UNMEASURED and is the first thing the cut should measure"; `:285-286`; `:404` "the first cell to measure" | correct, and the ruling that the amended text governs is right on vintage and on the package hash |
| A.3: "backfill" appears once, in a REFS filename (`:423`); `add_security` nowhere; population is the 93-folder list (`:79`, `:267`) | `:423` only; zero hits; `:79`, `:267` | correct; `FWD-19` is genuinely by subtraction from Andrew's ~04:3xZ word |
| A.3: `FWD-15` and `FWD-18` are marked PROPOSAL by the author (`:86`, `:117-118`) | `:86` (O6), `:117-118` (O9) | correct |
| A.5 limit 3: the Model-block pull has its own per-use word (`:253-254`, `:400`) | `:253-254`, `:400` | correct |
| A.7: the brief puts the induction ACT in `AMGT_RESAPP` (`:197`) | `:197` "the act is `AMGT_RESAPP`'s" | correct, and naming the L5 question there is the right place |
| A.6 R12 home `harvest / gold / research-dossier` | brief VIII-2 (`:318-347`, measured on the live bucket) and `C-DOSSIER-TABLE-SPELLING` | consistent, hyphenated |
| A.6 K6 closed by Andrew's ~05:0xZ word | `ANDREW_DIRECT_20260924_050xZ_AMGT_GOAL_AND_COMPLETION_TEST.md` (cited in RESAPP ADDENDUM B) | the quoted sentence matches that record |

The analysis-layer brief's BRIEF COVERAGE table (`:429-435`) is byte-unchanged since the v0.3 stamp and is not re-reviewed.

## Findings

**F1 -- note, no correction owed.** The PRD's L4-R section (`:576`) names the brief's author as `4.0.0_SA_CRO~F` and A.8 (`:773`)
names `4.0.0_SA_CRO~Y`. Both are true of different briefs (the analysis layer and the dossier fold) and the reviewer is the lane
either way; no text is wrong.

**F2 -- note, no correction owed.** A.3 records that the first cut defined the outcomes in the addendum and the header and the
surface-manifest gate refused it; at these bytes the definitions are in the ENDPOINT fence only (`:312-420`), the header carries
ids only, and A.3 carries reasoning only. One carrier, verified.

**F3 -- observation for the CTO, no correction owed here.** The device that makes A.4 and A.5 ratified text -- heading a section
`## CONTRACTS -- A.n` so the tool's first-word routing hashes it into the CVO's half -- is the fix the sibling `AMGT_RESAPP`
ADDENDUM B lacks (this seat's refusal of that half, same hour). It is named here because a reader of one addendum will assume the
other was built the same way.

No finding touches the brief half's content carriage. The v0.4 change note and the driver line are consistent with the records
they cite (msg 24530; the seating at ~01:5xZ). The one manifest row change is in the `serves` column and names outcomes that
exist.

## Verdict

**SIGN.** Every ADDENDUM A claim about the dossier brief resolves at the brief's pinned bytes; the two rulings against the brief
(A.1 numbering, A.2 stale passages) are correct on the evidence and are the CTO's to make; the contracts sit in the ratified
half where the CVO signed them. Bound with `--expect-half-hash` to the bytes the tool prints for this half at `8da812bf80`.
