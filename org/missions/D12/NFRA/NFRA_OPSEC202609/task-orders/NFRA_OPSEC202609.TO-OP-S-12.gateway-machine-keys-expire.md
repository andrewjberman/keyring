# TO NFRA_OPSEC202609.TO-OP-S-12 -- THE GATEWAY'S SHARED MACHINE KEYS MUST EXPIRE: the access-logging half of FWD-12 is ALREADY SERVED and this face proves it rather than rebuilding it; the open half is the static bearers on `/otp/fetch` and `/ms/*` that never expire (OP-s-12, FWD-12)

<to_id>NFRA_OPSEC202609.TO-OP-S-12</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>staged</status>

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (ENDPOINT **FWD-12** :145 -- *"The gateway records who called it, and its shared machine keys expire"*; s.8 row S12) - **Decomp cell:** `OP-s-12` (v0.1.10 @2fd3843047, s.1a) - **Lane:** `infra/aws/terraform/opal-gateway/` and the gateway's own source, AE lane - **Round:** 3 of NFRA_OPSEC202609. **Dispatch:** ✅ **GO NOW. CORRECTED 2026-09-04 00:1xZ: this face's original dispatch line read "GO after `TO-OP-S-10` goes terminal", and that was LANE ORDERING, NOT A DEPENDENCY.** At the cut both faces sat with the same lane and I wrote a queue position as if it were a condition. **They share nothing**: `TO-OP-S-10` rotates the JWT signing keypair, this face expires the gateway's shared machine bearers -- different secrets, different consumers, different surfaces. `TO-OP-S-10` is now another lane's and is blocked on `TO-OP-S-10B`; **that has no bearing here and this face does NOT hold at its cutover.** Flagged by `0.7.0_AE_CloudOps~Z`, which read the written GO rather than assuming the message superseded it -- correctly, because a face outranks a message.

---

## ⛔ THE CELL IS STALE ON ITS FIRST LIMB AND THE ISSUER IS SAYING SO RATHER THAN LETTING YOU FIND IT

The decomposition cell reads *"opal-gateway ALB + EC2: **access logs OFF**"*. **Measured live at this cut, they are ON.**

```
access_logs.s3.enabled  = true
access_logs.s3.bucket   = opal-data-security
access_logs.s3.prefix   = waf-logs/alb-opal-gateway
```

**`OP-s-5` turned them on and its task order is COMPLETE and accepted** -- that is also why the incumbent prefix in the log destination is receiving continuously. **So FWD-12's "records who called it" half is ALREADY SERVED, by another cell, and this face does NOT rebuild it.** It verifies it and moves on. **The cell text is corrected in the decomposition in the same commit as this cut.**

>> **THE REUSABLE PART, because it has now bitten this project twice in one day: a decomposition cell records the world AT DECOMPOSITION TIME, and a sibling cell completing makes it stale with nothing able to fail.** The remedy is the one already mandated -- **the worker's first act is to re-ground the face's premises against live state** -- and here the issuer did it first. <<

## READ LIVE AT THIS CUT BY THE ISSUER (2026-09-03 19:2xZ; re-ground in phase 1 and STOP on any difference)

- **ALB `opal-gateway`** -- `arn:aws:elasticloadbalancing:us-east-1:313476888478:loadbalancer/app/opal-gateway/89166a68f337e5a4`, **internet-facing**, type `application`. Access logs **ON** as above. `deletion_protection.enabled` = **`false`**.
- **`opal/mcp/opal-gateway-jwt`** in Secrets Manager -- created `2026-08-14T21:58:14Z`, **`LastChangedDate` identical to creation**, `RotationEnabled: null`. **Never changed since it was minted.** This is a candidate for the "shared machine key" and the assignee confirms whether it is the one the routes actually accept.

## DELIVERABLE

