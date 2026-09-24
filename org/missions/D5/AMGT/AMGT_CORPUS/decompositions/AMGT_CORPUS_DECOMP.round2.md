# AMGT_CORPUS -- L5 decomposition (COO) -- v2.0 (round 2: ADDENDUM A, the enrichment list)

**Seat:** `2.0.0_SA_COO~X`. **Cut:** 2026-09-24 ~06:5xZ at CLOUD HEAD (see the L5 commit). **Spec:** PRD v0.6 @`031c3a3a3e`
(ADDENDUM A cut at v0.5 @`1ffb156ecd`; v0.6 is a header-only bump plus the three contract headings re-named CONTRACTS),
both L4-R halves SIGNED current (`prd-signoff.py status` at the cut: ratified-text `3.0.0_SA_CVO~Z`, brief `4.0.0_SA_CRO~Z`
@`9b17fd5d49`; per R-10 the signature is not a bar for AMGT and this round is not held on it). **Analysis:** the CTO's
round-1 analysis @`031c3a3a3e` (`org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_CORPUS_ROUND1_ANALYSIS_20260924.md`), on
`3.0.0_SA_CVO~Z`'s slug (`ADJUDICATION_v4` @`96cbb2908d`). **Round 1** is terminal at `b4a8638eeb` (11 of 11, decomposition
v1.0 @`3c09ae6ce8` spent) and nothing in it re-opens. Round 1's file is kept beside this one, unchanged.

**Andrew's word this round rests on (verbatim, R-26 / ADDENDUM A):** *"spec out a new analysis that can be handed off
to new rounds for development on AMGT_CORPUS (Not only do we need the incorporated layers from the corpus however we
decided to do that i.e. using your dossier addendum we also need backfill for all the asset management securities)"*,
and the completion test: *"Only when all of this is done for every single security in the Asset Management research
folder is the goal complete."*

## 0. What this round IS, by subtraction from the analysis's enrichment list

The CTO's list (analysis s.6), item by item, and where each lands:

