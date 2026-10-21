# TO NFRA_FIDUPL.TO-FT-s-8 -- the daily-mode proof run on a config copy (switcher sweep, accountList paging, firm split)

<to_id>NFRA_FIDUPL.TO-FT-s-8</to_id>
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
<workstream>fidelity-r3-split</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-8` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 7) | **outcome_ref:** FWD-9 |
**depends_on:** FR-s-2 REPAIR 4 (split.py with null account columns, delivered by TO-FU-s-10)

---

## WORKER FACE

### THE CELL

**FT-s-8** -- Andrew's deliverable 1 is the daily pull split to each firm. The stages that do that (the switcher sweep over the 31 G numbers, the account lister's paging, the split under `fidelity/<firm>/`, the coverage record) have only run on fakes. Prove them once, on the box, on a COPY of the config, so that the scheduled fires keep running the raw land (`config.json` is not touched). CTO msg 8940.

**Read first:** `C:/Dev/ajb_workspace/org/missions/D8/NFRA/NFRA_FIDUPL/ledger/NEVER_WIDEN_SCHEDULE_ON_CTO_COUNTERSIGN_20261021.md` (what the schedule runs today), your own ledgers for TO-FT-s-6 and TO-FU-s-10, and `C:/Dev/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261020_NFRA_FIDUPL_SWITCHER_LIST_READ.md` (the firm table).

### WHAT TO DO

1. **Now (no sign-in):** open a change-management entry (`.tools/deploy_ledger.py open --slug nfra-fidupl-daily-proof-<date> ...`, legs: config copy, proof run). On the box through SSM write `/opt/fidelity-uploader/config.daily.json`: the current `config.json` plus exactly these keys, nothing else changed and `config.json` itself untouched:
   - `"mode": "daily"`
   - `"firm_labels": {"COTTONWOOD": "cottonwood", "INFLECTION": "inflection", "49 FINANCIAL": "49financial", "KEIL": "keilfinancial", "ABIDING": "abidingwealth", "LIGHTHOUSE": "lighthousewealth", "VM WEALTH": "vmwealth"}` (substring of the Wealthscape label, upper-case compare, first match wins; ALONGSIDE is deliberately absent: its accounts are the raw full files under `alongside`, and a split to that same prefix would collide)
   - `"account_columns": {"account.txt": 0, "position.txt": 5, "balance.txt": 0, "transact.txt": 0, "prices.txt": null, "security.txt": null}`
   Print only the key names. Run `fidupl_round_checks.py ft8c`.
2. **HOLD until the issuer's message says GO** (it signs in once, switches the G number 31 times and back, and the delivery of the new `split.py` must be on the box first). On GO: run once through SSM `/opt/fidelity-uploader/venv/bin/python /opt/fidelity-uploader/box/run.py /opt/fidelity-uploader/config.daily.json` and record its stdout lines verbatim (counts only). Do not retry on a refusal: report it. Do not touch the profile directories, the work folder or the agent Chrome unit.
2P. **Paging probe (added by the issuer 2026-10-21 ~03:50Z, CloudOps rows D1-S12 and D1-S13: no candidate paging form worked).** Once the box holds `box/paging_probe.py` (TO-FU-s-10, twenty-second delivery; it is there) and the issuer's GO message says so, run it ONCE, not before 04:30Z (hourly sign-in cap; read `date -u` first): `/opt/fidelity-uploader/venv/bin/python /opt/fidelity-uploader/box/paging_probe.py /opt/fidelity-uploader/config.json` through SSM, executionTimeout 900. It reads one account list on the starting G number, lands nothing and writes nothing to S3. Stop and report on any 401 or 403 (the probe stops itself). Report its stdout verbatim (every PROBE line carries counts, statuses, key names and prefix characters only) and your sign-in count for the hour. Step 2 (the daily-mode run) stays held after it until a further GO.
3. Run `fidupl_round_checks.py ft8r` and report, masked, the count of firm prefixes written, the number of keys per firm prefix (counts, no firm-by-firm G values) and the run-record keys of the run (`run-<id>.json`, `split-<id>.json`, the coverage record).

### ACCEPTANCE

<criterion id="FT-s-8-AC1" cell_refs="FT-s-8"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft8c</invocation><expect>R1-FT8C-OK daily config copy</expect></criterion>
`FT-s-8-AC1` -- the config copy exists with mode daily, the firm labels, the measured account columns (prices and security null) and the perg pointer.

<criterion id="FT-s-8-AC2" cell_refs="FT-s-8"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft8r</invocation><expect>R1-FT8R-OK split record</expect></criterion>
`FT-s-8-AC2` -- after the proof run: the newest split record shows four files split, at least three firms with rows, prices and security unsplit, no failure, conflict or firm without a scope row. A second criterion, with its reason: it is the outcome Andrew asked for and the first cannot see it.

<expected_criteria>FT-s-8-AC1,FT-s-8-AC2</expected_criteria>

Dry-run at the base (no config copy, no new split record): `FT-s-8-AC1` base: FAIL as expected; `FT-s-8-AC2` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** A file on the box and, on the issuer's GO, one real sign-in and a 31-fold G switch that restores the starting G in a `finally` and never sets a default. Ledger first, closed last. No alert, no secret value anywhere, no `safe-apply`/Terraform change in this order.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 7 addendum), cell `FT-s-8`.
<owned_cells>FT-s-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-8-AC1, FT-s-8-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FT-s-8.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-8-AC1,FT-s-8-AC2` BEFORE the flip. Commit the records first, then pin.
</proof_of_spec>

**REPORT:** the `ft8c` line, the proof run's stdout lines verbatim, the `ft8r` line, the masked per-firm counts, the run-record keys, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; denominator 0 IAM statements changed.
comp-adversary: RUN -- the run signs in once and switches the G number 31 times and back; the CTO's GO (msg 8940) and the issuer's GO message are the record.
lane: the paths block.
</preflight>

Source: CTO msg 8940; Andrew-direct v0.4.5/v0.4.6 (every G number to its firm); the first landed day and the seed (secret version 8473b6cf).
