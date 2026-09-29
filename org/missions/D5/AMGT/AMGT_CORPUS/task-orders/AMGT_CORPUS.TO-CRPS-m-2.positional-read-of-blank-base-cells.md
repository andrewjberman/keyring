# AMGT_CORPUS task order -- `CRPS-m-2` -- ROUND 11: a short scenario-table row is placed by the pdf page's x-coordinates when, and only when, the position puts the blank in exactly one column

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-m-2</owned_cells>
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

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 11, SECOND order on this slot (you completed `CRPS-m-1` on the same
file). Serves **FWD-12** limb 3's data half for six names.

## 1. THE CELL -- `CRPS-m-2`

**Where this came from.** Six names' page-0 scenario tables (k = 5: `2026E`..`2030E` x3 columns; rows `EPS`, `Multiple`,
`Price`, `Return`; values `[0,k)` Upside, `[k,2k)` Base, `[2k,3k)` Downside) have one genuinely blank Base cell: the Base column
carries 4 of 5 values in EPS, Price and Return. They are **8035_JP_Equity, BZLFY_US_Equity, HEI_US_Equity, SNPS_US_Equity,
TSM_US_Equity, V_US_Equity**, served today with
`"<LABEL> CASE scenario table row 'EPS' has 14 of 15 cells; the empty cell's position is not recoverable from line order (no x-coordinates)"`.
The stored extraction lines carry `text`, `page`, `size`, `bold_first`, `bold_all`, `n_spans`, `lead_prefix` -- no x-coordinates.
The source pdf is the picked report row's `bronze_key` (an S3 URI; read-only), reachable from `_picked_reports(security_key,
client)`. Arithmetic (Price = EPS x Multiple) suggests the blank is Base 2030E on some; arithmetic is NOT a placement rule.

**RULED -- what you build (the CTO's round-10 analysis, ruling 3):**
1. For a table row whose value count is short of 3k, read the pdf page's word positions (PyMuPDF `page.get_text("words")`,
   x0/x1 per word) from the bronze pdf bytes, locate the 3k year-header x-positions and the short row's values by text, and
   assign each value to the column band it falls in.
2. **Serve the row only if** every value falls in exactly one column band, no two values share a column, and exactly the
   missing count of columns is empty -- then that case serves the team's values with the empty slot `null`, per year.
   Any other outcome (a value between bands, two in one band, headers not found, the pdf unreadable) keeps today's ABSENT with
   today's reason. Never fill a blank cell.
3. **No PDF library at import:** importing `lib.research.corpus.dossier` must still load no `fitz` / `pymupdf` -- import it
   inside the function that reads positions (AMGT_RESAPP's Lambda imports `dossier` for `read_dossier`).
4. A read-only CLI mode `python -m lib.research.corpus.dossier --case-positional-census` (add to the existing group): for every
   resolved name whose table has a short row, one line `positional <key> <placed|ambiguous|no_positions> <detail>`; final line
   EXACTLY: `positional names <N> placed <p> ambiguous <a> no_positions <n> sum <p+a+n>`.
5. **Bump `METHOD_VERSION` to `"amgt-corpus-dossier/4"`** (this chain changes what a case serves but moves no dossier
   `inputs`; without the bump the issuer's rewrite writes 0 on every name).
6. `lib/research/corpus/tests/test_dossier_case_positional.py` (new), offline word-position fixtures: an unambiguous blank ->
   placed with `null` in its slot; a value between two bands -> ABSENT with today's reason; a round-9 full table -> unchanged;
   the import loads no PDF library.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_case_positional.py
lib/research/corpus/tests/test_dossier_case_layouts.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-m-2.positional-read-of-blank-base-cells.md
</paths>

READ-ONLY: every other file, every S3 object (bronze pdfs included). Scratch `.scratch/m2/`.

## 4. BOUNDS
- Pure ASCII source, LF, Python 3.9-compatible. NO S3 write: never run `dossier --write`.
- `test_dossier_case_layouts.py` may change only where it pins the ABSENT reason on a name this cell now places, or the old
  `METHOD_VERSION`; name each such test.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`,
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-m-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round11/m2_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-m-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round11/m2_AC2.sh</invocation><expect>(?m)^positional names 6 placed \d+ ambiguous \d+ no_positions \d+ sum 6$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-m-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round11/m2_AC3.sh</invocation><expect>l3 names 6 body_names \d+ absent_specific \d+ absent_generic 0 sum 6</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-m-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round11/m2_AC4.sh</invocation><expect>l1 dossier_import pdf_libs_loaded none read_dossier_callable True</expect></criterion>
  <criterion id="AC5" cell_refs="CRPS-m-2" judgment="true"/>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe on the six names' real pdf pages (each lands in exactly one branch); AC3 the bound:
  none of the six falls back to the generic message; AC4 (fourth criterion; reason: a cross-project consumer's Lambda cannot
  import a PDF library, and this cell adds one) the import stays PDF-free. AC5 (JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9 on
  the served rewrite, never by you): *is every placed value in the column the pdf page shows it in, and is every unplaced name
  still honestly ABSENT?* Record it under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-m-2.positional-read-of-blank-base-cells.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's per-name lines and summary; for each placed name, the empty slot's column and year.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-10 analysis s.2 ruling 3 + s.4 item 2 @`8b54c2b4fd`. Checks dry-run at the base: AC1 FAIL (no tests
ran); AC2 FAIL (argparse refuses `--case-positional-census`); AC3 PASS (`absent_generic 0 sum 6`); AC4 PASS (import PDF-free).
The fourth mechanical criterion carries its reason on the face.

<risk>SERVED</risk>
<status>complete</status>
<round>11</round>
<slot>~1</slot>
<fabric>site-z</fabric>
