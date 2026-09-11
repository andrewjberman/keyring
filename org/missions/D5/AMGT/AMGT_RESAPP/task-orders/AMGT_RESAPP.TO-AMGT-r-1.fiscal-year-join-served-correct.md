# AMGT_RESAPP.TO-AMGT-r-1 -- THE FISCAL-YEAR JOIN, SERVED-CORRECT: a non-December filer's period-end fundamentals pair with the price AT that period-end, proven by a control that FAILS under calendar-year grouping

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-r-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~1</issued_to>

## THE CELL, INLINED IN FULL (round 2, FWD-1/FWD-3; fixes AMGT-s-1 / row W1-S2)

```
AMGT-r-1. THE FISCAL-YEAR JOIN, SERVED-CORRECT. Round 1's join grouped by the CALENDAR year of the
`date` field (date[:4]); that satisfied AMGT-s-1's mechanical AC4 (10 labels, 0 unmerged rows) but for
a NON-DECEMBER filer it pairs each fiscal year's period-end fundamentals with a calendar-year price
~9 months off. Measured on BABA US Equity (fiscal year end 31 March): 100% of its rows split
period-end (March) fundamentals from calendar-year prices (W1-S2). This is a SERVED-CORRECTNESS defect
FWD-1/FWD-3 lean on -- "an analyst can defend every number" fails if the price beside a fundamental is
9 months adrift -- and a December-heavy sample cannot see it.

WHAT TO PRODUCE, under integrations/bloomberg/research/ and .../deliverables/0.9.0_WK_AMGT_RESAPP~1/:

  (a) THE FIX  in the model-block join (integrations/bloomberg/research/model_block_pull.py's join, or a
      join module beside it): re-key the fiscal-year join to the ISSUER'S OWN FISCAL PERIOD, so a
      fundamental reported as of the true period end is paired with the price AT (or nearest on/before)
      that period-end date -- never the calendar-year price. The issuer's fiscal-year-end month is read
      from the record (Bloomberg's fiscal-period fields the CRO mapped), never assumed December.

  (b) THE CONTROL, THE DIFFERENCE ARM  a test on BABA US Equity (FYE 31 March), whose block AMGT-s-1
      ALREADY landed (no new unique security): the join under CALENDAR-YEAR grouping mispairs (a
      fundamental's price is ~9 months from its period end) and FAILS a same-period-alignment assertion;
      the SAME data under FISCAL-PERIOD grouping PASSES it. The control that fails-then-passes is the
      whole point -- a control that only passes proves nothing.

  (c) THE READBACK  a check_join_fye.py that, per security AMGT-s-1 landed, prints one line: the max
      gap in days between any fiscal-year fundamental's period-end and its paired price, under the
      fiscal-period join. For a correct join every gap is small; a ~270-day gap is the defect.
```

## DEPENDENCIES

**NONE.** Independent of the other round-2 cells. Reads AMGT-s-1's landed blocks
(deliverables/0.9.0_WK_AMGT_RESAPP~1/model_block_*.json) and, if a re-pull of BABA's history is needed,
re-touches ONLY that existing key.

## BOUNDS

