# ADVI_FIRMBKTS task order -- `FB-l-5` -- FWD-5: THE FIRST TRIGGER MOVED TO ITS NEW HOME, EXERCISED AND READ

<!-- ===================== WORKER FACE -- this is the WHOLE of the executing seat's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R8.md</decomp_doc>
<owned_cells>FB-l-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the order adds no cron or cadence of its own; the act is named in an amendment at the un-park and is re-declared there.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is added by this order as cut; any grant the named act needs is stated in the un-park amendment and its pair, and `comp-iam` is run then.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a record with an unsigned or missing pair, an unclosed ledger entry, no recorded rollback, and (an old_target_present that is not false, a new_target_present that is not true, an exercised event that did not fire). Blindness: the grader proves the record's discipline, not that the act was the right one; the CTO's exercised read is that.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-l-5` (round 8, WORLD)

STAGED. This order is FWD-5's first moved trigger: ONE trigger that set an Advisor Intelligence pipeline running against a legacy home, moved to its new home in the plan's order,
exercised and read. It waits; it is not a standing GO. You act only after the issuer's UN-PARK AMENDMENT (in this file's record face), which names (1) the trigger and its move row in
`PLAN_INFLECTION.json` or `PLAN_COTTONWOOD.json` (the move with `depends_on` empty and the lowest `order`, or the one the CTO names), (2) the CTO's read of the plan, and (3) the signed
never-widen pair (COO half and CTO half, commits named). Until that amendment exists, do nothing. If the plan's first move is not ready inside round 8, this order is cut again as round 9's first cell.

### 1a. Steps (once un-parked)

1. **Preconditions (read, each recorded):** the plan record is merged and its AC1 PASS; the CTO has read the plan; the move row's `depends_on` is empty or landed; the pair is signed on both
   halves at the current bytes.
2. **Before (recorded):** the trigger's live definition at its OLD home (rule, schedule or S3 notification, with its target and state) and the new home's state, each by one live read; the saved
   copy of the old definition is the rollback.
3. **Ledger** (NEVER-2) with its `.open_deploys/` sentinel BEFORE the first write.
4. **The move:** create the trigger at the new home FIRST, then remove or disable the old, exactly as the move row and the pair name. Terraform only through `bash .tools/safe-apply.sh`; a
   notification singleton is replaced whole (read the whole configuration before and after).
5. **Exercise it:** drive one event deliberately by the mechanism the amendment names and read that the new trigger fired and its target ran (the log line, the invocation count, the object it
   writes), then read that the old trigger no longer exists or is disabled and nothing else changed.
6. **Roll back** (the saved copy) if the new trigger does not fire, anything outside the named resources changed, or the old target still fires after removal.
7. Close the ledger entry.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/MOVE_RECORD.json`

Write the record as one JSON file at that path; its shape is fixed by the grader `C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round8/checks/r8_checks.py` (`move`). Every value carries `claim` as `measured`, `inferred`, `held` or `absent`; print no
client name, account number or relationship id (write `<id>`).

## 2. BOUNDS

