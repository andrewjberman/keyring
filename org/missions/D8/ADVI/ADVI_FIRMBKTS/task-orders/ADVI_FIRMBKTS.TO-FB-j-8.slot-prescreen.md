# ADVI_FIRMBKTS task order -- `FB-j-8` -- THE SLOT PRE-SCREEN: WHICH OF THE 158 ADVISORS FIRE A SLOT TODAY (OFFLINE, NO MODEL CALL), THEN ONE TARGETED DRY RUN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-8</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads and dry-run invocations only; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 list and get with the actor's identity; ONE conditional `lambda:InvokeFunction` of the deployed generator with `dry_run: true` (the pair's own act, round 7 FB-j-6 COO half c811a75e60 and CTO half 1cefc87595); no grant is added.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a pre-screen with a model call, a zero-fire record with no per-slot reason, a targeted dry run that returned no bullets while advisors fire (the positive control failed), more than 10 targeted ids and a slot count other than six. Blindness: the grader proves shape and discipline, not that the evaluators were called faithfully; the issuer re-runs the pre-screen on three advisors.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-j-8` (round 7; the CTO's ruling on row `D1-S47`, FB-j-6 CTO half ADDENDUM 2, msg 4731)

`FB-j-6`'s one dry run returned ten artifacts with ZERO bullets (no slot fired, no model call, 7 seconds). The issuer read the served
objects: the May artifacts of the same ten advisors also carry zero bullets (all legacy `exec_summary.json` objects are 304-311 bytes,
one version each), and the canonical copies (act 3) too. So today's empty pass is not a regression against May. The CTO's ruling:
the empty pass is NOT a sample; before any regeneration serves, find out whether ANY advisor fires ANY slot on today's canonical data, and
if some do, read their text through a targeted dry run (the positive control).

### 1a. Step 1 -- the offline pre-screen of ALL advisors (no model call, no write)

1. List the served prefix (`advi/49financial/platinum/advisors/<id>/exec_summary.json` in `opal-data-49financial`): the denominator (158 at the cut).
2. For EACH advisor id, with the DEPLOYED generator's own code (the artifact you built in `FB-j-6`, or `infra/aws/lambda/exec-summary-generator/` at
   the merged HEAD), run ONLY the trigger evaluators and the readers they use, in `canonical` mode, with NO model call: the six evaluators
   `evaluate_top_gainer`, `evaluate_top_loser`, `evaluate_concentration_risk`, `evaluate_tax_loss_candidate`,
   `evaluate_leaderboard_rank_delta` and `evaluate_top_nna_mover` (in `platinum_reader.py` and `exec_summary/trigger_eval.py`; read how
   `process_advisor` in `lambda_function.py` calls them and reproduce exactly that, up to but NOT including `_build_slot` / `_call_llm`).
   Record per slot how many advisors fire (non-empty return) and the number of advisors firing at least one.
3. **If NONE fire (advisors_firing_any 0): say why, per slot, with counts, from the code and the data.** Read each evaluator's gate: the
   threshold, the date window (does it require data dated within N days of today?), the minimum rows, the leaderboard delta field. For each
   slot print how many advisors fail which gate (for example: `positions rows present 158 of 158; flagged by concentration threshold 0.10:
   0`; `leaderboard rank delta needs two dated snapshots, found 1`). A `claim` per reason (`measured` from your counts, `inferred` otherwise).
   Do NOT change any evaluator, threshold or file.
4. Compare (one more read, still no model call): run the same evaluators against the LEGACY home for the same advisor ids (frozen at act 2,
   2026-10-12) and print the per-slot counts beside the canonical ones. A difference between homes is a finding (the canonical readers
   differ from the legacy ones); equal zeros mean the inputs, not the seam, are why nothing fires.

### 1b. Step 2 -- ONE targeted dry run, ONLY if step 1 finds advisors that fire

