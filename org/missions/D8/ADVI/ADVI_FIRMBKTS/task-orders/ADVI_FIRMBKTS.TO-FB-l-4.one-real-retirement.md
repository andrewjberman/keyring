# ADVI_FIRMBKTS task order -- `FB-l-4` -- FWD-9(b): THE ONE REAL RETIREMENT, BY RECORDED DECISION, AFTER A LIVE CONSUMER CENSUS READS ZERO

<!-- ===================== WORKER FACE -- this is the WHOLE of the executing seat's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R8.md</decomp_doc>
<owned_cells>FB-l-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the order adds no cron or cadence of its own; the act is named in an amendment at the un-park and is re-declared there.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is added by this order as cut; any grant the named act needs is stated in the un-park amendment and its pair, and `comp-iam` is run then.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a record with an unsigned or missing pair, an unclosed ledger entry, no recorded rollback, and (a consumers_before count that is not 0 with a denominator above 0, an after_read that does not read the target absent). Blindness: the grader proves the record's discipline, not that the act was the right one; the CTO's exercised read is that.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-l-4` (round 8, WORLD)

STAGED. This order is the one real retirement of FWD-9(b): ONE legacy operation, retired by a recorded decision, after a live consumer census reads zero. It waits; it is not a standing GO.
You act only after the issuer's UN-PARK AMENDMENT (in this file's record face), which names (1) the target, taken from `FB-l-3`'s record (`first_zero_consumer`, or the candidate the CTO
names in its place), (2) the CTO's decision record for it, and (3) the signed never-widen pair (COO half and CTO half, commits named). Until that amendment exists, do nothing.

### 1a. Steps (once un-parked)

1. **Preconditions (read, each recorded):** `FB-l-3` is merged and its AC1 is PASS; the CTO's decision record for the target exists at the cited commit; the pair is signed on both halves at the
   current bytes; the target is NOT the Door 6 marker, its S3 notification, `mdpf-feeder-accelerator` or the `router_iam` Door 6 deny (those wait for `inf-portal-publisher`'s new trigger).
2. **Re-census immediately before the change:** repeat the target's consumer census exactly as `FB-l-3`'s record states its calls, now. `consumers` must read 0 with `scanned` above 0.
   Any live consumer is a STOP and a BLOCKING row; nothing is changed.
3. **Ledger** (NEVER-2) with its `.open_deploys/` sentinel BEFORE the first write: the target, its prior state (a saved copy of the definition, or the VersionId), the rollback and its test.
4. **The change:** exactly the one change the pair names (a disable-then-delete is two steps in one change; nothing else moves). Terraform only through `bash .tools/safe-apply.sh`; a repository removal is
   a commit through `.tools/safe-commit.sh`.
5. **Read back:** the target reads ABSENT (or disabled and unreferenced, as the pair names), the same census calls still read 0 consumers, and nothing else changed (the plan or the list of
   resources before and after).
6. **Rollback test:** where the pair names one that does not affect the world, run it on the saved definition; otherwise state it `held`.
7. Close the ledger entry.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/RETIRE_RECORD.json`

Write the record as one JSON file at that path; its shape is fixed by the grader `C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round8/checks/r8_checks.py` (`retire`). Every value carries `claim` as `measured`, `inferred`, `held` or `absent`; print no
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

</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-l-4.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-l-4"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round8/checks/r8_checks.py retire --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/RETIRE_RECORD.json</invocation><expect>^RETIRE: OK target=.+ consumers=0$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-l-4.proof_of_spec.json`. Commit the record FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report once to `2.0.0_SA_COO~B1` and `1.0.0_SA_CTO~DELL1`: what changed, the read-back, the pair commits, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED at the cut (round 8, item 2). Un-park conditions (all): `FB-l-3` merged and PASS; the CTO names the target in a decision record (the CTO's answer to the census); the never-widen pair for the named change is signed on both halves (COO half authored by the issuer at the un-park, naming the blast radius and the rollback per resource). The Door 6 retirement is NOT this order (it follows `inf-portal-publisher`'s new trigger, CTO ruling on D1-W80-S1, msg 5482). Executor: `0.7.0_AE_CloudOps~FB1`.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-14 ~12:5xZ) -- UN-PARKED, GO once the CTO half is signed:** (1) `FB-l-3` is merged (9977d91265) and closed (7440f2ec7e); AC1 and AC2 re-run by the issuer. (2) THE TARGET, named by the CTO in msg 5509: candidate C3, the DISABLED EventBridge rule `inf-gold-full-on-bronze-complete` (rule plus its one target plus its invoke permission plus the one line in the DLQ policy; `inf-gold-trigger` itself and `inf-canonical-prices-daily` are NOT in the act; the Door 6 items C4 to C6 are NOT in the act). (3) THE PAIR: COO half `ledger/NEVER_WIDEN_ROUND8_FIRST_RETIREMENT_C3_COO_HALF.md` (committed with this amendment); the CTO half is his file, named at his signing. Read both halves at HEAD before step 1; if the CTO half is not at HEAD and signed, do nothing and say so. The decision record is the COO half's first section (target, why, what replaced it: nothing that fires on this key). (4) The act is ONE Terraform change in `infra/aws/terraform/inf-pipeline/`, scoped by `-target` to the four addresses the COO half names; the plan must read `0 to add, 1 to change, 3 to destroy` or you STOP. Step 2's re-census reuses `FB-l-3`'s calls for candidate C3. The record `RETIRE_RECORD.json` takes `target` = `inf-gold-full-on-bronze-complete`. No criterion changed. Status pending.

<status>pending</status>
<round>8</round>
<workstream>RETIREMENT</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-l-4</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
