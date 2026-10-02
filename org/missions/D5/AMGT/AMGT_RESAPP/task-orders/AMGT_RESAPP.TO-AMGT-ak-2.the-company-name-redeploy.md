# AMGT_RESAPP task order -- `AMGT-ak-2` -- THE CODE-ONLY REDEPLOY OF THE COMPANY NAME (every price bar and bubble carries a company name)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ak-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one redeploy by hand, before 11:13Z if it can.
comp-iam: RUN by the issuer at the cut -- the new step reads `derived/model_block/<key>/` (one listing + one GET), the read the overlay's `header_figures` already makes live on every name. The plan must show NO IAM change. BLIND: no IAM simulation was run for this act (0 new actions); AC1's C1-C3 read the served names directly, so a denied read shows as an unnamed row.
comp-adversary: RUN by the issuer at the cut -- AC1 FAILS at the base against the deployed function (C0 unmoved; C1 24 of 94 unnamed on both price rankings; C2 RMS_FP_Equity unnamed; C3 25 of 95 chatter rows by ticker); PASSES on the issuance tree locally; FAILS locally with the step removed (--mutant).
EGRESS CLASS, declared: NONE for the acts; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-ak-2` (round 61, decomposition s.69)

ONE act, under ONE NEVER-2 entry and ONE never-widen pair: redeploy `opal-amgt-scoped-api` at the commit the issuer's GO names,
carrying ak-1. In `lib/research/api/scoped_amgt.py` and `lib/research/api/monthly_chatter.py`, a row the classifications table and the
crosswalk leave unnamed takes its own model block's header `NAME`, on the price rankings, the overlay and the chatter set.

**Begin only when all of these hold:**
- the GO names the build commit;
- both halves are committed: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round61/NEVER_WIDEN_HALF_COO_AK2.md` and
  `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND61_AK2_CTO_HALF.md`;
- the base CodeSha256 the halves name (`UnSqZgCDkSxM3J3roY8d+iVGZp+8JB1XnM/phfZrmeo=`) is still live, re-read immediately before the
  build. A moved base is a STOP and a re-sign.

**The acts, in order, under the entry opened AND COMMITTED first:**
1. `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round61/checks/b1_names.py --what pre --out org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ak2-pre.json`.
2. Build and upload the ONE artifact at the GO commit with `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`, recording the
   prior S3 VersionId (`1DFcRU3xDzUsi84yZnWv985DDF1MymMn` at the cut). Save the `CONTENT-DIFF` printout. STOP if any file other than
   `lib/research/api/scoped_amgt.py`, `lib/research/api/monthly_chatter.py` and `org/standards/NAMING_SCHEMA.json` is CHANGED/ADDED/REMOVED.
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
  <criterion id="AC1" cell_refs="AMGT-ak-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round61/checks/b1_names.py --where deployed --pre org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ak2-pre.json; echo "exit=$?"</invocation><expect>C0 PASS; C1-C4 PASS on the deployed function (0 of 94 rows unnamed on TRENDING/PRICE and on BREAKOUT/PRICE; RMS_FP_Equity named; 0 of 95 chatter rows by ticker; the RMS overlay serves the row's name); EVERY PRICE BAR AND BUBBLE CARRIES A COMPANY NAME: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ak-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round60/checks/aj_overlay_name.py --where deployed --pre org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ak2-pre.json; echo "exit=$?"</invocation><expect>C0-C4 PASS on the deployed function (every ranked row's overlay display_name equals the row's; AMD and TSM named; the identity block unchanged); EVERY BAR OPENS ONTO ITS OWN NAME: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ak-2.the-company-name-redeploy.proof_of_spec.json`.
Report once: the prior and new CodeSha256 and S3 VersionId, the CONTENT-DIFF summary, the plan's resource count, both criteria's
output lines, and RMS_FP_Equity's ranked `name` read off the deployed body. Name any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DSGN r21 analysis section 3B cell B1 (issuer ruling R1, decomposition s.69). AC2 is round 60's overlay-equals-row
check, a regression guard (ak-1 adds the same step to the overlay). The round-57 Friday-feed check is not re-run here: ak-1 touches
no figure, rank or percent field. Positive arm: `b1_names.py --where local` YES on the issuance tree; `--mutant` FAIL.

<status>staged</status>
<round>61</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

**ISSUER GO (2.0.0_SA_COO~Z, 2026-10-02 ~07:20Z):** build commit `63e78fe4f7` (the CTO half @02d032ee67 signed at it; the COO half @f234d5aa12). Build from a worktree at that commit: HARVST drain `fdd7442696` changed `lib/opal_data_harvest/` after it. GO message to `0.7.0_AE_CloudOps~A` 07:20:45Z.

<status>pending</status>
