# TO MDPF_SECCLASS.TO-SC-e70 -- round 12 SC-e-70: READ-ONLY census of FWD-15's 99 UNPLACED-KEY entries, and a proposal

<to_id>MDPF_SECCLASS.TO-SC-e70</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~60</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-70` (`decompositions/MDPF_SECCLASS_DECOMP_R12.md`) |
**outcome_ref:** FWD-15 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-70`. CTO round-12 analysis section 3 item 4: "FWD-15's 99 UNPLACED-KEY entries (87 Cottonwood, USD 76.84M; internal ids
such as `4175_VOYA`, `CXMANUAL_HOME`): a READ-ONLY census by firm and id pattern, then a proposal of key forms or a manual-entry route.
No write this round."

**Build:**
1. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/unplaced_key_census.py`. It reads `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/e49_replan/FWD15_AI_PLAN_<firm>_20261007.json`
   (route `UNPLACED-KEY`) and groups the entries by firm and by id pattern, for example `<digits>_<word>`, `CXMANUAL_*`, other. It
   gives each group a count, its amount (USD) and up to 5 examples. It writes `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNPLACED_KEY_CENSUS_20261008.json` and prints
   `UNPLACED-CENSUS ok=<bool> total=<n> firms=<n> patterns=<n> usd=<sum>`. ok means the total is 99 and every entry is in exactly one group.
2. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNPLACED_KEY_PROPOSAL_20261008.md`. For each pattern, propose a key form the contract's `identifier_namespace` could take
   (quote the contract), or a manual-entry route. State the dollar share each covers. Propose only; write no code and no row.

### ACCEPTANCE

<criterion id="SC12-e70-AC1" cell_refs="SC-e-70"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/unplaced_key_census.py</invocation><expect>UNPLACED-CENSUS ok=True total=99</expect></criterion>
`SC12-e70-AC1` -- every UNPLACED-KEY entry is in exactly one group, total 99.

<expected_criteria>SC12-e70-AC1</expected_criteria>

Dry-run at the base (dell1 CLOUD, 2026-10-08 ~02:5xZ): SC12-e70-AC1 FAIL as expected (the census script is absent).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- Read local files only. No AWS write, and no AWS read is needed. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W60-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/unplaced_key_census.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNPLACED_KEY_CENSUS_20261008.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/UNPLACED_KEY_PROPOSAL_20261008.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R12.md</decomp_doc> (round 12), cell `SC-e-70`.
<owned_cells>SC-e-70</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC12-e70-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~60/MDPF_SECCLASS.TO-SC-e70.unplaced-key-census.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC12-e70-AC1` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE read-only, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no AWS access.
comp-adversary: RUN -- a group that double-counts (exactly-one grouping, total 99); a proposal written as a decision (propose only).
lane: the <paths> block IS the grant.
</preflight>

Source: round-12 analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_12_20261008.md @82c4790d6c section 3 item 4; CTO note msg 766; DECOMP_R12.
