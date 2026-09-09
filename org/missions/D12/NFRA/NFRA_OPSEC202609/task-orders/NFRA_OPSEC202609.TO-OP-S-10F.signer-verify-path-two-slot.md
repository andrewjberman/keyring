# TO NFRA_OPSEC202609.TO-OP-S-10F -- THE SIGNER IS ALSO A VERIFIER: give its PUBLIC key read two slots while its PRIVATE read stays single-CURRENT. `/auth/refresh` verifies with that read and refresh tokens live SEVEN DAYS (OP-s-10, FWD-10)

<to_id>NFRA_OPSEC202609.TO-OP-S-10F</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~V</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-09</issued_date>
<status>staged</status>

**BLOCKER: NONE. GO immediately.** Fourth and final enabling instance on `OP-s-10`. It corrects a rule THIS ISSUER wrote.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.14 @5f4d4b894f** (ENDPOINT **FWD-10**) - **Decomp cell:** `OP-s-10` - **Round:** 3.

---

## WHY THIS FACE EXISTS, AND THE DEFECT IS THE ISSUER'S

`TO-OP-S-10E`'s `S10E-AC2` required BOTH of the signer's key reads to select ONE key and called a two-slot path on the signer a **FAIL**. `0.7.0_AE_CloudOps~V` implemented exactly that and the criterion graded PASS on accurate evidence. **The rule was right for one read and wrong for the other, and the rationale this issuer gave says so on its face:** *"two slots would let it sign under a retired one."* That is true of the PRIVATE key. **It does not transfer to the PUBLIC one, which does no signing at all.**

⛔ **`opalinvest-auth-handler` PLAYS TWO ROLES AND THE RULE WAS APPLIED TO BOTH:**
```
PRIVATE key read  -> SIGNING.       single-CURRENT is CORRECT and stays. Unchanged by this face.
PUBLIC key read   -> VERIFICATION.  src/jwt.ts:225 verifyAccessToken and :238 verifyRefreshToken
                     both call getJwtPublicKey() and hand the result straight to jwt.verify.
```
Measured on the bytes shipped at 22:38Z (`ZrHoxMzn0YsK5oA1lq0OMcsoaL9xzN3RkYFxY9Opjyk=`): `async function fZ(){ return await T8(U3) }` -- CURRENT only, and `verifyWithSlots` is **not bundled in that artifact at all**.

⛔ **AND NO ORDERING OF THE ENVELOPE SAVES IT.** The rotation writes `{current, previous}`. The three consumers taught by `TO-OP-S-10B`/`10D` accept BOTH slots; the signer accepts ONE. Whichever key sits in `current`, the signer rejects tokens signed by the other. Both orderings were checked before that conclusion was drawn.

⛔ **THE WINDOW IS SEVEN DAYS, NOT A MOMENT.** `REFRESH_TOKEN_EXPIRY '7d'` against `ACCESS_TOKEN_EXPIRY '15m'`. Refresh is the endpoint a client hits *precisely when* its access token has expired, so the failure lands on **every returning user for a week**. Route measured live on the wire: `POST /auth/refresh` returns 401 `{"error":"No refresh token"}` -- the handler ran and answered. Call site `src/auth.ts:435`.

⭐ **THE ESTATE'S STANDARD FOR THIS EXACT CLASS IS ALREADY INSIDE `refresh()` ITSELF**, from `OP-s-11` finding F-10: *"THE OLD SHAPE IS ACCEPTED FOR ONE REFRESH_TOKEN_EXPIRY WINDOW (7d) SO THAT NOBODY IS SIGNED OUT BY THIS CHANGE."* Two token SHAPES accepted for 7 days, for the no-sign-out reason. **The same reasoning applies to two token KEYS and was not applied.**

⛔ **AND EVERY CONDITION THE ROTATION'S GO CARRIED WOULD HAVE PASSED.** The three verifiers would converge and report green per consumer, correctly. The signer would converge on the SIGNING key, correctly. `S10-AC4` would show a NEW-key token from a fresh login, correctly. Every observation would be TRUE and the rotation would still have signed out every returning user through a SIXTH surface nobody was watching -- the signer's own verify path. **That is FWD-10's own bar failing while every mechanical criterion passes.**

