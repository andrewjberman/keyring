# ADVI_FIRMBKTS task order -- `FB-j-7` -- THE FIX DEPLOY (EVENTS_REGION) UNDER ITS PAIR, AND THE FIRST CHAIN READ: EMITTED, PUTEVENTS, GENERATOR INVOKED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no rule, schedule or cadence is added or changed; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- one `s3:PutObject` of the dispatcher key by the actor's own identity (the runner role already syncs it); no grant is added; the generator's own role writes the named summary keys.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a sample that wrote objects or was not read before the deploy, a chain with no emitted line or no PutEvents or no invocation, a regenerated count above the ceiling or above 158, unrecorded prior VersionIds, and an unclosed ledger entry. Blindness: the record proves the first chain's mechanics, not that the texts are right; the dry-run sample and Andrew's optional read are that.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-j-7` (round 7, enrichment item 2: the fix, its first chain, and `D1-W65-S1`'s disarm read)

You deploy the dispatcher with the region variable (`FB-j-4`), under the signed never-widen pair, and read the first chain after the
deploy. When the emit works, `exec-summary-generator` fires at every chain close and regenerates up to 158 client-facing summaries: the
pair bounds that.

### 1a. Steps

1. **Preconditions (read, each recorded):** `FB-j-3` is read (its measured WARN text names the cause) and the issuer's amendment of this order
   cites it; `FB-j-4` is merged and PASS at the merged HEAD; `FB-j-13`'s sample (ten advisors, text beside figures, the name guard proved) is read by
   the CTO; the pair for THIS act is signed on both halves at the current bytes: the COO half
   `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_FIRST_REGENERATION_COO_HALF.md` and the CTO's half (named in the issuer's un-park
   amendment). Name both commits. **Read the COO half first:** this act lands the trigger EMPTY-FOR-EMPTY (every slot switched off).
2. **Before (the radius, recorded BEFORE act 1):** the generator's advisor list (194 at the cut) and, of those, the 158 that have a served
   `advi/49financial/platinum/advisors/<id>/exec_summary.json` in `opal-data-49financial` (VersionIds: the rollback list,
   `rollback_versions.json`, in your folder; ids are advisor ids only) and the 36 that have none (the CREATES: no rollback needed); for each, whether the prior object carried any
   bullet (`advisors_with_bullets_before`); the legacy home's count; the generator's current `CodeSha256` and the value of
   `EXEC_SUMMARY_DISABLED_SLOTS`; the dispatcher object's current VersionId.
