# NFRA_OPLGTW task order -- `OG-au-2` -- the rivalfunds routes record which page was served: three audit args and the size (row Z-S64)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-au-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~31</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change with tests; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS surface is read or written; the tests run offline with fakes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is the CTO's round-24 analysis (org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round24.md @0e813364da).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-au-2` (decomposition addendum R3-T.21, item 1)

`infra/aws/ec2/opal-gateway/app/audit.py` keeps, per tool, only the args named in `_ARGS_ALLOWLIST` (`_safe_args`). The
tool `rivalfunds_view` is not in it, so every rivalfunds record reads `{"_omitted": ...}`: the page, audit, archive
and chart routes write records that differ only in time, identity and outcome. Nobody can read from the record which
page was served, or how large it was.

Do:
1. In `app/audit.py`, add ONE `_ARGS_ALLOWLIST` entry: `"rivalfunds_view": {"day", "route", "fund"}`, with a comment
   saying why the three are metadata: a day is a date, a route is one of four fixed names, a fund is a public ETF
   ticker already held to `[A-Z0-9]{1,8}`. Name exactly those three keys. Change nothing else in that file.
2. In `app/rivalfunds_view.py`, make every `audit.log_call(... "rivalfunds_view" ...)` pass a `route`, one of `page`,
   `audit`, `archive`, `chart`, and make each 200 answer pass `bytes_returned=len(<the body served>)`. `log_call`
   already takes `bytes_returned`. Do not change any response, status code, header, key or cache behaviour.
3. `verdict` and `days` stay passed by the handlers and stay DROPPED by the allowlist. Do not add them to it.
4. Add `tests/test_audit_rivalfunds_args.py`, offline, with the four named tests `test_ogau2_ac01` to `test_ogau2_ac04`
   that the header of `au2.AC1.sh` lists. Read the records the handlers write through `AUDIT_PATH`; reuse the fakes of
   `app/tests/test_rivalfunds_view.py`.
5. Negative control: with the allowlist entry removed, `test_ogau2_ac01` fails. Record that run in
   `W/AU2_NEGATIVE_CONTROL.md`.
6. Run `app/tests/test_rivalfunds_view.py`, `tests/test_principal_cutover.py` and every `tests/test_audit*.py`, each in
   its own process, and state each file's totals. A test that pinned the old `_omitted` record for rivalfunds is
   updated to the new record and named in your report.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~31/`.

## 2. BOUNDS

- No release and no host act. This cell is BUILT and HELD on your branch; the issuer drains it after release r26 closes.
- Never call a live gateway, portal or Graph route. The tests are offline.
- Never print or commit an email address, tid, oid, account id, credential or token.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/audit.py
infra/aws/ec2/opal-gateway/app/rivalfunds_view.py
infra/aws/ec2/opal-gateway/app/tests/test_rivalfunds_view.py
infra/aws/ec2/opal-gateway/tests/test_audit_rivalfunds_args.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~31/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W31-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-au-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r27/checks/au2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 4 of 4; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the record keeps day, route and fund and the size; any other arg is still dropped.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-au-2.rivalfunds-audit-args.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If the criterion PASSES, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC output, the code diff, the negative control, each neighbouring test file you ran and its
   totals, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 26 (R3-T.21, item 1), cut on `ROUND_ANALYSIS.round24.md` @0e813364da section 3, the ruling on row Z-S64. That
  file numbers the ruling R36; `1.0.0_SA_CTO~O` already used R36 for the send dedupe (msg 30594), so this order cites
  the row.
- Ships in the release AFTER r26 (`OG-rl-13`, cut when r26 closes). Held on the worker branch until then.
- If another audit test file must change, the worker reports it; the issuer amends `<paths>`.
- Pre-cut 10:5xZ: `au2.AC1` FAIL (the test file is absent).

<status>complete</status>
<round>26</round>
<slot>~31</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
