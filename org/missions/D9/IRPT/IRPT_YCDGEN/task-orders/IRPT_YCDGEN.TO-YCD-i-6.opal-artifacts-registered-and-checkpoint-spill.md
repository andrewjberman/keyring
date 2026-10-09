# IRPT_YCDGEN task order -- `YCD-i-6` -- ROUND 6 (THREAD): THE OPAL ARTIFACTS: A REGISTERED PDF FAMILY, THE PRODUCER RETAINS IT, AND THE DOCUMENT SPILLS OUT OF THE CHECKPOINT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6B.md</decomp_doc>
<owned_cells>YCD-i-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-i-6.opal-artifacts-registered-and-checkpoint-spill</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~3</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; the resident host's role is proved by the issuer's close run
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-i-6` -- the opal artifacts: a registered pdf family, the producer retains it, and the document spills out of the checkpoint (hops 7 Persist (artifacts); FWD-1)
- `infra/logic/registry/reporting_policies.json` and `lib/tests/test_irpt_destination.py`: R9 (1).
- `ycharts/research/opal_producer.py` and its test: R9 (2).
- `ycharts/generate/publisher.py`, `ycharts/generate/publication_worker.py` and their tests: R9 (3), and the publisher takes the producer's retained PDF ref.
- Keep every existing test in those files passing.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R9 The Opal artifacts are retained in registered families, and the checkpoint stays small.** (1) The Opal report PDF is retained through the reporting repository's `ArtifactRepository.put` in a family registered for it: add family `OPAL_REPORT_PDF` (tier `state`, extension `pdf`, the retention fields of its sibling `ORIGINAL_VENDOR_PDF`) to `infra/logic/registry/reporting_policies.json` under the policy `irpt-x10-v1`, with its table name drawn from the builder's registered grammar (`lib/opal_naming.py`; a builder REFUSAL is a missing registry row to add in `infra/logic/registry/`, never a hand-typed name), and add it to `FAMILIES` in `lib/tests/test_irpt_destination.py`. (2) `opal_producer.produce` retains the PDF through `put` and returns the retained `artifact_ref`; the publisher takes that ref (today the producer writes the PDF straight to the `ycharts_opal_reports` family through an injected put_object and no retained ref exists). (3) A full OPAL_ENGINE document can exceed the job store's 32 KiB checkpoint (`CHECKPOINT_BYTES`, refusal `WORKER_CHECKPOINT_SIZE`): the Opal path spills the document to a retained artifact of an EXISTING registered json family (prefer one already registered; name your choice in a surprise row; add a family only if none fits), and the checkpoint carries the artifact ref and the document's sha256, never the document. The vendor path's spill of its census to `EXTRACTION_EVIDENCE` is the model. Function signatures `produce` and the publisher's public entry points keep their present shape for their callers. The YCharts path is unchanged: every existing test passes and a v1 document persists byte-equal.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: worker rows IRPT_YCDGEN-W3-S8 and W3-S11 (and W3-S10, the Opal state sequence RECEIVED -> CERTIFYING -> READY) in `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md`; `infra/logic/registry/reporting_policies.json` (the family rows; sibling `ORIGINAL_VENDOR_PDF`, `EXTRACTION_EVIDENCE`); `lib/tests/test_irpt_destination.py` (`FAMILIES`); `lib/opal_naming.py`; the reporting repository (`reports/repository.py` and the `ArtifactRepository.put` it exposes); `publisher.py` (`metadata_kind`, `_publish_opal`, `OPAL_FAMILY`) and `publication_worker.py` (`checkpoint_pdf`, `finish`, the vendor census spill) merged from g-6.
- Code lives under `infra/aws/lambda/investor-reporting/` except the registry and `lib/`. The registry file is validated by a refusing validator: a bad row is refused, so run its own tests.
- Writer read: `resident_worker.py` is not in your paths (cell d-6 writes it); the three persist files were last written by g-6 (merged), and no other non-terminal order names any of your files.
- Tests use fakes for every store; no live AWS call.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W3-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/logic/registry/reporting_policies.json
lib/tests/test_irpt_destination.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/generate/publisher.py
infra/aws/lambda/investor-reporting/ycharts/generate/publication_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publisher.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publication_worker.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the registry holds family OPAL_REPORT_PDF and the repository put of that family succeeds (tests -k opal_report_pdf_family, >= 1 passed)
- **AC2** -- the producer retains the PDF through put and returns its artifact_ref (tests -k retains_pdf_artifact, >= 1 passed)
- **AC3** -- a document larger than the checkpoint limit is persisted and its checkpoint stays within the limit (tests -k opal_document_over_checkpoint_limit, >= 1 passed)
- **AC4** -- the Opal checkpoint carries an artifact ref and a sha256 and not the document (tests -k opal_checkpoint_is_a_reference, >= 1 passed)
- **AC5** -- a v1 document persists byte-equal to what the unchanged publisher persisted (tests -k v1_document_persists_byte_equal, >= 1 passed)
- **AC6** -- the whole publisher test file passes (tests, all, no failure)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-i-6"><invocation>python -m pytest lib/tests/test_irpt_destination.py -q -p no:cacheprovider -k opal_report_pdf_family</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-i-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer.py -q -p no:cacheprovider -k retains_pdf_artifact</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-i-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publisher.py -q -p no:cacheprovider -k opal_document_over_checkpoint_limit</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-i-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publication_worker.py -q -p no:cacheprovider -k opal_checkpoint_is_a_reference</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC5" cell_refs="YCD-i-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publisher.py -q -p no:cacheprovider -k v1_document_persists_byte_equal</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC6" cell_refs="YCD-i-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_publisher.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~3/IRPT_YCDGEN.TO-YCD-i-6.opal-artifacts-registered-and-checkpoint-spill.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-i-6.opal-artifacts-registered-and-checkpoint-spill`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~3`, second order (after g-6, merged); addendum B cell (decomposition IRPT_YCDGEN_DECOMP_R6B.md), cut by the issuer to disarm worker rows W3-S8 and W3-S11 (measured gaps in the live thread: no registered PDF family and a checkpoint that a full document overflows). AC2 runs in test_opal_producer.py, AC1 in test_irpt_destination.py and AC4 in test_publication_worker.py. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~23:3xZ):** worker 0.9.0_WK_IRPT_YCDGEN~3 @e923e0f463, merged 14eb4d115d (investigations-file conflict resolved as a union); i-6.AC1-AC6 PASS on the merged tree (AC6: 25 passed), instance VALID; with d-6 merged the persist, worker, producer and installer tests pass together (103 passed, 8 skipped; lib test_irpt_destination 76 passed). Family OPAL_REPORT_PDF registered (table opal_report_documents); the Opal document spills unconditionally to the existing family EXTRACTION_EVIDENCE (W3-S13 INERT, accepted) and the checkpoint is {pdf_ref, census, metadata_ref, metadata_sha256}. Rows W3-S8 and W3-S11 DISARMED by this cell. W3-S15 ARMED (produce retains the PDF only when its caller injects stores['artifacts']) -> DISARMED by cell YCD-k-6. W3-S16 INERT, accepted (run.json's report.key still names the layout's S3 address where no object is written; artifact_ref is the true location). **W3-S14 ARMED, NOT DISARMED:** adding the family changed irpt-x10-v1's policy_sha256 (e0046398 to a65635d3) and reports/retention.py:108-113 refuses any retention row stored under the old digest once the deployed registry carries the new one; the registry change is NOT SHIPPED and the CTO is asked to rule (a new policy version, a migration, or acceptance) in msg 20261005T233433Z; the registry file is merged to CLOUD but deployed nowhere.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<workstream>R6B_ARTIFACTS</workstream>
<slot>~3</slot>
<fabric>laptop</fabric>
