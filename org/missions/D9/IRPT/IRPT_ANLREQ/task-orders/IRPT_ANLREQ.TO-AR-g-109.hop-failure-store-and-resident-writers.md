# TO-AR-g-109 -- the set-once hop_failure store method on the job row, and its two resident writers (the ready-signal send and the packager) (C-HOP-FAILURE)

<to_id>IRPT_ANLREQ.TO-AR-g-109</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~251</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-109` (`decompositions/IRPT_ANLREQ_DECOMP_R28_G.md`) |
**outcome_ref:** FWD-4 (PRD v0.21 contract C-HOP-FAILURE) | **depends_on:** none. Order: CTO msgs 8907, 8971. The commentary writer is `2.0.0_SA_COO~T2`'s and calls the method this order lands.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~251`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-251` (branch `wk-IRPT_ANLREQ-251`), provisioned by the issuer with `infra/`, `docs/`, `data/`, `lib/`, `org/standards` and the project folder on disk. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~251 <0.9.0_WK_IRPT_ANLREQ~251@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. (A provisioner error about a portal sub-worktree does not concern you.)
- A row id has the form `IRPT_ANLREQ-D2-W251-S<k>` (take the next free `<k>`; check the channel file for `W251` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`). The checker is run WITHOUT `-I`.

### Read first (under `C:/dev/wk-irpt-anlreq-251/infra/aws/lambda/investor-reporting/`)

- `ycharts/generate/durable_job.py` (the constants block at the top; `get_state`; `mark_i3_sent`, the precedent for a set-once top-level attribute beside the receipt) and `ycharts/generate/tests/test_durable_job.py` (the boto3 `Stubber` pattern).
- `ycharts/generate/resident_worker.py` `send_ready` and `ycharts/generate/tests/test_resident_worker.py`.
- `reports/resident_installed.py` `make_packager` (and where `build_resident_runtime` calls it), `reports/tests/test_resident_packager_binding.py` (the `package` fixture and how the packager is exercised), and `ycharts/research/opal_packager.py` (`PackagerRefused`, `_closed_message(body) -> (tenant, request_id)`, `handle_commentary_ready`).

### THE CELL (`AR-g-109`, inlined)

PRD C-HOP-FAILURE: three hops fail without writing the job row (the ready-signal send, the commentary draft, the packager). Each writes ONE set-once attribute `hop_failure` = `{hop, code, at}` on the `irpt-jobs` row, beside the receipt, never changing the job's state. This cell lands the store method and the two resident writers; the commentary writer is another seat's and calls the same method, so its name and shape are fixed here.

