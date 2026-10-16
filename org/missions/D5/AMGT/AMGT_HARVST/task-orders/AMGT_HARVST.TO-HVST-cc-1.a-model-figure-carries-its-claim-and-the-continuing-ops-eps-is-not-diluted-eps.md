# AMGT_HARVST task order -- `HVST-cc-1` -- ROUND 88, workstream S29-EPS: A SERVED MODEL FIGURE CARRIES ITS CLAIM, AND THE CONTINUING-OPERATIONS EPS IS NEVER PRESENTED AS REPORTED DILUTED EPS (D1-S29 defect 1; CTO round-87 analysis section 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cc-1.a-model-figure-carries-its-claim-and-the-continuing-ops-eps-is-not-diluted-eps</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~150</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO S3 call, NO AWS call, NO network, NO deploy, NO edit outside `<paths>`. The tests use the in-memory S3 fake the existing gateway tests use.
comp-adversary: RUN at L5 -- the adversary is a claim added to the code but dropped by the field projection (so the served figure still carries none), a claim that is true of the wrong mnemonic, a claim that says "reported" about the continuing-operations line, and a test that passes whatever the code does.
</preflight>

## 0. THE CELL

The gateway tool `harvest_get_fundamentals(kind="model")` serves each model-block figure projected to `FIG_FIELDS = ("mnemonic", "fiscal_year", "value", "unit", "vintage", "source", "scope")` (`infra/aws/ec2/opal-gateway/app/harvest_figures.py` line 45; `_fund_model` lines 188-211, the projection at line 201). The producer (`integrations/bloomberg/research/model_block_pull.py`) attaches a `basis` to each figure (lines 1447, 1528, 1735, 1967; `FIELD_BASIS` from line 443), but the projection STRIPS it, so a consumer cannot tell what a value is. Measured live by the CRO (2026-10-16): `IS_DIL_EPS_CONT_OPS` for `UNH_US_Equity` FY2024 reads 33.3807 against reported diluted EPS 15.51 (FY2025 15.5194 against 13.23); `BA_US_Equity` FY2025 -8.81 against reported 2.48; `IS_EPS` for UNH FY2024 15.64. The CTO ruled: **a value carries its claim; a diluted EPS from continuing operations is served under that name and is never presented as reported diluted EPS; where the vendor supplies reported diluted EPS, that is the figure labelled "diluted EPS".**

## 1. THE BUILD (LOCAL, about 120 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `infra/aws/ec2/opal-gateway/app/harvest_figures.py`:
   - add the two names `"basis"` and `"figure_claim"` to `FIG_FIELDS` (after `"scope"`) and `"basis"` to `MODEL_COLUMNS`; keep every other name and order;
   - add a module constant `FIGURE_CLAIMS` (a dict mnemonic -> text). It holds `"IS_DIL_EPS_CONT_OPS"`: `"Bloomberg's diluted EPS from continuing operations, as the vendor computes it. It is NOT the reported (GAAP) diluted EPS and can differ from it by a large factor (UNH FY2024 33.38 against reported 15.51); never quote it as diluted EPS."` Read `integrations/bloomberg/research/model_block_pull.py` `FIELD_BASIS` (and the field list around line 443) and decide whether ANY of the model-block fields is the vendor's REPORTED diluted EPS. If one is, add it to `FIGURE_CLAIMS` with the text `"Reported diluted EPS (as filed)."` and say which in your note; if none is, add nothing for it and say so (then no served figure is labelled "diluted EPS");
   - `_fund_model` builds each kept figure as `{c: f.get(c) for c in FIG_FIELDS}`: make `basis` the producer's value passed through verbatim (None when the producer attached none) and `figure_claim` = `FIGURE_CLAIMS.get(mnemonic)` (None for any other mnemonic). The key `figure_claim` is present on every served figure; the key `basis` too.
