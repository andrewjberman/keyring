# AMGT_CORPUS task order -- `CRPS-l-3` -- ROUND 10: the six scenario tables round 9 could not read are read, or served ABSENT with a reason naming each one's own layout defect

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-l-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface; the served rewrite is the issuer's drain act.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 10, FIRST of two orders on this slot (the second, `CRPS-l-1`,
edits the same file after this one). Serves **FWD-12** limb 3's data half for six names.

## 1. THE CELL -- `CRPS-l-3`

**Where this came from.** `lib/research/corpus/dossier.py` reads each name's page-0 scenario table (round 9, `CRPS-k-1`):
after the three consecutive case labels `Upside Case` / `Base Case` / `Downside Case` come 3k year-header lines, then metric
rows (a label line followed by exactly 3k value lines; values `[0,k)` Upside, `[k,2k)` Base, `[2k,3k)` Downside). A lone
currency-symbol line after a value is read as that value's unit; a date-shaped line ends the table. A row whose value count
is not 3k makes the whole table unreadable and all three cases are served ABSENT with
`"<LABEL> CASE scenario table row '<metric>' carries <n> values, expected 3 x <k>"`. Six names read that way today, each with
`row 'EPS' carries 14 values, expected 3 x 5`: **8035_JP_Equity, BZLFY_US_Equity, HEI_US_Equity, SNPS_US_Equity,
TSM_US_Equity, V_US_Equity.** Round 9's worker measured one Base EPS value missing from the extraction's line list on each.
The extraction lines carry `text`, `page`, `size`, `bold_first`, `bold_all`, `n_spans`, `lead_prefix` -- no x-coordinates.
Reach a name's stored extraction through the module's own `_picked_reports(security_key, client)` (class-A pick first).

**RULED -- what you build (the CTO's round-9 analysis, ruling 3):**
1. **Read each of the six layouts first** (read-only) and record, per name, where the missing value went: e.g. two values
   merged on one line (`"24.37 27.48"`), a value split across lines, a value carried on the metric label line, a blank cell,
   a row wrapped, a value moved after the table. Put the per-name finding in your report.
2. **Extend the table rule** for every layout defect that the line list itself makes unambiguous (a merged line that splits
   into exactly the missing count; a value on the label line; ...), so that name's three cases are served from the team's own
   strings. Never invent, move or re-order a value to make a count fit.
3. **Where the line list cannot place the missing value unambiguously** (e.g. a genuinely blank cell: which of the 15 slots is
   empty cannot be read from line order), serve that name's three cases ABSENT with a reason naming ITS OWN defect, e.g.
   `"<LABEL> CASE scenario table row 'EPS' has 14 of 15 cells; the empty cell's position is not recoverable from line order
   (no x-coordinates)"`. The generic count message is not an acceptable final reason for these six.
4. The 28 tables round 9 read keep their exact served values (test it: no change for ADBE_US_Equity and AZN_LN_Equity).
5. `lib/research/corpus/tests/test_dossier_case_layouts.py` (new), offline fixtures reproducing each defect class you find --
   extended layouts read correctly; an unrecoverable one served ABSENT with its specific reason -- plus a round-9 k=5 table
   unchanged.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_case_layouts.py
lib/research/corpus/tests/test_dossier_case_table.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-l-3.six-unreadable-case-tables.md
</paths>

READ-ONLY: every other file, every S3 object. Scratch `.scratch/l3/`.

## 4. BOUNDS
- Pure ASCII source, LF, Python 3.9-compatible. NO S3 write: never run `dossier --write`. Do not change `METHOD_VERSION`.
- Values are the team's strings exactly as written; nothing is parsed into a computed number or re-ordered.
- `test_dossier_case_table.py` may change only where it pins the generic count message on a layout this cell now reads;
  name each such test.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`,
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-l-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round10/l3_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-l-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round10/l3_AC2.sh</invocation><expect>l3 names 6 body_names \d+ absent_specific \d+ absent_generic 0 sum 6</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe on the six names' real extractions: none is left on the generic message.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-l-3.six-unreadable-case-tables.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's per-name lines and summary; the per-name layout finding; then the issuer continues you on `CRPS-l-1`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-9 analysis s.2 ruling 3 + s.4 item 3 @`abfad1355c`; row `Z-W1-S12`. Checks dry-run at the base:
AC1 FAIL (no tests ran); AC2 FAIL (`l3 names 6 body_names 0 absent_specific 0 absent_generic 6 sum 6`).

<risk>SERVED</risk>
<status>complete</status>
<round>10</round>
<slot>~1</slot>
<fabric>site-z</fabric>
