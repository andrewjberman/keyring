# TO IRPT_CUSTDY.TO-CU-g-3a -- round 7 CU-g-3 (E3): the Black Diamond field map of one real 49 Financial client statement, sliced on its Run Report bases, plus its layout as the baseline template

<to_id>IRPT_CUSTDY.TO-CU-g-3a</to_id>
<project>IRPT_CUSTDY</project>
<issued_to>0.9.0_WK_IRPT_CUSTDY~17</issued_to>
<issued_by>2.0.0_SA_COO~K2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~K2-E3</workstream>

**Directive:** D9 | **Fabric:** laptop (placement dell2) | **Decomp cell:** `CU-g-3` (`decompositions/IRPT_CUSTDY_DECOMP.round7.md`) |
**outcome_ref:** FWD-9 | **depends_on:** none (the gate, one BD 49F report on dell2, opened 22:22Z)

---

## WORKER FACE

### THE CELL

`CU-g-3`, outcome FWD-9: "For every figure a Black Diamond report shows, anyone can see where Opal gets it instead." DONE WHEN: the
map is read for every field of one Black Diamond client report; for each figure, which Black Diamond source served it and where Opal
reads the same figure (the custodian or Opal's own store); a figure with no other source is named as such.

Andrew's word for this cell (~22:1xZ, relayed by `1.0.0_SA_CTO~DELL2` msg 1784): "Slice the Performance client statement on Black
Diamond's Run Report bases, and take the PDF's layout as the baseline template."

**The inputs (OUTSIDE the repo; READ ONLY; CLIENT DATA):**
- `C:\Users\Test\Downloads\17752262.pdf` (7,415,884 bytes, sha256 starts `ae08e1008368fb5c`) -- one real Black Diamond 49 Financial
  client report.
- `C:\Users\Test\Downloads\Screenshot 2026-10-08 180904.png` (61,935 bytes) -- the template as Andrew sees it.

**CLIENT-DATA RULE, verbatim (msg 1784):** "It is CLIENT DATA: it is never committed, copied into the repo or quoted in records.
Records carry sections, field names and counts only, and the files stay outside the repo." So: no value, name, account number, date
range, holding, amount or percentage from the PDF enters any file you write or any message. Do not copy the PDF or the PNG anywhere.
Read them in place. Never write extracted text to disk inside the worktree (hold it in memory, or under `.scratch/` uncommitted and
deleted before you report).

**Opal's side, to read (never edit):** the hop 3 producer `data/assets/scripts/gold/irpt_custody/client_report_figures.py` and
`hop3_real_run.py` (what Opal already computes for the statement); the 49F gold runners `data/assets/scripts/gold/runners_49f/`
(served 49F tables and columns); the Black Diamond side of IRPT_DASHBD's split pull
(`org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-45.bd-split-pull-run.md` and the code it names) for which BD API
endpoint serves which figure. PDF libraries already installed: `fitz` (PyMuPDF), `pdfplumber`, `pypdf`. No install, no download.

**Build:**
1. `data/assets/scripts/gold/irpt_custody/bd_field_map.py`: given a PDF path, enumerate the report's Run Report bases (each section
   Black Diamond generates from one report base, e.g. a performance summary, holdings, activity, fees -- name them as the PDF titles
   them), and within each base every figure-bearing field (a column header, a labelled figure, a chart series). Emit field NAMES and
   structure only, never values. It writes nothing outside the path you give it.
