# TO NFRA_FIDUPL.TO-FR-s-6 -- the adapters that let the daily attribution stage run

<to_id>NFRA_FIDUPL.TO-FR-s-6</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~5</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
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

**FR-s-6** -- The adapters that let the daily attribution stage run: a request object over the signed-in Playwright context, the account lister that pages `accountList.json`, a structural extractor for its unmeasured response shape, and the one edit of `box/run.py` `_real_daily_deps` that wires them. Contract rows: C-TENANCY, FWD-9. Answers your row NFRA_FIDUPL-D1-W5-S2 (armed on the issuer).

**Read first:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (sections 1, 9 and 11) and the cell text above.

### WHAT TO BUILD

Build `adapters.py`, `tests/test_adapters.py` and the one edit of `box/run.py` named below, to worker reference sections 9 and 11. Why this cell exists: your own row W5-S2 found that the real attribute stage cannot run, because the signed-in `Session` exposes only a Playwright `context` and `close()`, `gswitch.GSwitcher` needs a request object with `get_text(url)` and `post_form(url, fields)`, and nothing supplies the account lister `sweep_attribution` calls. This cell supplies them. The attribution, gswitch and split modules are now ON your branch (merged).

1. `adapters.py`: `ContextRequest(context)` wrapping `context.request` (Playwright's APIRequestContext): `get_text(url) -> (status, text)` (follows redirects, as the form's 302 to www2 needs), `post_form(url, fields) -> (status, text)` (an urlencoded body from a dict, never logging the values), and `post_form_json(url, fields, headers) -> (status, parsed_json_or_None)`. `xsrf_token(context)` reads the `XSRF-TOKEN` cookie value as `PlaywrightSession.xsrf_token` does in `fetch.py` (reuse that code, do not edit `fetch.py`).
2. `extract_accounts(obj, account_key="accountNumber")`: the shape of the `accountList.json` response is UNMEASURED, so find the rows by structure: walk the parsed JSON for the first list whose items are dicts containing `account_key`, and return that key's values as strings. If none is found, raise `AdapterShapeError` whose message carries ONLY the top-level key names and the types (never a value) so the next run's trace names the shape. The container's name is never hard-coded.
3. `make_account_lister(request, xsrf, length=2000, extract=extract_accounts)`: returns a callable that pages `accountList.json` (POST `/ssc/accountsearch/wc/channel/accountList.json`, form `length=2000&accountNumber=&sourceCode=BROK&custodianCode=FID`, header `x-xsrf-token`; the offset field past 2,000 rows is named `start`, UNMEASURED, the same assumption FR-s-1 made) until a page shorter than `length` comes back, and returns the list of account-number strings. Never prints or logs an account value.
4. Edit `_real_daily_deps` in **`box/run.py`** (it lives there, at about line 270, not in `daily.py`: the issuer's first draft of this order named the wrong file, your row W5-S3 caught it, and `box/run.py` is now in your paths block) so `attribute` builds `ContextRequest(handle.context)`, a `GSwitcher` on it, and `make_account_lister`, then calls `attribute.sweep_attribution(...)`; delete the refusal path (W5-S2). Keep every other behaviour.
5. Tests (fakes; no network): in the new `tests/test_adapters.py` `test_get_text_follows_redirect_and_returns_text`, `test_post_form_sends_urlencoded_body_without_logging_values`, `test_account_lister_pages_until_short_page`, `test_extract_accounts_finds_list_by_key_not_by_container_name`, `test_extract_failure_names_only_keys`, `test_daily_real_deps_use_adapters` (the last in this file, calling `_real_daily_deps` with a fake context). Your five daily tests must still pass.

### REPAIR (issuer, 2026-10-20 ~16:00Z; this order is REOPENED) -- the accountList.json shape is now MEASURED

The CRO read the response structure out of Andrew's human capture: `C:/Dev/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261020_NFRA_FIDUPL_ACCOUNTLIST_SHAPE.md` (absolute path, main tree, read-only; read it whole). It corrects two guesses in your `adapters.py`:
1. **The rows are `accountListResponse.accounts` and the account number is the key `number`** (not `accountNumber`). Fix `extract_accounts` to try that exact path and key FIRST, falling back to the structural search only if the path is absent (keep `AdapterShapeError` naming only key names and types). Keep ONLY the account-number strings; `ssn`, `taxReportingId`, `primaryOwner` and every other field are personal and are dropped immediately, never held, logged or returned.
2. **Paging.** The total is `accountListResponse.pageResponse.available` (5197 in Andrew's book, with 2000 rows on the first page). `pageResponse` also carries `start` and `sessionCacheId` (both null on the single page captured); their live behaviour is UNMEASURED. Rewrite `make_account_lister`: send the first page WITHOUT `start`; read `available` and `sessionCacheId` from the first response; while the rows collected are fewer than `available`, request the next page with `start=<rows collected so far>` and, when `sessionCacheId` is non-null, `sessionCacheId=<that value>` (the request-side field names are the same two words, an assumption to file as ONE row); stop when collected reaches `available` or a page returns no rows; never loop more than 50 pages; if the loop ends short of `available`, raise `AdapterShapeError` carrying only the two counts (collected, available), never staying silent about a short list.
Add four tests to the EXISTING `tests/test_adapters.py`: `test_extract_accounts_uses_measured_container_and_number_key`, `test_lister_stops_at_available_total`, `test_lister_sends_session_cache_id_on_later_pages`, `test_lister_fails_loud_when_short_of_available`. FR6-AC1 now needs ten; FR6-AC2 must still pass. Fakes only; no AWS, no live call, no account number in any output. Refresh the proof instance and flip only when both criteria PASS.

### REPAIR 1 (issuer, 2026-10-21 ~03:25Z; CloudOps row D1-S12, your own row D1-W5-S4 predicted this branch) -- the live page-2 request form is unmeasured, so the lister finds it

The daily-mode proof run reached the first G number's account list: page 1 returned 2000 rows with `available` 5204, and the next request under the form `start` + `sessionCacheId` returned no new distinct rows, so the lister failed loud (`collected 2000 of 5204 available`). Nothing in the repo or in the CRO's capture (RESEARCH_20261020_NFRA_FIDUPL_ACCOUNTLIST_SHAPE.md, "Not measured") names the live request form, and waiting for a capture stalls the project, so the lister DISCOVERS the form on the live API and says which one worked. Change `adapters.py` (`make_account_lister`), `box/daily.py` (one print) and `tests/test_adapters.py` only:
1. A table `PAGING_FORMS` of candidate forms, tried in this order, each a function of (`n` = distinct rows collected so far, `session` = the last `sessionCacheId` seen or None, `available`) returning the EXTRA form fields to send with the usual four fields: form 0 = today's (`start`=n, plus `sessionCacheId` when known); 1 = `pageRequest.start`=n (+ `pageRequest.sessionCacheId`); 2 = `startIndex`=n; 3 = `offset`=n; 4 = `page`=(n // length)+1; 5 = `pageNumber`=(n // length)+1; 6 = `firstResult`=n; 7 = `from`=n; 8 = `startRow`=n; 9 = `start`=n alone (no session); 10 = the FIRST-page form again with `length` = `available` (one big page, no start). A form that returns a non-200 status or an `AdapterShapeError`-grade page is counted as "no new rows" for that form and the next is tried; only a non-200 on the FIRST page is fatal, as today.
2. For page 2 and later: send the form currently in use; if a response adds NO new distinct number while the total is not yet reached, move to the NEXT form and resend (never the same form twice, never more than the table's length of extra requests in one lister call). The first form that adds new distinct numbers is KEPT for the rest of that call AND for every later call of the same lister (the lister object remembers it, so the other G numbers' lists do not search again). When the table is exhausted raise `AdapterShapeError("accountList paging: no form added rows; tried forms 0-10; collected %d of %d available")` (counts only).
3. The lister exposes the index of the form in use as the attribute `lister.paging_form` (None until a second page was needed). `box/daily.py`: after the attribution stage finishes, print ONE line `OK: accountList paging form=<index>` when the attribute is not None (nothing when it is None or the lister has no such attribute); record it as `paging_form` in the coverage record. Names the candidate's INDEX only, never a field value.
4. Everything else stays: distinct counting, `PAGE_CAP`, the PII drop, counts-only errors, the `finally` restore. The existing tests keep passing unchanged (form 0 is today's form).
5. Two tests in the EXISTING `tests/test_adapters.py`: `test_lister_tries_other_paging_forms_and_keeps_the_one_that_yields_new_rows` (a fake that returns new rows only for form 3 `offset`: the lister ends with every row, `lister.paging_form == 3`, and a SECOND call of the same lister sends form 3 for its page 2 without trying forms 0-2 again) and `test_lister_names_the_forms_tried_when_none_yields_new_rows` (a fake that never pages: `AdapterShapeError` whose message holds the counts and the form range and no value). FR6-AC1 (`fr6`) now needs twelve named; FR6-AC2 (`fr4`) must still pass. The whole module suite: no failure, last line in your report. Synthetic data only (fakes). The checker is `fidupl_round_checks.py`. FAST: a live re-run waits on it.

### ACCEPTANCE

<criterion id="FR6-AC1" cell_refs="FR-s-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fr6</invocation><expect>R1-FR6-OK passed=\d+</expect></criterion>
`FR6-AC1` -- the ten named adapter tests (six built, four of the REPAIR) exist and pass.

<criterion id="FR6-AC2" cell_refs="FR-s-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fr4</invocation><expect>R1-FR4-OK passed=\d+</expect></criterion>
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
infra/aws/ec2/canonical-fidelity/box/run.py
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
