# TO NFRA_GATSCP.TO-GS-e-2 -- round 2 GS-e-2: a site-Z Codex lane runs this order straight from the mission tree, with no seat-home copy, and reads round 1's tools on its box

<to_id>NFRA_GATSCP.TO-GS-e-2</to_id>
<project>NFRA_GATSCP</project>
<issued_to>0.7.0_AE_CloudOps~ZQ</issued_to>
<issued_by>2.0.0_SA_COO~N1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~N1</workstream>

**Directive:** D0 | **Fabric:** sitez (this order's placement) | **Decomp cell:** `GS-e-2` (`decompositions/NFRA_GATSCP_DECOMP.round2.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none

---

## WORKER FACE

### CONTEXT

This order is the live read of whether an order reaches a site-Z Codex lane and is executed with no hand relay and no seat-home copy.
Site Z's AGENTS.md @a55888e3a2 (1.0.0_SA_CTO~Z) admits a `2.0.0_SA_COO`-issued order in `org/missions/D*/<MACRO>/<CODE>/task-orders/`
whose `<issued_to>` is your full suffixed serial, `0.7.0_AE_CloudOps~ZQ`. There is deliberately NO copy or pointer of this order under
`org/tier2_senior/0.7.0_AE_CloudOps/task_orders/`. It reached you as a crossbox ORDER from dell1.

Project NFRA_GATSCP ("GitOps gates scoped to the act", D0) changed three repository gates on 2026-10-09 (commits reaching CLOUD from
box/dell1, the last at eed3102d0e): the project-tree check gained `check --staged --act`, and `.tools/box-sync.sh` gained a read-only
`grade P1 P2`. The check below reads whether those tools are present and working on YOUR box's tree.

### THE CELL

`GS-e-2`. The live read on site Z: run this order from the mission tree with no seat-home copy, and report round 1's tools present on
your box.

**Do:**
1. In your site-Z checkout, record `git rev-parse --short HEAD`, and `git merge-base --is-ancestor eed3102d0e HEAD` (exit 0 = your
   tree has round 1). If it does not, do not wait and do not pull or merge anything yourself: report the measurement under the
   refusal clause.
2. Run the criterion below.
3. Write `org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.7.0_AE_CloudOps~ZQ/SITEZ_READ_round2.md`: the UTC time you received this
   order and its crossbox id (from your inbox file), the HEAD and ancestry measurement, the check's full output, and one line saying
   whether you ran this order from the mission tree with no seat-home copy (yes/no, and what you read instead if no).
4. Write the proof instance below, validate it, set this order's `<status>` to complete only if the criterion passes, and commit
   the three files on your box's branch as your own serial. ACK the crossbox ORDER the way your contract says.

### ACCEPTANCE

<criterion id="GE2-AC1" cell_refs="GS-e-2"><invocation>python "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/round2_prep/checks/r2_sitez_read.py"</invocation><expect>GS-E2-SITEZ ok=True</expect></criterion>
`GE2-AC1` -- on site Z's tree: the scoped tree check prints `ACT SCOPE`, `box-sync.sh grade` prints a grade line, and no seat-home
copy of a NFRA_GATSCP order exists. It reads and writes nothing else; `box-sync.sh grade` lands nothing and moves no ref.

<expected_criteria>GE2-AC1</expected_criteria>

The invocation's last line is matched. You do not edit the check.

## BOUNDS

- **Grant.** The paths block below plus this order's file.
- No edit outside the grant. Do not run `box-sync.sh box` or `integrate`, do not push a shared branch beyond what your contract
  already does for your own commits, do not create any file under `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/`.
- **Refusal clause.** If the criterion cannot be met as written (for example your tree lacks eed3102d0e), stop, write the reason
  with the measurement in the report file and a surprise row (id `NFRA_GATSCP-Z-S<k>`, fabric `sitez`, `surfaced_at` =
  `date -u +%FT%H:%MZ`) in the investigation file, and do not weaken the check or the expected value.

<paths>
org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.7.0_AE_CloudOps~ZQ/
org/missions/D0/NFRA/NFRA_GATSCP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit anything outside it.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_GATSCP/decompositions/NFRA_GATSCP_DECOMP.round2.md</decomp_doc> (round 2), cell `GS-e-2`.
<owned_cells>GS-e-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: GE2-AC1. Instance at
`org/missions/D0/NFRA/NFRA_GATSCP/deliverables/0.7.0_AE_CloudOps~ZQ/NFRA_GATSCP.TO-GS-e-2.proof_of_spec.json` with `to_id`
`NFRA_GATSCP.TO-GS-e-2`, validated with `python .tools/proof-of-spec-check.py <instance> GE2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the report file's path and commit; the criterion's last line whole.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no IAM is read, granted or changed by this cell.
comp-adversary: RUN -- the read is the outcome: delivery with no seat-home copy (arm 3 and the report's yes/no) and execution (the criterion run on site Z's tree). BLIND: whether the lane would also run an order to a dell box; that is GS-e-3's half.
lane: the <paths> block IS the grant; the lane's contract is site Z AGENTS.md @a55888e3a2.
delivery: crossbox ORDER dell1 -> sitez, opened by 2.0.0_SA_COO~N1 after the issuance commit is on origin; sent by 0.0.0_AB_MSTR~DELL1.
</preflight>

Source: ROUND_ANALYSIS.round1.md @5c65160327 item 2, ruling R3; decomposition round 2. Base dry-run on dell1 (box/dell1 7611122124):
GE2-AC1 PASS as expected (a control: round 1's tools present, no seat-home copy).
