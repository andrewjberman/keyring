# NFRA_OPLGTW task order -- `OG-ap-42` -- APPLY: the round-43 ninth batched gateway release -- the probe-lease firm pin, the Graph host pin and the reset-discriminating test, under its own never-widen; NO ARMING

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-42</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-42</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; you still run `comp-schedule --drift` at the act and record what it scanned.
comp-iam: DECLARED-NOT-APPLICABLE -- the release changes NO IAM and writes NO SSM parameter. NOTHING ARMS THE PROBE LISTENER IN THIS ORDER: the lease parameter `/opal-gateway/probe/lease` is neither written nor deleted (it is absent; you read that it is absent, before and after).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-42 analysis (items 1, 2, 4 and 5): "No arming happens until this ships."
EGRESS CLASS, declared: NONE beyond Opal's own AWS (the release narrows what the listener and the Graph client accept).
</preflight>

## 1. THE CELL -- `OG-ap-42` (decomposition addendum R3-T.120, round 43, workstream ENRICH-R43-A)

**METHOD = `OG-ap-40`'s, read in `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-ap-40.round-42-eighth-batched-release-probe-listener.md` (and through it `OG-ap-38`'s, as amended) and followed step by step; this order states only what differs.** That includes the HARD-GUARD RULE for every fresh-process run, the live-ref re-read, the re-cut in a clean sparse tree with the overlay disclosure, the three-half ask, the ledger opened with entry AND sentinel first, no `HALT_OVERRIDE`, the 30-minute read-back, and the host clock and `systemctl --failed` read and PRINTED BEFORE THE LEDGER IS CLOSED.

⛔ **STAGED BEHIND GATES, all mechanical:** `OG-sec-3`'s `W153/SSRF_AUDIT_R43.json` reads `CLEAN` with 0 controllable (`ap42.AC1` refuses otherwise), and `OG-pr-4`, `OG-en-31` and `OG-sec-2` have drained to trunk and read COMPLETE. The GO names `trunk_sha`.

⛔ **AMENDMENT A1 (2.0.0_SA_COO~O, round 43, ~14:0xZ; the CTO's msg 35705 and MSTR's 35707): dell1's `ck-3` deploys on the host FIRST** (release `922ee425fe`, parent `6575999df5`, six paths under `infra/aws/ec2/opal-gateway/`: `harvest_figures`, `harvest_identity`, `harvest_keys`, `harvest_research`, `tests/test_cj6_slash_key_other_tools.py` modified and `tests/test_ck2_path_component_union_read.py` added; window 13:58Z to 15:00Z; I answered CLEAR). The CTO's half for this order is not signed until `ck-3`'s ledger closes. THEN this order bases on the live ref read on the host (expected `922ee425fe`) and carries ALL SIX `ck-3` paths unchanged, named in the ask with their blobs as read at `base_sha`, beside the four harvest files they include; `ap42.AC1` already enforces it (the diff against `base_sha` may hold only the four take-list files, so any `ck-3` path that differs is a refusal). `ck-3` touches neither `probe_listener.py` nor `graph.py`; if it did, the take list would be re-cut on top of it. `6575999df5` stays the required ancestor of `base_sha`. Gate limb: none graded (a modified order that declares no placeholder change).

