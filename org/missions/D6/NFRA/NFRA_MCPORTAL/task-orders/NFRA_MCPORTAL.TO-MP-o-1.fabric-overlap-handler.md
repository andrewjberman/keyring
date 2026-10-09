# NFRA_MCPORTAL task order -- `MP-o-1` -- WORKSTREAM CP2 ROUND 1: the owner-gated overlap handler and its rule file (FWD-15)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-o-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-o-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~8</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request handler; no cron, alarm, monitor or cadence (PRD C8, C12: read when opened).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; MP-x-3's live read grant covers both prefixes this handler reads; every test uses a fake S3 client.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (one-box surface, unrostered box, absent deploy list, unreadable store, non-owner).
EGRESS CLASS, declared: none. No AWS call is made by this cell; every S3 read in a test is a fake client.
</preflight>

## 1. THE CELL -- `MP-o-1` (workstream CP2 round 1, decomposition sections CP2.1 and CP2.3-O)

Your worktree is `C:/tmp/mp-cp2-8` (branch `wk-NFRA_MCPORTAL-cp2-8`). Work and commit only there.

Andrew wants to see on one page where two or more boxes are working on the same surface, rated by risk. A Terraform
module that two boxes edit while one of them holds an open deploy on it must stand out above two boxes appending to a
shared log (PRD v0.5 FWD-15, C13, acceptance A15).

**The two sources, both in `s3://opal-313476888478-globgrph/`, both readable by the gateway today:**
1. **The activity store** `fabric/activity/v1/dt=<YYYY-MM-DD>/box=<box>/<stamp>_<sha12>.json`. There is one record per
   commit with fields `when, box, box_claim, seat, sha, subject, files, surfaces [{key, cls}], projects`. `cls` is one of
   `INFRA, CODE, REGISTRY, TOOL, RECORD, APPEND`, assigned by `.tools/fabric-activity.py` `surface()` (about `:56-94`):
   for example `tf:<module>` is INFRA, `lambda-src:<fn>` is CODE, `append:<dir>` is APPEND. Read `cmd_overlap()` (about
   `:477-500`): it is the CLI form of what you serve.
2. **Each box's open-deploy list** `fabric/open-calls/v1/box=<box>/open_deploys.json`, schema `open-deploys/1`:
   `{schema, device, published_at, worktrees_total, worktrees_read, entries: [{slug, title, author, status, opened_at,
   window_hours, entry_path, legs: [{id, kind, target}], worktrees}], unreadable}`. The producer is
   `.tools/open-calls-scan.py` `open_deploys_doc()` (about `:346-379`). `status` is `OPEN` or `HELD-SOVEREIGN-GATED`.

**Reuse, do not copy:** `app/admin_fabric.py` (live, MP-x-1) already has `BUCKET`, `_s3_client()`, `_roster()`,
`_list_keys(client, start, end)`, `_read_records(client, keys)` and the dedup rule inside `_compute()`. Import what you
need from it. NEVER edit `admin_fabric.py`.

Build, in the gateway app at `infra/aws/ec2/opal-gateway/`:
1. **`app/refs/overlap_rules.json` (new),** versioned. It holds:
   - `version`: "1";
   - `prd`: "NFRA_MCPORTAL v0.5 C13";
   - `kinds`: per class, `{rank, label}`. The ranks are strictly INFRA > CODE > REGISTRY > TOOL > RECORD > APPEND. INFRA's
     label is "Terraform" and APPEND's is "shared log";
   - `deploy_uplift`: an integer larger than INFRA's rank minus APPEND's rank;
   - `deploy_open_statuses`: `["OPEN", "HELD-SOVEREIGN-GATED"]`;
   - `names`: per surface-key prefix, a list of needle templates in which `{name}` is the key after its prefix. At least
     `"tf:": ["infra/aws/terraform/{name}/"]`, `"lambda-src:": ["infra/aws/lambda/{name}/"]` and
     `"infra:": ["infra/aws/{name}/"]`.
2. **`app/admin_fabric_overlap.py` (new).** It has ONE handler, `overlap`, decorated with `owner_gate.owner_only`, and a
   module function `_compute(hours, client=None)` that returns the body (a release check calls `_compute(6)` on the host).
   - **`hours`:** an integer from 1 to 24, default 6; anything else is 400.
   - **The response,** exactly (do not rename or drop a field; the page is built against it in parallel):
     ```
     { "window": {"hours": N, "start": "<ISO Z>", "end": "<ISO Z>"},
       "read_at": "<ISO Z>", "records_scanned": <int>, "records_skipped": <int>,
       "source": "s3://opal-313476888478-globgrph/fabric/activity/v1/",
       "rules": {"file": "app/refs/overlap_rules.json", "version": "<string>"},
       "deploys": [ {"box": "<roster name>", "status": "read" | "absent", "published_at": "<ISO Z>" | null, "open": <int> | null} ],
       "overlaps": [ { "surface": "<surface key>", "cls": "INFRA" | "CODE" | "REGISTRY" | "TOOL" | "RECORD" | "APPEND",
                       "boxes": [ {"box": "<name>", "commits": <int>, "seats": ["<serial>"], "last": "<ISO Z>"} ],
                       "last": "<ISO Z>",
                       "deploys_open": [ {"box": "<name>", "slug": "<slug>", "status": "<status>", "opened_at": "<ISO>"} ],
                       "rating": <int>, "label": "<text>" } ] }
     ```
   - **Records:** dedup by `sha`, the measured claim wins, and keep `when` at or after the start. This is MP-x-1's rule.
   - **An overlap** is a surface key touched by 2 or more distinct ROSTER boxes. A box not on the roster never counts.
     List EVERY class, APPEND and RECORD included.
   - **Naming:** an entry whose `status` is in `deploy_open_statuses` names a surface when one of the surface prefix's
     needles, with `{name}` filled, is a substring of the entry's `title`, its `entry_path`, or any leg's `target`. A
     prefix with no `names` row is never deploy-matched. A naming entry from ANY box's list goes in `deploys_open`.
   - **Rating:** `rating = kinds[cls].rank + (deploy_uplift if deploys_open else 0)`. `label` is the kind label, plus
     " -- deploy open" when uplifted. Sort by rating descending, then box count descending, then `last` descending.
   - **`deploys`:** one row per roster box, in roster order. A `NoSuchKey`/404 on its `open_deploys.json` gives "absent",
     `published_at` null and `open` null. A read gives "read", the record's `published_at`, and `open` = the count of
     entries whose status is in `deploy_open_statuses`.
   - **Failure:** a listing failure, or any open-deploys read failure that is not NoSuchKey/404, returns **503**
     `{"error": "store unreadable", "reason": "<ExceptionClass: message>"}`. It is never a 200 with empty lists.
   - **Load:** run the S3 work in `run_in_threadpool`, as `admin_fabric.boxes` does.
