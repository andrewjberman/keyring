# TO IRPT_DASHBD.TO-DB-b-271 -- the HOUSEHOLDS CLAIM and COUNTS of the Cottonwood report-build handler (round 138, workstream B-49F): each filled day's object carries households_as_of and households_claim held in its schema, and each built day counts the accounts the membership drops and the households with no rows

<to_id>IRPT_DASHBD.TO-DB-b-271</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~220</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>138</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 138 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_COTTONWOOD_REPORTING_GOLD_LAMBDA_CTO_HALF.md @063567b63d question 3 (msg 8573) ("ACCEPTED, but it must carry its claim ... Each backfilled day's object carries a claim field in its manifest or schema: `households_as_of: <account_dim date>`, `households_claim: held` ('current membership applied to a past day', not measured as of that day). Each Act 3 and Act 4 after-read counts and records two sets: accounts that have a return row on the day but are absent from the newest `account_dim` (dropped by the membership); households in `account_dim` that have no account return row on the day. Both are counts, with ids in the private record only. They are never silently dropped.") | **Decomp cell:** `DB-b-271` (decomposition section 136).

**Risk class WORLD** is the floor of the paths below (`infra/` paths): this order edits a handler and its tests and runs no AWS call and no Terraform command. It follows round 137 (the same file, merged): your base already holds the unreported-day statement. The handler's bytes change here, so the report-build never-widen packet is re-pinned after this order merges.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-220` (branch `wk-IRPT_DASHBD-220`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~220/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~220/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The backfill builds every past day on TODAY's household membership (the newest `account_dim` partition; the table holds one, so there is no membership as of the day). The CTO accepts that only if each day says so and the loss is counted, never silent.

**The cell (`DB-b-271`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r138/p138_households.py` (your three criteria; its PROBE is the behavioural spec for this cell and it also runs every clause of rounds 135 and 137); the current handler `infra/aws/lambda/investor-reporting/reporting-gold-cot/handler.py` (`build_day`, `_day_rows`, `_parquet_bytes`) and its tests; `data/assets/scripts/gold/irpt_reporting/filled_report_values.py` (`date_partitions`, `read_partition`, `select_households`).
2. **The handler (edit `handler.py`, ADDITIVE; every earlier behaviour and test stays; no new import, no new environment variable, no new S3 call kind: GET and LIST only, one `put_object` per day as before).** In `build_day`, after the rows exist and BEFORE the put, compute four values and add them to a built day's result (also on a dry run):
   - `households_as_of`: the ISO date of the NEWEST `account_dim` partition the handler's households came from (`ad.gold_prefix("account_dim")` and `frv.date_partitions(reader, bucket, prefix)`, the maximum date);
   - `households_claim`: exactly the string `held`;
   - `accounts_dropped`: the count of distinct accounts that have a row in the built day's own returns partition (read through the reader with `frv.read_partition(reader, ad, frv.RET, day, ["account_id"])`) and are absent from the households' accounts (`inp["accounts"]`);
   - `households_no_rows`: the count of households in `inp["groups"]` that have no account present on the day (`len(inp["groups"])` minus the number of households that built rows).
   The day's ONE object carries the two claim values in its parquet SCHEMA METADATA, under the keys `households_as_of` and `households_claim` (`Table.replace_schema_metadata` in `_parquet_bytes`), and its columns stay exactly `frv.COLUMNS`, in order. The printed line for a built day also states the two counts. **No account id, household id or client value is printed, returned or put in any metadata: counts only.** A landed day (skipped) is unchanged.
3. **Tests** (extend `tests/test_reporting_gold_cot.py` or add `tests/test_households_claim.py`; `pytest` passing from the repo root; at least five NEW tests, all earlier tests still passing, still naming cottonwood only): the standard day states the newest `account_dim` date, `held`, 0 dropped and 1 household with no rows, and its object's schema metadata holds both claim keys with its columns unchanged; a returns partition holding two accounts that no household has gives `accounts_dropped` 2; two `account_dim` partitions give the NEWER date; a dry run states the four keys and puts nothing; no fake id appears in anything the handler printed or returned (capture stdout).
4. **Facts record** `RD_COT_HOUSEHOLDS_CLAIM_FACTS_R138.json` in your folder with EXACTLY these fields: `claim_location` (exactly "parquet schema metadata of the day's one object"); `claim_keys` (["households_as_of", "households_claim"]); `counts` (["accounts_dropped", "households_no_rows"]); `claim` ("held"); `words` (one paragraph, 80 to 1800 characters: what the day carries and counts, that ids never leave the handler, and what is NOT proven: the Lambda runtime, the first real build, and how any page prints the claim, which is a reader's change and not made here).

<criterion id="DB138-1-AC1" cell_refs="DB-b-271"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r138/p138_households.py" . DB138-1-AC1</invocation><expect>DB138-1-AC1 PASS</expect></criterion>
`DB138-1-AC1` -- the handler's source holds every round-137 clause and now holds the words `households_as_of`, `households_claim`, `accounts_dropped` and `households_no_rows`; the worker's own commits touch only the handler directory, the deliverables folder, the investigation file and task-order files.
<criterion id="DB138-1-AC2" cell_refs="DB-b-271"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r138/p138_households.py" . DB138-1-AC2</invocation><expect>DB138-1-AC2 PASS</expect></criterion>
`DB138-1-AC2` -- the checker stages the handler as packaged and runs it against a fake S3: every round-137 scenario still passes; the standard day's one object carries `households_as_of` (the newest `account_dim` date) and `households_claim` held in its parquet schema metadata with its columns unchanged, and its result states both plus `accounts_dropped` 0 and `households_no_rows` 1; a returns partition with two accounts outside every household counts 2 dropped; two `account_dim` partitions give the newer date; a dry run states the four keys and puts nothing; none of the fake account or household ids appears in the printed output or the result.
<criterion id="DB138-1-AC3" cell_refs="DB-b-271"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r138/p138_households.py" . DB138-1-AC3</invocation><expect>DB138-1-AC3 PASS</expect></criterion>
`DB138-1-AC3` -- the worker's tests pass under pytest and name cottonwood and no other firm; the probe passes again; the facts record has exactly the form of step 4.

<expected_criteria>DB138-1-AC1,DB138-1-AC2,DB138-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: `filled_report_values.py`, the adapters, the Terraform roots, the source map, `lib/`, the registry, the contracts, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. The tests use fakes; no network, no AWS call, no S3 read or write, no Terraform command, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic (account ids like `A1`, household ids like `HH1`).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If `frv.read_partition` or `frv.date_partitions` does not behave as this order says, record it, file a BLOCKING row and stop.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W220-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/lambda/investor-reporting/reporting-gold-cot/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~220/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-271.cottonwood-report-build-handler-households-claim-and-counts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 136 (round 138, workstream B-49F), cell `DB-b-271`.
<owned_cells>DB-b-271</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB138-1-AC1, DB138-1-AC2, DB138-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~220/IRPT_DASHBD.TO-DB-b-271.cottonwood-report-build-handler-households-claim-and-counts.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB138-1-AC1,DB138-1-AC2,DB138-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; what the day carries and counts in one line each; the test count; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a handler edit, tests and a facts record in a branch; nothing is wired to AWS, packaged, planned, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes: the handler reads one more object it is already granted (the day's own returns partition) and the account_dim listing it already holds.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its probe was validated by the issuer against a scratch reference handler (green) and seven single-fault mutants of it (all red), and its static, grant and facts clauses by the self-test.
lane: the <paths> block IS the grant.
</preflight>
