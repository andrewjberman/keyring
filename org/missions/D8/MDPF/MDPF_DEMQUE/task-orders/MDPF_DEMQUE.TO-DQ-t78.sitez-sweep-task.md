# TO MDPF_DEMQUE.TO-DQ-t78 -- DQ-t-78: register the 16:00 ET daily sweep task at site Z and read its first fire
<to_id>MDPF_DEMQUE.TO-DQ-t78</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.7.0_AE_CloudOps~MDPF1</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>SWEEPTASK</workstream>
**GO:** the issuer sets `pending` once `TO-DQ-t77` is merged and on `CLOUD`. Until then nothing at site Z moves. Addressee: `0.7.0_AE_CloudOps~MDPF1` ON THE SITEZ DEVICE.
**Directive:** D8 | **Fabric:** dell1 (placement site Z) | **Decomp cell:** `DQ-t-78` (`decompositions/MDPF_DEMQUE_DECOMP.md`, amendment 38) |
**outcome_ref:** C-PRICES, C-RESERVE | **depends_on:** DQ-t-77 (merged and on CLOUD)

---

## WORKER FACE

### THE CELL

Andrew ruled (record `org/tier1_exec/2.0.0_SA_COO~Q1/deliverables/ANDREW_DIRECT_20261019_16xxZ_LATE_DAY_SWEEP_OF_UNUSED_QUOTA.md`): **at 16:00 US Eastern, every day, trading days included, whatever is left of the 2,500,000-cell daily Bloomberg total is drawn by the backfill queue, the per-surface lines waived for that pass only.** `TO-DQ-t77` added the sweep to `data/mdpf/scripts/demque/standing_drawer.py` (`--apply --sweep`, its own marker, its own receipt `receipt.<day>.sweep.json`; it stops with `PRODUCTION_SPEND_UNREAD` and draws nothing when that day's production budget ledger is absent). **This cell registers the schedule and reads the first sweep.**

**Do, in order**
1. Open a NEVER-2 change-management entry (`org/critical_paths/change_management/` and its sentinel in `org/critical_paths/.open_deploys/`) before step 3; close it at the end, sentinel committed.
2. Bring the site Z checkout to `CLOUD` at or after the commit that carries the `TO-DQ-t77` merge (fast-forward only; no rebase, no reset). Print `git log --oneline -1`; prove it: `python data/mdpf/scripts/demque/standing_drawer.py --task-name --sweep` prints `mdpf-demque-sweep-daily`, and `--room --sweep --day <today>` prints one JSON line.
3. **Measure before registering:** on the most recent trading day, read the time of the LAST production row in that day's budget ledger (`bbg_budget_<day>.jsonl`, `at` field, modes other than `demque-backfill*`) and state it in US Eastern. If any production row lands after 16:00 ET, STOP and file a BLOCKING row naming the mode and time: the sweep would spend quota production still needs.
4. Register ONE Windows task, the name printed by `--task-name --sweep` (never typed), daily at 16:00 US Eastern, running `python data/mdpf/scripts/demque/standing_drawer.py --apply --sweep` from the repository root under the same account and settings as the existing `mdpf-demque-drawer-daily` task (read it with `schtasks /query /tn mdpf-demque-drawer-daily /v /fo list` and match its run-as user, working directory and Python). If site Z's clock is not US Eastern, set the trigger to the local time equal to 16:00 ET and say so. Change nothing on the existing drawer task.
5. After the first scheduled sweep, read `receipt.<day>.sweep.json` and that day's actuals rows with `"pass": "sweep"`: report cells drawn per request, `daily_total_left` at the start, `spent_today`, `unconverted_modes`, and any `empty_windows` or probe results. Run no draw by hand.

### ACCEPTANCE

<criterion id="DQ9-t78-AC1" cell_refs="DQ-t-78"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t78_task.py</invocation><expect>TASK-OK</expect></criterion>
<criterion id="DQ9-t78-AC2" cell_refs="DQ-t-78"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t78_fire.py</invocation><expect>FIRE-OK</expect></criterion>

<expected_criteria>DQ9-t78-AC1,DQ9-t78-AC2</expected_criteria>

`DQ9-t78-AC1` -- the task exists under the builder's name, daily, 4:00 PM, running `--apply --sweep`. `DQ9-t78-AC2` -- DATE-GATED to the first scheduled sweep after the GO: the newest sweep receipt drew more than 0 cells, no more than its `daily_total_left`, with no vendor-limit, refusal or `PRODUCTION_SPEND_UNREAD` stop; the order stays open until it reads FIRE-OK. Run each from the repository root at site Z. At the base: `TASK-BAD standing_drawer --task-name --sweep rc=2 ...`; `FIRE-BAD no sweep receipt ...`.

## BOUNDS

- **Bloomberg draws only through the scheduled task; no draw by hand; stop on any limit warning or refusal;** no auth path changed; no S3 write beyond the uploader's existing daily ledger object.
- Register exactly one task; change no other task; edit no code, request or allowance file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-Z-W5-S<k>`, `fabric` `site-z`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl
org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_STANDING/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9, amendment 38), cell `DQ-t-78`.
<owned_cells>DQ-t-78</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t78-AC1, DQ9-t78-AC2. Instance at `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE.TO-DQ-t78.sitez-sweep-task.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t78-AC1,DQ9-t78-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the checkout commit, the last production row time in ET, the registered task (name, trigger, action, run-as), the first sweep's receipt figures, the change-management entry, commits and push state.

---

## RECORD FACE

<preflight>
comp-schedule: RUN a new daily schedule (16:00 ET) beside the existing 10:00 ET drawer task; step 3 measures production's last row against it before registering.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the uploader's existing PutObject is unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE a registration read by schtasks and one scheduled fire read from its receipt.
risk: WORLD -- a new standing Bloomberg draw at site Z that can approach the 2,500,000-cell daily total; the drawer stops on any vendor limit or refusal and fails closed when production's spend is unread.
direct_act: false -- a seat order to the site Z MDPF CloudOps lane.
</preflight>

Source: Andrew-direct 2026-10-19 ~16:2xZ (record above, @19bcfdb913). The CTO is told (`1.0.0_SA_CTO~DELL1`, 2026-10-19 16:30Z). Codex lanes run this mission-tree order directly (site Z AGENTS.md @a55888e3a2).