## THE WORK -- ONE READ CHANGES, AND THE ASYMMETRY IS THE WHOLE POINT

```
private read  ->  STAYS single-CURRENT   (unchanged; the signing rationale is correct for it)
public  read  ->  getJwtKeySlots + verifyWithSlots, the same two-slot idiom the other three
                  verifiers already carry -- because IN THAT PATH THE SIGNER IS A VERIFIER
```
One function changes. The shared module already exports what it needs. **No new pattern is introduced and no fourth cache is hand-rolled** -- that would reproduce `Z-S155`.

⛔ **DO NOT ROTATE ANYTHING AND DO NOT WRITE EITHER SECRET.** The rotation stays `TO-OP-S-10`'s.

⚠ Carried forward, both already met once on this function: the hardcoded/data-lookup `source_code_hash` question -- read the plan rather than trusting a "No changes"; and `Z-S156`'s WAF ride, measured ABSENT on `TO-OP-S-10E` by reading the plan, to be measured again rather than inherited.

<expected_criteria>S10F-AC1, S10F-AC2, S10F-AC3, S10F-AC4, S10F-AC5</expected_criteria>

<criterion id="S10F-AC1" cell_refs="OP-s-10"><invocation>.tools/aws.cmd lambda get-function --function-name opalinvest-auth-handler --query 'Configuration.[CodeSha256,LastModified]' --output text</invocation><expect>The PRE-CHANGE baseline recorded, and the PUBLIC read RE-CONFIRMED single-CURRENT on those exact bytes with verifyWithSlots absent. If the public read is already two-slot, this face's premise is falsified -- STOP and file a row. A baseline taken after the change is not a baseline.</expect></criterion>

<criterion id="S10F-AC2" cell_refs="OP-s-10"><invocation>.tools/aws.cmd lambda get-function --function-name opalinvest-auth-handler --query 'Configuration.CodeSha256' --output text</invocation><expect>BOTH halves true on the post-deploy DEPLOYED bytes and graded as one: the PUBLIC read reaches a two-slot accept path (verifyWithSlots present and reachable from verifyAccessToken and verifyRefreshToken), AND the PRIVATE read still selects ONE CURRENT key. Either half alone is a FAIL -- a two-slot private read is the defect S10E correctly barred, and a single-key public read is the defect this face exists to fix.</expect></criterion>

<criterion id="S10F-AC3" cell_refs="OP-s-10"><invocation>.tools/aws.cmd logs filter-log-events --log-group-name /aws/lambda/opalinvest-auth-handler --start-time $(( ( $(date +%s) - 900 ) * 1000 )) --filter-pattern "refresh" --max-items 50</invocation><expect>The two-slot accept path REACHED on a real verify, evidenced rather than reasoned about. The genuine two-KEY test needs a previous key that does not exist until the rotation -- if so, file that limb UNCOMPUTABLE-BY-CONSTRUCTION naming the rotation as where it is obtainable, and do NOT record it as passed.</expect></criterion>

<criterion id="S10F-AC4" cell_refs="OP-s-10"><invocation>.tools/aws.cmd logs filter-log-events --log-group-name /aws/lambda/opalinvest-auth-handler --start-time $(( ( $(date +%s) - 900 ) * 1000 )) --filter-pattern "?ERROR ?MODULE_NOT_FOUND ?Traceback" --max-items 50</invocation><expect>LOGIN AND REFRESH BOTH STILL WORK after the deploy, with the invocation count stated so silence from a dead function cannot pass as health. Exercise /auth/refresh explicitly -- it is the surface this face is about and an unexercised fix on it is not evidence.</expect></criterion>

