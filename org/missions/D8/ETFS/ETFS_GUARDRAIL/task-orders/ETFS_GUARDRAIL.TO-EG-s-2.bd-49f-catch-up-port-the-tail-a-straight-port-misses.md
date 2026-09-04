# TO ETFS_GUARDRAIL.TO-EG-s-2 -- bd-49f-etf-ownership-daily: the catch-up PORTED in on the REPORTING-OBLIGATION window -- the one property a straight port fails while passing review is the 12-13 day tail, and it is tested here; a non-writing PROBE mode; deployed through Terraform under a ledger entry

<to_id>ETFS_GUARDRAIL.TO-EG-s-2</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO paired at cut (the spawn IS the GO); in your queue after EG-s-1; premise-bound to EG-s-11's WRITER determination (your earlier order). Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance (s.6a: the probe); Andrew-direct 2026-09-01 and 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S2; s.6 rulings 1 and 2; s.4 properties 1 and 2 -- "Property 2 is the one that matters"; brief s.3 the lag table) | **Decomp cell:** `EG-s-2` | **outcome_ref:** FWD-1 | **verb:** port | **depends_on:** `EG-s-3`, `EG-s-10`, `EG-s-11` (all earlier in your queue or slot 1's, merged before this hand-off)

---

## THE CELL

`EG-s-2` (PRD s.7.2 S2): `infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/lambda_function.py` (122 lines at HEAD), claim MEASURED (0 catch-up hits / 122 lines). Bound: *"49F tail 12-13 d exceeds the shipped 10-d constant; a straight port passes review and fails property 2."* Property 2: *"A partner day whose upstream does not arrive until 12-13 days late is still caught up."* The brief's lag table: 49 Financial mostly 1-5 d, tail at 6, 7, 8, **12, 13**; *"Schwab is ad-hoc-batch, so the tail is not bounded by anything we control -- do not pick a number."* Ruling 1 (the reporting-obligation window) is the build value; ruling 2 the shipped-signal terminus.

**PREMISE, from `EG-s-11` (your earlier order):** this order is cut against `bd-49f-etf-ownership-daily` as the served writer. Read your own `which-49f-twin-writes-the-served-slices.result.md` FIRST: if `WRITER=` named the `-canonical` twin or was UNDETERMINED, do NOT edit -- file a BLOCKING row on this order's premise and stop (the issuer re-addresses). The `-canonical` twin is never edited by this order in any case.

