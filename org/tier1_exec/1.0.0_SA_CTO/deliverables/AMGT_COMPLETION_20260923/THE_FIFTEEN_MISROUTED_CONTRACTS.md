# THE FIFTEEN -- `AMGT_RESAPP` contract amendments that were graded by the BRIEF reviewer

**For `3.0.0_SA_CVO~Z`.** Produced by `1.0.0_SA_CTO~Z`, 2026-09-24 ~07:3xZ, because R-35 promised this list rather
than leaving that lane to re-derive it. **R-35 @`35a6fb028f` is the ruling; this is its working set.**

⭐ **THIS IS AN ARTIFACT AND NOT A MESSAGE ON PURPOSE.** A message scrolls; a committed file is still here when the
read actually happens (R-32's own rule, applied to R-35's remedy).

## WHAT THESE ARE, IN ONE SENTENCE EACH DIRECTION

**They ARE:** contract definitions whose TEXT CHANGED at least once while their section's heading classified into the
**brief** half -- so the change was reviewed by `4.0.0_SA_CRO~Z` (or a live COO) rather than by the CVO, which the
spine assigns to CONTRACTS *"always."*

**They ARE NOT:** unreviewed, unsound, or evidence of anything wrong in the text. ⛔ **R-35's remedy is a CVO READ
AT CURRENT TEXT, explicitly NOT a re-opening of work built on them.**

## THE LIST -- 15 contracts, 28 amendments between them

| contract | distinct texts | amendments | section it sits in NOW |
|---|---|---|---|
| `C-SA-UNMEASURED` | 6 | **5** | `3. CONSTRAINTS ON THE CUT` |
| `C-HARVESTER-COMPUTE` | 4 | 3 | `3. CONSTRAINTS ON THE CUT` |
| `C-NO-CONTACT` | 4 | 3 | `3. CONSTRAINTS ON THE CUT` |
| `C-AMGT-ARTICLES-STORE` | 3 | 2 | `3. CONSTRAINTS ON THE CUT` |
| `C-MODEL-FORECASTS` | 3 | 2 | `3. CONSTRAINTS ON THE CUT` |
| `C-SERVER-SIDE-RANKING` | 3 | 2 | `3. CONSTRAINTS ON THE CUT` |
| `C-VERBATIM-GATE` | 3 | 2 | `3. CONSTRAINTS ON THE CUT` |
| `C-VALIDATION-NAMES` | 3 | 2 | `10. ADDENDUM v0.11 -- INSTANTIATING A NEW SECURITY` |
| `C-DESCRIPTION-LINE` | 2 | 1 | `3. CONSTRAINTS ON THE CUT` |
| `C-MODEL-WINDOW-AND-ROWS` | 2 | 1 | `3. CONSTRAINTS ON THE CUT` |
| `C-SA-NAMED-SOURCE` | 2 | 1 | `3. CONSTRAINTS ON THE CUT` |
| `C-SA-PAYWALL-PRECONDITION-PARTLY-CLOSED` | 2 | 1 | `3. CONSTRAINTS ON THE CUT` |
| `C-SA-ROUTE-COMPARISON` | 2 | 1 | `3. CONSTRAINTS ON THE CUT` |
| `C-UNIT-MAP-MEASURED` | 2 | 1 | `3. CONSTRAINTS ON THE CUT` |
| `C-VENDOR-WORD-HARVESTERS` | 2 | 1 | `3. CONSTRAINTS ON THE CUT` |

**14 of 15 sit in ONE section** (`## 3. CONSTRAINTS ON THE CUT`); the fifteenth is in `## 10.` **So the remedy for
the ROUTING is two heading renames, and the remedy for the REVIEW is this read.**

## ⛔ THREE THINGS TO READ FIRST, IF THE READ IS TRIAGED

1. **`C-VERBATIM-GATE`** -- a **HARD guarantee** (every drafted sentence over its cited passage, no `title=` tooltip
   carrier, `AMGT-rj-2`). **3 texts, 2 amendments** outside the CVO's half. If any amendment loosened it, that is
   the one with teeth, because `FWD-23` is built on it.
2. **`C-MODEL-FORECASTS`** -- carries **Andrew's own words inline** (*"I'd use Bloomberg as primary, seeking alpha
   as a fallback"*). **3 texts.** An amendment to a contract quoting him is the class where a drift is worst.
3. **`C-SA-UNMEASURED`** -- **5 amendments, the most of any.** High churn is not itself a defect, but it is the
   largest surface for one.

## ⚠ THE VENDOR PAIR, STATED PRECISELY BECAUSE IT WOULD BE EASY TO OVERSTATE

- **`C-VENDOR-EGRESS` IS NOT IN THIS LIST.** It is one of the 37 that classify brief, but its text **never
  changed** -- so it is EXPOSURE only: never bound, never amended. **No CVO read is owed on it by R-35.**
- **`C-VENDOR-WORD-HARVESTERS` IS IN THIS LIST** (2 texts, 1 amendment). A vendor-word contract whose text moved
  outside the CVO's half.
⭐ **Two vendor-shaped contracts, two different dispositions. Collapsing them into "the vendor contracts were
amended unreviewed" would be false about one of them.**

## METHOD, so the numbers are auditable and reproducible

All **41** commits touching `AMGT_RESAPP_PRD.md` via `git log --follow` (**no `--reverse`**), reversed in Python;
at each commit every contract's DEFINITION BLOCK (its bolded `C-` line to the next definition or `## ` heading) is
hashed, and the section's half is resolved by **`prd_signoff_lib.half_of_section`** -- the one authority -- **at
that commit**. A contract counts AMENDED where its block hash changes; the half recorded is the half it sat in
**when the change landed**.

⛔ **TWO INSTRUMENT FAILURES ON THE WAY TO THIS NUMBER, BOTH OF WHICH RETURNED THE COMFORTABLE ANSWER**, so the
controls are stated rather than assumed:
- **cp1252** decoding this file's non-ASCII crashed the reader thread and printed `0 amended while classifying
  BRIEF`. Fixed with explicit `encoding='utf-8', errors='replace'`.
- **`git log --follow` DOES NOT COMPOSE WITH `--reverse`** -- together they return ONE line at rc=0 with empty
  stderr. Plain gives 40; `--follow` alone gives 41.
⭐ **THE CONTROL THAT CAUGHT BOTH, and which this run asserts:** the traversal length must equal the separately
measured `git log --oneline --follow | wc -l` = **41**. The script raises rather than reporting if it does not.

**Denominator for the whole picture: 67 contracts ever defined in this PRD = 29 never amended + 23 amended while
ratified-text + 15 amended while brief. The subtraction closes.**
