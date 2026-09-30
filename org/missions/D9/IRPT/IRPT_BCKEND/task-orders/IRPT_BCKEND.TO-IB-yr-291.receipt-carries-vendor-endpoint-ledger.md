# TO-IB-yr-291 -- the job's receipt.json carries the vendor endpoint ledger: shapes, never values, refused off-shape

<to_id>IRPT_BCKEND.TO-IB-yr-291</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~94</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~Y | **Decomp cell:** `IB-yr-291` (`decompositions/IRPT_BCKEND_DECOMP_R29_Y.md`)

---

## WORKER FACE

### THE CELL

The YCharts generation job already records EVERY vendor request as a shape-only record. `transport.py` `_record()`
(around line 474) appends `{"method", "path", "status", "content_type", "bytes", "set_cookie_count", "waf_action",
"login_destination", "final_url_path", "body_complete"}` to `self.evidence` -- ten keys, no header value, no cookie,
no body. **Production then throws the list away:** `job.py` keeps only `len(self.tx.evidence)` (the duplicate-reuse
branch, around line 334) and the receipt it writes for a READY run (around lines 485-492) carries
`{"attempt", "artifact_key", "template_id", "variant"}` and nothing about the vendor traffic.

**Your cell: the receipt carries the ledger.** In `GenerationJob.run`, where the READY receipt is written, add
`"vendor_requests": <the list of records in self.tx.evidence>` to the JSON the job puts at `receipt_key`. Before
the write, VALIDATE the ledger: every record's key set must equal exactly the ten keys above; any record with a
different key set raises `JobRefused("VENDOR_LEDGER_SHAPE")` BEFORE `self.blobs.put(...)` of the receipt (the PDF
put above it has already happened; that is fine -- a receipt is written after the PDF by design, and a refused
receipt leaves a request that re-runs). Put the ten-key shape in ONE module-level constant in `job.py` (for
example `VENDOR_LEDGER_SHAPE = frozenset((...))`) so the test and the check read the same object.

