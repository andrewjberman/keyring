# TO NFRA_OPSEC202609.TO-OP3-S-3 -- FWD-14/15: TERRAFORM DECLARES `addresses = []` ON ALL FOUR BLOCKED-IP SETS, so every runtime block is silently reverted at the next apply. Make the declared state stop fighting the control (OP3-s-3)

<to_id>NFRA_OPSEC202609.TO-OP3-S-3</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.9.0_WK_NFRA_OPSEC202609~3</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged</status>

**Directive:** D12 · **Fabric:** site-z · **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.14** (FWD-14, FWD-15) · **Decomp cell:** `OP3-s-3` (round-3 rectangle v0.3.0) · **Round:** 3.

---

## THE CELL

Row **`NFRA_OPSEC202609-Z-S136`** (GRADUATED at L9, hazard ARMED): *"TERRAFORM IS A SECOND WRITER OF THE BLOCKED-IP SETS AND C-2 CANNOT SEE IT. All FOUR sets declare `addresses = []`."*

The auto-block framework's entire purpose is to put an address into a set **and keep it there**. The declared state says every set is empty. **So the next apply silently reverts every runtime block**, and nothing announces it.

⛔ **THIS IS WORSE THAN AN ABSENT CONTROL, WHICH IS WHY IT IS IN ROUND 3 AND NOT LATER.** An absent control is visibly absent. A control that reverts itself on a schedule nobody watches is **recorded as present** -- the register says the estate is protected, and it is not. `FWD-14`'s false positive is a LOCKED-OUT FIRM; its false negative here is an UNBLOCKED attacker with a green register row.

## WHAT THIS CELL DOES **NOT** DECIDE

⛔ **IT DOES NOT DECIDE WHICH ADDRESSES DESERVE BLOCKING.** That is the framework's runtime job and it is out of scope here. This cell moves **only** the persistence of a block once made -- the decomposition's postulate (iv) says so explicitly. If you find yourself choosing addresses, stop and file a row.

⛔ **IT DOES NOT BLOCK ANYTHING.** Do not add an address to any set as part of the remedy. `TO-OP-S-13`'s derivation already showed why on this estate: 0 of 5 candidate addresses could be tied to a NAMED PERSON, they looked residential and dynamic, and applying them would have approved a lockout the first time a home connection rotated.

## THE SHAPE OF THE REMEDY IS YOURS TO ESTABLISH, WITH ONE BOUND

The standard forms are `lifecycle { ignore_changes = [addresses] }`, or moving the set's membership out of the declared state entirely. **Which one is right depends on how the framework writes, and you must read that before choosing.** ⛔ **The bound: whichever you choose, a runtime-added address must SURVIVE a subsequent plan/apply, and you must DEMONSTRATE that rather than reason about it.**

## DELIVERABLE

1. **The four sets enumerated** with their declared state read at source, and their live membership read on the applied plane -- the two states side by side, before any edit.
2. **The remedy**, applied through `safe-apply` (never bare `terraform apply`), with a deploy-ledger entry opened before and closed after, rollback named.
3. **A demonstration** that a runtime-added address survives a plan/apply cycle.
4. **The proof-of-spec instance**, VALID before the `complete` flip.

## ACCEPTANCE -- criterion ids minted at cut, ONE CLAUSE EACH

<criterion id="S3-AC1" cell_refs="OP3-s-3"><invocation>the declared-state read over the Terraform source for the blocked-IP sets, listing each set by name.</invocation><expect>exactly FOUR sets are listed, matching `Z-S136`'s count, each showing its declared `addresses` value.</expect></criterion> `S3-AC1` -- ALL FOUR SETS ARE ENUMERATED WITH A PRINTED DENOMINATOR.

<criterion id="S3-AC2" cell_refs="OP3-s-3"><invocation>`aws wafv2 get-ip-set` for each of the four, outputs pasted.</invocation><expect>each set's live `Addresses` array is recorded, whether empty or not, as the before-state.</expect></criterion> `S3-AC2` -- THE LIVE MEMBERSHIP IS READ ON THE APPLIED PLANE BEFORE ANY EDIT.

