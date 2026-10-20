# TO NFRA_FIDUPL.TO-FR-s-4 -- the daily orchestration: sign in, fetch, land, attribute, split, record

<to_id>NFRA_FIDUPL.TO-FR-s-4</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~5</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>fidelity-perg</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FR-s-4` (`decompositions/NFRA_FIDUPL_DECOMP_R2.md` v1.0) | **outcome_ref:** FWD-9, C-BACKFILL |
**depends_on:** none (built against fakes; interfaces in worker reference section 11)

---

## WORKER FACE

### THE CELL

**FR-s-4** -- The daily orchestration: `box/daily.py` runs sign in, fetch, land staged, attribute, split, record, and `box/run.py main()` chooses it from `config["mode"]`. Contract rows: C-TENANCY, C-WINDOW.

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (sections 1 and 11 bind you; the rest is context) and the cell text above. Project NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning; round 2 splits it per firm by G number, backfills history per G number, and schedules it. You build against fakes; nothing here runs live.

### WHAT TO BUILD

Build `box/daily.py`, the one hookup in `box/run.py` and `tests/test_box_daily.py` to worker reference sections 7, 9 and 11. Read `box/run.py` first: `run_once` is the pattern (config pointers, injected deps, the record always written, a non-zero exit on any failure). Do not change `run_once`'s behaviour; its tests (`tests/test_box_run.py`) must still pass.

1. `daily.py`: `run_daily(config, deps)`. Stages in order: `read_secret`, `open_session`, `fetch_day` (into the run directory), `land` (the staged day under `alongside`, exactly as `run_once`), then `attribute(handle, business_day)` (returns the attribution dict, which you write to the run directory as `attribution.json` with file mode 0600 and NEVER print), `split(handoff_dir, attribution, config)` (returns the split record), and a final run summary printed as counts only. Any stage failure: the land stage still ran or its failure still produced a record; the exit code is non-zero; a failure in `attribute` or `split` never hides a successful land (the land result is kept and the run is reported as partial).
2. `run.py`: add `ALLOWED_KEYS` entries `mode`, `firm_labels` and `account_columns` to `check_pointers` (pointers and non-secret maps; reject any value that looks like a secret as before), and one hookup in `main()`: if `config.get("mode") == "daily"` call `run_daily(config, _real_daily_deps(config))`, otherwise `run_once` as before. `_real_daily_deps` imports lazily `attribute`, `gswitch` and `split` (written by other cells in this round; they are not on your branch, so you may only reference their documented function names and prove the wiring with fakes; a missing module is a surprise row, not a stub).
3. Tests (fakes): in the new `tests/test_box_daily.py` `test_daily_sequence_signin_fetch_land_attribute_split_record`, `test_attribution_failure_still_records_and_exits_nonzero`, `test_split_failure_exits_nonzero_after_land`, `test_config_pointers_accept_firm_labels_and_account_columns`, `test_main_chooses_daily_mode_from_config`.

### ACCEPTANCE

<criterion id="FR4-AC1" cell_refs="FR-s-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fr4</invocation><expect>R1-FR4-OK passed=\d+</expect></criterion>
`FR4-AC1` -- the five named daily-orchestration tests exist and pass.

<criterion id="FR4-AC2" cell_refs="FR-s-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu5</invocation><expect>R1-FU5-OK passed=\d+</expect></criterion>
`FR4-AC2` -- the five round-1 box tests still pass (run_once is unchanged).

<expected_criteria>FR4-AC1,FR4-AC2</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FR4-AC1` base: FAIL as expected; `FR4-AC2` base: PASS as expected (a regression guard on round 1).

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Every test uses SYNTHETIC data and fakes; no network, no AWS, no live call. G numbers and account numbers in tests are made up and are never real ones.
- **No secret, no alert; no G number, account number or firm label in any output.** Counts and booleans only (reference section 11).
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, `<n>` your slot, `<k>` next unused across the investigation file) and stop that piece. A premise that fails is a row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).

Reads (outside the grant):
- `infra/aws/ec2/canonical-fidelity/box/run.py`, `land.py`, `fetch.py`, `signin.py` (the existing stages)

<paths>
infra/aws/ec2/canonical-fidelity/box/daily.py
infra/aws/ec2/canonical-fidelity/box/run.py
infra/aws/ec2/canonical-fidelity/tests/test_box_daily.py
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R2.md</decomp_doc> (round 2), cell `FR-s-4`.
<owned_cells>FR-s-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FR4-AC1,FR4-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~5/NFRA_FIDUPL.TO-FR-s-4.daily-orchestration.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FR4-AC1,FR4-AC2` BEFORE the flip. Commit code first, then pin.
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

Source: CTO msg 8663 (PRD v0.4.5 @e4bb46835e); Andrew-direct @b329e1c5f3; decomposition round 2 cell FR-s-4; worker reference section 11.
