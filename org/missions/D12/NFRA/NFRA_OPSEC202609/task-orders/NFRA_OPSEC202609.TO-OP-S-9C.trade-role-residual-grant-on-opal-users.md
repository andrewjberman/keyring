# TO NFRA_OPSEC202609.TO-OP-S-9C -- THE RESIDUAL GRANT ON `opal-users` LIVES IN A DIFFERENT ROOT AND BACKS SEVEN ATTACHED LAMBDAS OF WHICH FIVE ARE DORMANT 51-129 DAYS: `trade-submission-lambda-role` holds full CRUD on the table and no trade code names it -- but "no code names it" is a SOURCE-plane claim, and this face may not remove the grant until a RUNTIME oracle agrees or is declared unobtainable (OP-s-9, round 2c)

<to_id>NFRA_OPSEC202609.TO-OP-S-9C</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~X</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete</status>

⛔ **GO CONDITION: `TO-OP-S-9-11` TERMINAL.** This face is the round-2c continuation of the same cell and the same lane holds every measurement it needs. **It is a SEPARATE CUT rather than a limb of that face for three measured reasons: a different terraform root, a role backing SEVEN ATTACHED functions, and evidence of disuse that exists only on the source plane.**

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (C-1 least privilege on the identity tables; s.9 item 5) - **Decomp cell:** `OP-s-9` (manifest row S9, round 2c) - **Lane:** `infra/aws/terraform/trade-pipeline/`, AE lane - **Round:** 3.

---

## WHY THIS IS ITS OWN FACE AND NOT A LINE IN `TO-OP-S-9-11`

`0.7.0_AE_CloudOps~X` re-grounded `TO-OP-S-9-11`'s premises before writing anything and found the face's model of the world wrong in a way that mattered: **it modelled TWO ARNs on ONE role in ONE root; the live population is THREE statements across TWO roles in TWO roots** (row `Z-S112`, @`776437a094`).

**`trade-submission-lambda-role` holds `dynamodb:GetItem/PutItem/UpdateItem/DeleteItem/Query/Scan` on `table/opal-users` AND `table/opal-users/index/*`**, declared at `infra/aws/terraform/trade-pipeline/iam.tf:63-64`. That role is the execution role of **seven ATTACHED functions** -- ⛔ **NOT "seven LIVE functions", which is what this face said until 2026-09-04 03:2xZ and which was FALSE; see the correction below**: `trade-auth-handler`, `trade-authorizer`, `trade-dashboard-api`, `trade-identifier-cache`, `trade-parquet-batch-export`, `trade-submission-handler`, `trade-workflow-handler`.

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
⛔ **AMENDED 2026-09-04 02:5xZ BY THE ISSUER ON ROW Z-S128. TWO OF THE SEVEN SEND MAIL AND MUST NOT BE INVOKED.** `trade-submission-handler` and `trade-workflow-handler` carry live `EMAIL_FROM` / dashboard recipients. **Invoking a function whose effect is sending mail to a real address is egress off our infrastructure and it is NOT reversible** -- an email cannot be un-sent, and a test invocation reaching a real inbox is a worse outcome than an unverified criterion.
**THE AMENDED BAR -- THE SAME RULE THIS SEAT SET ON `S12-AC4`: YOU DO NOT NEED TO INVOKE A FUNCTION TO VERIFY IT, YOU NEED TO OBSERVE IT.**
- **Five of seven: invoke BEFORE and AFTER, exactly as originally written, denominator 5 of 5.**
- **Two of seven: OBSERVE.** Declare an observation window **derived from each function's own trigger cadence, never a round number**, and confirm each **executed successfully AFTER the removal** from its own invocation record. **An observed production run is STRICTLY STRONGER than a driven one** -- it proves the function works unattended, on its own inputs, on its own schedule.
- ⛔ **If either is not observed inside its window it is NOT verified: RESTORE the grant and file that as the finding.** **Do not convert an unobserved function into a verified one by reasoning that the byte scan was clean.** The byte scan is why the removal is attemptable; it is not why it is safe.
**PASSES ON: 5 invoked with befores + 2 observed post-removal, or a restore with the unobserved function named.**

