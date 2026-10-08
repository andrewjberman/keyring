# TO MDPF_SECCLASS.TO-SC-e75 -- round 14 SC-e-75: the BD gold writer that still serves multi_asset, traced and routed through the six classes

<to_id>MDPF_SECCLASS.TO-SC-e75</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~65</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-75` (`decompositions/MDPF_SECCLASS_DECOMP_R14.md`) |
**outcome_ref:** FWD-16 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-75`, row `MDPF_SECCLASS-D1-S9`. After the six-class switch, Black Diamond's client concentration files still serve the retired
class `multi_asset`.

**Measured 2026-10-08 ~18:1xZ** (record `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/SERVED_MULTI_ASSET_SPLIT_20261008T1810Z.json`):
- 36 keys under `s3://opal-data-bd/platinum/clients/*/concentration.json`, written 2026-10-08 00:50-05:51Z, carry `multi_asset`.
- By ticker: ABALX 12, AMECX 9, CAIBX 9, SCGB1 5, and 88 items with no ticker.
- On 10-07 ~16:5xZ the same census read 0 post-switch hits.
- The canonical table holds 0 multi_asset rows.
- `comp-find 'multi_asset'` over `data/black_diamond`, `data/cot` and `_shared` reads 0 definition hits, so the value is not a source
  literal.

**Build:**
1. TRACE. Find the code that puts `multi_asset` on those items. Read the writer `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`.
   Compare the deployed bytes against the repo by content: `aws s3 cp s3://opal-data-bd/code/gold/<file> -` against `git show HEAD:<file>`,
   for D_04 and each module it imports for the class. Read the class inputs D_04 reads (`comp-pipescript io D_04.client_portal_summary.py`).
   Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_MULTI_ASSET_TRACE_20261008.md`. It must name:
   - the first file:line, or the input object, where the value enters;
   - the deployed-vs-repo result per file, with the denominator printed.
2. FIX, only if the source is `D_04.client_portal_summary.py`: route the class through the six-class mapping, so that no item can
   carry a class outside {equity, fixed_income, cash, alternatives, structured, commodities} (or `unclassified`). If the source is
   another file or an input object, STOP after step 1 and file a row. The issuer re-points.
3. Write `data/black_diamond/scripts/gold/tests/test_d04_bd_no_multi_asset.py`. It must cover:
   - an item whose input class is `multi_asset` (or the traced form) comes out inside the six classes;
   - a control: an `equity` item keeps its class.
4. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_MULTI_ASSET_20261008.md`,
   shaped like the other half requests in that folder. It must name:
   - `## The act`: the deploy of the fixed file to `s3://opal-data-bd/code/gold/`, then the next scheduled BD gold fire;
   - `## Blast radius`: the served concentration files and which items move, with a local candidate diff on one hit client's input;
   - `Rollback per key`: the prior code VersionId.
   Leave both halves unsigned.

### ACCEPTANCE

<criterion id="SC14-e75-AC1" cell_refs="SC-e-75"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests/test_c06_retained_dates_six_class.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC14-e75-AC1` -- the new pin passes: the traced multi_asset input lands inside the six classes, and the equity control holds.
<criterion id="SC14-e75-AC2" cell_refs="SC-e-75"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_MULTI_ASSET_20261008.md</invocation><expect>HALF-READY</expect></criterion>
`SC14-e75-AC2` -- the half request carries the act, the blast radius with a candidate diff, and the rollback per key.
<criterion id="SC14-e75-AC3" cell_refs="SC-e-75"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC14-e75-AC3` -- the whole BD gold suite still passes, the new pin included.

<expected_criteria>SC14-e75-AC1,SC14-e75-AC2,SC14-e75-AC3</expected_criteria>

JUDGMENT, not self-graded: 3.0.0_SA_CVO grades at L9 whether the trace names the true first entry point of the value.

Dry-run at the base (dell1 CLOUD, 2026-10-08 ~18:4xZ):
- SC14-e75-AC1: FAIL, as expected (the test file is absent).
- SC14-e75-AC2: FAIL, as expected (NOT-READY: the half is absent).
- SC14-e75-AC3: PASS, as expected (control, 76 passed).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY.** S3 get/list and `comp-pipescript` reads only.
  - No `aws s3 cp` TO any bucket, no deploy, no table write, no Lambda or Step Functions invoke. Never push.
  - Use the `.tools/aws` shim.
