# TO NFRA_OPSEC202609.TO-OP-S-9D -- THE RETIREMENT ANDREW AUTHORISED: delete `opal-users` THROUGH TERRAFORM by removing its declaration, never by console or CLI -- because a destroy Terraform performs leaves consistent state, while a delete it did not perform leaves a resource in state that the next plan proposes to RE-CREATE as an empty table wearing the retired one's name (OP-s-9, round 2d)

<to_id>NFRA_OPSEC202609.TO-OP-S-9D</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~X</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete</status>

✅ **SOVEREIGN AUTHORISATION, THE ONLY THING THIS CELL WAS WAITING ON. Andrew, 2026-09-04 ~03:4xZ, verbatim: "Recs approved"** -- against the card *"Delete the legacy `opal-users` table, or keep it standing?"* whose REC was *"Delete -- but only after removing it from Terraform management first, or the next plan proposes to re-create it as an empty table wearing the retired one's name."* **`S9-AC4`'s bar was that the retirement be parked with a human. It was, and the human has ruled.**

⛔ **GO CONDITION: `TO-OP-S-9C` TERMINAL.** Do not interleave a grant removal and a table deletion; if the grant work needs rolling back, a deleted table makes that harder to reason about.

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (FWD-9) - **Decomp cell:** `OP-s-9` (manifest row S9), round 2d - **Lane:** `infra/aws/terraform/portal-auth/`, AE lane - **Round:** 3.

---

## ⛔ THE METHOD IS THE RULING, AND IT IS NOT WHAT THE CARD'S REC LITERALLY SAID

I recommended *"remove it from Terraform management first."* **The intent was to prevent an orphan the next plan re-creates. Destroying it THROUGH Terraform serves that intent strictly better**, so that is what this face does:

**DELETE THE RESOURCE DECLARATION AND LET `safe-apply` PERFORM THE DESTROY.** State stays consistent, the act is in the plan and in the ledger, and **nothing is left behind to be re-created.**

⛔ **DO NOT `terraform state rm` AND THEN DELETE BY HAND.** That is the shape that produces an untracked live table if the second half fails, and it puts the destructive act outside the plan where no gate and no reviewer can see it. ⛔ **DO NOT delete via console or `aws dynamodb delete-table`.**

## ⛔ TWO GUARDS WILL REFUSE THIS, AND BOTH ARE CORRECT TO

The table is protected. **Expect and handle, as SEPARATE applies with the destroy LAST:**
- **`deletion_protection_enabled`** on the table -- must be set false in a **prior** apply.
- **`lifecycle { prevent_destroy = true }`**, if declared -- must be removed in the declaration.

⛔ **REMOVING A PROTECTION AND PERFORMING THE DESTROY IN ONE APPLY IS FORBIDDEN HERE.** Two applies, each with its own plan read, so **the destroy plan is read by a human-legible artifact showing exactly one resource destroyed and nothing else.**

## DELIVERABLE

1. **RE-VERIFY THE SNAPSHOT IMMEDIATELY BEFORE THE DESTROY** -- not the one read an hour ago. `opal-users-retire-snapshot-20260904T004712Z`: **AVAILABLE, item count AND byte size still matching the live table, expiry still null.** ⛔ **If the snapshot is not verifiable at that moment, STOP.** The whole reversibility argument rests on it.
2. **RE-VERIFY THE TABLE IS UNCHANGED: 12 items, and nothing written since the grant removal.** ⛔ **A row count that has MOVED means something still writes to it, which contradicts every census and is an immediate STOP and a ROW.**
3. **Disable `deletion_protection_enabled`** in its own apply, plan read and quoted.
4. **Remove the declaration and apply the destroy**, plan read and quoted showing **exactly one resource destroyed**.
5. **Deploy-ledger entry** opened before act 3 and closed after act 4, **with the rollback named before the first act** -- restore-from-backup into a new table, and **state plainly that a restore produces a NEW table name and is not a byte-for-byte undo.** An honest rollback beats an optimistic one.
6. **The residual re-read after**: `TO-OP-S-9-11`'s named residual and `TO-OP-S-9C`'s outcome restated against a world where the table no longer exists.
7. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~X/NFRA_OPSEC202609.TO-OP-S-9D.opal-users-retirement.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S9D-AC1" cell_refs="OP-s-9"/> `S9D-AC1` -- THE SNAPSHOT AND THE TABLE WERE BOTH RE-READ IMMEDIATELY BEFORE THE DESTRUCTIVE ACT, not inherited from an earlier report: the backup's status, item count, size and expiry pasted with their read timestamp; the table's item count pasted with its own. **Denominator: 12 of 12 expected.** ⛔ **A moved row count FAILS this criterion and stops the face.**
<criterion id="S9D-AC2" cell_refs="OP-s-9"/> `S9D-AC2` -- THE PROTECTIONS CAME OFF IN THEIR OWN APPLY, BEFORE AND SEPARATE FROM THE DESTROY: the plan for the protection change quoted, its changed-resource list enumerated, and the applied-plane re-read confirming protection is off. **A single apply that both unprotects and destroys FAILS this criterion regardless of outcome** -- the point is that a human-legible destroy plan exists.
<criterion id="S9D-AC3" cell_refs="OP-s-9"/> `S9D-AC3` -- THE DESTROY WAS PERFORMED BY TERRAFORM AND THE PLAN SHOWED EXACTLY ONE RESOURCE: the destroy plan quoted with its resource count, the apply output, and the post-apply `describe-table` returning `ResourceNotFoundException`. ⛔ **Evidence of `terraform state rm`, `aws dynamodb delete-table`, or a console deletion FAILS this criterion** even if the table is gone -- the method IS the criterion.
<criterion id="S9D-AC4" cell_refs="OP-s-9"/> `S9D-AC4` -- NOTHING ELSE RODE AND NOTHING IS ORPHANED: the UNSCOPED plan after the destroy showing **no proposal to re-create the table** and no unrelated changes. ⛔ **If the root's known non-converging diff makes a clean re-plan unobtainable, file `UNVERIFIABLE-BY-INSTRUMENT` and substitute** -- the plan structure showing the table absent from any create block, plus the applied-plane read. **The purpose is nothing-else-rode; the 0-diff is only its measure.**
<criterion id="S9D-AC5" cell_refs="OP-s-9"/> `S9D-AC5` -- LOGIN IS UNAFFECTED, WITH ITS BEFORE-HALF: a fixture login and `/auth/me` **before and after the destroy**, both pasted, the payloads compared. **The before is what makes the after mean anything.** Plus ledger CLOSED on exercised evidence with the rollback's real shape stated, and push state MEASURED.

