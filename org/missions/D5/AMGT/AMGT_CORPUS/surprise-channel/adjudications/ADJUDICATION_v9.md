# AMGT_CORPUS ROUND 6 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-26 ~17:2xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND6_DRAIN_END_PACKET.md` @`0615fed688` (read to EOF, 8,991 B), msg 26128.
**L7 RE-MEASURED not adopted:** 5 of 5 `h-` orders `complete` on their LAST `<status>` tag; 17 acceptance
criteria; **exactly 2 carrying `judgment="true"`** (`h-2` AC4, `h-5` AC4). Matches the packet.

---

## 1. L8 -- THE CHANNEL COMPILE

`_latest_dispositions`: **74 items, 10 files read, `unknown: []`, 30 NON-TERMINAL.**
Round-6 window (on/after 2026-09-26): **9 rows.** The packet names seven; the other two are `Z-S39` and
`Z-S40`, **my own**, filed earlier today. **So the packet's row set is COMPLETE for the issuer's rows.**

| row | disposition here |
|---|---|
| `Z-S41` (ARMED) | **GRADUATED** -- `read_dossier` serves the last write 95 of 95, and the exercised arm wrote **0 twice** at unchanged `inputs_sha16 fc1e3a62101e4598`. DELTA=0 on the store, so no never-widen pair was owed. The disarm is exercised, not described |
| `Z-S42` | **GRADUATED** -- the hold it carried is lifted by `Z-S44` |
| `Z-S43` | **GRADUATED** -- FWD-2's one bronze-without-silver is the Copa Holdings byte-identical pair |
| `Z-S44` | **GRADUATED** -- the disarm/lift carrier |
| `Z-S45` (BLOCKING, ARMED) | **CARRIED** -- the continuation readers take the FIRST sorted input-matching key and `inputs` does not carry `method_version`, so a `/2` rewrite would serve terms on **49** of 95 and keep serving `/1` on **46**. Unremedied; it needs a reader build. ⭐ **The issuer HELD the rewrite rather than running it, which is the correct act and is why this row is an EXPOSURE and not an INCIDENT** |
| `Z-S46` | **CARRIED** with `Z-S45` -- the hold that disarms it, valid only while the issuer remains the sole `continuation --write` writer |
| `Z-W2-S10` (ARMED) | **CARRIED** -- three SERVED Base cases (6861_JP, CAT_US, CSL_AU) sit in pre-`g-1` blocks carrying no band or currency fields. The issuer read them in band (1.257, 0.597, 1.390) but **the unit cannot be confirmed from fields the block does not carry**, which is the honest bound |
| `Z-S39`, `Z-S40` (mine) | **CARRIED** -- `Z-S39`'s metacharacter exposure is unremedied (see below); `Z-S40` stands as the record that my round-5 bound aged |

**Carried BLOCKING-or-ARMED from earlier rounds: `Z-S3`, `Z-S6`, `Z-S7`, `Z-S8`, `Z-S9`** (all 2026-09-23),
**CARRIED** -- none is round-6 business and none has a landed remedy. ⚠ `hazard_standing` is the value
written AT SURFACING and is never a current-state field; nothing here claims any of them live today.

⭐ **AND `Z-S39` IS PARTLY ANSWERED BY THIS ROUND'S OWN EVIDENCE.** The workbook keys render the literal-`/`
securities as **`BP-SLASH-_LN_Equity`** -- the harvest path escapes the metacharacter rather than carrying
it. So the `/` hazard is mitigated ON THIS SURFACE by an escaping convention. ⚠ That is one surface, not
the key space: the row stays carried, and `WALMEX*_MM_Equity`'s `*` is untouched by a `-SLASH-` rule.

## 2. L9 -- `h-2` AC4: A SPLIT VERDICT, AND THE HALVES ARE NOT CLOSE

**Read verbatim from the order:** *"beside the team's own workbook for that name, does each served Base case
read as a plausible Base case, **and** does the distribution just inside 0.33 and 3.0 support those
bounds?"* **Two questions. They grade differently.**

### (B) DOES THE DISTRIBUTION SUPPORT THE BOUNDS? -- **CEILING YES, FLOOR NO**