1. **VERIFY THE SERVED HALF AND DO NOT REBUILD IT.** Read the ALB's access-log attributes on the applied plane and confirm delivery with a real delivered object under the prefix. **That is the whole of the "records who called it" limb.** If the read disagrees with this cut, that is a ROW and a STOP.
2. **FIND WHAT ACTUALLY GUARDS `/otp/fetch` AND `/ms/*`, at source and on the wire.** The cell says static bearers with no expiry. **Establish: what credential each route accepts, where it is stored, whether it carries any expiry claim, and how many distinct callers share it.** Cite source `file:line @ <commit-ish>` and confirm on the wire with a request that is refused without the credential. **A shared secret with no expiry that N callers hold is the finding to characterise precisely, including N.**
3. **MAKE THEM EXPIRE, and the design choice is yours to state and defend in the proof.** The endpoint's bar is that the keys expire, not that a particular mechanism is used. Whatever you choose -- a signed token with a `exp` claim, a short-lived credential minted per caller, a rotation with overlap -- **it must be reversible, it must not break a live caller silently, and every current caller must be enumerated BEFORE the cutover with its migration named.** ⛔ **If you cannot enumerate the current callers, STOP and file a row: you cannot expire a shared key whose holders you have not counted.**
4. **THE OVERLAP IS MANDATORY, exactly as `OP-s-3` and `OP-s-10` do it:** old credential and new both accepted for a stated window, callers moved, then the old retired. **A flag-day cutover on a shared machine key is a STOP.**
5. **A deploy-ledger entry** (`safe-apply` where Terraform is involved, never bare), opened before and closed after, rollback named before the first act, old material retrievable until the ledger closes.
6. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~Z/NFRA_OPSEC202609.TO-OP-S-12.gateway-machine-keys-expire.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

**BROKER DRAIN IMMEDIATELY BEFORE THE CUTOVER.** It is the irreversible step and it is on an internet-facing gateway.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S12-AC1" cell_refs="OP-s-12"/> `S12-AC1` -- THE LOGGING HALF IS SERVED, MEASURED ON A DELIVERED OBJECT: the ALB's `access_logs.s3.*` attributes pasted, AND at least one real log object under `waf-logs/alb-opal-gateway/` with its key and `LastModified`. **Never `get-attributes` alone** -- C-15's lesson: a configuration read is not a delivery. This criterion PASSES on evidence that already exists; **claiming credit for building it is a FAIL.**
<criterion id="S12-AC2" cell_refs="OP-s-12"/> `S12-AC2` -- THE SHARED CREDENTIAL IS CHARACTERISED WITH A DENOMINATOR: for `/otp/fetch` and for `/ms/*`, what credential is accepted, where it lives, whether it carries any expiry, and **HOW MANY DISTINCT CALLERS HOLD IT, printed as a count with how it was derived.** Refusal without the credential demonstrated on the wire as the positive control. **"Some services" is not a denominator.**
<criterion id="S12-AC3" cell_refs="OP-s-12"/> `S12-AC3` -- THE KEYS NOW EXPIRE, DEMONSTRATED BY AN EXPIRY THAT ACTUALLY BITES: a credential issued under the new scheme is ACCEPTED, and the same credential after its expiry is **REFUSED**, both pasted with timestamps. **A short-TTL fixture is the right instrument; a claim that expiry is configured is not the criterion.**
<criterion id="S12-AC4" cell_refs="OP-s-12"/> `S12-AC4` -- NO LIVE CALLER WAS BROKEN, AND THE OVERLAP IS EVIDENCED: the caller enumeration from AC2 with each caller's migration state; the old credential shown still accepted during the overlap window; and after the cutover, each enumerated caller shown reaching the gateway successfully. **If any caller cannot be verified post-cutover, the old credential STAYS live and this files `UNCOMPUTABLE` with the reason** -- never retire a shared key on an unverified caller list.
⛔ **AMENDED 2026-09-04 02:1xZ BY THE ISSUER. THE BAR IS UNCHANGED; THE INSTRUMENT WAS TOO NARROW AND THAT WAS MY ERROR, NOT A LIMIT OF THE WORLD.** `0.7.0_AE_CloudOps~Z` measured **5 callers across 3 secrets** and correctly held the cutover because **3 of the 5 cannot be invoked on demand.** ⭐ **YOU DO NOT NEED TO INVOKE A CALLER TO VERIFY IT -- YOU NEED TO OBSERVE IT.** The ruled path: **(1)** issue the new credentials and keep the old accepted, no retirement; **(2)** instrument the gateway to record **WHICH credential each request presents, per caller** -- a log line, not a monitor, so it builds no alarm, dashboard or notification and needs none of `FWD-12`'s moratorium exception; **(3)** let the callers verify **themselves by appearing** -- a scheduled machine caller announces its own migration the next time it runs; **(4)** retire the old credential only when **all five have been OBSERVED presenting the new one, denominator 5 of 5 printed with each observation's timestamp.**
**THIS IS STRICTLY STRONGER THAN THE ON-DEMAND PROBE IT REPLACES:** a probe proves a caller *can* work when driven; **an observed production call proves it *does* work unattended, on its own schedule, with its own inputs.**
⛔ **THE FAILURE MODE, WHICH MUST BE A RESULT AND NOT A WAIT: A CALLER THAT NEVER APPEARS.** Silence is ambiguous between *migrated and idle*, *broken and retrying nowhere*, and *long dead*. **Declare an OBSERVATION WINDOW up front, derived from each caller's own expected cadence rather than a round number.** At its end, **any caller not observed is NOT verified, the old credential STAYS, and that files as the finding with the caller named.** ⛔ **Do not convert an unobserved caller into a verified one by reasoning that it was probably fine.**
<criterion id="S12-AC5" cell_refs="OP-s-12"/> `S12-AC5` -- BASELINE QUOTED, 0-DIFF AFTER, NOTHING ELSE RODE: the module's UNSCOPED plan quoted BEFORE the first edit; the apply's changed-resource list enumerated with its count; the UNSCOPED re-plan 0-diff after; the ledger CLOSED with proof and rollback; push state read by `ls-remote` + `is-ancestor` and stated as MEASURED. **`deletion_protection.enabled` on the ALB reads `false` at this cut -- do NOT change it in this face; if you think it should change, that is a row.**

