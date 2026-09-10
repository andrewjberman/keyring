# TO NFRA_OPSEC202609.TO-OP-S-10E -- BOUND THE SIGNER'S OWN KEY READS: `opalinvest-auth-handler` caches the JWT PRIVATE key with NO time component, so writing a new key does not switch signing and the rotation is unsatisfiable at any wait length. NOT two slots -- a TTL (OP-s-10, FWD-10)

<to_id>NFRA_OPSEC202609.TO-OP-S-10E</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~V</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-09</issued_date>
<status>complete</status>

**BLOCKER: NONE. GO immediately.** Third and last enabling instance on `OP-s-10`. `TO-OP-S-10B` taught two verifiers, `TO-OP-S-10D` the third; this one fixes the WRITE side, which no face in the chain had ever read on this axis.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.14 @5f4d4b894f** (ENDPOINT **FWD-10**) - **Decomp cell:** `OP-s-10` - **Round:** 3.

---

## WHY THIS FACE EXISTS

`TO-OP-S-10`'s rotation stopped a second time, on the SIGNER (`0.7.0_AE_CloudOps~V`, msg 20636, row `Z-S159` @`0de0d1ea2a`). Every face in this chain so far was scoped to VERIFIERS, so the signer's own key selection had never been read.

**MEASURED ON THE DEPLOYED BYTES, not source.** `opalinvest-auth-handler`, CodeSha256 `X8YBkwUqnuTDLW7XvqovWT9+TujBXbTaXQaEdwHxwZc=`, LastModified 2026-09-04T02:14:11Z:

```
async function E8(){ if(pq) return pq;
  if(pq=(await vZ.send(new yZ({SecretId:"opal/auth/jwt-private-key"}))).SecretString||"",!pq)
    throw Error("JWT private key not found"); return pq }

THREE unbounded caches in that one bundle:
  pq  the PRIVATE signing key          <- blocks the rotation
  cq  the PUBLIC key                   <- same one-line-shaped fix, in scope here
  A6  the MFA code seal key (HKDF-derived from the private key)   <- NOT changed here, see below
```

⛔ **WHY IT BLOCKS: WRITING A NEW PRIVATE KEY DOES NOT SWITCH SIGNING.** Each warm container keeps signing with whatever key it first cached, for a lifetime Lambda does not bound. `S10-AC4` -- *"a login performed after the switch yields a token whose header/key-id resolves to the NEW key"* -- is **UNSATISFIABLE AT ANY WAIT LENGTH.** That is precisely the defect `TO-OP-S-10B` was cut to fix, still sitting on the one component the rotation must actually switch.

⭐ **THE INTERNAL CONTROL IS WHY THIS IS A DEFECT RATHER THAN AN ESTATE CONVENTION, AND IT IS IN THE SAME BUNDLE:** the origin-verify read there IS bounded -- `q2=300000`, `if(d6 && q-b1<q2) return d6`. The function demonstrably knows the bounded-cache idiom, applies it to the ORIGIN secret, and applies it to NEITHER JWT key. ⛔ **The single `300000` in the whole bundle belongs to that ORIGIN cache and must not be misread as a JWT key TTL.**

⛔ **AND IT WOULD HAVE READ HEALTHY THROUGHOUT, which is why no consumer-side check could have caught it.** With the verifiers now holding two slots, tokens signed under the retired key AND under the new one both verify. Every per-consumer convergence observation the rotation's GO mandated would come back GREEN -- because the VERIFIERS would genuinely have converged. The SIGNER would not have, and no convergence check aimed at consumers looks there. The old key could then never be retired with confidence, because no observation establishes that no container still signs with it.

## THE WORK -- A TTL, EXPLICITLY NOT TWO SLOTS

**Bound BOTH JWT key reads (`pq` private, `cq` public) with the same idiom already deployed three times today**, reusing the shared module rather than hand-rolling a fourth cache.

⛔ **DO NOT TEACH THE SIGNER TWO SLOTS.** The issuer's re-cut @`dd39dab70e` is explicit: a signer must know which key is CURRENT, and two slots would let it sign under a retired one. The property it lacks is a BOUNDED window, not a second slot. **This face is SMALLER than `TO-OP-S-10D`, not larger.**

⛔ **DO NOT DISTURB THE ORIGIN-VERIFY CACHE.** `q2`/`d6`/`b1` already work and are another cell's landed work. `S10E-AC3` is the negative control on exactly that.

⛔ **DO NOT ROTATE ANYTHING AND DO NOT WRITE EITHER SECRET.** The rotation stays `TO-OP-S-10`'s and stays gated on this face going terminal.

