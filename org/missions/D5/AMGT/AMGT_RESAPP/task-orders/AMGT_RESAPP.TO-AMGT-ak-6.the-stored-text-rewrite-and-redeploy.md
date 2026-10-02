# AMGT_RESAPP task order -- `AMGT-ak-6` -- B2/B3/B4 SERVED: THE STORED-FIELD REWRITES THE FROZEN PLANS NAME, AND THE REDEPLOY CARRYING ak-3

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ak-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one rewrite and one redeploy by hand.
comp-iam: RUN by the issuer at the halves -- the writes are PutObject on `opal-data-harvest` keys under `management/v1/` and `posture/v1/` by the executor's own credentials (not the function's); the function gains no permission. The halves name the executor's write grant as measured.
comp-adversary: RUN by the issuer at the cut -- AC1-AC3 FAIL at the base against the deployed function (b2 C1 11 of 26; b3 C1/C2; b4 C1 2 of 12).
EGRESS CLASS, declared: NONE for the acts; the build pip-downloads its pinned wheels. No vendor or model call.
</preflight>

## 1. THE ACT -- `AMGT-ak-6` (round 61, decomposition s.69)

TWO acts under ONE NEVER-2 entry and ONE never-widen pair, in this order:
- **(A) the stored-field rewrite.** For every entry of the three FROZEN plans
  (`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~201/m1_lusha_reason_plan.json`,
  `.../0.9.0_WK_AMGT_RESAPP~202/m1_officer_plan.json`, `.../0.9.0_WK_AMGT_RESAPP~203/posture_claim_plan.json`, each at the sha256 the
  halves name): read the object at `store_key`, confirm `store_field` equals `before`, set it to `after`, and PUT the whole object back
  at the SAME key (the bucket is versioned). Record each key's prior VersionId. Two entries on one key are applied in ONE put.
- **(B) the redeploy** of `opal-amgt-scoped-api` at the build commit the GO names, carrying ak-3's serve-time peers reasons.

**Begin only when all of these hold:**
- the GO names the build commit and the three plans' sha256;
- both halves are committed: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round61/NEVER_WIDEN_HALF_COO_AK6.md` and
  `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND61_AK6_CTO_HALF.md`;
- each plan file's sha256 equals the halves'; any differing byte is a STOP and a re-sign.

**The acts, in order, under the entry opened AND COMMITTED first:**
1. `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round61/checks/b1_names.py --what pre --out org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ak6-pre.json`.
2. (A) per key: GET, assert every `before`, PUT the patched body; write `ak6_store_writes.json` in your deliverables dir (key, prior
   VersionId, new VersionId, fields set). An asserted `before` that differs is a STOP for that key and the act: write nothing more.
3. (B) build and upload ONE artifact; save the `CONTENT-DIFF`; STOP if a CHANGED/ADDED/REMOVED file is not on the halves' list. ONE
   code-only `safe-apply`, plan printed first; any destroy, IAM, route or gateway change is a STOP.
4. AC1-AC3. Close the entry.

A failing criterion after the act is the ROLLBACK trigger: for (A), copy each key's prior VersionId back over it (never an S3 delete);
for (B), the prior artifact version through one code-only `safe-apply`.

## 2. BOUNDS

1. The plans' keys and fields and the one redeploy, nothing else. No S3 delete, no vendor or model call.
2. Standing: no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ak-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round61/checks/b_served_text.py --cell b2 --where deployed; echo "exit=$?"</invocation><expect>C1 PASS (0 of the Lusha and peers absent reasons for BA and VLO carry a code-shaped token) and C2 PASS on the deployed function; B2 EVERY SERVED REASON IS WORDS: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ak-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round61/checks/b_served_text.py --cell b3 --where deployed; echo "exit=$?"</invocation><expect>C1, C2 and C3 PASS on the deployed function (VLO's officers carry person names and full titles with no trailing age; BA 12); B3 EVERY OFFICER CARRIES A FULL TITLE AND NO AGE: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ak-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round61/checks/b_served_text.py --cell b4 --where deployed; echo "exit=$?"</invocation><expect>C1 and C2 PASS on the deployed function (0 of BA's and VLO's posture claims carry a status token); B4 EVERY POSTURE CLAIM STATES A MISSING SCORE IN WORDS: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ak-6.the-stored-text-rewrite-and-redeploy.proof_of_spec.json`.
Report once: the keys written with prior and new VersionIds, the prior and new CodeSha256 and artifact VersionId, the CONTENT-DIFF
summary, the plan's resource count, and every criterion's output lines. Name any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DSGN r21 3B cells B2-B4 served (issuer rulings R2, R3). Staged until ak-3, ak-4 and ak-5 drain and the plans are
frozen in both halves. The write set is a LITERAL key list the plans fix (NEVER-1 non-application does not apply: the keys are served
output, so the pair stands).

<status>staged</status>
<round>61</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
