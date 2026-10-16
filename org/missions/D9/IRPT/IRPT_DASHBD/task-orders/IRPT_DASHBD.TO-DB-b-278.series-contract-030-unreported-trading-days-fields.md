# TO IRPT_DASHBD.TO-DB-b-278 -- the SERIES contract 0.3.0 (round 146): the carrier of the unreported-days statement, two optional fields, `unreported_trading_days` (ISO dates; always present on a series from a source that carries the statement, [] when none) and `unreported_trading_days_basis` (the fixed text), as a PAIR; every earlier series still validates

<to_id>IRPT_DASHBD.TO-DB-b-278</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~225</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>146</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F + contract, round 146 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md ADDENDUM v0.16 item 4 (CTO msg 8796) ("the unreported-days sentence has no carrier yet ... the contract field: `2.0.0_SA_COO~D2`, the contract's sole writer; ADDENDUM 2 of the workstream assignments (msg 8803): the first Cottonwood series publish is also `~D2`'s, in one drain with the field. Two fields: `unreported_trading_days` (list of ISO dates in the window); `unreported_trading_days_basis` (fixed text: 'trading calendar minus present partitions'). They are written from the report-build output's statement. An empty list is written as `[]`, never omitted.") | **Decomp cell:** `DB-b-278` (decomposition section 144).

