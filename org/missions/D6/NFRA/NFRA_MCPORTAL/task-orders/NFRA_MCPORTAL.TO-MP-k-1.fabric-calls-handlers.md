# NFRA_MCPORTAL task order -- `MP-k-1` -- WORKSTREAM CP2 ROUND 1: the open-calls read and the close-request write (FWD-17)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-k-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-k-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~10</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two request handlers; no cron, alarm, monitor or cadence (PRD C8). The box's own 10-minute scan applies the request; it is not this cell's.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this cell; the read is MP-x-3's live grant, the one PutObject on requests/ is MP-k-2's; every test uses a fake S3 client.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (absent list, closed call, bad input, non-owner, the real consumer's acceptance).
EGRESS CLASS, declared: none. No AWS call is made by this cell; every S3 call in a test is a fake client.
</preflight>

## 1. THE CELL -- `MP-k-1` (workstream CP2 round 1, decomposition sections CP2.1 and CP2.3-K)

Your worktree is `C:/tmp/mp-cp2-10` (branch `wk-NFRA_MCPORTAL-cp2-10`). Work and commit only there.

Andrew wants to read every open call on every box and close one with his ruling from the page. Calls show box, project,
asking seat and age. A box with no published list reads "absent", never empty. The close lands in that box's list with
his ruling (PRD v0.5 FWD-17, C11, acceptance A17). C11 also says the page NEVER edits a list: the close goes through the
box's own writer.

**The sources and the one write, all in `s3://opal-313476888478-globgrph/fabric/open-calls/v1/`:**
- **`box=<B>/open_calls.json`** (schema `open-calls/1`, writer `.tools/open-calls.py`):
  `{schema, device, written_at, written_by, rows: [{id, project, subject, asked_by, source, orders, roots, state,
  opened_at, scope, closed}]}`. `state` is "OPEN" or "CLOSED".