1. The act touches exactly the resources the un-park amendment and the signed pair name, and nothing else. A resource outside them is a STOP and a BLOCKING row.
2. `terraform` only through `bash .tools/safe-apply.sh`; AWS from bash is `.tools/aws`; a deploy opens a ledger entry (`org/critical_paths/`) BEFORE the first write and closes it at completion (CLAUDE.md NEVER-2).
3. Print no secret or token. `opal-data-inf/orion/jwt/current.json` is never read or touched.
4. No manual invoke of a pipeline to hasten a read; where the act's outcome needs an event, drive it deliberately by the mechanism the amendment names (a test event, a harmless object), and read the result.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/
infra/aws/lambda/
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-l-5.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-l-5"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round8/checks/r8_checks.py move --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/MOVE_RECORD.json</invocation><expect>^MOVE: OK trigger=.+$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-l-5.proof_of_spec.json`. Commit the record FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report once to `2.0.0_SA_COO~B1` and `1.0.0_SA_CTO~DELL1`: what changed, the read-back, the pair commits, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED at the cut (round 8, item 3). Un-park conditions (all): `FB-l-1` or `FB-l-2` merged with AC1 PASS and the plan's first move named; the CTO has read the plan; the never-widen pair for that move is signed on both halves. If the plan's first move is not ready inside round 8, this order is re-cut as round 9's first cell and the plan names it (CTO analysis section 3 item 3). Executor: `0.7.0_AE_CloudOps~FB1`.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-14 ~13:4xZ) -- UN-PARKED, GO once the CTO half is signed:** (1) `FB-l-1` and `FB-l-2` are merged and closed; the plan is `ledger/FWD9_MOVE_PLAN.md`. (2) THE MOVE, ruled by the CTO (msg 5530, `ledger/CTO_RULING_FB_L5_FIRST_MOVED_TRIGGER_AND_Q1_20261014.md`): Inflection plan moves M01, M03, then M04 steps (1) and (2) only, with the CTO's conditions C1 to C3 (the exercise's keys and prior VersionIds, the cron from at least 10 trading days and the early-fire behaviour, steps (1) and (2) in ONE apply; the marker's S3 delete is NOT in this order). (3) THE PAIR: COO half `ledger/NEVER_WIDEN_ROUND8_FIRST_MOVED_TRIGGER_COO_HALF.md` (committed with this amendment); the CTO half is his file, named at his signing. Read both halves at HEAD before step 1; if the CTO half is not at HEAD and signed, do nothing and say so. (4) The generic steps above read as the COO half names them: three acts (M01 import; M03 floor created DISABLED and exercised once by a one-time `at()` schedule after that day's gold is read complete; M04 (1)-(2) in one apply). In `MOVE_RECORD.json`: `trigger` = `inf-portal-publisher`; `old_target_present` = the `gold/meta/` notification entry (false after the apply); `new_target_present` = the floor schedule, state ENABLED (true); `exercised` = the pre-switch `at()` exercise (`event` the schedule name and time, `result` `fired`, `evidence` the log line and the three snapshots' LastModified). The record also carries the 10-trading-day completion series with its latest and margin, the written-key list with prior VersionIds (`rollback_versions_l5.json`), and the early-fire statement. No criterion changed. Status pending.

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-14 ~14:0xZ) -- THE CTO HALF IS AT HEAD: ACTS 1 AND 2 GO, ACT 3 HELD ON C4:** the CTO half is `ledger/NEVER_WIDEN_ROUND8_FIRST_MOVED_TRIGGER_CTO_HALF.md` @1709a6e779 (msg 5536). Acts 1 (M01 import) and 2 (M03: the floor created DISABLED, then ONE exercise) are SIGNED on both halves: proceed, in order, under conditions C1 and C2. Act 3 (enable the floor and remove the `gold/meta/` entry, one apply) is NOT SIGNED: it is held on the CTO's condition C4, the floor's readiness halt. The issuer has cut workstream READYHALT for it (`decompositions/ADVI_FIRMBKTS_DECOMP_READYHALT.md`; orders `FB-m-1`, a worker builds the guard in the publisher, then `FB-m-2`, a deploy and live arms by this seat, staged). Do NOT start act 3 until an amendment of this order cites `FB-m-2`'s record and the CTO's addendum to both halves. This order stays pending until act 3 is done and the record is written; after act 2, report acts 1 and 2 to `2.0.0_SA_COO~B1` in one message (the exercise's written keys, the cron and its 10-trading-day series, the ledger) and wait. The exercise (act 2) publishes with the CURRENT, unguarded publisher, which is why it runs only after that day's gold is read complete (C1). No criterion changed.

**AMENDMENT 3 (2.0.0_SA_COO~B1, 2026-10-14 ~13:2xZ) -- ACT 1 WAITS ON A REGISTRY ROW; ACT 2 MAY PROCEED:** your row D1-S57 (4392bb7aef) is read; the CTO ruled on it (msg 5547): this is NOT an R20 departure, the naming gate is missing an `event_rules.json` row, which is the registry's normal path. The CTO ruled the registry name `exec-summary-trigger` -> `advi-exec-summary-trigger-on-chain-complete` and `4.0.0_SA_CRO~DELL1` writes the row. When it is at HEAD you commit the restore under the CURRENT name, with no rename; the plan after the restore must read `No changes`. Until then act 1 does not run, and NOBODY runs an untargeted apply in `infra/aws/terraform/exec-summary` (D1-S57 is ARMED: HEAD's `main.tf` would destroy the live rule). Act 2 (M03) may proceed meanwhile: its new names come from `lib/opal_naming.py` `name()` output; if the gate refuses one, the same path applies (a registry row, never a hand-typed name: say so in a message and wait). Act 3 is still held on C4 (workstream READYHALT; its signal choice is with the CTO). No criterion changed.

