# TO NFRA_CTLPLN.TO-CT-w-9 -- workstream LOGFIX round 1 (cell CT-w-9): the data proxy stops writing callers' bearer tokens into its log group (row NFRA_CTLPLN-S9110)

<to_id>NFRA_CTLPLN.TO-CT-w-9</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~71</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>LOGFIX</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-w-9` (`decompositions/NFRA_CTLPLN_DECOMP.round8.md`, the added rows) | **outcome_ref:** FWD-28 (security hygiene) |
**depends_on:** none (it edits `lambda_function.py`; `CT-w-8` touches `firm_page_access.py` and the registry only)

---

## WORKER FACE

### THE CELL

Row NFRA_CTLPLN-S9110 (read it in `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`): the data proxy's `lambda_handler` begins with `print(f"Event: {json.dumps(event)}")` (about line 2122 of `infra/aws/lambda/portal_data_proxy/lambda_function.py`), so each caller's `Authorization` header (a 15-minute bearer JWT) is written to the log group `/aws/lambda/opal-portal-data-proxy` (14-day retention): 45 of 47 Event lines in the retention held a JWT-shaped string. The CTO has ruled (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_CTLPLN_S9110_DATA_PROXY_LOGS_BEARER_TOKENS_20261012.md`): class ARMED; REMOVE the event print and log method, path, status and request id only. You change CODE and prove it with unit tests. You deploy nothing and call no AWS service (a separate order applies it under a pair).

### BUILD

1. **Remove the whole-event print** in `lambda_handler`. Replace it with ONE log line built only from: the HTTP method, the normalised path, and the API Gateway request id (`event['requestContext']['requestId']`, or the `x-amzn-requestid`-free fallback `'-'`). Do not print `headers`, `multiValueHeaders`, `cookies`, `body`, `queryStringParameters`, `requestContext.authorizer`, or `json.dumps(event)` anywhere. (The method and path are computed AFTER the current print: move the new line to after they are known, and keep the OPTIONS preflight and `?warm=1` behaviour exactly as they are.)
2. **Audit every other logging call in the handler and in `session_tracker.py`** (there are about 67 `print(` / `tracker.log_*` / logger sites in `lambda_function.py`): list, in your report, every site whose arguments can contain the event, a header, the Authorization value, a cookie, a token, a body or a query string. Fix only the ones that can carry credentials (replace the value by its length or a fixed marker); change no other log line. `SessionTracker` extracts a session id from request headers: if it logs that header's VALUE and the value is a credential, say so in a row; a session id is not a credential.
3. **Tests**, a NEW file `infra/aws/lambda/portal_data_proxy/tests/test_no_credentials_in_logs.py`: with a fake event carrying `Authorization: Bearer eyJ<fake>.<fake>.<fake>`, a `Cookie: refresh=eyJ<fake>` header, a body containing a fake token, and an authorizer context, drive `lambda_handler` for EVERY route in the census (`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~62/DATA_PROXY_ROUTE_CLASS_CENSUS.md`, 41 routes; parse the route list the way `test_route_firm_fence.py` does), for an internal caller, a partner caller and an unmatched path, capturing stdout, stderr and the `logging` handlers; assert that NONE of the captured output contains `Bearer`, `eyJ`, the fake cookie value, the fake body token, or the whole `Authorization` value; and that the one new line carries the method, the path and the request id. A control arm: the same test against the OLD handler (`git show 2fbb74e87d:...`, a temp copy) must FAIL on the `eyJ` assertion. Stub `boto3` as the existing tests do; no firm name typed (use `ROUTE_FIRMS`/scopes at run time if you need a firm).

### RULES FOR THIS CELL

Your write surface is exactly the `<paths>`. You do not touch `firm_page_access.py`, the registry, `lib/opal_naming.py`, `lambda-source-map.json` or the portal. No terraform, no aws, no deploy, no push. `.tools/safe-commit.sh` for every commit (if the naming gate REFUSES, STOP and file a BLOCKING row). Do NOT commit the `portal` gitlink. No non-ASCII added; Python 3.11 compatible; ruff clean. CLAUDE.md and org/XXX.md are LOCKED. A real credential must never enter a file you write: every token in a test is a made-up string. FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to the surprise-channel file (id `NFRA_CTLPLN-W71-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTw9-AC1" cell_refs="CT-w-9"><invocation>python -m pytest -q infra/aws/lambda/portal_data_proxy/tests/test_no_credentials_in_logs.py</invocation><expect>passed</expect></criterion>
`CTw9-AC1` -- the log-capture tests pass for all 41 routes and three callers.

<criterion id="CTw9-AC2" cell_refs="CT-w-9"><invocation>python -m pytest -q infra/aws/lambda/portal_data_proxy/tests/test_route_firm_fence.py</invocation><expect>965 passed</expect></criterion>
`CTw9-AC2` -- the firm fence still holds exactly as built (965 tests, unchanged).
</proof_of_spec>

<expected_criteria>CTw9-AC1,CTw9-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~71/NFRA_CTLPLN.TO-CT-w-9.data-proxy-stop-logging-the-event.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTw9-AC1,CTw9-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID. Report the control arm's failure count and the audit list of logging sites.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round8.md</decomp_doc>
<owned_cells>CT-w-9</owned_cells>
</decomp_ref>

<paths>
infra/aws/lambda/portal_data_proxy/lambda_function.py
infra/aws/lambda/portal_data_proxy/tests/
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a credential logged through a path other than the one print (the audit of every logging site, and the capture test over all 41 routes and three callers); a log line so thin it hides an incident (method, path and request id stay); a fix that changes a route's answer (CTw9-AC2 holds the 965 fence tests); a fake token that is really one (every token in a test is made up); BLIND: log lines already written (14 days of retention hold tokens that expired within 15 minutes of each request, and the cookie/refresh measurement is the apply order's).
risk: WORLD is declared because the L6 gate derives a floor from the infra paths; this cell deploys nothing.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO ruling msg 108509 on row NFRA_CTLPLN-S9110.
