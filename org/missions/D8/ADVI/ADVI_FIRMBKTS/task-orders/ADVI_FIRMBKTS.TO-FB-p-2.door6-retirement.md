# ADVI_FIRMBKTS task order -- `FB-p-2` -- THE DOOR 6 RETIREMENT, IN THE CTO'S ORDER: the catch-up and the feeder's second look first, the marker write last

<!-- ===================== WORKER FACE -- this is the WHOLE of the executing seat's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R9.md</decomp_doc>
<owned_cells>FB-p-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the one AWS Scheduler resource this order adds is a production cadence for an existing function, not a gate carrier; the order's holds (the un-park after D1's read, the wait for the first live fire) live in this file and in the signed pair, and no new future-check promise is created outside them.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is added: the new schedule reuses the existing scheduler role `mdpf_feeder_scheduler` and its policy, and the fence Deny `DenyInfGoldSentinelAbsolutely` is left as it is.
comp-adversary: RUN by the issuer (`compose` on this order, read-vintage 2026-10-16T19:53Z, HEAD @0472e7db88): every cited commit and path verified; the only absent cited paths are the record and the proof instance the executor creates. At base the record is absent (AC1, AC2 and AC3 FAIL as expected). The grader (self-test, 68 arms) rejects a schedule off its cron or plan, an apply outside the Sunday-to-Monday window, an accelerator disabled before the first live fire, a per-date re-dispatch, a filled gap date, a deployed copy that did not change, a diff beyond the marker block, a census with errors or a reader, steps out of order, an unsigned pair, no rollback and an open ledger. Blindness: it proves the record's shape, not that the reads in it are true; the issuer and the CVO read the objects.
EGRESS CLASS, declared: NONE.
</preflight>

## 0. THE HOLD -- read this first

This order is `staged`. **You do nothing while `<status>` reads `staged`.** The issuer sets it to `pending` (the un-park) after D1 reports its read of the 2026-10-17 13:30Z fire (CTO msg 6983: that fire carries one change, so no feeder write lands before it). Then you act, in the order of section 1.

## 1. THE ACT -- `FB-p-2` (round 9, item 1 of the CTO's enrichment list, second half; WORLD)

Andrew's ruling (`ANDREW_DIRECT_20261013_200xZ_NINE_OPEN_CALLS_ANSWERED_FIRMBKTS_DEMQUE_BRIEF_HARVEST.md` row 1, DEC-13 Door 6): RETIRE the Inflection done-marker `opal-data-inf/gold/meta/pipeline-complete.json` and its watcher `mdpf-feeder-accelerator`; "there is no successor marker". The CTO's order of steps and its erratum 1 are in `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/CTO_DECISION_DOOR6_RETIREMENT_ORDER_20261016.md`: read all of it first. The signed never-widen pair for acts A and B1 below: COO half `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_DOOR6_FEEDER_SECOND_LOOK_AND_CATCHUP_COO_HALF.md` @8e1b650b9e (sha256 `6d54f7a4be2d6560bf474d2ae8f762793d42cdd7dc2bd28b4e01868c419d8bdc`), CTO half `..._CTO_HALF.md` @156165f766. Read the COO half in full: it holds the blast radius, both branches and the rollback per key, and an unmeasured change to anything it states voids it. The live census that dropped the CTO's step 1: `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/DOOR6_LIVE_READER_CENSUS_20261016.md`.

### 1a. Steps, in this order (each its own section of the record)

