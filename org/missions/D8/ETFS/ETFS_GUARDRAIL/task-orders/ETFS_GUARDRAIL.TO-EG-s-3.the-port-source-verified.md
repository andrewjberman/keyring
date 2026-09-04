# TO ETFS_GUARDRAIL.TO-EG-s-3 -- the PORT SOURCE verified: inf-etf-ownership-daily's catch-up as it runs today, its battery green, its helpers named, and the port contract written for the two producers that will receive it

<to_id>ETFS_GUARDRAIL.TO-EG-s-3</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO paired at cut (the spawn IS the GO). Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance; Andrew-direct at the 1.0.0_SA_CTO terminal 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S3; s.5 "No new catch-up engine. Port inf's"; s.6 rulings 1 and 2; brief s.3) | **Decomp cell:** `EG-s-3` | **outcome_ref:** FWD-1 | **verb:** verify | **depends_on:** --

---

## THE CELL

`EG-s-3` (PRD s.7.2 S3): `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py:271-316` (317 lines at HEAD), claim MEASURED (4 hits). Bound: *"PORT SOURCE. Relied on, NOT owned -- do not modify to suit the port."* PRD s.5: *"No new catch-up engine. Port inf's. Two implementations of one convention drift, and only one gets fixed."*

The mechanism as it exists (brief s.3): after processing today's date, walk back `CATCHUP_WINDOW_DAYS` (= 10, `:271`); for each date -- skip if it is the date just processed; skip if output already exists (`_output_exists`, idempotent); **skip if the upstream partition is not present** (so it can never fabricate); otherwise `_process_date`. Per-date failures are caught and reported in `catchup_processed` / `catchup_failed`, never fatal. Its own battery `test_catchup_scan.py` drives the REAL `_catchup_missing_dates()` unmodified with the S3 collaborators stubbed -- both arms (a hole found; nothing found) required.

This is a VERIFY cell: you change nothing here. You prove the source is what the PRD says, run its battery, and write the PORT CONTRACT the next two orders in your own queue (`EG-s-1`, `EG-s-2`) build to -- which lines port verbatim, which one is REPLACED (the window), and which invariants must survive.

## DELIVERABLE

`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/the-port-source-verified.result.md` -- (1) the battery's output; (2) the helper census (which of `_catchup_missing_dates`, `_output_exists`, `_partition_exists`, `_list_all_partitions`, `_process_date`, `_load_universe` exist, with line numbers); (3) THE PORT CONTRACT: (a) ported verbatim in shape: the per-date loop, the three skips, the try/except that never raises, the `catchup_processed`/`catchup_failed` return keys and the `CATCHUP:` / `CATCHUP-SKIP:` log lines; (b) REPLACED: `CATCHUP_WINDOW_DAYS = 10` and the `today - timedelta(d)` walk-back become the REPORTING-OBLIGATION WINDOW -- every TRADING DAY (the vendored `trading_calendar.py`, `EG-s-10`'s recommendation) from the 1st of the PRIOR month while that month's report has NOT shipped, else from the 1st of the CURRENT month, through yesterday UTC; the terminus is the SHIPPED SIGNAL: `head_object` on `s3://opal-data-etfs/platinum/reports/<YYYY-MM>/etf_ownership.pdf` (ruling 2: never a calendar assumption); (c) INVARIANTS: skip-on-absent-partition (never fabricate), skip-on-existing-output (idempotent), the ZERO-vs-MISSING contract untouched (an unpriced day writes no slice), per-date failures non-fatal; (d) the NEW non-writing PROBE mode the ports add (`{"date": d, "probe": true}` -> `{"partition", "priced", "output_exists"}`, writes nothing), which the source does NOT have and the ports do not port from anywhere -- state it as an addition beside the port; (e) the 49F tail: a partition landing 12-13 days late is inside the reporting-obligation window by construction; write the test arm the ports must carry for it. Each criterion's invocation and output verbatim with rc and denominator.

## ACCEPTANCE

