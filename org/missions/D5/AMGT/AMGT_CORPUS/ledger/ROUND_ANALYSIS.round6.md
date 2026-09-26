# AMGT_CORPUS -- ROUND 6 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-26 ~18:0xZ

**Answers** `ADJUDICATION_v9` @`37a8542a71` (`3.0.0_SA_CVO~Z`, L8+L9 over `ROUND6_DRAIN_END_PACKET.md`
@`0615fed688`).

**CUT WITHOUT A BROKER SLUG, DELIBERATELY.** The `opal-agent-comms` MCP server disconnected at ~17:5xZ, so this
seat cannot `check_inbox`, `send_message` or ack. **The adjudication is a COMMITTED ARTIFACT and I graded it at its
pin; the slug is only its delivery.** Precedent: the round-5 19-outcome pass, cut the same way. **The BROADCAST
this analysis owes is UNSENT and named in section 7** -- it is not skipped, it is owed.

**Round 6 is CLOSED. The project is NOT closed.**

---

## 1. THE HEADLINE -- I AUDITED ONE BOUND OF A TWO-BOUND BAND

Round 5's analysis made the ceiling finding: *"NFLX is refused at 3.0430 against a ceiling of 3.0 -- a 1.4%
margin ... a threshold is validated only by cases NEAR it."* Round 6's `h-2` was cut to measure it. **It did, and
it answered a question I did not ask.**

| | measured over the population |
|---|---|
| just INSIDE the ceiling (2.5-3.0) | **2** -- SAN_FP 2.566, ZTS_US 2.522 |
| just OUTSIDE it | NFLX_US **3.043**, 0.043 beyond |
| just INSIDE the floor (0.33-0.5) | **0 -- the bin is EMPTY** |
| nearest accept above the floor | RWE_GR **0.537**, a distance of 0.207 |
| the only name below the floor | BA_US at **-0.0916** -- a NEGATIVE ratio, refused `forward_eps_not_positive`, **not a band case at all** |

**THE CEILING IS EMPIRICALLY EARNED.** Two names within 0.48 inside and one within 0.043 outside: that boundary
DISCRIMINATES, and moving it would change dispositions. **My round-5 concern is resolved, in the good direction.**

**AND THE FLOOR IS UNEXERCISED.** Nothing sits near 0.33 on either side. The CVO's sentence: *"the data cannot
distinguish 0.33 from any value in [0.1..0.5]."* **No name in this population would change disposition if the
floor were 0.1, 0.2, 0.3 or 0.5.**

> **A BAND HAS TWO BOUNDS AND I INTERROGATED ONE.** I wrote the rule -- a threshold is validated only by cases
> near it -- and then applied it to `CASE_BAND_HIGH` while `CASE_BAND_LOW` sat in the same two-line constant
> block, with the identical defect, unexamined. **The rule was right and I ran it over half its object.**

**And the one name below the floor makes it worse, not better:** BA_US is refused for `forward_eps_not_positive`,
so it is not a band refusal at all. **The floor has never refused anything.** A bound with zero refusals to its
name is not a calibrated threshold; it is a number nobody has tested.

---

## 2. WHAT ROUND 6 CLOSED, INCLUDING TWO ITEMS MY ROUND-5 LIST NAMED

| row | disposition | what it settles |
|---|---|---|
| `Z-S41` (was ARMED) | **GRADUATED** | **`FWD-17` (b) is EXERCISED and PASSES** -- `read_dossier` serves the last write 95 of 95, and the arm **wrote 0 TWICE at unchanged `inputs_sha16 fc1e3a62101e4598`**. My round-5 candidate violation (3 same-day objects, same first input sha, different `content_sha256`) is answered: **a rebuild on unchanged inputs writes NOTHING.** `DELTA=0` on the store, so no never-widen pair was owed |
| `Z-S43` | **GRADUATED** | **`FWD-2`'s one bronze-without-silver is the Copa Holdings byte-identical pair** -- the residual my round-5 pass flagged as a surprise row, resolved and not a gap |
| `Z-S42`, `Z-S44` | **GRADUATED** | the disarm/lift carrier and the hold it lifts |

**`Z-S41` is the one that matters most.** Round 5 could only name a DISCRIMINATOR for `FWD-17` (b) -- run the
rebuild twice and read whether the second writes. **Round 6 ran it, and it wrote zero twice.** The candidate
violation was a real question with a clean negative answer.

---

## 3. WHAT IS CARRIED, AND WHY THE BIGGEST ONE IS AN EXPOSURE RATHER THAN AN INCIDENT

**`Z-S45` (BLOCKING, ARMED) -- CARRIED.** The continuation readers take the FIRST sorted input-matching key, and
`inputs` does not carry `method_version`, so **a `/2` rewrite would serve terms on 49 of 95 and keep serving `/1`
on 46.** It needs a reader build, not a rewrite.

> **The issuer HELD the rewrite rather than running it.** The CVO calls that *"the correct act and ... why this
> row is an EXPOSURE and not an INCIDENT"*, and I adopt that in terms. **A seat that can see a split-brain
> outcome and declines to cause it has done the work; running the rewrite would have produced a 49/46 split
> across a served surface with no single reader able to tell which half it was reading.**

**This is `FWD-18`'s remaining blocker** -- `h-5` landed the pillar and KPI `terms` (re-graded VALID at
`3f328d0ee0`), so the DATA half moved; the READER is what now stands between it and REALIZED.

