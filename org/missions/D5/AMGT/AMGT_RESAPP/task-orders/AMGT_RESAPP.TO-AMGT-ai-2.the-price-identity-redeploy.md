# AMGT_RESAPP task order -- `AMGT-ai-2` -- THE CODE-ONLY REDEPLOY OF THE PRICE IDENTITY JOIN (every price bar opens and names a covered security)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ai-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one redeploy by hand, DEMO-BLOCKING, before 22:00Z.
comp-iam: RUN by the issuer at the cut -- the join reads the research_dossier/ listing (already granted; exercised live by the monthly route since ag-1) and the packaged crosswalk; the name fallback reuses the classifications GetItem measured ALLOWED at ah-2. The plan must show NO IAM change. BLIND: no IAM simulation was run for this act (0 new actions); AC1's C2/C3 read the served effect directly, so a denied listing would leave 62 rows unkeyed and FAIL C2.
comp-adversary: RUN by the issuer at the cut -- AC1 FAILS at the base against the deployed function (C0 unmoved; C2: 62 of 94 rows per axis unkeyed; C3: no row carries display_name); PASSES on the issuance tree locally (0 / 0 / 0, every key covered, score_pct kept).
EGRESS CLASS, declared: NONE for the acts; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-ai-2` (round 59, decomposition s.67)

ONE act, under ONE NEVER-2 entry and ONE never-widen pair: redeploy `opal-amgt-scoped-api` at the commit the issuer's GO names,
carrying ai-1. In `lib/research/api/scoped_amgt.py`, `read_rankings` keys each unkeyed ranked row by an exact ticker match against
the covered universe, names newly keyed rows from the crosswalk, and gives every row a `display_name`.

**Begin only when all of these hold:**
- the GO names the build commit;
- both halves are committed: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round59/NEVER_WIDEN_HALF_COO_AI2.md` and
  `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND59_AI2_CTO_HALF.md`;
- the base CodeSha256 the halves name (`g9H0TW2garLGS0zMoLmJgFQU8a/6ZJUGMwJaYFSkc/c=`) is still live, re-read immediately before the
  build. A moved base is a STOP and a re-sign.

**The acts, in order, under the entry opened AND COMMITTED first:**
1. `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round59/checks/ai_price_identity.py --what pre --out org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ai2-pre.json`.
2. Build and upload the ONE artifact at the GO commit, recording the prior S3 VersionId (`hj5ITKr5Ct9Mn3ySEvztrK9eG.bnsHho` at the
   cut). Save the `CONTENT-DIFF` printout. STOP if any file other than `lib/research/api/scoped_amgt.py` is CHANGED/ADDED/REMOVED.
3. ONE `safe-apply`, plan printed first, code only (source hash). Any destroy, IAM, route or gateway change is a STOP.
4. AC1, then AC2. Close the entry.

A failing criterion after the act is the ROLLBACK trigger: the prior artifact version through one code-only `safe-apply`.

## 2. BOUNDS

1. The act and nothing else. No store write; the 09-30 generation is not rewritten.
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
  <criterion id="AC1" cell_refs="AMGT-ai-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round59/checks/ai_price_identity.py --where deployed --pre org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ai2-pre.json; echo "exit=$?"</invocation><expect>C0 PASS; C1-C6 PASS for both TRENDING and BREAKOUT price on the deployed function (0 rows without security_key, 0 without display_name, 0 raw-key labels, every key covered, score_pct kept); EVERY PRICE BAR OPENS AND NAMES A COVERED SECURITY: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ai-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round57/checks/ag_1_served.py --what post --pre org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ai2-pre.json; echo "exit=$?"</invocation><expect>C0 PASS; FWD-32, FWD-33 and FWD-34 still YES on the deployed function (no regression); THE DEPLOYED FUNCTION SERVES THE FRIDAY FEED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ai-2.the-price-identity-redeploy.proof_of_spec.json`.
Report once: the prior and new CodeSha256 and S3 VersionId, the CONTENT-DIFF summary, the plan's resource count, both criteria's
output lines, and the per-axis counts of rows with a company `name` read off the deployed body. Name any row. The `<status>` flip is
the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-58 analysis enrichment item 1 (rulings 1-2; DEMO-BLOCKING). The deploy-act list is decomposition s.67a. AC2
guards against regression on round 57's outcomes. Positive arm: `ai_price_identity.py --where local` YES on the issuance tree; today's
deployed counts (62 / 94) are the base.

<status>pending</status>
<round>59</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
