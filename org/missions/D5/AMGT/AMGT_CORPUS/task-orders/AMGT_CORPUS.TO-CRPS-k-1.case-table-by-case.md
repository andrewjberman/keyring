# AMGT_CORPUS task order -- `CRPS-k-1` -- ROUND 9: each served case is ITS OWN columns of the team's scenario table, `{metric: {year: value}}`, with its unit and page citation

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-k-1</owned_cells>
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

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 9. Serves **FWD-12** limb 3's data half (*"the team's
Upside/Base/Downside cases render as the team's, cited"*) and the cases half of **FWD-16** (PDF-only names).

## 1. THE CELL -- `CRPS-k-1`

**Where this came from.** `lib/research/corpus/dossier.py` resolves `fields.cases.{upside,base,downside}` through
`_resolve_case_field` / the case block rule added in round 8 (`CRPS-j-1`): the value is the text after the case heading up to
the next section lead. Measured over all 95 resolved names in round 8: **no stored pack carries prose under a case heading.**
The 34 names with case leads are all class-A pdf packs, where `Upside Case`, `Base Case`, `Downside Case` are THREE
CONSECUTIVE LINES on page 0 -- the row labels of a scenario table -- followed by 3k year-header lines and then metric rows.
ADBE_US_Equity's extraction, line by line after `Downside Case`:

```
2026E | 2027E | 2028E | 2029E | 2030E | 2026E | ... | 2030E | 2026E | ... | 2030E          (15 = 3 x k, k = 5)
EPS | 24.16 | 27.86 | 32.15 | 35.56 | 39.33 | 24.37 | 27.48 | 31.44 | 35.33 | 38.60 | 23.06 | 24.68 | 26.42 | 27.10 | 27.78
Multiple | 16.0x | 16.0x | 16.0x | 16.0x | 16.0x | 9.0x | ... | 9.0x | 6.0x | ... | 6.0x
Price | 416 | 446 | 514 | 569 | 629 | 233 | 247 | 283 | 318 | 347 | 143 | 148 | 159 | 163 | 167
Return | 88.4% | 101.8% | 132.8% | 157.5% | 184.8% | 5.6% | ... | 57.3% | -35.2% | ... | -24.6%
```

Values `[0,k)` are Upside, `[k,2k)` Base, `[2k,3k)` Downside, in the order the labels appear. AZN_LN_Equity carries its unit
on its values (the pound sign, U+00A3). Today's round-8 rule serves Downside as the whole table's cells and Upside/Base as
ABSENT (`case_census names 95 slots 285 body 34 heading_only 68 absent 183 sum 285`). The extraction lines carry `text`,
`page`, `size`, `bold_first`, `bold_all`, `n_spans`, `lead_prefix` -- no x-coordinates, so the table is read from line order.

