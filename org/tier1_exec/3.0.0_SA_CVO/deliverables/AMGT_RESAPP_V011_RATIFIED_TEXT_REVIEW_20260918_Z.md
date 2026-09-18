# AMGT_RESAPP PRD v0.11, v0.12 and v0.13 -- L4-R review of the ratified-text half (3.0.0_SA_CVO~Z)

**Current: v0.13 @`1699960261`, ratified-text half_hash `679b1d41f694` -- SIGNED (section 7).** v0.11 and v0.12 were
REFUSED on annotation, history and seat names inside CONTRACTS (sections 3 and 6). The substance passed at every
version.

**Under review:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` @`9c8e04cd9a`
- prd_version v0.11
- half ratified-text: ENDPOINT + CONTRACTS
- half_hash `2ea7e0a99695`
- delivered as msg 23735

**Compared against:** v0.10 @`49aedcf88b` (half_hash `1246a6ea32fc`), which this seat signed.

**Instrument:** the half was cut with `.tools/prd_signoff_lib.py`'s own `top_sections` / `half_of_section`, so the bytes
reviewed are the bytes hashed. The two versions were diffed line by line.

**Verdict: REFUSED on one criterion -- annotation, history and seat names inside the section.** The substance passes
every other check. The fix is mechanical, and this seat will re-review on the next bump without delay.

## 1. What changed

| section | v0.10 lines | v0.11 lines | changed lines |
|---|---|---|---|
| ENDPOINT | 243 | 243 | 2 (one line replaced) |
| CONTRACTS | 195 | 312 | 179 |

The CONTRACTS changes:
- **C-PEER-SET-SA, C-PEERS-V-FLOORS and C-FILINGS-TRANSLATION** are new.
- **C-FILINGS-ANALYZER and C-EXEC-MANAGEMENT** are rewritten.
- **C-SIMILARITY-RANKER** hands FWD-8's peer set to C-PEER-SET-SA.

## 2. The checks

**(a) ENDPOINT against its own ratified content -- PASS.** The one change is "Eighteen outcomes cannot be closed by
any build" -> "Nineteen". The section's own bar line, unchanged, reads "BAR DISTRIBUTION: 19 of 20 are `EXERCISED`;
only `FWD-9` is `APPLIED`". v0.10 contradicted itself (18 against 19), and v0.11 makes it agree.
- **This seat's own miss:** it signed v0.10 with that contradiction in place.
- **The [warning sign] line itself** is an operative instruction to L5 ("grade the DONE WHEN state line"), not history, and it
  stays.

**(b) Every operative constraint present -- PASS.** Read against Andrew's verbatim words in
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260918_17xxZ_PEERS_SEEKING_ALPHA.md`:
- "It's now 5 instead of 8, we'll fit to the SA shape" -> C-PEERS-V-FLOORS MIN_PEERS_FOR_V 8 -> 5.
- "Agree with everything" confirms the stated consequence -> MIN_PEERS_PER_MEASURE 6 -> 5. |M| >= 3 is unchanged.
- "If we can get the remaining two from BBG then do that, if not, fall back to what SA provides, as a general rule for
  the pipeline for that process" -> C-PEER-SET-SA SOURCE RULE, with every cell carrying its `source`.
- "Yes we can do that in SA shape" -> preferred + minority as one column, `other_cap_struct`.
- "not the crawler script" and "the rest fetch is probably it" -> the path is the existing `rest_fetch.py`, never
  the harvester or a sign-in.
- Production use stays gated by C-SA-VENDOR-WORD, and any schedule by C-SA-TERMS-BEFORE-SCHEDULE. This is the narrow
  reading, and it is right: his words authorized a TEST through the parked session, not production.

**(b2) The L4 reading in C-PEERS-V-FLOORS -- CONSISTENT with Andrew's words. This is the substantive call of this
review.** The reading: Peers V runs as written on its own Bloomberg FIELDS for the SA peer tickers; SA chooses WHO
and the measure's fields say WHAT. It does not conflict with his words:
- His 18:0xZ "general rule" is about the table COLUMNS that SA does not carry.
- "fit to the SA shape" answered the peer-COUNT question.
- His 18:3xZ Model ruling -- "I'd use Bloomberg as primary, seeking alpha as a fall back" -- puts Bloomberg first for
  the BEST_ consensus class that Peers V's own inputs belong to.
- Feeding the score SA's metrics would produce a different measure under the same name (Z-S164's concern).

This seat signs this reading on its merits once the hygiene below is fixed.

**(c) Cross-references resolve -- PASS.** Every contract id the new clauses cite is defined in this PRD:
C-SA-VENDOR-WORD, C-SA-TERMS-BEFORE-SCHEDULE, C-VENDOR-EGRESS, C-IDENTITY-RESOLVED, C-ETF-PLANE-READ (line 558),
C-VERBATIM-GATE, C-POSTURE, C-FILINGS-TRANSLATION and C-SIMILARITY-RANKER.

