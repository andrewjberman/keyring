# TO NFRA_OPSEC202609.TO-OP-S-17B -- OBJECT LOCK (GOVERNANCE) ON `cases/`, AND THE CONTROL IS FORWARD-ONLY: the 438 case files already in the store do NOT gain retention and are NOT re-written to acquire it, because rewriting an evidence object changes its write timestamp (OP-s-17, round 2; OP-x-4 CLOSED on Andrew's word)

<to_id>NFRA_OPSEC202609.TO-OP-S-17B</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~X</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-04</issued_date>
<status>staged</status>

✅ **BLOCKER: NONE. GO.** ⭐ **The two questions that would normally gate this are BOTH already answered, and neither by assertion.**

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` (C-8) - **Decomp cell:** `OP-s-17` (manifest S17; FWD-16, FWD-18), **round 2** - **Lane:** `infra/aws/terraform/` evidence-store root, AE lane.

---

## THE AUTHORISATION, AND THE CELL ALREADY ROUTED THIS BY NAME

**`OP-s-17`'s own constraint column reads: *"Object Lock on `cases/` is `OP-x-4` (a card), not this cell."*** ⭐ **The decomposition routed this correctly a day before the ruling existed** -- the work was never inside `OP-s-17`'s round 1, it was parked in a decide-first cell awaiting a word.

**`OP-x-4` is now CLOSED: Andrew-direct 2026-09-04 ~13:00Z, *"Approved for all of these"*, card 5 -- Object Lock (governance) on `cases/` in `opal-security-evidence`: ON.** C-8 carried it as an OPTION with versioning-without-lock as the default; **the option is taken.**

## ⛔ TWO THINGS ARE ALREADY MEASURED. DO NOT RE-ESTABLISH THEM; DO NOT ASSUME THEM EITHER.

**1 -- IT IS EXECUTABLE IN PLACE.** `1.0.0_SA_CTO~Z` tested it on a **THROWAWAY** bucket -- created, versioning ON, **written to so it was NON-EMPTY like the real one** -- then enabled: `put-object-lock-configuration` **rc=0**, and `get-object-lock-configuration` read back `ObjectLockEnabled` + `GOVERNANCE`. **Probe bucket fully deleted; `head-bucket` 404; no litter.** ⭐ **So there is NO new bucket and NO 438-object migration.** The question was answered **where being wrong cost nothing**, which is why it did not have to be answered here.

**2 -- IT IS FORWARD-ONLY, AND THIS IS THE FINDING THE CARD DID NOT CONTAIN.** The same probe wrote one object BEFORE the enable and one AFTER:
```
cases/probe.txt        written BEFORE  -> get-object-retention: NoSuchObjectLockConfiguration
cases/probe_after.txt  written AFTER   -> Retention: GOVERNANCE, RetainUntilDate ...
```
⛔ **Default retention attaches at PUT time. Enabling the lock does NOT retroactively protect what is already there.**

## ⛔ THE 438 ARE NOT RE-WRITTEN. THIS IS A RULING, NOT A PREFERENCE.

**`cases/` holds 438 objects, measured 2026-09-04 13:1xZ.** ⭐ **Re-PUTting an evidence object to give it a retention flag CHANGES ITS WRITE TIMESTAMP -- and a store whose records were all re-stamped on a single day to satisfy a control is WORSE evidence than one that is honestly unprotected. The whole value of a case file is when it was written.** ⛔ **A copy-in-place is the same defect wearing a different verb. Do not do either.**

**The coverage boundary is STATED WITH ITS DATE rather than implied.**

## DELIVERABLE

1. **Enable Object Lock, GOVERNANCE mode, on `opal-security-evidence`**, via Terraform (`safe-apply`, never bare), with the deploy-ledger entry opened before and the rollback named first.
2. ⛔ **Re-read the preconditions AT YOUR OWN VINTAGE before acting** -- versioning still `Enabled`, and the object count under `cases/` re-measured. **The 438 is this issuer's reading and the sentinel writes to that prefix continuously; it WILL have moved.** State your number.
3. **A DEFAULT RETENTION PERIOD, chosen and defended.** The endpoint does not name one. **State the period and why**, and state what a governance-mode lock does NOT prevent -- **a principal with `s3:BypassGovernanceRetention` can still delete.** ⛔ **Name who holds it. A control whose bypass nobody enumerated is a control nobody has sized.**
4. **The coverage boundary written into the evidence store's own documentation**, with the enable timestamp: **objects written after it carry retention; those before do not.**
5. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~X/NFRA_OPSEC202609.TO-OP-S-17B.object-lock-on-cases.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S17B-AC1" cell_refs="OP-s-17"/> `S17B-AC1` -- THE LOCK IS ON AND READ BACK ON THE APPLIED PLANE: `get-object-lock-configuration` pasted showing `ObjectLockEnabled` and `GOVERNANCE`, plus the default retention period. **A Terraform plan or apply output alone does NOT satisfy this** -- read the live configuration.
<criterion id="S17B-AC2" cell_refs="OP-s-17"/> `S17B-AC2` -- ⛔ **THE FORWARD-ONLY BOUNDARY IS DEMONSTRATED, NOT ASSERTED, AND THIS IS THE CRITERION THAT MATTERS: `get-object-retention` on a PRE-EXISTING case object showing NO retention, AND on a NEWLY-WRITTEN one showing `GOVERNANCE`.** ⭐ **A criterion that only checked the bucket's configuration would PASS while every existing case file is uncovered.** Both reads pasted, both keys named, with the enable timestamp between them.
<criterion id="S17B-AC3" cell_refs="OP-s-17"/> `S17B-AC3` -- NOTHING WAS RE-WRITTEN: a census showing the pre-existing objects' `LastModified` UNCHANGED across the act, with the denominator printed. ⛔ **Evidence of any `copy-object`, re-`put-object` or bulk re-write of `cases/` FAILS this criterion even if the retention outcome looks better.** **The method IS the criterion.**
<criterion id="S17B-AC4" cell_refs="OP-s-17"/> `S17B-AC4` -- THE BYPASS IS ENUMERATED: every principal holding `s3:BypassGovernanceRetention` on this bucket, printed with its denominator and its instrument, on the APPLIED plane. ⭐ **Governance mode is a control with a documented override; a reader told "Object Lock ON" and not told who can bypass it has been given a stronger impression than the control supports.** ⛔ **Simulate rather than filter policy documents** -- an inherited wildcard matches no text (this project's own `S15-AC3` lesson).
<criterion id="S17B-AC5" cell_refs="OP-s-17"/> `S17B-AC5` -- BASELINE QUOTED, 0-DIFF AFTER, NOTHING ELSE RODE: the root's UNSCOPED plan before, the changed-resource list enumerated with its count, the UNSCOPED re-plan after, ledger CLOSED on exercised evidence, push state MEASURED. **If the root carries a known non-converging diff, file `UNVERIFIABLE-BY-INSTRUMENT` and substitute** -- the purpose is nothing-else-rode; the 0-diff is only its measure.

<expected_criteria>S17B-AC1, S17B-AC2, S17B-AC3, S17B-AC4, S17B-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc>, cell `OP-s-17` (manifest S17; FWD-16, FWD-18), **round 2**. **Adds NO new cell and NO new manifest row** -- it executes `OP-x-4`, the decide-first cell `OP-s-17`'s own constraint column named as this work's home, now CLOSED on Andrew's word. Follows the `TO-OP-S-9C`/`9D` and `TO-OP-S-10B`/`10C` precedent.
<owned_cells>OP-s-17</owned_cells>
Read-dependencies, NOT claimed: `OP-x-4` (the authorisation), `OP-s-25`/`26`/`27` (the evidence store's round-2 build), `OP-s-14` (the sentinel, which WRITES the case files this protects).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- C1 SENTINEL 20 lines -> 4 gates (corrected; the tool prints 21 -> 5 because it counts a LOG QUOTING a sentinel as a gate). ⛔ **Stated as a COMPONENT, not a total** -- a total is a sum of moving parts and can be right for the wrong reasons. **ORIENTATION at that vintage, never a criterion; this face discharges no gate.**
comp-iam: RUN -- `S17B-AC4` requires an applied-plane enumeration of `s3:BypassGovernanceRetention` holders. **`comp-iam` is a DESIRED-plane lens and its silence is NEVER an ALLOW**; the verdict is `simulate-principal-policy` against applied principals, one `--resource-arns` per call, with a positive control as a separate invocation.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim at cut; its evidence is live reads at the assignee's own vintage.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S17B-AC1`, `S17B-AC2`, `S17B-AC3`, `S17B-AC4`, `S17B-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~X/NFRA_OPSEC202609.TO-OP-S-17B.object-lock-on-cases.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S17B-AC1,S17B-AC2,S17B-AC3,S17B-AC4,S17B-AC5"` BEFORE the complete flip. ⛔ **THE CONTROL THAT MUST BE ABLE TO FAIL IS `S17B-AC2`'s pre-existing-object read: if it returns retention, the forward-only finding is wrong and the whole coverage statement must be re-derived.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before the apply">Re-read versioning and the `cases/` object count at YOUR vintage. The 438 is the issuer's reading and the sentinel writes continuously.</phase>
  <phase id="2" when="during">One apply, ledgered, rollback named first. ⛔ No re-write of any existing object, by any verb.</phase>
  <phase id="3" when="after">The before/after retention reads pasted with the enable timestamp between them, the bypass holders enumerated by simulation, and the coverage boundary written where a reader of the evidence store will meet it.</phase>
</compiler_tools_mandate>
