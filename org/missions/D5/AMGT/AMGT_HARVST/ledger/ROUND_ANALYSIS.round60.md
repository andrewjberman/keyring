# AMGT_HARVST -- ROUND 60 ANALYSIS (L10), after served gold rebuild #8

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-08 ~00:0xZ. **Asked by:** `2.0.0_SA_COO~H` msg 31483 (every order of rounds 54 to 60 terminal).
**Graded inputs:** `3.0.0_SA_CVO~Z`'s grades of 2026-10-07, read as messages by this seat: the gain sample 29 of 30 and the
ticker forms (@399fcf7d0a); CSL on all 42 pairs, 39 of 42 (@f6e370e6cc); the 17 ICT pairs, 17 of 17 not about the security
(@160f1c9602). **No L10 slug for round 60 has reached this seat;** this analysis rests on those grades and the act's record, and
a slug that says otherwise re-opens it.
**The act:** rebuild #8, `deliverables/2.0.0_SA_COO_H/round60/gold_rebuild8.act_20261007T203825Z.json` @1c819a517e; CTO half
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_AMGT_HARVST_GOLD_REBUILD8_20261007.md` @201121c305.

## 1. Where the product stands

- The served gold is built from the list the code builds (242 securities), not the hand-carried 212. Ended 22:48Z.
- Mention pairs 33,665 to 48,025: lost 0, removed 17 by ruling, unexplained 0. Daily rows 59,148 to 67,760.
- This seat read both new parts as the newest of their tables (sizes and times equal to the record's). It opened neither.
- The Seeking Alpha job records are live (bf-1, 61 records).

## 2. What is not yet shown

1. **Pairs that rest on a bare company name.** The matcher falls back to the company's name when a security has no alias, and a
   lower-case hit counts (GSK, RWE, SAP, BP_US, Nokia). None was graded. They are served now.
2. **Nine ticker forms no sample reached,** 20 pairs (BNP 5, HEI 3, SNPS 3, DG 2, ED 2, GPN 2, ADBE 1, NKE 1, SHOP 1).
3. **Three known wrong pairs on CSL's page** (Carlisle Companies), and more will arrive with later stories.
4. **How the page reads with 14,400 more pairs.** No walk of the Security Analysis feed has been made on the rebuilt gold.

## 3. Rulings

| # | subject | ruling | why |
|---|---|---|---|
| R1 | the bare-name fallback (item 1) | First cell: a census of the pairs that rest on the fallback alone, by security, denominator printed; then a sample of 30 graded by `3.0.0_SA_CVO~Z`, bar 27 of 30. Below the bar the fallback requires the name in its stored case, or is removed for the securities that fail. | It is the only class of served pair nobody has read. |
| R2 | the nine unreached forms (item 2) | All 20 pairs are read whole by the CVO; 20 is a census, not a sample. A form with 2 or more wrong pairs goes to `ticker_refusals`. | A population of 20 is cheaper to read than to sample. |
| R3 | CSL and Carlisle (item 3) | One cell: where a security's bare ticker form is shared with a company outside coverage, a pair needs a second anchor in the article (the covered company's name or a brand) or it is not counted. CSL is its real case; the cell states how many other covered forms it changes, with 0 good pairs lost on the 39. | Three wrong pairs today and a rule that keeps admitting them. A refusal of the form would lose 39 good pairs. |
| R4 | names for `CAT_US_Equity`, `CSL_AU_Equity`, `6861_JP_Equity` | The built list takes a security's name from `lib/research/identity/registrations.json` where the gold list holds only a key. No vendor call. | The registry already holds all three (issuer msg 31219). `6861_JP_Equity` matches nothing today for want of a name. |
| R5 | cut legal names (row Z-S96) and the suffix list | One cell, one suffix list: a legal name is cut at a suffix on that list and nowhere else; the cell prints every name it changes. | Two rows, one cause. |
| R6 | `ICT_US_Equity` | The record states what that security is and where its key came from. If no source names it, it leaves the list by a cell, not by hand. | The CVO found no entry for it in the identity registry (@160f1c9602). |
| R7 | the next rebuild | None is cut in round 61. R1 to R5 land on the builder; the next rebuild is its own pair after their grades, with the same rule: 0 lost, every removal named and graded. | One rebuild per graded change set. |

## 4. ENRICHMENT LIST (round 61, ONE issuance by `2.0.0_SA_COO~H`)

1. R1: the fallback census, then its graded sample.
2. R2: the 20 pairs, read whole.
3. R3: the second-anchor rule, with CSL as its case.
4. R4: names from the registry for the three key-only securities.
5. R5: the suffix list and the cut legal names.
6. R6: what `ICT_US_Equity` is.

A build order carries at most three mechanical criteria. Items 1 and 2 are reads and can be issued beside the build cells.

## 5. ACTS ONLY ANDREW CAN DO (cited)

None for this round. No cell calls a vendor.

-- 1.0.0_SA_CTO~Z

## ADDENDUM 1, 2026-10-08 ~00:1xZ -- on the slug (`3.0.0_SA_CVO~Z` msg 31492, `ADJUDICATION_v65.md` @98e21862f2)

The slug was owed and had not been asked for by a terminal notice; this analysis was written before it. It dispositions 6 rows:
4 graduated, 2 dismissed. Three of the four are already in section 3 or are the issuer's own (Z-W107-S1 is R1; Z-S101 is R3;
Z-W108-S2, a job record's `finished_at` is the run's end, is the collector's cell). One was not carried:

- **R8, row Z-W107-S2 (ARMED).** The brand `ASML` is refused for `ASML_US_Equity`, and at rebuild #8 its mention count fell on 2
  served rows. Ruling: **a brand belongs to the ISSUER, so two listings of one issuer may both carry it.** The refusal that
  stops one brand matching two securities is right between different companies and wrong between two listings of the same one.
  One cell: the builder groups listings by issuer before it applies that refusal; its check names ASML's two listings as the
  real case and prints every other pair of listings the change affects, with 0 pairs lost elsewhere. It disarms the row.

**ENRICHMENT LIST, round 61, as amended:** items 1 to 6 of section 4, then 7, R8's issuer grouping; 8, Z-W108-S2's `finished_at`.

**A limit the slug states and this seat repeats:** the CVO's grades are on the dry runs and the pre-rebuild pairs. Nobody has
read the rebuilt gold itself beyond its counts and its rule. R1's census is the first read of it.

-- 1.0.0_SA_CTO~Z

## ADDENDUM 2 -- ROUNDS 61 TO 63 ANALYSIS (2026-10-08 ~04:4xZ), on `3.0.0_SA_CVO~Z` slug msg 31574 (`ADJUDICATION_v66.md` @d15b2c19d6)

Ten of ten orders terminal (`2.0.0_SA_COO~H` msg 31570, @6c959d416b): bh-1 to bh-10. Merged on CLOUD: registry names, cut legal
names, the second anchor with symbol anchors for CSL and HEI, issuer grouping, the stored-case fallback, the per-job
`finished_at`. Slug: 6 rows dispositioned, 1 graduated, 5 dismissed.

**Rulings made in these rounds, each closed the turn it arrived:**
- **R9, the bare-name fallback (R1's census).** It matches the name in its STORED CASE only. The sample read 27 of 30 and all 27
  were Nokia; the census split 277 as Nokia 262, BP 8, SAP 7. The CVO read all 15: 13 not about the company, 2 about BP.
- **R10, a symbol anchor (R3, row Z-W110-S4).** The issuer's own listing symbol in exact case is an admissible second anchor.
  `CSLLY` for CSL: 39 of 39 good pairs kept, 3 of 3 Carlisle dropped, 0 of 242 others changed. It is in no stored source (pool 0,
  registry 0, collector record 0), so its data row says "evidenced by article spans only".
- **R11, HEI (row Z-W110-S6).** Under the rule: 40 of 42 good HEICO pairs kept, 1 Hawaiian Electric pair dropped. Stated with it,
  from the CVO's read: Hawaiian Electric trades as HE, so the future risk this ruling named is smaller than it said.
- **R12, the bar.** "0 pairs lost" becomes "0 lost except pairs NAMED by key and read by the CVO". Four are named: BP
  sa:4473686 and sa:4441205; HEICO sa:3584086 and sa:3685322. Told to Andrew at ~02:0xZ and ~04:2xZ with the option to hold zero.
- **R13, `ICT_US_Equity` (R6).** It stays on the list with 0 pairs; the unresolved holding is the pool's, as a row on AMGT_RESAPP.

**For rebuild #9** (the word to dry-run it was given in msg 31571): the pair names the four lost pairs; states the 13 false
fallback pairs, the 3 Carlisle and the 1 Hawaiian Electric pair as removed, each with its grade; reconciles HEI's two counts (44
to 41 in msg 31570, 42 good pairs in msg 31567); and explains or states as unexplained row Z-W112-S1's BNP gap of 3 against the
dry run. An unexplained 3 is a count in the pair, not a silence.

**ENRICHMENT LIST, round 64:** rebuild #9 under its own pair; Z-W110-S5 (ICT and TTE listings are not grouped as one issuer:
the issuer grouping of R8 reaches them or says why not); then the first walk of the Security Analysis feed on rebuilt gold.

-- 1.0.0_SA_CTO~Z


## ADDENDUM 3 -- ROUNDS 64 AND 65 (2026-10-08 ~07:3xZ), on `2.0.0_SA_COO~H` drain end 31609 and `3.0.0_SA_CVO~Z` grade 31612 (`org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND65_FEED_WALK_GRADE_20261008.md` @96206b0d29)

**What is live.** Gold rebuild #9, ended 06:25Z: mention 48,358 rows, daily 68,002 (the COO's counts; the two newest parts listed
back by this seat). The CVO's own read of the served part: 0 of the 21 named removals still served. bi-1 merged (TTE grouped, ICT
left apart with its reason). bj-1, the first walk of the page's feed: twelve read, none failed, 8 served.

**Rulings.**
- **R14, row Z-S103: YES, read first.** Silver holds 714 articles published in the 30-day window, 5 of them from the FT, and 0
  naming Caterpillar, CSL or AIG. Three empty panels are true to what is held; what is held is thin. Round 66's first cell reads,
  from bronze, silver and the collector's own run logs only, the articles collected per source per day over 90 days, and names the
  day each source thinned. No publisher is called to find out what was missed: that is a vendor use with no word of Andrew's.
- **R15, row Z-S102.** "25 BP Rate Increase" is on BP's feed: basis points, in a headline capitalised throughout, matched on the
  exact-case ticker form. In a headline where every word is capitalised, case carries no information, so the exact-case form
  alone does not pair there; it needs the second anchor. One cell, with the count of pairs it moves printed before any rebuild.
- **R16.** This seat told Andrew at ~06:5xZ that CSL's empty panel was the result of removing the Carlisle stories. Wrong:
  `2.0.0_SA_COO~H` msg 31611 read rebuild #8's part and the panel was empty before. Corrected to him at ~07:0xZ.
- **R17.** BNP's unexplained 3 (row Z-W112-S1) stays open as a stated count.

**ENRICHMENT LIST, round 66:** R14's read first; R15; then a second feed walk.

-- 1.0.0_SA_CTO~Z

## ADDENDUM 4 -- R18 TO R29, ROUNDS 66 TO 72 (written 2026-10-08 ~21:3xZ), carried from this seat's ruling mail

These rulings were sent to `2.0.0_SA_COO~H` as messages between 08:12Z and 18:11Z and are written here, the carrier, now. Each
line names its message. The operative sentence is the message's own; read the message for the full text.

- **R18 (msg 31631).** Round 66 carries two READ cells before the second walk, and neither runs a job: the census of covered
  securities with no collection job, by subtraction, with both denominators reconciled; and AIG's six empty jobs read from their run
  records beside Nokia's three productive ones. Superseded in its cells by R20.
- **R19 (msg 31637, on `4.0.0_SA_CRO~Z` msg 31636 @2394cfc3d8).** This seat's "a scheduled sweep is owed" (msg 31626) is
  WITHDRAWN. No sweep is built or scheduled: the PRD puts any schedule outside the project, and Andrew's word of 2026-10-03 bars
  changes to data operations without his directive. The sweep's shape is recorded for his card only.
- **R20 (msg 31637).** It replaces R18's cells, and neither cell fetches: (a) reconcile the three universes (list 242, crosswalk 237,
  collector 234) and add the missing identity records; (b) repair AIG's truncated stored name and print every other name cut the
  same way. A run for any of them waits on Andrew's per-use word.
- **R21.** No ruling carries this number. This seat's sent mail of 2026-10-08 under `org/mcp/inbox/` holds 0 occurrences of it;
  the number is skipped, not lost.
- **R22 (msg 31649).** The collector's pointer does not move. Moving it is the data-operations adjustment that Andrew's 2026-10-03
  word reserves. The new dated files stay beside the old ones, unpointed. First: AIG's stored name becomes the full legal name, and
  the three names cut and not repaired (ICT_US, both OMAB lines) are repaired or their reasons stated.
- **R23 (msg 31664).** The AIG query is a stored per-security override for `AIG_US_Equity` only. `publishers._LEGAL_SUFFIX`
  is not changed. Proof: the derived-query table over all 242 names reads 1 changed, 241 identical. The merge is held until the
  live Seeking Alpha leg ends, and it carries a pair, because a merge into `lib/opal_data_harvest` is a deploy on this box.
  ICT_US unrepaired with its reason is accepted.
- **R24 (msg 31703).** One merge is one act and one pair. The pair on 419dc9b1fc lapses SPENT WITHOUT AN ACT, and a new pair names
  537ac56e9b. Recorded because C2's test found the whole Bloomberg leg stopping on one bad record: the new half shows the
  900-second cooldown is not set on the new path, and it states row Z-W123-S1's bound in words.
- **R25 (msg 31831).** Repair the ACCEPTANCE CHECK, not the aliases. Acceptance uses the strings `slug_queries` searched with,
  whole-word. No alias is edited for the 149 names. Proof before any merge: the before-and-after acceptance table over 242 names,
  every article accepted today still accepted, and the single-common-word names listed. The merge carries a pair, and any
  re-collection is Andrew's word. "Case-sensitive" is withdrawn by R27.
- **R26 (msg 31845, on `4.0.0_SA_CRO~Z` msg 31841 @3bb6d192e0).** No list of company names is kept: the rules are case, whole
  word and a second anchor. The order: (a) test whether gold pairs a planted lower-case "target" on a security that carries
  aliases; (b) if it does, gold matches an alias in its stored case; (c) only then R25. Each merge has its own pair, and nothing
  is re-collected.
- **R27 (msg 31867).** Acceptance is whole-word and case-INSENSITIVE on `slug_queries`' strings, a superset of today's rule. R25's
  "case-sensitive" is withdrawn: nine names are stored in capitals (NVIDIA, QUALCOMM, CATERPILLAR and six more). R26(a) stands as
  ruled. R26(b) is not cut; it waits on a census over built gold of the pairs that a stored-case rule would remove, by security.
- **R28 (msg 31945, on the gate stop 31942).** Rebuild #10 runs on the list that rebuild #9 served, frozen in
  `round72/securities.universe.r72.json`, and serves only the capitalised-headline rule (R15). The AIG/OMAB list move is rebuild
  #11, under its own pair. Its dry run prints the pairs moved per security for AIG and both OMAB lines, ten titles each, graded by
  `3.0.0_SA_CVO~Z`.
- **R29 (msg 31945).** The collector pointer has two readers, the collector and gold's list. Any act that moves it names both in
  its ledger.

**Read with them:** gold rebuild #10's CTO half, SIGNED (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_AMGT_HARVST_GOLD_REBUILD10_20261008.md`
@fee6ba8438), with C1 met by `3.0.0_SA_CVO~Z`'s grade (msg 31883: the ten GSK titles, 10 of 10 GlaxoSmithKline). PRD v0.22 was
SIGNED at L4-R (msg 31943). R26(a) read YES (`2.0.0_SA_COO~H` msg 31961): gold pairs a lower-case "target" on a security that
carries aliases, so R26(b)'s census is the next ruling input.

- **R30 = R26(b)'s shape (ruling sent to `2.0.0_SA_COO~H` at 21:24:04Z, on the census 32003 @7e1509b798,
  `deliverables/2.0.0_SA_COO_H/round73/stored_case_census.out`).** Exact stored case is REFUSED. The census shows it removes 1,466
  of 46,066 tested pairs over 37 securities, led by good pairs on all-caps stores (NVDA 782, JPM 179, QCOM 85) and by exact-form
  rows such as ASML, Nestle and EBay. The rule: an alias matches whole-word only where the matched text's first letter is
  upper-case; the rest is case-insensitive. The cell: the same census re-run under R30, by security, with both denominators;
  `3.0.0_SA_CVO~Z` reads 30 removed pairs, bar 27 of 30 wrong; and 10 kept pairs on V, CDNS, BKNG and ORA read for residual
  sentence-initial matches, stated as a count. Its own pair, served in a rebuild after #11, and nothing re-collected.

**ENRICHMENT LIST (open at this writing):** R30's census and grade; then R27's acceptance change under its pair; rebuild #11 under
its own pair (R28). The collector pointer and any re-collection wait on Andrew's per-use word (R22).

-- 1.0.0_SA_CTO~Z
