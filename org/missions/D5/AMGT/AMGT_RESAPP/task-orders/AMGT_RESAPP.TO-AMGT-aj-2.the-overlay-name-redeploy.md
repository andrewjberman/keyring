# AMGT_RESAPP task order -- `AMGT-aj-2` -- THE CODE-ONLY REDEPLOY OF THE OVERLAY NAME (every bar opens onto its own name)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aj-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one redeploy by hand, before 22:00Z.
comp-iam: RUN by the issuer at the cut -- the overlay label reuses the classifications GetItem and the packaged crosswalk the ranking path already reads (both exercised live by round 59). The plan must show NO IAM change. BLIND: no IAM simulation was run for this act (0 new actions); AC1's C2/C3 read the served label directly, so a denied read shows as a mismatch against the row.
comp-adversary: RUN by the issuer at the cut -- AC1 FAILS at the base against the deployed function (C0 unmoved; C2: 94 of 94 overlays carry no display_name; C3 AMD/TSM unnamed); PASSES on the issuance tree locally (94 of 94 equal; identity block unchanged).
EGRESS CLASS, declared: NONE for the acts; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-aj-2` (round 60, decomposition s.68)

ONE act, under ONE NEVER-2 entry and ONE never-widen pair: redeploy `opal-amgt-scoped-api` at the commit the issuer's GO names,
carrying aj-1. In `lib/research/api/scoped_amgt.py`, `read_security_overlay` serves top-level `name` / `display_name` by the ranking's
own chain (classifications table -> crosswalk -> display ticker). The shared identity block is left untouched.

**Begin only when all of these hold:**
- the GO names the build commit;
- both halves are committed: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round60/NEVER_WIDEN_HALF_COO_AJ2.md` and
  `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND60_AJ2_CTO_HALF.md`;
- the base CodeSha256 the halves name (`E6PdHVFB9z1xUcvCRtNIALjgAaCzNtolAdzaKmCssvM=`) is still live, re-read immediately before the
  build. A moved base is a STOP and a re-sign.

**The acts, in order, under the entry opened AND COMMITTED first:**
1. `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round60/checks/aj_overlay_name.py --what pre --out org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/aj2-pre.json`.
2. Build and upload the ONE artifact at the GO commit, recording the prior S3 VersionId (`q0Vf.FzuGpVovbH.xb2dumggs4k5kMKB` at the
   cut). Save the `CONTENT-DIFF` printout. STOP if any file other than `lib/research/api/scoped_amgt.py` is CHANGED/ADDED/REMOVED.
3. ONE `safe-apply`, plan printed first, code only (source hash). Any destroy, IAM, route or gateway change is a STOP.
4. AC1, then AC2. Close the entry.

A failing criterion after the act is the ROLLBACK trigger: the prior artifact version through one code-only `safe-apply`.

## 2. BOUNDS

1. The act and nothing else. No store write.
2. Standing: no S3 delete, no vendor call, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1200)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aj-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round60/checks/aj_overlay_name.py --where deployed --pre org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/aj2-pre.json; echo "exit=$?"</invocation><expect>C0 PASS; C1-C4 PASS on the deployed function (every ranked row's overlay display_name equals the row's, 94 at the cut; AMD and TSM overlays carry the company name; the identity block unchanged, AMD/TSM MEASURED); EVERY BAR OPENS ONTO ITS OWN NAME: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aj-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round57/checks/ag_1_served.py --what post --pre org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/aj2-pre.json; echo "exit=$?"</invocation><expect>C0 PASS; FWD-32, FWD-33 and FWD-34 still YES on the deployed function (no regression); THE DEPLOYED FUNCTION SERVES THE FRIDAY FEED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-aj-2.the-overlay-name-redeploy.proof_of_spec.json`.
Report once: the prior and new CodeSha256 and S3 VersionId, the CONTENT-DIFF summary, the plan's resource count, both criteria's
output lines, and AMD's and TSM's overlay `name` read off the deployed body. Name any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-59 analysis enrichment item 1 (ruling 2). The deploy-act list is decomposition s.68a. AC2 guards against
regression on round 57's outcomes. Positive arm: `aj_overlay_name.py --where local` YES on the issuance tree; today's deployed overlays
(94 of 94 without display_name) are the base.

<status>pending</status>
<round>60</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
