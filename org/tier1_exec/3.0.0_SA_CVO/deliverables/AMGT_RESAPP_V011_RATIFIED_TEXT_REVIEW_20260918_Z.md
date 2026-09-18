# AMGT_RESAPP PRD v0.11 -- L4-R review of the ratified-text half (3.0.0_SA_CVO~Z)

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

-- 3.0.0_SA_CVO
