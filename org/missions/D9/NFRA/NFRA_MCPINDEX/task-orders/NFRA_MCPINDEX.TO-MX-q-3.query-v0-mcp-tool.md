# NFRA_MCPINDEX task order -- `MX-q-3` -- `query_v0` becomes an MCP tool under C2, and discover names it instead of the HTTP route

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-q-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~20</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the tool calls the existing query_v0 handler under the gateway's existing opal-data-portal-v2 read; no role or policy changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the portal_index tool pattern, ruled (MX-t-9).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 reads).
</preflight>

## 1. THE CELL -- `MX-q-3` (round 5; `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/REINSTATE_RULINGS_20260930.md` @4e598ab7be, ruling B7)

**Why.** `query_v0` is the typed fallback for every catalogued row with no purpose-built tool. Today it is only an HTTP
route (`app/query_v0.py`, `handle` at :112, caps at :52-56; `app/server.py:658` and :960). Claude cannot call it, so
discover's `next_tool` for those rows names a route Claude cannot reach. At the cut, in-process on CLOUD,
`opal_discover('macro data')` names `query_v0` with `kind: http_route` for mac.01, and so do att.01, att.02, att.04 and
ft.04.

**The act:**
1. Add ONE read-only MCP tool in the `portal_index` integration (`app/integrations/portal_index/integration.py`,
   `register()` at :288-316) that calls the SAME handler path as the route. It keeps the same catalog gate, the same
   caps, typed `{key, params}` arguments only, never raw SQL, and the same audit line. Give it a name valid under the
   PRD's tool-name rule C3 (`{system}_{function}[_{qualifier}]`, scope as an argument) and record the name in your report.
2. **C2, in full** (`org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md:220-225`): tag it SAFE (`_SAFE_TAG`), enter it in
   `app/destructive_ops.py` and in `app/data_entitlement.py` `INDEX_TOOLS`, and move the pinned tool-count tests by one
   (`tests/test_entitlement_admin.py:347-348,361`, `tests/test_portal_index.py:45`). Add only this tool's name; MX-t-10
   adds its own names separately.
3. In `app/integrations/opal_discover/integration.py`, a row with no purpose-built tool names the new tool as
   `next_tool` with `kind: mcp_tool` and args carrying the row's key. The HTTP route stays and is not removed. Update the
   expectation at `tests/test_opal_discover.py:283`.
4. Tests in `tests/test_query_v0_tool.py` with exactly these names: `test_mx_q3_tool_registered_safe`,
   `test_mx_q3_uncatalogued_key_refused`, `test_mx_q3_entitled`, `test_mx_q3_same_answer_as_route` (the tool's answer
   equals the route's for the same key and params). Run AC1 and AC2, and commit.

## 2. BOUNDS

1. Nothing is deployed; the release is MX-r-6.
2. No new served surface and no identity, grant or sign-in change. The route's caps and gate are reused, never loosened.
3. Pre-existing failure at the cut: `tests/test_entitlement_admin.py::test_ogz2_ac06`. Leave it as found; it is not
   yours unless your change moves it.
4. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/portal_index/
infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/tests/test_query_v0_tool.py
infra/aws/ec2/opal-gateway/tests/test_opal_discover.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
infra/aws/ec2/opal-gateway/tests/test_portal_index.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~20/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W20-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-q-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/q3.AC1.sh; echo "exit=$?"</invocation><expect>mac.01 next_tool is not query_v0, kind=mcp_tool, defined as a function in app/integrations in 1 or more files -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-q-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/q3.AC2.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 4 of 4; failed/error tests 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~20/NFRA_MCPINDEX.TO-MX-q-3.query-v0-mcp-tool.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Reinstatement ruling B7 and round-5 order item 3. Dry-run at base: q3.AC1 FAIL
(mac.01 next_tool=query_v0 kind=http_route), q3.AC2 FAIL (file absent). Rides MX-r-6.

<status>complete -- issuer-graded on CLOUD after the drain @b26d0b3ae0 by 2.0.0_SA_COO~MI, 2026-09-30 ~10:3xZ: q3.AC1 PASS (mac.01 next_tool=gateway_query_catalog kind=mcp_tool; 5 of 5 route-only rows name it), q3.AC2 PASS (4 of 4 named tests, 0 failed), instance VALID. Tool gateway_query_catalog in portal_index on query_v0.handle (same gate, caps, audit); pins 52->53, portal_index 4->5. The first ~20 session left no writes in two ticks and was stopped; this is the reseat's work. Rows Z-W20-S1/S2 INERT. Rides MX-r-6. Was: pending.</status>
<round>5</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
