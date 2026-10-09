# NFRA_MCPORTAL task order -- `MP-g-1` -- WORKSTREAM CP2 ROUND 1: the owner-gated git-state handler (FWD-16)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-g-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-g-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~9</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request handler; no cron, alarm, monitor or cadence (PRD C8, C12).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the gitstate records sit under fabric/activity/v1/, inside MP-x-3's live read grant; every test uses a fake S3 client.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (absent record, null refs, unreadable store, non-owner).
EGRESS CLASS, declared: none. No AWS call is made by this cell; every S3 read in a test is a fake client.
</preflight>

## 1. THE CELL -- `MP-g-1` (workstream CP2 round 1, decomposition sections CP2.1 and CP2.3-G)

Your worktree is `C:/tmp/mp-cp2-9` (branch `wk-NFRA_MCPORTAL-cp2-9`). Work and commit only there.

Andrew wants to see each box's git state on one page: committed, pushed to its box branch, on the trunk, and when the
trunk last moved or integration was refused. A box whose work is not on the trunk must be seen as such the same day. An
event with no recorded home reads "not recorded", never absent-as-zero (PRD v0.5 FWD-16, C14, acceptance A16).

**The source.** Each box's scheduled `.tools/box-sync.sh` runs `.tools/fabric-gitstate.py` (read it) on every pass. That
tool writes to `s3://opal-313476888478-globgrph/`:
- the history record `fabric/activity/v1/gitstate/box=<box>/<YYYYMMDDTHHMMSSZ>.json`;
- `fabric/activity/v1/gitstate/box=<box>/latest.json`, a copy of the newest record.

Schema `fabric-gitstate/1`:
`{schema, box, at, pass: {mode, rc, serial, note}, box_branch, box_head, origin_box_head, trunk_head,
unpushed: {count, shas, capped}, pushed_not_on_trunk: {count, shas, capped}, behind_trunk, unread: [...]}`.
`pass.mode` is "box", "integrate" or "manual". An unreadable ref is null and is named in `unread`.

**Reuse, do not copy:** import `BUCKET`, `_s3_client()` and `_roster()` from `app/admin_fabric.py` (live, MP-x-1). NEVER
edit it.

Build, in the gateway app at `infra/aws/ec2/opal-gateway/`:
1. **`app/admin_fabric_gitstate.py` (new).** It has ONE handler, `gitstate`, decorated with `owner_gate.owner_only`, and a
   module function `_compute(client=None)` that returns the body (a release check calls `_compute()` on the host). The
   response is exactly this (the page is built against it in parallel):
   ```
   { "read_at": "<ISO Z>", "source": "s3://opal-313476888478-globgrph/fabric/activity/v1/gitstate/",
     "trunk": {"head": "<12>" | null, "first_seen": "<ISO Z>" | null, "claim": "inferred", "basis": "<text>"},
     "boxes": [ { "box": "<roster name>", "status": "recorded" | "not recorded", "at": "<ISO Z>" | null,
                  "box_branch": "<text>" | null, "box_head": "<12>" | null, "origin_box_head": "<12>" | null,
                  "trunk_head": "<12>" | null, "unpushed": <int> | null, "pushed_not_on_trunk": <int> | null,
                  "behind_trunk": <int> | null,
                  "state": "committed, not pushed" | "pushed, not on trunk" | "on trunk" | "not recorded",
                  "unread": ["<text>"],
                  "last_pass": {"mode": "<text>", "rc": <int>, "note": "<text>", "serial": "<text>"} | null,
                  "integration_refused": {"at": "<ISO Z>", "note": "<text>"} | "not recorded" } ] }
   ```
   - **`boxes`:** one row per roster box, in roster order, from that box's `latest.json`. A NoSuchKey/404 gives
     `status` "not recorded", `state` "not recorded", every other field null, and `unread` [].
   - **Field mapping:** shas are cut to 12 characters. `unpushed` and `pushed_not_on_trunk` carry the record's `.count`.
   - **`state` rule, in this order:**
     1. `unpushed.count > 0` -> "committed, not pushed";
     2. else `pushed_not_on_trunk.count > 0` -> "pushed, not on trunk";
     3. else any of `box_head`, `trunk_head` or the two counts is null -> "not recorded";
     4. else "on trunk".
   - **`trunk.head`:** the `trunk_head` (12 characters) of the newest `latest.json`, by `at`.
   - **`trunk.first_seen`:** the earliest `at` among the HISTORY records of every box whose key stamp is within the last
     48 hours and whose `trunk_head` equals that head. List `gitstate/box=<B>/` per roster box and parse the stamp from
     the key; `latest.json` is not history.
   - **`trunk.claim` and `basis`:** `claim` is always "inferred". `basis` says, in words, that this is the first record
     seen carrying the head, not the push time, which has no recorded home (C14).
   - **`integration_refused`:** the newest history record of that box with `pass.mode == "integrate"` and `pass.rc != 0`,
     as `{at, note}`. If there is none, the literal string "not recorded".
   - **Failure:** a listing failure, or a read failure that is not NoSuchKey/404, returns **503**
     `{"error": "store unreadable", "reason": "<ExceptionClass: message>"}`.
   - **Load:** run the S3 work in `run_in_threadpool`. Fetch at most 8 bodies at a time.
