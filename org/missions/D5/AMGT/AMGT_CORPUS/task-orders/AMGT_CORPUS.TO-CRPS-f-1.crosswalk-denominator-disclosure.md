# AMGT_CORPUS task order -- `CRPS-f-1` -- ROUND 4: the served crosswalk DISCLOSES the denominator it carries -- the count of folders in its own records and the live research directory's count join the denominators block, and the 2026-09-10 snapshot's 89 reads as the snapshot it is

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-f-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates (G-3 CTO, G-7 POD4), 0 on these surfaces (C1=23 C2=5 C3=12 C4=21 C5=334); no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes no S3 object; the one put of the rebuilt document is the issuer's drain act under its own pair.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 4. Serves **FWD-19**: the completion test's denominator.

## 1. THE CELL -- `CRPS-f-1`

**Where this came from.** The served crosswalk (`s3://opal-data-harvest/crosswalk/v1/2026-09-25.json`) carries 235 records over
94 distinct folders (`source_row.folder`), but its `denominators.input_names` reads 89 and its `coverage_vintage.denominator_folders`
reads 89 -- both copied from the coverage input file (`crosswalk.coverage_path()`, a 2026-09-10 snapshot of the research
directory). A reader checking "94 of 94" against the object's own block gets 89. The CTO's ruling (round-3 analysis s.2): the
object must disclose the denominator it carries. This is a DISCLOSURE fix: no record, key, association form or resolution changes.

**RULED -- what you build:**
- `crosswalk.build_crosswalk` gains an optional `research_folders=None` argument: the live research directory's folder names.
  When given, the document's `denominators` block gains `research_folders_live` (their count) and the document gains
  `research_universe`: `{"source": "<the root path given>", "read_at": "<UTC ISO>", "folders": <count>}`. When not given, both are
  ABSENT with a reason field (`research_universe: {"absent": "<why>"}`), never guessed.
- `denominators` ALWAYS gains `folders_in_records`: the count of distinct non-empty `source_row.folder` over `records`.
- `coverage_vintage` gains `snapshot_stale_against_live`: True when `research_folders_live` is present and differs from
  `denominator_folders`; absent otherwise. `input_names` and `denominator_folders` keep their values (they describe the input).
- The callers that build on this box pass the live list: `add_security._build_document` and `crosswalk.main` read it from
  `lib.research.corpus.library.list_folders(library.library_root())` (import inside the function; a failure to read the library
  leaves the fields absent-with-reason and never fails the build).
- `python -m lib.research.identity.crosswalk --disclosure --as-of <date>`: read-only (NO put, NO registrations write), builds that
  day's document in memory exactly as `--write-pool` would and prints ONE line:
  `folders_in_records <n> research_folders_live <m> snapshot_input_names <s> snapshot_stale_against_live <True|False>`.
- `tests/test_crosswalk_disclosure.py`: a fixture build with and without `research_folders`, the stale flag both ways, the
  absent-with-reason branch, and that no record/key/form differs between a build with and without the live list.
- `tests/test_crosswalk_enrich_coverage.py::NoEnrichRowsByteIdentical` is RED at HEAD (1 failed, 109 passed): it builds the
  pinned and the current module over the LIVE registrations minus ENRICH rows, and the issuer's re-mint (@c79872b0ff) added a
  keyed APPEND row for `Quanta Services PWR` beside its earlier KEYLESS row -- the current builder supersedes the keyless row
  (@9ec1226a01), the pinned module cannot, so the outputs differ by one record (97 vs 96). RULED fix: that arm also drops a
  keyless row whose folder carries a keyed row in the same filtered set, exactly as it already drops folders the coverage list
  carries as UNRESOLVED (the remedy has its own arm). The property the test proves is unchanged.

## 3. SURFACES

<paths>
lib/research/identity/crosswalk.py
lib/research/identity/add_security.py
lib/research/identity/tests/test_crosswalk_disclosure.py
lib/research/identity/tests/test_crosswalk_enrich_coverage.py
lib/research/identity/crosswalk.schema.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-f-1.crosswalk-denominator-disclosure.md
</paths>

READ-ONLY: `lib/research/corpus/`, `lib/research/identity/registrations.json`, every other identity module. Scratch `.scratch/f1/`.

**ISSUER AMENDMENT 1 (2026-09-25 ~04:1xZ, `2.0.0_SA_COO~X`, on your row `AMGT_CORPUS-Z-W1-S7`):** the ruled fields are refused by
`lib/research/identity/crosswalk.schema.json`'s `additionalProperties: false`, which this order did not grant -- the issuer's
cut. The schema file is now in `<paths>`. RULED: add `folders_in_records` and `research_folders_live` to `denominators`,
`snapshot_stale_against_live` to `coverage_vintage`, and `research_universe` at the top level, each an OPTIONAL property in the
schema's existing pattern (as `registered`/`enriched`/`resolved_folders` are), `research_universe` admitting both its present
shape and its `{"absent": ...}` shape. Nothing else in the schema moves; keep its line endings.

## 4. BOUNDS
- Pure ASCII source, LF, Python 3.9-compatible. NO S3 write, NO `--write-pool`, NO change to `registrations.json`, NO change to
  any record, key, form or resolution. Other seats commit to this package: merge CLOUD into your branch before you close.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-f-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round4/f1_AC1.sh</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-f-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round4/f1_AC2.sh</invocation><expect>folders_in_records (\d+) research_folders_live \1 snapshot_input_names \d+ snapshot_stale_against_live (True|False)</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-f-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round4/f1_AC3.sh</invocation><expect>(?m)^\d+ passed in </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe: the builder's own read-only disclosure line shows the records' folder count EQUAL
  to the live directory's; AC3 the bound: the whole identity suite still passes (no record, key or form moved).

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-f-1.crosswalk-denominator-disclosure.proof_of_spec.json`
   (the shape of your e-5 instance in that dir).
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-3 analysis s.2 ruling 2 @`eaed38bac0`. The issuer's reading of "re-pin identity_universe to the live
research directory" is decomposition s.8 (the identity file stays an INPUT; the live directory becomes the disclosed DENOMINATOR);
the CTO may correct it. `2.0.0_SA_COO~Z` is told this cell holds `crosswalk.py` and `add_security.py` until it drains. Checks
dry-run at the base: AC1 FAIL (no such test file), AC2 FAIL (no `--disclosure` flag), AC3 FAIL at the base (the Quanta
supersession arm above, caused by the issuer's re-mint) -- this cell's ruled test fix is what turns it; recorded in the issuance commit.

<risk>SERVED</risk>
<status>pending</status>
<round>4</round>
<slot>~1</slot>
<fabric>site-z</fabric>
