# ADVI_FIRMBKTS task order -- `FB-p-2` -- RETIRE THE DOOR 6 MARKER AND ITS WATCHER BY RECORDED DECISION, AND READ IT BACK

<!-- ===================== WORKER FACE -- this is the WHOLE of the executing seat's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R9.md</decomp_doc>
<owned_cells>FB-p-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the order removes a rule and adds no rule, schedule or cadence; the backstop schedule `mdpf-feeder-backstop-daily` is read, not changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is added; the one policy statement touched (`DenyInfGoldSentinelAbsolutely`) is named in step 5 and is a Deny, removed only after step 4.
comp-adversary: RUN by the issuer (`compose` on this order, read-vintage 2026-10-16 ~17:5xZ): any cited commit verified; the only absent cited paths are the record and the proof instance the executor creates. At base the record is absent (AC1 FAIL as expected). The grader rejects a rule that does not read ResourceNotFound, a marker copy not saved, a marker not reading 404, a writer not stopped with evidence, an unsigned pair, no recorded rollback and an unclosed ledger entry. Blindness: it proves the record's shape, not that nothing else read the marker; that is the census (`FB-p-1`) and the CTO's read of it.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-p-2` (round 9, item 1 of the CTO's enrichment list, second half; WORLD)

STAGED. You act only after the issuer's UN-PARK AMENDMENT in this file's record face, which names (1) the merged census `DOOR6_CENSUS.json` and the CTO's read of it, (2) the writer of the marker and the exact change that stops it (the census may leave this to the amendment), (3) the recorded decision, and (4) the signed never-widen pair, both halves, commits named. Until that amendment exists, do nothing.

Andrew's ruling (`ANDREW_DIRECT_20261013_200xZ_NINE_OPEN_CALLS_ANSWERED_FIRMBKTS_DEMQUE_BRIEF_HARVEST.md` row 1, DEC-13 Door 6): RETIRE the Inflection done-marker `opal-data-inf/gold/meta/pipeline-complete.json` and its watcher `mdpf-feeder-accelerator`; "there is no successor marker". Its condition (the marker not retired while `inf-portal-publisher` read it) is met: the S3 notification was removed on 2026-10-15 and the publisher runs on the Scheduler floor behind the readiness guard.

### 1a. Steps (once un-parked; the plan's move M04 steps 3 to 6, with the writer made explicit)

1. **Preconditions (read, each recorded):** the census is merged and read by the CTO; the pair is signed on both halves at the current bytes; the rule `mdpf-feeder-accelerator` is still ENABLED; the schedule `mdpf-feeder-backstop-daily` is ENABLED (`cron(52 12 * * ? *)`, it keeps starting `mdpf-feeder-trigger`); the marker exists.
2. **Before (recorded):** the rule's full definition and targets saved to the deliverables folder (the rollback); the marker object copied to a saved path (`s3api copy-object` to a key the amendment names, or a download to the deliverables folder) with its VersionId and ETag; the `opal-assets-one-way-fan-in-fence` policy's current document saved.
3. **Ledger** (NEVER-2) with its `.open_deploys/` sentinel BEFORE the first write.
4. **Stop the writer** exactly as the amendment names it (the change in the gold chain that writes the marker). Through Terraform only where Terraform owns it, through `bash .tools/safe-apply.sh`.
5. **Retire the watcher:** disable then delete the rule `mdpf-feeder-accelerator` (through Terraform when the repository declares it; otherwise the amendment says how). Read `events describe-rule` back: `ResourceNotFound`.
6. **The marker:** only after steps 4 and 5, with Andrew's word above, delete the marker object (a versioned bucket: the prior version is recoverable). Read `head-object` back: 404. Then, only after that, remove the Deny statement `DenyInfGoldSentinelAbsolutely` from the fence policy (the amendment confirms this step).
7. **Prove the writer stopped:** after the next gold chain day, read the marker's version history: no new version. Until then report steps 3 to 6 and wait.
8. **Roll back** (the saved rule definition, the saved marker copy, the saved policy document, the revert of the writer change) if anything outside the named set changes, a consumer breaks, or the backstop schedule stops starting its target. Close the ledger entry.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DOOR6_RETIREMENT_RECORD.json`

```json
{"order": "FB-p-2", "read_at": "<ISO UTC>", "census_ref": "<DOOR6_CENSUS.json and its commit>",
 "decision": {"text": "<the recorded decision>", "replaced_by": "nothing"},
 "steps": {"accelerator_rule": {"read_after": "ResourceNotFound"},
           "marker": {"copy_saved": true, "copy_path": "<where>", "read_after": "404"},
           "writer": {"stopped": true, "evidence": "<no new version after the chain day of D>"}},
 "pair": {"coo_half": "<commit>", "cto_half": "<commit>"},
 "rollback": {"recorded": true, "how": "<the exact steps>"}, "ledger_closed": true, "claim": "measured"}
```
`replaced_by` is the word `nothing` or a name; the decision text states which.

## 2. BOUNDS

1. The act touches exactly: the rule `mdpf-feeder-accelerator`, the marker object and its copy, the writer change the amendment names, the Deny statement (step 6 only), the ledger and the record. Anything else is a STOP and a BLOCKING row.
2. `terraform` only through `bash .tools/safe-apply.sh`; AWS from bash is `.tools/aws`; a deploy opens a ledger entry (`org/critical_paths/`) BEFORE the first write and closes it at completion (CLAUDE.md NEVER-2). Print no secret, client name or relationship id.
3. The S3 notification entry on `opal-data-inf` and the publisher floor are NOT touched (done in `FB-l-5`). `mdpf-feeder-backstop-daily` is NOT touched.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-p-2.door6-retirement.proof_of_spec.json` (named by this file's whole stem).
  <criterion id="AC1" cell_refs="FB-p-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 60 python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/checks/r9_checks.py door6retire --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DOOR6_RETIREMENT_RECORD.json</invocation><expect>^DOOR6RETIRE: OK steps=3 replaced_by=.+$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Commit the record FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report once to `2.0.0_SA_COO~B1` and `1.0.0_SA_CTO~DELL1`: the rule and marker reads, the writer change, the pair commits, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED at the cut (round 9, item 1). Un-park conditions (all): `FB-p-1` merged and its AC1 PASS; the CTO reads the census; the CTO's decision text ("nothing replaced it", or what did) is recorded; the writer and the stop-change are named; the never-widen pair for this act is signed on both halves (COO half authored by the issuer at the un-park). Executor: the one dell1 ADVI CloudOps lane (CLAUDE.md rule 34); `0.7.0_AE_CloudOps~FB1` today. The plan's M04 steps 1 and 2 landed in `FB-l-5`; this order is steps 3 to 6 plus the writer.

<status>staged</status>
<round>9</round>
<workstream>DOOR6</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-p-2</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