```
⛔ F2 / G-24: NO NEW UNIQUE SECURITY. BABA US Equity is already landed; re-read its block or re-pull the
same key. A fourth security is a widening (AC3).
⛔ integrations/bloomberg/READ_HERE.md binds if you re-pull: health first, NEVER a sign-in; a signed-out
terminal records the limitation and the control runs on the LANDED block instead.
⛔ C-FISCAL-YEAR-JOIN: fiscal year is the join key, read from the issuer's own fiscal period, never the
calendar year and never assumed December.
⛔ THE CONTROL MUST DISCRIMINATE: it fails under the old grouping and passes under the new. An
always-pass control does not meet AC1 (run the EXACT invocation against the world).
⚠ Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
W1-S2 (round 1, the surfacing row): BABA (FYE 31 March), 100% of raw rows split period-end fundamentals
    from calendar-year prices; calendar-year grouping passed AMGT-s-1 AC4 mechanically but is not the
    issuer's fiscal period.
L10 analysis @4d31cf4caa s.2 (FWD-1): "a served-correctness defect, not a render"; s.4: "a control on a
    NON-December filer; the join always succeeds and a December-heavy sample cannot see it".
AMGT-s-1's field map (landed): the fiscal-period fields are among the mapped header scalars; read the FYE
    month from the record, not from a constant.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
integrations/bloomberg/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-r-1.fiscal-year-join-served-correct.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~1/`. AMGT-s-1's deliverables and the store are READ.
A path missing from that block is a path you are REFUSED on. You cannot ask for one to be added.
⛔ REFUSE a criterion you cannot satisfy as written and report the refusal with its measurement; never
repair, widen, or satisfy it by a route this order did not name. If you need a surface not listed, file a
surprise ROW in the investigation file above and STOP on that criterion. Your surprise row id is
`AMGT_RESAPP-Z-W1-S<k>` continuing your prior sequence, `"project": "AMGT_RESAPP"`, `"fabric": "site-z"`.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-r-1"><invocation>python -m pytest integrations/bloomberg/research/tests/test_fye_join.py -q 2>&amp;1 | tail -1</invocation><expect>a summary line beginning "2 passed" with no "failed" -- on BABA's landed data: (1) the CALENDAR-YEAR grouping control mispairs a period-end fundamental with a price ~9 months off and FAILS the same-period-alignment assertion (the defect, demonstrated); (2) the FISCAL-PERIOD grouping PASSES it (the fix, the difference arm). Fewer than 2, or a control that does not fail under calendar-year grouping, is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-r-1"><invocation>python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/check_join_fye.py</invocation><expect>a line per landed security ending "max fundamental-to-price gap N days" with N under 45 for EVERY security including BABA (the fiscal-period join aligns the price to the period end); any security with a gap above 180 days is the calendar-year defect and is NOT met -- read from the served block, not the pull log</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-r-1"><invocation>python -c "import json; l=json.load(open('org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~1/pull_log.json')); print('unique securities requested', len(set(l['securities'])))"</invocation><expect>"unique securities requested" of 3 or fewer -- NEGATIVE: the fix and its control re-used BABA and added no new unique security (F2)</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-r-1" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, the difference arm): the join is correct on a non-December filer and the calendar-year grouping is shown to be wrong on the same data.
- **AC2** (mechanical, read from the served block): every fundamental sits beside a price at its own period end.
- **AC3** (mechanical, NEGATIVE): no new security.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names 3.0.0_SA_CVO~Z): pick one BABA fiscal year -- is the price beside its fundamentals the one an analyst would defend as "as of that period end", and would the same join be correct for a December filer (the fix is general, not a BABA special case)?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>complete</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.3 + L6 round 2) - **Project:** AMGT_RESAPP - **PRD:** v0.3 @f68818832b
**Authority chain:** L10 round-1 analysis @4d31cf4caa (1.0.0_SA_CTO~Z, the CTO's one send) -> L5 recut decomposition v0.3 @3d2d7af6e0 (section 10, AMGT-r-1) -> this round-2 issuance.
**Chain:** round 2, an independent chain of one (fanout 5 of 5, cap 8).
**Provenance:** the cell text is the decomposition v0.3 section 10a row for AMGT-r-1, verbatim; the defect is W1-S2 and the L10 analysis s.2/s.4.
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- v0.2's run stands (25 armed, none this project's; G-24/F2 bind this cell); no round-2 cell touches a new gate surface.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM touched (a join fix over landed/re-pulled data).
comp-adversary: DECLARED-NOT-APPLICABLE -- the L10 analysis @4d31cf4caa is the recut's authority, cited above; the round-1 comp-adversary (10/10) stands at its vintage.
comp-blast: DECLARED-NOT-APPLICABLE -- no infra act, no served-output move.
</preflight>
**Preflight disposition:** a recut cell over landed Bloomberg data; the battery is not re-run because the surface (integrations/bloomberg/research/, the store) is the round-1 surface and no new gate/IAM/adversary plane is touched. The authority is the L10 analysis.
