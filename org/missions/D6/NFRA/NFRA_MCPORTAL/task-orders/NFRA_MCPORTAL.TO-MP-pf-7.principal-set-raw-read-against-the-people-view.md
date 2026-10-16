# NFRA_MCPORTAL task order -- `MP-pf-7` -- WORKSTREAM PF ROUND 4: the People view's principal set against a raw read of the grant store under a different credential

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pf-7</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pf-7</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~37</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time read; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the read is the issuer's own `pf7.run.sh`: an `iam simulate-principal-policy` call, one read-only `dynamodb scan` of gateway-access-state-table under this box's IAM user, and one read-only SSM command on the gateway host; this order adds no permission and writes no AWS resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- the planted arms of AC1 are the adversary (a principal in one set only, both ways; two empty sets; a denied Scan).
EGRESS CLASS, declared: read-only AWS calls through the issuer's `pf7.run.sh` only (IAM simulate, DynamoDB Scan, SSM send-command and get-command-invocation to the gateway instance). No other network call.
</preflight>

## 1. THE CELL -- `MP-pf-7` (workstream PF round 4, decomposition section PF4.1)

You work in the workspace worktree `C:/tmp/mp-pf-37`, branch `wk-NFRA_MCPORTAL-37`. Your write surface is your own deliverables directory `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~37/` (all file names below are in it).
Commit with `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~37 <0.9.0_WK_NFRA_MCPORTAL~37@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push.
Every shell call of yours resets to the primary checkout: begin each call with `cd C:/tmp/mp-pf-37 &&`.

**Why this cell exists.** The /gateway People view lists the principals a Scan of the grant store returns under the gateway's host role (`_scan_principals`, `principal_profile` rows), and the check that compares the page with the store iterates that same list, so a principal the Scan missed is invisible to both sides (the CVO's row Z-C-S40). The independent test is a raw full read of the table under a DIFFERENT credential with none of the page's code.
This cell reads both sets once, compares them and records both denominators.

**What the issuer already measured** (so you know what the run file will probably read, not so you copy it): the raw read sees 1,669 items in 3 pages and 1 grant-bearing principal; the People view's set is 1 principal; the two digests are equal. The order grades what YOUR run reads, not that.

Build, in your deliverables directory:
1. **`r3_principal_sets.py`**, Python 3.9-compatible, standard library only:
   - `compare(page_set, raw_set)` takes two iterables of strings and returns `{"page_n", "raw_n", "only_page_n", "only_raw_n", "equal", "vacuous"}`: the two set sizes after de-duplication; the size of page minus raw; the size of raw minus page; `vacuous` true when BOTH sets are empty; `equal` true only when both differences are 0 AND `vacuous` is false.
   - A command line `python r3_principal_sets.py --from-read <file> --out r3_run.json`. `<file>` holds the stdout of the issuer's read step (below), whose lines are:
     `SIM identity=<name> table_arn_ok=<yes|no> Scan=<decision> DescribeTable=<decision> OperatorRoleScan=<decision>`;
     `RAW {json}` with `complete` (bool), `pages`, `per_page` (list of [Count, ScannedCount]), `count`, `scanned`, `policy_items`, `raw_set` (list of strings), `raw_n`, `audit_only_principals`;
     `ssm command=<id> status=<Success|Failed|NONE>`;
     `R3PAGE {json}` with `page_set` (list of strings) and `page_n`; and last `RESULT: READ` (or `RESULT: STOP`).
     It writes `r3_run.json` holding exactly these keys: `sim_scan` (the `Scan=` value), `sim_operator_role_scan` (the `OperatorRoleScan=` value), `raw_complete`, `raw_pages`, `raw_count`, `raw_scanned`, `raw_n`, `policy_items`, `audit_only_principals` (all from RAW), `page_n` (from R3PAGE), `only_page_n`, `only_raw_n`, `equal`, `vacuous` (from `compare` over `page_set` and `raw_set`),
     `ssm_status`, `ssm_command` (from the `ssm` line). It writes NO raw set (the digests stay out of the file). When the file ends `RESULT: STOP`, it prints the SIM line, exits 3 and writes NO run file. When the file lacks a RAW or R3PAGE line it writes no run file and exits 2.
2. **`test_r3_principal_sets.py`**, pytest, five tests by these exact names:
   - `test_equal_sets_report_equal`: `compare(["a", "b"], ["b", "a"])` gives `equal` true, `only_page_n` 0, `only_raw_n` 0, `vacuous` false;
   - `test_principal_only_in_raw_means_the_page_misses_it`: `compare(["a"], ["a", "b"])` gives `equal` false and `only_raw_n` 1 (a planted holder the page does not list);
   - `test_principal_only_in_page_is_reported`: `compare(["a", "b"], ["a"])` gives `equal` false and `only_page_n` 1;
   - `test_two_empty_sets_are_not_evidence`: `compare([], [])` gives `equal` false and `vacuous` true;
   - `test_scan_denied_stops_without_a_run`: write a small read file in a temp directory whose SIM line reads `Scan=implicitDeny` and whose last line is `RESULT: STOP`, run the command line on it with `subprocess` and `sys.executable`, and assert exit code 3 and that no run file was written.
3. **The one real read.** From your worktree root run `bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf7.run.sh > org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~37/r3_read.txt` (it takes up to two minutes; it is read-only), then `python r3_principal_sets.py --from-read r3_read.txt --out r3_run.json` in your deliverables directory.
   Commit `r3_read.txt` (digests and counts only, no raw id) and `r3_run.json`. If the read fails, run it once more; if it fails twice, keep the failing `r3_read.txt`, say so in your report and file a BLOCKING row.
   If `r3_read.txt` ends `RESULT: STOP` (the Scan simulate did not read allowed), STOP: file a BLOCKING row naming the SIM line; a never-widen ask for read-only Scan on that one table follows from the issuer, and no other route is tried.
4. In your report, state in plain words what `r3_run.json` reads (the two denominators, the pages, the controls, whether the sets are equal) and what it does NOT show.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No gateway file, no AWS write, no Terraform. The only AWS access is the issuer's `pf7.run.sh`, run exactly as written; do not edit it and do not run any other AWS command.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it. (This face overrides the worker rule that says to flip.)
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check scripts and the proof lines are the issuer's.
4. Never print or store a raw tenant or object id. The read prints 12-hex digests only; keep it that way.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~37/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other file, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/` (run `pf7.run.sh` from there).

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W37-S<k>` (k from 1).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pf-7"><invocation>cd C:/tmp/mp-pf-37 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf7.AC1.sh; echo "exit=$?"</invocation><expect>named tests PASSED 5 of 5.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pf-7"><invocation>cd C:/tmp/mp-pf-37 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf7.AC2.sh; echo "exit=$?"</invocation><expect>sim_scan=allowed control=(implicitDeny|explicitDeny) raw_complete=True.*equal=True.*ok=yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~37/NFRA_MCPORTAL.TO-MP-pf-7.principal-set-raw-read-against-the-people-view.proof_of_spec.json`, run `proof-of-spec-check.py` on it as the worker rules say, commit, and report once, with the check output, the workspace commit hash, the plain reading of `r3_run.json` and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PF round-4 issuance (decomposition v14) from the CTO's PF round-3 analysis @0a775f4f7b (msg 34710, cell R3) and the CVO's Z-C-S40. Departures from the analysis (PF4.2): a worker, not the CloudOps~Z seat; no live plant (the writer deletes nothing and appends audit rows); the both-ways arm is offline in the comparator. Reported to the CTO in the L10 slug.
Checks dry-run at the base: pf7.AC1 FAIL as expected (test file absent); pf7.AC2 FAIL as expected (run file absent); `pf7.run.sh` read from `/c/Users` (a wrong cwd, so the root anchor is proven) at ~04:0xZ: Scan allowed, DescribeTable allowed, operator-role Scan implicitDeny, 3 pages 1669 items, raw 1, page 1, digests equal.
The status flip is the issuer's.

<status>pending</status>
<status>complete</status>
<round>4</round>
<workstream>PF</workstream>
<slot>~37</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
