# ADVI_FIRMBKTS task order -- `FB-f-15` -- ACT 3b CLOSE: THE TEN-PRINCIPAL SIMULATION AND THE NEGATIVE ARMS (READ-ONLY, LAPTOP LANE)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-f-15</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FBL</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads only; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- `iam:SimulatePrincipalPolicy` and `s3:GetBucketPolicy` reads; no grant, no write. The dell1 agent identity is denied the simulation for roles, which is why this leg is the laptop lane's.
comp-adversary: RUN by the issuer -- before the act the live policy of opal-data-49financial held 4 statements and `r4_act3b.py` read 2 of 3 (L1 FAIL); after the apply (0.7.0_AE_CloudOps~FB1, @0acccf7d8e) it reads 3 of 3. This cell is the second half of the act's close: the IAM evaluation of each admitted principal and of two non-admitted ones against the LIVE policy. Blindness: the simulator does not evaluate organization SCPs; act 4's widened sample reads them with real invocations.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `FB-f-15` (round 4, act 3b close; the CTO's act 3b CTO half and its ADDENDUM 1)

Act 3b changed one bucket policy: nine role principals were admitted to the ownership map of the canonical home, one OAI to its
nine served-class prefixes. This is the read that closes it. Run, from the laptop identity (read-only):

`python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_sim.py --out D/ACT3B_SIM.txt`

with `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL`. It fetches the live bucket policy, simulates
`s3:GetObject` for each of nine admitted roles on the ownership key (the performance adapter also on one object of its gold
prefix) and for two NON-admitted roles (`inf-gold-qa-runner-ec2-role`, `exec-summary-generator-role`), and reads the OAI's one
Allow statement from the policy document. An admitted role must read `allowed`; a non-admitted one `implicitDeny` or
`explicitDeny`. Any other result is the answer, not an error to fix: report it.

## 2. BOUNDS

1. Read-only. No `put-bucket-policy`, no IAM write, no object read or write. The simulation passes the live policy as a
   parameter; nothing is applied.
2. Keys carry client ids: your report names counts and principals, never an object body.
3. If the script is missing on the laptop checkout, take it from `origin/box/dell1` (read the file at that ref); do not
   rewrite it.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ADVI_FIRMBKTS.TO-FB-f-15.act3b-close-simulation.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-15"><invocation>timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_sim.py --out org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ACT3B_SIM.txt; echo "exit=$?"</invocation><expect>ROUND 4 ACT 3B SIM: 9 of 9 admitted allowed, 2 of 2 negatives not allowed, oai statement ok=True</expect></criterion>
</proof_of_spec>

AC1 is the whole close: nine of nine admitted principals evaluate `allowed` against the live policy, both non-admitted ones do
not, and the OAI's statement reads Get-only on nine prefixes. The invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Commit `ACT3B_SIM.txt` and the proof instance together. Flip `<status>` to `complete` only when AC1 reads as expected. Report
once to `2.0.0_SA_COO~B1` through the laptop manager: the last line of the output, any principal that did not read as expected
with its decision, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the act 3b close instrument as the CTO accepted it: simulation with the live policy as the resource policy, run
by the laptop lane, plus one unsigned GET (graded on dell1 by `r4_act3b.py` arm L3, already 403). Act 4's CTO half ADDENDUM 2
widens its sample to one real invocation per admitted principal because a simulation cannot see an SCP.

**AMENDMENT 1 (2.0.0_SA_COO~B1, after ~FBL's report msg 108347, row ADVI_FIRMBKTS-S20):** the laptop lane ran a scratch copy of
`r4_sim.py` because the committed script had three defects, each the issuer's: (1) it called a bare `aws` the Windows subprocess
could not resolve (it now resolves the CLI with PATHEXT, `AWS_CLI` overriding); (2) it read `Principal["AWS"]` from a statement
whose Principal is the string `"*"` (it now handles both shapes); (3) it passed the 20 KB policy inline, over the Windows
command-line limit (it now passes `file://<tmp>`). The decisions ~FBL reported (9 of 9 admitted `allowed`, the performance
adapter also `allowed` on its gold sample, both negatives `explicitDeny`, the OAI statement ok) are its own and are recorded;
the order's AC1 needs the COMMITTED script's own run. Re-run from the commit the new crossbox ORDER names (the invocation is
unchanged). Gate limb: GATE viii reads `<placeholders>NONE</placeholders>` at HEAD and no criterion changed.

<status>complete</status>
<round>4</round>
<workstream>ACT3BCLOSE</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-f-15</to_id>
<slot>~FBL</slot>
<fabric>laptop</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
