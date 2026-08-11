# MDPF atomic window: crash recovery, L-A landing, L-C reads, wrong-channel finding -> L-D — 0.4.0_DS_ClientPlatform

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, VALIDATE, DIAGNOSE

**Date:** 2026-08-11 (session ~0245-0315Z, MSTR crash-recovery respawn)
**Task Order:** MDPF atomic window 20260811T0150Z legs L-A + L-C (COO GO 014749Z; frame re-confirmed post-crash 025008Z)
**Status:** L-A CLOSED @13a4cecce8; L-C verdicts validated + recorded @22aae247ef (item 3 CLOSED; item 2 split); WAITING on AE L-D for the single item-2 re-read.

---

## Window

Since prior log (`mdpf_remed_rpw1_rpw2_vendor_label_offset_and_frontier_unlink.md`, pre-crash session
which ended ~0230Z in the fabric crash). This session: respawned ~0245Z, recovery + window execution.

## What happened, in order

1. **Recovery:** /watcher (no orphan; fresh registration PID 16056; persistent Monitor task bcnfwc95f
   confirmed running via TaskOutput); session serial stamped per LD-0290; inbox drained — COO L-A GO
   (014749Z) + MSTR crash-recovery direct (024442Z) + COO frame confirmation (025008Z: window OPEN,
   crash ruled NOT a leg failure, GO valid as issued).
2. **L-A EXECUTED 025153-025157Z.** Pre-fire live-state check: S3 still held pre-window bytes
   (dim ETag 2b5bba700f0518ea5a302afd474df64d 158,352B; spine f52858d0c8f18415bb54dacc26ab72e4
   7,760B; 113/9 content-diff lines vs pinned — CTO's pre-crash read independently re-confirmed;
   not a no-op). cp fired from git BLOB bytes of @bf74d031c1 (git show extraction — deploys the
   reviewed artifact by construction), 2 files only, NO trio mint, to
   s3://opal-data-mdpf/code/scripts/gold/. Post-verify 3 layers: head-object (dim
   e7b169a70b80353dcb010187ad6903cd 161,769B @025153Z; spine 6ebc6a822c4d8f55634c070ab145b10b
   8,033B @025157Z); read-back cmp SERVED==PINNED byte-identical; comp-pipescript deployed
   --pipeline mdpf MATCH both. COO validated + CLOSED the ledger row @13a4cecce8.
   *Instrument note:* first live-copy download went to a shim-mangled phantom relative path and the
   diff printed a "0 diff lines" verdict that was counting an error message — caught by the printed
   denominator discipline, re-run clean before any verdict was trusted.
3. **L-C reads (AE fired qa_local cycle 025841-025856Z, fence intact).** Item-2 read found the
   inflection A4 bodies carrying PRE-fix values (label 08-07 custody 208,325,960.35 / model_aua
   144,545,199.97; D-4 anchor at the 08-05 mislabel). Mechanism grounded on three independent
   derivations BEFORE escalating: (i) declarative — lambda-source-map: mdpf-gold-lambda package
   ASSEMBLED FROM PINNED COMMIT @0bc739e7d5, deployed 2026-08-07T03:52Z, pre-RP-W1/W2;
   (ii) applied — live get-function-configuration CodeSha256
   XuLlClWT6kr6n5TCG7keFmzVd8KEafMuAIQutJB+utQ= == the 08-07 artifact, LastModified 08-07T03:51:21Z;
   (iii) behavioral — the qa bodies themselves (consolidator calls spine.build_firm_timeseries
   directly, mdpf_gold_consolidator.py:778-781, so PRE values prove the executing spine lacks RP-W1).
   Live wiring: EventBridge SCHEDULER schedule mdpf-scheduled-floor cron(30 13 * * ? *) UTC ENABLED
   -> mdpf-gold-lambda run_class=production, LastModificationDate tonight (the L-B floor apply);
   Scheduler is invisible to events list-rules — found via the Lambda's resource policy
   (search FOR the resource name; the trigger lives on the caller).
4. **WINDOW-EXISTENTIAL escalation 030919Z** to COO+CTO+AE: the 13:30Z bar fires a producer whose
   baked code predates the fix; L-A landed on the runner channel (s3 script store) the Lambda
   structurally never reads; comp-pipescript deployed MATCH is TRUE for its channel and blind to the
   zip channel. COO validated same turn (ruling @6dc47fc83a): NO leg failed, window spec incomplete
   by one leg; **L-D spawned** (AE lane: re-pin to the same reviewed artifact @bf74d031c1 +
   safe-apply); L-A stands untouched; 13:30Z interpretation table now carries an executing-code
   precondition (sha changed + POST values in bodies).
