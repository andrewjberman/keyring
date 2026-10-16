# TO IRPT_DASHBD.TO-DB-b-285 -- the SERIES contract 0.3.1 (round 148): `income_claim` carried to the series, `unreported_trading_days_basis` marked const with a one-line rule-24 note, and an optional manifest field `calendar_source`; every other key byte-identical

<to_id>IRPT_DASHBD.TO-DB-b-285</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~229</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>148</round>
<workstream>CONTRACT</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** CONTRACT, round 148 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_147_20261016.md @026e67f3a7 (msg 9060) and org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_146_20261016.md @a077d93eef (msg 9057) ("carried through to the series"; "mark unreported_trading_days_basis as const, with a one-line rule-24 note"; "the publish handler writes one manifest field, calendar_source") | **Decomp cell:** `DB-b-285` (decomposition section 147).

**Risk class LOCAL**: one JSON standard, one new test file and at most fourteen changed lines of the 0.3.0 test file; no AWS, no deploy, no push. The portal's mirror (`seriesContract.ts`, the iv-e-124 parity test) is `2.0.0_SA_COO~C2`'s NAMED READER CELL: do not edit or run it (the CTO's rule: an amendment never removes a failing reader test, it names the reader cell). The publisher and handler changes that WRITE these fields are a later cell.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-229` (branch `wk-IRPT_DASHBD-229`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~229/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~229/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Three rulings land in one edit of the series contract. (1) The Cottonwood series carries `income` all null (row S104); the CTO rules the claim is carried through to the series: an optional string field `income_claim` = `absent`, with the fixed reason `SOURCE_REPORTS_NO_INCOME`, present exactly when every `income` entry is null (the source contract's 0.4.4 column, DB-b-284, is the origin). (2) `unreported_trading_days_basis` has one value and no other state: it is marked `const` with a one-line rule-24 note. (3) The publish handler will state which trading calendar answered, so the manifest gains an OPTIONAL field `calendar_source` with the two values `pandas_market_calendars` and `fallback_2010_2027`.