**RULED -- what you build (the CTO's round-8 analysis, ruling 1):**
1. **Detect the table.** When the three case leads are consecutive lines (in label order) and are followed by year-header
   lines whose count is a multiple of 3 (group length k = count / 3; a year header is a 4-digit year with an optional letter
   suffix such as `E` or `A`), read the table: each following metric row is a non-numeric label line followed by exactly 3k
   value lines. The table ends at the first line that is neither, or at the next section lead.
2. **Case i takes values `[ik, (i+1)k)` of every metric row.** Serve each case as
   `{"value": {<metric>: {<year>: <value string as written>}}, "unit": <symbol or null>, "citation": {"report_key",
   "report_id", "locator": <the table's page>, "passage": <the case's rows as text, first _PASSAGE_CAP chars>}}`.
   Values are the strings the team wrote -- never parsed into numbers, never computed.
3. **Unit.** Read the currency symbol the row values carry (e.g. U+00A3 pound, `$`, U+20AC euro, U+00A5 yen) and put it in `unit`, per case (the
   same symbol for all three when the table uses one); `null` when the values carry none. **Pure ASCII rule for the code:**
   write the symbols as `\u` escapes in Python source (`"\u00a3"`), never literal non-ASCII; the JSON the dossier stores is
   written with the existing canonical writer.
4. **A row whose value count is not 3k** makes the whole table unreadable for that name: each case is served
   `{"value": null, "absent": "<LABEL> CASE scenario table row '<metric>' carries <n> values, expected 3 x <k>"}`.
5. **A case heading that is not a table row label** (no consecutive labels + year headers) keeps round 8's rule unchanged.
6. **The census** (`python -m lib.research.corpus.dossier --case-census`, same resolver path as `build()`, still writes
   nothing) prints per name `case <key> upside <state> base <state> downside <state> unit <symbol-as-\u-escape or none>
   ordering <held|violated|na>`, where `ordering` compares the three cases' FIRST-year `Price` values as numbers
   (Upside >= Base >= Downside is `held`; a name with no table or no parseable Price is `na`) -- a column only, never a
   refusal. Final line EXACTLY:
   `case_census names <N> slots <3N> body <B> heading_only <H> absent <A> sum <B+H+A> ordering_held <h> ordering_violated <v> ordering_na <n> unit_carried <u>`
   where `unit_carried` counts names whose table carries a unit.
7. `lib/research/corpus/tests/test_dossier_case_table.py` (new), offline fixtures: a k=5 table -> three cases with their own
   columns and the page locator; a k=3 table; a U+00A3 (pound) table -> `unit` carried; a row with a wrong value count -> all three ABSENT
   with the reason; a non-table case heading -> round-8 behaviour unchanged; the census's ordering column on a held and a
   violated fixture.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_case_table.py
lib/research/corpus/tests/test_dossier_case_body.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-k-1.case-table-by-case.md
</paths>

READ-ONLY: every other module, every S3 object. Scratch `.scratch/k1/`.

## 4. BOUNDS
- Pure ASCII source, LF, Python 3.9-compatible. NO S3 write: never run `dossier --write` (the served rewrite is the issuer's
  act under a signed pair, after your drain). Do not change `METHOD_VERSION` (round 8 set `/2`; nothing is stored at `/2`).
- Existing dossier tests keep passing; `test_dossier_case_body.py` may be updated ONLY where it pins the table-dump behaviour
  this cell replaces -- name each such test in your report.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`,
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-k-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round9/k1_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-k-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round9/k1_AC2.sh</invocation><expect>case_census names ([1-9]\d*) slots \d+ body [1-9]\d* heading_only 0 absent \d+ sum \d+ ordering_held \d+ ordering_violated \d+ ordering_na \d+ unit_carried \d+</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-k-1" judgment="true"/>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe over the real stored extractions of every resolved name: no case slot is a bare
  heading any more, with the ordering and unit columns reported as measured. AC3 (JUDGMENT, graded by `3.0.0_SA_CVO~Z` at L9
  on the served rewrite, never by you): *does each served case read as that case, in the team's numbers, with its unit?* --
  graded on names from more than one currency. Record it in the instance under `UNVERIFIABLE-BY-INSTRUMENT` with a
  `status_reason` naming the CVO.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-k-1.case-table-by-case.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's census line; every name with `ordering violated` and every name whose table was unreadable (with the
   reason); the three cases of ADBE_US_Equity and AZN_LN_Equity as served (value + unit).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-8 analysis s.2 ruling 1 + s.4 item 1 @`40ff643781` (msg 26356). Rows `Z-W1-S9` / `Z-S53` close on the
served rewrite. Checks dry-run at the base (`checks/round9/`): AC1 FAIL (no tests ran); AC2 FAIL (base line lacks
`heading_only 0` and the ordering/unit columns). The drain: a never-widen pair for the rewrite (expected: every name writes,
95 puts, objects 468 -> 563), a change entry, `dossier --write --workers 10`, verify `--case-census` and `--pick-census
stale_pick 0`, `read_dossier` on ADBE and AZN read by this seat; the CVO grades AC3 on the served table.

<risk>SERVED</risk>
<status>complete</status>
<round>9</round>
<slot>~1</slot>
<fabric>site-z</fabric>
