# TO NFRA_OPSEC202609.TO-OP-S-10C -- THE CONSUMER THAT CANNOT BE REBUILT IS THE ONE BLOCKING THE ROTATION: `session-analytics` is ALIVE at 141,685 invocations/14d, has NO build path and NO TTL, so rotating the signing key would break it PERMANENTLY with no mechanism left to fix it. Establish the build path, or prove the rotation must route around it (OP-s-10, round 2c)

<to_id>NFRA_OPSEC202609.TO-OP-S-10C</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-04</issued_date>
<status>staged</status>

✅ **BLOCKER: NONE. GO IMMEDIATELY.** Everything this face needs was measured by `0.7.0_AE_CloudOps~V` and is committed. **It is cut to a second lane because `TO-OP-S-10` blocks on it and `TO-OP-S-10B` is mid-build** -- one lane cannot hold both, and this is the critical path.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (FWD-10; the signing-key rotation) - **Decomp cell:** `OP-s-10` (manifest S10), round 2c - **Lane:** the `session-analytics` Lambda@Edge function and its build tooling, AE lane - **Round:** 3.

---

## WHY THIS FACE EXISTS: A ROTATION IS ONLY AS SAFE AS ITS LEAST REBUILDABLE CONSUMER

`0.7.0_AE_CloudOps~V` was asked to determine whether `session-analytics` was alive, because the answer selects the ending. **It is ALIVE: 141,685 invocations over 14 days** (row `Z-S123`, @`aa5cedbf45`).

**So the consequence is now concrete rather than hypothetical.** `session-analytics` has **no build path and no TTL**. Rotate the signing key and it **cannot receive the new key** and **cannot expire itself into a retry**. It does not degrade -- **it breaks permanently, and no mechanism remains to repair it.** ⛔ **That is not an acceptable cost, and a rotation that keeps the old key valid forever to avoid it has not rotated anything.**

**`TO-OP-S-10` IS BLOCKED ON THIS FACE.** Its ending is chosen here.

## ⛔⛔ RETRACTED 2026-09-04 03:4xZ -- BOTH "TRAPS" BELOW WERE MISAPPLIED BY THE ISSUER AND `opal-session-analytics` IS **NOT** LAMBDA@EDGE

**THE CORE PREMISE OF THIS FACE STANDS: `opal-session-analytics` IS a signing-key consumer, it DOES cache without a TTL, and it IS a genuine rotation blocker.** Everything below about the *instruments* was wrong, and `0.7.0_AE_CloudOps~W` measured it before writing anything.

⛔ **THE ERROR, AND IT IS A WRONG-OBJECT JOIN I MADE FROM TWO ADJACENT SENTENCES IN ONE SUMMARY.** That summary carried *"session-analytics ALIVE 141,685 inv/14d"* and *"Invocations is NOT an oracle for L@E, reads 0 on the busiest consumer (Z-S124)"*. **I read them as one fact about one function. They are two facts about two functions.** `Z-S124`'s false zero was on **`auth-validator-edge`** -- and **`opal-session-analytics` was `Z-S124`'s POSITIVE CONTROL, in those words.** I took the control for the subject.

**MEASURED, with the discriminator `Z-S124` itself used:** `list-metrics FunctionName=opal-session-analytics` -> **2 metrics (the metric EXISTS)**; `list-metrics FunctionName=auth-validator-edge` -> **[]**. **So `Invocations` is a WORKING oracle for this function and `S10C-AC1`'s disqualification of it is VOID.**

**AND IT IS STRUCTURALLY INELIGIBLE TO BE LAMBDA@EDGE:** it runs as `opal-portal-lambda-role`, trusting **`lambda.amazonaws.com` ONLY**. A Lambda@Edge execution role **must** trust `edgelambda.amazonaws.com` or CloudFront rejects the association -- and `lambda-edge-execution-role` in the same account is the control showing what an edge role looks like. **Corroborated independently across BOTH distributions (denominator 2): enumerating every behavior's `LambdaFunctionAssociations`, `opal-session-analytics` appears ZERO times.**

**CONSEQUENCES THAT CHANGE THE WORK:**
- **`S10C-AC1`'s disqualification of `Invocations` is VOID.** ⭐ **The PRINCIPLE survives and still binds: state what the instrument would show if the function were idle, and prove it differs from what it shows now.** The named metric is simply no longer the wrong one here.
- **The region/viewer log trap is VOID** -- ordinary Lambda logs land in the function's own region.
- ⭐ **ROLLBACK IS FAST, NOT SLOW.** No published-version requirement, no CloudFront association, no asynchronous edge replication. **Deliverable 2's edge mechanics do not apply to this function.**
- **A BUILD PATH DOES EXIST IN-REPO** -- the face's "no build path" framing was inherited from an earlier read and is superseded by this seat's measurement.

⛔ **THE ONE THING THAT REPLACES THEM, AND IT IS A HARD STOP: THE EXISTING BUILD PATH'S DEPLOY HALF USES `aws lambda update-function-code`, WHICH IS BANNED** (CLAUDE.md NEVER -- Terraform only). **Do NOT deploy through it.** The deploy must go through Terraform, and **if that requires building the Terraform path that does not yet exist, that is this face's real work.** ⛔ **Do not invoke the banned command "just to test", and do not treat its presence in the repo as authorisation.**

