# TO MDPF_SECHIST.TO-SH-t23 -- round 6 SH-t-23: FWD-9 QA replay of the deployed money-market rule

<to_id>MDPF_SECHIST.TO-SH-t23</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~22</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-23` (`decompositions/MDPF_SECHIST_DECOMP_R6.md`) | **outcome_ref:** FWD-9 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`SH-t-23` (FWD-9). Run the issuer's QA replay once and record it. The script `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R6_CHECKS/r6_fwd9_replay.py`
runs the DEPLOYED money-market rule (`data/etfs/scripts/gold/etf_positioning_gold.py`, the same git blob as the pin deployed to `etf-positioning-producer`)
over the real Bloomberg history for D = 2026-10-13, with SALXX and FXFXX blanked on D in an in-memory copy. Its S3 client refuses every call except
`get_object`, `list_objects_v2` and `head_object`, so it cannot write. It writes ONE local JSON file. You do not edit the script.

Your work: (1) run AC1 from the worktree root, writing the JSON to the deliverable path below; (2) run AC2 on that file; (3) write the proof-of-spec instance;
(4) report, in your final message, the two last lines the script printed and the `control`, `blank` and `fill` values for SALXX and FXFXX copied from the JSON.
The run takes about one minute; it is bounded by `timeout 120`. If AC1 prints `FWD9-QA-BAD <reason>`, report that line as is and file a surprise row; do not edit the script
or the JSON to make it pass.

### ACCEPTANCE

<criterion id="SH6-t23-AC1" cell_refs="SH-t-23"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R6_CHECKS/r6_fwd9_replay.py run 2026-10-13 org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~22/replay_out.json</invocation><expect>FWD9-QA-OK D=2026-10-13 arms=b,a,a2,c served_writes=0</expect></criterion>

<criterion id="SH6-t23-AC2" cell_refs="SH-t-23"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R6_CHECKS/r6_fwd9_replay.py verify org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~22/replay_out.json</invocation><expect>FWD9-QA-VERIFY-OK D=2026-10-13</expect></criterion>

<expected_criteria>SH6-t23-AC1,SH6-t23-AC2</expected_criteria>

AC2 FAILS at the base (no `replay_out.json` yet, `FWD9-QA-VERIFY-BAD cannot-read`); AC1 PASSES at the base (the instrument exists and is green; this cell's product is the recorded run, which AC2 grades).
Run each invocation from the worktree root. Do not edit anything under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/`.

## BOUNDS

- Write only the files in `<paths>`. Read only otherwise: no S3 or DynamoDB write, no Bloomberg call, no Lambda or Terraform change, no gold or pull run.
- Anything odd outside this cell: append ONE surprise row (dell1 id form `<CODE>-D1-W<n>-S<k>`) and keep working.
- Client-data bounds (0.0.0_AB_MSTR~DELL1, standing): never read, search, copy or `git show` any `org/**/W73_S*_EVIDENCE.json`, commits
  1ba8eafcda / f5645bb6e9, the ADVI_COTBKF ~74 / ~66 / ~70 cottonwood manifests, the IRPT_DASHBD tie-out files, or anything under
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/`. Search only inside the paths named here.

<paths>
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~22/replay_out.json
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~22/MDPF_SECHIST.TO-SH-t23.fwd9-qa-replay.proof_of_spec.json
org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R6.md</decomp_doc> (round 6), cell `SH-t-23`.
<owned_cells>SH-t-23</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH6-t23-AC1, SH6-t23-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~22/MDPF_SECHIST.TO-SH-t23.fwd9-qa-replay.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH6-t23-AC1 SH6-t23-AC2`
BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE reads existing scheduled output.
comp-iam: DECLARED-NOT-APPLICABLE dell1 read grants used in rounds 1-5 (opal-data-etfs, opal-data-portal-v2 read; lambda get-function-configuration).
comp-adversary: RUN -- the replay dry-ran green at the base 2026-10-14 ~13:1xZ (arms b, a, a2, c; 32 served cells compared; served prefix 67 objects before and after); BLIND: the live S3 state after that read.
risk: LOCAL (read-only AWS, one local file).
direct_act: true -- a single run of an issuer-authored instrument, under 300 lines, LOCAL.
</preflight>

Source: CTO round-5 analysis ADDENDUM 1 (@fa26b50ebc, corrected @f443ae70d2), msgs 5540, 5542, 5553. The cell is the replay half (ruling item 1). Item 2, the served-week read, is this seat's scheduled read and is not a cell.
