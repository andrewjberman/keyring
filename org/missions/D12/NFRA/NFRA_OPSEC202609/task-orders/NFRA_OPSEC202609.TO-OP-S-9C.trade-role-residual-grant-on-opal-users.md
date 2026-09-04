# TO NFRA_OPSEC202609.TO-OP-S-9C -- THE RESIDUAL GRANT ON `opal-users` LIVES IN A DIFFERENT ROOT AND BACKS SEVEN LIVE LAMBDAS: `trade-submission-lambda-role` holds full CRUD on the table and no trade code names it -- but "no code names it" is a SOURCE-plane claim, and this face may not remove the grant until a RUNTIME oracle agrees or is declared unobtainable (OP-s-9, round 2c)

<to_id>NFRA_OPSEC202609.TO-OP-S-9C</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~X</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-04</issued_date>
<status>staged</status>

⛔ **GO CONDITION: `TO-OP-S-9-11` TERMINAL.** This face is the round-2c continuation of the same cell and the same lane holds every measurement it needs. **It is a SEPARATE CUT rather than a limb of that face for three measured reasons: a different terraform root, a role backing SEVEN live functions, and evidence of disuse that exists only on the source plane.**

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (C-1 least privilege on the identity tables; s.9 item 5) - **Decomp cell:** `OP-s-9` (manifest row S9, round 2c) - **Lane:** `infra/aws/terraform/trade-pipeline/`, AE lane - **Round:** 3.

---

## WHY THIS IS ITS OWN FACE AND NOT A LINE IN `TO-OP-S-9-11`

`0.7.0_AE_CloudOps~X` re-grounded `TO-OP-S-9-11`'s premises before writing anything and found the face's model of the world wrong in a way that mattered: **it modelled TWO ARNs on ONE role in ONE root; the live population is THREE statements across TWO roles in TWO roots** (row `Z-S112`, @`776437a094`).

**`trade-submission-lambda-role` holds `dynamodb:GetItem/PutItem/UpdateItem/DeleteItem/Query/Scan` on `table/opal-users` AND `table/opal-users/index/*`**, declared at `infra/aws/terraform/trade-pipeline/iam.tf:63-64`. That role is the execution role of **seven live functions**: `trade-auth-handler`, `trade-authorizer`, `trade-dashboard-api`, `trade-identifier-cache`, `trade-parquet-batch-export`, `trade-submission-handler`, `trade-workflow-handler`.

**THE MEASUREMENT THAT FOUND IT CARRIED ITS OWN POSITIVE CONTROL AND THAT IS WHY IT IS TRUSTED:** an applied-plane census over `iam:GetAccountAuthorizationDetails`, account `313476888478`, vintage `2026-09-04T00:26:29Z`, **221 roles / 1173 inline statements**, with a matcher excluding `-v2`/`-master`/`-trade`. **The same census returns 4 roles for the v2 ARN**, so the two-role result is a measurement rather than an empty regex.

## ⛔ THE ONE THING THAT MUST NOT BE ASSUMED, AND IT IS THE WHOLE REASON FOR THIS FACE'S GATE

The grant reads **vestigial by code**: `comp-find` over the trade lambda and terraform trees returns **denominator 2 hits across 302 files, and BOTH hits ARE the grant lines themselves.** Zero trade source names the table.

>> **THAT IS A REPO-SOURCE CLAIM ABOUT SEVEN FUNCTIONS WHOSE DEPLOYED BYTES MAY BE OLDER THAN THE REPO. RUNNING-BYTES-OLDER-THAN-BUILT PASSES EVERY SOURCE RUNG** (CLAUDE.md 22a). A clean source census and a live caller are indistinguishable on this evidence, and the failure mode is not a plan diff -- it is **seven production functions losing access to an identity table**, discovered by whichever one next needs it. <<

## DELIVERABLE

1. **ESTABLISH A RUNTIME ORACLE, OR DECLARE ONE UNOBTAINABLE.** In order of preference:
   - **CloudTrail data events on `opal-users`** -- ⛔ **check whether they are enabled; do not assume either way.** DynamoDB data events are off by default, and *"CloudTrail shows no access"* from a trail that never recorded data events is a **false absence**, not a clean bill.
   - **The deployed bytes of all seven functions compared against their build input** (source map / build manifest), **never by filename** -- if the deployed bytes match a source tree that does not name the table, the source census transfers to the applied plane.
   - **If neither is obtainable, this criterion files `UNVERIFIABLE-BY-INSTRUMENT` and THE GRANT STAYS.** That is a complete and acceptable outcome for this face. **An honest non-removal beats a removal justified by an instrument that cannot see the thing it is trusted to rule out.**
