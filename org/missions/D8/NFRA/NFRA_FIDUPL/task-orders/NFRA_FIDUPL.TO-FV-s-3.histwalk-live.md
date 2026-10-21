# TO NFRA_FIDUPL.TO-FV-s-3 -- deliver hist_walk.py to the box and run the Historical backfill walk until every type has stopped

<to_id>NFRA_FIDUPL.TO-FV-s-3</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>fidelity-r3-histwalk-live</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FV-s-3` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 15) | **outcome_ref:** FWD-9 (C-BACKFILL) |
**depends_on:** FV-s-1 and FV-s-2 merged (the issuer's message names the head)

---

## WORKER FACE

### THE CELL

**FV-s-3** -- The CTO (msg 9101) ruled the Historical backfill walk: positions, balances and prices, one POST per trading day from 2026-10-15 backward to the proven floor, landed by content date, a type stopping after three consecutive "file does not exist" answers. The box command is `/opt/fidelity-uploader/hist_walk.py` (cells FV-s-1 and FV-s-2). Deliver it, then run it until it reports `all_types_stopped`. The walk resumes across runs from a state file on the box and lands each file by `address()`; a day already landed is skipped.

**HOLD.** Do nothing until the issuer's message "FV-s-2 merged at <head>". Then:

### WHAT TO DO

1. Open a change-management entry (`.tools/deploy_ledger.py open --slug nfra-fidupl-histwalk-delivery-<date> ...`, one leg: code equal to the repo). Deliver every shipped file of `infra/aws/ec2/canonical-fidelity/` (and `box/`) from the named head or later to `/opt/fidelity-uploader/` exactly as in TO-FU-s-10 (SSM file copy, md5-checked; the full shipped set now includes `hist_walk.py`): no bootstrap, no sign-in, no instance start or stop, nothing under either profile directory, `config.json`, `work/`, `venv/` or the bridge symlinks. Run `fidupl_round_checks.py fu10m` (expect `R1-FU10M-OK all N shipped files match`). Close the leg.
2. Open a second ledger entry (slug `nfra-fidupl-histwalk-runs-<date>`, one leg per run). **Run the walk** through SSM with executionTimeout 1200:
   `/opt/fidelity-uploader/venv/bin/python -u /opt/fidelity-uploader/hist_walk.py --config /opt/fidelity-uploader/config.json --max-days 20 --max-seconds 900`
   Record the stdout lines verbatim and read stderr. The command resumes where the last run stopped (state file) and ends with a `STOP <reason>` line.
3. **Chaining.** After a run whose stop is `day_cap`, `budget` or `terminated`, run the same command again, but only when (a) your own sign-in count in the trailing hour is under 3 (each run is ONE sign-in; count the issuer's and the standing runs too: the three scheduled legs fire at 09:45Z, 10:15Z and 10:45Z, so no run may start between 09:20Z and 11:00Z, and none may overlap a leg), (b) at most 2 runs start in any rolling hour, and (c) the previous run's stop was not `auth`, `error` or `refused`. Send the issuer ONE short message per run (stop, days walked, earliest landed per type). Stop chaining on any 401, 403 or lockout line, an `auth` or `error` stop, or a `refused` type (report the exact text); do NOT retry those. Do not touch any cookie or profile directory; the agent Chrome unit is not to be touched.
4. When a run ends `all_types_stopped`, run `fidupl_round_checks.py fv3r` and `fu10m`, close the ledger entries, and report: per type the earliest landed date, days landed, bytes; the stop evidence per type; the number of runs and sign-ins.

### ACCEPTANCE

<criterion id="FV-s-3-AC1" cell_refs="FV-s-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fv3r</invocation><expect>R1-FV3R-OK histwalk complete</expect></criterion>
`FV-s-3-AC1` -- the newest walk record carries the marker, no run error, and the stop `all_types_stopped`; the earliest landed date per type is printed.

<criterion id="FV-s-3-AC2" cell_refs="FV-s-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu10m</invocation><expect>R1-FU10M-OK all</expect></criterion>
`FV-s-3-AC2` -- the box code equals the repo, hist_walk.py included.

<expected_criteria>FV-s-3-AC1,FV-s-3-AC2</expected_criteria>

Dry-run at the base: `FV-s-3-AC1` base: FAIL as expected (no walk record yet); `FV-s-3-AC2` base: PASS as expected until `hist_walk.py` is merged, then FAIL until delivered.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** Real sign-ins (one per run) and Historical export requests (two POSTs per day walked, about 170 in all); the walk lands only under `fidelity/alongside/bronze/` by `address()`, never overwriting. Ledger first, closed last. No Terraform, no IAM change, no alert, no schedule change.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 15 addendum), cell `FV-s-3`.
<owned_cells>FV-s-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FV-s-3-AC1, FV-s-3-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FV-s-3.histwalk-live.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FV-s-3-AC1,FV-s-3-AC2` BEFORE the flip. Commit the records first, then pin.
</proof_of_spec>

**REPORT:** the stdout lines per run, the `fv3r` and `fu10m` lines, per type the earliest landed date, days and bytes, the stop evidence, runs and sign-ins, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; the runs avoid the 09:45Z to 10:45Z legs; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; denominator 0 IAM statements changed.
comp-adversary: RUN -- each run signs in once and issues Historical export requests (the create call) and Export Status reads; the CTO's order (msg 9101) and the issuer's GO are the record.
lane: the paths block.
</preflight>

Source: CTO msgs 9085, 9091, 9101; the issuer's live probe record FIDUPL_historical_live_request_and_cap_probe_20261021.md; FV-s-1 and FV-s-2 as merged.
