# TO IRPT_DASHBD.TO-DB-i-17 -- the WRAPPER'S PARTITION-KEY RULE CORRECTED: a silver partition `date=<d>` must hold only rows whose `day` is <d> (the real feed keys its partitions by calendar day and stamps every row of a pull with the pull date); a differing pull_date is NOT a refusal (direct act)

<to_id>IRPT_DASHBD.TO-DB-i-17</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~317</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>130</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the issuer (`2.0.0_SA_COO~I2`), on its own defect found at the round-129 drain; inside its own decomposition (no CTO ruling needed; the CTO reads it at the round analysis). The rule being corrected is round 125's order DB-i-12 step 4, which the CTO accepted from the issuer's batch (msg 8654).

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-317`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~317/`. Never touch a path outside the `<paths>` block below.

**Why.** Round 125 made `run()` in the wrapper refuse a silver partition `date=<d>` when any row's `pull_date` differs from `<d>` (worker row W311-S5, the issuer's wording). That is wrong for the real feed. `data/inf/manual_api/pull_inflection_scope_account_returns.py` writes ONE partition per calendar DAY (`write_day(s3, day, ...)`, partition `date=<day>`) and stamps every row of a pull with the PULL date, so a backfill or a multi-day scheduled pull has rows whose `pull_date` is later than their partition. The round-125 rule would refuse every such partition on the first real run (a fixture shaped like the real feed reads: `partition keys refused: 48 row(s) name another pull date`). The right check is that a partition `date=<d>` holds only rows whose `day` is `<d>`.

**The cell (`DB-i-17`).** Text of the owned cell: *"Correct the wrapper's partition-key rule: a silver partition date=<d> is refused, with a count and nothing written, when any of its rows has a day other than <d>; a pull_date that differs from the partition is accepted."*

**What you do (edit two existing files; add nothing else).**
1. `data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_run.py`: in the partition check of `run()`, compare each row's `day` (not `pull_date`) with the partition's `<d>`; keep the count in the message and change its words to say that the rows name a day other than their partition's. The check still runs before anything is written, and a partition name that does not start with `date=` still counts every one of its rows. Nothing else in the file changes.
2. `data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_run.py`: update the partition test(s) for the new rule (a row whose `day` is not its partition's is refused with a count and nothing written) and ADD one test that a feed whose rows carry a `pull_date` later than their partition (the backfill shape) is accepted. Every other test stays green. ASCII only.

**Read first (read only).** The wrapper and its tests; `data/inf/manual_api/pull_inflection_scope_account_returns.py` lines near `write_day` and `_day_rows` (the real partition and `pull_date` semantics); the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r130/p130_run_partition.py` (its `silver_backfill` is the real feed's shape; run it as you go).

<criterion id="DBI130-1-AC1" cell_refs="DB-i-17"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r130/p130_run_partition.py" . DBI130-1-AC1</invocation><expect>DBI130-1-AC1 PASS</expect></criterion>
`DBI130-1-AC1` -- the golden through the wrapper on a backfill-shaped feed (every row's `pull_date` is one later date, partitions keyed by day) is accepted with the golden counts (17 PRESENT, 11 ABSENT, the run record's keys). Base: FAIL (the merged wrapper refuses it).

<criterion id="DBI130-1-AC2" cell_refs="DB-i-17"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r130/p130_run_partition.py" . DBI130-1-AC2</invocation><expect>DBI130-1-AC2 PASS</expect></criterion>
`DBI130-1-AC2` -- the written parquet and the contract checks as in round 127 (declared fields and hash, the validator on every row, no AWS or network import, no typed contract version, nothing written outside the output directory), on the backfill-shaped feed. Base: FAIL.

<criterion id="DBI130-1-AC3" cell_refs="DB-i-17"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r130/p130_run_partition.py" . DBI130-1-AC3</invocation><expect>DBI130-1-AC3 PASS</expect></criterion>
`DBI130-1-AC3` -- the repairs still hold (edge-day fixtures 0 unaccounted; the dimension-key, repeated-key and non-empty-directory refusals; the 299-day chain), a row whose `day` is not its partition's day is refused with a count and nothing written, a differing `pull_date` is accepted, and the adapter and wrapper test files together pass at least 30 tests and name a mutant test. Base: FAIL.

<expected_criteria>DBI130-1-AC1,DBI130-1-AC2,DBI130-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the adapter, the contract, `lib/`, `infra/`, the feed script and every issuer check.
- **No AWS, no network, no client data.** Fixtures only; no run of 8 or more digits in anything you write except a `sha256` value or a path.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or widened. Rows (if any) go to the investigation file, ids `IRPT_DASHBD-D2-W317-S<k>`, `surfaced_at` from `date -u +%FT%TZ` at filing. Commit with `.tools/safe-commit.sh`. ASCII only.

<paths>
data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_run.py
data/assets/scripts/gold/irpt_reporting/tests/test_inflection_scope_feed_run.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~317/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-17.scope-feed-wrapper-partition-key-is-the-day-not-the-pull-date.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 16, cell `DB-i-17`.
<owned_cells>DB-i-17</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI130-1-AC1, DBI130-1-AC2, DBI130-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~317/IRPT_DASHBD.TO-DB-i-17.scope-feed-wrapper-partition-key-is-the-day-not-the-pull-date.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI130-1-AC1,DBI130-1-AC2,DBI130-1-AC3` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the three criteria's last lines; the tests passed in the wrapper's file; any case the rules did not cover (as row ids); the commit ids. No client value, no account or household id, no date.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a one-condition edit to a local module whose only importers are its tests and the round-129 run script (not yet run on real data); nothing is wired, scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call, no secret, no grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; all three criteria FAIL on the merged wrapper (it refuses the backfill shape, 48 rows), the checker passed a reference edit on all three, and two mutants of it (the partition check dropped, the rule on pull_date again) each failed the checker before the cut.
</preflight>