b. New test `infra/aws/ec2/opal-gateway/tests/test_cc1_model_basis.py`, offline, following the harness of `tests/test_og_gt3.py` (its recording S3 fake, its principal stand-in and its audit recorder; copy the helpers you need, edit nothing in that file):
   - (1) a model block for `UNH_US_Equity` with figures `IS_DIL_EPS_CONT_OPS` FY2024 = 33.3807 and FY2025 = 15.5194, `IS_EPS` FY2024 = 15.64, each with a producer `basis`: through the tool the `IS_DIL_EPS_CONT_OPS` figures carry a `figure_claim` containing the words `NOT the reported` and a `basis` equal to the producer's; `IS_EPS` carries `figure_claim` None;
   - (2) the same for `BA_US_Equity` FY2025 = -8.81;
   - (3) a figure whose producer attached no `basis` is served with the key `basis` present and None;
   - (4) no served figure other than the continuing-operations one carries a `figure_claim` containing the words `NOT the reported` (the claim is not leaked to the other lines);
   - (5) **A MUTANT:** with `FIG_FIELDS` monkeypatched back to the seven old names, arm (1) FAILS (assert that it does). It proves arm (1) discriminates.
c. Do not run anything against S3, AWS, a box or a browser; do not edit any other file. A surprise is a row; keep working.

<paths>
infra/aws/ec2/opal-gateway/app/harvest_figures.py
infra/aws/ec2/opal-gateway/tests/test_cc1_model_basis.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~150/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cc-1"><invocation>bash infra/aws/ec2/opal-gateway/tests/run_release_suites.sh tests/test_cc1_model_basis.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cc-1"><invocation>bash infra/aws/ec2/opal-gateway/tests/run_release_suites.sh tests/test_og_gt1.py tests/test_og_gt3.py tests/test_og_gt4.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^16 passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-16 ~15:2xZ):** AC1 FAIL as expected (the new test file does not exist); AC2 PASS as expected (`16 passed`). If your worktree's base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W150-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~150/AMGT_HARVST.TO-HVST-cc-1.a-model-figure-carries-its-claim-and-the-continuing-ops-eps-is-not-diluted-eps.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cc-1.a-model-figure-carries-its-claim-and-the-continuing-ops-eps-is-not-diluted-eps` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cc-1.a-model-figure-carries-its-claim-and-the-continuing-ops-eps-is-not-diluted-eps.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-87 analysis (`ledger/ROUND_ANALYSIS.round87.md` @4a08fffabe, msg 6766) section 1 "D1-S29: the EPS basis" and enrichment item 1; the CRO's row `D1-S29` (defect 1). Close condition (REMEDIATION_v19): the surfacing seat reads the figure on the SERVED data; this cell is LOCAL only, the deploy is `HVST-cc-7` (staged).
- **Mapped by a read-only agent (2026-10-16 ~15:0xZ):** the label is dropped at `harvest_figures.py:201` (projection); `FIELD_BASIS` at `model_block_pull.py:443-444` reads "Diluted EPS from continuing operations, Bloomberg's own definition"; `lib/research/api/model_words.py:32` already labels the line "Diluted EPS, continuing operations" (mirrors `portal/src/pages/SecurityAnalysis/modelSheet.ts` `LINE_NAMES`; this cell does not touch either). NOT established: why the vendor value is 33.38 against reported 15.51 (adjusted versus GAAP is a guess; the claim text says only what is measured: it is not the reported figure).
- **Class (gate, spine v3.19 L6):** `<paths>` names `infra/aws/ec2/opal-gateway/app/...`, an infrastructure path, so the floor is WORLD and the order is declared WORLD (the first commit attempt declared LOCAL and was REFUSED by `to-pipeline-gate`). The worker's acts stay LOCAL (code and offline tests, no deploy); the deploy is `HVST-cc-7`. It is not a direct act: it takes the full limbs and its close is the issuer's real run, `HVST-cc-7`'s served read.
- Slot ~150, worktree `C:/dev/wk-harvst-150`, branch `wk-AMGT_HARVST-150`. Widen the sparse set at provision with `org/tier1_exec/4.0.0_SA_CRO/scripts` and `infra/aws/ec2/opal-gateway`.
- **SENT:** with the round-88 issuance.

<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>88</round>
<workstream>S29-EPS</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
