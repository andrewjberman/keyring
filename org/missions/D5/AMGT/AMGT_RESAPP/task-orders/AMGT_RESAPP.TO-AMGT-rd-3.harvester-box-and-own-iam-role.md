# AMGT_RESAPP.TO-AMGT-rd-3 -- THE HARVESTER BOX AND ITS OWN IAM ROLE: a NEW stopped-between-runs EC2 box in the ASTN_WSJFT shape, with AMGT_RESAPP's OWN role, and a REFRESH THAT WAKES IT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rd-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~1</issued_to>

## THE CELL, INLINED IN FULL (round 5/v5, row S16, FWD-15)

```
AMGT-rd-3. THE HARVESTER BOX + ITS OWN IAM ROLE. A NEW EC2 box in infra/aws/terraform/amgt-resapp/
following the ASTN_WSJFT SHAPE -- stopped between runs, SSM-woken -- but with AMGT_RESAPP's OWN IAM role
and write access to `opal-amgt-articles`.

EXPLICITLY NOT THE ASTN_WSJFT BOX AND NOT ITS ROLE. Andrew's constraint names the SHAPE as the precedent
to copy and the INSTANCE as the thing to avoid. Reusing that box or attaching its role is the failure this
sentence exists to prevent: two projects sharing one harvester host means one project's egress budget,
one project's IAM blast radius, and one project's outage reaching the other.

ONE SHARED BOX FOR ALL FOUR HARVESTERS (`AMGT-rd-4` builds them; you build the host they run on).

THE WAKE IS PART OF THIS CELL, NOT A FOLLOW-UP. A stopped box that nothing wakes SILENTLY NO-OPS: the
refresh appears to run, nothing harvests, and no error is raised. Refresh MUST WAKE the box through SSM
(the `inf-jwt-trigger` shape is the estate's precedent). Prove the wake, not just the box.

WHAT TO PRODUCE, under infra/aws/terraform/amgt-resapp/ + .../deliverables/0.9.0_WK_AMGT_RESAPP~1/:

  (0) THE MODULE RECONCILE, FIRST, BEFORE ANYTHING ELSE -- surprise rows AMGT_RESAPP-Z-S9 and -Z-S10.
      The module you are about to extend IS CURRENTLY INVALID and `terraform validate` fails on it:

        Error: A module may have only one 'backend' configuration block (main.tf:30,3-15)
        Error: Duplicate provider configuration (security-metrics-table.tf line 63)

      CAUSE, so you do not misread it as someone's mistake: AMGT-rd-1 and AMGT-rd-2 ran in PARALLEL
      worktrees and each correctly declared a terraform{} and provider "aws"{} block for its own tree.
      Both are MODULE-SCOPED and may appear exactly once per directory, so they collided on merge. The
      rd-2 worker also chose a distinct backend key deliberately, to avoid a concurrent-apply state race
      while the two ran side by side, and documented that in the file's own header. Both workers were
      right; the gap was the ISSUER'S bound, which named file separation and not singleton scope.

      WHAT TO DO: keep `main.tf` as the single module root. Remove the duplicate terraform{} and
      provider "aws"{} blocks from `security-metrics-table.tf`, PRESERVING its
      `aws_dynamodb_table.security_metrics` resource and its explanatory header comments byte-for-byte.
      Leave a short note in that file saying the blocks were removed, by whom, and why. Then confirm
      `terraform validate` returns "Success! The configuration is valid." BEFORE you add the box.

      WHY IT IS YOURS AND NOT THE COO'S: the COO wrote this exact fix, verified it, and was then
      LANE-REFUSED -- infra/aws/terraform/ is lane CLOUD_OPS_OR_ETL ("any AE agent") and the COO is not
      one. It reverted rather than forcing an audited override to write infra it does not own. You hold
      the path through this order's <paths> (RULING 1), and you cannot add the harvester box to an
      invalid module in any case, so the reconcile is genuinely part of this cell.

      STATE IS NOT CONSOLIDATED AND YOU ARE NOT ASKED TO CONSOLIDATE IT. rd-1's table lives in backend
      key `amgt-resapp/tfstate`; rd-2's was applied under `amgt-resapp/rd-2-security-metrics/tfstate`.
      After your reconcile the module points at the former, which does NOT contain
      `aws_dynamodb_table.security_metrics`. A plan will therefore propose CREATING a table that already
      exists. DO NOT run an apply that would act on that proposal, and DO NOT run `terraform import` --
      state consolidation is a separate deploy-class act with its own change-management entry, owned by
      the COO. Scope your own apply to YOUR resources. If you cannot apply without touching that
      proposal, STOP and file a row rather than working around it.

  (a) THE BOX  a new EC2 instance declared in the module, stopped-between-runs, in the ASTN_WSJFT shape.
      Read that shape from its own Terraform and say in your deliverable what you copied and what you
      deliberately did not.

  (b) THE OWN ROLE  an IAM role belonging to AMGT_RESAPP, granting write to `opal-amgt-articles` (the
      table AMGT-rd-1 landed) and nothing wider. `comp-iam service` at Phase 1 and `comp-iam gaps` at
      Phase 2 -- both are auto-rule 3 and both are required because iam.tf changes.

  (c) THE WAKE PATH  an SSM-driven wake a refresh action can invoke, with the no-op hazard closed: if the
      box is stopped, the wake starts it and the run proceeds; it does not silently return success.

  (d) THE DEPLOY, THROUGH THE GUARDS  change-management entry OPENED BEFORE the apply and CLOSED before
      your grading read; `safe-apply`, NEVER bare `terraform apply`. Commit the ledger entry AND the
      sentinel.
```

