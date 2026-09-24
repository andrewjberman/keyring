# AMGT -- HAND-BACK TO CANONICAL FLOW + THE NEW ANALYSIS FOR ROUNDS

**Andrew-direct 2026-09-24 ~04:3xZ at the `1.0.0_SA_CTO~Z` terminal, VERBATIM:** *"I think we're positioned
here to get back to canonical flow. I want you to essentially clean up any residue laying about, and essentially
spec out a new analysis that can be handed off to new rounds for development on AMGT_CORPUS (Not only do we need
the incorporated layers from the corpus however we decided to do that i.e. using your dossier addendum we also
need backfill for all the asset management securities), AMGT_RESAPP (I don't really believe this is done but if it
really is and the only thing that's missing is data which can be handled in CORPUS, then I need you to get an
addendum for a fresh round by having 4.0.0_SA_CRO~Z do a comprehensive walk over the surfaces and spec out how to
completely upgrade the frontend to be in pattern and good design, because currently it is a nightmare zone of
walls of text and overlapping chaos, the brief they make will be the basis for the addendum). Then you can have
COO~X take CORPUS and COO~Z take RESAPP."*

**Seats, on his word:** `2.0.0_SA_COO~X` -> **AMGT_CORPUS** · `2.0.0_SA_COO~Z` -> **AMGT_RESAPP**.

---

## 1. THE PRECONDITION -- AND THE DEFECT IN THIS SEAT'S OWN EARLIER ACT, FOUND WHILE CLEARING IT