| # | item | disposition here |
|---|---|---|
| A | ADDENDUM A itself: FWD-10..FWD-18 (the fold) and FWD-19 (the backfill) | **THE RECTANGLE** -- cells d-1..d-5 |
| 1 | a control for the exempting branch at `readonly_proof.py:301` | **CELL d-6** (one instrument-repair cell for the round, per the diet) |
| 2 | the H re-review of the scanner (Z-S9's "NOT_EVALUATED") | **CLOSED BY EVIDENCE, no cell** -- row `AMGT_CORPUS-Z-S12` @`7f4a9d8c4e`: `2.0.0_SA_COO~Y` DID re-review at `1c877a8c87` (2026-09-23 18:07Z, after Z-S9 was filed) and PASSED all ten scanner controls; the bytes are in CLOUD since `b4a8638eeb`. A review is a reviewer's act, never a worker cell; the next L9 may adjudicate Z-S7..S9 on Z-S12. If the CTO overturns, it is one cell added, not a recut. |
| 3 | Z-S6's period ordering | **CLOSED BY EVIDENCE, no cell** -- same row: the typed.py fix landed at `d382f2a30e`, H's all-pairs validator PASSED 5,040 permutations at `1c877a8c87`, and the bytes are in CLOUD. |
| 4 | a contract-half guard on `prd_signoff_lib.py` | **NOT THIS PROJECT'S** -- the defect and the tool are `1.0.0_SA_CTO~Z`'s (analysis s.3), and the spine forbids one project's loop writing into another surface's fix. Routed back to the CTO with this seat's recommendation (`.tools` is lane ANY, so a cell COULD write it; the reason it is not cut here is ownership of the mechanism, not permission). |
| 5 | the router-driving fix for the reactive arm | **NOT THIS PROJECT'S** -- an `AMGT_RESAPP` Peers artifact (analysis s.4, the PNG filed under CAT while the panel shows BA). Routed to `2.0.0_SA_COO~Z`'s round via the CTO. |

**FOUR rows the analysis says stay ARMED (Z-S6..S9) are disarmed by their owner in Z-S12 on the evidence above.** The
analysis was written at 06:19Z and the disarm row landed at 06:22Z; neither seat had the other's text. This file does
not convert the disarm into a grade -- that is the CVO's L9 -- and cuts no cell for a hazard whose fix is in HEAD.

---

## 1. The rectangle -- six cells over the round's items, `CRPS-d-<n>`

**THE INVARIANT:** every cell mirrors exactly one item of s.0's rectangle and names the manifest row it enriches or
mints; every new manifest row (R12, R13, R14) has exactly one cell. Measured at this cut: 6 cells over 6 items; R12, R13,
R14 each mirrored once; R2, R6, R11 each enriched once. No cell touches R1, R3, R4, R5, R7, R8, R9, R10.

**CELL-ID CONFORMANCE, MEASURED** (`org/standards/DECOMP_CELL_ID_CONVENTION.md` SHAPE 1, `CELL_ID_RE` `fullmatch`): 6 of 6
ids match; the axis letter `d` is the round-2 axis (round 1 was `c`), so no round-2 id collides with a round-1 id.

**CELL STATUS VOCABULARY** (from v1.0 s.1): `NOT-EVALUATED | OPEN | IN-FLIGHT | HELD | COMPLETE | CLOSED`. Every cell at
this cut is `OPEN` (6 of 6 evaluated).

**CODE HOME:** `lib/research/corpus/` (exists; 15 modules + 15 tests at HEAD). Every cell owns its own module(s) and
test file(s); the two cells that EDIT an existing module (d-1 extract.py, d-2 continuation.py, d-6 readonly_proof.py)
are on different chains or different files, so no two cells edit one file at once.

| cell | row | outcome | act (the engine, and what binds it) | state | chain |
|---|---|---|---|---|---|
| `CRPS-d-1` | R2 (enriched: method 2) | FWD-16; upstream of FWD-10..13 | **EXTRACTION METHOD 2 -- THE INLINE-LEAD SECTION RULE.** `extract.py` gains, for PDF, per-line spans (`lead_prefix` = the concatenated leading BOLD spans, `bold_all`, `bold_first`, `n_spans`) and a `section_leads` list beside `headings`: a section opens on a standalone heading OR on a line whose leading bold spans, colon-trimmed and upper-cased, are a name in the SKELETON name set (the 2026-09-22 scan's names plus the PFOE set measured 2026-09-24: COMPANY DESCRIPTION, LONG-TERM GROWTH ALGORITHM [AND EXPECTED RETURN], OWNERSHIP, SPECIAL ITEMS, WHY WE OWN, POSITIVES, NEGATIVES, CHANGES IN ANALYST SENTIMENT, INVESTMENT CONSIDERATIONS, OPPOSING VIEW, HEADWINDS AND RISKS, MANAGEMENT AND CAPITAL ALLOCATION; a trailing colon never matters; `RISKS AND CONSDIERATIONS` -- the team's typo -- is in the set; VALUATION is NOT a section name). `METHOD_VERSION_2 = "amgt-corpus-extract/2"`. **V2 objects land BESIDE v1, never over it:** object name `<report_id>/extract.v2.json` under the same `research-report-extract` partition, through the ONE bronze writer (`store.bronze_put`, conditional put; existed/put_performed printed). Run over EVERY retained bronze report (denominator printed: N of 123 at the cut; N of whatever the store holds at run time). DOCX extraction is unchanged in substance: v2's docx `paragraphs`/`headings`/`tables` equal v1's for every docx (the CONTROL), v2 adds `section_leads` for docx too (a heading paragraph whose colon-trimmed upper text is a section name). Grounded on `4.0.0_SA_CRO~Y`'s instrument `measure_pdf_extractability.py` @`6ae4cb0c93` (`pdf_lines`, `section_name_of`, `is_section_heading`, `block_after`), which the cell REUSES by porting its rules, not by importing a deliverables script. | OPEN | A1 |
| `CRPS-d-2` | R6 (enriched: the PDF branch) | FWD-16, FWD-10 (corpus half) | **THE PDF PILLAR BRANCH, DOCX KEPT AS THE CONTROL.** `continuation.py`'s RULED "docx only" pillar rule gains a PDF branch over a v2 extraction: the block is the lines after the INVESTMENT THESIS section lead up to the next section lead; a pillar starts at a line whose leading bold spans end at a colon (`<Lead>: <body>`) OR an all-bold line ending in ':' OR a line ending in ':' whose text equals its bold prefix (the PFOE shape, CDNS's second pillar); a known section name is never a pillar; the body is the non-bold remainder plus following non-lead lines. The docx branch is byte-unchanged and remains the positive control (17 FULL of 19 same-stem pairs, 99 of 99 pillars, measured by the CRO). The continuation also gains `thesis_summary` (the inline `INVESTMENT THESIS: <sentence>` remainder, PFOE shape; '' for the Word shape) as a CITED field. **Extraction resolution:** `_read_reports_with_bytes` prefers `<report_id>/extract.v2.json` when it exists beside the typed row's `extract_key`, else v1 -- the typed silver rows are NOT rewritten (R3 is append-only and untouched); the v2 key enters `inputs`, so every name's continuation rebuilds into a NEW object beside the old (`C-INPUT-HASHED`; never overwrite). `--verify-citations` re-resolves every citation of every stored object (denominator printed, was 2,280 of 2,280). | OPEN | A2 (after d-1) |
| `CRPS-d-3` | **R12 (new)** | FWD-10, FWD-11, FWD-12 (labels/order + cases), FWD-13, FWD-15, FWD-17 (the store half) | **THE COMPOSED DOSSIER (gold `research-dossier`).** New module `dossier.py`: per resolved security, ONE document composed -- never authored -- from the continuation artifact (pillars, thesis_summary, kpi_set, fund_of_record, last_stated_position), the sector template for its business type, the fund form, the typecast, and the v2 extraction of its most recent class A pack and most recent class B update for the SECTIONS: `recommendation` (line, <=160 chars), `company_description`, `growth_algorithm`, `investment_thesis_summary`, `risks` (with `pre_mortem` first where present), `ownership`, `management` (MANAGEMENT / BOARD or MANAGEMENT AND CAPITAL ALLOCATION), `special_items`, `cases` (UPSIDE / BASE / DOWNSIDE, each block), `why_we_own`, `positives`, `negatives`, `comparison_set` (COMMON STOCK COMPARISON, as a cited field, never a second ranker). EVERY field is `{value, citation: {report_id, bronze_key, locator, passage}}` or `{value: null, absent: <reason a person can read>}` (`C-CITED-OR-ABSENT`; `C-DOSSIER-IS-COMPOSED-NEVER-AUTHORED`: no synthesis across reports, no paraphrase). `inputs` = every input object's `{key, sha256}` (`C-INPUT-HASHED`). **Address and name are builder output, never typed:** `lib/opal_naming.address(...)` for `harvest / gold / research-dossier / security_key=<KEY>`; object name `as_of=<YYYY-MM-DD>.<inputs_sha16>.json` (`C-DOSSIER-DATE-IN-THE-OBJECT-NAME`; the builder refuses a two-level partition); spelling `research-dossier` (`C-DOSSIER-TABLE-SPELLING`). Through `gold.gold_put` (never overwrite). **A rebuild with unchanged inputs writes NOTHING and prints `unchanged inputs_sha16 <x> wrote 0`** (`C-DOSSIER-REBUILD-IS-A-NO-OP-ON-UNCHANGED-INPUTS`). `read_dossier(security_key, client=...)` returns the newest `as_of` for the key with its hashes; `--census` prints, over every stored dossier, `fields_scanned N cited C absent_with_reason A neither 0` -- FWD-13's own denominator -- and a NEGATIVE CONTROL: a deliberately uncitable field (a planted section name no report carries) renders ABSENT with its reason, never blank. `DOSSIER_INTERFACE.md` in this lane's deliverables prints the dossier's field list SIDE BY SIDE with `ThesisBundle`'s slots (`portal/src/pages/SecurityAnalysis/types.ts:955`: `drafted_sections` ids `company_description / investment_thesis / risks / ceo_bio / recommendation`, `management`, `model_cases`, `posture`) and names the intersection -- the render half is `AMGT_RESAPP`'s (s.9). | OPEN | A3 (after d-1, d-2) |
| `CRPS-d-4` | **R14 (new)** | FWD-14, FWD-19 (the census) | **THE COVERAGE CENSUS, 93 OF 93 DISPOSITIONED.** `backlog.py --coverage` (a new scan vintage at `research-backlog`, beside the folder census, through `gold.gold_put`): the folder list read FRESH from the library (never a transcribed list), and for EVERY folder exactly one disposition: `dossier-served` (a `research-dossier` object exists for its security key and `read_dossier` returns it), `resolved-but-no-prose` (resolved, with the reason: workbook-only / empty / PDF unreadable to the skeleton), `unresolved-with-reason` (the crosswalk's own reason: ambiguous AXMB/AMXB, no evidence, refused). **The three counts SUM TO THE FOLDER COUNT, printed every run** (`C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER`; `C-FOLDER-LIST-IS-THE-DENOMINATOR`), and the 11 that can never carry prose (10 workbook-only, 1 empty at the cut -- re-measured, not copied) are NAMED with their reason. `--folder "<name>"` returns that folder's dossier or the printed reason there is none (FWD-14). No library write (lists only; `C-CORPUS-READ-ONLY`). | OPEN | A4 (after d-3 AND d-5) |
| `CRPS-d-5` | **R13 (new)** | FWD-19 (the induction) | **THE SCRIPTED INDUCTION PRODUCER -- BUILT AND DRY-EXERCISED HERE, FIRED AT THE DRAIN.** New module `induction_run.py`: rebuilds the induction request FRESH (`induction_request.build_request` over the current backlog: 60 unresolved at the cut), and for every row in state EVIDENCED calls `lib.research.identity.add_security.main(["--folder", <folder>, "--as-of", <today UTC>, "--write-pool"])` EXACTLY ONCE (add_security is itself idempotent: an already-registered folder makes no call and prints so); every row NOT evidenced (AMBIGUOUS -- America Movil AXMB/AMXB stays REFUSED with its reason; no-evidence; refused) is PRINTED with its reason and NEVER called (the word authorizes the CALLS, not a PICK). Per-row read-back `{folder, state, security_key | reason, bloomberg_calls}` and totals `evidenced E called C registered R refused F unresolved U -- sums to 60` (denominator printed). `--dry-run` runs the whole loop against an INJECTED fake blp client (the test poison: the real `_load_blp_client`, boto3, subprocess and sockets all RAISE, positive-controlled) and prints the identical read-back shape with `bloomberg_calls 0`. **`--fire` is refused inside a test and inside a worker turn** (it requires `OPAL_INDUCTION_FIRE=1` AND an operator-named as-of); the FIRE is the ISSUER's drain act on this terminal under R-16 V2 / `C-NO-VENDOR-CALL` v0.5 / R-21 (s.9). `add_security` is `2.0.0_SA_COO~Z`'s surface: this cell IMPORTS it and edits nothing under `lib/research/identity/`. | OPEN | B1 |
| `CRPS-d-6` | R11 (enriched: the exempting branch) | FWD-9 | **A CONTROL FOR THE BRANCH THAT EXEMPTS.** `readonly_proof.py:301` reads `reaches = LIBRARY in origins or (not is_test and UNKNOWN in origins)`: fail-closed for library code, fail-OPEN for test files, and 17 of 27 flagged sites at HEAD land on the exempting branch with origins `['unknown']` while the positive control plants into a NON-test file and so never exercises it (CTO analysis s.2; CVO row `Z-C-S4`). The cell does both things the analysis names: (a) a SECOND positive control that plants `open(library_root() / "x", "w")` inside a file named `test_plant_control.py` under a temp `tests/` dir and REQUIRES it flagged (`positive_control_test_file flagged 1`); (b) the exemption JUSTIFIED BY MEASUREMENT, not by default: a new origin class `tmp-fixture` for targets rooted in pytest's `tmp_path`/`tmpdir` (directly or through a local binding), so the 17 sites resolve to `['tmp-fixture']` and are exempt BECAUSE they are measured fixture writes; a test-site write whose origin is genuinely `unknown` COUNTS (`test_unknown_sites 0` at HEAD is a measurement, and a planted `open(compute(), "w")` in a test file flips it to 1 -- the difference control). `library_write_calls 0` and `positive_control flagged 1` unchanged. Fits in `tail -40` (the c-11 lesson: the census prints its totals FIRST and LAST). | OPEN | C1 |

---

## 1a. Re-groundings performed at L5 (CLOUD HEAD at the cut)

- **The store, live (`research-continuation/security_key=IMB_LN_Equity/`):** one object `ba32af5b2d065474.json` (read 03:3xZ). The
  gold tier under `amgt/harvest/gold/` carries 5 of 5 `research-*` tables hyphenated (CTO A.5) -- the spelling ruling is
  exercised on the live plane, not re-derived here.
- **The builder:** `lib.opal_naming.address()` takes a `source` argument this seat's first probe omitted (a `TypeError`, not
  a refusal); the CTO exercised the two-level-partition REFUSAL at A.5. Cell d-3 prints the builder's own output and the
  refusal message in its proof; a worker never types the address.
