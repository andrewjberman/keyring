# NFRA_OPLGTW task order -- `OG-sec-2` -- `graph.call` refuses an absolute URL whose host is not `graph.microsoft.com`, before any request is made (round 43; round-42 analysis item 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sec-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sec-2</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~152</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- gateway code and offline tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (round-42 analysis, item 2).
EGRESS CLASS, declared: NONE (the change narrows egress; the tests use a stub client and open no socket).
</preflight>

## 1. THE CELL -- `OG-sec-2` (decomposition addendum R3-T.120, round 43, workstream ENRICH-R43-A)

CONTEXT. `infra/aws/ec2/opal-gateway/app/graph.py` `call(token, method, path, ...)` builds `url = path if path.startswith("http") else GRAPH_BASE + path` (line 52) and sends the user's delegated Bearer token to `url`, following redirects. Two callers pass Graph's own `@odata.nextLink` straight through as `path` (`app/tools.py` near the transcript listing, `app/asker_scope.py` near the member listing); other callers (`mail_route.py`, `teams_route.py`, `transcript_route.py`) already check the host before calling. The link is issued by Graph, not by a caller, so no target is controllable today (the round-42 audit `OG-sec-1`: CLEAN); this is HARDENING, so that a future caller or a poisoned link can never send the token off Graph.

THE CHANGE (you write only `app/graph.py` and the new `tests/test_og_sec2.py`; every other file is read-only for you):
1. In `call`, BEFORE the `MOCK_GRAPH` branch and before any client is built: if `path` starts with `http` (case-insensitive), parse it with `urllib.parse.urlsplit` and require ALL of: scheme `https`; `hostname` equal (after lower-casing) to exactly `graph.microsoft.com`; no user-info (`@`) in the netloc; port absent or 443. Otherwise `raise GraphError(400, "GraphHostRefused", "refused: the URL is not on graph.microsoft.com")` (the message must not print the URL's query or any token). Relative paths (`/me/messages`) and absolute URLs on `graph.microsoft.com` behave exactly as today. Add a short module comment naming the pin and the round.
2. Do NOT touch `upload_large` (its pre-authorized `uploadUrl` goes through `httpx.Client.put`, not `call`) and do not add any other host to an allow-list: the login host is not used by `call` (the token flow lives in other modules).

NEW TESTS in `tests/test_og_sec2.py` (use a stub for `httpx.Client` that counts constructions and records the URL it is asked to request; set `MOCK_GRAPH` false through the config object or monkeypatch `graph.get_config` the way existing tests do; no socket may be opened):
- `test_ogsec2_ac01` FORGED HOSTS ARE REFUSED BEFORE ANY REQUEST: each of these `path` values raises `GraphError` with code `GraphHostRefused` and the stub client was constructed ZERO times: `https://evil.example/v1.0/me`, `https://graph.microsoft.com.evil.example/v1.0/me`, `https://graph.microsoft.com@evil.example/v1.0/me`, `http://graph.microsoft.com/v1.0/me` (not https), `https://graph.microsoft.com:8443/v1.0/me`, `HTTPS://GRAPH.MICROSOFT.COM.EVIL.EXAMPLE/v1.0/me`, `https://evil.example/graph.microsoft.com/v1.0/me`.
- `test_ogsec2_ac02` LEGITIMATE CALLS STILL REACH THE REQUEST: `https://graph.microsoft.com/v1.0/me/messages?$skiptoken=abc`, `HTTPS://Graph.Microsoft.Com/v1.0/me` and the relative `/me/messages` each reach the stub once with the expected URL (the relative one `GRAPH_BASE + path`), and the Authorization header is the Bearer token passed in.

Mutant control to run and report (restore the file byte-equal afterwards): deleting the host check makes `ac01` fail.

## 2. BOUNDS

- Write only the files in `<paths>`. No release, no deploy, no IAM, no env key, no Terraform, no change to `tools.py`, `asker_scope.py`, the route modules or any other app file.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print a secret, a token or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/graph.py
infra/aws/ec2/opal-gateway/tests/test_og_sec2.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE `app/graph.py` and `tests/test_og_sec2.py`; the rest you only READ. `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~152/`. Rows: id `NFRA_OPLGTW-Z-W152-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sec-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_named.sh tests/test_og_sec2.py test_ogsec2_ac01 test_ogsec2_ac02; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 2 of 2; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sec-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~152 '^infra/aws/ec2/opal-gateway/(app/graph\.py|tests/test_og_sec2\.py)$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~152: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-sec-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_bothorders.sh sec2set tests/test_og_sec2.py tests/test_transcript_route.py tests/test_teams_route.py tests/test_mail_route.py tests/test_transcript_tools.py tests/test_taxsma_workbook.py; echo "exit=$?"</invocation><expect>(?s)sec2set forward: passed (\d+); failed 0.*sec2set reverse: passed \1; failed 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the two new tests pass (forged hosts refused before any client is built; legitimate calls reach the request). `AC2`: your commits touch only the module and the new test file. `AC3`: the new tests and five existing Graph-calling test files (the route modules and the transcript and tax-workbook tools) pass together in both orders with the same count. Run `AC1` and `AC3` THREE times each and report the three results.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sec-2.round-43-pin-the-graph-host.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines and the three-run results, the mutant control).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 43, workstream ENRICH-R43-A. Source: round-42 analysis item 2 ("only `graph.microsoft.com`, plus the login host the token flow already uses; any other host raises before the request"). The cell reads "plus the login host" as not applying to `graph.call`: that function never calls the login host (`login.microsoftonline.com` appears only in `config.py` and `token_broker.py`); allowing it in `graph.call` would widen the function for nothing. Disclosed so the CTO can correct the reading.
- The existing nextLink checks in `tools.py:584` (`startswith(GRAPH_BASE + "/")`) and the route modules stay; this pin is the one in the sink.
- Chain: independent; feeds `OG-ap-42`. Slot `~152`.
- Pre-cut: `AC1` base FAIL as expected (the test file is absent).

<status>staged</status>
<round>43</round>
<workstream>ENRICH-R43-A</workstream>
<slot>~152</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
