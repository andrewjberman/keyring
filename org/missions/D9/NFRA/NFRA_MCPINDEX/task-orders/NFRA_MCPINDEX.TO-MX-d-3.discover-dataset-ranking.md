# NFRA_MCPINDEX task order -- `MX-d-3` -- the discover family routes a dataset ask to its dataset FIRST (row Z-W2-S8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-d-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~10</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change to one gateway integration; no schedule, cron, alarm or monitor.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS, no role.
comp-adversary: DECLARED-NOT-APPLICABLE -- the defect is measured (row Z-W2-S8) and graded on an existing harness.
EGRESS CLASS, declared: NONE. Offline code and tests only.
</preflight>

## 1. THE CELL -- `MX-d-3` (round 3, enrichment item 3, first step)

**Why.** The discover family (`infra/aws/ec2/opal-gateway/app/integrations/opal_discover/`) routes 21 of 27 real
staff asks correctly on the MX-v-6 harness. But all 21 hits are asks for something the catalog does NOT hold, answered
NOT_CATALOGUED. Of the 3 asks whose expected answer is a DATASET (Q05, Q07, Q22), 0 route to it first.

Row Z-W2-S8 names three miss signatures:
- one common word selects a whole channel (3 misses);
- an unranked channel puts the served dataset behind catalog order (2);
- an index ask matches no keyword (1).

**The act:**
1. Run the harness and read every miss:
   `python infra/aws/ec2/opal-gateway/tests/routing/run_routing.py`. Classify each of the 6 misses by signature.
2. Fix the RANKING inside `opal_discover`, so that a dataset ask ranks its dataset first. Do not special-case
   question ids or their words, and do not edit the question set (`tests/routing/questions.yaml`) or the harness. The
   fix is a rule a reviewer can state in one sentence. Put that sentence in your report.
3. Add or extend tests in `tests/test_opal_discover.py` that pin the rule on a synthetic catalog, never on the harness's
   own questions.
4. Run AC1-AC3. Commit under your serial.

## 2. BOUNDS

1. Nothing is deployed. The catalog (`app/refs/DATA_CATALOG.yaml`) is never edited.
2. The harness, the question set and every other integration are READ, never edited.
3. No AWS, no vendor, no push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~10/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W10-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-d-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/d3.AC1.sh; echo "exit=$?"</invocation><expect>plain run rc=0 ROUTING k of 27 with k>=21 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-d-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/d3.AC2.sh; echo "exit=$?"</invocation><expect>harness rc=0; dataset asks routed first k of 3 with k>=2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-d-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/d3.AC3.sh; echo "exit=$?"</invocation><expect>pytest rc=0; passed>=1; failed/error 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~10/NFRA_MCPINDEX.TO-MX-d-3.discover-dataset-ranking.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once: the one-sentence rule, the per-miss signature table
(before and after), the commit hashes, and any row. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-2 analysis s.5 item 3, first step: "a ranking fix for Z-W2-S8 (dataset asks
route first), graded on MX-v-6's harness: ROUTING >= 21 of 27, dataset asks >= 2 of 3".
- Dry-run at base: d3.AC1 PASS (21 of 27; a regression guard); d3.AC2 FAIL (0 of 3: Q05, Q07, Q22 MISS); d3.AC3 PASS
  (4 passed; a regression guard).
- d3.AC3's pytest bound is 300 s: at 110 s it timed out once under box load, although the suite runs in 10 s alone.
- Chain: MX-d-3 -> MX-r-4. The enable release carries this fix.

<status>complete -- issuer-graded on CLOUD after the drain @1328566f78 by 2.0.0_SA_COO~MI, 2026-09-28 ~21:4xZ: d3.AC1 PASS (ROUTING 23 of 27), d3.AC2 PASS (dataset asks 2 of 3: Q05, Q07 HIT; Q22 MISS), d3.AC3 PASS (8 passed), instance VALID. Worker control: 2 of the 4 new ranking tests FAIL on the pre-fix integration. Row Z-W10-S1 records the 4 residual misses as catalog vocabulary and precision defects, not ranking. Was: pending.</status>
<round>3</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
