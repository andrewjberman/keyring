# TO MDPF_SECCLASS.TO-SC-e7 -- round 2 SC-e-7: e18-iam-and-schedule

<to_id>MDPF_SECCLASS.TO-SC-e7</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~6</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-7` (`decompositions/MDPF_SECCLASS_DECOMP_R2.md`) |
**outcome_ref:** FWD-7 | **depends_on:** SC-e-4 (both scheduled callers)

---

## WORKER FACE

### THE CELL

`SC-e-7`, analysis item E7. FWD-7 is realized only by the ORDINARY scheduled run; the backfill was test evidence
only. BD's `E_18.detect_new_securities.py` (round 1, drained @d0e5b687f3; not yet deployed) now writes
`etf-classifications` through the scheduled module and no longer writes bd-securities. Its production principal needs
PutItem on etf-classifications and loses its bd-securities PutItem. The CTO requires a separate half for this (103098).
This runs after SC-e-4 in your worktree; COT's caller needs the same grant.

**Build (LOCAL: Terraform fmt/validate only, no plan against shared state, no apply, no deploy):**
1. **Principals.** From `infra/aws/terraform/bd-pipeline/iam.tf` (and COT's equivalent), name the principal that runs
   E_18 in production for BD and for Cottonwood.
2. **Terraform.** In `infra/aws/terraform/bd-pipeline/iam.tf`, add PutItem on `etf-classifications`, conditional on
   `attribute_not_exists` where IAM condition keys allow; otherwise state why not. Remove the bd-securities PutItem.
   Run `terraform fmt` and `terraform validate`.
3. **Schedule.** Name the ordinary schedule that runs E_18: the BD gold-layer run, with its trigger and time. The
   trigger is the schedule, never upstream success alone.
4. **Evidence and half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_E18_IAM_20260930.json` as `{"table_rows_at_build", "principal",
   "putitem_etf_classifications": true, "putitem_bd_securities": false, "fmt_ok": true, "validate_ok": true,
   "schedule"}`. Write the half `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_E18_IAM_20260930.md` for the IAM apply plus
   the E_18 code deploy (DS lane), with the first ordinary run as the acceptance.
5. **Amendment 1 (row MDPF_SECCLASS-W6-S1).** BD's round-1 `data/black_diamond/scripts/gold/E_18.detect_new_securities.py`
   computes `_REPO_ROOT` via `parents[3]`, one hop short of the repo root, so its deferred import of
   `etf_classification_scheduled` raises ModuleNotFoundError outside a test harness. SC-e-4 fixed COT's copy to
   `parents[4]`. Fix BD's the same way, and prove the import resolves when E_18 is run as a plain script from the repo
   root. Give the proof as an `import_ok: true` field in the evidence JSON, which the half cites, BEFORE the E_18
   deploy is named ready.

**Standing rulings (carried from the round-2 decomposition):**
- Andrew-direct 2026-09-30 ~02:2xZ: "yes, bd-securities values can seed new rows. THey just don't overwrite existing rows."
  So a bd-securities value may seed a NEW row and never writes into an EXISTING one. A write to an existing row from a
  bd-securities value is outside his word: stop, and name it in the half for his decision.
- CTO C-WRITER ruling (analysis @151c890591, section 1): `classified_by` is `seed` / `scheduled` / `constituents` /
  `legacy`; `seed` always wins; `scheduled` and `constituents` write only where no row exists; a missing label reads as
  `legacy`.
- The live `etf-classifications` holds 2,309 rows (release step 2, ledger CLOSED @f13cddd058). Read and print its row
  count at build time as `table_rows_at_build` in your evidence file.

### ACCEPTANCE

<criterion id="SC2-e7-AC1" cell_refs="SC-e-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CHECKS/r2_evidence.py e18</invocation><expect>E18-IAM-DESIRED</expect></criterion>
`SC2-e7-AC1` -- the grant drafted and validated, the bd-securities write removed, the schedule named.

<criterion id="SC2-e7-AC2" cell_refs="SC-e-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_E18_IAM_20260930.md</invocation><expect>HALF-READY</expect></criterion>
`SC2-e7-AC2` -- the IAM + deploy half.

<expected_criteria>SC2-e7-AC1,SC2-e7-AC2</expected_criteria>

Dry-run at the base 2026-09-30 03:1xZ (@30727a9413): SC2-e7-AC1 NOT-MET (evidence absent); SC2-e7-AC2 NOT-READY -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No table write (dry-run only), no upload, no deploy, no IAM apply, no outside-model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W6-S<k>`), and do not weaken the test to pass.

<paths>
infra/aws/terraform/bd-pipeline/iam.tf
data/black_diamond/scripts/gold/E_18.detect_new_securities.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_E18_IAM_20260930.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_E18_IAM_20260930.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R2.md</decomp_doc> (round 2), cell `SC-e-7`.
<owned_cells>SC-e-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC2-e7-AC1, SC2-e7-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~6/MDPF_SECCLASS.TO-SC-e7.e18-iam-and-schedule.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC2-e7-AC1,SC2-e7-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the principals, the IAM diff, fmt/validate lines, the schedule, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- E_18 runs in the BD gold-layer schedule; this cell names it (no schedule is created)
comp-iam: RUN -- 1 file read (infra/aws/terraform/bd-pipeline/iam.tf); BLIND: the production principals are unmeasured at the cut (this cell names them); desired only
comp-adversary: RUN -- 1 analysis read (ROUND1_ANALYSIS_MDPF_SECCLASS_20260930.md @151c890591, item E7), 1 table read (etf-classifications 2,309 rows after release step 2); BLIND: the inputs this cell names or measures are unmeasured at the cut (its census measures them).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-1 analysis @151c890591 (msg 103116), item E7; Andrew-direct 2026-09-30 ~02:2xZ.
