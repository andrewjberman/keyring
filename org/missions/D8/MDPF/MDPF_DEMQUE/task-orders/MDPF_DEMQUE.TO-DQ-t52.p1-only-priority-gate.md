# TO MDPF_DEMQUE.TO-DQ-t52 -- round 9 DQ-t-52: the priority gate -- former clients (P3) are never drawn, a match-open name (P2) waits on its match, and only P1 draws
<to_id>MDPF_DEMQUE.TO-DQ-t52</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~44</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>PRIGATE</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-52` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 16) |
**outcome_ref:** C-PRIORITY, C-IDENTITY, FWD-9 | **depends_on:** DQ-t-45 (merged), DQ-t-13 (rank.py)

---

## WORKER FACE

### THE CELL

The dell1 pivot packet ([DIRECTION_DELL1_20261013.md](file:///C:/dev/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL1_20261013.md);
repo-relative `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL1_20261013.md`, outcomes O6 and O12 and section 6; read them) carries Andrew's word:
**former Cottonwood clients (P3) are excluded from every draw, on any vendor; a match-open name (P2) draws only after its match resolves; P1 (a living client) draws.**
`rank.py` (DQ-t-13) today ranks "P3 gone" LAST and still pursues it. Measured by the issuer at 14:2xZ: of the 326 names landed in the price store, P1 246, P2 72, **P3 8**; of the
878 names in the IRPT request, P1 630, P2 229, **P3 19**. The nightly draw (22:30 ET) would still extend and draw them. This cell makes P2 and P3 refused at the one place every
draw passes. **It makes no vendor call and writes no store.**

**Build** (read `rank.py`, `extend_frontier.py` `_tiers` / `plan`, `daily_draw.py` `run`, `demand_queue.py` `draw`, `redraw_stale.py` first; import, do not copy):
1. **`priority_gate.py`** (NEW): `excluded(cusips, crosswalk_df, tx_df) -> dict[cusip, reason]`: a P3 name -> `"former client: never drawn (Andrew-direct 2026-10-13)"`, a P2 name ->
   `"match open: waits on its match (Andrew-direct 2026-10-13)"`, P1 and unclassified-as-P1 names are absent. It calls `rank.rank` and nothing else decides priority. A name with
   no holder on record is P2 (the rank rule), so it is excluded too. A `--census` CLI (read only, S3 read) prints ONE JSON line `{"index": {"names", "P1", "P2", "P3"},
   "excluded_from_extension", "files": [{"name", "securities", "P1", "P2", "P3"}], "rule": "..."}` over the price index and every `*.json` request in `requests/` and the device queue
   `~/.opal/demque/queue` (a `name` for a device file starts with `queue/`); `rule` names "former client" and "2026-10-13".
2. **`rank.py`**: a P3 name carries `pursued: False` with the reason above, and a P2 name `pursued: False` with its reason; a P1 name is unchanged. The request builders
   already leave out `pursued: False`. The existing `test_demque_rank.py` assertions that expect P3 pursued are changed to the new rule and nothing else.
3. **`extend_frontier.py`**: `_tiers` (and so `plan`, `plan_week`, `--lag-report`) leaves out every excluded name, and the plan prints `excluded_p2` and `excluded_p3` beside `frontier`
   (extra keys; every existing key keeps its value for P1 names). The crosswalk and transactions are read once per process.
4. **`daily_draw.py` / `demand_queue.py`**: a request security that the gate excludes is SKIPPED at draw time (no vendor call, no pacer entry used), counted in the run's printed
   result as `skipped_excluded`, never silently dropped. If the gate cannot read the crosswalk or transactions, the draw REFUSES with a loud message (fail closed: no name is drawn
   on an unread classification).
5. NEW `test_demque_priority_gate.py` (pytest; stub frames, no network, no S3) with exactly these names:
   `test_a_p3_name_is_never_pursued_and_a_p2_name_waits_on_its_match_while_p1_is_unchanged`,
   `test_the_standing_extension_tiers_leave_out_p2_and_p3_names_and_count_them`,
   `test_the_daily_draw_skips_an_excluded_request_security_and_counts_the_skip`.
   Existing demque tests that build a stub draw may take the stub's classification inputs and NOTHING else.

### ACCEPTANCE

<criterion id="DQ9-t52-AC1" cell_refs="DQ-t-52"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t52_tests.py</invocation><expect>GATE-OK</expect></criterion>
<criterion id="DQ9-t52-AC2" cell_refs="DQ-t-52"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t52_real.py</invocation><expect>GATE-REAL-OK</expect></criterion>
`DQ9-t52-AC1` -- the three named tests. `DQ9-t52-AC2` -- on the REAL inputs: the index splits into P1, P2 and P3 with the exclusions counted, every request file's classes add up, and the
IRPT device queue copy (cut to P1 by the issuer at 14:2xZ) carries no P2 or P3 name. The real check allows 115 seconds: load the crosswalk and transactions once. Report the whole folder
`pytest data/mdpf/scripts/demque` once.

<expected_criteria>DQ9-t52-AC1,DQ9-t52-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `GATE-BAD no file ...`; `GATE-REAL-BAD no file ...priority_gate.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO Yahoo call, NO Bloomberg call, no write to S3, the ledger, the queue or any pacer state, no AWS write, no deploy, no timer. `extend_frontier.py --apply`, `daily_draw.py`,
  `run_daily_draw.sh` and `redraw_stale.py --apply` are NEVER run.** The scheduled 22:30 ET draw runs from the shared tree after this merges: every change must keep a P1-only queue
  valid and drawing as before.
- **Account ids never enter a committed file or the output** (the crosswalk and transactions carry them; read them only to classify by CUSIP).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W44-S<k>`, `fabric` `dell1`, `surfaced_at` =
  `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a check or the rule. Rows are APPEND-ONLY. Merge `box/dell1` into your
  branch (a merge, never a rebase) before you append rows.

<paths>
data/mdpf/scripts/demque/priority_gate.py
data/mdpf/scripts/demque/rank.py
data/mdpf/scripts/demque/extend_frontier.py
data/mdpf/scripts/demque/daily_draw.py
data/mdpf/scripts/demque/demand_queue.py
data/mdpf/scripts/demque/test_demque_priority_gate.py
data/mdpf/scripts/demque/test_demque_rank.py
data/mdpf/scripts/demque/test_demque_daily_draw.py
data/mdpf/scripts/demque/test_demque_rolling_tiers.py
data/mdpf/scripts/demque/test_demque_extend_frontier.py
data/mdpf/scripts/demque/test_demque_redraw_stale.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit; another existing test file that fails on the new rule is a surprise row asking for the grant, not an edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-52`.
<owned_cells>DQ-t-52</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t52-AC1, DQ9-t52-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~44/MDPF_DEMQUE.TO-DQ-t52.p1-only-priority-gate.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t52-AC1,DQ9-t52-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the `--census` line verbatim, which existing tests took a changed assertion and why, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; the nightly draw runs the merged code.
comp-iam: DECLARED-NOT-APPLICABLE a read of the crosswalk and transactions with the dell1 identity; no grant is requested or changed.
comp-adversary: DECLARED-NOT-APPLICABLE a refusal gate; it only removes names from a draw, never adds.
risk: LOCAL -- code and tests. It narrows what the nightly draw asks Yahoo for; the draw fails closed if the classification cannot be read.
direct_act: false -- a worker order.
</preflight>

Source: dell1 pivot packet (laptop CTO order XB-c5bf, MSTR msg 5009), outcomes O6, O12, section 6; Andrew-direct 2026-10-13; decomposition round 9.
