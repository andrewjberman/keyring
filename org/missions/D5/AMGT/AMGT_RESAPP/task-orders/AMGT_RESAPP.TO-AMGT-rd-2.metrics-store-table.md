# AMGT_RESAPP.TO-AMGT-rd-2 -- THE METRICS STORE: a NEW DynamoDB table `opal-amgt-security-metrics` holding PRE-COMPUTED per-ticker ranking rows, mirroring the proven articles / trending-daily split

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rd-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~2</issued_to>

## THE CELL, INLINED IN FULL (round 5/v5, row S16, FWD-15)

```
AMGT-rd-2. THE METRICS STORE. A NEW DynamoDB table `opal-amgt-security-metrics` holding PRE-COMPUTED
per-ticker ranking rows, mirroring the PROVEN `opal-news-articles` / `opal-news-trending-daily` split:
content in one table, the rankings derived from it in another.

WHY THE SPLIT IS THE POINT (`C-SERVER-SIDE-RANKING`): Trending / Breakout x Price / Chatter are computed
SERVER-SIDE by daily jobs and WRITTEN here as rows. The Lead Panel READS them and NEVER re-derives a
ranking at render time. A page that sorts client-side, or recomputes a score on load, is the defect this
constraint exists to prevent.

The table holds the four axes' outputs. Two writers land later in this slot's queue: `AMGT-rd-5` (the
chatter axis, 30-day / 0-100 normalized / TOP_N=10) and `AMGT-rd-6` (the price axis, 30-day, BOX-SIDE).
`AMGT-rd-7` (the starred watchlist, PER-FIRM) also persists here or in a sibling keyspace -- your schema
should not make that impossible, but you are NOT building the writers or the watchlist.

MEASURED ABSENT on the live plane at the cut (surprise row AMGT_RESAPP-Z-S5: 0 hits across a denominator
of 2445 aws nodes). A GENUINE CREATE -- re-measure before you build and say what you found.

WHAT TO PRODUCE, under infra/aws/terraform/amgt-resapp/ + .../deliverables/0.9.0_WK_AMGT_RESAPP~2/:

  (a) THE TABLE  `opal-amgt-security-metrics` in the SAME module directory `AMGT-rd-1` creates
      (infra/aws/terraform/amgt-resapp/). PAY_PER_REQUEST. Keyed so a per-ticker row for a given axis and
      as-of date is a single point read -- the Lead Panel's read pattern is "give me the ranked set for
      this axis", not a scan.

  (b) THE DEPLOY, THROUGH THE GUARDS  change-management entry OPENED in
      org/critical_paths/change_management/ BEFORE the apply, CLOSED before your grading read; apply
      through `safe-apply`, NEVER bare `terraform apply`. Commit the ledger entry AND the sentinel.

  (c) THE READ-PATTERN RECORD  a short deliverable stating the key schema and the exact read the Lead
      Panel will issue against it, plus the `opal-news-trending-daily` shape you mirrored -- measured from
      the live table, not asserted.
```

## DEPENDENCIES

**NONE -- this is a ROOT and spawns at issuance**, alongside `AMGT-rd-1`, per Andrew's *"the box + both
tables, TABLES FIRST."* Everything else in CHAIN B depends on this cell.

## BOUNDS

```
BLOCK PRE-COMPUTED, SERVER-SIDE. This table stores ranking OUTPUTS. No cell downstream may re-derive a
  ranking at render time; your schema must make the pre-computed read the natural one.
BLOCK DO NOT BUILD THE WRITERS. AMGT-rd-5 (chatter) and AMGT-rd-6 (price) are separate cells later in this
  queue. Build the store, not its producers.
BLOCK NOT `opal-data-research` and NOT `opal-news-trending-daily` with a filter. A separate table.
BLOCK safe-apply, NEVER bare `terraform apply`. Change-management entry OPENED BEFORE, CLOSED BEFORE the
  grading read (NEVER-2). Commit the sentinel, not just the entry.
BLOCK NO MONITOR, NO ALARM, NO SNS, NO FRESHNESS CHECKER on this table. Standing moratorium.
BLOCK NO non-ASCII in code, logs or AWS.
WARN AMGT-rd-1 may be creating the same module directory concurrently in another worktree. Your Terraform
  goes in its own FILE inside that directory; do not restructure or rewrite that cell's file.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-find --corpus aws (at the cut): `opal-amgt-security-metrics` ABSENT -- 0 hits across 2445 aws nodes.
    A genuine create. `opal-news-articles` is drift=LIVE-no-DECLARED (in AWS, NOT in this repo's
    Terraform), so the proven split you are mirroring has no declarative source here: read the LIVE
    tables' shapes and say in your deliverable that you did.
comp-cache collisions (at the cut): 415 of 415 portal files scanned. Every existing react-query key
    collision is on ANOTHER surface (market-performance, model-portfolio, partner-analytics,
    positioning). NO AMGT/research key namespace exists yet -- so the Lead Panel (AMGT-rd-8) enters clean,
    and your key schema is what its query keys will be shaped around.
comp-schedule --drift (at the cut): C3 = 12 standing NEVER clauses, including the no-monitor moratorium.
PRD s.3b C-SERVER-SIDE-RANKING (Andrew-direct 2026-09-11 ~12:1xZ): the split, the four axes, "The Lead
    Panel READS them and never re-derives a ranking at render time", chatter = 30-day / 0-100 / TOP_N=10,
    price = the new engine.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/terraform/amgt-resapp/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-2.metrics-store-table.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~2/`. A path missing from that block is a path you