**The cell (`DB-b-285`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p153_series031.py` (your three criteria; `check_diff` is the exact spec of what may differ from the base, `series_problems` and `manifest_problems` are the behavioural spec); `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` (0.3.0); your predecessor's test `data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_030.py`; the publisher's tests under `infra/aws/lambda/investor-reporting/reporting-publish/tests/` (they read the contract and must still pass; you edit none of them).
2. **The contract (edit the one JSON file, ONE commit with the test of step 3).** `contract_version` becomes `0.3.1`. `lineage` keeps every entry byte-identical and gains ONE at the end: `{"contract_version": "0.3.0", "sha256": <the sha256 of the 0.3.0 file's bytes at your base, from `git show`>, "note": <one sentence: the bytes of 0.3.0 before income_claim, the const mark and calendar_source>}`. In `series`: `optional` becomes the five earlier names then `"income_claim"`; `fields` keeps every entry byte-identical except `unreported_trading_days_basis`, which gains `"const": true` and `"rule24_note"` (ONE line, containing the words `one value` and `no other state`, e.g. one value, one intent: how the list was derived; no other state exists), and gains ONE new field `income_claim` = `{"kind": "scalar string", "source": <words: the source table contract's income_claim column (0.4.4), carried unchanged>, "fixed_value": "absent", "fixed_reason": "SOURCE_REPORTS_NO_INCOME", "sentence": <words, containing: present exactly when every income entry is null; the source reports no income; a null is never read as zero, filled or carried; the word income, null, never, zero>}`. `required`, `array_keys` and `shape` stay identical. A new top-level key `income_claim_rule` holds EXACTLY `present_when` (words containing `every` and `income`), `value` (words containing `absent`), `reason` (words containing the code `SOURCE_REPORTS_NO_INCOME`) and `absent_means` (words containing `no statement`). In `manifest`: a new key `optional` = `["calendar_source"]` (`required` unchanged) and `fields` gains ONE field `calendar_source` = `{"values": ["pandas_market_calendars", "fallback_2010_2027"], "sentence": <words on which trading calendar answered the unreported-day derivation, and that the fallback is the hardcoded table>}` (the sentence contains the words `calendar` and `fallback`). Every other section and key stays byte-identical. No publisher, handler, reader or portal file is edited.
3. **The test** `data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_031.py`, at least ten passing tests driven only by the contract's declarations: the version and the lineage entry; the optional list; the basis field's const and its one-line note; the `income_claim` field's declaration; the rule's keys; the manifest's optional list and the `calendar_source` values; the validator rules: all-null income needs the claim, the claim beside a number is rejected, mixed income is rejected, numeric income without a claim is valid, a claim of other words is rejected; and a manifest `calendar_source` outside its values is rejected. Synthetic only.
4. **Your predecessor's test** `test_series_contract_030.py` may need a minimal edit if it pins `contract_version` to 0.3.0 or `series.optional` to its five names: change ONLY what the 0.3.1 edit forces, at most 14 lines in all, each commented with this order's id. The publisher's tests must pass UNEDITED; the portal's parity test is not yours.
5. **Facts record** `RD_SERIES_CONTRACT_031_FACTS_R148.json` in your folder with EXACTLY these fields: `contract_version` ("0.3.1"); `lineage_sha256` (the sha256 of step 2's lineage entry); `optional` (equal to the contract's `series.optional`); `basis_const` (true); `income_claim` ({"value": "absent", "reason": "SOURCE_REPORTS_NO_INCOME"}); `manifest_optional` (["calendar_source"]); `tests` (the count of passing tests of your new file); `words` (one paragraph, 80 to 1800 characters: what was added, that every series and manifest written without the new keys still validates, and what is NOT proven: that any publisher writes the new keys, and that the page's mirror reads them, which is the reader cell's).

<criterion id="DB153-1-AC1" cell_refs="DB-b-285"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p153_series031.py" . DB153-1-AC1</invocation><expect>DB153-1-AC1 PASS</expect></criterion>
`DB153-1-AC1` -- the contract differs from the base ONLY in `contract_version`, one appended lineage entry, `series.optional` (+income_claim), the basis field's const and note, the new `income_claim` field, the top-level `income_claim_rule`, `manifest.optional` and `manifest.fields.calendar_source`; every other key is byte-identical.
<criterion id="DB153-1-AC2" cell_refs="DB-b-285"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p153_series031.py" . DB153-1-AC2</invocation><expect>DB153-1-AC2 PASS</expect></criterion>
`DB153-1-AC2` -- a reference validator driven only by the contract's declarations accepts seven documents (numeric income, all-null income with the claim, a one-day series with the claim, zero income without a claim, and a manifest with no source, either named source) and rejects eight (all-null income without the claim, the claim beside numeric or mixed income, mixed income without it, a claim of other words, a null claim, a manifest source outside its values or null).
<criterion id="DB153-1-AC3" cell_refs="DB-b-285"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p153_series031.py" . DB153-1-AC3</invocation><expect>DB153-1-AC3 PASS</expect></criterion>
`DB153-1-AC3` -- your new test file holds at least ten passing tests, the 0.3.0 test file (at most fourteen changed lines) and the publisher's tests pass against the new contract, the worker's commits change only the contract, the two test files, the folder, the investigation file and task-order files, and the facts record equals the contract. The portal's parity test is NOT run here: it is the named reader cell's.

<expected_criteria>DB153-1-AC1,DB153-1-AC2,DB153-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the publisher, the handlers, the source contract, the portal, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the publisher's tests fail once the contract reads 0.3.1, record it as a BLOCKING row and stop: those files are not in your grant.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W229-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/standards/IRPT_DASHBD_SERIES_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_031.py
data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_030.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~229/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-285.series-contract-031-income-claim-const-basis-calendar-source.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 147 (round 148, workstream CONTRACT), cell `DB-b-285`.
<owned_cells>DB-b-285</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB153-1-AC1, DB153-1-AC2, DB153-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~229/IRPT_DASHBD.TO-DB-b-285.series-contract-031-income-claim-const-basis-calendar-source.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB153-1-AC1,DB153-1-AC2,DB153-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the changed keys in one line; the test counts and the number of 0.3.0-test lines changed; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a JSON standard and test files in a branch; nothing writes or reads the new keys.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its diff, behaviour, grant and facts clauses were validated by the issuer against a reference 0.3.1 built from the real 0.3.0 contract (green) and 23 single-fault arms (all red) by the self-test.
lane: the <paths> block IS the grant.
</preflight>
