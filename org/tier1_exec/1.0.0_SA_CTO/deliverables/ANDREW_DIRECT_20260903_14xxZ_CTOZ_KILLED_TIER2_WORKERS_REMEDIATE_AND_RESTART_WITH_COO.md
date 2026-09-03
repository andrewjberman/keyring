# ANDREW-DIRECT 2026-09-03 ~14:0xZ at the `1.0.0_SA_CTO~Z` terminal -- the Tier-2 workers were KILLED; remediate and restart with the COO

**VERBATIM, the whole word:**

> ok we need to move along here, i killed the tier2 workers because we were having API connection issues, I need you to remediate and restart from wherever they left off with COO, spawning the necessary workers so we can proceed

## What the word establishes

1. **The kill was ANDREW'S and its cause was infrastructural, not a work defect.** `0.7.0_AE_CloudOps~S` and
   `0.7.0_AE_CloudOps~Z` were terminated for API connection issues. Nothing either seat did is retracted, and neither
   is at fault; their work stands exactly as far as it got.
2. **Remediation is asked for FIRST, restart second.** "Remediate and restart from wherever they left off" -- so the
   resume point is MEASURED from artifacts, never assumed, and any half-landed state is closed before new work runs.
3. **The COO is the counterparty and the spawner.** "with COO, spawning the necessary workers" is consistent with the
   standing ruling (Andrew-direct 2026-09-03 ~06:1xZ, the `3.0.0_SA_CVO~A` terminal): the COO spawns the Tier-2 worker
   lanes at L6, and L7 stays Tier-2. This seat routes the restart package to `2.0.0_SA_COO~Z`; it does not seat workers.
4. **"we need to move along here" is a PACE instruction.** It is not a licence to skip a gate, an acceptance row or a
   ledger leg -- and in this case the fastest safe path and the correct one are the same, because the one genuine
   hazard is a five-minute fix.

## The state at the kill, measured (not recalled)

Both worker serials read STALE on the broker (245 s and 238 s at 14:0xZ). Their last summaries and the deploy ledgers
give an exact resume point for each.

**`0.7.0_AE_CloudOps~S`** -- two task orders:
- `TO-OP-S-25-26-27` (the project key, the admin role, the access-logs target): **BUILD COMPLETE AND VERIFIED**,
  instance VALID @`8b8538c37a`. Deploy ledger `opsec-r2-key-role-logs-target` has 5 of 6 legs closed. **L5 is OPEN BY
  DESIGN** -- it grades on a DELIVERED log object inside a 24 h window opened 11:53Z, and an empty read is not a
  failure. Nothing to remediate; it needs a re-read of the target prefix, not a rebuild.
- `TO-OP-S-16-17-8R2` (address-table key flip + demo-table adoption): **L1-L4 closed, L5 and L6 OPEN with `proof:
  null`.** The table key flip APPLIED cleanly and verified (in place, TableId and CreationDateTime identical -- the
  replace control held). The demo-table `terraform import` SUCCEEDED and its tick-2-bar plan was captured
  (0 add / 1 change / 0 destroy, no forces-replacement, deletion protection never true->false). **The apply of those
  two in-place diffs was never run, and the verify legs were never written.** The bucket limb is HELD NOT ATTEMPTED
  by the issuer's own ruling on row Z-S37 and must stay held.

**`0.7.0_AE_CloudOps~Z`** -- `TO-OP-S-2` (the nine anonymous data routes):
- DONE: phase-1 referents all re-grounded; deliverable 4, the belt rider, landed @`653e7dfead`.
- REMAINS, and it had not started: deliverable 1 (nine in-place attribute edits in
  `shared-infra/apigateway-portal/routes.tf`), the rollback exercise, the two probes, the instance, the status flip and
  the S3-AC5 amendment. **A clean stopping point with nothing half-done.**

## THE ONE REAL HAZARD, and it is not what the kill looks like

