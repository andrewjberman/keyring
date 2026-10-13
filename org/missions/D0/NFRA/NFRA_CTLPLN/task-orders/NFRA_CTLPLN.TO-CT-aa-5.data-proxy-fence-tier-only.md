# TO NFRA_CTLPLN.TO-CT-aa-5 -- workstream DEVFENCE round 3 (cell CT-aa-5): the data proxy's route fence goes back to `tier == 'internal'` only; the Dev clause CT-aa-3 added is removed (CTO msg 108612, PRD v0.28)

<to_id>NFRA_CTLPLN.TO-CT-aa-5</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~76</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>DEVFENCE</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-aa-5` (`decompositions/NFRA_CTLPLN_DECOMP.round12.md`) | **outcome_ref:** FWD-28 |
**depends_on:** none (it edits `lambda_function.py` and the tests folder; nothing else of the round touches them)

---

## WORKER FACE

### THE CELL

`_require_route_access(event, tracker, http_method, path)` in `infra/aws/lambda/portal_data_proxy/lambda_function.py` (about line 2094) currently reads: `user_type = str(claims.get('userType') or '').strip()` and admits when `tier == 'internal' or user_type == 'Dev'` (added by cell CT-aa-3, merged @96c4f5f063, live). MEASURED afterwards (row NFRA_CTLPLN-S9115): the auth handler derives a login's token tier from the firm (`tier = firmId === 'opal-capital' ? 'internal' : 'advisor'`), so every staff Dev login already presents tier `internal`; the Dev clause admits nobody new except a Dev token on a non-Opal firm, which is a WIDENING. RULED by the CTO (msg 108612, PRD v0.28): remove the clause; the fence is `tier == 'internal'` only.

### BUILD

1. In `_require_route_access`, delete the `user_type` line and make the test `if tier == 'internal':` again. Restore the docstring to say: the tier `internal` reads every route; a class-(i) route answers a caller whose `firmId` claim is in that route's `ROUTE_FIRMS` set and no one else; every other path answers 403 unless the authorizer tier is `internal`; and add ONE sentence: a login whose `userType` is `Dev` but whose tier is not `internal` is refused like any other non-internal caller (the authorizer derives the tier from the firm). Change nothing else in the file.
2. DELETE (`git rm`) `infra/aws/lambda/portal_data_proxy/tests/test_route_dev_fence.py` (it asserts the removed clause) and ADD a NEW test file `infra/aws/lambda/portal_data_proxy/tests/test_route_tier_only_fence.py`, built from the deleted file's scaffolding (read it whole first), over all 41 routes with the route functions replaced by sentinels: (a) a caller with tier `advisor`, `userType` `Dev` and a made-up firm answers 403 on every class-(ii) route, through BOTH the flat and the nested `lambda` authorizer context; (b) the same with tier absent: 403; (c) a partner-advisor caller (tier `advisor`, made-up partner firm, `userType` `Advisor`, absent, `'null'`) answers 403 on every class-(ii) route and, on the two class-(i) routes, 200 only when its firm is in `ROUTE_FIRMS`; (d) `'dev'`, `'DEV'`, `'Developer'`, `''`, `' Dev '` with a non-internal tier: 403 on every class-(ii) route; (e) tier `internal` with ANY userType (`Dev`, `Advisor`, absent) answers 200 on every route; (f) a Dev token whose firm is a made-up partner firm answers 403 on every class-(ii) route. Control arm: `PORTAL_PROXY_UNDER_TEST=<a copy of the CURRENT, pre-edit lambda_function.py (git show 96c4f5f063:infra/aws/lambda/portal_data_proxy/lambda_function.py)>` must make cases (a), (b), (f) FAIL; report the count. Every firm id and email in a test is made up; type no real firm name (the naming gate refuses firm tokens; if it REFUSES a commit, STOP and file a BLOCKING row, never encode around it).
3. Do NOT touch `firm_page_access.py`, the registry, `lib/opal_naming.py`, `lambda-source-map.json`, `session_tracker.py` or the portal.

### RULES FOR THIS CELL

Your write surface is exactly the `<paths>`. No terraform, no aws, no deploy, no push; nothing is deployed by this cell (a separate order applies it under a signed pair). `.tools/safe-commit.sh` for every commit. Do NOT commit the `portal` gitlink. No non-ASCII added; Python 3.11 compatible; ruff clean. CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W76-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaa5-AC1" cell_refs="CT-aa-5"><invocation>python -m pytest -q infra/aws/lambda/portal_data_proxy/tests/test_route_tier_only_fence.py</invocation><expect>passed</expect></criterion>
`CTaa5-AC1` -- the tier-only tests pass over all 41 routes (report the whole last line: it must read `N passed` with no `failed` and no `error`).

<criterion id="CTaa5-AC2" cell_refs="CT-aa-5"><invocation>python -m pytest -q infra/aws/lambda/portal_data_proxy/tests/test_route_firm_fence.py</invocation><expect>965 passed</expect></criterion>
`CTaa5-AC2` -- the firm fence still holds exactly as built (965 tests, unchanged; a control that PASSES at the base).

<criterion id="CTaa5-AC3" cell_refs="CT-aa-5"><invocation>python -m pytest -q infra/aws/lambda/portal_data_proxy/tests/test_no_credentials_in_logs.py</invocation><expect>1012 passed</expect></criterion>
`CTaa5-AC3` -- the log-capture tests still pass (1012; a control that PASSES at the base).
</proof_of_spec>

<expected_criteria>CTaa5-AC1,CTaa5-AC2,CTaa5-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation (no `timeout` prefix). Also run the whole folder once (`python -m pytest -q infra/aws/lambda/portal_data_proxy/tests/`) and report its last line: no test of a removed clause may remain. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~76/NFRA_CTLPLN.TO-CT-aa-5.data-proxy-fence-tier-only.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaa5-AC1,CTaa5-AC2,CTaa5-AC3`, and flip `<status>` to `complete` only when all three pass and the instance is VALID (if the flip is refused as outside your grant, leave it `pending` and say so; the issuer flips). Report the control-arm count and the diff of `lambda_function.py` (it should be a few lines).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round12.md</decomp_doc>
<owned_cells>CT-aa-5</owned_cells>
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
comp-adversary: RUN -- a removal that leaves the Dev clause reachable by another spelling (cases a, b, d, f over all 39 class-(ii) routes); a removal that refuses the internal tier (case e); a change to the class-(i) answer (CTaa5-AC2 holds the 965 tests); a stale test of the removed clause left in the folder (the whole-folder run); BLIND: Dev tokens minted outside the auth handler (none measured).
risk: WORLD is declared because the L6 gate derives a floor from the infra paths; this cell deploys nothing.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO msg 108612 (PRD v0.28), row NFRA_CTLPLN-S9115 and its disposition S9116.