⛔⛔ **RE-RULED 2026-09-04 03:2xZ ON ROW Z-S130, AND THE AMENDMENT ABOVE IS SUPERSEDED BECAUSE IT RESTED ON A FALSE PREMISE THAT I PROPAGATED.** `0.7.0_AE_CloudOps~X` filed and committed BEFORE acting: **"seven LIVE lambdas" was never measured.** It came from the graph's `lambda.Role` edge census, **which records ATTACHMENT** -- and attachment is not liveness. The second question was never asked. **That adjective travelled from row `Z-S112` into this face's title and body and then into my `Z-S128` ruling, and every carrier repeated it in good faith.**
**MEASURED ON TWO INDEPENDENT PLANES THAT PARTITION THE SET IDENTICALLY: FIVE OF SEVEN ARE DORMANT.** CloudWatch `Invocations` over 30 days -- `trade-submission-handler` 0, `trade-workflow-handler` 0, `trade-auth-handler` 0, `trade-authorizer` 0, `trade-identifier-cache` 0; `trade-dashboard-api` 58 over 10 active days; `trade-parquet-batch-export` 90 over 30. CloudWatch **Logs** last-event, a different plane with different retention and different failure modes: the same five at **51, 51, 129, 129 and 52 days**; the same two at 0. **The positive control is INSIDE the metrics query -- the identical namespace and dimension shape returns real datapoints for two of the seven, so the five zeroes are absences and not a dead probe.** An intermediate Logs query returning NO-EVENTS for all seven **including the two known-live ones** was caught and discarded, because a broken probe and a true absence read identically.
⛔ **WHY THE OBSERVATION ROUTE IS STRUCTURALLY IMPOSSIBLE, NOT MERELY SLOW: the two mail senders HAVE NO CADENCE.** Zero event source mappings, resource policies admitting only API Gateway -- **they fire when a human submits a trade, and none has for 51 days.** "A window derived from each function's own trigger cadence" cannot be constructed from a cadence that does not exist, **so as written the criterion could never be satisfied and the grant would stay by DEFAULT rather than by FINDING.** That is the failure mode this face exists to refuse, arriving through my own amendment.
**THE FINAL BAR, AND IT IS THE LAST WORD ON `S9C-AC4`:**
- **FIVE invoked BEFORE and AFTER** -- the five that send no mail -- **denominator 5 of 5.** ⛔ **Dormancy does NOT excuse invoking them: a dormant function is invocable, and these five are the CONTROL ON THE BYTE SCAN.**
- **TWO (`trade-submission-handler`, `trade-workflow-handler`) file `UNCOMPUTABLE-BY-CONSTRUCTION`**, naming the construction precisely: **no event source mapping, API-Gateway-only resource policy, 51 days dormant, and mail egress barring a driven invocation.** **Both routes are closed and the face says so rather than pretending one is open.**
⭐ **WHAT MAKES THIS A BOUNDED WEAKENING RATHER THAN AN UNVERIFIED REMOVAL, STATED SO NOBODY HAS TO RECONSTRUCT IT: the deployed bytes of all seven name the table ZERO times, with the positive control firing on the same artifacts and matcher family, and env vars on 7 of 7 point only at `opal-users-v2`. So there is no code path in these functions that touches the table at all.** The invocation test was always a **CONTROL ON THE BYTE SCAN**, never a test of the function. **Two of seven lacking that control is a stated, bounded reduction in corroboration -- not an absence of evidence.**
⛔ **AND THE RESIDUAL IS REAL AND GOES IN THE RUNBOOK, NOT A MONITOR: if a trade submission ever fails on a DynamoDB access denial, THIS REMOVAL IS THE FIRST THING TO CHECK, and the rollback is one apply.** Write that where a person diagnosing a failed trade will meet it.
<criterion id="S9C-AC5" cell_refs="OP-s-9"/> `S9C-AC5` -- BASELINE QUOTED, 0-DIFF AFTER, NOTHING ELSE RODE: the trade-pipeline root's UNSCOPED plan before the first edit; the changed-resource list enumerated with its count; the UNSCOPED re-plan 0-diff after; ledger CLOSED on exercised evidence rather than an apply's rc; push state read by `ls-remote` + `is-ancestor` and stated as MEASURED.

<expected_criteria>S9C-AC1, S9C-AC2, S9C-AC3, S9C-AC4, S9C-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc>, cell `OP-s-9` (manifest row S9; FWD-9), round 2c. **This face adds NO new cell and NO new manifest row** -- it is a second task order on an existing cell whose live population turned out wider than the cell text assumed, following the `TO-OP-S-8R2B` and `TO-OP-S-10B` precedent.
<owned_cells>OP-s-9</owned_cells>
Read-dependencies, NOT claimed: `TO-OP-S-9-11` (the portal-auth root's two ARNs -- this face does not touch them), row `Z-S112` (the enumeration this face acts on).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED **20** over 5 carriers AT THAT VINTAGE (C1 SENTINEL 20 lines -> **4** gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). ⛔ **CORRECTED 2026-09-04 08:4xZ BY `1.0.0_SA_CTO~Z` (msg 20364): the tool prints 21 lines -> 5 gates because it counts a LOG QUOTING a sentinel as a gate -- `org/tier1_exec/3.0.0_SA_CVO/logs/2026-09-01/work_0312Z_comp_schedule_gate_ledger_build.md:72`. **A `.md` CANNOT gate a deploy**: `safe_deploy_core` matches that grammar against the files it is about to SHIP. The other 20 lines are authoritative deployable source. ⛔⛔ **DO NOT "CONFIRM" THIS BY RE-RUNNING `comp-schedule` -- A FRESH RUN TONIGHT ALSO PRINTS 21, BY A DIFFERENT ROUTE:** C2 DEPLOY-LEDGER has moved 4 -> 5 since this preflight, so corrected C1 4 + current C2 5 + C3 12 = 21 again. **The same total from different components would read as confirmation and would be nothing of the kind.** ⭐ The correction is trusted because it imports `comp-schedule`'s OWN `SERVE_HELD_RE` and `_full_reason` over the tool's own scope and REPRODUCES 21/5 as a control BEFORE removing the quotation -- a census that could not first reproduce the figure it corrects would not be evidence. **This figure is ORIENTATION at its stated vintage, never a criterion, and no face in this project discharges a gate.**
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