- **Extraction v1 objects** are immutable at `<report_id>/extract.json` (`extract.py:493`, conditional put). A v2 that
  changed those bytes would be refused by the writer -- which is why d-1 lands v2 BESIDE v1 and why d-2 resolves v2 by
  key substitution rather than by rewriting silver.
- **`add_security`** (`lib/research/identity/add_security.py`): ONE `reference_data` call per name; idempotent on
  `registrations.json`; `--write-pool` refuses any `--as-of` that is not today (UTC); `--dry-run` still CALLS Bloomberg
  (the record is shown "from the in-memory response") -- so a worker's dry exercise must inject a fake client, never pass
  `--dry-run` to the real module. `_load_blp_client` is the seam the poison replaces.
- **The library on this device:** 93 folders / 351 files at the CRO's 2026-09-24 ~02:5xZ census (46 docx+pdf, 30 pdf-only,
  6 docx-only, 10 workbook-only, 1 empty); 157 top-level PDFs read with 0 read failures. Every cell that lists it lists
  only; nothing under it is opened for writing (`C-CORPUS-READ-ONLY`, proven by R11 and re-proven by d-6's census).
- **PDF-only resolved names for the seam probes** are chosen by the worker at run time by a stated deterministic rule
  (first resolved security key, sorted, whose most recent class A report is a PDF), never hard-coded here.
- **Open orders held by this lane:** 0 (`to-check.py --all --assignee`; the single `[OPEN]` hit is a DS lane's order
  naming `~X` in prose). LD-0521's refuser sees 0 non-terminal on this project (round 1 is 11 of 11 complete).

---

## 2. Rule 24 four-postulate record, for what this file ADDS

**(i) MECE over a declared domain -- by subtraction.** Domain = the analysis's enrichment list (5 items) + ADDENDUM A's ten
outcomes. Enrichment: 1 cell (d-6) + 2 closed-by-evidence + 2 routed = 5 of 5. Outcomes: FWD-10 (d-2 store half + d-3),
FWD-11 (d-3 `management`), FWD-12 (d-3 typecast/template rows + `cases`; the 22 added mnemonics' FIGURES wait on V3 and
read ABSENT-with-reason, which is FWD-13 working), FWD-13 (d-3 `--census` + negative control), FWD-14 (d-4 `--folder`),
FWD-15 (d-3 `fund_of_record` + `last_stated_position` as cited inputs; the machine posture untouched), FWD-16 (d-1 + d-2),
FWD-17 (d-3 no-op-on-unchanged + new object beside old; the "new report lands" half is R1's existing ingest, re-run at
the drain), FWD-18 (**DEFERRED** by this round on the analysis's own permission -- marked PROPOSAL and LATER by its author;
cut LAST means not this round; it re-enters via the round-2 analysis), FWD-19 (d-5 + d-4 + the drain sequence). 10 of 10
outcomes dispositioned: 9 served, 1 deferred with its authority named. **The RENDER halves of FWD-10/11/12/15 -- the tab
showing the field -- are `AMGT_RESAPP`'s** (A.7: no page-architecture change here; the bundle adapter and the tabs are
`2.0.0_SA_COO~Z`'s surfaces); this round delivers the store, the reader and the interface sheet, and s.9 names the hold.
**(ii) SAME GRAIN:** every cell is one producer or one instrument over one manifest row.
**(iii) INTENT COHERENCE:** one axis, DATA dependency (what a cell reads that another writes); the chain letters order by
it and by nothing else.
**(iv) STATE COHERENCE:** a cell's terminal proof-of-spec moves that cell to COMPLETE and nothing else; the FWD grades
move only at L9/L10; the four ARMED rows moved at Z-S12 and this file does not move them again.

---

## 2b. Battery disposition per lens

### `comp-schedule --drift` -- RUN
```
REACHED-DENOMINATORS: C1=23; C2=5; C3=12; C4=21; C5=334
GATES ARMED: 2 [--drift]   G-3 (owner CTO, INF silver)   G-7 (owner POD4, black_diamond gold_dispatch)
```
Neither names a harvest, research or corpus surface. Open deploy-ledger entries: 5 in the shared tree (C2), the AMGT one
being `amgt-h03-leadpanel-y-20260924` (H03 2a, `AMGT_HARVST`'s, an AE apply) -- not a surface any cell here writes.
**BLINDNESS, STATED:** live worktrees other than the shared tree were NOT read for `.open_deploys/` (43 rows at the last
census); no cell here is a deploy, so no act depends on that read.

### `comp-iam` -- RUN
`comp-iam roles` was run at the round-1 cut (214 found, DESIRED plane, no vintage); this seat did NOT re-run it this cut
and says so. **BLINDNESS:** this box's own credential is not read by that lens either way; every writing cell (d-1, d-2,
d-3, d-4) measures it with its first real conditional PUT to its own new prefix and prints the outcome; a refusal is a
BLOCKING row. d-5's `--write-pool` path is `add_security`'s and is exercised only at the fire.

### `comp-adversary` -- RUN on this file; declaration at section 7.

### `comp-blast` -- DECLARED-NOT-APPLICABLE
No cell moves a served object. Every write is a NEW object: v2 extraction beside v1, new continuation/dossier objects
by inputs hash, a new backlog scan vintage. The served `opal-amgt-scoped-api` reads none of these until `AMGT_RESAPP`
integrates the interface (s.9).

---

## 2c. Bounds the battery added to cells -- carried into the L6 cut
- **Every cell:** no vendor API and no Claude API from a worker turn (`C-NO-VENDOR-CALL` v0.5's exception is the SCRIPTED
  producer at the fire, never a turn); no install; no notifier, no schedule (`C-NO-NOTIFIER`; A.7).
- **Every writing cell:** S3 writes ONLY under `opal-data-harvest`, ONLY at `address()` output, NEVER overwriting; a
  refused PUT is a BLOCKING row, never a hand-typed key. `research-dossier` is spelled with a hyphen.
- **Every reader of the library** (d-4 lists): lists only; no write, move, rename or delete under the root; the root is
  derived (`library.library_root()`), never typed.
- **Every test file:** offline, under `tests/conftest.py`'s poison (boto3 client construction, `subprocess.run`,
  `socket.create_connection` RAISE) with a positive control proving it bites; d-5 additionally poisons
  `add_security._load_blp_client` and proves the poison bites.