⛔ **THE BASE IS THE LIVE REF READ ON THE HOST**, not the manifest block: dell1 deployed its harvest release `6575999df5d22c0123abfc0c88cd1c6f1efe8c96` (parent `3b94a83e05`) at 10:52:49Z on 2026-10-18 and owns the manifest block after its own deploys. Read `/opt/opal-gateway/.deployed_commit` on the host (and the running release's md5s), record it as `live_ref_host`, and make it `base_sha`. Today it is `6575999df5`; if it is anything else, STOP and file a row. `6575999df5` must be an ancestor of `base_sha`. **Every release carries dell1's four harvest files unchanged**: `app/harvest_research.py`, `app/harvest_figures.py`, `app/harvest_identity.py`, `app/harvest_keys.py` are byte-equal in `base_sha` and in your release, and the ask names their blobs as read at `base_sha`. The ask's diff lists every path that differs from live and takes only its own.

APPLY: ONE code release on the live ref. No Terraform, no IAM, no env key, no change to the unit file, `deploy-to-ec2.sh` or `EC2_MANIFEST.json` by hand, one deploy, ledger `nfra-oplgtw-gateway-release-batch10`. The take list is FOUR files taken whole from trunk at `trunk_sha`, each byte-equal to trunk's blob: `infra/aws/ec2/opal-gateway/app/probe_listener.py` (modified: the lease carries `firm`; a mismatched `firm` is refused 403 `probe_firm_refused` before the tool runs; a lease without `firm` is malformed), `infra/aws/ec2/opal-gateway/app/graph.py` (modified: `call` refuses an absolute URL whose host is not `graph.microsoft.com`, before any request), `infra/aws/ec2/opal-gateway/tests/test_og_pr1.py` (modified), `infra/aws/ec2/opal-gateway/tests/test_og_sec2.py` (new). NOT in this release (the check counts them at 0): `server.py`, `tools.py`, every `client_*.py`, `typed_scope.py`, `etfs_rivals_flow.py`, `destructive_ops.py`, `deploy-to-ec2.sh`, the unit file, `EC2_MANIFEST.json`, the catalog and `app/refs/`, Terraform. The diff of `graph.py` against the live ref must be exactly the host pin of `OG-sec-2`, and the diff of `probe_listener.py` exactly the firm pin of `OG-pr-4`; any other hunk is a STOP and a row.

### PHASE A (only on the issuer's GO): re-cut, HOST MEASUREMENTS UNDER THE GUARD, ask. NO deploy IN ANY FORM

Steps 1 and 2 as `OG-ap-40`, in `C:/tmp/og-rel-batch10`, branch `rel-nfra-oplgtw-batch10`; write `W/ap42_release.json` = `{"base_sha", "release_sha", "trunk_sha", "live_ref_host"}` (FULL 40-character shas; `base_sha` equals `live_ref_host`). In the release tree: the two taken test files and the window test files plus `test_og_en9.py`, `test_og_cl2.py` in BOTH orders; the full suite's failing set compared with the live ref's (name each difference); `bash -n deploy-to-ec2.sh` and `--preflight-only`; the host-shaped import check.
3. **THE HOST MEASUREMENTS** (candidate staged in a scratch folder on the host, removed after; every gateway-code run in a fresh process under the HARD GUARD; stop at 75 percent host used). The pins are exercised IN A FRESH GUARDED PROCESS with a fake lease source (the running service is not touched in Phase A, and NO SSM PARAMETER IS WRITTEN). Write `W/PHASE_A_OG-ap-42.json` = `{"body": {"release_sha", "firm_pin": {"mismatched_firm_status": 403, "mismatched_firm_error": "probe_firm_refused", "tool_ran_on_mismatch": false, "matched_firm_answered": true, "lease_without_firm_refused": true, "guard": "<named guard>"}, "graph_pin": {"forged_host_refused": true, "request_sent_to_forged_host": false, "graph_host_allowed": true}, "listener": {"bound_host": "127.0.0.1", "off_by_default": true, "armings": 0, "lease_parameter_written": false}, "tests": {"named_passed": n, "named_failed": 0, "window_set_passed": n, "window_set_failed": 0}}}`: `tool_ran_on_mismatch` is READ from a recorder on the tool function in your fresh process, `request_sent_to_forged_host` from a stub that counts constructions; `graph_host_allowed` is a call to a path on `graph.microsoft.com` that reaches the stub. Anything that fails: STOP, file a BLOCKING row with the numbers, write NO ask, report.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-42.md`, for THREE halves, each under a heading containing its word: the `diff` by file with the hunk attribution; the `widening` (NONE widens; stated plainly: the listener now refuses more, the Graph client accepts less; no arming; the harvest files carried unchanged with their blobs named); the `order` of acts; `both branches`; the `rollback` (redeploy the live ref's tree; there is no lease to delete); the `triggers` (health not 200 in 60 s; a tool of the 27 not answering under the guard; the `.env` key count not 65; `tools/list` changing; md5 beyond the released paths; host memory above 85 percent; `NRestarts` above 0; the listener answering any call with no lease; the marker not equal to the release sha); the gate lines. Commit, run AC1 (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ap42.AC1.sh`), REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha`)

5. As `OG-ap-38` step 5 with ledger `nfra-oplgtw-gateway-release-batch10`, deploy from `C:/tmp/og-rel-batch10`, `DEPLOY_BASE_REF=<the live ref read on the host>`.
6. **The served read, UNARMED ONLY**, writing `W/CODE10_SERVED.json` (fields as in `ap42.AC2.sh`'s header). Read that the lease parameter is ABSENT (before), a connection to the listener answers 403 `probe_not_armed` (record it), the lease parameter is still ABSENT after; `armings` is 0. The service PID is stable, `NRestarts` is 0, the 27-tool read passes 27 of 27 under the hard guard in a fresh process, and `tools/list` is equal before and after.
7. Standing clauses as `OG-ap-38` step 7; the host clock and failed units read BEFORE the ledger closes; close the ledger; commit; run `ap42.AC2`; report once per phase; send me the ledger CLOSED time and the live sha (I tell the CTO and `0.0.0_AB_MSTR~Z` for dell1).

## 2. BOUNDS

- The release's files only. No IAM or Terraform change, no env key, no deploy-script, unit or manifest edit by hand; NO SSM write of any parameter. No account number, person's name, credential or object content in any record (`****<last4>` form only).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply`; arm the probe listener; set `MUSE_CLIENT_ID`; **run gateway code on the host without the hard guard**.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-batch10.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-42"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ap42.AC1.sh; echo "exit=$?"</invocation><expect>(?s)SSRF audit \(OG-sec-3\) verdict and controllable count: CLEAN 0 \(want CLEAN 0\).*is the live ref read on the host: yes; dell1 harvest release 6575999df5 is an ancestor of base: yes.*four harvest files byte-equal between the live base and the release: 4 of 4 \(want 4 of 4\).*outside the take list 0 \(want 0\); take-list files missing 0 \(want 0\); not byte-equal to trunk's 0 \(want 0\).*firm pin on the host: mismatched firm 403 probe_firm_refused, the tool ran on the mismatch False.*graph host pin: forged host refused True.*armings 0 \(want 0\).*ask has the three halves yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-42"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/ap42.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; landed=(current|superseded).*the 27-tool read 27 of 27 under the hard guard yes.*read BEFORE the ledger closed True: ok.*listener read UNARMED only: armings 0 \(want 0\), unarmed answer 403 probe_not_armed.*: ok.*served verdict: OK.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me on my run before any GO to Phase B; `AC2` (Phase B) after the ledger closes.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-42.round-43-ninth-batched-release-firm-pin-and-graph-pin.proof_of_spec.json` after Phase B and validate it with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`. The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 43, workstream ENRICH-R43-A. Source: the round-42 analysis items 1, 2, 4 and 5 and its standing condition ("the base is the live ref at the GO, 6575999df5 today; each release carries dell1's four harvest files unchanged with the blobs read at 6575999df5 and named in the ask; the ask's diff lists every path that differs from live and takes only its own"). `ap42.AC1` reads the live ref from the host record rather than the manifest block because the manifest on trunk still names `3b94a83e05` until `OG-ap-43` lands dell1's release.
- `server.py` is not in the take list: neither pin touches it (the firm pin is inside `probe_listener.py`; the Graph pin inside `graph.py`).
- The arming is NOT part of this order. `OG-ev-7` arms once, with the firm pinned, on a later GO.
- Chain: joins `OG-pr-4` then `OG-en-31` (slot `~151`), `OG-sec-2` (slot `~152`) and `OG-sec-3` (slot `~153`); `OG-ev-7` follows its close.
- Pre-cut: `AC1` and `AC2` base FAIL as expected (the records are absent).

<status>staged</status>
<round>43</round>
<workstream>ENRICH-R43-A</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