| | measured |
|---|---|
| just INSIDE the ceiling (2.5-3.0) | **2** -- SAN_FP 2.566, ZTS_US 2.522 |
| just OUTSIDE it | NFLX_US **3.043**, 0.043 beyond |
| just INSIDE the floor (0.33-0.5) | ⛔ **0 -- the bin is EMPTY** |
| nearest accept above the floor | RWE_GR **0.537**, a distance of 0.207 |
| the only name below the floor | BA_US at **-0.0916** -- a NEGATIVE ratio, refused `forward_eps_not_positive`, not a band case at all |

⭐ **THE CEILING IS EMPIRICALLY SUPPORTED AND THE FLOOR IS UNEXERCISED.** Two names sit inside 3.0 within
0.48 and one sits outside within 0.043: that boundary DISCRIMINATES, and moving it would change
dispositions. **Nothing sits near 0.33 on either side.** No name in this population would change
disposition if the floor were 0.1, 0.2, 0.3 or 0.5 -- **the data cannot distinguish 0.33 from any value in
[0, 0.53]**, and the one sub-floor name is there for a different cause entirely.

So the answer AC4 asks for is: **the ceiling's number is earned; the floor's number is not yet evidence,
it is a choice no observation has tested.**

### (A) PLAUSIBLE BESIDE THE TEAM'S WORKBOOK? -- ⛔ **NOT GRADEABLE FROM THIS EVIDENCE**

Measured over the evidence's own denominator (`CASE_EVIDENCE_ROUND6.json`, `workbook.rows`):

- **53** distinct names carry workbook cells; **37** of those carry a numeric `served_base`.
- **200** Base-labelled cells in total -- and ⛔ **196 of them have an EMPTY `right` list.** The extractor
  captures `below` and essentially never `right`, **which is the direction a spreadsheet puts a value next
  to its label.**
- Names where a Base-labelled cell has ANY neighbour within 2x of the served base: **4 of 37** -- and all
  four are artifacts, not comparisons: ASML 1348.90 beside **2017.0**, KPN 4.374 beside **-7.0**, ORA 16.52
  beside **19.0**. ⚠ **Those are YEARS and a negative.** My own 2x window admitted them; reading them shows
  what they are.

**So 0 of 37 names yield a defensible workbook base-case NUMBER to compare against.** The packet says so
itself and says it honestly -- *"Workbook cells are laid out by coordinate, never selected"* -- so this is
not a claim the issuer overstated. It is that **the criterion asks for a comparison the evidence's SHAPE
cannot support.**

⭐ **AND MY ROUND-5 BOUND IS NOT YET DISCHARGED -- IT HAS MOVED, WHICH IS PROGRESS WORTH NAMING.** Round 5
left this half ungraded because *no workbook comparator existed in the corpus*. Round 6 BUILT one, deterministically, with a
printed denominator and a venue floor. The gap is now narrower and much more specific: **from "no workbook
data" to "workbook data that does not carry the number."** The remedy is correspondingly small -- capture
`right` as well as `below`, and select the case cell rather than dumping its neighbourhood.

## 3. L9 -- `h-5` AC4: **NOT GRADEABLE**, AND I AM NOT SUBSTITUTING A DIFFERENT OBJECT

The criterion reads *"at L9 **on the issuer's served rewrite**"*. **That rewrite is HELD, not run**
(`Z-S45`, section 2 item 3 of the packet). **The criterion's object does not exist, so there is nothing to
grade, and I do not grade the in-memory build in its place.** Where no real run exists the answer is NOT
GRADEABLE -- never a criterion re-pointed at whatever evidence happens to be present.

⚠ **Recorded, not graded**, because the next round will want it: the in-memory build gives AZN_LN_Equity
five pillars each carrying its heading as the first term, one also carrying a KPI term (`dividend`), and
25 of 25 KPI rows carrying terms. **The issuer's own reading is the fair one and I adopt it as a reading:**
*"the rule is honest and thin -- most pillar texts name no KPI-lexicon term, so most terms are the heading
alone."* Whether heading-only terms are ENOUGH is a ruling about vocabulary, not a worker's choice, and it
belongs to whoever answers enrichment item 4.

⭐ **THE ISSUER HELD THIS CORRECTLY AND SHOULD BE CREDITED.** Running the rewrite would have served terms on
49 names and silently left 46 on the old method with no signal. Holding it cost a judgment criterion and
prevented a split-brain served plane; that is the right trade and it is why `h-5` AC4 is ungradeable rather
than failed.

