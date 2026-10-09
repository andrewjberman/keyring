# AMGT_CORPUS -- L5 decomposition v40.0 -- ROUND 40 (FWD-14's printed line; three page builds and a row label; the Z-S89 extraction; six dispersion mnemonics; the DEV drive; FWD-12's sheet census)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-07 ~14:3xZ.

**Source:** `1.0.0_SA_CTO~Z` round-39 analysis `ledger/ROUND_ANALYSIS.round39.md` @`5ccdc90368` s.4 and ADDENDUM 1 (msgs 30972,
30980, 31011, all READ-acked), and its ruling msg 31013 on ruling 3 (the row label is a PAGE cell; the served class token stays).
PRD v0.8, both L4-R halves SIGNED; no ENDPOINT change this round. The rectangle is the analysis's six items. Round 39's
decomposition is kept as `AMGT_CORPUS_DECOMP.round39.md`. Base: CLOUD HEAD at the cut; portal origin/DEV `ba391aff`.

## 0. What this round IS

| # | item (analysis s.4) | cell | path | risk |
|---|---|---|---|---|
| 1 | FWD-14's printed line: four named counts and their sum, non-zero exit when the sum is not the folder count (ruling 1) | `CRPS-ap-1` | worker `0.9.0_WK_AMGT_CORPUS~1` (worker-light, direct act) | LOCAL |
| 2a | FWD-10: a team pillar opens to its report and passage (ruling 7) | `CRPS-ap-2` | worker `~4` | LOCAL (portal DEV candidate, CTO render review) |
| 2b | FWD-15: the team's fund of record and last stated position read cited on the header (ruling 7) | `CRPS-ap-3` | worker `~5` | LOCAL (portal DEV candidate, CTO render review) |
| 2c | FWD-18: the header feed filters to a pillar's terms (ruling 7) | `CRPS-ap-4` | worker `~5`, queued after ap-3 (the mount line is in ap-3's file) | LOCAL (portal DEV candidate, CTO render review) |
| 2d | FWD-20: a zero-dominated row's unit reads in plain words (ruling 3, as settled by msg 31013) | `CRPS-ap-5` | worker `~4`, queued after ap-2 (worker-light, direct act) | LOCAL (portal DEV candidate, CTO render review) |
| 3 | `Z-S89`: a section value that is only its own heading is not a passage; a census of short served passages (ruling 9) | `CRPS-ap-6` | worker `~2` | LOCAL |
| 4 | The six consensus-dispersion mnemonics ride the model-block pull, calls per fire stated against 768 (ruling 10) | `CRPS-ap-7` | worker `~3` | LOCAL |
| 5 | ONE read-only drive on DEV after the page cells land: the rendered-rows census (ruling 2), the no-forecast read (4), the FWD-11 walk on a name with a team passage AND a filing roster (5), the FWD-16 comparison extended to pillars and management (6), and the round's one real run of ap-2..ap-5 | `CRPS-ap-8` | the issuer's read; walker slot from `0.0.0_AB_MSTR~Z` | LOCAL (read) |
| 6 | FWD-12: the census of which sheet (`Model` or `Model NEW VERSION`) carries each covered name's figures, both counts printed, then the row comparison against each name's OWN workbook (ADDENDUM 1 rulings 1 and 2) | `CRPS-ap-9` | the issuer's read, through the Opal gateway's SharePoint read (a worker holds no gateway tool) | LOCAL (read) |
| 3s, 4s | The SERVED halves of items 3 and 4: the short-passage census on the served dossiers and the dossier re-write that ap-6 changes; the one-name scripted probe of the six mnemonics and the re-pin of `amgt-induction-daily` to ap-7's drain | `CRPS-ap-10` | the issuer's paired acts (one never-widen pair per act, to `1.0.0_SA_CTO~Z`), after ap-6 and ap-7 drain | SERVED |

