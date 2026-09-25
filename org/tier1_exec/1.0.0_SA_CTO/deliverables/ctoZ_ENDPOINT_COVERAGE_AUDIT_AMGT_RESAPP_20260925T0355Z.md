# ENDPOINT COVERAGE AUDIT -- `AMGT_RESAPP`, 2026-09-25 ~03:5xZ, `1.0.0_SA_CTO~Z`

**Why this exists.** The goal says *"Finish `AMGT_RESAPP`, `AMGT_CORPUS` and close them out."* Rule 27
closes a project **"when every FWD grades REALIZED."** I have written three round analyses tonight and
never once asked **how many of this project's declared outcomes carry a grade at all.** This is that
census, and it changes the remaining distance materially.

---

## 1. THE MEASUREMENT

**Denominator: 30 declared `endpoint_outcomes`** (`AMGT_RESAPP_PRD.md` header, `FWD-1`..`FWD-30`).
**Instrument:** a lexical census of all 39 committed round analyses (`ROUND_ANALYSIS.round1..40.md`),
taking for each outcome the most recent ROUND whose text places a grade token within 120 characters of
the id, with ranges expanded.

| band | count | which |
|---|---|---|
| **REALIZED** at last mention | **11** | `FWD-3` (round 36); `FWD-21`..`FWD-30` (rounds 37-40) |
| **NOT_REALIZED** at last mention | **13** | `FWD-1`, `FWD-2`, `FWD-4`..`FWD-14` |
| **NO GRADE FOUND** in any analysis | **6** | `FWD-15`..`FWD-20` |

**Twelve of the thirteen NOT_REALIZED were last graded in ROUND 1.** The project is at round 41.

## 2. WHAT THIS DOES AND DOES NOT ESTABLISH -- the instrument's own bound

**MEASURED:** what the LEDGER RECORDS. **NOT MEASURED:** whether those outcomes are realized in the
product today. Forty rounds of work sit between round 1 and now, and several of these outcomes have
plainly been advanced by cells that did not restate the outcome id beside a grade token.

**So this is not a claim that 19 outcomes are open. It is a claim that 19 outcomes CANNOT BE SHOWN
CLOSED FROM THE RECORD** -- and for a completion test that reads the record, those are the same thing.
**A project cannot close on outcomes nobody has graded**, whichever way the grades would fall.

WARN: **I nearly published a worse version of this.** The first run reported `FWD-22`..`FWD-27` as NEVER
GRADED. They are graded -- as a RANGE, `` `FWD-21`..`FWD-28` | **REALIZED** `` -- which my regex did not
expand. Twelve false entries. **A census with one provably wrong arm has no trustworthy arms**, so the
first run was discarded rather than corrected in place, and the rerun's range expansion is why
`FWD-22`..`FWD-28` now read REALIZED. The remaining six with NO GRADE FOUND survived both instruments.

## 3. HOW THIS HAPPENED, and it is visible in my own words

Round 38's analysis states its own scope plainly: **"Denominator: the 10 outcomes `FWD-21`..`FWD-30`."**
Rounds 38, 39 and 40 each graded that ten-outcome denominator honestly and completely. **The defect is
not in any round -- it is that a 10-outcome denominator has been serving a 30-outcome endpoint for
several rounds, and nothing in the loop compares the two.**

This is Rule 24's own tell, on my own work: **a denominator whose scope is narrower than the sentence
beside it.** Each analysis said "this round's outcomes"; the project's status implied "the project's
outcomes"; and the gap between them was never printed. **Addendum B (`FWD-21`..`FWD-30`) is the visible
work because it is what the recent rounds cut, and visibility became the selection criterion for
grading.**

## 4. WHAT IT MEANS FOR THE GOAL, stated against the goal's own clauses

- *"Visually polished Security Analysis application"* -- this is Addendum B, and it is **REALIZED across
  all ten** of its outcomes. **That half of the goal is genuinely done on the record.**
- *"with all Asset Management research companies folded in"* -- this maps to **`FWD-1`** (*"an analyst
  gets a first-draft pack for a covered name"*), whose last recorded grade is **NOT_REALIZED at round
  1**, and whose last recorded COVERAGE is round 12's *"model for 33 of 89; prose for 12."*
- *"export option functional ... 2pg max or machine readable rich text"* -- `FWD-30`, **REALIZED** on
  branch (b), bounded to ONE name; the population cell `rp-1` is cut and executing.
- *"complete backfill ... through the opal-data-harvest channels"* -- `AMGT_CORPUS`, identity complete at
  94 of 94, backfill NOT.

**So the honest distance is: the APPLICATION half is done and recorded; the SUBSTANCE half
(`FWD-1`..`FWD-20`) is not shown closed for 19 of 20 outcomes.**

## 5. THE REMEDY, and it is this seat's

**A re-grade pass over `FWD-1`..`FWD-20`, graded against each outcome's own PRD fence**, producing for
each: REALIZED / NOT_REALIZED / NOT GRADEABLE-and-why, with the population bound stated where the outcome
is per-name. It is the CTO's work (grading is this seat's at L10) and it is not a round: **no cell is cut
for it, and it blocks no issuer.**

**Cost:** 20 fence reads plus their evidence. **Non-application:** it does not re-open any of the eleven
REALIZED grades, and it does not touch `AMGT_CORPUS` or `AMGT_HARVST`, whose endpoints are smaller and
whose recent analyses grade their full declared set.

**Sequencing:** it runs BEHIND the live rounds rather than ahead of them -- `rp-1`, `f-1`..`f-3` and
HARVST round 6 are executing and none of them waits on this. **The audit changes what "done" means, not
what anyone is doing right now.**

## 6. WHAT I AM NOT DOING

**Not re-grading them in this record.** A grade asserted without reading the fence is exactly the failure
that produced the vacated Peers ruling tonight, and twenty of them written quickly would be twenty
chances to repeat it. **The census is the finding; the grades are the work.**

**And not carding it to Andrew.** No decision of his is required: the outcomes are declared, the fences
are written, and the grading authority is this seat's. Under the queue taxonomy this is neither a call
nor a blocked act -- it is **work**, and naming it as a card would be the avoidance the fourth class
describes.

Push state: this commit LOCAL on landing; origin/CLOUD @`4749dc06e2` at last read. This lane does not
push.

---

# THE RE-GRADE PASS BEGINS -- `FWD-1`, graded 2026-09-25 ~04:0xZ

**`FWD-1` -- NOT_REALIZED.** Graded against its own fence (`AMGT_RESAPP_PRD.md:426-433`), not re-asserted
from round 1.

**THE INSTRUMENT, and why it is sound.** Round 40's six `real-run-served/` captures are **DOM-LAYOUT
measurements** (`visibleElements`, `bandContainers`, `textChars`) -- the instrument for `FWD-21`..`FWD-28`,
and **the wrong instrument for a content claim.** There is no served CONTENT capture in round 40. So I
used the served **rich export** instead, which is sound for exactly one reason: **`FWD-30`'s grade
established the export is field-by-field EQUAL to the page** -- 165 figures, 15 cites, 17 absences,
extras 0, missing 0. Reading the export therefore reads the page, on a verified equality rather than an
assumed one.

**ITS ACCEPT NAMES THREE THINGS ON SCREEN. Measured on `BA_US_Equity`, the best-covered name:**

| item | measured | verdict |
|---|---|---|
| the model numbers | ten fiscal-year sections 2016-2025; `Revenue` x14; 165 figures | **PRESENT** |
| the business description | `## Company Description` exists -- and its own subheading reads **"Filed detail (does not describe the business)"** | **NOT a business description** |
| the segment breakdown | see control below | **ABSENT** |

