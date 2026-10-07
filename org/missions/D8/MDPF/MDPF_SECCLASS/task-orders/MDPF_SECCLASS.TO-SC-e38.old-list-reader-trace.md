# TO MDPF_SECCLASS.TO-SC-e38 -- round 8 SC-e-38: FWD-5 -- the trace of who reads the old list, each reader with the artifact or call it reads and a verdict

<to_id>MDPF_SECCLASS.TO-SC-e38</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~25</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-38` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none (R8: independent). Slot ~25's second order, after `TO-SC-e26`.

---

## WORKER FACE

### THE CELL

`SC-e-38`: the trace of who reads the old list -- Advisor Intelligence's screens, the news curation function (PRD surface S22) and
`resolve_tickers.py` (S25) -- each with the artifact or call it reads and a verdict. A READ-ONLY trace: no code edit.

- FWD-5 (PRD v0.12): "The old Black Diamond copy of the list is gone, and it can be shown that nothing needed it." Reader switches
  and the delete are later rounds (the delete is Andrew's act at the end, C-DELETE).
- PRD surfaces: S22 `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py`, "a reader of the old list" (held from
  the brief); S25 `data/black_diamond/scripts/classification/resolve_tickers.py` (held, the Black Diamond chain); S06/S17/S18 are
  the old list's writers and table (retired by `SC-e-35`..`SC-e-37`, not traced here except where they also read).
- **The old list** is DynamoDB `bd-securities`, us-east-1, hash key `ticker`.

**Leads measured by the issuer 2026-10-07** (`git grep -l bd-securities` over a scoped set; a lead, NOT the census -- build the
denominator yourself): `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py`;
`data/black_diamond/scripts/classification/resolve_tickers.py`;
`infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/{lambda_function.py,etf_classifier.py}` (a candidate for the
Advisor Intelligence screens' backend); `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`;
`infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py`; tests under `infra/aws/lambda/v2_portal/_shared/tests/`.
Also read the IRPT Holdings fallback (`data/assets/scripts/gold/investor_reporting/bd_securities_fallback.py`, PRD S21) and name
it; its removal is FWD-13's, not this cell's.

**Build:**
1. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reader_trace.py`: the census -- every repo file
   that names `bd-securities` (the table name, its env var, or the ARN), via `comp-find` with its denominator, plus the live
   plane: `comp-find --corpus aws 'bd-securities'` for the IAM policies and functions that can read it. It prints
   `DENOMINATOR: <files scanned> files, <hits> hits; aws nodes <n>` and the reader list.
2. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_READER_TRACE_<YYYYMMDD>.md` in exactly this grammar (the
   issuer's check reads it): one line `DENOMINATOR: ...`; then per reader a section headed `## READER: <name or path>` holding
   exactly one `READS:` line (the table, a derived artifact or a call; which attributes), one `EVIDENCE: <repo path>:<line>` (a
   path that exists at HEAD) and one `VERDICT:` line with one of `NEEDS-OLD-LIST` | `REPOINTABLE` | `DEAD-READ` |
   `NOT-A-READER`, followed by one sentence of reason. Sections are REQUIRED for the Advisor Intelligence screens (heading must
   contain "Advisor"), `semantic-news-layer3-curation` and `resolve_tickers.py`, plus one per further reader your census finds.
   For a deployed function, say whether the deployed config reads the table (the env var on the live function, read-only).
3. ASCII only.

### ACCEPTANCE

<criterion id="SC8-e38-AC1" cell_refs="SC-e-38"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/issuer_check_sc_e38.py</invocation><expect>SC-E38-TRACE ok=True</expect></criterion>
`SC8-e38-AC1` -- the trace carries a denominator and one well-formed section per reader, the three named readers included, each with evidence at HEAD and a verdict from the closed set.

<expected_criteria>SC8-e38-AC1</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`no OLD_LIST_READER_TRACE_*.md`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`,
  uncommitted. `R10_CHECKS/issuer_check_sc_e38.py` is READ-ONLY to you.
- **Read-only.** No code edit to any reader, no table or S3 write, no deploy, no invocation of a live function. Reading a deployed
  function's configuration is allowed. No vendor or model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W25-S<k>`), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reader_trace.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_READER_TRACE_*.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-38`.
<owned_cells>SC-e-38</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e38-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~25/MDPF_SECCLASS.TO-SC-e38.old-list-reader-trace.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e38-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the denominator, the reader list with verdicts, any reader the PRD's surface manifest does not name, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (2026-10-07 ~07:3xZ): no gate names a reader trace. A read-only cell arms nothing.
comp-iam: RUN -- R8 battery (comp-iam gaps): 0 gap lines name bd-securities; the worker's live-plane read (comp-find --corpus aws) covers the grants Terraform does not declare.
comp-adversary: RUN -- R8 battery; issuer leads 2026-10-07: git grep -l bd-securities over portal/src, v2_portal, the S22 function and S25 found 10 files (S22, S25, opal-partners-data x2, _shared x4, yang set-instrument-kind). BLIND: readers outside that scope (the worker's census sweeps the whole repo).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.12 @87ad6d2e4c (FWD-5, surfaces S06, S17, S18, S21, S22, S25); DECOMP_R8 @495efa3c32.
