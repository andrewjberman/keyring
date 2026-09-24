# THE 49-OUTCOME GRADE TABLE -- AMGT CLOSE, SKELETON

`1.0.0_SA_CTO~Z`. Built per **R-39 (2)** (the grade table is the closing analysis's first section, never a
PRD edit while the spec is frozen) and **R-39a** (the closing analysis NAMES ITS CARRIER PATH per project
rather than globbing for it). This file is EXTRACTION ONLY -- no outcome is graded here, so nothing in it
goes stale when a round lands. The closing analysis fills the GRADE column.

## THE CONTROLLED VOCABULARY -- R-39 (2), and it is the whole mechanism

One token per row from `{REALIZED, NOT_REALIZED, DEFERRED, HELD}`. **UNDERSCORED, NEVER SPACED.**
`NOT REALIZED` with a space contains `REALIZED` and inverts under a word-boundary match -- measured, 19 of
171 grade mentions across 604 AMGT files are in that form. `UNGRADED` is the starting value and is NOT a
close-eligible token: every row reaches one of the four or the close does not close.

## CARRIER PATHS -- the two projects differ, which is why a glob cannot find them (R-39a)

| project | L10 analysis carrier | count today |
|---|---|---|
| `AMGT_RESAPP` | `org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round<N>.md` | 36 |
| `AMGT_CORPUS` | `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_CORPUS_ROUND<N>_ANALYSIS_<date>.md` | 1 |

A round's analysis grades only the outcomes THAT ROUND TOUCHED -- round 36 names ONE id of 30 -- so the
table is filled by GRADING at the close, not by harvesting the analyses. That was measured and is why
R-39 (2) puts the table in the closing analysis rather than treating it as a lookup.

## AMGT_RESAPP v0.26 -- 30 outcomes

| id | outcome | grade | evidence coordinate |
|---|---|---|---|
| `FWD-1` | An analyst gets a first-draft pack for a covered name without opening | UNGRADED | |
| `FWD-2` | An analyst gets the same pack for a company the firm has never covered, | UNGRADED | |
| `FWD-3` | An analyst can defend every number on the page in a meeting | UNGRADED | |
| `FWD-4` | An analyst reads what has recently been said about the company without | UNGRADED | |
| `FWD-5` | Adam forwards a printed pack without reformatting it | UNGRADED | |
| `FWD-6` | An analyst returning to a company can say what changed | UNGRADED | |
| `FWD-7` | Adam can see which covered companies have gone stale | UNGRADED | |
| `FWD-8` | The comparison block is about the company on the page | UNGRADED | |
| `FWD-9` | Machine-written prose is never mistaken for a firm view | UNGRADED | |
| `FWD-10` | A figure that failed its check is visible as failed | UNGRADED | |
| `FWD-11` | An analyst sees social discussion admitted by a written rule | UNGRADED | |
| `FWD-12` | An analyst can see where each input came from and re-run any one alone | UNGRADED | |
| `FWD-13` | Everything on one page is about the same company | UNGRADED | |
| `FWD-14` | were added at L2 and accepted without reservation by `4.0.0_SA_CRO~Z` (msg 21001) as its | UNGRADED | |
| `FWD-15` | A PM can see which covered names are worth looking at right now, | UNGRADED | |
| `FWD-16` | The top of the page tells an analyst what the company is and what | UNGRADED | |
| `FWD-17` | An analyst sees who runs the company, and how long they have run it | UNGRADED | |
| `FWD-18` | The company's own filings are read for the analyst, and the one | UNGRADED | |
| `FWD-19` | An analyst sees what this company means for Opal | UNGRADED | |
| `FWD-20` | takes the next unused number. | UNGRADED | |
| `FWD-21` | A PM opens BA_US_Equity and reads the Thesis ON ONE SCREEN under ONE | UNGRADED | |
| `FWD-22` | The name's headline figures read as LABELLED TILES, not a mnemonic list | UNGRADED | |
| `FWD-23` | Every drafted sentence keeps its evidence, folded until asked for | UNGRADED | |
| `FWD-24` | The Model sheet reads as a table and a refusal as ONE line per row | UNGRADED | |
| `FWD-25` | The comparable set shows the columns that EXIST, and the absent ones | UNGRADED | |
| `FWD-26` | The Posture verdict reads as a headline and its reasons as cards | UNGRADED | |
| `FWD-27` | The Lead Panel's controls read as the Dashboard's controls do | UNGRADED | |
| `FWD-28` | Every panel renders one of the four DESIGNED states when empty | UNGRADED | |
| `FWD-29` | The contract's render check PASSES, and CAN FAIL | UNGRADED | |
| `FWD-30` | A PM exports the name they are reading and gets a usable artifact | UNGRADED | |

