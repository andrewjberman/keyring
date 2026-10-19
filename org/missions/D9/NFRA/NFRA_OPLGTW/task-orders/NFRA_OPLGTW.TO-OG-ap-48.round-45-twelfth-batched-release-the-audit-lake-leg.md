# NFRA_OPLGTW task order -- `OG-ap-48` -- APPLY: the round-45 twelfth batched gateway release -- the audit lake leg bounded and audible (`OG-pr-6`: `app/audit.py` and `tests/test_og_pr6.py`), under its own never-widen; NO ARMING

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-48</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-48</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; you still run `comp-schedule --drift` at the act and record what it scanned.
comp-iam: DECLARED-NOT-APPLICABLE -- the release changes NO IAM and writes NO SSM parameter. The audit client's S3 `put_object` is the SAME call the live ref makes (only its client Config changes). NOTHING ARMS THE PROBE LISTENER IN THIS ORDER (the lease parameter stays absent; you read that it is absent before and after).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-44 analysis, list item 3 (msg 35898): "the twelfth release, carrying OG-pr-6; Phase B also prints the new failure counter's value (expected 0) beside the dual count".
EGRESS CLASS, declared: NONE beyond Opal's own AWS. (Phase A's black-hole put targets a non-routable address inside a scratch fresh process; it never leaves the host.)
</preflight>

## 1. THE CELL -- `OG-ap-48` (decomposition addendum R3-T.122, round 45, workstream ENRICH-R45-B)

**METHOD = `OG-ap-46`'s, read in `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-ap-46.round-44-eleventh-batched-release-family-depth-and-comment.md` (through it `OG-ap-44`'s and `OG-ap-42`'s, each with its amendments) and followed step by step; this order states only what differs.** That includes the HARD-GUARD RULE for every fresh-process run, the live-ref re-read on the host, the re-cut in a clean sparse tree with the overlay disclosure, the three-half ask, the ledger opened with entry AND sentinel first, no `HALT_OVERRIDE`, the 30-minute read-back, and the host clock and `systemctl --failed` read and PRINTED BEFORE THE LEDGER IS CLOSED.

⛔ **STAGED BEHIND `OG-pr-6`** having drained to trunk and read COMPLETE. The GO names `trunk_sha`.

⛔ **THE BASE IS THE LIVE REF READ ON THE HOST** (`/opt/opal-gateway/.deployed_commit`; expected `e09c30c3f064296ae7f8eb2c47b91bfec0be9b60`, your eleventh release); record it as `live_ref_host` and make it `base_sha`; if it is anything else (dell1 may deploy again), STOP and file a row. `6575999df5` must be an ancestor of `base_sha`. dell1's four harvest files are byte-equal between base and release (the take list is TWO files, so the diff itself enforces it; the ask still names their blobs as read at `base_sha`).

⛔ **STANDING CONDITIONS FOR EVERY ROUND-45 RELEASE** (the CTO's round-44 analysis section 2 and the CVO's verdict 35844): (1) the base is the live ref at the GO; (2) the ask carries the line `process-wide state this change touches: <list>, or none, read`: here, STDERR VOLUME (one line on the first failed lake put, then at most one line per 60 s) and the boto3 S3 client's botocore Config (explicit connect and read timeouts and a one-attempt retry cap); you read `app/audit.py` and the worker's diff to say so; every Phase B prints the journal `POST /mcp` count AND the audit-lake count for ONE window; journal 0 against a non-zero lake does not grade until explained; (3) every read-only audit record pins its base sha.

APPLY: ONE code release. No Terraform, no IAM, no env key, no change to the unit file, `deploy-to-ec2.sh` or `EC2_MANIFEST.json` by hand, one deploy, ledger `nfra-oplgtw-gateway-release-batch13`. The take list is TWO files taken whole from trunk at `trunk_sha`, each byte-equal to trunk's blob: `infra/aws/ec2/opal-gateway/app/audit.py` (its diff against the live ref must be exactly the failure counter, the rate-bounded stderr line, the explicit `Config` and the imports they need; the floor-write lines of `_emit` byte-equal to the live ref's; any other hunk is a STOP and a row) and `infra/aws/ec2/opal-gateway/tests/test_og_pr6.py` (new). NOT in this release (the check counts them at 0): `server.py`, `graph.py`, `tools.py`, `probe_listener.py`, every `client_*.py`, `typed_scope.py`, `etfs_rivals_flow.py`, `destructive_ops.py`, `deploy-to-ec2.sh`, the unit file, `EC2_MANIFEST.json`, the catalog, Terraform.

### PHASE A (only on the issuer's GO): re-cut, HOST MEASUREMENTS UNDER THE GUARD, ask. NO deploy IN ANY FORM

