# TO ETFS_GUARDRAIL.TO-EG-s-10 -- the trading calendar: one library, three vendored copies, and which calendar each producer resolves

<to_id>ETFS_GUARDRAIL.TO-EG-s-10</to_id>
<project>ETFS_GUARDRAIL</project>
<issued_to>0.9.0_WK_ETFS_GUARDRAIL~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- proof-of-spec instance `org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-10.proof_of_spec.json` VALID (rc=0, `.tools/proof-of-spec-check.py`, re-confirmed at `de8693863c`); all 5 criteria S10-AC1..AC4 PASS by output, S10-AC5 judgment RECORDED for CVO L9 grading. Rows ETFS_GUARDRAIL-W1-S1 and ETFS_GUARDRAIL-W1-S2 filed and DISARMED by the issuer 2.0.0_SA_COO~B @`de8693863c`. Flip made by the assignee per the amended BOUNDS grant (task-orders/ own-file flip, tree convention). Prior: pending -- GO paired at cut (the spawn IS the GO). Authority: PRD v0.3 @`4e30d6b635` (flat lineage @`7aa1554881`, ON ORIGIN) RATIFIED; decomposition v0.1 @`c4ab429993`, v0.1.1 in this issuance; Andrew-direct at the 1.0.0_SA_CTO terminal 2026-09-04 ~17:0xZ (94224/94225).</status>

**Directive:** D8 | **Fabric:** laptop | **PRD:** `../prd/ETFS_GUARDRAIL_PRD.md` v0.3 (s.7.2 row S10; s.3 RELIES-ON; s.4 property 4) | **Decomp cell:** `EG-s-10` (`../decompositions/ETFS_GUARDRAIL_DECOMP.md`) | **outcome_ref:** none (a RELIES-ON row beneath FWD-1 and FWD-4) | **verb:** verify | **depends_on:** --

---

## THE CELL

`EG-s-10` (PRD s.7.2 S10): `lib/trading_calendar.py` (163 lines at HEAD) **+ 3 vendored copies** -- `infra/aws/lambda/bd-pipeline/bd-served-vintage-alarm/trading_calendar.py`, `infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/trading_calendar.py`, `infra/aws/lambda/opal-assets-absence-check/trading_calendar.py`; **neither target producer (`cot-etf-ownership-daily`, `bd-49f-etf-ownership-daily`) has one.** Bound: *"RELIES-ON, shared beneath S1/S2/S4. Rule 22 common-dependency limb. Which calendar each producer resolves is UNANSWERED."* CLAUDE.md NEVER: "count trading days ... One frontier: `lib/trading_calendar.py`".

This is a VERIFY cell. You change no code. You answer the question the PRD left open, with a census, so that the port cells (`EG-s-1`, `EG-s-2`) and the classifier (`EG-s-4`) -- all in this same queue or handed after you -- build on a measured calendar rather than an assumed one.

## DELIVERABLE