2. The field map, `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/BD_FIELD_MAP_CU-g-3.json` (+ a short `.md`
   reading of it): one row per field, `{run_report_base, field, page, bd_source, opal_status, opal_source, reason}`.
   - `opal_status` is `MAPPED` or `MISSING`.
   - `MAPPED` names the Opal source as a file path plus a function or column you read in the code (custodian table or Opal's store).
   - `MISSING` carries the reason (no custodian or Opal source; or held only by Black Diamond).
   - `bd_source` names the Black Diamond endpoint or report base that serves it, or `UNKNOWN` with a reason.
   - The header prints the denominator: fields per base and in total, `MAPPED` and `MISSING` counts.
   - Where Commonwealth history holds more than Black Diamond's feed, say so on the row.
3. The layout baseline, `.../0.9.0_WK_IRPT_CUSTDY~17/LAYOUT_BASELINE_CU-g-3.md`: page count; per page the base it belongs to; per base
   the block order (title, table, chart, footnote) and table column order -- structure only, as the input for the statement template
   (the Performance client statement, portal `ClientReportDocument`). Compare it with the PNG and with `ClientReportDocument.tsx`
   (read only): list each section the template lacks or orders differently.
4. `data/assets/scripts/gold/irpt_custody/bd_leak_check.py`: given the PDF path and a list of files, extract every value-like token
   from the PDF (numbers of 3+ digits, currency and percentage figures, dates, and capitalised multi-word names that are not section
   or column headings) and exit non-zero if any appears in the files. Print the token count it checked.
5. `data/assets/scripts/gold/irpt_custody/tests/test_bd_field_map.py`: build a small SYNTHETIC PDF in the test (with `fitz`, invented
   text, two bases, a table and a labelled figure) and assert the extractor finds its bases and fields, and that `bd_leak_check`
   fails on a planted value and passes on a clean file. No real PDF in tests or fixtures.

### ACCEPTANCE

<criterion id="CU20-AC1" cell_refs="CU-g-3"><invocation>python -m pytest -q data/assets/scripts/gold/irpt_custody/tests/test_bd_field_map.py</invocation><expect>passed</expect></criterion>
`CU20-AC1` -- the extractor and the leak check work on a synthetic statement, including the planted-value negative control.

<criterion id="CU20-AC2" cell_refs="CU-g-3"><invocation>python data/assets/scripts/gold/irpt_custody/bd_leak_check.py "C:\Users\Test\Downloads\17752262.pdf" org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/BD_FIELD_MAP_CU-g-3.json org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/BD_FIELD_MAP_CU-g-3.md org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/LAYOUT_BASELINE_CU-g-3.md</invocation><expect>rc 0</expect></criterion>
`CU20-AC2` -- no client value from the real PDF is in any deliverable (token count printed).

<criterion id="CU20-AC3" cell_refs="CU-g-3"><invocation>python -c "import json;d=json.load(open('org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/BD_FIELD_MAP_CU-g-3.json'));r=d['rows'];assert r and all(x['opal_status'] in ('MAPPED','MISSING') and (x['opal_source'] if x['opal_status']=='MAPPED' else x['reason']) for x in r);assert d['denominator']['total']==len(r);print('rows',len(r))"</invocation><expect>rows</expect></criterion>
`CU20-AC3` -- every field is MAPPED with a source or MISSING with a reason, and the printed denominator equals the rows.

<expected_criteria>CU20-AC1,CU20-AC2,CU20-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus this order's file. Scaffolding goes under `.scratch/`, uncommitted, deleted before you report.
- **Client data.** The two Downloads files are read in place and never copied; see the rule above. A value in a commit is a stop:
  revert it before you commit, never after.
- **No AWS call. No portal edit** (`ClientReportDocument.tsx` is read only). No install, no download.
- Commits via `.tools/safe-commit.sh` with your serial as author. A surprise row is committed in the same turn you write it.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a row (id `IRPT_CUSTDY-W17-S<k>`;
  `disposition` one of UNDER_INVESTIGATION | GRADUATED | DISMISSED_WITH_REASON | DECOMP_INVALIDATING), and do not weaken a test.

<paths>
data/assets/scripts/gold/irpt_custody/bd_field_map.py
data/assets/scripts/gold/irpt_custody/bd_leak_check.py
data/assets/scripts/gold/irpt_custody/tests/test_bd_field_map.py
org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/BD_FIELD_MAP_CU-g-3.json
org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/BD_FIELD_MAP_CU-g-3.md
org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/LAYOUT_BASELINE_CU-g-3.md
org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/IRPT_CUSTDY.TO-CU-g-3a.bd-field-map-and-layout-baseline.proof_of_spec.json
org/missions/D9/IRPT/IRPT_CUSTDY/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_CUSTDY/decompositions/IRPT_CUSTDY_DECOMP.round7.md</decomp_doc> (round 7), cell `CU-g-3`.
<owned_cells>CU-g-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CU20-AC1, CU20-AC2, CU20-AC3. Instance at `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/0.9.0_WK_IRPT_CUSTDY~17/IRPT_CUSTDY.TO-CU-g-3a.bd-field-map-and-layout-baseline.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CU20-AC1,CU20-AC2,CU20-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the Run Report bases found and fields per base; MAPPED/MISSING counts; the template gaps; the leak-check token count; rows;
commits. No client value in the report.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local read of one PDF; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the leak check reads the real PDF's own tokens (not a hand list) and is proven by a planted-value negative control; the map's Opal sources are read from code, not asserted; BLIND: the BD endpoint names depend on IRPT_DASHBD's pull code, so an unmatched one is UNKNOWN with a reason, never guessed.
lane: the <paths> block IS the grant.
</preflight>

Source: round-7 decomposition @0b672a8d47 cell CU-g-3 (gate: one BD 49F report on dell2); gate opened by MSTR msg 1782 and CTO GO msg
1784 (Andrew-direct ~22:1xZ, laptop record @a311147bd7). Andrew's added scope (Run Report bases, layout as baseline template) is taken
verbatim from msg 1784 inside the cell's own outcome (FWD-9) and its template input; the issuer rules it in, no ENDPOINT change.
