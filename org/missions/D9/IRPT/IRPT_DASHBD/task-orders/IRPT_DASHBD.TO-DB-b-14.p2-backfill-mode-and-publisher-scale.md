# TO IRPT_DASHBD.TO-DB-b-14 -- P-2's served move made buildable: a guarded backfill mode for the reporting gold, the publisher's account union and its own-function invoke grant (nothing served)

<to_id>IRPT_DASHBD.TO-DB-b-14</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** the issuer, inside its decomposition. Rows IRPT_DASHBD-W1-S12, S13 and S14 (DB-b-11,
merged @0637b0787d) name this seat as owner, and CTO batch 178 P-2 plus Andrew ~18:1xZ ("precomputed path widened to every 49
Financial account now") are the order. GATE (x) refuses a new file in rounds 5 and 6, so this is ROUND 7 (IRPT_BCKEND row S267).
| **Decomp cell:** `DB-b-14` (decomposition section 7) | **outcome_ref:** FWD-1 (every account), P-1 | **depends_on:** DB-b-13 (the
producer's S22 fix must be in the code the backfill runs)

---

## WORKER FACE

**The cell.** DB-b-11 measured P-2 and built the account-set widening (`P2_SCALE_R5.json` in your deliverables folder: 7,570
accounts; the publisher runs as 8 shards; the backfill is about 1.1 h in-region). Three things still stand between it and the served
move. This cell builds them. Nothing is served: the backfill run and the deploys are the issuer's packet.
1. **Row W1-S14: a BACKFILL mode for the reporting gold.** `reporting-gold/handler.py` computes only days after the newest landed
   partition, so the 562 landed partitions (2024-07-08..2026-10-01) can never gain the other ~7,560 accounts. Add an explicit,
   guarded event mode, `{"backfill": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}, "accounts": "population"}` or your equivalent.
   - It rewrites exactly the trading days in [start, end] for the declared account set, through the producer's own functions
     (`compute`, `emit_day`).
   - It refuses by name when the range exceeds a chunk bound (25 trading days), when no explicit `backfill` key is given, or when
     the range reaches past the newest landed day.
   - The scheduled fire's behaviour is unchanged.
   - Add `reporting-gold/tests/test_backfill_mode.py`, at least 4 tests (names `backfill`, `chunk`, `refuse`).
2. **Row W1-S12: the publisher's account set is the UNION** of accounts across the gold's partitions, not only the newest one. The
   885 population accounts with no positive value on the newest day still get their manifest and series.
   - Add `reporting-publish/tests/test_publisher_account_union.py`, at least 2 tests (names `union` and `newest`).
3. **Row W1-S13: the publisher may invoke its own function** for DB-b-11's shard fan-out.
   - In `infra/aws/terraform/investor-reporting/reporting-publish/iam.tf`, grant `lambda:InvokeFunction` on the publish function's
     own ARN, built from the existing name module, never `*`.
   - The measured numbers need no timeout or memory change; if your build says otherwise, file a row with the number.

<criterion id="DB7-1-AC1" cell_refs="DB-b-14"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r7/p7_1_ac1_backfill_mode_tests.py" .</invocation><expect>DB7-1-AC1 PASS</expect></criterion>
`DB7-1-AC1` -- the backfill mode tests pass (at least 4). Base: FAIL (no file).

<criterion id="DB7-1-AC2" cell_refs="DB-b-14"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r7/p7_1_ac2_publisher_union_and_selfinvoke.py" .</invocation><expect>DB7-1-AC2 PASS</expect></criterion>
`DB7-1-AC2` -- the union tests pass (at least 2), and `iam.tf` grants InvokeFunction on the publish function itself only. Base:
FAIL (no file).

<criterion id="DB7-1-AC3" cell_refs="DB-b-14"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/p5_ac3_suites_unchanged.py" . DB7-1-AC3</invocation><expect>DB7-1-AC3 PASS</expect></criterion>
`DB7-1-AC3` -- reporting-gold and reporting-publish suites pass unchanged. Base: PASS (a regression guard).

<expected_criteria>DB7-1-AC1,DB7-1-AC2,DB7-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. No plan, no apply, no invoke, no S3 write. Tests use stubs.
- **Refusal clause.** A change to the scheduled fire's behaviour is a defect: stop and file a row. An existing test that moves is a
  defect: stop and file a row.

<paths>
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/test_backfill_mode.py
infra/aws/lambda/investor-reporting/reporting-publish/handler.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_publisher_account_union.py
infra/aws/terraform/investor-reporting/reporting-publish/iam.tf
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r7/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/`, `infra/aws/terraform/investor-reporting/`, `data/assets/scripts/gold/irpt_reporting/`, `lib/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 7 (round 7, workstream B), cell `DB-b-14`.
<owned_cells>DB-b-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB7-1-AC1, DB7-1-AC2, DB7-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/IRPT_DASHBD.TO-DB-b-14.p2-backfill-mode-and-publisher-scale.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB7-1-AC1,DB7-1-AC2,DB7-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the backfill event shape and its refusals;
- the publisher's union rule;
- the IAM statement;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- two served handlers' source and the publish role's policy text; 0 served bytes move in the cell (the backfill run, the deploys and P-6's retirement are the issuer's packet with both halves).
comp-iam: RUN -- the publish role gains lambda:InvokeFunction on its own function only; graded by AC2; applied only under the packet.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the 07:41 and 08:15 ET schedules are not moved; the backfill mode is an explicit event, never a schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB7-1-AC1 base FAIL (no file), DB7-1-AC2 base FAIL (no file), DB7-1-AC3 base PASS (regression guard), dry-run at the base 2026-10-02 ~23:0xZ.
lane: the <paths> block IS the grant.
</preflight>