1. **Preconditions (read, each recorded):** `<status>` is `pending`; the pair is signed at those bytes (re-hash the COO half and compare the sha256 above); `mdpf-feeder-accelerator` is ENABLED and `mdpf-feeder-backstop-daily` is ENABLED (`cron(52 12 * * ? *)`); the registered ledger entry is open (NEVER-2, with its `.open_deploys/` sentinel) BEFORE the first write. STOP on any difference.
2. **B1, the current-date catch-up (the pair's act B1; record section `catch_up`).** Record every existing same-date VersionId in the 49 Financial feed families the dispatch can overwrite, and read the writer of those families first (pair section 4): STOP if a same-date key exists and the writers differ. Then invoke `mdpf-feeder-trigger` once with the event `{}` (today UTC), read `dispatched: true` and the `ssm_command_id`, and read that SSM command to `Success`; then invoke `mdpf-gold-lambda` once with the event `{"floor":"mdpf-scheduled-floor","run_class":"production","source":"aws.events"}` (the floor schedule's own input); read the floor's log for `wrote s3://.../_aggregate_aua/<date>.json` or the A7 refusal. **Never re-dispatch a past date; never fill 2026-10-13 to 10-16** (CTO msg 6986): list `s3://opal-data-assets/gold/mdpf_revamp/_aggregate_aua/` afterwards with its object count and record that those four dates are still absent.
3. **A, the second look (the pair's act A; record section `second_look`).** In `infra/aws/terraform/mdpf-pipeline/feeder-trigger.tf` add ONE `aws_scheduler_schedule` on the default group, `schedule_expression = "cron(8 13 * * ? *)"`, UTC, flexible window OFF, the same target block as `mdpf_feeder_backstop` (the same function, scheduler role and DLQ), no static input. Its name comes from the naming builder (`lib/opal_naming.py name()`); a builder refusal is a missing row in `infra/logic/registry/` to add, never a hand-typed name (CLAUDE.md rule 30). `terraform plan` must read exactly `add=1 change=0 destroy=0`; STOP on any other. Apply through `bash .tools/safe-apply.sh` **between 2026-10-18T13:09:00Z and 2026-10-19T13:00:00Z**, so Monday 2026-10-19 is the first live day. Read the schedule back ENABLED.
4. **Read the first live fire, then disable the accelerator.** After the 2026-10-19 13:08Z fire, read the trigger's log for that fire (`dispatched` or `NOT-YET`; a NOT-YET is read with its looked-for key). **Only then** change `mdpf_feeder_accelerator` in the same `.tf` file to `state = "DISABLED"`; the plan must read `add=0 change=1 destroy=0`; apply through `safe-apply`; read `events describe-rule` back DISABLED. Do not delete the rule.
5. **Re-run the live census, then stop the writer (record section `marker_writer`).** Immediately before the writer change, run `python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/door6_live_reader_census.py --out <your record folder>/CENSUS_RERUN.json` and record its denominators (`errors` 0 and `hits_reading_key` 0 once you read each hit line, as the issuer did: comments, docstrings and registry JSON are not readers). **A live reader found is a STOP and a BLOCKING row**: it gets its own step before this one. Then stop the marker write in the DEPLOYED copy `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh`, located by CONTENT (the block headed "Chain-complete sentinel -- ADVI_INFETL.002" and the text `pipeline-complete.json`), never by a line number: the repo file's lines differ from the deployed file's. **The repo copy is not the deployed copy** (the repo file carries other projects' undeployed edits), so do NOT deploy the repo file as it stands. Procedure: (i) download the deployed object, record its VersionId and sha256; (ii) in a throwaway linked worktree of the current branch, overwrite `data/inf/scripts/gold/orion-gold-dispatch.sh` with the deployed bytes and change only the success-branch marker write inside that block (the failure branch and `pipeline-failed.json` stay); `bash -n` the file; `diff` it against the deployed bytes and record that the diff touches that block alone; (iii) from that worktree run `bash .tools/safe-deploy.sh data/inf/scripts/gold/orion-gold-dispatch.sh` (no `--allow-stale`); read the S3 object's sha256 equal to the file's; remove the worktree; (iv) make the SAME block change in the repo source `data/inf/scripts/gold/orion-gold-dispatch.sh` in a normal commit so the next real deploy keeps it. The staging and rebuild copies (`code/gold-staging/`, `code/rebuild/`) read as manual-only (census ledger section 5.1): do not edit them; they change at their source on their next deploy, and a stray write is harmless (zero readers; the fence Deny stands). **Do not delete the marker object**: that is an S3 delete and waits on Andrew's word as a separate act.
6. **Prove the writer stopped:** after the next gold chain day, read the marker's version history: no new version. Until then report steps 1 to 5 and wait. Close the ledger entry.
7. **Roll back** (pair section 5, per key) if anything outside the named set changes, a consumer breaks, or the backstop stops starting its target.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DOOR6_RETIREMENT_RECORD.json`

```json
{"order": "FB-p-2", "read_at": "<ISO UTC>", "census_ref": "<DOOR6_LIVE_READER_CENSUS.json and its commit>",
 "decision": {"text": "<the recorded decision>", "replaced_by": "<the second look, or nothing>"},
 "steps": {
  "catch_up": {"done_at": "<ISO UTC>", "d1_read_ref": "<where D1 reported its 10-17 read>", "date": "<YYYY-MM-DD>", "dispatch_command_id": "<ssm command id>",
               "dispatch_status": "Success", "floor_rerun": "wrote | A7-refused", "prior_versions_recorded": true, "per_date_re_dispatch": false,
               "listing_denominator": 0, "gap_after": {"2026-10-13": "absent", "2026-10-14": "absent", "2026-10-15": "absent", "2026-10-16": "absent"}},
  "second_look": {"done_at": "<ISO UTC of the apply>", "schedule_name": "<builder output>", "expression": "cron(8 13 * * ? *)", "plan": "add=1 change=0 destroy=0",
                  "readiness_check": "<file:line of the gate test in the trigger>", "schedule_state_after": "ENABLED", "first_fire_at": "<ISO UTC>",
                  "first_fire_outcome": "dispatched | NOT-YET", "accelerator_state_before": "ENABLED", "accelerator_state_after": "DISABLED",
                  "accelerator_plan": "add=0 change=1 destroy=0", "accelerator_disabled_at": "<ISO UTC>"},
  "marker_writer": {"done_at": "<ISO UTC>", "census_rerun": {"done_at": "<ISO UTC>", "functions_listed": 0, "zip_scanned": 0, "errors": 0, "hits_reading_key": 0},
                    "deployed_copy_path": "code/gold/orion-gold-dispatch.sh", "deployed_sha256_before": "<hex>", "deployed_sha256_after": "<hex>",
                    "diff_only_marker_block": true, "repo_source_changed": true, "located_by_content": true, "stopped": true, "marker_object_deleted": false,
                    "gold_staging": "<what you read about what runs it>", "rebuild": "<what you read about what runs it>",
                    "evidence": "<no new marker version after the chain day of D>"}},
 "pair": {"coo_half": "<commit>", "cto_half": "<commit>"},
 "rollback": {"recorded": true, "how": "<the exact steps>"}, "ledger_closed": true, "claim": "measured"}
```
`replaced_by` is the word `nothing` or a name; the decision text states which.

## 2. BOUNDS

1. The act touches exactly: the new schedule and the accelerator's `state` in `feeder-trigger.tf`; one invoke each of `mdpf-feeder-trigger` and `mdpf-gold-lambda`; the new feed and aggregate keys those two runs write; the deployed `code/gold/orion-gold-dispatch.sh` and its repo source (the marker block only); the ledger and the record. Anything else is a STOP and a BLOCKING row.
2. `terraform` only through `bash .tools/safe-apply.sh`; deploy only through `bash .tools/safe-deploy.sh`; AWS from bash is `.tools/aws`; a deploy opens a ledger entry (`org/critical_paths/`) BEFORE the first write and closes it at completion (CLAUDE.md NEVER-2). Print no secret, client name, advisor or dollar value beyond the aggregate totals the floor already logs.
3. `mdpf-feeder-backstop-daily`, the S3 notification entry on `opal-data-inf`, the publisher floor, the fence Deny `DenyInfGoldSentinelAbsolutely`, the `code/gold-staging/` and `code/rebuild/` objects, and every existing S3 object are NOT touched. No delete of any kind.
4. The window in step 3 and the order of steps 4 and 5 are the CTO's; the grader checks them.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/mdpf-pipeline/
infra/logic/registry/
data/inf/scripts/gold/orion-gold-dispatch.sh
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-p-2.door6-retirement.proof_of_spec.json` (named by this file's whole stem).
  <criterion id="AC1" cell_refs="FB-p-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 60 python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/checks/r9_checks.py door6retire --part catch --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DOOR6_RETIREMENT_RECORD.json</invocation><expect>^DOOR6RETIRE: OK part=catch date=.+ floor=.+$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-p-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 60 python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/checks/r9_checks.py door6retire --part look --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DOOR6_RETIREMENT_RECORD.json</invocation><expect>^DOOR6RETIRE: OK part=look schedule=.+ first_fire=.+$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-p-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 60 python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/checks/r9_checks.py door6retire --part stop --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DOOR6_RETIREMENT_RECORD.json</invocation><expect>^DOOR6RETIRE: OK part=stop replaced_by=.+$</expect></criterion>
</proof_of_spec>

AC1 grades the catch-up section, AC2 the second look and the accelerator, AC3 the census re-run and the writer; together they grade the record's shape and the CTO's order.

## 5. WHEN YOU ARE DONE

Commit the record FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1, AC2 and AC3 pass. Report once to `2.0.0_SA_COO~B1` and `1.0.0_SA_CTO~DELL1`: the catch-up and the first-fire reads, the accelerator and writer changes, the pair commits, AC1 to AC3 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED at the cut (round 9, item 1). **AMENDMENT 1 (`2.0.0_SA_COO~B1`, 2026-10-16 ~19:5xZ):** the face now carries the CTO's order with his erratum 1 (msgs 6975, 6978, 6980, 6983, 6986, 6996, 7000): his step 1 (idempotency to its own record) is dropped because the deployed `inf-gold-trigger` never reads the marker (row `D1-S61`) and the live census found no reader; the signed pair's acts A and B1 are steps 2 and 3 here; the writer is stopped in the DEPLOYED copy by the throwaway-worktree procedure because the repo file differs from it. The AC1 grader mode `door6retire` changed shape (three `--part` modes; self-test 68 arms in `deliverables/2.0.0_SA_COO~B1/round9/`). The un-park (this file's `<status>` to `pending`) waits for D1's report of its 2026-10-17 13:30Z fire read; the issuer sets it. Executor: the one dell1 ADVI CloudOps lane (rule 34), `0.7.0_AE_CloudOps~FB1` live and idle at the cut. The plan's M04 steps 1 and 2 landed in `FB-l-5`.
**UN-PARKED (`2.0.0_SA_COO~B1`, 2026-10-17 ~13:5xZ, amendment 2):** D1's report of the 13:30Z fire read arrived (msg 7552); the record is committed at 882da2f5f8 (`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/real_run/FIRE_READ_20261017.md`), read by this seat in full. The un-park condition holds; `<status>` is now `pending`. No criterion, step or bound is edited. Two reads carried to the executor: (a) D1's message says the catch-up "for 10-13..10-16 is clear to land"; this order governs and is unchanged: the catch-up is the CURRENT date only, and 2026-10-13 to 10-16 are never filled (CTO msg 6986). (b) The record shows Global refused on 2026-10-16 (gate (v), five legs with `model_value=None`) and the feeder chain undispatched since 2026-10-12; step 2 records the Global keys and the 10-16 feed versions as found, and reports what the current-date dispatch changes beside them.

<status>pending</status>
<round>9</round>
<workstream>DOOR6</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-p-2</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
