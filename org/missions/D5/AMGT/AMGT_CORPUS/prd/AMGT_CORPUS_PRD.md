# AMGT_CORPUS -- PRD (L4)

```json
{
  "project": "AMGT_CORPUS",
  "directive": "D5",
  "fabric": "site-z",
  "prd_version": "v0.6",
  "step": 4,
  "brief_ref": "docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md@6c52138c2f",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8",
    "FWD-9",
    "FWD-10",
    "FWD-11",
    "FWD-12",
    "FWD-13",
    "FWD-14",
    "FWD-15",
    "FWD-16",
    "FWD-17",
    "FWD-18",
    "FWD-19"
  ],
  "status": "RATIFIED"
}
```

**author** `1.0.0_SA_CTO~Z` (L2 endpoint and L4 PRD). **driver** `2.0.0_SA_COO~X` -- the third Tier-2 COO lane on
this box, seated by `0.0.0_AB_MSTR~Z` at the L4->L5 handoff on 2026-09-23 ~01:5xZ, within Andrew's 3-lane cap.

| | |
|---|---|
| **Directive** | D5 Asset Management (placement SITEZ) |
| **Macro** | `AMGT` |
| **L1 brief** | `4.0.0_SA_CRO~F`, `docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md` @`42c05cd8a8`. **SHARED with the `AMGT_RESAPP` addendum and deliberately not copied into this tree** -- one brief, two consumers; a copy would age separately from its original |
| **Andrew's words** | the split and the name: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_182xZ_AMGT_CORPUS_SPLIT_BLOOMBERG_TO_CLAUDE_ALLOWED_LEAD_PANEL_DETERMINISTIC.md`; the population: `..._183xZ_RESEARCH_FOLDERS_ARE_THE_BACKFILL_BASIS_AND_INITIAL_POOL.md`; the design and the memo, verbatim at `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260922_17xxZ_CLAUDE_ANALYSIS_LAYER_PLATINUM_DESIGN.md` and `ANDREW_VOICE_MEMO_20260922_HARVEST_INFRA_OVERVIEW_TRANSCRIPT.md` |
| **Siblings** | `AMGT_RESAPP` (the page, the analysis producer, the report object, the export -- consumes this project's artifacts); `AMGT_HARVST` (the publication channels -- neither consumes nor is consumed by this project) |
| **L3** | registered @`7cedd1fd9d` |

### v0.2 CHANGE NOTE -- 2026-09-22 ~20:2xZ, `1.0.0_SA_CTO~Z`

v0.1 was REFUSED on the ratified-text half by `3.0.0_SA_CVO~Z` (@`f00abf5e5303`), two bounded items. Both are fixed
here; the design was not disputed and is unchanged.

- **R1, the brief pin did not resolve.** v0.1 pinned `@42c05cd8a8`, which is a DRAIN of a different CRO branch --
  `git cat-file -e` returns rc=128 there, so a reviewer following this PRD's own pointer got an error instead of the
  text that every one of the nine `SOURCE` lines cites. Re-pinned, **and NOT to the commit the refusal proposed.**
  ⚠ The CVO recommended `578f7072d1` (the ADD commit, 35,894 bytes); the brief has **two** commits, and its current
  bytes are `6c52138c2f` (**36,007 bytes**, +113). **The delta is exactly the origin line that names Andrew's eighth
  message -- the one that makes the Research library the backlog -- which is the authority FWD-3 and FWD-4 rest on.**
  Pinning to the ADD commit would have pinned this endpoint to a brief that does not carry the word two of its
  outcomes are built from. Measured on this seat's own instrument with a positive and a negative control
  (`578f7072d1` rc=0 / 35,894; `42c05cd8a8` rc=128; `HEAD` 36,007; working tree clean, so 36,007 IS what this seat
  read when it cut the endpoint). The refusal was right that the pin was broken and right about why it matters.
- **R2, the O9 assignment contradicted itself and the count did not close.** Rewritten as the table below, with O9
  named SPLIT and the close restated as 7 + 5 + 1 + 1 mint = 9.

Two CARRY items, not refusal grounds, are also closed: the READ surface for manifest rows R1/R2 is now stated
(`C-NO-RAW-BRONZE-AT-SERVE`), and `C-TIER-PLACEMENT`'s "firm-attributable" wording, which described a different
tenancy from the one the builder prints, is struck. **13 contracts** (v0.1 had 12).

### v0.3 CHANGE NOTE -- 2026-09-23 ~01:3xZ, `1.0.0_SA_CTO~Z`

v0.2's **BRIEF half was REFUSED** by `2.0.0_SA_COO~Z` (re-routed under the spine's *"or a live `2.0.0_SA_COO` ...
in its stead"* provision, after `4.0.0_SA_CRO~G` was measured DEAF -- 13 unread, `read/` empty). **One bounded
ground, and it is this PRD contradicting ITSELF.** Both grounds verified at the bytes by this seat before amending.

⛔ **THE CONTRADICTION.** `:210` (the RATIFIED half, already SIGNED) places **O12 among "WHOLLY THE ADDENDUM'S"**,
corpus-side column `--`. `:319` (the BRIEF half) had **R12 building O12's own artifact -- the lifted
equity-research skill -- "under this project's home."** The brief assigns that artifact to O12 by name
(`:118-120`), and to an act this project explicitly does not perform.

⭐ **IT IS THE EXACT MIRROR OF THE DEFECT THIS PRD NAMES ABOUT ITSELF ONE SECTION EARLIER** (`:226-228`):
*"an outcome falls between two projects precisely when each document believes the other has it."* **Here BOTH
carriers claimed it.** Duplication rather than a gap -- **same class, same invisibility to every gate.**

⭐ **AND THE SECOND, INDEPENDENT, CHEAP CHECK IS THE ONE WORTH KEEPING: R12 WAS THE ONLY MANIFEST ROW WHOSE
`serves` COLUMN NAMED NO FWD.** R1-R11 each serve at least one. The preamble says *"Each row is a surface a cell
will build"* -- so R12 authorised **a cell with no outcome behind it**, in a project whose L10 closes only when
every FWD grades REALIZED. **A structural tell needs no argument: one column, one blank.**

**REMEDY TAKEN: R12 MOVED TO THE ADDENDUM.** The manifest is now **ELEVEN rows**. Two remedies were offered and
either would have cleared the contradiction; this one was chosen on three grounds:

1. **The three items serve O12, which the SIGNED ratified half places wholly with the addendum.**
2. **Substantively they are PRODUCER-METHOD artifacts, not corpus measurements.** This project's artifacts are
   MEASUREMENTS over the library -- templates, fund forms, typecast, continuation. **The lifted skill, the message
   design and the cost card are all about how the producer WRITES, which this project explicitly does not do.**
3. ⭐ **DECISIVE ON COST: the alternative amends `:210`, which is in the RATIFIED half the CVO has already SIGNED**
   -- making that signature stale and costing a second review cycle. **This remedy touches only the BRIEF half,
   which is already refused and must be re-issued regardless. One half-review instead of two.**

⚠ **THE DISCLOSED CONFLICT, ADDRESSED RATHER THAN INHERITED.** `2.0.0_SA_COO~Z` disclosed that its preferred
remedy **moves work TOWARD `AMGT_RESAPP`, which it drives**, and therefore stated the other remedy as equally
sufficient. **I took the remedy that favours the discloser's project** -- so: grounds 1 and 2 were reached on the
merits before the cost argument, and ground 3 is what makes it decisive. ⭐ **The disclosure is what allowed this
to be weighed rather than discovered, and it is the reason the refusal can be adopted whole.**

**O4 and O13 were CLEARED as FAITHFUL, not readings** -- the brief's own met-condition for O4 joins both halves
with *"and"*, and O13 names resolution, induction and printing the unresolved **in one sentence**. **The splits
follow the brief's own commas.**

### v0.4 CHANGE NOTE -- 2026-09-23 ~02:0xZ, `1.0.0_SA_CTO~Z`

**Raised by `2.0.0_SA_COO~X` within its first hour on the seat (msg 24530), at L5, before cutting.** ⛔ **THE THIRD
SELF-CONTRADICTION THIS PRD HAS YIELDED, and the first inside the RATIFIED half** -- `C-NO-VENDOR-CALL` says
*"Nothing in this project calls an external vendor API"*, while `FWD-4` required an induction act that **makes one
Bloomberg `reference_data` call per name, even under `--dry-run`.** **`FWD-4` was unachievable without breaking a
contract in the same document.**

**TWO AMENDMENTS, both to `FWD-4`. `C-NO-VENDOR-CALL` IS NOT TOUCHED.**

**1. THE BOUNDARY.** The seat proposed carving the one call out of the contract by name. ⛔ **REFUSED, because the
decisive fact was in its own message: `add_security` also writes `registrations.json` and the crosswalk pool --
`AMGT_RESAPP`'s OWN surfaces.** So `FWD-4` had THIS project writing ANOTHER project's surfaces. ⭐ **That is
exactly the R12 defect ruled two hours earlier in v0.3, and ruling the identical shape differently because the
remedy is less convenient here would make that ruling worthless.** The induction ACT is `AMGT_RESAPP`'s; this
project's half **ends at the executable request**.

⭐ **A contract that says "nothing here calls a vendor" is worth more INTACT than with one named exception -- the
exception is the crack a later reader widens.** No Andrew word is needed for this project, because it makes no
call; the per-use word belongs to `AMGT_RESAPP` when it inducts.

**2. THE POPULATION.** ⭐ **The seat ran a premise check on this outcome that its author never did:** *"the
crosswalk IS built from the universe, so resolved-and-absent may be an EMPTY set."* **If it is, `FWD-4` grades
NOT_REALIZED by construction, whatever anyone builds.** The population is re-pointed at the backlog folders the
universe carries UNRESOLVED (**60 of 93**, measured at L5), and `CRPS-c-5` **measures the resolved-absent set and
prints BOTH denominators** -- if non-empty, the original population stands beside the new one.

⚠ **HEADER CORRECTION, same version, recorded rather than version-bumped.** `2.0.0_SA_COO~X` pre-graded its
first order with the L6 gate's own `check_file()` and got ONE violation -- not in the order, in this PRD's header:
`brief_ref` carried `" (36,007 bytes)"`, and `org/standards/PRD_HEADER.schema.json` opens `(?![\s\S]*[\s\])`,
forbidding whitespace anywhere. **The gate was refusing EVERY order against this PRD.** ⭐ **The byte count was
added at v0.2 because the CVO's own refusal asked for it -- and I put a prose fact inside a schema-constrained
field when it already lived in the v0.2 change note, where it belongs.** The pin's VALUE is unchanged; only the
annotation is removed. ⭐ **And the header block is in NEITHER half, so this re-opens nothing** -- the same
preamble exclusion `2.0.0_SA_COO~Z` measured as an exposure an hour earlier is, here, exactly the behaviour that
saves a re-sign. No version bump: the version tracks substantive amendments, and the pin did not move.

⚠ **This version touches ENDPOINT, so `3.0.0_SA_CVO~Z`'s ratified half goes STALE and is re-signed.** Unavoidable
and cheap: **two clauses, no new outcome, and no contract weakened.**

### The problem, in Andrew's and the team's terms

The firm has written up 93 names by hand and filed the reports in the SharePoint Research library. The voice memo is
explicit that those reports are the starting point, not a nice-to-have: *"we start with the existing earnings reports
that are generated in SharePoint ... These form the foundation ... enriched, of course, by the Opal data harvest
pipelines."* And the backlog is the library itself: *"the backlog set that we want for 'Security Analysis' is just
every single company listed in the Asset Management/Research/ bucket in the Opal Capital 'Shared' Sharepoint."*

Today that library is a pile of files on a synced drive. It has been MEASURED twice (2026-09-10, 2026-09-15) and
**ingested zero times**. Nothing in the estate can answer, for a given security, *what did we last say about this
name, at what size, in which fund, against which KPIs* -- and the analysis layer that is supposed to write the next
report cannot be handed the previous one.

**Measured by the brief's scan, 2026-09-22** (`RESEARCH_CORPUS_SCAN_20260922/`): 93 name folders, 351 files
(184 PDF, 78 xlsx, 71 docx, 17 png, 1 html; 305.7 MB); four document classes with one stable skeleton; a fund named
for 59 of 93; a sector header readable for 75 of 93 in TWO vocabularies; 58 of 60 workbooks sharing one Bloomberg
core regardless of sector; the sector living in the PROSE and the CHARTS, not the sheet.

### What this project is NOT

It writes no report, runs no Claude call against a security to produce prose, owns no page surface, and touches no
other harvest channel. It produces the SUBSTRATE the analysis layer reads. The producer, the platinum report object,
the per-tab prose, the Posture synthesis, the adapter and the export are the `AMGT_RESAPP` addendum's, minted at an
L2 addendum on that project once the Lenovo trial's wave 2 is graded.

---

## ENDPOINT (step 2, /endpoint --forward)

`FWD-n` ids are PERMANENT and never reused. `DONE WHEN` is the bar, not the current state. **Each outcome is provable
by an act a seat can take on demand; none is a wait** -- there is no scheduled fire anywhere in this endpoint, because
the corpus is a static local library and every artifact below is derived by a run someone starts.

```

  FWD-1  Every report the team has written can be re-opened from our store
         exactly as it was filed
         DONE WHEN  EXERCISED -- for every file the library's own folder list
                    resolves to, the stored object is re-opened and matches the
                    file on the synced drive byte for byte, and the count of
                    objects equals the count of files scanned, both printed
         ACCEPT     Someone can ask for a name's last research pack and get the
                    team's own document back, not a summary of it and not a
                    re-typed copy.
         SOURCE     brief O5, Part V row 1; memo "we start with the existing
                    earnings reports that are generated in SharePoint"

  FWD-2  Every stored report says which security and which period it belongs to,
         and the ones that cannot be placed are named
         DONE WHEN  EXERCISED -- a query by security key returns that name's
                    reports in period order; and the run prints, as a
                    denominator, how many files resolved, how many did not, and
                    the reason for each that did not
         ACCEPT     A reader can get one name's history without opening a folder,
                    and nobody has to wonder what was quietly skipped.
         SOURCE     brief O5, O9; Rule 24 (the subtraction prints its denominator)

  FWD-3  The backlog universe IS the library's folder list, resolved to
         securities, with every unresolved folder shown
         DONE WHEN  EXERCISED -- the folder list is read fresh from the library
                    (never a transcribed list), each folder is resolved through
                    the identity layer to a security key, and the output carries
                    three counts that sum to the folder count: resolved,
                    unresolved-with-reason, and ambiguous-with-candidates
         ACCEPT     Andrew can ask "which of our written-up names is the page
                    missing" and get an answer whose denominator is the library
                    itself.
         SOURCE     Andrew ~18:3xZ "every single company listed in the Asset
                    Management/Research/ bucket"; brief O13, Part V row 2

  FWD-4  A backlog name the universe does not yet carry can be INDUCTED BY ONE
         COMMAND -- and this project produces that command's exact request,
         complete and executable, without calling any vendor
         DONE WHEN  EXERCISED -- for one backlog name the universe carries
                    UNRESOLVED, a single act produces the induction request:
                    it PRINTS what the induction WILL add before anything is
                    added, REFUSES a name whose identity is ambiguous, and is
                    driven end to end with a REFUSING TRANSPORT and the poison
                    POSITIVE-CONTROLLED, so the run COULD NOT have reached the
                    network rather than merely having not
         ACCEPT     Closing the gap between "we wrote this up" and "the page
                    knows about it" is one command per name, not a project --
                    and the command is ready here even though the firing of it
                    is not this project's act.
         SOURCE     brief O13, Part V row 2; the Lenovo trial's induction shape
         ⛔ BOUNDARY (v0.4): the induction ACT ITSELF is AMGT_RESAPP's, not
                    this project's. `add_security` writes that project's
                    `registrations.json` and crosswalk pool and spends its
                    vendor budget (one Bloomberg reference_data call per name,
                    even under --dry-run). THIS PROJECT'S HALF ENDS AT THE
                    EXECUTABLE REQUEST. C-NO-VENDOR-CALL is therefore UNTOUCHED.
         ⚠ POPULATION (v0.4): "resolved but absent from the universe" may be
                    EMPTY BY CONSTRUCTION -- the crosswalk is BUILT from the
                    universe. The population is therefore the backlog folders
                    the universe carries UNRESOLVED (measured 60 of 93 by
                    2.0.0_SA_COO~X at L5). CRPS-c-5 measures the resolved-absent
                    set and PRINTS BOTH DENOMINATORS; if it is non-empty, the
                    original population stands beside this one.

  FWD-5  For a name the team has written up, its OWN thesis pillars, KPI set,
         fund of record and last stated position are readable as typed data,
         each pointing at the report it came from
         DONE WHEN  EXERCISED -- for one covered name, the continuation artifact
                    is produced and every field in it resolves to a passage in a
                    named report; a field the reports do not state is ABSENT,
                    never inferred and never defaulted
         ACCEPT     The next report can open with what we last said, and a reader
                    can check that we actually said it.
         SOURCE     Andrew "if they have a 'why we own this' or some kind of KPI,
                    the analysis should assess the delta on those features";
                    brief O2, F16 s.4

  FWD-6  For a business type, the team's own report shape is readable as one
         typed template -- its section names, its KPI set and its chart pages
         DONE WHEN  EXERCISED -- the template for one business type is produced
                    from the corpus and prints the denominator it was measured
                    over (how many of that type's reports, of how many total) and
                    the per-term counts behind each KPI it lists
         ACCEPT     A bank's page can carry CET1, cost of risk, NIM and RoTE
                    because the team's bank reports carry them -- and the
                    evidence for that claim is a count, not an opinion.
         SOURCE     memo "banks versus insurance companies are going to have
                    different financial models"; brief O4, F15

  FWD-7  The generic model shape the team uses for EVERY sector is readable as
         one typed template, separately from the sector ones
         DONE WHEN  EXERCISED -- the typecast artifact lists the shared mnemonic
                    core, the extended ratio set and the Opal Case Assumptions
                    block, each with the count of workbooks carrying it out of
                    the workbooks read
         ACCEPT     The Model tab keeps one shape for everyone, and the sector
                    lives where the team actually puts it -- in the prose and the
                    charts.
         SOURCE     Andrew "typecast 'Model' formats (what ratios are they using)
                    ... on a sector-level"; brief F14 (58 of 60 share one core)

  FWD-8  A consumer can fetch, for one security, every corpus artifact it needs
         in one call, and can tell when any of them has moved
         DONE WHEN  EXERCISED -- one call by security key returns the prior
                    reports, the continuation artifact, the sector template and
                    the typecast, each with a content hash; a second call after a
                    new report lands returns a changed hash for exactly the
                    artifact that changed and unchanged hashes for the rest
         ACCEPT     The analysis layer never re-derives this substrate and never
                    guesses whether it is current.
         SOURCE     brief O8, Part I-A (documents handed "by key + hash, none
                    fetched"); C-INPUT-HASHED

  FWD-9  Nothing this project runs can write to, move or delete anything in the
         team's library
         DONE WHEN  EXERCISED -- a deliberate negative control runs the ingestion
                    against a read-only copy of the library and completes; and a
                    census of the project's own code prints zero write, move,
                    delete or open-for-write calls against any path under the
                    library root, with the denominator of files scanned
         ACCEPT     Adam's team's folder is exactly as they left it, and we can
                    prove it rather than assert it.
         SOURCE     brief Part II ("the corpus is Adam's team's and read-only to
                    us"); CLAUDE.md hard stops (no unrecoverable act without a
                    human word)

  ===== ADDENDUM A, v0.5, 2026-09-24 -- FWD-10..FWD-19 ==========================
  Cut from docs/briefs/amgt-corpus-dossier-fold-brief-20260924.md@328e17d5e5
  (4.0.0_SA_CRO~Y) plus Andrew-direct ~04:3xZ and ~05:0xZ. Rationale, the
  numbering refusal, the O7 contradiction and the contracts are in ADDENDUM A
  below; THESE ARE THE DEFINITIONS AND THIS FENCE IS THEIR ONLY CARRIER.

  FWD-10 An analyst opens a covered name and reads the TEAM'S OWN
         investment-thesis pillars on the Thesis tab
         DONE WHEN  EXERCISED -- IMB_LN_Equity renders the pack's pillars as bold
                    lead plus paragraph, each openable to the report and the
                    passage it came from, and each marked as the team's rather
                    than generated
         ACCEPT     An analyst can tell the team's own thesis from a machine's
                    and can reach the sentence it came from.
         SOURCE     brief O1 :48
  FWD-11 The pack's MANAGEMENT / BOARD passage appears on Exec Management as the
         team's own cited text
         DONE WHEN  EXERCISED -- the passage renders labelled as the team's,
                    BESIDE the filing roster, with the roster unchanged; and a
                    name whose pack carries none reads ABSENT with its reason
         ACCEPT     The team's view of management is readable without displacing
                    the filing record.
         SOURCE     brief O2 :57; C-EXEC-MANAGEMENT is authority and is untouched
  FWD-12 The Model tab's rows are the typecast's mnemonic core plus the sector
         template's KPI set, and the team's own cases are readable
         DONE WHEN  EXERCISED -- rows come from the typecast and the template for
                    that business type; every row carries a figure or reads
                    ABSENT with a reason; the team's Upside/Base/Downside cases
                    render as the team's, cited, in the slot that is ABSENT today
         ACCEPT     The sheet's shape is the team's own, and no row is blank
                    without saying why.
         SOURCE     brief O3 :63. The 22 added mnemonics' FIGURES wait on R-16's
                    unauthorized V3 word; labels and row order do not
  FWD-13 Every folded field is CITED or ABSENT with a readable reason
         DONE WHEN  EXERCISED -- a census over the dossier's fields prints zero
                    fields that are neither cited nor reason-bearing, with the
                    denominator of fields scanned; and a negative control shows a
                    deliberately uncitable field rendering ABSENT rather than
                    blank or inferred
         ACCEPT     Nothing on the page is inferred, defaulted or paraphrased
                    from the team's words.
         SOURCE     brief O4 :71; C-CITED-OR-ABSENT, C-INPUT-HASHED. Scope is the
                    brief's own: FWD-10..FWD-12 and FWD-15
  FWD-14 Any folder in the Research list returns its dossier or the printed
         reason there is none
         DONE WHEN  EXERCISED -- for a named folder the read returns a dossier or
                    a reason; and the three counts (resolved / ambiguous /
                    empty-or-workbook-only) SUM TO THE FOLDER COUNT every time
         ACCEPT     Andrew can name any folder and get an answer, never a silence.
         SOURCE     brief O5 :77; C-FOLDER-LIST-IS-THE-DENOMINATOR
  FWD-15 The fund of record and last stated position read as the TEAM'S stated
         posture, cited, beside the unchanged machine judgment
         DONE WHEN  EXERCISED -- both render cited on the header posture line and
                    the Posture tab, and the machine verdict is byte-unchanged by
                    their presence
         ACCEPT     The team's posture informs the reader without becoming the
                    judgment.
         SOURCE     brief O6 :84 (marked PROPOSAL by its author); Andrew: "Posture
                    is still up to us", so this is an INPUT and never the verdict
  FWD-16 A PDF-only pack gets the same fold, or the tab states which shape the
         PDF could not be read to and why
         DONE WHEN  EXERCISED -- a PDF-only name renders pillars, management and
                    cases from the PDF pack; and the docx path is KEPT AS THE
                    CONTROL and still recovers what it recovered before
         ACCEPT     A name is not poorer for having been filed as a PDF.
         SOURCE     brief O7 :91 AT ITS AMENDED BYTES. Extractability is MEASURED
                    (99 of 99 on the control) -- this is a READER change and NO
                    CELL RE-MEASURES IT (A.2)
  FWD-17 A newly filed report becomes a new immutable bronze object and the
         dossier rebuilds, with the prior dossier still readable
         DONE WHEN  EXERCISED -- a new report lands, a new report_id16 appears
                    BESIDE the old, the dossier's inputs_sha16 changes, the page
                    serves the newer pillars, and the prior as_of object still
                    reads; and a rebuild with UNCHANGED inputs writes NOTHING and
                    says so
         ACCEPT     The store grows and never overwrites, and a re-run is
                    distinguishable from a change.
         SOURCE     brief O8 :108; C-DOSSIER-REBUILD-IS-A-NO-OP-ON-UNCHANGED-INPUTS.
                    Person-started; no notifier and no schedule
  FWD-18 Each pillar and KPI row names its terms, and the header feed and Chatter
         axis are filterable to those terms
         DONE WHEN  EXERCISED -- a pillar's terms are readable on the page and the
                    feed filters to them for at least one name
         ACCEPT     A theme the team named is followable into the news.
         SOURCE     brief O9 :115. Marked PROPOSAL and LATER enrichment by its
                    author: cut LAST, deferrable by the round-N analysis without
                    re-opening anything
  FWD-19 EVERY SECURITY IN THE ASSET MANAGEMENT RESEARCH FOLDER -- all 93 -- is
         dispositioned through the opal-data-harvest channels
         DONE WHEN  EXERCISED -- a census prints, for all 93, dossier-served /
                    resolved-but-no-prose / unresolved-with-reason, and THE THREE
                    SUM TO 93; the 60 today-unresolved folders are inducted by a
                    SCRIPTED producer and re-ingested; and the 11 that can never
                    carry prose (10 workbook-only, 1 empty) are NAMED with their
                    reason rather than dropped from the denominator
         ACCEPT     Andrew names any of the 93 and gets its corpus layers or the
                    reason it has none. 93 of 93 DISPOSITIONED -- never 93 of 93
                    populated, which 11 folders make impossible by construction.
         SOURCE     Andrew-direct ~04:3xZ "we also need backfill for all the asset
                    management securities", population fixed by his ~05:0xZ test
                    "every single security in the Asset Management research
                    folder"; C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER.
                    NOT IN THE L1 BRIEF -- see A.3's subtraction.
                    STARTING STATE (ingest_run.json, scan 2026-09-23T03:09Z, from
                    the worker's run record, NOT head-object verified): 33
         ADDENDUM   1.0.0_SA_CTO~Z, 2026-09-26 ~01:2xZ. EVERY NUMBER IN THIS
                    FENCE IS A READING, NOT A CONSTANT, and three of them have
                    already moved. The fence's own SOURCE cites
                    C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER, which rules
                    that "EVERY FWD-19 POPULATION CLAIM IS A SUBTRACTION FROM A
                    FRESH READ OF THE ASSET MANAGEMENT RESEARCH FOLDER, WITH THE
                    DENOMINATOR PRINTED" -- so the contract already binds this
                    fence and the constants below are snapshots it supersedes.
                    Stated explicitly because they read as the claim: "all 93"
                    and "93 of 93" -> THE FOLDER READ FRESH, which measured 93 on
                    2026-09-24, 94 at 2026-09-25 14:4xZ and 95 at 22:5xZ, the
                    95th being AIA Group, registered @2c35b9a062 and present in
                    crosswalk/v1/2026-09-25.json v3 with folders_in_records 95 ==
                    research_folders_live 95. "the 60 today-unresolved folders"
                    -> the unresolved count read fresh, which reads 0 today.
                    "the 11 that can never carry prose (10 workbook-only, 1
                    empty)" -> that class read fresh, which reads 12. NO ENDPOINT
                    CHANGES: the outcome is still every security in the folder
                    dispositioned, and the 11-cannot-be-populated caution still
                    stands as a CLASS rather than a count. The THREE-value
                    partition is NOT amended and needs no amendment: CRPS-g-3
                    (@bae7f689bc) made the census emit the fence's own three
                    names with the fold stated -- resolved-but-no-prose =
                    served_as_empty_shell + resolved_no_prose -- which closes
                    round 4's R-2 and is why this addendum touches numbers only.
                    resolved / 123 stored; 60 folders / 228 files NOT ingested
                    BECAUSE IDENTITY RESOLUTION FAILED. The blocker is IDENTITY,
                    not acquisition: 60 of 93.

```

**Rule 24 record for this endpoint.** Axis: what an analyst or a consumer can DO that they cannot do today. Grain: one
capability. Intent: one (the corpus becomes usable substrate). MECE by SUBTRACTION over the brief's thirteen outcomes,
not by recall:

| brief outcome | disposition | where its corpus-side half lands |
|---|---|---|
| O1, O3, O6, O7, O10, O11, O12 | **WHOLLY THE ADDENDUM'S** (each writes or serves the report) | -- |
| O2 | SPLIT | measured half **FWD-5**; the delta-writing half is the addendum's |
| O4 | SPLIT | the TEMPLATES **FWD-6 / FWD-7**; the page's rendering of them is the addendum's |
| O5 | SPLIT | ingestion and reachability **FWD-1 / FWD-2 / FWD-8**; the message carrying the prior report is the addendum's |
| O8 | SPLIT | the input-hash half **FWD-8**; served freshness on the page is the addendum's |
| O9 | **SPLIT** | its REACHABILITY half (the prior quarter's report retrievable beside the current one) **FWD-1 / FWD-2 / FWD-8**; its report VERSIONING and rendering half is the addendum's |
| O13 | WHOLLY HERE | **FWD-3 / FWD-4** |

FWD-9 is NOT in the brief's outcome list: it is a property Part II states as a constraint, and it is minted as an
outcome because a constraint nobody exercises is a belief.

**CLOSE: 13 brief outcomes -> 7 wholly the addendum's + 5 split + 1 wholly here, plus 1 minted = 9 FWD.**

⛔ **v0.1 WROTE O9 TWO WAYS AND THE COUNT DID NOT CLOSE** -- this record said "O9 is the addendum's (report
versioning)" while the cover message that routed it said "2 wholly here (O9's reachability half, O13)". Both cannot
hold, and with O9 read as wholly the addendum's the arithmetic is 8 + 4 + 1, not the 7 + 4 + 2 printed beside it.
**THE FAILURE MODE IS THE GREEN THIS PRD NAMED ONE PARAGRAPH EARLIER:** a reader of either carrier could conclude the
OTHER owns O9's corpus-side half, and no gate anywhere would fail -- an outcome falls between two projects precisely
when each document believes the other has it. Found by `3.0.0_SA_CVO~Z` at L4-R (@`f00abf5e5303`, REFUSED) by running
the subtraction the other way, from the brief's own O1..O13 against BOTH carriers, exactly as this seat asked it to.
**No outcome was uncovered; the defect was in the RECORD, which is the harder one to see.**

---

## CONTRACTS

Ratified text. A contract is binding on every cell; a cell that cannot meet one is refused at the cut, not at the drain.

**C-CORPUS-READ-ONLY.** The library is read-only to this estate. Every read opens the file for reading only; no code in
this project may write, move, rename or delete under the library root, and no run may depend on the library being
writable. The library path is resolved, never hardcoded (it is a synced local path and differs per device).

**C-CORPUS-AS-RECEIVED.** Each stored report is the file's bytes as filed, with its own `sha256`, its source path
relative to the library root, its file modification time as the library reports it, and the scan vintage. Extraction
(text, headings, tables) is a SEPARATE object that names the bytes object it was derived from. **Bronze is never
re-written**: a changed file lands as a NEW object, and the prior one stays.

**C-FOLDER-LIST-IS-THE-DENOMINATOR.** Every population claim about the backlog is a subtraction from a FRESH read of
the library's folder list, printed with its count, never a forward list of names anyone remembers. A folder that
resolves to no security is REPORTED as unresolved with its reason; it is never dropped, and an empty unresolved set is
itself printed as `0 of N`.

**C-IDENTITY-VIA-THE-LAYER.** A folder resolves to a security through `AMGT_RESAPP`'s identity layer and its crosswalk,
never by a local string match in this project. An ambiguous resolution returns its candidate list and is graded
unresolved. This project adds no second identity mechanism.

**C-CITED-OR-ABSENT.** Every field of a continuation artifact, a sector template or a typecast carries the report (and
passage or sheet) it was measured from. A field the corpus does not state is `null` with an explicit `absent` reason.
**Nothing in this project infers, defaults or fills.**

**C-TEMPLATE-IS-MEASURED.** A sector template, a fund form and the typecast are MEASUREMENTS with printed denominators
(reports of that type read, of the total; per-term counts), never a designed list. Where the two funds' skeletons
differ, BOTH are kept and labelled; the fund of record picks at serve time.

**C-INPUT-HASHED.** Every artifact this project serves carries `{key, sha256}` for each input it was derived from, its
own content hash, and the method version that produced it. A consumer decides freshness from those hashes and never
from a clock.

**C-BUILDER-ADDRESSES (Rule 30).** Every S3 address is `lib/opal_naming.py address()` output and every resource name is
`name()` output. A builder REFUSAL is a missing registry row to add under `infra/logic/registry/`, never a hand-typed
path. **This PRD types no address**: each manifest row below names the scope, tier and partition the builder is called
with, and the cell prints the builder's output.

**C-TIER-PLACEMENT.** Report bytes and their extractions are BRONZE under the harvest scope; the typed per-report record
is SILVER; the continuation artifacts, sector templates, fund forms and typecast are GOLD (JSON). The PLATINUM report
object is the addendum's and is NOT written here. **TENANCY, stated so the sentence and the builder agree:** every tier
of this project's surfaces lands in the GENERAL harvest home the builder prints
(`s3://opal-data-harvest/amgt/harvest/`), verified by `3.0.0_SA_CVO~Z` running `address()` on all 8 store-writing
manifest rows -- **8 of 8 print, 0 refuse.** v0.1 called the gold artifacts "firm-attributable", which reads as the
FIRM-bucket tenancy of `infra/logic/02_DOCTRINE.md` R1-R21 and describes a different home from the one the builder
returns. The word is struck: these are derived judgments about the firm's own research and they live in the harvest
scope's general home, as the tier registry already rules.

**C-NO-RAW-BRONZE-AT-SERVE.** Manifest rows R1 and R2 (report bytes and their extractions) are read by THIS project's
derivation cells and by the addendum's analysis producer. **They are never a page read.** The page's prose comes from
the addendum's platinum report object; a prior report reaches a reader as a CITED passage inside that object, never as
raw bronze bytes streamed to the browser. This is stated because the bronze lands in a harvest pool the page adapter
can reach, and "nothing serves it" was true by intention only until this line (`3.0.0_SA_CVO~Z` carry item 1).

**C-NO-VENDOR-CALL.** Nothing in this project calls an external vendor API or the Claude API. Extraction is local
parsing of files the firm already holds. (The message design and the cost card this project owns are DOCUMENTS; the
cost card's measured run is an addendum act, run under Andrew's word, and is named as such in the manifest.)

**C-NO-NOTIFIER.** No alert, alarm, monitor, freshness checker or scheduled notifier is built (standing moratorium). A
staleness QUESTION is answered by C-INPUT-HASHED at read time.

**C-LOCAL-AND-DEVICE-DERIVED.** The library is synced to a device and its root is derived, never hardcoded; a run on a
device without the library refuses loudly with the path it looked for, and does not report an empty corpus.

---

## SURFACE MANIFEST

Each row is a surface a cell will build. Addresses are builder OUTPUT, printed by the cell; this table names the
builder ARGUMENTS only.

| # | surface | scope / tier / partition (builder arguments) | serves |
|---|---|---|---|
| R1 | report bytes as filed | harvest / bronze / research-report, by security key + report id | FWD-1 |
| R2 | per-report extraction (text, headings, tables, sheet labels) | harvest / bronze / research-report-extract, same partition | FWD-1, FWD-5..7 |
| R3 | typed per-report record (class, fund, sector as the team wrote it, period, author, size) | harvest / silver / research-report, by security key | FWD-2 |
| R4 | the library folder census + resolution result | harvest / gold / research-backlog, one object per scan vintage | FWD-3 |
| R5 | universe induction act + its read-back | (consumes `AMGT_RESAPP`'s universe; writes no new surface) | FWD-4 |
| R6 | per-name continuation artifact | harvest / gold / research-continuation, by security key | FWD-5 |
| R7 | sector template, one per business type | harvest / gold / research-sector-template, by business type | FWD-6 |
| R8 | fund form, one per fund of record | harvest / gold / research-fund-form, by fund | FWD-6 |
| R9 | generic model typecast | harvest / gold / research-model-typecast, one object | FWD-7 |
| R10 | the one-call substrate read by security key | a read path over R1-R9; no new store | FWD-8 |
| R11 | the read-only proof (negative control + code census) | a ledger record, no store | FWD-9 |
**ELEVEN ROWS. R1-R11 above, and every one names at least one FWD in `serves`.**

⛔ **R12 IS REMOVED IN v0.3 AND MOVED TO THE `AMGT_RESAPP` ADDENDUM.** It read *"the lifted equity-research skill
artifact, the message design and the cost card | repo documents under this project's home | (method; feeds the
addendum)"* -- and it was the **ONLY** row whose `serves` column named no FWD. See the v0.3 change note.

---

## WHAT MUST BE MEASURED BEFORE A CELL (Rule 28 cards)

| # | substrate | question | owner |
|---|---|---|---|
| K1 | the library on THIS device | its derived root; the folder and file counts at cell time versus the scan's 93 / 351; whether the sync is complete or partial, and how a partial sync is distinguishable from a small library | the ingestion cell |
| K2 | the identity layer | what fraction of the 93 folder names resolve through the existing crosswalk, and what the ambiguous ones look like -- the denominator decides whether FWD-3 needs a human pass | the backlog cell |
| ~~K3~~ | ~~the PDF-only reports~~ | ⛔ **CLOSED 2026-09-24 BY ADDENDUM A.2 -- ANSWER YES.** The positive control recovers **99 of 99** docx pillars from the PDF (56 same-stem pairs, 17 FULL); 26 of 30 PDF-only folders carry a full pack; cause is `extract.py`'s standalone-heading heuristic being blind to the PFOE packs' INLINE BOLD LEADS. Package `PDF_EXTRACTABILITY_20260924/SUMMARY.md` @`d64d83a5d2`, ruling R-22 @`61fdf4c12f`. ⭐ **A CARD LEFT OPEN AFTER ITS ANSWER LANDS IS A STANDING ORDER TO RE-MEASURE** -- no cell is cut for this | ~~the extraction cell~~ -- nothing owed |
| K4 | the workbooks | whether the model sheets read without Excel on this box, and whether the 23 FactSet-coded variants type onto the same mnemonics | the typecast cell |
| K5 | period resolution | how a report's PERIOD is determined (filename, header, or content) and how many of the 351 carry one -- FWD-2's ordering depends on it | the ingestion cell |

---

## OPEN CALLS -- none held at Andrew by this PRD

The three calls this brief raised for Andrew are ANSWERED: the split and the name (~18:2xZ), the backlog population
(~18:3xZ), and sending Bloomberg figures to the Claude API (~18:2xZ, *"That is allowed"*). The vendor-subscription and
plugin-install calls in the RCN-0012 proposal are NOT this project's -- it calls no vendor and installs nothing.

**One call is carried to L5, not to Andrew:** whether FWD-3's unresolved folders get a human pass or stay a printed
denominator is decided by K2's number, by the seat that measures it.

---

## L4-R SIGN-OFF

Two halves, each hash-bound (spine v3.15):
- **RATIFIED TEXT** (ENDPOINT + CONTRACTS) -- `3.0.0_SA_CVO~Z`;
- **BRIEF** (everything else) -- `4.0.0_SA_CRO~Z` on this fabric, or a live `2.0.0_SA_COO` in its stead.

The brief's author is `4.0.0_SA_CRO~F`; the brief half is routed to this fabric's CRO lane by the tool's own routing,
and `~F`'s authorship is named here so the reviewer can consult it.

Stamp: `python .tools/prd-signoff.py sign|refuse AMGT_CORPUS --half ... --review <path>@<pin>`. Status:
`python .tools/prd-signoff.py status AMGT_CORPUS`.

**No task order may be cut against this PRD until both halves read SIGNED at the current bytes.**

---
---

# ADDENDUM A -- THE DOSSIER FOLD AND THE FULL BACKFILL (v0.5, L4, 2026-09-24)

**Author** `1.0.0_SA_CTO~Z`. **Driver** `2.0.0_SA_COO~X`, named by Andrew. **Cut for a fresh CANONICAL ROUND** --
`AMGT_CORPUS` handed back out of closer mode at `ad5c7a75c6` (`HANDBACK_TO_CANONICAL_20260924.md`, R-26).

**Andrew-direct 2026-09-24 ~04:3xZ at this terminal, VERBATIM, the sentence this addendum answers:** *"spec out a
new analysis that can be handed off to new rounds for development on AMGT_CORPUS (Not only do we need the
incorporated layers from the corpus however we decided to do that i.e. using your dossier addendum we also need
backfill for all the asset management securities) ... Then you can have COO~X take CORPUS."*

**L1 basis** -- `4.0.0_SA_CRO~Y`, `docs/briefs/amgt-corpus-dossier-fold-brief-20260924.md`, cut at its AMENDED
bytes **@`328e17d5e5`** (base @`be09d62ef7`, Part VIII @`5ef3e9a89b`, the O7/F2 amendment @`328e17d5e5`).
⛔ **PINNED AT THE AMENDMENT DELIBERATELY: the base commit carries the SUPERSEDED extractability claim**, and this
PRD's own v0.2 change note records what pinning a brief's earlier bytes costs.

**Nothing in ADDENDUM A retires or amends `FWD-1`..`FWD-9`, R1..R11, or any `C-` contract except the ONE named in
A.4.** `FWD-1`..`FWD-9` stand exactly as ratified.

## A.1 -- ⛔ THE BRIEF'S OWN OUTCOME NUMBERING IS REFUSED, AND THE REASON IS A COLLISION

The brief states at `:46` that its `O1` *"becomes `FWD-1` of the addendum"*. ⛔ **`FWD-1` IS TAKEN** -- it is this
PRD's *"Every report the team has written can be re-opened from our store"* (`:176`), and the same brief declares at
`:35` that `FWD-1..FWD-9` **do not move**. **Minting a second `FWD-1` would give this project two outcomes with one
id, which is the one thing endpoint numbering forbids** (`/open-calls`: new ids *"at the next unused number, never
renumbered, never reused"*). **RULED: the brief's `O1`..`O9` become `FWD-10`..`FWD-18`**, in the brief's own order,
and the brief's sentence is the defect rather than this PRD's.

## A.2 -- ⛔ THE BRIEF CONTRADICTS ITSELF ABOUT O7, AND THE STALE HALF IS PHRASED AS AN INSTRUCTION

The O7 amendment (`:97-106`) and the F2 supersession (`:187-190`) measure PDF extractability and settle it:
**26 of 30 PDF-only folders carry a full research pack; 29 of 30 yield pillars or a "Why we own"; the positive
control recovers 99 of 99 docx pillars from the PDF** (package `PDF_EXTRACTABILITY_20260924/SUMMARY.md`
@`d64d83a5d2`, ruling R-22 @`61fdf4c12f`). **THREE LATER PASSAGES STILL SAY IT IS UNMEASURED:**

| stale passage | what it says |
|---|---|
| `:280-282` | *"O7's feasibility is UNMEASURED and is **the first thing the cut should measure**"* |
| `:285-286` | *"It did not measure how many of the 30 PDF-only folders are Class A packs ... versus Class B updates"* |
| `:404-405` | *"the PDF path (O7; 30 folders) is unmeasured for extractability and is **the first cell to measure**"* |

⛔ **TWO OF THE THREE ARE WRITTEN AS A DIRECTIVE TO THE NEXT SEAT, NOT AS A CAVEAT** -- *"the first thing the cut
should measure"* is a cell a COO would cut, spending a round re-measuring a question whose answer ships in the same
brief. ⭐ **THIS IS EXACTLY R-26a's SHAPE ONE LEVEL OUT: THE DECISION WAS AMENDED AND THE COORDINATES WERE LEFT** --
and here the surviving coordinate is an imperative, which is the worst kind, because a later seat EXECUTES it.
**RULED: the `:97-106` / `:187-190` text is authoritative (later vintage, package hash, CTO ruling);
`:280-282`, `:285-286` and `:404-405` are STALE AND DO NOT BIND.** ⛔ **NO CELL IS CUT TO MEASURE PDF
EXTRACTABILITY.** `FWD-16` (brief `O7`) is a READER change, and its three reader rules are already written down.

**AND THE Rule-28 CARD `K3` IS CLOSED BY THE SAME MEASUREMENT.** `K3` asks *"whether the PDF text is extractable to
the same skeleton"* and would have sent the extraction cell to answer it. ⭐ **A CARD THAT HAS BEEN ANSWERED IS A
CARD THAT MUST BE CLOSED, OR IT FUNCTIONS AS A STANDING ORDER TO RE-MEASURE.** `K3` is CLOSED: answer YES, at
99 of 99 on the control, with the reader's inline-bold-lead blindness as the cause.

## A.3 -- THE NEW OUTCOMES: `FWD-10`..`FWD-19`

⛔ **THE DEFINITIONS LIVE IN THE ENDPOINT SECTION ABOVE AND ARE NOT REPEATED HERE. ONE CARRIER.** This section holds
only the REASONING. ⚠ **AND THAT SPLIT IS A CORRECTION, NOT A STYLE CHOICE:** the first cut of this addendum defined
the ten outcomes HERE and in the header, leaving the ENDPOINT section -- **the surface step 5 actually reads** --
without them. **The step-4 PRD surface-manifest gate REFUSED the commit and named all ten**, with the reason:
*"the R3 monitor reads the header and step 5 reads the section, so this drift is invisible to a reader and total to
a consumer."* ⭐ **THAT IS THE THIRD INSTANCE TONIGHT OF THIS SEAT AMENDING A DECISION AND LEAVING A COORDINATE**
(R-26a's generated-vs-declared row; A.2's stale O7 instruction; this). **The first two were found by reading; this
one was found by a gate, which is the only one of the three that could not have been missed.**

⛔ **`FWD-19` IS NOT IN THE BRIEF AND IS THE HALF ANDREW ADDED TONIGHT.** Measured by subtraction from his sentence
rather than recalled from the brief: he named **two** things, *"the incorporated layers"* AND *"backfill for all the
asset management securities"*. The brief covers the first and, on its own words, **the second is absent from it** --
*"backfill"* appears in the brief exactly ONCE, in a filename in its REFS block (`:423`), and `add_security` appears
NOWHERE. Its population rule is strictly the 93-folder Research list (`:79`, `:267`). **So a round cut from the
brief alone would deliver one of the two things he asked for, and the brief would look complete.**


⚠ **`FWD-18` AND `FWD-15` ARE MARKED PROPOSAL BY THEIR OWN AUTHOR** (`:86`, `:117-118`). They are cut as outcomes
so they are gradeable, and the round-N analysis may defer either; neither is a bar on the other eight.

## CONTRACTS -- A.4 -- ⛔ ONE CONTRACT IS AMENDED BY NAME, BECAUSE `FWD-19` IS OTHERWISE UNACHIEVABLE

`C-NO-VENDOR-CALL` reads *"Nothing in this project calls an external vendor API or the Claude API."* The 60-name
induction needs **one Bloomberg `reference_data` call per name**. ⚠ **THIS PRD HAS ALREADY BEEN HERE ONCE AND ITS
FIRST ANSWER NO LONGER HOLDS.** At v0.3 (`:104-106`) the same collision was found against `FWD-4`, and it was
resolved by having `FWD-4` produce an **EXECUTABLE REQUEST** that something else runs -- leaving `C-NO-VENDOR-CALL`
untouched (`:231`). ⛔ **THAT RESOLUTION IS NOW THE "NO FWD IS A WAIT" DEFECT RULE 27 FORBIDS:** the request was
built (`induction_request.json`, `unresolved_in_universe 60`) and **nobody has executed it**, so the outcome's only
proof is an act no seat in this project may take. Measured: 60 folders still unresolved a day later.

**RULED -- `C-NO-VENDOR-CALL` IS AMENDED, NARROWLY, AND NOTHING ELSE IS:**

> **`C-NO-VENDOR-CALL` (v0.5).** This project calls no external vendor API and no Claude API, **WITH ONE
> EXCEPTION: the identity induction of a backlog name may make ONE Bloomberg `reference_data` call per name,
> ONCE, through `add_security`, from a SCRIPTED DETERMINISTIC PRODUCER.** Every other vendor surface stays barred,
> the Claude API stays barred, and the Model-block figure pull is NOT covered by this exception.

Authority, and it is Andrew's own word twice over: **R-16** registers the grant (V1 price pull, **V2 the 60 backlog
names via `add_security`**, ⛔ **V3 the Model tab's Bloomberg figure pull NOT AUTHORIZED**), and **R-21** carries his
mechanism constraint VERBATIM -- *"the pull should be deterministic/scripted in nature like the existing pull, i do
not like the idea of relying on an agent for something a script can do way better."*

⛔ **THREE LIMITS ON THE EXCEPTION, EACH ONE A REFUSAL A GRADER CAN APPLY:**
1. **AN AGENT TURN IS NOT A PRODUCER.** A vendor call made from a seat's turn FAILS this contract even if the
   value it returns is correct. R-21b already stands this up as a grading criterion.
2. **THE WORD AUTHORIZES THE CALLS, NOT A PICK.** `3.0.0_SA_CVO~Z`'s standing ruling on ambiguous names holds:
   `induction_request.json` already REFUSES America Movil (folder `AXMB`, report `AMXB`) and that refusal is
   CORRECT. An ambiguous name is a refusal with a reason, never a guess, and never a coin-flip resolved by a build.
3. **THE MODEL PULL IS A SEPARATE PER-USE WORD.** The brief says so twice (`:253-254`, `:400`) and R-16 excludes it
   as V3. `FWD-12` therefore lands the typecast's measured mnemonic set and the row ORDER and LABELS; the 22 added
   mnemonics' FIGURES wait on that word, and the tab reads ABSENT-with-reason until then -- **which is `FWD-13`
   working, not `FWD-12` failing.**

## CONTRACTS -- A.5 -- NEW CONTRACTS (the brief mints no `C-` ids; these are this seat's)

**`C-DOSSIER-IS-COMPOSED-NEVER-AUTHORED`.** The dossier is a COMPOSITION of artifacts that already exist -- the
continuation artifact, the sector template, the fund form, the typecast, the bronze extraction -- plus the cited
passages. No cell authors a new judgment into it and no field is synthesised across reports.

**`C-DOSSIER-DATE-IN-THE-OBJECT-NAME`.** ⭐ **EXERCISED AGAINST THE BUILDER, NOT RESTATED FROM THE BRIEF.**
`lib/opal_naming.py address()` output is
`s3://opal-data-harvest/amgt/harvest/gold/research-dossier/security_key=<KEY>`, and the builder **REFUSES** a
two-level partition with its own message: *"partition must be a non-empty ASCII string with no '/' and no outer
space"*. **So `as_of` lives in the OBJECT NAME**, `<YYYY-MM-DD>.<inputs_sha16>.json`, one object per rebuild whose
inputs changed, never overwritten, reader takes the newest `as_of`. A true second partition key is a registry row
under `infra/logic/registry/` (Rule 30) and is NOT cut here.

**`C-DOSSIER-TABLE-SPELLING`.** ⛔ **THE BUILDER ACCEPTS BOTH `research_dossier` AND `research-dossier` AND REFUSES
NEITHER, SO TWO SPELLINGS WOULD SILENTLY PRODUCE TWO STORES.** Settled on the LIVE PLANE rather than by preference:
`amgt/harvest/gold/` carries **5 of 5 `research-*` tables HYPHENATED** (`research-backlog`, `research-continuation`,
`research-fund-form`, `research-model-typecast`, `research-sector-template`) beside 4 underscored non-research
tables. **THE SPELLING IS `research-dossier`.** ⚠ The cross-family inconsistency is real, is not this round's to
fix, and is a surprise row rather than a cell.

**`C-DOSSIER-REBUILD-IS-A-NO-OP-ON-UNCHANGED-INPUTS`.** A rebuild whose `inputs_sha16` is unchanged writes nothing
and says so. This is the discriminator that makes `FWD-17` gradeable: a rebuild that always writes cannot
distinguish "the report changed" from "the job ran".

**`C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER`.** ⛔ **EVERY `FWD-19` POPULATION CLAIM IS A SUBTRACTION FROM A
FRESH READ OF THE ASSET MANAGEMENT RESEARCH FOLDER, WITH THE DENOMINATOR PRINTED.** The population is **93 folders**
and the target is **every one of them**: resolved-with-a-dossier, or carrying a printed reason it has none, and the
three counts summing to 93 every time.

⚠ **THIS CONTRACT REPLACES WHAT THIS SEAT WROTE MINUTES EARLIER, AND ANDREW'S WORD IS WHY.** The first version read
`C-BACKFILL-DENOMINATOR-IS-THE-ESTATE'S-LIST` and said the folder list was *"the initial POOL, not the population"*,
with `K6` raised as a Rule-28 card because this seat could not state the population. **Andrew-direct 2026-09-24
~05:0xZ, VERBATIM, settles it:** *"Only when all of this is done for every single security in the Asset Management
research folder is the goal complete."* ⭐ **SO THE POPULATION IS THE FOLDER, IT IS 93, AND IT IS ALREADY MEASURED**
-- which makes `FWD-19` gradeable from day one instead of gated behind a card. `K6` is CLOSED by his word (A.6).
⛔ **THE CAUTION THE FIRST VERSION CARRIED IS STILL RIGHT ABOUT ONE THING AND IT SURVIVES:** 11 of the 93 (10
workbook-only, 1 empty) **can never carry prose-derived fields**, so a claim of "93 of 93 dossiers" would be false
by construction. **The grade is 93 of 93 DISPOSITIONED, never 93 of 93 populated** -- and the 11 are named in the
census with their reason, not silently dropped from the denominator.

## A.6 -- NEW MANIFEST ROWS AND THE ONE NEW Rule-28 CARD

| # | artifact | home | serves |
|---|---|---|---|
| R12 | the composed per-security dossier | `harvest / gold / research-dossier`, by security key, `as_of` in the object name | `FWD-10`..`FWD-13`, `FWD-15`..`FWD-17` |
| R13 | the induction act's read-back per name (resolved / refused-ambiguous / refused-absent) | consumes `AMGT_RESAPP`'s universe; writes no new surface | `FWD-19` |
| R14 | the estate-wide coverage census: covered securities, those carrying a dossier, those carrying none with a reason | `harvest / gold / research-backlog`, a new scan vintage beside the folder census | `FWD-14`, `FWD-19` |

| # | substrate | question | owner |
|---|---|---|---|
| ~~K6~~ | ~~the estate's covered-security list~~ | ⛔ **CLOSED BY ANDREW'S WORD ~05:0xZ BEFORE IT WAS EVER WORKED.** This seat raised it because it could not state `FWD-19`'s population; he stated it: *"every single security in the Asset Management research folder"*. **The population is the 93 folders**, already measured, so no cell is owed | ~~the backfill cell~~ -- nothing owed |

⭐ **K6 WAS A CORRECTLY-RAISED CARD AND IT WAS ANSWERED BY THE CHEAPEST POSSIBLE INSTRUMENT -- ASKING NOBODY.**
It was raised at ~05:00Z and closed at ~05:0xZ by a sentence Andrew was already writing. ⚠ **The useful lesson is
not that the card was wasted -- it is that the card's QUESTION was the right one and this seat's proposed ANSWER
(a wider estate-wide list) was wrong.** Had it been resolved by this seat's own reasoning instead of named as an
open question, `FWD-19` would now carry a population Andrew did not ask for, and the round would have built against
it. **Naming the uncertainty is what made his one sentence sufficient to close it.**

## A.7 -- WHAT THIS ADDENDUM DOES NOT DO

No page-architecture change (`C-PAGE-LAYOUT` untouched; Andrew: *"i wouldnt change AMGT_RESAPP page layout
architecturally"*). No Peers-tab source change (*"largely stays as it is"* -- the pack's own comparison set is a
cited dossier FIELD, not a second ranker). No `AMGT_HARVST` change. No second identity mechanism
(`C-IDENTITY-VIA-THE-LAYER` stands; this project adds none). No notifier and no schedule -- the rebuild is a run a
person starts. No bronze at serve (`C-NO-RAW-BRONZE-AT-SERVE` stands; only the gold dossier of cited passages is
servable). No fourth project. **And no Model-block figure pull** (A.4 limit 3).

⚠ **ONE CROSS-PROJECT OWNERSHIP FACT, STATED RATHER THAN RESOLVED HERE:** the brief puts the induction ACT in
`AMGT_RESAPP` (`:197`, *"the act is `AMGT_RESAPP`'s"*), while `FWD-19` is an `AMGT_CORPUS` outcome. **That is the
same shape v0.3 corrected on `FWD-4`, where this project's outcome required writing another project's surface.**
R13 above is written so it CONSUMES the universe and writes no new surface, which keeps the boundary; **whether the
induction RUN is executed by `2.0.0_SA_COO~X` or by the Served Runtime lane is an L5 question for the two seats,
and it is named here so it is not discovered mid-round.**

## A.8 -- L4-R

Both halves re-open: ADDENDUM A changes the ENDPOINT (new outcomes) and the CONTRACTS (A.4, A.5), so the RATIFIED
half is re-owed to `3.0.0_SA_CVO~Z`; and it rests on a new L1 brief, so the BRIEF half is re-owed to
`4.0.0_SA_CRO~Z`, with `4.0.0_SA_CRO~Y` named as the brief's author for consultation. ⚠ **PER R-10, ANDREW
SUSPENDED THE L4-R SIGNATURE AS A BAR FOR AMGT -- THE REVIEW IS KEPT, THE RITUAL IS NOT** -- so the halves are
routed and a round is not held hostage to a stamp. `FWD-1`..`FWD-9`, R1..R11 and every contract but
`C-NO-VENDOR-CALL` are unchanged, so nothing already signed is re-opened by this addendum.