Two false negatives of this seat's own instrument were caught before they were believed:
- a first definition pattern reported 42 ids missing because it required the id directly after `**`;
- a second missed `**C-ETF-PLANE-READ.**` because of the period before the closing `**`.

Each was checked against the file, with defined clauses as positive controls. Agreement with the counterpart:
C-ETF-PLANE-READ's producer counterpart stays NOT established, as v0.10 already said. v0.11 does not move it.

**(d) No annotation, history or seat name inside the section -- FAIL.** The v0.11 text adds all four classes inside
the CONTRACTS body.

## 3. What must change for this seat to sign

**The bar.** The two section bodies carry binding text and its provenance only.

**Provenance stays:**
- `Source:` lines;
- the label "L4 reading, not Andrew's word".

**Version tags in clause heads are acceptable.**

**What goes out, to the brief half, the change log, or the round-14 cell text:**

1. **Seat serials inside the body.**
   - C-PEERS-V-FLOORS: "[warning sign] L4 READING, `1.0.0_SA_CTO~Z`'s, FOR `3.0.0_SA_CVO` TO SIGN -- NOT ANDREW'S WORD". Keep the
     provenance ("L4 reading, not Andrew's word") and drop the serials and the note addressed to the reviewer.
   - C-FILINGS-ANALYZER: "Kept from v0.7 (`4.0.0_SA_CRO~W`, brief @`a65fe406c2`)". Drop the serial; a brief pin as
     provenance may stay.
2. **Present-tense defect descriptions with file:line citations.** Keep each RULE and move the evidence out:
   - C-FILINGS-ANALYZER's "(D1: `build_universe.py:503-508` ... `:518-520` ... `:510` ...)";
   - C-FILINGS-TRANSLATION's "(`passages.py:67-79` keeps 6.8% of Japanese characters)";
   - C-EXEC-MANAGEMENT's "Today the primitive breaks silently ... (`serp.py:264-272`) ... (`enrich.py:434-439`)";
   - C-EXEC-MANAGEMENT's "(today `enrich.py:582-594` keeps only one `as_of`)".

   **Why this is the load-bearing item:** ratified text that says a defect exists "today" becomes FALSE the moment
   round 14 fixes it. A cited line also ages separately from the text that quotes it (CLAUDE.md Rule 27).
3. **Measurement results.** C-FILINGS-TRANSLATION's "Measured on Keyence (the Yuho, Japanese): 70 of 71 ... 0 of 71
   translations re-locate". Evidence belongs in the brief half.
4. **Supersession narrative.** C-FILINGS-ANALYZER's "SUPERSEDED by this clause: the v0.7 premise ... retired". The
   change log carries it.

## 4. Consistency with this seat's v0.10 signature, stated plainly

v0.10 already carried items of the same classes: C-FILINGS-ANALYZER's "measured by `4.0.0_SA_CRO~W`" and its
dated probe narrative on `pipeline.py`. **This seat signed v0.10 with them.** That was a lapse in applying (d), not a
precedent, and the refusal applies the criterion as written. Item 1's C-FILINGS-ANALYZER serial is the v0.7 item
re-introduced by the rewrite; clearing it now clears the older lapse too.

## 5. Not required

- The CONTRACTS heading's "the reviewer is `3.0.0_SA_CVO`, always" sits in the TITLE, which the half hash does not
  cover beyond its first word.
- The ENDPOINT [warning sign] line is operative.

## 6. v0.12 @`4de34f0d95` -- THE BYTES THE STAMP BINDS (ratified-text half_hash `901bf534d397`)

**A grain correction this seat owes.** Sections 1-5 reviewed v0.11 (half_hash `2ea7e0a99695`). Between that review
and the stamp, 1.0.0_SA_CTO~Z bumped the PRD to v0.12. `prd-signoff.py` binds a stamp to the PRD at HEAD, so the
first REFUSED stamp (@`075227f4c0`) was bound to v0.12's bytes while citing a review of v0.11's. This seat did not
re-read the half hash immediately before stamping, and that is its miss. This section reviews the v0.12 delta so the
stamp and its review describe the same bytes, and the stamp is re-issued citing this version of the document.

**The delta.** Same instrument, v0.11 -> v0.12: ENDPOINT 0 changed lines; CONTRACTS 9 changed lines, in two places.

1. **C-PEER-SET-SA: "PRODUCTION USE WAITS" becomes "PRODUCTION USE AUTHORIZED, BY NAME".** `C-SA-VENDOR-WORD` is
   lifted for this path, one Peers read per security at instantiation and in validation, and a RECURRING or SCHEDULED
   read still waits on `C-SA-TERMS-BEFORE-SCHEDULE`.
   - **Verified** against `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md`
     @`4de34f0d95`. Card 1 asked for SA as a production source for Peers, per security at instantiation, and his
     answer is verbatim "1.) Yes use SA thats fine".
   - **The clause is the narrow reading.** It lifts the vendor word for the path by name and leaves the scheduled
     read behind the terms review, as card 1's (b) framed it. PASS.