`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/the-trading-calendar-each-producer-resolves.result.md` -- the result document: (1) the sha256 of the library and each vendored copy, side by side, with DRIFT stated per copy (IDENTICAL / DIFFERS + the diff's line count); (2) the library's public API (`is_trading_day`, `prev_trading_day`, `trading_days_between`, `trading_days_mtd`, `total_trading_days_in_window`, `calendar_source`) with what `calendar_source()` prints; (3) the trading-day counts for 2026-07 and 2026-08 (the brief says 22 and 21); (4) for EACH of the three producers, the calendar it resolves at runtime TODAY (inf: its vendored copy; cot and 49F: NONE -- they resolve no calendar and take the newest partition) and the consequence for the reporting-obligation window; (5) your recommendation for the ports: vendor `lib/trading_calendar.py` byte-identical (sha256 recorded) into each producer's source dir and add it to the source map `files`, the same pattern `inf-etf-ownership-daily` already uses -- or a different mechanism, with the reason. Each criterion's invocation and its output verbatim with rc and denominator.

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9, and a PASS or FAIL written on one is INVALID.

<criterion id="S10-AC1" cell_refs="EG-s-10"><invocation>sha256sum lib/trading_calendar.py infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/trading_calendar.py infra/aws/lambda/bd-pipeline/bd-served-vintage-alarm/trading_calendar.py infra/aws/lambda/opal-assets-absence-check/trading_calendar.py</invocation><expect>lib/trading_calendar.py</expect></criterion>
`S10-AC1` -- the four-copy census RAN over all four paths (denominator 4 of 4); the drift verdict per copy goes in the result document.

<criterion id="S10-AC2" cell_refs="EG-s-10"><invocation>python -c "import sys; sys.path.insert(0,'lib'); import trading_calendar as t; print('SOURCE=%s AUG2026=%d JUL2026=%d' % (t.calendar_source(), len(t.trading_days_between('2026-08-01','2026-08-31')), len(t.trading_days_between('2026-07-01','2026-07-31'))))"</invocation><expect>AUG2026=21</expect></criterion>
`S10-AC2` -- the library counts August 2026 as 21 trading days (the brief's own number; the July count is recorded beside it).

<criterion id="S10-AC3" cell_refs="EG-s-10"><invocation>python -m pytest lib/tests/test_trading_calendar.py -q</invocation><expect>passed</expect></criterion>
`S10-AC3` -- the library's own battery is green at HEAD (record the N passed).

<criterion id="S10-AC4" cell_refs="EG-s-10"><invocation>python -c "import os; print('COT_HAS_CAL=%s BD49F_HAS_CAL=%s' % (os.path.exists('infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/trading_calendar.py'), os.path.exists('infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/trading_calendar.py')))"</invocation><expect>COT_HAS_CAL=False BD49F_HAS_CAL=False</expect></criterion>
`S10-AC4` -- the PRD's claim that neither target producer carries a calendar is TRUE at HEAD (if it is not, that is a premise that does not hold: a row, and the criterion's honest output).

<criterion id="S10-AC5" cell_refs="EG-s-10" judgment="true"/>
`S10-AC5` -- THE ANSWER, graded by the CVO at L9: which calendar each of the three producers resolves at runtime today, the drift between the library and each vendored copy, and the vendoring recommendation for the ports with its reason. RECORD it; NO VERDICT.

<expected_criteria>S10-AC1, S10-AC2, S10-AC3, S10-AC4, S10-AC5</expected_criteria>

## BOUNDS

- **Your write surface is the `<paths>` block below, PLUS the two grants the tree convention gives every worker without an entry -- your own `deliverables/<serial>/` folder, and THIS ORDER'S OWN FILE under `task-orders/` (lane ANY) for the `<status>` flip -- and nothing else.** (Restated by the issuer at the drain on row ETFS_GUARDRAIL-W1-S2: the flip was always admitted; the wording withheld it.) A path you need that it does not name is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override. This cell changes NO source file; your writes are your deliverables folder and, if a row is needed, the investigation file.
- **EVERY invocation is bounded.** Run each under `timeout 120`; a timeout is RECORDED AS THE OUTPUT.
- **Read, do not chase.** If a vendored copy DIFFERS from the library, record the diff's shape; do not reconcile it (that is another surface's owner).
- **A spec-vs-world divergence is a ROW** at `org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `ETFS_GUARDRAIL-W1-S<k>` (`W1` = your slot; `<k>` the next unused within your coordinate) -- append inside the fenced json array, cite `path@commit`, never edit an existing row, keep working. The schema is `org/surprise_channel/schemas/investigation_item.schema.json` (required: id, surfaced_by, surfaced_at, one_line, class, grounding, disposition; plus project, fabric, spec_asserts, world_is, hazard_standing with disarm_owner when ARMED).
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote origin refs/heads/CLOUD`).

<paths>
lib/trading_calendar.py
lib/tests/
infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/trading_calendar.py
infra/aws/lambda/bd-pipeline/bd-served-vintage-alarm/trading_calendar.py
infra/aws/lambda/opal-assets-absence-check/trading_calendar.py
org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/
org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ETFS/ETFS_GUARDRAIL/decompositions/ETFS_GUARDRAIL_DECOMP.md</decomp_doc> v0.1 @`c4ab429993` (v0.1.1 in this issuance), cell `EG-s-10`.
<owned_cells>EG-s-10</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at the issuance (2026-09-04 18:0xZ) -- WITHIN BUDGET, 5 of 5 carriers scanned, reached denominators C1=21 C2=4 C3=12 C4=20 C5=336; 0 armed gates name ETFS_GUARDRAIL, the two producers, the orchestrator or the renderer.
comp-iam: DECLARED-NOT-APPLICABLE -- a repo-surface VERIFY cell; no principal, policy or resource is read or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- a FRESH CUT with no prior artifact to validate against; the assignee's instrument at report time, not the issuer's at the cut.
lane: the `<paths>` block above IS the grant (RULING 1, Andrew 2026-09-04 ~04:58Z @`9ef9a40aae`) -- a worker serial is admitted to exactly these paths while this order is NON-TERMINAL at HEAD, and to its own deliverables folder by the tree convention.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S10-AC1`, `S10-AC2`, `S10-AC3`, `S10-AC4`, `S10-AC5`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D8/ETFS/ETFS_GUARDRAIL/deliverables/0.9.0_WK_ETFS_GUARDRAIL~1/ETFS_GUARDRAIL.TO-EG-s-10.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> S10-AC1,S10-AC2,S10-AC3,S10-AC4,S10-AC5` BEFORE the complete flip, which the assignee commits itself.
A `complete` flip WITHDRAWS YOUR OWN GRANT (the grant is read from a NON-TERMINAL order): flip only when every MECHANICAL criterion PASSES by output. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (serial / TO / branch / HEAD; BLOCKING; CRITERIA with each invocation and its deciding line; PROOF with rc; ROWS; COMMITS; NEXT). You cannot send or receive messages -- anything you would ask is a surprise row.
