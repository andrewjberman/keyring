# AMGT_HARVST task order -- `HVST-bx-2` -- ROUND 80 (`1.0.0_SA_CTO~DELL1` msg 4215, `ledger/CTO_RULING_R79_BS3_CARRIED_AND_ENQUEUE_FENCE_20261012.md` section 1): THE FENCED RESEARCH-PULL-ENQUEUE HANDLER IS DEPLOYED, AND THE DEPLOYED FUNCTION REFUSES A NON-INTERNAL CALLER AND A CALLER WITH NO CONTEXT, AND ADMITS AN INTERNAL ONE

<!-- ===================== SEAT ORDER -- the executing seat reads the whole file ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bx-2.the-fenced-enqueue-handler-deployed</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bx-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~HV1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- the change is the function's CODE only. `comp-iam service opal-research-pull-enqueue` is read before and after; no role, no policy, no API Gateway route or authorizer changes.
comp-adversary: RUN at L5 -- the adversary is a deploy of bytes that are not the merged commit's, a plan that changes more than the function's code hash, a check that invokes the deployed function with a REAL ticker (that would enqueue a real Bloomberg pull if the fence were absent), or a rollback that was never rehearsed.
</preflight>

## 0. THE CELL

Cell `HVST-bx-1` (its own order, round 80) changes `infra/aws/lambda/research/pull_enqueue/lambda_function.py`: the handler
reads the authorizer context's `tier` and returns 403 unless it is exactly `internal`; no context is 403 too. This cell DEPLOYS
that file and proves the DEPLOYED function behaves so. It changes nothing else.

**START CONDITION:** the issuer's AMENDMENT 1 to this file names the merge commit `<M>` that carries bx-1. Do not start before it
exists. Verify at the start: `git cat-file -e <M>` and `git merge-base --is-ancestor <M> HEAD`, and that
`git show <M>:infra/aws/lambda/research/pull_enqueue/lambda_function.py` matches the working file byte for byte (print both sha256).

**AMENDMENT 1:** `<M>` is `824bdb355b`.

## 1. THE ACT (this box, once, under the never-widen pair named below)

1. **Before, read only.** `aws lambda get-function-configuration --function-name opal-research-pull-enqueue` through the
   `.tools/aws` shim; write `bx2_before.out` holding `CODESHA256 <value>`, `LASTMODIFIED <value>`, and the same read of
   `comp-iam service opal-research-pull-enqueue`.
2. **Open the ledger** before any write: `python .tools/deploy_ledger.py open --slug harvst-bx2-enqueue-fence-20261012 --title
   "HVST-bx-2 deploy the fenced opal-research-pull-enqueue handler" --author 0.7.0_AE_CloudOps~HV1` with legs `BUILD`
   (verify: zip built from <M>'s file), `UPLOAD` (activation: s3 object read back), `APPLY` (activation: Terraform apply of
   `module.harvest_enqueue` only), `ARMS` (verify: the three deployed arms). Commit the sentinel and the entry.
3. **Build and upload:** `bash infra/aws/terraform/harvest/build-and-upload.sh` (it zips `lambda_function.py` alone and uploads
   to `s3://opal-313476888478-lambda-artifacts/research/opal-research-pull-enqueue.zip` with read-back verify).
4. **Plan, then read:** the Terraform plan in `infra/aws/terraform/harvest`, targeted at `module.harvest_enqueue`, written to
   `bx2_plan.out`. It must read `Plan: 0 to add, 1 to change, 0 to destroy`, and the one change is the function's code hash. If it
   shows anything else, STOP, change nothing, and file a surprise row with the plan verbatim.
4a. **Before the apply, read where the portal authorizer puts `tier` for an INTERNAL login** (the authorizer function's source, or its
   served context; `comp-iam`/`comp-aws` name it; the API Gateway authorizer id is `naqxlm`). Write `bx2_authorizer.out` holding the
   field's path as read (for example `requestContext.authorizer.lambda.tier`). The handler reads `tier` at
   `requestContext.authorizer.tier` or `requestContext.authorizer.lambda.tier` and nowhere else. If the authorizer emits it elsewhere,
   or does not emit `tier` for an internal login, DO NOT APPLY: the fence would lock the internal page out. File a surprise row with
   the read verbatim and stop; the issuer re-cuts bx-1.
