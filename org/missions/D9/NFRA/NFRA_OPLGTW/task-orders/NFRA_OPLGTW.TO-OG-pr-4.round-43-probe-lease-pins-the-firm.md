# NFRA_OPLGTW task order -- `OG-pr-4` -- the probe lease pins the FIRM; the listener refuses a call whose firm is not the lease's, before the tool runs (round 43; the CVO's finding on `OG-ap-40`, the CTO's ruling)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pr-4</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-pr-4</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~151</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the lease parameter's JSON gains a field, written later by the applier.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling on the CVO's finding (round-42 analysis, item 1).
EGRESS CLASS, declared: NONE (the listener binds the loopback interface only).
</preflight>

## 1. THE CELL -- `OG-pr-4` (decomposition addendum R3-T.120, round 43, workstream ENRICH-R43-A)

INHERITED STATE (in your tree, merged, passing; do NOT restructure it): `infra/aws/ec2/opal-gateway/app/probe_listener.py` is the loopback probe listener (rounds 42's `OG-pr-1` to `OG-pr-3`): a second uvicorn server in the gateway process on `127.0.0.1:8099`, off by default, armed by an SSM lease `/opal-gateway/probe/lease` (JSON `order`, `account_ref`, `expires_at`, `set_at`; 60 minutes or less), serving two tools (`etfs_compare_peers`, `client_get_transactions`) for one fixed principal. `parse_lease` returns a `Lease(order, account_ref, expires_at, set_at)` or None; `probe_call` reads the body (bounded), then consults the lease, then checks the tool, the body shape and, for `client_get_transactions`, that `body["account"]` equals the lease's `account_ref`. `tests/test_og_pr1.py` holds `test_ogpr1_ac01` to `test_ogpr1_ac10`, all passing. Read both files in full first.

THE GAP (the CVO's finding on `OG-ap-40`): the lease pins the order and the account but NOT the firm. A call to `client_get_transactions` carries a `firm` argument; the only thing that stopped a call naming another firm was the Cottonwood adapter's own account-prefix fence. The listener must not rely on a fence it does not own.

THE CHANGE (you write only `app/probe_listener.py` and `tests/test_og_pr1.py`; `server.py`, `audit.py`, `client_*.py`, `tools.py` and every other file are read-only for you):
1. `Lease` gains a `firm: str`. `parse_lease` requires `obj["firm"]` to be a string matching `^[a-z0-9][a-z0-9_-]{1,63}$` (the form of the canonical firm keys `client_core` hands out; read `client_core.py` and `client_adapter_bd49f.py` to confirm the form and widen the pattern only if a real key does not match). A lease WITHOUT `firm`, or with a malformed one, is MALFORMED: `parse_lease` returns None, so the probe answers 403 `probe_not_armed` exactly as for any other malformed lease. Update the module docstring's lease description to name the field.
2. In `probe_call`, for `client_get_transactions`, BEFORE the account check and before any tool runs: `if body.get("firm") != lease.firm:` answer 403 `probe_firm_refused` (message: "the firm is not the probe lease's firm"), audited like every refusal (`_refuse`). The check runs before `set_current_principal` and before `run_in_threadpool`, so the tool body is never entered on a mismatch. `etfs_compare_peers` takes no firm or account (market data): it is unchanged, but its lease must still carry a valid `firm` (rule 1).
3. Every existing test in `tests/test_og_pr1.py` that builds a lease JSON must now include a valid `"firm"` (for example `"cottonwood"` or the key form the file's fixtures use); their meaning and assertions do not change.

NEW TESTS in `tests/test_og_pr1.py` (keep `test_ogpr1_ac01` to `test_ogpr1_ac10` passing, unchanged in meaning):
- `test_ogpr1_ac11` THE FIRM IS PINNED: with a valid lease whose firm is F, a `client_get_transactions` call whose body `firm` is a DIFFERENT valid firm is answered 403 `probe_firm_refused`, and a stub for the tool function (monkeypatch `_CALLS["client_get_transactions"]` or `_cc.client_get_transactions` with a recorder) was NEVER called; the same call with `firm` equal to F and the lease's own account reaches the stub and is answered 200; a body with no `firm` is refused 403 `probe_firm_refused` too (None is not F).
- `test_ogpr1_ac12` A LEASE WITHOUT A FIRM IS MALFORMED: `parse_lease` returns None for a lease JSON that lacks `firm`, for `"firm": ""`, `"firm": 7` and `"firm": "Bad Firm"`; and through `probe_call` such a lease answers 403 `probe_not_armed` and calls no tool.

Mutant control to run and report (restore the file byte-equal afterwards): deleting the `body.get("firm") != lease.firm` check makes `ac11` fail.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no SSM write, no env key, no Terraform, no change to `server.py`, `audit.py`, `tools.py`, the adapters or any other app file.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret, an account number or a client value (`****<last4>` forms only).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/probe_listener.py
infra/aws/ec2/opal-gateway/tests/test_og_pr1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/probe_listener.py` and `tests/test_og_pr1.py`; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~151/`. Rows: id `NFRA_OPLGTW-Z-W151-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pr-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_pr1.py test_ogpr1_ac01 test_ogpr1_ac02 test_ogpr1_ac03 test_ogpr1_ac04 test_ogpr1_ac05 test_ogpr1_ac06 test_ogpr1_ac07 test_ogpr1_ac08 test_ogpr1_ac09 test_ogpr1_ac10 test_ogpr1_ac11 test_ogpr1_ac12; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 12 of 12; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-pr-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~151 '^infra/aws/ec2/opal-gateway/(app/probe_listener\.py|tests/test_og_pr1\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~151: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-pr-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh pr4set tests/test_og_pr1.py tests/test_og_en21.py tests/test_og_en24.py tests/test_og_cl2.py tests/test_og_en9.py; echo "exit=$?"</invocation><expect>(?s)pr4set forward: passed (\d+); failed 0.*pr4set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the twelve named tests pass (the ten inherited and the two new: the firm is pinned and the tool never runs on a mismatch; a lease without a firm is malformed). `AC2`: your commits touch only the module and its test file. `AC3`: the file and four existing gateway test files pass together in both orders with the same count. Run `AC1` and `AC3` THREE times each and report the three results.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-pr-4.round-43-probe-lease-pins-the-firm.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines and the three-run results, the mutant control). Your queue holds a second order (`OG-en-31`, the same two files) that the issuer hands you after you drain; do not start it on this one.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 43, workstream ENRICH-R43-A (decomposition addendum R3-T.120; ONE issuance covers the CTO's nine cells). Source: `ledger/ROUND_ANALYSIS.round42.md` item 1: "the lease carries the firm; the listener refuses any call whose account does not resolve to that firm, BEFORE the tool runs; a mismatched firm is refused with 403 `probe_firm_refused`, a matched one answers, a lease without `firm` is refused as malformed. No arming happens until this ships."
- The cell reads the CTO's "account resolves to that firm" as the call's `firm` argument equalling the lease's firm: the account reference (`****<last4>/<vendor>/<alias>`) carries no firm, and `client_get_transactions(firm, account, ...)` is the call that uses the firm to choose its S3 prefix. Disclosed so the CTO and CVO can correct the reading before the ask.
- Chain: `OG-pr-4` then `OG-en-31` (same two files, one worker queue, slot `~151`); both feed `OG-ap-42`.
- Pre-cut: `AC1` base FAIL as expected (`ac11` and `ac12` are absent); `AC2` and `AC3` pass at the base only with a commit present.

<status>complete</status>
<round>43</round>
<workstream>ENRICH-R43-A</workstream>
<slot>~151</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
