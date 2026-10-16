# TO IRPT_DASHBD.TO-DB-b-279 -- the PUBLISHER's pure functions for the first Cottonwood series (round 147): `build_series` writes the series contract 0.3.0's unreported-days pair when it is given the present partition dates and a trading calendar, and writes `income` as the gold column stands (null stays null); `validate_against_contract` grades the pair; the 49 Financial path stays byte-identical

<to_id>IRPT_DASHBD.TO-DB-b-279</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~226</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>147</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F + contract, round 147 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md ADDENDUM v0.16 item 4 and the CTO boundary ruling msg 8803 ("~D2 owns handler.py, publisher.py, the publish tf root and the sources entry. The first Cottonwood series publish is ~D2's cell, under its own pair and in one drain with the contract field.") | **Decomp cell:** `DB-b-279` (decomposition section 145).

**Risk class WORLD** is the floor of the paths below (an `infra/` path), not a statement that anything is deployed: one python module and one new test file; no AWS, no deploy, no push. Nothing is served: the module is read by the 49 Financial function today and by the Cottonwood function (cell `DB-b-280`) later, and neither is changed to run it by this order.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-226` (branch `wk-IRPT_DASHBD-226`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~226/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~226/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The Cottonwood series needs two things the publisher cannot do today. (1) The series contract 0.3.0 (built, HELD on branch `wk-IRPT_DASHBD-225`, not merged: do NOT merge it) carries two optional fields, `unreported_trading_days` (the ISO dates of the trading days in the series' window that the source did not report) and `unreported_trading_days_basis` (the fixed text "trading calendar minus present partitions"), always both or neither. (2) The Cottonwood gold rows carry `income_received` null on every row (the Black Diamond-computed method separates no income; row IRPT_DASHBD-D2-S104), and `build_series` refuses a null income today. The 0.3.0 contract makes the `income` array number-or-null, null exactly where the gold row is null. Your edit is the publisher's side of both, with the 49 Financial output unchanged to the byte.

**The cell (`DB-b-279`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p147_publisher.py` (your three criteria; its fixtures and its `check_unchanged` rule are the behavioural spec); `infra/aws/lambda/investor-reporting/reporting-publish/publisher.py`; its tests under `infra/aws/lambda/investor-reporting/reporting-publish/tests/`; `lib/trading_calendar.py` (`trading_days_between`, inclusive of both ends; read only); `infra/aws/lambda/investor-reporting/reporting-gold-cot/handler.py` lines of `unreported_days` (read only: the same arithmetic over the report-build's returns partitions).
2. **Edit `publisher.py` ONLY, in exactly these places** (the checker compares the source of EVERY other top-level name to the base commit `df2468cbc8`; `PUBLISHER_VERSION`, `build_series` and `validate_against_contract` are the three that may change; new names may be added):
   - `PUBLISHER_VERSION = "0.2.0"`.
   - Two new module constants next to it: `UNREPORTED_BASIS = "trading calendar minus present partitions"` and `UNREPORTED_KEYS = ("unreported_trading_days", "unreported_trading_days_basis")`.
   - A new pure function `unreported_days(first, as_of, present_dates, calendar)` returning the sorted ISO strings of the days `d` that `calendar.trading_days_between(date(first), date(as_of))` returns, with `first < d <= as_of` (strictly after `first`, up to and including `as_of`) and `d` not among `present_dates`.
   - `build_series(rows, present_dates=None, calendar=None)`: (a) `income` is appended as `_num(r["income_received"])` (a null stays None; it is NEVER turned into 0.0; `external_flow` and `market_value_eod` stay required and still refuse a null); (b) when `present_dates` is not None: if `calendar` is None raise `PublishRefused`; else add, AFTER `drawdown_episodes` and in this order, `unreported_trading_days` = `unreported_days(first_data_date, as_of, present_dates, calendar)` (`[]` when there are none, never omitted) and `unreported_trading_days_basis` = `UNREPORTED_BASIS`; (c) when `present_dates` is None neither key is added and the document is exactly today's.
   - `validate_against_contract(series, manifest, contract)`: keep every existing check and add, for a series that carries either key: both or neither (a lone field is a failure); the basis equals the contract's `series.fields.unreported_trading_days_basis.fixed_value` when the contract declares it, else `UNREPORTED_BASIS`; the list is a list of ISO date strings, strictly increasing, each strictly after `first_data_date`, at most `as_of`, and none of them a day in `date`. A contract whose `series.optional` does not name the two keys must still reject a series that carries them (the existing "keys the contract does not name" check already does; keep it).
   - No edit to `handler.py`, to any existing test, to the contract, to the portal or to any other file. If an existing test fails after your edit, that is a BLOCKING row and you stop.
3. **The new test file** `infra/aws/lambda/investor-reporting/reporting-publish/tests/test_publisher_unreported.py`, at least twelve passing tests over synthetic rows only: the unreported list for a window with a missing day in the middle, one before `first_data_date` (not listed), one after `as_of` (not listed), and `first_data_date` and `as_of` themselves (never listed when present, `as_of` listed when its partition is absent); `[]` written and the basis written when there are none; the pair absent when `present_dates` is None; `present_dates` without a calendar refused; income null stays null and a non-null income stays a number; a null `external_flow` and a null `market_value_eod` still refused; equal input gives equal bytes; the 49 Financial fixture gives the same document with and without the new arguments left out; and the validator accepting the good document and rejecting a lone field, a wrong basis, a non-ISO date, an unsorted list, a date outside the window and a present day. Name no real account or client value.
4. **Facts record** `RD_PUBLISHER_UNREPORTED_FACTS_R147.json` in your folder with EXACTLY these fields: `publisher_version` ("0.2.0"); `build_series_signature` (the string `str(inspect.signature(build_series))`); `basis` (the fixed text); `byte_identical_49f` (true); `tests` ({"new": the count of passing tests of your file, "existing": the count of passing tests of the other files in that tests directory}); `words` (one paragraph, 80 to 1800 characters: what changed, that the 49 Financial output is byte-identical, and what is NOT proven: that any function writes the Cottonwood series, which is `DB-b-280` and then a pair-gated run).

<criterion id="DB147-1-AC1" cell_refs="DB-b-279"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p147_publisher.py" . DB147-1-AC1</invocation><expect>DB147-1-AC1 PASS</expect></criterion>
`DB147-1-AC1` -- the 49 Financial series is byte-identical to the base commit's on a synthetic fixture, the manifest differs only in `publisher_version` (0.2.0), the three refusals stand, every top-level name of the base other than the three allowed keeps its exact source, and the module still holds its summary and filled-report functions.
<criterion id="DB147-1-AC2" cell_refs="DB-b-279"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p147_publisher.py" . DB147-1-AC2</invocation><expect>DB147-1-AC2 PASS</expect></criterion>
`DB147-1-AC2` -- on a synthetic Cottonwood-shaped frame the income array stays null, the unreported list is the calendar over (first_data_date, as_of] minus the present partitions, the pair follows `drawdown_episodes`, `[]` is written when none, the pair is absent without `present_dates`, and the validator accepts the good document and rejects nine bad ones.
<criterion id="DB147-1-AC3" cell_refs="DB-b-279"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p147_publisher.py" . DB147-1-AC3</invocation><expect>DB147-1-AC3 PASS</expect></criterion>
`DB147-1-AC3` -- your new test file holds at least twelve passing tests, the module's existing tests pass beside it, the worker's commits change only the publisher, the new test file, the folder, the investigation file and task-order files, and the facts record equals the recount.

<expected_criteria>DB147-1-AC1,DB147-1-AC2,DB147-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: `handler.py`, the existing tests, the contract (its 0.3.0 form is HELD on another branch), the portal, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W226-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/lambda/investor-reporting/reporting-publish/publisher.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_publisher_unreported.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~226/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-279.publisher-unreported-days-and-nullable-income.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 145 (round 147, workstream B-49F + contract), cell `DB-b-279`.
<owned_cells>DB-b-279</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB147-1-AC1, DB147-1-AC2, DB147-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~226/IRPT_DASHBD.TO-DB-b-279.publisher-unreported-days-and-nullable-income.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB147-1-AC1,DB147-1-AC2,DB147-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the three changed names in one line; the test counts; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a python module and a test file in a branch; nothing is deployed, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its clauses were validated by the issuer against a scratch reference publisher (green) and 16 single-fault mutants of it (all red), and its test, grant and facts clauses by the self-test.
lane: the <paths> block IS the grant.
</preflight>
