# NFRA_OPLGTW -- surprise channel, INVESTIGATION v1

**Opened by:** `2.0.0_SA_COO~O` at L6, 2026-09-15. **Home:** the project tree's channel. Lane `ANY`; the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project). **Append-only.**
Worker rows carry their slot's coordinate, `NFRA_OPLGTW-W<n>-S<k>`; a seat's row carries none.

**Why this file is opened at the issuance.** The first row was found while grounding the task orders' test criteria: the
Gateway's existing test suite does not pass at the cut base, so every "whole suite passes" criterion of this round has to
name the one known failure instead of silently inheriting it.

**Denominator at this write: 1 row** -- `NFRA_OPLGTW-S1`, 2.0.0_SA_COO~O at L6.

```json
[
  {
    "id": "NFRA_OPLGTW-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T09:10Z",
    "one_line": "The Gateway's own suite fails one test at the cut base: test_scoped_deny_by_default still lists opal_data_refresh_upload as denied to the Bloomberg service identity, while the tracked allowlist overlay grants that identity that tool.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TEST: infra/aws/ec2/opal-gateway/tests/test_identity_scope.py:32-51 @7921d898c0 -- _FRAME_III_DENIED includes 'opal_data_refresh_upload', and test_scoped_deny_by_default asserts identity_scope.check('opalbloomberg@opalinvest.com', tool) is not None for every member.",
        "OVERLAY: infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt:13 @7921d898c0 reads 'opalbloomberg@opalinvest.com opal_data_refresh_upload'; the test module's own AC-D says the overlay widens the named identity, and infra/aws/ec2/opal-gateway/deploy-to-ec2.sh:134 carries the grant's rationale, so the grant reads as deliberate.",
        "RUN: Python 3.12.10, pytest 9.0.2, 'python -m pytest tests -q -p no:cacheprovider' from infra/aws/ec2/opal-gateway at 2026-09-15 09:03Z: '1 failed, 76 passed, 34 subtests passed'; FAILED tests/test_identity_scope.py::test_scoped_deny_by_default -- AssertionError: opal_data_refresh_upload."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The round's cut would have said 'the whole infra/aws/ec2/opal-gateway/tests suite passes' as a criterion on every Gateway code cell, which assumes the suite is green at the base the workers branch from.",
    "world_is": "The suite is red at the base on one test that predates this project and belongs to the opal_portal integration's grant, not to any NFRA_OPLGTW cell. Every suite criterion in this issuance therefore deselects exactly that test by name (-k 'not test_scoped_deny_by_default') and cites this row; no worker edits the test or the overlay.",
    "notes": "INERT: the failure does not change the Gateway's runtime behaviour, which follows the overlay. OBSERVATION: it blocks nothing in this round, because the criteria name it. Whether the test or the overlay is the one to change is the owner of the opal_portal integration's grant to decide; it is outside this project's write surface."
  },
  {
    "id": "NFRA_OPLGTW-W5-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-15T10:43:23Z",
    "one_line": "The audit field list names 'master' in the same sentence that excludes raw account IDs, and the contract's masters are 8-digit account-number-shaped codes; OG-o-1 records master as given, bounded to the contract's two keys.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:282 @f0aa50dbc0 -- 'Audit fields: ... master/dataset/date ... Exclude raw account IDs, customer values, prompts, OAuth credentials, cookies, ticket secrets and complete URLs.'",
        "CONTRACT: org/standards/NFRA_OPLGTW_CONTRACT.json:6-9 @1bcc827bda -- masters keyed '08242234' (SmartX) and '08335338' (BlackDiamond), both 8-digit codes.",
        "BUILD: infra/aws/ec2/opal-gateway/app/schwab_audit.py (_MASTERS, build_record) on branch wk-nfra_oplgtw-1-5 -- master is an enum of exactly those two keys; any other value (the AC5 fixture's 87654321) is dropped and named in redacted_fields; test_ogo1_ac05 asserts both halves."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-o-1 quotes the PRD: the Schwab audit record carries master/dataset/date and excludes raw account IDs. It does not say whether a Schwab master number counts as an account ID.",
    "world_is": "The contract's two masters are 8-digit account-number-shaped values, so the two clauses can be read as conflicting. The worker had to choose: master is written as given, restricted to the contract's closed set, and no other account-shaped value can enter the record. If a master number counts as a raw account ID, the field needs a hash or an alias instead, which is the spec owner's call.",
    "notes": "INERT: nothing deploys in this order, and only the two contract masters can appear in the field. OBSERVATION: no criterion is blocked; AC5's fixture uses a non-master account number."
  },
  {
    "id": "NFRA_OPLGTW-W3-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T10:42Z",
    "one_line": "Neither OG-d-1's order, OG-i-1's order nor the contract names the access-state table's key attribute names, whether it has a sort key, or its TTL attribute; the adapter chose pk (HASH) + sk (RANGE) and expires_at as both logical expiry and TTL attribute while OG-i-1 designs the table in parallel.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-d-1.access-state-adapter.md:22-35 @2fdc84e250 -- names record types, namespaces, consistency and the TTL policy; names no attribute, key schema or TTL attribute.",
        "TO: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-i-1.access-state-table.md:65 @2fdc84e250 -- OGI1-AC4 grades 'the TTL attribute set and the designed key schema' without naming either.",
        "CONTRACT: org/standards/NFRA_OPLGTW_CONTRACT.json state_store @2fdc84e250 -- fields service, table, region, account, record_types, consistency, ttl, key_namespaces, runtime_policy_access; no attribute-name or key-schema field.",
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:193 @2fdc84e250 -- 'The DynamoDB partition key separates POLICY#<tid>#<oid> records (profile, grant, approval, operator audit)': several records under one partition key, which implies a sort key without naming it.",
        "ADAPTER: infra/aws/ec2/opal-gateway/app/access_state.py on branch wk-nfra_oplgtw-1-3 -- PK='pk', SK='sk', RECORD_TYPE='record_type', EXPIRES_AT='expires_at', module constants in one place."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order specifies the adapter's namespaces, record types, strong reads, conditional writes and logical expiry against the table OG-i-1 builds in parallel, but states no attribute names, no key schema and no TTL attribute.",
    "world_is": "The adapter had to choose them: a composite key pk (HASH, S) + sk (RANGE, S), record_type on every item, and expires_at (integer epoch seconds) as both the logical expiry and the TTL attribute. If OG-i-1's table uses other names, every adapter call against the live table fails with a ValidationException, which the adapter maps to DEPENDENCY_UNAVAILABLE: closed, but the feature never works. A different TTL attribute would leave expired RUNTIME records uncollected (cleanup only; authorization unaffected).",
    "notes": "ARMED: left alone, the two cells' drains can land a table and an adapter that disagree, and no offline test sees it because moto builds whatever key schema the test declares. OG-i-1's live arm or the first on-host call is the first instrument that can see it. Reconciling is one edit of the constants on either side."
  },
  {
    "id": "NFRA_OPLGTW-W3-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T10:50Z",
    "one_line": "Running the Gateway suite the way row NFRA_OPLGTW-S1 records it appends three lines to the tracked infra/aws/ec2/opal-gateway/audit.jsonl, a path outside every Gateway code cell's write grant, so a worker who runs the suite leaves a tracked file modified that its grant forbids it to restore.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: from infra/aws/ec2/opal-gateway, '.venv-og/Scripts/python -m pytest tests -q -p no:cacheprovider' on branch wk-nfra_oplgtw-1-3 at 2026-09-15 ~10:45Z: '1 failed, 83 passed, 34 subtests passed' (the failure is S1's test_scoped_deny_by_default); afterwards 'git diff --stat -- infra/aws/ec2/opal-gateway/audit.jsonl' reads '1 file changed, 3 insertions(+)'.",
        "WRITER: infra/aws/ec2/opal-gateway/app/audit.py:29-33 @2fdc84e250 -- _emit appends every record to _cfg.AUDIT_PATH; the added lines are _ratelimit_control alarm records of the kind test_ratelimit.py induces.",
        "GRANT: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-d-1.access-state-adapter.md:88-93 @2fdc84e250 -- the <paths> block does not name audit.jsonl."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The grant limits a worker's writes to its <paths> block, and the round's suite criteria (row NFRA_OPLGTW-S1) have Gateway code workers run the whole infra/aws/ec2/opal-gateway/tests suite.",
    "world_is": "The suite run writes the tracked audit.jsonl. This worker did not restore it (a restore is a write outside the grant) and did not commit it; it stays modified in the worktree at /c/tmp/wk-oplgtw-1-3 only. Every later worker that runs the suite will do the same.",
    "notes": "INERT: nothing is committed, and the drain merges commits, not worktree changes. OBSERVATION: blocks nothing. Whether the suite should write to a temporary AUDIT_PATH is for the owner of the Gateway test harness to decide."
  },
  {
    "id": "NFRA_OPLGTW-W3-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T11:51:38Z",
    "one_line": "OG-a-1's durable refresh route cannot keep the stateless JWT refresh branch without breaking C1's no-stateless-branch rule, so it already refuses every pre-durable refresh token with invalid_grant -- a refusal the decomposition gives to OG-a-2's legacy cutover.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-a-1.durable-oauth.md:52-53 @8d8b221ee6 -- 'The immutable principal (tid/oid) and the legacy cutover are the NEXT cell's (OG-a-2)'.",
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:137 @f0aa50dbc0 -- 'Legacy refresh tokens cannot be safely upgraded ... Cutover rejects them with invalid_grant ... Failure of durable state fails new/refresh exchanges closed; it must not silently select an old stateless branch.'",
        "DECOMP: org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md:265 @8768f46770 -- OG-a-2 is 'the immutable principal, the legacy cutover and the challenge semantics'.",
        "BASE: infra/aws/ec2/opal-gateway/app/server.py:377-379 @8d8b221ee6 -- the refresh grant called oauth_as.validate_refresh_token (a signed JWT, no store) and re-issued tokens.",
        "BUILD: infra/aws/ec2/opal-gateway/app/oauth_as.py on branch wk-nfra_oplgtw-1-3b -- issue_refresh_token/validate_refresh_token removed; exchange_refresh answers any token that is not 'ogr1.<family>.<n>.<secret>' with invalid_grant 'a token issued before durable refresh cannot be upgraded -- reconnect from Claude'; test_oga1_ac15 prints a legacy refresh JWT refused 400 with the store failing and with it healthy."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order gives the legacy cutover to the next cell (OG-a-2) and has this cell bind families 'behind one function OG-a-2 will change', while the C1 text it quotes forbids any stateless fallback for new or refresh exchanges.",
    "world_is": "Durable refresh families replace the stateless JWT refresh token outright. Keeping validate_refresh_token on /token would be the stateless branch C1 forbids, so this cell removed it, and the token endpoint answers a legacy refresh JWT with invalid_grant and a reconnect description. What remains for OG-a-2 is the rest of the cutover: legacy ACCESS JWTs on protected routes, the inventory of registered clients, and the one-time reconnect notice.",
    "notes": "INERT: nothing deploys in this order; the release is OG-r-1's. OBSERVATION: blocks no criterion. If a release ships OG-a-1 without OG-a-2, every user holding a live refresh token is sent to reconnect without the one-time notice C1 describes."
  },
  {
    "id": "NFRA_OPLGTW-W3-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T11:51:38Z",
    "one_line": "Token lifetimes were environment knobs (GATEWAY_TOKEN_TTL, default 3600 s access; GATEWAY_REFRESH_TTL, 30 d); OG-a-1 takes them from the contract's limits instead (900 s; 30 d absolute and 7 d idle), which leaves both config.py keys declared but read by nothing, and config.py is outside this order's grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CONFIG: infra/aws/ec2/opal-gateway/app/config.py:119-120 @8d8b221ee6 -- GATEWAY_TOKEN_TTL default '3600' ('1h access') and GATEWAY_REFRESH_TTL default '2592000'.",
        "BASE: infra/aws/ec2/opal-gateway/app/oauth_as.py:42-43 @8d8b221ee6 -- ACCESS_TOKEN_TTL = int(_cfg.GATEWAY_TOKEN_TTL); REFRESH_TOKEN_TTL = int(_cfg.GATEWAY_REFRESH_TTL).",
        "CONTRACT: org/standards/NFRA_OPLGTW_CONTRACT.json limits @8d8b221ee6 -- access_token_seconds 900, refresh_absolute_seconds 2592000, refresh_idle_seconds 604800.",
        "CENSUS: native Grep for 'GATEWAY_TOKEN_TTL|GATEWAY_REFRESH_TTL' over infra/ at 8d8b221ee6: 2 hits, both config.py:119-120; no deploy unit, env file or Terraform under infra/ sets either.",
        "BUILD: infra/aws/ec2/opal-gateway/app/oauth_as.py on branch wk-nfra_oplgtw-1-3b -- ACCESS_TOKEN_TTL = 900, REFRESH_ABSOLUTE_SECONDS = 2592000, REFRESH_IDLE_SECONDS = 604800 as module constants citing the contract; test_oga1_ac12 asserts them equal to the contract file read at test time."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order sets the lifetimes from the contract (access_token_seconds 900, refresh 30 d absolute / 7 d idle) and grants oauth_as.py and server.py, not config.py.",
    "world_is": "The lifetimes are now fixed to the contract values in oauth_as.py. The two environment keys in config.py stay declared with their old defaults (the access one says '1h') and nothing reads them, so setting either has no effect. Removing or re-pointing them is an edit to config.py, outside this grant.",
    "notes": "INERT: nothing reads the keys, and the census finds no deploy surface setting them. OBSERVATION: blocks nothing; a reader of config.py is misled about the access-token lifetime until the keys are removed."
  },
  {
    "id": "NFRA_OPLGTW-W3-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T11:51:38Z",
    "one_line": "C1 says to persist client records so a restart does not forget them, but names no lifetime for a registration; OG-a-1 stores every Dynamic Client Registration with no expiry, so unauthenticated registrations accumulate in the access-state table without bound, throttled only by the per-IP auth limit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:137 @f0aa50dbc0 -- 'Persist client records so restarting a worker does not forget clients'; :137 also 'preserves registered Code client callbacks' at cutover. No lifetime is stated for a client record.",
        "BASE: infra/aws/ec2/opal-gateway/app/oauth_as.py:358 @8d8b221ee6 -- the in-memory store swept clients after 30 days (_sweep(_clients, 86400 * 30)).",
        "LIMIT: infra/aws/ec2/opal-gateway/app/ratelimit.py:42 @8d8b221ee6 -- /register is in AUTH_PATHS; infra/aws/ec2/opal-gateway/app/config.py:297 @8d8b221ee6 -- RL_IP_AUTH_LIMIT default 20 per 60 s per IP.",
        "BUILD: infra/aws/ec2/opal-gateway/app/oauth_as.py register_client on branch wk-nfra_oplgtw-1-3b -- puts RUNTIME#client#<client_id> (record_type oauth_client) with no expires_at; test_oga1_ac14 proves a registration survives a restart."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order asks for durable client registration that survives a restart and preserves registered Code clients through the cutover; it states no lifetime for a client record.",
    "world_is": "The worker had to choose one. It chose no expiry, because any TTL would silently unregister an idle but legitimate Code client and force a reconnect the PRD does not ask for. The cost is that /register, which is public, can add records without bound, limited only to 20 per minute per IP by default. An idle expiry refreshed at each authorize would bound it; which lifetime is right is the spec owner's call.",
    "notes": "INERT: nothing deploys in this order. OBSERVATION: blocks no criterion. The old 30-day sweep was process-local and a restart erased it anyway, so no deployed behaviour carried a lifetime either."
  },
  {
    "id": "NFRA_OPLGTW-W3-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T11:58:00Z",
    "one_line": "tests/test_ratelimit.py replaces time.monotonic for the WHOLE test process at import and never restores it, which freezes asyncio's loop clock for every Gateway test in the same run: no event-loop timer or asyncio.wait_for timeout can fire after it is collected.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TEST: infra/aws/ec2/opal-gateway/tests/test_ratelimit.py:19-20 @8d8b221ee6 -- module level: '_clock = {\"t\": 1000.0}' and 'rl.time.monotonic = lambda: _clock[\"t\"]'; rl.time is the process's one time module, and nothing restores the attribute.",
        "RUN: the whole Gateway suite (AC19 invocation) on branch wk-nfra_oplgtw-1-3b, twice at ~11:45Z and ~11:50Z: '1 failed, 107 passed, 1 deselected, 34 subtests passed', the failure test_oauth_durable.py::test_oga1_ac18, which passes alone ('1 passed in 4.93s').",
        "BISECT: test_oga1_ac18 paired with each of the 10 other Gateway test modules: 9 pairs clean, 1 failing -- test_ratelimit ('1 failed, 6 passed').",
        "DIAGNOSTIC: that pair with the assertion printing its values: 'AssertionError: (201, 200, 1.507, 1.581)' -- 1.5 s of handler work under a 0.3 s asyncio.wait_for budget answered 201/200 instead of 503, because the loop's clock (time.monotonic via BaseEventLoop.time) no longer advances."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order has every Gateway code cell run the whole infra/aws/ec2/opal-gateway/tests suite as one process (OGA1-AC19), which assumes the suite's modules do not leak state into each other.",
    "world_is": "One existing module changes a process-wide clock at collection time. Any later test whose outcome depends on asyncio timers or on time.monotonic sees a frozen clock: a timeout-enforcement test can fail, as test_oga1_ac18 did, and a test that should wait could pass without waiting. This worker did not edit test_ratelimit.py (outside the grant; the order forbids editing existing tests). Instead its own fixture restores the builtin time.monotonic for the duration of each OG-a-1 test, and monkeypatch puts the neighbour's fake back afterwards.",
    "notes": "INERT: test-only; no runtime code reads the fake clock. OBSERVATION: blocks nothing now that the OG-a-1 fixture guards itself. Every later cell whose tests use asyncio timeouts inherits the same trap until test_ratelimit.py scopes its clock (for example with monkeypatch in a fixture); that edit is for the owner of the rate-limit tests."
  }
]
```
