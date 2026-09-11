# AMGT_RESAPP.TO-AMGT-rd-1 -- THE ARTICLE STORE: a NEW DynamoDB table `opal-amgt-articles`, genuinely separate from `opal-news-articles`, created by Terraform through safe-apply under a change-management entry

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rd-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~1</issued_to>

## THE CELL, INLINED IN FULL (round 5/v5, rows S4 + S13, FWD-4 / FWD-11)

```
AMGT-rd-1. THE ARTICLE STORE. Per-ticker article content lands in a NEW DynamoDB table
`opal-amgt-articles`, shaped like the proven `opal-news-articles` (title / source / url / published_at /
sentiment) PLUS `ticker` / `security_key` (resolved via the S12 identity layer) and `platform`.

It is GENUINELY SEPARATE from two existing stores and the separation is the point:
  - NOT `opal-news-articles` with a filter. That table is the general-market news store; this one is
    per-ticker research content for covered and on-demand names.
  - NOT `opal-data-research`. That bucket stays S1's model-block home and S5's print-snapshot home.

MEASURED ABSENT on the live plane at the cut (surprise row AMGT_RESAPP-Z-S5: `comp-find --corpus aws`
returned 0 hits for `opal-amgt-articles` across a denominator of 2445 aws nodes). So this is a GENUINE
CREATE, not an integration -- re-measure before you build and say what you found.

WHAT TO PRODUCE, under infra/aws/terraform/amgt-resapp/ + .../deliverables/0.9.0_WK_AMGT_RESAPP~1/:

  (a) THE TERRAFORM MODULE  a new module directory infra/aws/terraform/amgt-resapp/ declaring the table
      `opal-amgt-articles`. PAY_PER_REQUEST billing (matching opal-news-articles). The key schema and
      attributes carry ticker/security_key and platform as first-class, not packed into a blob.

  (b) THE DEPLOY, THROUGH THE GUARDS  a change-management entry OPENED in
      org/critical_paths/change_management/ BEFORE the apply and CLOSED before your grading read; the
      apply through `safe-apply`, NEVER a bare `terraform apply`. Commit the ledger entry AND the
      sentinel -- a staged-but-uncommitted sentinel does not survive a worktree teardown.

  (c) THE SHAPE RECORD  a short deliverable naming the attribute set you landed and, beside it, the
      attribute set of `opal-news-articles` you shaped it after -- so a later reader can see the
      mirroring was measured rather than asserted.
```

## DEPENDENCIES

**NONE -- this is a ROOT and spawns at issuance.** It is one of the two roots of round 5, and Andrew's
order is explicit: *"the box + both tables, TABLES FIRST."* `AMGT-rd-3` (the harvester box) depends on this
cell because the box's IAM role needs this table to grant write access to.

## BOUNDS

