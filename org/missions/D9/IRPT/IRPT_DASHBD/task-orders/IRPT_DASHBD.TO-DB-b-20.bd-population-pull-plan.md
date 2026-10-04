# TO IRPT_DASHBD.TO-DB-b-20 -- the ONE Black Diamond population pull: its script and its OFFLINE plan (E3 / P-5 build)

<to_id>IRPT_DASHBD.TO-DB-b-20</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~6</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-04</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** ANDREW-DIRECT ~22:0xZ 2026-10-04, "all recs approved", card 2 (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_220xZ_ALL_RECS_APPROVED_REPORT_OPEN_BD_PULL_RSI_49F_BUILD.md`
@66f1e98e98, relayed by 1.0.0_SA_CTO msg 105003): the ONE Black Diamond performance pull across all 49 Financial accounts. Terms:
one pull, scoped to Opal's gap-free segments, graded against 0.35 pp, no second pull. His 2026-10-03 data-collection hold is lifted
for this one pull only. | **Decomp cell:** `DB-b-20` (decomposition section 12) | **outcome_ref:** P-5 (FWD-8's population
tie-out) | **depends_on:** none.

THIS CELL MAKES NO VENDOR CALL. It builds the script and the offline plan. The live run is a separate act: it waits on
1.0.0_SA_CTO's ruling on the run's shape (asked 22:2xZ), and it is never this worker's.

---

## WORKER FACE

**What exists.** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/bd_likeday_pull_r4.py` (TO-DB-b-10) is the
only Black Diamond performance caller, and it is locked to five accounts (`FIVE` :27, cap :177). Reuse its structure:
- `plan` runs offline with `DRY_RUN=1`;
- `pull --go` rebuilds the plan, requires it equal to the written one, mints the bearer once, sends one `performancePeriod` POST per
  account and writes the records;
- `segments_for` (:78-101) gives maximal runs of consecutive trading days with non-null `total_return_daily`, at least
  `MIN_DAYS=5` long, each run becoming a `Custom` dateRange;
- `build_plan` (:104).

The client stays the estate's, read-only:
- `infra/aws/lambda/investor-reporting/performance/bd_adapter.py` (`load_bd_helpers` :70, `build_period_request` :96,
  `parse_period` :139);
- the helpers it loads from `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py`.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-dashbd-6`. Run everything from its root.

**What you build**, all under `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/`:
1. **`bd_population_pull_e3.py`**, a fork of the round-4 script, changed as follows:
   - **Population:** every 49 Financial account in the served reporting gold (`opal_naming.address("irpt","49financial","gold",
     "account_return_daily", ...)`, as `read_gold` does), not a fixed list.
   - **Mapping:** Schwab account to Black Diamond internal id through `s3://opal-data-assets/blackdiamond/49f/silver/dim_account_xref/`,
     the resolver's first tier (`infra/.../taxsma_resolver.py:8-9`: `bd_internal_id = int(bd_account_id[3:])`, no vendor call).
     Every account it cannot map goes into `unmapped` with its reason. Never guess a mapping.
   - **Requests:** one per mapped account that has at least one gap-free segment of MIN_DAYS or more. `requests` is that count.
   - **`WORD = "66f1e98e98 card 2"`.**
   - **`plan`** stays OFFLINE and runs under `DRY_RUN=1`. It writes `BD_POPULATION_PLAN_E3.json` with `accounts_total`,
     `mapped`, `unmapped` (a list of `{account, reason}`), `requests`, `vendor_calls: 0`, `dry_run`, `word`, the sha256 of the
     request bodies, and per-account segment counts. It never writes a credential.
   - **`pull`** keeps every refusal of the round-4 script, and adds two:
     - **No second pull:** it refuses when a pull record (`BD_POPULATION_PULL_E3.json`) already exists.
     - **The CTO's shape ruling:** it refuses unless `E3_SHAPE_RULING.json` exists beside it, naming the CTO's ruling id and the
       pace (requests per second) and abort rule the run must follow. The issuer writes that file when the ruling lands.

     Raw responses go to `s3://opal-data-assets/blackdiamond/49f/bronze/reporting_performance/<pull_date>/` through the estate's
     `land_bronze`, not `.scratch`. You do NOT run `pull`.
2. **`tests/test_bd_population_pull_e3.py`**, at least 4 pytest tests, all offline, with no network and no boto3 call (patch or
   stub them). Each test asserts one refusal of `pull`:
   - without `--go`;
   - with a written plan whose hash differs from the rebuilt one;
   - when a pull record already exists (the second-pull refusal);
   - without `E3_SHAPE_RULING.json`.

   The four words `--go`, `hash`, `second` and `ruling` appear in the file.
3. **Run `plan` once**, then commit the plan file and the script.

<criterion id="DB12-1-AC1" cell_refs="DB-b-20"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r12/p12_population_plan.py" . DB12-1-AC1</invocation><expect>DB12-1-AC1 PASS</expect></criterion>
`DB12-1-AC1` -- the plan exists, was built with DRY_RUN=1 and vendor_calls 0, and names the word. Its population equals mapped plus
unmapped, every unmapped account has a reason, and requests is between 1 and mapped. Base: FAIL.

<criterion id="DB12-1-AC2" cell_refs="DB-b-20"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r12/p12_population_plan.py" . DB12-1-AC2</invocation><expect>DB12-1-AC2 PASS</expect></criterion>
`DB12-1-AC2` -- the refusal tests pass, at least 4, naming --go, hash, second and ruling. Base: FAIL.

<criterion id="DB12-1-AC3" cell_refs="DB-b-20"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r12/p12_population_plan.py" . DB12-1-AC3</invocation><expect>DB12-1-AC3 PASS</expect></criterion>
`DB12-1-AC3` -- a GUARD: your commits touch only IRPT_DASHBD paths, and no REMEDIATION file. Base: PASS.

<expected_criteria>DB12-1-AC1,DB12-1-AC2,DB12-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** S3 reads only (the served gold, the xref silver). NO Black Diamond call of any kind. `DRY_RUN` stays 1 for every
  command you run. No `pull`, no token mint, and no Secrets Manager read of `blackdiamond/49f/session`.
- **Refusal clause.** Any network call to a Black Diamond host, a `pull` run, or a credential written anywhere is a defect: stop
  and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-20.bd-population-pull-plan.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 12 (round 12, workstream B), cell `DB-b-20`.
<owned_cells>DB-b-20</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB12-1-AC1, DB12-1-AC2, DB12-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/IRPT_DASHBD.TO-DB-b-20.bd-population-pull-plan.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB12-1-AC1,DB12-1-AC2,DB12-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes; the plan's population, mapped, unmapped (with the top reasons and their
counts) and request counts; each criterion's last line; and any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a script and an offline plan under a deliverables folder; 0 served bytes move; no vendor call in this cell (DRY_RUN=1 throughout).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB12-1-AC1 base FAIL (no plan), DB12-1-AC2 base FAIL (no tests), DB12-1-AC3 base PASS (guard), dry-run at base 681c49eeeb 2026-10-04 ~22:3xZ.
lane: the <paths> block IS the grant.
</preflight>
