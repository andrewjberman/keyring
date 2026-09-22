# AMGT_CORPUS -- PRD (L4)

```json
{
  "project": "AMGT_CORPUS",
  "directive": "D5",
  "fabric": "site-z",
  "prd_version": "v0.1",
  "step": 4,
  "brief_ref": "docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md@42c05cd8a8",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8",
    "FWD-9"
  ],
  "status": "RATIFIED"
}
```

**author** `1.0.0_SA_CTO~Z` (L2 endpoint and L4 PRD). **driver** UNSEATED -- a third Tier-2 COO lane is asked of
`0.0.0_AB_MSTR~Z` at the L4->L5 handoff and never before.

| | |
|---|---|
| **Directive** | D5 Asset Management (placement SITEZ) |
| **Macro** | `AMGT` |
| **L1 brief** | `4.0.0_SA_CRO~F`, `docs/briefs/amgt-resapp-claude-analysis-layer-brief-20260922.md` @`42c05cd8a8`. **SHARED with the `AMGT_RESAPP` addendum and deliberately not copied into this tree** -- one brief, two consumers; a copy would age separately from its original |
| **Andrew's words** | the split and the name: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_182xZ_AMGT_CORPUS_SPLIT_BLOOMBERG_TO_CLAUDE_ALLOWED_LEAD_PANEL_DETERMINISTIC.md`; the population: `..._183xZ_RESEARCH_FOLDERS_ARE_THE_BACKFILL_BASIS_AND_INITIAL_POOL.md`; the design and the memo, verbatim at `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260922_17xxZ_CLAUDE_ANALYSIS_LAYER_PLATINUM_DESIGN.md` and `ANDREW_VOICE_MEMO_20260922_HARVEST_INFRA_OVERVIEW_TRANSCRIPT.md` |
| **Siblings** | `AMGT_RESAPP` (the page, the analysis producer, the report object, the export -- consumes this project's artifacts); `AMGT_HARVST` (the publication channels -- neither consumes nor is consumed by this project) |
| **L3** | registered @`7cedd1fd9d` |

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

  FWD-4  A resolved name that the harvest universe does not carry is inducted,
         on demand, one name at a time
         DONE WHEN  EXERCISED -- for one resolved backlog name absent from the
                    universe, a single deliberate act adds it and the universe
                    read-back shows it; the act prints what it will add BEFORE
                    it adds it, and refuses a name whose identity is ambiguous
         ACCEPT     Closing the gap between "we wrote this up" and "the page
                    knows about it" is one command per name, not a project.
         SOURCE     brief O13, Part V row 2; the Lenovo trial's induction shape

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

```

**Rule 24 record for this endpoint.** Axis: what an analyst or a consumer can DO that they cannot do today. Grain: one
capability. Intent: one (the corpus becomes usable substrate). MECE by SUBTRACTION over the brief's thirteen outcomes,
not by recall: O1, O3, O6, O7, O10, O11, O12 are the ADDENDUM's (they write or serve the report); O2 splits -- its
measured half is FWD-5 here, its delta-writing half is the addendum's; O4 splits -- the TEMPLATES are FWD-6/FWD-7 here,
the page's rendering of them is the addendum's; O5 splits -- ingestion and reachability are FWD-1/FWD-2/FWD-8 here, the
message that carries the prior report is the addendum's; O8's input-hash half is FWD-8 here; O9 is the addendum's
(report versioning); O13 is FWD-3/FWD-4 here. FWD-9 is NOT in the brief's outcome list: it is a property Part II states
as a constraint, and it is minted as an outcome because a constraint nobody exercises is a belief. **13 brief outcomes
-> 7 wholly the addendum's, 4 split, 2 wholly here, plus 1 minted = 9 FWD.**

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
is SILVER; the continuation artifacts, sector templates, fund forms and typecast are GOLD (JSON), because they are
firm-attributable derived judgments about the firm's own research. The PLATINUM report object is the addendum's and is
NOT written here.

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
| R12 | the lifted equity-research skill artifact, the message design and the cost card | repo documents under this project's home | (method; feeds the addendum) |

---

## WHAT MUST BE MEASURED BEFORE A CELL (Rule 28 cards)

| # | substrate | question | owner |
|---|---|---|---|
| K1 | the library on THIS device | its derived root; the folder and file counts at cell time versus the scan's 93 / 351; whether the sync is complete or partial, and how a partial sync is distinguishable from a small library | the ingestion cell |
| K2 | the identity layer | what fraction of the 93 folder names resolve through the existing crosswalk, and what the ambiguous ones look like -- the denominator decides whether FWD-3 needs a human pass | the backlog cell |
| K3 | the PDF-only reports | 184 PDFs against 71 Word files: whether the PDF text is extractable to the same skeleton, since the scan's term census read the Word files only | the extraction cell |
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