**THE SEGMENT CONTROL, because a bare-word zero is not an absence -- and it overturned my first read.**
`segment` reads **0**, which I nearly published. The control on Boeing's real segment names reads
`Commercial Airplanes` 1, `Global Services` 1, `BDS` 2, `Defense` 2. **So the names ARE in the document
and the bare-word zero was wrong.** Locating them settles it: `BDS` is ONE filed backlog sentence inside
the "does not describe the business" section, and `Commercial Airplanes`/`Global Services` appear **in
the Management/Board table as parts of executives' JOB TITLES.** Neither is a breakdown of results by
segment. **Positive controls on the same instrument: `Fiscal year` 12, `Revenue` 14, `Company
Description` 1 -- the reader can see what it is meant to see.**

**So two of the three named items fail**, and the second fails in a way worth stating precisely: the page
does not silently omit a business description, it **discloses that the filed detail is not one.** That is
honest behaviour and it is still not the outcome, because `FWD-1`'s analyst wanted the description, not
a notice about it.

**The EXERCISED limb is separately unmet:** *"an analyst has actually done it, not merely could"* -- no
analyst read is recorded. Same person-limb shape as `FWD-30`'s ACCEPT, and it cannot be closed by any
seat.

**AND THE BOUND THAT MAKES THIS WORSE, NOT BETTER:** this is `BA_US_Equity`, the name every round has
exercised. **If the best-covered name in the corpus carries no segment breakdown and no business
description, the other 88 are not better.** The goal's clause *"with all Asset Management research
companies folded in"* is therefore not met at its best case, before the population question is even
reached.

**1 of 20 graded. 19 remain**, and this one took a wrong-instrument correction and an overturned zero to
get right -- which is the argument for grading them one at a time rather than in a batch.

---

# RE-GRADE PASS, ENTRIES 2-3 -- and a rule that governs the remaining 17

## `FWD-10` -- **REALIZED**

Fence `:499-506`. DONE WHEN *"EXERCISED -- a check has actually refused something and the refusal was
seen on the page"*; ACCEPT *"a failure shows as a MARKED VALUE -- never as a blank, a zero, or a row that
quietly disappeared."*

**Measured on the served export:** `REFUSED` x1, and it is a marked value carrying its own cause --
`IS_DIV_PER_SHR: REFUSED -- unit/sign convention is 'SIGN-UNRESOLVED', not MEASURED`. `ABSENT` x18
alongside it. **Not a blank, not a zero, not a vanished row.** Round 40's `ro-1` AC4 independently
established the same string is the PAGE's own refusal, so it is on both surfaces.

## THE RULE THIS PRODUCED -- READ THE DONE WHEN'S QUANTIFIER BEFORE DEMANDING A POPULATION

Round 41 made a one-name pass look like a cardinal sin. **It is not, and the distinction is in the
fence's own grammar:**

- **`FWD-30` is a UNIVERSAL.** *"a field-by-field comparison against the page shows the SAME figures"* is
  a claim about **the name a PM exports**, so it must hold for any of them. One name proved nothing, and
  84 of 89 duly failed.
- **`FWD-10` is an EXISTENTIAL.** *"a check has ACTUALLY REFUSED SOMETHING and the refusal was seen"* is
  satisfied by ONE exercised refusal -- that is what EXERCISED means, and demanding 89 of them would be
  inventing a bar the fence does not set.

**So the population question is not owed by every outcome; it is owed by the ones whose DONE WHEN
quantifies over names.** Applying round 41's lesson indiscriminately would have been over-correction --
the mirror of the error it corrected. **For each of the remaining outcomes the pass asks first: is this
fence an EXISTENCE claim or a UNIVERSAL? Only universals carry a population bound.**

## `FWD-9` -- **NOT GRADEABLE on the available evidence**, and the reason is an instrument bound

Fence `:490-497`. Two limbs: **(a)** the marking is in place so an analyst can tell **at a glance** which
sentences a machine wrote; **(b)** the machine-written ones **sit beside the evidence** behind them.

**Limb (b) is MEASURED and PASSES.** Every drafted sentence in `## Investment Thesis` and `## Risks and
Considerations` is immediately followed by its source, blockquoted with the passage id, the accession and
the paragraph -- e.g. a capex sentence followed by `> P0234 -- accession 000162828026004357 -- ITEM 7 ...
paragraph 141` and the quoted text. The evidence is adjacent, not filed elsewhere.

**Limb (a) CANNOT BE READ FROM THIS INSTRUMENT, and saying so is the point.** A "tell at a glance" marking
is VISUAL -- rounds 38-39 record PASS badges on the thesis sentences -- and **the export is markdown.**
`FWD-30`'s verified equality covers **figures, cites and absences**; it says nothing about badges.
**Extending a three-axis equality to a fourth axis is exactly the wrong-instrument error this pass already
made once on `FWD-1`**, where round 40's DOM-layout captures were reached for to settle a content claim.

**So `FWD-9` waits on a served PAGE read, not on more argument.** It is the second outcome in three whose
grade is gated by an instrument rather than by the product -- which is itself a finding about this
project's evidence base: **the served plane is captured for LAYOUT and for EXPORT, and not for what the
page SAYS.**

**3 of 20 graded: 1 REALIZED, 1 NOT_REALIZED, 1 NOT GRADEABLE.** 17 remain.

---

# RE-GRADE PASS, ENTRY 4 -- `FWD-17` -- **NOT_REALIZED**

Fence `:575-587`. Its ACCEPT is a FOUR-part conjunction and the grade turns on parts three and four
being read separately rather than as one "management tab exists" impression.

| ACCEPT component | measured on the served export | verdict |
|---|---|---|
| one tab lists the senior executives | 12 officers under `## Management/Board` | **PRESENT** |
| each with their ROLE and HOW LONG they have held it | role text plus `Tenure (yrs)` 6.37 / 3.70 / 3.54 / 2.54 ... 1.12 | **PRESENT** |
| each with a PROFILE LINK | `Source` reads `filing` on all 12, and the section's last line reads **`CEO public-profile reading: UNREADABLE_OBJECT`** | **ABSENT, and its source is failing** |
| states how the team's average tenure compares with the average **across EVERY COMPANY THE PAGE COVERS** | no pool line in this instrument; and `ADJUDICATION_v49` quotes the exec footer as *"the pool 4.09 years over 40 officer(s) of **7 name(s)**"* | **FAILS on the DENOMINATOR** |

**The fourth component is the substantive failure and it is not about rendering.** The fence says *every
company the page covers*; the pool is **7 names**. Whether the page covers 89 or 94 -- the card still at
Andrew -- **7 is neither**, so the comparison a PM reads is against a pool two orders smaller than the
one the outcome names. `3.0.0_SA_CVO~Z` had already flagged this as a **stale disclosed denominator**
(`ADJUDICATION_v49`: *"two disclosed denominators went stale today by DECISION rather than by drift"*),
and this grade is the endpoint consequence of that finding rather than a new one.

**INSTRUMENT BOUND, stated:** the pool line may render on the exec TAB and simply not survive into the
markdown export, so "absent" is bounded to this instrument. **It does not matter to the grade** -- the
`v49` quote establishes the pool is 7 names wherever it renders, and a denominator of 7 fails the fence
however well it is displayed. **This is the one component the served-content capture would NOT rescue.**

**Component 4 of the fence -- *"where a person cannot be confirmed ... the page says so"* -- PASSES**, and
notably: `CEO public-profile reading: UNREADABLE_OBJECT` is the page disclosing its own failed read
rather than showing a blank. That is `FWD-10`'s virtue appearing in a second outcome, and it is worth
recording as a thing this product does WELL, in a pass otherwise accumulating gaps.

**DONE WHEN is separately unmet:** *"EXERCISED -- an analyst has used the profile to answer a question
about a management team."* No analyst read is recorded, and the profile it names is the `UNREADABLE_OBJECT`.