5. **Apply once** with `safe-apply` (never a bare `terraform apply`); write `bx2_apply.out`.
6. **After, read only:** `get-function-configuration` again into `bx2_after.out` with `CODESHA256 <value>`, then a line
   `CODESHA256 CHANGED: yes` or `CODESHA256 CHANGED: no` (compare to `bx2_before.out`), and `comp-iam service` again.
7. **The three arms on the DEPLOYED function.** Each is one `aws lambda invoke --function-name opal-research-pull-enqueue` with a
   payload file and `--cli-binary-format raw-in-base64-out`. **NO payload carries a `ticker`**, so no arm can write a status object or
   send a message even if the fence were absent. Record each response's `statusCode` in `bx2_arms.out`, as these literal lines:
   - `ARM non_internal: statusCode <n>` for `{"requestContext": {"authorizer": {"tier": "partner"}}}` (expected 403);
   - `ARM no_context: statusCode <n>` for `{}` (expected 403);
   - `ARM internal_no_ticker: statusCode <n>` for `{"requestContext": {"authorizer": {"tier": "internal"}}}` (expected 400: the
     internal caller was admitted past the fence and refused only for the missing ticker).
   Without the fence, all three read 400, so 403 against 400 discriminates. Do NOT invoke with a real ticker, and do NOT run
   `check_e2e.py` (it launches a real Bloomberg draw).
8. **Close the ledger** only when all four legs carry proof (`python .tools/deploy_ledger.py close-leg ...` then `close`).
9. **(AMENDMENT 2) Post-act read, owed by this seat after the ledger closes:** the first real internal enqueue through the portal
   after the deploy is read in the function's CloudWatch log (`/aws/lambda/opal-research-pull-enqueue`) and must answer 2xx. Record
   it in `bx2_first_internal.out` with the log stream, the timestamp and the status. **A 403 to an INTERNAL session within the first
   trading day's log is Branch B: rebuild the prior version from its pin the same hour (the rollback in section 2) and file a row.**
   A partner session's 403, if one occurs, is the fence working: print it, do not roll back. If no real enqueue occurs in the first
   trading day, say so; the post-act read is then UNMEASURED, not passed. This read is not one of the three criteria.

## 2. BOUNDS AND ROLLBACK

