# NFRA_MCPORTAL task order -- `MP-pf-6` -- WORKSTREAM PF ROUND 3: the host-role scan's principal set and the grant writer's change-history set, both read, both denominators printed

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pf-6</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pf-6</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~36</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-time read; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the read is the issuer's own `pf6.run.sh`, one read-only SSM command on the gateway host under its instance role (the role already holds the Scan the page uses); this order adds no permission and writes no AWS resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- the planted arms of AC1 are the adversary (a principal in one set only; two empty sets).
EGRESS CLASS, declared: ONE read-only AWS call path, the issuer's `pf6.run.sh` (SSM send-command and get-command-invocation to the gateway instance). No other network call.
</preflight>

## 1. THE CELL -- `MP-pf-6` (workstream PF round 3, decomposition section PF3.3)

You work in the workspace worktree `C:/tmp/mp-pf-36`, branch `wk-NFRA_MCPORTAL-pf-36`. Your write surface is your own deliverables directory `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~36/` (all file names below are in it).
Commit with `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~36 <0.9.0_WK_NFRA_MCPORTAL~36@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push.

**Why this cell exists.** The People page lists the principals a Scan of the grant store returns (`app.admin_gateway_breakdown._scan_principals`, a host-role read), and the check that compares the page with the store iterates that same list, so a principal the Scan missed
is invisible to both sides (the CVO's row Z-C-S40). The CTO asked for a second plane: the set of principals in the grant writer's OWN change history, to compare with the Scan's set. This cell reads both sets once and compares them, and states what the comparison can and cannot show.

**What the issuer already measured** (so you do not repeat it, and so you know what the run file will probably read): the grant store holds 1 principal; the grant writer's table `mcportal-grant-changes-table` holds 1 item, a REFUSED attempt by a placeholder principal, and no grant. The two sets differ.
The comparison is therefore expected to read `equal` false; that is a finding, and this order does NOT require equality. It requires that the measurement is made and is not vacuous.

Build, in your deliverables directory:
1. **`r2_principal_sets.py`**, Python 3.9-compatible, standard library only:
   - `compare(scan_set, history_set)` takes two iterables of strings and returns a dict `{"scan_n", "history_n", "only_scan_n", "only_history_n", "equal", "vacuous"}`. `scan_n` and `history_n` are the sizes of the two sets after de-duplication; `only_scan_n` is the size of scan minus history, `only_history_n` of history minus scan;
     `vacuous` is true when BOTH sets are empty; `equal` is true only when `only_scan_n` and `only_history_n` are both 0 AND `vacuous` is false (two empty sets are NOT evidence of equality).
   - A command line `python r2_principal_sets.py --from-read <file> --out r2_run.json`: `<file>` holds the stdout of the issuer's read step (below). It has a line `ssm command=<id> status=<Success|Failed|NONE>` and, when the read worked, one line `R2 {json}` whose JSON has `scan_set` and `history_set` (lists of strings), `scan_n`,
     `history_n`, `history_items`, `history_pages` and `history_unparsed_items`. The command writes `r2_run.json` holding exactly these keys: `ssm_status`, `ssm_command`, `scan_n`, `history_n`, `history_items`, `history_pages`, `history_unparsed_items`, `only_scan_n`, `only_history_n`, `equal`, `vacuous`
     (the first two from the `ssm` line, the next five from the `R2` line, the last four from `compare` over the two sets). When there is no `R2` line it writes `ssm_status` and `ssm_command` and a key `error` with the line it did read, and exits 2. It writes NO raw set (the digests stay out of the file).
2. **`test_r2_principal_sets.py`**, pytest, four tests by these exact names:
   - `test_equal_sets_report_equal`: `compare(["a", "b"], ["b", "a"])` gives `equal` true, `only_scan_n` 0, `only_history_n` 0, `vacuous` false;
   - `test_principal_only_in_scan_fails`: `compare(["a", "b"], ["a"])` gives `equal` false and `only_scan_n` 1;
   - `test_principal_only_in_history_fails`: `compare(["a"], ["a", "b"])` gives `equal` false and `only_history_n` 1;
   - `test_two_empty_sets_are_not_evidence`: `compare([], [])` gives `equal` false and `vacuous` true.
3. **The one real read.** From your worktree root run `bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf6.run.sh > org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~36/r2_read.txt` (it takes up to a minute; it is read-only), then
   `python r2_principal_sets.py --from-read r2_read.txt --out r2_run.json` in your deliverables directory. Commit `r2_read.txt` (it holds digests and counts only, no raw id) and `r2_run.json`. If the read fails, run it once more; if it fails twice, keep the failing `r2_read.txt`, say so in your report and file a BLOCKING row.
4. In your report, state in plain words what `r2_run.json` reads (the two denominators, the pages, whether the sets are equal) and what it does NOT show.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No gateway file, no AWS write, no Terraform. The only AWS access is the issuer's `pf6.run.sh`, run exactly as written; do not edit it and do not run any other AWS command.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>` and the issuer flips it. (This face overrides the worker rule that says to flip.)
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never repair a criterion; the check scripts and the proof lines are the issuer's.
4. Never print or store a raw tenant or object id. The read prints 12-hex digests only; keep it that way.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~36/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other file, and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/` (run `pf6.run.sh` from there).

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W36-S<k>` (k from 1).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root `C:/tmp/mp-pf-36` after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pf-6"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf6.AC1.sh; echo "exit=$?"</invocation><expect>named tests PASSED 4 of 4.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pf-6"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf6.AC2.sh; echo "exit=$?"</invocation><expect>ssm=Success.*consistent=yes ok=yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-pf-6" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~36/NFRA_MCPORTAL.TO-MP-pf-6.principal-sets-scan-and-writer-history-both-read.proof_of_spec.json`
(AC3 is a judgment criterion: record it under UNVERIFIABLE-BY-INSTRUMENT with no verdict), run `proof-of-spec-check.py` on it as the worker rules say, commit, and report once, with the check output, the workspace commit hash, the plain reading of `r2_run.json` and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PF round-3 issuance (decomposition v13) from the CTO's round-2 analysis @bfe9f3549c (cell R2) and the CVO's Z-C-S40. The CTO's wording was "the principal set equals the grant writer's change history ... a planted principal present in only one set FAILs".
I MEASURED the world first (PF3.0 item 3, SSM command a9f00f73): the sets are 1 and 1 and DIFFER, because the writer's table holds a refused placeholder-principal attempt and no grant, so the premise "the writer is the only writer" does not hold today. An equality criterion would FAIL on the world, not on the work,
so AC2 grades the MEASUREMENT (both denominators at least 1, one SSM read that succeeded, no history item dropped, the verdict consistent with its own counts) and AC3 hands the verdict to the CVO. The planted-principal FAIL arm is AC1. This departure from the CTO's wording is carried to the CTO in the L10 slug.
Checks dry-run at the base: pf6.AC1 FAIL as expected (test file absent); pf6.AC2 FAIL as expected (run file absent); `pf6.run.sh`'s probe read at ~03:2xZ: scan_n 1, history_n 1, history_items 1, history_pages 1, unparsed 0.

<status>pending</status>
<status>complete</status>
<round>3</round>
<workstream>PF</workstream>
<slot>~36</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
