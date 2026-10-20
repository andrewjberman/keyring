# TO IRPT_ANLREQ.TO-AR-y-469.audit-record-live-wiring-ticket-source-and-reporting-put-in-the-resident-worker -- BUILD OFFLINE: give the packager's two optional audit ports (audit_source, audit_put) their live implementations in the resident worker, so a real attach writes the audit record; offline, with tests; nothing is released or deployed

<to_id>IRPT_ANLREQ.TO-AR-y-469.audit-record-live-wiring-ticket-source-and-reporting-put-in-the-resident-worker</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~343</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ128</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-469` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-AUDIT-RECORD (PRD v0.28) | **depends_on:** AR-y-467 (worker 341: the schema, `reports/analysis_audit.py` and the packager's optional ports `audit_source` and `audit_put`; its branch `wk-IRPT_ANLREQ-341` is not drained yet: read its commits there with `git show wk-IRPT_ANLREQ-341:<path>` until the issuer tells you it is on the trunk), AR-y-466 (the family row, trunk 5143b9b2565), worker 341's rows W341-S2, S3, S10

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~343`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-343` (branch `wk-IRPT_ANLREQ-343`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~343 <0.9.0_WK_IRPT_ANLREQ~343@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W343-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first), with `to_id` exactly the order's id, a `controls.mutant` that FIRES and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "AR469-y-AC1,AR469-y-AC2,AR469-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID.

### THE CELL (`AR-y-469`, inlined)

*Context.* PRD v0.28 C-AUDIT-RECORD (CTO ruling msgs 11466, 11484): one audit JSON per analysis request at `opal-data-irpt/irpt/<firm>/platinum/analysis_audit/`, written by the packager after each successful attach. Worker 341 built the schema, the validating writer (`infra/aws/lambda/investor-reporting/reports/analysis_audit.py`) and the packager's call (`infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py`), with TWO OPTIONAL ports the live caller does not supply: `audit_source(ticket_id)` (the ticket side: `{ticket_id, ticket_type, answers, filed_at, filer_user_type, ...}` as worker 341 defined it; read its definition in `analysis_audit.py` and the packager) and `audit_put(bucket, key, body_bytes)`. Without them a live attach records `AUDIT_PORTS_UNWIRED` and writes nothing. The live caller is the resident worker `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`. The resident already reads the ticket table with one consistent `GetItem` in `ycharts/generate/ticket_confirmation.py` (`make_confirm_ticket(dynamodb, table_name)`, pure, no logging, every exception False); the ticket service that WRITES the item is `ticket_center/lambda_function.py` (find its path; read how a ticket item stores its `answers`, creation time and requester).

*The change.* (1) New module `infra/aws/lambda/investor-reporting/ycharts/generate/ticket_audit_source.py`, pure and in the style of `ticket_confirmation.py`: `make_audit_source(dynamodb, table_name)` returns `audit_source(ticket_id)` doing ONE consistent `GetItem` on the ticket table and returning the ticket side of the audit input in worker 341's shape from the item's real attributes (answers as filed, the creation time as `filed_at`, the requester's user type as `filer_user_type`), or `None` on any miss or exception; it returns NO e-mail address and no display name in any field (the audit schema forbids them), and it does not log. (2) In `resident_worker.py`, where the packager is called (read how `package_on_ready` and the commentary signal build its ports and stores), supply `audit_source` from (1) over the same ticket table and DynamoDB client the confirm port uses, and `audit_put` as a function that puts the body with the resident's own S3 client to the REPORTING bucket the resident already writes its other reporting objects to (find it: the same bucket as the `ycharts_opal_reports` and `analysis_commentaries` families, NOT a firm bucket; read how the worker resolves that bucket and use the same variable), adding no new environment variable if one exists. If the resident has no S3 client for that bucket in this code path, say so in a surprise row and use the narrowest existing one. (3) Tests in `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_audit_live_wiring.py` (offline): a fake DynamoDB item yields the audit input with no `@` in any value; a miss and an exception yield `None`; the resident worker's packager call passes both ports (a recording fake); an attach through the recording fakes ends with exactly one `put` to `opal-data-irpt` at `irpt/<firm>/platinum/analysis_audit/` and not `AUDIT_PORTS_UNWIRED`. Commit the module, the worker edit and the tests as ONE commit (message citing AR-y-469), then your deliverables and instance.

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~343/`: `check_audit_live_wired.py` (stdlib only, ruff clean, offline) reads `resident_worker.py` by AST and prints `AUDIT-LIVE-WIRED-OK source=yes put=yes` when the packager call supplies both ports from `make_audit_source` and an S3 put function, else `AUDIT-LIVE-WIRED-BAD <why>` (rc 1); `--selftest` removes each port in memory in turn and prints `CONTROL-FIRES` only when BOTH removals read BAD; `check_audit_source_clean.py` runs the source against a fake item that carries an e-mail address and a display name and prints `AUDIT-SOURCE-CLEAN-OK no_email=yes no_name=yes` only when no output value contains the address or the name.