`/canonical-drive` **skips a project whose row carries `closer_contract`** -- no recut, no issuance, no nudge -- so
the field comes off **`AMGT_CORPUS` and `AMGT_RESAPP`** at hand-back (`/closer`'s own rule: *"At hand-back the CTO
removes the field"*), and **STAYS on `AMGT_HARVST`**, whose H03 2a is mid-apply with the AE mandate issued, the
ledger `amgt-h03-leadpanel-y-20260924` OPEN and the never-widen pair closed against one patch hash.

⛔ **BUT THE FIELD WAS ON THE WRONG CARRIER, AND IT WAS THIS SEAT THAT PUT IT THERE @`7b26e2ac1c`.** Measured
here before removing it:
- **It has NO MECHANICAL CONSUMER.** `closer_contract` census: **49 hits across 72,197 files**, bands
  `SURFACED=4` (all three of them my own comp-rail log lines), `CONFIG=5` (five `project.json` rows), `DOC=40`
  (skills and the spine). **NOT ONE `.py` or `.sh` reads it.** So the skip is a READING rule in
  `/canonical-drive`'s and `/canonical-flow`'s prose, not a gate -- the same law-stronger-than-tool shape this
  seat has been ruling on all night, and §1 of this file asserted it as mechanical until this measurement.
- ⛔ **I WROTE IT TO THE GENERATED INDEX ROW (`org/projects/*.json`), NOT THE DECLARED TREE ROW.**
  `org/standards/PROJECT_TREE.contract.json:121` -- *"an index entry carrying `home` is GENERATED from the tree row
  at `home`/project.json and is never hand-edited"* -- and `closer_contract` is not among the eleven
  `index.fields` (`:100-110`) at all.
- ⛔ **AND THE GENERATOR ERASES IT ON THE FIRST WRITE.** `.tools/missions-tree-index.py:356` is a FULL OVERWRITE
  with `compose_index(t)`, built from the tree row; `:352-354` skip that write only while all six
  `compared_fields` match -- `directive, macro_code, fabric, **dep_stage**, **status**, name`. **So the field
  survived only because nothing had moved yet, and `dep_stage`/`status` are exactly what a closer changes.** The
  skip I believed I had installed on HARVST was one `derive --write` from vanishing, silently.
- ⭐ **THE DISCRIMINATOR IS A CLEAN INVERTED PAIR, AND IT SETTLES WHICH FILE IS RIGHT.** `IRPT_BCKEND` /
  `IRPT_FNTEND` -- the precedent that created this field -- carry it in the **tree** row
  (`org/missions/D9/IRPT/*/project.json:41,43`) and **ABSENT** from their generated rows. AMGT carried it in the
  **generated** row and **ABSENT** from the tree. Exactly inverted; mine is the outlier.
- ⚠ **`missions-tree-index.py check` reads `RESULT: 0 violation(s)` BOTH BEFORE AND AFTER**, over 25 tree
  projects and 374 index rows. **Nothing was ever going to tell me** -- an extra key in a generated row is not
  INDEX-DRIFT, which only grades the six compared fields.

**DONE IN THIS COMMIT:** `closer_contract` **off all three generated rows** and **onto the `AMGT_HARVST` TREE
row**, appended exactly as `IRPT_BCKEND` does. ⭐ Side effect worth naming: the three generated rows are now
byte-canonical to what the generator writes (`indent=1, ensure_ascii=True`), where my earlier hand-edit had
reformatted them to `indent=2` -- **so the next `derive --write` is a no-op instead of a diff.** The tree row keeps
its hand-authored `indent=2`, so its diff is **3 insertions / 2 deletions** rather than 139 lines of churn.

⭐ **AND THE CLOSER WORK IN FLIGHT COMPLETES UNDER ITS OWN SPEC** -- Rule 27's scope clause, verbatim: *"Work in
flight at arm time completes under its own spec."* The Peers consumer-2 grading, failure case 3, the 2a apply and
the DE_US_Equity fork finish as closer items; they do NOT become round cells. **The rounds carry ENRICHMENT, not
the thread.**

## 2. WHAT IS ACTUALLY DONE, SO THE ROUNDS ARE NOT SPECCED AGAINST A FICTION

⚠ **HIS INSTINCT IS RIGHT: RESAPP IS NOT DONE, AND THE GAP IS NOT ONLY DATA.** Measured tonight:

| | state |
|---|---|
| `E0` live thread | ✅ **REACHED** 03:12Z, served stack, no `/market` redirect -- the first live journey in the record |
| Peers route/data | ✅ **PASS** on deployed bytes against an independent baseline |
| Peers **render** | ⛔ counts line still reads **"1 column(s) carry"** -- the 5-column render needs the portal deploy of `1ec5446c` |
| Peers **consumer 2** | ⛔ **UNGRADED** -- every case is HALF-GRADED by the mandate's own rule |
| Peers failure cases | ⛔ **0 of 3 exercised**; case 3 (`BP/_LN_Equity`) OPEN and localised to the URL path + a decode |
| Lead Panel live thread | ⛔ **NOT REACHED** |
| Lead Panel chatter water | ⛔ `names_with_links` **3 of 250**; gold resolves **0 of 191** -- NEITHER source has the data |
| Lead Panel price | ⛔ generations **2026-09-15**, served only by a fallback **EXPIRING 2026-09-29** |
| Lead Panel `dated` on screen | ⛔ absent from `RankingSet` -- a nine-day-old list under a fresh timestamp |
| `H1`-`H4`, `C1`-`C3`, `L1`-`L4`, `W1`, `F1` | ⛔ **NOT_EVALUATED** |

⭐ **SO THE ANSWER TO HIS CONDITIONAL IS: NO, DATA IS NOT THE ONLY THING MISSING.** Render, second-consumer
grading, failure cases, the `dated` carry and the price producer are all real and none is a CORPUS item. **The
frontend walk he commissioned is therefore necessary but NOT sufficient**, and the RESAPP round must carry the
non-data items too or it will close on a false completion.

## 3. AMGT_CORPUS -- the analysis for its round (`2.0.0_SA_COO~X`)

**TWO OUTCOMES, and he named both.**

**(a) THE INCORPORATED LAYERS -- the dossier fold.** Basis: `4.0.0_SA_CRO~Y`'s L1 brief
`docs/briefs/amgt-corpus-dossier-fold-brief-20260924.md` (`be09d62ef7`, Part VIII @`5ef3e9a89b`), **cut at the
AMENDED hash** once `O7`/Part IV-F2 land the PDF-extractability correction. Measured inputs:
- **93 company folders** -- 46 docx+pdf, 30 pdf-only prose, 6 docx-only, 10 workbook-only, **1 empty**
- ⭐ **`O7` IS SMALL: the absence was in the READER, not the corpus.** 26 of 30 PDF-only folders carry a full
  research pack; **29 of 30 carry pillars or "Why we own"**; positive control recovered **99 of 99 docx pillars
  from the PDF**. The fix is `extract.py`'s inline-lead rule + the PFOE name set + `continuation.py`'s PDF branch
  **with the docx branch KEPT AS THE CONTROL**.
- Dossier gains `thesis_summary`, `company_description`, `growth_algorithm`, `ownership`, `special_items`,
  `why_we_own`, `positives`/`negatives` -- **each CITED or explicitly ABSENT.**
- ⚠ **Andrew's fold constraint (R-18) binds:** *"i wouldnt change AMGT_RESAPP page layout architecturally"*, and
  *"Peers I think largely stays as it is"*. The dossier is **one channel among equals**, not the page's shape.

**(b) BACKFILL FOR ALL ASSET MANAGEMENT SECURITIES -- new, and the bigger half.**
⛔ **THE CURRENT BLOCKER IS IDENTITY RESOLUTION, NOT ACQUISITION, AND IT IS MEASURED:** `ingest_run.json` shows
**33 folders resolved / 123 files stored** and **60 folders / 228 files NOT ingested BECAUSE IDENTITY RESOLUTION
FAILED.** ⭐ **So "backfill everything" is 60 of 93 folders blocked on the SAME identity class the Peers hop-4
work just fixed one layer of** -- the crosswalk now registers 194 keys against 36, and the 60-name induction is
already authorized under **R-16 V2** (one `reference_data` call each, once, through `add_security`).
⛔ **AND R-21's MECHANISM CONSTRAINT BINDS THE INDUCTION: scripted and deterministic, never an agent turn.**
⚠ **V2 authorizes the CALLS, NOT A PICK** -- `3.0.0_SA_CVO~Z`'s standing ruling on ambiguous names
(`AXMB`/`AMXB`) is untouched, so an ambiguous name is a REFUSAL with a reason, never a guess.
**The round's shape:** run the scripted induction -> re-resolve the 60 -> re-ingest -> **print both denominators
(folders resolved of 93, files stored of 351)** at every step.

## 4. AMGT_RESAPP -- the analysis for its round (`2.0.0_SA_COO~Z`)

**COMMISSIONED AND IN FLIGHT:** `4.0.0_SA_CRO~Z`'s comprehensive surface walk + spec (sent 04:2xZ). **His words
are the standard: "a nightmare zone of walls of text and overlapping chaos" -> "in pattern and good design."**
The brief is the addendum's basis; the ratified contract is `DESIGN.md` C1-C12 and a rejection **cites the clause
number**. ⚠ **Flagged to that seat as a fork rather than resolved here: his 02:47Z "wouldnt change the layout
architecturally" against this word -- the narrow reading (conformance within the existing tabs) is what this seat
is acting on, and if the walk concludes the architecture must change, that goes back to him.**

**THE ROUND ALSO CARRIES THE NON-DATA ITEMS FROM §2, which the frontend brief will not cover:** the `1ec5446c`
portal deploy for the 5-column render · consumer-2 exercise · the three failure cases · `dated`/`requested_as_of`
into `RankingSet` (⭐ **client-side only -- the route ALREADY SERVES both fields; R-17**) · the overlay's
point-read fallback so the **list and the overlay AGREE about the same name** · `ABSENT beside EMPTY`.

## 5. RESIDUE -- censused, and split by who may clear it

| class | measured | owner |
|---|---|---|
| shared tree | **9 modified**, **28 untracked** top-level | mixed; Class C of the earlier ledger, **six lanes** -> integrator |
| `.runtmp_*` / `.scratch` | **0** -- the earlier sweep held, no regrowth | -- |
| **worktrees** | **43**, **0 prunable** (all present on disk) | ⛔ **NOT this seat's** -- each is a live seat's workspace; MSTR's own drain note refused to remove one for exactly this reason |
| **local branches** | **67** -- 54 `wk-*`, 5 `closer/*` | the owning seat, then MSTR |
| origin | **1** (`CLOUD`) -- ONE TRUNK complete, `SITEZ` archived at `archive/SITEZ-20260924` | -- |

⭐ **THE USEFUL CUT IS MEASURED, NOT GUESSED -- containment in `CLOUD`, never age or naming.** Census complete:

**67 local branches = `CLOUD` itself + 53 FULLY MERGED into it (nothing unique lost -- the safe-to-delete set) +
13 carrying unique commits.** ⚠ **`git branch --merged CLOUD` reads 54 because IT COUNTS `CLOUD`** -- 54 + 13 = 67
and the deletable set is 53. Both numbers are right under different definitions, so the definition is printed.
The 13 are the only branches that could lose work:

| branch | age | reading |
|---|---|---|
| `closer/amgt-peers-z-20260924` | 27 min | **LIVE closer work** |
| `closer-amgt-corpus-x-20260923` | 43 min | **LIVE**, and 1.8 G of worktree |
| `closer/amgt-h-y-20260923` | 86 min | **LIVE** -- the 2a lane |
| `closer/amgt-r-20260923` | 3 h | 1.7 G of worktree |
| `closer/amgt-experience-z-20260923` | 6 h | |
| `cvo-z-harvst-l4r` | 9 h | |
| `wk-amgt-13-{26,27,28,29,29-sp,30}`, `wk-amgt-14-50` | **5-7 days** | the only genuinely cold set, **7 branches** |

⛔ **THIS SEAT DELETES NEITHER A WORKTREE NOR A BRANCH IT DOES NOT OWN -- INCLUDING THE 53 "SAFE" ONES.** A
worktree is a live seat's workspace, MSTR's own drain note refused to remove one for exactly that reason, and
**merged-into-`CLOUD` does not mean idle** -- three of the thirteen unmerged were written to in the last 90
minutes. ⚠ **And a branch census cannot see whether a worker was ever spawned**: a zero-commit `wk-*` branch reads
identically live or abandoned, so even the 7 cold ones go to their owning seat, not to a sweep. The set is handed
to `0.0.0_AB_MSTR~Z` as an integrator decision with this denominator printed; **the earlier sweep's lesson stands
-- `.tools/ps-lock/` looked like a lock and held two working scripts.**

## 6. WHAT THIS SEAT DOES NEXT, IN ORDER

1. Re-point `AMGT_CORPUS` + `AMGT_RESAPP` for rounds and **remove `closer_contract` from those two only** (§1).
2. Relay the seat assignments to `~X` and `~Z` with §3/§4 as their analysis basis.
3. Cut the **CORPUS L4 addendum** at the amended dossier-brief hash; cut the **RESAPP L4 addendum** when
   `4.0.0_SA_CRO~Z`'s walk lands.
4. Route the residue ledger to `0.0.0_AB_MSTR~Z` with the merged/unmerged branch split printed.

**AT ANDREW, unchanged and none of it blocking a round:** the **notification decision** ·
**`0.0.3_BG_BBGTerminal`** needs bringing up (**price fallback expires 2026-09-29**) · **`2b`**, the gold-table
population, without which Trending x Chatter shows nothing from any source.