**4 of 20 graded: 1 REALIZED, 2 NOT_REALIZED, 1 NOT GRADEABLE.** 16 remain.

---

# RE-GRADE PASS, ENTRY 5 -- `FWD-19` -- **NOT_REALIZED**, and it lands on the universe card

Fence `:603-617`. The machinery is built, honest and well-cited. **It cannot deliver the outcome, and the
reason is not a defect in this project.**

**WHAT IS PRESENT, and it is substantial:**
- **The verdict and its named comparable:** `Verdict: hold (comparable: DE_US_Equity)`.
- **Reasons, each linked to what it rests on** -- five sentences, every one carrying a `> cites:` line of
  specific evidence ids across six prefixes (`S:` sections, `F:` figures, `E:` passages, `FIT:` factors,
  `B:` membership, `C:` rung). **This is the strongest provenance I have seen in the export** and it
  satisfies the fence's *"gives the reasons with each one linked to what it rests on"* outright.
- **Not an instruction:** `hold` is a verdict, and nothing in the section directs a trade.

**WHY IT STILL FAILS -- the posture's own first sentence:**

> *"The comparable Deere pack carries **no thesis, management, peer or model evidence at all**, so no
> side-by-side judgment of its fundamentals is possible from these packs."*

The fence requires the page to *"say whether this company looks like a better or a worse pick than the
most similar name on the other side."* **The page instead says, correctly and in its own words, that the
comparison cannot be made.** That is honest behaviour and it is not the outcome.

WARN: **AND THE COMPARABLE IS `DE_US_Equity` -- DEERE -- WHICH `Z-S270` MEASURED AS OUTSIDE THE 89-KEY
SET.** So the posture selects its symmetric comparable from a universe WIDER than the corpus covers, and
the selected name has no pack **because nothing in scope ever built one for it.** `FWD-19` is therefore
**blocked by the universe question, not by the posture engine** -- the same card that bounds `rp-1` and
that `FWD-17`'s pool-of-7 sits beside. **Three outcomes now turn on one unanswered word.**

**Two components NOT gradeable from this instrument**, and both are the marking problem again: *"marked
as a machine's view for a person to accept or reject"* (visual), and *"a line in the header"* (the Header
section was not read for this). **Not asserted either way.**

**DONE WHEN unmet:** *"EXERCISED -- a PM has read a posture and acted on it, or declined it, on the page."*

**A finding recorded in passing, because it is the product behaving well:** the Peers column table
declares `Present columns (5 of 17 declared)` and states, per column, `P/E 2025 | ey | RECIPROCAL:
P/E = 1 / ey; trailing grain, NOT a 2025 fiscal-year estimate`. **The page discloses that its own column
LABEL and its GRAIN differ** -- independently confirming `Z-S273`'s reciprocal finding from the product's
own mouth, and exactly the "a value must carry its claim" behaviour the estate keeps asking for.

**5 of 20 graded: 1 REALIZED, 3 NOT_REALIZED, 1 NOT GRADEABLE.** 15 remain.

---

# RE-GRADE PASS, ENTRY 6 -- `FWD-8` -- **NOT_REALIZED**, and the fence hands the verdict to a person

Fence `:482-488`. **DONE WHEN *"EXERCISED -- an analyst who distrusted it has stopped"*** -- the test is
an analyst's restored trust, which no seat can supply. **Unmet, and unmeetable from here.** What I CAN
measure is the composition, and it bears directly on whether that trust would be restored.

**MEASURED -- the peer set served for `BA_US_Equity`:** 12 members, **every one `Industrials` /
`United States`**, market caps 100,405 to 266,414 musd. So the set is selected by **SECTOR + COUNTRY +
SIZE**, not by what the business does.

| genuinely aerospace/defence | everything else |
|---|---|
| Lockheed Martin, General Dynamics, Howmet Aerospace -- **3 of 12** | Deere (agricultural machinery), Eaton (electrical), Union Pacific (railroads), **Uber (ride-hailing)**, Trane (HVAC), Vertiv (data-centre infrastructure), Quanta (utility construction), GE Vernova (energy), Parker-Hannifin (motion control) |

**`Uber Technologies` as a Boeing comparable is the tell.** It is GICS-Industrials by classification and
shares no business with Boeing. The fence asks for a list *"genuinely about the company being shown"*;
a sector-and-size screen is a defensible METHOD and it does not clear that bar on this evidence.

**BUT COMPONENT 2 IS SATISFIED, and the distinction matters.** The fence's named failure mode is
*"showing ANOTHER COMPANY'S list"* -- `F6`, *"48 of 54 measured wrong today"*, which is what this outcome
was written for. **That is not happening here:** these are BA's own screen results, not another name's
peers. **The defect this outcome was created to catch is fixed; a different and weaker one remains.**

**So the grade is NOT_REALIZED on the DONE WHEN, and the ACCEPT is SPLIT** -- cross-contamination gone,
business comparability thin. **I am not converting my own read of "Uber is not a Boeing peer" into the
grade**, because the fence deliberately assigns that judgment to an analyst who distrusted the block.
**Naming the composition is the useful act; declaring the trust restored or withheld is not mine.**

**AND THE ABSENCE DISCLOSURES HERE ARE THE BEST IN THE PRODUCT**, recorded because this pass should not
only accumulate gaps. Twelve columns are declared ABSENT and **each names its own cause against a printed
denominator** -- *"no preferred-equity code among the 289 registry factors"*, *"the growth category tops
out at a THREE-year window"*, *"cash_mv is 'Cash to Market Value', a RATIO; no absolute cash level"*,
*"P/E 2027: the value category carries trailing (ey) and NTM (ey_ntm) only -- no second-forward-year
estimate at any grain"*. **That is a value carrying its claim, twelve times over, with the registry as
its denominator.**

**6 of 20 graded: 1 REALIZED, 4 NOT_REALIZED, 1 NOT GRADEABLE.** 14 remain.

## PATTERN AFTER SIX -- worth stating before the remaining fourteen

**Five of the six failures are NOT rendering defects.** They are: a missing business description and
segment breakdown (`FWD-1`), a pool of 7 where the fence says every covered company (`FWD-17`), a
comparable outside the corpus with no pack (`FWD-19`), a population that diverges on 84 of 89
(`FWD-30`), and a peer set screened by sector rather than business (`FWD-8`). **The product RENDERS what
it has, discloses what it lacks, and cites what it asserts -- consistently and well.** What it does not
yet have is the SUBSTANCE behind the frames. That is the same split the endpoint audit found from the
other direction, and two independent readings agreeing is worth more than either alone.

---

## `FWD-5` -- **NOT_REALIZED.** THE SERVED PDF IS **13 PAGES**, AND THE GOAL SAYS 2

Fence `:461-466`. **The instrument was already ruled, which is why this grade is possible at all:**
`ROUND_ANALYSIS.round11.md@4055200e2f` A1.3 R2 -- *"NOT ruled a browser act: `FWD-5`'s displacement test is
that a person forwards the output AS PRODUCED, and a browser-rendered print is the analyst's own
reformatting under another name."* So the object to grade is the SERVED pdf, and nothing else.

**AND NO ROUND HAD EVER TAKEN THAT MEASUREMENT.** Round 40's served capture
(`0.9.0_WK_AMGT_RESAPP~150/served_capture.py:120`) builds `{"path": print_path, "query": {"format": "rich"}}`
-- **rich only.** The pdf axis has been unmeasured through 42 rounds. This is its first read.

**MEASURED** -- one `lambda:Invoke` of `opal-amgt-scoped-api` (`CodeSha256 pmH20bb+L1Kcejf4MKS4tVt+tCIPgeHwSZAsTe+nXZo=`,
`LastModified 2026-09-24T23:54:02Z`), at `/api/scoped/amgt/security/BA_US_Equity/print` with **no format
argument** and again with `format=pdf`. Both: `status 200`, `Content-Type application/pdf`,
`isBase64Encoded True`, **113,853 pdf bytes**.

