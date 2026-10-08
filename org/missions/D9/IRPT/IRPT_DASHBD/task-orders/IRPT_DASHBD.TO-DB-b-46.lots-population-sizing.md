# TO IRPT_DASHBD.TO-DB-b-46 -- row S31: measure the extended reporting-gold handler over the whole 49F population for one trading day, wall time and peak memory against 900 s / 2048 MB (FWD-4)

<to_id>IRPT_DASHBD.TO-DB-b-46</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~26</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 1184 ("YES -- cut the S31 sizing cell now as
round 27 B"; "one trading day of the extended handler over all 7,597 49F accounts. Print wall time and peak memory against 900 s / 2048
MB, plus the per-account tail. A breach is a finding with its size, not a tuning loop."), correcting its round-26 analysis @0ae2f15e5c |
**Decomp cell:** `DB-b-46` (decomposition section 28) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-41 (merged @f3500197db).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-26`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~26/`.

**The cell (`DB-b-46`).** Round 26 extended the served reporting-gold handler
(`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`) to emit `account_activity_daily`, `account_lot_realized` and
`account_lot_unrealized_daily` through `data/assets/scripts/gold/irpt_reporting/account_activity_lots.py`, after the returns and class
tables. On 20 accounts and one day (record `deliverables/0.9.0_WK_IRPT_DASHBD~23/RELEASE_LOCAL_RUN.json`) the extension added about 35 s
and about 764 MB. The served function has a 900 s timeout and 2048 MB of memory, and the 49F population is about 7,597 accounts. Row S31
withholds the release until the whole population is measured. Measure it; do not tune.

1. Run the extended handler's `--local` mode (writing to a local output folder, never S3) for ONE trading day, 2026-10-06, over the
   handler's OWN population (its population function, the same one the scheduled fire uses), in ONE process. Record wall time and peak
   memory (peak working set) per stage -- returns, class, lots -- and in total, and the seconds per account for the lots stage.
2. **Wall cap:** if the run passes 3,600 s, stop it, and record `stopped_at_cap` true, `cap_seconds` 3600, how many accounts finished, and
   the measurements so far. Do not extrapolate a figure as if it were measured; an estimate, if you give one, sits in its own field
   labelled `estimate`.
3. Write `SIZING_S31.json`: `day`, `population_count` (from the handler's population function), `accounts_run`, `stopped_at_cap`,
   `cap_seconds`, `stages` {returns, class, lots: {wall_seconds, peak_mb}}, `total` {wall_seconds, peak_mb}, `limits` {timeout_s: 900,
   memory_mb: 2048}, `per_account_seconds` {p50, p95, p99, max}, `verdict` (`FITS` only when the run completed and total wall <= 900 and
   peak <= 2048; else `BREACH`), `breach` (each limit exceeded and by how much), `handler_sha256` and `producer_sha256` (sha256 of the two
   files you ran), and the machine (cores, RAM). Write `SIZING_S31.md`, COUNTS ONLY.

A breach is the finding: report its size. Do not change the handler, the producer or the function's limits.

<criterion id="DB27-2-AC1" cell_refs="DB-b-46"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r27/p27_sizing.py" . DB27-2-AC1</invocation><expect>DB27-2-AC1 PASS</expect></criterion>
`DB27-2-AC1` -- the population measured (or stopped at the cap and said so), per stage and in total, against 900 s / 2048 MB, with the
per-account tail and a verdict that agrees with the numbers. Base: FAIL.

<criterion id="DB27-2-AC2" cell_refs="DB-b-46"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r27/p27_sizing.py" . DB27-2-AC2</invocation><expect>DB27-2-AC2 PASS</expect></criterion>
`DB27-2-AC2` -- the measured handler and producer are HEAD's bytes. Base: FAIL.

<expected_criteria>DB27-2-AC1,DB27-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. The handler, the producers and the Terraform are read and run, never edited.
- **AWS:** S3 reads only. No S3 write, no Lambda invoke, no deploy, no vendor call, no bun, no download of any package, script or program.
- **Refusal clause.** A code or limit change, an S3 write, an estimate presented as a measurement, or a client figure in a committed `.md`
  is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~26/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-46.lots-population-sizing.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 28 (round 27, workstream B), cell `DB-b-46`.
<owned_cells>DB-b-46</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB27-2-AC1, DB27-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~26/IRPT_DASHBD.TO-DB-b-46.lots-population-sizing.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB27-2-AC1,DB27-2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the population and accounts run, wall time and peak memory per stage and total, the
per-account tail, the verdict and any breach's size, and any row ids.


## AMENDMENT 1 (2026-10-08 ~04:2xZ, issuer 2.0.0_SA_COO~D2, on the worker's report and row W26-S1)

The measurement is complete and is the finding: total 461 s of 900 s; peak 2,759.5 MB against 2,048 MB (a floor: the lots stage
REFUSED at population scale on a realized lot id repeated within one day's frame -- 87 ids over 175 rows in 36 accounts, none spanning
accounts, none a full-row duplicate). AC1 as cut demanded a per-account tail that a refused stage cannot produce; that is the issuer's
check defect, not the record's. AC1 is amended: when `lots_stage_completed` is false and `lots_refused.reason_class` is named, the tail
may be null and the verdict is BREACH. The record is unchanged; re-run AC1, update the proof, flip. Row W26-S1 is ruled by issuer row S33.
No gate limb graded this modification (LIMB 6 does not fire on a modification; GATE (viii) grades the unchanged `<placeholders>NONE</placeholders>`).

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a local measurement of code already merged; nothing is written to S3 or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads only, from this box; no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB27-2-AC1 and AC2 base FAIL (no record), dry-run at base ce3d3b20c8 2026-10-08 ~02:1xZ.
lane: the <paths> block IS the grant.
</preflight>
