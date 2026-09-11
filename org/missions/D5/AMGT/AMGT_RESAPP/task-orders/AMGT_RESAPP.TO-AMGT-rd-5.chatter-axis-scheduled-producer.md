# AMGT_RESAPP.TO-AMGT-rd-5 -- THE CHATTER AXIS WRITER: a SCHEDULED PRODUCER computing the 30-day, 0-100 normalized, TOP_N=10 chatter ranking and writing PRE-COMPUTED rows to `opal-amgt-security-metrics`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rd-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~2</issued_to>

## THE CELL, INLINED IN FULL (round 5/v5, row S16, FWD-15)

```
AMGT-rd-5. THE CHATTER AXIS WRITER. A SCHEDULED PRODUCER that computes the chatter ranking daily and
writes PRE-COMPUTED per-ticker rows into `opal-amgt-security-metrics`.

THE AXIS IS ALREADY DEFINED AND IS NOT YOURS TO CHOOSE: the committed chatter gate -- a 30-DAY window,
0-100 NORMALIZED, TOP_N=10. Andrew unified chatter and price to a 30-day window; do not widen, narrow or
re-tune it, and do not invent a new scoring threshold. The PRD is explicit that no qualification
threshold exists anywhere upstream in this project and none may be invented at L5 or L7.

IT IS A PRODUCER, NOT A MONITOR, AND THE DISTINCTION IS LOAD-BEARING. A standing moratorium forbids
building an alert, alarm, SNS topic, SES send, freshness checker or monitor unless Andrew explicitly asks.
A scheduled job that COMPUTES A RANKING and WRITES IT is a production pipeline, which is not merely
permitted but REQUIRED to be scheduled ("production pipelines MUST be scheduled; success-of-upstream as
the only trigger is a defect"). What you may NOT add is anything that WATCHES the output and tells someone
about it.

THE READ SIDE IS NOT YOURS. `AMGT-rd-8` (the Lead Panel) reads these rows. You write them. Do not build a
route, a component or a client-side sort.

WHAT TO PRODUCE, under lib/research/ + .../deliverables/0.9.0_WK_AMGT_RESAPP~2/:

  (a) THE PRODUCER  computing the chatter score per ticker over a 30-day window, normalized 0-100, and
      writing the TOP_N=10 ranked set as PRE-COMPUTED rows into `opal-amgt-security-metrics` under the key
      schema AMGT-rd-2 landed.

  (b) THE SCHEDULE  a real schedule, not success-of-upstream as the only trigger. An ad-hoc run is
      permitted for QA and its artifacts are NEVER production evidence.

  (c) THE WINDOW RECORD  a deliverable stating the window, the normalization and TOP_N you implemented,
      each cited to the committed chatter gate rather than chosen here.
```

## DEPENDENCIES

**DEPENDS ON `AMGT-rd-2` (the metrics store).** You write into the table and key schema that cell landed.
Worked SECOND in slot ~2's queue, after `AMGT-rd-2`; your worktree is cut from the HEAD carrying it.
Independent of `AMGT-rd-6` and `AMGT-rd-7` -- they share your root, not your work.

## BOUNDS