<criterion id="S3-AC3" cell_refs="OP3-s-3"><invocation>the declared values from `S3-AC1` set beside the live values from `S3-AC2`.</invocation><expect>for each of the four, either a stated divergence or a stated agreement -- **an agreement is a legitimate result and is NOT a reason to skip the remedy**, because the hazard is what the NEXT apply would do.</expect></criterion> `S3-AC3` -- THE DIVERGENCE IS STATED AS A MEASURED COMPARISON.

<criterion id="S3-AC4" cell_refs="OP3-s-3"><invocation>add a test address to one set at runtime, then run the plan.</invocation><expect>the plan does NOT propose removing that address.</expect></criterion> `S3-AC4` -- A RUNTIME-ADDED ADDRESS SURVIVES A PLAN.

<criterion id="S3-AC5" cell_refs="OP3-s-3"><invocation>`aws wafv2 get-ip-set` for that set after cleanup.</invocation><expect>the test address is absent, and the set's membership matches its `S3-AC2` before-state.</expect></criterion> `S3-AC5` -- THE TEST ADDRESS IS REMOVED AFTERWARDS.

<criterion id="S3-AC6" cell_refs="OP3-s-3"><invocation>the `safe-apply` changed-resource list, then an unscoped re-plan.</invocation><expect>the changed list contains only the IP-set resources this order names; the re-plan reads 0 to add / 0 to destroy / no forces-replacement.</expect></criterion> `S3-AC6` -- THE APPLY MOVED ONLY WHAT WAS INTENDED.

<criterion id="S3-AC7" cell_refs="OP3-s-3"><invocation>the deploy-ledger entry under `org/critical_paths/change_management/`, read after closure.</invocation><expect>the entry is CLOSED, names its rollback, and its push state is stated as a MEASURED value.</expect></criterion> `S3-AC7` -- THE LEDGER CLOSES ON THE ARTIFACT.

<expected_criteria>S3-AC1, S3-AC2, S3-AC3, S3-AC4, S3-AC5, S3-AC6, S3-AC7</expected_criteria>

<paths>
org/missions/D12/NFRA/NFRA_OPSEC202609/task-orders/NFRA_OPSEC202609.TO-OP3-S-3.blocked-ip-sets-second-writer.md
org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~3/
org/missions/D12/NFRA/NFRA_OPSEC202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_OPSEC202609/prd/NFRA_OPSEC202609_PRD.md
org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP_round3.md
infra/aws/terraform/opsec/
org/critical_paths/change_management/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP_round3.md</decomp_doc> (v0.3.0), cell `OP3-s-3`.
<owned_cells>OP3-s-3</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN -- the DEPLOY-LEDGER carrier BINDS -- this is a ledgered `safe-apply` on live WAF resources. G-15 does not bind: no alarm, monitor or notification is built.
comp-iam: DECLARED-NOT-APPLICABLE at the cut -- no IAM identity policy is authored. If the chosen remedy turns out to need a policy change, that is a difference from this face and a row.
comp-adversary: RUN -- `Z-S136`'s "all FOUR declare `addresses = []`" is the row's measurement, not this seat's; `S3-AC1` and `S3-AC2` re-take it independently and a difference is a STOP.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S3-AC1` .. `S3-AC7`. The worker fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~3/NFRA_OPSEC202609.TO-OP3-S-3.blocked-ip-sets-second-writer.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S3-AC1,S3-AC2,S3-AC3,S3-AC4,S3-AC5,S3-AC6,S3-AC7"` BEFORE the `complete` flip. ⭐ **THE CONTROL THAT MUST BE ABLE TO FAIL IS `S3-AC4`** -- it is the only criterion that tests the actual hazard, and a remedy that applies cleanly while still proposing the removal is exactly the failure this cell exists to prevent. Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before any write">Confirm the worktree: `test -d org && test -d .tools`. Enumerate the four sets at source and live. STOP on any difference from `Z-S136`.</phase>
  <phase id="2" when="before the apply">Unscoped baseline plan, ledger opened, rollback captured verbatim. NEVER bare `terraform apply` -- `safe-apply` only.</phase>
  <phase id="3" when="after the apply">The survival demonstration, the cleanup, the unscoped re-plan, the ledger closed on that evidence.</phase>
</compiler_tools_mandate>

⛔ **RUN EVERY COMP-TOOL BY ITS EXPLICIT `.tools/` PATH, NEVER THE BARE NAME** (LIMIT 4 / 4a: the bare name is a shim pinned to the MAIN checkout and censuses the wrong tree from a worktree).