## DEPENDENCIES

**DEPENDS ON `AMGT-rd-1` (the article store).** The role's write grant needs the table to exist to be
scoped to it -- a role granting write to a table that does not exist is either a wildcard or a lie. Worked
SECOND in slot ~1's queue, after `AMGT-rd-1` lands; your worktree is cut from the HEAD carrying it.

## BOUNDS

```
BLOCK NOT THE ASTN_WSJFT BOX AND NOT ITS ROLE. Copy the SHAPE; create your own instance and your own role.
  Do not attach, extend, or reuse that project's role, instance profile or box.
BLOCK OWN ROLE, SCOPED: write to `opal-amgt-articles` and nothing wider. No wildcard resource on a
  PutItem grant. A wildcard cannot be falsified by a resource check and will read as GRANTED-BROAD.
BLOCK THE WAKE IS PROVEN, NOT ASSUMED. A stopped box that nothing wakes silently no-ops. Exercise the wake.
BLOCK safe-apply, NEVER bare `terraform apply`. Ledger entry OPENED BEFORE, CLOSED BEFORE the grading read
  (NEVER-2). Commit the sentinel, not just the entry.
BLOCK NO VENDOR EGRESS FROM THIS CELL. The vendor word is TIME-SCOPED and its clock is THIS BOX being
  stood up -- it is AMGT-rd-4 that may then call Seeking Alpha / FT / Bloomberg / WSJ. You build the host;
  you do not fetch from any vendor.
BLOCK NO MONITOR, NO ALARM, NO SNS, NO FRESHNESS CHECKER on the box. Standing moratorium.
BLOCK NO non-ASCII in code, logs or AWS.
BLOCK NEVER `aws lambda update-function-code` -- Terraform only.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-iam gaps (at the cut): 836 call(s) verdicted across 96 mapped role(s); 12 missing, 291 deny-present,
    1 coverage-unknown, 2 resource-mismatch across 31 services. NO AMGT ROLE EXISTS YET -- you create the
    first one, so there is no prior AMGT verdict to compare against and the baseline is honestly empty.
    COVERAGE LIMITS carried, NOT cleared: 630 UNRESOLVABLE-RESOURCE; 266 calls in 26 role-UNMAPPED
    services NOT resource-checked; 51 GRANTED-BROAD rows EXCLUDED rather than cleared -- a wildcard grant
    CANNOT be falsified by a resource check, which is exactly why the bound above forbids one.
comp-schedule --drift (at the cut): 6 open deploy-ledger entries (carrier C2) -- an OPEN entry is an ARMED
    gate, so yours must be CLOSED before your grading read, not left open. C3 = 12 standing NEVER clauses.
PRD s.3b C-HARVESTER-COMPUTE (Andrew-direct 2026-09-11 ~12:1xZ): the ASTN_WSJFT SHAPE, the OWN IAM role,
    write access to opal-amgt-articles, "explicitly NOT the ASTN_WSJFT box", ONE shared box for all four,
    and "Refresh must WAKE the stopped box (SSM / inf-jwt-trigger shape) or it silently no-ops."
AMGT_RESAPP-Z-W1-S7 (0.9.0_WK_AMGT_RESAPP~1, filed on rd-1, ARMED): safe-apply's HALTGT checkpoint
    REFUSES with IDENTITY UNRESOLVED until a session-keyed serial file exists at
    org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial -- the gate reads it to resolve whose inbox to scan
    for a STOP. It is gitignored, per-session, collision-free across workers, and is TOOL PLUMBING on the
    same footing as resolving a PATH shim, not a deliverable. rd-1's order did not grant that path and
    its worker had to judge the call under a live BLOCK. THAT GRANT IS NOW EXPLICIT IN <paths> BELOW so
    you do not have to re-derive it: write it if safe-apply refuses on identity, and do not file a row
    for it.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/mcp/sessions/
infra/aws/terraform/amgt-resapp/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-3.harvester-box-and-own-iam-role.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~1/`. A path missing from that block is a path you
are REFUSED on. Refuse a criterion you cannot satisfy as written and report it; file a surprise ROW
(`AMGT_RESAPP-Z-W1-S<k>` continuing your prior sequence) and STOP on that criterion if you need a surface
not listed. MINT THE ROW ID FROM A RE-READ of the channel file, never from recall.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rd-3"><invocation>cd infra/aws/terraform/amgt-resapp &amp;&amp; timeout 110 terraform validate -no-color 2>&amp;1 | tail -5</invocation><expect>"Success! The configuration is valid." -- the module carrying both tables, the instance and the role parses and type-checks. A validate error is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rd-3"><invocation>timeout 110 .tools/aws iam list-attached-role-policies --role-name $(timeout 60 .tools/aws iam list-roles --query "Roles[?contains(RoleName,'amgt')].RoleName" --output text | head -1) --output text 2>&amp;1 | tail -5</invocation><expect>an AMGT-named role that EXISTS and has at least one attached or inline policy -- AMGT_RESAPP's OWN role is live. An empty role name (no amgt role found) or a NoSuchEntity is NOT met. The role name must NOT be an ASTN_WSJFT role</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rd-3"><invocation>timeout 110 .tools/aws ec2 describe-instances --filters "Name=tag:Project,Values=AMGT_RESAPP" --query "Reservations[].Instances[].[InstanceId,State.Name]" --output text 2>&amp;1 | tail -5</invocation><expect>exactly ONE instance id with a state of "stopped" or "running" -- the box exists and is tagged to THIS project, which is what distinguishes it from the ASTN_WSJFT box. Zero instances means the apply did not land; more than one means a second box was created and is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rd-3" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical): the module validates with the box and role added.
- **AC2** (mechanical): an AMGT-OWNED role exists with a policy -- not a borrowed one.
- **AC3** (mechanical): exactly one box, tagged to this project, in the stopped-between-runs shape.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names `3.0.0_SA_CVO~Z`): is the WAKE actually proven -- does a refresh against a STOPPED box start it and run, rather than silently no-opping -- and is the role's write grant SCOPED to `opal-amgt-articles` rather than a wildcard that no resource check could falsify? These are the two ways this cell can look done and not be.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>superseded</status>
<superseded_by>THE HARVEST ESTATE, per PRD v0.5 L4 ADDENDUM @5517e071e8, on ANDREW-DIRECT 2026-09-11 ~17:3xZ (one box, one lambda, harvest naming, one consolidated harvester tf) and his ~18:3xZ approval of 4.0.0_SA_CRO~Z's draw (the box is an EC2 instance, NOT site-Z). That seat oversees and executes it. Routing (a) decided by 1.0.0_SA_CTO~Z as L10 owner (msg 21516); this status set by the ISSUER 2.0.0_SA_COO~ZZZ only AFTER the addendum existed, because a terminal status without its pointer is rot with a tidier label. Coverage repair rides THIS SAME COMMIT: decomp s.13c/13d/13f amended so the subtraction is TRUE at SIX cells.</superseded_by>
<amended>2026-09-11T18:0xZ by 2.0.0_SA_COO~ZZZ, BEFORE the spawn: granted org/mcp/sessions/ per row Z-W1-S7 ; added the module reconcile per rows Z-S9/Z-S10</amended>
<round>5</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.6.1 + L6 round 5) - **Project:** AMGT_RESAPP - **PRD:** v0.4 @6c52a4e380 (L4-R ADMITTED)
**Authority chain:** L10 round-4 analysis @959ba3e947 -> PRD s.3b `C-HARVESTER-COMPUTE`, ANDREW-DIRECT 2026-09-11 ~12:1xZ -> L5 decomposition v0.6.1 @d0efe81ca8 (section 13, AMGT-rd-3) -> this round-5 issuance.
**Chain:** round 5 (v5), CHAIN A middle, slot ~1. Handed after `AMGT-rd-1` lands; followed by `AMGT-rd-4`.
**Provenance:** decomposition v0.6.1 section 13b's `AMGT-rd-3` row.
> **NOTE (2.0.0_SA_COO~ZZZ).** This cell is the CLOCK on the vendor word. `C-VENDOR-WORD-HARVESTERS` is effective "when the harvester box is stood up and ready to run -- NOT before", so `AMGT-rd-4` is gated on this cell landing, and this cell itself may not egress to any vendor.
<preflight>
comp-schedule: RUN -- 5 of 5 carriers; C2 = 6 OPEN deploy-ledger entries (an OPEN entry is an ARMED gate, so yours closes before the grading read); C3 = 12 standing NEVER clauses. BLIND: C4/C5 not decidable.
comp-iam: RUN -- 836 call(s) verdicted across 96 mapped role(s); NO AMGT role exists, so this cell creates the first and has no prior AMGT verdict to compare against. BLIND: 630 UNRESOLVABLE-RESOURCE, 266 calls in 26 role-UNMAPPED services never checked, and 51 GRANTED-BROAD rows EXCLUDED not cleared -- which is exactly why a wildcard grant is forbidden here.
comp-adversary: RUN -- 1 artifact declared (decomposition v0.6.1 @d0efe81ca8). BLIND: author's stated evidence context only.
comp-blast: DECLARED-NOT-APPLICABLE -- creates new resources; modifies no shared one.
</preflight>
**Preflight disposition:** infra + IAM create, deploy-class. Ledger entry and sentinel both in `<paths>`. The wake is the cell's real risk and is carried as a judgment criterion because a silent no-op passes every mechanical check.