2. **C-FILINGS-ANALYZER: the international battery goes from "PROPOSED, NOT RATIFIED" to "RATIFIED v0.12".**
   - **Verified** against the same record. Card 3 put the order EDGAR ticker -> EDGAR Bloomberg CIK -> ESEF/UKSEF by
     LEI -> company site -> national regulator -> UNRESOLVED, and his answer is verbatim "3.) Yes.". PASS.

**The refusal grounds are unchanged in v0.12.** None of the items in section 3 was removed: the seat serials in
C-PEERS-V-FLOORS and C-FILINGS-ANALYZER, the present-tense defect narratives with file:line citations, the Keyence
measurement narrative and the supersession history are all still in the body. The v0.12 provenance additions --
"(v0.12; Andrew-direct ~19:4xZ, ...)" with the record's path -- are provenance and are acceptable under the bar in
section 3.

**Verdict on v0.12: REFUSED on criterion (d) alone.** The substance passes, including both v0.12 changes. Clearing
section 3's four items is the whole of what this seat needs in order to sign.

**Record note.** The re-stamp citing this section was refused by the tool at ~20:1xZ: "the PRD's worktree copy
differs from HEAD in a half's bytes". The v0.13 edit was in progress in the shared tree at the time. The v0.12
REFUSED stamp @`075227f4c0` therefore still cites the review at @`969755b2f2`, which covers v0.11. This section is
the record of the v0.12 bytes, and v0.13 supersedes both.

## 7. v0.13 @`1699960261` -- SIGNED (ratified-text half_hash `679b1d41f694`)

**Two reads, because a check scoped to the diff cannot see what the diff did not touch.**

**(i) The v0.12 -> v0.13 diff.** ENDPOINT 0 changed lines; CONTRACTS 313 -> 299 lines, 52 changed. Every item in
section 3 is removed:
- **Seat serials (item 1):** "L4 READING, NOT ANDREW'S WORD" carries no serials, and "Kept from v0.7 (brief
  @`a65fe406c2`)" drops `4.0.0_SA_CRO~W`.
- **Present-tense defect narratives with file:line citations (item 2):** build_universe.py D1, passages.py,
  serp.py / enrich.py and enrich.py:582-594 are all out, and the "Preconditions" line no longer says "each absent
  today".
- **The Keyence measurement (item 3):** out.
- **The supersession paragraph (item 4):** out.
- **Beyond what was asked:** the clause heads drop their line pins, and the dated example lists (Roche / RWE /
  Zurich; "3 of 22 names") are out. Every RULE is intact.

**(ii) The whole v0.13 half, scanned.** Denominator: 542 lines.
- **file:line citations:** 0.
- **measurement narrative:** 0.
- **supersession:** 1 hit, "Kept from v0.7 (brief @`a65fe406c2`)" -- provenance, admitted by section 3's bar.
- **"today":** 4 hits. Three are ENDPOINT text unchanged since v0.10 (ENDPOINT:48, :72, :149), and ENDPOINT is
  ratified content this review does not rewrite. One is an older CONTRACTS state line with no citation
  (CONTRACTS:279, "Today each is a Python module a person runs by hand").
- **seat serials:** 15 hits, all in contracts older than v0.11. They are OWNERSHIP assignments ("Owner of the
  readers: `2.0.0_SA_COO~W`") and provenance paths to records. An owner assignment is binding content, not
  annotation.

**Why these 19 residuals do not block the signature.** None was in section 3's list. 1.0.0_SA_CTO~Z cleared exactly
what this seat asked for, and refusing now over items this seat did not name would move the bar after it was met.

**Recommended at a later bump, not required:** several of the ownership serials name `~W` lanes, which may no longer
be the live owners; and CONTRACTS:279's "Today" line states a present condition that will age.

**(iii) The one new substantive change, VERIFIED.** C-PEER-SET-SA now reads `C-SA-TERMS-BEFORE-SCHEDULE` SATISFIED
for this path, and the vendor word covers "its refresh". Andrew-direct ~20:0xZ, verbatim in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_20xxZ_AMGT_RESAPP_SA_TERMS_CLEARED.md`: "I have
already clarified SA ToS, we are good, if I had an issue with the design i wouldnt have designed it this way." The
clause is his word, scoped to this path. The "NOT CHANGED" list correctly drops the two contracts this change does
touch. PASS.

**Verdict on v0.13: SIGNED.**
- **Substance:** passes every check -- sections 2, 6 and (iii) above.
- **Hygiene:** meets section 3's bar.

-- 3.0.0_SA_CVO
