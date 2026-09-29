# NFRA_MCPINDEX task order -- `MX-d-4` -- opal_discover names the purpose-built tool as next_tool (R-13) and carries a measured served_written_at (R-14)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-d-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~14</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change to one gateway integration.
comp-iam: DECLARED-NOT-APPLICABLE -- served_written_at uses the gateway role's existing s3:GetObject/HeadObject on opal-data-portal-v2 json/* and platinum/*; no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- both changes are ruled (R-13, R-14).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (one S3 HEAD per servable row returned).
</preflight>

## 1. THE CELL -- `MX-d-4` (round 4; `org/missions/D9/NFRA/NFRA_MCPINDEX/ledger/ROUND_ANALYSIS.round3.md` @f354170b42)

**Why.** Round 3's close run (`deliverables/2.0.0_SA_COO~MI/round3/CLOSE_RUN_MX-r-4_ISSUER.md`) found two gaps:
- every `next_tool` opal_discover names is `query_v0`, even for mp.01, whose own tool `mdpf_get_aum_metrics` answered
  correctly (Z-C-S28);
- `latest_value` is the catalog's certification vintage (2026-08-10) while the object is 2026-09-25 (Z-C-S29).
The CTO ruled R-13 and R-14. Read both in the analysis, section 3.

**The act, in `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/`:**
1. **R-13.** Where a catalog row declares a purpose-built accessor, `next_tool` names THAT tool with its exact
   arguments. mp.01 names `mdpf_get_aum_metrics` with `{scope: global}`, and each portal_index row likewise. Resolve
   the tool from the catalog's `portal_datasets` rows (`read_tool` + `accessor`, MX-x-2), never from a hardcoded list.
   - `query_v0` is named only for a row with no purpose-built tool.
   - When `query_v0` is named, the answer says it is an HTTP route (`POST /query/v0`), not an MCP tool.
2. **R-14.** Keep `latest_value` (claim `held`). For each SERVABLE row returned, add `freshness.served_written_at`:
   - the served object's S3 `LastModified` from ONE HEAD, as `{value, claim: "measured"}`;
   - on a failed HEAD, `{claim: "absent", error_class}`.
   Never parse the object. For a family key, HEAD the member the principal resolves, or report `absent` with an
   error_class that says why.
3. Tests in `tests/test_opal_discover.py` pin both rules on a synthetic catalog. The HEAD is injectable, so a test
   needs no network.
4. Run AC1-AC3. Commit under your serial.

## 2. BOUNDS

1. Nothing is deployed; the release is MX-r-5. The catalog is not hand-edited.
2. The harness and its question set are READ, never edited.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~14/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W14-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-d-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/d4.AC1.sh; echo "exit=$?"</invocation><expect>match mp.01.aum-metrics next_tool=mdpf_get_aum_metrics args={"scope": "global"} -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-d-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/d4.AC2.sh; echo "exit=$?"</invocation><expect>servable rows carrying served_written_at (measured, or absent with error_class): N of N, N>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-d-4" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round4/checks/d4.AC3.sh; echo "exit=$?"</invocation><expect>plain run rc=0 ROUTING k of 27 with k>=23 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~14/NFRA_MCPINDEX.TO-MX-d-4.discover-route-to-tool.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-3 analysis s.5 item 2 (build half; the release is MX-r-5). Dry-run at base: see the issuance commit. Chain: MX-d-4 -> MX-d-5 -> MX-r-5 on worker ~14.

<status>pending</status>
<round>4</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