Steps 1 and 2 as `OG-ap-46`, in `C:/tmp/og-rel-batch13`, branch `rel-nfra-oplgtw-batch13`; write `W/ap48_release.json` = `{"base_sha", "release_sha", "trunk_sha", "live_ref_host"}` (FULL 40-character shas; `base_sha` equals `live_ref_host`). In the release tree: the taken test file (`test_og_pr6.py`), the existing audit tests (`test_audit_bytes_principal.py`, `test_audit_lake_key_stamp.py`, `test_audit_rivalfunds_args.py`, `test_og_en10.py`) and the window test files in BOTH orders, using `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh`; the full suite's failing set compared with the live ref's (name each difference); `bash -n deploy-to-ec2.sh` and `--preflight-only`; the host-shaped import check.
3. **THE HOST MEASUREMENTS** (candidate staged in a scratch copy on the host, removed after; every gateway-code run in a fresh process under the HARD GUARD; stop at 75 percent host used; the running service is NOT touched; NO SSM write; no write to the real audit lake). In ONE fresh process with `AUDIT_S3_BUCKET` set to a throwaway name, `AUDIT_PATH` a scratch file, and the environment variable `AWS_ENDPOINT_URL_S3` set to a black-hole address (`http://10.255.255.1:9`, non-routable: the put can only time out): import the candidate's `app.audit`, call `audit._emit` ONCE with a small record, and read (a) the client's configuration from `audit._s3_client.meta.config` (`connect_timeout`, `read_timeout`, the retry `max_attempts`), (b) the wall time of the failed put (must be bounded: at most 15 s; it is expected near the connect timeout), (c) `audit.lake_put_failure_count()` (must read 1), (d) the number of lines written to stderr (must read 1), (e) that the floor file holds exactly the one line. Then run the SAME call with the LIVE ref's `audit.py` and record, as a disclosure in the ask (not a criterion), how long ITS failed put took (the default Config's connect timeout is 60 s: use a 70 s wall limit and report a timeout as such). Write `W/PHASE_A_OG-ap-48.json` = `{"body": {"release_sha", "audit_leg": {"config": {"connect_timeout": n, "read_timeout": n, "max_attempts": n}, "failed_put_wall_s": x, "counter_after_failure": 1, "stderr_lines": 1, "floor_line_written": true, "guard": "<named guard>"}, "listener": {"bound_host": "127.0.0.1", "off_by_default": true, "armings": 0, "lease_parameter_written": false}, "tests": {"named_passed": n, "named_failed": 0, "window_set_passed": n, "window_set_failed": 0}, "process_wide_state": "<what the change touches, or 'none, read' with the files you opened>"}}`. Anything that fails: STOP, file a BLOCKING row with the numbers, write NO ask, report.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-48.md`, for THREE halves, each under a heading containing its word: the `diff` by file with the hunk attribution; the `widening` (NONE widens: no route, tool, IAM, env key, unit or page size; the lake put is the same call with a bounded client; a failed put now adds a counter and at most one stderr line per 60 s; no arming); the `order` of acts; `both branches`; the `rollback` (redeploy the live ref's tree; there is no lease); the `triggers` (health not 200 in 60 s; a tool of the 27 not answering under the guard; the `.env` key count not 65; `tools/list` changing from 103; md5 beyond the two released paths; the md5 of any of dell1's four harvest files not equal to its blob; host memory above 85 percent; `NRestarts` above 0; the listener answering any call with no lease; the marker not equal to the release sha; no `POST /mcp` access line under traffic in the 30-minute read-back; **any `audit-lake WARN` line in the journal during the read-back**, since a failing lake put in production is exactly what the new line reports); the line `process-wide state this change touches: ...`; the gate lines. Commit, run AC1 (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r45/checks/ap48.AC1.sh`), REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

5. As `OG-ap-42` step 5 with ledger `nfra-oplgtw-gateway-release-batch13`, deploy from `C:/tmp/og-rel-batch13`, `DEPLOY_BASE_REF=<the live ref read on the host>`.
6. **The served read, UNARMED ONLY, and the counts**, writing `W/CODE13_SERVED.json` (fields as in `ap48.AC2.sh`'s header, the same as `CODE12` plus `audit_failure_counter`). The lease parameter ABSENT before and after; a connection to the listener answers 403 `probe_not_armed`; `armings` 0. **THE COUNTS (standing condition 2):** the service's own `POST /mcp` journal lines over the 30-minute read-back and, over the SAME window, the audit-lake records (method as in your `ap42_graphcounts.py`; state it in `access_log.method`); the rule fixed before the run: lines > 0 and lines >= 0.25 times the records; the listener's own access lines (`POST /probe/...` from 127.0.0.1) are counted SEPARATELY and EQUAL the listener requests you made (at least three). **THE NEW COUNTER (the CTO's):** `audit_failure_counter` = `{"journal_lines_readback": n, "counter_value": n, "method": "<how counted>"}`: the number of `audit-lake WARN` lines in the journal over the read-back, and the counter's value as the last `count=` those lines print (0 when there is no line); the counter is read by no route, so the journal line is its only observation. Both must read 0 (a nonzero value is a failing lake put in production, a TRIGGER until explained). The service PID is stable, `NRestarts` is 0, the 27-tool read passes 27 of 27 under the hard guard in a fresh process, and `tools/list` is equal before and after.
7. Standing clauses as `OG-ap-38` step 7; the host clock and failed units read BEFORE the ledger closes; close the ledger; commit; run `ap48.AC2`; report once per phase; send me the ledger CLOSED time and the live sha (I tell the CTO and `0.0.0_AB_MSTR~Z`).

