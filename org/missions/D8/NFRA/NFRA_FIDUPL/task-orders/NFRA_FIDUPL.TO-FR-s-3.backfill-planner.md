# TO NFRA_FIDUPL.TO-FR-s-3 -- the per-G backfill planner and stop detection

<to_id>NFRA_FIDUPL.TO-FR-s-3</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~4</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>fidelity-perg</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FR-s-3` (`decompositions/NFRA_FIDUPL_DECOMP_R2.md` v1.0) | **outcome_ref:** FWD-9, C-BACKFILL |
**depends_on:** none (built against fakes; interfaces in worker reference section 11)

---

## WORKER FACE

### THE CELL

**FR-s-3** -- The backfill per G: the backward window planner, stop detection with its named reasons, and the per-G per-kind record, against an injected `ExportClient` and `lander`. Contract row: C-BACKFILL (PRD v0.4.5: as far back as possible for every G number; name each stop).

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (sections 1 and 11 bind you; the rest is context) and the cell text above. Project NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning; round 2 splits it per firm by G number, backfills history per G number, and schedules it. You build against fakes; nothing here runs live.

### WHAT TO BUILD

Build `backfill.py` and `tests/test_backfill.py` to worker reference section 11 (the `backfill.py` bullet). The real export-request adapter is NOT built here (its calls are not yet captured); this cell is the planner, the stop logic and the record, against fakes.

1. `ExportClient` (an abstract base with the three methods), `EntitlementRefused` and `RetentionLimit` exceptions, `plan_windows(today, floor_date, chunk_days)` (an iterator of `(date_from, date_to)` going backward, newest first, non-overlapping, covering `today` back to `floor_date`), and `backfill_g(client, g, kinds, today, floor_date, lander, chunk_days=30, cap_years=20)`.
2. For each kind in turn, walk the windows newest first: `request_export`, `wait`, and on `COMPLETED` write the bytes into a local window directory and call `lander(window_dir, g, kind, date_from, date_to)`; record the window as served. Stop that kind at the first `EntitlementRefused` (stop reason `entitlement refusal`), `RetentionLimit` (`retention limit`), an `EMPTY` window whose end is older than `floor_date` (`account open date`), or when the walk passes `cap_years` (`cap`). A failure of the injected `lander` is recorded as the stop reason `lander failure` and stops that kind; nothing is retried.
3. Return a record per G: `{"kinds": {kind: {"windows_served": n, "earliest_date_served": "YYYY-MM-DD" or null, "stop_reason": ...}}}`. A G number is identified in any print, log or exception message only by its index in the run's list or `g#<n>`, never by value.
4. Tests (a fake client scripted per window, a fake lander): `test_windows_walk_backward_in_chunks`, `test_stops_on_entitlement_refusal_and_names_it`, `test_stops_on_retention_limit_and_names_it`, `test_stops_at_account_open_date`, `test_record_names_earliest_date_per_g_and_kind`, `test_never_prints_g_numbers` (capture stdout, stderr and logging; assert the made-up G value is absent), `test_calls_injected_lander_per_window`.

### ACCEPTANCE

<criterion id="FR3-AC1" cell_refs="FR-s-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fr3</invocation><expect>R1-FR3-OK passed=\d+</expect></criterion>
`FR3-AC1` -- the seven named backfill tests exist and pass.

<expected_criteria>FR3-AC1</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FR3-AC1` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Every test uses SYNTHETIC data and fakes; no network, no AWS, no live call. G numbers and account numbers in tests are made up and are never real ones.
- **No secret, no alert; no G number, account number or firm label in any output.** Counts and booleans only (reference section 11).
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, `<n>` your slot, `<k>` next unused across the investigation file) and stop that piece. A premise that fails is a row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).

Reads (outside the grant):
- `org/missions/D8/NFRA/NFRA_FIDUPL/prd/NFRA_FIDUPL_PRD.md` (the C-BACKFILL row)

<paths>
infra/aws/ec2/canonical-fidelity/backfill.py
infra/aws/ec2/canonical-fidelity/tests/test_backfill.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R2.md</decomp_doc> (round 2), cell `FR-s-3`.
<owned_cells>FR-s-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FR3-AC1. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~4/NFRA_FIDUPL.TO-FR-s-3.backfill-planner.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FR3-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- fakes only; denominator 0 IAM statements changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- build round on fakes; runs when the live round touches this surface.
lane: the paths block.
</preflight>

Source: CTO msg 8663 (PRD v0.4.5 @e4bb46835e); Andrew-direct @b329e1c5f3; decomposition round 2 cell FR-s-3; worker reference section 11.
