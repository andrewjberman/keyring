# AMGT_HARVST task order -- `HVST-by-2` -- ROUND 81 (`1.0.0_SA_CTO~DELL1` msg 4394, `ledger/ROUND_ANALYSIS.round79.md` ADDENDUM 1 item 1): THE REFUSAL-LOGGING `opal-research-pull-enqueue` HANDLER IS DEPLOYED, AND THE DEPLOYED FUNCTION WRITES `DENIED: tier=<tier>` FOR A REFUSED CALLER AND NOTHING FOR AN ADMITTED ONE

<!-- ===================== SEAT ORDER -- the executing seat reads the whole file ===================== -->

<to_id>AMGT_HARVST.TO-HVST-by-2.the-refusal-logging-handler-deployed</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-by-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~HV1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- the change is the function's CODE only. `comp-iam service opal-research-pull-enqueue` is read before and after; no role, policy, route or authorizer changes.
comp-adversary: RUN at L5 -- the adversary is a deploy of bytes that are not the merged commit's, a plan that changes more than the code hash, an arm that carries a real ticker (it would enqueue a Bloomberg pull if the fence were absent), or a log read that cannot tell this seat's invocations from a real session's.
</preflight>

## 0. THE CELL

Cell `HVST-by-1` (its own order, round 81) makes the handler's refusal branch write one log line, `DENIED: tier=<tier or NONE>`,
before it returns 403. This cell DEPLOYS that file and proves the DEPLOYED function writes the line for a refused caller and writes
none for an admitted one. It is the same act as round 80's `HVST-bx-2` (your own prior order): same function, same module, same
build script. It changes nothing else.

**START CONDITION:** the issuer's AMENDMENT 1 to this file names the merge commit `<M>` that carries by-1. Do not start before it
exists. Verify at the start: `git cat-file -e <M>`, `git merge-base --is-ancestor <M> HEAD`, and that
`git show <M>:infra/aws/lambda/research/pull_enqueue/lambda_function.py` matches the working file byte for byte (print both sha256).

**AMENDMENT 1:** `<M>` is `31590746f1`. Both pair halves are signed.

## 1. THE ACT (this box, once, under the never-widen pair named in the issuer notes)

1. **Before, read only.** `get-function-configuration` for `opal-research-pull-enqueue` into `by2_before.out` (`CODESHA256`,
   `LASTMODIFIED`), and `comp-iam service opal-research-pull-enqueue`. Record `T0` = `date -u +%FT%TZ` there.
2. **Open the ledger:** `python .tools/deploy_ledger.py open --slug harvst-by2-enqueue-refusal-log-20261012 --title "HVST-by-2 deploy
   the refusal-logging opal-research-pull-enqueue handler" --author 0.7.0_AE_CloudOps~HV1` with legs `BUILD`, `UPLOAD`, `APPLY`,
   `ARMS` (kinds as in `harvst-bx2-enqueue-fence-20261012`). Commit the sentinel and the entry.
3. **Build and upload:** `bash infra/aws/terraform/harvest/build-and-upload.sh`.
4. **Plan, then read:** targeted at `module.harvest_enqueue`, into `by2_plan.out`. It must read
   `Plan: 0 to add, 1 to change, 0 to destroy`, the one change being the function's code hash. Anything else: STOP and file a row.
5. **Apply once** with `safe-apply`; `by2_apply.out`. Then `by2_after.out` with `CODESHA256 <value>` and `CODESHA256 CHANGED: yes|no`.
6. **The three arms on the DEPLOYED function**, each one `aws lambda invoke` with a payload file, **no payload carrying a `ticker`**:
   - `ARM non_internal: statusCode <n>` for `{"requestContext": {"authorizer": {"tier": "partner"}}}` (expected 403);
   - `ARM no_context: statusCode <n>` for `{}` (expected 403);
   - `ARM internal_no_ticker: statusCode <n>` for `{"requestContext": {"authorizer": {"tier": "internal"}}}` (expected 400).
   Write them to `by2_arms.out`.
