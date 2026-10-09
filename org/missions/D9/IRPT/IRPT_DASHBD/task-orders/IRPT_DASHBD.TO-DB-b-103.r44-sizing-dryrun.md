# TO IRPT_DASHBD.TO-DB-b-103 -- E1: the R44 sizing read -- ONE dry-run population backfill of 2026-10-08 on live oNgy4rnr, no writes; under 85% of timeout and memory closes ledger leg S1, over either rolls back to yIAQjspL now

<to_id>IRPT_DASHBD.TO-DB-b-103</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~78</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>50</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's R44 CTO half AMENDMENT 1 (msg 3550, @b758031ba2), enrichment item E1 | **Decomp cell:** `DB-b-103` (decomposition section 52) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-95 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-78`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~78/`.

**The cell (`DB-b-103`).** The R44 release is live: `irpt-49f-reporting-gold-lambda` CodeSha256 `oNgy4rnr...` (DB-b-95). Ledger
`org/critical_paths/change_management/20261009T1414Z_irpt-dashbd-r44-release-1009_deploy_completion.md` has leg S1 (sizing) OPEN. The first
scheduled fire is Monday 07:41 ET, after the ledger window. The CTO ruled (R44 CTO half AMENDMENT 1, `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R44_RELEASE_CTO_HALF.md`)
that ONE dry run sizes it now.

Run everything from `C:/dev/wk-irpt-dashbd-78`.

1. **Before.** Read live CodeSha256 (it must be `oNgy4rnr...`, else STOP), Timeout (900 s) and MemorySize (2048 MB).
2. **ONE invoke**, synchronous, with the event `{"backfill": {"start": "2026-10-08", "end": "2026-10-08"}, "accounts": "population", "dry_run": true}`.
   - A dry run computes and prints, and writes nothing.
   - Read the function's REPORT line for that RequestId from CloudWatch: Duration and Max Memory Used.
   - Read accounts and lots rows from the function's log lines.
   - Count the objects written during the run under the firm's gold prefixes, by LastModified after the invoke start. Expect 0.
3. **Verdict.**
   - UNDER: both Duration < 765,000 ms and Max Memory < 1,740.8 MB. Close ledger leg S1 with the read (`python .tools/deploy_ledger.py`), so the
     ledger CLOSES.
   - OVER: either one over. Branch B now: roll back to `yIAQjspL` by its S3 version (`a.YllA9SmwwfY34NlajqOaNsex2bBZAy`), through ONE targeted
     `.tools/safe-apply.sh` of the function, the R44 packet's rollback route. Record `rollback.live_codesha256_after`, and file a row.
   - A run that sized nothing (accounts < 7000 or lots rows 0, e.g. SOURCE_LAG) is neither: file a row and STOP.
4. Record `R44_SIZING_DRYRUN.json` {codesha256, timeout_s, memory_mb, event, request_id, duration_ms, max_memory_mb, accounts, lots_rows,
   written_objects, verdict, ledger_leg_closed, rollback (on OVER)}.
5. Also add a row that keeps Monday 2026-10-12 07:41 ET as the acceptance read, with that clock and the 85% lines, owner `2.0.0_SA_COO~D2`.

**No other invoke. No delete.**

<criterion id="DB50-1-AC1" cell_refs="DB-b-103"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r50/p50_round50.py" . DB50-1-AC1</invocation><expect>DB50-1-AC1 PASS</expect></criterion>
`DB50-1-AC1` -- one dry run of 2026-10-08 on live oNgy4rnr sized the lots stage, wrote nothing, and its verdict closed leg S1 or rolled back. Base: FAIL.

<expected_criteria>DB50-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** ONE dry-run invoke of the gold Lambda, plus CloudWatch and S3 reads. On OVER only: ONE targeted safe-apply rollback under the R44 pair. No other invoke, no delete.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~78/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~78/
org/critical_paths/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-103.r44-sizing-dryrun.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 52 (round 50), cell `DB-b-103`.
<owned_cells>DB-b-103</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB50-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~78/IRPT_DASHBD.TO-DB-b-103.r44-sizing-dryrun.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB50-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the before reads, the REPORT line, the counts, the verdict, the ledger leg, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one function; a dry run writes nothing; the only write path is the pair's rollback on OVER.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role or policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is unchanged; Monday's fire stays the acceptance.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB50-1-AC1 FAIL at base (no record). R44 CTO half AMENDMENT 1 @b758031ba2.
lane: the <paths> block IS the grant.
</preflight>
