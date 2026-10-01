# AMGT_RESAPP task order -- `AMGT-ah-2` -- THE CODE-ONLY REDEPLOY OF THE NAME FIX (every bubble named for a person)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ah-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one redeploy by hand.
comp-iam: RUN by the issuer at the cut -- the name fix adds no read the role lacks: the classifications GetItem is the read read_rankings already makes; resolve_identity reads the packaged crosswalk. The plan must show NO IAM change. BLIND: no IAM simulation was run for the classifications-table GetItem on opal-amgt-scoped-api-role (1 action, 1 table not simulated); it is exercised live by AC1 (a denied read leaves names on the ticker fallback, which C2 still passes -- so AC1 cannot see that denial; the executor reads name_source counts from the deployed body and reports them: 7 classification at the cut).
comp-adversary: RUN by the issuer at the cut -- AC1 FAILS at the base against the deployed function (C0 unmoved; C2: 32 of 95 rows serve the raw key); PASSES on the issuance tree locally (0 of 95; 63 crosswalk / 7 classification / 25 ticker; counts unmoved).
EGRESS CLASS, declared: NONE for the acts; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-ah-2` (round 58, decomposition s.66)

ONE act, under ONE NEVER-2 entry and ONE never-widen pair: redeploy `opal-amgt-scoped-api` at the commit the issuer's GO names,
carrying ah-1 (`lib/research/api/monthly_chatter.py`: crosswalk name -> classifications name -> display ticker, with `name_source` on
every row) and any rider the halves list.

**Begin only when all hold:**
- the GO names the build commit;
- both halves are committed: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round58/NEVER_WIDEN_HALF_COO_AH2.md` and
  `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND58_AH2_CTO_HALF.md`;
- the base CodeSha256 the halves name (`/HInwjrnGBzDLzV2EnYyGFseCcXIuWC/ddnyYUpUEX8=`) is still live, re-read immediately before the
  build. A moved base is a STOP and a re-sign.

**The acts, in order, under the entry opened AND COMMITTED first:**
1. `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round58/checks/bg_names.py --what pre --out org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ah2-pre.json`.
2. Build and upload the ONE artifact at the GO commit, recording the prior S3 VersionId (`RhEQ661Bi9gnVKhBphUCMtjH_rrsscPS` at the
   cut). Save the `CONTENT-DIFF` printout. STOP if a CHANGED/ADDED/REMOVED file is outside the halves' list.
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

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ah-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round58/checks/bg_names.py --where deployed --pre org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ah2-pre.json; echo "exit=$?"</invocation><expect>C0 PASS (CodeSha256 and LastModified moved off the printed pre values); C1-C5 PASS on the deployed function; EVERY COVERED BUBBLE IS NAMED FOR A PERSON: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ah-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round57/checks/ag_1_served.py --what post --pre org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ah2-pre.json; echo "exit=$?"</invocation><expect>C0 PASS; FWD-32, FWD-33 and FWD-34 still YES on the deployed function (no regression); THE DEPLOYED FUNCTION SERVES THE FRIDAY FEED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ah-2.the-name-fix-redeploy.proof_of_spec.json`.
Report once: the prior and new CodeSha256 and S3 VersionId, the CONTENT-DIFF summary, the plan's resource count, both criteria's
output lines, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-57 analysis enrichment item 1 (CTO msg 27675 ruling; row Z-S331). Ruling 3's deploy-act list is
decomposition s.66a. AC2 is the regression guard on round 57's outcomes. Positive arm: `bg_names.py --where local` YES on the
issuance tree.

<status>pending</status>
<round>58</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-01 ~10:0xZ):** ACCEPTED. Executor proof `174cf144e9` (AC1, AC2 PASS; entry CLOSED; artifact RhEQ661... -> hj5ITKr5Ct9Mn3ySEvztrK9eG.bnsHho; CodeSha256 /HInwjrn... -> g9H0TW2g...). The BLIND classifications read measured ALLOWED off the deployed body (classification 7 / crosswalk 63 / ticker 25). Issuer's independent read 09:5xZ: names YES, regression YES (`round58/ah2_issuer_*_read.out`).

<status>complete</status>