- **THE VERIFICATION DIET (spine v3.16-3.18):** a build order carries at most THREE mechanical criteria -- the built
  behaviour, the seam probe against its real neighbour (the STORE, read-only), and at most one more with a one-line
  reason -- plus a judgment criterion only where the outcome needs one. Repo-wide hygiene (the full corpus suite,
  `py_compile`, ruff, the hyg script) is NOT a criterion: the issuer runs it once per merge at the drain.
- **`tail -N` windows on every census invocation are sized to the output at the cut PLUS headroom, and every census
  prints its totals BOTH first and last** (the c-11 lesson, row Z-S10).

---

## 3. Placement axis

Every cell executes on **site-z** (this box): the store is reachable from here, the library copy is here, and the
Bloomberg terminal the fire needs is this device. No cell is placed on the laptop fabric.

---

## 4. Dependency edges, keyed to OBSERVED completion (a drained, VALID proof-of-spec instance), never a status word

```
  chain A:  CRPS-d-1 -> CRPS-d-2 -> CRPS-d-3 -> CRPS-d-4
  chain B:  CRPS-d-5 -> CRPS-d-4
  chain C:  CRPS-d-6
```
- d-2 reads d-1's v2 extraction objects; d-3 reads d-2's rebuilt continuation and d-1's sections; d-4 reads d-3's
  dossiers AND the post-induction crosswalk state d-5's fire produces (a census before the fire would count 60 unresolved
  as a fact about the world when it is a fact about the run order).