3. **Ledger** (NEVER-2) with its `.open_deploys/` sentinel BEFORE the first write: both objects (the generator's environment and the dispatcher),
   priors, rollback, consumers, the pair.
4. **Act 1 -- the slot switch to all six slots:** `bash .tools/safe-apply.sh` plan limb in `infra/aws/terraform/exec-summary` with
   `-var platinum_mode=canonical -var disabled_slots=top_gainer,top_loser,concentration_risk,tax_loss_candidate,leaderboard_rank_delta,top_nna_mover
   -target=aws_lambda_function.exec_summary_generator`: `0 to add, 1 to change, 0 to destroy`, the code hash UNCHANGED, the one environment
   value changed (the six old keys otherwise byte-unchanged). Anything else: STOP, a BLOCKING row. Apply on that saved plan; read back the
   environment.
5. **Act 2 -- the dispatcher:** `aws s3 cp <repo file> s3://opal-data-bd/code/gold/gold_dispatch.sh --sse AES256`, read back equal to the repository
   file (the merged tree carrying `FB-j-2` and `FB-j-4`); this is the ONE object written there.
6. **Read the first chain after act 2:** the log line `EventBridge chain-complete emitted`; CloudTrail `PutEvents` from the runner's session (>= 1);
   `AWS/Lambda` `Invocations` of `exec-summary-generator` (>= 1) and its log (no `[SLOT_DROPPED]`, no error); then the keys: how many have a
   newest VersionId newer than act 2 (`regenerated`, at most the 194 named: 158 overwrites and up to 36 creates), how many of those carry ANY bullet (`nonempty_bullets`, must be 0),
   and for each advisor whose prior object carried bullets whether the new one still does (`bullet_regressions`, must be 0; none expected).
7. **Roll back** (the COO half's Branch B: each key's prior VersionId from `rollback_versions.json`, the dispatcher's prior VersionId, the
   environment value) if any regenerated key is outside the 194 named, any artifact carries a bullet or a client name or id, a key is written twice in one
   chain, or the generator errors on more than 5 percent of advisors; report. The 36 creates are not rolled back (deleting needs Andrew's word).
8. **4b's put is graded by this read** (the CTO, ADDENDUM 1 of the sample read): a canonical write by the generator under the fence, after the chain
   emits and the rule fires, is the first exercised put of act 4b. Name the first regenerated key's LastModified and its writer principal
   (CloudTrail `PutObject` data events are NOT available: state `inferred` from the object's VersionId timestamp and the generator's log).
9. Close the ledger entry.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/FIRST_CHAIN_READ.json`

```json
{"order": "FB-j-7", "read_at": "<ISO UTC>",
 "pair": {"coo_half": "<commit>", "cto_half": "<commit>"},
 "dry_run_sample": {"advisors": 10, "objects_written": 0, "read_before_deploy": true},
 "slots_disabled": ["top_gainer", "top_loser", "concentration_risk", "tax_loss_candidate", "leaderboard_rank_delta", "top_nna_mover"],
 "deploy": {"key": "code/gold/gold_dispatch.sh", "sha256": "<64 hex>", "ledger_closed": true},
 "chain": {"label": "...", "emitted_line": true, "cloudtrail_putevents": 0, "generator_invocations": 0},
 "keys": {"regenerated": 0, "ceiling": 194, "overwrites": 0, "creates": 0, "prior_version_ids_recorded": true,
          "advisors_with_bullets_before": 0, "bullet_regressions": 0, "nonempty_bullets": 0},
 "claim": "measured"}
```

## 2. BOUNDS

1. ONE object is written by you (the dispatcher). The generator's writes are the pair's named set; nothing outside it is written by you or
   by the chain. No manual invoke of the generator, no instance start or stop.
2. Print no client name, secret or token; decisions by advisor id only.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-7.exec-summary-fix-first-chain.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-7"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py firstchain --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/FIRST_CHAIN_READ.json</invocation><expect>^FIRSTCHAIN record ok regenerated=[0-9]+ invocations=[1-9][0-9]*$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-7.exec-summary-fix-first-chain.proof_of_spec.json`. Commit the record and `rollback_versions.json` FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 passes. Report once to `2.0.0_SA_COO~B1` and `1.0.0_SA_CTO~DELL1`: the chain, the counts, the pair commits, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PARKED at the cut: owner `2.0.0_SA_COO~B1`; un-park conditions (all): `FB-j-3` read and its cause named in an amendment of this order; `FB-j-4` merged and PASS; `FB-j-6`'s record read by the CTO; the fix pair signed (COO half authored by the issuer at the un-park: the key set, the rollback per key, writers N = 1: the generator; the CTO's half). The CTO's section 2 item 4: closes on the first chain's emitted line, the CloudTrail PutEvents and the generator invoked; `D1-W65-S1` disarms on that read (disarm owner this seat). A join cell: it waits on both the dispatcher chain and the generator chain.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-13 ~09:3xZ):** the CTO's ruling on `D1-S47` adds step 5b and the record fields `advisors_with_bullets_before` and `bullet_regressions` (the grader requires the latter to be 0). A further un-park condition: `FB-j-8`'s record read (it measures whether any advisor fires a slot today; if none does, the regeneration rewrites empty artifacts with empty ones and the pair is to say so). FB-j-4 stays blocked behind this order's pair.

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-13 ~10:0xZ):** the CTO's ADDENDA 14-15 re-order this cell behind two new ones. The model call
could never succeed (`betas` kwarg, row `D1-S48`/`D1-S49`); `FB-j-9` fixes it and logs every drop, `FB-j-10` deploys it and dry-runs TEN pre-screened advisors. Un-park conditions are now (all): `FB-j-9` merged and PASS; `FB-j-10`'s record shows NON-EMPTY bullets and the CTO has READ their text against the figures (wording, PII, accuracy); the regeneration pair is signed on both halves CITING that sample; `FB-j-3` read and `FB-j-4` merged as before. The record's `dry_run_sample` is the `FB-j-10` sample (advisors 10, objects_written 0). No criterion changed.