⚠ **THE `source_code_hash` TRAP APPLIES HERE TOO AND IT HAS NOW BITTEN TWICE IN ONE SESSION** (the `qualified_arn` pin, then session-analytics). Read the plan; if the hash is hardcoded, **updating that line IS the deploy** and a "No changes" plan means the artifact is uploaded and unreferenced.

⚠ **Z-S156's WAF RIDE: CHECK, DO NOT ASSUME EITHER WAY.** It applies to a deploy that repoints the CloudFront DISTRIBUTION. `TO-OP-S-10D` measured that targeting the FUNCTION plans 0 wafv2. This is a regular Lambda in `portal-auth`, not Lambda@Edge -- so the ride most likely does not apply, and **`S10E-AC5` requires that be MEASURED and stated rather than asserted.**

## ⛔ THE MFA SEAL KEY IS NAMED HERE AND DELIBERATELY NOT CHANGED

`A6` is HKDF-derived from the private key and its cache is ALSO unbounded, so during a rotation window containers would disagree about the seal key non-deterministically. **It is NOT in this face's scope.** `0.7.0_AE_CloudOps~V` measured that it DEGRADES GRACEFULLY -- `unsealCode` returns null on a wrong key and `mfa.ts`'s callers mint a REPLACEMENT code rather than sending nothing, and verification uses `hashCode` against the stored row and is untouched -- so the consequence is that **resend-idempotency lapses during the window.** That is a RUNBOOK EXPECTATION for `TO-OP-S-10`, recorded here so it is not discovered live. `S10E-AC6` carries it to L9 as a judgment rather than resolving it in this lane.

## TERRITORY, STATED SO IT IS NOT READ AS SCOPE CREEP

PRD s.3 lists the auth-handler Lambda under **"Relies on, does not own"**, with the rule *"Any change this project makes inside those is made through their owners' lanes."* The named owner is the **AE lane `0.7.0_AE_CloudOps`**, and `0.7.0_AE_CloudOps~V` is an instance of it -- so this cut IS the prescribed route, not an exception to it. Precedent inside this project: `TO-OP-S-3` already put origin verification on this same function by this same route.

<expected_criteria>S10E-AC1, S10E-AC2, S10E-AC3, S10E-AC4, S10E-AC5, S10E-AC6</expected_criteria>

<criterion id="S10E-AC1" cell_refs="OP-s-10"><invocation>.tools/aws.cmd lambda get-function --function-name opalinvest-auth-handler --query 'Configuration.[CodeSha256,LastModified]' --output text</invocation><expect>The PRE-CHANGE baseline recorded verbatim, and the UNBOUNDED shape of both JWT reads RE-CONFIRMED on those exact bytes before any change. If either read is already bounded, this face's premise is falsified -- STOP and file a row rather than deploying anyway. A baseline taken after the change is not a baseline.</expect></criterion>

<criterion id="S10E-AC2" cell_refs="OP-s-10"><invocation>.tools/aws.cmd lambda get-function --function-name opalinvest-auth-handler --query 'Configuration.CodeSha256' --output text</invocation><expect>A CodeSha256 DIFFERENT from S10E-AC1's baseline, and the downloaded post-deploy artifact showing BOTH JWT key reads carrying a bounded time component, each still selecting ONE key. Quote both from the DEPLOYED bytes. A two-slot accept path on the signer is a FAIL, not a bonus.</expect></criterion>

<criterion id="S10E-AC3" cell_refs="OP-s-10"><invocation>.tools/aws.cmd lambda get-function --function-name opalinvest-auth-handler --query 'Configuration.CodeSha256' --output text</invocation><expect>NEGATIVE CONTROL: the origin-verify bounded cache is UNCHANGED in the post-deploy artifact -- its guard and its window still present and still 300000. State how the JWT TTL constant is distinguished from it in the new bytes, so no later reader repeats the conflation Z-S159 warns about.</expect></criterion>

<criterion id="S10E-AC4" cell_refs="OP-s-10"><invocation>.tools/aws.cmd logs filter-log-events --log-group-name /aws/lambda/opalinvest-auth-handler --start-time $(( ( $(date +%s) - 900 ) * 1000 )) --filter-pattern "?ERROR ?Traceback ?MODULE_NOT_FOUND" --max-items 50</invocation><expect>LOGIN STILL WORKS after the deploy: no new error class, and the INVOCATION COUNT stated over the window so silence from a dead function cannot pass as health. A cold start on the new bundle observed is stronger than an absence of errors -- state whether one occurred.</expect></criterion>

