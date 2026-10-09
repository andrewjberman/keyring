# NFRA_OPLGTW task order -- `OG-da-1` -- the data_refresh admission fails closed: Dev or Opal-internal only (CTO~Z ruling msg 32354)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-da-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-da-1</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code fix and one Lambda deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE no role or policy changes; the deploy is code only via Terraform (infra/aws/terraform/data-refresh/main.tf, function opal-data-refresh-api).
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is 1.0.0_SA_CTO~Z's ruling msg 32354 (relayed by 0.0.0_AB_MSTR~Z msg 32368) on dell2 row TCKT_VNEXT-D2-W6-S2 (45 PROFILE rows lack userType).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-da-1` (round 32, workstream DATA-REFRESH-ADMIT)

`infra/aws/lambda/data_refresh/lambda_function.py` `validate_user_type` (lines ~137-195) admits a caller when its userType
is `Dev` OR EMPTY: `if not user_type or user_type == 'Dev': return True` (line ~165). 45 PROFILE rows carry no userType
(dell2's row), so any of those principals is admitted. It also admits a call with NO authorizer context at all, as
`dev@test.com` (the "development fallback", Method 3). The ruling: admit `Dev` or an Opal-internal principal (firm
`opal-capital`), and REFUSE an empty or null userType. Fail closed everywhere.

**MEASURED AT THE CUT: the LIVE function does NOT equal box/sitez HEAD.** `da1.AC2` read
`lambda_function.py equal-to-HEAD=False` (live `CodeSha256 E4944Imr7Y4S4//rTR6HN5sbwczbwLw5DcaH4IZ0D0E=`). A deploy from HEAD
would ship that difference too.

### PHASE A -- build and measure; NO deploy
1. **The drift.** Download the live zip and diff every member against HEAD. Name every difference (file, hunk, which commit
   introduced it on box/sitez if traceable). The ask must cover it: the deploy ships HEAD plus the fix, nothing else.
2. **The callers.** From the function's CloudWatch logs for the last 14 days (the `Lambda authorizer context: email=...,
   userType=..., tier=...` lines and the JWT/no-authorizer lines), list every distinct principal that called it, BY ROLE
   (never print an email): the opalgateway caller, the bbg-daily and terminal-upload senders (Alyssa's account), and any
   other. For each: which path (authorizer / JWT / none), its userType, and whether the authorizer context carries a firm
   field. Write `W/da1_callers.json`.
3. **The fix** in `lambda_function.py`: admit `Dev`, or an Opal-internal principal (firm `opal-capital`, read from the
   field the authorizer context actually carries; if no firm field reaches the Lambda, say so and stop: the ask names
   what must carry it). REFUSE empty, missing or `null`. The JWT path follows the same rule. The no-authorizer path REFUSES.
   Every named caller in step 2 must read ADMITTED under the new rule (show each, with Dev as the positive control); if
   one would be refused, STOP and say which.
4. **Tests**: `infra/aws/lambda/data_refresh/test_admission_gate.py` (pytest), named exactly `test_ogda1_ac01` ..
   `test_ogda1_ac05` as the header of `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/da1.AC1.sh`
   lists them.
5. **The ask**, `W/NEVER_WIDEN_ASK_OG-da-1.md`: the drift, the fix, the callers (each admitted, by role), the blast radius
   (one Lambda's code), the rollback (the live artifact version and its `CodeSha256`), the deploy path (Terraform, `-target`
   the one function, `bash .tools/safe-apply.sh`, a NEVER-2 ledger). Halves owed: `1.0.0_SA_CTO~Z` (the site-Z CTO half, per
   the ruling) and `2.0.0_SA_COO~O`. Commit, report, STOP.

### PHASE B -- only after both halves are at HEAD (the issuer names them)
6. Ledger `nfra-oplgtw-og-da-1-data-refresh-admit`; plan (1 resource, code only) and apply `-target` that function;
   read back; close the ledger; run the criteria. A read-back that disagrees: roll back to the live artifact version and
   file an ARMED row naming `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- Phase A deploys nothing. One Lambda's code in Phase B; no other function, role, route or authorizer changes.
- Never print an email, token or principal id; callers by role.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform`; `aws lambda update-function-code`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/lambda/data_refresh/lambda_function.py
infra/aws/lambda/data_refresh/test_admission_gate.py
infra/aws/terraform/data-refresh/qa-scratch-instance.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-da-1-data-refresh-admit.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from the repo root after Phase B's ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-da-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/da1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)named tests passed 5 of 5; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-da-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/da1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)lambda_function\.py equal-to-HEAD=True; .*State=Active LastUpdateStatus=Successful.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-da-1" judgment="true"/>
</proof_of_spec>

- `AC1`: the fail-closed rule's five arms, offline.
- `AC2`: the live function runs HEAD's fixed code.
- `AC3` (judgment, the CVO at L9): each caller named in `W/da1_callers.json` reads ADMITTED in the function's own log on
  its first real call after the deploy. Record it as UNVERIFIABLE-BY-INSTRUMENT with `status_reason` naming the CVO.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-da-1.data-refresh-admission-fail-closed.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance>`, and flip the ONE `<status>` tag to `complete` only if AC1 and AC2 PASS.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32, workstream DATA-REFRESH-ADMIT, on 1.0.0_SA_CTO~Z's ruling msg 32354 (this seat issues it; 0.7.0_AE_CloudOps~Z
  is site Z's producer owner). Cut after the applier closed OG-ap-1 and OG-ap-2.
- Pre-cut: da1.AC1 base FAIL as expected (test file absent); da1.AC2 base FAIL -- NOT the expected PASS: live already
  differs from HEAD (CodeSha256 E4944Imr...), so Phase A step 1 names the drift before any deploy.

- A1 (issuer, 2026-10-09 ~08:1xZ, on ARMED row Z-S72): disposition (b) -- PIN the qa-scratch clone
  (`module.data_refresh_api_qa_scratch`) to the prior artifact version `WJQGGIAlTSMp0Vny8avvQ7LxflVuvLf6` (its own
  explicit version or key), so the signed radius stays true. `qa-scratch-instance.tf` joins <paths>. Done when: the
  clone's live CodeSha256 still reads `E4944Imr7Y4S4//rTR6HN5sbwczbwLw5DcaH4IZ0D0E=` and a FULL plan of the
  data-refresh root reads No changes. Any plan row that moves the clone's code is a STOP. Then close leg RB and the
  ledger. Not ratified as a widening: that needs both halves. The clone keeps the pre-fix admission until
  `1.0.0_SA_CTO~Z` rules its teardown (its recorded call). Graded by no gate limb as a modification.

<status>pending</status>
<round>32</round>
<workstream>DATA-REFRESH-ADMIT</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
