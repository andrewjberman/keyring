# TO NFRA_OPSEC202609.TO-OP-S-10D -- TEACH THE THIRD VERIFIER TWO SLOTS: `opal-session-analytics` reads the JWT public key into ONE scalar with NO time component on its DEPLOYED bytes, at 52,540 invocations in 7 days, and it is the last thing standing between this project and FWD-10's rotation (OP-s-10, FWD-10)

<to_id>NFRA_OPSEC202609.TO-OP-S-10D</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~V</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-09</issued_date>
<status>staged</status>

**BLOCKER: NONE. GO immediately.** This face is the remedy that `TO-OP-S-10`'s binding condition produced, addressed to the same lane because it already holds every read this face needs and deployed the identical idiom to the other two verifiers today.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.14 @5f4d4b894f** (ENDPOINT **FWD-10**) - **Decomp cell:** `OP-s-10` (the enabling limb, second instance) - **Round:** 3.

---

## WHY THIS FACE EXISTS, AND WHY IT IS A CUT RATHER THAN AN EXTENSION

`TO-OP-S-10B` taught two slots and a 300 s TTL to the two verifiers it owned. `TO-OP-S-10`'s rotation was then gated by the issuer on establishing the CONSUMER DENOMINATOR first. **That gate closed and the STOP branch fired** (`0.7.0_AE_CloudOps~V`, msg 20616, row `Z-S157` @`f3731b9705`).

**MEASURED, and the census is the reason this face is narrow:** 203 live functions (`NextMarker` ABSENT -- a real denominator, not a page) across 115 roles; the five roles granting `secretsmanager:GetSecretValue` on `opal/auth/jwt-public-key` carry 31 of them; 29 of 31 deployed artifacts downloaded and searched for the literal secret id; **25 no-hit, 4 READERS.** Of the four: two were taught by `TO-OP-S-10B`; one is `opalinvest-auth-handler`, **THE SIGNER, correctly single-slot**; and one is the blocker.

```
opal-session-analytics   opal-portal-lambda-role   SINGLE-SLOT, NO TTL   *** THIS FACE ***
  CodeSha256 TW+G6NyLoKxqCdp6CtfU5WAixRf8phcP69Kxg6kx8EU=  LastModified 2026-09-04T05:44:08Z
  async function lJ(){ if(wq) return wq;
    if(wq=(await cJ.send(new uJ({SecretId:"opal/auth/jwt-public-key"}))).SecretString||"",!wq)
      throw Error("JWT public key not found"); return wq }
  ONE scalar, `if(wq) return wq` with NO time component, ONE occurrence of the secret id.
  Source agrees at src/auth.ts:42-56, single jwt.verify at :75.
  ALIVE: 52,540 invocations over 7 days (18,035 / 8,679 / 585 / 42 / 7,283 / 17,916 by day).
```

⛔ **WHY THE ROTATION CANNOT SIMPLY PROCEED AND WAIT FOR A COMPLAINT.** The cache is bounded by CONTAINER LIFETIME, so a rotation under a single-slot reader does not break loudly. It produces a **PARTIAL, SILENT, SELF-CLEARING outage of unbounded tail** (`TO-OP-S-10C` verdict (a); the correction at msg 20309 that "breaks permanently" is WRONG). ⭐ **A CLEAN POST-ROTATION CHECK IS CONSISTENT WITH THAT OUTAGE, so there is no post-hoc verification that catches it. The only control is not rotating until this face lands.**

## ⛔ TWO INSTRUMENT FAILURES THE CENSUS SEAT CAUGHT IN ITSELF -- INHERIT BOTH, DO NOT RE-DISCOVER THEM

1. **THE CENSUS FIRST RETURNED A FALSE CLEAN: `READERS: 0` across all 31**, because python cannot exec the `.tools/aws` bash shim on Windows (`WinError 193`). A summary line reading zero that meant *the probe never ran*; **the error count of 31 was the only tell.** Use `.tools/aws.cmd`, and POSITIVE-CONTROL any census before trusting it -- a known reader must HIT and a known non-reader must not.
2. **AN ABSENCE OF A SOURCE-LEVEL NAME IN A COMPILED ARTIFACT IS NOT EVIDENCE ABOUT BEHAVIOUR.** A first pass grepped the deployed bundle for `cachedPublicKey` and got 0, which reads as *the single-slot cache is gone*. It is not gone -- `tsc` renamed it to `wq`. Search the deployed bytes for the SECRET ID and the CACHE SHAPE, never for a source identifier.

## THE WORK

**Teach `opal-session-analytics` the same current-or-previous read with the same bounded TTL the other two verifiers now carry.** `TO-OP-S-10C` established the lawful build path for this function and proved it with two clean builds byte-identical to the deployed artifact; that path is the one to use. The function has a `src/` directory, the canonical build already mirrors `infra/aws/lambda/lib/` into it, and `jwtPublicKeys.mjs` is already present in its tree -- so this is an import swap plus the TTL, not a research problem.

