# TO IRPT_DASHBD.TO-DB-b-286 -- the CLASS PRODUCER's DATED CLASSIFICATION READ and its SUM-TO-ACCOUNT TEST (round 148): every GetItem is stamped with its run-day, `ClassTable.as_of()` answers the oldest, the day's manifest carries `class_source.as_of` and `claim: held`, the class contract 0.1.1 says so, and a new test file proves the classes sum to the account on four mutants

<to_id>IRPT_DASHBD.TO-DB-b-286</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~230</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>148</round>
<workstream>CLASS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** CLASS, round 148 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_119_20261016.md ERRATUM and ADDENDUM 1 (msgs 8827, 8918) ("~D2 adds the sum-to-account test and the dated classification read (held, as_of) to the existing module"; "the dated classification read records its own run-day as-of and a held claim, and is not tied to the swap snapshot") | **Decomp cell:** `DB-b-286` (decomposition section 148).

**Risk class WORLD** is the floor of the paths below (`infra/` and the producer bundled into a deployed function), not a statement that anything is deployed: python files, a JSON standard and tests; no AWS, no deploy, no push. The producer is bundled into the 49 Financial `reporting-gold` function; moving its code to the cloud is a LATER code-update pair of this seat's.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-230` (branch `wk-IRPT_DASHBD-230`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~230/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~230/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The account-class table (`account_class_daily`) classifies each holding by ONE live DynamoDB GetItem per ticker, with nothing recording WHEN. A reader cannot tell a classification read today from one read last week, and the contract carries no claim about it. The CTO rules the read records its own run-day as-of and a `held` claim, and is NOT tied to the swap snapshot (a different, operator-dated read path). And the acceptance "classes sum to the account on every day, by test" is covered only for the identity and the null path: no test fixes the account value independently of the class values and survives a dropped tie.

