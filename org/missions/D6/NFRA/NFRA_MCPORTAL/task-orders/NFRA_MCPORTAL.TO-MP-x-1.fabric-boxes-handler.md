# NFRA_MCPORTAL task order -- `MP-x-1` -- ROUND 4: the owner-gated handler that reads the fabric activity store (FWD-14 hop 3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-x-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~5</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request handler; no cron, alarm, monitor or cadence (PRD C8, C12: read when opened).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change in this cell; the read grant is MP-x-3's, and every test uses a fake S3 client.
comp-adversary: DECLARED-NOT-APPLICABLE -- the five named tests are the adversary arms (absent box, duplicate sha, unreadable store, roster drift, non-owner).
EGRESS CLASS, declared: none. No AWS call is made by this cell; every S3 read in a test is a fake client.
</preflight>

## 1. THE CELL -- `MP-x-1` (round 4, decomposition section R4.2 and the contract in R4.3)

Your worktree is `C:/tmp/mp-r4-5` (branch `wk-NFRA_MCPORTAL-r4-5`, a sparse checkout). Work and commit only there.

Andrew wants a page that shows which box is working on what right now, without asking any seat. Every commit on a box
writes one JSON record to `s3://opal-313476888478-globgrph/fabric/activity/v1/dt=<YYYY-MM-DD>/box=<box>/<stamp>_<sha12>.json`.
The record fields are `when, box, box_claim (measured|inferred|absent), seat, committer, sha, branch, worktree, subject,
verb, files, file_count, surfaces [{key, cls}], projects`. The writer and reader is `.tools/fabric-activity.py`. Read its
`fetch()` (about `:290-337`) and `cmd_boxes()` (about `:504-525`). Your handler serves the same figures over HTTP.

Build, in the gateway app at `infra/aws/ec2/opal-gateway/`:
1. **`app/admin_fabric.py` (new).** It holds one handler, `GET /fabric/boxes`, decorated with `owner_gate.owner_only`, as
   `app/admin_grants.py` and `app/admin_refusals.py` decorate theirs. It takes the query `hours`: an integer from 1 to 24,
   default 6. Anything else returns 400. It returns exactly this JSON shape (the page is built against it in parallel, so
   do not rename or drop a field):
   ```
   { "window": {"hours": N, "start": "<ISO Z>", "end": "<ISO Z>"},
     "read_at": "<ISO Z>", "records_scanned": <int>, "records_skipped": <int>,
     "source": "s3://opal-313476888478-globgrph/fabric/activity/v1/",
     "boxes": [ { "box": "<roster name>", "status": "reporting" | "not reporting", "commits": <int>,
                  "seats": ["<serial>", ...],
                  "projects": [ {"code": "<CODE>", "commits": <int>, "last": "<ISO Z>"} ],
                  "last_commit": {"when": "<ISO Z>", "sha": "<12 chars>", "seat": "<serial>", "subject": "<text>"} | null,
                  "claims": ["measured" | "inferred" | "absent", ...] } ],
     "unrostered": [ "<box seen in records but not on the roster>", ... ] }
   ```
   - **Listing.** List `fabric/activity/v1/dt=<day>/` for every UTC day the window touches, paginated. Read each object.
   - **Filtering.** Keep records whose `when` is at or after the window start.
   - **Deduplication.** Deduplicate by `sha`, keeping the `box_claim == "measured"` record over any other. This is
     `fetch()`'s rule.
   - **Roster.** Every box on the roster appears in `boxes`, ordered by commits descending, then name. A roster box with no
     record has `status` "not reporting", `commits` 0, empty lists and `last_commit` null.
   - **Unrostered boxes.** A box name in the records that is not on the roster goes in `unrostered` and never into
     `boxes`.
   - **Projects.** `projects` is sorted by commits descending.
   - **Unparseable records.** A record that fails to parse is skipped and counted in `records_skipped`.
2. **Load.** The gateway is ONE worker on a t4g.nano, so never block the event loop. Run the S3 work in
   `starlette.concurrency.run_in_threadpool`, as `app/browser_oidc.py:172` does. Fetch bodies with at most 8 threads.
   Each record object is write-once and its body is a function of its key, so cache bodies in-process by key in a
   bounded dict (cap 20000 entries, oldest dropped). Make the S3 client injectable, as `app/admin_refusals.py:72-80` does
   (`_s3_client()`, region from `AWS_REGION`, default `us-east-1`), so tests pass a fake.
