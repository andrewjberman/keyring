# NFRA_OPLGTW task order -- `OG-ap-46` -- APPLY: the round-44 eleventh batched gateway release -- the site Z code that is on trunk and in no release (`family_depth.py` with its data and test) and the corrected listener comment, under its own never-widen; NO ARMING

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-46</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-46</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; you still run `comp-schedule --drift` at the act and record what it scanned.
comp-iam: DECLARED-NOT-APPLICABLE -- the release changes NO IAM and writes NO SSM parameter. The `family_depth` read grant (`family_depth_read_iam.tf`) is NOT part of this release and is not applied by it. NOTHING ARMS THE PROBE LISTENER IN THIS ORDER (the lease parameter stays absent; you read that it is absent before and after).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-43 analysis, list item 5 (msg 35841): "the eleventh release: `family_depth.py` and the comment fix; `admin_people_access.py` ONLY on the written yes of 2.0.0_SA_COO~MP".
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-46` (decomposition addendum R3-T.121, round 44, workstream ENRICH-R44-B)

**METHOD = `OG-ap-44`'s, read in `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-ap-44.round-43-tenth-batched-release-access-log-repair.md` (through it `OG-ap-42`'s, each with its amendments) and followed step by step; this order states only what differs.** That includes the HARD-GUARD RULE for every fresh-process run, the live-ref re-read on the host, the re-cut in a clean sparse tree with the overlay disclosure, the three-half ask, the ledger opened with entry AND sentinel first, no `HALT_OVERRIDE`, the 30-minute read-back, and the host clock and `systemctl --failed` read and PRINTED BEFORE THE LEDGER IS CLOSED.

⛔ **STAGED BEHIND `OG-en-34`** having drained to trunk and read COMPLETE (the corrected comment must be on trunk before it can be taken). The GO names `trunk_sha` and says whether `W/MP_YES.md` exists.

⛔ **THE BASE IS THE LIVE REF READ ON THE HOST** (`/opt/opal-gateway/.deployed_commit`; expected `eff517546eeea48811cf13f3de38926c5944c6df`, your tenth release); record it as `live_ref_host` and make it `base_sha`; if it is anything else (dell1 may deploy again), STOP and file a row. `6575999df5` must be an ancestor of `base_sha`. dell1's four harvest files are byte-equal between base and release (the diff itself enforces it; the ask still names their blobs as read at `base_sha`).

⛔ **STANDING CONDITIONS FOR EVERY ROUND-44 RELEASE** (the CTO's round-43 analysis section 3 and the CVO's verdict 35844, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/3.0.0_SA_CVO~Z/GOVERNANCE_VERDICT_tick145_process_wide_state_line_20261019.md`):
1. The ask carries the line `process-wide state this change touches: <list>, or none, read` (loggers, signal handlers, environment, `sys.path`, global config). "Read" means you opened the code that constructs the change; here that is `app/probe_listener.py` (a comment only) and the `family_depth` module (a module with no import-time side effect: verify it by reading its top level). `ap46.AC1` refuses an ask without the line and a Phase A record without `process_wide_state`.
2. Every Phase B prints the journal `POST /mcp` count AND the audit-lake count for ONE window (`access_log` in `W/CODE12_SERVED.json`); journal 0 against a non-zero lake does not grade until explained (`ap46.AC2` requires lines above 0 and at least 0.25 times the records).

APPLY: ONE code release. No Terraform, no IAM, no env key, no change to the unit file, `deploy-to-ec2.sh` or `EC2_MANIFEST.json` by hand, one deploy, ledger `nfra-oplgtw-gateway-release-batch12`. The take list is FOUR REQUIRED files taken whole from trunk at `trunk_sha`, each byte-equal to trunk's blob: `infra/aws/ec2/opal-gateway/app/family_depth.py` (site Z's own, `OG-cd-1`; on trunk and in no release), `infra/aws/ec2/opal-gateway/app/refs/silver_families.json` (the data file `family_depth.py` reads), `infra/aws/ec2/opal-gateway/tests/test_og_cd1.py` (its test), `infra/aws/ec2/opal-gateway/app/probe_listener.py` (its diff against the live ref must be exactly the corrected comment of `OG-en-34`; any other hunk is a STOP and a row). **If** `W/MP_YES.md` exists (the issuer writes it when `2.0.0_SA_COO~MP` answers in writing that `app/admin_people_access.py` may ride, quoting the answer and its message id), the OPTIONAL pair `infra/aws/ec2/opal-gateway/app/admin_people_access.py` and `infra/aws/ec2/opal-gateway/tests/test_admin_people_access.py` is taken too; **if it does not exist the pair is NOT in the release** and the ask and your report say so. `ap46.AC1` enforces both directions. NOT in this release (the check counts them at 0): `server.py`, `graph.py`, `tools.py`, every `client_*.py`, `typed_scope.py`, `etfs_rivals_flow.py`, `destructive_ops.py`, `deploy-to-ec2.sh`, the unit file, `EC2_MANIFEST.json`, the catalog, any Terraform. THE RELEASE LEAVES `family_depth` INERT: read `app/server.py` and `app/tools.py` of the release and show they do not import or name it (`ap46.AC1` counts 0 such lines); the module's route is not mounted by this release. Check that the three taken `family_depth` files are the ONLY ones it needs at import (read `family_depth.py`'s imports and file reads against the release tree); if it needs a further file that is on trunk and in no release, STOP and file a row naming it.

