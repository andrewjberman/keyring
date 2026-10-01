# AMGT_RESAPP task order -- `AMGT-ag-1` -- THE ONE SCOPED-API REDEPLOY THAT SERVES THE FRIDAY FEED (FWD-32, FWD-33, FWD-34)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ag-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one redeploy by hand.
comp-iam: RUN by the issuer at the cut -- the new route reads gold chatter_daily and article_security_mention and lists research_dossier/, all already granted to opal-amgt-scoped-api-role (scoped-amgt-api.tf:203-226); the per-name reads use the same DynamoDB pointer/GetItem calls. No simulation was run: AC1 exercises every one live. The plan must show NO IAM change.
comp-adversary: RUN by the issuer at the cut -- AC1 and AC2 each FAIL at the base against the deployed function (C0: CodeSha256 /QP4upEV... unmoved; FWD-32 400 refused; FWD-33 overlay ABSENT; FWD-34 breakout a fraction; text: 16 status tokens, ASML posture without absent_reason). The merged local tree passes every grader YES (the positive arm).
EGRESS CLASS, declared: NONE for the acts; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-ag-1` (round 57, decomposition s.65)

ONE act, under ONE NEVER-2 entry and ONE never-widen pair: redeploy `opal-amgt-scoped-api` at the commit the issuer's GO names. It
carries af-1 (the monthly chatter route), af-2 (the T-1 fallback, `breakout_price`, percent by name), ag-0 (the request-time import and
the dotted calendar import), ag-2 (served reasons in plain words, if the GO says it has drained), and the riders the halves list (CORPUS
ab-3 `case_rule.py`, CORPUS ab-1 `dossier.py`, HARVST ae-1 `publication_gold.py`, the VENDOR display_name naming/registry change, af-4's
hash).

**Item 0 (yours, the AE lane): the package closure.** In `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`, add
`"lib.trading_calendar"` to `CLOSURE_ROOTS`, so the line reads exactly
`CLOSURE_ROOTS = ("lib.research", "lib.opal_data_harvest", "lib.opal_naming", "lib.trading_calendar")`, with a comment naming
AMGT-ag-1. Commit it. Then run `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only <zip>`: rc=0, and
the zip must carry `lib/trading_calendar.py`, `lib/research/api/monthly_chatter.py` and `lib/research/coverage/covered_universe.py`.
Without it, every staleness read on the deployed function raises ImportError. The issuer measured that defect at the cut.

**Begin the deploy only when all of these hold:**
- the issuer's GO names the build commit;
- both halves are committed: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round57/NEVER_WIDEN_HALF_COO_AG1.md` and
  `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND57_AG1_CTO_HALF.md`;
- the base CodeSha256 the halves name (`/QP4upEVzTjnHV2bAeIXIud0k0DgjDDGrlMgtm0uo7o=`) is still the live one, re-read immediately
  before the build. A moved base is a STOP and a re-sign.

**The acts, in order, under the entry opened AND COMMITTED first:**
1. `python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round57/checks/ag_1_served.py --what pre --out org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ag1-pre.json`.
2. Build and upload the ONE artifact at the GO commit, recording the prior S3 VersionId. Save the `CONTENT-DIFF` printout to your
   deliverables. STOP if any CHANGED/ADDED/REMOVED file is outside the halves' list.
3. ONE `safe-apply`, plan printed first: code only (the function's source hash). Any destroy, IAM, route or gateway change in the plan
   is a STOP (MSTR~Z HOLD 27462: plan from a tree at CLOUD HEAD).
4. AC1, then AC2. Close the entry.

A criterion failing after the act is the ROLLBACK trigger named in the halves. The rollback is the prior artifact version through one
code-only `safe-apply`.

## 2. BOUNDS

1. The act and nothing else. A plan beyond the function's code, a packaged file outside the halves' list, or a gate refusal is a
   REFUSAL. No store write.
2. Standing: no S3 delete, no vendor call, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ag-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round57/checks/ag_1_served.py --what post --pre org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ag1-pre.json; echo "exit=$?"</invocation><expect>C0 PASS (CodeSha256 and LastModified moved off the printed pre values); FWD-32, FWD-33 and FWD-34 each YES on the deployed function; THE DEPLOYED FUNCTION SERVES THE FRIDAY FEED: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ag-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round57/checks/ag_1_served.py --what text --pre org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/ag1-pre.json; echo "exit=$?"</invocation><expect>C0 PASS; C1, C2 and C3 PASS on the deployed function; THE DEPLOYED FUNCTION SERVES EVERY REASON IN PLAIN WORDS: YES -- and exit=0 (only if the GO says ag-2 rides; otherwise the GO states AC2 is carried, not graded)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ag-1.the-one-redeploy.proof_of_spec.json`.
Report once: item 0's commit and the `--build-only` membership lines, the prior and new CodeSha256 and S3 VersionId, the CONTENT-DIFF
summary, the plan's resource count, both criteria's output lines, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-56 analysis enrichment item 1. Ruling 3's deploy-act list is decomposition s.65a. The served limbs compare a
moving field (CodeSha256 / LastModified) against the printed pre (round-55 ruling 2). The served graders are round 56's, swapped onto
the deployed function. Positive arm: they read YES on the merged local tree (CLOUD `78167bb8fc`).

<status>pending</status>
<round>57</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-01 ~08:5xZ):** ACCEPTED. Executor proof `cffc66ed7e` (AC1, AC2 PASS; entry CLOSED). Issuer's independent served read of the deployed function (08:2xZ): post YES (C0 /QP4upEV... -> /HInwjrn...; FWD-32/33/34 YES), text YES. Row Z-S330 (print-route census wording) carried to the L8 packet.

<status>complete</status>