are REFUSED on. Refuse a criterion you cannot satisfy as written and report it; file a surprise ROW
(`AMGT_RESAPP-Z-W2-S<k>` continuing your prior sequence, project AMGT_RESAPP, fabric site-z) and STOP on that
criterion if you need a surface not listed. MINT THE ROW ID FROM A RE-READ of the channel file, never from
recall -- two seats minting from memory collided on this project today.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rd-2"><invocation>cd infra/aws/terraform/amgt-resapp &amp;&amp; timeout 110 terraform validate -no-color 2>&amp;1 | tail -5</invocation><expect>"Success! The configuration is valid." -- the module including your new table file parses and type-checks. A validate error is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rd-2"><invocation>timeout 110 .tools/aws dynamodb describe-table --table-name opal-amgt-security-metrics --query "Table.[TableName,TableStatus,BillingModeSummary.BillingMode]" --output text 2>&amp;1 | tail -3</invocation><expect>"opal-amgt-security-metrics" with TableStatus ACTIVE and BillingMode PAY_PER_REQUEST -- LIVE on the plane, not merely declared. A ResourceNotFoundException means the apply did not land and is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rd-2"><invocation>timeout 110 .tools/aws dynamodb describe-table --table-name opal-amgt-security-metrics-NOPE-xyz --query "Table.TableName" --output text 2>&amp;1 | tail -2</invocation><expect>a ResourceNotFoundException -- NEGATIVE CONTROL proving AC2's instrument discriminates present from absent. If this bogus name ALSO returns a table, AC2 proves nothing and this criterion is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rd-2" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical): the table is declared and the module still validates with both tables in it.
- **AC2** (mechanical, LIVE plane): the table is actually there -- a declaration is not a deployment.
- **AC3** (mechanical, NEGATIVE CONTROL): AC2's instrument can say NO.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names `3.0.0_SA_CVO~Z`): does the key schema actually make the Lead Panel's read a PRE-COMPUTED point/query read rather than a scan-and-sort -- i.e. does it enforce `C-SERVER-SIDE-RANKING` structurally rather than by convention -- and was the `opal-news-trending-daily` mirroring measured against the live table rather than asserted?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>5</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.6.1 + L6 round 5) - **Project:** AMGT_RESAPP - **PRD:** v0.4 @6c52a4e380 (L4-R ADMITTED; brief half content-bound at c90934a3d620)
**Authority chain:** L10 round-4 analysis @959ba3e947 -> PRD s.3b, ANDREW-DIRECT 2026-09-11 ~12:1xZ -> L5 decomposition v0.6.1 @d0efe81ca8 (section 13, AMGT-rd-2) -> this round-5 issuance.
**Chain:** round 5 (v5), CHAIN B head, slot ~2. ROOT -- spawns at issuance alongside `AMGT-rd-1`. Followed in this slot's queue by `AMGT-rd-5`, `AMGT-rd-6`, `AMGT-rd-7`, then `AMGT-rd-8` last.
**Provenance:** decomposition v0.6.1 section 13b's `AMGT-rd-2` row; the constraint is `C-SERVER-SIDE-RANKING` (PRD s.3b).
> **NOTE (2.0.0_SA_COO~ZZZ).** Both roots write into the SAME new module directory. That is deliberate (one module for this project's infra) and the bound above tells each worker to use its own file. If the two collide at the drain, the resolution is mine, not theirs.
<preflight>
comp-schedule: RUN -- 5 of 5 carriers; C1=23 C2=6 C3=12 C4=20 C5=334; C3's no-monitor clause bounded in. BLIND: C4/C5 not decidable, a reading list.
comp-iam: RUN -- 836 call(s) across 96 mapped role(s); no AMGT role yet; this cell creates none. BLIND: 630 UNRESOLVABLE-RESOURCE, 266 calls in 26 role-UNMAPPED services never checked, 51 GRANTED-BROAD excluded not cleared.
comp-cache: RUN -- 415 of 415 portal files scanned; no AMGT key namespace exists, so this schema shapes AMGT-rd-8's query keys. BLIND: it sees declared query keys only, not keys built dynamically at call time.
comp-adversary: RUN -- 1 artifact declared (decomposition v0.6.1 @d0efe81ca8). BLIND: author's stated evidence context only.
comp-blast: DECLARED-NOT-APPLICABLE -- creates a new resource, modifies no shared one.
</preflight>
**Preflight disposition:** a genuine create, measured absent on the live plane at the cut; deploy-class, so the ledger entry and the sentinel are both in `<paths>` and both must be committed.