*AMENDMENT 1 (issuer, 2026-10-20 ~19:5xZ, ruling on your BLOCKING rows IRPT_ANLREQ-D2-W343-S1 and S2).* S1 TAKEN (my error: the order named the wrong file): the packager's ports are built in `infra/aws/lambda/investor-reporting/reports/resident_installed.py` `make_packager` (near lines 469-475), not in `resident_worker.py`, which only receives the packager as an injected callable. Supply `audit_source` (from `make_audit_source` over the same ticket table and DynamoDB client the `make_packager` already uses for its other ports) and `audit_put` (to the reporting bucket through the S3 client `make_packager` already builds for the reporting repository, bucket from the variable it already reads) THERE. `resident_worker.py` and `ycharts/generate/ticket_confirmation.py` are NOT edited; if you left a change in `resident_worker.py` revert it in a new commit. S2 TAKEN: the ticket writer stores no user type, and the audit must not fail for want of one. In `AnalysisAudit.v1.schema.json` `filer.user_type` becomes a string OR null (the key stays required); `reports/analysis_audit.py` takes it from `audit_source` when present and sets it to null otherwise; `ticket_audit_source.py` returns the ticket's own user type only if the item carries one (read the ticket writer to see) and `None` otherwise, never a guess. In `reports/tests/test_analysis_audit.py` change only what the old requirement asserted (a record with `user_type` null validates; a record with the `user_type` key MISSING is rejected); every other test stays green (24 before). S3 and S4 accepted. The write set of this order is therefore: `ticket_audit_source.py` and `tests/test_audit_live_wiring.py` (yours), `reports/resident_installed.py`, `_contracts/AnalysisAudit.v1.schema.json`, `reports/analysis_audit.py`, `reports/tests/test_analysis_audit.py`, plus your deliverables, this order and the investigation file. The tests of your own file must now include the packager-call test and the one-put test the grant blocked before: build the packager through `make_packager` with recording fakes for DynamoDB and S3 and assert both ports are supplied and that one attach ends with exactly one put to `opal-data-irpt` under `irpt/<firm>/platinum/analysis_audit/`. The `--selftest` of `check_audit_live_wired.py` (each port removed in turn reads BAD) now has a baseline that reads OK, so it can fire. Take this amended order onto your branch first (committed alone), then do the above in new commits, re-run all three criteria, and flip `<status>` to `complete` with the instance only on VALID.

---

## ACCEPTANCE

<criterion id="AR469-y-AC1" cell_refs="AR-y-469"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_audit_live_wiring.py -q --color=no -p no:cacheprovider 2>&1 | tail -1</invocation><expect>^[0-9]+ passed</expect></criterion>
<criterion id="AR469-y-AC2" cell_refs="AR-y-469"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~343/check_audit_live_wired.py</invocation><expect>^AUDIT-LIVE-WIRED-OK source=yes put=yes$</expect></criterion>
<criterion id="AR469-y-AC3" cell_refs="AR-y-469"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~343/check_audit_source_clean.py</invocation><expect>^AUDIT-SOURCE-CLEAN-OK no_email=yes no_name=yes$</expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~343/IRPT_ANLREQ.TO-AR-y-469.audit-record-live-wiring-ticket-source-and-reporting-put-in-the-resident-worker.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-469.audit-record-live-wiring-ticket-source-and-reporting-put-in-the-resident-worker`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR469-y-AC1,AR469-y-AC2,AR469-y-AC3"`; flip `<status>` to `complete` only when it prints VALID. The controls: the mutant is the `--selftest` of `check_audit_live_wired.py`.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-469</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/ticket_audit_source.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_audit_live_wiring.py
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/_contracts/AnalysisAudit.v1.schema.json
infra/aws/lambda/investor-reporting/reports/analysis_audit.py
infra/aws/lambda/investor-reporting/reports/tests/test_analysis_audit.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~343/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-469.audit-record-live-wiring-ticket-source-and-reporting-put-in-the-resident-worker.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one new module, one edit to the resident worker and tests, plus checks in the worker deliverables; nothing is released, deployed or run against AWS; the resident release that ships it (with AR-y-467) and the IAM apply of AR-y-468 are later orders under a signed pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker; the ticket table read reuses the resident's existing GetItem grant (the confirm port), the reporting put needs the AR-y-468 statement.
comp-adversary: RUN -- by reading worker 341's rows W341-S2, S3, S10 and the resident code against this cell; the lens: an e-mail address or display name in an audit value, a source that logs or lets an exception text out, a put to a firm bucket (fenced) instead of the reporting bucket, a new environment variable where one exists, a packager call that still passes only one port, a worker edit that changes any other behaviour of the attach, a ticket attribute name assumed instead of read from the ticket service's writer. NOT seen (blind): the live ticket table item shape beyond what the ticket service writes, the resident host's environment; denominator: three criteria.
</preflight>