### PHASE A (only on the issuer's GO): re-cut, HOST MEASUREMENTS UNDER THE GUARD, ask. NO deploy IN ANY FORM

Steps 1 and 2 as `OG-ap-42`, in `C:/tmp/og-rel-batch12`, branch `rel-nfra-oplgtw-batch12`; write `W/ap46_release.json` = `{"base_sha", "release_sha", "trunk_sha", "live_ref_host"}` (FULL 40-character shas; `base_sha` equals `live_ref_host`). In the release tree: the taken test files (`test_og_cd1.py`, `test_og_pr1.py`, `test_og_pr5.py`, plus `test_admin_people_access.py` when the pair is taken) and the window test files in BOTH orders, using `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh` once `OG-en-33` has repaired it (it keeps the forward text); the full suite's failing set compared with the live ref's (name each difference); `bash -n deploy-to-ec2.sh` and `--preflight-only`; the host-shaped import check.
3. **THE HOST MEASUREMENTS** (candidate staged in a scratch copy on the host, removed after; every gateway-code run in a fresh process under the HARD GUARD; stop at 75 percent host used; the running service is NOT touched; NO SSM write). As `OG-ap-44` step 3 (the four uvicorn loggers unchanged after the candidate's `make_server`, an INFO record on `uvicorn.access` reaches the handler, the restore on a raising `Config`), plus: import `app.family_depth` in a fresh guarded process and record that the import starts no thread, opens no socket and reads no AWS resource (counts from a stub of `boto3` and `socket`). Write `W/PHASE_A_OG-ap-46.json` = `{"body": {"release_sha", "loggers": {"checked": ["uvicorn", "uvicorn.error", "uvicorn.access", "uvicorn.asgi"], "loggers_unchanged": true, "access_record_reaches_handler": true, "restore_on_raise": true, "listener_access_log": false, "guard": "<named guard>"}, "listener": {"bound_host": "127.0.0.1", "off_by_default": true, "armings": 0, "lease_parameter_written": false}, "tests": {"named_passed": n, "named_failed": 0, "window_set_passed": n, "window_set_failed": 0}, "process_wide_state": "<what the change touches, or 'none, read' with the files you opened>", "family_depth_import": {"threads_started": 0, "sockets_opened": 0, "boto3_calls": 0}}}`. Anything that fails: STOP, file a BLOCKING row with the numbers, write NO ask, report.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-46.md`, for THREE halves, each under a heading containing its word: the `diff` by file with the hunk attribution; the `widening` (NONE widens: a comment, an inert module, its data and test; no new route, no new tool, no IAM; the optional pair stated as in or out); the `order` of acts; `both branches`; the `rollback` (redeploy the live ref's tree; there is no lease); the `triggers` (health not 200 in 60 s; a tool of the 27 not answering under the guard; the `.env` key count not 65; `tools/list` changing; md5 beyond the released paths; the md5 of any of dell1's four harvest files not equal to its blob; host memory above 85 percent; `NRestarts` above 0; the listener answering any call with no lease; the marker not equal to the release sha; no `POST /mcp` access line in the journal under traffic in the 30-minute read-back); the line `process-wide state this change touches: ...`; the gate lines. Commit, run AC1 (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/ap46.AC1.sh`), REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

5. As `OG-ap-42` step 5 with ledger `nfra-oplgtw-gateway-release-batch12`, deploy from `C:/tmp/og-rel-batch12`, `DEPLOY_BASE_REF=<the live ref read on the host>`.
6. **The served read, UNARMED ONLY, and the counts**, writing `W/CODE12_SERVED.json` (fields as in `ap46.AC2.sh`'s header, the same as `CODE11`). The lease parameter ABSENT before and after; a connection to the listener answers 403 `probe_not_armed`; `armings` 0. **THE COUNTS (standing condition 2):** the service's own `POST /mcp` journal lines over the 30-minute read-back and, over the SAME window, the audit-lake records (method as in your `ap42_graphcounts.py`; state it in `access_log.method`); the rule is fixed before the run: lines > 0 and lines >= 0.25 times the records; the listener's own access lines (`POST /probe/...` from 127.0.0.1) are counted SEPARATELY and EQUAL the listener requests you made (at least three). The service PID is stable, `NRestarts` is 0, the 27-tool read passes 27 of 27 under the hard guard in a fresh process, and `tools/list` is equal before and after.
7. Standing clauses as `OG-ap-38` step 7; the host clock and failed units read BEFORE the ledger closes; close the ledger; commit; run `ap46.AC2`; report once per phase; send me the ledger CLOSED time and the live sha (I tell the CTO and `0.0.0_AB_MSTR~Z`).

## 2. BOUNDS

- The release's files only. No IAM or Terraform change (the `family_depth` IAM `.tf` stays unapplied), no env key, no deploy-script, unit or manifest edit by hand; NO SSM write of any parameter. No account number, person's name, credential or object content in any record (`****<last4>` form only).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply`; arm the probe listener; set `MUSE_CLIENT_ID`; **run gateway code on the host without the hard guard**.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-batch12.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-46"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/ap46.AC1.sh; echo "exit=$?"</invocation><expect>(?s)SSRF audit \(OG-sec-3, outbound code unchanged by this repair\) verdict and controllable count: CLEAN 0 \(want CLEAN 0\).*is the live ref read on the host: yes; dell1 harvest release 6575999df5 is an ancestor of base: yes.*four harvest files byte-equal between the live base and the release: 4 of 4 \(want 4 of 4\).*outside the take list 0 \(want 0\); take-list files missing 0 \(want 0\); not byte-equal to trunk's 0 \(want 0\).*process-wide state this change touches, as recorded in Phase A \(CVO verdict 35844\): named.*loggers on the host after the listener's server is built: unchanged True.*armings 0 \(want 0\).*consistent: yes; server\.py or tools\.py of the release naming family_depth: 0 \(want 0, the module stays inert\).*ask has the three halves and the process-wide state line yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-46"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/ap46.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; landed=(current|superseded).*the 27-tool read 27 of 27 under the hard guard yes.*read BEFORE the ledger closed True: ok.*listener read UNARMED only: armings 0 \(want 0\), unarmed answer 403 probe_not_armed.*: ok.*ACCESS LOG BACK: POST /mcp journal lines \d+ against \d+ audit records over the same 30-minute window.*: ok.*served verdict: OK.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me on my run before any GO to Phase B; `AC2` (Phase B) after the ledger closes.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-46.round-44-eleventh-batched-release-family-depth-and-comment.proof_of_spec.json` after Phase B and validate it with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`. The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 44, workstream ENRICH-R44-B. Source: the CTO's round-43 analysis (`ledger/ROUND_ANALYSIS.round43.md` @d35c913755, msg 35841), list item 5 and standing conditions 1 and 2, and the CVO's verdict 35844 relayed in msg 35845.
- READINGS DISCLOSED TO THE CTO: (1) "family_depth.py" is taken WITH `app/refs/silver_families.json` and `tests/test_og_cd1.py`, because `OG-cd-1`'s commits `046bc2be02` and `2b000fea49` put all three on trunk together and the module reads the data file; the `family_depth_read_iam.tf` of the same commit is excluded and unapplied, so the module is inert in the release (not imported by `server.py` or `tools.py`; its route, named in its docstring, is not mounted). (2) "the comment fix" needs its own trunk edit first, cut as `OG-en-34`. (3) The optional pair for `admin_people_access.py` includes its test, `tests/test_admin_people_access.py`; `app/admin_people.py` (`MP-pd-3` modified it) is code-equal to live per `OG-ap-45` `AC3`, so it is not in the diff.
- Pre-cut: `AC1` and `AC2` base FAIL as expected (the records are absent).

<status>staged</status>
<round>44</round>
<workstream>ENRICH-R44-B</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
