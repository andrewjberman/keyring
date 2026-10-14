# AMGT_RESAPP task order -- `AMGT-ar-1` -- THE ADAPTER ROLE'S READ GRANT FOR THE AI-FILL PREFIX: ONE LIST ENTRY, A TARGETED APPLY, A LIVE RE-READ (FWD-41, STEP 1 OF THE NEVER-WIDEN PAIR; A WORLD ACT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ar-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ar-1.the-adapter-role-reads-the-ai-fill-prefix</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one IAM policy leg; no schedule is touched.
comp-iam: RUN at the cut -- `comp-iam service opal-amgt-scoped-api` ran (DESIRED plane only, as it states: it parses Terraform, cannot tell landed from planned and is blind to grants Terraform does not declare); the APPLIED plane is `check_ar1_grant.py`'s live `iam:GetRolePolicy` read, which at the base reads `AIFILL AR-1 GRANT: NO (4 of 7)` (the three arms that name the new entry FAIL; the pre-act statement count, the two statements and the byte-equality control PASS, the control reading `77c69f8359764942 vs 77c69f8359764942`).
comp-adversary: RUN at the cut -- the check's negative arm is the base itself (the entry absent -> NO); its control strips the one entry from each limb and compares the canonical sha16 to the pre-act policy, so any other statement or resource that moves is a NO.
EGRESS CLASS, declared: NONE. One IAM write (the role's inline policy) through Terraform; no S3, no model, no Bloomberg.
</preflight>

## 1. THE CELL -- `AMGT-ar-1` (round 104, workstream AIFILLREL, decomposition s.10)

STEP 1 of the never-widen pair for FWD-41 (both halves SIGNED: `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND104_AIFILL_STORE_GRANT_REDEPLOY_{COO,CTO}_HALF.md`; read both, their blast radius is this order's bound). The AI fill's documents will live at
`amgt/harvest/gold/ai_fill/security_key=<K>/ai_fill.json` in bucket `opal-data-harvest`. The adapter's role `opal-amgt-scoped-api-role` reads a fixed list of pool prefixes (`local.scoped_amgt_pool_prefixes` in
`infra/aws/terraform/harvest/scoped-amgt-api.tf`, feeding BOTH the `s3:GetObject` resources and the `s3:ListBucket` prefix condition of the inline policy `opal-amgt-scoped-api-grants`); this prefix is not in it, so the deployed
serve could not read a stored document. You add that one prefix. It is an ADDITIVE read grant on an EMPTY prefix (measured `KeyCount 0` at 2026-10-14 ~00:05Z) and nothing else.

SEQUENCE, in this order and no other:
1. Print the generated constant: `PYTHONPATH="$(pwd)" python -c "from lib.research.api import _harvest_prefixes as h; print(h.AI_FILL_GOLD_PREFIX)"` -- it must read `amgt/harvest/gold/ai_fill/` (the builder's output; the trailing slash is mandatory). Run
   `check_ar1_grant.py` (below, AC1) and read the live policy BEFORE the act: it must read the pre-act values the half names: 7 statements, `ReadThePoolPrefixesTheAdapterReads` with 34 resources, canonical sha16 `77c69f8359764942`. If the live policy is not that (someone else changed it), STOP and report: the half's table is stale.
2. Open the change-management entry (`deploy_ledger.py open`, per `/cloud-ops`) and its `.open_deploys` sentinel, before the edit.
3. Edit `infra/aws/terraform/harvest/scoped-amgt-api.tf`: add ONE entry to `local.scoped_amgt_pool_prefixes`, as the LAST element of the list, with a comment naming both halves of this pair: `"amgt/harvest/gold/ai_fill/",`. Touch nothing else in the file.
4. A targeted plan of `aws_iam_role_policy.scoped_amgt_api_grants` (through the repo's `safe-apply` dry-run form, never a bare `terraform`): it must show EXACTLY one resource changing in place, with exactly one resource added to the `s3:GetObject` statement and one prefix added to the `s3:ListBucket` condition and no other difference. Anything else is a STOP BEFORE APPLY.
5. The targeted `safe-apply` of that one resource. NEVER a bare `terraform apply`; NEVER a plan wider than the one resource.
6. Re-read the live policy: `check_ar1_grant.py` must read YES. Close the change-management entry with the pre and post sha16 printed.
7. Show the function still answers: AC2.

ROLLBACK: remove the one list entry, the same targeted apply, a live re-read shows it absent and the canonical sha16 back at `77c69f8359764942`. It is additive, so it may also stay; the serve reads `ABSENT` with `read_completed` false until it is present.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>` (a seat order's rows), `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. The act and nothing else: ONE list entry in ONE file, ONE targeted apply of ONE resource. No other prefix, statement, role, route, schedule or function; no change to the function's code (that is `AMGT-ar-3`).
2. No S3 write or delete of any kind, no Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches; the Terraform edit is committed on your seat's branch.
4. A change the plan shows beyond the one resource, or the check reading NO after the apply, is a STOP and, inside the same hour, the rollback above.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/scoped-amgt-api.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ar-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_ar1_grant.py"; echo "exit=$?"</invocation><expect>no `FAIL` arm line and the line `AIFILL AR-1 GRANT: YES (7 of 7)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ar-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; AIFILL_SERVED_FUNCTION=opal-amgt-scoped-api PYTHONPATH="$(pwd)" timeout 120 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round104_aifill_prep/checks/check_ar3_aifill_served.py" capture --names ASML_NA_Equity,AMD_US_Equity --out ".scratch_ar1/thesis_post.json"; echo "exit=$?"</invocation><expect>the line `CAPTURED 2 name(s) to .scratch_ar1/thesis_post.json; non-200: none`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with the NAMED rollback (the entry removed, the sha16 back at `77c69f8359764942`) as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ar-1.the-adapter-role-reads-the-ai-fill-prefix.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the step-1 print of the constant and the pre-act check output;
- the plan's resource count and its diff lines, the apply's output;
- the change-management entry's slug and state, the pre and post sha16;
- both criteria's output lines;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** GO 2026-10-14 by the issuer (`2.0.0_SA_COO~R2`) -- the conditions, read: BOTH HALVES SIGNED (COO half in this round's ledger, CTO half `ledger/NEVER_WIDEN_ROUND104_AIFILL_STORE_GRANT_REDEPLOY_CTO_HALF.md`, CTO msg 5304 naming `0.7.0_AE_CloudOps~RA1` as the applier of steps 1 and 3). This step is independent of `2.0.0_SA_COO~R1`'s `AMGT-bk-2` (an IAM grant, not the function's code) and may run now; the function's code is untouched. The policy values (7 statements, 34 pool resources, sha16 `77c69f8359764942`) were read by the issuer at ~00:05Z; the check's control re-derives the sha16 on every run, and it read the same value again at the cut. The prefix is EMPTY; the grant is additive. The seat has no GO message from this file: the issuer tells it by the broker, with the path.

<status>complete</status>
<round>104</round>
<workstream>AIFILLREL</workstream>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<proof_genre>DEPLOY</proof_genre>
