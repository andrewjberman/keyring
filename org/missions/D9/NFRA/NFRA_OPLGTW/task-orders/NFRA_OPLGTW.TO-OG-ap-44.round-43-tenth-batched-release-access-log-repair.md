# NFRA_OPLGTW task order -- `OG-ap-44` -- APPLY: the round-43 tenth batched gateway release -- the repair of the access-log regression (`Z-S395`, `OG-pr-5`), under its own never-widen; NO ARMING; ahead of `OG-ev-7`

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-44</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-44</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; you still run `comp-schedule --drift` at the act and record what it scanned.
comp-iam: DECLARED-NOT-APPLICABLE -- the release changes NO IAM and writes NO SSM parameter. NOTHING ARMS THE PROBE LISTENER IN THIS ORDER (the lease parameter stays absent; you read that it is absent before and after).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling on your row `Z-S395` (msg 35769): "cut a repair cell in round 43 ... ships in a batched release under its own never-widen, ahead of OG-ev-7".
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-44` (decomposition addendum R3-T.120 amendment A1, round 43, workstream ENRICH-R43-C)

**METHOD = `OG-ap-42`'s, read in `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-ap-42.round-43-ninth-batched-release-firm-pin-and-graph-pin.md` (with its amendment A1) and followed step by step; this order states only what differs.** That includes the HARD-GUARD RULE for every fresh-process run, the live-ref re-read on the host, the re-cut in a clean sparse tree with the overlay disclosure, the three-half ask, the ledger opened with entry AND sentinel first, no `HALT_OVERRIDE`, the 30-minute read-back, and the host clock and `systemctl --failed` read and PRINTED BEFORE THE LEDGER IS CLOSED.

⛔ **STAGED BEHIND `OG-pr-5`** having drained to trunk and read COMPLETE. The GO names `trunk_sha`.

⛔ **THE BASE IS THE LIVE REF READ ON THE HOST** (`/opt/opal-gateway/.deployed_commit`; expected `a0c83303ee48c95c16a61c0d5e8bd186b1083b66`, your ninth release, on dell1's `922ee425fe`); record it as `live_ref_host` and make it `base_sha`; if it is anything else (dell1 may deploy again), STOP and file a row. `6575999df5` must be an ancestor of `base_sha`. dell1's four harvest files are byte-equal between base and release (the take list is TWO files, so the diff itself enforces it; the ask still names their blobs as read at `base_sha`).

APPLY: ONE code release. No Terraform, no IAM, no env key, no change to the unit file, `deploy-to-ec2.sh` or `EC2_MANIFEST.json` by hand, one deploy, ledger `nfra-oplgtw-gateway-release-batch11`. The take list is TWO files taken whole from trunk at `trunk_sha`, each byte-equal to trunk's blob: `infra/aws/ec2/opal-gateway/app/probe_listener.py` (its diff against the live ref must be exactly the logger snapshot and restore of `OG-pr-5` in `make_server`; any other hunk is a STOP and a row) and `infra/aws/ec2/opal-gateway/tests/test_og_pr5.py` (new). NOT in this release (the check counts them at 0): `server.py`, `graph.py`, `tools.py`, every `client_*.py`, `typed_scope.py`, `etfs_rivals_flow.py`, `destructive_ops.py`, `deploy-to-ec2.sh`, the unit file, `EC2_MANIFEST.json`, the catalog and `app/refs/`, Terraform.

### PHASE A (only on the issuer's GO): re-cut, HOST MEASUREMENTS UNDER THE GUARD, ask. NO deploy IN ANY FORM

Steps 1 and 2 as `OG-ap-42`, in `C:/tmp/og-rel-batch11`, branch `rel-nfra-oplgtw-batch11`; write `W/ap44_release.json` = `{"base_sha", "release_sha", "trunk_sha", "live_ref_host"}` (FULL 40-character shas). In the release tree: the two taken test files in both orders with the window files, the full suite's failing set compared with the live ref's (name each difference), `bash -n deploy-to-ec2.sh` and `--preflight-only`, the host-shaped import check.
3. **THE HOST MEASUREMENTS** (candidate staged in a scratch copy on the host, removed after; every gateway-code run in a fresh process under the HARD GUARD; stop at 75 percent host used; the running service is NOT touched; NO SSM write). In ONE fresh process: build the service-style `uvicorn.Config` (as the service builds its own, with the service's log settings read from `server.py`'s run call), attach a capturing handler to `uvicorn.access`, snapshot the four loggers `uvicorn`, `uvicorn.error`, `uvicorn.access` and `uvicorn.asgi` (level, handler objects, propagate, disabled, filters), call the candidate's `probe_listener.make_server(port=0)`, compare: write `W/PHASE_A_OG-ap-44.json` = `{"body": {"release_sha", "loggers": {"checked": ["uvicorn", "uvicorn.error", "uvicorn.access", "uvicorn.asgi"], "loggers_unchanged": true, "access_record_reaches_handler": true, "restore_on_raise": true, "listener_access_log": false, "guard": "<named guard>"}, "listener": {"bound_host": "127.0.0.1", "off_by_default": true, "armings": 0, "lease_parameter_written": false}, "tests": {"named_passed": n, "named_failed": 0, "window_set_passed": n, "window_set_failed": 0}}}`. In the same fresh process ALSO build the LIVE ref's `make_server` the same way and record, as a disclosure in the ask (not as a criterion), that its snapshot DIFFERS (this is the regression reproduced on the host). Anything that fails: STOP, file a BLOCKING row with the numbers, write NO ask, report.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-44.md`, for THREE halves, each under a heading containing its word: the `diff` by file with the hunk attribution; the `widening` (NONE widens; the service's access log is RESTORED to what it was before `OG-ap-40`; the listener still writes none; no arming); the `order` of acts; `both branches`; the `rollback` (redeploy the live ref's tree; there is no lease); the `triggers` (health not 200 in 60 s; a tool of the 27 not answering under the guard; the `.env` key count not 65; `tools/list` changing; md5 beyond `probe_listener.py`; the md5 of any of dell1's four harvest files not equal to its blob; host memory above 85 percent; `NRestarts` above 0; the listener answering any call with no lease; the marker not equal to the release sha; and **no `POST /mcp` access line in the journal under traffic in the 30-minute read-back**); the gate lines. Commit, run AC1 (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ap44.AC1.sh`), REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

5. As `OG-ap-42` step 5 with ledger `nfra-oplgtw-gateway-release-batch11`, deploy from `C:/tmp/og-rel-batch11`, `DEPLOY_BASE_REF=<the live ref read on the host>`.
6. **The served read, UNARMED ONLY, and the access log**, writing `W/CODE11_SERVED.json` (fields as in `ap44.AC2.sh`'s header). The lease parameter ABSENT before and after; a connection to the listener answers 403 `probe_not_armed`; `armings` 0. **THE ACCESS LOG (the CTO's criterion):** count the service's own `POST /mcp` lines in the journal over the 30-minute read-back and, over the SAME window, the audit-lake records (the method of your `ap42_graphcounts.py`; state it in `access_log.method`); the baseline is the window before the `OG-ap-40` deploy (157 to 171 lines per 30 minutes). The rule is fixed before the run: lines > 0 and lines >= 0.25 times the audit records; the listener's own lines in the journal: 0. The service PID is stable, `NRestarts` is 0, the 27-tool read passes 27 of 27 under the hard guard in a fresh process, and `tools/list` is equal before and after.
7. Standing clauses as `OG-ap-38` step 7; the host clock and failed units read BEFORE the ledger closes; close the ledger; commit; run `ap44.AC2`; report once per phase; send me the ledger CLOSED time and the live sha (I tell the CTO and `0.0.0_AB_MSTR~Z`).

## 2. BOUNDS

- The release's files only. No IAM or Terraform change, no env key, no deploy-script, unit or manifest edit by hand; NO SSM write of any parameter. No account number, person's name, credential or object content in any record (`****<last4>` form only).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply`; arm the probe listener; set `MUSE_CLIENT_ID`; **run gateway code on the host without the hard guard**.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-batch11.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-44"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ap44.AC1.sh; echo "exit=$?"</invocation><expect>(?s)is the live ref read on the host: yes; dell1 harvest release 6575999df5 is an ancestor of base: yes.*four harvest files byte-equal between the live base and the release: 4 of 4 \(want 4 of 4\).*outside the take list 0 \(want 0\); take-list files missing 0 \(want 0\); not byte-equal to trunk's 0 \(want 0\).*uvicorn loggers on the host after the listener's server is built: unchanged True.*armings 0 \(want 0\).*ask has the three halves yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-44"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ap44.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; landed=(current|superseded).*the 27-tool read 27 of 27 under the hard guard yes.*read BEFORE the ledger closed True: ok.*listener read UNARMED only: armings 0 \(want 0\).*: ok.*ACCESS LOG BACK: POST /mcp journal lines \d+ against \d+ audit records over the same 30-minute window.*listener lines in the journal 0: ok.*served verdict: OK.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me on my run before any GO to Phase B; `AC2` (Phase B) after the ledger closes.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-44.round-43-tenth-batched-release-access-log-repair.proof_of_spec.json` after Phase B and validate it with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`. The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 43, workstream ENRICH-R43-C (a third issuance in round 43; decomposition addendum R3-T.120 amendment A1). The CTO's ruling on `Z-S395` (msg 35769). Chain: `OG-pr-5` (slot `~156`) then this order; `OG-ev-7` follows its close.
- The rule for the access-log criterion (`lines > 0` and `lines >= 0.25 x audit records`) is the issuer's: the earlier windows read about 0.55 (about 164 lines to 295 records); 0.25 tolerates the audit lake counting tool and login records the access log does not, and a restoration to near zero cannot pass.
- `ap44.AC1` also requires `6575999df5` as an ancestor of the base and the SSRF audit record `CLEAN 0` (outbound code is unchanged; the record is read, not re-run).
- Pre-cut: `AC1` and `AC2` base FAIL as expected (the records are absent); `ap44.AC2`'s python half graded a good record OK and a zero-lines, a 40-of-290 and a listener-lines record NO.

<status>staged</status>
<round>43</round>
<workstream>ENRICH-R43-C</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