⛔ **REUSE THE SHARED MODULE. DO NOT HAND-ROLL A THIRD CACHE.** One estate, one two-slot idiom -- the same bar `TO-OP-S-10B` was held to. A second hand-rolled cache in this handler would reproduce exactly the `Z-S155` defect (two independent 300 s caches in one handler, indistinguishable to the obvious instrument).

⛔ **DO NOT ROTATE ANYTHING IN THIS FACE, AND DO NOT WRITE THE SECRET.** The rotation is `TO-OP-S-10`'s and is gated on this face going terminal.

## ⛔ DELIVERABLE 0 -- CLOSE THE TWO THE CENSUS COULD NOT READ, OR FILE THEM UNCOMPUTABLE WITH THE REASON

`opal-news-ai-sentiment` and `news-semantic-clustering` are `PackageType Image` (ECR `finbert-lambda:latest`, `news-semantic-clustering:latest`), so there is no zip to fetch and **the 25 zeros DO NOT COVER THEM.** Close them by pulling the images and searching their layers, or file `UNCOMPUTABLE-BY-CONSTRUCTION` naming what was attempted. **A rotation taken with two unread candidates is a rotation taken against an open denominator, and the whole reason this face exists is that an unestablished denominator is load-bearing at rotation time.**

⚠ **AND STATE THE FRAME'S OWN LIMITS IN THE INSTANCE RATHER THAN LETTING A LATER READER ASSUME THEM:** a dynamically-built secret id would not match a literal needle; a reader outside the five granting roles is out of frame entirely; and **the code plane says who CAN read, never who DOES.**

<expected_criteria>S10D-AC0, S10D-AC1, S10D-AC2, S10D-AC3, S10D-AC4, S10D-AC5</expected_criteria>

<criterion id="S10D-AC0" cell_refs="OP-s-10"><invocation>.tools/aws.cmd lambda get-function --function-name opal-news-ai-sentiment --query 'Configuration.[PackageType,ImageConfigResponse]' --output json</invocation><expect>PackageType Image confirmed for the two image-packaged candidates, and EITHER their layers searched for the literal secret id with the result stated, OR an explicit UNCOMPUTABLE-BY-CONSTRUCTION naming what was attempted. A silent omission is a FAIL.</expect></criterion>

<criterion id="S10D-AC1" cell_refs="OP-s-10"><invocation>.tools/aws.cmd lambda get-function --function-name opal-session-analytics --query 'Configuration.[CodeSha256,LastModified,State]' --output text</invocation><expect>The PRE-CHANGE baseline recorded verbatim, CodeSha256 reading TW+G6NyLoKxqCdp6CtfU5WAixRf8phcP69Kxg6kx8EU= or, if it has moved since 2026-09-09 20:4xZ, the new value recorded and the single-slot shape RE-CONFIRMED on those bytes before any change. A baseline taken after the change is not a baseline.</expect></criterion>

<criterion id="S10D-AC2" cell_refs="OP-s-10" judgment="true"/>

<criterion id="S10D-AC3" cell_refs="OP-s-10"><invocation>.tools/aws.cmd lambda get-function --function-name opal-session-analytics --query 'Configuration.CodeSha256' --output text</invocation><expect>A CodeSha256 DIFFERENT from S10D-AC1's baseline, and the downloaded post-deploy artifact searched for the secret id showing the current-or-previous accept path and a bounded time component. Searched on the DEPLOYED BYTES, never on source, and never for a source-level identifier.</expect></criterion>

<criterion id="S10D-AC4" cell_refs="OP-s-10"><invocation>.tools/aws.cmd logs filter-log-events --log-group-name /aws/lambda/opal-session-analytics --start-time $(( ( $(date +%s) - 900 ) * 1000 )) --filter-pattern "?ERROR ?jwt ?verify" --max-items 50</invocation><expect>The function still verifying real traffic after the deploy: no new error class attributable to the key read, on a function averaging thousands of invocations a day. Silence alone is NOT sufficient -- state the invocation count over the window so a dead function cannot pass as a healthy one.</expect></criterion>