## 4. L10 PRECONDITION

1. **Every task order terminal** -- 5 of 5 on their last `<status>` tag. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- 9 round-6 rows disposed (4 graduated, 5 carried), plus
   the 5 carried legacy ARMED rows named. **MET**
3. **Every judgment criterion graded** -- 2 of 2 ADDRESSED: `h-2` AC4 split (ceiling supported, floor
   unexercised, workbook half NOT GRADEABLE with its denominator printed); `h-5` AC4 NOT GRADEABLE with its
   reason. **MET** -- a bounded non-grade with a stated cause is a grade; a silent pass is not.

---

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S9",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-26T17:25:00Z",
    "one_line": "L9 round 6: h-2 AC4 SPLITS -- the 3.0 ceiling is empirically supported (2 names inside within 0.48, NFLX 0.043 outside, so the boundary discriminates) while the 0.33 FLOOR IS UNEXERCISED (the 0.33-0.5 bin is EMPTY, nearest accept 0.537, and the only sub-floor name is BA at a NEGATIVE ratio refused for a different cause), so no name would change disposition anywhere in [0, 0.53]. The workbook half is NOT GRADEABLE: 196 of 200 Base-labelled cells carry an EMPTY 'right' list and 0 of 37 names yield a workbook base-case number, the 4 apparent within-2x matches being YEARS. h-5 AC4 is NOT GRADEABLE because its object, the served rewrite, was correctly HELD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: 5 of 5 h- orders read 'complete' on their LAST <status> tag; 17 acceptance criteria; exactly 2 carry judgment=\"true\" (h-2 AC4, h-5 AC4). Matches the packet.",
        "L8: _latest_dispositions reads 74 items over 10 files, unknown [], 30 NON-TERMINAL. The round-6 window holds 9 rows; the packet names seven and the other two are Z-S39 and Z-S40, this seat's own, so the packet's row set is COMPLETE for the issuer's rows. Disposed: Z-S41 GRADUATED (read_dossier serves the last write 95 of 95 and the exercised arm wrote 0 twice at unchanged inputs_sha16 fc1e3a62101e4598, DELTA=0 on the store), Z-S42, Z-S43, Z-S44 GRADUATED; Z-S45, Z-S46, Z-W2-S10, Z-S39, Z-S40 CARRIED with reasons. Carried BLOCKING-or-ARMED from earlier rounds: Z-S3, Z-S6, Z-S7, Z-S8, Z-S9, none round-6 business and none with a landed remedy. hazard_standing is the value written AT SURFACING and is never a current-state field.",
        "h-2 AC4 READ VERBATIM from the order, not the packet: 'beside the team's own workbook for that name, does each served Base case read as a plausible Base case, AND does the distribution just inside 0.33 and 3.0 support those bounds?' Two questions, graded separately because they do not grade alike.",
        "(B) THE BOUNDS: CEILING SUPPORTED, FLOOR UNEXERCISED. Just inside 3.0: SAN_FP 2.566 and ZTS_US 2.522, two names within 0.48. Just outside: NFLX_US 3.043, 0.043 beyond. That boundary DISCRIMINATES and moving it changes dispositions. The 0.33-0.5 bin is EMPTY; the nearest accept above the floor is RWE_GR at 0.537, a distance of 0.207; and the only name below the floor is BA_US at -0.0916, a NEGATIVE ratio refused forward_eps_not_positive, which is not a band case at all. So NO name in this population would change disposition if the floor were 0.1, 0.2, 0.3 or 0.5: the data cannot distinguish 0.33 from any value in [0, 0.53]. The ceiling's number is earned; the floor's is a choice no observation has tested.",
        "(A) THE WORKBOOK HALF IS NOT GRADEABLE, measured over the evidence's own denominator in CASE_EVIDENCE_ROUND6.json workbook.rows: 53 distinct names carry workbook cells and 37 of those carry a numeric served_base; 200 Base-labelled cells exist and 196 of them have an EMPTY 'right' list, which is the direction a spreadsheet puts a value beside its label; names where a Base-labelled cell has ANY neighbour within 2x of the served base number 4 of 37, and all four are artifacts rather than comparisons -- ASML 1348.90 beside 2017.0, KPN 4.374 beside -7.0, ORA 16.52 beside 19.0, which are YEARS and a negative that my own 2x window admitted. So 0 of 37 names yield a defensible workbook base-case NUMBER to compare against.",
        "THE PACKET DISCLOSED THIS ITSELF -- 'Workbook cells are laid out by coordinate, never selected' -- so nothing was overstated by the issuer; the criterion asks for a comparison the evidence's SHAPE cannot support. AND MY ROUND-5 BOUND HAS MOVED RATHER THAN HELD: round 5 left this half ungraded because no workbook comparator existed in the corpus, and round 6 BUILT one, deterministically, with a printed denominator and a venue floor. The gap narrowed from 'no workbook data' to 'workbook data that does not carry the number', and the remedy narrowed with it: capture 'right' as well as 'below', and select the case cell rather than dumping its neighbourhood.",
        "h-5 AC4 IS NOT GRADEABLE AND NO OBJECT WAS SUBSTITUTED. The criterion reads 'at L9 on the issuer's served rewrite'; that rewrite is HELD, not run (row Z-S45), so the criterion's object does not exist. Where no real run exists the answer is NOT GRADEABLE, never a criterion re-pointed at whatever evidence is present. RECORDED BUT NOT GRADED, for the next round: the in-memory build gives AZN_LN_Equity five pillars each carrying its heading as the first term, one also carrying a KPI term (dividend), and 25 of 25 KPI rows carrying terms; the issuer's own reading is fair and adopted AS A READING -- 'the rule is honest and thin, most pillar texts name no KPI-lexicon term, so most terms are the heading alone'.",
        "THE HOLD WAS THE RIGHT ACT AND IS CREDITED. Running the served rewrite would have served terms on 49 of 95 names while silently leaving 46 on the old method, because the continuation readers take the FIRST sorted input-matching key and 'inputs' does not carry method_version. Holding it cost a judgment criterion and prevented a split-brain served plane, which is why h-5 AC4 is ungradeable rather than failed.",
        "Z-S39 IS PARTLY ANSWERED BY THIS ROUND'S OWN EVIDENCE: the workbook keys render the literal-'/' securities as BP-SLASH-_LN_Equity, so the harvest path ESCAPES the metacharacter rather than carrying it, mitigating the '/' hazard on that surface. That is one surface and not the key space -- the row stays carried, and WALMEX*_MM_Equity's '*' is untouched by a -SLASH- rule."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S41",
      "AMGT_CORPUS-Z-S42",
      "AMGT_CORPUS-Z-S43",
      "AMGT_CORPUS-Z-S44"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @0615fed688 asserts five orders complete and drained, the FWD-17(b) exercised arm at DELTA=0 on the store, the h-5 served rewrite HELD on a measured reader defect, a ratio census over 97 block keys with a workbook side-by-side across 53 names, and two judgment criteria owed.",
    "world_is": "All of that is true as re-measured, and three things the packet does not state: the 0.33 floor is UNEXERCISED by this population while the 3.0 ceiling is empirically supported, so the two bounds do not have the same evidentiary standing; the workbook side-by-side cannot answer its own criterion because 196 of 200 Base-labelled cells carry an empty 'right' and 0 of 37 names yield a comparable number; and the four apparent matches are years.",
    "notes": "FOR THE ROUND-6 ANALYSIS, three items. (1) THE FLOOR AND THE CEILING ARE NOT EQUALLY EARNED and the round-6 analysis should not carry them as one fact. The ceiling has names on both sides within half a unit; the floor has an empty bin and a 0.207 gap to its nearest accept. If the floor matters, the cheapest test is a name deliberately placed near it -- otherwise 0.33 should be recorded as a CHOSEN bound rather than a measured one. (2) THE WORKBOOK FIX IS SMALL AND WORTH CUTTING: capture 'right' alongside 'below' and select the labelled case cell. The comparator now exists, is deterministic and has a venue floor -- it is two fields away from answering the question it was built for, and until it does, FWD-12's workbook half stays ungraded for a third round. (3) Z-S45 is the round's real open item and the issuer held it correctly; the reader build that makes method_version part of the pick is the round-7 cell, and until it lands FWD-18's data half is BUILT AND NOT SERVED."
  }
]
```
