# TO MDPF_HEALGAP.TO-HG-d3 -- round 1, the one real run of FWD-1: make one morning's Cottonwood Rebalancer pull fail, watch it heal the same day (laptop)

<to_id>MDPF_HEALGAP.TO-HG-d3</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.7.0_AE_CloudOps~F</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>DEPLOY-FWD1</workstream>

**Directive:** D8 | **Fabric:** laptop (project placement dell1; THIS act on the laptop) | **Decomp cell:** `HG-t-1`, `HG-t-2`
(`decompositions/MDPF_HEALGAP_DECOMP.md`, the issuer's drain act 4: "The one real run of FWD-1") | **outcome_ref:** FWD-1 |
**depends_on:** `MDPF_HEALGAP.TO-HG-d2` (complete)

**GO condition (all, read on the trunk):** `MDPF_HEALGAP.TO-HG-d2` reads `complete` with its act-0 SKIP probe passed and HG1-d2-AC1 `WIRED-OK` (CTO half condition 1); both never-widen halves SIGNED in
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/NEVER_WIDEN_HALF_REQUEST_HEALGAP_FWD1_EXERCISE_20261008.md`. The issuer flips
`<status>` to `pending`. Exercise date D = 2026-10-08; if the GO lands after 05:50Z that day, the GO commit amends D to the next date.

---

## WORKER FACE

### THE CELL

FWD-1: on a day the morning Cottonwood model pull fails because the vendor login has lapsed, a reader of the Cottonwood models sees that
day's figures by the end of the same day, with nobody acting. DONE WHEN EXERCISED: one morning pull deliberately made to fail, followed
to that day's figures. The runner (`cot-rebalancer-runner`, HG-t-1 build) raises an HTTP 401 before any secret read or vendor call when
its event carries `"induce": "auth-lapse"`; the re-attempt target on `cot-bronze-complete` (HG-d2) re-runs it at ~11:32Z. Andrew's
standing word (ACT 1, @e5fb41862f) covers this exercise.

**Act, on the exercise date D (UTC), with CHECKPOINT_DISABLE=1 for any terraform and WITHOUT MSYS_NO_PATHCONV:**
0. Open a change-management ledger entry naming this order, the laptop, the rule `cot-rebalancer-runner-daily` and date D.
1. Before 05:50Z on D: `aws events list-targets-by-rule --rule cot-rebalancer-runner-daily` (exactly one target), then
   `aws events put-targets --rule cot-rebalancer-runner-daily` re-putting THAT target (same Id, same Arn) with
   Input `{"mode":"pull","induce":"auth-lapse"}`. Read it back; print it in the ledger.
2. After 06:05Z and before 06:20Z on D: re-put the same target with Input `{"mode":"pull"}`; run HG1-d3-AC3. Then
   `terraform plan -target=aws_cloudwatch_event_target.cot_rebalancer_runner_daily` in `infra/aws/terraform/opal-assets` must read
   no change (CTO half condition 3). Time-stamp both put-targets and the plan in the ledger (condition 2). Close nothing yet.
3. Do NOT touch anything at ~11:32Z: the heal must happen with nobody acting.
4. After 13:00Z on D: run HG1-d3-AC1 and HG1-d3-AC2. If AC2 reads BAD after 18:00Z, the half's branch (B) remedy applies: ONE invoke of
   `cot-rebalancer-runner` with `{"mode":"pull"}` for D, recorded in the ledger, and the report says FWD-1 was NOT realized for D.
4b. Record in the ledger whether the date's served Cottonwood figures were in place by 13:30Z (CTO half condition 4): the
   newest silver/gold write time for D under the existing `on_success` chain against 13:30Z, MET or MISSED.
5. Close the ledger entry and commit it (exact pathspec; never another seat's sentinel, row MDPF_HEALGAP-S6).

### ACCEPTANCE

<criterion id="HG1-d3-AC1" cell_refs="HG-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_fwd1_exercise.py --failed 2026-10-08</invocation><expect>FAILED-OK</expect></criterion>
`HG1-d3-AC1` -- the 06:00Z pull of D failed as induced and wrote nothing before 11:00Z (D = 2026-10-08; if the GO lands after 05:50Z on D, the issuer amends D in the GO commit).

<criterion id="HG1-d3-AC2" cell_refs="HG-t-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_fwd1_exercise.py --healed 2026-10-08</invocation><expect>HEALED-OK</expect></criterion>
`HG1-d3-AC2` -- D healed the same day with nobody acting: a complete-stamp written after 11:00Z naming all three feeds, each feed non-empty.

<criterion id="HG1-d3-AC3" cell_refs="HG-t-1"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R1_CHECKS/hg_fwd1_exercise.py --restored</invocation><expect>RESTORED-OK</expect></criterion>
`HG1-d3-AC3` -- the 06:00Z rule's target is back to `{"mode":"pull"}`. A fourth criterion would be redundant: the reader's page read is the issuer's at close.

<expected_criteria>HG1-d3-AC1 HG1-d3-AC2 HG1-d3-AC3</expected_criteria>

Base 2026-10-07 ~14:3xZ (dell1): AC1 BAD, AC2 BAD (not run), AC3 OK. Controls on 2026-10-07 (a normal day): AC1 BAD
(never induced), AC2 BAD (stamp written 06:00:58Z, before 11:00Z).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- The only AWS writes: two `put-targets` on `cot-rebalancer-runner-daily` (input only, same target), and on branch (B) only, one
  Lambda invoke. No terraform apply, no other rule, function, IAM or S3 write.
- **Refusal clause.** If a step or criterion cannot be met as written, stop, restore the input (step 2), write the reason and the
  row's `spec_asserts` / `world_is` in your report; `0.0.0_AB_MSTR` carries the row and the issuer files it.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/MDPF/MDPF_HEALGAP/ledger/
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 1, the thread), cells `HG-t-1`,
`HG-t-2` (the issuer's drain act 4: the one real run of FWD-1).
<owned_cells>HG-t-1 HG-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG1-d3-AC1, HG1-d3-AC2, HG1-d3-AC3. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.7.0_AE_CloudOps~F/MDPF_HEALGAP.TO-HG-d3.fwd1-exercise-induced-morning-failure.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG1-d3-AC1,HG1-d3-AC2,HG1-d3-AC3 --governing-order <this file>` BEFORE the flip.
</proof_of_spec>

**REPORT:** the ledger entry path, both put-targets read-backs, the three checks' output, any branch (B) act, commits, push state.

---

## RECORD FACE

<preflight>
comp-schedule: RUN by reading -- the act changes ONE fire's input of cot-rebalancer-runner-daily (cron(0 6 * * ? *)) and restores it within ~25 minutes; AC3 reads the restore.
comp-iam: DECLARED-NOT-APPLICABLE no grant moves; the seat's own events:PutTargets and lambda:InvokeFunction are the laptop's.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
risk: WORLD -- a deliberate production failure of one morning's pull and one vendor re-pull (Andrew ACT 1 @e5fb41862f). Never-widen halves CTO + COO before the GO; change-management entry by the seat.
direct_act: false -- WORLD.
</preflight>

Workstream DEPLOY-FWD1: round 1's drain act 4 (the one real run), on the laptop seat that holds HG-d1/HG-d2; write surface the ledger only.

Source: PRD v0.1 @78db344481 ENDPOINT FWD-1 (DONE WHEN EXERCISED) and section 2 hop 1; decomposition round 1, drain act 4.
