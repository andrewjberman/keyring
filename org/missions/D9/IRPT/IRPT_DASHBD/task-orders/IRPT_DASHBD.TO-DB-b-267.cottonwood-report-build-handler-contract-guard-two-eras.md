# TO IRPT_DASHBD.TO-DB-b-267 -- the CONTRACT GUARD of the Cottonwood report-build handler (round 135, workstream B-49F, row D2-S92): the handler reads each returns partition's manifest, chains only within ONE (contract_version, method_version), states the era it used, and a test spans 2026-06-22 and 2026-07-10

<to_id>IRPT_DASHBD.TO-DB-b-267</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~217</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>135</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 135 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_128_20261015.md ADDENDUM 2 @45b66b34e7 and row IRPT_DASHBD-D2-S92 (msg 8491) ("The consumer never chains across a contract. The report-build handler reads each partition's manifest contract and method_version, and chains only within one contract. A window that reaches before 2026-07-10 serves from the Black Diamond era only and states 'returns from July 10, 2026', or reads 'not enough history' in words. It never splices eras and never fills the gap. This is a build criterion of that handler, with a test that spans 06-22 and 07-10.") | **Decomp cell:** `DB-b-267` (decomposition section 133).

**Risk class WORLD** is the floor of the paths below (`infra/` paths): this order edits a handler and its tests and runs no AWS call and no Terraform command. The handler is the bundle's root file, so its bytes change here, BEFORE the report-build pair is written.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-217` (branch `wk-IRPT_DASHBD-217`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~217/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~217/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The table `irpt/cottonwood/gold/account_return_daily` holds two eras under one name: the Commonwealth era (3,325 dates to 2026-06-22, `method_version` 3, a manifest keyed `asof`/`firm_scope`) and the Black Diamond era (dates from 2026-07-10, `method_version` 2, a manifest carrying `business_date` and `contract_version` 0.3.0), with a 12-trading-day gap between them. A consumer that chains across them serves a spliced return. Your predecessor's handler (`infra/aws/lambda/investor-reporting/reporting-gold-cot/handler.py`, round 131) never LISTS a partition before the floor `FLOOR_DAY = "2026-07-10"`, which keeps the Commonwealth era out; the CTO rules that the guard must not rest on a date alone: it reads each used partition's manifest and refuses a mix, and the report states the era it used.

