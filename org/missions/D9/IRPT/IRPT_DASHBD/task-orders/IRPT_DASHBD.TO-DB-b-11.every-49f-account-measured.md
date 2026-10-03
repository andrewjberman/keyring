# TO IRPT_DASHBD.TO-DB-b-11 -- P-2, every 49 Financial account: the population declared, the scale measured against the Lambda limit, the widening built (nothing served)

<to_id>IRPT_DASHBD.TO-DB-b-11</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-02</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 178 (@2a537cbad4, msg 104324; Andrew's IR fold-in,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 1, P-2: "Every 49 Financial account in the
holdings population gets a published manifest and series ... Andrew's 14:5xZ words are the deliberate act that
`reporting-gold/handler.py:18-19` waits for") | **Decomp cell:** `DB-b-11` (decomposition section 5) | **outcome_ref:** FWD-1 (every
account), P-1 the acceptance | **depends_on:** none

---

## WORKER FACE

**The cell.** Today the reporting gold (`infra/aws/lambda/investor-reporting/reporting-gold/handler.py`) and the publisher
(`reporting-publish/handler.py`) serve 6 accounts. The gold's account set is the newest partition's (`handler.py:18-19`,
`newest_accounts`), and the publisher publishes every account in the newest gold partition. P-2 widens both to every 49 Financial
account in the HOLDINGS POPULATION, the account ids of the newest 49 Financial holdings gold partition at
`lib/opal_naming.py address("irpt", "49financial", "gold", "holdings_performance_daily", "date=<d>")`. This cell MEASURES first and
BUILDS the widening. It writes nothing served: no upload, no apply, no invoke. The backfill and the deploy are the issuer's packet.

**Measure** (reads only; local; nothing uploaded). Write `P2_SCALE_R5.json` in your deliverables folder, in the shape the AC1 check
reads:
- **population:** the source address and the account count.
- **producer:** the reporting gold producer (`data/assets/scripts/gold/irpt_reporting/account_return_daily.py`, through the
  handler's own `compute()`) for ONE recent trading day over the whole population. Record the accounts, rows and seconds. Memory
  helps.
- **publisher:** the publisher's per-account build at that population. Sample k trading days of locally computed gold, or the real
  6-account history scaled by accounts. Record the measured seconds, a projection for the daily fire over the full history,
  `lambda_timeout_s` 900, and how the publisher stays under it (parallel puts, account shards, or both).
- **backfill:** the trading days from the population's first data to T-1, the projected hours, and a plan that respects the Lambda
  limit (chunked fires, or one local run under a ledger).
- **Disk:** the laptop has about 7 GB free. Never write more than about 1 GB of scratch, and say what you deleted.

**Build** (source only). In `reporting-gold/handler.py`, the account set comes from the declared population (the holdings gold's
newest partition). It is never FEWER than the newest reporting partition's accounts, so no served account drops. In
`reporting-publish/handler.py`, the daily fire fits the measured limit (bounded parallel puts, and an account shard per invoke if the
measure says so). Add `reporting-gold/tests/test_population_account_set.py`, at least 3 tests, naming `population` and `newest`:
- the population supplies the set;
- an account in the newest partition but absent from the population is kept;
- an empty population refuses by name.

<criterion id="DB5-1-AC1" cell_refs="DB-b-11"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/p5_1_ac1_scale_record.py" .</invocation><expect>DB5-1-AC1 PASS</expect></criterion>
`DB5-1-AC1` -- the scale record covers the population (at least 1,000 accounts) with producer, publisher and backfill numbers against
900 s. Base: FAIL (no record).

<criterion id="DB5-1-AC2" cell_refs="DB-b-11"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/p5_1_ac2_population_tests.py" .</invocation><expect>DB5-1-AC2 PASS</expect></criterion>
`DB5-1-AC2` -- the population account-set tests pass (at least 3). Base: FAIL (no file).

<criterion id="DB5-1-AC3" cell_refs="DB-b-11"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/p5_ac3_suites_unchanged.py" . DB5-1-AC3</invocation><expect>DB5-1-AC3 PASS</expect></criterion>
`DB5-1-AC3` -- reporting-gold (9) and reporting-publish (13) suites pass unchanged. Base: PASS (a regression guard).

<expected_criteria>DB5-1-AC1,DB5-1-AC2,DB5-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** reads only. No S3 write, no upload, no Terraform, no Lambda invoke. `account_return_daily.py` is read only, because it
  is packaged through pins and runs UNEDITED.
- **Refusal clause.** A served account that would drop is a defect: stop and file a row. A population that cannot be read is a row,
  never a guess. If a measurement cannot fit the disk, file a row with the size, and never fill the disk.

<paths>
infra/aws/lambda/investor-reporting/reporting-gold/handler.py
infra/aws/lambda/investor-reporting/reporting-gold/tests/test_population_account_set.py
infra/aws/lambda/investor-reporting/reporting-publish/handler.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r5/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda/investor-reporting/`, `data/assets/scripts/gold/`, `lib/`, `infra/aws/terraform/investor-reporting/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 5 (round 5, workstream B), cell `DB-b-11`.
<owned_cells>DB-b-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB5-1-AC1, DB5-1-AC2, DB5-1-AC3. Instance at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1/IRPT_DASHBD.TO-DB-b-11.every-49f-account-measured.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DB5-1-AC1,DB5-1-AC2,DB5-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes and each criterion's last line;
- the population count, and the producer and publisher seconds with the projection against 900 s;
- the backfill plan in two lines;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- reads the 49 Financial holdings gold and the reporting gold; builds two handlers' account-set and fan-out code; 0 served bytes move (the backfill and deploy are the issuer's packet with both halves).
comp-iam: DECLARED-NOT-APPLICABLE in the cell -- no role changes; the packet reads whether the gold role may read the holdings gold prefix.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the two existing schedules (07:41 and 08:15 ET) are not moved; only what each fire covers is built.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB5-1-AC1 base FAIL (no record), DB5-1-AC2 base FAIL (no file), DB5-1-AC3 base PASS (regression guard: reporting-gold 9, reporting-publish 13), dry-run at the base 2026-10-02 ~18:2xZ.
lane: the <paths> block IS the grant.
</preflight>
