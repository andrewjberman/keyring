# TO MDPF_SECCLASS.TO-SC-e68 -- round 12 SC-e-68: the canonical CASH row to cash/Cash: writer, dry run and half request

<to_id>MDPF_SECCLASS.TO-SC-e68</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~58</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-68` (`decompositions/MDPF_SECCLASS_DECOMP_R12.md`) |
**outcome_ref:** FWD-2, FWD-16 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-68`. CTO round-12 analysis section 3 item 2: "The `CASH` row to `cash`/`Cash`, by a conditional update on
`classified_by = legacy` under its own never-widen pair, with the served mix delta named (e42 condition 5)."

**Measured:** the etf-classifications row `CASH` reads fixed_income / Ultra Short Duration, classified_by legacy, name
"Cash & Cash Equivalents". It is the largest open mis-class by dollars (Cottonwood -$5.48M in the e42 compare).

**Build:**
1. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/cash_row_write.py`, shaped like `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_write_v2.py`:
   - dry run by default, with a guarded client that refuses any write;
   - `--write --half <file> --snapshot <path>`, one `update_item` on key `CASH` setting asset_class `cash`, sub_asset_class `Cash`
     and an `updated_by` you name, conditioned on `classified_by = legacy` AND the current asset_class and sub_asset_class;
   - `--rollback <snapshot> [--write]`, which puts the snapshot values back under the reverse condition.
   The dry run prints `CASH-ROW-DRY-RUN write=<0|1> current=<class>/<sub> classified_by=<v> puts=0`.
2. Write the half request `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CASH_ROW_20261008.md`, shaped like
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CLEAN_NAMES_V2_20261007.md`. It names:
   - the one row and its before and after values;
   - the served mix delta, per firm. Name which served files read the CASH key. A firm bucket dell1 cannot read is written as UNREAD,
     with the seat that can read it;
   - both branches (the row moves, or the condition refuses);
   - the rollback by snapshot;
   - which writers can touch that key.

### ACCEPTANCE

<criterion id="SC12-e68-AC1" cell_refs="SC-e-68"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/cash_row_write.py</invocation><expect>CASH-ROW-DRY-RUN write=1</expect></criterion>
`SC12-e68-AC1` -- the writer's dry run plans the one conditional update and makes no write.
<criterion id="SC12-e68-AC2" cell_refs="SC-e-68"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CASH_ROW_20261008.md</invocation><expect>HALF-READY</expect></criterion>
`SC12-e68-AC2` -- the half request is ready to sign.

<expected_criteria>SC12-e68-AC1,SC12-e68-AC2</expected_criteria>

Dry-run at the base (dell1 CLOUD, 2026-10-08 ~02:5xZ): SC12-e68-AC1 FAIL as expected (the writer is absent); SC12-e68-AC2 FAIL as expected (NOT-READY: absent).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- No table write: run only the dry run. The write is the issuer's act under the signed pair. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W58-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/cash_row_write.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CASH_ROW_20261008.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R12.md</decomp_doc> (round 12), cell `SC-e-68`.
<owned_cells>SC-e-68</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC12-e68-AC1, SC12-e68-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~58/MDPF_SECCLASS.TO-SC-e68.cash-row-to-cash.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC12-e68-AC1,SC12-e68-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE an ad-hoc issuer act, run outside any E_18 window.
comp-iam: DECLARED-NOT-APPLICABLE dell1 already writes etf-classifications (e48, e49, e32).
comp-adversary: RUN -- a second writer racing the key (the condition on classified_by and the current class); a served mix moved unseen (the half names the delta per firm); no way back (snapshot rollback); BLIND: the 49F and Cottonwood served mix files, which dell1 cannot read (the half marks them UNREAD).
lane: the <paths> block IS the grant.
</preflight>

Source: round-12 analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_12_20261008.md @82c4790d6c section 3 item 2; CTO note msg 766; DECOMP_R12.
