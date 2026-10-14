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

<status>staged</status>
<round>8</round>
<workstream>FIRSTMOVE</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-l-5</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