## AMGT_CORPUS v0.6 -- 19 outcomes

| id | outcome | grade | evidence coordinate |
|---|---|---|---|
| `FWD-1` | Every report the team has written can be re-opened from our store | UNGRADED | |
| `FWD-2` | Every stored report says which security and which period it belongs to, | UNGRADED | |
| `FWD-3` | The backlog universe IS the library's folder list, resolved to | UNGRADED | |
| `FWD-4` | A backlog name the universe does not yet carry can be INDUCTED BY ONE | UNGRADED | |
| `FWD-5` | For a name the team has written up, its OWN thesis pillars, KPI set, | UNGRADED | |
| `FWD-6` | For a business type, the team's own report shape is readable as one | UNGRADED | |
| `FWD-7` | The generic model shape the team uses for EVERY sector is readable as | UNGRADED | |
| `FWD-8` | A consumer can fetch, for one security, every corpus artifact it needs | UNGRADED | |
| `FWD-9` | Nothing this project runs can write to, move or delete anything in the | UNGRADED | |
| `FWD-10` | An analyst opens a covered name and reads the TEAM'S OWN | UNGRADED | |
| `FWD-11` | The pack's MANAGEMENT / BOARD passage appears on Exec Management as the | UNGRADED | |
| `FWD-12` | The Model tab's rows are the typecast's mnemonic core plus the sector | UNGRADED | |
| `FWD-13` | Every folded field is CITED or ABSENT with a readable reason | UNGRADED | |
| `FWD-14` | Any folder in the Research list returns its dossier or the printed | UNGRADED | |
| `FWD-15` | The fund of record and last stated position read as the TEAM'S stated | UNGRADED | |
| `FWD-16` | A PDF-only pack gets the same fold, or the tab states which shape the | UNGRADED | |
| `FWD-17` | A newly filed report becomes a new immutable bronze object and the | UNGRADED | |
| `FWD-18` | Each pillar and KPI row names its terms, and the header feed and Chatter | UNGRADED | |
| `FWD-19` | EVERY SECURITY IN THE ASSET MANAGEMENT RESEARCH FOLDER -- all 93 -- is | UNGRADED | |

## THE ARITHMETIC -- it must close or the close is not a close

**30 + 19 = 49.** Denominator verified on a second
instrument: distinct contiguous ids read from the PRD bodies, not a self-declared `endpoint_outcomes`
header. The closing analysis prints `N of 49 REALIZED`, names every non-REALIZED row with its reason, and
the two sum to 49.

## THE FOUR KNOWN EXCEPTIONS -- `AMGT_CLOSE_CONDITION_20260924.md` @`1ccf401cfd`

| id | token | reason |
|---|---|---|
| `rk-49` (Lusha) | HELD | an external vendor API needs Andrew's explicit per-use word; no measurement moves it |
| CORPUS `FWD-18` | DEFERRED | marked PROPOSAL and later enrichment by its own author |
| CORPUS `FWD-12` figures | NOT_REALIZED | the 22 added Bloomberg mnemonics are R-16's excluded V3; labels and row order realize, figures read ABSENT-with-reason, which is `FWD-13` working |
| RESAPP `FWD-30` branch (a) | UNGRADED | may need a field no route serves; branch (b) may satisfy the outcome alone |

This list is NOT a licence to grow. A stop-condition satisfiable by shrinking its own denominator is not a
stop-condition, and this seat is the party that would benefit.

## ORDER COVERAGE OF THE 49 -- MEASURED BY SUBTRACTION, 2026-09-24 ~10:0xZ