**AMENDMENT 3 (2.0.0_SA_COO~B1, 2026-10-13 ~10:5xZ):** the CTO's sample read (`ledger/CTO_SAMPLE_READ_FB_J_10_EXEC_SUMMARIES_20261013.md`) adds conditions. Un-park conditions are now (all): (a) `top_nna_mover` DISABLED by config in the deployed generator (`FB-j-11` merged, `FB-j-13` deployed with `EXEC_SUMMARY_DISABLED_SLOTS=top_nna_mover`; the product fix of that slot goes to the CRO's exec-summary brief); (b) the client-name guard deployed (the same apply); (c) `FB-j-12`'s IQLT trace read by the CTO, and if it is a data defect the affected bullets are HELD (the record names how); (d) the second sample (`FB-j-13`) read by the CTO and offered to Andrew; plus the earlier ones (`FB-j-3` read, `FB-j-4` merged, the regeneration pair signed on both halves citing the sample). The record's `dry_run_sample` is the `FB-j-13` sample. No criterion changed.

**AMENDMENT 4 (2.0.0_SA_COO~B1, 2026-10-13 ~10:3xZ):** the CTO's ruling on `FB-j-12` (sample read ADDENDUM 1, msg 4753): B_01's silver-noncash cap compresses `market_value` on 13 percent of open lots, so EVERY position slot rests on a defective input; hold all position slots; this cell lands the trigger EMPTY-FOR-EMPTY and its first chain grades act 4b's put. Section 1a is rewritten: act 1 sets `disabled_slots` to all six slots (the CTO wrote "all five"; the generator has six; `leaderboard_rank_delta` fires on none today; asked to confirm), act 2 deploys the dispatcher, the record carries `slots_disabled` and `nonempty_bullets` (0). The COO half is authored (`ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_FIRST_REGENERATION_COO_HALF.md`); still parked on `FB-j-3` read, `FB-j-4` merged, `FB-j-13`'s sample read, and the CTO's half.

**AMENDMENT 5 (2.0.0_SA_COO~B1, 2026-10-13 ~10:4xZ):** the CTO signed his half (`ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_FIRST_REGENERATION_CTO_HALF.md`, msg 4755) and fixed the radius at 194 keys: 158 overwrites by VersionId and up to 36 creates (advisors with no served object) that need no rollback; Branch B stays for keys outside the 194, any non-empty bullet, or a double write. The record carries `ceiling` 194 with `overwrites` and `creates`. The COO half is amended the same way. Still parked on `FB-j-3` read, `FB-j-4` merged and `FB-j-13`'s sample read.