**The producer as it is** (read it whole; 122 lines): a REVIVAL shell (2026-07-29) around the DS-owned module `backfill_49f_daily_from_monolith_rps.py` vendored VERBATIM beside it (sha256-identical to `data/etfs/scripts/backfill/backfill_49f_daily_from_monolith_rps.py` at HEAD; **ONE-PRODUCER LAW: never edit the copy**); `list_rps_partitions(s3, start, end)`, `compute_slice(s3, universe, day) -> (rows, diag)`, `load_universe(s3)`, constants `ASSETS_BUCKET`, `RPS_PREFIX = schwab/08242234/silver/fact_rps` (49F's OWN data in the monolith; NEVER#2 cleared for this read, CTO 013139Z); the shell's guard at `:89-95` (`diag["rows"] == 0` -> NO slice, `skipped-empty-source`) is the uniform ZERO-vs-MISSING contract for this producer -- TOUCHED BUT MUST NOT CHANGE. Env: `ETFS_BUCKET`, `OUTPUT_PREFIX = daily/49financial/`. Module-deployed via `infra/aws/terraform/bd-pipeline/bd-49f-etf-ownership-daily.tf` (yang-lambda, `artifact_key = bd-pipeline/bd-49f-etf-ownership-daily.zip`, `python3.11`, `local.pandas_layer`), source map `files: ["lambda_function.py", "backfill_49f_daily_from_monolith_rps.py"]`, pipeline `bd-pipeline`. Scheduled floor `cron(45 10 * * ? *)` daily incl. weekends.

**What you build (the port contract from `EG-s-3`, the same shape as `EG-s-1` which you just did):** in the SHELL only -- `_output_exists(d)`, `_partition_exists(d)` (head_object on `<RPS_PREFIX>/date=<d>/data.parquet`), `_report_shipped(month)`, `_window_dates(today)` (trading days via the vendored `trading_calendar.py`; prior month's 1st while its report is not shipped, else the current month's 1st; through yesterday UTC), `_catchup_missing_dates(universe, skip_date)` with the three skips, the non-fatal per-date try/except, the `CATCHUP:`/`CATCHUP-SKIP:` lines and the `catchup_processed`/`catchup_failed`/`catchup_skipped_empty_source` return keys; the scheduled run = latest partition then the catch-up. The PROBE mode `{"date": d, "probe": true}` -> `{"status": "probe", "date": d, "partition": bool, "priced": int, "output_exists": bool}` where `priced` = `diag["rows"]` from `compute_slice` when the partition exists (no write reachable). Vendor `trading_calendar.py` byte-identical from `lib/`, add it to the source map `files`; the one Sid `ReadShippedSignal` (`s3:GetObject` on `arn:aws:s3:::opal-data-etfs/platinum/reports/*/etf_ownership.pdf`) in the role policy. The test `test_catchup_window.py` beside the shell (not packaged; ZERO AWS calls) with the same eight arms as `EG-s-1`'s PLUS the arm that matters: (i) THE TAIL -- a partition for day D that appears only on D+13, with today = D+14, inside a window whose prior-month report is not shipped -> D is returned and processed; and (j) the same fixture with the source's `CATCHUP_WINDOW_DAYS = 10` semantics simulated -> D would NOT have been found (the negative control that shows the test can tell the two designs apart). The deploy sequence exactly as in `EG-s-1` with `bd-pipeline` / `bd-49f-etf-ownership-daily` and the ledger slug `etfs-guardrail-eg-s-2-bd49f-catchup-port`.

## DELIVERABLE

The shell, the test, the vendored calendar, the source map update, the IAM Sid, the ledger entry (committed), and `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/bd-49f-catch-up-port-the-tail-a-straight-port-misses.result.md` -- criteria verbatim with rc and denominators; the plan summary; the hash pair; the probe output.

## ACCEPTANCE

<criterion id="S2-AC1" cell_refs="EG-s-2"><invocation>python -m pytest infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/test_catchup_window.py -q</invocation><expect>passed</expect></criterion>
`S2-AC1` -- the ten-arm battery is green, the tail arm (i) and its negative control (j) included (record N passed).

<criterion id="S2-AC2" cell_refs="EG-s-2"><invocation>python -c "s=open('infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/lambda_function.py').read(); print('DAYCOUNT_WINDOW=%s SHIPPED_SIGNAL=%s PROBE=%s EMPTY_SOURCE_GUARD=%s' % ('CATCHUP_WINDOW_DAYS' in s, 'etf_ownership.pdf' in s, '\"probe\"' in s, 'skipped-empty-source' in s))"</invocation><expect>DAYCOUNT_WINDOW=False SHIPPED_SIGNAL=True PROBE=True EMPTY_SOURCE_GUARD=True</expect></criterion>
`S2-AC2` -- no day-count constant; the shipped signal; the probe; the contract guard survives.

<criterion id="S2-AC3" cell_refs="EG-s-2"><invocation>python -c "import hashlib; f=lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest(); print('CAL_VENDORED_IDENTICAL=%s DS_MODULE_UNTOUCHED=%s' % (f('lib/trading_calendar.py')==f('infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/trading_calendar.py'), f('data/etfs/scripts/backfill/backfill_49f_daily_from_monolith_rps.py')==f('infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/backfill_49f_daily_from_monolith_rps.py')))"</invocation><expect>CAL_VENDORED_IDENTICAL=True DS_MODULE_UNTOUCHED=True</expect></criterion>
`S2-AC3` -- the vendored calendar is byte-identical to the library AND the vendored DS module is byte-identical to its source (the one-producer law as a property of the bytes).

<criterion id="S2-AC4" cell_refs="EG-s-2"><invocation>bash .tools/commit-gate.sh infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/lambda_function.py infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/test_catchup_window.py</invocation><expect>pre-commit gate clean</expect></criterion>
`S2-AC4` -- the commit gate is clean.

<criterion id="S2-AC5" cell_refs="EG-s-2"><invocation>.tools/terraform.exe -chdir=infra/aws/terraform/bd-pipeline plan -no-color -input=false -lock=false</invocation><expect>to change</expect></criterion>
`S2-AC5` -- the plan changes this Lambda (new artifact version) and its role policy (the one Sid) and NOTHING ELSE. `bd-pipeline` is a wide directory: a plan naming any other resource is NOT applied -- BLOCKING row -- and you may narrow the apply with `-target` ONLY to the two addresses the plan showed for this function, stating the target in the ledger entry.

<criterion id="S2-AC6" cell_refs="EG-s-2"><invocation>.tools/terraform.exe -chdir=infra/aws/terraform/bd-pipeline plan -no-color -input=false -lock=false -detailed-exitcode; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`S2-AC6` -- 0-diff after the apply (if the directory carried foreign drift before you started and you applied by target, record the pre-existing drift verbatim as the honest output and file a row naming it; the criterion then reads as it reads).

<criterion id="S2-AC7" cell_refs="EG-s-2"><invocation>python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/bd49f_served_vs_built.py</invocation><expect>VERDICT: MATCH</expect></criterion>
`S2-AC7` -- served `CodeSha256` equals the uploaded artifact's `artifact_sha256`.

<criterion id="S2-AC8" cell_refs="EG-s-2"><invocation>.tools/aws lambda invoke --function-name bd-49f-etf-ownership-daily --payload "{\"date\":\"2026-08-04\",\"probe\":true}" /dev/stdout</invocation><expect>"partition": true</expect></criterion>
`S2-AC8` -- the deployed PROBE answers for 2026-08-04 without writing (record `priced` and `output_exists`).

<criterion id="S2-AC9" cell_refs="EG-s-2" judgment="true"/>
`S2-AC9` -- graded by the CVO at L9: the tail arm proves the window catches a 13-day-late partition and its negative control proves the old constant would not have; no day count is re-proposed; the DS module is untouched; FWD-1's EXERCISED grade is a real recovered date on a scheduled fire, not manufactured here. RECORD; NO VERDICT.

<expected_criteria>S2-AC1, S2-AC2, S2-AC3, S2-AC4, S2-AC5, S2-AC6, S2-AC7, S2-AC8, S2-AC9</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below and nothing else.** A path you need that it does not name is a BLOCKING row, never an override. The `-canonical` twin and the DS module are NOT edited.
- **NEVER#1 / NEVER#2:** this producer reads `schwab/08242234/silver/fact_rps/*` ONLY (49F's own data; the Sid stays scoped to `fact_rps/*` exactly); the new Sid is on the aggregation bucket's `platinum/reports/` key; nothing on `opal-data-bd`, `opal-data-cot`, `opal-data-inf` or `blackdiamond/`.
- **NO SERVED DELETE, NO FABRICATION, no dated non-probe invoke in this order** (it writes; overwrite-per-date is the AVGCAP per-day invariant and a scheduled floor exists).
- **NEVER-2 / NEVER-9:** `.tools/safe-apply.sh` only; ledger before/after; plan read before apply; 0-diff after; artifact upload before the plan.
- **EVERY invocation is bounded.** `timeout 120`.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W2-S<k>`.
- **NEVER `git push`.** Report push state as MEASURED.

<paths>
infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/
infra/aws/terraform/bd-pipeline/bd-49f-etf-ownership-daily.tf
infra/aws/terraform/bd-pipeline/.terraform.lock.hcl
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ci/build-and-upload.sh
infra/aws/lambda/ci/record-terraform-deploy.sh
lib/trading_calendar.py
data/etfs/scripts/backfill/backfill_49f_daily_from_monolith_rps.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-s-2`.
<owned_cells>EG-s-2</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL or bd-49f-etf-ownership-daily.
comp-iam: RUN by the worker at Phase 1 -- `comp-iam service bd-49f-etf-ownership-daily` was NOT run at L5 because EG-s-11 decides which twin the port lands in; the worker runs it before the edit and after, records both, and the delta is exactly one Sid; the role policy was read at source by the issuer (5 statements, fact_rps/* scoped, no platinum/reports read).
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`); the ledger directory and the sentinel are named so the NEVER-2 entry can be COMMITTED.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S2-AC1` .. `S2-AC9`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-2.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> S2-AC1,S2-AC2,S2-AC3,S2-AC4,S2-AC5,S2-AC6,S2-AC7,S2-AC8,S2-AC9` BEFORE the complete flip, which the assignee commits itself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