```
BLOCK GENUINELY SEPARATE: do NOT add a filter, a GSI or a tenant column to `opal-news-articles` and call
  it done. A separate table is the instruction, and the reason is that the two have different owners,
  different lifecycles and different consumers.
BLOCK NOT `opal-data-research`: that bucket is S1's model-block + S5's print-snapshot home and is an
  EXISTING declared resource. Do not extend it, re-create it, re-declare it or reconfigure it.
BLOCK safe-apply, NEVER bare `terraform apply`. A change-management entry is OPENED BEFORE the act and
  CLOSED before the grading read (NEVER-2). Commit the sentinel, not just the entry.
BLOCK NO SECOND OUTPUT PATH beside the one table.
BLOCK NO non-ASCII in code, logs or AWS. Use OK: / WARN: / ERROR: / SKIP: / BLOCKED:.
BLOCK NO MONITOR, NO ALARM, NO SNS, NO FRESHNESS CHECKER on this table. Standing moratorium.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-find --corpus aws (at the cut, surprise row AMGT_RESAPP-Z-S5): DENOMINATOR 2 hit(s) across 2445 aws
    node(s). `opal-news-articles` = DYNAMODB_TABLE, drift=LIVE-no-DECLARED -- it EXISTS in AWS but is NOT
    declared in this repo's Terraform. So the table you are shaping after has no declarative source to
    copy: read the LIVE table's shape, and say in your deliverable that you did.
    NEITHER `opal-amgt-articles` NOR `opal-amgt-security-metrics` appeared -- both are genuine creates.
comp-iam gaps (at the cut): 836 call(s) verdicted across 96 mapped role(s); NO AMGT role exists yet. That
    is the honest baseline -- AMGT-rd-3 creates the first one. Nothing here grants this table's writers.
comp-schedule --drift (at the cut): 5 of 5 carriers; C3 = 12 standing NEVER clauses, including the
    no-monitor moratorium bounded above. 2 drift candidates, neither this project's.
PRD s.3b C-AMGT-ARTICLES-STORE (Andrew-direct 2026-09-11 ~12:1xZ): the table shape, the separation from
    both existing stores, and "Andrew-authorized 2026-09-11: the box + both tables, TABLES FIRST."
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/terraform/amgt-resapp/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-1.article-store-table.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~1/`. A path missing from that block is a path you
are REFUSED on. Refuse a criterion you cannot satisfy as written and report it; file a surprise ROW
(`AMGT_RESAPP-Z-W1-S<k>` continuing your prior sequence, project AMGT_RESAPP, fabric site-z) and STOP on that
criterion if you need a surface not listed. MINT THE ROW ID FROM A RE-READ of the channel file, never from
recall -- two seats minting from memory collided on this project today.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rd-1"><invocation>cd infra/aws/terraform/amgt-resapp &amp;&amp; timeout 110 terraform validate -no-color 2>&amp;1 | tail -5</invocation><expect>"Success! The configuration is valid." -- the new module parses and type-checks. A validate error, or a missing module directory, is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rd-1"><invocation>timeout 110 .tools/aws dynamodb describe-table --table-name opal-amgt-articles --query "Table.[TableName,TableStatus,BillingModeSummary.BillingMode]" --output text 2>&amp;1 | tail -3</invocation><expect>"opal-amgt-articles" with TableStatus ACTIVE and BillingMode PAY_PER_REQUEST -- the table is LIVE on the plane, not merely declared in a .tf file. A ResourceNotFoundException means the apply did not land and is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rd-1"><invocation>timeout 110 .tools/aws dynamodb describe-table --table-name opal-amgt-articles-NOPE-xyz --query "Table.TableName" --output text 2>&amp;1 | tail -2</invocation><expect>a ResourceNotFoundException -- NEGATIVE CONTROL proving AC2's describe-table actually discriminates present from absent rather than returning success for any name. If this bogus name ALSO returns a table, AC2 proves nothing and this criterion is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rd-1" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical): the Terraform module exists and is valid.
- **AC2** (mechanical, LIVE plane): the table is actually there with the intended billing mode -- a declaration is not a deployment.
- **AC3** (mechanical, NEGATIVE CONTROL): AC2's instrument can say NO. A describe-table that succeeds on a bogus name would make AC2 vacuous.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names `3.0.0_SA_CVO~Z`): is the table GENUINELY SEPARATE in the sense Andrew's constraint meant -- its own store for per-ticker research content, carrying ticker/security_key and platform as first-class, shaped after `opal-news-articles` rather than being that table with a filter -- and was the mirroring MEASURED against the live table rather than asserted?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>5</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.6.1 + L6 round 5) - **Project:** AMGT_RESAPP - **PRD:** v0.4 @6c52a4e380 (L4-R ADMITTED; brief half content-bound at c90934a3d620)
**Authority chain:** L10 round-4 analysis @959ba3e947 (answering CVO slug REMEDIATION_v4 @b97837e7fe) -> PRD s.3b, ANDREW-DIRECT 2026-09-11 ~12:1xZ "Recs approved" -> L5 decomposition v0.6.1 @d0efe81ca8 (section 13, AMGT-rd-1) -> this round-5 issuance.
**Chain:** round 5 (v5), CHAIN A head, slot ~1. ROOT -- spawns at issuance alongside `AMGT-rd-2` (TABLES FIRST). Followed in this slot's queue by `AMGT-rd-3` then `AMGT-rd-4`.
**Provenance:** decomposition v0.6.1 section 13b's `AMGT-rd-1` row; the constraint is `C-AMGT-ARTICLES-STORE` (PRD s.3b).
> **NOTE (2.0.0_SA_COO~ZZZ).** The cut did NOT rest on the gate's ADMITTED alone: row `AMGT_RESAPP-Z-S6` measured that gate false-greening the brief half, so a second limb was required -- a `4.0.0_SA_CRO*.json` record whose `half_hash` equals the brief half's CURRENT hash. Verified PASS at c90934a3d620 in the LANE record before this order was cut.
<preflight>
comp-schedule: RUN -- 5 of 5 carriers scanned; C1=23 C2=6 C3=12 C4=20 C5=334; C3's no-monitor clause bounded into this cell. BLIND: C4/C5 are SEMI- and NOT-DECIDABLE, so 20 scope_guards and 334 project blocking fields are a reading list, not gates.
comp-iam: RUN -- 836 call(s) verdicted across 96 mapped role(s); 12 missing, 291 deny-present, 2 resource-mismatch. NO AMGT role exists yet. BLIND: 630 UNRESOLVABLE-RESOURCE, 266 calls in 26 role-UNMAPPED services never resource-checked, 51 GRANTED-BROAD EXCLUDED not cleared.
comp-adversary: RUN -- 1 artifact declared (decomposition v0.6.1 @d0efe81ca8). BLIND: it declares the AUTHOR'S evidence context only; it can never certify what exists outside what the author cited.
comp-blast: DECLARED-NOT-APPLICABLE -- this cell CREATES a new resource and modifies no shared one; no live served artifact moves.
</preflight>
**Preflight disposition:** a genuine create on a new Terraform module, measured absent on the live plane at the cut; deploy-class, so the change-management entry and the sentinel are both in `<paths>` and both must be committed.
