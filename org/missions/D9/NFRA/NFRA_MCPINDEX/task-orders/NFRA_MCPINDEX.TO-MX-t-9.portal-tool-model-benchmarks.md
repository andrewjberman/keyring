# NFRA_MCPINDEX task order -- `MX-t-9` -- a purpose-built read-only tool for the json/* model-benchmark table (mp.05), on the mdpf pattern

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-t-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~15</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only tool in an existing integration.
comp-iam: DECLARED-NOT-APPLICABLE -- the gateway role already reads opal-data-portal-v2 json/* and platinum/*.
comp-adversary: DECLARED-NOT-APPLICABLE -- the mdpf tool pattern, ruled.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 reads).
</preflight>

## 1. THE CELL -- `MX-t-9` (round 4; `org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round3.md` @f354170b42)

**Why.** FWD-2 is "portal figures equal the portal's". Round 3 proved `platinum/mdpf` end to end. `json/*`
has no purpose-built tool, so its question went unanswered in the close run.

**The act, on the portal_index pattern** (`infra/aws/ec2/opal-gateway/app/integrations/portal_index/`; read its three
mdpf tools first):
1. The surface is `json/benchmarks/model_portfolio_benchmarks.json`, catalog row `mp.05.model-portfolio-benchmarks`, which is already SERVE-WITH-CAVEAT in an approved channel. No widening.
2. One read-only tool. It reads ONE whole object whose key comes from its own catalog row, through `catalog_gate`, and
   answers with the object's own as-of date. It is a new `ROWS` entry whose `catalog_ref` names a `portal_datasets`
   row carrying `read_tool` + `accessor`, added through `catalog_entries/` and the emitter, never a hand edit.
   Classify it SAFE, like the others.
3. The answer ALWAYS carries mp.05's caveat: MODEL-DESIGN returns, never a client's realized return. It also names the benchmark basis whenever a figure is quoted.
4. **Prove the figure.** Call the tool in-process, read-only, against the served object. Read the same key by
   VersionId with `aws s3api get-object`. Record in `EQUALITY_MX-t-9.md`: the headline figure and as-of on both
   sides, and the VersionId. It is graded live at MX-r-5's r5.J1.
5. Tests in `tests/test_portal_index.py`. Run AC1 and AC2, and commit.

## 2. BOUNDS

1. Nothing is deployed; the release is MX-r-5.
2. No new served surface: mp.05 is already approved.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/portal_index/
infra/aws/ec2/opal-gateway/tests/test_portal_index.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/catalog_entries/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~15/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W15-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-t-9" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/t9.AC1.sh; echo "exit=$?"</invocation><expect>placed and naming their reader N of N with N>=4 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-t-9" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/t9.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; passed>7; failed/error 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~15/NFRA_MCPINDEX.TO-MX-t-9.portal-tool-model-benchmarks.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-3 analysis s.5 item 3a. Figure equality to the served object is graded live at MX-r-5 (r5.J1), recorded here in EQUALITY_MX-t-9.md.

<status>pending</status>
<round>4</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
