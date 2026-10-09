# TO MDPF_DEMQUE.TO-DQ-t8 -- round 2 DQ-t-8: Cottonwood's price build survives the absent Yahoo tier and runs in the scheduled gold chain
<to_id>MDPF_DEMQUE.TO-DQ-t8</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~7</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>superseded</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
**SUPERSEDED** by `1.0.0_SA_CTO~DELL1` msg 1368 (2026-10-09 ~01:3xZ), on the issuer's REC (msg 1366): under the FWD-1 ruling (CTO adjudication
`CTO_ADJUDICATION_MDPF_DEMQUE_20261009T0108Z.md`) MDPF_DEMQUE's store is the queue's own price store, not `canonical_prices.parquet`. The naming
gate refuses any diff to `build_canonical_prices_v2.py` keeping its existing literal (surface of the live remediation ADVI_FIRMBKTS; row
`MDPF_DEMQUE-D1-W7-S2`). The tolerant-load + optional S_00 step route to ADVI_FIRMBKTS as an input:
`deliverables/2.0.0_SA_COO~Q1/ADVI_FIRMBKTS_INPUT_S00_TOLERANT_LOAD.patch`. Worker branch `wk-MDPF_DEMQUE-7` kept, not merged.
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `DQ-t-8` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 2) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-8`, row `MDPF_DEMQUE-D1-W4-S1`: Cottonwood's canonical price build (`S_00`, `data/cot/scripts/gold/build_canonical_prices_v2.py`)
has not run since 2026-06-09, because the scheduled gold chain never calls it, and it would die if it did: `load_historical_prices()`
(`:280-287`, `get_object` at `:283`) and `load_ticker_lookup()` (`:290-298`, `get_object` at `:298`) have no missing-key branch, both
objects are absent live, and `main()` turns the error into `FATAL` and rc 1 (`:639-652`).

**Build:**

1. In `build_canonical_prices_v2.py`: when `silver/historical_prices.parquet` is absent (`NoSuchKey` / 404), `load_historical_prices()`
   prints one `WARN:` line and returns an EMPTY frame with columns `ticker, date, close`; when `config/ticker_lookup.json` is absent,
   `load_ticker_lookup()` prints one `WARN:` line and starts from an empty mapping (the in-code `YF_OVERRIDES` / `TICKER_CORRECTIONS` still
   apply). The build then continues on Tiers 1, 3, 4 and writes as it does today. Any OTHER S3 error still raises. ASCII only in output.
2. NEW `data/cot/scripts/gold/test_s00_missing_tier2.py` (pytest; stub the module's `s3` client; no AWS) with exactly these names:
   `test_missing_historical_prices_skips_tier2_and_writes`, `test_missing_ticker_lookup_skips_tier2_and_writes`,
   `test_present_tier2_is_still_joined`. Call the two loaders (and, if practical, `main()` with a stubbed client and small frames);
   assert no exception, the WARN, and the empty/present shapes.
3. In `infra/aws/terraform/cot-pipeline/ssm.tf`, document `opal-cot-gold-run`: add ONE line immediately before
   `"run_gold A_00 A_00.accounts_dimension.py ..."`:
   `"run_gold S_00 build_canonical_prices_v2.py \"$UPLOAD_FLAG\" optional",` with a one-line `#` comment above it naming MDPF_DEMQUE
   DQ-t-8 and why it is optional (a failure WARNs and the chain continues; `run_gold`'s own `optional` mode). Read `run_gold` (the
   function a few lines above) and confirm the script honours `$UPLOAD_FLAG`'s form; if it takes a different upload flag, use that and
   say so in the comment. Change nothing else in the file.

### ACCEPTANCE

<criterion id="DQ2-t8-AC1" cell_refs="DQ-t-8"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R2_CHECKS/dq_t8_tests.py</invocation><expect>S00-OK</expect></criterion>
<criterion id="DQ2-t8-AC2" cell_refs="DQ-t-8"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R2_CHECKS/dq_t8_schedule.py</invocation><expect>SCHED-OK</expect></criterion>
`DQ2-t8-AC1` -- the build survives either absent Tier-2 object and still joins a present one, by the three named tests. `DQ2-t8-AC2` --
exactly one optional S_00 step ahead of A_00, and the 18 existing steps unchanged (control arm).

<expected_criteria>DQ2-t8-AC1,DQ2-t8-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base: `S00-BAD no file ...`, `SCHED-BAD S_00 optional lines=0 (steps=18)`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No deploy, no apply:** never `aws s3 cp` the script, never `terraform init/plan/apply`, never `safe-apply`, never `safe-deploy.sh`,
  never run the gold chain or any SSM document. The upload and the apply are the issuer's acts at the drain.
- **Cottonwood (cot) is its own firm:** touch nothing of another firm.
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W7-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation
  file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/cot/scripts/gold/build_canonical_prices_v2.py
data/cot/scripts/gold/test_s00_missing_tier2.py
infra/aws/terraform/cot-pipeline/ssm.tf
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 2, the enrichment), cell `DQ-t-8`.
<owned_cells>DQ-t-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ2-t8-AC1, DQ2-t8-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~7/MDPF_DEMQUE.TO-DQ-t8.s00-scheduled-and-tolerant.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ2-t8-AC1,DQ2-t8-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the schedule `cot-bd-session-daily-et` is unchanged; only the gold-run document's step list gains one optional step, read at the drain apply.
comp-iam: DECLARED-NOT-APPLICABLE no role change; the drain's S3 upload to opal-data-cot/code/gold/ reads the dell1 user's PutObject first.
comp-adversary: DECLARED-NOT-APPLICABLE the step is optional by construction; the apply is a never-widen act at the drain.
risk: WORLD -- Terraform of a production SSM document and a production gold script; the worker edits only, the issuer deploys.
direct_act: false -- a worker order; worker-light (two small edits and one test file).
</preflight>

Source: PRD v0.3 FWD-1; row MDPF_DEMQUE-D1-W4-S1; CTO round-1 analysis item 3; decomposition round 2.