<criterion id="S3-AC1" cell_refs="EG-s-3"><invocation>python -m pytest infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/test_catchup_scan.py -q; echo BATTERY_RC=$?</invocation><expect>BATTERY_RC=</expect></criterion>
`S3-AC1` -- AMENDED BY THE ISSUER AT THE DRAIN (2026-09-04 21:1xZ) on row ETFS_GUARDRAIL-W2-S1: the original expectation `passed` is UNREACHABLE at HEAD -- the source's own battery crashes at import (KeyError: 'ASSETS_BUCKET', 0 of 4 checks collected) because it was never updated across the 2026-08-03 repoint @001a73530a; a premise of this cell that does not hold, declared on the record. The criterion now RECORDS the battery's collection state (rc and the first error line, verbatim); the defect is W2-S1's, for the inf producer's owner, outside this order's read-only bound on the port source.

<criterion id="S3-AC2" cell_refs="EG-s-3"><invocation>python -c "import re; s=open('infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py').read(); m=re.search(r'CATCHUP_WINDOW_DAYS\s*=\s*(\d+)', s); print('CATCHUP_WINDOW_DAYS=%s' % (m.group(1) if m else 'ABSENT'))"</invocation><expect>CATCHUP_WINDOW_DAYS=10</expect></criterion>
`S3-AC2` -- the shipped constant is 10 at HEAD (the number the PRD says a straight port would carry and fail property 2 with).

<criterion id="S3-AC3" cell_refs="EG-s-3"><invocation>python -c "import re; s=open('infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/lambda_function.py').read(); print('HELPERS=' + ','.join(sorted(n for n in ('_catchup_missing_dates','_list_all_partitions','_output_exists','_partition_exists','_process_date') if re.search(r'^def ' + n + r'\(', s, re.M))))"</invocation><expect>HELPERS=_catchup_missing_dates,_list_all_partitions,_output_exists,_partition_exists,_process_date</expect></criterion>
`S3-AC3` -- the five helpers the port contract names all exist at HEAD.

<criterion id="S3-AC4" cell_refs="EG-s-3"><invocation>git diff --stat HEAD -- infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/</invocation><expect></expect></criterion>
`S3-AC4` -- the relied-on producer is UNCHANGED by this order (an EMPTY diff is the expectation; the PRD's bound is a property of the bytes you leave behind).

<criterion id="S3-AC5" cell_refs="EG-s-3" judgment="true"/>
`S3-AC5` -- graded by the CVO at L9: the port contract is complete (verbatim set, the one replacement, the invariants, the probe addition, the 49F-tail test arm) and it re-proposes NO day-count window (ruling 1: "not to be re-proposed"). RECORD; NO VERDICT.

<expected_criteria>S3-AC1, S3-AC2, S3-AC3, S3-AC4, S3-AC5</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** (Restated by the issuer at the drain on row ETFS_GUARDRAIL-W1-S2: the flip was always admitted; the wording withheld it.) No source file changes in this cell; the inf directory is named for READING and for running its battery, not for editing.
- **EVERY invocation is bounded.** `timeout 120`.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W2-S<k>` (`W2` = your slot; `<k>` the next unused in your coordinate -- your first is `W2-S1`). Append inside the fenced json array per `org/surprise_channel/schemas/investigation_item.schema.json`, cite `path@commit`, never edit an existing row, keep working.
- **NEVER `git push`.** Report push state as MEASURED (`git ls-remote origin refs/heads/CLOUD`).

<paths>
infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-s-3`.
<owned_cells>EG-s-3</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL or inf-etf-ownership-daily.
comp-iam: DECLARED-NOT-APPLICABLE -- a repo-surface VERIFY cell that changes no principal, policy or resource.
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`).
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S3-AC1` .. `S3-AC5`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~2/ETFS_GUARDRAIL.TO-EG-s-3.the-port-source-verified.proof_of_spec.json`
(AMENDED BY THE ISSUER at the drain on row ETFS_GUARDRAIL-W3-S2: the instance file is named by the TASK ORDER'S OWN BASENAME stem, which is what `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`; the short `to_id` form this face carried before would have refused every flip. ONE instance file, this name, no duplicate.),
validated with `python .tools/proof-of-spec-check.py <instance> S3-AC1,S3-AC2,S3-AC3,S3-AC4,S3-AC5` BEFORE the complete flip, which the assignee commits itself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when every MECHANICAL criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
