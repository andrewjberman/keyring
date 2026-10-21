# TO NFRA_FIDUPL.TO-FW-s-2 -- deliver api_walk.py to the box and run the API surfaces walk until every account of every surface is done

<to_id>NFRA_FIDUPL.TO-FW-s-2</to_id>
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
<workstream>fidelity-r3-apiwalk-live</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FW-s-2` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 16) | **outcome_ref:** FWD-9 (C-BACKFILL) |
**depends_on:** FW-s-1 merged (the issuer's message names the head); TO-FV-s-3 runs alternate with this order's

---

## WORKER FACE

### THE CELL

**FW-s-2** -- The CTO (msgs 9117 and 9121, Andrew-direct) ruled the per-account API surfaces landed as raw bronze JSON: transactions in 365-day windows back to the first empty window, realized lots over a 30-year range split until complete, and open (unrealized) lots as a daily snapshot. The box command is `/opt/fidelity-uploader/api_walk.py` (cell FW-s-1). Deliver it, then run it until it reports `all_done`. The walk resumes across runs from a state file on the box.

**HOLD.** Do nothing until the issuer's message "FW-s-1 merged at <head>". Then:

### WHAT TO DO

1. Open a change-management entry (`.tools/deploy_ledger.py open --slug nfra-fidupl-apiwalk-delivery-<date> ...`). Deliver every shipped file of `infra/aws/ec2/canonical-fidelity/` (and `box/`) from the named head or later to `/opt/fidelity-uploader/` exactly as in TO-FV-s-3 step 1 (SSM file copy, md5-checked; the shipped set now includes `api_walk.py`): no bootstrap, no sign-in, no instance start or stop, nothing under either profile directory, `config.json`, `work/`, `venv/` or the bridge symlinks. Run `fidupl_round_checks.py fu10m`. Close the leg.
2. Open a second ledger entry (slug `nfra-fidupl-apiwalk-runs-<date>`). **Run the walk** through SSM with executionTimeout 3000:
   `/opt/fidelity-uploader/venv/bin/python -u /opt/fidelity-uploader/api_walk.py --config /opt/fidelity-uploader/config.json --max-seconds 2400`
   The FIRST run uses `--surfaces open --max-accounts 100 --max-seconds 600` (a short proof: the open-lots surface only, 100 accounts); read its stdout and the `apiwalk-<id>.json` record before the full runs. Report it to the issuer and then continue with the full command above (all three surfaces) without waiting for a reply unless the first run stopped on `auth`, `throttled` or `error`.
3. **Chaining.** After a run whose stop is `budget`, `terminated` or `surface_end`, run the same command again (`surface_end` means every account was worked once and some ERROR accounts await their one retry on the next run; a second `surface_end` with the same count means they are final: report the count and finish with step 4 instead). Rules: (a) never start a run while another run (this order's or TO-FV-s-3's) is running on the box: one browser profile; (b) your own sign-in count in the trailing hour is under 3, counting the issuer's and every other run; the three scheduled legs fire at 09:45Z, 10:15Z and 10:45Z, so no run may start between 09:20Z and 11:00Z; (c) at most 2 runs start in any rolling hour; (d) alternate with TO-FV-s-3's runs until that order reports `all_types_stopped`, then run only this one. Send the issuer ONE short message per run (stop, accounts done per surface, earliest content dates). Stop chaining on any 401, 403, lockout line, an `auth`, `throttled` or `error` stop (report the exact line, do NOT retry).
4. When a run ends `all_done`, run `fidupl_round_checks.py fw2r` and `fu10m`, close the ledger entries, and report: per surface the accounts done, no access, errors, incomplete, the earliest content date, objects and bytes landed; the number of runs and sign-ins. **In anything committed to git, mask account numbers** (sha8 only); the S3 objects and the S3 record keep the numbers.

### ACCEPTANCE

<criterion id="FW-s-2-AC1" cell_refs="FW-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fw2r</invocation><expect>R1-FW2R-OK apiwalk complete</expect></criterion>
`FW-s-2-AC1` -- the newest walk record carries the marker, no run error and the stop `all_done`; the earliest content date per surface is printed.

<criterion id="FW-s-2-AC2" cell_refs="FW-s-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu10m</invocation><expect>R1-FU10M-OK all</expect></criterion>
`FW-s-2-AC2` -- the box code equals the repo, api_walk.py included.

<expected_criteria>FW-s-2-AC1,FW-s-2-AC2</expected_criteria>

Dry-run at the base: `FW-s-2-AC1` base: FAIL as expected (no walk record yet); `FW-s-2-AC2` base: PASS as expected until `api_walk.py` is merged, then FAIL until delivered.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** Real sign-ins (one per run) and read calls to three Fidelity APIs (about 30,000 transaction calls, 5,013 realized-lot calls and 5,013 open-lot calls in all, paced 0.3 s apart); the walk lands only under `fidelity/alongside/bronze/` by `address()`, never overwriting. Ledger first, closed last. No Terraform, no IAM change, no alert, no schedule change.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 16 addendum), cell `FW-s-2`.
<owned_cells>FW-s-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FW-s-2-AC1, FW-s-2-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FW-s-2.apiwalk-live.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FW-s-2-AC1,FW-s-2-AC2` BEFORE the flip. Commit the records first, then pin.
</proof_of_spec>

**REPORT:** the stdout lines per run, the `fw2r` and `fu10m` lines, per surface the counts and earliest content date, runs and sign-ins, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; the runs avoid the 09:45Z to 10:45Z legs; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; denominator 0 IAM statements changed.
comp-adversary: RUN -- each run signs in once and issues read calls to three Fidelity APIs; the CTO's orders (msgs 9117, 9121) and the issuer's GO are the record.
lane: the paths block.
</preflight>

Source: CTO msgs 9117, 9121; the issuer's live probes; FW-s-1 as merged.