**Chains (M = 5 worker chains):**
- `ap-1` (no edge);
- `ap-6 -> ap-10` (the dossier half);
- `ap-7 -> ap-10` (the pull half);
- `ap-2 -> ap-5 -> ap-8` (one worker's queue: two tab files, one portal branch; ap-8 walks the landed page);
- `ap-3 -> ap-4 -> ap-8` (one worker's queue: ap-4's mount line is in ap-3's file);
- `ap-9` (no edge; the issuer's).

`fanout: 5 of 5 worker chains, cap 8`. Slots: `~1` ap-1; `~2` ap-6; `~3` ap-7; `~4` ap-2 then ap-5 by continuation; `~5` ap-3
then ap-4 by continuation. The issuer runs ap-8, ap-9 and ap-10.

**Write sets (disjoint; census at the cut over 2,285 task-order files on every project: 118 name one of these files in
`<paths>`, 0 of them non-terminal):**
- ap-1: `lib/research/corpus/backlog.py`, `lib/research/corpus/tests/test_backlog_fence14.py`;
- ap-6: `lib/research/corpus/dossier.py`, three dossier test files (one new);
- ap-7: `integrations/bloomberg/research/model_block_pull.py`, `build_unit_map.py`, seven test files (one new);
- ap-2: `portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx`;
- ap-5: `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` (`rowUnitWords` only);
- ap-3: `portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx` (`DossierPositionLine` only);
- ap-4: `portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx`, and ONE mount line in `SecurityOverlay.tsx`.

No cell edits `types.ts` or a `__harness__/` file. DSGN_AMGTV1 (`2.0.0_SA_COO~D`) maintains this page's design; told at the cut.
Portal worktrees take their dependencies by link, never by install (`1.0.0_SA_CTO~Z` interim rule, msg 30907).

## 1. The cells

**CRPS-ap-1.** `_print_fence14_line` (`backlog.py:458-480`) sums three classes and prints the fourth beside the sum:
`sum 96 outside-fence 1` against 97 folders. The line becomes four named counts (the fourth `unresolved-with-reason`, PRD v0.8
ADDENDUM C) and their sum, and the function returns False when the sum is not `folders_read`.
- **Check** `checks/round40/ap1_check.py` at the base: `ap1 build 0/1 control 2/2`. As expected.

**CRPS-ap-2.** `ResearchTeamPillars` (`ThesisTab.tsx:111-175` on DEV) shows a pillar's lead, text, terms and report file name. The
served citation's `passage` and `locator` are not shown and nothing opens a pillar. The cell adds a native opener per pillar with
the passage and its location; a pillar with no served passage says so. No control opens the report DOCUMENT: no route by report
key exists, so the cell shows the passage and names the report.
- **Check** `checks/round40/page_check.cjs ap2` at the base: `ap2 build 0/1 control 1/1`. As expected.

**CRPS-ap-3.** `DossierPositionLine` (`SecurityOverlay.tsx:251-287`) prints the team's fund of record and last stated position
with no citation, though each served field carries one. The cell shows each field's report file name, location and passage, marks
the line as the research team's, and leaves the machine's `PostureHeaderLine` byte-unchanged. The Posture TAB half of FWD-15's
DONE WHEN is not in this cell (ruling 7 names the header line); ap-8 reads it.
- **Check** `page_check.cjs ap3` at the base: `ap3 build 0/1 control 2/2`. As expected.

**CRPS-ap-4.** `FeedList` (`HeaderBrief.tsx:106-152`) lists the served headlines and filters nothing. A feed item serves no term
field, so the filter matches the team's pillar terms against the headline's TITLE: one native block per term with its count and
its matching headlines. The terms reach the feed through ONE mount line in `SecurityOverlay.tsx`. The Chatter axis half of FWD-18
is NOT covered by this round and is named so in the packet.
- **Check** `page_check.cjs ap4` at the base: `ap4 build 0/1 control 1/1`. As expected.

**CRPS-ap-5.** The phrase "zero-dominated: no magnitude: 10 of 10 fiscal years are zero" is SERVED text
(`integrations/bloomberg/research/build_unit_map.py:556`), and its prefix is a class token three readers match
(`lib/research/provenance/validate.py:27`, `render_print.py:86`, two tests). Ruled a page cell (msg 31013): one branch in
`rowUnitWords` (`ModelTab.tsx:160-182`) reads the two counts from the served text and words them; an unparseable text falls back
to the served text. Served text unchanged.
- **Check** `page_check.cjs ap5` at the base: `ap5 build 1/3 control 3/3` (the fallback arm already holds). As expected.

**CRPS-ap-6.** `_resolve_section_field` (`dossier.py:384-396`) serves a section block that is only its own lead line; the one
refusal today is empty text (`:373-375`). The cell refuses a block with no prose beyond its heading (absent, with a reason, the
case path's `heading_only` shape), bumps `METHOD_VERSION`, and adds a read-only `--short-passage-census <N>`.
- **Check** `checks/round40/ap6_check.py` at the base: `ap6 build 0/2 control 2/2` (both heading-only fixtures serve
  "Management/Board 80"). As expected.

**CRPS-ap-7.** `FORECAST_FIELDS` (`model_block_pull.py:330-334`) holds 12 names; the six `lib/research/scores/divergence.py:64-65`
divides by are absent (0 of 6). Appended, they ride the three existing forecast requests: 8 calls per name before and after, 768
per fire before and after. `_NUMEST` is a count and carries no currency.
- **Check** `checks/round40/ap7_check.py` at the base: `ap7 build 0/1 control 2/2`. As expected.

**CRPS-ap-8.** With a walker slot from MSTR~Z, on the DEV build carrying ap-2..ap-5:
- FWD-20: the census of shown / refused / absent / unmapped over the Model sheet's rows for every covered name with a block,
  unmapped 0, denominators printed (ruling 2); ASML's row label read in words (ap-5);
- FWD-21: a name without forecast years walked and its reason read, or the census showing 0 served names lack them, with its
  denominator (ruling 4);
- FWD-11: one walk on a name with BOTH a team passage and a FILING roster (BA US or VLO US), "unchanged" compared by content, name
  by name; a labelled Bloomberg officer list is not the filing roster (ruling 5);
- FWD-16: the 2026-09-29 comparison extended to pillars and management, 95 names (ruling 6);
- FWD-10, FWD-15, FWD-18: the opener, the cited header line (and the Posture tab's half), the term filter, each on a real name.

**CRPS-ap-9.** Through the gateway's SharePoint read (CRO file `CORPUS_FWD12_SHAREPOINT_TEMPLATE_LOCATION_20261007.md`
@`acb0fd45bd`): for each covered name's own `<Company> FactSet Based ONE PAGER TEMPLATE <date>_vN.xlsx`, which of `Model` and
`Model NEW VERSION` carries the company's figures; both counts printed; a split reported, not averaged. Then the Model tab's rows,
order and labels against that sheet's, per name; a name with no workbook is compared to the master and the read says so. No
workbook content enters the repository beyond the row labels compared. The CTO amends FWD-12's DONE WHEN after the census.

**CRPS-ap-10.** Two paired acts, each with its own never-widen pair and ledger entry:
- (d) after ap-6 drains: the short-passage census on the served dossiers (8306 JP and 8316 JP are the named fail cases), then the
  dossier re-write for the names whose a field changes, read back;
- (m) after ap-7 drains: ONE name pulled through the scripted producer as the probe (each of the six returned, or its field error
  read), then the re-pin of `amgt-induction-daily` to the ap-7 drain; the next scheduled fire is the acceptance. No one-off pull
  of the population (CTO msg 30490).

## 2. Found at the cut (rows, not cells)

None new. `Z-S89` is this round's ap-6. `Z-S87` is carried (analysis ruling 11). A 2026-09-15 probe instrument spells
`BEST_CPS_STDDEV` where the consumer spells `BEST_CPS_STANDARD_DEV`; ap-10 (m)'s probe settles it before any re-pin.

## 3. Coverage

| cell | order | slot |
|---|---|---|
| CRPS-ap-1 | `AMGT_CORPUS.TO-CRPS-ap-1.fence14-line-four-counts.md` | `~1` |
| CRPS-ap-2 | `AMGT_CORPUS.TO-CRPS-ap-2.pillar-opens-to-its-passage.md` | `~4` |
| CRPS-ap-3 | `AMGT_CORPUS.TO-CRPS-ap-3.header-dossier-line-cited.md` | `~5` |
| CRPS-ap-4 | `AMGT_CORPUS.TO-CRPS-ap-4.feed-filters-to-pillar-terms.md` | `~5` (after ap-3) |
| CRPS-ap-5 | `AMGT_CORPUS.TO-CRPS-ap-5.zero-dominated-in-plain-words.md` | `~4` (after ap-2) |
| CRPS-ap-6 | `AMGT_CORPUS.TO-CRPS-ap-6.heading-only-section-is-absent.md` | `~2` |
| CRPS-ap-7 | `AMGT_CORPUS.TO-CRPS-ap-7.six-dispersion-mnemonics.md` | `~3` |
| CRPS-ap-8 | the issuer's read (no order) | -- |
| CRPS-ap-9 | the issuer's read (no order) | -- |
| CRPS-ap-10 | the issuer's paired acts (no order) | -- |