- d-6 touches only `readonly_proof.py` and its test; nothing reads it.
- **M = 3**, the widest antichain (d-1, d-5, d-6 can all be in flight at once from the start).

---

## 5. The round -- one issuance, fan-out as data

- **Round 2 covers all 6 cells in ONE issuance.** Three worker slots:
  - `~1` drains chain A in order (d-1, d-2, d-3, d-4). Continued, not respawned, so the extraction context carries into
    the composition and the census.
  - `~2` d-5, spawned at once.
  - `~3` d-6, spawned at once.
- Fan-out line for the issuance commit:
  `fanout: 3 of 3 chains, cap 8, reason: M is the widest antichain at the start; chain A is one continued worker; d-5 and d-6 are independent of it and of each other.`
- **Drain duties owed by this seat, not by a worker (in order):**
  1. When `d-5` drains VALID: send the pinned candidate to `2.0.0_SA_COO~Z` for ONE exchange (`add_security` is that
     lane's surface; the runner imports it). Then, under R-16 V2 / R-21 / `C-NO-VENDOR-CALL` v0.5 and
     `integrations/bloomberg/READ_HERE.md`, FIRE the producer ONCE on this terminal (`OPAL_INDUCTION_FIRE=1`, today's
     as-of), record the read-back (E called, R registered, F refused, U unresolved -- summing to 60) in this lane's
     deliverables, and re-run the existing ingest (`ingest.ingest`, idempotent, prints stored/existed/put_performed) so the
     newly resolved folders' files land in bronze. This is an issuer act because the spine names the FIRE a scripted
     producer under Andrew's word and a worker face carries NEVER CALL A VENDOR API.
  2. Before continuing `~1` onto `d-4`: merge `~2`'s drained branch into `~1`'s worktree branch, then run the scripted
     production sequence ONCE for the newly resolved names -- extraction v2 (d-1's `--run`), typed silver (c-3's
     `typed --run`), continuation (`continuation --write`), sector template / fund form / typecast (`--write` each),
     dossier (d-3's `--write`) -- each printing its denominators; every run is a producer this project already owns.
  3. At every merge: the full corpus suite, `py_compile`, ruff and the hyg census once, beside `safe-merge.sh`'s row gate.
  4. When `d-3` drains VALID: deliver `DOSSIER_INTERFACE.md` and the pinned `read_dossier` surface to `2.0.0_SA_COO~Z`
     as an interface publication (one message), so the render half can be cut in `AMGT_RESAPP`'s round.
- The surprise channel is `org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md`
  (seat rows to `Z-S12`). Workers mint `AMGT_CORPUS-Z-W<n>-S<k>`, `disarm_owner` `2.0.0_SA_COO~X`.

---

## 6. `<preflight>` -- what this decomposition actually ran
```
prd-signoff.py status AMGT_CORPUS        v0.6 @031c3a3a3e; ratified-text SIGNED current (3.0.0_SA_CVO~Z); brief SIGNED current @9b17fd5d49 (4.0.0_SA_CRO~Z); ADMITTED
sequence-check.py --project AMGT_CORPUS  not in SEQUENCE.yaml (not sequenced); 3 live COO lanes on this box (~X ~Y ~Z)
to-check.py --all --assignee 2.0.0_SA_COO~X   0 held (1 hit is a DS lane's order naming ~X in prose)
comp-schedule --drift                    2 armed, 0 on these surfaces (C1=23 C2=5 C3=12 C4=21 C5=334)
comp-iam roles                           NOT re-run this cut (round-1 read: 214 found, DESIRED plane); credential measured by each cell's first PUT
research-continuation IMB object         1 object live (ba32af5b2d065474.json), read 03:3xZ
task-order status census (anchored)      11 of 11 complete on this project -> LD-0521's refuser sees 0 open
proof-of-spec-check.py CELL_ID_RE        6 of 6 ids match
```

---

## 7. comp-adversary declaration

Recorded at the issuance commit (the tool reads committed citations). Declared blindness this file accepts in advance:
the tool's neighbourhood is filesystem adjacency; the cells' real neighbours are the store (`lib/research/harvest/store.py`,
`gold.py`), the identity layer (`add_security`, `crosswalk`), the CRO's PDF instrument in a deliverables folder, and the
portal's `ThesisBundle` type -- read directly in s.1a and cited by path in the cells.

---

## 8. Rulings this decomposition makes, and what it REFUSES to assume

**Rulings (L5's own, each stated so a reader can dispute it):**
1. **Extraction v2 lands BESIDE v1 and silver is not rewritten.** The bronze writer refuses a changed byte at an existing
   key; R3's typed rows are append-only. So v2 is a new object per report and readers resolve it by key substitution.
   Reported to the CTO in the drain-end read as a manifest-argument reconciliation (R2's "same partition" now holds two
   method versions), not a defect.
2. **The dossier's SECTIONS are read from the v2 extraction of the two most recent reports (class A pack, class B update),
   not synthesised across the corpus.** `C-DOSSIER-IS-COMPOSED-NEVER-AUTHORED` admits composition of existing artifacts
   and cited passages; a section from a third report is a later enrichment, not this round's.
3. **FWD-18 is deferred** on the analysis's and the addendum's own words ("cut LAST, deferrable by the round-N analysis
   without re-opening anything").
4. **The FIRE is the issuer's drain act, not a worker's criterion.** A worker face carries the vendor ban; Andrew's word
   authorises a scripted producer; the seat that holds both the word and the terminal runs it once and records it.
5. **Items 4 and 5 of the enrichment list are routed, not cut** (s.0). One project's loop never writes another's fix.
6. **The render half of FWD-10/11/12/15 is a hold, not a cell** (s.9). This project cannot grade "renders on the Thesis
   tab" from its own surfaces; it delivers the store, the reader and the side-by-side interface, and `AMGT_RESAPP`'s
   round grades the screen.

**What this decomposition REFUSES to assume:**
- That the 30 PDF-only folders all yield pillars: the CRO measured 26 of 30 with a full pack and 29 of 30 with pillars
  or "Why we own"; d-2 prints its own count against the resolved PDF-only names and names each miss with its reason.
- That the 60 unresolved folders all induct: E evidenced of 60 is measured at the fire; the refused and the ambiguous are
  printed, and 93 of 93 DISPOSITIONED -- never "populated" -- is the grade.
- That this box can write the new prefixes: each writing cell measures it with a real conditional PUT.
- That a test-site write is safe because it is in a test: d-6 measures its origin or counts it.
- That the render half will follow automatically: it is a named hold with an owner (s.9).

---

## 9. Holds, and whose they are

| hold | on | owner | what lifts it |
|---|---|---|---|
| the FIRE of d-5's producer (60 names, one `reference_data` call each) | this lane's drain, on this terminal | `2.0.0_SA_COO~X`, after ONE exchange with `2.0.0_SA_COO~Z` on the pinned candidate (add_security is its surface) | d-5 drained VALID; the exchange returned; READ_HERE s.2 sign-in state OK; then the fire is taken and recorded -- NOT a wait on any seat's silence |
| the RENDER half of FWD-10, 11, 12, 15 (the tabs showing the dossier fields) | `AMGT_RESAPP`'s surfaces (`scoped_amgt.py` bundle adapter, `portal/src/pages/SecurityAnalysis/**`) | `2.0.0_SA_COO~Z` via `1.0.0_SA_CTO~Z` (the RESAPP round) | d-3's `DOSSIER_INTERFACE.md` + pinned `read_dossier` delivered as an interface publication; the RESAPP round cuts the adapter/tab cells; graded there |
| FWD-12's FIGURES for the 22 added mnemonics | Bloomberg (R-16 V3) | Andrew, per-use word | his word; until then the rows read ABSENT-with-reason (FWD-13 working) |
| FWD-18 | this project, a later round | `1.0.0_SA_CTO~Z` (the round-2 analysis) | the analysis re-lists it |
| enrichment items 4 (contract-half guard) and 5 (router-driving fix) | `.tools/prd_signoff_lib.py` / `AMGT_RESAPP` Peers | `1.0.0_SA_CTO~Z` / `2.0.0_SA_COO~Z` | routed with this seat's recommendation in the L5 message; not this project's cells |

-- `2.0.0_SA_COO~X`
