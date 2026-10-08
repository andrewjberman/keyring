# TO ADVI_COTBKF.TO-CB-q-3.page-counts -- round 17 CB-q-3: document page counts read from the documents themselves

<to_id>ADVI_COTBKF.TO-CB-q-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~36</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-q-3` (`decompositions/ADVI_COTBKF_DECOMP.round17.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-5: a person searches Cottonwood's client documents by account, type and date and opens the one they need. The served index
`s3://opal-data-assets/commonwealth/cottonwood/silver/document_index/date=2026-06-23/document_index.parquet` (11,119 rows, built by
`data/assets/scripts/silver/commonwealth_document_index.py`) has a `page_count` column that is 0 or null on every row (row D2-S26).
The issuer's read: `page_count` comes only from the archive listing's `NumberOfPages` field (`commonwealth_document_index.py:268`);
10,072 listings carry no such field and 1,034 carry it as "0".

**Your item.** Build `data/assets/scripts/analysis/commonwealth_page_counts.py`, read-only:
1. name the cause from the data: count, per doc_type, listings with no `NumberOfPages`, with "0", and with a positive value;
2. read every document's PDF from the served documents table
   (`s3://opal-data-assets/commonwealth/cottonwood/silver/documents/date=2026-06-23/documents.parquet` gives each `written_key`)
   and count its pages with `pypdf` (installed; nothing is downloaded); a PDF that cannot be read is null with its reason
   (encrypted, damaged, not a PDF), never guessed;
3. write `page_counts.csv` (`document_id, doc_type, page_count, reason`) and `page_counts.md` to `--out`; LAST line exactly:
   `PAGE-COUNTS documents=<n> counted=<c> unreadable=<u> listing_none=<a> listing_zero=<z> listing_positive=<p> cause=<one word>`.
The served index is NOT rewritten here; filling it is the issuer's apply afterwards, from your csv.

Tests `data/assets/scripts/analysis/tests/test_commonwealth_page_counts.py` (stubs, no AWS): a two-page PDF built in the test counts
2; bytes that are not a PDF give null with a reason.

### ACCEPTANCE

<criterion id="CB17q3-AC1" cell_refs="CB-q-3"><invocation>python -m pytest -q data/assets/scripts/analysis/tests/test_commonwealth_page_counts.py</invocation><expect>passed</expect></criterion>
`CB17q3-AC1` -- the page count and the unreadable case on stubs.

<criterion id="CB17q3-AC2" cell_refs="CB-q-3"><invocation>python data/assets/scripts/analysis/commonwealth_page_counts.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~36</invocation><expect>PAGE-COUNTS documents=11119</expect></criterion>
`CB17q3-AC2` -- every served document counted from its own bytes, the unreadable ones counted with their reason, and the cause named.

<expected_criteria>CB17q3-AC1,CB17q3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets named here; never
  `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Blank, never filled.** A value, return, month or page count that cannot be worked out is null with its reason, never estimated.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W36-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/analysis/commonwealth_page_counts.py
data/assets/scripts/analysis/tests/test_commonwealth_page_counts.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round17.md</decomp_doc> (round 17), cell `CB-q-3`.
<owned_cells>CB-q-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB17q3-AC1, CB17q3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~36/ADVI_COTBKF.TO-CB-q-3.page-counts.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB17q3-AC1,CB17q3-AC2` BEFORE the flip. Mechanical: CB17q3-AC1, CB17q3-AC2; a judgment
criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the PAGE-COUNTS line, the cause, the unreadable documents by reason, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- pages read from each document's own bytes, not the listing; an unreadable PDF is counted, never guessed; BLIND: documents that are images inside a PDF (pages count, content not read).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-16 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_16_20261007.md` @8b6829c89f (msg 1100); decomposition round 17.