| what the fence and the goal ask | what the served pdf is |
|---|---|
| the goal: *"2pg max"* | **13 PAGES** (`pypdf`, `len(reader.pages)`) |
| *"replaces the document he circulates today"* | 420 extracted lines, of which **391 are figure lines** -- one line per figure, each carrying value, unit class, mnemonic, **the full Bloomberg field description in parentheses**, the as-of stamp and the source |
| *"rather than looking like a screenshot of a dashboard"* | **it does not look like a dashboard screenshot. It looks like a FIELD DICTIONARY** -- a third thing the fence never named |

**AND THE PDF CARRIES LESS THAN THE RICH EXPORT, not more.** Its sections, read off the extracted text:
title (`BOEING CO/THE [BA US Equity] Research Note`), `MODEL BLOCK`, `Header`, `Fiscal year 2016` through
`Fiscal year 2028` (13 years), `Management/Board`. **That is all.** No Recommendation, no Company
Description, no Investment Thesis, no Risks, no Peers, no Analyst Posture, no Model Notes, no Model Cases
-- **every one of which the 402-line rich export carries.** So the pdf is a strict SUBSET of the rich
document, rendered at 13 pages because each figure occupies a full line of provenance.

**THIS SPLITS THE GOAL'S OWN SENTENCE, and that is the finding worth more than the grade.** The goal reads
*"presentation in Opal Brand Guidelines form mimicking Asset Mgmt team's earnings reports 2pg max **or**
machine readable rich text output"*. **The rich-text branch is BUILT** (`FWD-30` branch (b); the 402-line
markdown). **The 2-page branded branch does not exist at all** -- what sits at the pdf route is a 13-page
provenance dump carrying a subset of the rich document's content. An `or` was satisfied on one side and the
other side was never started, and because the route answers 200 with a real pdf, **nothing in the record
read as missing.**

**DONE WHEN separately unmet:** *"EXERCISED -- Adam has actually forwarded one."* No forward is recorded,
and this is not a thing a seat can supply.

### A SECOND FINDING FROM THE SAME RUN -- 192 of 391 figure lines carry NO UNIT CLASS

Counted, denominator printed: **391 figure lines, 192 of them `[UNRESOLVED UNIT]` -- 49%.** Distinct
mnemonics on the pdf: **64**. Distinct mnemonics with no unit class: **26**, and they are not a random tail:

`BEST_BPS BEST_CAPEX BEST_DIV_YLD BEST_DPS BEST_EBIT BEST_EBITDA BEST_ESTIMATE_FCF BEST_NET_INCOME`
`BS_CASH_NEAR_CASH_ITEM BS_TOTAL_LIABILITIES EBITDA_TO_REVENUE EQY_DPS EQY_FUND_CRNCY`
`FREE_CASH_FLOW_MARGIN FREE_CASH_FLOW_YIELD GROSS_MARGIN IS_ADJUSTED_GROSS_PROFIT`
`IS_ADJUSTED_OPERATING_INCOME IS_COMP_EPS_ADJUSTED IS_DIL_EPS_CONT_OPS NET_INCOME`
`PX_TO_FREE_CASH_FLOW RETURN_ON_CAP RETURN_ON_INV_CAPITAL RETURN_ON_TANGIBLE_ASSETS REVENUE_PER_SH`

**EVERY `BEST_*` FORWARD ESTIMATE IS IN THAT LIST, and so is `NET_INCOME`.** The resolved ones
(`SALES_REV_TURN MILLIONS`, `OPER_MARGIN PERCENT`, `PE_RATIO RATIO`) are the older registry entries; the
unresolved ones are the later additions. **This is a REGISTRY-COVERAGE boundary showing through to the
served artifact**, not a renderer defect -- the renderer prints exactly what the registry gave it and marks
the gap, which is the right behaviour. **It bears on `FWD-3`** (*"defend every number on the page"*): a
figure whose unit is `[UNRESOLVED UNIT]` cannot be defended in a meeting, and `NET_INCOME` is not a
figure anyone will let pass. **Routed to `2.0.0_SA_COO~Z` as a round-43 input; not a cell I cut.**

**7 of 20 graded: 1 REALIZED, 5 NOT_REALIZED, 1 NOT GRADEABLE.** 13 remain.

---

## `FWD-2` -- **NOT_REALIZED, and its blocker is a RESERVATION this fabric cannot lift**

Fence `:435-442`. ACCEPT: an analyst types the ticker of a never-covered company and **gets the same
assembled page**, which **says plainly it is being fetched now** rather than shown from an earlier save.
DONE WHEN: *"EXERCISED -- a real uncovered name has been pulled and read."*

**THE PRD ALREADY RULED WHY THIS CANNOT CLOSE HERE.** `C-ROUND12-PULL-WIRED` (`AMGT_RESAPP_PRD.md:1042-1051`),
`FWD-2`'s own named carrier, ruled at L10 `ROUND_ANALYSIS.round11.md@4055200e2f` A1.3 R3 as corrected by
Addendum 2 C1, verbatim:

> *"The on-demand pull is WIRED, not retired: the page calls the enqueue route, and the adapter DECLARES its
> queue carrier so the refresh route stops answering 501. THE CONSUMER STAYS BOX-SIDE AND IS NOT A LAMBDA.
> ... **NO LAMBDA CONSUMER IS BUILT**, and the consumer's CADENCE is RESERVED to Andrew by name, on the same
> standing as the harvest cadence -- a card, never a cell."*

**So the half of `FWD-2` the fabric can build is the ENQUEUE, and the half that makes it an outcome is the
DRAIN -- which is reserved, unbuilt, and box-side by a dependency rather than a preference** (the consumer
reaches the Bloomberg desktop interface on the terminal box's loopback, so a Lambda consumer would fail
every message at the health check). A name typed today enqueues and is never pulled. **`FWD-2` is
NOT_REALIZED, and no round can move it.**

**AND I DID NOT EXERCISE IT, deliberately.** Calling the refresh route for an uncovered ticker is the act
the outcome describes, and it is a WRITE that enqueues work whose consumer reaches a vendor terminal. Under
*"NEVER call an external vendor API without Andrew's explicit per-use word -- availability is not
authorization"*, the exercise is not mine to run. **The instrument bound and the law point the same way
here, which is the cheap case:** grading it on the PRD's own ruled contract costs one read and reaches the
same answer the exercise would.

**THIS IS THE FOURTH OUTCOME OF THE PASS BLOCKED BY SOMETHING OUTSIDE THE PRODUCT** -- `FWD-17` and
`FWD-19` on the unanswered universe word, `rp-1` on the same, and now `FWD-2` on a reserved cadence.
Three of the four are ONE card at Andrew; this one is a SECOND card, and it is a different question:
**not "which universe", but "who drains the queue, and how often".** It goes to him as a card, per the
contract's own words, and nothing in the loop waits on it.

**8 of 20 graded: 1 REALIZED, 6 NOT_REALIZED, 1 NOT GRADEABLE.** 12 remain.

---

## FOUR OUTCOMES ON ONE MEASUREMENT -- `FWD-6`, `FWD-7`, `FWD-12`, `FWD-14`

**The measurement that grades all four is a DIFF WITH BOTH DENOMINATORS PRINTED**, and the adapter predicted
its own result. `scoped_amgt.handler`'s docstring (`:3945-3960`): *"THE ROUTE TABLE IS THE DENOMINATOR.
SIXTEEN routes ... eleven of these sixteen have a client call, five do not yet. A reader who diffs this table
against the client's call set will find five routes with no caller -- that is the true state, not drift."*

