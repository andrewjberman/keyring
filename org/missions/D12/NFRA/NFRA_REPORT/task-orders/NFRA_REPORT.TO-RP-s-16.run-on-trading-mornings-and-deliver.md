# NFRA_REPORT.TO-RP-s-16 -- RUN it on trading mornings and DELIVER before Andrew's morning

<!-- ============ WORKER FACE -- this is the WHOLE of the worker's context ============ -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md</decomp_doc>
<owned_cells>RP-s-16</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_REPORT~1</issued_to>

## THE CELL, INLINED IN FULL (manifest row S3; outcome FWD-1; acceptance property 1)

```
RP-s-16 mirrors manifest row S3, verb `align`. ACT: the composer runs on TRADING DAYS ONLY and
its edition is delivered before Andrew's morning.
MEASURED STARTING STATE (brief F2): the detectors are weekday-aware and NOT trading-day-aware. IT SENT
ON LABOR DAY, 2026-09-07.
```

## DEPENDENCIES

This cell depends on: RP-s-15.
A dependency is keyed to OBSERVED COMPLETION -- a deliverable that exists and whose criteria passed -- never to a status word and never to a merge.

## BOUNDS -- what this cell may not cross

```
C-TRADING-DAYS and CLAUDE.md NEVER#4: never call a pipeline stale until the trading calendar
is resolved; Friday IS Monday's answer; there is ONE frontier. NEVER a calendar-day subtraction.
THE ALERTING MORATORIUM IS ARMED. This cell DELIVERS an existing report on a schedule. It mints NO
alarm, NO topic, NO subscription and NO notification. Repairing an existing non-delivering egress is
permitted; creating one is NOT.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
ROUND 1's SCHEDULE CELL ALREADY SETTLED THE FRONTIER AND YOU INHERIT IT RATHER THAN
RE-DERIVING IT: five files share the basename `trading_calendar.py`; three under infra/aws/lambda are
BYTE-IDENTICAL vendored deployment copies of the canonical source and the fifth is a test file excluded
on role. Name the frontier by a DERIVED repo-root anchor, never a hardcoded literal and never a bare
basename -- CLAUDE.md forbids device-specific hardcoding and a worktree path is worker-specific.
comp-schedule gate G-7 remains a DRIFT CANDIDATE on that basename; it is POD4's and not this cell's.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
org/missions/D12/NFRA/NFRA_REPORT/deliverables/
org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md
org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md
org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_NFRA_REPORT_ROUND1_20260910.md
org/missions/D12/NFRA/NFRA_REPORT/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_REPORT/task-orders/NFRA_REPORT.TO-RP-s-16.run-on-trading-mornings-and-deliver.md
</paths>

A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
If you need a surface that is not listed, file a surprise ROW in the investigation file above and STOP on that criterion.

Your deliverable is `org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/RUN_AND_DELIVERY.md`.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="RP-s-16"><invocation>grep -c -E '[a-z_/]+/lib/trading_calendar\.py' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/RUN_AND_DELIVERY.md</invocation><expect>a count of 1 or greater</expect></criterion>
  <criterion id="AC2" cell_refs="RP-s-16"><invocation>grep -c -i -E 'labor day|holiday' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/RUN_AND_DELIVERY.md</invocation><expect>a count of 1 or greater</expect></criterion>
  <criterion id="AC3" cell_refs="RP-s-16"><invocation>grep -c -i -E 'create-topic|put-metric-alarm|subscribe --' org/missions/D12/NFRA/NFRA_REPORT/deliverables/0.9.0_WK_NFRA_REPORT~1/RUN_AND_DELIVERY.md</invocation><expect>a count of 0 -- grep -c exits rc=1 on zero and THAT IS THE PASS; score the OUTPUT, not the exit code</expect></criterion>
</proof_of_spec>

### What each criterion means

- **AC1** (mechanical): the schedule keys on the trading-day frontier by a resolved path
- **AC2** (mechanical): market holidays are excluded, with Labor Day named as the measured failure
- **AC3** (mechanical): no new alerting was minted -- the moratorium limb, an ABSENCE test

Every invocation runs under `timeout 120`; a timeout is recorded AS the output, so keep every invocation bounded.

⚠ THE MECHANICAL CRITERIA ABOVE ARE MOSTLY WORD-PRESENCE GREPS AND THEY ARE THE FLOOR, NOT THE BAR.
Three of round 1's twelve orders carried a criterion that could not test what it was written to test --
an under-cut cell, a wrong interpreter, and an OR-alternation counted by line. The cell's ACT is the bar.
If a criterion passes on a deliverable that does not do the ACT, say so in your report rather than
letting the grep stand in for the work.

<!-- ============ RECORD FACE -- does NOT travel to the worker ============ -->

<status>complete</status>
<round>2</round>
<sub_round>B</sub_round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>

<preflight>
comp-schedule: RUN -- re-run at the round-2 cut, 5 of 5 carriers; denominators C1=23 C2=7 C3=12 C4=20 C5=335; 2 gates ARMED (G-3 CTO, G-7 POD4), NEITHER this project's.
comp-iam: RUN -- re-run at the round-2 cut; 12 missing, 291 deny-present, 1 coverage-unknown, 2 resource-mismatch across 31 services; BLIND on wafv2, the plane C-SENTINEL-STATE lives on.
comp-adversary: RUN -- on the round-2 decomposition; 1 of 1 cited commit VERIFIED, 1 of 1 cited path stable, 0 file:line cites; BLIND on the decomposition neighborhood (T11 NOT RESOLVED -- a DECOMP carries no decomp_ref), so its packet digested 12 of 420 filesystem siblings and is NOT evidence about these cells; class census S1/S2/S3 all 0 of 420, which is itself the clean signal.
</preflight>

**Issuer:** `2.0.0_SA_COO~ZZ` (L6, round 2) - **Project:** NFRA_REPORT - **Directive:** D12
**Authority chain:** round 1 CLOSED at L10 -> `1.0.0_SA_CTO~Z` round-N analysis @9dae635237 -> L5 recut `org/missions/D12/NFRA/NFRA_REPORT/decompositions/NFRA_REPORT_DECOMP_R2.md` -> this issuance.
