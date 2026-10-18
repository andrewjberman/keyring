# NFRA_OPLGTW task order -- `OG-sec-1` -- a READ-ONLY audit of the gateway's outbound HTTP call sites for a caller-controlled target (the precondition of the probe listener `OG-pr-1`; round 42; CTO decision msg 35584, CRO research `GATEWAY_SERVICE_PROBE_DESIGN_FORK_RESEARCH_20261018.md`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-sec-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-sec-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~145</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read of source files; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's decision 35584, item 4 (any controllable target is a STOP on the listener cell).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-sec-1` (decomposition addendum R3-T.119, round 42, workstream ENRICH-R42-A)

WHY. The next release adds a SEPARATE listener bound to `127.0.0.1` on the running gateway (`OG-pr-1`), reachable only from the host. Any process on the host can call loopback, so if an OUTBOUND fetch inside the gateway can be steered to a caller-chosen host (server-side request forgery, SSRF), a caller could reach that listener. This cell answers one question about the code as it is: does any outbound HTTP call take its target (scheme, host, port or path prefix) from a value a caller controls?

THE AUDIT (read-only; you change NO product file). The five modules, under `infra/aws/ec2/opal-gateway/app/`: `identity.py`, `graph.py`, `integrations/ycharts/client.py`, `integrations/globgrph/integration.py`, `integrations/opal_portal/integration.py`. The CRO counted 18 outbound call sites; the check measures the denominator itself with this pattern over those five files: `(requests|httpx|urllib\.request|aiohttp|http\.client|session|client|_http|conn)[A-Za-z_.]*\.(get|post|put|delete|patch|request|head|urlopen)\(|urlopen\(|\.request\(` (grep -nE; each matching line is a site). For EVERY matching line write one row in `W/SSRF_AUDIT.json`:
`{"body": {"sites": [{"file": "<path under app/, for example identity.py>", "line": <the line number>, "call": "<the call text, 120 characters or fewer>", "target_source": "<where the URL or host comes from: a module constant, an environment value, a config value, a Secrets Manager value, or a function argument and which caller supplies it>", "controllable": "yes|no", "reason": "<one line: what you read to decide>"}], "controllable_yes": <count of yes>, "verdict": "CLEAN|STOP"}}`.
Decide `controllable` by tracing the target back to its source in the code: `yes` only if a value that a REQUEST (a tool argument, a query or path parameter, a header, a request body, a stored record a caller writes) can influence reaches the scheme, host, port or a path that decides the host. A fixed base URL with a path segment built from a validated identifier is `no`, and you say why. A site you cannot trace is `yes` until you can. `verdict` is `STOP` if ANY row is `yes`, otherwise `CLEAN`. A `yes` row ALSO becomes a surprise row (class `BLOCKING`, `hazard_standing` `ARMED`, named in `disarm_owner` `2.0.0_SA_COO~O`) quoting the file, line and the controllable value. Do not print an environment value, a secret or a client value anywhere.

## 2. BOUNDS

- Write only `W/SSRF_AUDIT.json` and (if a row is needed) the channel. NO product file, no test, no release, no deploy.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~145/` (the tree convention grants it). You only READ the gateway source. Rows: id `NFRA_OPLGTW-Z-W145-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-sec-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r42/checks/sec1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)call sites matched by the pattern in the five modules: (\d+) \(the CRO counted 18\); listed in the record: \1; matched lines missing from the record: 0 \(want 0\); malformed rows: 0 \(want 0\).*controllable yes: \d+; the record says \d+ and verdict (CLEAN|STOP): consistent.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-sec-1"><invocation>git log --author='0.9.0_WK_NFRA_OPLGTW~145 <' --name-only --format= | grep -v '^org/missions/D9/NFRA/NFRA_OPLGTW/' | grep -c . ; echo "exit=$?"</invocation><expect>(?s)^0\s*exit=[01]\s*$</expect></criterion>
</proof_of_spec>

- `AC1`: every outbound call line the pattern finds is a row of the audit, each row is complete, and the verdict follows from the rows (a `yes` anywhere means `STOP`). Either verdict PASSES `AC1`: a STOP is a finding, not a failure of the audit. `AC2`: your commits touch no file outside the project tree (no product file).

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-sec-1.round-42-ssrf-audit-of-the-outbound-calls.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hash, the AC lines, the verdict, and for each `yes` row its file and line only).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 42, workstream ENRICH-R42-A (decomposition addendum R3-T.119). The CTO's cell 4 (msg 35584): the audit is the precondition of `OG-pr-1` and `OG-ap-40`; `ap40.AC1` reads `SSRF_AUDIT.json` and refuses unless the verdict is `CLEAN` with 0 controllable. A `yes` is a STOP on the listener chain and a row for the CTO; it is not a finding the worker fixes. Read-only, so `<risk>LOCAL</risk>`.
- Pre-cut: `AC1` base FAIL as expected (the record is absent); the pattern matches 18 lines in the five modules at the base (the CRO's count).

<status>staged</status>
<round>42</round>
<workstream>ENRICH-R42-A</workstream>
<slot>~145</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