**`ycharts/generate/durable_job.py`, exactly this:**
1. After `VENDOR_LEDGER_APPEND_BYTES`, a comment naming C-HOP-FAILURE and the constant `HOP_FAILURE_CODES = {"READY_SIGNAL": ("READY_SIGNAL_SEND_FAILED",), "COMMENTARY": ("COMMENTARY_DRAFT_FAILED", "COMMENTARY_DRAFT_REFUSED"), "PACKAGER": ("PACKAGER_REFUSED", "PACKAGER_FAILED")}` (the closed sets, exactly these), and a compiled pattern `_HOP_AT` that fully matches `YYYY-MM-DDTHH:MM:SSZ` (digits only).
2. `DynamoGenerationStore.mark_hop_failure(self, job_id, hop, code, at)`: calls `self._job(job_id)`; raises `LeaseRefused("HOP_FAILURE_INVALID")` (that exact text, before any call) when `hop` is not a key of `HOP_FAILURE_CODES`, `code` is not in that hop's tuple, or `at` is not a `str` fully matching `_HOP_AT`. Then one `update_item` on `self.table` with `Key=self.key`, `UpdateExpression="SET hop_failure = :value"`, `ConditionExpression="attribute_exists(composition_sha256) AND attribute_not_exists(hop_failure)"`, and `ExpressionAttributeValues={":value": {"M": {"hop": _s(hop), "code": _s(code), "at": _s(at)}}}` and nothing else (the state is not read or written). Return `True` when it succeeds. On a conditional-check failure, read the row (`self._row()`): if it holds `hop_failure`, return `False` (set-once: the first failure stands); otherwise re-raise the original exception. Any other exception propagates. Write the docstring in the style of `mark_i3_sent`.
3. `get_state`: when the row holds `hop_failure`, the returned dict gains the key `hop_failure` = `{"hop": ..., "code": ..., "at": ...}` as plain strings (read from the row's `M` map); when it does not, the dict has no such key. No other key changes.
4. (AMENDMENT 1, 2026-10-16, on `2.0.0_SA_COO~T2` msg 8990: the commentary hop has no composition hash and its role will hold UpdateItem only.) A MODULE-LEVEL function, placed directly above `class DynamoGenerationStore`:
   `def mark_hop_failure_keyed(client, tenant, job_id, hop, code, at, table="irpt-jobs")` -> `True` when it wrote, `False` when the condition failed. It raises `LeaseRefused("HOP_FAILURE_INVALID")` before any call when `tenant` or `job_id` is not a non-blank `str`, or `hop`, `code` or `at` fails the same checks as `mark_hop_failure`. Then ONE `client.update_item` with `TableName=table`, `Key={"tenant": _s(tenant), "job": _s(job_id)}`, `UpdateExpression="SET hop_failure = :value"`, `ConditionExpression="attribute_exists(#job) AND attribute_not_exists(hop_failure)"`, `ExpressionAttributeNames={"#job": "job"}`, `ExpressionAttributeValues={":value": {"M": {"hop": _s(hop), "code": _s(code), "at": _s(at)}}}` and nothing else (no read, no ReturnValues). A conditional-check failure returns `False` (the value is already there OR the row does not exist: this form cannot tell, it reads nothing); any other exception propagates. Docstring says so.

**`ycharts/generate/resident_worker.py`, exactly this:** in `send_ready`, in the `except Exception:` branch that prints `ERROR: ANALYSIS_READY_SEND_FAILED <request_id>`, keep that print, then (before the `return`) call `store.mark_hop_failure(request_id, "READY_SIGNAL", "READY_SIGNAL_SEND_FAILED", <now as %Y-%m-%dT%H:%M:%SZ in UTC>)` inside its own `try/except Exception` that prints `ERROR: HOP_FAILURE_MARK_FAILED READY_SIGNAL <request_id>` (no exception text) and carries on. A successful send, an unset queue url and the `mark_i3_sent` branch are unchanged.

**`reports/resident_installed.py`, exactly this:** `make_packager` gains the keyword `clock=None` (after `ticket_ports=None`; `None` means `time.time`; add `import time` at the top, alphabetical); its docstring says `clock` stamps a recorded hop failure. The returned packager is now a function `packager(body)` that calls `opal_packager.handle_commentary_ready(body, ports)` and returns its result; on ANY exception it first calls a local `_record_packager_failure(body, exc)` and then re-raises the SAME exception. `_record_packager_failure` never raises: inside one `try/except Exception` it takes `tenant, request_id = opal_packager._closed_message(body)`, reads `ports["acceptance"].get(tenant, request_id)`, builds `DynamoGenerationStore(clients["dynamodb"], tenant=tenant, request_id=request_id, composition_sha256=record["composition_ref"]["sha256"], table=jobs_table)` (imported from `durable_job` inside the function), and calls `mark_hop_failure(request_id, "PACKAGER", code, <clock() as UTC %Y-%m-%dT%H:%M:%SZ>)` with `code` `"PACKAGER_REFUSED"` when `type(exc).__name__ == "PackagerRefused"` and `"PACKAGER_FAILED"` otherwise; in its `except` it prints `ERROR: HOP_FAILURE_MARK_FAILED PACKAGER <request_id>` (the id, or `unknown` when the message could not be read; no exception text). `build_resident_runtime` passes `clock=clock` to `make_packager`. A good package writes nothing.

**Tests.** A NEW file `ycharts/generate/tests/test_hop_failure.py`, offline (boto3 `Stubber`; fake clients), with these exact test function names (the checker looks for each by name): `test_mark_hop_failure_is_set_once` (the first call returns True and sends exactly the update above; a conditional failure with the value already stored returns False), `test_get_state_carries_hop_failure` (absent: no key; present: the three plain strings), `test_a_failed_ready_send_records_the_hop` (`send_ready` with a raising send and a fake store: one `mark_hop_failure` call with the right hop and code, no exception out), `test_a_packager_failure_records_the_hop` (the packager built by `make_packager` with `handle_commentary_ready` patched to raise `PackagerRefused` then another error: `PACKAGER_REFUSED` then `PACKAGER_FAILED` is written and the error is re-raised), `test_a_failing_hop_write_never_masks_the_error` (a failing write leaves the original packager error unchanged and prints the named line), `test_mark_hop_failure_keyed_is_set_once_without_a_read` (AMENDMENT 1: the keyed form sends exactly the update of item 4, returns True; a conditional failure returns False with no read).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR109-g-AC1" cell_refs="AR-g-109"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g109_checks.py g109</invocation><expect>^AR-G109-OK</expect></criterion>

<criterion id="AR109-g-AC2" cell_refs="AR-g-109"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g109_checks.py regress109</invocation><expect>^AR-G109-REGRESS-OK</expect></criterion>

<expected_criteria>AR109-g-AC1,AR109-g-AC2</expected_criteria>

- AC1 runs the issuer's 29 tests against your tree (the closed code sets; the exact update and its set-once condition; the second write a no-op returning False; a conditional failure with no stored value raised; six invalid shapes refused before any call; `get_state` carrying the value only when set; the ready-send writer: one write, swallowed failure, no write on a good send or an unset queue; the packager writer: refusal and other error recorded then re-raised, a good package writing nothing, a failing write never masking the error, an unreadable message recording nothing), then checks your six named tests exist and pass. At base it FAILs.
- AC2 runs six existing test files one at a time (136 tests: the durable job, the resident worker, the installer, the packager bindings, the packager) and needs all of them to pass, and needs your branch (against the merge-base with `box/dell2`) to change only your three product files, your test file, your folder, your order and the channel file. At base it PASSes. Run it under `timeout` 590000 ms (the resident worker file alone takes about 30 s).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_hop_failure.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~251/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-109.hop-failure-store-and-resident-writers.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R28_G.md</decomp_doc> round 28, workstream ~G, cell `AR-g-109`.
<owned_cells>AR-g-109</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR109-g-AC1, AR109-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~251/IRPT_ANLREQ.TO-AR-g-109.hop-failure-store-and-resident-writers.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-109`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR109-g-AC1,AR109-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed in each product file with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the three files are members of the resident package; `durable_job.py` is ALSO staged into the `irpt-status` Lambda (its source-map row), so the read half (`get_state`) reaches the Lambda only at its own release (a later cell re-pins the row; `get_state` is additive and returns the same keys when no `hop_failure` exists). New write path: the resident's host role already holds `dynamodb:UpdateItem` on `irpt-jobs` (`resident.tf` `JobStateAcceptanceAndRetainedIndexes`, no attribute condition; declared in source, the live policy NOT read), so no IAM change is needed for these two writers. Nothing changes until a release carries the bytes. Behaviour: a failed ready-signal send or a failed or refused packager message additionally writes ONE attribute on that job's row, once; the job's state, receipt and `i3_sent_at` are untouched; a failing write is swallowed and journalled and never changes the hop's own outcome. The other writer of the attribute (commentary) is `2.0.0_SA_COO~T2`'s cell and calls the same method.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change in this cell (the commentary Lambda role's grant is another cell and pair, CTO msg 8971).
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by the issuer's reference build in a scratch tree (21 issuer tests pass; at base 18 fail) and the CTO's ruling (msgs 8907, 8971). Traps: a write that is not set-once (a later failure overwrites the first, or a READY job's receipt is clobbered); a write that changes the state; a code outside the closed sets stored; a failing write that masks the packager's own error (the DLQ path then changes); the packager failure recorded for an unreadable message (no request id to write to); `clock` not passed so a test clock is ignored; the `at` format free; the key name (`hop_failure`) or the map shape different from what the status reader and the commentary writer expect.
</preflight>

- Cut on CTO msgs 8907 and 8971 and the issuer's reference build. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR109-g-AC1` FAILs and `AR109-g-AC2` PASSes (136), as expected.
- NOT claimed: that the live host role can write the attribute (the declared policy says yes; the r35 apply order reads it with the simulator); that the commentary writer or the status reader exists; that any package carries these bytes.