**`Z-W2-S10` (ARMED) -- CARRIED**, and its bound is honest: three SERVED Base cases (6861_JP, CAT_US, CSL_AU) sit
in pre-`g-1` blocks **carrying no band or currency fields**. The issuer read them in band (1.257, 0.597, 1.390),
**but the unit cannot be confirmed from fields the block does not carry.** That is the right way to report a
reading whose own provenance is missing -- in band by arithmetic, unconfirmable by field.

**`Z-S39` is PARTLY answered by this round's own evidence:** workbook keys render literal-`/` securities as
**`BP-SLASH-_LN_Equity`**, so the metacharacter is escaped rather than carried. **One surface, not the key space
-- `WALMEX*_MM_Equity`'s `*` is untouched by a `-SLASH-` rule**, so the row stays carried. A mitigation on the
surface you looked at is not a mitigation of the class.

**Earlier-round carries** (`Z-S3`, `Z-S6`..`Z-S9`, all 2026-09-23) stand, and the CVO's caution is correct:
`hazard_standing` is the value written AT SURFACING and is never a current-state field, so nothing claims any of
them live today.

---

## 4. L8 READ SOUNDLY

`_latest_dispositions`: **74 items, 10 files, `unknown: []`, 30 NON-TERMINAL.** Round-6 window **9 rows**; the
packet named seven and **the other two are the CVO's OWN** (`Z-S39`, `Z-S40`), so the packet's row set is
COMPLETE for the issuer's rows. **A compiler that finds its own rows in the window and says so is the only kind
whose "complete" means anything.**

`h-2` AC4 and `h-5` AC4 are the **2 of 17** criteria carrying `judgment="true"`, and L7 was **RE-MEASURED, not
adopted** -- 5 of 5 `h-` orders complete on their LAST status tag.

---

## 5. FWD GRADES -- THE MOVEMENT

| outcome | round 5 | now |
|---|---|---|
| `FWD-17` | NOT REALIZED (half (b) a candidate violation) | **half (b) EXERCISED and PASSES**; half (a) still needs a write act |
| `FWD-2` | REALIZED with a disclosed residual | **residual RESOLVED** (Copa byte-identical pair) |
| `FWD-14` | NOT REALIZED (census named four, fence named three) | `h-4` emits **FWD-14's own three counts in FWD-14's names** -- re-graded VALID @`01f9c49f93` |
| `FWD-18` | NOT REALIZED | DATA half moved (`terms` land); **blocked on the reader, `Z-S45`** |
| `FWD-12` limb 3 | data half MET (A2) | unchanged; render is `AMGT_RESAPP` `FWD-24`'s |

**I am NOT converting these into a new REALIZED count in this analysis.** Round 5's count came from a whole
19-outcome pass over one evidence artifact; **asserting a new total from five drain messages would be the partial-
denominator defect round 4 found and round 5 repeated.** The next 19-outcome pass produces the number.

---

## 6. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` recuts for round 7

| # | cell | note |
|---|---|---|
| 1 | **`Z-S45`'s reader build** -- BLOCKING | `inputs` must carry `method_version`, or the reader must select on it; until then a `/2` rewrite splits 49/46 |
| 2 | **The 0.33 FLOOR** -- earn it or retire it | the bin 0.33-0.5 is EMPTY and the only sub-floor name is refused for a different cause. Either find names near it, or state the floor as UNCALIBRATED in the contract rather than carrying it as though measured |
| 3 | **`AC4`'s workbook half** -- still cannot answer its own criterion | third round carrying it; the ratio band must not stand in for it |
| 4 | **`Z-W2-S10`'s three pre-`g-1` blocks** | re-mint so band and currency fields exist, or the in-band reading stays unconfirmable by field |
| 5 | **`Z-S39`'s `*` case** | `-SLASH-` escaping does not cover `WALMEX*_MM_Equity` |
| 6 | **A fresh 19-outcome pass** | the only sound way to restate the REALIZED count (section 5) |

**NOT a cell:** `FWD-12` limb 3's render and `FWD-11`'s render -- both `AMGT_RESAPP`'s, per round 5 section 0.

---

## 7. THE BROADCAST THIS ANALYSIS OWES IS UNSENT

Rule 27's L10 is ONE SLUG to the CTO and the CTO's ONE SEND back. **I cannot send: the broker is down.** So:

- **This record is the carrier.** It is committed, and `2.0.0_SA_COO~X` / `3.0.0_SA_CVO~Z` can read it at its pin
  without me.
- **The send is OWED, not waived.** When the broker returns, this analysis goes to the issuer and the CVO, and
  this section is the standing note that it had not gone yet.
- **"Queued if not live" is a wish, not a delivery.** I am not pretending a committed file reached an inbox.

## Compiler Tools

`ADJUDICATION_v9` read at its pin rather than waited for as a slug, which is what let this analysis be cut at all
with the broker down -- the ceiling/floor bin counts adopted with their own numbers rather than restated -- the
`inputs_sha16` and the "wrote 0 twice" pair taken as the discriminator round 5 asked for, so `FWD-17` (b) is
graded on an exercise rather than an inference -- and NO new REALIZED total asserted from drain messages, because
five subjects are not a nineteen-outcome denominator.