- Blast radius: the function's code, once. IAM, the API Gateway route, the authorizer, the queue and the bucket are not touched.
- Rollback, if an arm reads other than expected: rebuild the zip from the pre-change file
  (`git show <base>:infra/aws/lambda/research/pull_enqueue/lambda_function.py`, `<base>` = `<M>~1`'s tree for that path), upload it,
  apply the same targeted plan once, and read `CODESHA256` equal to the value in `bx2_before.out`. File a row and keep working.
- A half-landed deploy is never left: finish in-session or roll back and say so (CLAUDE.md NEVER).

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-bx2-enqueue-fence-20261012.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bx-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round80/bx2_arms.out</invocation><expect>(?s)ARM non_internal: statusCode 403.*ARM no_context: statusCode 403.*ARM internal_no_ticker: statusCode 400</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bx-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round80/bx2_plan.out</invocation><expect>Plan: 0 to add, 1 to change, 0 to destroy</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bx-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round80/bx2_after.out</invocation><expect>CODESHA256 CHANGED: yes</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. Write all five `.out` files under
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round80/`.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/AMGT_HARVST.TO-HVST-bx-2.the-fenced-enqueue-handler-deployed.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-bx-2.the-fenced-enqueue-handler-deployed`.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-HV1-S1`.
- Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
   This order writes the code artifact bucket and one Lambda only.
2. 49 Financial data never goes into another firm's tree. This order touches none.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4215 and the record `ledger/CTO_RULING_R79_BS3_CARRIED_AND_ENQUEUE_FENCE_20261012.md` section 1,
  "under its own pair". The pair: COO half `deliverables/2.0.0_SA_COO_W1/round80/NEVER_WIDEN_HALF_COO_ENQUEUE_FENCE_DEPLOY.md`,
  and `1.0.0_SA_CTO~DELL1`'s half (owed). The act does not start without both.
- **The arms are chosen so that no arm has a side effect.** The CTO's fourth arm, "the amended e2e check passes", would launch the
  check's consumer step, which is a real Bloomberg draw for one ticker. The issuer reads it narrowly: bx-1 proves the amended payload
  (unit test) and this cell proves the DEPLOYED function admits an internal context (400 on an empty body). A full live e2e is a
  separate act through the Bloomberg queue and is not in this round. The CTO is told this in the round-80 drain-end message.
- Executes on dell1 (`dell1 runs its own deploys`, Andrew-direct via `0.0.0_AB_MSTR~DELL1` msg 1590). The Lambda lives in AWS and
  is not a site Z asset.
- **AMENDMENT 2 (2026-10-12 ~13:4xZ, issuer; no criterion changes):** the CTO half is SIGNED
  (`ledger/NEVER_WIDEN_ROUND80_ENQUEUE_FENCE_DEPLOY_CTO_HALF.md`, msg 4362). It makes C-d a PRECONDITION of the apply (step 4a), accepts
  the narrow fourth arm, and adds step 9 (the post-act read) and Branch B.
- **AMENDMENT 1 (2026-10-12 ~14:3xZ, issuer; no criterion changes):** `<M>` = **824bdb355b**, the merge of HVST-bx-1 on box/dell1
  (`safe-merge.sh`, proof VALID rc 0, bx-1 flipped complete). The START CONDITION is met except the seat itself: lane
  `0.7.0_AE_CloudOps~HV1` is spawned by the issuer, and `1.0.0_SA_CTO~DELL1`'s half of the pair is owed.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>80</round>
<slot>dell1</slot>
<fabric>dell1</fabric>

**COMPLETE 2026-10-12 ~14:1xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** `0.7.0_AE_CloudOps~HV1` @adfc9044a0 (on box/dell1 HEAD), under the pair COO @7b4512b094 and `1.0.0_SA_CTO~DELL1`
  (`ledger/NEVER_WIDEN_ROUND80_ENQUEUE_FENCE_DEPLOY_CTO_HALF.md`). The seat read the authorizer's `tier` path first (C-d, step 4a):
  `requestContext.authorizer.lambda.tier`, which the handler reads; SATISFIED. Plan `0 to add, 1 to change, 0 to destroy`, apply
  once, function code hash `THhz...` -> `+e2d...` (LastModified 2026-10-12T13:50:11Z, Active, Successful). Ledger
  `harvst-bx2-enqueue-fence-20261012` CLOSED. Proof VALID rc 0 at box/dell1 HEAD (re-run by this seat with `--governing-order`).
- **AC1 PASS** the three deployed arms read 403 (non-internal), 403 (no context), 400 (internal, no ticker: admitted past the fence).
  No arm carried a ticker, so nothing was written or enqueued. **AC2 PASS. AC3 PASS.**
- **Step 9 (the CTO's post-act read) is UNMEASURED, not passed:** no real internal enqueue had occurred by 13:52Z.
- **Rows, ruled by the issuer:**
  - **D1-S8** (the function log can never show a 403, so Branch B reads the same as "no enqueue happened"): the read is RESTATED as
    START count minus `OK:` lines in the first trading day's log, which gives refusals plus errors without the caller's tier. It
    cannot say whom the fence refused. CARRIED to the next round's enrichment list as a one-line handler change (log the refusal and
    the tier string, never the ticker or body) and a redeploy; the stage's access log is another project's infrastructure.
  - **D1-S9** (the authorizer grants ALL to `userType` Dev whatever its tier, so a Dev login whose tier is not `internal` is
    refused 403 here): NOT adjudicated by this seat. The ruling is the CTO's: "403 unless exactly internal". Not measured: whether
    any Dev login carries another tier or uses the research page. Sent to `1.0.0_SA_CTO~DELL1` with the drain-end message.
- **Not done here:** the full live e2e (a Bloomberg draw) is not run, as ruled.

<status>complete</status>
