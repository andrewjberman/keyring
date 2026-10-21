# TO NFRA_FIDUPL.TO-FT-s-11 -- backfill probe 1, live: walk the export calendar back at the rep level

<to_id>NFRA_FIDUPL.TO-FT-s-11</to_id>
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
<workstream>fidelity-r3-backfill-live</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FT-s-11` (`decompositions/NFRA_FIDUPL_DECOMP_R3.md` section 10) | **outcome_ref:** FWD-9 (C-BACKFILL) |
**depends_on:** FT-s-7 (merged and delivered, TO-FU-s-10 eighteenth delivery onward)

---

## WORKER FACE

### THE CELL

**FT-s-11** -- Andrew's deliverable 2 is the backfill: land the days before the first scripted day, "as far back as possible", found empirically ("exports at progressively earlier dates until the channel refuses or returns empty"). The CTO (msg 8999) ruled it runs now at the rep level, because the Export Status list and the exports belong to the login, not to a G number. The box already holds the walk (`/opt/fidelity-uploader/backfill_main.py`, FT-s-7): one sign-in, the planner walks the New York calendar back day by day through the Export Status list, lands every COMPLETED day by content date under `fidelity/alongside/bronze/`, stops on a refusal, on three consecutive empty trading days, on the run cap or on the day cap, writes ONE completion record and logs out.

### WHAT TO DO

1. Open a change-management entry (`.tools/deploy_ledger.py open --slug nfra-fidupl-backfill-probe1-<date> ...`, one leg: the run). Check `date -u` and your own sign-in count first: the standing cap is 3 per hour and the run makes ONE sign-in with no recovery; the run is ordered for 06:01Z or later.
2. Run ONCE through SSM, executionTimeout 900: `/opt/fidelity-uploader/venv/bin/python /opt/fidelity-uploader/backfill_main.py --config /opt/fidelity-uploader/config.json` (defaults: 125 days, 12 exports, 2 sessions a day). Record the stdout lines verbatim. Do NOT retry on a refusal or an error; stop and report on any 401, 403 or lockout signal. Do not touch the profile directories, the work folder or the agent Chrome unit. The run lands by content date; a day already landed is `skipped_existing`, not rewritten.
3. Run `fidupl_round_checks.py ft11r` and read the completion record (`fidelity/alongside/bronze/_runs/<New York day>/backfill-<run id>.json`, via `lib/opal_naming.py address()`). Report: the stdout lines, the `ft11r` line, per file type the earliest date, days and bytes landed, the stop reason and evidence, and the FIRST earlier-date result as served, empty or refused with its date (the dates only, no other value).
3B. **Second run (issuer, 2026-10-21 ~06:22Z; your row D1-S14).** After the twenty-sixth box code sync (`backfill_main.py` with DAY lines and a 120 s request timeout), and ONLY at 06:47Z or later (read `date -u` and your own count first; the issuer's read-only walk makes a sign-in at about 06:32Z), run the same command ONCE more and report as in step 3, with the new `DAY` lines verbatim and the record's `days` list (date, result, secs) and `stop`. A `timeout` stop is a real answer; do not retry it.
3C. **Third run (issuer, 2026-10-21 ~07:20Z; CTO msg 9018, your row D1-S15).** After the twenty-seventh box code sync, open a ledger entry FIRST (your omission last time), and at 07:22Z or later (read `date -u` and your count: 06:47 and the issuer's 07:08 are in the hour; this is the 3rd) run ONCE through SSM with executionTimeout 660: `/opt/fidelity-uploader/venv/bin/python -u /opt/fidelity-uploader/backfill_main.py --config /opt/fidelity-uploader/config.json --max-seconds 480 --max-sessions 4`. (The daily session cap of 2 was the cell's own rule; the issuer amends it to 4 for today only, per the CTO.) The run now prints every DAY, REQ, SIGNIN and CLOSE line as it happens and stops itself at the wall budget; a `budget` or `timeout` stop is a real answer, do not retry it. Report the stdout verbatim, the ft11r line, the record's `days` list and `stop`, and read the SSM stderr too.
3D. **Fourth run (issuer, 2026-10-21 ~07:55Z; CTO msg 9031).** After the twenty-eighth box code sync, open a ledger entry FIRST, and at **08:22Z or later** (read `date -u` and your count: the hour ending then holds 07:22 and the issuer's refused 07:49 attempt; the issuer makes NO further sign-in) run ONCE through SSM with executionTimeout 660: `/opt/fidelity-uploader/venv/bin/python -u /opt/fidelity-uploader/backfill_main.py --config /opt/fidelity-uploader/config.json --max-seconds 480 --max-sessions 6`. The run reads each download inside the browser with a 120 s idle bound, lands a partly served day's files, retries the missing files once at the end and writes the record after every day. Report stdout and stderr verbatim, the ft11r line, the record's `days` (date, result, secs, files, missing), per file type `earliest_served`, `served_days` and the `stop`. A stall, budget or timeout stop is a real answer: no retry. Stop on any 401, 403 or lockout line. Do not clear any cookie or profile directory; the agent Chrome unit is not to be touched.
3E. **Fifth run (issuer, 2026-10-21 ~08:45Z; CTO msgs 9031 and 9036).** After the twenty-ninth box code sync, open a ledger entry FIRST, and at **08:56Z or later** and DONE BEFORE 09:30Z (the first scheduled fire is 09:45Z) run ONCE through SSM with executionTimeout 660: `/opt/fidelity-uploader/venv/bin/python -u /opt/fidelity-uploader/backfill_main.py --config /opt/fidelity-uploader/config.json --max-seconds 480 --max-sessions 8`. Your count then: 08:22 yours, and nothing of the issuer's (the 07:49 attempt aged out at 08:49). A stalled file is cut at 90 s and named missing; the day lands its served files; the walk goes on to earlier days (2026-10-16 and before). Report stdout and stderr verbatim, the ft11r line, the record's `days` (date, result, secs, files, missing), per file type `earliest_served`, `served_days`, days landed and bytes, and the `stop`. A stall, budget or timeout stop is a real answer: no retry. Stop on any 401, 403 or lockout line. Touch no cookie or profile directory.
4. Close the ledger entry.

### ACCEPTANCE

<criterion id="FT-s-11-AC1" cell_refs="FT-s-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py ft11r</invocation><expect>R1-FT11R-OK backfill record</expect></criterion>
`FT-s-11-AC1` -- after the run the newest backfill completion record carries the backfill marker, one sign-in, no run error and a stop reason; the earliest dates per file type are printed.

<criterion id="FT-s-11-AC2" cell_refs="FT-s-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/fidupl_round_checks.py fu10m</invocation><expect>R1-FU10M-OK all</expect></criterion>
`FT-s-11-AC2` -- the box code is unchanged by the run (a regression guard).

<expected_criteria>FT-s-11-AC1,FT-s-11-AC2</expected_criteria>

Dry-run at the base: `FT-s-11-AC1` base: FAIL as expected (no backfill record yet); `FT-s-11-AC2` base: PASS as expected.

## BOUNDS

- **Grant.** The `<paths>` block below and your deliverables folder.
- **WORLD.** One real sign-in and read-only Export Status calls; the lander writes only under `fidelity/alongside/bronze/` by `address()`. Ledger first, closed last. No Terraform, no IAM change, no alert.
- **Refusal clause.** A premise that fails is a surprise row in the investigation file (`NFRA_FIDUPL-D1-<your slot>-S<k>`, next unused) and you stop that piece.

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R3.md</decomp_doc> (round 3, section 10 addendum), cell `FT-s-11`.
<owned_cells>FT-s-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FT-s-11-AC1, FT-s-11-AC2. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.7.0_AE_CloudOps~NFRA1/NFRA_FIDUPL.TO-FT-s-11.backfill-probe1.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FT-s-11-AC1,FT-s-11-AC2` BEFORE the flip. Commit the records first, then pin.
</proof_of_spec>

**REPORT:** the stdout lines, the `ft11r` line, per-file-type earliest date, days and bytes, the stop reason, the first earlier-date result, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched; denominator 0 schedules changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant changes; denominator 0 IAM statements changed.
comp-adversary: RUN -- the run signs in once and issues read-only Export Status calls; the CTO's order (msg 8999) and the issuer's GO are the record.
lane: the paths block.
</preflight>

Source: CTO msg 8999; Andrew-direct (backfill as far back as possible, found empirically); FT-s-7 as merged.
