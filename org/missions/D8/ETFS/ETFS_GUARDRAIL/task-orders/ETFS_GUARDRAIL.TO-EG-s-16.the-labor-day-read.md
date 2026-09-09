# TO ETFS_GUARDRAIL.TO-EG-s-16 -- THE LEGITIMATELY-EMPTY DAY THAT HAS ALREADY HAPPENED: 2026-09-07 (Labor Day, US market shut) read on EG-s-15's September run as class A -- no hole, no slice, no write

<to_id>ETFS_GUARDRAIL.TO-EG-s-16</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- issued in round 2's ONE issuance on PRD v0.4 @`a830ea1cc0` (the manual-trigger addendum on Andrew's ~21:4xZ word), s.9 row S16; decomposition v0.2 s.8-s.11. THIRD on slot ~1, after EG-s-15 is terminal: this order READS that run and runs nothing.</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.4 (s.9 row S16; s.4 property 4 -- class B is not a hole; s.7.2 S4 the classifier) | **Decomp cell:** `EG-s-16` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md` v0.2, s.8-s.11) | **outcome_ref:** FWD-4 | **verb:** verify | **depends_on:** `EG-s-15`

---

## THE CELL

`EG-s-16` (PRD s.9 S16): FWD-4 (a legitimately-empty day is classified A, not a hole, and nothing is backfilled against it) graded NOT_EVALUATED only because every prior class-A proof was a FIXTURE. 2026-09-07 is a REAL closed-market day (Labor Day) inside the month EG-s-15 ran on real data -- so the classifier's verdict for it is already on the served plane. This order reads it and writes nothing.

## DELIVERABLE

`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/test_egs16_labor_day.py` (the battery) and `the-labor-day-read.result.md` (criteria verbatim with rc and denominator), plus the proof-of-spec instance (below).

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry** -- your own `deliverables/<serial>/` folder and THIS ORDER'S OWN FILE for the `<status>` flip. A path you need that it does not name is a BLOCKING row, never an override.
- **READ-ONLY on the plane.** No invoke, no write, no deploy. Every S3 read via `s3api` in UTC; every list with its denominator.
- **YOUR AWS IDENTITY IS THE LAUNCHING SEAT'S** (decomposition s.3 decision 1); outputs recorded VERBATIM.
- **EVERY invocation is bounded.** `timeout 120`.
- **Scratch:** `<your worktree>/.scratch/` only.
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W1-S<k>`.
- **NEVER `git push`.** Report push state as MEASURED.

## ACCEPTANCE

<criterion id="S16-AC1" cell_refs="EG-s-16"><invocation>timeout 300 python org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/test_egs16_labor_day.py</invocation><expect>EGS16-LABOR-DAY-CLASS-A</expect></criterion>
`S16-AC1` -- a battery you write, printing the token ONLY when every arm holds on EG-s-15's real run: (a) `lib/trading_calendar.py` says 2026-09-07 is NOT a trading day (print the call and its answer; positive control: 2026-09-08 IS); (b) `platinum/reports/2026-09/coverage_verdict.json` (the object EG-s-15's run wrote; its UTC printed) classifies 2026-09-07 as class A (market closed) for EVERY partner it covers, and 2026-09-07 appears in NO partner's `holes`; (c) `expected_empty` (or the verdict's equivalent field, named) carries 2026-09-07 with the partners' hole counts UNAFFECTED by it (print the hole list with and without the date -- equal); (d) NO daily slice exists for 2026-09-07 for cottonwood or 49financial: `list-objects-v2` on `daily/<partner>/` filtered to the date, 0 keys, with the prefix's total key count as the denominator, beside a positive control (2026-09-08's slice, if present, or the nearest trading day's); (e) CloudTrail `PutObject` for any key containing `2026-09-07` under `daily/` over EG-s-15's run window == 0, denominator printed (the events scanned); (f) the run this reads is EG-s-15's (the request id from that order's record cited; the verdict object's UTC inside that run's window). Denominators on every list.

<criterion id="S16-AC2" cell_refs="EG-s-16" judgment="true"/>
`S16-AC2` -- graded by the CVO at L9: that a real closed-market day was told apart from a hole by the deployed classifier on real data (the A/B/C/D verdicts across the month printed as a table with the calendar beside them), that no backfill was attempted against it, and where the fixture-based proofs of round 1 would have been blind. Evidence with vintage. NO VERDICT.

<expected_criteria>S16-AC1, S16-AC2</expected_criteria>

<paths>
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>
No code path and no ledger path is granted: this order reads and records. `lib/trading_calendar.py` and `data/etfs/scripts/coverage/classifier.py` are READ (import the calendar for the battery's own check; never edit).

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.2, cell `EG-s-16`.
<owned_cells>EG-s-16</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-09 ~22:2xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 56.25 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names ETFS_GUARDRAIL or opal-data-etfs. BLIND SPOT: none that bears -- a read-only cell.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only; the launching seat's identity.
comp-adversary: DECLARED-NOT-APPLICABLE -- a verify cell over another order's run; the controls are the calendar and the positive-control date.
lane: the `<paths>` block above IS the grant (RULING 1 @`9ef9a40aae`) plus the two tree-convention grants.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: `S16-AC1`, `S16-AC2`. Instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-16.the-labor-day-read.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), validated with `python .tools/proof-of-spec-check.py <instance> S16-AC1,S16-AC2` BEFORE the complete flip, which you commit yourself. A `complete` flip WITHDRAWS YOUR OWN GRANT: flip only when S16-AC1 PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
