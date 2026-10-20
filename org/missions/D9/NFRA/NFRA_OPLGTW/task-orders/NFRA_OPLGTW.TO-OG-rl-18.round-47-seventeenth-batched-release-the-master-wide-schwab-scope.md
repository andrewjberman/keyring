# NFRA_OPLGTW task order -- `OG-rl-18` -- APPLY: the round-47 gateway release `batch17` -- the MASTER-WIDE Schwab scope code (`OG-rt-1`: `app/data_entitlement.py`, `app/account_ref.py`, `app/integrations/schwab/integration.py`, `tests/test_og_rt1.py`) PLUS the master-admin exemption on the legacy `/callback` consent branch (`OG-ed-1`: `app/server.py`, `app/token_broker.py`, three tests); the Schwab scope code is INERT until a grant names `["*"]`, the exemption is live at once; under its own never-widen; then the landing

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-18</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rl-18</to_id>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is added or changed; you still run `comp-schedule --drift` at the act and record what it scanned.
comp-iam: DECLARED-NOT-APPLICABLE -- the release changes NO IAM and writes NO SSM parameter. NOTHING ARMS THE PROBE LISTENER IN THIS ORDER.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429) rank 6: "the master-wide Schwab scope resolved at read time, with no stored list (Andrew-direct ~17:2xZ 10-19); then Andrew's own grant moves to it"; the CTO's release discipline gives the entitlement parser its own release.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-rl-18` (decomposition addendum R3-T.124, amendment A4, round 47, workstream ENRICH-R47-E)

**METHOD = `OG-rl-17`'s** (`org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-rl-17.round-47-sixteenth-batched-release-the-client-fences-the-size-caps-and-the-in-flight-guard.md`), through it `OG-ap-50`'s, read at HEAD and followed step by step: the hard guard, the live-ref re-read, the clean sparse re-cut, the three-half ask, the ledger with entry AND sentinel first, no `HALT_OVERRIDE`, the 30-minute read-back, the host clock and failed units printed before the ledger closes. This order states only what differs.

⛔ **THE BASE IS THE LIVE REF READ ON THE HOST** (`/opt/opal-gateway/.deployed_commit`); record it as `live_ref_host` and make it `base_sha`; `6575999df5` must be an ancestor; dell1's four harvest files byte-equal.

⛔ **THE RELEASE-ORDER CONDITION (the ask states it in a sentence containing the words "before any grant names"):** this code must be live BEFORE any grant names the sentinel `["*"]`: an OLD gateway reads a stored sentinel as `Malformed` and would deny that principal's whole Schwab access. So the grant orders (`OG-gv-1`, `OG-gm-1`) start only after this ledger is CLOSED.

⛔ **WINDOW:** off-hours; **not before one full day after `OG-rl-17`'s ledger is CLOSED, and not before 2026-10-22 06:00Z**; 06:00Z to 06:45Z, abort line `/health` 200 by 06:30Z; announce to `0.0.0_AB_MSTR~Z`. Phase A runs at once; Phase B only on the issuer's GO naming all three halves signed and the window.