Do NOT change `transport.py` (it is another cell's read surface this round and already correct). Do NOT change the
duplicate-reuse branch's `vendor_requests: len(...)` return value -- the offline suite pins it and AC2 is its
control. Do NOT change any state-store write, the attempt row, or the PDF key.

**Why:** Andrew-direct 2026-09-30 ~06:5xZ -- *"record HAR and identify the endpoints that appear in that recording
... see if we can just call those in order and assemble with a script."* The resident's per-job ledger is the
HAR-equivalent for generation, values-free by construction; persisting it is what makes the next window's receipts
diffable against `YCHARTS_GENERATION_ENDPOINT_CENSUS_20260930.md`.

### ACCEPTANCE (run from your worktree root unless the invocation says otherwise)

<criterion id="Y29-1-AC1" cell_refs="IB-yr-291"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_291_receipt_ledger.py</invocation><expect>PASS: receipt vendor_requests carries every transport record on the ten-key shape</expect></criterion>

<criterion id="Y29-1-AC2" cell_refs="IB-yr-291"><invocation>python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_291_dup_control.py</invocation><expect>PASS : duplicate re-delivery spends 0 vendor requests; first run spent 7</expect></criterion>

<criterion id="Y29-1-AC3" cell_refs="IB-yr-291"><invocation>cd infra/aws/lambda/investor-reporting && python -m pytest -q -p no:cacheprovider ycharts/generate/tests/test_receipt_ledger.py</invocation><expect>0 failed, at least 2 passed: one node reads the receipt ledger back equal to tx.evidence with every record on the ten-key shape, and one CONTROL node plants an off-shape record (for example a key named `cookie`) into the transport's evidence and asserts the receipt write raises JobRefused naming VENDOR_LEDGER_SHAPE and NO receipt object exists in the blob store</expect></criterion>

<expected_criteria>Y29-1-AC1,Y29-1-AC2,Y29-1-AC3</expected_criteria>

**Issuer's base run at CLOUD HEAD a7a6d286f2 (CTO 103159: the base reading beside every criterion):**

- **AC1 -- FAIL as expected:** `run ok: True | receipts written: 1 | transport evidence records: 7`; receipt keys
  `['artifact_key', 'attempt', 'template_id', 'variant']`; `FAIL: receipt.vendor_requests is NoneType, not a list`.
  The denominator you must match is **7** records for the OVERVIEW replay.
- **AC2 -- PASS as expected (control):** `duplicate_outcome EXISTING_ARTIFACT_REUSED, duplicate_vendor_requests 0,
  first_vendor_requests 7, blob_head_calls 2`. **It is green at base and must stay green:** a re-delivery still
  spends no vendor request and the receipt is still found by exact key.
- **AC3 -- FAIL as expected:** the test file does not exist. Build it from the harness the check uses:
  `ycharts/generate/tests/run_offline_suite.py` exposes `owned_name()`, `base_script(collection_owned_name=...)`,
  `make_job(script, blobs=...)`, `JOB_ID`, `REQUEST_ID`, `REVISION`, `HOLDINGS`, `COVER`, and `jobmod.MemoryBlobs`
  (whose `.objects` is keyed `(bucket, key)`). Importing that module installs the network guard; nothing you write
  may open a socket.

## BOUNDS

- **Grant.** The `<paths>` block plus `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~94/` and
  this order's file. `run_offline_suite.py` and the check scripts are READ-ONLY.
- **AMENDMENT 1 (issuer ruling on row W94-S1, decomposition amendment 1):** `transport.py` is granted for EXACTLY ONE
  change -- remove the `"location": fixture.get("location", "")` line from `ReplayTransport`'s evidence record
  (around line 594) so the replay records the same ten-key shape as the real `Transport._record`. Nothing else in
  `transport.py` moves; the reply/`info` path keeps its `location`. `job.py` validates STRICTLY against
  `VENDOR_LEDGER_SHAPE` (your `candidate_strict_validate.patch`); do NOT strip any key in production code (the
  `candidate_strip_location.patch` is not taken). The three criteria are unchanged.
- **No AWS call, no deploy, no Terraform, no vendor/external network call.** The change lands on the resident by
  `~P`'s install packet later; nothing here restarts anything.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken the test to pass. If a file you need is not in `<paths>`, that is a REFUSAL AND A ROW
  naming the file. It is not your shortfall.
- **Row ids** are `IRPT_BCKEND-W94-S<k>`, appended to the project surprise channel with a
  `## <ID> -- <one line>` markdown heading. Other seats append concurrently: re-read immediately before writing and
  re-check your `<k>`. `hazard_standing` is `ARMED` or `INERT`, nothing else. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~94 <0.9.0_WK_IRPT_BCKEND~94@opal.agent>" -F <msgfile> -- <paths>`; do NOT pre-`git add`; the message file is written by the Write tool or python, never a shell heredoc and never a `python -c "..."` containing double quotes.
- **Verify every commit with git, not the tool's stdout** (`git status --porcelain <path>` empty).
- **MSYS trap (row S215):** a unix path inside a `python -c` SOURCE BODY is not converted. Pass paths as argv.
- **Search discipline:** raw recursive `grep`/`find` in Bash is gated; use `comp-find` or the native Grep/Glob/Read
  tools, and never pipe `comp-find` into `head`.
- **ASCII only** in `job.py` and the test (CLAUDE.md: no non-ASCII in production code).

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/job.py
infra/aws/lambda/investor-reporting/ycharts/generate/transport.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_receipt_ledger.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_291_receipt_ledger.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y/R29_checks/check_291_dup_control.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R29_Y.md</decomp_doc> round 29, workstream ~Y, cell `IB-yr-291`.
<owned_cells>IB-yr-291</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: Y29-1-AC1, Y29-1-AC2, Y29-1-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~94/IRPT_BCKEND.TO-IB-yr-291.receipt-carries-vendor-endpoint-ledger.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> Y29-1-AC1,Y29-1-AC2,Y29-1-AC3` BEFORE the flip. Copy
the shape from `deliverables/0.9.0_WK_IRPT_BCKEND~92/IRPT_BCKEND.TO-IB-yr-282.served-answers-tell-the-truth.proof_of_spec.json`.
</proof_of_spec>

**REPORT (your final message):** each criterion's output line; the receipt's key list after the change; the name of
the shape constant; the diff summary; and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule, trigger or scheduled producer is touched.
comp-blast: RUN -- WORLD by the gate's floor (an infrastructure path). The change is one key added to a JSON object the job writes under its own generations prefix, read back only by the duplicate-reuse HEAD (exact key, existence only). No served answer, contract or route changes. Blast radius: receipt objects written after the resident next installs this file; nothing at rest moves.
comp-iam: DECLARED-NOT-APPLICABLE -- no boto3 call, no role, no grant.
comp-adversary: RUN -- three risks. (1) The worker persists something with a value in it (a header, a cookie, a body): the ten-key shape is pinned in the check (AC1 FORBIDDEN set) and in the write-time refusal (AC3 control). (2) The worker moves the duplicate-reuse count to keep a test green: AC2 is the offline suite's own duplicate_redelivery arm, pinned at 7/0. (3) The worker writes the receipt before validating and leaves a half-written object on refusal: AC3's control asserts no receipt object exists after the refusal. Blind to whether ~P's next install picks the file up -- outside this cell, stated on the decomposition.
lane: the <paths> block IS the grant. Measured: no non-terminal ~P or ~M order names job.py or the new test (11 non-terminal orders of 155 scanned, 0 hits). job.py sits in IRPT_Y_ACCESS_INTEGRATION_P, which permits 2.0.0_SA_COO~Y (the drain's merge author).
</preflight>