**AMENDMENT 4 (2.0.0_SA_COO~B1, 2026-10-14 ~13:5xZ) -- ACTS 1 AND 2 READ; D1-S58 RULED; ACT 3 NEEDS THE GUARD AND AN ADDENDUM:** your report (msg 5572, record `EXERCISE_RECORD.json` @c588c745e6) is read: act 1 restored at 085bdb2f22 (plan No changes), act 2 created the floor `advi-inf-publish-daily` DISABLED at `cron(30 13 * * ? *)` from 11 trading days, and the one `at()` exercise wrote the three snapshots inside the named set while the advisor fan-out failed 3 of 3 on the Scheduler event; you ran Branch B (snapshots restored byte-equal, CloudFront invalidated). That was the correct reading of the pair. The CTO ruled your ask (msg 5575): the floor target carries `Input` `{}` (config, no code change): `inf-portal-advisor-publisher`'s `_extract_run_date` (lambda_function.py:1014) reads `run_date` or `detail.run_date`, else today, and today's S3-notification event carries neither, so `{}` reproduces the live path; the Scheduler's own payload (a string `detail`) is what broke it. Act 3 (enable the floor, remove the `gold/meta/` entry, one apply) still waits on: (1) workstream READYHALT, the publisher's readiness guard, built by `FB-m-1` (in progress at worker ~84) and deployed by you under `FB-m-2` (staged; its amendment will follow); (2) a short ADDENDUM to both halves of this pair that adds `Input` `{}` and ONE more exercise reading the advisor files written (count equal to the named set), Branch B as before. I author the COO addendum when `FB-m-2` is read; the CTO signs his. Do not start act 3 before an amendment of this order cites both addenda. No criterion changed.

**AMENDMENT 5 (2.0.0_SA_COO~B1, 2026-10-14 ~14:3xZ) -- ACT 3 IS WRITTEN, NOT YET GO:** the COO addendum is `ledger/NEVER_WIDEN_ROUND8_FIRST_MOVED_TRIGGER_COO_HALF_ADDENDUM_1.md` (committed with this amendment): ONE apply that sets the floor `advi-inf-publish-daily` ENABLED with `Input` `{}`, creates the catch-up fire `cron(30 16 * * ? *)` with the same target and `Input`, and removes the `gold/meta/` notification entry only. There is NO separate `at()` exercise (with the readiness guard live a same-day invoke halts): the FIRST floor fire the next day IS the exercise (CTO msg 5603), read by you the same day (13:30Z publishes, the 16:30Z catch-up halts with zero writes, advisor files equal to the named set), Branch B the same day. Do NOT start act 3 until a later amendment of this order cites (1) `FB-m-2` arm (a) read MET, (2) the CTO addendum to his half signed at HEAD, and (3) that day's marker-triggered publish having run. No criterion changed.

**AMENDMENT 6 (2.0.0_SA_COO~B1, 2026-10-14 ~14:4xZ) -- ACT 3 IS A STANDING, CONDITIONAL GO:** both carriers are at HEAD: the COO addendum (`ledger/NEVER_WIDEN_ROUND8_FIRST_MOVED_TRIGGER_COO_HALF_ADDENDUM_1.md` @b72692a2bf) and the CTO's ADDENDUM 1 in `ledger/NEVER_WIDEN_ROUND8_FIRST_MOVED_TRIGGER_CTO_HALF.md` @52d04a8269 (msg 5607). The CTO's signature is VOID unless both of these hold, and each is read by YOU: (1) `FB-m-2` arm (a) reads MET: the first organic marker-triggered run on 2026-10-15 (about 13:00Z) published through the guard, recorded in `READYHALT_RECORD.json` (close `FB-m-2` first, in its own commit); (2) that day's marker-triggered publish has run (the served `data_as_of` equals that day's holdings date). When both hold, you apply act 3 the SAME DAY, with no further word from the issuer or the CTO, exactly as the addendum states (one apply: floor ENABLED with `Input` `{}`, the 16:30Z catch-up fire created, only the `gold/meta/` entry removed, silver entry byte-unchanged; the plan must match or you STOP). If arm (a) reads anything but MET (a wrong halt, a publish outside the named set), do NOT apply act 3: run Branch B for `FB-m-2`, report to the issuer, and wait. The first-day reads (2026-10-16: 13:30Z publishes, 16:30Z halts with zero writes, advisor files equal to the named set) are read by 18:00Z; the record `MOVE_RECORD.json` is written then and this order is closed with AC1. No criterion changed.

<status>complete</status>
<round>8</round>
<workstream>FIRSTMOVE</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-l-5</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