Pick up to 10 advisor ids that fire at least one slot (spread over the slots that fire). Invoke the deployed generator ONCE with
`{"dry_run": true, "advisor_ids": [<those ids>]}` (the pair covers dry-run-only invocations of at most 10 ids; no other invocation). Read
the returned artifacts: count bullets per advisor and per slot. Save them as `SLOT_DRYRUN_ARTIFACTS.json` in your folder (advisor ids and
amounts only; if an artifact carries a client name, record the count and withhold that artifact's text). List the served prefix before and
after: identical (0 objects written), else ROLL BACK to the prior artifact VersionId and report. If step 1 finds no advisor firing, DO NOT
invoke: record `second_dry_run.done` false.

### 1c. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SLOT_PRESCREEN.json`

```json
{"order": "FB-j-8", "read_at": "<ISO UTC>", "calls": ["aws s3api list-objects-v2 ...", "..."],
 "advisors": 158,
 "per_slot_fired": {"top_gainer": 0, "top_loser": 0, "concentration_risk": 0, "tax_loss_candidate": 0,
                    "leaderboard_rank_delta": 0, "top_nna_mover": 0},
 "per_slot_fired_legacy_home": {"top_gainer": 0, "top_loser": 0, "concentration_risk": 0, "tax_loss_candidate": 0,
                    "leaderboard_rank_delta": 0, "top_nna_mover": 0},
 "advisors_firing_any": 0, "targeted_ids": [],
 "no_model_call_in_prescreen": true,
 "zero_reason": "<per slot, with counts; empty only when advisors fire>",
 "second_dry_run": {"done": false, "bullets_returned": 0, "listing_before": 0, "listing_after": 0},
 "claim": "measured"}
```

Also write `SLOT_PRESCREEN.md` (one page, prose).

## 2. BOUNDS

1. Reads; at most ONE invocation of the deployed generator, `dry_run: true`, at most 10 ids. No non-dry invocation, no S3 write, no deploy,
   no rule change. No evaluator, threshold, prompt or code file is changed.
2. Print no secret, no client name, no account number; advisor ids and counts only.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-8.slot-prescreen.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-8"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py prescreen --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SLOT_PRESCREEN.json</invocation><expect>^PRESCREEN record ok advisors=[0-9]+ firing_any=[0-9]+ second_dry_run=(True|False)$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and discipline. The findings' truth is read by the issuer (a three-advisor re-run of the pre-screen) and the CTO.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-j-8.slot-prescreen.proof_of_spec.json`. Commit the record, the prose file and (if any) `SLOT_DRYRUN_ARTIFACTS.json` FIRST, your rows and the instance second; flip
`<status>` to `complete` in the SAME commit only when AC1 passes. Row ids `ADVI_FIRMBKTS-D1-S<k>`. Report once to `2.0.0_SA_COO~B1` and
`1.0.0_SA_CTO~DELL1`: per-slot counts, whether any advisor fires, the reason if none, the second dry run's bullets, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's ADDENDUM 2 of the FB-j-6 half (msg 4731): "(1) read the served May artifacts for the same 10 advisors; if they have
bullets, today's empty pass is a defect; (2) run the targeted dry run with offline pre-screen and no model call; it must return non-empty
bullets as the positive control; (3) FB-j-7 carries the criterion that no summary with bullets today is replaced by one with none, read per
advisor." Item (1) was read by the issuer at 08:5xZ: the same ten advisors' May objects (2026-05-04T16:43-44Z) and canonical copies
(2026-10-11T04:02Z) carry 0 bullets; the legacy version histogram over 152 objects is 304-311 bytes, one version each. The consequence the
issuer states: the "stale summaries" were empty artifacts all along, so a regeneration may rewrite 158 empty artifacts, and the open question is
product-side (why no trigger fires), not this project's; this order measures it. Item (3) is FB-j-7's new criterion (`keys.bullet_regressions` 0,
read per advisor). Class WORLD (a deployed function, dry-run only), reads otherwise.

<status>pending</status>
<round>7</round>
<workstream>SLOTPRESCREEN</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-8</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