<criterion id="S10D-AC5" cell_refs="OP-s-10"><invocation>.tools/aws.cmd secretsmanager describe-secret --secret-id opal/auth/jwt-public-key --query '[VersionIdsToStages,LastChangedDate,RotationEnabled]' --output json</invocation><expect>NOTHING ROTATED BY THIS FACE: one version at AWSCURRENT with the same version id, LastChangedDate unchanged at 2026-04-06, RotationEnabled unset. This face teaches a reader; it never writes the secret.</expect></criterion>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> (v0.1.16), cell `OP-s-10` (manifest S10; FWD-10) -- **the ENABLING limb, second instance.** `TO-OP-S-10B` closed the first two verifiers; this closes the third. `TO-OP-S-10` holds the rotation and is blocked until this lands.
<owned_cells>OP-s-10</owned_cells>
Read-dependencies, NOT claimed: `OP-s-10` via `TO-OP-S-10B` (COMPLETE -- the shared two-slot module and the 300 s TTL idiom to reuse), and `TO-OP-S-10C` (COMPLETE -- it established and proved this function's lawful build path with two clean builds byte-identical to the deployed artifact).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-09 ~20:5xZ at this seat. REACHED-DENOMINATORS C1=23, C2=7, C3=12, C4=20, C5=335. The three DECIDABLE carriers arm **26** gates: C1 SENTINEL 23 lines -> 7 (grouped by discharge condition), C2 DEPLOY-LEDGER 7 open entries -> 7, C3 MORATORIA 12 standing NEVER clauses -> 12. C4 SCOPE-GUARD is SEMI-DECIDABLE, 20 -> 0. C5 PROJECT-BLOCKING is NOT-DECIDABLE, 335 -> 0, of which 137 carry non-null prose -- **a reading list, never gates.** **ZERO gates name NFRA_OPSEC202609.** The two DRIFT CANDIDATES are `G-3` (owner CTO, the never-widen co-sign on inf silver) and `G-7` (owner POD4, the trading-calendar guard); **neither binds this face.** ⛔ **THE DEPLOY-LEDGER CARRIER BINDS:** this is a ledgered act on a live function, and C2 reads **7 OPEN entries** at this vintage -- four of which `0.7.0_AE_CloudOps~V` surfaced as PAST-WINDOW and belonging to other seats (msg 20612), none of them this face's to close. ⭐ **THE DEFECT `1.0.0_SA_CTO~Z` NAMED AT msg 20364 IS NOW FIXED IN THE TOOL, not merely worked around:** C1 excludes `org/mcp/inbox` AND any line inside a fence, so an agent QUOTING a sentinel is no longer counted as one. ⛔ **DO NOT TREAT ANY RE-RUN'S TOTAL AS CONFIRMATION OF AN EARLIER ONE** -- `TO-OP-S-10B` carried 20 at its vintage and the carriers have moved since; the same total reached from different components reads as confirmation and is nothing of the kind. This figure is ORIENTATION at its stated vintage, never a criterion, and no face in this project discharges a gate.
comp-iam: DECLARED-NOT-APPLICABLE -- this face creates no role and attaches no policy. `opal-session-analytics` already holds `secretsmanager:GetSecretValue` on this secret via `opal-portal-lambda-role`; that grant is what the census used to FIND it. Whether it can read the PREVIOUS slot is a property of the value returned, not of the policy, and is verified on the deployed bytes by `S10D-AC3`.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim at cut. Its one inherited figure (the 4-reader census) is cited to msg 20616 and row `Z-S157` @`f3731b9705` and is RE-ESTABLISHED rather than assumed wherever this face acts on it.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S10D-AC0`, `S10D-AC1`, `S10D-AC2`, `S10D-AC3`, `S10D-AC4`, `S10D-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~V/NFRA_OPSEC202609.TO-OP-S-10D.session-analytics-two-slot.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S10D-AC0,S10D-AC1,S10D-AC2,S10D-AC3,S10D-AC4,S10D-AC5"` BEFORE the complete flip. **`S10D-AC1` is the control that must be able to fail:** if the pre-change bytes do NOT read single-slot, the premise of this whole face is falsified and the correct act is to STOP and file a row, not to deploy anyway. **`S10D-AC2` is a JUDGMENT criterion and carries no verdict here** -- whether the shared module was genuinely REUSED rather than a third cache hand-rolled beside it is `3.0.0_SA_CVO~Z`'s at L9; record it `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming the CVO. Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Re-ground: re-read `opal-session-analytics`'s DEPLOYED bytes at this face's own vintage rather than trusting msg 20616's CodeSha256, and re-read the shared module in `infra/aws/lambda/lib/` at HEAD. Confirm `TO-OP-S-10C`'s build path still reproduces the deployed artifact before changing anything.</phase>
  <phase id="2" when="before the deploy">Ledger opened, rollback named, and the live-path baseline captured BEFORE the deploy. Deliverable 0's image census closed or filed.</phase>
  <phase id="3" when="after the deploy">Re-probe on the DEPLOYED bytes and on the live path. ⛔ A redeploy is the mechanism that already clears a container-bound cache, so any TTL claim measured across a redeploy is void -- hold the environment, exactly as `S10B-AC2` did.</phase>
</compiler_tools_mandate>

<paths>
infra/aws/opalinvest_dev/lambda/session-analytics/
infra/aws/lambda/lib/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D12/NFRA/NFRA_OPSEC202609/task-orders/NFRA_OPSEC202609.TO-OP-S-10D.session-analytics-two-slot.md
org/missions/D12/NFRA/NFRA_OPSEC202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>