⛔ **STANDING CONDITIONS:** the base is the live ref at the GO; the ask carries `process-wide state this change touches: ...`; here: `app/data_entitlement.py` (the parser and `check_scope`, read per request by every Schwab tool and by the dispatch chokepoint's `tool_denial`), `app/account_ref.py` (the resolver) and the Schwab integration's filter helper change; no import-time side effect is added (read the three diffs and say so); `tools/list` does NOT change; the stored grants are untouched; every Phase B prints the journal `POST /mcp` count AND the audit-lake count for ONE window.

APPLY: ONE code release, ledger `nfra-oplgtw-gateway-release-batch17`. **The take list** (whole from trunk at `trunk_sha`, each byte-equal), under `infra/aws/ec2/opal-gateway/`: `app/data_entitlement.py`, `app/account_ref.py`, `app/integrations/schwab/integration.py`, `tests/test_og_rt1.py` (the four of `OG-rt-1`); and `app/server.py`, `app/token_broker.py`, `tests/test_og_ed1.py`, `tests/test_scoped_consent_r253.py`, `tests/test_login_admit_r24.py` (the five of `OG-ed-1`, amendment A10, drained `17c53cdd2cb`): NINE files. NOT in it (the check counts them at 0): every other file, including the batch16 files whether or not batch16 is live, `deploy-to-ec2.sh`, the unit, `deploy/`, `EC2_MANIFEST.json` by hand, every `.tf`.

### PHASE A (only on the issuer's GO, given when `OG-rl-17` is CLOSED): re-cut, HOST MEASUREMENTS UNDER THE GUARD, ask. NO deploy IN ANY FORM

Steps 1 and 2 as `OG-rl-17`, in `C:/tmp/og-rel-batch17`, branch `rel-nfra-oplgtw-batch17`; write `W/rl18_release.json` = `{"base_sha", "release_sha", "trunk_sha", "live_ref_host"}`. In the release tree: the new test file, the existing entitlement, account-reference, Schwab, grant-admin and contract tests in BOTH orders (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh`), the full suite's failing set against the LIVE ref's per test id (name each difference), `bash -n deploy-to-ec2.sh` and `--preflight-only`, the host-shaped import check.
3. **THE HOST MEASUREMENTS** (candidate in a scratch copy on the host, removed after; every gateway-code run in a fresh process under the HARD GUARD; stop at 75 percent host used; the running service is NOT touched):
   - **(a) The probes.** Run the python probes of `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/rt1.AC1.sh` and `rt1.AC2.sh` against the candidate tree (the same code with the gateway folder pointed at the scratch copy) and count the labelled lines that read `ok`: `probes` = `{"rt1_ac1_ok": 11, "rt1_ac2_ok": 11, "ed1_ac1_ok": 7}` (the 7 labelled lines of `ed1.AC1` run the same way against the candidate tree).
   - **(b) Explicit scopes unchanged.** In ONE fresh process, parse the SAME explicit-list scope (two masters, eight-digit fixture ids built at run time) with the live ref's `data_entitlement` and the candidate's, and compare `check_scope` answers for an in-list id, an out-of-list id and an empty list, and the `account_filter` / candidate list the resolver builds: all equal. `explicit_unchanged` true.
   - **(c) No stored sentinel.** A read-only scan of the POLICY grant records (strong reads, counts only): the number whose `scope.accounts` holds the string `*` is `sentinel_grants_in_store` (expected 0). A non-zero value is a STOP.
   Write `W/PHASE_A_OG-rl-18.json` = `{"body": {"release_sha", "tests": {"named_passed", "named_failed": 0, "window_set_passed", "window_set_failed": 0, "suite_difference_named": true}, "probes": {...}, "explicit_unchanged": true, "sentinel_grants_in_store": 0, "process_wide_state": "..."}}`. Anything failing: STOP, a BLOCKING row, no ask.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-rl-18.md`, for THREE halves under headings containing CTO, COO, CVO: the `diff` by file; the `widening`, stated plainly: TWO. (1) The Schwab scope code adds a grant shape that no stored grant uses; it widens nothing until a later grant order writes `["*"]`, and that order is its own never-widen. (2) The legacy `/callback` consent branch now lets a MASTER ADMIN (exactly one `MASTER_ADMIN_EMAILS` entry) complete the sign-in although an `email_deny` record names that email (before: 403); no other email's verdict changes, an unreadable store still fails closed 503 for everyone else, and the browser routes already exempted the tier (`OG-en-14`); the CTO's half of `OG-gv-1` named it (option 2, msg 36207); the ask must say `a non-admin with a deny record still gets 403` and `the exemption is live at once, not inert`; what the code will do for such a grant (read the master's own data without a stored account list; resolve account references against the master's CURRENT accounts from the newest complete `dim_position` snapshot; a master-wide grant without `dim_position` is refused fail-closed); the RELEASE-ORDER condition sentence; the `order`; `both branches` (an explicit scope behaves as before; a sentinel scope parses and filters on nothing); the `rollback` (redeploy the live ref's tree; with NO stored sentinel the rollback is clean, which is why the grant orders wait); the `triggers` (health not 200 in 60 s; a tool of the 27 not answering; `.env` key count not 65; `tools/list` changing from 103; md5 beyond the nine files; host memory above 85 percent; `NRestarts` above 0; the marker not equal to the release; a Schwab tool answering differently for the explicit-list grants read in Phase B; any `audit-lake WARN`); the line `process-wide state this change touches: ...`. Commit, run AC1 (`.../r47/checks/rl18.AC1.sh`), REPORT, STOP.

### PHASE B (only on the issuer's GO, which names all three halves signed at `release_sha` and the window)

5. As `OG-rl-17` step 5 with ledger `nfra-oplgtw-gateway-release-batch17`, deploy from `C:/tmp/og-rel-batch17`, `DEPLOY_BASE_REF=<the live ref read on the host>`.
6. **The served read, UNARMED ONLY**, writing `W/CODE17_SERVED.json` (the field names in `rl18.AC2.sh`'s header, the same as `OG-rl-17`'s with `masterwide` in place of `inflight`): health 200, the marker equal to the release, `unit_memory_high` `5600M` / `unit_memory_max` `6400M`, `tools_list` 103 before and after, `env_key_count` 65, the 27-tool read 27 of 27, `host_md5` `differ` 0, the host clock and failed units read BEFORE the ledger closes, the 30-minute read-back, the listener UNARMED, the access-log counts, the audit-failure counter 0, and `masterwide` = `{"sentinel_parse_in_deployed_tree": true, "explicit_scope_unchanged": true, "sentinel_grants_in_store": 0}`: the first and second read from the DEPLOYED tree under the hard guard (parse a sentinel scope; run the explicit-scope comparison of step 3(b) against the deployed code), the third re-scans the store.
7. Standing clauses as `OG-rl-17` step 8; close the ledger; commit; run `rl18.AC2`; report once per phase; send me the ledger CLOSED time and the live sha.
8. **PHASE C, the landing** as `OG-rl-17` step 9: `W/rl18_landing.json`; the issuer drains it.

## 2. BOUNDS

- The release's nine files only (the four of `OG-rt-1` and the five of `OG-ed-1`). No IAM or Terraform change, no env key, no deploy-script or unit edit, NO SSM write, NO write of any stored grant (the sentinel is written by `OG-gv-1` and `OG-gm-1`, not here). No account number, person's name, credential or object content in any record.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform apply`; arm the probe listener; run gateway code on the host without the hard guard.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-batch17.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~NFRA1/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-18"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/rl18.AC1.sh; echo "exit=$?"</invocation><expect>(?s)is the live ref read on the host: yes; dell1 harvest release 6575999df5 is an ancestor of base: yes.*four harvest files byte-equal between the live base and the release: 4 of 4 \(want 4 of 4\).*files differing 9 \(want 9\); outside the take list 0 \(want 0\); take-list files missing 0 \(want 0\); not byte-equal to trunk's 0 \(want 0\); deploy script, deploy folder, manifest or Terraform files in the diff 0 \(want 0\).*host runs on release_sha equal; tests: .*suite difference named True: ok.*probes on the candidate tree: rt1\.AC1 lines ok 11 of 11, rt1\.AC2 lines ok 11 of 11, ed1\.AC1 lines ok 7 of 7: ok; explicit-list scope unchanged True; stored grants naming the sentinel 0 \(want 0\): ok.*process-wide state this change touches, as recorded in Phase A \(CVO verdict 35844\): named.*ask has the three halves, the process-wide state line, the release-order condition and the exemption widening yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-18"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/rl18.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledger CLOSED 1 of 1; sentinel at HEAD 0; landed=(current|superseded).*tools/list 103 before 103 \(want 103 and 103\); marker equals the release sha yes; health 200; registry 103 \(want 103\); env keys 65 \(want 65\); the 27-tool read 27 of 27 under the hard guard yes; host md5 differ 0, missing 0 \(want 0, 0\).*unit limits live ok; host clock Normal synchronised True, failed units 0, read BEFORE the ledger closed True: ok; read-back [3-9]\d* minutes, triggers 0, service restarts 0: ok.*listener read UNARMED only: armings 0 \(want 0\), unarmed answer 403 probe_not_armed.*: ok.*ACCESS LOG BACK: POST /mcp journal lines \d+ against \d+ audit records over the same 30-minute window.*: ok.*AUDIT FAILURE COUNTER.*journal failure lines 0 over the read-back, counter value 0: ok.*MASTER-WIDE CODE LIVE: the sentinel parses in the deployed tree True, an explicit-list scope is unchanged True, stored grants carrying the sentinel 0 \(want 0\): ok.*served verdict: OK.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (Phase A) is graded by me on my run before any GO to Phase B; `AC2` (Phase B) after the ledger closes.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rl-18.round-47-seventeenth-batched-release-the-master-wide-schwab-scope.proof_of_spec.json` after Phase B and validate it with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). The `<status>` flip is mine.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-E, amendment A4 of R3-T.124. Source: the CTO's round-46 analysis (msg 36165) rank 6 and "release discipline". `OG-rt-1` drained `fd69a7cb77` (AC1 to AC3 PASS on the issuer's runs). Staged: the Phase A GO is given when `OG-rl-17` is CLOSED.
- READINGS DISCLOSED TO THE CTO: (1) a release of its own, because the parser guards every Schwab tool; the cost is one more window, a day after batch16. (2) The ask must say the code widens NOTHING by itself; the widening is the later grant orders'. (3) The refs of a master-wide master resolve against the newest complete `dim_position` snapshot, so a reference to an account with no position row there does not resolve (worker row Z-W170-S1, ruled in Z-S430).
- Pre-cut: `AC1` and `AC2` base FAIL as expected (records absent). Arms: `rl18.AC2` is `rl17.AC2` with the slug, record and `masterwide` block changed; `rl18.AC1` follows `rl17.AC1`'s diff logic with a nine-file take list.
- AMENDED 2026-10-20 ~14:5xZ (2.0.0_SA_COO~O, decomposition A10): the take list gains the five files of `OG-ed-1` (the master-admin exemption on the legacy `/callback` branch, the CTO half of `OG-gv-1`, option 2), so the release is NINE files and no longer inert; the ask states the second widening; Phase A runs `ed1.AC1`'s seven lines against the candidate tree; `rl18.AC1` takes the nine files. Gate limb: none graded (an existing tree order that declares no placeholders).

<status>staged</status>
<status>pending</status>
<round>47</round>
<workstream>ENRICH-R47-E</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