<criterion id="S10E-AC5" cell_refs="OP-s-10"><invocation>MSYS_NO_PATHCONV=1 .tools/terraform -chdir=infra/aws/terraform/portal-auth plan -target=aws_lambda_function.auth_handler -no-color</invocation><expect>The plan MEASURED and its counts stated: what is added, changed and destroyed, and whether ANY wafv2 resource appears. Z-S156's ride is confirmed ABSENT by reading the plan, never assumed absent because this is not Lambda@Edge. A non-zero wafv2 count means STOP and report.</expect></criterion>

<criterion id="S10E-AC6" cell_refs="OP-s-10" judgment="true"/>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.16), cell `OP-s-10` (manifest S10; FWD-10) -- **the ENABLING limb, third and last instance: the WRITE side.** `TO-OP-S-10` holds the rotation and is blocked until this lands.
<owned_cells>OP-s-10</owned_cells>
Read-dependencies, NOT claimed: `OP-s-10` via `TO-OP-S-10B` and `TO-OP-S-10D` (both COMPLETE -- the shared module and the bounded-TTL idiom, now deployed three times), and `OP-s-3` (COMPLETE -- it put the origin-verify read on this same function, and that read is this face's negative control).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-09 ~20:5xZ at this seat and carried forward unchanged at this cut, no carrier having moved between them. REACHED-DENOMINATORS C1=23, C2=7, C3=12, C4=20, C5=335; the three DECIDABLE carriers arm **26** gates (C1 23 -> 7, C2 7 open deploy-ledger entries -> 7, C3 12 -> 12); C4 SEMI-DECIDABLE 20 -> 0; C5 NOT-DECIDABLE 335 -> 0, of which 137 are non-null prose and are **a reading list, never gates**. **ZERO gates name NFRA_OPSEC202609.** The two DRIFT CANDIDATES are `G-3` (CTO) and `G-7` (POD4); neither binds this face. ⛔ **THE DEPLOY-LEDGER CARRIER BINDS** -- this is a ledgered act on the live login path. ⛔ **Do NOT treat any re-run's total as confirmation of this one:** the components move independently and the same total reached differently reads as confirmation while being nothing of the kind. Orientation at its stated vintage, never a criterion; no face in this project discharges a gate.
comp-iam: DECLARED-NOT-APPLICABLE -- this face creates no role and attaches no policy. `opalinvest-auth-handler` already reads both JWT secrets; that is the defect being bounded, not a permission being added. Whether the read returns the CURRENT value is a property of the call's timing, not of the policy.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim at cut. Its inherited figures (the deployed-bytes shape, the three unbounded caches, the bounded origin read) are cited to msg 20636 and row `Z-S159` @`0de0d1ea2a` and are RE-ESTABLISHED by `S10E-AC1` rather than assumed.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S10E-AC1`, `S10E-AC2`, `S10E-AC3`, `S10E-AC4`, `S10E-AC5`, `S10E-AC6`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~V/NFRA_OPSEC202609.TO-OP-S-10E.signer-key-read-ttl.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S10E-AC1,S10E-AC2,S10E-AC3,S10E-AC4,S10E-AC5,S10E-AC6"` BEFORE the complete flip. **`S10E-AC1` is the control that must be able to fail** -- a pre-change read showing either JWT cache already bounded falsifies this face and the correct act is to STOP. **`S10E-AC6` is a JUDGMENT criterion and carries no verdict from this lane:** whether the MFA seal key's unbounded cache genuinely DEGRADES GRACEFULLY across a rotation window -- `unsealCode` returning null, callers minting a replacement, `hashCode` verification untouched -- and is therefore a runbook expectation rather than a defect, is `3.0.0_SA_CVO~Z`'s at L9. Record it `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO. Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Re-ground on the DEPLOYED bytes at this face's own vintage rather than trusting msg 20636's CodeSha256. Read the shared module at HEAD and reuse it; a fourth hand-rolled cache reproduces `Z-S155` exactly.</phase>
  <phase id="2" when="before the deploy">Ledger opened, rollback named, the plan READ rather than its rc taken, and the live-path baseline captured BEFORE the deploy.</phase>
  <phase id="3" when="after the deploy">Re-probe on the DEPLOYED bytes and on the live login path. ⛔ A redeploy clears a container-bound cache, so any TTL claim measured across a redeploy is void -- hold the environment.</phase>
</compiler_tools_mandate>

<paths>
infra/aws/opalinvest_dev/lambda/auth-handler/
infra/aws/lambda/lib/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/portal-auth/
org/missions/D12/NFRA/NFRA_OPSEC202609/task-orders/NFRA_OPSEC202609.TO-OP-S-10E.signer-key-read-ttl.md
org/missions/D12/NFRA/NFRA_OPSEC202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>
