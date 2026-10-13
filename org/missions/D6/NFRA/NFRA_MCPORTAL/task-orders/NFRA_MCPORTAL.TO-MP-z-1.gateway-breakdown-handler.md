# NFRA_MCPORTAL task order -- `MP-z-1` -- WORKSTREAM GW ROUND 1: the owner-gated gateway breakdown handler (FWD-20)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-z-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-z-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~13</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request handler; no cron, alarm, monitor or cadence (PRD C8: read when opened).
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes no IAM. The one read it needs on the grant store (dynamodb:Scan) is MP-z-4's grant, applied by another seat; every test here uses a fake client.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (unclassified tool, unrated channel, no holder, kill switch, unreadable store, non-owner, the chain equality with its difference control).
EGRESS CLASS, declared: none. No AWS call is made by this cell; every store read in a test is a fake client.
</preflight>

## 1. THE CELL -- `MP-z-1` (workstream GW round 1, decomposition sections GW.1 and GW.3)

Your worktree is `C:/tmp/mp-gw-13` (branch `wk-NFRA_MCPORTAL-gw-13`). Work and commit only there.

Andrew wants ONE page that shows the gateway's full breakdown: every vendor or channel, the tools and catalog indexes on
each, and who is entitled to each today (PRD v0.7 FWD-20). The rule that binds everything here (PRD C15): the map is
GENERATED from the gateway's own definitions and decision code. No hand-kept list of channels, tools or people, and no
re-typed copy of an access rule. A parallel cell builds the page against the response below, so do not rename or drop
a field.

Build, in the gateway app at `infra/aws/ec2/opal-gateway/`:

1. **`app/admin_gateway_breakdown.py` (new).** It has ONE handler, `breakdown`, decorated with `owner_gate.owner_only`,
   and a module function `_compute(scan_client=None, store=None)` that returns the body (a release check calls
   `_compute()` on the host). Run `_compute` in `run_in_threadpool`, as `app/admin_fabric.py` `boxes` does. The body,
   exactly:
   ```
   { "read_at": "<ISO Z>",
     "kill_switch": true | false,
     "channels": [
       { "id": "m365" | "<integration spec id>",
         "name": "Microsoft 365" | "<spec.display_name>",
         "kind": "native" | "integration",
         "auth": "delegated" | "<spec.auth_kind value>",
         "min_tier": "<spec.min_tier>" | "per tool",
         "rating": {"value": "<R0..R4>" | "unrated", "reason": "<text>" | null},
         "tools": [ { "name": "<tool>", "access": "read" | "write",
                      "write_class": "<destructive_ops.write_class(tool)>" | null,
                      "data_class": "<data_entitlement.classify(tool)>" | "unclassified",
                      "graph_scopes": ["<scope>"] | null,
                      "indexes": ["<catalog id>"] } ],
         "indexes": ["<catalog id>"],
         "holders": [ { "who": "<email or display>", "how": "<basis>", "tools": ["<tool>"] } ],
         "holders_basis": "<one line>" } ],
     "grant_store": {"status": "read" | "unreadable", "principals": <int> | null, "reason": "<text>" | null} }
   ```
   - **Tools and channels.** The tool set is the live server's registered list, UNFILTERED by principal: `app/tools.py:99`
     `mcp` is a `_PolicyGuardedMCP`, whose `list_tools` filters per principal, so call the PARENT `FastMCP.list_tools(mcp)`
     (or read the tool manager directly), never `mcp.list_tools()`. Import `app.tools` lazily inside `_compute`, not at
     module load. A tool that an active integration owns (`app/integrations/registry.py` `_ACTIVE_BY_TOOL[tool]`, an
     `IntegrationSpec`, `app/integrations/base.py:56`) goes to that integration's channel: `id` = `spec.id`, `name` =
     `spec.display_name`, `auth` = `spec.auth_kind.value`, `min_tier` = `spec.min_tier`. Every other tool goes to ONE
     channel, `id` "m365", `name` "Microsoft 365", `kind` "native", `auth` "delegated", `min_tier` "per tool". Order:
     `m365` first, then integrations by `id`; tools by name inside a channel. Each tool appears exactly once.
   - **Per tool:** `access` is "write" iff `destructive_ops.write_class(tool)` is not None, else "read".
     `data_class` is `data_entitlement.classify(tool)`, or "unclassified" when it returns None. `graph_scopes` is the
     sorted `graph_scope_map.TOOL_GRAPH_SCOPES[tool]` when the tool has an entry, else null. `indexes` is
     `registry.catalog_ref_for_tool(tool)` when not None, plus every catalog row id in `app/refs/DATA_CATALOG.yaml` whose
     `read_tool` equals the tool (load the YAML once per `_compute`; find where `read_tool` sits by reading the file --
     it appears on 4 rows today, under keys you will see near lines 1385-1455), sorted, de-duplicated.
   - **Channel `indexes`:** the sorted union of its tools' `indexes`.
   - **Rating (PRD C16):** read `app/refs/channel_ratings.json` IF IT EXISTS (`{"channels": {"<id>": {"value": ...,
     "reason": ...}}}`). A channel with an entry gets it; every other channel, and every channel when the file is absent,
     gets `{"value": "unrated", "reason": null}`. Never a default level. Do NOT create the file.
   - **Holders (the third part).** Computed by CALLING the gateway's own per-call chain, in its own order (read
     `app/tools.py` `_run`, about `:116-170`, and `app/integrations/base.py` `run_integration_tool`, about `:125-160`, to
     see it): `blocklist.kill_switch_active()` / `blocklist.is_blocked(email)`; `data_entitlement.tool_denial` /
     `data_entitlement.decide(tool, access)`; `identity_scope.check(email, tool)`; the tier from `tier.resolve_tier`
     through `guard.enforce(tool, email, tier)` and `entitlements.is_entitled(tier, destructive_ops.write_class(tool))`
     for a native tool, and `guard.enforce_min_tier(tool, tier, spec.min_tier)` for an integration tool. Write ONE
     function `_admits(candidate, tool) -> bool` that runs that chain and returns False on the first denial. Where a
     chain function reads the request context (the current principal or email), set it for the candidate the way the
     gateway's own tests do, or pass it explicitly where the function takes it; never copy a rule's body.
     - **Candidates:** every address in `config.MASTER_ADMIN_EMAILS` and `config.WRITE_CAPABLE_EMAILS`; every scoped
       identity `identity_scope` knows (its seed plus its live overlay, `identity_scope._load_scopes()`); every principal
       with a `principal_profile` in the grant store (below); and ONE population row, `who` "every signed-in Opal
       Microsoft user", evaluated as an address in no roster, unscoped, unblocked, unprofiled, at tier `read_only`.
     - **`how`:** "master admin (MASTER_ADMIN_EMAILS)", "write-capable (WRITE_CAPABLE_EMAILS)", "scoped allowlist",
       "data grant revision <n>" (from the principal's active grant), or "tier read_only floor" for the population row.
       A candidate in two rosters gets one row with both bases joined by "; ".
     - A holder row lists only that channel's tools the candidate is admitted to; a candidate admitted to none of a
       channel's tools is not listed in that channel. A blocklisted candidate holds nothing. A channel with no holder has
       `holders: []`.
     - **Kill switch on:** every channel's `holders` is `[]` and `holders_basis` is "kill switch on: no one may call".
       Otherwise `holders_basis` names the candidate sources and, when the grant store was unreadable, that its principals
       are missing.
   - **The grant store.** Scan `gateway-access-state-table` (`app/access_state.py` `TABLE_NAME`) with a boto3 DynamoDB
     client, `ProjectionExpression` on `pk` and `sk` only, paginating on `LastEvaluatedKey`. Keep rows whose `pk` starts
     `POLICY#` and whose `sk` is exactly `principal_profile`. A real principal's `pk` is `POLICY#<tid>#<oid>`, two GUIDs;
     skip any other shape (the live table holds three `probe-og-i1-*` test keys and one `POLICY#EMAILDENY#...` row). Read
     each principal's profile and grant through the EXISTING `data_entitlement.current_access(principal, store)` (strong
     reads; build the `Principal` the way `app/context.py` does); `who` is the profile's `email` field when present, else
     `<tid>/<oid>`. `grant_store.principals` = the number of real principals kept. A Scan that raises (AccessDenied
     included, which is TODAY's live state until MP-z-4 applies) gives `status` "unreadable" with `reason`
     "<ExceptionClass: message>", `principals` null, and the handler still answers 200 with every other part. Never treat
     a failed Scan as zero principals.
   - **Writes:** none. This module calls no write API of any store.
2. **DO NOT edit `app/admin_api.py`.** The release cell adds `Route("/gateway/breakdown", admin_gateway_breakdown.breakdown,
   methods=["GET"])` and its import. Name that line in your report.
3. **`tests/test_admin_gateway_breakdown.py` (new).** Mount the handler on a `Starlette` test app as
   `tests/test_admin_fabric.py` does (its owner stubbing and `TestClient`). These nine tests, by these exact names:
   - `test_every_live_tool_in_exactly_one_channel` -- a planted tool list plus one planted active integration spec: each
     tool appears once; the integration's tools sit under its `id`; the rest under `m365`.
   - `test_unclassified_tool_reads_unclassified` -- a planted tool `data_entitlement.classify` returns None for reads
     `data_class` "unclassified".
   - `test_unrated_without_ratings_file` -- with `channel_ratings.json` absent, every channel reads `{"value": "unrated",
     "reason": null}`; with a planted file naming one channel, that one carries its value and the rest stay "unrated".
   - `test_channel_with_no_holder_is_empty_list` -- an integration whose `min_tier` no candidate meets has `holders: []`.
   - `test_kill_switch_empties_every_channel` -- kill switch on: every channel `holders` [] and the basis says so.
   - `test_grant_store_unreadable_is_labelled` -- a fake Scan raising botocore `ClientError` AccessDenied: 200, `grant_store`
     `status` "unreadable" with the reason, `principals` null, channels still listed.
   - `test_breakdown_non_owner_is_refused` -- a non-owner gets 403 and the fake clients record zero calls.
   - `test_holders_match_the_dispatch_chain` -- THE SEAM. Plant: one master-admin address, one write-capable address, one
     scoped identity (an overlay row), one profiled principal with an active grant (fake store returning its profile and
     grant), one blocklisted address, and the population row. For each, the set of tools the breakdown lists it as
     holding (across channels) EQUALS the set of tools for which the gateway's real chokepoints admit it: drive
     `app.tools._run`'s checks and `run_integration_tool`'s checks with the candidate as the request identity (stub only
     the token fetch and the tool body, never a check) and record which tools are not denied. Difference control in the
     same test: add the write-capable address to the blocklist; BOTH sides become empty for it.
   - `test_real_server_tool_inventory` -- the real `app.tools.mcp` registered list with the registry's active set as the
     test environment leaves it: every registered tool appears in exactly one channel, none is invented, and the channel
     count is 1 + the number of distinct active integration specs.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change any other `app/` module (`admin_api.py`, `owner_gate.py`,
   `tools.py`, `data_entitlement.py`, `identity_scope.py`, `tier.py`, `guard.py`, `blocklist.py`, `entitlements.py`,
   `destructive_ops.py`, `graph_scope_map.py`, `access_state.py`, `integrations/**`, `refs/**`), Terraform, the manifest
   or anything in `mcportal/`. Make no deploy and no AWS call.
2. If a chain function cannot be called for a candidate without editing gateway code, REFUSE that criterion with what you
   measured and file a BLOCKING row. Never re-type the rule to make the test pass.
3. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py
infra/aws/ec2/opal-gateway/tests/test_admin_gateway_breakdown.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~13/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every `infra/aws/ec2/opal-gateway/app/` module named above, `app/refs/DATA_CATALOG.yaml`,
`tests/test_admin_fabric.py`, `tests/test_owner_gate.py`, the gateway's existing tests of `_run` and
`run_integration_tool`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/GATEWAY_CHANNEL_MAP_20261008.md` (a census for
orientation; never a source for the map), `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W13-S<k>` (the next free k for W13). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-z-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z1.AC1.sh; echo "exit=$?"</invocation><expect>breakdown tests: 0 failed; named tests PASSED 7 of 7 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-z-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z1.AC2.sh; echo "exit=$?"</invocation><expect>breakdown seam: 0 failed; named tests PASSED 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~13/NFRA_MCPORTAL.TO-MP-z-1.gateway-breakdown-handler.proof_of_spec.json`.
Report once, with:
- the two check outputs;
- the commit hash;
- the route line for the issuer;
- from `test_real_server_tool_inventory`: the channel count and tool count per channel in the test environment;
- every chain function you called and how you set the candidate's identity for it;
- any field of the response you could not fill as written, and why;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the GW issuance (decomposition v7) from PRD v0.7 FWD-20, C15, C16 @cdb5ff66b1 (ratified-text
half signed @3318b66cd0). Checks dry-run at base 8abe56f2cd: AC1 FAIL (test file absent), AC2 FAIL (test file absent).
Live grant store measured by the issuer (keys only): 1 real principal, 3 probe keys, 1 EMAILDENY row. No gate. Lives
through MP-z-5.

<status>pending</status>
<round>1</round>
<workstream>GW</workstream>
<slot>~13</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