3. **DO NOT edit `app/admin_api.py`.** The issuer adds the route line `Route("/fabric/overlap",
   admin_fabric_overlap.overlap, methods=["GET"])` at the merge. Name that line in your report.
4. **`tests/test_admin_fabric_overlap.py` (new).** Mount the handler on a `Starlette` test app as
   `tests/test_admin_fabric.py` does: the owner stubbing, a fake S3 client and `TestClient`. These six tests, by these
   exact names:
   - `test_terraform_with_open_deploy_rated_above_shared_log` (A15). Plant two roster boxes editing `tf:<m>`, with box
     one's `open_deploys.json` holding an OPEN entry whose leg target names `infra/aws/terraform/<m>/`. Plant the same two
     boxes both touching an `append:` surface. The `tf:` overlap has `deploys_open` non-empty and a rating strictly above
     the `append:` overlap's, and it is first in the list.
   - `test_overlap_needs_two_roster_boxes`. A surface touched by one roster box only, and a surface touched by one roster
     box plus one unrostered box, produce no overlap row.
   - `test_deploys_absent_box_reads_absent`. A fake client raising NoSuchKey for one box's `open_deploys.json` gives that
     box `status` "absent" and `open` null, while the others read "read".
   - `test_overlap_store_unreadable_returns_503`. The listing raises `botocore` ClientError AccessDenied. Expect 503,
     `error` "store unreadable", and no `overlaps` key.
   - `test_overlap_non_owner_is_refused`. A non-owner gets 403, and the fake client records zero calls.
   - `test_real_capture_overlap`. Serve the VERBATIM capture
     `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/fixtures/s3_capture_20261009T0728Z.json`
     (`{"objects": {<s3 key>: <parsed body>}}`; the repo root is four parents above the gateway dir) from a fake client
     that lists by prefix and gets by key. Call `_compute(hours)` with the clock pinned so that the window covers the
     capture: the activity keys are stamped 04:00Z-07:59Z on 2026-10-09; patch the module's notion of "now" to
     2026-10-09T08:00:00Z with hours=6. Assert:
     - every overlap has 2 or more boxes;
     - the INFRA overlap `tf:transcripts` is present and rated above EVERY APPEND overlap;
     - `deploys` reads "read" for all four roster boxes;
     - each `open` equals the count of entries with an open status that the TEST computes from the capture itself.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `admin_fabric.py`, `admin_api.py`, `owner_gate.py`,
   `server.py`, any other `app/` module, Terraform, the manifest or anything in `mcportal/`. Make no deploy and no AWS call.
2. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_fabric_overlap.py
infra/aws/ec2/opal-gateway/app/refs/overlap_rules.json
infra/aws/ec2/opal-gateway/tests/test_admin_fabric_overlap.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~8/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `.tools/fabric-activity.py`, `.tools/open-calls-scan.py`, `infra/aws/ec2/opal-gateway/app/admin_fabric.py`,
`app/owner_gate.py`, `tests/test_admin_fabric.py`, `org/devices/DEVICES.json`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/` (fixture and checks).

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W8-S<k>` (the next free k for W8). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-o-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/o1.AC1.sh; echo "exit=$?"</invocation><expect>overlap tests: 0 failed; named tests PASSED 5 of 5 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-o-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/o1.AC2.sh; echo "exit=$?"</invocation><expect>overlap real capture: 0 failed; named tests PASSED 1 of 1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~8/NFRA_MCPORTAL.TO-MP-o-1.fabric-overlap-handler.proof_of_spec.json`.
Report once, with:
- the two check outputs;
- the commit hash;
- the route line for the issuer;
- the real capture's overlap count by class and the `tf:transcripts` row as served;
- any field of the response you could not fill as written, and why;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the CP2 issuance (decomposition v6, Andrew-direct ~06:0xZ 2026-10-09 approval of the CP2
workstream) from PRD v0.5 FWD-15, C13, A15 @cecf26d2c9. Checks dry-run at base 2851a9190d: AC1 FAIL (test file absent), AC2
FAIL (test file absent). The capture holds 31 overlaps over 860 activity records (INFRA 1 `tf:transcripts`, CODE 3, TOOL 1,
RECORD 18, APPEND 8). No gate. Lives through MP-r-2.

<status>pending</status>
<round>1</round>
<workstream>CP2</workstream>
<slot>~8</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
