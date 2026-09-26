# AMGT_CORPUS task order -- `CRPS-i-3` -- ROUND 7: the team's written Base-case number is read from the cell BESIDE its label, selected by a stated rule and cited by coordinate, next to the served Base case

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-i-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only evidence producer.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only (opal-data-harvest); nothing written outside the worker's deliverables.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 7. Serves **FWD-12**'s judgment half: a served Base case read beside
the team's own workbook number for that name. You produce EVIDENCE; the grade is the CVO's.

## 1. THE CELL -- `CRPS-i-3`

**Where this came from.** Round 6 built
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/case_evidence.py`, a deterministic read-only producer
(`python <path> --out-json <p> [--out-md <p>]`) that lays every Base/Bull/Bear/Upside/Downside/target-price labelled cell of
every bronze workbook beside the served Base case, selecting nothing. Graded: 200 Base-labelled cells, and **196 of them
came back with an empty `right` list** -- the direction a sheet puts a value next to its label. The workbooks are opened with
openpyxl `read_only=True, data_only=True`, and `_numbers_to_right` loops to `ws.max_column`; in read-only mode that comes from
the sheet's stored dimension, which is commonly stale. A value that is an uncached formula would also read as None. Of 37
names with a numeric served base, 0 yielded a comparable workbook number; the few neighbours found were years (2017) and a
negative. Quoting a number the team wrote, with its locator, is EXTRACTION and is in scope; generating a case is not.

**RULED -- what you build (edit the round-6 producer in place):**
- Measure first and say which cause holds: for the Base-labelled cells, how many have a numeric cell to the right within 6
  columns when the sheet is read WITHOUT `read_only` (or with the dimension reset), and how many of those right-hand cells are
  formulas with no cached value. Print both counts in the `.md`.
- Fix the neighbour capture so `right` reads the real row (up to 6 numbers), and keep `below` as it is.
- Add `workbook.selections`: at most ONE per workbook, chosen by this rule, printed verbatim as `rule` on every selection: the
  label cell's text, stripped and case-folded, contains the word `base` as a whole word (never inside `database`, `baseline`,
  `based`); the value is the first number to its RIGHT in the same row, else the first below in the same column; an integer
  from 1900 to 2100 inclusive is skipped as a year; a negative number is skipped. Each selection carries `security_key` (the
  block directory name), `workbook_key`, `sheet`, `cell` (the VALUE's coordinate), `label_cell`, `label`, `value`, `direction`
  (`right` / `below`), `rule`, `served_base`, `px_last`, `status`, `cause`, and `workbook_to_served` (value / served_base, or
  null). When a workbook has several matching labels, choose the first in sheet order, then row, then column, and list the
  others under `other_candidates` with their coordinates.
- Write `CASE_EVIDENCE_ROUND7.json` and `CASE_EVIDENCE_ROUND7.md` (the ROUND6 files stay as they are). The `.md` adds, per venue
  (London `LN`, US `US`, Asian listings), a table of the selections beside the served Base case.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/case_evidence.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/CASE_EVIDENCE_ROUND7.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/CASE_EVIDENCE_ROUND7.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-i-3.workbook-base-case-selected-and-cited.md
</paths>

READ-ONLY: every module in the repo. Scratch `.scratch/i3/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO S3 write, NO vendor or gateway call, NO edit to any producer outside your paths.
  No Base/Upside/Downside figure is computed; a selection is a number the team typed, with its coordinate.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W2-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-i-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i3_AC1.sh</invocation><expect>i3 OK census_rows (\d+) keys_with_block \1 base_labels \d+ right_nonempty [1-9]\d* names_with_selection [1-9]\d* selections_without_coord 0\b</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-i-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i3_AC2.sh</invocation><expect>i3 determinism identical sha [0-9a-f]{12}</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-i-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i3_AC3.sh</invocation><expect>i3 floor LN [1-9]\d* US [1-9]\d* ASIA [1-9]\d*</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-i-3" judgment="true"/>
</proof_of_spec>

- AC1 the evidence covers every block key, Base labels carry right-hand neighbours, selections exist and every one is located;
  AC2 the producer is deterministic; AC3 the sample floor (R-1): selections in every venue.
- **AC4 (JUDGMENT, the CVO's, at L9 -- nothing for you to produce beyond the evidence):** does each selected cell read as the
  team's own Base-case number for that name, and does the served Base case read as plausible beside it? The sample is a FLOOR
  and names every venue present (R-1): at least one London, one US large-cap, one Asian listing, and every refused key with a
  selection.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-i-3.workbook-base-case-selected-and-cited.proof_of_spec.json`
   (AC4 as a declared exclusion; the checker admits no judgment row).
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes; commit the files you changed plus the instance.
4. Report ONCE: the two cause counts, AC1's line, and the selections' `workbook_to_served` spread by venue.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-6 analysis s.6 item 3 @`1e53f322f3` (third round carrying it); ADJUDICATION_v9 s.2(A) ("capture
`right` as well as `below`, and select the case cell"); CTO adjudication @`bfc179c2ea` (quoting the team's number is
extraction). Checks dry-run at the base: AC1/AC2/AC3 FAIL (no ROUND7 evidence, no selections).

<risk>LOCAL</risk>
<status>pending</status>
<round>7</round>
<slot>~2</slot>
<fabric>site-z</fabric>