**ADAPTER SIDE, as DATA not as prose:** `scoped_amgt_route_table()` returns **16** routes.
**CLIENT SIDE:** `portal/src/api/endpoints/amgt-lead-panel.ts` builds **10** call functions on **11** routes
(`setStarred` is star-or-unstar). **BY SUBTRACTION from the printed 16 -- Rule 24's method, never a forward
list -- the FIVE with no client call are:**

| route, served but uncalled | the outcome it was built for |
|---|---|
| `GET /api/scoped/amgt/freshness` | `FWD-7` |
| `GET /api/scoped/amgt/lists` | `FWD-14` |
| `GET /api/scoped/amgt/security/{key}/ledger` | `FWD-12` |
| `GET /api/scoped/amgt/security/{key}/versions` | `FWD-6` |
| `GET /api/scoped/amgt/security/{key}/compare` | `FWD-6` |

WARN: **MY FIRST INSTRUMENT FOR THIS WAS BROKEN AND ITS OWN POSITIVE CONTROL CAUGHT IT.** I searched
`apiRequest[^)]*(peers|coverage)` and got ONE hit, on a different route -- because
`encodeURIComponent(securityKey)` puts a `)` inside the path and `[^)]*` stops there. **A route I knew was
called did not appear, so the matching zero on the five was worthless.** Re-run on
`BASE\}/security/[^']*/(...)`: the positive arm returns all five called leaves at `:125 :132 :138 :145 :155`,
and two independent negative patterns return **0 across 1042 scanned files**. That is the zero I am grading on.

**AND THE SERVED HALF IS REAL AND GOOD -- five live invokes, all `status 200`:** `freshness` 102,013 body
chars, `lists` 1,661, `ledger` 1,461, `versions` 1,807, `compare` 11,744. Every one returns a `denominators`
block. **So `C-ROUND12-SURFACED-OUTCOMES` is satisfied on its first limb and fails on its second** -- the
contract's words are *"each get a SERVED ROUTE **and a PAGE SURFACE**"*, and *"an outcome whose only
implementation is a hand-run module is NOT REALIZED, whatever its rows say."* These are better than hand-run
modules and they are still not on a page.

### `FWD-6` -- **NOT_REALIZED, and it is the strongest near-miss in the product**

Fence `:468-473`. **BOTH ACCEPT CLAUSES MEASURE TRUE on the served plane:**

- *"Refreshing adds a version; it does not overwrite the old one"* -- `versions` returns **10 versions**,
  `objects_listed 10`, stamps from `20260910T224432Z` to `20260925T043907Z`. **Nothing was overwritten.**
- *"can say what moved, naming the earlier version that shows it"* -- `compare` returns `from_stamp`,
  `to_stamp`, and `added 212, removed 0, changed 7, unchanged 172` over `figures_from 179 -> figures_to 391`.
  **It names the versions and itemises the movement.** `reason` is `null` because it had no reason to refuse.

**So the failure is not substance and not rendering. It is ELEVEN LINES OF CLIENT CODE THAT DO NOT EXIST.**
Of everything graded in this pass, `FWD-6` is the one where the product's own capability is complete and the
outcome is unreachable anyway. **That is a different failure class from the other nine and should be cut
differently** -- it is a wiring cell, not a build cell.

**DONE WHEN unmet:** *"EXERCISED -- someone has actually compared two versions."* Nobody has, because there
is nowhere to do it from.

**AND ONE CROSS-INSTRUMENT AGREEMENT WORTH BANKING:** `compare`'s `figures_to` is **391**, which is exactly
the figure-line count I measured independently off the served PDF. Two unrelated instruments on the same
object agreeing is worth more than either. It also shows the model block roughly **DOUBLED today** (179 ->
391, `added 212`) -- `AMGT_CORPUS` round 4's re-pull landing on the served plane, corroborating row `Z-S277`
from a third direction.

### `FWD-7` -- **NOT_REALIZED, and its denominator is a FOURTH universe: 250**

Fence `:475-480`. `freshness` serves **250 rows** with `last_refreshed` and a `per_input` map per name
(`bloomberg`, `seekingalpha`, `serp`). The content is right and the surface is absent.

**THE DENOMINATOR IS THE FINDING.** `universe_denominators` on the route's own body:
`coverage 89, holdings_distinct 167, union 250, both 6, resolved 191, unresolved 59`. The fence says *"every
company the team covers"*; the route serves **the UNION, 250** -- wider than the fence, not narrower, so the
content clause passes. **But this is now the FOURTH denominator loose in one project: 89 (frozen snapshot),
94 (live research group), 7 (`FWD-17`'s tenure pool), 250 (this route's union).** The card at Andrew is no
longer a tidying question.

**AND THE ROUTE MEASURES THE GOAL'S BACKFILL CLAUSE DIRECTLY, which nothing else has:**
**`never_refreshed 196` of 250, `with_something_landed 54`.** Against `coverage 89`, at most **54 of 89**
covered names carry anything at all. The goal asks for *"complete backfill for all of these securities"*;
**this is the first number in the record that bounds how far that is from done, and it came out of an
outcome grade rather than a backfill measurement.**

One blemish, recorded: every row carries the same `rot` string
(*"publishers: not stale (0/2 stale ...) | social_accounts: not stale (0/267 stale ...)"*). That is
`FWD-14`'s list-rot field replicated onto all 250 rows; it is not per-company staleness, and a reader could
take it for one.

### `FWD-12` -- **NOT_REALIZED, and the fence's own disqualifier names what the client DOES call**

Fence `:519-527`. The `ledger` route returns `classes`, `latest_by_class`, `entries_total`, `outcomes` --
per-input provenance, which is the fence's first half. **No client call.**

**The second half is where it is sharpest.** The fence says *"any one can be re-run on its own. **A single
button that refreshes everything under one timestamp does not count.**"* The ONE refresh route the client
does call is `POST ${BASE}/refresh` (`amgt-lead-panel.ts:115`), which is `FWD-2`'s whole-pack enqueue --
**precisely the single button the fence disqualifies.** So the page offers the disqualified control and
withholds the qualifying one.

### `FWD-14` -- **NOT_REALIZED, blocked by TWO reservations, and its refusals are exemplary**

Fence `:541-549`. `lists` serves both declared lists (`lists_declared 2, lists_served 2`) with
`entries_total`, `entries_stale`, `reviewed_at`, `review_interval_days`.

**The fence's first clause is *"each have a named person responsible"*, and the route answers, verbatim:**
`"owner": "UNASSIGNED -- Andrew names the owner (C-NO-CONTACT: not Adam's team directly)"`,
`"owner_status": "UNASSIGNED"` -- **for both lists.** The field exists, it is honest, and the value is
RESERVED to Andrew by the contract's own words. **The second clause, *"when one goes out of date somebody is
told"*, is reserved a second time** -- the standing moratorium forbids building a notifier without Andrew's
explicit ask. **Two reservations on one outcome; no cell can close it.**

**AND THE ROUTE REFUSES ONE LIMB IN THE BEST WAY I HAVE SEEN IN THIS PRODUCT:**
`"unresolvable_count": "NOT_EXERCISED"` with `"dns_limb": "not exercised by the served route: resolving every
publisher domain is egress off this estate's infrastructure taken on behalf of a request; run the lists
module by hand for that count"`. **A served route declining to take egress on a caller's behalf, naming the
egress, and pointing at the hand-run path instead.** That is the vendor-egress law applied by the code
without a seat in the loop, and it is the right call.

**12 of 20 graded: 1 REALIZED, 10 NOT_REALIZED, 1 NOT GRADEABLE.** 8 remain
(`FWD-3`, `FWD-4`, `FWD-11`, `FWD-13`, `FWD-15`, `FWD-16`, `FWD-18`, `FWD-20`).

## THE FAILURES NOW SPLIT INTO THREE CLASSES, and they need different cells

