# TO NFRA_FIDUPL.TO-FR-s-6 -- the adapters that let the daily attribution stage run

<to_id>NFRA_FIDUPL.TO-FR-s-6</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~5</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>fidelity-perg-adapters</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FR-s-6` (`decompositions/NFRA_FIDUPL_DECOMP_R2.md` section 7) | **outcome_ref:** FWD-9 |
**depends_on:** FR-s-1, FR-s-4 (both merged)

---

## WORKER FACE

### THE CELL

**FR-s-6** -- The adapters that let the daily attribution stage run: a request object over the signed-in Playwright context, the account lister that pages `accountList.json`, a structural extractor for its unmeasured response shape, and the one edit of `box/daily.py` that wires them. Contract rows: C-TENANCY, FWD-9. Answers your row NFRA_FIDUPL-D1-W5-S2 (armed on the issuer).

**Read first:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (sections 1, 9 and 11) and the cell text above.

### WHAT TO BUILD

Build `adapters.py`, `tests/test_adapters.py` and the one edit of `box/daily.py` named below, to worker reference sections 9 and 11. Why this cell exists: your own row W5-S2 found that the real attribute stage cannot run, because the signed-in `Session` exposes only a Playwright `context` and `close()`, `gswitch.GSwitcher` needs a request object with `get_text(url)` and `post_form(url, fields)`, and nothing supplies the account lister `sweep_attribution` calls. This cell supplies them. The attribution, gswitch and split modules are now ON your branch (merged).

1. `adapters.py`: `ContextRequest(context)` wrapping `context.request` (Playwright's APIRequestContext): `get_text(url) -> (status, text)` (follows redirects, as the form's 302 to www2 needs), `post_form(url, fields) -> (status, text)` (an urlencoded body from a dict, never logging the values), and `post_form_json(url, fields, headers) -> (status, parsed_json_or_None)`. `xsrf_token(context)` reads the `XSRF-TOKEN` cookie value as `PlaywrightSession.xsrf_token` does in `fetch.py` (reuse that code, do not edit `fetch.py`).
2. `extract_accounts(obj, account_key="accountNumber")`: the shape of the `accountList.json` response is UNMEASURED, so find the rows by structure: walk the parsed JSON for the first list whose items are dicts containing `account_key`, and return that key's values as strings. If none is found, raise `AdapterShapeError` whose message carries ONLY the top-level key names and the types (never a value) so the next run's trace names the shape. The container's name is never hard-coded.
3. `make_account_lister(request, xsrf, length=2000, extract=extract_accounts)`: returns a callable that pages `accountList.json` (POST `/ssc/accountsearch/wc/channel/accountList.json`, form `length=2000&accountNumber=&sourceCode=BROK&custodianCode=FID`, header `x-xsrf-token`; the offset field past 2,000 rows is named `start`, UNMEASURED, the same assumption FR-s-1 made) until a page shorter than `length` comes back, and returns the list of account-number strings. Never prints or logs an account value.
4. Edit `box/daily.py` `_real_daily_deps` (your own file from FR-s-4) so `attribute` builds `ContextRequest(handle.context)`, a `GSwitcher` on it, and `make_account_lister`, then calls `attribute.sweep_attribution(...)`; delete the refusal path (W5-S2). Keep every other behaviour.
5. Tests (fakes; no network): in the new `tests/test_adapters.py` `test_get_text_follows_redirect_and_returns_text`, `test_post_form_sends_urlencoded_body_without_logging_values`, `test_account_lister_pages_until_short_page`, `test_extract_accounts_finds_list_by_key_not_by_container_name`, `test_extract_failure_names_only_keys`, `test_daily_real_deps_use_adapters` (the last in this file, calling `_real_daily_deps` with a fake context). Your five daily tests must still pass.

### ACCEPTANCE

<criterion id="FR6-AC1" cell_refs="FR-s-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fr6</invocation><expect>R1-FR6-OK passed=\d+</expect></criterion>
`FR6-AC1` -- the six named adapter tests exist and pass.

<criterion id="FR6-AC2" cell_refs="FR-s-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fr4</invocation><expect>R1-FR4-OK passed=\d+</expect></criterion>
`FR6-AC2` -- the five daily-orchestration tests still pass after the wiring edit.

<expected_criteria>FR6-AC1,FR6-AC2</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FR6-AC1` base: FAIL as expected; `FR6-AC2` base: PASS as expected (a regression guard).

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder.
- **Fixtures only.** Fakes and synthetic data; no network, no AWS, no live call. No G number, account number or firm label in any output.
- **Refusal clause.** A premise that fails is a surprise row (`NFRA_FIDUPL-D1-W5-S<k>`, next unused), never a guess.
- **ASCII and Python 3.9 syntax** in every file.

<paths>
infra/aws/ec2/canonical-fidelity/adapters.py
infra/aws/ec2/canonical-fidelity/tests/test_adapters.py
infra/aws/ec2/canonical-fidelity/box/daily.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R2.md</decomp_doc> (round 2, section 7 addendum), cell `FR-s-6`.
<owned_cells>FR-s-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FR6-AC1,FR6-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~5/NFRA_FIDUPL.TO-FR-s-6.adapters.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FR6-AC1,FR6-AC2` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- fakes only; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- build on fakes; runs when the live round touches this surface.
lane: the paths block.
</preflight>

Source: worker row NFRA_FIDUPL-D1-W5-S2; decomposition round 2 section 7; worker reference sections 9 and 11.
