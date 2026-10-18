# NFRA_OPLGTW task order -- `OG-sec-3` -- COMPLETE the SSRF audit of the gateway's outbound calls: the JWKS fetches the round-42 pattern missed (round 43; round-42 analysis item 3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sec-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sec-3</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~153</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only audit; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (round-42 analysis, item 3).
EGRESS CLASS, declared: NONE (you read source files only).
</preflight>

## 1. THE CELL -- `OG-sec-3` (decomposition addendum R3-T.120, round 43, workstream ENRICH-R43-A)

WHY. Round 42's audit (`OG-sec-1`, `W145/SSRF_AUDIT.json`, verdict CLEAN, 0 controllable) counted 18 outbound HTTP call sites with a pattern that did not match the JWKS fetches: `PyJWKClient(url)` fetches the signing keys from a URL. A later cell lets the loopback probe listener be armed again, and an outbound fetch steerable to a caller-chosen host could reach it. This cell finishes the audit: the same question about the code as it is. Does any outbound HTTP call take its target (scheme, host, port or path prefix) from a value a caller controls?

THE AUDIT (read-only; you change NO product file). The SIX modules, under `infra/aws/ec2/opal-gateway/app/`: `identity.py`, `graph.py`, `token_broker.py`, `integrations/ycharts/client.py`, `integrations/globgrph/integration.py`, `integrations/opal_portal/integration.py` (`token_broker.py` is the sixth: the CTO's analysis counted the denominator as 20 in the five round-42 modules; `token_broker.py` line 307 is one more `PyJWKClient(` site, so the check measures 21 and says so). The check measures the denominator itself with this pattern over those six files: `(requests|httpx|urllib\.request|aiohttp|http\.client|session|client|_http|conn)[A-Za-z_.]*\.(get|post|put|delete|patch|request|head|urlopen)\(|urlopen\(|\.request\(|PyJWKClient\(` (grep -nE; each matching line is a site). You may start from `W145/SSRF_AUDIT.json` (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~145/SSRF_AUDIT.json`, 18 rows), but you RE-READ each site: carry a round-42 row over only after you have read the code at the line it names now (line numbers may have moved), and say in `reason` that you re-read it. For EVERY matching line write one row in `W/SSRF_AUDIT_R43.json`:
`{"body": {"sites": [{"file": "<path under app/, for example identity.py>", "line": <the line number>, "call": "<the call text, 120 characters or fewer>", "target_source": "<where the URL or host comes from: a module constant, an environment value, a config value, a Secrets Manager value, a template filled from a token claim, or a function argument and which caller supplies it>", "controllable": "yes|no", "reason": "<one line: what you read to decide>"}], "controllable_yes": <count of yes>, "verdict": "CLEAN|STOP"}}`.
Decide `controllable` by tracing the target back to its source in the code: `yes` only if a value that a REQUEST (a tool argument, a query or path parameter, a header, a request body, a token claim that the caller writes, a stored record a caller writes) can influence reaches the scheme, host, port or a path that decides the host. For the JWKS sites trace the `jwks_url` / `UPSTREAM_JWKS_TEMPLATE.format(tid=tid)` value: if `tid` comes from an UNVERIFIED token claim, say so and decide `yes` or `no` on whether it can change the HOST (a tenant id substituted into a path segment of a fixed host is `no` only if the template's host is fixed and the value is validated or cannot contain `/`, `@` or `.`; say which). A site you cannot trace is `yes` until you can. `verdict` is `STOP` if ANY row is `yes`, otherwise `CLEAN`. A `yes` row ALSO becomes a surprise row (class `BLOCKING`, `hazard_standing` `ARMED`, named in `disarm_owner` `2.0.0_SA_COO~O`) quoting the file, line and the controllable value. Do not print an environment value, a secret or a client value anywhere.

## 2. BOUNDS

- Write only `W/SSRF_AUDIT_R43.json` and (if a row is needed) the channel. NO product file, no test, no release, no deploy.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~153/` (the tree convention grants it). You only READ the gateway source. Rows: id `NFRA_OPLGTW-Z-W153-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sec-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r43/checks/sec3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)call sites matched by the pattern in the six modules: (\d+) \(round 42 counted 18 in five.*listed in the record: \1; matched lines missing from the record: 0 \(want 0\); malformed rows: 0 \(want 0\).*controllable yes: \d+; the record says \d+ and verdict (CLEAN|STOP): consistent.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sec-3"><invocation>git log --author='0.9.0_WK_NFRA_OPLGTW~153 <' --name-only --format= | grep -v '^org/missions/D9/NFRA/NFRA_OPLGTW/' | grep -c . ; echo "exit=$?"</invocation><expect>(?s)^0\s*exit=[01]\s*$</expect></criterion>
</proof_of_spec>

- `AC1`: every outbound call line the pattern finds is a row of the audit, each row is complete, and the verdict follows from the rows (a `yes` anywhere means `STOP`). Either verdict PASSES `AC1`: a STOP is a finding, not a failure of the audit. `AC2`: your commits touch no file outside the project tree (no product file).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sec-3.round-43-complete-the-ssrf-audit.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hash, the AC lines, the verdict, the matched count, and for each `yes` row its file and line only).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 43, workstream ENRICH-R43-A. Source: round-42 analysis item 3 ("add `PyJWKClient(`, so the denominator is 20, not 18; re-run read-only; any controllable target is a STOP and becomes its own row"). Measured by the issuer at the cut: `PyJWKClient(` matches `identity.py:44`, `identity.py:115` (the two sites of the slug) and `token_broker.py:307` (a third, outside the five modules), so the six-module denominator is 21, not 20; disclosed to the CTO in the issuance. Both `identity.py` URLs were read as config-sourced in round 42; `token_broker.py:307` builds its URL from `UPSTREAM_JWKS_TEMPLATE.format(tid=tid)`.
- A `STOP` here is a STOP on `OG-ap-42` (its `ap42.AC1` requires `CLEAN 0`), not a failure of this order.
- Read-only, no product path in `<paths>`: `<risk>LOCAL</risk>`.
- Pre-cut: `AC1` base FAIL as expected (the record is absent).

<status>complete</status>
<round>43</round>
<workstream>ENRICH-R43-A</workstream>
<slot>~153</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