**Ten NOT_REALIZED is not ten problems.** Sorted by what would close them:

| class | outcomes | what closes it |
|---|---|---|
| **WIRING** -- the capability is built and served, nothing calls it | `FWD-6`, `FWD-7`, `FWD-12` | client calls plus a surface. Cheapest by far, and `FWD-6` needs no backend work at all |
| **SUBSTANCE** -- the frame renders, the content behind it is thin or absent | `FWD-1`, `FWD-5`, `FWD-8`, `FWD-17`, `FWD-19`, `FWD-30` | real work: a 2-page branded export, a business description, a segment breakdown, a business-similarity peer set, a 94-name tenure pool |
| **RESERVED** -- a word only Andrew can give | `FWD-2` (queue-drain cadence), `FWD-14` (list owner + notification) | nothing the fabric can cut |

**The three classes were invisible while the pass reported a running NOT_REALIZED count.** Naming them is
what lets round 43 cut the cheap class first: **`FWD-6` alone converts a complete, measured, unreachable
capability into a reachable one.**

---

## `FWD-18` -- **NOT_REALIZED, and it has the best ACCEPT showing in the pass: THREE of four clauses measure TRUE**

Fence `:589-599`. Instrument: a fresh live read of the `thesis` route (client-called at
`amgt-lead-panel.ts:132`) plus a fresh rich export, both taken at `2026-09-25 ~06:2xZ`.

| clause | measured |
|---|---|
| *"in the company's own words and with each sentence linked to the passage in the filing it came from"* | **PASSES** -- each served sentence carries `P0234 -- accession 000162828026004357 -- ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS / paragraph 141` and the paragraph's full text |
| *"what the company is doing now, its biggest challenges and its biggest bets"* | **TWO of three.** Capex trend (doing now) and the 737-9 door-plug response (challenges). **"biggest bets" is ABSENT** |
| *"one chart, chosen for that company, of the thing it lives or dies on"* | **PASSES, and it is good** -- see below |
| *"the Model tab's figures are the plain financial model, built the same way for every company"* | the same mnemonic set across names; **27 of them REFUSED** (see `FWD-5`'s registry finding) |

**THE ONE CHART IS SERVED AND IT IS THE BEST-CHOSEN THING IN THIS PRODUCT.** `thesis_driver_chart`:
`status SERVED`, `driver_series "Commercial Airplanes (BCA) aircraft deliveries"`, `source "filing"`,
three points -- **2023: 528, 2024: 348, 2025: 600 aircraft** -- **each carrying its own `passage_id` and a
character `span` into the filing**, `held_uncited_count 0`. And the driver's own stated reason:
*"BCA revenue growth and the swing in operating cash flow were both driven primarily by higher
deliveries, making delivery volume the measurable hinge of the business."* **That is a chart chosen for
Boeing specifically, of the thing Boeing lives or dies on, with every point traceable to a filing
passage.** The fence's hardest-to-fake clause is the one that passes cleanest.

WARN: **I NEARLY FILED A FABRICATED-CITATION FINDING AND THE CAUSE WAS MY OWN TRUNCATION.** My first read
printed each line at 170 characters. The drafted sentence *"Capital expenditures totaled $2.9 billion in
2025, up from $2.2 billion in 2024 and $1.5 billion in 2023"* sat beside a quote that opened *"Investing
Activities Net cash provided by investing activities during 2025 was $0.5 billion, compared with cash used
of $12.0 billion..."* -- different subject, different numbers, and it read as a sentence cited to a
paragraph that does not support it. **The paragraph is 1,122 characters and its NINTH sentence is
"Capital expenditures totaled $2.9 billion in 2025, compared with $2.2 billion in 2024 and $1.5 billion in
2023."** The citation is exact. **The positional-slice trap, for the fourth time this session, and this
time it would have accused the product of the one defect that would most damage trust in it.** The rule
that saved it is the one already in the record: go back for the untruncated bytes before converting a
mismatch into a finding.

### AND THE REASON THERE ARE ONLY TWO SENTENCES IS MEASURED, NAMED, AND PRODUCER-SIDE

**`held_no_span_count: 21`**, with `held_no_span_basis: "READ_GATE_ONLY_OBJECT_FIELD_ABSENT"` and
`held_uncited_count: 0`, `drafting_status SERVED`, `drafting_read_completed true`.

**So the Thesis has 23 drafted sentences and serves 2.** Twenty-one are withheld by the read gate because
**the span field is ABSENT ON THE OBJECT** -- the drafting producer did not write character spans for them,
and the reader correctly refuses to serve a sentence it cannot point at. **The gate is behaving exactly as
FWD-9 demands, and the cost is 91% of the drafted prose.**

**THIS IS THE SHARPEST SUBSTANCE FINDING OF THE PASS, and it is ONE producer-side fix.** `FWD-18`'s missing
*"biggest bets"* is almost certainly among the 21; `FWD-9`'s marking limb and `FWD-3`'s defensibility limb
both ride on the same 21. **A single cell that writes spans on the drafting object moves three outcomes** --
and unlike the wiring class, it is invisible from the served artifact, because the page shows two
well-cited sentences and says nothing about the twenty-one it is holding.

**DONE WHEN unmet:** *"EXERCISED -- an analyst has clicked a filing-derived figure through to the passage
it came from."* Not recorded.

---

## `FWD-20` -- **NOT_REALIZED. The house forecast DOES NOT EXIST, was RULED not to exist, and says so correctly**

Fence `:618-637`. This is the largest single unbuilt thing in the endpoint, and the record is unambiguous.

**THE MODULE'S OWN DOCSTRING IS THE GRADE** (`lib/research/scores/divergence.py:12-19`, ruled Andrew-direct
2026-09-15 ~18:3xZ @`287d2c2619`):

> *"THE HOUSE FORECAST DOES NOT EXIST YET (FWD-20, CTO~W call 4, adopted verbatim): 'D is ABSENT with reason
> until FWD-20 serves' ... `score_divergence` in this module therefore ALWAYS returns ABSENT for D today, by
> construction (no `model_fcf` producer to call) -- and that is the CORRECT, RULED behaviour, not a failure
> this cell owes a fix for."*

`score_divergence(model_fcf=None)` returns, and I read it live off the served `thesis` route
(`scores_status SERVED`):

> `{"D": null, "U": null, "Delta": null, "state": "ABSENT_SOURCE", "absent_reason": "FWD-20's house FCF`
> `forecast has not been built yet (no model_fcf producer exists); D is ruled ABSENT with reason until it`
> `serves, per CTO~W adjudication call 4", "dispersion": null}`