**Risk class LOCAL**: one JSON standard and one new test file; no AWS, no deploy. The contract and its first writer (the first Cottonwood series publish, a later cell of this issuer: the CTO moved the publish to `2.0.0_SA_COO~D2`, msg 8803) land in ONE drain: the issuer drains your branch together with that writer, so do not expect it to merge the moment you finish.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-225` (branch `wk-IRPT_DASHBD-225`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~225/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~225/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The report-build handler states, for any window, the trading days the source did not report (`unreported_days`, the sentence "N trading days not reported by the source (dates)", never filled). The Performance page reads the series files, and the series contract has no field to carry that statement, so a Cottonwood series published today could not say which days it lacks. The CTO rules two fields in the series contract. They go into `series.optional`, not `series.required`, so every series written without a statement (every other firm's) still validates; on a series from a source that carries the statement they are a PAIR, always present.

**The cell (`DB-b-278`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r146/p146_series030.py` (your three criteria; its constants name the byte-identical sections and its reference validator `series_problems` is the behavioural spec); the current contract `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` (0.2.0); the publisher's tests `infra/aws/lambda/investor-reporting/reporting-publish/tests/test_publisher.py` and the portal's `portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-124.series-contract.test.ts` (both read the contract and must still pass; you edit neither); the handler `infra/aws/lambda/investor-reporting/reporting-gold-cot/handler.py` (`unreported_days`, `unreported_statement`, read only: it is where the statement comes from).
2. **The contract (edit the one JSON file, ONE commit with the test of step 3).** `contract_version` becomes `0.3.0`. `lineage` keeps its first entry byte-identical and gains a second: `{"contract_version": "0.2.0", "sha256": "2f0cb189ad07bef091269d5db9b36ccf23748c836af0fa7b3791f1df2f9764ea", "note": <one sentence: the bytes of 0.2.0 before the unreported-days fields>}` (that sha256 is the hash of the file's bytes at your base; confirm it with `sha256sum` of the file at `HEAD` before editing). `series.required`, `series.array_keys` and `series.shape` stay byte-identical. `series.optional` becomes `["class_value", "class_weight", "class_names", "unreported_trading_days", "unreported_trading_days_basis"]`. `series.fields` keeps its 16 entries byte-identical and gains two: `unreported_trading_days` = `{"kind": "scalar list of string", "source": "the report-build output's statement, its key unreported_days (the trading days from returns_from to the day per lib/trading_calendar.py, minus the returns partitions present)", "sentence": "The ISO dates (YYYY-MM-DD) of the trading days in the series' window that the source did not report, strictly increasing, each after `first_data_date`, up to `as_of` and not in `date`; always present on a series from a source that carries the report-build statement, and `[]` when there are none, never omitted; a day listed here is never filled, carried forward or treated as zero."}` and `unreported_trading_days_basis` = `{"kind": "scalar string", "source": "a fixed text", "fixed_value": "trading calendar minus present partitions", "sentence": "The fixed text 'trading calendar minus present partitions': how the list was derived (the trading calendar from `first_data_date` to `as_of`, minus the date partitions present); fixed, never free text, and present exactly when `unreported_trading_days` is."}`. A new top-level key `unreported_days_rule` holds EXACTLY these five keys, each a sentence: `present_when` ("the series' source carries the report-build statement (the Cottonwood report-build handler's unreported_days); a series from a source with no such statement carries neither field"), `pair` ("both fields or neither; a lone field is invalid"), `empty` ("[] is written when there are none, never omitted"), `window` ("each date is a trading day strictly after `first_data_date`, at or before `as_of`, and not in `date`; the list is strictly increasing"), `absent_means` ("no statement is made: the page says nothing about unreported days and never guesses"). Every other section (`manifest`, `model_windows`, `open_changes`, `files`, `change_rule`, `prd_contracts`, `source_table_contract`, `writer`, `reader`, `project`, `prd`) stays byte-identical. No publisher, reader, handler or portal file is edited.
3. **The test** `data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_030.py`, at least ten passing tests driven only by the contract file's declarations (read `fixed_value`, `series.required` and the rule's window generically; never hard-code the fixed text): an earlier series with neither field validates; a series with `[]` and the basis validates; a series with one and with two unreported days validates; a lone `unreported_trading_days` is rejected; a lone basis is rejected; a basis of other words is rejected; a null list and a string for the list are rejected; a non-ISO date is rejected; a date before `first_data_date`, after `as_of` and one that is in `date` are each rejected; duplicates and an unsorted list are rejected; and the contract invariants (version 0.3.0, the optional list, the 16 earlier fields unchanged, the lineage entry). The file defines its own small validator over a dict series and names no real account or client value.
4. **Facts record** `RD_SERIES_CONTRACT_030_FACTS_R146.json` in your folder with EXACTLY these fields: `contract_version` ("0.3.0"); `lineage_sha256` (the sha256 of step 2); `optional` (equal to the contract's `series.optional`); `fixed_value` ("trading calendar minus present partitions"); `words` (one paragraph, 80 to 1800 characters: what was added, that every earlier series still validates, that the pair is always present on a series from a source with the statement, and what is NOT proven: that any publisher writes the fields, which is the Cottonwood publish cell's, and that the page reads them).

<criterion id="DB146-1-AC1" cell_refs="DB-b-278"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r146/p146_series030.py" . DB146-1-AC1</invocation><expect>DB146-1-AC1 PASS</expect></criterion>
`DB146-1-AC1` -- the contract file holds every declaration of step 2 (the version, the lineage entry with the 0.2.0 bytes' sha256, the three series sections and the 16 earlier fields byte-identical, the optional list, the two new fields, the rule in words, every other section byte-identical) and the worker's commits change only the contract, its test, its folder, the investigation file and task-order files, the contract and the test together in ONE commit.
<criterion id="DB146-1-AC2" cell_refs="DB-b-278"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r146/p146_series030.py" . DB146-1-AC2</invocation><expect>DB146-1-AC2 PASS</expect></criterion>
`DB146-1-AC2` -- a reference validator driven only by the contract's declarations accepts four series (an earlier one, `[]` with the basis, one unreported day, two) and rejects eleven (a lone field either way, a wrong basis, a null list, a string, a non-ISO date, a date before the window, after it, one that is a present day, a duplicate, an unsorted list).
<criterion id="DB146-1-AC3" cell_refs="DB-b-278"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r146/p146_series030.py" . DB146-1-AC3</invocation><expect>DB146-1-AC3 PASS</expect></criterion>
`DB146-1-AC3` -- your new test file holds at least ten passing tests, the publisher's tests and the portal's series-contract test still pass against the new contract, and the facts record equals the contract.

<expected_criteria>DB146-1-AC1,DB146-1-AC2,DB146-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the publisher, the reader, the handler, the portal, the other contracts, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the publisher's tests or the portal's series-contract test fail once the contract reads 0.3.0, record it as a BLOCKING row and stop: those files are not in your grant.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W225-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/standards/IRPT_DASHBD_SERIES_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_030.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~225/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-278.series-contract-030-unreported-trading-days-fields.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 144 (round 146, workstream B-49F + contract), cell `DB-b-278`.
<owned_cells>DB-b-278</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB146-1-AC1, DB146-1-AC2, DB146-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~225/IRPT_DASHBD.TO-DB-b-278.series-contract-030-unreported-trading-days-fields.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB146-1-AC1,DB146-1-AC2,DB146-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the contract's changed keys in one line; the test count; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a JSON standard and a test file in a branch; nothing reads the new fields yet and no writer changes.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its clauses were validated by the issuer against a scratch reference contract (green) and 19 single-fault mutants of it (all red), and its behaviour, grant and facts clauses by the self-test.
lane: the <paths> block IS the grant.
</preflight>
