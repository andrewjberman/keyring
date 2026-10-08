# TO ADVI_COTBKF.TO-CB-r-2.index-page-counts -- round 18 CB-r-2: the document index builder fills page_count from the documents

<to_id>ADVI_COTBKF.TO-CB-r-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~38</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-r-2` (`decompositions/ADVI_COTBKF_DECOMP.round18.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-5: a person searches Cottonwood's client documents by account, type and date and opens the one they need. The served index
`s3://opal-data-assets/commonwealth/cottonwood/silver/document_index/date=2026-06-23/document_index.parquet` (11,119 rows) is built
by `data/assets/scripts/silver/commonwealth_document_index.py` (`--source` the bronze imaging zips, `--data-date 2026-06-23`,
`--out`; `--apply` is the issuer's act and you never pass it). Its `page_count` comes only from the listing field `NumberOfPages`
(line 268), which no listing carries usefully, so every row is 0 or null. Round 17 counted pages from the served PDFs:
`data/assets/scripts/analysis/commonwealth_page_counts.py` -> `page_counts.csv` (`document_id, doc_type, page_count, reason`),
11,087 counted, 32 unreadable (31 not a PDF, 1 encrypted); the committed csv is
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~36/page_counts.csv`.

**Your item.**
1. The builder takes `--page-counts <csv>`; when given, each row's `page_count` is that csv's count for its `document_id` (null for
   an unreadable one); without it the builder behaves exactly as today. No other column and no schema change;
2. a read-only checker `data/assets/scripts/silver/commonwealth_index_page_diff.py`: build the index locally with `--page-counts`,
   read the SERVED index (record its VersionId), and compare row by row; LAST line exactly:
   `INDEX-PAGE-DIFF rows=<n> served_version=<VersionId> only_page_count_differs=<True|False> filled=<f> null=<u> other_columns_differing=<k>`
   and write `index_page_diff.md` to `--out` listing the 32 null rows with their reasons (document id, type, reason; never content).
The local build output stays under `.scratch/` (the issuer applies it later under a never-widen pair).

Tests: extend `data/assets/scripts/silver/tests/test_commonwealth_document_index.py` -- with a counts file, page_count is taken
from it and an unreadable id is null; without one, the output is unchanged (the control).

### ACCEPTANCE

<criterion id="CB18r2-AC1" cell_refs="CB-r-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_document_index.py -k page_count</invocation><expect>passed</expect></criterion>
`CB18r2-AC1` -- the counts file is read, the unreadable case is null, and the no-file control is unchanged.

<criterion id="CB18r2-AC2" cell_refs="CB-r-2"><invocation>python data/assets/scripts/silver/commonwealth_index_page_diff.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~38</invocation><expect>only_page_count_differs=True</expect></criterion>
`CB18r2-AC2` -- the local rebuild against the served index: only page_count moves, 11,087 filled and 32 null, recorded.

<expected_criteria>CB18r2-AC1,CB18r2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets named here; never
  `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Blank, never filled.** A value, return, month or page count that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W38-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_document_index.py
data/assets/scripts/silver/commonwealth_index_page_diff.py
data/assets/scripts/silver/tests/test_commonwealth_document_index.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round18.md</decomp_doc> (round 18), cell `CB-r-2`.
<owned_cells>CB-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB18r2-AC1, CB18r2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~38/ADVI_COTBKF.TO-CB-r-2.index-page-counts.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB18r2-AC1,CB18r2-AC2` BEFORE the flip. Mechanical: CB18r2-AC1, CB18r2-AC2; a judgment
criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the INDEX-PAGE-DIFF line, the served VersionId, the 32 null rows by reason, the local build path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the rebuild compared to the SERVED bytes with its VersionId; only page_count may move; BLIND: none -- the apply is a separate act under a pair.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-17 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_17_20261008.md` @0ae2f15e5c (msg 1185); decomposition round 18.
