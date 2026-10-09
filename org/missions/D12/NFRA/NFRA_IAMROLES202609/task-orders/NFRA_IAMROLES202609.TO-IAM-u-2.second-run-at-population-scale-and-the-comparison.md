# NFRA_IAMROLES202609.TO-IAM-u-2 -- THE SECOND RUN at population scale, and the comparison with round 3

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R4.md</decomp_doc>
<owned_cells>IAM-u-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_IAMROLES202609~11</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (outcome FWD-8; the round-3 analysis calls this R4-B)

```
IAM-u-2. ACT: RE-RUN the permission-grain assessment over the same population rule and lookback that
round 3 used, through a harness someone who did not build it can invoke by hand, and put the answer
beside round 3's.

FWD-8, verbatim:
  "The assessment can be re-run without doing it by hand again"
  DONE WHEN  EXERCISED -- it has actually been re-run and produced a comparable answer
  ACCEPT     Someone can ask the same question next quarter and get an answer they can put beside this
             one. It does not quietly stop happening because only one person knew how to do it.

THE FIRST RUN (read only, never edited):
  org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/permission-cold-raw-bundle.json
  run_date_utc 2026-09-10, lookback_days 90, attempted 219, returned_rc0 219, account 313476888478.
  population_rule: "every IAM role in account 313476888478 at Path "/" as returned by a single
  auto-paginated aws iam list-roles; the 10 roles at Path "/aws-service-role/" are excluded and named".
  instrument: "bash .tools/comp-iam-usage permission-cold --role <ROLE> --lookback 90 --json"
  instrument_blobs: .tools/comp-iam-usage 5c7f03ba3702d5de5c0edf7a955a72dd20e596f5,
                    org/modules/graph/comp_iam_usage.py 8670fc5025694c942f8a7c725a19e2317cf63c20
  results: {role_name: {role, role_arn, lookback_days, granted_read_ok, advisor_read_ok,
            rows: [{permission, status (never-used|used|unobservable), last_used?, age_days?, reason?}]}}
  Totals: granted 5494 = used 421 + never-used 1437 + unobservable 3636.

THE EXISTING HARNESS (read it, do not edit it):
  org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/rerun-assessment.sh
  Round 1 composed it over ONE role (opal-data-refresh-lambda-role). It has --dry-run, --role,
  --lookback and calls the instruments by explicit .tools/ path. It does NOT do population scale. That
  gap is why FWD-8 is not met: round 3's 219-role run was done by a worker by hand.

WHAT TO PRODUCE, in deliverables/0.9.0_WK_NFRA_IAMROLES202609~11/:

  (a) rerun-population.sh -- COMPOSES, never re-implements: one `aws iam list-roles` (auto-paginated),
      the same Path "/" rule with service-linked roles excluded and named, then per role
      `timeout 120 bash "$REPO_ROOT/.tools/comp-iam-usage" permission-cold --role <ROLE> --lookback 90 --json`,
      writing a bundle in THE SAME TOP-LEVEL SHAPE as round 3's (same keys, including instrument_blobs
      read with `git hash-object` at run time, and per_role_rc). It must have `--dry-run` (prints the
      population rule, `lookback=90` and the per-role invocation, makes no AWS call, exits 0). Chunking
      or resume options are fine and are yours to design. It is invoked BY HAND and never schedules
      itself (G-21). Derive the repo root (`git rev-parse --show-toplevel`); never hardcode a path.

  (b) permission-cold-raw-bundle.round4.json -- the second run's bundle, produced by (a).

  (c) compare-runs.py -- stdlib only, two bundle paths as arguments, NO cloud call. Prints:
        one line beginning `COMPARABLE: ` that reads `yes` only when lookback_days, population_rule and
        instrument_blobs are equal across the two bundles, and otherwise names which differ;
        one line `INTERSECTION roles=<n>` for roles present in both;
        totals per status for each run, on all roles and on the intersection;
        roles ADDED and REMOVED between the runs, by name;
        on the intersection, per-permission status transitions (e.g. used -> never-used) with counts.

  (d) RERUN_COMPARISON.md -- the answer put beside round 3's: what moved, by how much, and why where you
      can say why (a role added in the interval, a permission aging out of the 90-day window, a grant
      added or removed). Name the population change explicitly: round 3 counted 219; the live role graph
      read 283 IAM_ROLE nodes on 2026-10-09 (a different instrument that also counts service-linked
      roles). Your own list-roles read is the figure of record for your run.
```

## DEPENDENCIES

None. IAM-u-1 rolls up round 3's bundle beside you and does not read yours.

## BOUNDS

