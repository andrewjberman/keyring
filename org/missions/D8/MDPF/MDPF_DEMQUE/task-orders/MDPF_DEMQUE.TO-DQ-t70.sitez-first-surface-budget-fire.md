# TO MDPF_DEMQUE.TO-DQ-t70 -- DQ-t-70: site Z runs the surface-budget drawer and the 2026-10-17 fire draws surface-tagged requests past the history ceiling
<to_id>MDPF_DEMQUE.TO-DQ-t70</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.7.0_AE_CloudOps~MDPF1</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>SURFROOM</workstream>
**GO (issuer, 2026-10-17 ~04:4xZ):** `TO-DQ-t69` is merged @8ce2921610 and on `CLOUD` @3af9864832 (ls-remote read; `merge-base --is-ancestor 8ce2921610 origin/CLOUD` TRUE). Addressee: `0.7.0_AE_CloudOps~MDPF1` ON THE SITEZ DEVICE (the lane site Z seated 04:24Z; the laptop's lane of the same name is a different seat and is NOT the addressee). Site Z's checkout must take `CLOUD` at or after 3af9864832 BEFORE the 14:00Z fire.
**AMENDED by the issuer 2.0.0_SA_COO~Q1, 2026-10-18 ~14:2xZ (site Z rows MDPF_DEMQUE-Z-S6 and Z-S8):** AC2 is RE-DATED from the 2026-10-17 fire to the **2026-10-24 14:00Z** fire (the next fire day: Monday 10-19 to Friday 10-23 are trading days and the drawer draws nothing on them). The 10-17 fire read FIRE-BAD (it stopped on an empty window in a surface-B request; surface-tagged cells 5,618) and the 10-18 fire drew 0 history cells (its history probe of `/cusip/662858FV6` returned 0 rows, so every history request was refused). Both reads stay on this order as FIRE-BAD; neither exercised the property AC2 grades, because the draw was stopped upstream of the surface rooms. Before the 10-24 fire, `0.7.0_AE_CloudOps~MDPF1` and the BBGTerminal seat measure READ-ONLY why the probe returned 0 (Terminal sign-in state, entitlement, the probe's own request against a known-good security); no draw is run by hand. `dq_t70_fire.py` DAY is now 2026-10-24.
**Directive:** D8 | **Fabric:** dell1 (placement site Z) | **Decomp cell:** `DQ-t-70` (`decompositions/MDPF_DEMQUE_DECOMP.md`, amendment 33) |
**outcome_ref:** C-PRICES, C-RESERVE | **depends_on:** DQ-t-69 (merged and on CLOUD)

---

## WORKER FACE

### THE CELL

`TO-DQ-t69` makes the quote and the standing drawer read the surface budgets Andrew set on 2026-10-16: a request tagged surface C draws up to 400,000 cells a fire, an untagged request keeps the 5,858 history ceiling, and a trading-day fire still draws nothing (CTO ruling `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/CTO_RULING_DRAWER_HONOURS_SURFACE_BUDGETS_20261017.md` @d4ad590946). **This cell is the site Z half: confirm site Z runs that code, and read the first fire that uses it.** Executor of the draw: the registered daily task `mdpf-demque-drawer-daily` (10:00 ET, 14:00Z). Saturday 2026-10-17 is a non-trading day, so that fire may draw. You change no code, no limit and no schedule.

**Do, in order**
1. Open a change-management entry for this act (`org/critical_paths/change_management/`, and its sentinel in `org/critical_paths/.open_deploys/`) BEFORE the fire; close it at the end.
2. Bring the site Z checkout to a commit that contains the `TO-DQ-t69` merge (a fast-forward pull of the branch site Z follows; no rebase, no reset). Print `git log --oneline -1` and prove the content: `python data/mdpf/scripts/demque/standing_drawer.py --room --day 2026-10-17` prints surface C 400000.
3. Read the task's next trigger and last result (`schtasks /query /tn <the built task name> /v /fo list`, where `python data/mdpf/scripts/demque/standing_drawer.py --task-name` prints the name). Do not edit the task.
4. After the 14:00Z fire, read the receipt in `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_STANDING/` and the actuals ledger rows of 2026-10-17: report, per request, the cells drawn, and the total per surface.
5. If the fire draws nothing (a stop reason in the receipt), write the stop reason into your report and a surprise row; do not run a draw by hand.

### ACCEPTANCE

<criterion id="DQ9-t70-AC1" cell_refs="DQ-t-70"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t69_room.py</invocation><expect>SURF-OK</expect></criterion>
<criterion id="DQ9-t70-AC2" cell_refs="DQ-t-70"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R10_CHECKS/dq_t70_fire.py</invocation><expect>FIRE-OK</expect></criterion>

<expected_criteria>DQ9-t70-AC1,DQ9-t70-AC2</expected_criteria>

`DQ9-t70-AC1` -- run at site Z's repository root: the checkout reads the room the surface budgets give (Saturday untagged 5858, surface C 400000, daily total left 2500000; Monday 0). `DQ9-t70-AC2` -- run after the 2026-10-17 14:00Z fire: the surface-tagged cells drawn that day exceed 5,858, each surface stays within its budget, the day's cells total at most 2,500,000, and no row stopped on a vendor limit. (Amended by the issuer ~04:4xZ: every ETFS_RIVALS-C1 request, the surface-C requests, carries a draw_hold by CTO msg 7279, so the fire is graded on the surfaces that draw; criterion text only, no new check.) AC2 is date-gated to that fire and the order stays open until it reads FIRE-OK. At the base: `SURF-BAD standing_drawer --room rc=2 ... unrecognized arguments: --room`; `FIRE-BAD no surface-tagged cells drawn on 2026-10-17`.

## BOUNDS

- **Bloomberg draws only through the standing drawer, only on non-trading days;** stop on any limit warning or refusal; no manual draw (`--apply` is not run by you); no auth path changed; no S3 write beyond the uploader's existing daily ledger object.
- **You arm no timer, background task or OS task, and edit no limit or request file.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-Z-W4-S<k>`, `fabric` `site-z`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl
org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE_ZQ_STANDING/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9, amendment 33), cell `DQ-t-70`.
<owned_cells>DQ-t-70</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t70-AC1, DQ9-t70-AC2. Instance at `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_DEMQUE.TO-DQ-t70.sitez-first-surface-budget-fire.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t70-AC1,DQ9-t70-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the checkout commit and the room read, the task's trigger and last result, the fire's receipt and per-request cells, the change-management entry, commits and push state.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is created or changed; the registered task `mdpf-demque-drawer-daily` runs the updated file.
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the uploader's existing PutObject is unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE a read of one scheduled fire against the budget Andrew set; the code is graded under TO-DQ-t69.
risk: WORLD -- the standing Bloomberg history draw at site Z through the queue now draws up to the surface budget; the CTO ruling @d4ad590946 is the pair's CTO half; `1.0.0_SA_CTO~Z` signs the site-Z half.
direct_act: false -- a seat order to the site-Z per-project lane.
</preflight>

Source: Andrew-direct 2026-10-16 ~15:5xZ ("round-10 cells DQ-t-69 and DQ-t-70") and 2026-10-17 ~03:1xZ / ~03:4xZ; CTO ruling @d4ad590946; the same drawer and fire as `TO-DQ-t34` (AC2 of that order reads the same 2026-10-17 fire).
Codex lanes run this mission-tree order directly (site Z AGENTS.md @a55888e3a2).
