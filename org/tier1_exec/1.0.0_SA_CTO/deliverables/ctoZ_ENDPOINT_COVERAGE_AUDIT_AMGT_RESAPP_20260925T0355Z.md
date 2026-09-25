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