### AMENDMENT A1 (issuer, 2026-10-19 ~07:0xZ, on the CVO's finding 2 in the CVO half @c57a121b47, the CTO's CT3 @2f57a5ef26 and my F6): what an `audit-lake WARN` line in the Phase B read-back DOES

The ask's section 6 lists any `audit-lake WARN` line as a trigger for an immediate rollback. All three halves read the same trouble with that: a WARN most likely reports a lake failure that already happened SILENTLY under the live ref, and rolling back would hide it again and bring back the put that stalls for over a minute. The ask's bytes stay (the halves bind to them); THIS AMENDMENT governs the WARN line and supersedes the ask's section 6 on that one trigger. On any `audit-lake WARN` line in the journal during the read-back: (1) report it to me AND `1.0.0_SA_CTO~Z` the same turn, with the exception CLASS NAME the line prints, the running `count=` and the rate (lines per minute); (2) read the same window's healthy puts (the audit-lake records written in the window): ROLL BACK only if the failures look caused by the new timeouts, that is a timeout class (`ConnectTimeoutError`, `ReadTimeoutError`, `EndpointConnectionError`) while healthy puts in the same window land in under 2 s; (3) otherwise HOLD, file the lake failure as a row (OBSERVATION, disarm_owner me) and carry on. Every other trigger of the ask stays an immediate rollback. `ap48.AC2` still requires `audit_failure_counter` 0 and 0 lines to PASS, so a WARN means the order does not close on that read-back until I rule on your report.

## 2. BOUNDS

- The release's files only. No IAM or Terraform change, no env key, no deploy-script, unit or manifest edit by hand; NO SSM write of any parameter; no write to the real audit lake in Phase A. No account number, person's name, credential or object content in any record (`****<last4>` form only).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply`; arm the probe listener; set `MUSE_CLIENT_ID`; **run gateway code on the host without the hard guard**.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-batch13.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-48"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r45/checks/ap48.AC1.sh; echo "exit=$?"</invocation><expect>(?s)SSRF audit \(OG-sec-3, outbound HTTP code unchanged by this release\) verdict and controllable count: CLEAN 0 \(want CLEAN 0\).*is the live ref read on the host: yes; dell1 harvest release 6575999df5 is an ancestor of base: yes.*four harvest files byte-equal between the live base and the release: 4 of 4 \(want 4 of 4\).*outside the take list 0 \(want 0\); take-list files missing 0 \(want 0\); not byte-equal to trunk's 0 \(want 0\).*process-wide state this change touches, as recorded in Phase A \(CVO verdict 35844\): named.*audit lake leg on the host: client Config connect [0-9.]+ s, read [0-9.]+ s, attempts [12]; a put to a black-hole endpoint raised in [0-9.]+ s; failure counter 1 and stderr lines 1 after one failure; the local floor line still written True: ok.*armings 0 \(want 0\).*ask has the three halves and the process-wide state line yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-48"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r45/checks/ap48.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; landed=(current|superseded).*the 27-tool read 27 of 27 under the hard guard yes.*read BEFORE the ledger closed True: ok.*listener read UNARMED only: armings 0 \(want 0\), unarmed answer 403 probe_not_armed.*: ok.*ACCESS LOG BACK: POST /mcp journal lines \d+ against \d+ audit records over the same 30-minute window.*: ok.*AUDIT FAILURE COUNTER \(the new lake-put failure line, expected 0\): journal failure lines \d+ over the read-back, counter value \d+: ok.*served verdict: OK.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me on my run before any GO to Phase B; `AC2` (Phase B) after the ledger closes.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-48.round-45-twelfth-batched-release-the-audit-lake-leg.proof_of_spec.json` after Phase B and validate it with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 45, workstream ENRICH-R45-B. Source: the CTO's round-44 analysis (`ledger/ROUND_ANALYSIS.round44.md` @ebefeda213, msg 35898), list item 3 and standing conditions.
- READING DISCLOSED TO THE CTO: "Phase B also prints the new failure counter's value (expected 0)": the counter is a module variable read by no route, so its observable is the `audit-lake WARN` journal line (the counter value is the last `count=` it prints, 0 when there is none); both read 0 or the read-back has a TRIGGER. The Phase A black-hole put is a scratch fresh-process measurement with a non-routable endpoint, not a write to the real lake.
- Pre-cut: `AC1` and `AC2` base FAIL as expected (the records are absent).

<status>staged</status>
<round>45</round>
<workstream>ENRICH-R45-B</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