**The cell (`DB-b-267`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r135/p135_contract.py` (your three criteria; its PROBE script is the behavioural spec for this cell and it also runs every earlier clause of `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r131/p131_cothandler.py`); the current handler and its tests `infra/aws/lambda/investor-reporting/reporting-gold-cot/tests/test_reporting_gold_cot.py`; the CTO addendum and row `IRPT_DASHBD-D2-S92` named above.
2. **The handler (edit `handler.py`, ADDITIVE; every earlier behaviour and test stays).** In `_inputs`, BEFORE reading any returns data, read the `manifest.json` of EACH returns partition that the floor-limited listing keeps (the partitions at or after `FLOOR_DAY`; use the address `opal_naming.address("irpt", FIRM, "gold", frv.RET, "date=<day>", "manifest.json")` and `ad.guard(uri)` so the adapter's guard still applies, and read it through the same `_Reader`). Each manifest must carry BOTH `contract_version` and `method_version`; take the set of distinct `(str(contract_version), method_version)` pairs across the partitions: **exactly one pair, or `raise SystemExit("REFUSED: ...")` with a message that contains the word `contract`** (a manifest naming neither, or two pairs, both refuse). The refusal reaches the caller through `build_day`'s existing handler (printed `FILLED_SKIPPED`, returned as `{"day": ..., "failed": reason}`): nothing is written. A day that builds returns, besides what it returns today, `"returns_from"` (the earliest returns partition date it used, an ISO string) and `"contract"` (`{"contract_version": ..., "method_version": ...}`, the one pair). A landed day (skipped) is unchanged. The 2026-06-22 partition and its manifest must never be listed, opened or named in any call.
3. **Tests** (extend `tests/test_reporting_gold_cot.py` or add `tests/test_contract_guard.py`; `pytest` passing from the repo root; at least four NEW tests, all earlier tests still passing, still naming cottonwood only): a consistent Black Diamond era builds and its result states `returns_from` 2026-07-10 and the contract (`contract_version` "0.3.0", `method_version` 2); a returns manifest naming a different `contract_version` inside the floor window refuses with zero puts; a manifest naming no contract refuses with zero puts; and **a test that SPANS 2026-06-22 and 2026-07-10**: the fake store holds a Commonwealth partition for 2026-06-22 (its manifest has `asof` and `firm_scope`, `method_version` 3, no `contract_version`) beside the Black Diamond partitions; building 2026-07-13 never lists, opens or names a key of the 2026-06-22 partition, and, run with the REAL `frv.build_document` and `frv.to_rows` (stub only the served model series module, as the probe does), the rows whose `member_id` begins `account.window_status.` and ends `qtd`, `ytd` or `last_12_months` all read `NOT_SPANNED` (the contract's words for a window the account's data does not span), none a number.
4. **Facts record** `RD_COT_CONTRACT_GUARD_FACTS_R135.json` in your folder with EXACTLY these fields: `era_guard` ("manifest contract_version and method_version of each returns partition used; one pair or refuse"); `floor_day` ("2026-07-10"); `stated` (["returns_from", "contract"]); `windows_before_floor` ("NOT_SPANNED in words; no number is served"); `words` (one paragraph, 80 to 1800 characters: what the guard reads and refuses, what the result states, what is NOT proven: the Lambda runtime, the first real build, a literal 'returns from July 10, 2026' text row in the served report, which would be a change to the report contract and is not made here).

<criterion id="DB135-1-AC1" cell_refs="DB-b-267"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r135/p135_contract.py" . DB135-1-AC1</invocation><expect>DB135-1-AC1 PASS</expect></criterion>
`DB135-1-AC1` -- the handler's source holds every round-131 clause (import-time third party only pyarrow/boto3/botocore, no other firm, exactly one `put_object`, no delete/copy/upload call, exactly one `Event` self-invoke, `FLOOR_DAY` "2026-07-10", a `lambda_handler`) and now names `manifest.json`, `contract_version` and `method_version`; the worker's own commits touch only the handler directory, the deliverables folder, the investigation file and task-order files.
<criterion id="DB135-1-AC2" cell_refs="DB-b-267"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r135/p135_contract.py" . DB135-1-AC2</invocation><expect>DB135-1-AC2 PASS</expect></criterion>
`DB135-1-AC2` -- the checker stages the handler as packaged and runs it against a fake S3 holding a Commonwealth partition for 2026-06-22 and two Black Diamond partitions: a consistent era builds one day, puts once, states `returns_from` 2026-07-10 and `contract_version` 0.3.0 / `method_version` 2, reads each used partition's manifest and never lists or opens a 2026-06 key; a mixed contract and a manifest naming no contract each REFUSE by the word `contract` with zero puts; run with the REAL `frv.build_document` and `frv.to_rows`, the qtd, ytd and last_12_months window status of every account reads `NOT_SPANNED`.
<criterion id="DB135-1-AC3" cell_refs="DB-b-267"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r135/p135_contract.py" . DB135-1-AC3</invocation><expect>DB135-1-AC3 PASS</expect></criterion>
`DB135-1-AC3` -- the worker's tests pass under pytest and name cottonwood and no other firm; the probe passes again; the facts record has exactly the form of step 4.

<expected_criteria>DB135-1-AC1,DB135-1-AC2,DB135-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: `filled_report_values.py`, the adapters, the Terraform roots, the source map, `lib/`, the registry, the contract, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. The tests use fakes; no network, no AWS call, no S3 read or write, no Terraform command, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic (account ids like `A1`, household ids like `HH1`).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Do not change `filled_report_values.py` or the report contract; if the real build does not read `NOT_SPANNED` for an early window, record it, file a BLOCKING row and stop.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W217-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/lambda/investor-reporting/reporting-gold-cot/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~217/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-267.cottonwood-report-build-handler-contract-guard-two-eras.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 133 (round 135, workstream B-49F), cell `DB-b-267`.
<owned_cells>DB-b-267</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB135-1-AC1, DB135-1-AC2, DB135-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~217/IRPT_DASHBD.TO-DB-b-267.cottonwood-report-build-handler-contract-guard-two-eras.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB135-1-AC1,DB135-1-AC2,DB135-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the guard's reads and refusals in one line each; the test count; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a handler edit, tests and a facts record in a branch; nothing is wired to AWS, packaged, planned, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes: the manifest keys are under the account_return_daily prefix the cell-2 execution role already reads.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its probe was validated by the issuer against a scratch reference handler (green), the round-131 handler (red) and four mutants (no mixed refusal, no floor, no stated era, no unnamed refusal: three red, one equivalent), and its static, grant and facts clauses by its self-test.
lane: the <paths> block IS the grant.
</preflight>