7. **The log read.** About 20 seconds after the arms, read the function's log group `/aws/lambda/opal-research-pull-enqueue` for
   events since `T0` that hold `DENIED` (`aws logs filter-log-events --filter-pattern '"DENIED"'`). Write to `by2_log.out`: each
   matching message verbatim, then one line `DENIED LINES FOR internal: <n>` counting messages whose text is `DENIED: tier=internal`
   (must be 0; an internal caller is never refused). Expect exactly the two lines `DENIED: tier=partner` and `DENIED: tier=NONE`
   from this seat's arms, plus any real caller's, which you print too.
8. **Close the ledger** when all four legs carry proof.
9. **Post-act read (the CTO's, carried from bx-2 step 9), now observable:** the first real internal enqueue through the portal
   answers 2xx (an `OK:` line), and a `DENIED: tier=internal` line is Branch B (rebuild the prior version from its pin the same
   hour, file a row). A `DENIED: tier=<other>` is the fence working: print it. If no real call occurs in the first trading day, say
   so; the read is then UNMEASURED, not passed. Write it in `by2_first_real.out`. Not one of the three criteria.

## 2. BOUNDS AND ROLLBACK

- Blast radius: the function's code, once. IAM, the route, the authorizer, the queue and the bucket are not touched.
- Rollback: rebuild the zip from the pre-change file (`git show <M>~1:infra/aws/lambda/research/pull_enqueue/lambda_function.py`),
  upload it, apply the same targeted plan once, and read `CODESHA256` equal to the value in `by2_before.out`. File a row.
- A half-landed deploy is never left: finish in-session or roll back and say so.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-by2-enqueue-refusal-log-20261012.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-by-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round81/by2_arms.out</invocation><expect>(?s)ARM non_internal: statusCode 403.*ARM no_context: statusCode 403.*ARM internal_no_ticker: statusCode 400</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-by-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round81/by2_plan.out</invocation><expect>Plan: 0 to add, 1 to change, 0 to destroy</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-by-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round81/by2_log.out</invocation><expect>(?s)DENIED: tier=partner.*DENIED: tier=NONE.*DENIED LINES FOR internal: 0</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. Write every `.out` file under
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round81/`.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS (about 500 CRLF lines).** Append a row by BYTES (binary read, insert before the closing
  `]` in the tail's own line ending, binary write) and check `git diff --numstat HEAD -- <file>` reads N insertions and 1 deletion.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/AMGT_HARVST.TO-HVST-by-2.the-refusal-logging-handler-deployed.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-by-2.the-refusal-logging-handler-deployed`.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Row ids: the channel's gate refuses a lane tag, so mint the next
  free `AMGT_HARVST-D1-S<n>` (as you did for D1-S8 and D1-S9).
- Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
   This order writes the code artifact bucket and one Lambda only.
2. 49 Financial data never goes into another firm's tree. This order touches none.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4394 and `ledger/ROUND_ANALYSIS.round79.md` ADDENDUM 1.
- The pair: COO half `deliverables/2.0.0_SA_COO_W1/round81/NEVER_WIDEN_HALF_COO_REFUSAL_LOG_DEPLOY.md` (signed in the issuance commit) and
  `1.0.0_SA_CTO~DELL1`'s half (owed). The act does not start without both. The CTO's round-80 half
  (`ledger/NEVER_WIDEN_ROUND80_ENQUEUE_FENCE_DEPLOY_CTO_HALF.md`) is the model.
- This is the same seat and the same function as bx-2, so the seat's context already holds the act; the order is for the
  one-project-per-seat rule's sake a continuation on AMGT_HARVST only.
- **AMENDMENT 1 (2026-10-12 ~14:4xZ, issuer; no criterion changes):** `<M>` = **31590746f1**, the merge of HVST-by-1 on box/dell1
  (`safe-merge.sh`, proof VALID rc 0, by-1 flipped complete). Both pair halves are SIGNED (COO @49b5ed47f3, CTO
  `ledger/NEVER_WIDEN_ROUND81_BY2_BY3_CTO_HALVES.md`, msg 4402): the act may start now.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>81</round>
<slot>dell1</slot>
<fabric>dell1</fabric>
