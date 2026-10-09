# TO IRPT_BCKEND.TO-IB-pr-386 -- ONE named subject, svc-commentary, reads REQUEST_COMPOSITION read-only through get(), tenant-bound, via one callable surface

<to_id>IRPT_BCKEND.TO-IB-pr-386</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~197</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>95</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO msg 2340 (on ~P msg 2337 / ~T2 msgs 2329, 2333, 2344) and msg 2351 (cut now, code-only) | **Decomp cell:** `IB-pr-386` (decomposition section 88) |
**outcome_ref:** NFRA_TRNSPT FWD-10 H2 (the commentary Lambda reads the composition behind a READY analysis) | **depends_on:** none for the code. The release follows IB-pr-383's after-read, under its own pair.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-197` (branch `wk-IRPT_BCKEND-197`, cut from `box/dell2`). Work and commit only there. Paths are
relative to the worktree. Keep scratch OUTSIDE the worktree.

**The gap.** The commentary Lambda (~T2, `outlook-global-commentary-draft-lambda`) must read the REQUEST_COMPOSITION behind each READY
analysis. The path:
1. GetItem `analysis#<request_id>#1`;
2. take `record.composition_ref` (`infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py:61-62,:107-113`);
3. read through `ArtifactRepository.get()` (`infra/aws/lambda/investor-reporting/reports/repository.py:390`).

`get()` admits only a same-firm caller, or an OPAL_GLOBAL caller that passes `authorize` (`repository.py:329-332`). No service principal
passes today. Under the ruling, the caller makes NO direct S3 or DynamoDB read.

**Your cell.**
1. Admit ONE named subject, `svc-commentary`:
   - read-only, family REQUEST_COMPOSITION only, through `get()` with its retention check kept;
   - tenant taken from the READY item IRPT emitted;
   - never ALL, never another family; `put()` refused.
2. Expose ONE callable surface the Lambda calls: an IRPT route or Lambda operation, with its name built by `lib/opal_naming.py`.
   - Request: `{tenant, request_ref}`.
   - Response: the composition document and its sha256, never `owner`.
   - It performs the two reads and the `get()` server-side.
3. Write the tests in `infra/aws/lambda/investor-reporting/reports/tests/test_svc_commentary.py`, names containing `svc_commentary`, at least 5:
   - own-tenant read admitted;
   - another tenant refused;
   - another family refused;
   - put refused;
   - another service subject refused.
   The whole `reports/tests` suite still passes.
4. Write the surface file `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~197/IB95-3_svc_commentary_surface.json`:
   `{kind: route|lambda, name, request: {tenant, request_ref}, response: {...}, caller_iam: [...]}`.
   The caller's IAM is what ~T2's role needs to call the surface, and nothing more: no `dynamodb:GetItem`, `kms:Decrypt` or `s3:GetObject*`.
   - If a NEW route, Lambda or IAM resource is needed, write it as code and DESIRED Terraform only, with nothing applied.
   - `svc-commentary`'s sign-off pair is amended by ~V2 before the read deploys.

Prove each criterion by running its invocation from the worktree root.

<criterion id="IB95-3-AC1" cell_refs="IB-pr-386"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r95/p95_svccom.py" . IB95-3-AC1</invocation><expect>IB95-3-AC1 PASS</expect></criterion>
<criterion id="IB95-3-AC2" cell_refs="IB-pr-386"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r95/p95_svccom.py" . IB95-3-AC2</invocation><expect>IB95-3-AC2 PASS</expect></criterion>
<criterion id="IB95-3-AC3" cell_refs="IB-pr-386"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r95/p95_svccom.py" . IB95-3-AC3</invocation><expect>IB95-3-AC3 PASS</expect></criterion>

<expected_criteria>IB95-3-AC1, IB95-3-AC2, IB95-3-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. Code and tests only: no build, upload, apply or deploy. AWS reads only, if any.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check or a test.
- **Row ids** are `IRPT_BCKEND-D2-W197-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~197" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~197@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~197 <0.9.0_WK_IRPT_BCKEND~197@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool, outside the worktree.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/investor-reporting/reports/
infra/aws/lambda/investor-reporting/export/
infra/aws/lambda/investor-reporting/_authz/
infra/aws/terraform/investor-reporting/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-386.svc-commentary-read-only-request-composition.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~197/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 88 (round 95, workstream ~P), cell `IB-pr-386`.
<owned_cells>IB-pr-386</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB95-3-AC1, IB95-3-AC2, IB95-3-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~197/IRPT_BCKEND.TO-IB-pr-386.svc-commentary-read-only-request-composition.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give what you built and where, the commit hashes, each criterion's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- CTO msg 2340 (on ~P msg 2337 / ~T2 msgs 2329, 2333, 2344) and msg 2351 (cut now, code-only); code + tests only in this cell; its release follows IB-pr-383 under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; any IAM is DESIRED code for the release pair.
comp-routes: DECLARED-NOT-APPLICABLE -- nothing is applied by this cell; a route, if needed, is DESIRED code for the release pair.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p95_svccom.py dry-run at base 6172924378 on dell2 2026-10-09 ~03:5xZ: new-test criteria FAIL (0 selected), suite criteria PASS as control, surface file FAIL (absent); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; ~P's code (CTO msgs 2151, 2311, 2340, 2351).
</preflight>