**The cell (`DB-b-286`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p154_classdated.py` (your three criteria; `check_behaviour` is the exact spec of the dating and the manifest, `UNCHANGED` lists the pure functions that keep their exact source, `MUTANTS` the four faults your tests must kill); `data/assets/scripts/gold/irpt_reporting/account_class_daily.py` (`ClassTable`, `class_contribution`, `account_day_rows`, `emit_class_day`); `data/assets/scripts/gold/irpt_reporting/tests/test_account_class_daily.py` (the existing file: it stays unedited); `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` (`emit_classes`, read; ONE call site is yours); `org/standards/IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json` (0.1.0, its `class_source`).
2. **The module.** (a) `ClassTable.__init__(self, classifier=None, clock=None)`: `clock` is a callable returning the run-day as an ISO date string; the default returns the UTC date today. (b) Every GetItem the table makes (including one that finds no item) stamps its identifier in `self.read_dates` (identifier -> ISO date) with `str(clock())`; a cached lookup NEVER re-stamps and never re-reads. (c) A new method `as_of(self, identifiers=None)` returns the OLDEST stamp over `identifiers` (default: every identifier read), None when none of them was read. (d) `emit_class_day(s3, rows, firm, day, *, upload, classification_as_of=None)`: the manifest's `class_source` keeps its three keys and gains `as_of` (= `classification_as_of`, null when not given) and `claim` (exactly the string `held`). (e) The pure functions `class_contribution`, `account_day_rows`, `classify_identifier`, `positions_by_class`, `check_class_rows`, `class_values`, `holding_identifier` and `unclassified_share` keep their EXACT source. Nothing else in the module changes.
3. **The handler.** In `emit_classes` ONLY: every `acd.emit_class_day(...)` call passes `classification_as_of=acd.default_table().as_of()`. No other line of the handler changes.
4. **The class contract** `org/standards/IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json`: `contract_version` becomes `0.1.1`; `class_source` keeps its keys byte-identical and gains exactly TWO: `as_of` (words, containing `oldest`, `GetItem`, `swap`: the oldest GetItem read date over the identifiers used, taken at run time by the producer's own read, and NOT the swap snapshot's operator date) and `claim` (exactly `held`). Every other key stays byte-identical (`schema_hash` unchanged).
5. **The test** `data/assets/scripts/gold/irpt_reporting/tests/test_account_class_dated_and_sum.py`: at least SIX passing tests. Load the module by path as the existing test file does. Tests of the SUM, with the account's values GIVEN independently of the class values (the producer's `v_t`, `v_p`, `f_t`) and a SUB-CENT residual (the class values tie to `v_t` within the half-cent tolerance but not exactly): (i) the class `market_value_eod` of an account-day sum to `v_t` to 1e-9; (ii) the class returns sum to the account return `(v_t - f_t - v_p) / v_p` on a day with a flow and a trade; (iii) a flow that is not a trade lands in `cash`; (iv) the denominator is the prior day's value (a day where `v_t` is double `v_p`); (v) a day that misses the tie is null with `CLASS_VALUES_DO_NOT_SUM_TO_ACCOUNT`; (vi) the identity over many seeded random days. These six, run ALONE, must FAIL on each of the checker's four mutants of `class_contribution` (its `MUTANTS`): that is what `DB154-1-AC2` runs. The tests of the dating are yours to add (the checker's `check_behaviour` is the minimum). Synthetic only; no real account or client value.
6. **Facts record** `RD_CLASS_DATED_FACTS_R148.json` in your folder with EXACTLY these fields: `as_of_rule` (the string `oldest GetItem read date over the identifiers used`); `claim` (`held`); `mutants_killed` (4); `tests` (the count of passing tests of your new file); `words` (one paragraph, 80 to 1800 characters: what changed, that the pure functions keep their exact source, and what is NOT proven: that the deployed function writes the date, which is a later code-update pair, and that any reader reads it).

<criterion id="DB154-1-AC1" cell_refs="DB-b-286"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p154_classdated.py" . DB154-1-AC1</invocation><expect>DB154-1-AC1 PASS</expect></criterion>
`DB154-1-AC1` -- the dating: `as_of()` is the oldest GetItem read date (an injected clock; an absent item counts; a cached get never re-stamps; none read -> None); the manifest's `class_source` carries `as_of` and `claim` `held` (null `as_of` when not given); eight pure functions keep their exact source; the handler passes the date at every `emit_class_day` call of `emit_classes`; the class contract is 0.1.1 and gains exactly `as_of` and `claim`.
<criterion id="DB154-1-AC2" cell_refs="DB-b-286"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p154_classdated.py" . DB154-1-AC2</invocation><expect>DB154-1-AC2 PASS</expect></criterion>
`DB154-1-AC2` -- MUTATION: on a copy of the repo the checker runs your new test file, which passes on the module (at least six tests) and FAILS on each of four mutants of `class_contribution` (the tie dropped, the wrong denominator, no cash flow residual, cash not made exact).
<criterion id="DB154-1-AC3" cell_refs="DB-b-286"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p154_classdated.py" . DB154-1-AC3</invocation><expect>DB154-1-AC3 PASS</expect></criterion>
`DB154-1-AC3` -- your new test file holds at least six passing tests, the existing class test file passes unedited, the worker's commits change only the module, the handler call site, the class contract, the new test, the folder, the investigation file and task-order files, and the facts record equals the recount.

<expected_criteria>DB154-1-AC1,DB154-1-AC2,DB154-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the existing class test file, the returns producer, the other handlers, the portal, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If an existing test fails after your edit, record it as a BLOCKING row and stop. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W230-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
data/assets/scripts/gold/irpt_reporting/account_class_daily.py
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
org/standards/IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/tests/test_account_class_dated_and_sum.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~230/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-286.class-producer-dated-read-and-sum-test.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 148 (round 148, workstream CLASS), cell `DB-b-286`.
<owned_cells>DB-b-286</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB154-1-AC1, DB154-1-AC2, DB154-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~230/IRPT_DASHBD.TO-DB-b-286.class-producer-dated-read-and-sum-test.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB154-1-AC1,DB154-1-AC2,DB154-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the changed names in one line; the test count; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: python files, a JSON standard and a test file in a branch; nothing is deployed, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its dating, handler, contract, grant and facts clauses were validated by the issuer against a scratch reference module, handler and contract (green) and seven single-fault mutants of the module (all red); its mutation clause against a scratch reference test file that kills all four mutants (green).
lane: the <paths> block IS the grant.
</preflight>
