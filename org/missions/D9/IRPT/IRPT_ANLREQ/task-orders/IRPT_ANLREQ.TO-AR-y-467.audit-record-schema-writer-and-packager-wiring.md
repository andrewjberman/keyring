# TO IRPT_ANLREQ.TO-AR-y-467.audit-record-schema-writer-and-packager-wiring -- SCHEMA AND WRITER: publish AnalysisAudit.v1, build the audit record from the four linkages, validate it, write it once per request through the naming builder, and call it from the packager at attach time; offline, with tests

<to_id>IRPT_ANLREQ.TO-AR-y-467.audit-record-schema-writer-and-packager-wiring</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~341</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ126</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD | **Decomp cell:** `AR-y-467` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-AUDIT-RECORD (PRD v0.27) | **depends_on:** CTO msg 11466; the read of AR-y-462

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~341`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-341` (branch `wk-IRPT_ANLREQ-341`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~341 <0.9.0_WK_IRPT_ANLREQ~341@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W341-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** Terraform is not installed on this box: do not try to run it. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR467-y-AC1,AR467-y-AC2,AR467-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-467`, inlined)

*Context.* PRD v0.27 (`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`, the row beginning `C-AUDIT-RECORD:`; CTO ruling msg 11466): one audit JSON per analysis request in a NEW PLATINUM family `ANALYSIS_AUDIT` (table `analysis_audit`, extension json, `accepted_ceiling_days` 2555, `unreferenced_days` null) of the reporting policy revision `irpt-anlreq-x10-v1`, written by the packager at attach time (the hop that holds all four linkages), the form as filed taken from the ticket answers, validated against a published schema `AnalysisAudit.v1`. The read that grounds it: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~327/AUDIT_RECORD_READ.md` (read it first). Every new S3 address is `lib/opal_naming.py` `address()` output (CLAUDE.md rule 30).

*The change.* (1) New `infra/aws/lambda/investor-reporting/_contracts/AnalysisAudit.v1.schema.json` (JSON Schema Draft 2020-12, `additionalProperties: false` at the top level, `required` all of: `schema_version` const `AnalysisAudit.v1`, `request_id`, `firm_id`, `filed_at`, `ticket` {`ticket_id`, `ticket_type` const `analysis_request`}, `form_as_filed` (an object: the ticket answers as filed, no uploaded file content), `filer` {`principal_id`, `user_type`} (NO e-mail address, NO display name), `package` {`report_ref`, `pdf_ref`, `commentary_ref`, `original_ref`} (each a string pointer or null), `written_at`). Read the sibling `_contracts/AnalysisReport.v2.schema.json` for style. (2) New module `infra/aws/lambda/investor-reporting/reports/analysis_audit.py` (stdlib plus `jsonschema` imported lazily): `build_audit_record(...)` from the four linkages (the inputs as plain dicts the packager already holds: the ticket, the accepted request record with `owner.principal_id`, the package pointers, the commentary pointer); `validate(record)` using `jsonschema` Draft 2020-12 and raising a `ValidationUnavailable` error when the library cannot be imported (as `infra/aws/lambda/investor-reporting/export/bundle.py:74-88` does) and a `ValueError` naming the first schema error on a malformed record, so an unvalidated record is NEVER written; `audit_address(firm, request_id)` using `lib/opal_naming.py` `address()` (source `irpt`, the firm's scope, tier `platinum`, table `analysis_audit`; load the builder the way the other reports/ modules do, read `reports/` for the precedent; one key per request derived from the request id so a replay writes identical content to the same key); `write_audit(record, put_object)` taking an injected `put_object(bucket, key, body_bytes)` port, validating first, returning the address. (3) In `infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py` (read `handle_commentary_ready` and the attach path), call the writer ONCE after a successful attach, through the module's existing injected ports; a failure to write the audit must be recorded in the packager's existing outcome vocabulary and must NOT undo the attach (say in a comment why); no other behaviour of the packager changes. Also add `AnalysisAudit.v1.schema.json` wherever the resident package builder lists the `_contracts` it ships (read `reports/build_resident_package*.py`), additions only. (4) Tests in `infra/aws/lambda/investor-reporting/reports/tests/test_analysis_audit.py` (offline, no network): a good record validates and writes once to the builder address; each of the four linkages missing is rejected (four cases); `jsonschema` unavailable (monkeypatched import) refuses to write; the packager attach path writes exactly one audit and an audit failure leaves the attach standing; (e) the two cases the CVO grades (CTO msg 11472): a commentary failure at attach (`pdf_ref` and `commentary_ref` both null) STILL writes the record, and the schema admits exactly those two pointers as null (and rejects a null `report_ref`); a replace attach (`prior_attached_at` set on the ticket) writes the SAME address again with the new content and never a second address, so the injected port sees one distinct key per request across the first and the replace attach. Commit the schema, module, packager edit and tests as ONE commit (message citing AR-y-467), then your deliverables and instance.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~330/`: `check_audit_schema.py` (stdlib plus `jsonschema` if importable in this tree's interpreter; if it is NOT importable here, say so in a surprise row and validate with a minimal in-script checker instead) prints `AUDIT-SCHEMA-OK good=1 bad_rejected=4` when the schema meta-validates, the good sample passes and the four one-linkage-missing samples are rejected; `check_audit_wired.py` reads `opal_packager.py` by AST and prints `AUDIT-WIRED-OK calls=1 after_attach=yes` when exactly one call to the writer sits after the attach in the commentary-ready path, else `AUDIT-WIRED-BAD <why>`. Criterion AC2 is the new test file run with pytest.

*AMENDMENT 1 (issuer, 2026-10-20 ~18:3xZ, from worker 342's row W342-S2 and the issuer's own probe).* The ruling behind all three: the client firms' own buckets are FENCED (`shared-infra/s3-lgic-firm-buckets.tf`, Sid `DenyForeignFirmPrincipals`, read in `infra/aws/terraform/investor-reporting/ycharts/resident.tf` lines 229-241): they deny every principal that does not carry the firm's own slot, and widening the fence to the resident role is the cross-firm act CLAUDE.md forbids. Every other `irpt` retained family (commentaries, compositions, analysis reports) is addressed by `lib/opal_naming.py` `reporting_destination(firm, family, artifact_id, sha256, *, policy_revision)`, which returns the PRODUCT bucket `opal-data-irpt` and the key `irpt/<firm>/<tier>/<table>/ART-<hex64>/<sha256>.<ext>` (the issuer ran it: ANALYSIS_COMMENTARY of `irpt-anlreq-x10-v1` for `49financial` gives `('opal-data-irpt', 'irpt/49financial/state/analysis_commentaries/ART-.../....json')`). The audit family `ANALYSIS_AUDIT` is addressed the same way, so the audit record lives under `opal-data-irpt/irpt/<firm>/platinum/analysis_audit/`, not in a firm bucket. (The PRD's words 'in each firm's bucket' and the AR-y-462 read's per-firm-bucket reading are superseded by this; the CTO is told.) FOR THIS ORDER: `audit_address(firm, request_id)` calls `reporting_destination(firm, 'ANALYSIS_AUDIT', artifact_id, sha256, policy_revision='irpt-anlreq-x10-v1')`, never `address()` with a firm scope. Because the builder puts a sha256 in the key, the key must NOT depend on the record's content or a replace attach would write a SECOND key: use `artifact_id = 'ART-' + sha256(request_id)` and `sha256 = sha256(request_id)` (a stable name, not a content hash; say so in a comment and in the test), so a replace attach writes the same key again (the versioned bucket keeps the superseded content as a prior version). The test of the replace case asserts the two puts hit the identical `(bucket, key)`. The record is written through the packager's existing writer port for the reporting bucket; if the packager has no such port, say so in a surprise row and use an injected `put_object(bucket, key, body_bytes)` as the order says. If you have already built on `address()`, change it in a new commit; keep the earlier commits.

---

## ACCEPTANCE

<criterion id="AR467-y-AC1" cell_refs="AR-y-467"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~341/check_audit_schema.py</invocation><expect>^AUDIT-SCHEMA-OK good=1 bad_rejected=4$</expect></criterion>
<criterion id="AR467-y-AC2" cell_refs="AR-y-467"><invocation>python -m pytest infra/aws/lambda/investor-reporting/reports/tests/test_analysis_audit.py -q 2>&1 | tail -1</invocation><expect>^[0-9]+ passed</expect></criterion>
<criterion id="AR467-y-AC3" cell_refs="AR-y-467"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~341/check_audit_wired.py</invocation><expect>^AUDIT-WIRED-OK calls=1 after_attach=yes$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~341/IRPT_ANLREQ.TO-AR-y-467.audit-record-schema-writer-and-packager-wiring.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-467.audit-record-schema-writer-and-packager-wiring`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR467-y-AC1,AR467-y-AC2,AR467-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-467</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/_contracts/AnalysisAudit.v1.schema.json
infra/aws/lambda/investor-reporting/reports/analysis_audit.py
infra/aws/lambda/investor-reporting/reports/tests/test_analysis_audit.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py
infra/aws/lambda/investor-reporting/reports/build_resident_package.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~341/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-467.audit-record-schema-writer-and-packager-wiring.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- files named in `<paths>` plus checks in the worker deliverables; nothing is planned, applied, deployed or run against AWS; the release and apply are later orders under a signed pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the CTO ruling (msg 11466), the PRD row and the AR-y-462 read against this cell; the lens: an email or display name in the record (forbidden: principal id and user type only), a writer that writes before it validates, a missing jsonschema treated as valid, an audit failure that undoes the attach, two writes per request, a typed bucket or key, a packager edit that changes anything else, the build lister left without the schema. NOT seen (blind): whether `jsonschema` is installed on the resident host (a separate IB2 read) and the live buckets; denominator: three criteria.
</preflight>