```
BLOCK THE AXIS IS GIVEN: 30-day window, 0-100 normalized, TOP_N=10, from the committed chatter gate. Do
  not re-tune it and do not invent a threshold.
BLOCK PRODUCER, NOT MONITOR. No alert, alarm, SNS, SES send, freshness checker or monitor on the output.
  Standing moratorium; a finding lands as a gate or an owned blocking item, never as a watcher.
BLOCK SCHEDULED. Production pipelines MUST be scheduled; success-of-upstream as the ONLY trigger is a
  defect. Ad-hoc runs are QA only and are never production evidence.
BLOCK PRE-COMPUTED ONLY. Write ranking OUTPUTS. Never leave the ranking to be derived at render time --
  that is `C-SERVER-SIDE-RANKING` and AMGT-rd-8 depends on it holding.
BLOCK DO NOT BUILD THE READ SIDE. No route, no component, no client-side sort.
BLOCK NO non-ASCII in code, logs or AWS.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
PRD s.3b C-SERVER-SIDE-RANKING (Andrew-direct 2026-09-11 ~12:1xZ): "Trending/Breakout/Price/Chatter are
    computed SERVER-SIDE by daily jobs and written as pre-computed per-ticker rows into a SEPARATE metrics
    table ... The Lead Panel READS them and never re-derives a ranking at render time. Chatter axis = the
    committed chatter gate (30-day, 0-100 normalized, TOP_N=10)."
comp-schedule --drift (at the cut): 5 of 5 carriers scanned; carrier C3 = 12 STANDING NEVER CLAUSES, one
    of which is the no-alert/no-monitor moratorium bounded above. This is the finding that most directly
    shapes this cell: it is why the job is a producer and why nothing may watch its output.
comp-cache collisions (at the cut): 415 of 415 portal files; no AMGT key namespace exists yet. Not your
    surface -- named so you know the read side is genuinely unbuilt and you must not build it.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
lib/research/
infra/aws/terraform/amgt-resapp/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-5.chatter-axis-scheduled-producer.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~2/`. A path missing from that block is a path you
are REFUSED on. Refuse a criterion you cannot satisfy as written and report it; file a surprise ROW
(`AMGT_RESAPP-Z-W2-S<k>` continuing your prior sequence) and STOP on that criterion if you need a surface
not listed. MINT THE ROW ID FROM A RE-READ of the channel file, never from recall.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rd-5"><invocation>timeout 110 python -m pytest lib/research -q -k "chatter" 2>&amp;1 | tail -3</invocation><expect>a summary line with a passed count and no "failed" -- including a test asserting the window is 30 DAYS, the scale is 0-100, and TOP_N is 10, each read from the committed chatter gate rather than a literal re-declared in this cell. A suite that does not pin all three is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rd-5"><invocation>timeout 110 .tools/aws dynamodb scan --table-name opal-amgt-security-metrics --max-items 12 --output text 2>&amp;1 | tail -10</invocation><expect>pre-computed chatter rows present -- at most TOP_N=10 ranked entries for the chatter axis, each carrying a ticker and a score in the 0-100 range. An empty table means the producer never ran and is NOT met; more than 10 chatter entries for one as-of date breaks TOP_N and is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rd-5"><invocation>timeout 110 comp-find "sns|publish_alert|send_email|freshness_check|cloudwatch_alarm" lib/research infra/aws/terraform/amgt-resapp --limit 20 2>&amp;1 | tail -10</invocation><expect>a printed denominator with ZERO hits in this cell's own new code -- NEGATIVE: the producer adds no alert, SNS topic, email send, freshness checker or alarm. Any hit inside code this cell authored violates the standing moratorium and is NOT met. A denominator of 0 files scanned is OUT-OF-CORPUS, not a zero, and is NOT met either</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rd-5" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical): the three axis parameters are pinned to the committed gate, not re-invented.
- **AC2** (mechanical, LIVE plane): real pre-computed rows landed, respecting TOP_N.
- **AC3** (mechanical, NEGATIVE, denominator-bearing): no monitor/alert snuck in alongside the producer.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names `3.0.0_SA_CVO~Z`): is this genuinely a SCHEDULED PRODUCER rather than a monitor wearing a producer's name, is it triggered by a real schedule rather than success-of-upstream alone, and does it write ranking OUTPUTS such that the Lead Panel can read without re-deriving?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>5</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.6.1 + L6 round 5) - **Project:** AMGT_RESAPP - **PRD:** v0.4 @6c52a4e380 (L4-R ADMITTED)
**Authority chain:** L10 round-4 analysis @959ba3e947 -> PRD s.3b `C-SERVER-SIDE-RANKING`, ANDREW-DIRECT 2026-09-11 ~12:1xZ -> L5 decomposition v0.6.1 @d0efe81ca8 (section 13, AMGT-rd-5) -> this round-5 issuance.
**Chain:** round 5 (v5), CHAIN B, slot ~2. Handed after `AMGT-rd-2` lands. Independent of `AMGT-rd-6` and `AMGT-rd-7`, which share its root.
**Provenance:** decomposition v0.6.1 section 13b's `AMGT-rd-5` row.
> **NOTE (2.0.0_SA_COO~ZZZ).** The producer/monitor line is the one a well-meaning worker crosses. "It would be useful to alert when the ranking goes stale" is exactly the thought the moratorium exists to stop, so AC3 is a negative control on this cell's OWN code rather than a general sweep.
<preflight>
comp-schedule: RUN -- 5 of 5 carriers; C3 = 12 standing NEVER clauses, the direct source of this cell's producer-not-monitor bound. BLIND: C4/C5 not decidable.
comp-iam: RUN -- 836 call(s) across 96 mapped role(s); the producer's write rides a role and a refused PutItem is a finding filed as a row. BLIND: 630 UNRESOLVABLE-RESOURCE, 266 calls in 26 role-UNMAPPED services never checked, 51 GRANTED-BROAD excluded not cleared.
comp-cache: RUN -- 415 of 415 portal files; no AMGT key namespace, so the read side is genuinely unbuilt and is NOT this cell's. BLIND: declared keys only.
comp-adversary: RUN -- 1 artifact declared (decomposition v0.6.1 @d0efe81ca8). BLIND: author's stated evidence context only.
comp-blast: DECLARED-NOT-APPLICABLE -- writes this project's own new table; no shared served artifact moves.
</preflight>
**Preflight disposition:** a scheduled producer against a landed store, with the standing no-monitor moratorium as its sharpest bound and a negative control asserting it.
