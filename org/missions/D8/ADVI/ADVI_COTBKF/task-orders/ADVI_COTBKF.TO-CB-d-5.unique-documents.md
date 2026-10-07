# TO ADVI_COTBKF.TO-CB-d-5 -- round 4 CB-d-5: C-DOCUMENTS -- each unique document unpacked once from bronze into the documents table

<to_id>ADVI_COTBKF.TO-CB-d-5</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~16</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-d-5` (`decompositions/ADVI_COTBKF_DECOMP.round4.md`) | **outcome_ref:** FWD-5 |
**depends_on:** none (the three imaging archives landed in bronze, ledger @97463796de)

---

## WORKER FACE

### THE CELL

`CB-d-5`, FWD-5: "a person searches by account, document type and date and opens the one document they need, without unpacking an archive
by hand; a document that appears in more than one advisor's archive is listed once." Contract C-DOCUMENTS: the 51 listings became one
de-duplicated index (round 3, done); **each UNIQUE document is unpacked once into a declared documents table; the three archives also stay
whole in bronze.** You build the unpacker and prove it plans every document once against the real archives. You write NOTHING to S3:
`--apply` is the issuer's act.

**The data, measured at the cut.**
- The index: `address('commonwealth', <cottonwood scope via lookup>, 'silver', 'document_index', 'date=2026-06-23')`, file
  `document_index.parquet`: 11,119 rows, columns `document_id, file_name, doc_type, account, doc_date, date_source, doc_name, page_count,
  rep_codes, archives, paths, listed, present, listing_files, listing_fields`. Every row present and listed. `document_id` =
  `<file_name>|<crc32 hex>|<bytes>`; `paths` lists every copy as `<archive>:<member path>` (24,489 paths: 202 documents in 1 archive, 8,464
  in 2, 2,453 in 3). Doc types STMT 7,736, NCSD 1,239, TXRP 1,034, CLNT 932, ADVS 165, REPR 13.
- The archives in bronze: `address('commonwealth', <scope>, 'bronze', 'imaging', 'date=2026-06-23', object='plan_id=<ID>/<ID>.zip')` for
  `HKE` (1,554,270,895 B), `HJH` (1,503,993,172 B), `4XF` (113,362,389 B). Read a member by HTTP range reads of the zip (its central
  directory at the tail, then the member's local header and data) -- never download a whole archive in a criterion run.

**Build `data/assets/scripts/silver/commonwealth_documents.py`:**
- For each index row choose ONE source path (the first archive in `paths` order, deterministic) and verify from that archive's central
  directory that the member exists and its CRC-32 and uncompressed size equal the `document_id`'s. A mismatch is REFUSED (listed, never
  written).
- The object for each document: `address('commonwealth', <scope>, 'silver', 'documents', 'date=2026-06-23',
  object='doc_type=<DOC_TYPE>/<file stem>_<crc32 hex>.pdf')` -- unique per document by construction; assert no two documents share a key.
- `--plan` (the default): reads only the three central directories plus the index; writes `documents_plan.parquet` (document_id, doc_type,
  account, doc_date, source path, bytes, crc32, target key) under `--out`; LAST line exactly
  `DOCUMENTS-PLAN unique=<n> every_document_once=<True|False> sources_verified=<v> refused=<r> keys_unique=<True|False> bytes=<total>`.
- `--apply` (never run by you; unit-tested on a stub): streams each chosen member out of its archive by range reads, inflates it, checks
  CRC-32 and size, computes SHA-256, writes it once (refuses a DIFFERENT existing object at the key; skips an identical one), and finally
  writes `documents.parquet` (the plan plus `sha256` and the written key) at the table root
  `address(..., 'silver', 'documents', 'date=2026-06-23')`.

**Tests** `data/assets/scripts/silver/tests/test_commonwealth_documents.py` (fixture zips built in the test, a stub S3 that serves byte
ranges; no AWS): a document present in two archives is planned and written ONCE; a CRC mismatch is refused; two documents with one file name
and different CRCs get two keys; `--apply` on the stub writes each once and refuses a different existing object; the range reader inflates a
deflated member correctly.

### ACCEPTANCE

<criterion id="CB4d5-AC1" cell_refs="CB-d-5"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_documents.py</invocation><expect>passed</expect></criterion>
`CB4d5-AC1` -- once-per-document, refusal on a CRC mismatch, and the range reader, on fixtures.

<criterion id="CB4d5-AC2" cell_refs="CB-d-5"><invocation>python data/assets/scripts/silver/commonwealth_documents.py --plan --out .scratch/advi_cotbkf/documents_plan</invocation><expect>DOCUMENTS-PLAN unique=11119 every_document_once=True sources_verified=11119 refused=0 keys_unique=True</expect></criterion>
`CB4d5-AC2` -- the real index against the real bronze archives: all 11,119 documents planned once, each source verified.

<criterion id="CB4d5-AC3" cell_refs="CB-d-5" judgment="true"/>
`CB4d5-AC3` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9 after the issuer's apply: one statement and one tax form found by account and date
in the documents table and opened (FWD-5's DONE WHEN).

<expected_criteria>CB4d5-AC1,CB4d5-AC2,CB4d5-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Local output and caches under `.scratch/`, uncommitted.
- **No S3 write, no `--apply`;** S3 READS only of this project's silver index and bronze imaging archives (range reads); never another bucket.
- **Within 120 seconds** for CB4d5-AC2 (three central directories, a few MB of range reads; cache them under `.scratch/` if needed and say so).
- **Rule 13:** a DS-lane script; your commit is a candidate. **Rule 30:** every address is builder output.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W16-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_documents.py
data/assets/scripts/silver/tests/test_commonwealth_documents.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round4.md</decomp_doc> (round 4), cell `CB-d-5`.
<owned_cells>CB-d-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB4d5-AC1, CB4d5-AC2, CB4d5-AC3 (judgment: UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO; never PASS or
FAIL). Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~16/ADVI_COTBKF.TO-CB-d-5.unique-documents.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB4d5-AC1,CB4d5-AC2,CB4d5-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `DOCUMENTS-PLAN` line, the planned bytes, three planned rows (one STMT, one TXRP, one in three archives), commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time builder.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; reads this project's silver and bronze under the laptop profile.
comp-adversary: RUN -- once per document (CRC + size from the central directory, not the file name); refuses a different existing object; archives stay whole in bronze; BLIND: document content (a PDF that is itself a duplicate under a different CRC, e.g. re-rendered) -- the index's identity, not this cell's.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD C-DOCUMENTS, FWD-5; CTO analysis enrichment item 5 (msg 105940); decomposition round 4 (measured constraint 5).
