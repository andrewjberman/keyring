# TO MDPF_SECCLASS.TO-SC-e71 -- round 12 SC-e-71: the 12 SEED-SOURCE names read clean_name()'s output

<to_id>MDPF_SECCLASS.TO-SC-e71</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~61</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-71` (`decompositions/MDPF_SECCLASS_DECOMP_R12.md`) |
**outcome_ref:** FWD-14, FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-71`. CTO round-12 analysis section 3 item 5: "The 12 SEED-SOURCE names (e48's list, AAETX through VTTHX), corrected in
`etf_classification.py`'s seed source with `clean_name()`'s output and pinned by test." A seed row always wins over the table, so these
names stay wrong until the seed source changes.

**Measured:** the 12 keys are the SEED-SOURCE rows of `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_V2_20261007.tsv`.
Their names sit all-caps in `infra/aws/lambda/v2_portal/_shared/etf_classification.py` `ETF_NAME_OVERRIDES` (~:937).

**Build:**
1. In `ETF_NAME_OVERRIDES`, set each of the 12 keys' name to `clean_name(<its current value>)`, using
   `infra/aws/lambda/v2_portal/_shared/security_name.py` (R12c, ASCII only). Change no other key and no class.
2. Write `infra/aws/lambda/v2_portal/_shared/tests/test_seed_names_clean.py`. It pins all 12 names, and the difference control that
   one untouched key keeps its exact value.

### ACCEPTANCE

<criterion id="SC12-e71-AC1" cell_refs="SC-e-71"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/sc_r12_seed_names.py</invocation><expect>SEED-NAMES ok=True</expect></criterion>
`SC12-e71-AC1` -- all 12 seed names equal clean_name()'s output.
<criterion id="SC12-e71-AC2" cell_refs="SC-e-71"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py infra/aws/lambda/v2_portal/_shared/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC12-e71-AC2` -- the whole _shared suite still passes, the new pin included.

<expected_criteria>SC12-e71-AC1,SC12-e71-AC2</expected_criteria>

Dry-run at the base (dell1 CLOUD, 2026-10-08 ~02:5xZ): SC12-e71-AC1 FAIL as expected (SEED-NAMES ok=False match=0); SC12-e71-AC2 PASS as expected (control, 328 passed).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- No deploy: a shipped `_shared` member to a firm code prefix waits on limit item 5. No table write. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W61-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
infra/aws/lambda/v2_portal/_shared/etf_classification.py
infra/aws/lambda/v2_portal/_shared/tests/test_seed_names_clean.py
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R12.md</decomp_doc> (round 12), cell `SC-e-71`.
<owned_cells>SC-e-71</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC12-e71-AC1, SC12-e71-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~61/MDPF_SECCLASS.TO-SC-e71.seed-source-names-clean.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC12-e71-AC1,SC12-e71-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the deploy and the seed write follow under their pair when item 5 lifts.
comp-iam: DECLARED-NOT-APPLICABLE no grant change.
comp-adversary: RUN -- touching another key (the control); a non-ASCII name (R12c's clean_name); BLIND: the seed write that carries these names to the table (its own pair).
lane: the <paths> block IS the grant.
</preflight>

Source: round-12 analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_12_20261008.md @82c4790d6c section 3 item 5; CTO note msg 766; DECOMP_R12.