5. **L-C verdicts filed 031222Z, validated + recorded @22aae247ef.** Item 2 SPLIT: FAIL-as-emitted
   (wrong code channel, not a code regression) / PASS-on-landed-code — instrumented run of the
   deployed-channel bytes (S3-synced, cmp==pinned, import path asserted) emits the POST oracles:
   custody 209,373,343.50 / model_aua 145,329,103.38 at true label 2026-08-07, sv overall==frontier,
   lag=0 truthful, orion named gap at TRUE label 08-05 (pinned old code says 08-06 — a one-line
   executing-code discriminator handed to AE for post-L-D confirmation). Item 3 CLOSED — PASS on two
   legs: instrumented boto3 trace, DENOMINATOR 987 S3 read calls, smartx keys touched = 0, distinct
   targets exactly eclipse/orion inflection silver + inflection's own account_distribution.json;
   Lambda invocation log corroborates (139 events materialised 025741-025956Z, 0 smartx mentions,
   positive control present — log names its eclipse/orion/opal-data-assets legs; leg-grain only,
   corroboration not proof). Pre-registered readings observed as expected (feeders 0 partitions for
   08-11 = frozen separate WS-lambda mechanism; ROW11 frontier-stamp STALE = known uncovered
   sibling; cottonwood VALUE_DATE collision + honest global-fold skip = AE's thread).

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pipescript deployed | `comp-pipescript deployed <script>` (flagless) | REFUSED rc=2 | correct behavior — flagless refused per 07-30 hardening; re-ran with flag |
| comp-pipescript deployed | `comp-pipescript deployed dim_mdpf_aggregate_aua_timeseries.py --pipeline mdpf` (+ spine) | PASS | MATCH both files, 0 STALE; no R-33 CRLF false-STALE encountered; phase-3 evidence for L-A close |
| comp-estate | `comp-estate mdpf` | PARTIAL | gave the runner-channel chain map (trigger->SSM->EC2) but census vintage predates the window by construction — could NOT see the Scheduler floor; live aws (rail-checked) closed it |

**What worked:** printed-denominator discipline caught a broken diff verdict (error-counting "0")
before it became a false no-op call on L-A; the three-derivation grounding made the wrong-channel
finding immediately actionable (COO validated same turn); the instrumented-trace harness recovered
intact from the dead session's scratchpad and re-based onto S3-synced deployed bytes cleanly.
**What failed:** aws s3 cp with a /cygdrive destination path wrote to a phantom relative path
(shim arg-layer class); comp-estate/graph structurally cannot adjudicate a just-applied change
(known, worked as designed — live primitives used per Rule 22a).
**Gap found:** deploy-verify has NO instrument tying a baked-Lambda pin to the script-store channel
it shadows — comp-pipescript deployed reads GREEN while the executing zip is stale; surfaced to CTO
(030927Z) for instrument-roster routing. Also: EventBridge Scheduler schedules are invisible to
`events list-rules` — a floor census keyed on rules alone under-counts triggers.

## Briefs Written (DS)

None this window — evidence delivered via MCP messages (030919Z escalation, 031222Z verdicts) and
this log; QA artifacts deliberately machine-local per the L-C fence (never committed, never
production evidence).

## MCP Traffic

~13 handled. Significant: COO L-A GO (014749Z, executed) · MSTR crash-recovery direct (024442Z) ·
COO frame confirmation (025008Z) · L-A LANDED evidence out to COO+CTO (025326/025331Z) · COO L-A
CLOSE @13a4cecce8 (025556Z) · AE L-C fire (030059Z) · WINDOW-EXISTENTIAL out to COO+CTO+AE
(030919-030934Z) · COO L-D ruling @6dc47fc83a (031206Z) · L-C verdicts out x3 (031222-031235Z) ·
COO verdict close @22aae247ef (031344Z).

## Blockers

None. (Waiting on [0.7.0_AE_CloudOps] L-D is a sequenced handoff, not a blocker.)

## Current State (zero-prior-context handoff)

- **Window:** org/critical_paths/change_management/20260811T0150Z_mdpf-atomic-window.md — L-A CLOSED
  @13a4cecce8, L-B closed pre-crash, L-C item 3 CLOSED / item 2 recorded split @22aae247ef, L-D
  (mdpf-gold-lambda re-pin to @bf74d031c1 + safe-apply) OPEN at [0.7.0_AE_CloudOps].
- **Served code state:** s3://opal-data-mdpf/code/scripts/gold/{dim_mdpf_aggregate_aua_timeseries,
  build_mdpf_spine}.py == @bf74d031c1 byte-identical (ETags e7b169a7... / 6ebc6a82...).
  mdpf-gold-lambda still executes the @0bc739e7d5 pin until L-D lands.
- **The bar:** 13:30Z unattended cycle (mdpf-scheduled-floor -> mdpf-gold-lambda), with the new
  executing-code precondition: Lambda CodeSha256 changed from
  XuLlClWT6kr6n5TCG7keFmzVd8KEafMuAIQutJB+utQ= AND POST values in bodies.
- **Item-2 re-read oracle (ledger-recorded):** custody 209,373,343.50 / model_aua 145,329,103.38 at
  label 2026-08-07; D-4 anchor 209,431,383.43 at label 2026-08-04; orion named gap at 2026-08-05.
- **Harness (this session's scratchpad, lc_harness/):** lc_traced_inflection.py imports from
  deployed_gold/ (S3 sync, cmp==pinned) + repo lib/ for the calendar authority; baseline artifact
  lc_inflection_standalone_traced.json.
- **Session infra:** Monitor task bcnfwc95f live; PID 16056; serial file
  org/mcp/sessions/3c32414f-44fe-49c5-9875-a0548f7ae337.serial.

## Next Steps

1. On [0.7.0_AE_CloudOps] L-D completion + re-fired fenced qa_local cycle: single item-2 re-read
   against the POST oracle above (item 3 needs NO re-confirm — COO-narrowed scope). Report to
   [2.0.0_SA_COO] + [1.0.0_SA_CTO] + [0.7.0_AE_CloudOps].
2. [2.0.0_SA_COO] adjudicates the 13:30Z bar (12/12 A4, served meta advancing, executing-code
   precondition).
3. Carry-forward (pre-existing, banked pre-window): uncovered run-date siblings
   (dim_mdpf_account_distribution.py + wsc feeder — ROW11 symptom); cottonwood VALUE_DATE collision
   thread; eclipse_id=31 crosswalk review.