**So the fence's DISCLOSURE clause -- *"states ABSENT, with the reason, for every name where the house
forecast does not yet serve"* -- PASSES, on a served, client-called route.** And the degeneracy guard
(*"the spread of Divergence across the covered universe is checked for the sign that the drivers were
seeded from consensus after all"*) is satisfied vacuously: nothing is shown, so nothing is shown unchecked.
**The fence's SUBSTANTIVE clause -- *"a forward free-cash-flow forecast is produced for a covered name from
the company's own filings and its history, seeded independently of consensus"* -- is UNBUILT.**

**AND THE STREET SIDE OF THE COMPARISON IS ALSO REFUSED, which nothing had joined up.** The rich export's
Model Notes refuses **every `BEST_*` consensus figure** -- `BEST_EBITDA`, `BEST_DPS`, `BEST_DIV_YLD`,
`BEST_EBIT`, `BEST_NET_INCOME`, `BEST_CAPEX`, `BEST_ESTIMATE_FCF`, `BEST_BPS` -- each
*"unit/sign convention is 'NOT-YET-BUILT', not MEASURED"*. **`BEST_ESTIMATE_FCF` is the consensus NTM FCF
that is `D`'s own subtrahend.** So `D = (model NTM FCF - consensus NTM FCF) / dispersion` is missing BOTH
operands: the minuend has no producer and the subtrahend is refused for want of a unit convention.
**The house-forecast cell is not the only prerequisite, and that was not visible from either side alone.**

### AND ONE STALENESS FINDING THE GRADE TURNED UP

**The served scores object is `as_of 2026-09-17`. The model block it sits beside is `2026-09-25`.**
Eight days, across the day `AMGT_CORPUS` round 4 roughly doubled the block (179 -> 391 figures). So
`robustness` (*"n=1 of 6 measured ... below the n>=5 eligibility floor"*) and `peers_v` (`K=12`, every
measure *"ABSENT for the subject"*) were both computed against a block that no longer exists.
**Their absences may be artefacts of the vintage rather than of the data**, and neither carries a field
that would let a consumer tell. Routed as a round-43 input: **re-run the scores producer before anyone
reads an absence off it.**

**14 of 20 graded: 1 REALIZED, 12 NOT_REALIZED, 1 NOT GRADEABLE.** 6 remain
(`FWD-3`, `FWD-4`, `FWD-11`, `FWD-13`, `FWD-15`, `FWD-16`).

**THE THREE-CLASS SPLIT UPDATES:** WIRING `FWD-6`, `FWD-7`, `FWD-12`; **SUBSTANCE** `FWD-1`, `FWD-5`,
`FWD-8`, `FWD-17`, `FWD-18`, `FWD-19`, `FWD-20`, `FWD-30`; RESERVED `FWD-2`, `FWD-14`. **And the substance
class now has a cheapest member of its own: the 21 held sentences.** One producer-side span write moves
`FWD-18`, `FWD-9` and `FWD-3` together, which no other substance fix does.

---

# THE LAST SIX, AND A CORRECTION OF MY OWN GRADE

All six graded off live reads of the `overlay`, `thesis` and `lead-panel/rankings` routes at
`2026-09-25 ~07:0xZ`. **Every one of these routes is client-called**, so unlike the previous block the
page-surface half is not in question here.

## FIRST: `FWD-9` -- **I GRADED IT ON THE WRONG INSTRUMENT AND THE GRADE IS WITHDRAWN**

I recorded `FWD-9` **NOT GRADEABLE** with the reason *"evidence limb PASSES; the MARKING limb is visual and
the export is markdown."* **That was measured on the export and the marking is served as DATA, one invoke
away, on a route the client already calls.**

`overlay.check_face` is an array of per-figure verdicts. **Denominator 17: 16 `PASS`, 1 `REFUSE`.** Each
carries a `marker`:

> `{"figure_id": "header:EQY_FUND_CRNCY", "value": "USD", "verdict": "REFUSE", "reason":`
> `"EQY_FUND_CRNCY: unit/sign convention is 'NOT-YET-BUILT', not MEASURED",`
> `"marker": {"verdict": "REFUSE", "colour_token": "red", "icon": "BLOCKED"}}`

**Colour tokens: 16 green, 1 red.** So a figure that failed its check carries a distinct verdict, a distinct
colour token and a distinct icon, beside its reason -- **the marking limb's DATA is present, correct, and
discriminating.** Whether the page paints the token is a page question and a different one.

**`FWD-9` is therefore NOT_REALIZED, not NOT GRADEABLE** -- its DONE WHEN is *APPLIED*, *"the marking is in
place and sits beside the evidence the sentence was drawn from"*, and the marking on PROSE is what
`held_no_span_count 21` withholds: the two served sentences sit beside their evidence, the twenty-one do not
exist on the page to be marked. **The figure marking is built; the prose marking reaches 2 of 23 sentences.**

**THE LESSON IS MINE AND IT IS THE SECOND TIME THIS PASS.** I banked *"the served plane is captured for
layout and for export, and not for what the page says"* as an instrument bound, and then let that bound stop
me from looking at the JSON routes, which say plenty. **A bound on one instrument is not a bound on the
question.** `FWD-1`'s content claim and `FWD-9`'s marking claim were both answerable off `overlay` and
`thesis` the whole time.

## `FWD-3` -- **NOT_REALIZED, and 27 figures are the reason**

Fence `:444-450`. ACCEPT: *"Someone asks where a figure came from, on what basis, and as of when."*

**MEASURED, and the first two-thirds are outstanding.** Every one of the **391** served figures carries its
mnemonic, its Bloomberg field description, its as-of stamp and its source (`bloomberg-dapi`) -- *where it
came from* and *as of when*, 391 times, on both the pdf and the rich export. **I have not seen a research
artifact anywhere in this estate carry provenance this densely.**

***"On what basis"* is where it fails, and the number is exact: 27 mnemonics carry NO unit/sign convention**
-- 26 reading `NOT-YET-BUILT` and one (`IS_DIV_PER_SHR`) reading `SIGN-UNRESOLVED`, which is the very figure
`FWD-10` passes on. **192 of 391 figure lines on the served pdf are affected.** A figure whose unit is
unresolved cannot be defended on its basis, and the list includes `NET_INCOME`, `GROSS_MARGIN`,
`RETURN_ON_CAP` and every `BEST_*` estimate. **DONE WHEN unmet** (*"a figure has actually been challenged and
answered from the page"*): no challenge is recorded.

## `FWD-4` -- **NOT_REALIZED. The feed serves ONE item, and the frequency ordering declares itself ABSENT**

Fence `:452-459`. `overlay.feed`: `coverage_status SERVED`, `item_count 1`, `store_item_count 2`.

The one item is real and clickable -- a WSJ article with its URL, title, `published_at 2026-09-03T09:30:00Z`,
`words 842` and a `body_sha256`. **And the ordering clause answers itself, honestly:**
`"order": "newest first by published_at (P-1's own order)"`, and
**`"most_discussed_basis": "ABSENT -- P-1 carries no discussion count, so no item is ordered by it"`.**

The fence asks for commentary *"ordered by how recent AND how often it came up"* and for three kinds --
*"news, analyst writing, and mentions from the company's own investor channel."* **One publisher, one item,
one of the three kinds, and half the ordering rule declared absent with its reason.** The surface is right
and nearly empty. This is a SUBSTANCE failure: the feed needs items, not code.

## `FWD-11` -- **NOT_REALIZED, and the absence is a BARE NULL, which is its own finding**

Fence `:508-517`. **`overlay.chatter` is `null`.** Not an absent-record; a bare `null`.

**AND THE CONTRAST IS ON THE SAME PAYLOAD, WHICH IS WHY IT IS A FINDING RATHER THAN A QUIBBLE.**
`description`, `feed` and `posture` each carry a `status`/`coverage_status` and a reason. **The two keys that
carry a bare `null` are `chatter` and `price`.** So a consumer reading this payload can tell WHY the
description or the feed is thin, and cannot tell whether `chatter` is absent because nothing was collected,
because the read failed, or because the field was never wired -- **the exact state
`docs/doctrine/A_VALUE_MUST_CARRY_ITS_CLAIM.md` exists to forbid, inside a product that carries its claim
everywhere else.** Two keys, one payload, and the fix is the estate's own `classify.absent()` helper that
five neighbouring fields already use.

The fence's substantive clause -- *"each item is there because it met a written rule the analyst can read"* --
cannot be graded at all while the feed is null: **there are no items to carry a rule.** Recorded as UNGRADED
within a NOT_REALIZED outcome rather than as a second finding.

## `FWD-13` -- **NOT_REALIZED on the DONE WHEN; the identity machinery is the most thorough thing in the product**

Fence `:529-539`. ACCEPT: *"The numbers, the recent commentary, the comparison list and the social posts on a
page are all about the same company. Where the page cannot confirm that two sources describe the same
company, it says so."*

**The confirm-or-say-so clause PASSES and is over-built in the right direction.** Every per-security reader
takes ONE resolved identity carried unchanged from the route boundary (`scoped_amgt.py:4024-4034`: *"ONE
resolution, carried unchanged into whichever reader serves the leaf: no reader below resolves again, and none
transforms it"*); `_print_pack` refuses outright when the landed display form does not resolve back to the
same key (`:4128-4136`); and `peers` returns an absent arm naming *"which absence it is"*.

**But the fence names FOUR surfaces and one of them is `null`.** *"The social posts on a page"* cannot be
confirmed as the same company when there are no social posts -- and, per `FWD-11`, the payload does not say
why. **The identity guarantee is real for the numbers, the commentary and the comparison list, and vacuous
for the fourth.** DONE WHEN separately unmet: *"EXERCISED -- checked on a name that more than one business
uses, and found not mixed."* No such name has been exercised on the served plane; `BA` is not that name.

## `FWD-15` -- **NOT_REALIZED on the DONE WHEN, and the PRICE axis substantively WORKS**

Fence `:551-562`. The fence is an **OR** -- *"names that are moving in price OR spiking in discussion"* -- so
one working axis satisfies the substantive clause. **Read both:**

| axis | `as_of_date` | `row_count` | scores |
|---|---|---|---|
| `trending/price` | **2026-09-24** | **10** | a real spread: `16.95, 16.75, 12.47, 8.17, 4.18, 3.09, 2.74, 2.59, 0.15, -0.33` |
| `trending/chatter` | **2026-09-25** | **2** | **both `0`** |

**`ranking_status SERVED`, `state COMPLETE`, `empty_reason null` on both**, and the route is client-called
(`amgt-lead-panel.ts:69`). **So the price axis delivers exactly what the fence describes: a short ranked list
with a real spread a PM could act on** -- `992 HK, PBR US, VLO US, BP/ LN, 9433 JP, 2317 TT, SSE LN, RWE GR,
ASML NA, BBSE3 BZ`.

**TWO DEFECTS THE GRADE TURNED UP, neither of which is the outcome failing:**

1. **The chatter axis is DEGENERATE and does not say so.** Two rows, both scoring `0`, `state COMPLETE`,
   `empty_reason null`. `BA US` is `rank 1` on a `raw_chatter_count` of **0**. **A ranked list whose top name
   scores zero is not a ranking, and `COMPLETE` with a null `empty_reason` asserts that it is.** That is the
   `FWD-11` null feed surfacing on a second route, and here it wears a success state.
2. **The two axes disagree on vintage by a day** -- price `2026-09-24`, chatter `2026-09-25`. A panel showing
   both shows two different days beside each other, and only the per-axis field says so.

**And a third thing worth a card rather than a fix:** none of the ten price-ranked tickers is obviously a
covered name. The fence says *"which COVERED names are worth looking at"*; these look like the holdings union.
**That is the 89/94/7/250 denominator question arriving on a fifth surface.**

## `FWD-16` -- **NOT_REALIZED. The description PASSES outright; the day's items are the `FWD-4`/`FWD-11` gap**

Fence `:564-573`. ACCEPT: above the tabs, *"a one-line description of the company AND the day's news and
social items about it, newest and most-discussed first, each one clickable."*

**The description clause PASSES, measured and clean:** `overlay.description` = `status SERVED`,
`source "bloomberg CIE_DES"`, `field "CIE_DES"`, **`generated: false`** -- so it is the company's own
description, not machine prose, and the payload says which. Text: *"The Boeing Company operates as an
aerospace company. The Company develops, manufactures, and services commercial airplanes, defense products,
and space systems. Boeing serves clients worldwide."*

**The rest of the fence is the same two gaps already graded:** the day's news is the one-item `feed`
(`FWD-4`), the day's social is `null` (`FWD-11`), and *"most-discussed first"* is the ordering the feed
declares ABSENT. **`FWD-16` therefore closes when `FWD-4` and `FWD-11` do, and needs nothing of its own.**

**AND ONE THING THE DESCRIPTION READ SETTLES that `FWD-1` left open.** `FWD-1` graded NOT_REALIZED partly
because the export's Company Description section is subheaded *"Filed detail (does not describe the
business)"*. **The business description EXISTS and is served** -- on `overlay.description`, from `CIE_DES`,
and the pdf carries it too. So `FWD-1`'s business-description limb is **a rendering-placement gap in the
export, not a missing datum**, while its segment-breakdown limb remains genuinely absent. **A correction to
the weight of that grade, not to its verdict.**

---

# 20 OF 20 GRADED -- THE PASS IS COMPLETE

**1 REALIZED, 18 NOT_REALIZED, 1 correction (`FWD-9`, from NOT GRADEABLE to NOT_REALIZED).**
No outcome is NOT GRADEABLE. The 30-outcome endpoint's first twenty now have a grade read against their own
PRD fence, and `FWD-21`..`FWD-30` were graded in rounds 38-41.

## The four classes, final

| class | outcomes | what closes it |
|---|---|---|
| **REALIZED** | `FWD-10` | -- |
| **WIRING** -- served, measured, nothing calls it | `FWD-6`, `FWD-7`, `FWD-12` | client calls plus a surface. `FWD-6` needs no backend work at all |
| **SUBSTANCE** -- the frame is right, the content is thin or absent | `FWD-1`, `FWD-3`, `FWD-4`, `FWD-5`, `FWD-8`, `FWD-9`, `FWD-11`, `FWD-13`, `FWD-15`, `FWD-16`, `FWD-17`, `FWD-18`, `FWD-19`, `FWD-20`, `FWD-30` | real work, but it CONCENTRATES -- see below |
| **RESERVED** -- a word only Andrew can give | `FWD-2`, `FWD-14` | nothing the fabric can cut |

## THE FIFTEEN SUBSTANCE FAILURES ARE NOT FIFTEEN PROBLEMS -- FOUR INPUTS CARRY ELEVEN OF THEM

This is the finding the pass exists to produce, and it is only visible now that all twenty are graded:

| one fix | closes or unblocks |
|---|---|
| **write character spans on the drafting object** (21 held sentences) | `FWD-18` (*biggest bets*), `FWD-9` (prose marking), `FWD-3` (defensibility of prose claims) |
| **build the 27 missing unit/sign conventions** | `FWD-3` (*on what basis*), `FWD-5` (the pdf's 192 unmarked lines), `FWD-20` (`BEST_ESTIMATE_FCF` is `D`'s subtrahend) |
| **land social items + give `chatter` an absent-record** | `FWD-11`, `FWD-13` (its fourth surface), `FWD-15` (the degenerate chatter axis), `FWD-16` (half its content) |
| **answer the universe question** | `FWD-17` (pool of 7), `FWD-19` (Deere outside the corpus), `FWD-15` (ranking the union, not coverage), `rp-1` |

**Four inputs reach eleven outcomes. The remaining four substance failures are genuinely separate work:**
the 2-page branded export (`FWD-5`), a business-similarity peer set (`FWD-8`), the house FCF forecast
(`FWD-20`'s minuend), and the export absence-marker fix already cut as round 42's `rq-1` (`FWD-30`).

**AND THE PRODUCT IS BETTER THAN 1-OF-20 SOUNDS, which the running count hid.** Measured this pass, on the
served plane: 391 figures each carrying source, basis and as-of; 17 figure verdicts with discriminating
colour tokens; twelve peer columns each declaring its absence against the 289-factor registry; a filing
chart chosen for Boeing with a passage id and a character span on every point; two thesis sentences whose
cited paragraphs contain them verbatim; ten versions of a model block with a 212/0/7/172 diff between two of
them; a served route declining a DNS sweep because it would be egress on a caller's behalf.
**The machinery is real and honest. It is starved of content and under-wired, and those are different
projects from the one the round count implies.**
