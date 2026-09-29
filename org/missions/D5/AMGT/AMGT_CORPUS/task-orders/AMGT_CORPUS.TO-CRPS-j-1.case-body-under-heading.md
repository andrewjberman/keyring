# AMGT_CORPUS task order -- `CRPS-j-1` -- ROUND 8: each served case carries the team's text UNDER its heading, cited, and a method bump is no longer a no-op on the write

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-j-1</owned_cells>
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

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 8, on your SECOND order (you completed `CRPS-j-4` on the same file:
`read_dossier` now prefers the current `METHOD_VERSION`). Serves **FWD-12** limb 3's data half (*"the team's
Upside/Base/Downside cases render as the team's, cited"*) and the cases half of **FWD-16** (PDF-only names).

## 1. THE CELL -- `CRPS-j-1`

**Where this came from.** `lib/research/corpus/dossier.py` resolves `fields.cases.{upside,base,downside}` through
`_resolve_section_field(<LABEL> + " CASE", CASE_SECTION_NAMES[...], pick_a, pick_b, ...)`, which calls
`_resolve_section_block_from_picks` -> `_find_section_lead` (the FIRST `section_leads` entry named `UPSIDE CASE` /
`BASE CASE` / `DOWNSIDE CASE`) -> `_section_block_items`, which collects the lead line and every item up to the next section
lead, or (docx) the next bold paragraph of at most `extract._HEADING_WORD_CAP` words, or (pdf) the next standalone heading
that is not lead-only. The value is those items joined. Measured on the served table (all 95 dossiers): **all 102 of 102
case values that are present are the heading alone** (`"Upside Case"` / `"Base Case"` / `"Downside Case"`), cited to a
passage that is the same heading -- e.g. AZN_LN_Equity: `cases.base = {"value": "Base Case", "citation": {"passage":
"Base Case", "locator": 0}}`. So the block ends at the line after the heading and no case body is carried. The team writes
its case under that heading; the dossier serves only the heading.

**A second defect the issuer's rewrite would hit.** `write_one` first reads the stored object (via `read_dossier`) and writes
NOTHING when its `inputs` equal fresh `current_inputs` -- and `inputs` carries no method version. A code fix alone, even
with a `METHOD_VERSION` bump, would print `unchanged ... wrote 0` on all 95 names.

**RULED -- what you build:**
1. **The case value is the text UNDER the heading.** Measure first (read-only, docx AND pdf names; the stored extractions are
   reachable through the module's own `_picked_reports`) where the case text sits relative to the case lead and why
   `_section_block_items` stops after one line (a bold sub-heading, a table, a standalone-heading line, the next case lead,
   a sibling case heading on the same line or page). Then change ONLY how a CASE block ends (and, if needed, which item
   starts its body) so the value is the team's text beneath its own heading, up to the next case lead or the next section
   lead. The heading itself is NOT the value. Other section fields (management, recommendation, risks, ...) do not change.
2. **No heading-only value is ever served.** A case whose block carries no text under the heading is served
   `{"value": null, "absent": "<LABEL> CASE heading carries no text under it in <class/period label>"}` -- never its heading.
3. **Citation** stays `{report_key, report_id, locator, passage}`; `locator` is where the BODY starts; `passage` is the
   body's first `_PASSAGE_CAP` characters.
4. **The no-op compares the method too.** `write_one` writes nothing only when the stored object's `method_version` equals
   `METHOD_VERSION` AND its `inputs` equal fresh inputs (keep the printed `unchanged inputs_sha16 <h> wrote 0` line for that
   case). Bump `METHOD_VERSION` to `"amgt-corpus-dossier/2"`.
5. **A read-only census:** `python -m lib.research.corpus.dossier --case-census` (add it to the existing mutually exclusive
   group). Over `_resolved_security_keys()`, it resolves ONLY the three case fields per name, through the SAME resolver
   `build()` uses (never `build()` itself, which is minutes per name), writes nothing, and prints per name
   `case <key> upside <state> base <state> downside <state>` with state in `body` / `heading_only` / `absent`, then EXACTLY:
   `case_census names <N> slots <3N> body <B> heading_only <H> absent <A> sum <B+H+A>`. `heading_only` counts a slot whose
   resolved block carries a heading and no text under it -- after your change these are served ABSENT (rule 2) but still
   counted as `heading_only` here, so the census distinguishes "no case section" from "an empty case section". It may run
   names concurrently (processes: the work is CPU-bound PDF/docx text handling).
6. **The producer runs concurrently:** `dossier --write --workers N` (default 1 = the existing serial loop, unchanged) runs
   `write_one` over the same key list in a process pool of N, one S3 client per process, printing the same per-name lines
   and the same final `names <n> written <w> existed <e>` summary.
7. `lib/research/corpus/tests/test_dossier_case_body.py` (new), offline stubs: a docx and a pdf document whose case heading
   is followed by body text -> the value is the body, cited at the body's locator; a heading with nothing under it -> ABSENT
   with the reason, census state `heading_only`; a document with no case lead -> `absent`; the no-op writes 0 when method and
   inputs both match and WRITES when only the method differs; `--workers 1` equals the serial path.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_case_body.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-j-1.case-body-under-heading.md
</paths>

READ-ONLY: every other module, every S3 object. Scratch `.scratch/j1/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO S3 write: never run `dossier --write` (the served rewrite is the issuer's act,
  under a signed pair, after your drain). `--case-census` and your measurements are reads.
- Existing dossier tests keep passing unmodified, except an assertion that pins a heading-only case value, which you may
  update to the rule-2 ABSENT shape -- name each such test in your report.
- Generate nothing: every case value is text the team wrote, cited; no summarising, no rewording, no inferred number.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`,
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-j-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round8/j1_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-j-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round8/j1_AC2.sh</invocation><expect>case_census names ([1-9]\d*) slots \d+ body [1-9]\d* heading_only \d+ absent \d+ sum \d+</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-j-1" judgment="true"/>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe over the real stored extractions: the census runs over every resolved name and
  finds case BODIES (`body` is at least 1); report `heading_only` as measured. AC3 (JUDGMENT, graded by `3.0.0_SA_CVO~Z` at
  L9 on the served rewrite, never by you): does each served case read as the team's own written case for that name?
  Record it in the instance under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-j-1.case-body-under-heading.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's census line; where the case text sat and what ended the block (docx and pdf); three sample
   `(key, case, first 120 chars of value)` from the census run.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-7 analysis s.2 ruling 1 + s.5 item 1 @`03327ebbf9`; CTO msg 26235; rows `Z-W5-S3`, AMGT_RESAPP
`Z-S293`. Checks dry-run at the base @`e3fd90cb63`: AC1 FAIL (no test file), AC2 FAIL (argparse refuses `--case-census`).
The drain: a never-widen pair (COO half reads `write_one`'s rule for both branches: method differs -> write; method and
inputs equal -> 0), a change entry, `dossier --write --workers 10`, verify objects 468 -> 563, one new object per name,
`--pick-census stale_pick 0`, `--case-census`; the CVO grades AC3 on the served table.

<risk>SERVED</risk>
<status>pending</status>
<round>8</round>
<slot>~1</slot>
<fabric>site-z</fabric>