- **`box=<B>/scan.json`** (schema `open-calls-scan/1`) carries `scanned_at`.
- **`box=<B>/requests/<id>.json`** is the close REQUEST the page writes.
- **`box=<B>/request_results/<id>.json`** is the box's RESULT: `{schema "open-calls-close-result/1", id, device, state
  "APPLIED" | "REFUSED", detail, at}`.

The box applies requests in `.tools/open-calls-scan.py` `apply_requests()` (about `:390-450`). READ IT. It refuses a
request unless:
- the request `id` equals the file name, matches `^[A-Za-z0-9._-]{1,80}$`;
- `schema == "open-calls-close-request/1"`;
- `ruled_by == "andrew"`;
- `call_id` is a string and `ruling` is non-empty.

It then runs `open-calls.py close --ruled-by andrew` and writes the result.

**Reuse, do not copy:** import `BUCKET`, `_s3_client()` and `_roster()` from `app/admin_fabric.py` (live, MP-x-1). NEVER
edit it.

Build, in the gateway app at `infra/aws/ec2/opal-gateway/`:
1. **`app/admin_fabric_calls.py` (new),** with two handlers, both decorated with `owner_gate.owner_only`, and a module
   function `_compute(state="open", client=None)` that returns the GET body (a release check calls `_compute('open')` on
   the host).
   - **`calls` (GET).** The query `state` is "open" (the default) or "all"; anything else is 400. The response is exactly
     this (the page is built against it in parallel):
     ```
     { "read_at": "<ISO Z>", "source": "s3://opal-313476888478-globgrph/fabric/open-calls/v1/",
       "boxes": [ {"box": "<roster name>", "status": "published" | "absent", "written_at": "<ISO Z>" | null,
                   "written_by": "<serial>" | null, "scanned_at": "<ISO Z>" | null, "open": <int> | null} ],
       "calls": [ {"box": "<name>", "id": "<id>", "project": "<CODE>", "subject": "<text>", "asked_by": "<serial>",
                   "opened_at": "<ISO Z>", "state": "<state>", "source": "<path>",
                   "request": {"id": "<rid>", "state": "PENDING" | "APPLIED" | "REFUSED", "requested_at": "<ISO Z>",
                               "detail": "<text>" | null} | null } ] }
     ```
     - **`boxes`:** one row per roster box, in roster order. A NoSuchKey/404 on `open_calls.json` gives "absent",
       `open` null and no calls from that box. `open` is the count of rows with `state` "OPEN". `scanned_at` comes from
       `scan.json`, or null if that is absent.
     - **`calls`:** `state=open` keeps OPEN rows only. Sort by `opened_at`, oldest first.
     - **Requests:** list `box=<B>/requests/` and read each request. Read its result at `request_results/<id>.json`; a
       NoSuchKey means "PENDING". Attach the NEWEST request (by `requested_at`) per `call_id` to its call.
   - **`close_call` (POST).** The JSON body is `{"box", "call_id", "ruling"}`.
     - **Validation:**
       - a box not on the roster -> 400;
       - a `ruling` empty after strip, or over 4000 characters -> 400;
       - a `call_id` that is not an OPEN row of that box's `open_calls.json`, read NOW -> 409 `{"error": "call not open
         on that box"}`. An absent list is the same 409.
     - **The write:** exactly ONE `put_object`, Key `fabric/open-calls/v1/box=<B>/requests/<rid>.json`, ContentType
       `application/json`.
       - `rid` = `<YYYYMMDDTHHMMSSZ>-<8 lowercase hex>`.
       - The body is `{"schema": "open-calls-close-request/1", "id": rid, "call_id": ..., "ruling": <stripped>,
         "ruled_by": "andrew", "requested_at": "<ISO Z>", "requested_by": "andrew", "owner":
         request.state.owner_email}`.
     - **Answer:** 202 `{"request_id": rid, "key": "<key>", "state": "PENDING"}`. A failed put returns 503
       `{"error": "request not written", "reason": "<ExceptionClass: message>"}`.
     - **Bound:** this is the gateway's ONLY write. It never writes `open_calls.json`, `request_results/` or anything
       else.
   - **Failure (GET, and the POST's read):** a listing failure, or a read failure that is not NoSuchKey/404, returns 503
     `{"error": "store unreadable", "reason": ...}`.
   - **Load:** run the S3 work in `run_in_threadpool`.
2. **DO NOT edit `app/admin_api.py`.** The issuer adds `Route("/fabric/calls", admin_fabric_calls.calls, methods=["GET"])`
   and `Route("/fabric/calls/close", admin_fabric_calls.close_call, methods=["POST"])` at the merge. Name both lines in
   your report.
3. **`tests/test_admin_fabric_calls.py` (new).** Mount the handlers as `tests/test_admin_fabric.py` does. These eight
   tests, by these exact names:
   - `test_calls_absent_box_reads_absent`. NoSuchKey on one box's `open_calls.json` gives "absent", `open` null and none
     of its calls.
   - `test_calls_open_filter_and_order`. `state=open` returns only OPEN rows, oldest first. `state=all` includes CLOSED
     rows. `state=x` is 400.
   - `test_close_writes_one_request_under_requests`. Expect 202. The fake client saw exactly ONE `put_object`, its Key
     under `box=<B>/requests/`, and its body parses with every field above, `ruled_by` "andrew" and the stubbed owner
     email.
   - `test_close_refuses_call_not_open`. A CLOSED call_id and an unknown call_id each give 409, with zero `put_object`.
   - `test_close_bad_input_400`. An off-roster box, an empty ruling and a 4001-character ruling each give 400, with zero
     `put_object`.
   - `test_calls_non_owner_is_refused`. GET and POST by a non-owner each give 403, with zero store calls.
   - `test_real_capture_calls`. Serve the VERBATIM capture
     `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/fixtures/s3_capture_20261009T0728Z.json`
     (`{"objects": {<s3 key>: <parsed body>}}`; the repo root is four parents above the gateway dir) from a fake client
     that lists by prefix and gets by key. `_compute('open')` reads every roster box "published". Each `open` equals the
     count of that box's captured OPEN rows, computed IN THE TEST. Each `scanned_at` equals that box's captured
     `scan.json` `scanned_at`.
   - `test_request_accepted_by_open_calls_scan`. This is the seam against the REAL consumer.
     1. POST a close for a planted OPEN call and capture the object the fake client was given.
     2. Load `.tools/open-calls-scan.py` from the repo root with `importlib.util.spec_from_file_location`.
     3. Call its `apply_requests(device, False, now, xa, close=<recorder>)`:
        - `xa` is an in-memory object with `_list_keys(prefix)`, `_get(key)` (None when absent) and `_put(key, obj)`,
          holding your request object;
        - `<recorder>` records the `a` it is called with;
        - `OPAL_STATE_ROOT` is set to a `tmp_path` via `monkeypatch.setenv`.
     4. Assert the return is `(1, 0, 1, [])`, the recorder saw `a.id == call_id` and `a.ruled_by == "andrew"`, and the
        stored result has `state` "APPLIED".

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `admin_fabric.py`, `admin_api.py`, `owner_gate.py`, any
   other `app/` module, `.tools/` (read `open-calls-scan.py`, never edit it), Terraform, the manifest or anything in
   `mcportal/`. Make no deploy, no AWS call and no real S3 write.
2. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_fabric_calls.py
infra/aws/ec2/opal-gateway/tests/test_admin_fabric_calls.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~10/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `.tools/open-calls-scan.py`, `.tools/open-calls.py`, `infra/aws/ec2/opal-gateway/app/admin_fabric.py`,
`app/owner_gate.py`, `tests/test_admin_fabric.py`, `org/devices/DEVICES.json`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/` (fixture and checks).

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W10-S<k>` (the next free k for W10). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-k-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/k1.AC1.sh; echo "exit=$?"</invocation><expect>calls tests: 0 failed; named tests PASSED 6 of 6 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-k-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/k1.AC2.sh; echo "exit=$?"</invocation><expect>calls seams: 0 failed; named tests PASSED 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~10/NFRA_MCPORTAL.TO-MP-k-1.fabric-calls-handlers.proof_of_spec.json`.
Report once, with:
- the two check outputs;
- the commit hash;
- the two route lines for the issuer;
- the real capture's per-box open counts as served;
- any field you could not fill as written, and why;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the CP2 issuance (decomposition v6) from PRD v0.5 FWD-17, C11, A17 @cecf26d2c9 and the CTO's Q3 ruling
(msg 32404). The request schema is the scan's own (@5bf8350baa, `open-calls-scan.py:328`, `apply_requests` `:390`). Checks
dry-run at base 2851a9190d: AC1 FAIL (test file absent), AC2 FAIL (test file absent). The live POST needs MP-k-2's grant;
before it, a live POST answers 503 "request not written", which is the failure arm. No gate. Lives through MP-r-2.

<status>complete</status>
<round>1</round>
<workstream>CP2</workstream>
<slot>~10</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