2. **DO NOT edit `app/admin_api.py`.** The issuer adds `Route("/fabric/gitstate", admin_fabric_gitstate.gitstate,
   methods=["GET"])` at the merge. Name that line in your report.
3. **`tests/test_admin_fabric_gitstate.py` (new).** Mount the handler as `tests/test_admin_fabric.py` does: the owner
   stubbing, a fake S3 client and `TestClient`. These six tests, by these exact names:
   - `test_gitstate_state_rule`. Four planted roster boxes: one with `unpushed.count` 3, one with `pushed_not_on_trunk.count`
     2, one with both 0, and one with a null `trunk_head`. They read "committed, not pushed", "pushed, not on trunk",
     "on trunk" and "not recorded".
   - `test_gitstate_absent_box_reads_not_recorded`. NoSuchKey on one box's `latest.json` gives `status` and `state` "not
     recorded", null fields, and the other boxes unaffected.
   - `test_gitstate_integration_refused`. A history record with `pass.mode` "integrate" and rc 4 is shown with its `at` and
     `note`. A box whose history has only "box" passes reads the literal "not recorded".
   - `test_gitstate_store_unreadable_returns_503`. The listing raises ClientError AccessDenied. Expect 503 with `error`
     "store unreadable".
   - `test_gitstate_non_owner_is_refused`. A non-owner gets 403, and the fake client records zero calls.
   - `test_real_capture_gitstate`. Serve the VERBATIM capture
     `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/fixtures/s3_capture_20261009T0728Z.json`
     (`{"objects": {<s3 key>: <parsed body>}}`; the repo root is four parents above the gateway dir) from a fake client
     that lists by prefix and gets by key. Pin "now" to 2026-10-09T08:00:00Z. Assert:
     - all four roster boxes read "recorded";
     - each box's `state` equals the rule above applied, IN THE TEST, to that box's captured `latest.json`;
     - `trunk.head` equals the newest captured `latest.json`'s `trunk_head[:12]`, with `claim` "inferred".

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change `admin_fabric.py`, `admin_api.py`, `owner_gate.py`, any
   other `app/` module, Terraform, the manifest, `.tools/` or anything in `mcportal/`. Make no deploy and no AWS call.
2. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_fabric_gitstate.py
infra/aws/ec2/opal-gateway/tests/test_admin_fabric_gitstate.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~9/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `.tools/fabric-gitstate.py`, `.tools/box-sync.sh`, `infra/aws/ec2/opal-gateway/app/admin_fabric.py`,
`app/owner_gate.py`, `tests/test_admin_fabric.py`, `org/devices/DEVICES.json`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/` (fixture and checks).

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W9-S<k>` (the next free k for W9). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-g-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/g1.AC1.sh; echo "exit=$?"</invocation><expect>gitstate tests: 0 failed; named tests PASSED 5 of 5 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-g-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/g1.AC2.sh; echo "exit=$?"</invocation><expect>gitstate real capture: 0 failed; named tests PASSED 1 of 1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~9/NFRA_MCPORTAL.TO-MP-g-1.fabric-gitstate-handler.proof_of_spec.json`.
Report once, with:
- the two check outputs;
- the commit hash;
- the route line for the issuer;
- the real capture's four box states and the trunk row as served;
- any field you could not fill as written, and why;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the CP2 issuance (decomposition v6) from PRD v0.5 FWD-16, C14, A16 @cecf26d2c9. Checks dry-run at base
2851a9190d: AC1 FAIL (test file absent), AC2 FAIL (test file absent). The capture holds 71 gitstate objects (4 latest.json;
pass modes: box 53, integrate 17, manual 1). No gate. Lives through MP-r-2.

<status>pending</status>
<round>1</round>
<workstream>CP2</workstream>
<slot>~9</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