`terraform import` put `module.firm_demo.aws_dynamodb_table.partner_table` into the **partner-firms STATE**, while the
declaration that justifies it, `infra/aws/terraform/partner-firms/demo.tf`, is **UNTRACKED -- never committed.**

That asymmetry is the danger, not the unapplied diff. A resource in state with no configuration is a resource
Terraform plans to **DESTROY**, and this one is a live partner-tenant identity table. Site Z is a shared checkout that
loses uncommitted work; the whole adoption was one lost file away from a destroy plan against `opal-partner-demo`.

**Acted on immediately by this seat:** the file was copied off the shared tree to session scratchpad
(`RESCUED_demo.tf`, 1,907 bytes) so it cannot be lost, before anything else. It is NOT this seat's lane to commit
(`infra/aws/**` is CLOUD_OPS_OR_ETL), so committing it is the FIRST act of the respawned `~S` worker.

Secondary and lower: the two in-place diffs (SSE AWS-owned -> AWS-managed KMS, PITR OFF -> ON) sit unapplied, so any
seat applying partner-firms for another reason would sweep them up. They are expected and pre-declared, so this is a
sequencing note, not a defect.

## Disposition

Recorded verbatim, broadcast the same turn, restart package routed to `2.0.0_SA_COO~Z` with the resume point for each
face, the hazard, the open ledger legs and their windows. `0.0.0_AB_MSTR~Z` and `3.0.0_SA_CVO~Z` copied for the record.

## CORRECTION (15:5xZ): this record OVERSTATED the hazard's severity, and the deciding value is now measured

**What this record said:** "A resource in state with no configuration is a resource Terraform plans to **DESTROY**, and
this one is a live partner-tenant identity table." That reads as imminent data loss and it is wrong in the direction
that matters for triage.

**The correction, offered by `3.0.0_SA_CVO~Z` (19826) and MEASURED by this seat rather than taken on report:**
`describe-table` on `opal-partner-demo` reads `DeletionProtectionEnabled: True`, TableId 99ddc090, ACTIVE, 1 item.
Positive control on the same probe: `opal-partner-49financial` also reads True. **So a destroy would be REFUSED BY
THE API at apply.** The CVO offered this with its own qualifier -- that the live value rested on the module's
declaration and the worker's header line and was unmeasured -- and that qualifier is now discharged: it is measured,
and it says the CVO's reading is right and this record's was not.

**What is TRUE and unchanged, which is why the item still mattered and still does:** while the declaration is
untracked, any plan or apply in `infra/aws/terraform/partner-firms/` from a clean checkout carries a **destroy LINE**
against a live table, and that root also holds `firm_49financial`, `firm_cottonwood` and `firm_inflection` -- three
REAL firms' identity tables. So the correct cost is **a shared Terraform root blocked for three real firms until state
and configuration agree**, and a destroy line is a STOP and a row under this project's own tick-2 bar. That is a
serious operational cost. It is not the loss of a live table.

**The class, since this is the fourth of the day at this seat:** every one of them attached a faithfully measured fact
to a consequence the measurement did not establish. Here the measured facts -- resource in state, declaration
untracked -- were exactly right, and the word DESTROY was carried from what Terraform would PLAN to what would
actually HAPPEN, across an API refusal nobody had checked. **A plan line is not an outcome, and the step between them
had its own measurable value sitting one call away.**

**Carried to the seats that received the overstatement** (`2.0.0_SA_COO~Z`, `0.0.0_AB_MSTR~Z`, `3.0.0_SA_CVO~Z`) in
the same turn as this amendment. `3.0.0_SA_CVO~Z`'s row Z-S41 @37cc373469 is the durable carrier and already states
the corrected severity; the remedy and its sequencing are unchanged -- the commit is still the discharge and still the
respawned `~S` lane's first act.

**And the restart itself is DONE, measured:** `2.0.0_SA_COO~Z` spawned both lanes at 15:45:34Z (`~S`, pid 6532) and
15:45:44Z (`~Z`, pid 13624), four minutes BEFORE this seat's chase message reached it. Nothing was blocking the spawn
and this seat's chase did not cause it.
