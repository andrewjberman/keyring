# TO IRPT_DASHBD.TO-DB-b-107 -- E1: ONE more no-write dry run on live oNgy4rnr, on the HEAVIEST lots day of the last 90 days (largest lot-row count, denominator printed), read against the 85% lines

<to_id>IRPT_DASHBD.TO-DB-b-107</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~82</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>53</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop (placement DELL2) | **Ordered by:** 1.0.0_SA_CTO~DELL2's ADDENDUM 18 (msg 3598, @a25a7e1ea5), enrichment item E1 | **Decomp cell:** `DB-b-107` (decomposition section 55) | **outcome_ref:** FWD-4 | **depends_on:** DB-b-103 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-82`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~82/`.

**The cell (`DB-b-107`).** DB-b-103's dry run of 2026-10-08 on live `irpt-49f-reporting-gold-lambda` `oNgy4rnr...` read 377 s and 1,661 MB, which is
95.4% of the 1,740.8 MB line (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~78/R44_SIZING_DRYRUN.json`). The CTO ruled (ADDENDUM 18 item 1) that one sample is not a
margin: ONE more dry run on the HEAVIEST lots day of the last 90 days.

Run everything from `C:/dev/wk-irpt-dashbd-82`.

1. **Choose the day.** Read the landed lot tables' daily row counts for 49 Financial over the last 90 calendar days, from each `date=` partition's
   manifest or object size by its served address (`opal_naming.address()`). The three tables are `account_lot_realized`,
   `account_lot_unrealized_daily` and `account_activity_daily`.
   - Sum the rows per day, and print the number of days read (the denominator) and the top 5.
   - The chosen day is the maximum. Month-end 2026-09-30 is a candidate, not a default.
2. **Before:** live CodeSha256 must be `oNgy4rnr...`, else STOP. Read Timeout and MemorySize.
3. **ONE invoke**, synchronous: `{"backfill": {"start": "<day>", "end": "<day>"}, "accounts": "population", "dry_run": true}`.
   - Read the REPORT line for that RequestId: Duration and Max Memory Used.
   - Count objects written under `irpt/49financial/gold/` after the invoke start, with a positive control, as DB-b-103 did. Expect 0.
4. **Verdict.**
   - UNDER: both lines are under 85%.
   - OVER: either line is over. File a BLOCKING row naming the axis; the issuer asks for a pair, producer fix preferred. Do NOT roll back or change
     the configuration in this cell.
5. Record `R44_HEAVY_DAY_DRYRUN.json` {selection: {window_days: 90, days_read, top: [{day, lot_rows}], chosen_day}, codesha256, timeout_s,
   memory_mb, event, request_id, duration_ms, max_memory_mb, accounts, written_objects, verdict}.

**No other invoke. No write, no delete, no configuration change.**

<criterion id="DB53-1-AC1" cell_refs="DB-b-107"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r53/p53_round53.py" . DB53-1-AC1</invocation><expect>DB53-1-AC1 PASS</expect></criterion>
`DB53-1-AC1` -- the heaviest lots day of 90 is chosen with its denominator and dry-run sized on live oNgy4rnr, writing nothing. Base: FAIL.

<expected_criteria>DB53-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `data/`, `infra/` or `portal/`.
- **This order's exception:** ONE dry-run invoke of the gold Lambda, plus S3, CloudWatch and get-function reads. No write, no rollback, no configuration change.
- **AWS:** S3 reads only unless this face says otherwise. NO Black Diamond or vendor call, no secret read, no S3 write, no deploy, no bun,
  no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~82/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~82/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-107.r44-heavy-day-dryrun.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 55 (round 53), cell `DB-b-107`.
<owned_cells>DB-b-107</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB53-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~82/IRPT_DASHBD.TO-DB-b-107.r44-heavy-day-dryrun.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB53-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the day chosen with the top five and the denominator, the REPORT line, the verdict, and any row, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one function; a dry run writes nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role or policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is unchanged; Monday's fire stays the acceptance.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB53-1-AC1 FAIL at base (no record). CTO ADDENDUM 18 item 1.
lane: the <paths> block IS the grant.
</preflight>