2. **ONLY IF THE ORACLE AGREES: remove `trade-pipeline/iam.tf:63-64`**, with the deploy-ledger entry opened before and the rollback named before the first act.
3. **THE SEVEN FUNCTIONS EXERCISED AFTER, EACH ONE, not a sample.** A grant removal that breaks one of seven is not caught by testing three.
4. **The residual set re-enumerated after the act**, so `TO-OP-S-9-11`'s named residual is either discharged or restated with what remains.
5. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~X/NFRA_OPSEC202609.TO-OP-S-9C.trade-role-residual-grant-on-opal-users.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S9C-AC1" cell_refs="OP-s-9"/> `S9C-AC1` -- THE RUNTIME PLANE WAS INTERROGATED AND ITS INSTRUMENT'S REACH IS STATED: whether CloudTrail data events on `opal-users` are enabled, read and pasted; if enabled, the access census over a stated window with its denominator; if not enabled, **that fact stated explicitly as the reason a no-access reading would have been vacuous.** ⛔ **A quiet trail is not evidence of no access unless the trail was recording the events in question** -- this criterion FAILS on a no-access claim from an unverified trail.
<criterion id="S9C-AC2" cell_refs="OP-s-9"/> `S9C-AC2` -- THE SOURCE CENSUS WAS TRANSFERRED TO THE DEPLOYED BYTES, OR DECLARED UNTRANSFERABLE: for each of the seven functions, the deployed artifact compared against its build input by CONTENT, never by filename, with the denominator **7 of 7** printed. Any function whose deployed bytes cannot be resolved to a source tree is named, and its presence forces `UNVERIFIABLE-BY-INSTRUMENT` on the removal.
<criterion id="S9C-AC3" cell_refs="OP-s-9"/> `S9C-AC3` -- THE ACT MATCHES THE VERDICT: if the oracles agreed, the `iam.tf` diff and the applied policy re-read showing `:63-64` absent; **if they did not, NO DIFF EXISTS and this criterion PASSES on the stated non-removal with its reason.** ⛔ **Both outcomes pass this criterion. Only an unevidenced removal fails it.**
<criterion id="S9C-AC4" cell_refs="OP-s-9"/> `S9C-AC4` -- ALL SEVEN FUNCTIONS EXERCISED AFTER ANY REMOVAL, WITH A BEFORE: each of the seven invoked before and after, both results pasted, denominator **7 of 7**. **The before is what makes the after mean anything.** If no removal occurred, this files `N/A-BY-CONSTRUCTION` naming `S9C-AC3`'s outcome.
<criterion id="S9C-AC5" cell_refs="OP-s-9"/> `S9C-AC5` -- BASELINE QUOTED, 0-DIFF AFTER, NOTHING ELSE RODE: the trade-pipeline root's UNSCOPED plan before the first edit; the changed-resource list enumerated with its count; the UNSCOPED re-plan 0-diff after; ledger CLOSED on exercised evidence rather than an apply's rc; push state read by `ls-remote` + `is-ancestor` and stated as MEASURED.

<expected_criteria>S9C-AC1, S9C-AC2, S9C-AC3, S9C-AC4, S9C-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc>, cell `OP-s-9` (manifest row S9; FWD-9), round 2c. **This face adds NO new cell and NO new manifest row** -- it is a second task order on an existing cell whose live population turned out wider than the cell text assumed, following the `TO-OP-S-8R2B` and `TO-OP-S-10B` precedent.
<owned_cells>OP-s-9</owned_cells>
Read-dependencies, NOT claimed: `TO-OP-S-9-11` (the portal-auth root's two ARNs -- this face does not touch them), row `Z-S112` (the enumeration this face acts on).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL denominator 21 -> 5 gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0).
comp-iam: RUN -- this face is entirely about an IAM grant, and the assignee's own applied-plane census at vintage 2026-09-04T00:26:29Z (221 roles / 1173 inline statements, positive control returning 4 roles for the v2 ARN) is the grounding. **Re-run it at the assignee's own vintage before acting; a census taken an hour earlier is not a census taken now.** Its silence is never an ALLOW.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim at cut; its source citations are required to carry `file:line @ <commit-ish>` in the PROOF.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S9C-AC1`, `S9C-AC2`, `S9C-AC3`, `S9C-AC4`, `S9C-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~X/NFRA_OPSEC202609.TO-OP-S-9C.trade-role-residual-grant-on-opal-users.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S9C-AC1,S9C-AC2,S9C-AC3,S9C-AC4,S9C-AC5"` BEFORE the complete flip. **THE CONTROL THAT MUST BE ABLE TO FAIL IS `S9C-AC1`'s trail check: a no-access reading from a trail that never recorded DynamoDB data events is the false absence this entire face exists to refuse.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before any act">Establish the runtime oracle's REACH before its result. Ask what the instrument would show if the grant WERE in use, and if the answer is "the same thing", the instrument is not an oracle.</phase>
  <phase id="2" when="before removal">Ledger opened, rollback named, and the seven functions' pre-state captured. A removal whose before-state was never read cannot be shown harmless.</phase>
  <phase id="3" when="after">All seven exercised, the residual set re-enumerated, and the ledger closed on that evidence rather than on an apply's return code.</phase>
</compiler_tools_mandate>