3. **Failure arm.** If the listing raises (AccessDenied, a timeout, any `botocore` error), return **503** with
   `{"error": "store unreadable", "reason": "<ExceptionClass: message>"}`. Never return 200 with an empty `boxes`.
4. **`app/refs/fabric_boxes.json` (new).** It holds the roster, `{"boxes": [...]}`. The names are exactly the
   `devices[].name` values of `org/devices/DEVICES.json`, in that order. Today they are laptop, sitez, dell1 and dell2.
   Read the file, do not type the names from this order.
5. **`app/admin_api.py`.** Add ONE route line to `routes`: `Route("/fabric/boxes", admin_fabric.boxes, methods=["GET"])`,
   plus its import. Change nothing else in the file.
6. **`tests/test_admin_fabric.py` (new).** Mount the handler as `tests/test_admin_refusals.py` does: the `app_mods` fixture,
   owner stubbing, a `Starlette` test app, `TestClient`. Write these five tests by these exact names:
   - `test_not_reporting_box_reads_not_reporting`: the fake store holds records for two roster boxes only. Each other
     roster box is in `boxes` with `status` "not reporting" and `last_commit` null.
   - `test_counts_match_records_dedup_measured`: plant about 6 records over 2 boxes, 3 projects and 2 seats, one `sha`
     twice (inferred, then measured), and one record older than the window. Assert every box's `commits`, `seats`,
     per-project `commits` and `last`, and `last_commit` equal what you compute by hand. The duplicate counts once, as
     its measured record. The old record is excluded.
   - `test_store_unreadable_returns_503`: the fake client's listing raises a `botocore.exceptions.ClientError`
     AccessDenied. Expect 503 with `error` "store unreadable" and no `boxes` key.
   - `test_roster_equals_devices_register`: load `app/refs/fabric_boxes.json` and the workspace's
     `org/devices/DEVICES.json`, the repo root being four parents above the gateway dir. Assert the two name lists are
     equal.
   - `test_non_owner_is_refused`: a non-owner identity gets 403, and the fake client records zero calls.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `owner_gate.py`, `server.py`, `config.py`, any other
   `app/` module, Terraform, the manifest or anything in `mcportal/`. Make no deploy and no AWS call.
2. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_fabric.py
infra/aws/ec2/opal-gateway/app/admin_api.py
infra/aws/ec2/opal-gateway/app/refs/fabric_boxes.json
infra/aws/ec2/opal-gateway/tests/test_admin_fabric.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~5/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `.tools/fabric-activity.py`, `org/devices/DEVICES.json`, `infra/aws/ec2/opal-gateway/app/owner_gate.py`,
`app/admin_refusals.py`, `app/admin_grants.py`, `app/browser_oidc.py`, `tests/test_admin_refusals.py`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round4/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W5-S<k>` (the next free k for W5). `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-x-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round4/checks/x1.AC1.sh; echo "exit=$?"</invocation><expect>fabric tests: 0 failed; named tests PASSED 5 of 5 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-x-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round4/checks/x1.AC2.sh; echo "exit=$?"</invocation><expect>admin suites: N passed (N>=1), 0 failed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-x-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round4/checks/x1.AC3.sh; echo "exit=$?"</invocation><expect>fabric/boxes GET routes=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~5/NFRA_MCPORTAL.TO-MP-x-1.fabric-boxes-handler.proof_of_spec.json`.
Report once, with:
- the three check outputs;
- the commit hash;
- any field of the response shape you could not fill as written, and why;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the round-4 issuance from PRD v0.5 (FWD-14, C11, C12) @cecf26d2c9, ratified-text half signed
@8de5b2dc76. Checks dry-run at base 39889dd4d7: AC1 FAIL (test file absent), AC2 FAIL (test file absent), AC3 FAIL (routes=0).
Positive control for AC2: the five existing admin suites pass at base (23 passed). This cell goes live only through MP-x-4.
Until MP-x-3's grant is applied, the live handler returns the 503 arm. No gate. Slot `~5` continues to MP-x-4 and MP-x-5
when they are cut.

<status>complete</status>
<round>4</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