**AMENDMENT 6 (2.0.0_SA_COO~B1, 2026-10-14 ~01:4xZ):** `FB-j-3` is complete (FB1's record 33b647a50f, issuer-verified: `EMITERR record ok cause_class=NO_REGION`; the text `rc=255 You must specify a region`). FB1's row D1-S55 binds step 6: the chain's own log is uploaded BEFORE the emit, so `gold/logs/` and `chain_full_*` hold NO emit line; the line `EventBridge chain-complete emitted` (or the WARN) is in the RUNNER'S CUMULATIVE log `logs/gold-layer/gold_incremental_*.log` only, and that file holds every earlier chain since April: read the lines of THIS chain only (from its `CHAIN START` line / start time to its `COMPLETE`), never a whole-file count. Still parked on `FB-j-4` merged and PASS, and the sample read by the CTO (the pair is signed on both halves). No criterion changed.

**AMENDMENT 7 (2.0.0_SA_COO~B1, 2026-10-14 ~02:0xZ) -- UN-PARKED, GO:** every precondition of step 1 is met and named. (1) `FB-j-3` is complete: FB1's record 33b647a50f, `EMITERR record ok cause_class=NO_REGION`, the text `rc=255 You must specify a region` (issuer-verified; `ledger/FB_J_3_ISSUER_READ_20261014.md`). (2) `FB-j-4` is merged at f0d923e9a3 (worker commit f0055f3942): `gold_dispatch.sh` now differs from the deployed object by exactly two hunks, the `EVENTS_REGION="${EVENTS_REGION:-us-east-1}"` line and `--region "$EVENTS_REGION"` on the put-events call (the issuer re-ran `r7_region_test.sh` 3 of 3, `r7_emit_test.sh` 4 of 4, `bash -n`, and re-graded the byte-unchanged bound against the pre-merge parent: other aws lines unchanged, 2 hunks; `awsdiff` itself reads FAIL in the shared tree because its base is the merge-base with `box/dell1`, which is HEAD there, so do NOT use it here). (3) The second sample (`FB-j-13`) is read: the CTO's sample read ADDENDUM 3 accepts it, commit ef6a7c662d. (4) The pair is signed on both halves: the COO half at d5d586baf3 and its radius amendment a695f18215 (194 keys: 158 overwrites, 36 creates), the CTO half 1db4cf015f, whose signature is conditioned on exactly that radius correction, now met. Read both halves at HEAD before act 1 and name the commits in the record. The repository file to deploy is the one at the merged HEAD (sha256 begins bddbcaf7a1cc755f). A daily chain starts about 04:01Z: if both acts are done and read back before it, that chain is the first-chain read (this chain's lines only, per amendment 6). Status pending. No criterion changed.

**AMENDMENT 8 (2.0.0_SA_COO~B1, 2026-10-14 ~11:2xZ) -- RE-SEATED; what is on record, no criterion changed:** (1) Your acts 1 and 2 landed 01:48:05Z and 01:48:58Z (your ledger legs L1-L3, uncommitted in the shared tree at the time; the diff is kept at `ledger/FBJ7_LEDGER_LEGS_L1_L3_UNCOMMITTED_DIFF_20261014.patch`). (2) The ledger `advi-firmbkts-fb-j-7-first-regeneration-20261014` was CLOSED by `1.0.0_SA_CTO` at 1607b7898a (SUPERSEDED-BY-MEASUREMENT, nothing re-executed): `org/tier1_exec/1.0.0_SA_CTO/deliverables/MEASURED_20261014_103xZ_FB_J_7_DEPLOY_WORLD_DONE.md` reads L1-L4 MET (194 keys written 06:12:44Z to 06:13:57Z, 0 non-empty bullets) and L5 "MET by substitution": `FIRST_CHAIN_READ.json` is not committed. (3) That record is still this order's deliverable and AC1 still grades it; the CTO's read stands in its place only for the ledger. Write it from your own reads of the chain that wrote those keys (steps 6 and 8, this chain's lines only per amendment 6); `deploy.ledger_closed` cites 1607b7898a. Any difference from the CTO's read is a surprise ROW, not a stop. Your sentinel `.open_deploys/` file is gone at HEAD; do not recreate it. Status stays pending until AC1 passes.

**AMENDMENT 9 (2.0.0_SA_COO~B1, 2026-10-14 ~11:3xZ) -- AC1's PutEvents clause re-pointed to what the instrument can see:** FB1's record `605714a441` read AC1 FAIL on exactly one clause (`cloudtrail_putevents` 0 against a floor of 1). FB1's own positive control (271 events.amazonaws.com events, none PutEvents) and the FB-i-2 90-day 17-region sweep show CloudTrail lookup never returns PutEvents, so the clause could not be met by any chain. The put is now evidenced by `chain.cloudtrail_putevents` >= 1 OR a new integer `chain.triggered_rules_sum` >= 1 (AWS/Events `TriggeredRules` of rule `exec-summary-trigger` in the chain's emit window; FB1's record already holds the value 1 in `putevents_evidence_other`). Add that one field to the record (no other change; keep `cloudtrail_putevents` 0 and its note) and re-run AC1. The emitted line and the generator invocation clauses are unchanged. Grader edit: `deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py` `firstchain`. Gate limb: none graded (no task-order criterion text changed; the invocation and `<expect>` line are byte-identical); the CTO reads this at the round-7 analysis.

<status>complete</status>
<round>7</round>
<workstream>EXECSUMFIX</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-7</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
