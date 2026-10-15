# TO IRPT_DASHBD.TO-DB-b-269 -- the UNREPORTED-DAY STATEMENT of the Cottonwood report-build handler (round 137, workstream B-49F): the handler derives the trading days the source did not report and states them beside any window that holds one, never filling a day

<to_id>IRPT_DASHBD.TO-DB-b-269</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~218</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>137</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 137 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUNDS_130_131_132_20261015.md ADDENDUM 1 @3204c9ab6d (msg 8524) ("The handler derives the unreported days itself: the trading calendar (`lib/trading_calendar.py`) minus the Black Diamond-era partitions present. For any window holding one or more such days, it states 'N trading days not reported by the source (dates)' beside the figure. The return is never filled. This takes no write, no IAM grant and no redeploy ... the unreported-day count with a test spanning 08-19.") | **Decomp cell:** `DB-b-269` (decomposition section 135).

**Risk class WORLD** is the floor of the paths below (`infra/` paths): this order edits a handler and its tests and runs no AWS call and no Terraform command. It follows the contract guard of round 135 (the same file, now merged): your base already holds it.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-218` (branch `wk-IRPT_DASHBD-218`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~218/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~218/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Three trading days (2026-08-19, 2026-09-24, 2026-09-25) have no Black Diamond gold partition because the source holds no flows for them: a window that compounds across one lacks that day's return. The CTO rules that no sidecar row is written (the sidecar is a Commonwealth-era table, so a Black Diamond row there repeats the two-contract defect). The handler states the gap itself and never fills it.

**The cell (`DB-b-269`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r137/p137_unreported.py` (your three criteria; its PROBE is the behavioural spec for this cell and it also runs every clause of round 135, `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r135/p135_contract.py`); the current handler `infra/aws/lambda/investor-reporting/reporting-gold-cot/handler.py` and its tests in that folder; `lib/trading_calendar.py` (`trading_days_between`); `data/assets/scripts/gold/irpt_reporting/filled_report_values.py` `window_start`.
2. **The handler (edit `handler.py`, ADDITIVE; every earlier behaviour and test stays).** When it builds a day, compute `unreported_days`: the trading days from `returns_from` (the earliest returns partition used, already in the guard) up to and including the day being built, per `lib/trading_calendar.py` `trading_days_between`, MINUS the dates of the returns partitions that are present (the listing the handler already holds, kept at or after `FLOOR_DAY`). Sorted ISO strings. Then the built day's result gains three keys: `"unreported_days"` (that list); `"statement"` (`None` when the list is empty, otherwise exactly `"%d trading days not reported by the source (%s)"` with the count and the dates joined by `", "`, e.g. `1 trading days not reported by the source (2026-08-19)`: the count word is always `trading days`, never singularised); `"windows"` (a dict with exactly the keys `qtd`, `ytd`, `last_12_months`, `since_inception`, each the sub-list of `unreported_days` that falls inside that window: a day belongs to a window when it is on or after the window's start, where `qtd`, `ytd` and `last_12_months` take `frv.window_start(name, <the day as a date>)` and `since_inception` takes `returns_from`). The handler NEVER fills a day: the absent day is never listed from the store, never read, never written, and the day's output is still ONE `put_object` at the same key as before. No write, no new grant, no new import, no new environment variable. A landed day (skipped) is unchanged.
3. **Tests** (extend `tests/test_reporting_gold_cot.py` or add `tests/test_unreported_days.py`; `pytest` passing from the repo root; at least four NEW tests, all earlier tests still passing, still naming cottonwood only): **a test that SPANS 2026-08-19**: a fake store holding every Black Diamond returns partition from 2026-07-10 to 2026-08-24 EXCEPT 2026-08-19, building 2026-08-21, lists exactly `["2026-08-19"]`, states `1 trading days not reported by the source (2026-08-19)`, lists the day in all four windows, and never lists, reads or writes a key of `date=2026-08-19`; a day built BEFORE the gap (2026-08-18) states none (`[]`, `None`, empty windows); a gap on 2026-07-14 with the day 2026-10-02 lists the gap in `ytd`, `last_12_months` and `since_inception` and NOT in `qtd`; and two gaps (for example 2026-08-19 and 2026-09-24, built at 2026-09-28) state the count `2` and both dates in order.
4. **Facts record** `RD_COT_UNREPORTED_FACTS_R137.json` in your folder with EXACTLY these fields: `rule` (exactly "the trading calendar from the era's first day to the day, minus the present Black Diamond returns partitions"); `statement_form` (exactly "N trading days not reported by the source (dates)"); `windows` (["qtd", "ytd", "last_12_months", "since_inception"]); `fills` ("never"); `words` (one paragraph, 80 to 1800 characters: what the handler derives and states, what it never does, and what is NOT proven: the Lambda runtime, the first real build, and how the served report prints the statement, a report-contract change that is not made here).

<criterion id="DB137-1-AC1" cell_refs="DB-b-269"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r137/p137_unreported.py" . DB137-1-AC1</invocation><expect>DB137-1-AC1 PASS</expect></criterion>
`DB137-1-AC1` -- the handler's source holds every round-135 clause and now holds the words `trading days not reported by the source`; the worker's own commits touch only the handler directory, the deliverables folder, the investigation file and task-order files.
<criterion id="DB137-1-AC2" cell_refs="DB-b-269"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r137/p137_unreported.py" . DB137-1-AC2</invocation><expect>DB137-1-AC2 PASS</expect></criterion>
`DB137-1-AC2` -- the checker stages the handler as packaged and runs it against a fake S3: every round-135 scenario still passes; a gap on 2026-08-19 in the middle of a landed run gives `unreported_days` exactly `["2026-08-19"]`, the statement `1 trading days not reported by the source (2026-08-19)`, the day in all four windows, no list, read or write of the absent day and one put at the right key; a day before the gap states none; a gap before a later quarter's start is not listed in the quarter-to-date window.
<criterion id="DB137-1-AC3" cell_refs="DB-b-269"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r137/p137_unreported.py" . DB137-1-AC3</invocation><expect>DB137-1-AC3 PASS</expect></criterion>
`DB137-1-AC3` -- the worker's tests pass under pytest and name cottonwood and no other firm; the probe passes again; the facts record has exactly the form of step 4.

<expected_criteria>DB137-1-AC1,DB137-1-AC2,DB137-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: `filled_report_values.py`, the adapters, the Terraform roots, the source map, `lib/`, the registry, the contract, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. The tests use fakes; no network, no AWS call, no S3 read or write, no Terraform command, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic (account ids like `A1`, household ids like `HH1`).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If `frv.window_start` or `trading_days_between` does not behave as this order says, record it, file a BLOCKING row and stop.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W218-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/lambda/investor-reporting/reporting-gold-cot/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~218/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-269.cottonwood-report-build-handler-unreported-trading-days-statement.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 135 (round 137, workstream B-49F), cell `DB-b-269`.
<owned_cells>DB-b-269</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB137-1-AC1, DB137-1-AC2, DB137-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~218/IRPT_DASHBD.TO-DB-b-269.cottonwood-report-build-handler-unreported-trading-days-statement.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB137-1-AC1,DB137-1-AC2,DB137-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; what the handler derives and states in one line each; the test count; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a handler edit, tests and a facts record in a branch; nothing is wired to AWS, packaged, planned, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes: the handler reads the same listing it already holds.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its probe was validated by the issuer against a scratch reference handler (green), the round-135 handler (red) and 15 arms of its self-test, and its static, grant and facts clauses by the self-test.
lane: the <paths> block IS the grant.
</preflight>
