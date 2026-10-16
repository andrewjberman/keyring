# NFRA_OPLGTW task order -- `OG-en-10` -- the per-identity rate limit writes an audit row when it answers 429, so the limiter's own count can be read (round 38 E10; CTO finding msg 34991)

<!-- ===================== THE WORKER FACE IS EVERYTHING UP TO THE RECORD FACE MARKER ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-10</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-10</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~124</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule. The release is a later applier order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the audit sink is the one the gateway already writes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act answers the CTO's finding (msg 34991: the gateway answered `429 {"error":"rate_limited","scope":"identity"}` to the CTO seat at ~12:2xZ and to the CVO seat at ~10:0xZ; the audit lake read 11:00Z onward holds 873 records, 588 ok calls by the one shared Opal Bloomberg identity, and NO 429 row, so "the limiter's own count is unread"). It adds the missing evidence; it does not change a limit.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-10` (decomposition addendum R3-T.94, round 38 item E10, workstream ENRICH-R38-B, FWD-22)

THE FACTS (issuer's read of the code, to check, not to trust). `app/server.py` `GuardMiddleware.__call__` calls `ratelimit.enforce_identity(principal.key)` for every `/mcp` POST of a valid bearer; on refusal it answers `429 {"error": "rate_limited", "scope": "identity"}` with `Retry-After`, and writes NOTHING to the audit. The limit is `RL_MCP_IDENTITY_LIMIT` (default 120) requests per `RL_MCP_IDENTITY_WINDOW` (default 60 s) per identity, a sliding-window log kept in memory in `app/ratelimit.py` (`check(bucket, key, limit, window)` returns `(ok, retry)`; `enforce_identity(email)` at about line 137 is fail-open). The site Z seats share one Opal identity, and every `/mcp` POST counts (not only tool calls: initialize, tools/list and notifications too), so the audit's tool-call count under-reads what the limiter sees.

THE FIX (code only). When `enforce_identity` refuses, write ONE audit row through the audit writer the gateway already uses for a denial (read how `app/server.py` or `app/audit.py` records an entitlement denial or a kill-switch refusal and copy that shape; do not invent a sink): outcome `rate_limited`, the identity as the audit already identifies a principal (its hashed or keyed form, never a new plaintext field), the `limit`, the `window_s`, the `count_in_window` the limiter measured at refusal, the `retry_after_s`, and the request's JSON-RPC method if the middleware can read it without consuming the body (otherwise omit it). To get the count, extend `app/ratelimit.py` minimally: `enforce_identity` keeps its `(ok, retry)` return for existing callers and gains a second function (for example `identity_count(key)`) or an optional out-parameter that returns the in-window count; no behaviour of the limit changes. The audit write must never change the 429: a failing audit write is swallowed (the limiter and the 429 stay fail-open/closed exactly as today) and is itself counted in a module-level counter. Rate-limit the audit row itself (at most one row per identity per 10 s, with a `suppressed` count of the refusals folded into it) so a hot loop of 429s cannot flood the audit lake.
Change no limit value and no admission; do not add an endpoint.

TESTS (new file `tests/test_og_en10.py`; read `tests/test_ratelimit*.py` and the nearest server-middleware test for the fixture style):
- `test_ogen10_ac01`: an identity driven past `RL_MCP_IDENTITY_LIMIT` gets the 429 answer exactly as before (status, body, `Retry-After`) AND one audit row with outcome `rate_limited`, the limit, the window, a `count_in_window` at or above the limit, and no plaintext e-mail.
- `test_ogen10_ac02`: a burst of refusals inside 10 s writes ONE row carrying a `suppressed` count (not one row per refusal); a refusal after the 10 s writes a new row.
- `test_ogen10_ac03`: a failing audit writer leaves the answer a 429 with the same body and raises nothing; below the limit no row is written and the response is untouched.
If an existing test pins that a refusal writes no audit row, update it to the new truth with the smallest edit and name it; never weaken it.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no change of any limit value or default.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print an account number, a token or a person's name.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/ratelimit.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/audit.py
infra/aws/ec2/opal-gateway/tests/test_og_en10.py
infra/aws/ec2/opal-gateway/tests/test_ratelimit.py
infra/aws/ec2/opal-gateway/tests/test_rate_limit.py
infra/aws/ec2/opal-gateway/tests/test_server_guard.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE the three app files only as far as the change needs and `tests/test_og_en10.py` and, only to follow the new truth, the existing rate-limit and guard tests listed; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~124/`. Rows: id `NFRA_OPLGTW-Z-W124-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_en10.py test_ogen10_ac01 test_ogen10_ac02 test_ogen10_ac03; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~124 '^infra/aws/ec2/opal-gateway/(app/(ratelimit|server|audit)\.py|tests/(test_og_en10|test_ratelimit|test_rate_limit|test_server_guard)\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~124: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the three named tests pass: a 429 leaves an audit row with the limiter's count, bursts are folded, an audit failure never changes the answer. `AC2`: the commits of this serial touch only the limiter, the server guard, the audit module and their tests.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-10.rate-limit-429-is-audited.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, the audit sink and row shape you used, each existing test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 38 (CTO finding msg 34991), workstream ENRICH-R38-B (decomposition addendum R3-T.94). Risk WORLD by the L6 floor, no deploy in this cell; rides the batched gateway release. The row for the finding is filed by the issuer with the limiter's config read (identity limit 120 per 60 s, in-memory sliding log, every /mcp POST counted) and this cell as its instrument; whether to raise the limit or give the seats distinct identities is decided AFTER the first 429 audit rows exist (a number chosen without the count would be a guess).
- Pre-cut: AC1 base FAIL as expected (the test file is absent); AC2 base FAIL as expected (no commit of this serial yet).

<status>staged</status>
<round>38</round>
<workstream>ENRICH-R38-B</workstream>
<slot>~124</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
