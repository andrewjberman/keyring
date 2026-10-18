# NFRA_OPLGTW task order -- `OG-en-31` -- a test that DISCRIMINATES the body-first read of the probe listener (round 43; worker row `Z-W148-S3`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-31</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-31</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~151</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a test file only; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (round-42 analysis, item 4).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-31` (decomposition addendum R3-T.120, round 43, workstream ENRICH-R43-A)

INHERITED STATE (in your tree, merged, passing; the queue's first order `OG-pr-4` has drained): `app/probe_listener.py` reads the request body FIRST, bounded (`_read_body_bounded`), and only then consults the lease and the other refusals, so that every answer to a body within the bound leaves no unread request bytes (a server that replies and closes with an unread body can reset the client's connection before the client reads the refusal). `tests/test_og_pr1.py` holds `test_ogpr1_ac01` to `test_ogpr1_ac12`.

THE GAP (worker row `Z-W148-S3`): `test_ogpr1_ac07` was meant to prove that body-first behaviour with a real loopback server, but a mutant that answers BEFORE reading the body did not fail it in 3 of 3 runs on the worker's machine: on loopback the reset does not reproduce reliably, so the test proves clean answers, not the property. The property is deterministic one level up: at the ASGI boundary, every refusal within the bound must have PULLED THE WHOLE REQUEST BODY before it sends `http.response.start`.

THE CHANGE (you write only `tests/test_og_pr1.py`; `app/probe_listener.py` and every other file are read-only for you; no product line changes):
- Add `test_ogpr1_ac13` THE BODY IS READ BEFORE ANY REFUSAL IS SENT. Drive `pl.probe_app` through a hand-written ASGI call (an async function that builds the `scope`, a `receive()` that yields a request body split into exactly 3 chunks (`more_body` true, true, false) and COUNTS how many times it was awaited, and a `send()` that records, at the moment it receives `http.response.start`, the count of chunks pulled so far and the status). Use the `world` fixture and `arm`/`_set_phase` the file already has. The body is a JSON object padded to about 24 KB (three chunks of 8 KB, still under the 65536 bound), so every refusal below is reached after a successful body read. Six cases, each asserting that at `http.response.start` the chunks pulled equal 3 AND the status and error code are the expected ones:
  1. the probe unarmed: 403 `probe_not_armed`;
  2. armed, tool `whoami`: 404 `probe_tool_refused`;
  3. armed, `etfs_compare_peers`, a body that is valid JSON but not an object (a list padded to size): 400 `probe_bad_request`;
  4. armed, `client_get_transactions` with another account: 403 `probe_account_refused`;
  5. armed, `client_get_transactions` with another firm (the lease's account): 403 `probe_firm_refused`;
  6. a lease WITHOUT a firm (malformed): 403 `probe_not_armed`.
- Do NOT delete or weaken `test_ogpr1_ac07`: it still proves clean answers over a real socket; its docstring gains one sentence saying that `test_ogpr1_ac13` is the test that discriminates the order of the read.

A mutant check is part of the order (criterion AC3): `deliverables/2.0.0_SA_COO~O/r43/checks/en31.AC3.sh` copies `app/probe_listener.py` aside, inserts an early `probe_not_armed` refusal BEFORE the body read, runs `test_ogpr1_ac13` (it must FAIL), restores the file byte-equal and runs it again (it must PASS). You run it; you do not edit it.

## 2. BOUNDS

- Write only `tests/test_og_pr1.py` (and your proof instance). No product file, no release, no deploy, no IAM, no env key, no Terraform.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret, an account number or a client value (`****<last4>` forms only).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/test_og_pr1.py
infra/aws/ec2/opal-gateway/app/probe_listener.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `tests/test_og_pr1.py`. `app/probe_listener.py` is listed because the mutant check modifies it for seconds and restores it byte-equal; you never edit it by hand. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~151/`. Rows: id `NFRA_OPLGTW-Z-W151-S<k>` (the next free for your slot), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-31"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_pr1.py test_ogpr1_ac01 test_ogpr1_ac02 test_ogpr1_ac03 test_ogpr1_ac04 test_ogpr1_ac05 test_ogpr1_ac06 test_ogpr1_ac07 test_ogpr1_ac08 test_ogpr1_ac09 test_ogpr1_ac10 test_ogpr1_ac11 test_ogpr1_ac12 test_ogpr1_ac13; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 13 of 13; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-31"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~151 '^infra/aws/ec2/opal-gateway/(app/probe_listener\.py|tests/test_og_pr1\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~151: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-31"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/en31.AC3.sh; echo "exit=$?"</invocation><expect>(?s)mutant \(a refusal before the body read\): test_ogpr1_ac13 FAILED \(want failed\).*unmutated: test_ogpr1_ac13 PASSED \(want passed\).*probe_listener\.py restored byte-equal: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the thirteen named tests pass (the twelve inherited and the new discriminating one). `AC2`: your slot's commits (this order's and `OG-pr-4`'s, which the same slot authored) touch only the module and its test file; in THIS order you commit only the test file (the mutant check restores the product file byte-equal, so it never appears in a commit of this order). `AC3`: the discrimination itself: the same test fails against the mutant and passes against the real file. Run `AC1` THREE times and report the three results.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-31.round-43-test-discriminates-the-body-first-read.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines and the three-run results).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 43, workstream ENRICH-R43-A. Source: round-42 analysis item 4 ("make `test_ogpr1_ac07` discriminate the connection reset; a test-only cell that folds into the release"). The cell does not try to reproduce the TCP reset (it does not reproduce reliably on loopback: row `Z-W148-S3`, 3 of 3 mutant runs passed); it asserts the deterministic property the reset depends on, one level up. Disclosed so the CTO can correct the reading.
- Chain: second order of slot `~151` (after `OG-pr-4`, same file); feeds `OG-ap-42`. Cases 5 and 6 need `OG-pr-4`'s firm pin: spawn this order only after `OG-pr-4` has drained.
- Pre-cut: `AC1` base FAIL as expected (`ac13` is absent); `AC3` base FAIL (no `ac13` to fail under the mutant is a different failure: the check reports it).

<status>staged</status>
<round>43</round>
<workstream>ENRICH-R43-A</workstream>
<slot>~151</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
