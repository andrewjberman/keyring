# TO NFRA_FIDUPL.TO-FT-s-9 -- the account-list paging probe (read-only, counts only)

<to_id>NFRA_FIDUPL.TO-FT-s-9</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~5</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3-paging</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-9` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 8) | **outcome_ref:** FWD-9 |
**depends_on:** FR-s-6 (merged)

---

## WORKER FACE

### THE CELL

**FT-s-9** -- The live account list returns 2000 of 5204 and none of the eleven paging forms your lister tries (`adapters.PAGING_FORMS`) adds a row. This cell builds ONE module that measures what the live API does, in one signed-in session, so the next repair is cut from facts. It makes only read requests to the one `accountList.json` endpoint, on the G number the session starts on (no G switch), and prints COUNTS ONLY.

**Read first:** `box/run.py` (`main`, `check_pointers`, `_real_deps`: its `read_secret` and `open_session` are what you reuse), `adapters.py` (`ContextRequest`, `xsrf_token`, `PAGING_FORMS`, `_page_fields`, `_page_meta`, `extract_accounts`, `WC_BASE`), `attribute.py` (`ACCOUNT_LIST_FIELDS`, `ACCOUNT_LIST_PATH`), and `tests/test_box_daily.py` for the fake-context style.

### WHAT TO BUILD

`box/paging_probe.py` (new, Python 3.9, ASCII) and `tests/test_paging_probe.py` (new, fakes only). The module:
1. `main(argv=None)`: config path = first argument or `/opt/fidelity-uploader/config.json`; load it, run `run.check_pointers` (import the sibling `run` the way `tests/test_box_daily.py` does); `deps = run._real_deps(config)`; `creds = deps["read_secret"](config["wealthscape_secret_id"])`; `session = deps["open_session"](config, creds)`; then `probe(session.context, emit)` inside a `try`, and `session.close()` in the `finally` (a close failure prints `ERROR: session close did not finish`). Return 0 when page 1 was read, 1 otherwise. A failure prints `ERROR: probe <class name>` only (the class name, never a message).
2. `probe(context, emit)` with `emit` a one-argument print function (injectable). Build `request = adapters.ContextRequest(context)` and post with `request.post_form_json(adapters.WC_BASE + attribute.ACCOUNT_LIST_PATH, fields, {"x-xsrf-token": adapters.xsrf_token(context)})`. Send at most 50 requests in all.
   - **Page 1** with `adapters._page_fields(2000)`: emit `PROBE page1 status=<s> rows=<n> available=<a> distinct=<d> page_start=<int|null> page_length=<int|null> session=<null|present> resp_keys=<sorted keys of accountListResponse, comma-joined> statuses=<codes>`. Keep the set of page-1 account numbers in memory only; a non-200 here emits `PROBE stop: HTTP <s>` and ends.
   - **Each form** `i` in `range(len(adapters.PAGING_FORMS))`: call `PAGING_FORMS[i](len(page1_set), session_value, available, 2000)` exactly as `make_account_lister` does (read it; the call returns the extra fields and the page length), post, and emit `PROBE form=<i> status=<s> rows=<n> new=<k> available=<a|null> page_start=<int|null> session=<null|present> statuses=<codes>` where `new` counts numbers NOT in the page-1 set. A request that raises emits `PROBE form=<i> error=<class name>` and goes on.
   - **Prefix sweep:** for each character `c` in `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ`, post `ACCOUNT_LIST_FIELDS` with `accountNumber=c` and `length` `1`, and emit `PROBE prefix=<c> status=<s> available=<a|null>`.
   - A status 401 or 403 on ANY request emits `PROBE stop: HTTP <s>` and ends the probe at once (project rule: stop and report). End with `PROBE done requests=<n>`.
   - `<codes>` = up to five `<severity>:<code>` pairs from `accountListResponse.statuses` (never the `text`), each part cut to 20 characters and any character outside `A-Za-z0-9_.-` replaced by `?`; `none` when the list is empty or absent.
3. Never print, log or return an account number, G number, cookie, token or any response text. Counts, statuses, key names and the character `c` only. Drop each response body right after reading its counts.
4. Tests in the NEW `tests/test_paging_probe.py`, with a fake context and a fake poster (synthetic numbers such as `SYN-0001`): `test_probe_prints_counts_only_for_page_one_forms_and_prefixes` (the emitted lines are page1, eleven `form=` lines, 36 `prefix=` lines and `done`; a fake where only form 3 returns new rows shows `new>0` on form 3 only; the sum of the output holds no `SYN-`), `test_probe_stops_at_once_on_an_auth_refusal` (a fake answering 403 on the fifth request: `PROBE stop: HTTP 403` and no sixth request), `test_probe_closes_the_session_and_prints_no_account_number` (`main` with injected fakes calls `close()` exactly once even when the probe raises, and captured stdout holds no `SYN-`).

### ACCEPTANCE

<criterion id="FT-s-9-AC1" cell_refs="FT-s-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft9</invocation><expect>R1-FT9-OK passed=\d+</expect></criterion>
`FT-s-9-AC1` -- the three named probe tests exist and pass.

<criterion id="FT-s-9-AC2" cell_refs="FT-s-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fr6</invocation><expect>R1-FR6-OK passed=\d+</expect></criterion>
`FT-s-9-AC2` -- the lister's thirteen tests still pass (a regression guard: this cell must not touch `adapters.py`).

<expected_criteria>FT-s-9-AC1,FT-s-9-AC2</expected_criteria>

Dry-run at the base: `FT-s-9-AC1` base: FAIL as expected; `FT-s-9-AC2` base: PASS as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder.
- **Fakes only.** No network, no AWS, no live call from your tests. No G number, account number or firm label in any output.
- **Do not edit** `adapters.py`, `attribute.py`, `box/run.py` or `box/daily.py`: import from them.
- **Refusal clause.** A premise that fails is a surprise row (`NFRA_FIDUPL-D1-W5-S<k>`, next unused), never a guess.
- **ASCII and Python 3.9 syntax** in every file. The whole module suite must have no failure: its last line goes in your report.

<paths>
infra/aws/ec2/canonical-fidelity/box/paging_probe.py
infra/aws/ec2/canonical-fidelity/tests/test_paging_probe.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 8 addendum), cell `FT-s-9`.
<owned_cells>FT-s-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-9-AC1, FT-s-9-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~5/NFRA_FIDUPL.TO-FT-s-9.paging-probe.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-9-AC1,FT-s-9-AC2` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, the test names, each check line verbatim, the module suite's last line, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- fakes only; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- build on fakes; the live run is ordered separately (TO-FT-s-8, amended) under the CTO's go, one sign-in.
lane: the paths block.
</preflight>

Source: CloudOps row D1-S13; worker row D1-W5-S4; CRO research RESEARCH_20261020_NFRA_FIDUPL_ACCOUNTLIST_SHAPE.md ("Not measured").