⭐ **AND THE OBSERVATION WORTH KEEPING: THE NO-TTL CACHE IS EXACTLY WHY THIS FUNCTION LOOKS LIKE A NON-CONSUMER.** It holds the key without re-fetching, so it makes no ongoing calls that would mark it as a consumer of the signing key -- **its invisibility is a direct consequence of the defect being repaired**, which is also why it would have survived a rotation until the moment its cache was invalidated.

## THE BUILD-PATH GROUND ALREADY ESTABLISHED -- inherit it, do not re-derive it

From `0.7.0_AE_CloudOps~V`'s `TO-OP-S-10B` design work: **the bundler inlines imports, so `files[]` does not govern what ships**; and the **canonical `lib/` mirror is gated on `src/`, which neither target has.** ⛔ **Read that seat's rows before writing anything** -- re-deriving it wastes the measurement and risks diverging from it.

## DELIVERABLE

1. **ESTABLISH A REPEATABLE BUILD-AND-DEPLOY PATH FOR `session-analytics`**, or prove one cannot be established and say precisely what blocks it. **The test is not "I deployed it once by hand" -- it is that a second person, or this face's own tooling, can do it again from the repo.**
⛔ **SCOPE CALL RULED 2026-09-04 04:1xZ: YES, THE TERRAFORM ADOPTION IS INSIDE THIS FACE -- BOUNDED TO THIS ONE FUNCTION.** `0.7.0_AE_CloudOps~W` returned verdict **(a)**: a build path exists and is exercised -- **2 clean builds byte-identical to each other AND to the artifact deployed 2026-01-08, 12/12 by sha256** -- but the deploy half uses the **BANNED** `aws lambda update-function-code`. ⭐ **WITHOUT THE ADOPTION, VERDICT (a) IS HOLLOW: "a build path exists but you may not lawfully use it to deploy" leaves the rotation EXACTLY as blocked as verdict (b) would.** Deliverable 1 says build-**and-deploy**, and a deploy path nobody may run is not a path.
⛔ **BOUNDED, AND THE BOUND IS THE RULING'S OTHER HALF: adopt THIS function only, on the existing module pattern. Do NOT refactor the portal's Terraform, do NOT adopt sibling functions, do NOT "tidy" adjacent resources.** A rotation-blocker face is not an authorisation to restructure a root.
⛔ **THE IMPORT IS THE DANGEROUS STEP AND IT HAS ITS OWN CONTROL: `terraform import` THEN `plan`, AND THE PLAN MUST SHOW NO CHANGES TO THE RUNNING FUNCTION.** An import whose config does not match reality **proposes to modify or replace a live function**, and applying it would change one serving production. **If the plan is not clean, STOP and reconcile the declaration to the world -- never the other way round, and never by applying.** Quote that plan in the proof.
**THE FOUR BUILD-PATH DEFECTS: file each as a ROW. In scope to FIX only where a defect blocks the compliant deploy path itself; everything else is named and left.** ⛔ **Do not fix a defect merely because it is now visible.**
2. ⛔ **Lambda@Edge DEPLOY MECHANICS ARE NOT ORDINARY LAMBDA MECHANICS AND THE DIFFERENCES ARE LOAD-BEARING:** the function must be **published as a numbered VERSION** (`$LATEST` cannot be associated), the **CloudFront distribution association must be updated to that version**, and **replication to the edge is asynchronous and takes minutes.** ⛔ **ROLLBACK IS THEREFORE SLOW.** Name the rollback and its expected duration **before** the first act; a rollback nobody has timed is a hope.
3. **A TTL / KEY-REFRESH PATH so the function can pick up a rotated key without a redeploy**, if that is achievable. **If it is not, say so** -- then the rotation's ending is "redeploy this consumer as part of every rotation", which is a legitimate answer that must be **written down** rather than discovered during the next rotation.
4. **THE VERDICT `TO-OP-S-10` NEEDS, IN WRITING**, in one of exactly three forms: **(a)** a build path exists and is exercised -- rotation may proceed; **(b)** no build path is achievable -- rotation must route around this consumer, with the route named; **(c)** the function is retirable -- with the evidence, and the retirement is a human's call, not this face's.
5. **Deploy-ledger entry** per applied root (`safe-apply`, never bare), opened before and closed on exercised evidence.
6. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~W/NFRA_OPSEC202609.TO-OP-S-10C.session-analytics-build-path.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S10C-AC1" cell_refs="OP-s-10"/> `S10C-AC1` -- ALIVENESS RE-ESTABLISHED ON AN INSTRUMENT THAT COULD SAY "DEAD": the function's activity confirmed at this assignee's own vintage, **with the instrument named and its discriminating power stated** -- what it would show if the function were idle, and how that differs from what it shows now. ⛔ **DISQUALIFICATION RETRACTED 2026-09-04 03:4xZ: `Invocations` IS a working oracle for `opal-session-analytics` (2 metrics exist), and `Z-S124`'s false zero was on `auth-validator-edge` -- a DIFFERENT function, for which THIS one was the POSITIVE CONTROL. The issuer took the control for the subject.** ⭐ **THE PRINCIPLE STILL BINDS AND IS THE WHOLE CRITERION: name the instrument, state what it would show if the function were IDLE, and demonstrate that differs from what it shows now.** The region-denominator clause is VOID -- this is not Lambda@Edge and its logs land in its own region.
<criterion id="S10C-AC2" cell_refs="OP-s-10"/> `S10C-AC2` -- THE BUILD PATH IS REPEATABLE, NOT A ONE-OFF: the build run **twice** from a clean state producing a **byte-identical or explained-different** artifact, with the commands recorded such that another seat could run them. **A single successful manual build does not pass** -- the whole defect being repaired is that no repeatable path exists.
<criterion id="S10C-AC3" cell_refs="OP-s-10"/> `S10C-AC3` -- DEPLOYED AND SERVING, VERIFIED AT THE EDGE RATHER THAN AT THE API: the published version number, the CloudFront association updated to it, **and evidence the NEW code is actually EXECUTING** -- not merely that a deploy call returned success. ⛔ **AMENDED 03:4xZ: the edge framing is VOID (ordinary Lambda, not Lambda@Edge), so there is no published-version requirement, no CloudFront association, no asynchronous replication -- and ROLLBACK IS FAST.** What survives is the rung that matters: **a deploy call returning success proves a configuration change, never that the new bytes are the ones running.** Verify on the running function. ⛔ **AND THE DEPLOY MUST GO THROUGH TERRAFORM: the in-repo build path's deploy half uses `aws lambda update-function-code`, which is BANNED.** Its presence in the repo is not authorisation.
<criterion id="S10C-AC4" cell_refs="OP-s-10"/> `S10C-AC4` -- THE KEY-REFRESH QUESTION IS ANSWERED EITHER WAY: either a refresh path demonstrated with the function picking up a changed key **without a redeploy**, or an explicit statement that redeploy-per-rotation is required, **with the rotation runbook amended to say so.** **Both pass. Silence on it fails.**
<criterion id="S10C-AC5" cell_refs="OP-s-10"/> `S10C-AC5` -- THE VERDICT IS DELIVERED IN ONE OF THE THREE NAMED FORMS, and `TO-OP-S-10`'s owning lane has it in writing with the message id recorded. **A verdict nobody receives has not unblocked anything.** Plus: the unscoped plan before, the changed-resource list enumerated, the unscoped re-plan after, ledger CLOSED on exercised evidence, push state MEASURED.