<criterion id="S10F-AC5" cell_refs="OP-s-10"><invocation>.tools/aws.cmd secretsmanager describe-secret --secret-id opal/auth/jwt-private-key --query '[VersionIdsToStages,LastChangedDate,RotationEnabled]' --output json</invocation><expect>NOTHING ROTATED BY THIS FACE: one version at AWSCURRENT, same version id, LastChangedDate unchanged at 2026-04-06, RotationEnabled unset -- for BOTH the private and the public secret. This face teaches a reader; it never writes a secret.</expect></criterion>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.16), cell `OP-s-10` (manifest S10; FWD-10) -- **the ENABLING limb, fourth instance: the signer's VERIFY half.** `TO-OP-S-10` holds the rotation and is blocked until this lands.
<owned_cells>OP-s-10</owned_cells>
Read-dependencies, NOT claimed: `OP-s-10` via `TO-OP-S-10B`, `TO-OP-S-10D` and `TO-OP-S-10E` (all COMPLETE -- the shared module, the two-slot idiom and the bounded read this face builds on), and `OP-s-11` (COMPLETE -- finding F-10's 7-day old-shape acceptance, the estate's own precedent for this class).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-09 ~23:0xZ at this seat and carried forward unchanged, no carrier having moved between them. REACHED-DENOMINATORS C1=23, C2=7, C3=12, C4=20, C5=335; three DECIDABLE carriers arm **26** gates (C1 23 -> 7, C2 7 open deploy-ledger entries -> 7, C3 12 -> 12); C4 SEMI-DECIDABLE 20 -> 0; C5 NOT-DECIDABLE 335 -> 0, of which 137 are non-null prose -- **a reading list, never gates**. **ZERO gates name NFRA_OPSEC202609.** DRIFT CANDIDATES `G-3` (CTO) and `G-7` (POD4) bind nothing here. ⛔ **THE DEPLOY-LEDGER CARRIER BINDS** -- a ledgered act on the live login path. ⛔ Do NOT treat a re-run's total as confirmation of this one; the components move independently.
comp-iam: DECLARED-NOT-APPLICABLE -- no role created, no policy attached. The function already reads the public secret; this face changes how the returned value is CONSUMED, not whether it may be read.
comp-adversary: DECLARED-NOT-APPLICABLE -- no commit-scoped claim pinned at cut. The inherited figures (the shipped CodeSha256, the two call sites, the 7d/15m expiries, the live 401 on /auth/refresh) are cited to msg 20669 and row `Z-S160` @`7e8cc537af` and are RE-ESTABLISHED by `S10F-AC1` rather than assumed.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S10F-AC1`, `S10F-AC2`, `S10F-AC3`, `S10F-AC4`, `S10F-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~V/NFRA_OPSEC202609.TO-OP-S-10F.signer-verify-path-two-slot.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S10F-AC1,S10F-AC2,S10F-AC3,S10F-AC4,S10F-AC5"` BEFORE the complete flip. **`S10F-AC1` is the control that must be able to fail.** **`S10F-AC2` IS DELIBERATELY A PAIRED CRITERION** -- both halves graded together, because the defect this face corrects was created by a rule that treated one component as having one role. Grading the halves separately would reproduce exactly that error. Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Re-ground on the DEPLOYED bytes at this face's own vintage. ⛔ **Enumerate every READ of a key value in the bundle and state what each is USED FOR -- per READ, not per component.** That is the check that would have caught this defect and it is now mandatory here.</phase>
  <phase id="2" when="before the deploy">Ledger opened, rollback named, the plan READ rather than its rc taken, live-path baseline captured for BOTH /auth/login and /auth/refresh.</phase>
  <phase id="3" when="after the deploy">Re-probe both surfaces on the DEPLOYED bytes and on the wire. A redeploy clears a container-bound cache, so any TTL claim measured across one is void.</phase>
</compiler_tools_mandate>

<paths>
infra/aws/opalinvest_dev/lambda/auth-handler/
infra/aws/lambda/lib/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/portal-auth/
org/missions/D12/NFRA/NFRA_OPSEC202609/task-orders/NFRA_OPSEC202609.TO-OP-S-10F.signer-verify-path-two-slot.md
org/missions/D12/NFRA/NFRA_OPSEC202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>
