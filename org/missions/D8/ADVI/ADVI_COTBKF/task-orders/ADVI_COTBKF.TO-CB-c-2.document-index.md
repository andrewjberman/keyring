# TO ADVI_COTBKF.TO-CB-c-2 -- round 3 CB-c-2: the document index -- the three imaging archives' 51 listings as one index, every PDF accounted for, each document once

<to_id>ADVI_COTBKF.TO-CB-c-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~9</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~C</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `CB-c-2` (`decompositions/ADVI_COTBKF_DECOMP.round3.md`) | **outcome_ref:** FWD-5 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-c-2`, FWD-5: "a person searches by account, document type and date and opens the one document they need, without unpacking an archive
by hand; a document that appears in more than one advisor's archive is listed once." C-DOCUMENTS: "The 51 listing files become one
de-duplicated document index (account, type, date, page count, source archive or archives)." You build the index builder and prove it on the
real archives into a LOCAL directory. You write NOTHING to S3: landing the archives and `--apply` are the issuer's acts.

**The input, measured.** `$HOME/Downloads/Files.zip` (READ ONLY) holds three imaging zips (each one advisor plan ID):
`HKE.zip` (1,554,270,895 bytes; 11,075 members: 11,033 PDF, 17 `Listing.csv`), `HJH.zip` (1,503,993,172; 11,042: 11,000 PDF, 17 listings),
`4XF.zip` (113,362,389; 2,498: 2,456 PDF, 17 listings): 24,489 PDFs, 51 listings. Inside each, one folder per document type -- ADVS
(advisor documents), CLNT (client documents), NCSD (non-Commonwealth scanned), QSMT (quarterly statements, empty), REPR (advisor reports),
STMT (monthly statements), TXRP (tax documents) -- with one sub-folder per rep code holding a `Listing.csv`, and the PDFs at paths such as
`REPR/REPR20251010211946KFX12236588.pdf`. Each zip has a vendor `ReadMe.txt`: read it first.
- Listing layouts differ by type (7 layouts). Measured: REPR header `ReportID, ReportSectionID, ReportVersionID, FileName, DocType, DocName,
  NumberOfPages`; STMT header `ReportID, ReportSectionID, ReportVersionID, FileName, Acct, DisplayName, StmtDate` (`StmtDate` as
  `YYYYMMDD`). Values carry a leading space; `ReportVersionID` a leading apostrophe. Read the other five from the files.
- The first STMT listing read held 5 rows against 7,724 STMT PDFs in that archive: a listing may not cover every PDF. **Account for every
  PDF:** indexed by a listing row, or present without one (`listed=False`, its type and date taken from the file name where the name carries
  them), and every listing row whose file is absent (`present=False`). Never drop either.
- Brief F4: 10,917 PDF paths of `HKE.zip` are also in `HJH.zip`, and 2,453 of `4XF.zip`'s are in both: three advisor views of largely the
  same documents. **De-duplicate WITHOUT reading the PDFs:** a document's identity is (file name, CRC-32, uncompressed size) from each zip's
  central directory (`zipfile.ZipInfo`), so the 3.2 GB is never read in full.

**Build `data/assets/scripts/silver/commonwealth_document_index.py`:**
1. CLI: `--source <path or s3://>` (the outer Box zip with `--outer` and the member names, or a bronze prefix holding the three zips),
   `--data-date 2026-06-23`, `--out <local dir>`, `--apply` (writes at
   `address('commonwealth', <scope>, 'silver', 'document_index', 'date=<data-date>')`; unit-tested on a stub, never run by you). Read the
   scope through `opal_naming.lookup`. Device-free (LD-0405).
2. One row per UNIQUE document: `document_id` (`<file name>|<crc32 hex>|<size>`), `file_name`, `doc_type` (the folder), `account`
   (`Acct` where the listing has it, else null), `doc_date` (`StmtDate` or the listing's date, else from the file name, else null, with
   `date_source` saying which), `doc_name`, `page_count`, `rep_codes` (list), `archives` (list of the zips holding it), `paths` (list of the
   in-zip paths), `listed` (bool), `listing_files` (list), plus `source_zip_sha256` per archive in a side table. Every listing column kept in a
   `listing_fields` map.
3. LAST line exactly:
   `DOCUMENT-INDEX archives=<a> listings=<l> pdfs=<p> accounted=<c> unique_documents=<u> listed=<k> unlisted=<n> listing_rows_without_pdf=<m>`.
4. Tests `data/assets/scripts/silver/tests/test_commonwealth_document_index.py` (fixture zips in `tmp_path`): two archives holding the same
   PDF (same name, CRC, size) give one row with both archives; same name and different CRC give two rows; an unlisted PDF is kept with
   `listed=False`; a listing row with no PDF is counted; the leading space and apostrophe are stripped; `--apply` writes the builder key on a stub.

### ACCEPTANCE

<criterion id="CB3c2-AC1" cell_refs="CB-c-2"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_document_index.py</invocation><expect>passed</expect></criterion>
`CB3c2-AC1` -- the index rules on fixtures, including the duplicate and the same-name-different-content controls.

<criterion id="CB3c2-AC2" cell_refs="CB-c-2"><invocation>python data/assets/scripts/silver/commonwealth_document_index.py --source "$HOME/Downloads/Files.zip" --outer HKE.zip HJH.zip 4XF.zip --data-date 2026-06-23 --out .scratch/advi_cotbkf/document_index</invocation><expect>DOCUMENT-INDEX archives=3 listings=51 pdfs=24489 accounted=24489</expect></criterion>
`CB3c2-AC2` -- the real archives: 51 listings read and every one of the 24,489 PDFs accounted for.

<expected_criteria>CB3c2-AC1,CB3c2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Local output under `.scratch/`, uncommitted.
- **No S3 write, no `--apply`, no AWS call.** The archives' landing and the apply are the issuer's acts.
- **The input is read-only;** never unpack an archive to disk (read members in memory).
- **Within 120 seconds** for CB3c2-AC2: open each inner zip without reading the PDFs (`zipfile` reads only the central directory and the
  listings; the outer member can be opened as a stream with `ZipFile(outer.open(name))`).
- **Rule 13:** a DS-lane script; your commit is a candidate; no `safe-deploy`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-W9-S<k>`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_document_index.py
data/assets/scripts/silver/tests/test_commonwealth_document_index.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round3.md</decomp_doc> (round 3), cell `CB-c-2`.
<owned_cells>CB-c-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB3c2-AC1, CB3c2-AC2. Instance at `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~9/ADVI_COTBKF.TO-CB-c-2.document-index.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB3c2-AC1,CB3c2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the `DOCUMENT-INDEX` line, the seven listing layouts as read, the listed/unlisted split per type, the schema, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a one-time builder.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the issuer's apply runs under the laptop profile into a new prefix of opal-data-assets.
comp-adversary: RUN -- the archives hold client documents (statements, tax forms): the index carries account, type, date and names, the PDFs stay in bronze, and nothing is unpacked here (unpacking is round 4 under C-DOCUMENTS); cross-firm (cottonwood scope); BLIND: whether listings cover the PDFs (measured partially: the worker accounts for every one).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.4 @51a7c07278 C-DOCUMENTS, FWD-5, backlog item 4; CTO msg 105855; decomposition round 3 (measured constraint 3).