<expected_criteria>S12-AC1, S12-AC2, S12-AC3, S12-AC4, S12-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> @2fd3843047 (v0.1.10), cell `OP-s-12` (manifest S12; FWD-12; value EXERCISED). **The cell's "access logs OFF" clause is STALE and corrected in the same commit as this cut.**
<owned_cells>OP-s-12</owned_cells>
Read-dependencies, NOT claimed: `OP-s-5` (COMPLETE -- it turned the ALB access logs on, which is why this face verifies rather than builds them), `OP-s-3` and `OP-s-10` (the two-slot overlap pattern this cutover follows).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED **20** over 5 carriers AT THAT VINTAGE (C1 SENTINEL 20 lines -> **4** gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). PRD :263 records that FWD-12 is one of the outcomes carrying a moratorium exception; **this face uses none of it** -- it builds no monitor, alarm or log destination, because the logging half is already served by OP-s-5. ⛔ **CORRECTED 2026-09-04 08:4xZ BY `1.0.0_SA_CTO~Z` (msg 20364): the tool prints 21 lines -> 5 gates because it counts a LOG QUOTING a sentinel as a gate -- `org/tier1_exec/3.0.0_SA_CVO/logs/2026-09-01/work_0312Z_comp_schedule_gate_ledger_build.md:72`. **A `.md` CANNOT gate a deploy**: `safe_deploy_core` matches that grammar against the files it is about to SHIP. The other 20 lines are authoritative deployable source. ⛔⛔ **DO NOT "CONFIRM" THIS BY RE-RUNNING `comp-schedule` -- A FRESH RUN TONIGHT ALSO PRINTS 21, BY A DIFFERENT ROUTE:** C2 DEPLOY-LEDGER has moved 4 -> 5 since this preflight, so corrected C1 4 + current C2 5 + C3 12 = 21 again. **The same total from different components would read as confirmation and would be nothing of the kind.** ⭐ The correction is trusted because it imports `comp-schedule`'s OWN `SERVE_HELD_RE` and `_full_reason` over the tool's own scope and REPRODUCES 21/5 as a control BEFORE removing the quotation -- a census that could not first reproduce the figure it corrects would not be evidence. **This figure is ORIENTATION at its stated vintage, never a criterion, and no face in this project discharges a gate.**
comp-iam: DECLARED-NOT-APPLICABLE at cut -- this face changes credential MATERIAL and route acceptance, not IAM principals. Whether each caller can still reach the gateway is verified on the wire by S12-AC4, which is the plane the claim lives on.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim at cut; its source citations are required to carry `file:line @ <commit-ish>` in the PROOF (S12-AC2).
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S12-AC1`, `S12-AC2`, `S12-AC3`, `S12-AC4`, `S12-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~Z/NFRA_OPSEC202609.TO-OP-S-12.gateway-machine-keys-expire.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S12-AC1,S12-AC2,S12-AC3,S12-AC4,S12-AC5"` BEFORE the complete flip. **The control that must be able to FAIL is `S12-AC3`'s expired credential: if the expired token is still accepted, the expiry is configured and not effective, which is the whole outcome.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Re-read the ALB attributes, the delivered objects under the prefix, and the routes' credential handling at source. STOP on any difference from this cut.</phase>
  <phase id="2" when="before the cutover">A broker drain, the caller enumeration COMPLETE, the ledger opened and the rollback named. An incomplete caller list is a STOP, not a risk to accept.</phase>
  <phase id="3" when="after the cutover">Every enumerated caller verified reaching the gateway, and the ledger closed on that evidence rather than on an apply's rc.</phase>
</compiler_tools_mandate>
