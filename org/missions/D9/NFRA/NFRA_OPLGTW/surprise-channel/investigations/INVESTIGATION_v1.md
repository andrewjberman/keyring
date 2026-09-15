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
    "id": "NFRA_OPLGTW-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T11:25Z",
    "one_line": "Disarm of W3-S1 by its named owner: the table OG-i-1 declares uses exactly the adapter's key names (pk HASH, sk RANGE, TTL expires_at), and the COO binds the applied-plane check to OG-i-1's drain.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ADAPTER: infra/aws/ec2/opal-gateway/app/access_state.py:48-51 @8d8b221ee6 (merged) -- PK = \"pk\", SK = \"sk\", EXPIRES_AT = \"expires_at\".",
        "TABLE (declared): infra/aws/terraform/opal-gateway/schwab_access_state.tf on branch wk-nfra_oplgtw-1-1 @59b567eed0 -- hash_key = \"pk\" (type S), range_key = \"sk\" (type S), ttl attribute_name = local.access_state_ttl_attr = \"expires_at\"; read at 11:1xZ from the worker's own commit, not from a message.",
        "NOT YET APPLIED: OG-i-1 refused its plan (row W1-S1) and applied nothing, so the agreement is at the DESIRED plane only."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "W3-S1 names 2.0.0_SA_COO~O as the disarm owner of the risk that the adapter's key names and OG-i-1's table disagree.",
    "world_is": "The two agree name for name in the declared state. The residual is the applied plane: when OG-i-1 re-runs and applies, 2.0.0_SA_COO~O reads its AC4 describe-table readback at the drain and does not merge OG-i-1's branch unless the live key schema is pk/sk and the TTL attribute is expires_at. A mismatch there is a new row and a hold on the merge, not a silent pass.",
    "notes": "Disarms W3-S1 in the declared plane and moves the applied-plane residue to a named act at a named moment (OG-i-1's drain) by the named owner. INERT: no live table exists yet. The adjudication of W3-S1 is 3.0.0_SA_CVO's at L9."
  },
  {
    "id": "NFRA_OPLGTW-W2-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~2",
    "surfaced_at": "2026-09-15T10:57Z",
    "one_line": "OGP1-AC11 cannot be met as written: the Gateway's audit record carries no latency or duration field, so p95 latency per tool is not computable from it.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: infra/aws/ec2/opal-gateway/app/audit.py:122-132 @7bd89b5d71 (the manifest's deployed_commit; blob byte-identical at 417631ae6f, sha256 b744a535...) -- log_call writes ts, user, tool, args, outcome, detail, tier; ts is taken once, inside log_call, after the tool has returned, so no start time exists to difference against.",
        "HOST: og_p1.py AC11, ssm a6a55353-e24d-4c88-86d8-f7799f9f7f58 at 2026-09-15T10:57:48Z on i-07dccb1615503ac99 -- /opt/opal-gateway/audit.jsonl 79091 lines; 78049 records in the 30-day window; 0 in the window and 0 in the whole file carry any of duration, duration_ms, duration_s, latency, latency_ms, elapsed, elapsed_ms, elapsed_s, took_ms; the top-level key census in the window is args, caller, credential_class, detail, event, outcome, route, tier, tool, ts, user.",
        "PARITY: og_p1.py AC1, ssm dff40742-2145-45c5-8fbf-f3b560b7d4dd -- the host's app/audit.py digest matches the deployed commit (50 of 50 files match), so the record shape above is the running one."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-p-1 OGP1-AC11: 'the existing-user baseline records p95 latency per representative tool from the audit record over a stated window, with its sample count printed.'",
    "world_is": "The audit record has no timing field, so no latency, and therefore no p95, can be derived from it. The probe prints the window and each tool's sample count (e.g. ms_site_children 42055, poll_addressed_teams_messages 19370, read_channel_messages 3526, whoami 163) and refuses the p95: VERDICT FAIL-OGP1-AC11. It does not substitute another latency source the order does not name.",
    "notes": "The S3 audit lake (opal-mcp-audit) receives the same serialized line (audit.py:30 and :48-53), so it carries no timing field either; that is read from the code, not measured. BLOCKING only in the sense that AC11 stays FAIL and the order stays open."
  },
  {
    "id": "NFRA_OPLGTW-W2-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~2",
    "surfaced_at": "2026-09-15T10:58Z",
    "one_line": "OGP1-AC12 cannot be met as written: no audit record carries a client_id, so an OAuth client inventory drawn from the audit record is empty by construction, whatever clients exist.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: infra/aws/ec2/opal-gateway/app/audit.py:122-151 @7bd89b5d71 -- log_call writes ts, user, tool, args, outcome, detail, tier; log_credential writes ts, event, route, credential_class, caller; neither has a client_id field. No audit.log_call site exists in app/oauth_as.py, where DCR registration mints the client_id (oauth_as.py:350-362 at the worktree base 417631ae6f; that file is unchanged between 7bd89b5d71 and 417631ae6f).",
        "HOST: og_p1.py AC12, ssm d9bfff7a-be92-4fd3-b45b-759e9048fad7 at 2026-09-15T10:57:59Z -- 0 of 79091 records in /opt/opal-gateway/audit.jsonl contain the key client_id (0 of 78049 in the 30-day window).",
        "PROCESS-LOCAL: oauth_as.py:336 @7bd89b5d71 '_clients: dict = {}' -- a module-level in-memory store; deploy/opal-gateway.service:13-16 pins --workers 1 for that reason. This half of AC12 is met and printed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-p-1 OGP1-AC12: 'the OAuth client inventory lists every client_id the audit record shows over a stated window, with counts, and states that clients are process-local.'",
    "world_is": "The audit record cannot show a client_id, so the list it yields is empty for a structural reason, not because no clients registered. Printing that empty list as the inventory would be a check that cannot return a non-empty answer. The probe prints the census and the process-local statement, then refuses: VERDICT FAIL-OGP1-AC12.",
    "notes": "Other cells take this inventory as a pre-change reference (the durable-OAuth migration cell among them). Where a client_id is actually observable on a read-only path is for the issuer to name; this cell does not widen to another source."
  },
  {
    "id": "NFRA_OPLGTW-W2-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~2",
    "surfaced_at": "2026-09-15T11:01Z",
    "one_line": "OGP1-AC13 cannot pass as written: the host-read route the order itself names (aws ssm send-command) is the API operation SendCommand, which is none of Describe, Get, List or Head.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-p-1.baseline.md:39-40 @417631ae6f -- 'Host reads go through SSM (aws ssm send-command with AWS-RunShellScript, then get-command-invocation) using .tools/aws'; :47, :50 and :74 require AC1, AC2 and AC10 to be read on the host; :83 AC13 requires every AWS call in the command log to be a read verb (Describe, Get, List, Head).",
        "LOG: og_p1.py AC13 at 2026-09-15T11:01:03Z over deliverables/0.9.0_WK_NFRA_OPLGTW~2/command_log.jsonl -- 57 calls, 49 read verbs, 8 ssm:SendCommand (AC1 x2 including the HEAD discrimination control, AC2, AC10, AC11 x2, AC12 x2); each SendCommand row logs a sha256 prefix of its script, and every script is in probes/og_p1.py and only reads files, /proc, /sys and systemd state.",
        "API: no Describe/Get/List/Head operation runs a command on an EC2 instance. ssm:GetCommandInvocation reads a result but cannot start one."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-p-1 OGP1-AC13: 'every AWS call in the cell's command log is a read verb (Describe, Get, List, Head)', in the same order that names ssm send-command as the host-read route for AC1, AC2 and AC10.",
    "world_is": "The two clauses cannot both hold: every host read needs SendCommand. The probe grades the log literally, prints the 8 SendCommand rows by operation, and says VERDICT FAIL-OGP1-AC13. It does not reclassify SendCommand as a read. Nothing was written in AWS or on the host; SendCommand's only side effect is the SSM command record itself.",
    "notes": "Whether AC13 should read 'read-verb or the named SSM read route', or the host criteria should be re-cut, is the issuer's call."
  },
  {
    "id": "NFRA_OPLGTW-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T11:29Z",
    "one_line": "The standing '+ description' backfill on the Gateway's two regional blocked-IP sets (row W1-S1) has no owner who will apply it and no seat holding an order to, so OG-i-1 stays blocked and OG-i-2..i-4, which plan the same root, are held unspawned for the round.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "BLOCK: row NFRA_OPLGTW-W1-S1 by 0.9.0_WK_NFRA_OPLGTW~1, on branch wk-nfra_oplgtw-1-1 @59b567eed0: 'Plan: 4 to add, 2 to change, 0 to destroy' on infra/aws/terraform/opal-gateway; the 2 updates are description-only on aws_wafv2_ip_set.opal_blocked_ips_regional_v4/_v6 (waf.tf:261, :302 @da63a446ef). The branch stays UNMERGED: its schwab_access_state.tf merged before an order-bound apply would let any later apply of the root create the table outside the ledger.",
        "OWNER: the sets were declared for NFRA_OPSEC202609, whose register row org/projects/NFRA_OPSEC202609.json reads dep_stage CLOSED @da63a446ef; its last act on them, 3758b14afc (0.7.0_AE_CloudOps~T, 2026-09-04), recorded the backfill as 'benign' and left it standing.",
        "ROUTE: send_message from 2.0.0_SA_COO~O to 0.7.0_AE_CloudOps at ~11:27Z asking for an owner-ledger apply was REFUSED by LD-0529 (a Tier-2 seat hears an act only as a task order); nothing was written for the recipient."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The decomposition @8768f46770 (OG-i-1 acceptance) and orders OG-i-1..OG-i-4 assume a plan of the opal-gateway root that changes nothing existing beyond each cell's own resources, with -target banned.",
    "world_is": "Every plan of that root also changes the two sets' description. The issuer (this seat) does not widen OG-i-1's blast-radius bound mid-round -- the spec and the orders are frozen -- and no live seat holds an order to apply the backfill. So OG-i-1 is BLOCKED and OG-i-2, OG-i-3 and OG-i-4 are held unspawned; everything downstream of the applied table (the live arms of the S1 chain) waits with them. Unblocking is an act only the round's L10 read can order: an order that applies the backfill under its own ledger, or one that admits it in the bound.",
    "notes": "INERT: nothing was applied and nothing is half-landed. Source-only cells that test against moto (OG-a-1, OG-q-1, OG-c-1 and their chains) are unaffected and proceed. Carried into L9/L10 with W1-S1."
  },
  {
    "id": "NFRA_OPLGTW-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T12:03Z",
    "one_line": "Every 08335338 marker date is PUT about ten times within ~40 s and each PUT dispatches the whole 49F gold chain: 94 accelerator dispatches in 14 days for 10 dates, 61 of all 108 dispatches REFUSED by the chain lock, and 40 in-window terminals the dispatcher cannot classify.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "LOGS: logs filter-log-events /aws/lambda/advi-49f-gold-dispatch, 14 days to 2026-09-15T12:0xZ, 249 events, no nextToken: 108 'Event:' lines = 14 source advi.49f.scheduled-floor + 94 Records[aws:s3] on schwab/08335338/meta/complete/date=<D>.json, in bursts of ~10 per date within ~40 s (e.g. 2026-09-15 09:46:08Z..09:46:40Z, 10 for date=2026-09-14); outcomes: 61 CHAIN REFUSED, 33 host starts, 40 'ERROR: chain terminal within poll window, signature=UNKNOWN(first_line=...s3 sync progress...)'.",
        "OBJECTS: s3api list-objects-v2 opal-data-assets schwab/08335338/meta/complete/ at 12:0xZ: 10 objects, each LastModified equal to the last event of its burst (e.g. date=2026-09-14 at 09:46:40Z).",
        "CHAIN LOGS: list-objects-v2 opal-data-49financial gold/advi/_logs/chain_2026091*: 6-8 logs per burst, all but one landing within ~2 s of their stamp, plus one 12:45Z floor log per day.",
        "CODE: infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/lambda_function.py:90-101 @e9b070d842 classifies on CHAIN OK/REFUSED/ABORT lines in StandardOutputContent; :104-128 reads the key only; silver.tf:744-746 calls the notification 'an ACCELERATOR ONLY'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Gate G-B (decomposition @8768f46770 s.6) and OG-c-2 treat the accelerator as one fire per marker write, and silver.tf:744-746 treats it as an accelerator beside the 12:45Z floor.",
    "world_is": "The producer PUTs one date's marker about ten times per conversion burst, so the chain is dispatched about ten times per date. The lock refuses the overlaps, so one run lands, but 40 of 108 dispatch outcomes are unclassified because the chain's first stdout is s3 sync progress. OG-c-1's rule that an identical qualified closure writes nothing (W4-S4) can only lower the count after OG-c-2's deploy. The replay adds at least one dispatch, which the G-B record names.",
    "notes": "INERT: the lock prevents concurrent chain runs and every run re-derives the same D. OBSERVATION: the dispatcher and the producer's PUT cadence belong to the 49F ADVI chain's owners, outside this project's write surface. Named in org/tier1_exec/2.0.0_SA_COO~O/deliverables/NEVER_WIDEN_SIGNOFF_NFRA_OPLGTW_OG_C2.md s.3."
  },
  {
    "id": "NFRA_OPLGTW-W4-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T11:11Z",
    "one_line": "The task order's marker census (361 hits over 172,084 files) does not reproduce in this worker's worktree: the same comp-find invocation read 128 hits in 53 files over 32,970 files scanned.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-c-1.closure-contract.md:39-40 @1bcc827bda -- 'measured at the cut by an unscoped read (comp-find meta/complete --files --all, 361 hits over 172,084 files)'.",
        "RUN: comp-find 'meta/complete' --files --all in /c/tmp/wk-oplgtw-1-4 (branch wk-nfra_oplgtw-1-4, HEAD 1bcc827bda) before 11:11Z 2026-09-15, rc=0: 'DENOMINATOR: 128 hit(s) across 32970 file(s) scanned in scope [corpus=all] | 3 EPHEMERAL-FLOOR ... | 1870 BINARY', 'PAGE 1 of 1 (showing 53 of 53)'.",
        "CONTENT: the four executed readers the order names or implies are in both reads -- infra/aws/terraform/opal-assets/silver.tf, infra/aws/terraform/opal-assets/advi_49f_floor.tf, data/assets/scripts/silver/conversion_manifest.py and its vendored copy under infra/aws/lambda/opal-assets/opal-assets-silver-schwab/."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGC1-AC13 re-runs the cut's unscoped census 'with its own denominator'; the order quotes that census as 361 hits over 172,084 files.",
    "world_is": "The corpus=all denominator is the CHECKOUT's, and a fresh linked worktree carries tracked files only -- none of the shared tree's untracked or gitignored files (the shared tree's git status lists .worktrees/, archive/, .scratch_* and other untracked directories). The same invocation therefore reads 32,970 files, not 172,084. The AC13 census in this worker's deliverables carries its own denominator; it is not the cut's population.",
    "notes": "INERT: every executed reader of the marker is tracked, so the narrower corpus loses no consumer this criterion is about -- the files it cannot see are untracked scratch, archives and worktrees. Recorded so an L9 reader comparing the two denominators does not read the difference as a coverage loss. The worker did not read the shared tree (its write and read surface is its own worktree)."
  },
  {
    "id": "NFRA_OPLGTW-W4-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T11:11Z",
    "one_line": "Exactly one qualified closure per date rests on S3's conditional PUT (If-None-Match / If-Match), and the Schwab silver Lambda runs python3.11 on the runtime's own boto3 -- no botocore is vendored or pinned, so whether the deployed client can send those conditions is unmeasured.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUNTIME: infra/aws/terraform/opal-assets/silver.tf:592 @1bcc827bda -- 'schwab = { memory = 3008, timeout = 600, runtime = \"python3.11\", layers = [data.aws_lambda_layer_version.pandas_pyarrow.arn] }'.",
        "PACKAGE: infra/aws/lambda/opal-assets/opal-assets-silver-schwab/ @1bcc827bda holds 13 files (BUILD_MANIFEST.json, backfill_status.py, conversion_manifest.py, crs_reader.py, cs_reader.py, lambda_function.py, schwab_conversion.py, schwab_projections.py, schwab_runtime.py, schwab_schemas.py, set_identity_guard.py, silver_registry.py, stream_parquet.py) -- no boto3 or botocore.",
        "GRANT: infra/aws/terraform/opal-assets/silver.tf:320-336 @1bcc827bda -- s3:PutObject and s3:GetObject on schwab/{master}/meta/*, which is all the conditional write and its re-read need.",
        "CODE: data/assets/scripts/silver/conversion_manifest.py _client_lacks_conditional_writes / _write_closure_marker at this worker's commit -- a client that refuses the parameters (botocore ParamValidationError) writes the v1 marker unchanged with closure.write_guard = 'unconditional' and status 'incomplete'; exercised in test_ogc1_ac08."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGC1-AC8: 'concurrent completion yields exactly one qualified closure'; this cell is built and tested, not deployed -- the deploy and replay are OG-c-2's.",
    "world_is": "The only S3 primitive that gives exactly-one under concurrency is the conditional PUT, which botocore accepts only in releases that know IfNoneMatch and IfMatch on put_object. The deployed runtime's botocore version is not pinned anywhere in the repo, so the premise the mechanism depends on is unmeasured from here. The code fails closed for the closure and safe for v1: if the client refuses the conditions, the v1 marker still lands unchanged and no date ever qualifies.",
    "notes": "INERT: left alone the failure mode is 'no date qualifies' with UNGUARDED_WRITE named in every record, never a wrong qualified closure and never a changed v1 field. OG-c-2 is the cell that can read the deployed runtime; its replay criterion ('each replayed record validates against OG-c-1's schema') would read UNGUARDED_WRITE rather than pass silently."
  },
  {
    "id": "NFRA_OPLGTW-W4-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T11:11Z",
    "one_line": "The producer holds no declared per-day expected source set, so the closure's 'expected source partitions' are the bronze objects observed for the date when the closure is composed -- a type that lands after a qualified closure is not expected by it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "GUARD: data/assets/scripts/silver/set_identity_guard.py:24-26 @1bcc827bda -- 'Per-master type sets DIFFER BY CONSTRUCTION ... so the expected-table map derives from the BRONZE CENSUS of the lane, never from a fixed cross-master list.'",
        "DECLARED: data/assets/scripts/silver/conversion_manifest.py:242-245 @1bcc827bda -- declared_not_written 'carries fact_rlw on every date until that spec is resolved'; the SPECS-declared list names 17 fact tables and neither master receives all of them.",
        "DAY LAW: data/assets/scripts/silver/schwab_conversion.py:95 @1bcc827bda -- NON_OPTIONAL = ('RLD',), the only day-level requirement the producer states (assert_rld_covered, :214-245).",
        "RECORD: the closure carries expected_source_basis ('OBSERVED ...') and required_types ['rld'] at this worker's commit; test_ogc1_ac04 shows a later landing re-composing the same date to qualified."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.2 C3 @f0aa50dbc0: 'include ... expected source partitions ... Publish qualified closure only after the complete expected set is reconciled.'",
    "world_is": "Nothing in the producer or the vendor feed declares which source types a given master delivers on a given date. The closure therefore reconciles against the bronze observed at composition (plus the RLD law) and states that basis on the record. Every observed partition must reconcile, but a type that has not landed yet is not in the expected set, so a day can qualify and later be superseded when that type lands.",
    "notes": "INERT: a table whose source has not landed is absent from the closure and cannot be served as present, and the superseding closure is written by the next completion. Whether 'expected' should instead be a DECLARED per-master type set is a spec question for the PRD owner, 1.0.0_SA_CTO; this cell does not invent that declaration."
  },
  {
    "id": "NFRA_OPLGTW-W4-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T11:11Z",
    "one_line": "Exactly-one-qualified-closure means a run whose composition equals the qualified closure already at the key writes nothing, so the accelerator (s3:ObjectCreated on schwab/08335338/meta/complete/) fires once per distinct closure rather than once per clean lane run; no v1 field is removed, renamed or changed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CONSUMER: infra/aws/terraform/opal-assets/silver.tf:756-760 @1bcc827bda -- lambda_function 'advi-49f-silver-complete-accelerator', events ['s3:ObjectCreated:*'], filter_prefix 'schwab/08335338/meta/complete/', filter_suffix '.json'.",
        "TARGET: infra/aws/lambda/opal-assets/advi-49f-gold-dispatch/lambda_function.py:124-127 @1bcc827bda -- reads Records[0].s3.object.key and nothing of the marker body.",
        "RECTANGLE: the task order quotes the certified L4 rectangle @c9a44aa896 -- 'Each run can replace the same date-keyed marker.'",
        "CODE: conversion_manifest.py _write_closure_marker's ALREADY_QUALIFIED branch at this worker's commit; test_ogc1_ac08 asserts one marker write for a two-run race."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "'Existing consumers you must not break ... none reads a field this cell removes or renames' (OGC1-AC13), and OGC1-AC8 'concurrent completion yields exactly one qualified closure'.",
    "world_is": "The field set is unchanged, but the write CADENCE the accelerator observes changes. A completion whose closure is identical to the qualified one already published writes no object, so it no longer re-fires the gold dispatcher. A new date, an incomplete record, an incomplete-to-qualified change and a superseding overwrite all still write, and so all still fire.",
    "notes": "INERT: the floor (advi_49f_floor.tf, cron(45 12 * * ? *)) remains the 49F chain's production trigger and is untouched, and a suppressed fire is one whose information the dispatcher already had. Recorded because it is a behaviour change visible to an existing consumer that no field census can see; OG-c-2's G-B never-widen sign-off covers the act's blast radius and can name it."
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
  },
  {
    "id": "NFRA_OPLGTW-W5-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-15T12:04:25Z",
    "one_line": "OGQ1-AC13's platform tag (manylinux2014_aarch64) matches no DuckDB release from 1.3.0 on, including the cut interpreter's 1.5.0 and the newest stable 1.5.5, so the order as written forces the DuckDB pin down to 1.2.2; OG-q-1 pins duckdb==1.2.2 and pyarrow==18.1.0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-q-1.execution-engine.md:84 @da63a446ef -- AC13 is graded by 'pip download --only-binary=:all: --no-deps --platform manylinux2014_aarch64 --python-version <host>' for each pin; :146-147 (record face) says the cut's interpreter carries PyArrow 18.1.0 and DuckDB 1.5.0 for local tests.",
        "RUN: on 2026-09-15 in /c/tmp/wk-oplgtw-1-5b, 'pip download --only-binary=:all: --no-deps --platform manylinux2014_aarch64 --python-version 3.11 duckdb==1.5.0' -> 'ERROR: No matching distribution found for duckdb==1.5.0'; the same with --platform manylinux_2_28_aarch64 downloaded duckdb-1.5.0-cp311-cp311-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl. pyarrow==18.1.0 downloaded under both tags.",
        "INDEX: https://pypi.org/pypi/duckdb/json read on 2026-09-15 -- among the last 20 stable releases, 1.1.2 through 1.2.2 carry a cp311 manylinux_2_17_aarch64.manylinux2014_aarch64 wheel; 1.3.0 through 1.4.1 carry only manylinux_2_27_aarch64.manylinux_2_28_aarch64; 1.4.2 through 1.5.5 carry only manylinux_2_26_aarch64.manylinux_2_28_aarch64. Every one of the 20 carries a cp312 win_amd64 wheel.",
        "PROBE: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q1.py AC13 on branch wk-nfra_oplgtw-1-5b -- 'resolved 2 of 2 pins for manylinux2014_aarch64 on Python 3.11', 'VERDICT: PASS-OGQ1-AC13', rc=0, with duckdb==1.2.2.",
        "BASELINE: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json OGP1-AC2 @da63a446ef -- python_version 'Python 3.11.15', kernel 6.1.175-219.357.amzn2023.aarch64; no glibc version was measured, so whether a manylinux_2_28 wheel installs on the host is unmeasured."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-q-1 OGQ1-AC13: the pinned PyArrow and DuckDB wheels resolve for linux aarch64 on the host's Python, graded with --platform manylinux2014_aarch64. The cell pins 'compatible PyArrow/DuckDB dependencies' and names no version.",
    "world_is": "No DuckDB release since 1.3.0 publishes a manylinux2014 aarch64 wheel, so a 1.3+ pin, 1.5.0 included, cannot pass AC13 as written. The worker pinned duckdb==1.2.2, the newest release that does, reinstalled .venv-og from the edited file, and ran every OG-q-1 test on 1.2.2; AC9 reads the lockdown settings back from 1.2.2 itself. AC13 passes as written. The cost: the Gateway would ship a DuckDB three minor releases older than the one the cut's interpreter carries, and the grading tag chose the version, not the host.",
    "notes": "INERT: nothing deploys in this order. Whether AC13 should name manylinux_2_28_aarch64 (Amazon Linux 2023 ships glibc 2.34 according to its distribution, not measured here) and allow a newer pin is the issuer's call. A newer pin is one requirements.txt edit plus a re-run of this cell's tests and probe."
  },
  {
    "id": "NFRA_OPLGTW-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T12:36Z",
    "one_line": "On 2026-09-15 the 08335338 completion burst dispatched the 49F chain before the silver it names existed: a00 refused at 09:46:28Z for a missing fact_acc date=2026-09-14 that landed at 09:46:37Z; the one lock holder that ran then wrote 31 objects and hung until the 3600 s document timeout.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "HANDED BY 1.0.0_SA_CTO in its G-B half, section F: org/tier1_exec/2.0.0_SA_COO~O/deliverables/NEVER_WIDEN_SIGNOFF_NFRA_OPLGTW_OG_C2.md @65e254cafe, and msg 97058. Its instruments: the chain log line 'REFUSED: fact_acc has no partition date=2026-09-14' at 09:46:28Z; the silver object fact_acc/date=2026-09-14 at 09:46:37Z; the marker's latest version at 09:46:40Z.",
        "CORROBORATED BY THIS SEAT (a different instrument): s3api list-objects-v2 at 12:0xZ puts schwab/08335338/meta/complete/date=2026-09-14.json at LastModified 09:46:40Z, and the dispatcher log records 10 invocations on that key from 09:46:08Z to 09:46:40Z, the first 20 s before the silver landed (row S4).",
        "W-PARTIAL: the G-B half's branch table records that the 09:46:38Z lock holder wrote 31 objects for date=2026-09-14 (dim_account .. twr_daily) by 09:48:35Z, uploaded no log, and its SSM command reads TimedOut at advi_49f_floor.tf:268 (timeoutSeconds 3600)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The PRD's C3 treats a completion record as a statement that the day's outputs exist, and silver.tf:744-746 wires the 49F accelerator to fire on that record.",
    "world_is": "The v1 marker is PUT during the conversion burst, per table, before the day's silver set is complete, so the accelerator starts the chain on a record that precedes its own data. OG-c-1's qualified closure (merged 1f03a3f209) is the remedy on the producer side. It goes live only with OG-c-2's deploy under G-B. Today's date=2026-09-14 partition was left W-partial by the hung run, and the CTO's half expects the 12:45Z floor to complete it.",
    "notes": "INERT for this project: nothing of NFRA_OPLGTW is deployed yet, and the lock and the floor bound the effect. The chain's timeout and hang belong to the 49F ADVI chain's owners. G-B condition 4 keeps OG-c-2's replay behind a day whose floor reads CHAIN OK."
  },
  {
    "id": "NFRA_OPLGTW-W6-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~6",
    "surfaced_at": "2026-09-15T12:27Z",
    "one_line": "The order's operated_by is one of two values per A-row, but the decomposition proves nine A-rows in BOTH a machine cell and a walkthrough and grades A13 in OG-i-1/OG-i-2's live arms, which neither value names; A_ROWS.json therefore carries each row as one or two halves.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-v-1.acceptance-expectations.md:33-34 @1f03a3f209 -- 'operated_by = machine (graded by OG-v-2 or OG-r-2 in process) or person (graded from a walkthrough record by OG-v-4 or OG-v-5)'.",
        "DECOMP: org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md:610-631 @1f03a3f209 (decomposition v1 @8768f46770) -- A2, A3, A4, A6, A10, A11, A12, A17 and A19 are proved in a machine cell AND OG-v-4; A13 is proved in 'OG-i-1, OG-i-2 (live arms)'.",
        "ARTIFACT: infra/aws/ec2/opal-gateway/tests/acceptance/A_ROWS.json at this worker's commit -- 20 rows, 29 halves (15 machine, 14 person), 9 rows with both; A13's machine half names graded_by OG-i-1, OG-i-2."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Each A-row carries operated_by = machine or person.",
    "world_is": "Nine rows need both a machine result and a walkthrough observation, and one row (A13) is graded by neither OG-v-2/OG-r-2 nor OG-v-4/OG-v-5. Each row is therefore written as halves: every half is exactly machine or person and has its own expected result, instrument and grader, and the row's operated_by lists its halves' operators.",
    "notes": "INERT: no row loses a grader. OG-v-2 reads the machine halves and OG-v-4/OG-v-5 the person halves; the probe's AC1 checks that every half is one of the two values."
  },
  {
    "id": "NFRA_OPLGTW-W6-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~6",
    "surfaced_at": "2026-09-15T12:27Z",
    "one_line": "No carrier declares the unique grain of dim_position, dim_balance or dim_asset, yet PRD C3/C4 make duplicate grains 'unavailable' and paging depend on 'a validated unique source grain'; the fixtures assume (account_id, cusip, l_s), (account_id) and (cusip).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:161 @1f03a3f209 (v0.2 @f0aa50dbc0) -- 'Duplicate/conflicting source grains produce unavailable'; :175 -- 'Tie-break rows deterministically using a validated unique source grain. If a dataset lacks that grain, reject paging'.",
        "CONTRACT: org/standards/NFRA_OPLGTW_CONTRACT.json v1.0 @1f03a3f209 -- fields, additive_fields and quantity_sum_required_groups [cusip, l_s]; no grain or unique-key member.",
        "RECTANGLE: workflows/atom_decomposition/runs/nfra-oplgtw/20260914T1919Z/rectangle.final.certified.json @1f03a3f209, S3-data unverified_boundary -- open question 'Are date alignment, metric units, balance overlaps and future security join uniqueness established?'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Duplicate grains produce unavailable, and paging needs a validated unique grain (PRD C3, C4).",
    "world_is": "The grain the engine must validate is named nowhere. The fixtures' duplicate-grain day (2026-07-07) therefore carries both a conflicting row and an EXACT duplicate row in each dataset, so it is a duplicate under any grain an implementation picks. The A18 paging expectation assumes dim_position is unique on (account_id, cusip, l_s) on the complete dates.",
    "notes": "INERT for the fixtures. Which grain is declared is a spec question for 1.0.0_SA_CTO, and it is OG-q-3's to implement. If the real grain is wider (a lot or accounting-rule column), real-data paging may be rejected by the rule as written."
  },
  {
    "id": "NFRA_OPLGTW-W6-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~6",
    "surfaced_at": "2026-09-15T12:27Z",
    "one_line": "PRD C3 has the catalog HEAD every silver object the closure names, and the published closure names the day's fact_* objects too, but neither Gateway role may GetObject (the permission HeadObject needs) outside the six dim prefixes and two meta/complete prefixes.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:159 @1f03a3f209 (v0.2 @f0aa50dbc0) -- 'Gateway catalog construction validates the closure record and independently HEADs every named silver object'; :185-187 -- the data reader gets GetObject/GetObjectVersion on the six exact prefixes and the catalog role only the two completion prefixes.",
        "CONTRACT: org/standards/NFRA_OPLGTW_CONTRACT.json @1f03a3f209 -- data_prefixes are the six schwab/<master>/silver/dim_*/ prefixes; completion_prefixes the two meta/complete/ prefixes.",
        "CLOSURE: data/assets/scripts/silver/tests/test_conversion_manifest.py:474-475 @1f03a3f209 -- OG-c-1's own complete day names 8 objects, 5 of them fact_* tables; the closure's objects[] carries every successful expected table (result file section 3).",
        "FIXTURES: this worker's closures name 7 objects per day (fact_rld, fact_rps, fact_rps_s2, fact_sec and the three dims), and make_fixtures.py writes fact_* stub objects so an emulated bucket holds every named object."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The catalog independently HEADs every named silver object (PRD C3), under read grants limited to the six dim prefixes and the two completion prefixes (PRD C6).",
    "world_is": "A closure names fact_* objects outside both Gateway roles' grants. If the catalog HEADs every named object, then in AWS each fact HEAD is AccessDenied and every date reads unavailable. The local run cannot see this: an emulated bucket without IAM answers the same HEADs, so OG-v-2 would go green on an implementation that fails live.",
    "notes": "ARMED because a local green would certify behaviour that fails closed in production. Disarm: 1.0.0_SA_CTO rules whether 'every named silver object' means the dim objects the Gateway serves, or whether a grant widens (which C6 forbids without a revision). The fixtures carry both object classes, so either ruling can be tested."
  },
  {
    "id": "NFRA_OPLGTW-W6-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~6",
    "surfaced_at": "2026-09-15T12:27Z",
    "one_line": "The order has the synthetic Parquet fixtures written and committed under fixtures/, but infra/.gitignore:75 ignores *.parquet; they land only because safe-commit force-adds each NAMED file, and a plain git add or a directory pathspec would drop them silently.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "IGNORE: 'git check-ignore -v' on infra/aws/ec2/opal-gateway/tests/acceptance/fixtures/s3/opal-data-assets/schwab/08242234/silver/dim_position/date=2026-07-09/data.parquet at 1f03a3f209 printed 'infra/.gitignore:75:*.parquet' (rc 0).",
        "STAGING: .tools/safe-commit.sh:49 @1f03a3f209 -- 'Staging uses git add -f, which FORCE-adds files EVEN IF gitignored'; this worker names each of the 113 Parquet files in its pathspec.",
        "PIN: fixtures/MANIFEST.json carries each Parquet file's sha256; make_fixtures.py regenerates the set byte-identically (two runs, diff -r clean)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "make_fixtures.py and the synthetic Parquet and closure fixtures it writes under fixtures/ are this cell's committed deliverables (TO-OG-v-1, What you write, item 2).",
    "world_is": "Parquet is ignored repository-wide under infra/. Once force-added the files are tracked and reach every checkout. A later regeneration committed by a route other than named force-adding would silently leave the old bytes, and MANIFEST.json's sha256 would then disagree with the regenerated files.",
    "notes": "INERT: the negation that would un-ignore the fixture directory lives in infra/.gitignore, outside this order's paths. The og_v1 probe checks every Parquet file against MANIFEST.json's sha256, and it regenerates from make_fixtures.py when a file is absent."
  },
  {
    "id": "NFRA_OPLGTW-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T13:14Z",
    "one_line": "Disarm of W6-S3 as its owner 1.0.0_SA_CTO ruled (msg 97078): the catalog HEADs and GETs only named objects under the contract's six data_prefixes, fact_* entries are never read or granted, and the rule is carried as criteria in TO-OG-k-1 and TO-OG-v-2, amended before hand-off @230168e108.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULING: 1.0.0_SA_CTO msg 97078 (2026-09-15T13:02:46Z), reading (a). PRD C3 :155 names only silver/dim_position/, dim_balance/ and dim_asset/ as data-readable. C3 :157 has the completion object carry sufficient sanitized closure facts itself. C6 :185 grants GetObject/GetObjectVersion on those six prefixes, and :191 forbids bucket-policy broadening. The silver HEADs run under the data reader role, and the catalog role stays on the completion prefixes (:187).",
        "CRITERIA @230168e108: TO-OG-k-1 narrows OGK1-AC5 to data_prefixes and adds OGK1-AC16 (the HEAD/GET key set is a subset of data_prefixes read from org/standards/NFRA_OPLGTW_CONTRACT.json) and OGK1-AC17 ((difference) fact-naming closures make zero fact_* calls and still qualify on dims; a missing dim yields incomplete). TO-OG-v-2 adds OGV2-AC5 (every S3 call is inside the prefixes its role is granted). The to-pipeline-gate's GATE (viii) graded both modified orders at commit.",
        "NO WORKER READ THE OLD TEXT: TO-OG-k-1 (slot ~5) and TO-OG-v-2 (slot ~6) had not been handed at 230168e108; both remain pending."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "W6-S3 (0.9.0_WK_NFRA_OPLGTW~6) is ARMED with disarm_owner 1.0.0_SA_CTO: C3's 'independently HEADs every named silver object' would have the catalog read fact tables that no Gateway read role may read, and moto evaluates no IAM, so a local run could pass on code AWS denies.",
    "world_is": "The owner ruled the ratified text's own reading, so the PRD and the decomposition do not change. The hazard is converted into criteria: a call-set subset check and a fact_* negative arm in the catalog cell, and the same call-set check in the local acceptance run. The live proof stays A13's safe negative fixture, an out-of-prefix HEAD by the reader role reading AccessDenied.",
    "notes": "Disarms W6-S3 on the declared plane, as criteria; the exercised plane is OG-k-1's and OG-v-2's grading. The adjudication of W6-S3 remains 3.0.0_SA_CVO's at L9."
  },
  {
    "id": "NFRA_OPLGTW-W4-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T13:12:00Z",
    "one_line": "The opal-assets root's plan carries two rows outside opal-assets-silver-schwab -- an IAM policy change on the daily emitter's role and an env change on the emitter Lambda, both committed STAGED-NOT-APPLIED by 0.7.0_AE_CloudOps @2740e4de8f -- so the only permitted apply (safe-apply, no -target) would land another seat's held change; no build, upload, apply or replay was done.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PLAN: .tools/terraform.exe -chdir=infra/aws/terraform/opal-assets plan -out, at 271bab18dc on branch wk-nfra_oplgtw-1-4b, finished before 13:08Z on 2026-09-15: 'Plan: 0 to add, 3 to change, 0 to destroy.' Rows: aws_iam_role_policy.emitter (Resource and the s3:prefix condition gain portal/gold/mdpf/_staging/aggregate_aua/*); module.emitter.aws_lambda_function.this (AGGREGATE_PREFIX 'gold/mdpf_revamp/_aggregate_aua/' -> 'portal/gold/mdpf/_staging/aggregate_aua/'); module.silver_converter[\"schwab\"].aws_lambda_function.this (OPAL_BUILD_COMMIT '5c7b2a9a6b' -> '1f03a3f209'). Saved as org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/plans/plan_pre_upload.json.",
        "SOURCE: git log -- infra/aws/terraform/opal-assets/emitter.tf at 3f94e0a024 -- newest commit 2740e4de8f (0.7.0_AE_CloudOps, 2026-08-11), subject 'infra(mdpf+assets, X-ii-a AE half STAGED-NOT-APPLIED): consumer env repoints + IAM pure-adds for the _staging re-home -- apply held for the act's own window'.",
        "BOUND: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-c-2.producer-deploy-replay.md BOUNDS @3f94e0a024 -- 'A plan row for any other family, any IAM change, or any change to the bucket, its notifications or its policy is a BLOCKING row and no apply' and 'Terraform only through .tools/safe-apply.sh, never bare terraform apply, never -target'.",
        "STATE: lambda get-function-configuration opal-assets-silver-schwab read 2026-09-15 ~12:50Z -- CodeSha256 /Uog2LDpLg42FrCU5MfTrEBaTFJTlVRY97tONxmjhVM=, LastModified 2026-08-30T03:37:41Z, OPAL_BUILD_COMMIT 5c7b2a9a6b; s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-silver-schwab.zip latest version RigDVPxrZlvI49kyJJrOMk4vXnxEACzs (2026-08-30T03:31:43Z). This worker changed neither."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-c-2: deploy opal-assets-silver-schwab through module.silver_converter with .tools/safe-apply.sh, never -target, on a plan that 'changes only opal-assets-silver-schwab and shows zero rows for the other five families' (OGC2-AC3); then run the replay.",
    "world_is": "The root's plan carries another seat's staged-and-held IAM grant and env repoint for opal-assets-daily-emitter. With -target forbidden, no permitted apply of this root can move the schwab function alone until that change is applied in its own window or withdrawn. The order stops at the plan: OGC2-AC3 FAILs by output, and OGC2-AC4, AC5 and AC7-AC10 have no act to grade.",
    "notes": "Nothing is armed: no artifact uploaded, no ledger entry opened, and the function and every marker are unchanged. Two things unblock it: 0.7.0_AE_CloudOps applies or withdraws the staged emitter change in its window, or the issuer amends the order's apply route. The vendoring and pin commit 271bab18dc stands, so its OPAL_BUILD_COMMIT row is already in the plan; the next attempt re-reads the plan before any upload."
  },
  {
    "id": "NFRA_OPLGTW-W4-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T13:12:30Z",
    "one_line": "The order routes code under data/*/scripts/silver/ through Rule 13's DS guard (.tools/safe-deploy.sh), but the guard's PIPELINE_MAP holds black_diamond, inf, cot, mdpf and advi -- no assets -- and this Lambda deploys as a zip built from its package dir, so the guard has no path to grade here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "GUARD: py -3.12 -c 'import safe_deploy_core as s; print(list(s.PIPELINE_MAP))' with .tools on sys.path, at 3f94e0a024 -> ['black_diamond', 'inf', 'cot', 'mdpf', 'advi'].",
        "MAP: infra/aws/lambda/ci/lambda-source-map.json @3f94e0a024, entry opal-assets-silver-schwab -- source_dir infra/aws/lambda/opal-assets/opal-assets-silver-schwab, tf_file infra/aws/terraform/opal-assets/silver.tf, artifact_s3_key opal-assets/opal-assets-silver-schwab.zip, 12 files.",
        "MODULE: infra/aws/terraform/modules/yang-lambda/main.tf:17-39 @3f94e0a024 -- the function reads the artifact's S3 object version and its content-sha256 metadata, which infra/aws/lambda/ci/build-and-upload.sh writes."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-c-2 THE CELL: 'Rule 13: code under data/*/scripts/silver/ deploys through the DS lane's .tools/safe-deploy.sh guard; if that guard, or any lane, refuses your serial, file a BLOCKING row and stop'.",
    "world_is": "The guard was not invoked: it maps no data/assets tree and grades S3 code-prefix copies, not a Lambda zip. Neither the guard nor any lane refused this serial. The path the estate uses for this function is build-and-upload.sh, then safe-apply.",
    "notes": "INERT: not blocking. Recorded so a re-cut does not seat a DS lane for a guard that does not reach this package."
  },
  {
    "id": "NFRA_OPLGTW-W4-S7",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T13:13:00Z",
    "one_line": "The named build (infra/aws/lambda/ci/build-and-upload.sh opal-assets opal-assets-silver-schwab) rewrites infra/aws/lambda/ci/lambda-source-map.json after a verified upload, and this order's grant does not name that path; the build was not run here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "BUILD: infra/aws/lambda/ci/build-and-upload.sh:125-138 and :433-438 @3f94e0a024 -- after the verified upload, a node helper writes artifact_s3_key and artifact_sha256 into SOURCE_MAP_PATH, the source map.",
        "GRANT: the <paths> block of NFRA_OPLGTW.TO-OG-c-2.producer-deploy-replay.md @3f94e0a024 names 7 paths, none under infra/aws/lambda/ci/."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-c-2: 'Find the build that writes that artifact from the vendored directory, and use it'; BOUNDS 'Grant': the <paths> block is the write surface, and 'A path you need that is not named is a BLOCKING surprise row on that criterion'.",
    "world_is": "Running the build as written leaves an out-of-grant change to lambda-source-map.json. Unless its owner commits that change, the map's artifact_sha256 stays stale at HEAD. Not exercised: the order stopped at the plan (NFRA_OPLGTW-W4-S5) before any build.",
    "notes": "INERT (not run). For a re-cut: grant infra/aws/lambda/ci/lambda-source-map.json, or state that the map update stays uncommitted."
  },
  {
    "id": "NFRA_OPLGTW-W4-S8",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T13:13:30Z",
    "one_line": "The G-B sign-off's conditions 4, 5 and 7 need reads of s3://opal-data-49financial/gold/advi/ (the floor's CHAIN OK log, the date=D VersionIds), but the order's cross-firm bound reads 'Only schwab/08242234/ and schwab/08335338/; no other firm's bucket or prefix'. This worker read that bucket once, for condition 4: one listing and one log object.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SIGNOFF: org/tier1_exec/2.0.0_SA_COO~O/deliverables/NEVER_WIDEN_SIGNOFF_NFRA_OPLGTW_OG_C2.md @65e254cafe, Half 2 section E, conditions 4, 5 and 7 -- the 08335338 write waits for 'that day's 12:45Z floor reads CHAIN OK date=<prev_trading_day> in gold/advi/_logs/', and the result names before/after VersionIds of every date=D key.",
        "ORDER: NFRA_OPLGTW.TO-OG-c-2.producer-deploy-replay.md BOUNDS @3f94e0a024 -- 'Cross-firm law. Only schwab/08242234/ and schwab/08335338/; no other firm's bucket or prefix.'",
        "READS: 2026-09-15 ~12:53-12:55Z, s3api list-objects-v2 --bucket opal-data-49financial --prefix gold/advi/_logs/chain_20260915 -> 7 objects; get-object gold/advi/_logs/chain_20260915T124542Z.log (VersionId 3eNJFWhmCUu_orz4If4TQ83BMOdrVHkq) -> line 1 'CHAIN START date=2026-09-14 mode=production ...', last line 'CHAIN OK date=2026-09-14 wall=132.0s'.",
        "CONSUMER: infra/aws/terraform/opal-assets/silver.tf:755-761 @3f94e0a024 -- the accelerator on schwab/08335338/meta/complete/ targets advi-49f-gold-dispatch, the 49F chain's dispatcher."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's cross-firm bound, and sign-off condition 4, which the order makes binding through 'Read: ... the sign-off record'.",
    "world_is": "The two binding carriers disagree on one read. Meeting condition 4 before the 08335338 replay needs a read of the 49F gold bucket. The order's bound forbids that read, unless 08335338's own firm is 49 Financial; the accelerator wiring suggests it is, but no carrier this worker read says so. Reads only; nothing written.",
    "notes": "INERT: two read calls, no write. The issuer states which reading binds before any replay runs."
  },
  {
    "id": "NFRA_OPLGTW-W4-S9",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-15T13:14:00Z",
    "one_line": "The producer's only replay path for one date is an event naming that date's bronze keys, with force false. That path also PUTs one run manifest per lane at schwab/{master}/meta/conversions/{run_id}.json, which neither 'the replay writes completion records only' nor the sign-off's A2 write set (2 marker keys) names. It would also write any missing projection dim, because the skip needs the fact AND every dim present.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUNTIME: data/assets/scripts/silver/schwab_runtime.py:207-213 @1f03a3f209 -- run_event builds and writes one manifest per lane (cm.write_manifest_verified) before the marker; :385-405 -- lambda_entry accepts only S3 Records or {\"mode\": \"sweep\"}. The sweep (:271-369) converts every shortfall on all dates, writes backfill-status.json and drains the DLQ.",
        "MANIFEST: data/assets/scripts/silver/conversion_manifest.py:53-56 and :124-129 @1f03a3f209 -- manifest_key = 'schwab/' + master + '/meta/conversions/' + run_id + '.json', written by client.put_object.",
        "SKIP: data/assets/scripts/silver/schwab_conversion.py:461-469 @1f03a3f209 -- skip = fact_exists and not dims_missing; :489-506 -- each missing dim gets a ChunkedParquetWriter, i.e. a silver write. :248-258 -- existence is head_object on the key."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "BOUNDS 'No source mutation': 'No write, delete or overwrite of any bronze or silver object; the replay writes completion records only'; sign-off Half 1 s.4: A2 writes '2 keys for D_r, one per master'.",
    "world_is": "An event replay writes 4 objects (2 markers + 2 run manifests), not 2, and no producer path writes the marker alone. A read-only dry run of the same convert_object can decide, before the replay, whether a silver dim would be written for the chosen date. That dry run was not run here, because the order was blocked at NFRA_OPLGTW-W4-S5.",
    "notes": "INERT (not run). For a re-cut: add the run manifests to the write set, or name a metadata-backfill route instead."
  },
  {
    "id": "NFRA_OPLGTW-W1-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-15T10:44Z",
    "one_line": "OG-i-1's plan of the opal-gateway root reads 4 to add, 2 to change, 0 to destroy: the two change rows are in-place '+ description' backfills on the existing aws_wafv2_ip_set.opal_blocked_ips_regional_v4 and _v6, so the order's own blast-radius bound refuses the apply.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PLAN: .tools/terraform.exe v1.9.8 'plan -input=false -out' on infra/aws/terraform/opal-gateway at worktree base 417631ae6f, 2026-09-15T10:42:25Z..10:42:38Z, rc 0: 'Plan: 4 to add, 2 to change, 0 to destroy.' -- 71 resource_changes = 65 no-op + 4 create (this cell's four) + 2 update; redacted plan JSON at org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/og_i1.plan.json.",
        "DIFF: each update changes exactly one attribute, description, absent live and declared in waf.tf ('+ description = NFRA_OPSEC202609 C-2: addresses blocked at the ALB. Written ONLY by the OP-s-15 reconciler ...'); addresses is not in the diff because of lifecycle ignore_changes = [addresses] at infra/aws/terraform/opal-gateway/waf.tf:294-296 and :335-337 @417631ae6f.",
        "PRIOR RECORD: commit 3758b14afc (2026-09-04, 0.7.0_AE_CloudOps~T) says in its message 'THE ONLY REMAINING DIFF ON ALL FOUR SETS IS + description, a backfill of a field absent on the live resource -- benign'; the declared strings date from 37c4bde812 (waf.tf:261 and :271), so this diff has stood on the root since then.",
        "BOUND: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-i-1.access-state-table.md @417631ae6f BOUNDS 'Blast radius': 'A plan that shows any change or destroy is refused: a BLOCKING row, no apply.', and 'Terraform': 'never -target'. CLOUD @496a89e4b5 carries no change under infra/aws/terraform/opal-gateway/ against the base (git diff --stat empty)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order and the decomposition (OG-i-1 acceptance, first bullet, decomposition @8768f46770 line 178) assume a plan of the opal-gateway root that creates only this cell's four resources and changes nothing that exists.",
    "world_is": "Every plan of this root also carries two in-place description backfills on the Gateway's regional blocked-IP sets, which NFRA_OPSEC202609 owns. With -target forbidden and the bound literal, no apply of this cell is admissible: no ledger entry was opened, nothing was applied, and OGI1-AC2..AC9 have no applied object to read. The branch wk-nfra_oplgtw-1-1 carries infra/aws/terraform/opal-gateway/schwab_access_state.tf DECLARED and NOT APPLIED, so any later apply of this root from a tree that holds it (a drain to CLOUD included) would create the table and both grants outside this order's ledger.",
    "notes": "INERT: nothing moved in AWS. Form only, not significance: the diff leaves this cell's plan by one of two acts, neither this worker's -- the order's author names the two description backfills as admitted changes in the bound, or the IP sets' owner applies the backfill under its own ledger so the root plans with no change to existing resources. The probe's OGI1-AC1 arm reads the saved plan and prints both NOT-CREATE rows."
  },
  {
    "id": "NFRA_OPLGTW-W1-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-15T10:55Z",
    "one_line": "The order runs OGI1-AC8, the operator revision race, 'through SSM on i-07dccb1615503ac99 with the instance's own role', but that role is the RUNTIME principal, which by the same order cannot write POLICY# keys; the race can run only under the separate operator role.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: NFRA_OPLGTW.TO-OG-i-1 @417631ae6f lines 48-49: 'The on-host arms (AC7, AC8) run through SSM on i-07dccb1615503ac99 with the instance's own role'; OGI1-AC6 and OGI1-AC8 name the operator principal and two concurrent operator revisions of one POLICY# record.",
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:193 @f0aa50dbc0: 'The operator role alone may conditionally update POLICY records' and runtime writes are 'conditioned through dynamodb:LeadingKeys to the RUNTIME prefix only'.",
        "LIVE: ec2 describe-instances i-07dccb1615503ac99 at 2026-09-15 ~10:36Z: running, IamInstanceProfile arn:aws:iam::313476888478:instance-profile/opal-gateway-profile, whose role is opal-gateway-role (infra/aws/terraform/opal-gateway/main.tf:160-163 @417631ae6f)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGI1-AC7 and OGI1-AC8 are both on-host arms run with the Gateway instance's own role.",
    "world_is": "Only OGI1-AC7 can be. The probe's AC8 arm assumes opal-gateway-access-admin from the checkout's operator identity (arn:aws:iam::313476888478:user/Andrew_Berman) and races two conditional UpdateItem calls (ConditionExpression revision = 1) released by one barrier. Running it on the host would require the operator role to trust opal-gateway-role, which schwab_access_state.tf refuses by aws:PrincipalArn and OGI1-AC6 grades as separation.",
    "notes": "INERT: the arm was not exercised in this run, because W1-S1 blocks the apply. The race uses single-item conditional UpdateItem rather than TransactWriteItems because two concurrent transactions on one item can be cancelled with TransactionConflict rather than ConditionalCheckFailed; the operator's one-transaction update-plus-audit is exercised separately in the AC6 arm."
  },
  {
    "id": "NFRA_OPLGTW-W1-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-15T10:52Z",
    "one_line": "The PRD and OGI1-AC5 grant and grade 'TransactWrite' as a runtime action, but dynamodb:TransactWriteItems is not an IAM action: AWS Access Analyzer returns INVALID_ACTION for it, and a transaction is authorized per item against PutItem and UpdateItem.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "LIVE: aws accessanalyzer validate-policy --policy-type IDENTITY_POLICY, us-east-1, account 313476888478, one Allow on the table ARN: dynamodb:TransactWriteItems at 2026-09-15T10:52:10Z -> 'ERROR INVALID_ACTION The action dynamodb:TransactWriteItems does not exist.'; positive control dynamodb:PutItem at 10:52:13Z -> no finding; dynamodb:TransactGetItems at 10:52:16Z -> 'ERROR INVALID_ACTION The action dynamodb:TransactGetItems does not exist.'",
        "SPEC: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:189 @f0aa50dbc0 'limited to needed Get/Put/Update/TransactWrite operations' and :193 'all transaction items must satisfy the restriction'; OGI1-AC5 in NFRA_OPLGTW.TO-OG-i-1 @417631ae6f."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The runtime grant allows Get, Put, Update and TransactWrite on the table, as four grantable operations.",
    "world_is": "A policy naming dynamodb:TransactWriteItems would carry an action that grants nothing. schwab_access_state.tf grants GetItem, and PutItem and UpdateItem under ForAllValues:StringLike dynamodb:LeadingKeys RUNTIME#* with Null dynamodb:LeadingKeys false -- the same condition that binds every item of a TransactWriteItems call. The probe's AC5 arm grades TransactWrite on those constituents, and its AC7 arm exercises a mixed RUNTIME# plus POLICY# transaction as a supplementary line.",
    "notes": "INERT: no grant was applied (W1-S1). The same holds for a later cell that wants transactional reads: TransactGetItems is authorized against GetItem."
  },
  {
    "id": "NFRA_OPLGTW-S7",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T14:04Z",
    "one_line": "Disarm of W3-S7 by its owner: OG-a-2's branch wk-nfra_oplgtw-1-3c is held UNMERGED, so its 16 red existing tests never reach CLOUD; the fix needs three test files no order grants, which changes the frozen decomposition's write surface for OG-a-2, so whether to grant them in-round or in round 2 is asked of 1.0.0_SA_CTO.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RE-RUN BY THIS SEAT (a different invocation from the worker's census, same venv): at wk-nfra_oplgtw-1-3c @fed567f54e, per module with -m 'not live': test_jwt_cve_lock.py '1 failed, 5 passed'; test_schwab_audit.py '1 failed, 6 passed'; test_oauth_durable.py '14 failed, 4 passed'; test_principal_cutover.py '11 passed'. That is 16 failures, the worker's count exactly.",
        "WHY THE TESTS FAIL (row W3-S7): the durable fixture's fake sign-in yields only an email (test_oauth_durable.py:128-137, :186-189 @3f94e0a024), and the other two tests mint a family-less access token for an email (test_jwt_cve_lock.py:64-66, test_schwab_audit.py:301-305). Both are the legacy access C1 removes, which OGA2-AC4 and AC5 grade.",
        "SURFACE: the decomposition @8768f46770 lists OG-a-2's write surface as six app modules plus tests/test_principal_cutover.py (new), and TO-OG-a-2's <paths> matches it. None of the three test files appears. Mid-round the decomposition is frozen (CLAUDE.md Rule 27)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-a-2 requires 'tests/test_oauth_durable.py stays green' and forbids editing an existing test, while its criteria remove the email-only sign-in and family-less tokens those tests use.",
    "world_is": "The order cannot be met as written: every criterion passes (proof VALID 11/11 on the branch), and 16 existing tests fail because they assert the removed behaviour. The repair belongs to the three test files: the durable fixture's upstream fake returns a tid/oid principal, and the two single tests mint from a refresh family. Until a cell holds those files, the branch stays unmerged, and every cell built on OG-a-2 (OG-a-3, OG-z-1, OG-z-3, OG-z-2, then OG-k-1, OG-v-2, OG-r-1) waits.",
    "notes": "INERT: nothing is merged or deployed; CLOUD's suite is unchanged. The worker flipped the order complete on its branch by the mechanical rule, and the breach travels in W3-S7. Asked of 1.0.0_SA_CTO: grant the three files to OG-a-2 in round 1, limited to how the tests obtain a principal or token, or carry the repair to round 2."
  },
  {
    "id": "NFRA_OPLGTW-S8",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T14:05Z",
    "one_line": "Disarm of W3-S9 by its owner: the email-keyed tier and tool allowlist only become a live exposure when OG-a-2's code is deployed, which is OG-r-1, so this seat does not hand OG-r-1 while W3-S9 is undispositioned; whether PRD C1's 'email is display/audit metadata only' reaches the existing tier layer is asked of 1.0.0_SA_CTO.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: NFRA_OPLGTW-W3-S9 (0.9.0_WK_NFRA_OPLGTW~3), ARMED, disarm_owner 2.0.0_SA_COO~O, on branch wk-nfra_oplgtw-1-3c @fed567f54e: tools.py:72,79,84, integrations/base.py:114,120,125 and query_v0.py:134 still resolve tier, tool scope and the /query/v0 principal from get_current_email() @3f94e0a024.",
        "SCOPE READ: TO-OG-z-1 (policy guard) keys the NEW data grants by tid/oid (OGZ1-AC1) and denies a restricted principal with an opalinvest.com email on /query/v0 (OGZ1-AC9). Its bounds put the existing tier and tool allowlist out of its scope: 'Existing users are regression, not scope ... identity_tool_allowlist.txt and tests/test_identity_scope.py are not yours'.",
        "NO DEPLOY BEFORE OG-r-1: every Gateway cell's order says 'Nothing deploys' and names OG-r-1 as the release (e.g. TO-OG-a-2 BOUNDS). The live Gateway runs 7bd89b5d71's code (OG-p-1 OGP1-AC1), which already resolved by email before this project."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C1 :131 says email is display/audit metadata only, and C2 :145 says 'Key grants by tid/oid, not email'.",
    "world_is": "After OG-a-2 the session, families, tokens, revocation and Graph cache are keyed by (tid, oid). The pre-existing tier, tool allowlist and integration min-tier gate still key by email, and no round-1 cell's order re-keys them (OG-z-1 re-keys only the new Schwab grants). The exposure is unchanged from before this project and does not reach users until OG-r-1 deploys.",
    "notes": "Disarmed at a named moment by the named owner: 2.0.0_SA_COO~O does not hand TO-OG-r-1 while W3-S9 has no disposition. The scope question (re-key the existing tier layer in this project, or leave it as a pre-existing, out-of-scope condition) is 1.0.0_SA_CTO's as L4 owner and was asked with this row. The adjudication is 3.0.0_SA_CVO's at L9."
  },
  {
    "id": "NFRA_OPLGTW-S9",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T14:58Z",
    "one_line": "Record of 1.0.0_SA_CTO's three in-round rulings (msg 97114) and the amendments that carry them: OG-a-2 is granted three test files fixture-only (AC12, AC13); W3-S9 is in scope as a round-2 cell and OG-r-1 is guarded by AC11; suite criteria run per module over a glob-derived list.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULING 1 (a): amend TO-OG-a-2 in round 1 to grant tests/test_oauth_durable.py, tests/test_jwt_cve_lock.py and tests/test_schwab_audit.py. Edits touch only how each test obtains a principal or token; no assertion is removed, weakened or re-targeted. Criteria: the three modules pass, and per module the assert count at HEAD equals the count at the base. Carried @adc6874dea on the held branch wk-nfra_oplgtw-1-3c (OGA2-AC12, OGA2-AC13; status back to pending).",
        "RULING 2: C1 :131 puts every authorization that still resolves by email in NFRA_OPLGTW's scope, including the existing tier, the per-identity tool allowlist and the integration min-tier gate. No round-1 cell holds it, so it is a round-2 cell named in the CTO's round-1 analysis. W3-S9's disposition is 'in scope, round-2 cell'. The release ships in round 1 only if the Schwab path's authority is the tid/oid grant. Carried @43e7076fb6 as OGR1-AC11: locally and before the deploy, a predecessor's email and tier with no tid/oid grant is denied every Schwab tool. If it fails, nothing deploys.",
        "RULING 3 (note 3): round-1 suite criteria run per module over a module list derived by glob of infra/aws/ec2/opal-gateway/tests/test_*.py, never typed, and print the module count. The census of unhanded orders naming a one-process suite run found 1 (TO-OG-v-2 AC4); TO-OG-a-1's AC19 belongs to a complete order and is untouched. Carried @43e7076fb6. The root cure, scoping tests/test_ratelimit.py's import-time time.monotonic patch, is a round-2 hygiene cell."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Mid-round the PRD, the decomposition and the issued orders are frozen, and TO-OG-a-2 forbade editing existing tests while granting none of the three files its criteria break.",
    "world_is": "1.0.0_SA_CTO, as L4 owner, ruled that the three changes are C1's own outcome or a necessary invocation change, not new scope. Each is carried as criteria in orders no worker is reading. Two round-2 cells are named: re-keying the email-based tier layer, and scoping the ratelimit clock patch. Row S8's hand-off hold on OG-r-1 resolves into OGR1-AC11.",
    "notes": "The rulings are the authority these amendments cite. W3-S7, W3-S9, W3-S6 and W3-S12 are adjudicated by 3.0.0_SA_CVO at L9."
  },
  {
    "id": "NFRA_OPLGTW-S10",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T15:52Z",
    "one_line": "Disarm of W3-S13 by its owner: OG-a-2's branch stays HELD UNMERGED after the fixture-only re-run, because its three remaining red tests are assertions of sub == email that the ruling's bound forbids re-targeting; whether they may be re-targeted to the tid/oid principal is asked of 1.0.0_SA_CTO.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RE-READ BY THIS SEAT at wk-nfra_oplgtw-1-3c @f8feaf081e: test_oauth_durable.py:710 asserts validate_access_token(...)['sub'] == email; test_jwt_cve_lock.py:117 asserts validate_access_token(tok)['sub'] == 'attacker@opalinvest.com'; test_schwab_audit.py:342 asserts claims['sub'] == 'colleague@opalinvest.com'. The cell's own AC1 test asserts claims['sub'] == '%s/%s' % (TENANT, oid) and '@' not in claims['sub'] (test_principal_cutover.py:410).",
        "FIXTURE-ONLY HELD: git diff 3f94e0a024..wk-nfra_oplgtw-1-3c over the three granted files contains 0 changed lines that assert or call pytest.raises. The worker's AC13 reads equal assert counts per module (123/123, 6/6, 63/63).",
        "RULING: 1.0.0_SA_CTO msg 97114 (1) bounds the grant as 'No assertion is removed, weakened or re-targeted'. The worker refused OGA2-AC12 ('3 failed, 28 passed') rather than cross it; the proof instance is VALID and the order stays pending."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Ruling 97114 (1) expects the fixture-only edit to turn the 16 red tests green without touching any assertion.",
    "world_is": "13 of the 16 turned green. The 3 left are assertions whose expected value is the removed identity (sub = email), so no fixture can satisfy them while AC1 holds. The question put to 1.0.0_SA_CTO is whether each may become 'sub == <tid>/<oid> and email == <the same email>': one expression each, keeping its intent and its assert count.",
    "notes": "INERT: nothing is merged or deployed and CLOUD's suite is unchanged. Row S7's hold continues under this row. On an affirmative ruling this seat amends TO-OG-a-2 on the branch with the ruling's discriminator and re-hands slot ~3."
  }
]
```