<expected_criteria>S9D-AC1, S9D-AC2, S9D-AC3, S9D-AC4, S9D-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc>, cell `OP-s-9` (manifest row S9; FWD-9), round 2d. **Adds NO new cell and NO new manifest row** -- it is the act `OP-s-9`'s own `closes on` reserved for a human word, now given. **This face CLOSES `OP-s-9` and serves `FWD-9`.**
<owned_cells>OP-s-9</owned_cells>
Read-dependencies, NOT claimed: `TO-OP-S-9-11` (COMPLETE -- the grants and the snapshot), `TO-OP-S-9C` (the trade residual; GO condition).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED **20** over 5 carriers AT THAT VINTAGE (C1 SENTINEL 20 lines -> **4** gates; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). **This face builds no monitor, alarm or notification.** ⛔ **CORRECTED 2026-09-04 08:4xZ BY `1.0.0_SA_CTO~Z` (msg 20364): the tool prints 21 lines -> 5 gates because it counts a LOG QUOTING a sentinel as a gate -- `org/tier1_exec/3.0.0_SA_CVO/logs/2026-09-01/work_0312Z_comp_schedule_gate_ledger_build.md:72`. **A `.md` CANNOT gate a deploy**: `safe_deploy_core` matches that grammar against the files it is about to SHIP. The other 20 lines are authoritative deployable source. ⛔⛔ **DO NOT "CONFIRM" THIS BY RE-RUNNING `comp-schedule` -- A FRESH RUN TONIGHT ALSO PRINTS 21, BY A DIFFERENT ROUTE:** C2 DEPLOY-LEDGER has moved 4 -> 5 since this preflight, so corrected C1 4 + current C2 5 + C3 12 = 21 again. **The same total from different components would read as confirmation and would be nothing of the kind.** ⭐ The correction is trusted because it imports `comp-schedule`'s OWN `SERVE_HELD_RE` and `_full_reason` over the tool's own scope and REPRODUCES 21/5 as a control BEFORE removing the quotation -- a census that could not first reproduce the figure it corrects would not be evidence. **This figure is ORIENTATION at its stated vintage, never a criterion, and no face in this project discharges a gate.**
comp-iam: DECLARED-NOT-APPLICABLE -- the grants on this table were already removed and verified by `TO-OP-S-9-11` on the applied plane (7 -> 5 resources, zero exact grants remaining). This face changes no principal.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim at cut; its evidence is live reads at the assignee's own vintage.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S9D-AC1`, `S9D-AC2`, `S9D-AC3`, `S9D-AC4`, `S9D-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~X/NFRA_OPSEC202609.TO-OP-S-9D.opal-users-retirement.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S9D-AC1,S9D-AC2,S9D-AC3,S9D-AC4,S9D-AC5"` BEFORE the complete flip. **THE CONTROL THAT MUST BE ABLE TO FAIL IS `S9D-AC1`'s row count: if it has moved, something still writes to a table four independent censuses said nothing reads, and that discovery is worth more than the retirement.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before any act">Snapshot and table re-read at THIS vintage. An hour-old reading is not a pre-destroy check.</phase>
  <phase id="2" when="between applies">The destroy plan read as its own artifact, showing one resource. If it shows more, STOP.</phase>
  <phase id="3" when="after">describe-table returning ResourceNotFoundException, the unscoped re-plan proposing no re-creation, login verified against its before, ledger closed on that evidence rather than on an apply's rc.</phase>
</compiler_tools_mandate>
