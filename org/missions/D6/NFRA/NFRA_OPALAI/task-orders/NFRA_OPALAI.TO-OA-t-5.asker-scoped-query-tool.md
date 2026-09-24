# NFRA_OPALAI task order -- `OA-t-5` -- HOP 5: every answer scoped to the ASKER, resolved by the gateway itself (C10)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-t-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~2</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE, reason measured at the cut -- the new tool reads through the gateway host's EXISTING role on the prefixes query_v0 and the policy store already read; no IAM surface is written. An action or resource the role lacks is a BLOCKING row, never a grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: AWS READ-ONLY from this box (AC2's one DynamoDB read of the policy store). No write, no deploy.
</preflight>

## 1. THE CELL -- `OA-t-5` (round 1, decomposition s.2/s.3)

Andrew-direct 2026-09-24: *"the real engineering comes in its entitlements per user/entra-id. A lot of this work has
already been done is just needs to all be synthesized cleanly."* PRD C10: every answer the Teams agent gives is scoped to
the ASKER's entitlement, never the agent's. Today the agent calls the gateway as ONE service identity, so every colleague
would get that identity's reach. **Carry the existing work; do not rebuild it:**
- the policy store and model: `app/access_state.py`, and `app/data_entitlement.py`, where records are keyed
  `POLICY#<tid>#<oid>` by Entra tenant and object id (`:1-45`: `principal_profile` + versioned `data_entitlement` grant,
  and a revoked record is a tombstone);
- the calling identity's allowlist: `app/identity_scope.py`;
- the tier model: `app/tier.py`;
- the catalog-gated fetch: `app/query_v0.py` (today reachable only as the bearer REST route `POST /query/v0`,
  `server.py:558-582`, not as an MCP tool);
- the `_run` chokepoint in `app/tools.py`.

Build, under `infra/aws/ec2/opal-gateway/`:
1. **`app/asker_scope.py`** (new) and the MCP tool **`opal_asker_query(chat_id, message_id, key, params)`**,
   registered in `app/tools.py` and classified in `app/data_entitlement.py`. That file denies any tool it does not
   classify, so add ONE classification line for the new tool, nothing else there. The tool:
   - (a) reads the Teams message `chat_id`/`message_id` ITSELF, through the calling identity's own delegated token
     (the existing graph/token_broker path), and takes the sender's Entra `tenantId` + `user.id` (oid). If the message
     has no resolvable user sender, refuse;
   - (b) loads that asker's profile and active grant through the existing store. **No profile: refuse** with a plain
     line the agent can quote, saying the asker has no access yet and how to get it (ask Andrew), reading no data;
   - (c) computes the effective scope as the INTERSECTION of the asker's grant and the calling identity's allowlist,
     so the service identity never widens what an asker may see;
   - (d) serves `key`/`params` through query_v0's catalog-gated fetch, and only within that scope;
   - (e) IGNORES any identity field the agent passes (an `asker`, `email` or `oid` argument changes nothing);
   - (f) writes an audit row with the asker oid, key and verdict, and no values.
   Measure how a catalog key maps onto the grant's scope dimensions (`datasets`, `operations`). If the model cannot
   express it without a NEW dimension, REFUSE that part with a row. Never invent a dimension.
2. **`probe_store(tid, oid, table=None) -> str`** in `asker_scope.py`: returns exactly `NO-PROFILE`, `PROFILED` or
   `STORE-UNAVAILABLE`. A missing or unreadable table is `STORE-UNAVAILABLE`, never `NO-PROFILE`. `table=None` means
   the gateway's configured policy table.
3. **`tests/test_asker_scope.py`** (new), with fakes/stubs only (`moto` is NOT installed on this box; do not install it),
   naming exactly: `test_asker_resolved_from_message_sender`, `test_unprofiled_asker_refused`,
   `test_scope_is_intersection`, `test_agent_supplied_identity_ignored`.

## 2. BOUNDS

1. Nothing is deployed by this order. The deploy is `OA-t-6`, the next order in your queue, after this one merges.
2. `/query/v0`'s REST route, every existing tool's gate, and the legacy path for unprofiled users of EXISTING tools are
   unchanged. No policy record is written.
3. At the cut, on this box: `tests/test_identity_scope.py` = 5 passed, 1 failed (`test_scoped_deny_by_default`, red
   before you start). `test_data_entitlement_guard.py` and `test_access_state.py` do not collect here (no `moto`).
4. Standing: no push, no install, no vendor call, no AWS write. REFUSE a criterion you cannot meet as written, and report
   the refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/asker_scope.py
infra/aws/ec2/opal-gateway/tests/test_asker_scope.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~2/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `app/access_state.py`, `app/identity_scope.py`, `app/tier.py`, `app/query_v0.py`, `app/graph.py`,
`app/graph_read.py`, `app/token_broker.py`, `app/context.py`, `app/refs/DATA_CATALOG.yaml`, `app/config.py` (all under
`infra/aws/ec2/opal-gateway/`).

Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W2-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-t-5"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t5.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0; named tests passed 4 of 4; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-t-5"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t5.AC2.sh; echo "exit=$?"</invocation><expect>live store: NO-PROFILE; bogus table: STORE-UNAVAILABLE -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-t-5"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/round1/checks/t5.AC3.sh; echo "exit=$?"</invocation><expect>passed>=5; failing=[test_scoped_deny_by_default] or none; failures not present at the cut=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~2/NFRA_OPALAI.TO-OA-t-5.asker-scoped-query-tool.proof_of_spec.json`. Report once: what you changed and where, the commit hash, how a catalog key maps onto the grant scope, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** C10, S10 round-1 half. Disjoint from NFRA_MCPINDEX MX-t-1 (`app/integrations/portal_index/`). The drain
runs py_compile + ruff py39 over the gateway app once.

<status>pending</status>
<round>1</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
