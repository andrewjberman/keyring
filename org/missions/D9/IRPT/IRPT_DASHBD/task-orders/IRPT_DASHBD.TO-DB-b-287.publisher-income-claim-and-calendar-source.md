# TO IRPT_DASHBD.TO-DB-b-287 -- the PUBLISHER and the Cottonwood publish HANDLER write what series contract 0.3.1 declares (round 148): `income_claim` = absent exactly when every income entry is null, `calendar_source` in the manifest, publisher 0.3.0; the 49 Financial series byte-identical

<to_id>IRPT_DASHBD.TO-DB-b-287</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~231</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>148</round>
<workstream>PUBWRITE</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** PUBWRITE, round 148 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_147_20261016.md @026e67f3a7 (msg 9060) ("the publish handler writes one manifest field, calendar_source"; the income claim "carried through to the series") | **Decomp cell:** `DB-b-287` (decomposition section 149).

**Risk class WORLD** is the floor of the paths below (`infra/` paths), not a statement that anything is deployed: python files and tests; no AWS, no deploy, no push. The publisher and the handler are bundled into the deployed `irpt-cot-reporting-publish-lambda` (and the publisher into the 49 Financial function); moving this code to the cloud is a LATER code-update pair of this seat's. Series contract 0.3.1 and source contract 0.4.4 are on trunk.

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-16 ~08:0xZ, on the CTO's msg 9158 rulings A and B; gate limb: an existing order modified, placeholders NONE unchanged, no criterion id, cell or path change):** (1) The reason code named in this order's Why (`SOURCE_REPORTS_NO_INCOME`) is FALSE and is renamed `RETURN_METHOD_DOES_NOT_SEPARATE_INCOME` in both contracts by `DB-b-289`; YOUR code never writes a reason, only `income_claim` = `absent`, so nothing in your cell changes. (2) Your branch is HELD by the issuer and merges in ONE drain with `DB-b-289` (the CTO's one-drain rule: a contract and its writer land together); do not expect it to merge the moment you finish. (3) The publish pair's code update and the republish of the 939 series are later acts of the issuer's, not yours.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-231` (branch `wk-IRPT_DASHBD-231`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~231/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~231/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The first Cottonwood series are served (939 series, income null on every day, no claim: row S104). Series contract 0.3.1 declares the claim (`income_claim` = `absent`, fixed reason `SOURCE_REPORTS_NO_INCOME`, present exactly when every `income` entry is null) and an OPTIONAL manifest field `calendar_source` (`pandas_market_calendars` or `fallback_2010_2027`: which calendar answered the unreported-days derivation). The writer does neither yet.

**The cell (`DB-b-287`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p155_claimcal.py` (your three criteria; `check_publisher` and `check_handler_run` are the exact behavioural spec, `CHANGED_FUNCS` lists the only publisher names that may change); `infra/aws/lambda/investor-reporting/reporting-publish/publisher.py` and `.../reporting-publish-cot/handler.py` (DB-b-279 and DB-b-280's, as merged); `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` (0.3.1: `income_claim`, `income_claim_rule`, `manifest.optional`, `manifest.fields.calendar_source`); the existing tests under `infra/aws/lambda/investor-reporting/reporting-publish/tests/` and `.../reporting-publish-cot/tests/`; `lib/trading_calendar.py` (`calendar_source()`, `FALLBACK_FIRST_YEAR`, `FALLBACK_LAST_YEAR`; read only).
2. **`publisher.py` (edit ONLY `PUBLISHER_VERSION`, `build_series`, `build_manifest`, `validate_against_contract`; add new names freely; every other top-level name keeps its exact source).** `PUBLISHER_VERSION = "0.3.0"`; module constants `INCOME_CLAIM = "absent"` and `CALENDAR_SOURCES = ("pandas_market_calendars", "fallback_2010_2027")`. `build_series`: after the unreported-days pair (when present), if EVERY `income` entry is None write `income_claim` = `INCOME_CLAIM` as the LAST key; if some entries are None and some are numbers raise `PublishRefused` (a null carries its claim only when every day is null); numeric income writes no claim (the 49 Financial series stays BYTE-IDENTICAL to the base commit's on the checker's fixture). `build_manifest(account_id, firm, series, gz_len, built_at=None, calendar_source=None)`: when `calendar_source` is given and is not in `CALENDAR_SOURCES` raise `PublishRefused`; when given, append `calendar_source` as the LAST manifest key; when None the key is absent. `validate_against_contract`: the manifest's extra-key check accepts the contract's `manifest.optional` names; `calendar_source` must be one of `contract["manifest"]["fields"]["calendar_source"]["values"]`; `income_claim` must equal `INCOME_CLAIM` and be present only when every income entry is null; all-null income without the claim is a failure; mixed income is a failure.
3. **`reporting-publish-cot/handler.py`.** A function `_calendar_source()` returning `pandas_market_calendars` when `trading_calendar.calendar_source()` starts with `NYSE/pandas_market_calendars`, else `"fallback_%d_%d" % (trading_calendar.FALLBACK_FIRST_YEAR, trading_calendar.FALLBACK_LAST_YEAR)`; `build_manifest(..., calendar_source=_calendar_source())` at the one call; `_contract()` additionally refuses by name (SystemExit `REFUSED`, before any S3 call) a contract whose `series.optional` lacks `income_claim` or whose `manifest.optional` lacks `calendar_source`. The summary's 14 keys do not change. Nothing else in the handler changes.
4. **Tests.** A NEW file `infra/aws/lambda/investor-reporting/reporting-publish/tests/test_publisher_claim_calendar.py`, at least ten passing tests over synthetic rows only: the claim for all-null income (last key, after the pair), none for numeric income, a mixed income refused, the claim without the unreported pair, `calendar_source` appended last, absent when not named, refused for other words, the validator accepting the good document and rejecting the six bad ones of the checker's list and a contract that does not name the new keys. The EXISTING tests change by at most FOURTEEN lines in all, each edit commented with this order's id and forced by the new version or key (for example the `PUBLISHER_VERSION` pin in `test_publisher_unreported.py`, the manifest assertions in `reporting-publish-cot/tests/test_handler.py`); any other existing failure is a BLOCKING row. No client data.
5. **Facts record** `RD_PUBLISHER_CLAIM_CAL_FACTS_R148.json` in your folder with EXACTLY these fields: `publisher_version` ("0.3.0"); `income_claim` ({"value": "absent", "rule": "present exactly when every income entry is null"}); `manifest_optional_key` ("calendar_source"); `byte_identical_49f` (true); `tests` (the count of passing tests of your new file); `words` (one paragraph, 80 to 1800 characters: what changed, that the 49 Financial output is byte-identical, and what is NOT proven: that the deployed function writes any of it, which is a later code-update pair, and that the page reads it).

<criterion id="DB155-1-AC1" cell_refs="DB-b-287"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p155_claimcal.py" . DB155-1-AC1</invocation><expect>DB155-1-AC1 PASS</expect></criterion>
`DB155-1-AC1` -- the publisher is 0.3.0; the 49 Financial series is byte-identical to the base commit's and its manifest differs only in `publisher_version`; an all-null income writes `income_claim` absent as the last key and a mixed income is refused; `build_manifest` appends `calendar_source` last and refuses other words; the validator rejects six bad documents and a contract that does not name the new keys; every other publisher name keeps its exact source.
<criterion id="DB155-1-AC2" cell_refs="DB-b-287"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p155_claimcal.py" . DB155-1-AC2</invocation><expect>DB155-1-AC2 PASS</expect></criterion>
`DB155-1-AC2` -- on a fake S3 holding synthetic Cottonwood gold the handler stores, for each account that builds, a series with `income_claim` absent beside null income and a manifest with `calendar_source` (the calendar's own answer, and `pandas_market_calendars` when the package answers) and publisher 0.3.0; the 14 summary keys are unchanged; a contract that omits either new key refuses before any S3 call.
<criterion id="DB155-1-AC3" cell_refs="DB-b-287"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p155_claimcal.py" . DB155-1-AC3</invocation><expect>DB155-1-AC3 PASS</expect></criterion>
`DB155-1-AC3` -- your new test file holds at least ten passing tests, the existing publisher and handler tests pass with at most fourteen changed lines, the worker's commits change only the publisher, the handler, the test directories, the folder, the investigation file and task-order files, and the facts record equals the recount.

<expected_criteria>DB155-1-AC1,DB155-1-AC2,DB155-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the contracts, the gold handlers, the Terraform roots, the portal, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W231-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/lambda/investor-reporting/reporting-publish/publisher.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/
infra/aws/lambda/investor-reporting/reporting-publish-cot/handler.py
infra/aws/lambda/investor-reporting/reporting-publish-cot/tests/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~231/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-287.publisher-income-claim-and-calendar-source.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 149 (round 148, workstream PUBWRITE), cell `DB-b-287`.
<owned_cells>DB-b-287</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB155-1-AC1, DB155-1-AC2, DB155-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~231/IRPT_DASHBD.TO-DB-b-287.publisher-income-claim-and-calendar-source.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB155-1-AC1,DB155-1-AC2,DB155-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the changed names in one line; the test counts and the existing-test lines changed; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: python files and tests in a branch; nothing is deployed, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its publisher and handler clauses were validated by the issuer against a scratch reference publisher 0.3.0 and handler on a fake S3 (green) and 13 single-fault mutants (all red, one equivalent mutant noted), and its grant and facts clauses by the self-test.
lane: the <paths> block IS the grant.
</preflight>