- **Refusal clause.** If a criterion cannot be met as written, or the source is outside `D_04.client_portal_summary.py`, stop. Write
  the reason in your report and file a surprise row (id `MDPF_SECCLASS-W65-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not
  weaken the test.

<paths>
data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py
data/black_diamond/scripts/gold/tests/test_c06_retained_dates_six_class.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_MULTI_ASSET_TRACE_20261008.md
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_MULTI_ASSET_20261008.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R14.md</decomp_doc> (round 14), cell `SC-e-75`.
<owned_cells>SC-e-75</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC14-e75-AC1, SC14-e75-AC2, SC14-e75-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~65/MDPF_SECCLASS.TO-SC-e75.bd-gold-no-multi-asset.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC14-e75-AC1,SC14-e75-AC2,SC14-e75-AC3`. Record a
judgment criterion as `UNVERIFIABLE-BY-INSTRUMENT`, with a `status_reason` naming 3.0.0_SA_CVO, never as PASS or FAIL.
</proof_of_spec>

**REPORT:** what you read and changed (file:line), the trace result, each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the deploy and the leg-G served read are the issuer's acts under the pair, after the next scheduled BD gold fire.
comp-iam: DECLARED-NOT-APPLICABLE no grant change (S3 reads under the seat's existing role).
comp-adversary: RUN -- running bytes older than the repo (deployed-vs-repo by content); an input object carrying the class rather than code; BLIND: COT's twin (SC-e-67, round 12) and other BD platinum writers than D_04.
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO~DELL1 msg 1050 (DECISION, SELF-DRIVE tick 18); row MDPF_SECCLASS-D1-S9 @90d90b9dc8; DECOMP_R14 (cut as round 14: round 13 already holds the e74 issuance).

### AMENDMENT 1 -- re-point to C_06's incremental merge (issuer 2.0.0_SA_COO~M1, 2026-10-08 ~19:0xZ; row MDPF_SECCLASS-D1-W65-S1)

The worker's trace (`BD_MULTI_ASSET_TRACE_20261008.md` @623e08ca6b) found the following:
- D_04 copies `concentration` unchanged from the C_06 envelope `gold/entities/clients/{rel_id}.json` (D_04:1192, :1208).
- The value sits on dated entries 2026-10-03 to 10-05: 141 holdings across the 36 keys. They were classified from the table before the
  remap (commit 0d9457b639, 10-07 07:10Z).
- C_06's incremental merge (`C_06.client_mix_timeseries.py` ~:731-740) rewrites only the dates in new partitions, so those retained
  entries are never reclassified.
- Deployed bytes equal the repo on 9 of 9 files.
Of the trace's three options, this seat chooses the fix at the writer, so the next scheduled fire heals all 36 files. A D_04 guard
would mask the cause, and a hand rewrite of envelopes edits served data by hand.

Steps 2-3, replaced:
2. FIX in `C_06.client_mix_timeseries.py`'s merge. A RETAINED dated entry (one not rebuilt this run) with any holding whose class is
   outside the six {equity, fixed_income, cash, alternatives, structured, commodities} (or `unclassified`):
   - reclassify that holding through the same classifier call C_06 uses for new dates (~:228), by its ticker and name;
   - recompute that date's mix class totals from the reclassified holdings;
   - leave market values, weights, dates and any entry already inside the six unchanged.
   Print one census line per run, e.g. `C06-RETAINED-RECLASS entries=<n> holdings=<n>`.
3. Write `data/black_diamond/scripts/gold/tests/test_c06_retained_dates_six_class.py`. It must cover:
   - a retained entry holding `multi_asset` comes out inside the six, with its date's mix totals consistent;
   - a retained entry already inside the six is byte-identical after the merge (the control).
Step 4 (the half request) stands. Its act is the deploy of C_06 to `s3://opal-data-bd/code/gold/`, then the next scheduled BD gold
fire. The blast radius names the 36 keys, the 141 holdings, and a local candidate diff on z08119861's envelope. AC1 now runs the new C_06
test. The <paths> grant swaps D_04 and its test for C_06 and its test. AC2, AC3 and the bounds are unchanged.
Gate limb: none grades an amendment to an existing order.

