# TO IRPT_BCKEND.TO-IB-pr-212 -- Every served HoldingsSnapshot contract copy re-pinned to the additive CATEGORY revision

<to_id>IRPT_BCKEND.TO-IB-pr-212</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~68</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 2.0.0_SA_COO~M msg 102599 (step 1 of
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_L0_CATEGORIES_20260929.md`;
CTO ruling 102475 on AD-01), accepted by ~P as shared packaging (~P's reply 2026-09-29T05:17Z) | **Decomp cell:** `IB-pr-212` (decomposition
section 18) | **outcome_ref:** FWD-5 (Holdings) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-pr-212` -- ~M's Holdings producer will serve a new L0 node kind, `CATEGORY` (plus a top-level
`source_vendor_keys` and an ACCOUNT `assigned_strategy`). The contract `docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`
already carries these additively at commit `a69fe8e33e`, and today's documents stay valid under it. The served
validators do not yet:
- `irpt-holdings` stages that file at pin `b3e3bcb044`;
- `irpt-ycharts-generate` stages it at pin `19d8f3038c` (both in
  `C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/lambda/ci/lambda-source-map.json`, `staged_from`,
  `packaged_as` `contracts/HoldingsSnapshot.schema.json`);
- the lambda-tree copy `infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json` is older still.

**Build:**
1. In the source map, re-pin that one `staged_from` row in BOTH functions to `a69fe8e33e`, with its `sha256` set to the
   blob's own sha256 (`git show a69fe8e33e:docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json`). Change
   no other row.
2. Replace `infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json` with that blob's bytes.
3. Prove "today's documents stay valid": validate the latest served snapshot document for each of the three firms
   (read-only S3; locate them from `infra/aws/lambda/investor-reporting/holdings/` and ~M's records) against the new
   schema. Print the result in your report.

Do NOT run build-and-upload and do NOT apply anything: the served move is the issuer's, under its own ledger and both
halves.

### ACCEPTANCE (run from your worktree root)

<criterion id="P21-2-AC1" cell_refs="IB-pr-212"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r21/p21_2_ac1_holdings_contract_repin.py" .</invocation><expect>P21-2-AC1 PASS</expect></criterion>
`P21-2-AC1` -- both functions stage the a69fe8e33e blob with its sha256, the `_contracts` copy is byte-equal to it,
and its node_kind enum carries CATEGORY plus every prior member. Base: FAIL (pins b3e3bcb044 and 19d8f3038c; copy
differs).

<expected_criteria>P21-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **No deploy, no S3 write, no Terraform.** S3 reads only for step 3.
- **Refusal clause.** If a served document fails the new schema, stop, write it in your report and a surprise row,
  and do not edit the schema.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 18 (round 21, workstream ~P), cell `IB-pr-212`.
<owned_cells>IB-pr-212</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: P21-2-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~68/IRPT_BCKEND.TO-IB-pr-212.holdings-contract-category-repin.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> P21-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message: the commit hash, the criterion's last line, the three served-document validation
lines, and any surprise row id (`IRPT_BCKEND-W68-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- 0 roles touched.
comp-blast: RUN -- two served functions' staged contract pin + the lambda-tree copy; additive enum; the served move (issuer) re-reads each function's validation.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache.
comp-adversary: RUN -- P21-2-AC1 dry-run at the base: FAIL (irpt-holdings pin b3e3bcb044, irpt-ycharts-generate pin 19d8f3038c, _contracts copy differs, CATEGORY absent).
lane: the <paths> block IS the grant.
</preflight>