```
AWS READS ONLY: list-roles, and what comp-iam-usage permission-cold reads (get-role, list-role-policies,
  list-attached-role-policies, policy reads, Access Advisor). Nothing that changes AWS.
C-ANALYZER-PRICED-FIRST + G-25: NO AWS Access Analyzer, not even to compare. A vendor call reserved to Andrew.
C-NO-ACCESSDENIED: naming an unused permission is not removing it; nothing is narrowed or applied.
INSTRUMENTS ARE RUN, NOT REWRITTEN: .tools/ is not in your write surface. If comp-iam-usage cannot answer
  for a role, that is a FINDING and a surprise row, not a licence to fork it.
READ, NEVER WRITE: the ~1 harness and the ~8 bundle are read-only; every other worker directory too.
G-21: no alert, alarm, monitor, schedule, cron, timer or notification of any kind.
BOUND EVERY AWS READ: each tool call runs under `timeout 120` and a timeout is recorded AS the output.
  Run the population sweep in chunks or in the background and resume; never one unbounded call.
A ROLE THE INSTRUMENT CANNOT SEE MUST NOT READ AS CLEAN: rc != 0 roles are counted and named apart.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam-usage    pins at the base 54c2fd91b6 equal round 3's (5c7f03ba37 / 8670fc5025): the second run
                  uses byte-identical instrument code. Invoke it as `bash .tools/comp-iam-usage` from YOUR
                  worktree: a bare `comp-iam-usage` resolves through a ~/bin forwarder to the MAIN checkout.
comp-find aws     283 IAM_ROLE nodes, graph vintage 2026-10-09 03:31:25 UTC (DECLARED=262,
                  LIVE-no-DECLARED=18, MULTI_STATE_MANAGED=3). Round 3: 219 at Path "/" of 229.
aws shim          use `.tools/aws` (with `MSYS_NO_PATHCONV=1` only for ARN arguments).
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~11/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-u-2.second-run-at-population-scale-and-the-comparison.md
</paths>

Read surfaces (not granted for writing): `.tools/comp-iam-usage`, `org/modules/graph/comp_iam_usage.py`, the
`~1` harness and the `~8` bundle and report. Your surprise row id is `NFRA_IAMROLES202609-Z-W11-S<k>`,
`"fabric": "site-z"`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-u-2"><invocation>python org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~11/compare-runs.py org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~8/permission-cold-raw-bundle.json org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~11/permission-cold-raw-bundle.round4.json</invocation><expect>output carries a line `COMPARABLE: yes` and a line `INTERSECTION roles=<n>` with n of 1 or greater, computed from the two committed bundles with no cloud call; a missing script or bundle (rc=2) means the criterion is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-u-2"><invocation>python -c "import json;d=json.load(open('org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~11/permission-cold-raw-bundle.round4.json',encoding='utf-8'));print(d['run_date_utc'],d['lookback_days'],d['attempted'],d['returned_rc0'],len(d['results']))"</invocation><expect>one line: a run_date_utc of 2026-10-09 or later, lookback 90, then attempted, returned_rc0 and the results count, with results equal to attempted -- a second run, not a copy of the first; a FileNotFoundError means the run did not happen</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-u-2"><invocation>bash org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~11/rerun-population.sh --dry-run</invocation><expect>rc=0 and output naming `lookback=90` and the `permission-cold` invocation, with no AWS call made -- the harness can be read and invoked by someone who did not build it</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-u-2" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT -- never self-graded; record it UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming
  3.0.0_SA_CVO~Z): could a reviewer next quarter run the harness without the builder and put the answer beside
  this one -- and does RERUN_COMPARISON.md explain the differences it finds rather than only listing them?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>4</round>
<slot>~11</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-u-2</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 4) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-3 slug @36e167a2ea -> `ROUND_ANALYSIS.round3.md` @f8571787db section 7 (R4-B) -> L5 round-4 decomp -> this issuance.
**Chain:** an independent chain of one. **Risk LOCAL:** AWS reads only; the write surface is one deliverables directory.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule`, BUDGET REACHED at 220 s, 1 of 6 carriers, denominator C1=23 (7 gates armed), C2=32 PARTIAL (0 of 32 scanned); PARTIAL_OR_BLIND, not read as clean. G-21 binds as CLAUDE.md law.
comp-iam: RUN -- `bash .tools/comp-iam stats` from the main checkout: 214 TF roles / 196 services / 1154 operations / denominator 338 gaps; a source count, a different population from the live list-roles rule this cell uses.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 2 of 2 (instrument pins unchanged; population moved 219 -> 283 graph nodes).
</preflight>

**Preflight disposition:** the ACCESS plane is this cell's own instrument and is exercised by the cell. Check dry-run at the base `54c2fd91b6`: AC1 base: FAIL as expected (script absent); AC2 base: FAIL as expected (bundle absent); AC3 base: FAIL as expected (script absent).
