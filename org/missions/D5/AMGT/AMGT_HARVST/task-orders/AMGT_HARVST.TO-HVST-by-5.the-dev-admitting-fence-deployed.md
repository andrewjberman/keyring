# AMGT_HARVST task order -- `HVST-by-5` -- ROUND 81 (`1.0.0_SA_CTO~DELL1` msg 4413, `ledger/ROUND_ANALYSIS.round79.md` ADDENDUM 2; row `AMGT_HARVST-D1-S9`): THE DEV-ADMITTING `opal-research-pull-enqueue` FENCE IS DEPLOYED, AND THE DEPLOYED FUNCTION ADMITS A DEV LOGIN OF ANY TIER AND REFUSES A NON-DEV ADVISOR AND A CALLER WITH NO CONTEXT

<!-- ===================== SEAT ORDER -- the executing seat reads the whole file ===================== -->

<to_id>AMGT_HARVST.TO-HVST-by-5.the-dev-admitting-fence-deployed</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-by-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~HV1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- the change is the function's CODE only. `comp-iam service opal-research-pull-enqueue` is read before and after; no role, policy, route or authorizer changes.
comp-adversary: RUN at L5 -- the adversary is a deploy of bytes that are not the merged commit's, a plan that changes more than the code hash, an arm that carries a real ticker (it would enqueue a Bloomberg pull for a refused or admitted caller alike), or a Dev arm whose evidence is a 202 (which writes and enqueues) instead of a 400.
</preflight>

## 0. THE CELL

`HVST-by-4` (its own order, round 81) makes the handler's fence admit a caller whose authorizer context has `tier == "internal"`
OR `userType == "Dev"` (exact strings), still refusing every other caller and a caller with no context. This cell DEPLOYS that
file and proves the DEPLOYED function behaves so. It is the same act as your `HVST-bx-2` and `HVST-by-2`: same function, same
module, same build script. It changes nothing else.

**START CONDITIONS (all, read at the start):**
- `HVST-by-2` is complete (your own order: its ledger CLOSED), so this deploy builds on the refusal-logging code and never races it.
- The issuer's AMENDMENT 1 to this file names the merge commit `<M>` that carries by-4. Do not start before it exists.
- `git cat-file -e <M>`, `git merge-base --is-ancestor <M> HEAD`, and `git show <M>:infra/aws/lambda/research/pull_enqueue/lambda_function.py`
  matches the working file byte for byte (print both sha256).

**AMENDMENT 1:** `<M>` is `f94560218c`; by-2 is complete; both pair halves are signed.
- Both never-widen halves are signed.

## 1. THE ACT (this box, once, under the pair named in the issuer notes)

1. **Before, read only:** `get-function-configuration` into `by5_before.out` (`CODESHA256`, `LASTMODIFIED`), `comp-iam service`, and `T0` = `date -u +%FT%TZ`.
2. **Open the ledger:** `python .tools/deploy_ledger.py open --slug harvst-by5-enqueue-dev-admit-20261012 --title "HVST-by-5 deploy the
   Dev-admitting opal-research-pull-enqueue fence" --author 0.7.0_AE_CloudOps~HV1`, legs `BUILD`, `UPLOAD`, `APPLY`, `ARMS`.
3. **Build and upload:** `bash infra/aws/terraform/harvest/build-and-upload.sh`.
4. **Plan, then read:** targeted at `module.harvest_enqueue`, into `by5_plan.out`: `Plan: 0 to add, 1 to change, 0 to destroy`, the one
   change the code hash. Anything else: STOP and file a row.
5. **Apply once** with `safe-apply`; `by5_apply.out`; then `by5_after.out` with `CODESHA256 CHANGED: yes|no`.
6. **The arms on the DEPLOYED function**, each one `aws lambda invoke` with a payload file, **no payload carrying a `ticker`** (an
   admitted caller with no ticker answers 400 and writes nothing; a refused one answers 403 and writes nothing). Write to `by5_arms.out`:
   - `ARM dev_non_internal_tier: statusCode <n>` for `{"requestContext": {"authorizer": {"lambda": {"tier": "advisor", "userType": "Dev"}}}}` (expected **400**: admitted past the fence);
   - `ARM advisor_non_dev: statusCode <n>` for `{"requestContext": {"authorizer": {"lambda": {"tier": "advisor", "userType": "Advisor"}}}}` (expected **403**);
   - `ARM no_context: statusCode <n>` for `{}` (expected **403**);
   - `ARM internal_no_ticker: statusCode <n>` for `{"requestContext": {"authorizer": {"tier": "internal"}}}` (expected **400**: unchanged).
7. **Close the ledger** when all four legs carry proof.
8. **Post-act read (carried):** the first real portal enqueue by a Dev login whose tier is not internal answers 2xx (an `OK:` line);
   a `DENIED: tier=<t>` line for a login the CTO named a Dev admin is Branch B (rebuild the prior version from its pin the same hour).
   If none occurs in the first trading day, say so: UNMEASURED, not passed. Write `by5_first_real.out`. Not one of the three criteria.

## 2. BOUNDS AND ROLLBACK

- Blast radius: the function's code, once. IAM, the route, the authorizer, the queue and the bucket are not touched. One population
  changes: a Dev login with a non-internal tier is admitted where the fence refused it.
- Rollback: rebuild the zip from the pre-change file (`git show <M>~1:infra/aws/lambda/research/pull_enqueue/lambda_function.py`),
  upload, apply the same targeted plan once, and read `CODESHA256` equal to the value in `by5_before.out`. File a row.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-by5-enqueue-dev-admit-20261012.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-by-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round81/by5_arms.out</invocation><expect>(?s)ARM dev_non_internal_tier: statusCode 400.*ARM advisor_non_dev: statusCode 403.*ARM no_context: statusCode 403.*ARM internal_no_ticker: statusCode 400</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-by-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round81/by5_plan.out</invocation><expect>Plan: 0 to add, 1 to change, 0 to destroy</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-by-5"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round81/by5_after.out</invocation><expect>CODESHA256 CHANGED: yes</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. Write every `.out` file under
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/round81/`.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS (about 500 CRLF lines).** Append a row by BYTES and check the diff reads N insertions and 1 deletion.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~HV1/AMGT_HARVST.TO-HVST-by-5.the-dev-admitting-fence-deployed.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-by-5.the-dev-admitting-fence-deployed`.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ`; mint the next free `AMGT_HARVST-D1-S<n>` (the gate refuses a lane tag).
- Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
   This order writes the code artifact bucket and one Lambda only.
2. 49 Financial data never goes into another firm's tree. This order touches none.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 4413 (the cluster lead's ruling on row D1-S9, from the laptop CTO's count: 3 of 6 Dev logins
  have a tier other than internal, all opal-capital admins). Its own pair: COO half
  `deliverables/2.0.0_SA_COO_W1/round81/NEVER_WIDEN_HALF_COO_DEV_ADMIT_DEPLOY.md` (signed in the issuance commit), the CTO's half owed.
- It was cut as its own build and deploy because HVST-by-1 was merged and `HVST-by-2`'s deploy had begun before the ruling arrived.
- **AMENDMENT 1 (2026-10-12 ~14:5xZ, issuer; no criterion changes):** `<M>` = **f94560218c**, the merge of HVST-by-4 on box/dell1
  (`safe-merge.sh`, proof VALID rc 0, by-4 flipped complete). `HVST-by-2` is complete (ledger CLOSED, flipped @d3fd887c8f). Both pair
  halves are SIGNED (COO, and the CTO @0e8a1d59cc, msg 4424): every start condition is met.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>81</round>
<workstream>DEVADMIT</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
