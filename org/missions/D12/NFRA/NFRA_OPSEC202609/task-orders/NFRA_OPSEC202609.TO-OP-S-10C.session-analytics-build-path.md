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

## ⛔ TWO INSTRUMENT TRAPS, BOTH MEASURED ON THIS EXACT FUNCTION, BOTH FATAL IF INHERITED

**1. `Invocations` IS NOT AN ORACLE FOR Lambda@Edge.** Row `Z-S124`: the metric reads **ZERO on the busiest consumer in the set** -- the one doing 141,685 invocations. **An aliveness check built on it returns "dead" for a function under heavy production load**, which is the exact reading that would have authorised breaking it. **Whatever instrument this face uses, state what it would show if the function WERE active, and prove that differs from what it shows now.**

**2. Lambda@Edge WRITES ITS LOGS IN THE REGION NEAREST THE VIEWER, NOT IN THE FUNCTION'S HOME REGION.** A log census scoped to `us-east-1` will find little or nothing while the function runs constantly worldwide. **Enumerate the regions before concluding anything from log volume, and print the region denominator.**

## THE BUILD-PATH GROUND ALREADY ESTABLISHED -- inherit it, do not re-derive it

From `0.7.0_AE_CloudOps~V`'s `TO-OP-S-10B` design work: **the bundler inlines imports, so `files[]` does not govern what ships**; and the **canonical `lib/` mirror is gated on `src/`, which neither target has.** ⛔ **Read that seat's rows before writing anything** -- re-deriving it wastes the measurement and risks diverging from it.

## DELIVERABLE

1. **ESTABLISH A REPEATABLE BUILD-AND-DEPLOY PATH FOR `session-analytics`**, or prove one cannot be established and say precisely what blocks it. **The test is not "I deployed it once by hand" -- it is that a second person, or this face's own tooling, can do it again from the repo.**
2. ⛔ **Lambda@Edge DEPLOY MECHANICS ARE NOT ORDINARY LAMBDA MECHANICS AND THE DIFFERENCES ARE LOAD-BEARING:** the function must be **published as a numbered VERSION** (`$LATEST` cannot be associated), the **CloudFront distribution association must be updated to that version**, and **replication to the edge is asynchronous and takes minutes.** ⛔ **ROLLBACK IS THEREFORE SLOW.** Name the rollback and its expected duration **before** the first act; a rollback nobody has timed is a hope.
3. **A TTL / KEY-REFRESH PATH so the function can pick up a rotated key without a redeploy**, if that is achievable. **If it is not, say so** -- then the rotation's ending is "redeploy this consumer as part of every rotation", which is a legitimate answer that must be **written down** rather than discovered during the next rotation.
4. **THE VERDICT `TO-OP-S-10` NEEDS, IN WRITING**, in one of exactly three forms: **(a)** a build path exists and is exercised -- rotation may proceed; **(b)** no build path is achievable -- rotation must route around this consumer, with the route named; **(c)** the function is retirable -- with the evidence, and the retirement is a human's call, not this face's.
5. **Deploy-ledger entry** per applied root (`safe-apply`, never bare), opened before and closed on exercised evidence.
6. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~W/NFRA_OPSEC202609.TO-OP-S-10C.session-analytics-build-path.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S10C-AC1" cell_refs="OP-s-10"/> `S10C-AC1` -- ALIVENESS RE-ESTABLISHED ON AN INSTRUMENT THAT COULD SAY "DEAD": the function's activity confirmed at this assignee's own vintage, **with the instrument named and its discriminating power stated** -- what it would show if the function were idle, and how that differs from what it shows now. ⛔ **`Invocations` is DISQUALIFIED by `Z-S124`** (reads 0 on this very function under load); citing it as the aliveness oracle FAILS this criterion. **Region denominator printed** if the evidence is log-based.
<criterion id="S10C-AC2" cell_refs="OP-s-10"/> `S10C-AC2` -- THE BUILD PATH IS REPEATABLE, NOT A ONE-OFF: the build run **twice** from a clean state producing a **byte-identical or explained-different** artifact, with the commands recorded such that another seat could run them. **A single successful manual build does not pass** -- the whole defect being repaired is that no repeatable path exists.
<criterion id="S10C-AC3" cell_refs="OP-s-10"/> `S10C-AC3` -- DEPLOYED AND SERVING, VERIFIED AT THE EDGE RATHER THAN AT THE API: the published version number, the CloudFront association updated to it, **and evidence the NEW code is actually executing at an edge location** -- not merely that the association was updated. ⛔ **`update-distribution` returning 200 proves a configuration change, never that replication completed**; state how long it took and how you knew it had finished.
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