⛔ **COVERAGE IS NOT REALIZATION. An order NAMING an outcome is not the outcome being MET.** This section
answers only *"does every declared outcome have a cell that was cut for it"*, which is the question the
enrichment-list subtraction needs. The GRADE column above stays UNGRADED regardless.

Instrument: every `FWD-<n>` id named in any task-order file, subtracted from the printed denominator.

| project | denominator | orders scanned | outcomes named by >=1 order | **named by NO order** |
|---|---|---|---|---|
| `AMGT_RESAPP` | 30 | 201 | **30** | **0** |
| `AMGT_CORPUS` | 19 | 17 | **18** | **1 -- `FWD-18`** |

⭐⭐ **THE ONE UNCOVERED OUTCOME IS EXACTLY THE DEFERRED EXCEPTION THIS DOCUMENT ALREADY NAMED.** CORPUS
`FWD-18` is the row marked DEFERRED above -- *"marked PROPOSAL and later enrichment by its own author"*. **So
the subtraction independently re-derived a known exception and found NOTHING NEW**, which is a positive control
on the instrument rather than a lucky agreement. The other three exceptions all HAVE orders: they are blocked
on CONTENT, not on coverage.

⚠ **AND THE CENSUS RETURNED AN IMPOSSIBLE COUNT FIRST -- "31 named of 30" -- WHICH IS WHAT SENT A READER TO
THE BYTES.** The extra id is `FWD-99`, in `TO-AMGT-rh-1` (`complete`), and reading it shows *"FWD-99 control
fires"*: **a deliberately nonexistent id used as a NEGATIVE CONTROL to prove the coverage checker detects an
unknown outcome.** ⭐ **So an out-of-range id in an order census is a SENTINEL until read -- calling it a defect
unread would have convicted good practice.** COST: one read. NON-APPLICATION: a census whose corpus carries no
control sentinels.

### THE SEVEN OUTCOMES IN FLIGHT, AND THEY ARE THE GOAL'S OWN LIMBS

Outcomes carrying a NON-TERMINAL order: `AMGT_RESAPP` **17, 27, 28, 29, 30** · `AMGT_CORPUS` **14, 19**.
Four non-terminal orders carry them, fabric-wide:

| order | outcomes | Andrew's limb |
|---|---|---|
| `TO-AMGT-rl-10.the-export` | `FWD-30` | **limb 2** -- the export, brand-guideline form, 2pg or machine-readable |
| `TO-AMGT-rl-9.designed-states` | `FWD-27/28/29` | **limb 1** -- the visually polished surface |
| `TO-CRPS-d-4.coverage-census-93-of-93` | CORPUS `FWD-19`, `FWD-14` | **limb 4** -- every single security, all 93 |
| `TO-AMGT-rk-49.lusha-domain` | `FWD-17` | HELD on Andrew's key-rotation fact |

⭐⭐⭐ **SO EVERY BUILDABLE LIMB OF THE GOAL IS CARRIED BY AN ACTIVE WORKER ORDER, AND THE DECLARED ENDPOINT IS
FULLY COVERED EXCEPT ONE DELIBERATELY-DEFERRED PROPOSAL.** What stands between this state and the close is:
those four orders reaching terminal; the L10 analyses this seat owes once they drain; whatever round 38's
enrichment list produces by subtraction; and **two facts from Andrew**. ⛔ **That is a statement about WORK
REMAINING, never about outcomes realized** -- all 49 grades are still UNGRADED and only the closing analysis
moves them.

## ANDREW'S COMPLETION TEST, MAPPED ONTO DECLARED OUTCOMES

His sentence -- *"only when all of this is done for every single security in the Asset Management research
folder is the goal complete"* -- is already a DECLARED OUTCOME and not a separate test: CORPUS `FWD-19`
reads *"EVERY SECURITY IN THE ASSET MANAGEMENT RESEARCH FOLDER -- all 93"*. The other three limbs map to
RESAPP `FWD-21..29` (the polished Security Analysis surface), RESAPP `FWD-30` (the export in Opal Brand
Guidelines form, 2pg or machine-readable), and CORPUS `FWD-10..19` (the dossier fold plus the backfill).
So closing the 49 IS closing his goal, and no fifth artifact is owed.