<expected_criteria>S10C-AC1, S10C-AC2, S10C-AC3, S10C-AC4, S10C-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc>, cell `OP-s-10` (manifest row S10; FWD-10), round 2c. **This face adds NO new cell and NO new manifest row** -- it is a third task order on an existing cell whose consumer set turned out to contain one member that cannot be rebuilt, following the `TO-OP-S-8R2B` / `TO-OP-S-10B` / `TO-OP-S-9C` precedent.
<owned_cells>OP-s-10</owned_cells>
Read-dependencies, NOT claimed: `TO-OP-S-10B` (`0.7.0_AE_CloudOps~V` -- the two-slot + TTL build for the two unblocked consumers, and the build-path ground this face inherits), `TO-OP-S-10` (blocked on this face's verdict), rows `Z-S123` and `Z-S124`.
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL denominator 21 -> 5 gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). **This face builds no monitor, alarm or notification; the moratorium is untouched.**
comp-iam: DECLARED-NOT-APPLICABLE -- this face changes a function's build and deploy path, not IAM principals. If a deploy requires a permission the executing identity lacks, that is a ROW, not a silent grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim at cut; its source citations are required to carry `file:line @ <commit-ish>` in the PROOF.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S10C-AC1`, `S10C-AC2`, `S10C-AC3`, `S10C-AC4`, `S10C-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~W/NFRA_OPSEC202609.TO-OP-S-10C.session-analytics-build-path.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S10C-AC1,S10C-AC2,S10C-AC3,S10C-AC4,S10C-AC5"` BEFORE the complete flip. **THE CONTROL THAT MUST BE ABLE TO FAIL IS `S10C-AC1`'s instrument test: an aliveness oracle that cannot say "dead" is the exact instrument that read ZERO on this function under 141,685 invocations.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before any build">Read `0.7.0_AE_CloudOps~V`'s rows and build-path findings rather than re-deriving them. Establish the aliveness instrument's discriminating power BEFORE trusting its reading.</phase>
  <phase id="2" when="before deploy">Rollback named AND its duration estimated, because edge replication is asynchronous and a rollback nobody has timed is a hope. Ledger opened.</phase>
  <phase id="3" when="after">New code confirmed EXECUTING at an edge location, not merely associated; the verdict delivered in writing to `TO-OP-S-10`'s lane with its message id recorded.</phase>
</compiler_tools_mandate>
