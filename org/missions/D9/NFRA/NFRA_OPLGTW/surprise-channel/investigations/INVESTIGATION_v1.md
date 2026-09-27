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
  },
  {
    "id": "NFRA_OPLGTW-S11",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T15:55Z",
    "one_line": "Record of 1.0.0_SA_CTO's ruling msg 97141, which amends 97114 (1): exactly three assertions of sub == email are re-targeted to the tid/oid principal AND the same email, bound by four arms that TO-OG-a-2 now carries as AC12 (31 passed), AC13 and the new AC14; W3-S13 is disarmed on the green re-run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULING 97141: test_oauth_durable.py:710, test_jwt_cve_lock.py:117 and test_schwab_audit.py:342 each go from sub == <email> to sub == '<tid>/<oid>' of that test's principal AND email == <the same email>. 97114's 'no assertion re-targeted' stops a check being weakened; these three asserted the identity C1 :131 removes, and the re-targeted form is stricter because it checks both the principal and the email.",
        "BOUND (four arms): (1) the diff against the base changes exactly those 3 assertion lines; (2) each keeps its original email literal or variable; (3) AC13's per-module assert counts stay 123/123, 6/6, 63/63; (4) AC12 reads 31 of 31. A token without the email claim fails the test, and that is a row; the email half is never dropped.",
        "CARRIED on the held branch wk-nfra_oplgtw-1-3c: TO-OG-a-2 amended (AC12's expect is '^31 passed'; OGA2-AC14 added) in this seat's commit after f8feaf081e; slot ~3 is re-handed on that order."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Ruling 97114 (1) bounds the grant as 'No assertion is removed, weakened or re-targeted'.",
    "world_is": "The owner of the ruling narrows it: three named assertions, which asserted the removed identity, are re-targeted to a stricter form. Every other assertion is still bound unchanged, and the four arms are mechanical criteria.",
    "notes": "Recorded beside S9 (ruling 97114) at 1.0.0_SA_CTO's request. W3-S13 and S10's hold are disarmed at OG-a-2's drain once the re-run is green; the adjudication is 3.0.0_SA_CVO's at L9."
  },
  {
    "id": "NFRA_OPLGTW-W3-S7",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T13:48:30Z",
    "one_line": "Three existing Gateway test files assert the pre-cutover behaviour this order's criteria remove, so after OG-a-2 16 existing tests fail (test_oauth_durable 14 of 18, test_jwt_cve_lock::test_control_valid_token_accepted, test_schwab_audit::test_ogo1_ac06), while the order requires test_oauth_durable.py to stay green, forbids editing an existing test, and grants none of the three files.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-a-2.principal-cutover.md @3f94e0a024 -- BOUNDS 'tests/test_oauth_durable.py stays green' and 'No existing test is edited to make it pass'; <paths> names five app modules, tests/test_principal_cutover.py and this channel, none of the three test files.",
        "FIXTURE: infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py:186-189 @3f94e0a024 -- monkeypatches token_broker.redeem_code_for_email with LocalIssuer.redeem, which returns claims['email'] (:133-137); the LocalIssuer ID token carries no tid or oid (:128-131).",
        "TESTS: infra/aws/ec2/opal-gateway/tests/test_jwt_cve_lock.py:64-66 and infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py:301-305 @3f94e0a024 -- issue_access_token(<email>, 'mcp', <client>) with no refresh family, then validate_access_token(token)['sub'] == <email>.",
        "RUN base 3f94e0a024, one process per module, -m 'not live' -k 'not test_scoped_deny_by_default': 12 modules, 121 passed, 1 deselected, 0 failed. The same at d02e73c272: test_oauth_durable '14 failed, 4 passed' (each 'Sign-in refused ... the upstream identity provider is not configured', assert 400 == 302; AC1, AC2, AC4, AC14 still pass), test_jwt_cve_lock '1 failed, 5 passed' and test_schwab_audit '1 failed, 6 passed' (TypeError: issue_access_token() missing 1 required positional argument: 'family_id'); the other 9 modules unchanged.",
        "EGRESS: tests/test_oauth_durable.py plus tests/test_principal_cutover.py at d02e73c272 under a socket-and-DNS-refusing pytest plugin: 'EGRESS-ATTEMPTS: 0' -- the refused callbacks make no network call."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order binds 'tests/test_oauth_durable.py stays green' and 'No existing test is edited to make it pass', and grants only app modules plus tests/test_principal_cutover.py; its criteria require the token and request context to carry the validated tid/oid (OGA2-AC1), every protected route to reject a token lacking the token version and principal (OGA2-AC4), and the family to be checked on every request (OGA2-AC6).",
    "world_is": "test_oauth_durable's fixture replaces the upstream seam with a fake that yields only an email, so no immutable principal can come back from its sign-in: the bridge, which now requires a validated tid/oid, refuses that sign-in fail-closed and every durable test that completes one fails at the callback. The other two tests mint a family-less access token for an email and expect it accepted -- the legacy token OGA2-AC4 must reject. No design meets the bound and the criteria together: any path that turns an email-only upstream result or a family-less token into access is the email or legacy authorization that C1 removes. The worker edited none of the three files.",
    "notes": "ARMED: left alone, the drain carries 16 red existing tests into CLOUD and every later Gateway cell inherits them. Disarm: a re-cut granting the three files to a cell -- the durable fixture's upstream fake returns a tid/oid principal through token_broker.redeem_code_for_principal, as tests/test_principal_cutover.py's local issuer does, and the two single tests mint from a refresh family. The 11 OG-a-2 criteria pass by output either way."
  },
  {
    "id": "NFRA_OPLGTW-W3-S8",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T13:48:30Z",
    "one_line": "A denied entitlement at the MCP tool layer comes back as a SUCCESSFUL MCP result (isError false) whose text is the denial, because tools._run returns every denial as a dict; the gateway never answers it with a 401, a challenge or a login, but a client that reads only isError sees success, and tools.py is outside this order's grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:141 @f0aa50dbc0 -- 'A denied data entitlement is a terminal tool authorization error, not an OAuth escalation or a login loop.'",
        "CODE: infra/aws/ec2/opal-gateway/app/tools.py:74-106 @3f94e0a024 -- every _run denial is a returned dict {error, guard_denied: True, code}, never a raised tool error.",
        "PROBE at the base code (scratch, MOCK_GRAPH, no identity): POST / on the MCP app, tools/call send_email -> 200 text/event-stream, result content '{error: no verified identity established, guard_denied: true, code: identity_required}' with 'isError': false.",
        "RUN: test_oga2_ac11 at d02e73c272 prints 'policy denial (read-only -> send_email) x2 -> HTTP 200, no WWW-Authenticate, tool result guard_denied code=read_only_denied ... (MCP isError=False); Graph 403 -> HTTP 200, tool error ... (isError=False)'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGA2-AC11: 'a denied data entitlement returns a terminal tool error and never a 401 or an OAuth escalation'; C1: 'a terminal tool authorization error'.",
    "world_is": "The denial is terminal (identical on repeat, no needs_login, no login_url, no challenge, and the same token keeps working), and OGA2-AC11 asserts exactly that. At the protocol level, though, the tool call reports success and carries the denial as its text. Raising the denial as an MCP tool error (isError true) is a change to tools._run, outside this grant.",
    "notes": "INERT: no OAuth loop and no 401 is possible from it; the model reads the denial text. Recorded for OG-z-1, which owns the tool policy layer and the new data entitlements it will add."
  },
  {
    "id": "NFRA_OPLGTW-W3-S9",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T13:48:30Z",
    "one_line": "The session is now bound to the tid/oid principal, but every authorization decision after the guard still keys on the email the principal carries for display -- tier (andrew@opalinvest.com resolves MASTER_ADMIN by default), the per-identity tool allowlist, the integration min-tier gate and the /query/v0 catalog principal -- so a second principal holding the same email still inherits the first one's tier and tool scope.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:131 @f0aa50dbc0 -- 'email is display/audit metadata only'; :145 -- 'Key grants by tid/oid, not email'; :255 -- A3 'tid/oid mismatch denied even with same email'.",
        "DECOMP: org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md:614 @8768f46770 -- 'A3 | OG-a-2, OG-z-1'.",
        "CODE @3f94e0a024: infra/aws/ec2/opal-gateway/app/tools.py:72,79,84 (email = get_current_email(); tier.resolve_tier(email, cfg); identity_scope.check(email, tool)); app/integrations/base.py:114,120,125 (the same three); app/query_v0.py:134 (_principal(email)); app/config.py:241-245 (MASTER_ADMIN_EMAILS default 'andrew@opalinvest.com').",
        "RUN: test_oga2_ac08 at d02e73c272 -- two principals, one email: B's principal on A's family -> 401; B's Graph call used B's delegated token; A revoked by principal key -> A 401, B 200. Those are the bindings inside this grant."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGA2-AC8: 'a principal with the same email and a different oid is denied (A3)'; C1: 'email is display/audit metadata only'.",
    "world_is": "Within its grant the worker bound codes, refresh families, access tokens, the request context, the rate-limit key, principal revocation and the delegated Graph cache to (tid, oid), and OGA2-AC8 shows the second principal denied the first one's family, Graph token and revocation state. The consumers that decide what a caller may do read get_current_email(): tools.py, tier.py, identity_scope.py, integrations/base.py and query_v0.py, all outside the grant, all still resolving by email. The blocklist also matches by email, which only adds denial.",
    "notes": "ARMED: until the grant and tier layer keys on the principal (C2, OG-z-1, which depends on this cell), a reassigned email inherits the previous holder's tier and tool scope at its next sign-in. Not a new exposure: the same resolution by email held before this cell."
  },
  {
    "id": "NFRA_OPLGTW-W3-S10",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T13:48:30Z",
    "one_line": "To keep a Graph-using tool's NeedsLogin from looping, the worker also changed the legacy /login consent route (build_consent_url, redeem_consent) to validate the ID token and write the principal's cache, which the order does not name; and a principal's FIRST delegated Graph token now comes from the refresh token of an OpenID-only sign-in, which nothing offline can measure against Entra.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:131 @f0aa50dbc0 -- 'Authentication must not require Graph mail/file consent; retain delegated Graph acquisition only for tools that use it.'",
        "BASE: infra/aws/ec2/opal-gateway/app/token_broker.py:35-38, 136-156 @3f94e0a024 -- one cache per sha256(email); build_auth_url and redeem_code both request GRAPH_SCOPES; app/tools.py:108-111 -- NeedsLogin returns login_url, which is /login (token_broker.py:28).",
        "BUILD: infra/aws/ec2/opal-gateway/app/token_broker.py @d02e73c272 -- build_auth_url asks AUTHENTICATION_SCOPES ('email'; MSAL adds openid, profile, offline_access); build_consent_url asks GRAPH_SCOPES; redeem_consent writes the principal-keyed and the email-keyed cache; _cache_owner_for reads the principal's cache when the request carries that principal.",
        "RUN: test_oga2_ac02 at d02e73c272 -- sign-in scopes ['email'], code-redemption scopes ['email'], Graph scopes among them 0 of 17; the /login consent URL asks 17 scopes; test_oga2_ac03 -- the delegated Graph token acquired silently from the sign-in's cache at 8 read-only tier scopes (a fake MSAL client)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The cell text names the bridge's Graph coupling (token_broker requests GRAPH_SCOPES) and the context; it says nothing of the /login consent route or of where a Graph-using tool's first token comes from once the sign-in stops asking for Graph scopes.",
    "world_is": "Once the bridge asks for identity only, a Graph tool's token must come from the principal's MSAL cache, keyed by tid/oid so that a same-email principal cannot reach it. NeedsLogin sends the user to /login, whose callback wrote only an email-keyed cache that a principal-keyed lookup never reads: a login loop. The worker made /login's callback validate the ID token as the bridge does and write the cache under both the principal and the access-layer email; the fixed server-held identities of /otp and /ms still read theirs by email. Whether Entra issues a Graph token silently from an OpenID-only sign-in's refresh token depends on the tenant's existing delegated consent for the app registration. The harness fakes that exchange.",
    "notes": "INERT: nothing deploys in this order. The live half -- silent Graph acquisition after an OpenID-only sign-in, and the /login fallback -- is OG-v-2's and OG-v-4's to exercise."
  },
  {
    "id": "NFRA_OPLGTW-W3-S11",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T13:48:30Z",
    "one_line": "GET /ms/site_children answers 400 'site_id required' before it checks any credential, so the OGA2-AC4 census had to send well-formed parameters before that route's own gate would answer; the worker did not reorder the handler.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: infra/aws/ec2/opal-gateway/app/server.py:636-641 @3f94e0a024 -- ms_site_children returns 400 when site_id is absent and only then calls _ms_run, whose _ms_guard checks the bearer.",
        "RUN: the first test_oga2_ac04 run at the build -> AssertionError ('/ms/site_children', 'capability', 400, '{\"error\":\"site_id required\"}'); with site_id supplied the legacy token is refused 401 on 19 of 19 protected routes (test_oga2_ac04 at d02e73c272)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGA2-AC4: every protected MCP and REST route rejects an access token lacking the new token-version and principal claims, over all route declarations.",
    "world_is": "One protected route validates its query parameters before its credential, so an unauthenticated caller learns its parameter contract and a credential census that sends no parameters reads a 400, not a rejection. Reordering the handler is a neighbouring behaviour, not this cell's; the census supplies site_id, q and path to every /ms/* GET.",
    "notes": "INERT: the 400 releases no data; the route still refuses every credential it does not accept."
  },
  {
    "id": "NFRA_OPLGTW-W3-S12",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T13:48:30Z",
    "one_line": "At the cut base 3f94e0a024 the whole Gateway test suite does not finish in one process: after tests/test_ratelimit.py freezes time.monotonic at import (row W3-S6), test_schwab_engine.py::test_ogq1_ac02 waits on the event-loop clock and never returns, so a 300 s bound expired on it; the same test also misses its 0.25 s lag bar while the box is loaded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DECOMP: org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md:287 @8768f46770 -- OG-a-1's acceptance closes on 'the whole GW/tests/ suite passes, count printed'.",
        "RUN base 3f94e0a024: 'timeout 300 pytest infra/aws/ec2/opal-gateway/tests -m not live -k not test_scoped_deny_by_default' printed the OG-a-1 lines and 14 more dots, then rc=124.",
        "RUN at the build: test_ratelimit.py plus test_schwab_engine.py::test_ogq1_ac02 in one process, -v, timeout 60 -> rc=124, last line 'test_schwab_engine.py::test_ogq1_ac02' with no verdict; each of the 12 modules alone passes at base (121 passed).",
        "RUN: test_ogq1_ac02 measured 'assert 0.26149860000645275 < 0.25' and 'assert 1.3060927999997511 < 0.25' in two runs while the box was loaded, then passed 2 of 2 at base (an archive of 3f94e0a024) and 2 of 2 at the build, alternating; the test imports only app.integrations.schwab.engine."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OG-a-1's acceptance, and the practice of each Gateway cell, runs the whole Gateway suite in one process as the regression census; this worker needed that census to measure what OG-a-2 changes.",
    "world_is": "The one-process suite hangs at base, so the worker took the census one process per module. Row W3-S6 predicted that a timer-dependent test could fail or pass without waiting; here one waits forever. The same test's lag bar is also sensitive to load on the shared box, independent of this cell's change.",
    "notes": "INERT: test-only. Any cell told to run the whole suite in one process will hit the bound until test_ratelimit.py scopes its clock (the disarm row W3-S6 names) or the suite is run per module."
  },
  {
    "id": "NFRA_OPLGTW-W3-S13",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T15:22:26Z",
    "one_line": "Under the amended order's fixture-only grant OGA2-AC12 cannot pass as written: with every fixture now signing in through a tid/oid principal and minting from a refresh family, 3 of 31 tests in the three granted modules still fail, each on an untouched assertion that compares the validated token's sub to an email, while OGA2-AC1 requires sub = <tid>/<oid> with no '@' and the bound forbids re-targeting an assertion.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-a-2.principal-cutover.md @adc6874dea -- the grant is FIXTURE-ONLY: 'edit only how each test obtains a principal or token' and 'no assertion is removed, weakened or re-targeted'; OGA2-AC12 expects '(?m)^[1-9][0-9]* passed' with no 'failed' on that line.",
        "CRITERION: infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py:410 @d02e73c272 (OGA2-AC1) -- assert claims[\"sub\"] == \"%s/%s\" % (TENANT, oid) and \"@\" not in claims[\"sub\"]. infra/aws/ec2/opal-gateway/app/oauth_as.py:264 and :321 @d02e73c272 -- the token's sub is principal.key, and validate_access_token refuses a token whose sub is not its tid/oid principal.",
        "ASSERTIONS, unchanged since the cut base: infra/aws/ec2/opal-gateway/tests/test_oauth_durable.py:710 @318e119c4f (:700 @3f94e0a024) validate_access_token(...)[\"sub\"] == email; tests/test_jwt_cve_lock.py:117 @318e119c4f (:66 @3f94e0a024) validate_access_token(tok)[\"sub\"] == \"attacker@opalinvest.com\"; tests/test_schwab_audit.py:342 @318e119c4f (:305 @3f94e0a024) claims[\"sub\"] == \"colleague@opalinvest.com\".",
        "RUN OGA2-AC12 verbatim at 318e119c4f: '3 failed, 28 passed in 17.08s', rc=1 (at adc6874dea: '16 failed, 15 passed'). Each of the 3 reaches its sub assertion holding a token validate_access_token accepted, e.g. \"assert '7f3a9c1e-2b4d-4e6f-8a0b-1c2d3e4f5a6b/77a75443-83c9-58c3-a508-5eb28fbcefa6' == 'attacker@opalinvest.com'\".",
        "DIFF: git diff -U0 over the three files before 318e119c4f -- 107 changed lines, 0 of them naming assert, self.assert* or pytest.raises. Probe og_a2.py AC13 at 318e119c4f -- assert counts HEAD == base 123/123, 6/6, 63/63, 'VERDICT: PASS-OGA2-AC13'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGA2-AC12: the three granted modules pass, count printed -- reached by fixture-only edits (how each test obtains a principal or token), with no assertion removed, weakened or re-targeted. OGA2-AC1: the token's sub is <tid>/<oid>, and email is display metadata only.",
    "world_is": "The ruling's disarm for row W3-S7 changed how each test obtains its principal and token, and 13 of the 16 failures are gone. It did not reach three assertions that name the email as the token's subject. Each states the pre-cutover identity model rather than a fixture: no fixture makes a validated token's sub an email without the email authorization C1 removes and OGA2-AC1 forbids. Passing them means re-targeting each to the principal key or to the email claim, which the bound forbids. In test_ogo1_ac06 the structural assertions after the sub assertion do not run while it fails. The worker left all three as written and refuses OGA2-AC12.",
    "notes": "ARMED: left alone, the drain carries 3 red existing tests into CLOUD. Disarm is the issuer's call: an amendment that lets these three assertions compare sub to the principal key (test_oauth_durable.py:710, test_jwt_cve_lock.py:117, test_schwab_audit.py:342 @318e119c4f). The change is one expression per assertion, and the per-module counts OGA2-AC13 grades would not move, so AC13 cannot distinguish that re-target from none."
  },
  {
    "id": "NFRA_OPLGTW-W3-S14",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T15:22:26Z",
    "one_line": "test_jwt_cve_lock.py's standalone smoke (its __main__ block) calls test_control_valid_token_accepted() with no arguments, and that test now takes the family_store pytest fixture, so running the file directly stops at a TypeError; pytest runs are unaffected.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "SOURCE: infra/aws/ec2/opal-gateway/tests/test_jwt_cve_lock.py @318e119c4f -- the module docstring offers 'python tests/test_jwt_cve_lock.py for a standalone smoke'; the if __name__ == \"__main__\" block calls every listed test as t(); test_control_valid_token_accepted(family_store) now requires the fixture.",
        "SOURCE: the same block @d02e73c272 -- the control test called issue_access_token(email, scope, client) without the family id that signature then required, so the smoke already stopped at a TypeError before this commit; @3f94e0a024 it ran.",
        "NOT RUN: the direct invocation was not executed; the verdict is read from the source."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The fixture-only grant: the control test mints its token from a refresh family, and edits are limited to how each test obtains a principal or token.",
    "world_is": "A refresh family needs a durable store, which the control test now receives from a pytest fixture (moto DynamoDB). The __main__ runner supplies no fixtures. The worker did not edit the __main__ block: it is not how a test obtains a token, and no criterion names it.",
    "notes": "INERT: every criterion and the commit gate run the file through pytest, which supplies the fixture."
  },
  {
    "id": "NFRA_OPLGTW-W3-S15",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T16:27:44Z",
    "one_line": "Re-targeting tests/test_schwab_audit.py:342 to the test's own '<tid>/<oid>' principal needs the uuid module at module scope, because that test's oid is uuid5-derived inside a helper that imports uuid locally. So the re-target commit adds one non-assertion line, 'import uuid' (line 15), beside the three ruled assertion lines, and the order names no line but those three.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-a-2.principal-cutover.md @1efed70736 -- exactly three assertions, one expression each, re-targeted to sub == \"<tid>/<oid>\" of that test's principal AND email == the same email; 'No other assertion changes'; otherwise the grant is fixture-only ('edit only how each test obtains a principal or token').",
        "SOURCE: infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py @f8feaf081e -- _family_access_token imports uuid locally and mints make_principal(_TENANT, str(uuid.uuid5(uuid.NAMESPACE_URL, \"ogo1-ac06/\" + email)), email); the module-level imports are asyncio, fnmatch, json, sys and pathlib, with no uuid.",
        "DIFF: infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py @7183f7a3d3 -- line 15 'import uuid' and line 343 the re-targeted assertion; probe og_a2.py AC14 at 7183f7a3d3: 'since f8feaf081e: 2 HEAD-side line(s) changed, 1 inside an assertion; other: ['15 import uuid']'. test_oauth_durable.py and test_jwt_cve_lock.py: 1 HEAD-side line changed each, 'other: none' (LocalIssuer.oid_for; uuid already imported at module scope @318e119c4f).",
        "RUN: OGA2-AC12 verbatim at 7183f7a3d3 -- '31 passed in 18.37s', rc=0; OGA2-AC13 -- 63 = 63 for test_schwab_audit.py, 'VERDICT: PASS-OGA2-AC13'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Ruling 97141 as carried by the order @1efed70736: exactly three assertion lines change, each to sub == \"<tid>/<oid>\" of that test's principal AND email == the same email; no other assertion changes; every other edit is fixture-only.",
    "world_is": "The ruled expression for test_ogo1_ac06 names that test's oid, which only uuid.uuid5 can reproduce, and uuid was not in scope at the assertion. One module-level import line was added. It is neither an assertion nor a change to how the test obtains its token. The alternatives were worse by the worker's reading: reaching uuid through sys.modules, or changing the helper to hand back its principal, which edits a fixture line to serve an assertion.",
    "notes": "INERT: an import changes no assertion and no behaviour. The AC14 probe counts it as a non-assertion line and prints it as a disclosure; OGA2-AC13 reads 63/63 for the module."
  },
  {
    "id": "NFRA_OPLGTW-S12",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T17:10Z",
    "one_line": "Disarm of W3-S7 and W3-S13 (and the holds of S7 and S10) on OG-a-2's green re-run, which is now merged to CLOUD; and a measured flake: test_schwab_engine.py::test_ogq1_ac02 failed 2 of 3 isolated runs on this box, which will read as a FAILED-MODULE in any per-module suite criterion.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "GREEN RE-RUN: wk-nfra_oplgtw-1-3c @aef164f8e2. proof-of-spec-check --governing-order VALID (rc=0), 14/14. OGA2-AC12 '31 passed'; AC13 assert counts 123/123, 6/6, 63/63; AC14: exactly the 3 named assertion lines changed, each keeping its original email. That meets every arm of 1.0.0_SA_CTO rulings 97114 (1) and 97141.",
        "COO RE-RUN (a different instrument from the worker's criteria): on the same branch, every module of the glob infra/aws/ec2/opal-gateway/tests/test_*.py in its own process, -m 'not live', -k 'not test_scoped_deny_by_default'. 13 modules; 12 green, including test_oauth_durable 18 passed, test_jwt_cve_lock 6, test_schwab_audit 7 and test_principal_cutover 11; test_schwab_engine '1 failed, 12 passed'.",
        "FLAKE, NOT REGRESSION: test_schwab_engine re-run '13 passed'; test_ogq1_ac02 alone x3 read failed, passed, failed. OG-a-2 changed app/context.py, oauth_as.py, revocation.py, server.py and token_broker.py (git diff 3f94e0a024..aef164f8e2); app/integrations/schwab/ is untouched, and the engine test imports only app.integrations.schwab.engine (test_schwab_engine.py:22)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "W3-S7 and W3-S13 were ARMED: OG-a-2's drain would carry red existing tests into CLOUD. OG-q-1's AC2 treats test_ogq1_ac02 as deterministic, and TO-OG-v-2 AC4 requires every module green.",
    "world_is": "OG-a-2 reached CLOUD with its granted modules green, so the red-test hazard is gone. Separately, test_ogq1_ac02's 0.25 s event-loop lag bar is load-sensitive on this shared box, as W3-S12 first reported. Any per-module suite run here, including OGV2-AC4, can read FAILED-MODULES 1 on that test alone.",
    "notes": "The disarm is by the named owner at the named moment: the drain of OG-a-2 with its green re-run. The flake is OG-q-1's test; whether its bar is re-stated or run under a quiet box is for L9/L10. For OG-v-2 it is known in advance, so a FAILED-MODULE on test_schwab_engine alone is re-run before it is read as a regression."
  },
  {
    "id": "NFRA_OPLGTW-S13",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T18:50Z",
    "one_line": "Disarm of W3-S16 and W3-S17 by their owner: OG-a-3's branch wk-nfra_oplgtw-1-3d is held UNMERGED, because merging it turns OG-a-2's route census test_oga2_ac04 red on CLOUD and its own AC7 pins an exact route table the next route-adding cell will break; the grant and the criterion restatement are asked of 1.0.0_SA_CTO.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RE-RUN BY THIS SEAT at wk-nfra_oplgtw-1-3d @06a9aec60d: proof-of-spec-check --governing-order VALID (rc=0) 7/7; test_browser_oidc.py '7 passed'; test_principal_cutover.py 'FAILED ...::test_oga2_ac04, 1 failed, 10 passed'.",
        "W3-S16: test_principal_cutover.py:540 asserts set(ROUTE_CLASS) == set(routes) over every route of app.server. OG-a-3 serves two new paths, /schwab/download/login and /schwab/download/callback (BROWSER_PATHS.json), that the hand-written ROUTE_CLASS does not list, and the file is outside TO-OG-a-3's <paths>.",
        "W3-S17: test_browser_oidc.py:620 asserts tuple(rest) == BASE_ROUTES and :625 asserts that the head-minus-base declared routes equal exactly the two new ones. Both hold only until another cell adds a route; TO-OG-x-1 adds download routes."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-a-3's <paths> grants no other cell's test, and OGA3-AC7 reads 'the route table differs from the one at your base only by the new paths'.",
    "world_is": "Two tests pin the whole route table: OG-a-2's classification guard and OG-a-3's exact-diff check. The first needs each route-adding cell to classify its own paths, a file no such cell is granted. The second fails as soon as any later cell adds a route. Until ruled, OG-a-3 stays unmerged. Slot ~3's next cell, OG-z-1, writes the same app/server.py and so waits for this merge.",
    "notes": "INERT: nothing merged or deployed; CLOUD's suite is unchanged. Asked of 1.0.0_SA_CTO: A, an entries-only grant of ROUTE_CLASS to OG-a-3 for its two public paths; B, AC7 restated as a superset of the base, with the exact diff kept as a one-time proof record; C, a standing entries-only grant for later route-adding cells. W3-S19 (the Entra redirect URI registration) was proposed to ride gate G-C."
  },
  {
    "id": "NFRA_OPLGTW-S14",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T19:05Z",
    "one_line": "Record of 1.0.0_SA_CTO's ruling msg 97203 on W3-S16/W3-S17: (A) OG-a-3 gets an entries-only ROUTE_CLASS grant for its two public paths; (B) OGA3-AC7 is restated as a superset of the base with the exact diff kept as a one-time probe; (C) a standing entries-only grant for OG-x-1 and OG-z-1, each entry carrying the route's real guard class; W3-S19 rides gate G-C; W3-S20 becomes a fixed input in OG-x-1's worker face.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULING 97203 A: tests/test_principal_cutover.py is granted to OG-a-3 for ENTRIES ONLY. /schwab/download/login and /schwab/download/callback go into ROUTE_CLASS as 'public', their true class, because a login and its OIDC callback are reachable without a session; the public-route arm at :549-554 grades them. Discriminator: the file's diff against the base is exactly those 2 lines, and the module passes 11 of 11.",
        "RULING 97203 B: OGA3-AC7 becomes a superset. Every base route is served unchanged and in order, the two browser routes are served, the middleware is unchanged, and /login, /sprint and /sprint/archive stay guarded. The 'exactly 2 added at this cell's HEAD' fact is a one-time proof record, because an exact-equality test that later route cells must keep green goes red by design.",
        "RULING 97203 C, with a condition: any later round-1 cell that adds a route gets the same entries-only grant for its own paths, with the same discriminator, and each entry carries the route's REAL guard class as the code enforces it, never a default 'public'. A genuinely unclear class is a row, not an entry. Census of unhanded orders granting app/server.py: TO-OG-x-1 and TO-OG-z-1, 2 of 2 carried. W3-S19 (the Entra redirect URI for /schwab/download/callback) rides gate G-C before any live download. W3-S20 (download path /schwab/download, cookies Path=/schwab/download) is written into TO-OG-x-1's worker face."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Each Gateway cell's order grants only its own surface, and OGA3-AC7 pins the route table exactly.",
    "world_is": "Two tests pin the whole route table, so every route-adding cell has to touch another cell's test. The ruling converts that into an entries-only grant with a diff discriminator and a real-class condition, carried as criteria in TO-OG-a-3 (on its held branch), TO-OG-x-1 and TO-OG-z-1. No FWD changes.",
    "notes": "Recorded beside S9 (97114) and S11 (97141). W3-S16 and W3-S17 (and S13's hold) are disarmed at OG-a-3's drain once its re-run is green; the adjudication is 3.0.0_SA_CVO's at L9."
  },
  {
    "id": "NFRA_OPLGTW-W3-S16",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T18:08:00Z",
    "one_line": "Adding OG-a-3's two routes turns tests/test_principal_cutover.py::test_oga2_ac04 red: its route census requires every served path to appear in its hand-written ROUTE_CLASS table, which lacks /schwab/download/login and /schwab/download/callback, and that file is outside this order's grant.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: cd /c/tmp/wk-oplgtw-1-3d && timeout 600 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py -q -p no:cacheprovider --color=no -m \"not live\", on the worktree committed as 6a4e94d734 -- '1 failed, 10 passed in 6.40s'; FAILED test_oga2_ac04 at test_principal_cutover.py:540 (assert set(ROUTE_CLASS) == set(routes)): 'AssertionError: ['/schwab/download/callback', '/schwab/download/login']'.",
        "SOURCE: infra/aws/ec2/opal-gateway/app/server.py @6a4e94d734 -- two Route declarations added (browser_oidc.LOGIN_PATH, browser_oidc.CALLBACK_PATH); OGA3-AC7 prints 'added 2 ... removed 0; changed 0'.",
        "BASE: the drain commit 7459929520 records the COO re-run at the cut base green on 12 of 13 modules, the 13th being test_schwab_engine's known load flake, so test_principal_cutover passed there.",
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-a-3.browser-oidc.md @6a4e94d734 -- <paths> names app/browser_oidc.py, app/server.py, tests/test_browser_oidc.py and this channel; tests/test_principal_cutover.py is not named."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order grants exactly app/browser_oidc.py, app/server.py, tests/test_browser_oidc.py and the channel. Its criteria are the seven tests of tests/test_browser_oidc.py, and OGA3-AC7 requires the route table to differ from the base only by the new paths.",
    "world_is": "OG-a-2's test_oga2_ac04 fixes the set of served routes through a classification table and fails on any unclassified path, so any cell that adds a route fails it. The worker did not edit that file. The seven OGA3 criteria pass, and the other 12 Gateway modules pass, one process each.",
    "notes": "ARMED: after this branch drains, the COO's per-module re-run reads test_principal_cutover 1 failed. Disarm: a grant adding the two paths to ROUTE_CLASS (as public routes, each gated by its own state cookie, nonce and ID-token validation), or a ruling that the census reads BROWSER_PATHS.json."
  },
  {
    "id": "NFRA_OPLGTW-W3-S17",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T18:08:00Z",
    "one_line": "OGA3-AC7 as written pins the route table recorded at the cut base 7459929520, so test_oga3_ac07 turns red as soon as any later cell adds or changes a route. OG-x-1 and OG-z-1 both write app/server.py, per the decomposition.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: NFRA_OPLGTW.TO-OG-a-3 @6a4e94d734 -- OGA3-AC7: 'the route table differs from the one at your base only by the new paths.'",
        "SOURCE: infra/aws/ec2/opal-gateway/tests/test_browser_oidc.py @6a4e94d734 -- BASE_ROUTES (27 rows read from the running app at 7459929520) and test_oga3_ac07, which asserts the live table minus the two browser routes equals BASE_ROUTES and re-derives it from the git object of server.py at 7459929520.",
        "DECOMP: org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md @8768f46770 -- :507 OG-x-1 writes GW/app/download_routes.py (new) and GW/app/server.py; :315 OG-z-1 writes GW/app/server.py."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGA3-AC7 compares the route table with the one at this order's base.",
    "world_is": "Written as ruled, the test holds only until the next cell changes the route table. The first route-adding cell turns OGA3-AC7 red with no defect in OG-a-3. test_oga2_ac04 has the same property (row W3-S16).",
    "notes": "ARMED for later drains. Disarm: the route-adding cell's order grants amending BASE_ROUTES (or the test's reference commit), or a ruling retires AC7 from the regression set after this round."
  },
  {
    "id": "NFRA_OPLGTW-W3-S18",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T18:08:00Z",
    "one_line": "The two browser OIDC endpoints fall into the rate limiter's coarse FAIL-OPEN global per-IP bucket, not the tight FAIL-CLOSED auth bucket, because app/ratelimit.py's AUTH_PATHS lists only /authorize, /token, /register and /callback, and that file is outside the grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SOURCE: infra/aws/ec2/opal-gateway/app/ratelimit.py @6a4e94d734 -- :42 AUTH_PATHS = frozenset({\"/authorize\", \"/token\", \"/register\", \"/callback\"}); :117-120 enforce_ip: AUTH endpoints get the tight bucket, FAIL-CLOSED, everything else the coarse global bucket, FAIL-OPEN.",
        "SOURCE: infra/aws/ec2/opal-gateway/app/server.py @6a4e94d734 -- RateLimitMiddleware: is_auth = path in ratelimit.AUTH_PATHS.",
        "SOURCE: infra/aws/ec2/opal-gateway/app/browser_oidc.py @6a4e94d734 -- the callback redeems an upstream code and validates an ID token (a key lookup) per request, as the /callback bridge leg does."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order asks for the login and callback in browser_oidc.py and server.py and says nothing of rate limiting. The existing auth endpoints sit in the tight FAIL-CLOSED per-IP bucket.",
    "world_is": "/schwab/download/login and /schwab/download/callback are rate-limited as ordinary traffic, although each callback costs an upstream code redemption.",
    "notes": "INERT: nothing deploys in this order. The one-line act, adding the two paths to AUTH_PATHS, belongs to the owner of app/ratelimit.py, before OG-r-1's release."
  },
  {
    "id": "NFRA_OPLGTW-W3-S19",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T18:08:00Z",
    "one_line": "The separate callback is a new redirect URI at the upstream: the upstream app registration must list <PUBLIC_BASE_URL>/schwab/download/callback beside /callback, and no cell of the decomposition names that act (OG-i-3 is the ALB only).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "SOURCE: infra/aws/ec2/opal-gateway/app/browser_oidc.py @6a4e94d734 -- callback_url() = PUBLIC_BASE_URL + '/schwab/download/callback', passed as redirect_uri both to get_authorization_request_url and to acquire_token_by_authorization_code.",
        "SOURCE: infra/aws/ec2/opal-gateway/app/config.py @6a4e94d734 -- redirect_uri = PUBLIC_BASE_URL + '/callback', the code's only redirect URI before this cell.",
        "DECOMP/PRD: a case-insensitive search of decompositions/*.md and prd/*.md under org/missions/D9/NFRA/NFRA_OPLGTW for 'redirect[ _-]?ur[il]|app registration|reply url' returns 2 lines (PRD C5 :179 and DECOMP :514), both about the ticket never appearing in a redirect URL; none about registering one. OG-i-3 (DECOMP :157) writes TFGW/alb.tf only.",
        "INFERRED: that the upstream refuses a sign-in whose redirect URI is not registered is standard OpenID Connect behaviour; it was not exercised (the tests use a local issuer)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C1: 'The download browser uses a separate Gateway-owned OIDC callback'. The order's only downstream hand-off is BROWSER_PATHS.json, for OG-i-3's ALB rules.",
    "world_is": "Until the app registration lists the new URI, the live sign-in stops at the upstream before the Gateway sees a code. BROWSER_PATHS.json records the URI under upstream_redirect_uri, marked as not an ALB rule.",
    "notes": "INERT now: nothing deploys. It becomes a hard stop of the download journey at OG-r-1 or OG-v-4 unless the holder of the Entra app registration adds the URI."
  },
  {
    "id": "NFRA_OPLGTW-W3-S20",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T18:08:00Z",
    "one_line": "Neither the contract nor the PRD names a URL path for the download page or its login. The worker chose /schwab/download as the cookie scope, from the one existing hint (the audit test's sentinel URL https://gateway.opalinvest.com/schwab/download#...). That choice binds OG-x-1 to put its download page and routes at or under /schwab/download, or the session cookie never reaches them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CONTRACT: org/standards/NFRA_OPLGTW_CONTRACT.json @6a4e94d734 -- a case-insensitive search for '\"/[a-z]|path|url' returns 1 line (:278 download_ticket_transport), which names no path.",
        "SOURCE: infra/aws/ec2/opal-gateway/tests/test_schwab_audit.py @6a4e94d734 :263 -- the sentinel \"complete URL\": \"https://gateway.opalinvest.com/schwab/download#tkt_s3cr3tQ9xLmN0pR\".",
        "SOURCE: infra/aws/ec2/opal-gateway/app/browser_oidc.py @6a4e94d734 -- COOKIE_PATH = '/schwab/download'; org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~3/BROWSER_PATHS.json @6a4e94d734 -- cookie_path and cookie_path_note."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order: write BROWSER_PATHS.json with 'the exact login and callback paths this cell serves'; OGA3-AC4: the session cookie is 'scoped to the download paths'. Neither names the download paths.",
    "world_is": "The download paths belong to OG-x-1 and are not yet written. Scoping the cookie needs a prefix now, so that prefix fixes where OG-x-1's page can live.",
    "notes": "INERT: a naming decision, recorded in BROWSER_PATHS.json, which OG-i-3 reads. OG-x-1's order should name /schwab/download as its page path, or re-cut COOKIE_PATH."
  },
  {
    "id": "NFRA_OPLGTW-W3-S21",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T18:08:00Z",
    "one_line": "The order says tests/test_identity_scope.py::test_scoped_deny_by_default fails at the cut base (row NFRA_OPLGTW-S1). In this worktree the premise does not hold: the module ran 6 passed, 0 failed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: cd /c/tmp/wk-oplgtw-1-3d && AUDIT_PATH=<.scratch> timeout 600 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_identity_scope.py -q -p no:cacheprovider --color=no -m \"not live\", on the worktree committed as 6a4e94d734 -- '6 passed in 0.07s', rc=0.",
        "DIFF: 6a4e94d734 against 7459929520 changes 4 files (app/browser_oidc.py, app/server.py, tests/test_browser_oidc.py, BROWSER_PATHS.json); neither identity_scope.py, its test nor identity_tool_allowlist.txt.",
        "ORDER: NFRA_OPLGTW.TO-OG-a-3 @6a4e94d734 BOUNDS -- 'tests/test_identity_scope.py::test_scoped_deny_by_default fails at the cut base (row NFRA_OPLGTW-S1).'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's BOUNDS: the named test fails at the cut base.",
    "world_is": "It passed here. The worker did not investigate why (environment, data files or a later fix), because it is not this cell's.",
    "notes": "INERT: no criterion of this order reads it. Recorded so the premise is re-grounded before the next order repeats it."
  },
  {
    "id": "NFRA_OPLGTW-S15",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T20:25Z",
    "one_line": "Disarm of W3-S16 and W3-S17 (and S13's hold) by their owner: OG-a-3's amended re-run is green and merged, with every Gateway module passing in its own process, so neither route-table coupling reaches CLOUD red.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RE-RUN: wk-nfra_oplgtw-1-3d @4870b953d9, proof-of-spec-check --governing-order VALID (rc=0) 10/10 under ruling 97203. OGA3-AC9 '11 passed' (test_oga2_ac04 reads 29 declarations == 29 app routes). OGA3-AC10: exactly 2 added ROUTE_CLASS lines, both 'public'. OGA3-AC7 is now a superset (27 of 27 base routes unchanged and in order). OGA3-AC8 records base 27 -> HEAD 29, exactly BROWSER_PATHS.json.",
        "COO RE-RUN (a different instrument): the same branch, every module of the glob infra/aws/ec2/opal-gateway/tests/test_*.py in its own process, -m 'not live', -k 'not test_scoped_deny_by_default': 'MODULES: 14 FAILED-MODULES: 0', including test_principal_cutover 11 passed, test_browser_oidc 7 and test_schwab_engine 13.",
        "FUTURE-PROOF: TO-OG-x-1 and TO-OG-z-1 carry standing rule C (@a8a250297c), so the next route-adding cell classifies its own paths with their real guard class instead of breaking test_oga2_ac04."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "W3-S16 and W3-S17 were ARMED: merging OG-a-3 would turn test_oga2_ac04 red on CLOUD, and its exact route-table AC7 would break at the next route-adding cell.",
    "world_is": "Both tests are green at the merge, and the second no longer pins later cells. The hazard is gone at the named moment: OG-a-3's drain with its green re-run.",
    "notes": "W3-S19 (the Entra redirect URI for /schwab/download/callback) rides gate G-C per ruling 97203. W3-S18, W3-S20 and W3-S21 stay INERT observations for L9. The adjudication is 3.0.0_SA_CVO's."
  },
  {
    "id": "NFRA_OPLGTW-S16",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T21:05Z",
    "one_line": "Record of 1.0.0_SA_CTO's /self-drive ruling msg 97237, the disposition path of W1-S1 and the lift of S3's block: the two WAF description backfills are admitted by name into the opal-gateway root's first apply (OG-i-1's) under four conditions, now TO-OG-i-1's AC10-AC12 and its bounds; OG-i-1 is re-handed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULING 97237 (1.0.0_SA_CTO, under Andrew-direct ~19:3xZ 'YOU ADJUDICATE THEM'). The owner NFRA_OPSEC202609 is CLOSED with no COO lane. Both descriptions are the owner's own declared text (waf.tf:261, :302), so live comes to match declared, with DELTA=0 on behaviour. addresses is under lifecycle ignore_changes (waf.tf:294-296, :335-337) and is not in the diff.",
        "CONDITIONS, carried in TO-OG-i-1 by this seat's amendment: (1) the out-of-cell changes are exactly those two ~ description updates, addresses absent (OGI1-AC10); (2) aws wafv2 get-ip-set before and after the apply reads identical address lists with counts (OGI1-AC11); (3) plan and apply run in one safe-apply run, and a WAFOptimisticLockException is a clean abort and re-run (bound); (4) a post-apply plan reads 0 changes on both sets (OGI1-AC12).",
        "SHARED ROOT: 1.0.0_SA_CTO states that G-S half (b) for MDPF_TAXSMA's TX-i-3 is satisfied by this ruling plus condition 4, and that TX-i-3 applies after OG-i-1's apply and after this seat's G-S half (a)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-i-1's blast-radius bound refused any change to an existing resource, and row S3 held OG-i-1..OG-i-4 for the round.",
    "world_is": "The adjudicator admits exactly the two named description backfills into one apply, under criteria that prove the reconciler's address lists survive. The block of S3 lifts: OG-i-1 is re-handed on the amended order, and OG-i-2..OG-i-4 follow on a root that plans clean. Row S2's check still binds OG-i-1's drain: the applied key schema must read pk/sk with TTL on expires_at.",
    "notes": "W1-S1's adjudication cites 97237; it is 3.0.0_SA_CVO's at L9. The same amendment corrects the AC8 harness sentence to the operator role, per W1-S2. W1-S3 needs no act (97237)."
  },
  {
    "id": "NFRA_OPLGTW-W3-S22",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T20:10:00Z",
    "one_line": "The restricted profile is keyed by tid/oid, but 5 access-layer routes (/login, /sprint, /sprint/, /sprint/archive, /sprint/{day}) and the /callback legacy-consent branch identify a caller only by the ALB OIDC email. So the same person, signed in to the ALB with their work account, can read Daily Sprint pages and complete the legacy Graph consent. The guard cannot see them before that read or credential exchange.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SOURCE: infra/aws/ec2/opal-gateway/app/server.py @7f1ab996a0 :185-198 -- GuardMiddleware resolves /login and /sprint* by get_user_email() (the ALB x-amzn-oidc-data email) and set_current_email(), which clears any principal (app/context.py :93-96).",
        "SOURCE: infra/aws/ec2/opal-gateway/app/identity.py @7f1ab996a0 :50-69 -- the ALB claims yield an email; no tid or oid is read. app/sprint_view.py @7f1ab996a0 :173-175 -- with SPRINT_VIEW_ALLOWED_EMAILS empty, every tenant email is served.",
        "SOURCE: infra/aws/ec2/opal-gateway/app/token_broker.py @7f1ab996a0 :330-341 -- redeem_consent exchanges the code for the Graph envelope and writes the cache; its principal is known only after that exchange. The /callback state carries only an email (:358-366).",
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md @f0aa50dbc0 :145 'Key grants by tid/oid, not email'; :141 'Do not infer that match from the existing ALB email-only helper'. access_state.py @7f1ab996a0 :117-123 keys POLICY records by tid/oid only; there is no email index.",
        "RUN: test_data_entitlement_guard.py::test_ogz1_ac08 -- the restricted profile's own gateway token is refused 401 on all 5 access-layer routes, with 0 reads. The row is about the ALB session, a different credential that the same person holds."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGZ1-AC8 / PRD C2: '/teams/poll, /query/v0 and every other non-MCP route are denied to the restricted profile before any credential or data read'; 'Existing admin/Graph/portal routes retain their existing policy for other users'.",
    "world_is": "What is built: the restricted profile's tid/oid principal and its gateway token are denied on every non-MCP route before any read (AC8, 28 of 28). The ALB-email routes never carry that principal. A person holding a restricted profile can still reach them through the ALB with an email identity. Closing that needs one of: a SPRINT_VIEW_ALLOWED_EMAILS roster (config), an ALB rule, or an email-keyed deny index in the access-state table. access_state.py, config.py, sprint_view.py and token_broker.py are all outside this order's grant.",
    "notes": "ARMED: harmless while no restricted profile exists (OG-z-2 creates the first one) and nothing is deployed. Once a restricted profile is live, the Daily Sprint pages are readable by its holder unless a roster is configured. The worker did not add a post-exchange refusal on /callback, because the credential would already have been fetched and cached."
  },
  {
    "id": "NFRA_OPLGTW-W3-S23",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T20:10:00Z",
    "one_line": "At the cut no Schwab tool is registered anywhere in the Gateway (OG-q-2 builds them). OGZ1-AC4, AC6, AC7 and AC12 are therefore exercised against a test-only stand-in integration that registers the contract's five names through the real run_integration_tool. data_entitlement.py pre-classifies those five names and maps each to an operation.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: at 7f1ab996a0 the served MCP surface registers 35 native tools, and the 3 buildable integrations register 9 (ycharts 6, opal_portal 1, globgrph 2). None is named schwab_*.",
        "CONTRACT: org/standards/NFRA_OPLGTW_CONTRACT.json v1.0 :25-31 -- tools schwab_get_access, schwab_list_files, schwab_describe_dataset, schwab_query, schwab_prepare_download.",
        "SOURCE: infra/aws/ec2/opal-gateway/app/data_entitlement.py (this cell) SCHWAB_TOOLS -- get_access: any active grant; list_files: list; describe_dataset: describe; query: query; prepare_download: download_filtered."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGZ1-AC4: 'an unknown user sees no Schwab tool in discovery and a direct Schwab call fails'.",
    "world_is": "With zero Schwab tools registered, that criterion would pass vacuously. The tests register stand-ins carrying the contract's names so that the discovery filter and the dispatch denial are actually exercised.",
    "notes": "INERT. OG-q-2 must register exactly these five names; a renamed tool would be unclassified and so denied to everyone (row W3-S24). The operation map above is this cell's choice; PRD C4 (:167) describes what the tools do, not which operation gates each."
  },
  {
    "id": "NFRA_OPLGTW-W3-S24",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T20:10:00Z",
    "one_line": "'A newly added tool is denied until classified' is enforced for EVERY principal, as PRD C2 states it, not only for the restricted profile that OGZ1-AC5 names. From now on, any cell that adds a tool to tools.py or an integration must also add it to app/data_entitlement.py TOOL_CLASSES; otherwise the tool is hidden and denied Gateway-wide.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md @f0aa50dbc0 :145 -- 'A newly added tool is denied until classified. Preserve existing users' current tool access ... without granting new data tools by default.'",
        "RUN: test_data_entitlement_guard.py::test_ogz1_ac05 -- an unclassified tool registered outside both chokepoints: tool_unclassified for the restricted profile and for a no-profile principal, with 0 body runs; once classified legacy, the no-profile principal is served.",
        "SOURCE: app/integrations/registry.py (this cell) -- register_enabled reports any unclassified tool under 'unclassified' rather than registering it silently."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGZ1-AC5: 'a newly registered, unclassified tool is denied to the restricted profile'.",
    "world_is": "The criterion holds, and so does the wider PRD sentence: the unclassified tool is denied to everyone. All 44 tools registered at the cut are classified 'legacy', so OGZ1-AC11 holds: existing users keep the same tool set before and after.",
    "notes": "INERT for this round. A later order that adds a tool needs app/data_entitlement.py in its <paths>, or the new tool is dead on arrival."
  },
  {
    "id": "NFRA_OPLGTW-S17",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T22:12Z",
    "one_line": "Record of 1.0.0_SA_CTO's ruling msg 97251: W3-S22 rides round 2 inside the email-keyed authorization cell (an email-keyed deny record in the access-state table) and is disarmed for round 1 by TO-OG-r-1's new AC12 withholding line; OG-q-2 gets an entries-only grant on app/data_entitlement.py for its five tools (AC25, AC26), standing for any later tool-adding cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULING 97251 (1), on W3-S22 (disarm owner 1.0.0_SA_CTO): round 2, widening the email-keyed cell of ruling 97114 to /login, the four /sprint paths and /callback's legacy-consent branch. Mechanism: an email-keyed deny record in the access-state table, so there is ONE carrier, not an ALB rule or a roster. Round 1 is disarmed because the restricted profile is new with this project, and TO-OG-r-1 AC12 prints the restricted-profile principals able to complete the ALB browser login, which must count 0.",
        "RULING 97251 (2), on W3-S24 and W3-S23: an entries-only grant on app/data_entitlement.py for OG-q-2's five tools, each with its real contract operation class, with no widening and no permissive default. An unclear class is a row. Discriminator: the diff is exactly five entries, and test_data_entitlement_guard.py stays green. It stands for any later NFRA_OPLGTW round-1 cell that adds a tool.",
        "CARRIED: TO-OG-r-1 (AC12) and TO-OG-q-2 (AC25, AC26, <paths> + app/data_entitlement.py), both amended before any worker was handed them, in this seat's commit beside this row."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "W3-S22 was ARMED: a restricted-profile holder could still reach the email-authorized browser routes. W3-S24: TO-OG-q-2 did not grant the file where its tools must be classified, so its tools would be denied to everyone.",
    "world_is": "W3-S22's gap is placed in round 2's email-keyed cell and cannot be exercised in round 1, because the release withholds any restricted profile from a principal who can complete the browser login, and the printed count is the discriminator. OG-q-2 can classify its own tools under a discriminated, entries-only grant.",
    "notes": "W3-S22's disposition cites 97251 as 1.0.0_SA_CTO instructed. The adjudication is 3.0.0_SA_CVO's at L9."
  },
  {
    "id": "NFRA_OPLGTW-S18",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T22:56Z",
    "one_line": "Disarm of NFRA_OPLGTW-W1-S6: the issuer provisioned the gitignored session serial file naming 0.9.0_WK_NFRA_OPLGTW~1 inside worker ~1's worktree. Run from that worktree, the halt gate moved from IDENTITY UNRESOLVED to resolving the worker and scanning its issuer's inbox. OG-i-1 is re-handed on the same branch with its OPEN ledger entry.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "GATE SOURCE: .tools/halt-gate-check.sh @923f7dcab8. :38 roots the gate at the checkout holding the script, which is the worktree. :56-64 resolve identity only from org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial (or an .orphan-cleaned marker). :118 prints this exact one-line remedy. :171-174 admit a 0.9.0_WK_* serial only when a non-terminal order at the checkout's HEAD is issued_to it; at a0bcaa6bae TO-OG-i-1 is issued_to 0.9.0_WK_NFRA_OPLGTW~1 with status pending.",
        "BEFORE/AFTER in /c/tmp/wk-oplgtw-1-1b @a0bcaa6bae, 2026-09-15T22:5xZ. Before the file: 'HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed)'. After writing org/mcp/sessions/e09b6e12-6f85-4732-b702-3307d4a68532.serial = 0.9.0_WK_NFRA_OPLGTW~1: 'worker 0.9.0_WK_NFRA_OPLGTW~1 has no inbox; scanning its issuer 2.0.0_SA_COO~O', then rc=1 on 14 routine pending messages with no STOP-class message.",
        "UNTRACKED: .gitignore:423 ignores org/mcp/sessions/. After the write, git status --porcelain in the worktree lists only .scratch/ and .venv-og/, so nothing tracked moved and the worker's <paths> grant is unchanged.",
        "WORLD: no AWS change had occurred (W1-S6 grounding). The ledger entry opened @4b9671ec09 (2026-09-15T21:54:38Z) stays OPEN on the unmerged branch wk-nfra_oplgtw-1-1b. The re-handed worker's apply closes it, so it is never drained to CLOUD OPEN."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A worker that exports OPAL_AGENT_SERIAL can run .tools/safe-apply.sh from its own worktree.",
    "world_is": "Exporting the variable satisfies only the identity gate that runs second (resolve_actor). The halt gate runs first and needs a session serial file inside the worktree, a path the worker's grant does not name. So the issuer provisions that file at spawn, as it does .tools/terraform.exe, for every NFRA_OPLGTW worker whose order applies Terraform.",
    "notes": "This seat is W1-S6's disarm owner; this act and row disarm it. Sibling finding: NFRA_OPLGTW-S19 (the same gate's inbox root in a worktree)."
  },
  {
    "id": "NFRA_OPLGTW-S19",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-15T22:58Z",
    "one_line": "In a linked worktree the halt gate scans an inbox root that does not exist. HALT_GATE_INBOX_ROOT defaults to <worktree>/org/mcp/inbox, which is gitignored and absent. So once a worker's serial resolves, the gate passes rc=0 with its issuer's real inbox unread, and a [STOP] to the issuer would not halt that worker's apply.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "GATE SOURCE: .tools/halt-gate-check.sh @923f7dcab8. :38-39 set HALT_GATE_INBOX_ROOT to ${HALT_GATE_REPO_ROOT}/org/mcp/inbox, where the repo root is the checkout holding the script. :247 reads 'Missing inbox dir = no messages (not an error)'. :11 reads 'Empty inbox -> PASS silently, exit 0'. :139-141 say a [STOP] to the issuer halts its workers' deploys.",
        "DISCRIMINATING PAIR in /c/tmp/wk-oplgtw-1-1b @a0bcaa6bae with the worker serial resolved, 2026-09-15T22:5xZ. Default root: 'ls org/mcp/inbox: No such file or directory', then 'scanning its issuer 2.0.0_SA_COO~O' and rc=0. With HALT_GATE_INBOX_ROOT exported to the shared tree's org/mcp/inbox, the same gate at the same HEAD listed 14 pending messages for the same issuer and returned rc=1."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Before a deploy, the halt gate scans the acting agent's inbox, or for a v3 worker its issuer's, and a [STOP] there blocks the deploy (halt-gate-check.sh:139-141).",
    "world_is": "From a linked worktree the gate scans an absent directory and passes silently. Every NFRA_OPLGTW worker whose order applies is spawned with HALT_GATE_INBOX_ROOT exported to the shared tree's inbox, beside the issuer-provisioned serial file (S18).",
    "notes": "INERT within NFRA_OPLGTW because of the spawn export. The exposure is estate-wide: any v3 worker that safe-applies from a linked worktree has it. The fix is a gate edit outside this project's write surface, so 1.0.0_SA_CTO is informed. Even with the right root, the gate reads only top-level unread files, which a live stream Monitor empties within seconds; that is Rule 18's standing concession, not a new finding."
  },
  {
    "id": "NFRA_OPLGTW-W3-S25",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T23:11:00Z",
    "one_line": "Neither end of the interface to OG-i-2's alias-key secret is stated by any carrier: nothing names the configuration setting that holds the secret's NAME, and nothing states the secret VALUE's shape. app/config.py carries no such setting and is outside this order's grant, and the ~1 deliverable SCHWAB_IDENTITIES.json does not exist at the cut. OG-z-3 therefore chose both: the environment variable SCHWAB_ACCOUNT_REF_SECRET_ID holds the name, and the SecretString is {\"current_version\": \"v<n>\", \"keys\": {\"v<n>\": \"<base64 of at least 32 bytes>\"}}.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SOURCE: infra/aws/ec2/opal-gateway/app/config.py @f4c7184f6d -- comp-read --enumerate '(?i)secret|schwab|account_ref|hmac' reads 11 hits across 341 lines (CLIENT_SECRET at :25 and :308, a Fernet comment at :174, YCHARTS_SECRET_ID at :231 with its comments, the integration-enablement comments). No setting names a Schwab alias-key secret, and config.py is not in TO-OG-z-3's <paths>.",
        "ABSENT: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/ @f4c7184f6d holds 4 entries (the OG-i-1 proof instance, access-state-table.result.md, og_i1.plan.json, probes/) and no SCHWAB_IDENTITIES.json. OG-i-2 has not run.",
        "DECOMP: org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md @8768f46770 :156 gives OG-i-2 'the alias-key secret' and :189 asks only for 'the alias-key secret with the Gateway's read grant on it'. PRD @f0aa50dbc0 :147 says only 'keep its key in the existing approved secret mechanism'. Neither states the value's shape or where its name is configured.",
        "SOURCE (this cell): infra/aws/ec2/opal-gateway/app/account_ref.py -- SECRET_ID_ENV = 'SCHWAB_ACCOUNT_REF_SECRET_ID', current_keyring() through app/integrations/base.py SecretsCredential, parse_keyring() for the value. RUN: OGZ3-AC1, 6 of 6 fail-closed arms (name unset, no such secret, not JSON, 16-byte key, no key for current_version, key not base64) raise KeyUnavailable on a mint and answer UNAVAILABLE on a resolution."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-z-3's cell: 'The key lives in the secret OG-i-2 provisions; its NAME (never its value) is in org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/SCHWAB_IDENTITIES.json once that cell merges. Read the key through the Gateway's existing secret path (app/integrations/base.py, the secretsmanager:GetSecretValue call).'",
    "world_is": "The secret PATH is used exactly as named: base.SecretsCredential, one GetSecretValue, cached, never logged. What no carrier supplies is the two ends of that path -- which configuration key holds the secret's name at runtime (a deliverable JSON is not deployed to the host), and what the SecretString must contain. This cell chose both and fails closed on anything else, so nothing silently degrades to an unkeyed alias. Both settings must be adopted elsewhere: the value's shape by OG-i-2, the environment variable by the release cell OG-r-1, and neither file is in this order's <paths>.",
    "notes": "ARMED, disarm 2.0.0_SA_COO~O: harmless while nothing deploys and no Schwab tool is built (OG-q-2), and every failure is UNAVAILABLE rather than a weak alias. Left alone, OG-i-2 provisions a value in a shape nobody told it and the release ships without the variable, and every account_ref then reads UNAVAILABLE on a live Gateway. It disarms by naming the shape above in OG-i-2's order and SCHWAB_ACCOUNT_REF_SECRET_ID in OG-r-1's, or by re-cutting this cell with app/config.py in its grant so the name sits beside YCHARTS_SECRET_ID."
  },
  {
    "id": "NFRA_OPLGTW-W3-S26",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~3",
    "surfaced_at": "2026-09-15T23:11:00Z",
    "one_line": "With the root logger at DEBUG, one strong read of a data_entitlement grant writes the DynamoDB response body to the log through botocore's wire logger, and that body carries the grant's raw account ids. The Gateway configures no Python logging anywhere in app/, so the host's root level is Python's default WARNING and the same read logs nothing; the exposure appears only if a later cell lowers the level.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: .scratch/botocore_debug_probe.py in this worktree (moto DynamoDB, one grant carrying one raw account id, data_entitlement.current_access) -- 'root WARNING (host default): log lines 0, lines carrying the raw id 0'; 'root DEBUG: log lines 40, lines carrying the raw id 1', the line being botocore's response body b'{\"Item\"...}'.",
        "SOURCE: infra/aws/ec2/opal-gateway/app/ @f4c7184f6d -- one logging.getLogger in the whole package, app/account_ref.py:70 (this cell's own logger); no basicConfig, setLevel or dictConfig anywhere in app/, so the root logger keeps Python's default WARNING.",
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md @f0aa50dbc0 :147 -- 'never log raw IDs'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGZ3-AC4: 'a raw account ID appears in no log or audit line the harness captures'.",
    "world_is": "The criterion holds for this cell's own surface: 13 arms over 5 corpora (log records, stdout, stderr, the audit JSONL, everything returned to the tool layer), 0 raw ids and 0 key bytes, with the SDK wire loggers held at WARNING, their level on the host. One level below that, the leaking line is not this module's but the AWS SDK's, and it carries the grant record rather than any response this module builds.",
    "notes": "INERT: nothing deploys and the host's level is WARNING by default. A later cell that adds logging configuration to the Gateway should hold botocore/boto3/urllib3 no lower than INFO, or every grant read puts raw account ids in the journal. Any logging configuration and app/config.py are outside this order's grant."
  },
  {
    "id": "NFRA_OPLGTW-S20",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-16T00:40Z",
    "one_line": "Disarm of NFRA_OPLGTW-W3-S25: OG-z-3 chose the alias-key secret's environment variable and value shape because no carrier stated either, and that choice is now carried as a bound into the two unhanded orders that must honour it -- TO-OG-i-2 provisions the secret in that shape and records its name, TO-OG-r-1 sets SCHWAB_ACCOUNT_REF_SECRET_ID from that record.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: NFRA_OPLGTW-W3-S25 (0.9.0_WK_NFRA_OPLGTW~3, ARMED, disarm owner 2.0.0_SA_COO~O) measured that app/config.py names no Schwab alias-key secret, that SCHWAB_IDENTITIES.json does not exist because OG-i-2 has not run, and that neither the decomposition (:156, :189) nor the PRD (:147) states the value's shape or where its name is configured.",
        "CODE, now on CLOUD: infra/aws/ec2/opal-gateway/app/account_ref.py -- SECRET_ID_ENV = 'SCHWAB_ACCOUNT_REF_SECRET_ID'; the value parses as {current_version, keys{v<n>: base64 >= 32 bytes}}; OGZ3-AC1 ran 6 of 6 fail-closed arms, each answering UNAVAILABLE rather than an unkeyed alias.",
        "CARRIED: TO-OG-i-2 (the secret's shape, the Gateway read grant already in its AC1, and the name recorded in SCHWAB_IDENTITIES.json) and TO-OG-r-1 (the release sets the variable from that record, never typed). Both amended in this seat's commit beside this row, and NEITHER order has been handed to a worker.",
        "DRAIN: OG-z-3 merged at c9ff7dbbd3 with the row gate clean on the merged index; the module re-run on the shared checkout (not the worker's) reads 5 passed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-z-3 told the worker the key lives in the secret OG-i-2 provisions and that its name would be in SCHWAB_IDENTITIES.json once that cell merged.",
    "world_is": "OG-z-3 ran before OG-i-2, so the worker had to choose both the variable name and the value shape. The choice is sound and fail-closed, but it binds two later cells that never heard it. It is now written into both of their orders, so neither can honour it by accident or miss it.",
    "notes": "W3-S25's disarm owner is this seat; this act and row disarm it. No criterion was added or removed in either order: both amendments are cell-text bounds, and both orders were unhanded at the time of writing. Filed during the 2026-09-15 ~23:3xZ managed wind-down."
  },
  {
    "id": "NFRA_OPLGTW-W1-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-15T21:52:10Z",
    "one_line": "The amended OG-i-1 order puts grading reads INSIDE the change-management entry (OGI1-AC11's get-ip-set before and after the apply, recorded in the entry; condition 4 as 'a line in your entry'), while its deploy discipline closes and commits the entry BEFORE the reads that grade the act; OG-i-1 records the AC11 reads as a verify leg's proof before the close and runs AC12's fresh plan after it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-i-1.access-state-table.md:56-57 @09668e3207 'Each condition is a line in your change-management entry'; :106 OGI1-AC11 'both reads are recorded in the change-management entry'; :120 'close-leg each leg with its proof and close the entry, and COMMIT that BEFORE the reads that grade the act ... open, commit, act, close, commit, read'; :82 OGI1-AC3 compares the close commit with the first readback.",
        "TOOL: .tools/deploy_ledger.py:438-469 @09668e3207 -- an entry takes content only through its legs (close-leg re-renders it), and close REFUSES while any leg is unproven; its usage text lists a verify leg's proof as a 'post-deploy live-state check (0-diff plan, smoke, served artifact read)'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Open, commit, act, close, commit, read: every read that grades the act follows the committed close, and each of the ruling's four conditions is a line in the entry, with AC11's two reads recorded in it.",
    "world_is": "For AC11 both cannot hold: its reads must be in the entry, the entry takes content only as leg proof, and a leg must be proven before the close. So the get-ip-set reads immediately before and after the apply are the proof of verify leg L4, proven before the close. Condition 4 is declared as a line in leg L5's target and graded by OGI1-AC12's fresh plan after the committed close. No read of the new table or roles precedes the close, so AC3's instrument (the probe's first readback of the table) is unaffected.",
    "notes": "INERT: a sequencing choice, and every read is timestamped under deliverables/0.9.0_WK_NFRA_OPLGTW~1/evidence/. Form only."
  },
  {
    "id": "NFRA_OPLGTW-W1-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-15T21:52:10Z",
    "one_line": "OGI1-AC11's discriminating comparison runs on two EMPTY lists: both regional blocked-IP sets hold 0 addresses live and 0 in the plan's prior state, so 'identical before and after' holds whether or not a description-only UpdateIPSet would preserve a non-empty reconciler list.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "LIVE: probes/og_i1_act.py waf (wafv2 list-ip-sets REGIONAL, 2 sets listed, then get-ip-set x2) at 2026-09-15T21:49:30Z: opal-blocked-ips-regional (f073f448-eb85-4d23-9306-0cadf4573331) count 0 and opal-blocked-ips-regional-ipv6 (85f90377-7cba-45dd-baca-397310d61f8e) count 0, both sha256 e3b0c44298fc1c14 (the empty list), description absent.",
        "PLAN: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/og_i1.plan.json on branch wk-nfra_oplgtw-1-1b (terraform show -json sha256 6056c82b39a1502e, plan 2026-09-15T21:35:37Z): addresses_count_before 0 and addresses_count_after 0 on both sets; addresses is not a changed attribute.",
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-i-1.access-state-table.md:60-62 @09668e3207 -- 'WAF's UpdateIPSet sends the full list, so this readback is what proves the reconciler's list survived'; :106 marks OGI1-AC11 '(discriminating)'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGI1-AC11 is the discriminating proof that the reconciler's address list survives the description backfill.",
    "world_is": "The reconciler's list is empty at this apply, so AC11 compares 0 with 0 and cannot fail on the property it exists for; it can still see a list appearing or vanishing across the apply. The probe prints the lock-token rotation beside it (not deciding) to show the two reads bracket an applied UpdateIPSet. Seeding an address to make the check bite would be a WAF write this order does not grant, so it was not done.",
    "notes": "INERT: an empty list cannot be lost. It matters to the next apply of this root that meets a non-empty list: ignore_changes keeps addresses out of the diff, but whether the provider's UpdateIPSet sends the refreshed live list is not exercised by this apply."
  },
  {
    "id": "NFRA_OPLGTW-W1-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-15T21:56:47Z",
    "one_line": "OG-i-1's one safe-apply run was refused before terraform ran: the halt gate resolves the acting serial only from org/mcp/sessions/<session-id>.serial (or an .orphan-cleaned marker) under the worktree root and never reads OPAL_AGENT_SERIAL, and that gitignored directory is absent in the worker's worktree and outside its write grant.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: probes/og_i1_act.py apply, 2026-09-15T21:56:44.893672Z..21:56:47.841644Z, safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply -no-color: 'HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed)', remedy printed as writing the serial to org/mcp/sessions/e09b6e12-6f85-4732-b702-3307d4a68532.serial, 'Do NOT override this'; exit 3; no approval prompt, terraform never invoked. Record: deliverables/0.9.0_WK_NFRA_OPLGTW~1/evidence/apply.json and apply.log on branch wk-nfra_oplgtw-1-1b.",
        "CODE: .tools/halt-gate-check.sh:52-120 @09668e3207 -- halt_gate_resolve_serial reads ${HALT_GATE_REPO_ROOT}/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial, then ${CLAUDE_CODE_SESSION_ID}.*.orphan-cleaned, else returns 1; :38 HALT_GATE_REPO_ROOT is the script's own checkout (this worktree); :267-274 halt_gate_check blocks on the failed resolution. Native Grep for OPAL_AGENT_SERIAL over the file: 0 hits. The worker admission path (:142-174) validates a 0.9.0_WK serial against a non-terminal order, but is reached only after a serial resolves.",
        "WORKTREE: org/mcp/sessions/ is gitignored (.gitignore:423 @09668e3207), 0 tracked files, absent in /c/tmp/wk-oplgtw-1-1b; the worker's CLAUDE_CODE_SESSION_ID is e09b6e12-6f85-4732-b702-3307d4a68532, the parent session's.",
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-i-1.access-state-table.md:117 and :133-139 @09668e3207 -- the <paths> grant does not name org/mcp/sessions/, and an unnamed path needed is 'a BLOCKING surprise row on that criterion -- never an override'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A worker that exports OPAL_AGENT_SERIAL can run .tools/safe-apply.sh from its own worktree (spawn identity line: 'Begin every Bash call with export OPAL_AGENT_SERIAL=... -- safe-apply's identity gates read it').",
    "world_is": "The halt gate, which safe-apply runs first, never reads OPAL_AGENT_SERIAL. Its only identity sources are session-keyed files under the worktree's org/mcp/sessions/, which is gitignored, absent in a fresh worktree and outside this order's grant. Its remedy is to write that file, and the gate itself says not to override. So the apply did not run: nothing changed in AWS (WAF get-ip-set before and after, 0 and 0 on both sets), the ledger nfra-oplgtw-og-i-1-access-state stays OPEN with L1-L5 unproven, and schwab_access_state.tf sits committed and unapplied at 4b9671ec09 on the worker branch.",
    "notes": "ARMED, the issuer's to disarm, on two counts. (1) Draining wk-nfra_oplgtw-1-1b's schwab_access_state.tf to CLOUD before an order-bound apply lets any later apply of the root create the table and both grants outside this ledger (the shape W1-S1 named). (2) The OPEN sentinel will blare RED past its 2 h window once it is on CLOUD, although nothing was deployed. A re-run needs one of three things: the session serial file admitted by a re-cut <paths> (worktree-local, gitignored, never committed); a serial file the issuer provisions at spawn, as it does .tools/terraform.exe; or an apply by a seat whose identity the gate resolves. It can reuse the open ledger. Form only."
  },
  {
    "id": "NFRA_OPLGTW-W1-S7",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-16T00:14Z",
    "one_line": "OG-i-1's apply ran only with two environment variables the order does not name, HALT_ACK=1 and HALT_GATE_INBOX_ROOT: a worker has no inbox of its own, so safe-apply's halt gate scans its ISSUER's, and the worker's HALT_ACK acknowledged 14 ROUTINE messages addressed to 2.0.0_SA_COO~O, none of them about this apply.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-i-1.access-state-table.md @fd2f1e4b31, BOUNDS/Terraform -- 'Only through .tools/safe-apply.sh, never bare terraform apply, never -target ... Plan and apply run in ONE safe-apply run'. No clause names HALT_ACK, HALT_GATE_INBOX_ROOT or the halt gate at all; the two variables came in the re-hand-off instruction, citing issuer rows S18 and S19 on CLOUD.",
        "GATE: .tools/halt-gate-check.sh in this worktree, run twice under bound at 2026-09-15T23:1xZ: without HALT_ACK rc 1 after 120 s, printing 'HALT-GATE: worker 0.9.0_WK_NFRA_OPLGTW~1 has no inbox; scanning its issuer 2.0.0_SA_COO~O (a [STOP] to the issuer halts its workers)' and 'HALT-GATE: 14 pending message(s) -- review before proceeding (unspecified)'; with HALT_ACK=1 rc 0 after 120 s, 'HALT-GATE: HALT_ACK set -- messages acknowledged. Proceeding.' The 14 subjects are the issuer's mail (sprint Lambda routing, PRD sign-off law, L4 hand-offs), no STOP class.",
        "IDENTITY: org/mcp/sessions/e09b6e12-6f85-4732-b702-3307d4a68532.serial, provisioned by the issuer, gitignored (.gitignore:423), reads '0.9.0_WK_NFRA_OPLGTW~1'; this worker neither wrote nor committed it.",
        "ACT: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/evidence/apply.json @b17f9b05cb -- the ONE run 2026-09-15T23:27:50.539654Z..23:32:28.811293Z, rc 0, 'Apply complete! Resources: 4 added, 2 changed, 0 destroyed.', saved_planfile_consumed false, waf_optimistic_lock_exception false."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The apply runs through .tools/safe-apply.sh, plan and apply in ONE run; the order names no environment the wrapper needs.",
    "world_is": "safe-apply's first stage is the halt gate, and for a worker serial the gate scans the ISSUER's inbox because the worker has none. It returned rc 1 on 14 routine pending messages to 2.0.0_SA_COO~O and rc 0 only once HALT_ACK=1 was exported, with HALT_GATE_INBOX_ROOT pointed at the parent checkout because a linked worktree has no org/mcp/inbox. Both variables were supplied at re-hand-off, not by the order. Under them the one run applied cleanly.",
    "notes": "INERT and FORM ONLY: this records what was done that the order does not say, not whether it should have been. W1-S6's identity block is gone in fact -- the gate resolved this worker from the issuer-provisioned file and nothing under org/mcp/sessions/ was written or committed here. What remains for the adjudicator is whose acknowledgement a worker's HALT_ACK is: the 14 messages are another serial's mail, and a STOP to the issuer would have shown as rc 2, which this run did not see (rc 1 then rc 0)."
  },
  {
    "id": "NFRA_OPLGTW-W1-S8",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-16T00:30Z",
    "one_line": "OG-i-1's proof bound says commit the instance, the deliverables and the status flip TOGETHER, but proof-of-spec-check REFUSES a PENDING-THIS-COMMIT artifact row whose file is NEW AND UNTRACKED, so the run-only evidence file evidence/first_readback.json had to be committed on its own first and pinned by hash before the instance could read VALID.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-i-1.access-state-table.md @fd2f1e4b31, <proof_of_spec> -- the instance is 'validated ... BEFORE the complete flip'; the worker definition adds 'commit instance, deliverables and flip together'.",
        "CHECKER: py -3.12 .tools/proof-of-spec-check.py (checker-vintage 7da8112496) on the instance at 2026-09-16T00:2xZ -- 'VIOLATION: artifact-resolution: .../evidence/first_readback.json is PENDING-THIS-COMMIT but is ABSENT at the instance commit a0bcaa6bae -- it did not ride the commit that carries this proof', INVALID (rc=1). Its own frame line states the rule: a PENDING row is admitted when a dry run finds the TRACKED artifact modified in place, which a brand-new untracked file cannot be.",
        "REMEDY TAKEN: commit 8acd1d3459 carries evidence/first_readback.json and evidence/postplan.json alone; the instance then pins both by that hash and the same checker run reads VALID (rc=0) with 9 resolved at pin and 1 PENDING co-committed. The instance, the result file, this channel and the <status> flip then go in ONE commit, as the bound asks."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Validate the instance, then flip <status> and commit the instance, the deliverables and the flip together.",
    "world_is": "The two acts cannot both hold for an artifact the RUN creates: the checker resolves PENDING against the instance's LAST commit, so a file first written after that commit reads ABSENT and the instance is INVALID until the file is committed separately. Splitting the evidence file into its own prior commit is what makes the validation the bound requires possible at all; the flip still rides one commit with the instance and the deliverables.",
    "notes": "INERT and FORM ONLY. It costs one extra commit per run-created evidence file and nothing else; no criterion's measurement changes. The general shape is the known PENDING one-shot: the sentinel names 'this commit' but is read against the commit the instance already has."
  },
  {
    "id": "NFRA_OPLGTW-W5-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-16T18:13:06Z",
    "one_line": "TO-OG-k-1's hand-off names tests/test_identity_scope.py::test_scoped_deny_by_default as 'the known red test' that 'fails at the cut base', with an instruction never to edit it or identity_tool_allowlist.txt. Neither file carries any change in this worktree (both clean at HEAD f4c7184f6d), and the test PASSES.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: cd /c/tmp/wk-oplgtw-1-5c && .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_identity_scope.py::test_scoped_deny_by_default -v -p no:cacheprovider --color=no -> '1 passed in 0.07s', at HEAD f4c7184f6d.",
        "git status --short infra/aws/ec2/opal-gateway/tests/test_identity_scope.py -> no output (clean, unmodified by this worker or any predecessor in this worktree).",
        "git log -1 -- infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt -> 2781aac326 (LD-0415 repo rename), no commit since; the file is clean in this worktree's git status."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-k-1 hand-off: 'tests/test_identity_scope.py::test_scoped_deny_by_default fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or identity_tool_allowlist.txt.'",
    "world_is": "The test passes at this worktree's base, unmodified. Either row S1's finding was already remediated upstream of this cut by a change outside this cell's <paths> (so the hand-off's premise is stale), or the failure is state-dependent (test order / fixture interaction) and does not reproduce standalone -- this row does not adjudicate which. This cell's own 17 criteria (OGK1-AC1..17) are unaffected: none of them names or depends on this test, and neither identity_tool_allowlist.txt nor test_identity_scope.py is in this cell's <paths>, so no action was taken beyond this observation.",
    "notes": "INERT: no criterion of this order reads this test, and the worker made no edit to either named file. Filed on the bounded sanity check this order itself invited ('Existing AuthKind values and their integrations keep their behaviour'), not as a hunt."
  },
  {
    "id": "NFRA_OPLGTW-W1-S9",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-16T18:20Z",
    "one_line": "OG-i-2's two role names are fixed verbatim by PRD C6, and safe-apply's naming limb grades both as REFUSE when it reads the plan (a new IAM role with an out-of-pattern name). The limb is in WARN mode today, so the apply is not stopped. Under ENFORCE, the same apply would stop with exit 7 unless the names get a registry row or an R20 departure.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SPEC: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md @f0aa50dbc0, C6 -- 'the dedicated assumed role `opal-mcp-emp-menachem-schwab-read`' and 'a separate Gateway-assumable `opal-mcp-schwab-catalog-read` role'; the order's cell text repeats both names.",
        "GATE: python .tools/naming-apply-gate.py --plan-json <show -json of the saved plan> in worktree /c/tmp/wk-oplgtw-1-1c @5503d92f88 plus the uncommitted schwab_reader_iam.tf, 2026-09-16T18:0xZ, rc 0 -- 'NAMING REFUSE aws_iam_role.schwab_catalog_read opal-mcp-schwab-catalog-read -> opal-mcp-schwab-catalog-read-role' and 'NAMING REFUSE aws_iam_role.schwab_data_read opal-mcp-emp-menachem-schwab-read -> opal-mcp-emp-menachem-schwab-read-role', each 'why: ... (ADDITION): OUT-OF-PATTERN as IAM_ROLE'.",
        "SWITCH: .tools/safe-apply.sh @5503d92f88 -- ENFORCE only when org/mcp/naming-gate.enforce exists or NAMING_GATE_ENFORCE=1; neither file exists in this worktree or in the shared checkout (ls, 2026-09-16T18:0xZ), so the plan-mode stage never changes the exit code."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The two reader roles carry the names C6 gives them.",
    "world_is": "They do, and the canon's builder would name them with a -role suffix. In WARN mode the naming limb prints REFUSE for both and lets the apply continue. The order is frozen and names the roles verbatim, so they are kept as written. Rule 30 exempts existing pipelines and routes a deliberate departure to an R20 register entry; this order records neither.",
    "notes": "INERT and FORM ONLY. Nothing is renamed here. If ENFORCE is switched on before a later apply of this root, that apply stops at exit 7 on these two names unless a registry row or an R20 entry exists by then. The five resources already in taxsma_gateway_iam.tf print WARN, not REFUSE, only because they already exist."
  },
  {
    "id": "NFRA_OPLGTW-W1-S10",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-16T18:20Z",
    "one_line": "OG-i-2 names no mechanism for three things it requires, so this worker chose: (1) the two ExternalIds are generated by Terraform (uuid() frozen by ignore_changes) into a Secrets Manager secret, so they sit in Terraform state; (2) the alias-key VALUE is written out-of-band with put-secret-value, not by Terraform; (3) the Gateway's read grants on both secrets are resource policies on the secrets, so its identity policies gain exactly the one assume statement.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-i-2.reader-identities.md -- 'where each ExternalId and the alias key live (secret or parameter NAMES, never values)'; 'Provision the secret with THAT shape'; BOUNDS 'No ExternalId value, alias key, credential or object content enters a committed file'; Blast radius 'adds exactly one statement to the Gateway role's inline policies'; AC1 'the alias-key secret with the Gateway's read grant on it'.",
        "CONVENTION: infra/aws/terraform/opal-gateway/secrets.tf @5503d92f88 -- 'METADATA ONLY -- never aws_secretsmanager_secret_version (the value never enters TF state)'. The existing Tax SMA ExternalId is typed literally in taxsma_gateway_iam.tf, which this order forbids for its own values.",
        "LOCK: infra/aws/terraform/opal-gateway/.terraform.lock.hcl @5503d92f88 pins only hashicorp/archive and hashicorp/aws, so no random provider exists to generate either value without a new provider download.",
        "PLAN: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/og_i2.plan.json (terraform 1.9.8, 2026-09-16T18:03:38Z) -- 'Plan: 10 to add, 0 to change, 0 to destroy.', including aws_secretsmanager_secret_version.schwab_reader_external_ids and two aws_secretsmanager_secret_policy resources, and no version resource for the alias key."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Provision the two ExternalIds and the alias-key secret (JSON shape of OG-z-3), give the Gateway a read grant on the alias-key secret, and add exactly one statement to the Gateway role; no value in a committed file.",
    "world_is": "An ExternalId cannot be kept out of Terraform state, because each trust policy Terraform writes carries it. So generating it there adds no new copy. The estate convention keeps a real secret VALUE out of state, so the alias key (32 bytes from secrets.token_bytes, base64, under current_version v1) is written once by og_i2_act.py put-alias-key after the apply. That command refuses if the secret already holds a version, and it records the version id and the read-back shape, never the value. Identity-policy grants on the two secrets would add a second and third statement to opal-gateway-role, so each secret carries its own resource policy, principal opal-gateway-role, secretsmanager:GetSecretValue only.",
    "notes": "INERT and FORM ONLY. What a later cell inherits: the Gateway reads ExternalIds from opal/mcp/opal-gateway-schwab-reader-external-ids (fields data_read, catalog_read) and the key from opal/mcp/opal-gateway-schwab-account-ref-key. Rotating an ExternalId means tainting the version resource. Rotating the key means adding a version and moving current_version, which put-alias-key refuses to do. Both secrets carry prevent_destroy."
  },
  {
    "id": "NFRA_OPLGTW-W1-S11",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-16T18:35Z",
    "one_line": "Row NFRA_OPLGTW-W1-S9 undercounts: the naming limb printed THREE REFUSE verdicts on OG-i-2's additions, not two. The third is the Gateway inline policy opal-gateway-assume-schwab-readers (-> gateway-assume-schwab-readers-policy). That name is this worker's choice, following the root's existing var.name-prefixed policy names, not a name the PRD fixes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SAVED-PLAN RUN: naming-apply-gate.py --plan-json over the show -json of og_i2.plan.json, 2026-09-16T18:0xZ -- '(WARN window: 3 REFUSE verdict(s) did not block ...)', REFUSE on aws_iam_role.schwab_catalog_read, aws_iam_role.schwab_data_read and aws_iam_role_policy.gw_assume_schwab_readers. S9 was written from a first page of this output cut at 30 lines, which showed only the two roles.",
        "APPLY RUN: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/evidence/og_i2/apply.log -- the in-run naming plan stage prints the same three REFUSE lines, and the apply proceeded (WARN mode), 'Apply complete! Resources: 10 added, 0 changed, 0 destroyed.'",
        "CONVENTION: infra/aws/terraform/opal-gateway/taxsma_gateway_iam.tf and schwab_access_state.tf @5503d92f88 name their Gateway policies with the var.name prefix: '-assume-emp-roles' and '-access-state-runtime'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row W1-S9's count of naming REFUSE verdicts on this cell's additions (two).",
    "world_is": "There are three: the two C6 role names and the Gateway policy name. W1-S9 stands as filed, because rows are never edited, and this row carries the correct count. Under ENFORCE, a later apply of this root would stop on all three.",
    "notes": "INERT and FORM ONLY. The policy name could conform without any spec change, unlike the two role names. It is left as applied because renaming an inline policy destroys and recreates it, which is outside this order's blast radius."
  },
  {
    "id": "NFRA_OPLGTW-W4-S10",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-16T18:42:00Z",
    "one_line": "The estate build for this Lambda (infra/aws/lambda/ci/build-and-upload.sh opal-assets opal-assets-silver-schwab) exits rc=1 with no error line, before the zip, on every package whose BUILD_MANIFEST.json declares no declared_blobs: its manifest probe exits 1 by design for 'declares nothing', but the script runs under set -e, so the shell aborts before MANIFEST_DECL=$? can route that to the SKIP branch. The worker re-ran with the script's own documented per-build override BAU_MANIFEST_SKIP=1, which reaches the same state the SKIP branch was written to reach.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: TMPDIR=<ws>/.scratch bash infra/aws/lambda/ci/build-and-upload.sh opal-assets opal-assets-silver-schwab at worktree HEAD 58a95125c1, 2026-09-16T18:38:31Z -> last line 'OK: import-closure -- 12 packaged .py file(s) ...', then rc=1; no SHA256 line, no upload, source map unchanged (git status clean under infra/). Log: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/deploy/build.log.",
        "SOURCE: infra/aws/lambda/ci/build-and-upload.sh @58a95125c1 -- :33 'set -e'; :300-310 the unguarded 'python - \"$PY_SOURCE\" <<PYEOF ... sys.exit(0 if m.get(\"declared_blobs\") else 1)'; :311 'MANIFEST_DECL=$?'; :346-349 the SKIP branch ('this BUILD_MANIFEST declares no declared_blobs ... (not a pass)'). Last touched by dbbbfb89b2 (2026-08-30 05:43 -0400), after the schwab pin's build 5c7b2a9a6b (2026-08-29 22:26 -0400).",
        "MANIFEST: py -3.12 json.load of infra/aws/lambda/opal-assets/opal-assets-silver-schwab/BUILD_MANIFEST.json @58a95125c1 -> keys [function, vendored_modules, vendoring, layer_dependencies, memory_mb, timeout_s, sizing_basis, contract]; declared_blobs False.",
        "REPRODUCTION (different instrument, no repo file): bash -c 'set -e; python - <<PYEOF / import sys; sys.exit(1) / PYEOF; X=$?; echo reached' -> prints nothing, outer rc=1."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-c-2 THE CELL: 'Find the build that writes that artifact from the vendored directory, and use it.'",
    "world_is": "The build as written cannot produce this package's zip: it stops rc=1 silently at the manifest-declaration probe, which is also how a non-declaring package reached the dead branch for every build since dbbbfb89b2. The override BAU_MANIFEST_SKIP=1 (documented at :286 'Override per-build ... justify in the commit message') skips only that probe, whose designed outcome for this manifest is SKIP; import-closure still runs. The worker used it for this one build and records it here and in the ledger commit.",
    "notes": "INERT for this order (the override reaches the designed branch). Estate-wide it is a latent build break for 13 of 14 packages per the script's own count at :278; that repair is the script owner's, not a rider on this order."
  },
  {
    "id": "NFRA_OPLGTW-W4-S11",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-16T19:20:00Z",
    "one_line": "To name 'every date=D key' that G-B condition 5 asks for, this worker had to LIST prefixes under s3://opal-data-49financial/gold/advi/ (5 delimiter listings per pass returning CommonPrefixes: gold/advi/, canonical/, dimensions/, insurance/, reference/) before reading the date=2026-09-15 keys; ruling R-OG-4 as carried in the order admits read-only access on exactly gold/advi/_logs/ and the named date=D keys, and no carrier names the date=D keys themselves.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER at CLOUD 68bd819cd8 (amended @7c44a2cf82), BOUNDS Cross-firm law: 'admitted read-only (list, head, get) on exactly s3://opal-data-49financial/gold/advi/_logs/ and the date=D keys those conditions name, with every key read printed and nothing else in that bucket'.",
        "SIGNOFF at CLOUD 68bd819cd8, Half 2 s.E condition 5: 'For W and W-partial it also names the before and after VersionIds of every date=D key'; s.A lists areas (dimensions/, reference/ref_txn_classification/, canonical/, insurance/) but no key list.",
        "READS: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/replay/gold49f_date_d_before.json and _after.json, field 'reads' -- 29 calls each pass: 5 delimiter listings (CommonPrefixes only, no object keys outside date=D) and 24 list-object-versions on <table>/date=2026-09-15/. Result: 31 keys; also reference/bd_legacy_* tables, which Half 2 s.B names as another writer's keys."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Cross-firm law as amended: only _logs/ and the date=D keys the conditions name, nothing else in that bucket.",
    "world_is": "The date=D key set is not enumerated in any carrier, so meeting condition 5 needed 5 prefix listings one level above the admitted keys on each of 2 passes (before, after). No object outside _logs/ and date=2026-09-15/ was read; nothing was written.",
    "notes": "INERT: read-only listings, every call printed in the evidence files. For a later replay: name the date=D table prefixes in the sign-off, or admit the prefix listing."
  },
  {
    "id": "NFRA_OPLGTW-W4-S12",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~4",
    "surfaced_at": "2026-09-16T19:21:00Z",
    "one_line": "The replay-caused 49F dispatch ran a full chain that ends CHAIN OK date=2026-09-15, but advi-49f-gold-dispatch logged 'ERROR: chain terminal within poll window, signature=UNKNOWN(first_line=Completed 1.5 KiB/1.1 MiB ... with 84 file(s) remaining)' for the same command -- the dispatcher classifies the SSM output by its first line, which was an aws s3 progress line.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DISPATCHER: CloudWatch /aws/lambda/advi-49f-gold-dispatch filter-log-events from 2026-09-16T19:09Z (8 events, no nextToken): 19:11:45 'dispatched: doc=advi-49f-chain-dispatch command_id=8e7e7614-e014-4342-ae4a-47b8bb7ac0d1 started_by_dispatcher=True'; 19:14:15 'ERROR: chain terminal within poll window, signature=UNKNOWN(first_line='Completed 1.5 KiB/1.1 MiB (5.8 KiB/s) with 84 file(s) remaining') {\"statusCode\": 200, \"dispatched\": true, ...'.",
        "SSM: get-command-invocation 8e7e7614-e014-4342-ae4a-47b8bb7ac0d1 on i-01003b035d2988dfb -> Success (19:14:31Z).",
        "CHAIN LOG: s3://opal-data-49financial/gold/advi/_logs/chain_20260916T191146Z.log VersionId v46i6VrCC8vcbd4.1l49c88tS1GtV7aK, 145 lines: first 'CHAIN START date=2026-09-15 mode=production ... stages=18', last 'CHAIN OK date=2026-09-15 wall=144.6s'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "G-B sign-off Half 2 s.C: each dispatch branch (R, A, W, W-partial) is distinguishable from what the chain writes and logs.",
    "world_is": "The dispatcher's own verdict line for a successful branch-W run reads ERROR with signature UNKNOWN, so the dispatcher log cannot be used to classify a dispatch's branch; the chain log and the SSM status can. Not caused by this order's code.",
    "notes": "INERT for this order: branch W was classified from the chain log and SSM status. Owner of advi-49f-gold-dispatch decides."
  },
  {
    "id": "NFRA_OPLGTW-W2-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~2",
    "surfaced_at": "2026-09-16T19:16Z",
    "one_line": "A CloudWatch GetMetricStatistics percentile query whose one requested Period spans the 15-day 1-minute-resolution retention boundary silently returns TWO datapoints instead of one, split unevenly (measured [10, 79222] samples for a 30-day window on this ALB) -- reading Datapoints[0] alone (the first build of AC11) reported a p95 of 31 ms from the 10-sample sliver where the window's true, dominant figure is ~553 ms.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: cloudwatch get-metric-statistics (AWS/ApplicationELB TargetResponseTime, LoadBalancer=app/opal-gateway/89166a68f337e5a4, ExtendedStatistics p95, Statistics SampleCount) via .tools/aws, one call per width, StartTime = EndTime - width, Period = width, EndTime fixed at 2026-09-16T18:51:44Z/19:1xZ: widths 1 hour through 14 days each returned exactly 1 Datapoint (e.g. 14 d -> SampleCount 43642); 15 d -> 2 datapoints SampleCount [10.0, 45233.0]; 16 d -> [46676.0, 10.0]; 30 d -> [10.0, 79222.0] (timestamps exactly one Period apart, both at :50:00 minute-of-hour, not proportional to elapsed time).",
        "CODE (this worktree, uncommitted at grounding time): org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_p1.py -- AC11_WINDOW_DAYS lowered from 30 to 14 with this finding recorded beside it; ac11() no longer indexes Datapoints[0] directly -- _cw_datapoint(data) refuses (returns a problem, not a value) whenever len(Datapoints) != 1.",
        "RE-RUN AFTER FIX: same probe, AC11, 14-day window: exactly 1 datapoint, sample_count=43745, p95_seconds=0.5535 (553.5 ms) -- consistent with the dominant bucket the 15/16/30-day probes also showed (~0.55 s), confirming the 31 ms figure from the unfixed build was the defect, not the true baseline."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGP1-AC11 (amended) asks for p95 latency from the ALB's TargetResponseTime over 'a stated window', with no width named -- any width the criterion states is legal on its face.",
    "world_is": "CloudWatch keeps 1-minute-resolution datapoints, which percentile (ExtendedStatistics) queries require, for 15 days; a single-period request whose span crosses that boundary is not clipped to the requested window -- it is silently answered with two datapoints that do not partition the window proportionally to time, and nothing in the response signals the split as an error. A caller that assumes 'one period, one datapoint' and reads Datapoints[0] gets a real AWS value that is nonetheless the wrong one for the claimed window, with no error, no denominator mismatch and no exception -- the exact 'clean metric with a wrong verdict' shape Rule 22 warns about. This cell caught it before recording by widening the control from a single dry run to a day-by-day bisection, fixed it by choosing a window under the retention boundary, and added a second, independent guard that refuses outright rather than mis-picking if the split ever recurs (a shorter window, a different metric, or a future retention-policy change).",
    "notes": "INERT: caught and fixed inside this same cell before any figure was recorded or committed; nothing downstream consumed the wrong 31 ms value. OBSERVATION, not ARMED: no other cell in this project currently issues a CloudWatch ExtendedStatistics query, so disarm_owner is not named; any FUTURE cell (in this or another project) that queries CloudWatch percentiles with a period longer than ~14 days should read this row first -- an estate-wide instrument-trap catalogue entry (CLAUDE.md 22a) is the issuer's or CTO's call, not this cell's to make."
  },
  {
    "id": "NFRA_OPLGTW-W5-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-16T19:37:00Z",
    "one_line": "OGQ2-AC26 cannot be met as written. It requires app/data_entitlement.py to differ from the cut base by exactly five added entries, one per Schwab tool, but the cut base already classifies all five: OG-z-1 added them. schwab_get_access also has no contract operation class. The worker added no entry, and the AC26 probe prints FAIL.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SOURCE: infra/aws/ec2/opal-gateway/app/data_entitlement.py:75-81 @0fc7c71160 -- SCHWAB_TOOLS already maps schwab_get_access: None, schwab_list_files: 'list', schwab_describe_dataset: 'describe', schwab_query: 'query', schwab_prepare_download: 'download_filtered'; :103 puts all five in TOOL_CLASSES as CLASS_SCHWAB; :279 allowed_tools grants an op=None tool to any active grant.",
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-q-2.tools-and-validation.md:68 @85e35f511c -- 'So your five tools need entries in app/data_entitlement.py'; :72 'No entry widens an existing one, and none takes a permissive default'; :73 'A tool whose class is unclear is a surprise row, not an entry'.",
        "PRIOR ROW: NFRA_OPLGTW-W3-S23 (this channel) already recorded that 'data_entitlement.py pre-classifies those five names and maps each to an operation'.",
        "RUN: cd /c/tmp/wk-oplgtw-1-5d && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q2.py AC26 -> 'diff 0fc7c71160..worktree: 0 added line(s), 0 removed line(s)', 'VERDICT: FAIL-OGQ2-AC26 0 added lines, expected exactly 5; 0 of 5 contract tools have an added entry', rc=1. The probe was checked with a synthetic diff: five well-formed entries print PASS (rc 0), and the same entries plus one removed line print FAIL (rc 1).",
        "RUN: OGQ2-AC25, the guard module with the real schwab integration registered in the registry: '12 passed in 13.02s', rc=0; test_ogq2_ac01 asserts de.classify(t) == 'schwab' for all 5 registered tools."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-q-2 (amended on 1.0.0_SA_CTO's ruling msg 97251), AC26: 'the diff of app/data_entitlement.py against your cut base is exactly five added entries, one per contract tool name, each with an operation class from the contract, and no other line'.",
    "world_is": "At the cut base the file already classifies all five tools, so the classification the amendment wanted exists and the guard serves the real tools (AC1, AC25). Five more entries could only duplicate or override lines that already exist. schwab_get_access also has no contract operation: it is None, 'any active grant'. Giving it one of list/describe/query/download_filtered would change an existing entry, and the order routes an unclear class to a surprise row, not an entry. So app/data_entitlement.py is unchanged, AC26 is refused as written, and the order stays open.",
    "notes": "BLOCKING on OGQ2-AC26 only. The other 25 criteria pass by output. INERT: nothing deploys, and the existing classification is what the guard enforces. Two ways out, both the issuer's: re-cut AC26 to certify that the file is unchanged and already classifies the five tools, or rule a contract class for schwab_get_access. The second would be a change to OG-z-1's entry, outside this order's 'entries only' grant."
  },
  {
    "id": "NFRA_OPLGTW-W5-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-16T19:37:00Z",
    "one_line": "schwab_query and schwab_prepare_download refuse dim_asset with UNAVAILABLE (asset_policy_selection_unavailable). The PRD's partial-account CUSIP restriction for dim_asset belongs to OG-q-3 and is not built yet. Without it, an asset read would ignore the account grant. The tool layer therefore takes an asset_policy hook, and until one is supplied it fails closed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md @f0aa50dbc0 C3 -- 'For a partial-account grant restrict its CUSIPs to holdings of the authorized accounts for that same master/date ... absent qualification denies the asset read.'",
        "ORDER: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-q-3.snapshot-semantics.md -- OGQ3-AC11..AC13 assign that selection to OG-q-3 (semantics.py), which depends on OG-q-2.",
        "SOURCE: infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py on branch wk-nfra_oplgtw-1-5d -- SchwabService(asset_policy=None) is the default, and query() and prepare_download() raise UNAVAILABLE 'asset_policy_selection_unavailable' for dim_asset while it is None.",
        "SOURCE: the same branch's app/integrations/schwab/query.py DATASET_SCHEMAS -- field types copied from data/assets/scripts/silver/schwab_schemas.py @0fc7c71160 (dim_position quantities decimal(15,5), market_value_settled_unsettled decimal(17,4), closing_price decimal(16,5), dim_balance values decimal(15,2)); DATASET_GRAINS declares dim_position (account_id, cusip, l_s), dim_balance (account_id,) and dim_asset (cusip,), each validated per snapshot by a count-per-grain job before any page is cut."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-q-2: 'schwab_query executes one master/dataset/date' over the contract's three datasets.",
    "world_is": "schwab_query and schwab_prepare_download serve dim_position and dim_balance. dim_asset is listed and described but refuses data until OG-q-3 supplies the asset policy. The declared unique grains are unmeasured against real silver: a snapshot whose grain is not unique refuses paging (AC20) rather than paging wrongly.",
    "notes": "INERT: fail-closed, nothing deploys, and no criterion of this order reads dim_asset data. OG-q-3 fills SchwabService(asset_policy=...) and owns the measured dataset descriptions."
  },
  {
    "id": "NFRA_OPLGTW-W5-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-16T19:37:00Z",
    "one_line": "The 500-row response cap is counted across every representation. Each result carries its rows twice, in structuredContent and in the duplicate JSON text block, so no single page returns more than 250 rows even though page_size accepts up to 500.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md @f0aa50dbc0 C4 -- 'Limit the entire serialized MCP result to 500 rows, 100,000 Unicode codepoints and 131,072 UTF-8 bytes, including all content blocks, structuredContent and duplicated text.'",
        "SOURCE: infra/aws/ec2/opal-gateway/app/integrations/schwab/envelope.py measure() on branch wk-nfra_oplgtw-1-5d -- rows = structuredContent rows plus the rows of each text block.",
        "RUN: test_ogq2_ac16 -- 'page_size 500 over 700 matched -> returned 151, truncated True; measured rows 302 (structured 151 + text 151), codepoints 70340, utf-8 bytes 130740' (here the byte cap bound first)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C4 names 500 rows and says the limit includes duplicated text, but not whether a duplicated row counts once or twice.",
    "world_is": "The worker took the literal, conservative reading: a row counts once in each representation. A larger page is always truncated with explicit counts and a cursor, so no row is lost. The other reading, rows counted once, would let a page return up to 500.",
    "notes": "INERT: the stricter reading only shortens pages. The spec owner can relax it by changing envelope.measure()."
  },
  {
    "id": "NFRA_OPLGTW-S21",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-16T20:15Z",
    "one_line": "Two drained cells' tests contradict on CLOUD: OG-z-2's test_ogz2_ac08 asserts 'schwab' is not a registered integration id (a self-declared tripwire for widening its POLICY# census), while OG-q-2 registers the schwab integration in app/integrations/registry.py as its own order required. After both drains the shared tree reads test_entitlement_admin.py 1 failed, 8 passed; each branch was green alone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN (shared tree @6a7e9f6caf, the OG-z-2 worktree's venv): pytest tests/test_entitlement_admin.py -> '1 failed, 8 passed'; FAILED test_ogz2_ac08: AssertionError 'the five Schwab tools are classified but not yet registered on any factory; if that changes, this census's file set must widen with it' -- assert 'schwab' not in ['globgrph', 'opal_portal', 'schwab', 'ycharts'] (tests/test_entitlement_admin.py:311). Re-run: same result.",
        "CONTROL: the same module in the OG-z-2 worktree @7a5554face (before OG-q-2's merge) -> '9 passed'.",
        "CAUSE, read: OG-q-2 @c3728d6bdb adds schwab to app/integrations/registry.py, registering only when ENABLED_INTEGRATIONS lists it (OGQ2-AC24); OG-z-2's AC8 census enumerates registered integration ids and fails closed when schwab appears.",
        "OG-q-2's own module on the shared tree: tests/test_schwab_query.py 24 passed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGZ2-AC8: no registered MCP tool writes a POLICY# record, over all tools, denominator printed -- with the schwab integration inside 'all tools' once it is registered.",
    "world_is": "The census's file set excludes the schwab integration's modules and trips by design now that OG-q-2 registered them, so the criterion is unmet at CLOUD HEAD though no tool writes POLICY# by either cell's evidence. Remedy by this seat within L6: TO-OG-z-2 is re-opened (status pending) with an amendment widening AC8's census to the schwab integration's modules, and cold re-handed to 0.9.0_WK_NFRA_OPLGTW~3.",
    "notes": "No served surface; nothing deployed. This seat is the disarm owner and the re-opened OG-z-2's drain is the disarming act."
  },
  {
    "id": "NFRA_OPLGTW-S22",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-17T13:06Z",
    "one_line": "Ruling R-OG-10(a) adds `access` to the contract's `operations` enum, but that enum is the GRANTABLE scope-operation set: ops/schwab_entitlement_admin.py:163 builds its allowed set from it, while app/data_entitlement.py:61 OPERATIONS (checked at :214) would refuse a grant naming `access` as Malformed. The ruling's 'one mapping line' is also short by one: allowed_tools() at :282 admits a tool only when `op is None or op in grant.scope.operations`, so mapping schwab_get_access to 'access' alone denies it to every grant.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ @4c179f1826: infra/aws/ec2/opal-gateway/ops/schwab_entitlement_admin.py:163 `ops_allowed = set(contract.get(\"operations\") or de.OPERATIONS)`.",
        "READ @4c179f1826: infra/aws/ec2/opal-gateway/app/data_entitlement.py:61 `OPERATIONS = (\"list\", \"describe\", \"query\", \"download_filtered\")`; :214 `if not operations <= set(OPERATIONS): raise Malformed(...)`; :76 `\"schwab_get_access\": None`; :282 `if op is None or op in grant.scope.operations`.",
        "RULING: 1.0.0_SA_CTO msg 97578 (R-OG-10): (a) `access` added to NFRA_OPLGTW_CONTRACT.json `operations` enum in v1.1 and to SCHWAB_TOOLS; (b) AC26 re-cut as 'the file unchanged against the cut base except the one mapping line'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "R-OG-10: one mapping line in app/data_entitlement.py and one `access` entry in the contract `operations` enum make schwab_get_access's class explicit, granted iff the grant is active.",
    "world_is": "Applied as written, the enum entry makes `access` grantable by the admin command yet refused by the guard's parser (a grant the admin writes denies its principal everything), and the mapping line without the :282 predicate change denies schwab_get_access to every principal. Not applied: TO-OG-q-2 is NOT amended until 1.0.0_SA_CTO rules call 11; its re-hand is queued after OG-q-3 on slot ~5, so no worker waits.",
    "notes": "No served surface; nothing deployed. REC sent as call 11: carry `access` as a tool class outside the grantable `operations` enum (a separate contract key naming each tool's class), leave OPERATIONS and the admin set unchanged, and let AC26 admit exactly two lines: the :76 mapping and the :282 predicate `op == \"access\" or op in grant.scope.operations`."
  },
  {
    "id": "NFRA_OPLGTW-W6-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~6",
    "surfaced_at": "2026-09-17T13:57:35Z",
    "one_line": "A newer qualified closure now exists live in AWS for date=2026-09-16 (both masters, status qualified, 0 findings), produced independently of OG-c-2's replay after this cell's inherited premise ('2026-09-15 is the only qualified closure that exists') was written; the sealed hashes this cell commits still use only OG-c-2's 2026-09-15 silver objects, per the order's own explicit VersionId source, so the Gateway's live catalog at OG-v-4/A7 time may report 2026-09-16 as the true 'latest' business date while these sealed hashes assume 2026-09-15.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN (read-only, this worker's worktree): '.tools/aws s3api head-object --bucket opal-data-assets --key schwab/08242234/meta/complete/date=2026-09-16.json' -> LastModified 'Thu, 17 Sep 2026 10:16:23 GMT', VersionId TJRM3DcNtwtdAUWd2jU0JlrjRX_z508x, ContentLength 15650 -- absent at the 2026-09-16 16:20 local vintage the inherited handoff (C:/tmp/nfra-oplgtw-handoff/og-v-3-partial/scripts/QUALIFIED_VERSIONS.json) sealed against.",
        "RUN: the same for 08335338/meta/complete/date=2026-09-16.json -> LastModified 'Thu, 17 Sep 2026 09:46:56 GMT', VersionId KGvM5aTswwqrJe6tHImICkdyU2Q5WyyS.",
        "RUN: GetObject of the 08242234 record -> schema opal.silver.completion (new C3-extended shape), closure.status='qualified', closure.findings=[], closure.day_disposition='DATA', closure.date='2026-09-16'.",
        "RUN: '.tools/aws s3api head-object ... date=2026-09-17.json' for both masters -> 404 Not Found, so 2026-09-16 is the latest closure as of this row's timestamp, not 2026-09-15.",
        "The order's own worker face (NFRA_OPLGTW.TO-OG-v-3.sealed-real-expectations.md) directs: 'compute the expected answer from the qualified silver objects OG-c-2 produced' and 'The qualified object keys and VersionIds are in OG-c-2's result file' -- OG-c-2 replayed and closed only 2026-09-15 (deliverables/0.9.0_WK_NFRA_OPLGTW~4/producer-deploy-replay.result.md section 1); this cell follows that instruction literally and does not re-derive 'latest' from AWS at seal time.",
        "WALKTHROUGH_PROTOCOL.md section 4 (infra/aws/ec2/opal-gateway/tests/acceptance/) defines 'latest' as 'the latest qualified complete business date the catalog reports for that master and dataset at the time OG-v-3 seals' -- a live-clock definition the order's OG-c-2-scoped instruction does not literally match now that a later qualified date exists."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-v-3 worker face: 'compute the expected answer from the qualified silver objects OG-c-2 produced'; the inherited (unverified, superseded) handoff concluded '2026-09-15 is the only qualified closure that exists for either master as of this seal. No previous qualified date exists to compare against for RQ5/RQ6.'",
    "world_is": "As of this row's timestamp (2026-09-17T13:57:35Z), both masters carry a second qualified closure for date=2026-09-16 (status qualified, 0 findings), produced by the live production Schwab pipeline independently of OG-c-2. This cell deliberately seals its RQ1-RQ6 expected answers against OG-c-2's 2026-09-15 objects only, exactly as the order instructs, and does not use the 2026-09-16 closure or its silver objects. If the Gateway's catalog construction (OG-c-1/OG-k-1) runs before OG-v-4's A7 walkthrough and reports 2026-09-16 as the latest qualified date, the real answers to RQ1, RQ3, RQ4's SmartX/BlackDiamond legs and RQ5/RQ6's 'latest' leg would be computed over 2026-09-16 data and would not hash-match these 2026-09-15-based sealed values; RQ5/RQ6 would also gain a real previous-qualified-date (2026-09-15) where this seal says NONE_QUALIFIED.",
    "notes": "ARMED because a hash mismatch at OG-v-4/A7 time is not cosmetic -- it would read as the Gateway giving a wrong answer when the real cause is this seal using a superseded 'latest'. Nothing served or deployed by this row. Disarm: the issuer (2.0.0_SA_COO~O) either re-seals OG-v-3 against whatever is qualified-latest immediately before OG-v-4 runs A7, or fixes 2026-09-15 as the walkthrough's authorized business date for A7 (a fixed-date grant per PRD C3) so the comparison is apples-to-apples; either is the issuer's call, not this cell's to make unilaterally mid-round."
  },
  {
    "id": "NFRA_OPLGTW-S23",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-17T14:59Z",
    "one_line": "Disarm evidence for NFRA_OPLGTW-W6-S5 (ARMED, disarm owner 2.0.0_SA_COO~O): ruling R-OG-12 is carried into TO-OG-o-2 and TO-OG-v-4 @71bc5b82ed, before either is handed. RQ1-RQ6 are fixed to business date 2026-09-15 (the date OG-v-3 sealed), and one live, unsealed no-date request per master grades the explicit latest date. A daily qualified closure can no longer make a correct Gateway fail OGV4-AC5.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULING: 1.0.0_SA_CTO msg 97602, R-OG-12 @df750f1e26 (item 4: W6-S5 disarms when the amendment commits; this seat files the disarm evidence).",
        "COMMIT 71bc5b82ed: TO-OG-o-2 grants infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md for section 4's dates and one A7 step, and adds AC10/AC11. TO-OG-v-4's AC5 is re-worded to the fixed date 2026-09-15, and AC6 (the returned latest equals the newest qualified closure marker before the ask time) and AC7 (the available dates contain 2026-09-15) are added.",
        "PLACEMENT: the ruling's item 3 put the protocol in TO-OG-v-4's <paths>. v-4 spawns only after the G-D walkthrough record exists, so the protocol edit rides TO-OG-o-2, which v-4 depends on and which is not yet handed. Stated in both orders' records.",
        "GRANT CHECK @71bc5b82ed: `owned-paths-validate.py --check-agent 0.9.0_WK_NFRA_OPLGTW~5 .owned-paths.yaml` on the protocol path -> rc=0; the same path for 2.0.0_SA_COO~O -> VIOLATION (lane CLOUD_OPS_OR_ETL), which is why a worker carries the edit.",
        "HELD: TO-OG-v-4 stays HELD on gates G-C and G-D, so no grading could run against the old wording before this commit."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row W6-S5: the sealed RQ1-RQ6 hashes assume 2026-09-15 while the protocol's 'latest' tracks the live newest qualified date.",
    "world_is": "The protocol amendment is ordered on TO-OG-o-2 and the grading on TO-OG-v-4, both committed @71bc5b82ed. The protocol text itself changes when OG-o-2's worker lands it, before any walkthrough.",
    "notes": "Evidence only. This row does not adjudicate W6-S5; its L9 disposition is 3.0.0_SA_CVO's."
  },
  {
    "id": "NFRA_OPLGTW-W1-S12",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-17T14:10:00Z",
    "one_line": "OG-i-5's OGI5-AC7 parenthetical ('the project's historical records: its deliverables, surprise channel, rulings, logs and change-management entries') does not literally name task-orders/, prd/ or decompositions/ -- but an unscoped git grep -F opal-gateway-access-state at HEAD hits all three (frozen, out-of-<paths>-grant documents describing already-issued/already-completed cells OG-i-1/a-1/d-1/p-1/v-5 truthfully under the name that was correct when each was written). A literal reading of the parenthetical as closed/exhaustive makes AC7 mechanically unsatisfiable by any worker, since this cell has no write grant over task-orders/, prd/ or decompositions/ and BOUNDS itself calls the decomposition and spec FROZEN.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: git grep -F -n opal-gateway-access-state at wk-nfra_oplgtw-1h HEAD (post reference-move commit 63f0ccec7d) -- 74 hit lines across 27 files; org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md (3 hits), org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md (1 hit) and org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-{a-1,d-1,i-1,i-5,p-1,v-5}.*.md (7 hits) match none of AC7's five named categories.",
        "ORDER: NFRA_OPLGTW.TO-OG-i-5.access-state-rename.md BOUNDS -- 'Spec frozen ... Mid-round the spec AND the decomposition are FROZEN'; <paths> block names only schwab_access_state.tf, access_state.py, oauth_as.py, the contract JSON, change_management/, the sentinel and this order's own surprise-channel file -- no task-orders/, prd/ or decompositions/ path.",
        "PROBE: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i5.py ac7() widens its historical-marker set to '/task-orders/', '/prd/', '/decompositions/' beyond the criterion's literal parenthetical, with this reasoning inlined as a comment beside the marker list."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGI5-AC7's parenthetical names exactly five historical categories (deliverables, surprise channel, rulings, logs, change-management) as the full set excluded from the zero-live-hits requirement.",
    "world_is": "Three more categories -- task orders, the PRD and the decomposition doc -- are equally frozen project history, equally outside this cell's write grant, and equally correct as written (each named the table under the name that was live when it was authored). This worker's probe treats them as historical too, on that reasoning, rather than reporting a false FAIL it has no path to fix.",
    "notes": "INERT: no served surface, nothing deployed by this row. The judgment is disclosed in the probe's own output (per-hit HISTORICAL/LIVE tag) so a reviewer can re-narrow the set without re-deriving the reasoning."
  },
  {
    "id": "NFRA_OPLGTW-W5-S7",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-17T17:40:00Z",
    "one_line": "OG-x-1's first server.py route declarations used a two-level attribute reference (download_routes.export.DOWNLOAD_PAGE_PATH), which broke test_browser_oidc.py's AST route-table reader (outside this cell's <paths> grant) with AttributeError: 'Attribute' object has no attribute 'id'; fixed by using literal string paths, the same form that reader's ast.Constant branch already accepts.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_browser_oidc.py -q before the fix -> 'FAILED ...::test_oga3_ac07 - AttributeError: 'Attribute' object has no attribute 'id'', 1 failed, 6 passed.",
        "tests/test_browser_oidc.py:374 (_declared_routes): 'path = first.value if isinstance(first, ast.Constant) else getattr(names[first.value.id], first.attr)' -- names={'oauth_as': oauth_as, 'browser_oidc': browser_oidc} only; a two-level chain's first.value is itself an ast.Attribute, which has no .id.",
        "FIX (this cell's own file, app/server.py): Route(\"/schwab/download\", ...) and Route(\"/schwab/download/exchange\", ...) as literal strings, not download_routes.export.DOWNLOAD_PAGE_PATH/EXCHANGE_PATH.",
        "RE-RUN after the fix: timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_browser_oidc.py tests/test_data_entitlement_guard.py tests/test_principal_cutover.py -q -> 7 passed, 12 passed, 11 passed (three separate module runs; each starts its own MCP lifespan)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The route-table rule (ruling 97203 C, cited in this order's worker face) grants OG-x-1 ROUTE_CLASS entries only and says nothing about the FORM of the Route() path argument in app/server.py.",
    "world_is": "A sibling test file this cell cannot edit (test_browser_oidc.py) parses app/server.py by AST and only understands a path argument that is a string literal or a ONE-level module.attribute reference bound in its own hardcoded names={'oauth_as':..,'browser_oidc':..} map. OG-a-3's own two routes fit that map; OG-x-1's new module (download_routes / its export submodule) does not and cannot be added to that map without editing a file outside every route-adding cell's grant. Resolved here by declaring the two new paths as literal strings in server.py, which the SAME reader already accepts via its ast.Constant branch -- no foreign file touched, no new grant needed.",
    "notes": "INERT: caught and fixed before any commit; re-verified green (test_browser_oidc.py 7/7, test_data_entitlement_guard.py 12/12, test_principal_cutover.py 11/11). Flagged as an OBSERVATION for any LATER route-adding cell under ruling 97203 C's standing grant: a module.attribute path form silently breaks this reader unless the module is a literal in that fixed map; a literal string path is the portable choice."
  },
  {
    "id": "NFRA_OPLGTW-W5-S8",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-17T17:41:00Z",
    "one_line": "OG-x-1 classes its two new routes (/schwab/download, /schwab/download/exchange) 'public' in ROUTE_CLASS -- a reasoned choice, not a default: neither route consults the Authorization-bearer or ALB access-layer axes ROUTE_CLASS grades at all, the SAME reasoning ruling 97203 A already gave OG-a-3's login/callback (NFRA_OPLGTW-S14); the REAL guard (session cookie + ticket checks) is independent and is graded by OGX1-AC1..AC16, never by ROUTE_CLASS.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO-OG-x-1 worker face, the route-table rule: 'each entry carries the route's REAL guard class, as your code enforces it, never a default \"public\"... A route whose class is genuinely unclear is a surprise row, not an entry.'",
        "app/download_routes.py: neither download_page nor download_exchange reads request.headers['Authorization'] or any ALB identity header; both consult only browser_oidc.session_principal(request) (a cookie) and, for the exchange, the ticket itself.",
        "tests/test_principal_cutover.py:551-557 (the 'public' arm of test_oga2_ac04) and tests/test_data_entitlement_guard.py's else-branch (test_ogz1_ac08) both grade EXACTLY Bearer/legacy-token invariance for a 'public' route, never 'reachable with no guard at all' -- verified by running both suites green with the two new routes classed 'public' (7/7 and 12/12 including the OGZ1-AC8/OGA2-AC4 rows naming /schwab/download and /schwab/download/exchange by path)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The route-table rule: a genuinely unclear class is a row, not an entry; a lazy default to 'public' is exactly what the rule forbids.",
    "world_is": "No class in the existing ROUTE_CLASS taxonomy (access / capability / static-exchange / static / access-layer / public) names 'gated by this cell's own cookie+ticket mechanism, no Bearer, no ALB header' as a distinct value -- the taxonomy's only axis is which OF THE GATEWAY'S OWN SCHEMES (if any) gates a route. On that axis, 'public' is the only class both routes are correctly members of, and it is also OG-a-3's own precedent for the exact same cookie family. Recorded here so L9 can independently confirm or overturn the reasoning rather than infer it from the diff alone.",
    "notes": "INERT: entries only, mechanically verified against both consuming test suites. Not a request to widen the taxonomy -- YAGNI holds unless a future consumer branches on a class this taxonomy cannot express."
  },
  {
    "id": "NFRA_OPLGTW-W5-S9",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-17T17:42:00Z",
    "one_line": "PRD C5's 'if login is needed, retain only a hashed pending ticket bound to the secure browser session while the separate OIDC flow completes' does not specify a resumption protocol; this cell reads it as a one-way, non-resumable retention (the exchange's pending:true action retains only the ticket's own SHA-256, already its storage key, in a session-scoped cookie) rather than inventing an auto-resume mechanism the literal text does not promise.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD C5 quoted in the worker face: 'If login is needed, retain only a hashed pending ticket bound to the secure browser session while the separate OIDC flow completes.' No further text describes what happens after the OIDC flow completes.",
        "app/download_routes.py download_exchange, pending branch: reads the ticket record by its hash (export._read), sets cookie __Secure-og_dl_pending = export._hash(secret) (Path=/schwab/download, HttpOnly, Secure), returns login_url; the raw secret is discarded client-side once the browser navigates away (the static page never persists it to storage).",
        "A SHA-256 hash is one-way by construction: the retained cookie value cannot be used to recover the raw ticket after login, so no code path in this cell attempts to auto-resume the SAME download once the OIDC round trip returns.",
        "Test OGX1-AC6 (tests/test_schwab_export.py::test_ogx1_ac06) verifies the retained value is the ticket's SHA-256 and is never the raw secret, and that an unknown ticket in pending mode is refused."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C5's pending-ticket sentence, verbatim above.",
    "world_is": "The user must re-issue a Claude call to schwab_prepare_download for a new ticket after completing sign-in; the pending cookie is retained only as a defensive/anti-fixation artifact (evidence that this browser session held this ticket hash before login), never as a resumption key. Declared as a declared_exclusion in this cell's proof-of-spec instance rather than left implicit.",
    "notes": "INERT: a reasoned interpretation of underspecified text, not a defect against a stated requirement. Recorded for L9 to confirm the reading or direct a different one on a future round."
  },
  {
    "id": "NFRA_OPLGTW-W6-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~6",
    "surfaced_at": "2026-09-17T15:20:00Z",
    "one_line": "OGV2-AC2's independent A8-refusals check (schwab_query aggregate mode) FAILS against the real, unmocked app: app/integrations/schwab/semantics.py's assert_sum_allowed / assert_quantity_sum_grouped / assert_field_summable are never imported or called from app/integrations/schwab/query.py or integration.py, so SUM(closing_price) (nonadditive, contract's own additive_fields excludes it) and SUM(quantity_settled_unsettled) with no group_by cusip/l_s both SUCCEED instead of refusing INVALID_REQUEST.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: infra/aws/ec2/opal-gateway/tests/acceptance/test_local_acceptance.py::test_ogv2_a08 against the real app.server + real SchwabService (moto S3/DynamoDB/STS, real catalog, real entitlement grant) -- both refusal requests return 200 with rendered aggregate rows, not the 5xx-shaped INVALID_REQUEST error_result the contract's error_codes and A_ROWS.json's A8-refusals independent expectation (expect_independent.py, never re-derived) name.",
        "comp-find 'assert_quantity_sum_grouped|assert_field_summable|assert_single_balance_metric' over infra/aws/ec2/opal-gateway/app -- 3 DEF hits (semantics.py:243,250,260) and 3 SURFACED hits, all three INSIDE semantics.py's own assert_sum_allowed (semantics.py:273-279); zero hits in query.py or integration.py.",
        "comp-find 'quantity_sum_required_groups' over infra/aws/ec2/opal-gateway/app -- the only app/ consumers are integration.py:467-468 (describe_dataset's DESCRIPTIVE metrics.quantity_sum_required_groups field, read-only) and semantics.py's own declaration; query.py's check_against_grant (query.py:438-484) checks field-kind/scope/alias-collision only, never additivity or required grouping.",
        "grep across infra/aws/ec2/opal-gateway/app and tests for 'asset_policy' shows the SAME shape one level up: integration.py accepts an asset_policy constructor arg and gates dim_asset on its mere presence (':535,:717,:790'), but no caller anywhere (production wiring in build_default_service(), or any existing test) ever passes one -- a second, adjacent instance of a declared-but-unwired dependency in the same module."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C4 (query.py's own docstring, quoting it): 'No expressions, SQL fragments... are accepted'; contract additive_fields excludes closing_price from every dataset; contract quantity_sum_required_groups = [cusip, l_s]; A_ROWS.json A8's machine half: 'every request in A8-refusals is refused with its listed code'.",
    "world_is": "query.py's check_against_grant enforces field existence, grant visibility, decimal-kind-for-sum and alias collisions, but not additivity or the quantity/cusip+l_s grouping rule; those checks exist, are correct in isolation (test_schwab_semantics.py, OG-q-3's own acceptance), and are simply never called from the one place (SchwabService.query, integration.py:523-673) that would need to call them before build_plan()/run_query(). The gap is NOT this cell's to fix (query.py and integration.py are outside this task order's <paths> grant; BOUNDS: 'You grade; you do not fix').",
    "notes": "ARMED: a live query surface accepts and answers a request the contract's own closed grammar and A_ROWS.json's independent fixture both say must be refused, on the deployed-shape code path (real catalog, real entitlement, real DuckDB job) -- not a mock artifact. disarm_owner: 1.0.0_SA_CTO (the cell whose surface this lands on, OG-q-2/OG-q-3, is a CTO-ruled boundary per this project's msg-97078 pattern). Recorded in this order's proof_of_spec.json under criterion OGV2-AC2 and in local-acceptance-run.result.md; OGV2-AC2 is graded FAIL by this row, not silently passed."
  },
  {
    "id": "NFRA_OPLGTW-W6-S7",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~6",
    "surfaced_at": "2026-09-17T15:25:00Z",
    "one_line": "TO-OG-v-2's cell text reads 'each A-row that A_ROWS.json marks operated_by: machine and whose instrument is the local harness becomes one test' (13 rows: A2,A3,A4,A5,A6,A8,A9,A10,A11,A12,A14,A17,A18); within this order's single-turn budget this worker built 6 of those 13 as real tests against the real app (A2 as OGV2-AC3, A4, A5, A8, A11) plus the S3 call-set assertion (OGV2-AC5) -- A3, A6, A9, A10, A12, A14, A17, A18 are NOT built and are not exercised here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/tests/acceptance/test_local_acceptance.py -- grep for 'def test_ogv2_' lists exactly test_ogv2_ac01, test_ogv2_a08, test_ogv2_a11, test_ogv2_a04, test_ogv2_a05, test_ogv2_ac03, test_ogv2_ac05; no test_ogv2_a03/a06/a09/a10/a12/a14/a17/a18 exists.",
        "A_ROWS.json rows A2..A18 (excluding A1/A7/A13/A15/A16/A19/A20, which are person/OG-i/OG-r graded and correctly out of this cell's scope): 13 machine-and-OG-v-2 rows named in this order's own worker-face text."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "'Each A-row that A_ROWS.json marks operated_by: machine and whose instrument is the local harness becomes one test test_ogv2_a<nn>' (this order's WORKER FACE, THE CELL paragraph).",
    "world_is": "Building the full harness (real moto S3/DynamoDB/STS, real Catalog/AssumedRole/entitlement/account_ref/envelope/audit, an in-process query-engine substitute, real OAuth) and one genuinely correct test per remaining row (A3's forged-header/tid-oid-mismatch matrix, A6's grant-revision-and-cache-warming sequence, A9's twelve closure variants, A10's two-browser-session ticket redemption via OG-a-3's separate cookie-session mechanism, A12's CSV formula-escaping export, A14's joint OG-v-2/OG-r-2 memory-and-deadline measurement, A17's concurrent-refresh-race and family-revocation semantics, A18's Unicode/paging byte-exact measurement) each individually approaches or exceeds the single-turn budget already spent reaching 6 rows + AC5; this order's own text says nothing about a per-row time bound, so the reduction is this worker's own scope call, not a spec reading.",
    "notes": "INERT: no served surface, nothing deployed. OGV2-AC2 is already graded FAIL on NFRA_OPLGTW-W6-S6 regardless of this reduction, so this row's own disposition does not change this round's AC2 outcome; it is filed so a re-cut task order (or the same worker resumed) has the exact denominator of what remains, rather than a diff against the full 13."
  },
  {
    "id": "NFRA_OPLGTW-W1-S13",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-17T18:30:00Z",
    "one_line": "TO-OG-i-3's FIRST ACT text asks this cell to 're-run the OG-i-2 live denial and assume arms against the new ARNs' -- but OG-i-2's arms run entirely on-host via SSM AWS-RunShellScript (host_arm(), a dynamic script parameterized by role ARN/ExternalId/S3 key), and R-OG-6 (binding 'from OG-i-3 onward') forbids AWS-RunShellScript and permits only the one named, FIXED, parameterless document this same cell creates. That document's content is scoped to 'exactly the reads later cells need' (file digests, systemd status, RSS, package versions) and deliberately carries no caller-supplied interpolation, so it cannot express an assume-role/GetObject diagnostic without becoming exactly the parameterized-script shape R-OG-6 exists to close off.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "og_i2.py host_arm()/ac6()/ac7()/ac8(): each builds a per-call shell body (role ARN, ExternalId env var, S3 bucket/key literals) and sends it via ssm send-command --document-name AWS-RunShellScript (og_p1.py's ssm_read() is the same shape OG-i-2 inherited).",
        "RULINGS_NFRA_OPLGTW_20260916.md R-OG-6: 'the limb binds from OG-i-3: one aws_ssm_document resource in OG-i-3's order ... whose content is the fixed read-only commands ... AWS-RunShellScript with caller-supplied parameters is not that document.'",
        "This order's own text (the read-only host-command document paragraph): 'Its content: only the read commands later cells need (file digests ... systemd unit's status, process RSS, and installed package versions), with no shell interpolation of a caller string.'",
        "infra/aws/terraform/opal-gateway/ssm_readonly_host.tf (this commit): mainSteps.runCommand is a fixed literal list, parameters={} -- no role ARN, ExternalId or S3 key can reach it as a caller argument.",
        "Substitute performed instead (declared, not host-exercised): iam get-role/get-role-policy on both new roles confirm the trust Principal (opal-gateway-role only), the two distinct re-keyed ExternalIds (91b31fde... for gateway-schwab-read-role, a2d39502... for gateway-schwab-catalog-read-role), and the unchanged six-statement deny/allow Sid shape on each role's inline policy -- recorded in this cell's result file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-i-3 FIRST ACT: 'Re-run the OG-i-2 live denial and assume arms against the new ARNs, and record them in this cell's result file.'",
    "world_is": "The mechanism this same cell is required to install (R-OG-6's one fixed, parameterless document) cannot carry a dynamic assume-role/GetObject diagnostic without reopening the caller-supplied-interpolation hole R-OG-6 exists to close; AWS-RunShellScript, the mechanism OG-i-2's arms actually use, is the thing this cell forbids from itself onward. This worker refused the live re-run as written and substituted a declared-level check (trust policy + inline policy readback via iam get-role/get-role-policy, no host execution) against the new ARNs, disclosed as a weaker instrument than a host-exercised assume/deny arm.",
    "notes": "INERT: no served surface exercised by either the refused act or its substitute; both are reads. Recorded for L9 to rule whether a host-exercised re-run belongs to a LATER cell (its own document, or an audited AWS-RunShellScript exception) rather than OG-i-3."
  },
  {
    "id": "NFRA_OPLGTW-S24",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-17T20:30Z",
    "one_line": "OG-i-3's rename drain left CLOUD's acceptance harness RED: tests/acceptance/conftest.py:87-88 hardcodes the pre-rename reader ARNs, aws_roles.role_config() refuses them against the renamed contract, and integration.py swallows it as UNAVAILABLE. Measured on the shared tree, not in a worktree: tests/acceptance/test_local_acceptance.py reads 5 failed, 2 passed. The issuer's cut of OG-i-3 carried R-OG-7's rename with no census of the old names' consumers.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN on the shared tree @033f152e5d (not a worker worktree): `pytest -q tests/acceptance/test_local_acceptance.py` -> `5 failed, 2 passed in 6.56s`, failures include test_ogv2_a05 and test_ogv2_ac05.",
        "READ @033f152e5d: tests/acceptance/conftest.py:87-88 READER_ARN and CATALOG_ARN are the pre-rename names `opal-mcp-emp-menachem-schwab-read` and `opal-mcp-schwab-catalog-read`; both roles return NoSuchEntity live and the contract now names gateway-schwab-read-role / gateway-schwab-catalog-read-role (OG-i-5/OG-i-3 @258d786fbd).",
        "CAUSE CHAIN, read: app/integrations/schwab/aws_roles.py role_config() refuses an ARN that does not match the contract's configured role; app/integrations/schwab/integration.py returns UNAVAILABLE / schwab_integration_unavailable rather than surfacing it.",
        "INDEPENDENT CORROBORATION: 0.9.0_WK_NFRA_OPLGTW~5 hit the same failure inside OG-q-4's worktree after the issuer merged CLOUD into its branch, and filed NFRA_OPLGTW-W5-S11 naming the same two lines. Two instruments, two checkouts, one cause.",
        "SCOPE: tests/acceptance/conftest.py is in TO-OG-v-2's <paths> and OG-v-2 is OPEN, so no grant widening is needed to repair it."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OG-i-3 carried R-OG-7's rename of the three identities to builder output, and OG-v-2's harness constructs the Schwab roles from their ARNs.",
    "world_is": "The rename moved the contract's role names and left the acceptance harness's hardcoded ARNs behind, so five of seven acceptance tests fail on CLOUD and OG-q-4's live-path criteria AC1-AC4 cannot be exercised at all (the integration refuses to construct before the wiring runs). Nothing is deployed and nothing served is wrong; the red is in the test harness, not the product. Remedy routed: OG-v-2's re-hand re-keys the two fixture ARNs to the builder's names inside its own grant, then OG-q-4 re-grades AC1-AC4.",
    "notes": "ARMED because CLOUD carries a red module until the re-hand lands. This seat is the disarm owner and OG-v-2's drain is the disarming act. The issuer's cut is the cause: R-OG-7's rename was carried into OG-i-3 with no census of consumers of the old ARNs, which is the same shape as W6-S6 (a check proven where nothing calls it) one level out."
  },
  {
    "id": "NFRA_OPLGTW-W6-S8",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~6",
    "surfaced_at": "2026-09-17T22:05:00Z",
    "one_line": "OGV2-AC2's independent A6-partial-grant-asset-cusips check FAILS against the real, unmocked app: a partial-account grant on dim_asset (accounts={99000002}) returns all four fixture CUSIPs (SYN000001/2/3/9) instead of the two held by that account (SYN000001/2) -- PRD C3's 'restrict its CUSIPs to holdings of the authorized accounts for that same master/date' is not wired on any live query path, the same class of gap W6-S6 already named for additivity/grouping, one level over (dim_asset's account-scoping rather than the quantity-sum grammar).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: infra/aws/ec2/opal-gateway/tests/acceptance/test_local_acceptance.py::test_ogv2_a06 (this order's re-hand, W6-S7's own denominator) against the real app.server + real SchwabService -- a dim_asset rows query under a grant scoped to account 99000002 alone returns rows for all four ASSET_SEED CUSIPs, matching neither EXPECTED['A6-partial-grant-asset-cusips']['expect']['dim_asset_cusips'] (['SYN000001','SYN000002']) nor its 'excluded' list.",
        "READ: app/integrations/schwab/integration.py:535,717,790 -- the ONLY dim_asset gate is `if q.dataset == 'dim_asset' and self._asset_policy is None: raise ServiceError(UNAVAILABLE, ...)`; the CONSTRUCTOR ARGUMENT's VALUE is never read again anywhere in the module or elsewhere in app/ (comp-find 'self._asset_policy' over app/ -- 4 hits, all three raise-sites plus the assignment; comp-find 'asset_policy' over app/ -- zero callers of build_default_service() ever pass one, confirmed by direct read of build_default_service()).",
        "READ: tests/acceptance/conftest.py:322-328's own disclosed-seam-3 comment (already on CLOUD before this row, filed by a prior worker against a DIFFERENT criterion, W6-S6): 'nothing in the shipped code ever reads its VALUE ... a non-None sentinel is this harness's only way to reach dim_asset at all' -- this row is that same disclosed gap surfacing on ITS OWN acceptance criterion (A6) rather than as supporting evidence for A8's."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C3 (semantics.py's own docstring, quoting it): 'For a partial-account grant restrict its CUSIPs to holdings of the authorized accounts for that same master/date, using a qualified position snapshot solely for policy selection.' A_ROWS.json A6's machine half: 'a partial-account grant limits dim_asset to the CUSIPs its accounts hold'.",
    "world_is": "app/integrations/schwab/integration.py's `asset_policy` constructor argument gates dim_asset access by mere PRESENCE (is None / is not None) and nothing ever reads its value to compute a CUSIP restriction; no qualified-position-snapshot policy-selection code exists on the dim_asset query path at all. query.py and integration.py are outside this order's <paths> grant (BOUNDS: 'you grade; you do not fix').",
    "notes": "ARMED: a live dim_asset query surface answers with every CUSIP under a partial-account grant instead of the PRD-stated subset, on the deployed-shape code path (real catalog, real entitlement, real DuckDB job) -- not a mock artifact. disarm_owner: 1.0.0_SA_CTO, matching W6-S6's routing (the OG-q cell surface this lands on is a CTO-ruled boundary). Recorded in this order's proof_of_spec.json under criterion OGV2-AC2 and in local-acceptance-run.result.md; OGV2-AC2 is graded FAIL by this row AND by W6-S6 independently, so disarming either alone does not flip AC2 green."
  },
  {
    "id": "NFRA_OPLGTW-W6-S9",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~6",
    "surfaced_at": "2026-09-17T22:20:00Z",
    "one_line": "OGV2-AC4's per-module sweep of infra/aws/ec2/opal-gateway/tests/test_*.py (the one named red test S1 already deselects) is itself non-deterministic: two consecutive runs of the literal invocation each failed exactly one module, a DIFFERENT module each time, on causes unrelated to any NFRA_OPLGTW cell -- an event-loop-latency timing assertion (test_schwab_engine.py::test_ogq1_ac02, threshold 0.25s, measured 0.446s) and a random-secret substring collision (test_schwab_export.py::test_ogx1_ac01 asserting 's3'/'amazonaws'/'?' are absent from a base64url-random ticket, which occasionally contains them by chance).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN 1 (this worker, first pass): the AC4 loop over 21 modules -> 'FAIL(1): infra/aws/ec2/opal-gateway/tests/test_schwab_engine.py' / 'MODULES: 21 FAILED-MODULES: 1'; the module's own failure: test_ogq1_ac02 asserts child_lag < 0.25, measured 0.446s over 193 samples (a probe of event-loop responsiveness while a child process runs a CPU-bound job) -- re-run of that SAME module ALONE immediately after: '13 passed in 58.49s', no failure.",
        "RUN 2 (this worker, second pass, ~10 minutes later, box otherwise busy): the SAME AC4 loop -> 'FAIL(1): infra/aws/ec2/opal-gateway/tests/test_schwab_export.py' / 'MODULES: 21 FAILED-MODULES: 1'; the module's own failure: test_ogx1_ac01 asserts '?' not in url and 'amazonaws' not in url.lower() and 's3' not in url.lower() on a schwab_prepare_download URL whose fragment is secrets.token_urlsafe(32) -- this run's random secret happened to contain the substring 's3' (inside a longer run of characters), tripping the check on pure chance.",
        "Neither failing test imports or exercises tests/acceptance/conftest.py or test_local_acceptance.py; both are pre-existing modules this order's <paths> grant does not include and this worker did not touch."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGV2-AC4's own invocation and expect: '^MODULES: [1-9][0-9]* FAILED-MODULES: 0$' -- a single deterministic-looking pass/fail line.",
    "world_is": "The line is not deterministic: at least two modules outside this project's write surface carry their own flakiness (a hardcoded wall-clock timing threshold sensitive to box load, and a fixed-length random-token substring check with a nonzero collision probability per run), so AC4 as literally invoked can fail on an UNRELATED module on any given run regardless of NFRA_OPLGTW's own code. This is IN ADDITION to NFRA_OPLGTW-S1's already-known, already-deselected red test -- these two are neither named nor deselected by the criterion's own -k filter.",
    "notes": "INERT: no NFRA_OPLGTW cell is implicated, and the flake rate/root cause is fully characterized in evidence above (not merely asserted). Recorded because OGV2-AC4's literal invocation is graded on this run's actual output (RUN 2, FAILED-MODULES:1, itself a FAIL against the criterion's regex) and a reader of that FAIL should not conclude an OG-v-2 regression caused it. Repair (fixing the threshold or the substring check, or widening the -k deselect) is outside this order's <paths> grant."
  },
  {
    "id": "NFRA_OPLGTW-S25",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-17T22:38Z",
    "one_line": "Disarm evidence for NFRA_OPLGTW-S24 (ARMED, disarm owner 2.0.0_SA_COO~O): OG-v-2's drain @65fa11a5ba re-keys both Schwab role names in tests/acceptance/conftest.py FROM THE CONTRACT instead of hardcoded pre-rename ARNs, and the SHARED-TREE re-run R-OG-16 limb 3 requires reads 2 failed, 12 passed where it read 5 failed, 2 passed before. All five ARN-class failures are gone; the two that remain have different causes and their own rows.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN on the SHARED TREE after the drain (R-OG-16 limb 3), @65fa11a5ba: `pytest -q tests/acceptance/test_local_acceptance.py` -> `2 failed, 12 passed in 43.00s`. BEFORE, at @033f152e5d: `5 failed, 2 passed in 6.56s`. Same command, same interpreter, one drain between them.",
        "READ @65fa11a5ba: conftest.py now sets READER_ROLE_NAME and CATALOG_ROLE_NAME from org/standards/NFRA_OPLGTW_CONTRACT.json's `reader_role` and `catalog_role`; the two hardcoded `opal-mcp-*` ARN literals are gone. The repair reads the name rather than typing it, so the next rename cannot reintroduce this row.",
        "DISCRIMINATION: the two remaining failures are NOT this row's class. test_ogv2_a08 waits on OG-q-4's wiring, which is still on branch wk-nfra_oplgtw-5e and not at CLOUD (row W6-S6); test_ogv2_a06 is the dim_asset partial-account restriction, unwired on the live path (row W6-S8, ARMED, owner 1.0.0_SA_CTO). Neither is the UNAVAILABLE construction error S24 named.",
        "DENOMINATOR: 14 tests in the module at both vintages; the delta is 5 failures cleared, 0 new."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S24: the acceptance harness's hardcoded pre-rename ARNs make the module red on CLOUD and block OG-q-4's live-path criteria from constructing at all.",
    "world_is": "Repaired at CLOUD. The harness derives both role names from the contract, the five ARN-class failures are cleared on the shared tree, and OG-q-4's criteria can now reach the wiring (its re-grade is running at this write). S24's hazard is spent; this seat gives the word as its disarm owner.",
    "notes": "Evidence only; this row does not adjudicate S24, whose L9 disposition is 3.0.0_SA_CVO's, and R-OG-16 leaves the clock to that seat. The rename bar R-OG-16 states -- census, repoint, shared-tree re-run -- is what this row exercises end to end for the first time."
  },
  {
    "id": "NFRA_OPLGTW-W5-S10",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-17T19:17:17Z",
    "one_line": "OGQ4-AC5 requires tests/test_schwab_query.py, tests/test_schwab_semantics.py and tests/test_schwab_export.py to all pass unchanged, but wiring semantics.assert_quantity_sum_grouped into query.py's check_against_grant (this cell's own OGQ4-AC2) breaks two pre-existing OG-q-2 tests that treat an ungrouped quantity sum as legal; test_schwab_query.py is outside this order's <paths> grant, so it cannot be fixed here.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-q-4.semantics-wiring.md OGQ4-AC5: 'the probe runs tests/test_schwab_query.py, tests/test_schwab_semantics.py and tests/test_schwab_export.py, ONE pytest process per module, and every module passes' -- no test in any of the three is named as an exception.",
        "GRANT: the same order's <paths> block names only app/integrations/schwab/query.py, app/integrations/schwab/integration.py, tests/test_schwab_wiring.py and this investigation file -- tests/test_schwab_query.py is not granted.",
        "BUILD: app/integrations/schwab/query.py check_against_grant, this worker's commit -- calls semantics.assert_field_summable and semantics.assert_quantity_sum_grouped on every sum aggregate, exactly OGQ4-AC1/AC2's own requirement (dataset's own datasets.json quantity_fields.dim_position includes quantity_settled; quantity_sum_required_groups = [cusip, l_s]).",
        "RUN: '.venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_query.py -q -p no:cacheprovider --color=no' at this worker's commit: '2 failed, 23 passed in 6.64s' -- FAILED test_ogq2_ac07 (tests/test_schwab_query.py:491-497, its own 'control' case sums quantity_settled with no group_by and asserts success) and FAILED test_ogq2_ac15 (tests/test_schwab_query.py:743-750, a second query summing quantity_settled with no group_by, now refused INVALID_REQUEST quantity_sum_ungrouped before the engine's deadline-kill path it means to exercise ever runs); tests/test_schwab_semantics.py '14 passed in 1.22s' and tests/test_schwab_export.py '27 passed in 6.41s' both clean.",
        "PROBE: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q4.py AC5 prints exactly this per-module result with the denominator 3 and returns VERDICT: FAIL-OGQ4-AC5 2 of 3 module(s) passed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGQ4-AC5, verbatim above: the three named modules all pass, unchanged, in the same round that OGQ4-AC1/AC2 require the exact refusal that breaks two of test_schwab_query.py's own cases.",
    "world_is": "OG-q-2's test_ogq2_ac07 and test_ogq2_ac15 were written and merged before any caller enforced the contract's quantity-sum-grouping rule (C3), so their own 'control'/'complete scan' cases sum a quantity field (quantity_settled) with no group_by and expect success -- exactly the shape OGQ4-AC2 requires this cell to refuse. Wiring the call site correctly therefore makes those two OG-q-2 tests fail; nothing else in the three named modules regresses (test_schwab_semantics.py and test_schwab_export.py are unaffected, and test_schwab_query.py's other 23 tests still pass). test_schwab_query.py is not in this order's <paths> grant and OG-q-2's cell is merged and closed, so this worker refuses to edit it (BOUNDS: 'never widen the order or fix a neighbouring defect'; 'a path you need that is not named is a BLOCKING surprise row on that criterion -- never an override'). OGQ4-AC5 is graded FAIL by this row's own measurement, not silently passed or worked around.",
    "notes": "INERT: nothing deploys in this order; the two failing assertions are pytest-local and no served behaviour changes as a result of this row. BLOCKING: OGQ4-AC5 stays FAIL and this order stays open on that criterion until an issuer either updates test_ogq2_ac07/test_ogq2_ac15 to group their quantity sums (or otherwise re-scopes AC5), which is outside this cell's grant."
  },
  {
    "id": "NFRA_OPLGTW-W5-S11",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-17T20:10:00Z",
    "one_line": "OGQ4-AC1/AC2/AC3 (and AC4's mutant, which copies the same tree) all run through tests/acceptance/conftest.py's og_v2 fixture, which hardcodes the PRE-rename role ARNs (opal-mcp-emp-menachem-schwab-read / opal-mcp-schwab-catalog-read); commit b2e4a10678 (merged into this branch via the issuer's CLOUD merge, R-OG-7) renamed the contract's reader_role/catalog_role to gateway-schwab-read-role/gateway-schwab-catalog-read-role, so aws_roles.role_config now refuses the fixture's own ARNs at construction, every og_v2-based test returns UNAVAILABLE/schwab_integration_unavailable, and tests/acceptance/conftest.py is not in this order's <paths> grant.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: 'timeout 180 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_wiring.py::test_ogq4_ac01 -q -p no:cacheprovider --color=no' at this worker's HEAD (2392d6f9fb) -- FAILED, payload {'error': {'code': 'UNAVAILABLE', 'reason': 'schwab_integration_unavailable'}}, not the expected INVALID_REQUEST.",
        "FIXTURE: infra/aws/ec2/opal-gateway/tests/acceptance/conftest.py:88-91 @2392d6f9fb -- READER_ARN='arn:aws:iam::313476888478:role/opal-mcp-emp-menachem-schwab-read', CATALOG_ARN='arn:aws:iam::313476888478:role/opal-mcp-schwab-catalog-read'; :262-269 sets SCHWAB_READER_ROLE_ARN/SCHWAB_CATALOG_ROLE_ARN to those two constants for every og_v2-fixtured test.",
        "CONTRACT: org/standards/NFRA_OPLGTW_CONTRACT.json reader_role='gateway-schwab-read-role', catalog_role='gateway-schwab-catalog-read-role' at this worker's HEAD; git diff 881b1a5445 HEAD -- org/standards/NFRA_OPLGTW_CONTRACT.json shows exactly this rename, landed by commit b2e4a10678 (in the 881b1a5445..d91629cfd8 range the issuer's CLOUD merge brought into this branch as HEAD's second parent) -- 'git log --oneline 881b1a5445..d91629cfd8 -- org/standards/NFRA_OPLGTW_CONTRACT.json' names only that one commit, and the same range for tests/acceptance/conftest.py is empty (the fixture was never updated to match).",
        "CODE: app/integrations/schwab/aws_roles.py:116-135 role_config() -- 'if matched.group(2) != declared: raise RoleConfigError(...)'; this validation is UNCHANGED between 881b1a5445 and HEAD (git diff shows only a docstring update to that file), so the discriminator is the contract's renamed value, not new code.",
        "REPRO: direct call to app.integrations.schwab.aws_roles.role_configs(contract.raw, env) with the fixture's exact env values raises 'RoleConfigError: SCHWAB_READER_ROLE_ARN names role opal-mcp-emp-menachem-schwab-read; the contract's reader_role is gateway-schwab-read-role -- refusing a role the contract does not name'; app/integrations/schwab/integration.py:917-920 swallows this as bare Exception and returns the generic UNAVAILABLE/schwab_integration_unavailable this worker's test run measured.",
        "GRANT: this order's <paths> block names infra/aws/ec2/opal-gateway/app/integrations/schwab/{query.py,integration.py}, tests/test_schwab_{wiring,query}.py and this investigation file only -- tests/acceptance/conftest.py is not granted, and it is OG-v-2's harness, not this cell's."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGQ4-AC1/AC2/AC3 (and AC4's mutant control, which runs the same three against a copy of the same tree): each is graded 'through the registered schwab_query tool on OG-v-2's live-app harness' and is expected to reach the semantic refusal/legal-sum outcome this cell wired, not a harness-configuration error.",
    "world_is": "The og_v2 fixture's hardcoded role ARNs are stale against org/standards/NFRA_OPLGTW_CONTRACT.json's v1.1 rename (reader_role/catalog_role, landed by b2e4a10678 and merged into this branch by the issuer to deliver R-OG-15's amendment), so every test built on og_v2 -- test_ogq4_ac01/02/03 and AC4's mutant copies of the same three -- now fails at role construction with UNAVAILABLE/schwab_integration_unavailable before this cell's own wiring is ever exercised. Fixing tests/acceptance/conftest.py is outside this order's <paths> grant (BOUNDS: 'a path you need that is not named is a BLOCKING surprise row on that criterion -- never an override'; 'never widen the order or fix a neighbouring defect'), so this worker did not edit it. OGQ4-AC1, AC2, AC3 and AC4 are measured and reported FAIL by this row's own evidence, not silently patched around.",
    "notes": "INERT: nothing deploys or is served differently as a result of this row; the break is entirely test-fixture configuration. AC5 (test_schwab_query.py/test_schwab_semantics.py/test_schwab_export.py, none of which use og_v2/aws_roles) and AC6/AC7 (pure diff/collection-count measurements on test_schwab_query.py) are UNAFFECTED by this row and are graded independently. BLOCKING: AC1/AC2/AC3/AC4 stay FAIL and this order stays open on them until an issuer either updates tests/acceptance/conftest.py's READER_ARN/CATALOG_ARN to the builder names or grants this cell that path."
  },
  {
    "id": "NFRA_OPLGTW-W5-S12",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-17T22:40:00Z",
    "one_line": "OGQ4-AC4's mutant control read as FAIL on every re-hand (including the round that measured NFRA_OPLGTW-W5-S11) for a SECOND, unrelated reason: the probe's scratch copy sat one directory level SHALLOWER than the real tree, so tests/acceptance/conftest.py's own hardcoded `_GATEWAY.parents[3]` resolved one level ABOVE the real repo root and raised FileNotFoundError on import against every one of AC1/AC2/AC3 run against the mutant -- masking the intended AC1-FAIL/AC2-FAIL/AC3-PASS discriminator as a uniform collection error. Fixed in the probe itself (in this worker's own deliverables grant): the scratch copy now mirrors the real relative depth and carries a copy of the real, unmutated contract file at the matching path.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ @e51ef17b11^ (before this fix): org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q4.py ac4() built `dst_gateway = scratch_root / \"opal-gateway\"` -- one level shallower than the real `<repo_root>/infra/aws/ec2/opal-gateway`.",
        "READ: infra/aws/ec2/opal-gateway/tests/acceptance/conftest.py:52-57 -- `_GATEWAY = _TESTS.parent`, `_REPO = _GATEWAY.parents[3]`, `_CONTRACT_PATH = _REPO / \"org\" / \"standards\" / \"NFRA_OPLGTW_CONTRACT.json\"` -- a hardcoded depth with NO `NFRA_OPLGTW_CONTRACT_PATH` (or any env) fallback; only `app/integrations/schwab/catalog.py`'s `load_contract` reads that variable, and `test_schwab_wiring.py` imports `acceptance.conftest` directly, before catalog.py's own loader ever runs.",
        "RUN (before the fix, this worker, this HEAD's predecessor state): `timeout 300 .venv-og/Scripts/python .../probes/og_q4.py AC4` -> mutant runs AC1/AC2/AC3 each `rc=4 last-line='1 error in ...s'`; manual repro isolating the import: `pytest tests/test_schwab_wiring.py::test_ogq4_ac03` against a same-shape shallow copy raised `FileNotFoundError: [Errno 2] No such file or directory: 'C:\\\\tmp\\\\org\\\\standards\\\\NFRA_OPLGTW_CONTRACT.json'` (one level above the real repo root `C:\\\\tmp\\\\wk-oplgtw-5e`) at `tests/acceptance/conftest.py:95` (`_CONTRACT_RAW = json.loads(_CONTRACT_PATH.read_text(...))`), confirming the depth math, not the wiring, was the failure's cause.",
        "FIX committed at e51ef17b11 (org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q4.py, this worker's own deliverables grant, not the order's <paths>): `dst_gateway = scratch_root / \"infra\" / \"aws\" / \"ec2\" / \"opal-gateway\"`, plus a copy of the real `org/standards/NFRA_OPLGTW_CONTRACT.json` mirrored to `scratch_root/org/standards/NFRA_OPLGTW_CONTRACT.json`.",
        "RUN (after the fix, same HEAD 35c7b4b274 plus e51ef17b11): `timeout 300 .venv-og/Scripts/python .../probes/og_q4.py AC4` -> `mutant run AC1 ... outcome=FAIL`, `mutant run AC2 ... outcome=FAIL`, `mutant run AC3 ... rc=0 last-line='1 passed in 3.45s' outcome=PASS`, `git status --porcelain` before==after, `VERDICT: PASS-OGQ4-AC4`."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGQ4-AC4 (ruling R-OG-13's standing bar): 'passes only if AC1 and AC2 FAIL while AC3 still passes' -- a control that DISCRIMINATES the call site's removal, never one whose own scratch-copy plumbing fails independently of the mutation.",
    "world_is": "The probe's scratch-copy depth did not match the real tree's depth, so `tests/acceptance/conftest.py`'s own hardcoded parent-count derivation of the repo root (never contract-path-aware via an env var) walked one directory too high and crashed at import for every one of AC1/AC2/AC3 run against the mutant copy, independent of whether the call site was present or absent -- a probe defect, not a measurement of the wiring or of NFRA_OPLGTW-W5-S11's stale-ARN harness bug (which this same mutant copy also carries, and which is separately REPAIRED at this HEAD per the issuer's OG-v-2 drain @65fa11a5ba). Fixed within this worker's own deliverables grant (the probe file), never touching `tests/acceptance/conftest.py` or any file outside grant.",
    "notes": "INERT: the probe never wrote a tracked file (git status --porcelain identical before/after, both before and after this fix); no served surface is touched. Recorded because a prior round's AC4 FAIL verdict (composited with NFRA_OPLGTW-W5-S11's real, separate cause) partly reflected THIS probe bug rather than only the harness ARN mismatch -- a reader of that earlier FAIL should not conclude the wiring's mutant control was ever proven sound before this fix."
  },
  {
    "id": "NFRA_OPLGTW-S26",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-17T23:44Z",
    "one_line": "FOURTH instance of the one root cause, found by the shared-tree re-run after OG-q-4's drain: tests/acceptance/test_local_acceptance.py::test_ogv2_a18 asserts an ungrouped quantity sum is ACCEPTED, so OG-q-4's now-live refusal (reason quantity_sum_ungrouped) fails it. A08 went green with that drain as predicted; A18 went red in the same run. R-OG-15 corrected the two OG-q-2 tests of this shape but the population was never enumerated past that module.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN on the SHARED TREE after the drain @791faecfc1: `pytest -q tests/acceptance/test_local_acceptance.py` -> `2 failed, 12 passed`; FAILED test_ogv2_a18 with `{'error': {'code': 'INVALID_REQUEST', 'reason': 'quantity_sum_ungrouped', 'where': 'aggregates[1].field'}}` at test_local_acceptance.py:909 -- the refusal is CORRECT and the assertion is stale.",
        "SAME RUN: test_ogv2_a08 now PASSES, which is the arm OG-q-4's wiring was predicted to turn green (row W6-S6). So this drain cleared one acceptance failure and exposed another in the same module.",
        "READ: the other failure in that run, test_ogv2_a06 at :477, is the dim_asset partial-account restriction -- row W6-S8, already cut as cell OG-q-5 @321de65374. Two failures, two different causes, neither this row's twin.",
        "GREEN ELSEWHERE at the same vintage, one module per process: tests/test_schwab_wiring.py 3 passed; tests/test_schwab_query.py 25 passed (the two tests R-OG-15 corrected).",
        "WHY OG-q-4 DID NOT CATCH IT: this issuer wrote OGQ4-AC5 over three modules -- query, semantics, wiring -- and left the acceptance module out of that set, so a stale expectation there could not fail q-4's own gate. TO-OG-q-5's AC6 names four modules including tests/acceptance/test_local_acceptance.py."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGV2-AC2: every machine A-row of OG-v-1's protocol passes on the integrated local harness, A18 among them.",
    "world_is": "A18 encodes the pre-wiring behaviour the contract forbids, so it fails now that the refusal is live on CLOUD. The file is tests/acceptance/test_local_acceptance.py, which is in TO-OG-v-2's own <paths> and that order is OPEN, so no grant widening is needed: the correction rides OG-v-2's last re-hand, flipping A18 to expect the refusal with its contract clause cited, exactly as R-OG-15 had OG-q-4 correct the two OG-q-2 tests. Nothing deployed; nothing served is wrong.",
    "notes": "ARMED because CLOUD carries a red module until that re-hand lands. This seat is the disarm owner and OG-v-2's drain is the disarming act, with a shared-tree re-run as its evidence per R-OG-16 limb 3. The issuer's own module-set choice is the cause and is named above rather than left to inference; R-OG-17's C3 census is the wider remedy already in flight on OG-q-5."
  },
  {
    "id": "NFRA_OPLGTW-W5-S13",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-17T23:59:00Z",
    "one_line": "TO-OG-q-5's HALF ONE (the live-path dim_asset CUSIP restriction) cannot be wired inside this order's <paths> grant: the only call site that can orchestrate it -- app/integrations/schwab/integration.py SchwabService.query()/prepare_download()/export_query() -- is not a granted path, so OGQ5-AC1/AC2/AC3/AC4 cannot be satisfied as written and OGQ5-AC6 cannot reach a clean tests/acceptance/test_local_acceptance.py while test_ogv2_a06 stays red for this same reason.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py:535-536,717-718,790-791 @3dbdb084c7 -- the ONLY three call sites that gate dim_asset all read `if q.dataset == \"dim_asset\" and self._asset_policy is None: raise ServiceError(UNAVAILABLE, \"asset_policy_selection_unavailable\")`; the value of `self._asset_policy` is never read anywhere else in the file (a non-None-only sentinel), matching tests/acceptance/conftest.py:324-328's own disclosed-seam-3 comment ('zero consumers, zero other tests passing one either').",
        "READ infra/aws/ec2/opal-gateway/app/integrations/schwab/semantics.py:330-360 @3dbdb084c7 -- `qualify_asset_plan(asset_plan, position_sources, position_cusips)` is ALREADY BUILT (labelled AC11/AC12/AC13 in its own docstring, the exact PRD C3 mechanism: appends `eng.PolicyFilter(\"cusip\", sorted(position_cusips))` to the asset plan, re-tags the position SourceObjects role=\"policy\" so they count toward the same object/byte/deadline caps per engine.py's own SOURCE_ROLES contract at :112,213-218, and raises ENTITLEMENT_DENIED/asset_read_denied_unqualified when `position_cusips` is empty or `position_sources` is empty) -- but a corpus scan for its name found ZERO production callers: comp-find 'qualify_asset_plan' infra/aws/ec2/opal-gateway --all -> DENOMINATOR 5 hit(s) across 135 file(s) scanned, 1 DEF (semantics.py:330) and 4 TEST (tests/test_schwab_semantics.py:357,378,409,416, its own unit tests calling it directly against synthetic parquet, never through a tool).",
        "TRACED why only integration.py can supply qualify_asset_plan's inputs: `position_sources`/`position_cusips` need (a) the catalog's qualified snapshot for (master, business_date) on dim_position -- `self._catalog.snapshot`/`self._entries`, only reachable with the request's `policy_check` closure built in `SchwabService._policy_check` (integration.py:246-247); (b) the S3 fetch of those sources -- `self._fetch` (integration.py:150-192, `S3SourceFetcher`); (c) a small engine job filtering those sources to `scope.accounts[q.master]` and projecting `cusip` -- `self._engine.run_query` (integration.py:588); and (d) `scope.accounts`, read from the caller's OWN grant (`access.grant.scope`, integration.py:530). None of query.py or catalog.py (this order's granted app files) has access to (a)+(c) together with a specific caller's account grant: query.py does no I/O by its own docstring ('Nothing here knows the caller's grant') and catalog.py's `Catalog` class is never handed `scope.accounts`, the engine, or `qry.build_plan` -- confirmed by re-reading both files in full at this HEAD, granted here, no I/O-plus-grant seam exists in either.",
        "TRACED the actual read path for `_plan_job` (engine.py:630-696) to rule out a naive fear that concatenating a dim_position source with a dim_asset source would break on schema mismatch: `_plan_job`'s `paths` argument is already filtered to `role == \"data\"` sources ONLY by its caller (conftest.py:131-132 InProcessEngine.run_query, the same pattern production ExecutionEngine.submit uses) BEFORE `_plan_job` ever runs, so a `role=\"policy\"` position source is read only by the SEPARATE `ExecutionEngine.check_sources` budget check (engine.py:951, exercised at tests/test_schwab_semantics.py:380-389 OGQ3-AC12) and never concatenated into the asset table -- the mechanism is sound and does not require touching engine.py or semantics.py, only wiring the orchestration in integration.py's `query()`/`prepare_download()`/`export_query()`, none of which is a granted path.",
        "GRANT: this order's <paths> block (org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-q-5.asset-policy-and-c3-census.md:109-114 @3dbdb084c7) names exactly infra/aws/ec2/opal-gateway/app/integrations/schwab/{query.py,catalog.py}, tests/test_schwab_asset_policy.py and this investigation file -- app/integrations/schwab/integration.py is absent from it and from the BOUNDS paragraph's explicit not-mine list alike (that list names semantics.py/datasets.json/data_entitlement.py/test_schwab_query.py but is silent on integration.py, so its exclusion is read from <paths> itself, the stated grant, per the order's own text: '<paths> IS your write grant')."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGQ5-AC1/AC2/AC3 each require exercising 'the registered schwab_query tool on OG-v-2's live-app harness' and observing the PRD C3 partial-account dim_asset CUSIP restriction; OGQ5-AC4 mutates and re-measures the same call site; OGQ5-AC6 requires tests/acceptance/test_local_acceptance.py (which carries test_ogv2_a06, the arm this half must turn green per the cell's own READ paragraph) to show 0 failures.",
    "world_is": "The call site that must be edited to wire PRD C3's dim_asset restriction on the live path is app/integrations/schwab/integration.py's SchwabService.query() (and, for parity, prepare_download()/export_query()), which this order's <paths> grant does not name. query.py and catalog.py -- the two files this order DOES grant -- cannot supply the orchestration (catalog access plus the caller's own account grant plus a small engine job) that semantics.py's already-built qualify_asset_plan needs as input, so HALF ONE cannot be wired inside this cell's write surface as cut. This worker did not edit integration.py (BOUNDS: 'a path you need that is not named is a BLOCKING surprise row on that criterion -- never an override'; 'Nothing else' write surface) and did not widen the order to reach it.",
    "notes": "INERT: nothing deploys in this order and no served behaviour changes; the gap is a decomposition/grant mismatch, not a production incident. OGQ5-AC1, AC2, AC3, AC4 and AC6 are measured and reported FAIL by this worker's own runs, not silently patched around or satisfied by a route this order does not name. OGQ5-AC5 (the C3 census, HALF TWO) does not depend on integration.py and is completed and reported separately by this same worker. BLOCKING: this order stays open on AC1/AC2/AC3/AC4/AC6 until an issuer either grants app/integrations/schwab/integration.py to this cell (or a re-hand) or re-scopes HALF ONE's mechanism to a file this cell already owns."
  },
  {
    "id": "NFRA_OPLGTW-W5-S14",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-18T00:30:00Z",
    "one_line": "C3 census finding (row R20): PRD C3's 'grouping never removes master/date identity' has a built, unit-tested guard -- semantics.py assert_grouping_preserves_identity() -- with ZERO production callers, so a live schwab_query aggregate can group_by business_date today, unrefused.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find 'assert_grouping_preserves_identity' infra/aws/ec2/opal-gateway/app --all @3dbdb084c7 -> DENOMINATOR 1 hit across 65 file(s) scanned, 1 DEF (semantics.py:173), 0 SURFACED -- no call site anywhere in app/.",
        "MEASURED this turn, direct call against the shipped, unedited app/integrations/schwab/query.py check_against_grant() with the real org/standards/NFRA_OPLGTW_CONTRACT.json: parse_query({...,'dataset':'dim_balance','mode':'aggregate','group_by':['business_date'],'aggregates':[{'function':'count','field':None,'alias':'c'}]}) then check_against_grant(q, granted, rules) -> 'NO REFUSAL: group_by business_date accepted' (business_date is a real contract field of dim_balance, per query.py DATASET_SCHEMAS).",
        "READ semantics.py:173-181 assert_grouping_preserves_identity() and its own docstring: 'business_date IS a contract field of dim_position/dim_balance, and grouping by it inside a query already bound to one business_date is a no-op that can only mislead a caller ... Refused outright, independent of query.py's own grammar check (which allows business_date as an ordinary groupable field)' -- the function exists BECAUSE query.py's own grammar does not refuse this, and nothing calls the function that would.",
        "Full C3 census: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/C3_CALL_PATH_CENSUS.md row R28 [P4.S2] @this commit."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C3 (v0.9 @e09219470f, paragraph 4, sentence 2): 'Grouping never removes master/date identity and never sums snapshots across dates.'",
    "world_is": "A caller can request group_by=[\"business_date\"] on dim_position or dim_balance through the live schwab_query tool today and it succeeds, because the one function built to refuse it (semantics.assert_grouping_preserves_identity) is never called from query.py's check_against_grant or from integration.py's query(). Nothing is deployed (decomposition bound 9, ENABLED_INTEGRATIONS default empty), so nothing served is wrong today; this is a finding, not a fix, per this cell's own bound ('the census FINDS; it does not FIX').",
    "notes": "INERT: pre-deployment gap, same standing as NFRA_OPLGTW-W6-S8. The remedy (wiring the one-line call in query.py's check_against_grant, the same shape OG-q-4 already used for R-OG-13/R-OG-15) is the issuer's to place; this cell's <paths> grant does include query.py, but widening this cell to fix a SECOND rule is exactly the re-cut this project's own ruling (R-OG-17) says it keeps paying for, so this worker did not fix it here."
  },
  {
    "id": "NFRA_OPLGTW-W5-S15",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-18T00:31:00Z",
    "one_line": "C3 census finding (row R22): PRD C3's 'never construct a cash/AUA total by adding different balance fields' has a built guard -- semantics.py assert_single_balance_metric(), reached only via assert_sum_allowed() -- and assert_sum_allowed() itself has ZERO production callers, so a live schwab_query aggregate can SUM two distinct dim_balance fields in one request today, unrefused.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find 'sem.describe_field|sem.describe_dataset|assert_single_balance_metric' infra/aws/ec2/opal-gateway/app --all @3dbdb084c7 -> assert_single_balance_metric: 1 DEF (semantics.py:260) + 1 internal call from assert_sum_allowed (semantics.py:279); assert_sum_allowed itself: no hit outside its own def -- zero external callers of either.",
        "READ app/integrations/schwab/query.py check_against_grant():464-478 @3dbdb084c7 -- calls only sem.assert_field_summable(query.dataset, agg.field) and sem.assert_quantity_sum_grouped(query.dataset, agg.field, query.group_by) per aggregate, never sem.assert_sum_allowed or sem.assert_single_balance_metric, which would need to see ALL summed fields across the request at once.",
        "MEASURED this turn, direct call against the shipped, unedited query.py check_against_grant() with the real contract: an aggregate query on dim_balance with aggregates=[{'function':'sum','field':'mkt_value_long','alias':'a'},{'function':'sum','field':'mkt_value_short','alias':'b'}] -> 'NO REFUSAL: summing two different dim_balance fields in one query accepted'.",
        "Full C3 census: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/C3_CALL_PATH_CENSUS.md row R22 [P4.S4] @this commit."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C3 (v0.9 @e09219470f, paragraph 4, sentence 4): 'Vendor balance fields overlap: permit a named field's sum across approved accounts, never construct a cash/AUA total by adding different balance fields.'",
    "world_is": "A caller can request SUM(mkt_value_long) and SUM(mkt_value_short) (or any two distinct additive dim_balance fields) in one aggregate query today and add the two returned numbers back together outside the Gateway, approximating exactly the combined total C3 forbids -- semantics.py's own docstring names this as the residual risk assert_single_balance_metric exists to close (':261-265'), but the function that closes it is never called. Nothing is deployed, so nothing served is wrong today; a finding, not a fix.",
    "notes": "INERT: pre-deployment gap. The remedy is a second call inside query.py's check_against_grant (collecting summed_fields per dataset across the whole aggregates list and calling sem.assert_single_balance_metric once) -- the issuer's to place, not fixed here per this cell's own bound against widening to a second rule."
  },
  {
    "id": "NFRA_OPLGTW-W5-S16",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-18T00:32:00Z",
    "one_line": "C3 census finding (row R24): PRD C3's 'duplicate/conflicting source grains produce unavailable, not silent deduplication' has a built guard -- semantics.py assert_unique_grain() -- with ZERO production callers anywhere, and engine.py's own DuckDB execution has no grain-uniqueness check of its own either, so a duplicate/conflicting grain is served (rows mode) or silently folded into a SUM (aggregate mode) instead of refusing the read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find 'assert_unique_grain' infra/aws/ec2/opal-gateway/app --all @3dbdb084c7 -> DENOMINATOR 1 hit across 65 file(s) scanned, 1 DEF (semantics.py:285), 0 SURFACED.",
        "READ app/integrations/schwab/engine.py _plan_job():630-696 @3dbdb084c7 in full -- reads the parquet columns, applies PolicyFilter(s), projects, renames to positional columns and runs the generated DuckDB statement; no grain-uniqueness check of any kind exists in this function or anywhere else in engine.py (confirmed by reading engine.py's full public surface, __all__ at :52-74, which names no grain-related symbol).",
        "READ app/integrations/schwab/query.py and app/integrations/schwab/integration.py in full @3dbdb084c7 -- neither calls semantics.assert_unique_grain at any point after a job's rows are returned (integration.py's query() renders rows straight from job.value['rows'] into the response, integration.py:609-632).",
        "Full C3 census: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/C3_CALL_PATH_CENSUS.md row R24 [P4.S6] @this commit."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C3 (v0.9 @e09219470f, paragraph 4, sentence 6): 'Duplicate/conflicting source grains produce unavailable, not silent deduplication.'",
    "world_is": "Two rows sharing one grain key (the same account/cusip/long-short for dim_position, for example) are never detected by the live query path: in rows mode both rows are simply returned; in aggregate mode both are folded into the same SUM/COUNT like any other pair of rows, the opposite of the contract's 'produce unavailable'. semantics.assert_unique_grain exists and is unit-tested (OGQ3-AC9 per its own comment) but is never called. Nothing is deployed, so nothing served is wrong today; a finding, not a fix.",
    "notes": "INERT: pre-deployment gap. Wiring this needs a call site AFTER a job's rows return but BEFORE they render (integration.py, not this cell's <paths>) -- named here as a finding, not repaired, per this cell's bound against fixing a rule beyond HALF ONE and against editing integration.py (see NFRA_OPLGTW-W5-S13)."
  },
  {
    "id": "NFRA_OPLGTW-W5-S17",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-18T00:33:00Z",
    "one_line": "C3 census finding (row R25): PRD C3's dataset-description rule requires grain/type/unit/sign/null-semantics; the live schwab_describe_dataset tool exposes grain/type/unit only -- sign and null_semantics, present in datasets.json and served by semantics.py's own describe_field()/describe_dataset() (zero production callers), are never returned to a caller.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find 'sem.describe_field|sem.describe_dataset' infra/aws/ec2/opal-gateway/app --all @3dbdb084c7 -> 0 hits outside semantics.py's own definitions (describe_field :151-156, describe_dataset :159-163) -- neither is called from app/integrations/schwab/integration.py or anywhere else.",
        "READ app/integrations/schwab/integration.py describe_dataset():438-477 @3dbdb084c7 in full -- builds `described` from qry.DATASET_SCHEMAS directly: {'name','type'} always, plus 'precision'/'scale'/'unit'/'representation' for KIND_DECIMAL fields only, plus a special 'representation' string for account_ref; no 'sign' key and no 'null_semantics' key appear anywhere in the built doc.",
        "READ app/integrations/schwab/semantics.py:81 @3dbdb084c7 -- _FIELD_DESCRIPTION_KEYS = ('type','unit','sign','grain','null_semantics','source'); _validate_datasets() (:91-135) asserts datasets.json carries exactly these six keys for every field of every dataset, cross-checked against query.py's DATASET_SCHEMAS at import time -- so 'sign' and 'null_semantics' data DOES exist for every field, it is simply never read by the live tool.",
        "Full C3 census: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/C3_CALL_PATH_CENSUS.md row R25 [P4.S7] @this commit."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C3 (v0.9 @e09219470f, paragraph 4, sentence 7): 'Dataset description records grain, field type, unit, sign and null semantics from measured source plus independent fixtures.'",
    "world_is": "A caller of the registered schwab_describe_dataset tool receives name/type/grain/unit/precision/scale but never a field's sign or null semantics, even though datasets.json (validated against query.py's own schema at import time) carries both for every field -- integration.py's describe_dataset() builds its response from qry.DATASET_SCHEMAS (which has no sign/null_semantics attributes at all) instead of from semantics.describe_dataset(), which does. Nothing is deployed, so nothing served is wrong today; a finding, not a fix.",
    "notes": "INERT: pre-deployment gap. The remedy (integration.py's describe_dataset() reading semantics.describe_field()/describe_dataset() instead of, or alongside, qry.DATASET_SCHEMAS) touches integration.py, which is not this cell's <paths> grant (see NFRA_OPLGTW-W5-S13's same boundary) and is a second rule beyond this cell's HALF ONE; named here, not repaired."
  },
  {
    "id": "NFRA_OPLGTW-W5-S18",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-18T01:17:00Z",
    "one_line": "HALF ONE's wiring (row NFRA_OPLGTW-W5-S13's re-hand) turned tests/acceptance/test_local_acceptance.py::test_ogv2_a06's dim_asset CUSIP assertion (:477) green, which UNMASKED a second, unrelated failure at the SAME test's last assertion (:488): a post-revocation schwab_query denial arrives with the raw app/data_entitlement.py guard-denial dict as the tool payload and MCP `isError` left falsy, so a client that trusts `isError` (as this test's own harness does) reads a revoked principal's denied call as a SUCCESS.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN on the shared worktree after HALF ONE's wiring @35377638d7+working-tree: `pytest -q tests/acceptance/test_local_acceptance.py::test_ogv2_a06` -> FAILED at test_local_acceptance.py:488 `assert is_error, payload` with `AssertionError: {'code': 'entitlement_denied', 'error': \"the principal's restricted profile is revoked (revision 5) does not include tool 'schwab_query'\", 'error_code': 'ENTITLEMENT_DENIED', 'guard_denied': True}` -- NOT at :477 (the dim_asset CUSIP assertion this cell's HALF ONE governs, which the same run's stdout shows PASSING: 'OGV2-AC2/A6/partial-grant-asset-cusips: got ['SYN000001', 'SYN000002'], EXPECTED ['SYN000001', 'SYN000002'] (MATCH)').",
        "Before HALF ONE was wired, this same test failed earlier, at :477 (this cell's own task order text and row W5-S13's grounding both cite test_ogv2_a06 failing 'for this reason' -- the CUSIP mismatch), so Python's assert-stops-at-first-failure semantics MASKED this :488 defect until this cell's fix let execution reach it. Not this fix's defect; this fix's necessary side effect of exposing it.",
        "TRACED the shape: app/data_entitlement.py:305-306 `_denial(code, reason, error_code)` returns the bare `{'error': reason, 'guard_denied': True, 'code': code, 'error_code': error_code}` dict; `tool_denial()` (data_entitlement.py:360) returns it for a revoked/restricted profile. app/tools.py:70-75 `_PolicyGuardedMCP.call_tool()` -- 'the per-principal policy guard on DISCOVERY and DISPATCH of every tool on this server -- native, integration and any tool registered later -- before the tool function runs' (its own docstring, :57-61) -- calls `data_entitlement.tool_denial(name, principal)` and, on a denial, `return denial` (:73-75) DIRECTLY, never routing through `super().call_tool()` or any `CallToolResult(isError=True, ...)` construction the way app/integrations/schwab/envelope.py's `error_result()` (:151-160, `mcp_result(doc, is_error=True)`) or app/integrations/schwab/integration.py's `_denied()` (:931-934, which DOES wrap via `env.error_result`) both do.",
        "So `_PolicyGuardedMCP.call_tool()` is a SECOND, EARLIER guard chokepoint than `SchwabIntegration._call()`'s own `_admit()`/`_denied()` (integration.py:924-934, which DOES correctly wrap): a revoked profile is caught by `app/tools.py`'s dispatch-level guard first, and THAT path is the one that skips the isError wrap. Confirmed the observed payload's exact shape (`error`+`guard_denied`+`code`+`error_code`, no nested `error.code`) matches data_entitlement.py's `_denial()` output and NOT `env.error_result()`'s nested shape, so the request travelled the tools.py chokepoint, not integration.py's own.",
        "This chokepoint (app/tools.py `_PolicyGuardedMCP`) guards EVERY registered tool on the live Gateway server, not only schwab_query, and is not conditioned on ENABLED_INTEGRATIONS or the decomposition bound-9 flag that keeps the Schwab integration itself dormant -- unlike this cell's other C3-census OBSERVATION rows (W5-S14..S17), which are all inert because Schwab is not registered by default. Whether this specific chokepoint is exercised by a live caller today is NOT measured here (only reproduced on this local, moto-backed harness); ARMED is this worker's best-evidence read given the guard's own docstring scope, not a confirmed live incident."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The MCP contract implied by every caller in this codebase that inspects `result.isError` to decide success/failure (this test's own `h_._tool()` at tests/test_principal_cutover.py:342-353, and this cell's own AC1-3 tests' `run_query()` helper) -- a denied/refused tool call sets isError=True.",
    "world_is": "app/tools.py's `_PolicyGuardedMCP.call_tool()` returns app/data_entitlement.py's raw guard-denial dict as the tool's structured result without ever constructing a `CallToolResult(isError=True, ...)`, for EVERY tool this dispatch guard denies (a revoked/restricted profile, an unclassified tool, a scoped-identity refusal, a write-class denial -- every `guard_denied: True` dict this file and app/integrations/base.py's parallel run_integration_tool build). A caller trusting `isError` alone, not the payload shape, reads such a denial as a success. Not this cell's defect and not caused by this cell's fix; only exposed by it, per the grounding above.",
    "notes": "ARMED (best-evidence, not confirmed live): this chokepoint is unconditional on every registered tool, unlike this cell's own Schwab-scoped findings. The remedy (app/tools.py `_PolicyGuardedMCP.call_tool()` wrapping a `guard_denied` dict into a proper `CallToolResult(isError=True, ...)` before returning it) touches app/tools.py and app/data_entitlement.py, neither in this cell's <paths> grant and neither this cell's task (HALF ONE is the dim_asset restriction only); named here, not repaired, per this order's own bound against widening to a second defect."
  },
  {
    "id": "NFRA_OPLGTW-W5-S19",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-18T02:44:00Z",
    "one_line": "TO-OG-q-6's R20 wiring (query.py check_against_grant -> semantics.assert_grouping_preserves_identity) correctly refuses group_by containing business_date, which turns tests/test_schwab_query.py::test_ogq2_ac06's 'at_limit' group_fields case RED -- that case groups by ALL_POSITION[:10] (dim_position's own contract-field order), and business_date sits at index 1, so it was always inside the 10-field 'at the limit, should succeed' arm.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN this turn on this cell's own edited worktree: `pytest -q infra/aws/ec2/opal-gateway/tests/test_schwab_query.py` -> `2 failed, 23 passed` (test_ogq2_ac06 and test_ogq2_ac20); test_ogq2_ac06 fails at test_schwab_query.py:462 `good = ok(world.query(at_limit))` with payload `{'error': {'code': 'INVALID_REQUEST', 'reason': 'group_removes_date_identity', 'where': 'group_by'}}`.",
        "READ infra/aws/ec2/opal-gateway/tests/test_schwab_query.py:49 `ALL_POSITION = tuple(CONTRACT['fields']['dim_position'])` and org/standards/NFRA_OPLGTW_CONTRACT.json `fields.dim_position` at this commit -> `['account_ref','business_date','cusip',...]`, index('business_date')==1, so `groups[:10]` (the case's 'at_limit', asserted to SUCCEED) and `groups[:11]` (the 'over', asserted to be REFUSED for count-of-fields reasons) BOTH contain business_date.",
        "READ app/integrations/schwab/semantics.py:173-181 `assert_grouping_preserves_identity` (OG-q-3's own code, unedited by this cell) -- its own docstring states the rule is 'Refused outright, independent of query.py's own grammar check', i.e. this test's OLD expectation (group_by=[...,'business_date',...] succeeds when under the field-count limit) is exactly the C3 R20 gap this cell's task order (ruling R-OG-18) was cut to close, not an interaction this cell introduced by choice.",
        "Re-run confirmed via this cell's own probe: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q6.py AC6's informational regression pass, this commit."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This order's own BOUNDS text: 'tests/test_schwab_query.py ... are NOT yours -- other cells', merged or open. A needed change there is a BLOCKING row.'",
    "world_is": "test_schwab_query.py::test_ogq2_ac06 now fails because it asserts the PRE-R20 behaviour (grouping by business_date among up to 10 fields succeeds) as correct; C3 R20 says it must always refuse. This cell cannot edit test_schwab_query.py (not its <paths>), so the test stays red until its owner updates the 'at_limit' fixture to exclude business_date from the group_fields case (or asserts a refusal there instead).",
    "notes": "ARMED: a real, committed test-suite regression (not a dormant-feature latent risk like this cell's other C3 rows) -- whoever next runs the full opal-gateway suite sees this red. Not this cell's defect to fix (file outside <paths>); this cell's own AC1..AC6 are unaffected and all PASS. Remedy: update test_ogq2_ac06's 'at_limit' group_fields fixture to a field list that excludes business_date (or move business_date to the 'over the limit, refused' arm), the issuer's or that file's owning cell's call."
  },
  {
    "id": "NFRA_OPLGTW-W5-S20",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~5",
    "surfaced_at": "2026-09-18T02:45:00Z",
    "one_line": "TO-OG-q-6's R24 wiring (integration.py SchwabService.query() -> semantics.assert_unique_grain, rows mode with every grain field requested) correctly refuses a duplicated source grain even on a SINGLE page, which turns tests/test_schwab_query.py::test_ogq2_ac20's one-page duplicate-grain case RED -- that case asserts a duplicate-grain dataset SUCCEEDS once page_size is large enough to avoid paging, the exact 'silent deduplication is acceptable if it fits in one page' shape C3 R24 forbids.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN this turn on this cell's own edited worktree: `pytest -q infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac20` -> FAILED at test_schwab_query.py:905 `one_page_dup = ok(dup.query(dict(q, page_size=50)))` with payload `{'error': {'code': 'UNAVAILABLE', 'reason': 'duplicate_source_grain'}}`.",
        "READ infra/aws/ec2/opal-gateway/tests/test_schwab_query.py:895-906 @this commit -- the test builds `dup_rows = POSITIONS + [one extra row sharing (A1, 'AAA000001', 'AAA', 'L') 's grain fields]`, asserts the SMALL-page-size query `err(...)` (paging refused, the PRE-EXISTING `_grain_unique` paging guard, unrelated to this cell), then asserts the SAME duplicated dataset queried with `page_size=50` (one page, no pagination needed) SUCCEEDS -- i.e. the test's own design treats 'fits in one page' as license to skip the duplicate-grain check entirely.",
        "READ this cell's own C3_CALL_PATH_CENSUS.md row R24 -- the census's own measured gap, this order's task table, and this cell's wiring in integration.py's query() (columns=['account_ref','cusip','l_s'] intersect the grain fields) apply sem.assert_unique_grain to `all_rows` regardless of page_size, exactly because C3's text ('produce unavailable, not silent deduplication') names no page-size exception.",
        "Re-run confirmed via this cell's own probe: org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_q6.py AC6's informational regression pass, this commit."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This order's own BOUNDS text: 'tests/test_schwab_query.py ... are NOT yours -- other cells', merged or open. A needed change there is a BLOCKING row.'",
    "world_is": "test_schwab_query.py::test_ogq2_ac20 now fails because its 'one_page_dup' case asserts success for a duplicated source grain merely because pagination is not needed; C3 R24 requires UNAVAILABLE regardless of page size. This cell cannot edit test_schwab_query.py (not its <paths>), so the test stays red until its owner updates that assertion to expect a refusal (or narrows the fixture so the duplicate-grain row is not among the requested/grain-visible columns).",
    "notes": "ARMED: a real, committed test-suite regression (not a dormant-feature latent risk) -- whoever next runs the full opal-gateway suite sees this red. Not this cell's defect to fix (file outside <paths>); this cell's own AC1..AC6 are unaffected and all PASS. Remedy: update test_ogq2_ac20's one-page duplicate-grain expectation to a refusal, the issuer's or that file's owning cell's call."
  },
  {
    "id": "NFRA_OPLGTW-W6-S10",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~6",
    "surfaced_at": "2026-09-18T03:35:00Z",
    "one_line": "OGV2-AC4's module sweep, re-run fresh at this order's HEAD (CLOUD @1529bcd131, after TO-OG-q-6's reopen+amend commit), measures MODULES: 25 FAILED-MODULES: 1 -- test_schwab_query.py::test_ogq2_ac06 and ::test_ogq2_ac20 are still red, the same defect rows W5-S19/W5-S20 already named and ARMED against disarm_owner 2.0.0_SA_COO~O; the reopen commit re-grants the file, it has not yet drained a fix.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN at this worker's HEAD: `cd /c/tmp/wk-oplgtw-6f && n=0; f=0; for m in infra/aws/ec2/opal-gateway/tests/test_*.py; do n=$((n+1)); timeout 300 .venv-og/Scripts/python -m pytest \"$m\" -q -p no:cacheprovider --color=no -m \"not live\" -k \"not test_scoped_deny_by_default\" || [ $? = 5 ] || f=$((f+1)); done; echo \"MODULES: $n FAILED-MODULES: $f\"` -> `MODULES: 25 FAILED-MODULES: 1`, the one failing module printing `FAILED infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac06` and `FAILED infra/aws/ec2/opal-gateway/tests/test_schwab_query.py::test_ogq2_ac20` (`2 failed, 23 passed in 10.72s`) -- OGV2-AC4's own `<expect>` (`^MODULES: [1-9][0-9]* FAILED-MODULES: 0$`) does not match this output.",
        "READ this worktree's commit log: HEAD @1529bcd131 is `reopen+amend(NFRA_OPLGTW.TO-OG-q-6, 2.0.0_SA_COO~O): test_schwab_query.py granted for EXACTLY test_ogq2_ac06 and test_ogq2_ac20 -- the R20/R24 wiring turns both red because each asserts the pre-wiring shape the contract forbids (rows W5-S19, W5-S20); AC7-AC9 grade the correction` -- so the re-grant to fix this exact pair is already cut and owned; the fix itself has not landed at this HEAD.",
        "This is the SAME defect rows NFRA_OPLGTW-W5-S19 and NFRA_OPLGTW-W5-S20 (this file, `disarm_owner: 2.0.0_SA_COO~O`) already ground -- not a new class, a re-measurement at a later HEAD confirming it is still open and still blocks a criterion that reads the whole `test_*.py` glob (OGV2-AC4), where W5-S19/S20's own cell (TO-OG-q-6) only needed its own AC7-AC9 clean."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGV2-AC4's invocation and `<expect>`: every module the glob `infra/aws/ec2/opal-gateway/tests/test_*.py` derives passes in its own process, `MODULES: [1-9][0-9]* FAILED-MODULES: 0`, with only the one named row-S1 test deselected.",
    "world_is": "test_schwab_query.py carries two tests (test_ogq2_ac06, test_ogq2_ac20) asserting the pre-R20/R24 shape C3 now forbids; they fail, so FAILED-MODULES reads 1, not 0. This cell's <paths> grant is `tests/acceptance/test_local_acceptance.py`, `tests/acceptance/conftest.py` and this investigation file -- it cannot edit test_schwab_query.py to close this, and the order that can (TO-OG-q-6) is already reopened for exactly this pair but not yet drained at this HEAD.",
    "notes": "BLOCKING for THIS order's OGV2-AC4 (a whole-glob criterion, unlike TO-OG-q-6's own narrower AC7-AC9); not a new hazard -- re-measured against the already-ARMED W5-S19/W5-S20 rows at a later commit to confirm they are still open. OGV2-AC4 is recorded FAIL by this measurement; no repair attempted outside this cell's grant."
  },
  {
    "id": "NFRA_OPLGTW-S27",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T04:10Z",
    "one_line": "Disarm evidence for THREE rows this seat owns -- NFRA_OPLGTW-W5-S19, W5-S20 and W6-S10 -- which are ONE defect measured by two cells at two vintages: test_schwab_query.py::test_ogq2_ac06 and ::test_ogq2_ac20 asserted the pre-wiring shape OG-q-6's R20/R24 wiring correctly refuses. Corrected in OG-q-6's re-open, drained @e58d9d2b04, and the SHARED-TREE re-run R-OG-16 limb 3 requires reads test_schwab_query.py 25 passed, test_schwab_c3_rules.py 4 passed, tests/acceptance/test_local_acceptance.py 14 passed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN on the SHARED TREE after the drain @e58d9d2b04, one module per process: `pytest -q tests/test_schwab_query.py` -> 25 passed; `tests/test_schwab_c3_rules.py` -> 4 passed; `tests/acceptance/test_local_acceptance.py` -> 14 passed. BEFORE, at @7785d21060: test_schwab_query.py 2 failed / 23 passed, both failures those two tests.",
        "THE CORRECTION'S TIGHTNESS IS GRADED, not asserted: OGQ6-AC7 confined all 5 diff hunks to the two granted test functions, OGQ6-AC8 read 25 of 25 tests collected before and after with 2 of 2 clause citations present, OGQ6-AC9 read 4 of 4 modules green (46 passed).",
        "ONE DEFECT, THREE ROWS, TWO CELLS: W5-S19 and W5-S20 were filed by 0.9.0_WK_NFRA_OPLGTW~5 when its wiring turned the two tests red; W6-S10 was filed by 0.9.0_WK_NFRA_OPLGTW~6 re-measuring the SAME two tests at OG-v-2's own HEAD, because that order's whole-glob OGV2-AC4 needed the module clean where OG-q-6's narrower AC7-AC9 did not. Both filings were correct and neither is a duplicate: they are the same fact measured from two grants.",
        "WORKER-SIDE R-40 APPLICATION, unprompted and worth recording: 0.9.0_WK_NFRA_OPLGTW~5 found its own AC5 mutant had gone STALE once its earlier drain merged into CLOUD, and re-pinned the mutant to the pre-wiring BYTES (query.py at 881b1a5445, integration.py at 0ced7baf10) rather than a branch label -- a LABEL IS NOT AN IDENTITY, applied by the worker without being told."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGQ2-AC6 and OGQ2-AC20 assert that a grouping dropping date identity and a duplicate-grain read succeed; OGV2-AC4 requires every one of 25 test modules green.",
    "world_is": "Both tests now expect the contract's refusal with their clauses cited, the wiring stands, and all three modules are green on the shared tree. The three rows' hazard is spent. This seat is the disarm owner of all three and gives the word here; 3.0.0_SA_CVO writes the clock at L9.",
    "notes": "This is the FIFTH and SIXTH instance of the defect-asserting-test class in this project, all six in ONE file, and they were found by the C3 census's population read rather than one at a time. Evidence only: this row adjudicates nothing."
  },
  {
    "id": "NFRA_OPLGTW-W2-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~2",
    "surfaced_at": "2026-09-18T05:15Z",
    "one_line": "infra/aws/ec2/safe-ec2-deploy.sh's own worktree fix redirects HALT_GATE_REPO_ROOT to the SHARED MAIN TREE (via git-common-dir) before sourcing .tools/halt-gate-check.sh, so a worker's own linked-worktree copy of its session-serial file (org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial, pre-provisioned by the issuer per this order's identity line) is NEVER checked; the halt gate fails closed with 'IDENTITY UNRESOLVED', and its own printed remediation line writes a RELATIVE path that -- given the script's absolute MAIN_TREE override -- would still land in the wrong place. AC2 (the deploy) is BLOCKING on this; every criterion that depends on the deploy having run (AC2-AC10, AC12-AC14, and AC8's close) is BLOCKING as a result. AC1 and AC11 do not depend on the deploy and both PASS.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ infra/aws/ec2/ec2/safe-ec2-deploy.sh:25-41 @this worktree's HEAD (cut from CLOUD @1ca5067f6e): `_GIT_COMMON_DIR=\"$(git -C \"$WORKSPACE_ROOT\" rev-parse --git-common-dir ...)\"` then `MAIN_TREE=\"$(cd \"$_GIT_COMMON_DIR/..\" && pwd)\"` then unconditionally `HALT_GATE_REPO_ROOT=\"$MAIN_TREE\"` -- WORKSPACE_ROOT here is this worker's OWN worktree (/c/tmp/wk-oplgtw-2a), and the comment at :25-30 states the INTENT is runtime state resolving from 'the LIVE main-tree inbox + serial even when this wrapper is invoked from a build worktree'.",
        "MEASURED directly in this worktree: `git rev-parse --git-common-dir` -> `C:/Users/AndrewBerman/Desktop/ajb_workspace/.git`; `git rev-parse --show-toplevel` -> `C:/tmp/wk-oplgtw-2a`. So MAIN_TREE resolves to `C:/Users/AndrewBerman/Desktop/ajb_workspace`, NOT this worktree, for every worker spawned into a linked worktree of the CLOUD session.",
        "READ .tools/halt-gate-check.sh:68-109 `halt_gate_resolve_serial()`: it checks `${repo_root}/org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial` then `${HALT_GATE_SHARED_ROOT}/org/mcp/sessions/...`, where `repo_root=HALT_GATE_REPO_ROOT` (already overridden to MAIN_TREE by safe-ec2-deploy.sh before sourcing) and HALT_GATE_SHARED_ROOT (:48-53) re-derives from HALT_GATE_REPO_ROOT's OWN git-common-dir, landing on the SAME MAIN_TREE again -- so BOTH checked directories are the main tree; neither is this worktree.",
        "MEASURED: this worker's own worktree carries `org/mcp/sessions/e3c2c727-fc4c-4791-9a1d-09455d5089b8.serial` containing `0.9.0_WK_NFRA_OPLGTW~2` (the issuer's pre-provisioning, per this order's identity line) -- `ls`/`cat` confirmed present and correct. The SAME path under the main tree (`/c/Users/AndrewBerman/Desktop/ajb_workspace/org/mcp/sessions/e3c2c727-....serial`) does NOT exist -- confirmed absent by direct `ls`.",
        "RUN this turn: `timeout 550 .venv-og/Scripts/python .../probes/og_r1.py AC2` -> safe-ec2-deploy.sh Step 1 (pre-deployment check) PASSED, then the sourced halt_gate_check printed 'HALT-GATE: IDENTITY UNRESOLVED -- BLOCKED (fail-closed)' verbatim and safe-ec2-deploy.sh exited rc=3 BEFORE Step 2 ('Running Deployment') ever ran -- no artifact was built, no S3 upload, no SSM command issued, no host state changed. Confirmed by re-reading EC2_MANIFEST.json's opal-gateway.deployed_commit unchanged from before this run.",
        "READ .tools/halt-gate-check.sh:295-308: the identity-unresolved path `return 3` is reached BEFORE any HALT_OVERRIDE check (that env var is read only later, at :438, on the STOP-found branch) -- there is no audited override for this failure mode; the gate's own printed text says so ('Do NOT override this').",
        "This worker's <paths> grant (this order, <paths> block) is `infra/aws/ec2/EC2_MANIFEST.json`, `org/critical_paths/change_management/`, the one named .open_deploys sentinel, and this investigation file -- it does not include `org/mcp/sessions/` in EITHER tree, and the blocking path lies in the SHARED MAIN TREE outside this worktree entirely, so writing the missing serial file there would be an out-of-grant write to a different checkout altogether, not merely an out-of-grant path in this one."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This order's BOUNDS: 'The Gateway only through infra/aws/ec2/safe-ec2-deploy.sh. No hand copy, no direct SSM install...'; and 'A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.'",
    "world_is": "The one sanctioned deploy route fails closed at its own halt-gate identity check before any deploy work begins, because the route's own worktree-redirect fix points the identity resolver at the shared main tree rather than at the worker's own (issuer-provisioned) worktree copy of its session-serial file -- and the fix needed to close that gap is a write outside this worker's <paths>, in a different checkout entirely. No override exists for this failure branch and none was attempted.",
    "notes": "ARMED, not disarmed here: nothing was deployed (Step 1 passed, Step 2 never ran), so no AWS/host state changed and the deploy is not half-landed in the CLAUDE.md NEVER-2 sense -- it never landed at all. The open deploy-completion ledger (org/critical_paths/.open_deploys/nfra-oplgtw-og-r-1-first-release.json, opened this run for OGR1-AC1) has every leg still OPEN and unproven; it does NOT qualify for deploy_ledger.py hold (an open apply-kind leg disqualifies HELD by construction) and cannot be truthfully closed (nothing to prove). It is left OPEN, correctly reading as a stranded start once its window elapses, until a seat with write access to the shared main tree's org/mcp/sessions/ (or a fix to safe-ec2-deploy.sh's HALT_GATE_REPO_ROOT redirect so it also checks the INVOKING worktree, not only MAIN_TREE) unblocks AC2. Remedy is either: (a) provision org/mcp/sessions/e3c2c727-fc4c-4791-9a1d-09455d5089b8.serial in the shared main tree, or (b) amend safe-ec2-deploy.sh/halt-gate-check.sh to also check WORKSPACE_ROOT's own org/mcp/sessions/ before or alongside MAIN_TREE's. Disarm owner is the issuing COO (a worker is terminal at its drain and cannot carry an ARMED row's disarm word, R-18) since the actual FIX -- either provisioning the serial file in the shared main tree or amending safe-ec2-deploy.sh/halt-gate-check.sh -- is outside this cell's <paths>."
  },
  {
    "id": "NFRA_OPLGTW-W2-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~2",
    "surfaced_at": "2026-09-18T05:30Z",
    "one_line": "The live 'gateway-access-state-table' DynamoDB table carries 8 leftover items from OTHER cells' own acceptance probes (og_i1.py/og_i5.py), pk-shaped 'POLICY#probe-og-i1-<timestamp>[-ttl|-race]' (sk PROFILE/AUDIT#000N) and 'RUNTIME#probe-og-i5-<timestamp>' (sk AC9) -- synthetic test fixtures, never cleaned up, sitting in the PRODUCTION table this release's OGR1-AC3/AC12 grade for 'no principal profile active'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN this turn: dynamodb Scan(ProjectionExpression=pk,sk) on gateway-access-state-table via boto3 -> 8 of 8 items, every pk/sk pair matching either `POLICY#probe-og-i1-\\d{8}T\\d{6}...` or `RUNTIME#probe-og-i5-\\d{8}T\\d{6}` -- none carries a real tid/oid-shaped identifier.",
        "The naming (`probe-og-i1-...`, `probe-og-i5-...`) matches the OG-i-1 and OG-i-5 cells' own probe scripts (org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py, og_i5.py), which write synthetic RUNTIME/POLICY records under access_state.runtime_key() to grade their own criteria against the live table -- not a real Schwab or OAuth principal."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGR1-AC3/AC12 read the live access-state table as evidence that no principal profile/grant is active this release.",
    "world_is": "The table is not empty, but every item present is a pre-existing, other-cell test fixture rather than a real principal profile; OGR1-AC3/AC12 classify and exclude these (pattern probe-og-<cell>-<timestamp>) to grade the REAL population, which is empty, rather than reporting a false FAIL on a non-zero raw count.",
    "notes": "INERT: no principal is actually affected and this release grants nothing; the leftover fixtures are a housekeeping gap in OG-i-1/OG-i-5's own test hygiene (their probes never delete what they write), not a security exposure. Not this cell's defect to fix (its <paths> does not reach those cells' probes or a table-cleanup act); left for whichever cell's remit covers access-state table hygiene."
  },
  {
    "id": "NFRA_OPLGTW-W2-S7",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~2",
    "surfaced_at": "2026-09-18T05:35Z",
    "one_line": "The Gateway's CURRENTLY-DEPLOYED commit (EC2_MANIFEST.json opal-gateway.deployed_commit, 7bd89b5d71b8d488d9e8c4168513193c9d6a9ec2, 2026-09-09 -- the OG-r-1 rollback target per the runbook's 7.2) has NO app/data_entitlement.py at all: `git cat-file -e 7bd89b5d71...:infra/aws/ec2/opal-gateway/app/data_entitlement.py` fails ('exists on disk, but not in' that commit). app/revocation.py and app/identity_scope.py DO exist there. So this release's own rollback-to-previous-binary path (SCHWAB_PILOT_RUNBOOK.md s.7.2, step 1: 'Confirm the target commit is NOT older than ... the restricted-profile denial (app/data_entitlement.py, app/identity_scope.py)') is UNSAFE against the ACTUAL previous artifact as things stand today: it fails that named precondition.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN this turn: `git cat-file -e 7bd89b5d71b8d488d9e8c4168513193c9d6a9ec2:infra/aws/ec2/opal-gateway/app/data_entitlement.py` -> rc!=0, stderr 'fatal: path ... exists on disk, but not in 7bd89b5d71...'. Same commit: `app/identity_scope.py` and `app/revocation.py` both `cat-file -e` clean (rc=0, present).",
        "READ infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md:255-260 (s.7.2 step 1, OG-o-2): 'Confirm the target commit is NOT older than the durable token revocation shim (app/revocation.py) or the restricted-profile denial (app/data_entitlement.py, app/identity_scope.py) -- rolling back past either would reopen the email-only path or accept legacy refresh tokens, which C6 forbids outright.' The currently-deployed (pre-OG-r-1) commit fails this exact named check for one of the two named files.",
        "READ infra/aws/ec2/EC2_MANIFEST.json services.opal-gateway.deployed_commit at this worktree's cut base -- 7bd89b5d71b8d488d9e8c4168513193c9d6a9ec2, deployed_at 2026-09-09T19:08:11Z, i.e. the live host predates essentially all of this project's own build (data_entitlement.py, identity_scope.py's OG-a-2 cutover work, etc.) that landed afterward on CLOUD."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGR1-AC10 (and the runbook it cites) treats 'the previous release artifact ... restorable by the runbook's rollback section' as a property this release can simply record.",
    "world_is": "The previous release artifact fails the runbook's own restorability precondition (data_entitlement.py absent), so OGR1-AC10 measures FAIL truthfully -- not a probe defect, a genuine gap: were an operator ever to invoke SCHWAB_PILOT_RUNBOOK.md s.7.2 against THIS specific previous commit, the runbook's own step 1 would (correctly) refuse it, leaving s.7.1 (the ENABLED_INTEGRATIONS flag flip, which does not depend on which binary is running) as the only safe rollback route until a newer previous-release commit -- one that carries data_entitlement.py -- exists to roll back to.",
    "notes": "ARMED because it is a real operational gap in the rollback story this release's PRD C6 promises, not merely a probe artifact; disarmed once EITHER a later deploy makes the recorded 'previous' commit one that carries data_entitlement.py, or the runbook/PRD is amended to say s.7.1 (flag-disable) is the ONLY safe rollback route at this stage of the rollout (round 1, nothing enabled, so s.7.1 alone is sufficient regardless). This cell cannot amend the runbook (outside its <paths>) or choose a different 'previous' commit to record (there is only one deployed_commit)."
  },
  {
    "id": "NFRA_OPLGTW-W2-S8",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~2",
    "surfaced_at": "2026-09-18T06:05Z",
    "one_line": "OG-r-1's real deploy (safe-ec2-deploy.sh, from this Windows worktree, core.autocrlf=true) deployed 9 of 68 shipped files with CRLF line endings that differ byte-for-byte from their LF-stored git blobs -- deploy/opal-gateway.service, requirements.txt, identity_tool_allowlist.txt, app/refs/DATA_CATALOG.yaml, app/integrations/schwab/datasets.json, app/graphql_plumbing/DESIGN.md, app/entity_resolution/SCAFFOLD.md, app/static/schwab_download/index.html, app/org/mcp/agent_telemetry/0.7.0_AE_CloudOps.jsonl -- every one an extension NOT covered by a `text: set / eol: lf` .gitattributes rule (only .py carries that rule; OGR1-AC4's own digest comparison caught it, 9 MISMATCH of 68).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN this turn (OGR1-AC4): SSM sha256sum on i-07dccb1615503ac99 (/opt/opal-gateway) vs git blob sha256 at the deployed commit -- 68 of 68 files compared, 9 MISMATCH, all 9 host hashes differing from tree hashes; 0 host-only, 0 tree-only (every file exists on both sides, only the bytes differ).",
        "MEASURED: `git config --get core.autocrlf` on this worktree/box -> `true`. `git check-attr text eol -- infra/aws/ec2/opal-gateway/requirements.txt` -> `text: unspecified, eol: unspecified` (no override), vs the SAME check on `app/server.py` -> `text: set, eol: lf` (explicit override). Read `infra/aws/ec2/opal-gateway/requirements.txt` as raw bytes on this worktree: 17 CRLF sequences, 0 bare-LF -- CRLF on disk, LF in the git blob (git always stores LF-normalized content for a non-binary path under autocrlf=true).",
        "deploy-to-ec2.sh builds its artifact with `tar -czf $ART -C $SRC ... app deploy requirements.txt identity_tool_allowlist.txt` (line ~69) -- `$SRC` is the literal WORKTREE CHECKOUT directory, so tar packages whatever autocrlf rendered on disk, not the git-stored (LF) bytes; only paths an explicit `.gitattributes` rule protects (only `*.py` -> `eol=lf`, measured) survive a Windows checkout unchanged.",
        "IMPACT CHECKED, NOT ASSUMED: `app/identity_scope.py:77` opens `identity_tool_allowlist.txt` in TEXT MODE (`open(path, \"r\", encoding=\"utf-8\")`), which universal-newlines-translates CRLF to LF per line before `.split()` ever runs -- so this file's CRLF does NOT corrupt its own parsing. `deploy/opal-gateway.service` demonstrably worked: the SAME deploy run's own on-box smoke (`systemctl restart opal-gateway` + `curl /health` + `/mcp` 401) succeeded this run (OGR1-AC2 PASS), so systemd tolerated the CRLF unit file this time. OGP1-AC1's OWN baseline (2026-09-15, the PRE-OG-r-1 deployed commit) recorded these SAME paths' host hashes as MATCH == tree (BASELINE.json OGP1-AC1 measurement, `deploy/opal-gateway.service` and `requirements.txt` both listed, denominator 50, digest_mismatch 0) -- so the corruption is NEW to THIS deploy, not a pre-existing, already-tolerated condition; the prior deploying box did not render CRLF for these paths."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C6: 'Pin Terraform, dependency lock and EC2 release artifacts using the existing Gateway release manifest/process. Measure declared/deployed parity on-instance via the normal SSM inspection.' OGR1-AC4: 'every deployed file's digest equals the build input's, file by file.'",
    "world_is": "9 of 68 deployed files are byte-different from their git blobs (CRLF vs LF) because deploy-to-ec2.sh tars the literal checkout directory and only .py carries an eol=lf .gitattributes override; on THIS deploying box (core.autocrlf=true) every OTHER text extension in the artifact rendered CRLF on checkout. OGR1-AC4 measures this truthfully as FAIL (9 mismatch). No functional break was found for the two paths checked closely (the allowlist parses in text mode; the systemd unit started), but exact byte parity -- the thing AC4 and PRD C6 both name -- is violated, and a future file needing byte-exact content (a checksum, a signature, a binary misclassified as text) would not get this same free pass.",
    "notes": "ARMED: a real defect in the release PROCESS (deploy-to-ec2.sh has no line-ending normalization and no full eol=lf .gitattributes coverage), reproducible on any Windows deploying box with autocrlf=true, not specific to this worker or this release's content. This cell cannot edit deploy-to-ec2.sh or .gitattributes (outside its <paths>) and did not attempt to (spec frozen; AC4 is reported FAIL with this true reason, not repaired). Remedy candidates for the owning cell: add `.gitattributes` `eol=lf` for the whole `infra/aws/ec2/opal-gateway/` tree (or at minimum `deploy/*.service`, `requirements.txt`, `identity_tool_allowlist.txt`), or have deploy-to-ec2.sh build its artifact via `git archive` (which always emits the repository's normalized bytes) instead of `tar -C $SRC` over the live checkout."
  },
  {
    "id": "NFRA_OPLGTW-W2-S9",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~2",
    "surfaced_at": "2026-09-18T07:10Z",
    "one_line": "Root-caused R-56 item 1's DRIFT-DANGEROUS finding: og_r1.py's own ac8() hardcoded L1's ledger proof text as literal 'OGR1-AC4 PASS (<commit>)' regardless of AC4's actual verdict (it was FAILED, 9/68 CRLF mismatch, at the time ac8() ran and wrote it), and ac8()'s own safe-commit call listed only `org/critical_paths/change_management/` as its commit path -- never the sentinel `org/critical_paths/.open_deploys/nfra-oplgtw-og-r-1-first-release.json` -- so `deploy_ledger.py close`'s real, correct on-disk sentinel deletion was never staged or committed. The result, verified at the bytes: commit 864aa6a9372a7137fbc20796190c530497d119f3 ('deploy-ledger(close...)') touches ONLY the .md entry (git show --stat: 1 file changed), while the sentinel stayed committed OPEN with all 3 legs unproven -- exactly the entry-vs-sentinel DRIFT-DANGEROUS state `deploy_ledger.py check` flagged and R-56 item 1 ruled on.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/probes/og_r1.py's ac8() (pre-this-run version, git show HEAD~1 or the R-56-amendment-era blob): `proofs = {\"L1\": \"OGR1-AC4 PASS (%s)\" % st.get(\"deploy_manifest_deployed_commit\", ...), ...}` -- an unconditional literal, never reading AC4's own recorded verdict; and `commit_paths = [\"org/critical_paths/change_management/\"]`, omitting the sentinel path entirely.",
        "RUN this turn: `git show --stat 864aa6a9372a7137fbc20796190c530497d119f3` -> '1 file changed, 8 insertions(+), 4 deletions(-)', only the .md entry -- the sentinel .json's real on-disk deletion (performed by the tool's own `close` call, which the log shows DID run: state.json carried a `ledger_close_commit` key) was left uncommitted in the worktree, matching exactly what the issuing COO's own message described finding and restoring via `git checkout --` before this run.",
        "RUN this turn: `py -3.12 .tools/deploy_ledger.py check` (before OGR1-AC20's fix) printed `DRIFT-DANGEROUS [WARN]: nfra-oplgtw-og-r-1-first-release entry reads terminal ('CLOSED -- nothing stranded -- closed 2') while leg(s) ['L1', 'L2', 'L3'] carry NO proof`, and the sentinel file (restored by the COO) was present on disk reading `status: OPEN`, `proof: null` on all three legs, confirming the .md's prior 'OGR1-AC4 PASS' claim was fabricated (AC4 has never once passed on this deploy)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md Rule 22a / the ledger tool's own doctrine: a leg's `proof` records what was actually checked, never a claim a criterion did not reach; 'NEVER leave a confirmed deploy half-landed... finish in-session' implies the close, once attempted, either fully lands (record AND sentinel agree) or is retried, never half-committed.",
    "world_is": "ac8()'s own code is the mechanism that produced R-56 item 1's DRIFT-DANGEROUS state: a fabricated PASS claim on a leg whose named criterion (AC4) was genuinely FAILED, paired with a commit_paths list that structurally could never commit the sentinel's deletion. OGR1-AC20 (this run) repairs the STATE through the tool with honest, non-fabricated per-leg proof text and a commit_paths list naming both the sentinel and the entry -- but ac8()'s own code is UNCHANGED and would reproduce the identical defect (fabricated proof + uncommitted sentinel deletion) if its `if \"ledger_close_commit\" not in st\" gate were ever re-entered (e.g. a fresh state.json, or the same pattern copied into a future cell's probe).",
    "notes": "ARMED: the specific instance (this ledger, this run) is DISARMED by OGR1-AC20's honest close, but the code pattern itself is untouched and latent -- this order's <paths> does not grant editing og_r1.py's ac8() beyond what AC19/AC20 required, and the order names only items (a)-(d) (AC20/AC19/AC4/AC9); fixing ac8() itself was not asked and is left to the issuing COO's disposition. Disarm by either patching ac8()'s L1 proof text to read AC4's actual recorded verdict (never a hardcoded PASS) and adding the sentinel path to its commit_paths, or by retiring ac8()'s bespoke close logic in favor of calling the same close path OGR1-AC20 now uses."
  },
  {
    "id": "NFRA_OPLGTW-S28",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T08:26Z",
    "one_line": "DISARM EVIDENCE for NFRA_OPLGTW-W2-S9 (the ARMED latent half of R-56 item 1): og_r1.py's ac8() no longer hardcodes L1's ledger-proof text and no longer omits the sentinel from its close-commit pathspec -- both defects are fixed in code at 1304801ca6, graded by the new OGR1-AC21 AGAINST THE FAILING CASE (AC4's real measured verdict False), and this issuer's own MUTANT control -- a scratch copy with both defects restored -- reads FAIL-OGR1-AC21, 1 of 4 checks OK, with each restored defect flipping its own named row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ the fix at the bytes: `git show 1304801ca6` -- `_l1_proof_text()` derives `word = \"PASS\" if ac4_ok else \"FAILED\"` from `st[\"ac4_ok\"]`, which only `ac4()`'s own run writes (`save_state` at og_r1.py's ac4(), same commit); `_ac8_close_commit_paths()` returns `[_sentinel_rel(), \"org/critical_paths/change_management/\"]`; and ac8() REFUSES outright (`return verdict(8, False, ...)`) when `ac4_ok` is absent from state.json rather than assuming one. There is no branch in the new helper that can emit PASS while `ac4_ok` is False.",
        "READ the recorded fact the derivation reads: evidence/og_r1/state.json at 1304801ca6 carries `\"ac4_ok\": false`, `\"ac4_verdict_utc\": \"2026-09-18T07:55:14.678528Z\"`, `\"ac4_denominator\": \"68 files (tree 68, host 68)\"`, `\"ac4_mismatch_counts\": {\"digest_mismatch\": 9, \"host_only\": 0, \"tree_only\": 0}` -- written by ac4()'s own run, not by hand.",
        "MUTANT CONTROL, run by 2.0.0_SA_COO~O (the ISSUER, not the worker) on a scratch copy `og_r1_MUTANT.py` in the same directory so REPO/state resolution is identical, with BOTH original defects restored in one copy (`word = \"PASS\"` unconditionally; pathspec back to `[\"org/critical_paths/change_management/\"]`): output `VERDICT: FAIL-OGR1-AC21`, `DENOMINATOR: 1 of 4 checks OK`. The per-row attribution is what makes it two controls rather than one union: arm 1 flipped rows 2 and 3 ('names AC4 as FAILED' NOT, 'does NOT name AC4 as PASS' NOT) and arm 2 flipped row 4 ('pathspec includes the sentinel path' NOT), while row 1 (AC4's verdict is FAILING) stayed OK in both. The mutant copy was deleted after the run (`git status --porcelain` clean of it).",
        "RUN by the issuer at the MERGED vintage (CLOUD @5e4ab26836, a DIFFERENT CHECKOUT from the worker's wk-nfra_oplgtw-2a, so this is corroboration and not repetition): `py -3.12 .tools/proof-of-spec-check.py <instance> OGR1-AC1..OGR1-AC21` -> `VALID (rc=0)`; invocation-alignment '21/21 comparable row(s) match modulo placeholder expansion; 0 diverge'. The instance's own acceptance array, denominator 21 of 21: AC4 FAIL, AC10 FAIL, AC9 N/A-BY-CONSTRUCTION, AC21 PASS, the other 17 PASS -- the two adjudicated failures are carried, not graded away.",
        "RUN by the issuer: `py -3.12 .tools/deploy_ledger.py check --all` -> `SCAN DENOMINATOR: 6 of 6 sentinel(s) scanned`; slug `nfra-oplgtw-og-r-1-first-release` no longer appears in any finding (the only finding is the unrelated, pre-existing `freshguard-leg4-writer-wiring-finish` HELD-STALE, another seat's). The DRIFT-DANGEROUS finding R-56 item 1 ruled on is gone from the tool's own read.",
        "RUN by the issuer, NEVER-2's union read across every live worktree (`git worktree list --porcelain` -> 13 worktrees; `git -C <wt> ls-tree -r --name-only HEAD org/critical_paths/.open_deploys/` plus an on-disk `ls`): the sentinel is committed=0 / ondisk=0 in CLOUD and in the worker's own worktree. THREE worktrees (verify-lt-n-2, wk-lgic-lgctfm-2-1, wk-lgic-lgctfm-2-2) still carry it committed=1 / ondisk=1 at their own older HEADs -- a STALE CHECKOUT, which is precisely the state NEVER-2's union clause exists to distinguish from an open deploy, and not evidence this ledger is open."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_OPLGTW-W2-S9's own disarm condition, quoted from its notes: 'Disarm by either patching ac8()'s L1 proof text to read AC4's actual recorded verdict (never a hardcoded PASS) and adding the sentinel path to its commit_paths, or by retiring ac8()'s bespoke close logic in favor of calling the same close path OGR1-AC20 now uses.' 1.0.0_SA_CTO ruling R-58 item 2 (msg 97876 @508eb695ca) adopted the first branch and bound its grading: 're-run ... WITH AC4 STILL FAILING. Against a passing case a hardcoded \"PASS\" and a derived \"PASS\" are byte-identical.'",
    "world_is": "The first branch is taken and proven. The code pattern W2-S9 called 'untouched and latent' is patched at 1304801ca6 and drained to CLOUD at 5e4ab26836; OGR1-AC21 grades it against AC4's REAL failing verdict, and the issuer's mutant control shows the criterion goes RED when either defect is restored -- so AC21 is a detector that can return non-zero on the positive case, which is the exact property the original ac8() lacked. W2-S9's hazard is therefore DISARMED. What is NOT disarmed and is NOT claimed here: NFRA_OPLGTW-W2-S8 (the CRLF/.gitattributes release-process defect that makes AC4 fail truthfully) stays ARMED and separate, and per R-56 item 3 its .gitattributes remedy is deferred to its own act with its own printed blast radius, never a rider on this cell; and NFRA_OPLGTW-W2-S7 (the previous release artifact failing the runbook's own restorability precondition, which is why AC10 fails) stays ARMED on its own terms.",
    "notes": "Filed INERT by the issuer as W2-S9's `disarm_owner` (2.0.0_SA_COO~O). This row is EVIDENCE for that disarm and carries no `adjudicates` key: disposing W2-S9 is the CVO's act at L9, not the issuer's, and a disarm asserted in prose disposes nothing. OG-r-1's `<status>` is `complete` at be38a0f475 under the order's own amended flip bound (R-58 item 1: the spine reads terminality from the PROOF, `.tools/surprise-row-gate.py:820-824` `_proof_terminal`, never from the status field), carrying AC4 and AC10 into L8/L9 as ADJUDICATED FAILS citing R-56 and AC9 as N/A-BY-CONSTRUCTION."
  },
  {
    "id": "NFRA_OPLGTW-S29",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T08:44Z",
    "one_line": "DISARM EVIDENCE for NFRA_OPLGTW-W2-S5 (BLOCKING): safe-ec2-deploy.sh's halt-gate identity redirect is repaired under R-53 and graded by OGR1-AC15/AC16/AC17/AC18, all four PASS in OG-r-1's VALID proof instance -- including the MUTANT (AC17: the old block restored in a scratch copy FAILS AC15's arm while AC16 still passes) and the audit-trail arm the CTO added (AC18). AND THE SIBLING IS EXPLICITLY NOT CLOSED: NFRA_OPLGTW-W1-S6 names a DIFFERENT caller (safe-apply) and stays ARMED -- this fix touched one caller's identity resolution, not the shared gate.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ OG-r-1's proof instance (org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/NFRA_OPLGTW.TO-OG-r-1.first-release-cutover.proof_of_spec.json) at CLOUD @5e4ab26836: OGR1-AC15 PASS 'REPO_ROOT resolved: C:/tmp/wk-oplgtw-2a SERIAL resolved: 0.9.0_WK_NFRA_OPLGTW~2 (rc=0)', denominator 2 of 2; OGR1-AC16 PASS (positive control, main-tree caller resolves identically pre- and post-edit), denominator 3 of 3; OGR1-AC17 PASS (MUTANT: the pre-R-53 block restored in a scratch copy -- AC15's arm FAILS under it, AC16's still passes, and the live file is byte-identical before and after building the mutant), denominator 3 of 3; OGR1-AC18 PASS (HALT_GATE_CONTEXT_FILE and HALT_GATE_AUDIT_LOG both still resolve under the MAIN tree), denominator 3 of 3.",
        "RUN by the issuer at the merged vintage from a DIFFERENT CHECKOUT than the worker's: `py -3.12 .tools/proof-of-spec-check.py <instance> OGR1-AC1..OGR1-AC21` -> VALID (rc=0), 21 of 21 comparable invocation rows match, 0 diverge. The four criteria above are inside that VALID instance, so their recorded evidence matches what each <expect> admits.",
        "WHY AC17 AND AC18 CARRY THE WEIGHT: AC15 alone would have passed a BARE --show-toplevel flip, which 1.0.0_SA_CTO measured as ALSO relocating HALT_GATE_AUDIT_LOG and HALT_GATE_CONTEXT_FILE into a worktree deleted at drain (R-53, msg 97843). AC18 is the arm this issuer's own three controls could not have produced, and it is the one that proves the fix did not move the override audit trail.",
        "NEGATIVE CONTROL ON THE SIBLING, run so this row does not overclaim: NFRA_OPLGTW-W1-S6 names OG-i-1's `safe-apply` run refused before terraform ran, NOT safe-ec2-deploy.sh. R-53's grant was scoped to 'infra/aws/ec2/safe-ec2-deploy.sh for the identity-resolution lines ONLY', so nothing in OGR1-AC15..AC18 exercises safe-apply's own identity gate. W1-S6 is therefore NOT disarmed by this row and stays ARMED."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_OPLGTW-W2-S5's own finding: safe-ec2-deploy.sh's worktree redirect points the halt-gate identity resolver at the SHARED MAIN TREE via git-common-dir before sourcing the gate, so a worker's session-serial file -- which exists only in the worker's own worktree -- is never found and the deploy fails IDENTITY UNRESOLVED. 1.0.0_SA_CTO R-53 (msg 97843) granted the repair and named its four controls.",
    "world_is": "The redirect is gone: HALT_GATE_REPO_ROOT now resolves to the CALLING worktree, the worker's own serial resolves (rc=0), the main-tree caller is unchanged, the old block still fails when restored, and the audit log and agent-context file still root in the main tree. Four criteria, one of them a mutant and one of them an arm added precisely because the issuer's own controls were blind to it, all PASS inside a VALID proof instance. W2-S5's hazard is DISARMED. The BLOCKING class is what makes this worth a row of its own: an ARMED BLOCKING row is the kind that stops an L10 slug, and this project has four orders left, so the distinction between 'fixed' and 'recorded as fixed' is about to matter.",
    "notes": "Filed INERT by the issuer as W2-S5's disarm_owner (2.0.0_SA_COO~O), EVIDENCE only, no `adjudicates` key -- disposing W2-S5 is the CVO's act at L9. THE DELIBERATE NON-CLAIM IS THE POINT OF THE LAST EVIDENCE LINE: W1-S6 shares this row's ROOT CAUSE (a worker-scoped fact looked up in the shared tree) but not its SURFACE, and a fix verified on one caller certifies nothing about the other. Disarming both on one instrument would be exactly the shared-dependency blindness Rule 22 names, run backwards. W1-S6 needs its own measurement against safe-apply's identity gate and is left ARMED for it."
  },
  {
    "id": "NFRA_OPLGTW-S30",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T09:12Z",
    "one_line": "DISARM EVIDENCE for SEVEN ARMED rows at ONE instrument: a per-module sweep of the ENTIRE Gateway test suite at HEAD's code vintage reads 26 modules, 25 GREEN, 1 RED -- and the one red is the KNOWN, RULED, PRE-PROJECT test of row NFRA_OPLGTW-S1 (test_scoped_deny_by_default), which every suite criterion in this issuance already deselects by name. Every test named as failing by W3-S7, W3-S13, W3-S16, W3-S17, W6-S10, W5-S19/W5-S20, S24 and S26 now PASSES, verified by exact node id where a row named one.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN by 2.0.0_SA_COO~O, per-module (one process each), at the worktree wk-oplgtw-2a whose Gateway code is BYTE-IDENTICAL to CLOUD HEAD (`git diff --stat be38a0f475 HEAD -- infra/aws/ec2/opal-gateway` prints NOTHING, so this measures HEAD's code): MODULE DENOMINATOR 27 files from `tests/*.py` + `tests/acceptance/test_*.py`, MINUS 1 conftest = 26 modules run. Results: acceptance/test_local_acceptance 14 passed; test_access_state 7; test_account_ref 5; test_attachment_tools 5; test_browser_oidc 7; test_data_entitlement_guard 12; test_entitlement_admin 9; test_identity_scope 1 FAILED 5 passed; test_jwt_cve_lock 6; test_min_tier_gate 3; test_oauth_durable 18; test_principal_cutover 11; test_ratelimit 6; test_schwab_asset_policy 3; test_schwab_audit 7; test_schwab_c3_rules 4; test_schwab_catalog 17; test_schwab_denial_envelope 2; test_schwab_engine 13; test_schwab_export 27; test_schwab_query 25; test_schwab_semantics 14; test_schwab_wiring 3; test_sprint_view 8; test_ssavail_contract 8; test_teams_format 35 (+34 subtests).",
        "THE ONE RED IS THE ONE ALREADY RULED, checked before being reported as a finding: `tests/test_identity_scope.py::test_scoped_deny_by_default` fails with `AssertionError: opal_data_refresh_upload`. Row NFRA_OPLGTW-S1 describes exactly this ('still lists opal_data_refresh_upload as denied to the Bloomberg service identity, while the tracked allowlist overlay grants that identity that tool'), and OGV2-AC4's own invocation deselects it by name -- `-k \"not test_scoped_deny_by_default\"` -- citing S1 and 1.0.0_SA_CTO msg 97114. MEASURED that it is NOT this project's: `git log --oneline -4` on app/identity_scope.py, tests/test_identity_scope.py AND identity_tool_allowlist.txt each returns the SAME single commit 2781aac326 (the repo rename), so no NFRA_OPLGTW cell has touched any of the three.",
        "WHY MY 26 AND OGV2-AC4's 25 ARE BOTH RIGHT: AC4's invocation globs `infra/aws/ec2/opal-gateway/tests/test_*.py`, which does NOT descend into `tests/acceptance/`. My sweep added `tests/acceptance/test_local_acceptance.py`. 26 = 25 + 1, and the extra module passes (14 passed). The denominators differ because the POPULATIONS differ, and both are printed rather than either being assumed.",
        "PER-ROW, at exact node ids where a row named one: W6-S10 / W5-S19 / W5-S20 named `test_schwab_query.py::test_ogq2_ac06` and `::test_ogq2_ac20` -- run by exact node id, `2 items collected, 2 passed` (a collected count of 2, so not a silent zero from a renamed test). W3-S16 named `test_principal_cutover.py::test_oga2_ac04` and W3-S7 named `test_jwt_cve_lock.py::test_control_valid_token_accepted` -- run together by exact node id, 2 collected, 2 PASSED. W3-S7 also named test_oauth_durable (14 of 18 red) -> 18 passed, and test_schwab_audit -> 7 passed. W3-S13 named 3 of 31 across three modules -> those modules are green. S24 and S26 named tests in tests/acceptance/test_local_acceptance.py -> 14 passed.",
        "W3-S17 IS CLOSED IN SUBSTANCE, NOT MERELY GREEN: its hazard was that OGA3-AC7 pinned the WHOLE route table at the cut base 7459929520, so any later cell adding a route would turn it red. The test's own current output reads 'base routes 27 (git object 7459929520: 27 declared, equal to the recorded table); served now 31; base routes still served unchanged 27 of 27, in base order, each path once; browser routes served 2 of 2' -- the criterion now compares the BASE SUBSET against a larger served set instead of demanding equality, which is the brittleness the row predicted, removed rather than accidentally satisfied.",
        "INSTRUMENT NOTE, and it cost this seat one abandoned run: a ONE-PROCESS whole-suite run (`pytest tests`) does NOT finish and shows errors in the acceptance tests that the per-module run does not reproduce. Row NFRA_OPLGTW-W3-S12 (INERT) already records this -- test_ratelimit.py freezes time.monotonic at import (row W3-S6) and a later module then waits on the event-loop clock. The channel being censused already held the answer to how to run the census. The per-module sweep is the project's own instrument (OGV2-AC4) and is the one used here."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Seven ARMED rows assert, each at its own earlier vintage, that a named Gateway test or module is RED: W3-S7 (16 tests across three modules after OG-a-2), W3-S13 (3 of 31 under the fixture-only grant), W3-S16 (test_oga2_ac04's route census), W3-S17 (test_oga3_ac07's pinned route table), W6-S10 with W5-S19 and W5-S20 (test_schwab_query's two pre-R20/R24 tests, FAILED-MODULES 1 at CLOUD @1529bcd131), plus S24 (conftest's pre-rename reader ARNs) and S26 (the a18 stale assertion).",
    "world_is": "At HEAD's code vintage every one of those named tests and modules is GREEN. The suite's only red is the pre-project, already-ruled, explicitly-deselected test of row S1, whose three files no cell of this project has touched. Each of those rows was true when written and each has been closed by a later cell's drain -- W6-S10 by TO-OG-q-6's, which had been reopened for exactly that test pair and had not yet drained at the vintage W6-S10 measured. THE COUNT DID NOT MOVE AND THE MEMBER DID: 'FAILED-MODULES: 1' reads the same at @1529bcd131 and here, but the failing module is a DIFFERENT one, so a reader carrying the old number forward would have carried the wrong member with it.",
    "notes": "Filed INERT by the issuer as the disarm_owner of all seven, EVIDENCE only, no `adjudicates` key -- disposing them is the CVO's act at L9. Deliberately NOT claimed here: W2-S7, W2-S8, W3-S1, W3-S9, W3-S22, W5-S18, W6-S3, W6-S6 and W6-S8 are not test-state rows and are untouched by this sweep; a green suite is not evidence about a permission gap, a rollback target or an email-keyed authorization decision. This row closes exactly the rows whose assertion was 'this test is red', and nothing else."
  },
  {
    "id": "NFRA_OPLGTW-S31",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T09:14Z",
    "one_line": "TWO CORRECTIONS THIS SEAT OWES ITS OWN ROWS, plus the structural reason the ARMED count will not fall no matter how much evidence this seat files: (1) my coverage census of which ARMED rows already carry an INERT disarm returned 4-of-23 on one instrument and 19-of-23 on the next, NEAR-INVERSE answers over the same file, because rows ABBREVIATE a row id after first mention and my first pattern demanded the full `NFRA_OPLGTW-` prefix; (2) row S29's closing sentence said W1-S6 'needs its own measurement', when row S18 -- this seat's own, filed earlier -- already made it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, both instruments over the SAME file at the same vintage, 23 ARMED and 96 INERT rows: instrument A required the FULL id (`NFRA_OPLGTW-W5-S20`) in an INERT row's JSON and returned 4 ARMED rows with a disarm claim, 19 without. Instrument B additionally admitted the SHORT form (`W5-S20`, word-bounded) and returned 19 ARMED rows mentioned by an INERT row, 4 not. Neither number is the answer to 'is it disarmed' -- a mention can be a sibling finding rather than a disarm -- but the point stands that the two sweeps disagreed by inversion. Concrete cause, verifiable in one read: row S27's one_line reads 'NFRA_OPLGTW-W5-S19, W5-S20 and W6-S10', full id ONCE and short form twice, so instrument A saw S27 as covering ONE row when it covers THREE.",
        "READ org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md, row NFRA_OPLGTW-S18 (INERT, filed by this seat): 'Disarm of NFRA_OPLGTW-W1-S6: the issuer provisioned the gitignored session serial file naming 0.9.0_WK_NFRA_OPLGTW~1 inside worker ~1's worktree. Run from that worktree, the halt gate moved from IDENTITY UNRESOLVED to resolving the worker...'. That IS the measurement against the halt gate's identity resolution that S29's closing sentence said was still owed.",
        "WHAT S29 GOT RIGHT AND KEEPS: its substantive claim -- that OGR1-AC15..AC18 exercise safe-ec2-deploy.sh ONLY, and that R-53's grant was scoped to that one file's identity-resolution lines, so nothing in those four criteria certifies safe-apply's own gate -- is unchanged and still the reason the two rows were not disarmed on one instrument. The error is narrower and in the opposite direction from an overclaim: it described as UNPAID a measurement this seat had already made, which would have sent a reader to redo it.",
        "THE STRUCTURAL FACT, read from the rollup's own definition line rather than inferred: `comp-surprise` prints 'ARMED (hazard still live: open, or graduated and not DISARMED) [by LATEST carrier: own row, then `adjudicates`, then remediation id]'. Every one of the 23 carries `disposition: UNDER_INVESTIGATION`, and an issuer's disarm-evidence row deliberately carries NO `adjudicates` key, because adjudicating is the CVO's act at L9 and a disarm asserted in prose disposes nothing. So NO quantity of issuer evidence lowers that count: 23 ARMED is a CVO-PLANE number, and reading it as 'work nobody has touched' is wrong in both directions at once."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md Rule 22: a printed denominator certifies the SWEEP, never the SET; and Rule 24(i)'s subtraction requires the domain to be the claim's population. A token census over a corpus whose members abbreviate their own references has a domain narrower than its claim, and prints a denominator anyway.",
    "world_is": "A census of row-to-row references cannot be run on the full id alone in this corpus, because the corpus's own convention is to abbreviate after first mention. The failure mode is the dangerous one: instrument A returned a SMALLER coverage number, which reads as conservative and would have driven this seat to re-file evidence for rows that already carry it -- wasted work that looks like diligence. The correction to S29 is an instance of exactly that: acting on the under-read, this seat wrote that a measurement was still owed when its own earlier row had made it.",
    "notes": "Filed INERT: neither correction changes any hazard's standing, and NOTHING in the record is rewritten -- S29 stands as committed (@1980f132bd) and this row is its correction, per the append-only discipline. Carried for the CVO at L9: when the 23 are dispositioned, the disarm evidence for a row may be reachable only through a SHORT-FORM reference in another row, so `_resolve_latest` over full ids alone will under-read this channel."
  },
  {
    "id": "NFRA_OPLGTW-S32",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T09:22Z",
    "one_line": "DISARM EVIDENCE for NFRA_OPLGTW-W3-S1, by a THREE-WRITER census rather than one read: the access-state table's key attribute names and TTL attribute are now pinned identically by all three writers of that property -- DECLARED in Terraform (`hash_key = \"pk\"`, `range_key = \"sk\"`, `access_state_ttl_attr = \"expires_at\"`), APPLIED on the live table (OGI5-AC4 PASS, describe-table, 5 of 5 properties), and EXERCISED by the adapter's own code. AND THE ROW'S TTL CLAUSE WAS NEVER FULLY TRUE: the contract DOES name TTL, at a different GRAIN -- its ROLE (`\"ttl\": \"cleanup_only_never_authorization\"`), not its attribute name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "WRITER CENSUS FIRST, because a property with N writers needs N rules read and N is a number this row prints: the key schema of `gateway-access-state-table` has THREE writers -- the Terraform that creates it (DECLARED), the live table itself (APPLIED), and the adapter code that reads and writes items (EXERCISED). All three were read; a single one would have been Rule 22's shared-dependency blindness.",
        "DECLARED -- READ infra/aws/terraform/opal-gateway/schwab_access_state.tf, `resource \"aws_dynamodb_table\" \"access_state_new\"`: `hash_key = \"pk\"`, `range_key = \"sk\"`, two `attribute` blocks (`pk` type S, `sk` type S), `ttl { attribute_name = local.access_state_ttl_attr, enabled = true }`, and that local resolves in the same file to `\"expires_at\"`. Also declared there and worth the record: `point_in_time_recovery` enabled, `server_side_encryption` enabled, PAY_PER_REQUEST, `deletion_protection_enabled = true` with the comment naming PRD C6 ('a table delete is never a rollback step').",
        "APPLIED -- READ the OG-i-5 proof instance (org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/NFRA_OPLGTW.TO-OG-i-5.access-state-rename.proof_of_spec.json), criterion OGI5-AC4, status PASS: 'SSE: ENABLED PITR: ENABLED Billing: PAY_PER_REQUEST TTL: ENABLED attribute=expires_at KeySchema: [{AttributeName: pk, KeyType: HASH}, {AttributeName: sk, KeyType: RANGE}]', denominator '5 of 5 live-read properties OK: SSEDescription, PointInTimeRecoveryStatus, BillingMode, TimeToLiveDescription, KeySchema'. That is a LIVE describe-table read, not a restatement of the Terraform, and TO-OG-i-5's own `<status>` reads `complete`.",
        "EXERCISED -- READ infra/aws/ec2/opal-gateway/app/access_state.py (24904 bytes): the literals `\"pk\"` and `\"sk\"` each appear, `expires_at` three times, and the two key namespaces the contract names appear as item-key prefixes (`RUNTIME#` 10, `POLICY#` 7). The code operates on the same three names the other two writers declare.",
        "THE ROW'S THIRD CLAUSE, CHECKED RATHER THAN CARRIED: W3-S1 says the contract does not name 'its TTL attribute'. READ org/standards/NFRA_OPLGTW_CONTRACT.json `state_store`: it carries `service`, `table` (gateway-access-state-table), `region`, `account`, 9 `record_types`, `consistency`, `\"ttl\": \"cleanup_only_never_authorization\"`, `key_namespaces` (POLICY and RUNTIME, with 'no TTL or ordinary delete' on POLICY), and `runtime_policy_access` ('write actions require all LeadingKeys match RUNTIME#*'). So the contract governs TTL's MEANING and the key-VALUE convention; what it does not carry is the three physical attribute NAMES -- a different grain from 'does not name the TTL attribute', and the distinction is the whole residual.",
        "OG-i-5 ALSO pins the namespaces against real data, which is why this is not merely a naming agreement: OGI5-AC6 PASS, 'old counts_by_namespace={OTHER#: 0, POLICY#: 7, RUNTIME#: 0, operator_audit: 4} new counts_by_namespace={identical}; key sets equal: True; digest mismatches: 0', denominator '7 of 7 (pk,sk) keys equal on both sides'. The migration compared items BY (pk, sk), so those attribute names are load-bearing in a passing criterion rather than incidental to one."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_OPLGTW-W3-S1: 'Neither OG-d-1's order, OG-i-1's order nor the contract names the access-state table's key attribute names, whether it has a sort key, or its TTL attribute; the adapter chose pk (HASH) + sk (RANGE) and expires_at' -- the hazard being an unwritten choice a later cell could silently contradict.",
    "world_is": "All three questions are answered by carriers that now exist and agree: there IS a sort key, it is `sk`, the hash key is `pk`, and the TTL attribute is `expires_at` -- declared in Terraform, applied on the live table and exercised in the adapter. A later cell cannot silently contradict them: the Terraform is the creating carrier and a PASSING live-read criterion in a COMPLETE order records what the table actually is. THE RESIDUAL, stated exactly and not more: the CONTRACT -- the cross-cell carrier a cell is most likely to read alone -- still carries none of the three names, so deriving them from the contract remains impossible and requires reading the Terraform. That is a SPEC question owned by 1.0.0_SA_CTO (the contract is an L4 artifact), not a hazard, and it is deliberately not being converted into one here.",
    "notes": "Filed INERT by the issuer as W3-S1's disarm_owner (2.0.0_SA_COO~O), EVIDENCE only, no `adjudicates` key -- disposing it is the CVO's act at L9. The row's own TTL clause is corrected rather than repeated: it asserted an absence that is a PRESENCE AT ANOTHER GRAIN, which is the failure mode where a claim is checked against the wrong level of the same object. Nothing in W3-S1 is rewritten; it stands as filed and this row is its evidence. NOT claimed: this says nothing about whether the POLICY/RUNTIME namespace split is correctly ENFORCED by IAM -- that is the `runtime_policy_access` LeadingKeys condition, a different property with its own writers, and no criterion cited here exercises it."
  },
  {
    "id": "NFRA_OPLGTW-S33",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T10:12Z",
    "one_line": "MEASUREMENT SUPPLIED TO 1.0.0_SA_CTO for the three ARMED rows it owns that assert a live wiring gap -- W6-S6 (additivity/grouping never called), W6-S8 (dim_asset CUSIP restriction not wired) and W5-S18 (MCP isError left falsy on a guard denial): all three are CLOSED IN BEHAVIOUR at HEAD, each by the cell cut for it (OG-q-4, OG-q-5, OG-z-4), proven by the A-row tests that still carry the ORIGINAL assertions against an INDEPENDENT expectation file that was NOT weakened. ONE NUANCE THAT A CALL-COUNT ALONE WOULD GET WRONG IN BOTH DIRECTIONS, and one stale comment that now asserts a defect that no longer exists.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W6-S6 -- THE NUANCE, and it is the reason this row exists. The row names three functions as never called from the query path: `assert_sum_allowed`, `assert_quantity_sum_grouped`, `assert_field_summable`. CENSUS over a WALKED denominator (app 59 .py files, tests 30 .py files): `assert_quantity_sum_grouped` x2 in query.py, `assert_field_summable` x2 in query.py -- both now wired. `assert_sum_allowed` has ZERO callers in either tree; its only two occurrences are in semantics.py, one of them its own definition. THAT IS NOT AN UNENFORCED RULE. READING ITS BODY (semantics.py:273-279) shows it is a COMPOSER: it calls `assert_field_summable`, `assert_quantity_sum_grouped` and `assert_single_balance_metric` in order. The third constituent was censused on its own and is ALSO called from query.py (x2). So all three constituent checks are wired DIRECTLY and the composer is REDUNDANT DEAD CODE -- the rule it would enforce is enforced. A verdict from the call count alone would have said 'still not wired' (wrong) or, had the count been nonzero, 'wired' without ever checking what it composed (also wrong). The discriminator was reading the FUNCTION BODY, not counting its callers.",
        "W6-S6 -- THE BEHAVIOUR, which is what the row actually asserts: `tests/acceptance/test_local_acceptance.py::test_ogv2_a08` PASSES at HEAD and still carries the original case literally -- a request labelled `\"sum closing_price (nonadditive)\"` over `dim_asset` with `aggregates: [{function: sum, field: closing_price}]`, asserted with `assert is_error, (label, payload)` and `assert got_refusals[label] in want_refusals[label]`. The nonadditive SUM the row says is NOT refused IS refused.",
        "W6-S8 -- MECHANISM, read at the bytes rather than inferred from a green test: app/integrations/schwab/integration.py:597-618 now performs a qualified POSITION-snapshot read solely for policy selection (`pos_accounts = tuple(sorted(scope.accounts.get(q.master, ())))`, `QueryPlan(..., policy_filters=(PolicyFilter(qry.ACCOUNT_SOURCE, pos_accounts),))`), and its own comment cites `NFRA_OPLGTW.TO-OG-q-5 (row NFRA_OPLGTW-W6-S8)` and PRD C3 by name. `asset_policy` is no longer the presence-only sentinel the row measured.",
        "W6-S8 -- THE R-56 CHECK, because a passing test is not evidence until you know the expectation was not moved to meet it: `test_ogv2_a06` asserts `got_cusips == want_cusips` where `want_cusips = EXPECTED[\"cases\"][\"A6-partial-grant-asset-cusips\"][\"expect\"][\"dim_asset_cusips\"]` -- an INDEPENDENT file, not a literal in the test. READ tests/acceptance/expected/EXPECTED.json: that value is still exactly `[\"SYN000001\", \"SYN000002\"]` with `\"excluded\": [\"SYN000003\", \"SYN000009\"]` and the rule restated ('a partial-account grant restricts dim_asset to the CUSIPs its accounts hold on the same master/date'). The row reported all FOUR being returned. The expectation is UNCHANGED and the app now matches it.",
        "W5-S18 -- `test_ogv2_a06`'s tail still asserts the exact property the row says is missing: `assert is_error, payload` followed by `assert payload[\"error_code\"] == \"ENTITLEMENT_DENIED\", payload` on a post-revocation query, with an in-test comment naming the fix ('OG-z-4 wired the dispatch guard (app/tools.py) to set isError=True on a guard denial'). PASSING at HEAD.",
        "VINTAGE, so this is not read at the wrong one: measured in worktree wk-oplgtw-2a, whose TRACKED Gateway content is byte-identical to CLOUD HEAD -- `git diff --stat be38a0f475 HEAD -- infra/aws/ec2/opal-gateway` prints NOTHING, re-run at HEAD b64a188d82 after CLOUD moved past the vintage of row S30's sweep. The source reads above were taken from the MAIN tree at that same HEAD."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_OPLGTW-W6-S6, W6-S8 and W5-S18 each assert, at their own earlier vintages, that a PRD C3 rule with a correct and unit-tested implementation is not reachable from any live query path -- the 'proven where nothing calls it' class this project has now met five times.",
    "world_is": "All three rules are enforced on the live path at HEAD, each by the cell cut for it, and each proven by an A-row test whose assertion and whose independent expectation are both UNCHANGED from when the row was filed. What survives is NOT a gap but a residue: `assert_sum_allowed` is a redundant composer with zero callers whose three constituents are individually wired, so it is dead code rather than an unenforced rule. Deleting it or re-pointing query.py at it is a judgment for the owning seat; leaving it is safe and leaving it UNDOCUMENTED is how a future census re-derives the alarm this row just retired.",
    "notes": "THE DISARM IS NOT THIS SEAT'S TO MAKE: all three rows carry `disarm_owner: 1.0.0_SA_CTO`. This row supplies the measurement so that decision is one read, and claims no disarm. A SEPARATE, SMALLER FINDING that belongs to whoever next edits the acceptance harness: the comment immediately ABOVE a06's now-passing CUSIP assertion still reads '...this restriction is not wired on any path this harness can reach'. That was true when written and is FALSE at HEAD -- a descriptive comment that survived the fix it describes, sitting on top of the assertion that disproves it, which is precisely the shape that makes a later reader trust the comment over the code. Not repaired here: tests/acceptance/test_local_acceptance.py is outside this lane's act for this tick and the fix belongs with whichever cell next opens that file."
  },
  {
    "id": "NFRA_OPLGTW-S34",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T10:41Z",
    "one_line": "MEASUREMENT SUPPLIED TO 1.0.0_SA_CTO for NFRA_OPLGTW-W6-S3, whose disarm is a RULING and not a measurement: the implementation has already taken the NARROW reading -- the catalog HEADs only the dataset (dim) objects a closure names and makes ZERO S3 calls under any fact_ key -- and that is ENFORCED by `tests/test_schwab_catalog.py::test_ogk1_ac17` in BOTH arms, which asserts the CALL LOG rather than the answers. THAT CHOICE OF INSTRUMENT IS EXACTLY THE ANSWER TO THE ROW'S OWN OBJECTION: an IAM-free emulator answers a HEAD identically, but it cannot mask a call that was never issued.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN by 2.0.0_SA_COO~O at HEAD's Gateway code vintage, by EXACT node id (1 collected, so not a silent zero from a renamed test): `tests/test_schwab_catalog.py::test_ogk1_ac17` -> `1 passed`. Its own printed output: 'CLOSURE sha256:e08876780f0a169c names 7 object(s): 3 dim, 4 fact'; four lines 'fact named, never read: schwab/08242234/silver/fact_{rld,rps,rps_s2,sec}/date=2026-07-10/data.parquet'; 'ARM 1 (all objects present): status=complete, 3 file(s) on dims, 0 of 4 S3 calls under a fact_ key'; 'ARM 2 (one DIM object deleted, same closure_id): status=incomplete classes=(VERSION_UNAVAILABLE,), 0 S3 call(s) under a fact_ key'.",
        "READ the test at the bytes (test_schwab_catalog.py:1135-1177) rather than trusting its printed line: `touched_facts = [c for c in world.log.s3_calls() if \"/silver/fact_\" in (c[\"key\"] or \"\")]` then `assert touched_facts == []`, and the identical pair again on the incomplete arm (`touched_facts_2`). The property is asserted on BOTH the success path AND the failure path -- the failure path being where an implementation would most plausibly widen its search.",
        "THE POSITIVE CONTROL IS IN THE TEST ITSELF, which is what stops the zero being vacuous from the fixture side: `assert fact_keys` at :1143, with the comment 'the fixture's qualified closure does name fact objects'. A fixture that stopped naming fact objects would make the whole criterion trivially true, and that assertion refuses it.",
        "THE LOGGER IS NOT DEAD, checked because an empty input set returns a vacuous pass: `world.log` is a botocore `before-parameter-build` event hook registered on the client (:192), it is reset per arm by `world.log.start()`, and a SEPARATE test in the same module asserts the instrument records non-zero -- `assert len(world.log.s3_calls()) > 0` at :541. Within ac17 the snapshot demonstrably did work on the same log (status complete, 3 dim files served), so the fact-key zero is a scoped zero, not an absent recording.",
        "THE GRANT SIDE IS UNCHANGED, so the row's premise still holds and only its consequent is unreachable: the acceptance harness's own printed denominators at this vintage read 'DATA ROLE HEAD+GET: 69 call(s) over 18 distinct key(s); 18 of 18 under the 6 data_prefixes read from NFRA_OPLGTW_CONTRACT.json' and 'CATALOG ROLE: 14 distinct key(s); 14 of 14 under the 2 completion_prefixes'. Six dim prefixes and two completion prefixes, exactly as W6-S3 describes."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_OPLGTW-W6-S3: 'The catalog independently HEADs every named silver object (PRD C3), under read grants limited to the six dim prefixes and the two completion prefixes (PRD C6)' -- and its hazard: if the catalog HEADs every named object then in AWS each fact HEAD is AccessDenied and every date reads unavailable, which a local emulated bucket without IAM would not reveal.",
    "world_is": "The catalog does NOT HEAD every named object: it reads the dataset objects and issues no S3 call at all under a fact_ key, in both the complete and the incomplete arm. So the AccessDenied-in-AWS hazard cannot arise from this implementation, and a regression toward the broad reading would turn ac17 RED rather than passing locally and failing live -- which is the specific failure mode W6-S3 was filed to prevent. WHAT IS NOT ANSWERED HERE, and is the whole of what remains: whether the narrow reading is the CORRECT reading of PRD C3's 'every named silver object'. That is a ruling, the row names 1.0.0_SA_CTO as its disarm_owner for exactly that reason, and this seat does not make it. The row's own note that 'the fixtures carry both object classes, so either ruling can be tested' remains true and is confirmed by the 3-dim/4-fact closure above.",
    "notes": "Filed INERT as MEASUREMENT for the owning seat, no `adjudicates` key, no disarm claimed -- W6-S3 is 1.0.0_SA_CTO's. The transferable part is the instrument, not the verdict: W6-S3's objection was that a local run cannot discriminate here because 'an emulated bucket without IAM answers the same HEADs'. That is true of any assertion about the RESPONSE and false of an assertion about the REQUEST. Counting the calls the code ISSUES, per access key, through a botocore hook is immune to the emulator's permissiveness, and it is the same shape as the harness's ambient-key control ('AMBIENT KEY: 0 of 159 calls') already used elsewhere in this module. A LOCAL TEST CAN BOUND A LIVE IAM OUTCOME WHEN IT ASSERTS WHAT WAS ASKED RATHER THAN WHAT WAS ANSWERED."
  },
  {
    "id": "NFRA_OPLGTW-S35",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T10:58Z",
    "one_line": "NOT A DISARM -- THE OPPOSITE. NFRA_OPLGTW-W3-S22 (ARMED, disarm_owner 1.0.0_SA_CTO) rests its harmlessness on a condition that HAS NOW LAPSED: it says the Daily-Sprint email-identity gap is 'harmless while no restricted profile exists (OG-z-2 creates the first one) and nothing is deployed'. TO-OG-z-2 reads `complete` and OG-r-1 DEPLOYED the release. The roster remedy the row named is now BUILT (`SPRINT_VIEW_ALLOWED_EMAILS`) -- and its DEFAULT IS OPEN BY RULING: an empty roster admits every signed-in tenant account, so building it did not close the gap.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE LAPSED CONDITION, both halves read rather than recalled: `org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-z-2.entitlement-admin.md` carries `<status>complete</status>`; and OG-r-1 performed a real deploy (the probe's own state.json records `deploy_finished_utc` 2026-09-18T05:58:38Z with a deployed commit, and OGR1-AC2's on-box smoke -- systemctl restart plus /health plus /mcp 401 -- PASSED). Both clauses of the row's 'harmless while' are therefore spent.",
        "THE REMEDY EXISTS NOW AND DID NOT WHEN THE ROW WAS FILED: W3-S22 listed three possible closures, all outside its own order's grant -- 'a SPRINT_VIEW_ALLOWED_EMAILS roster (config), an ALB rule, or an email-keyed deny index'. A WALK of 123 files under infra/aws/ec2/opal-gateway finds `SPRINT_VIEW_ALLOWED` in exactly two: `app/config.py` (x2) and `app/sprint_view.py` (x2). The first one is built.",
        "BUT ITS DEFAULT ADMITS EVERYONE, AND THAT IS DELIBERATE, NOT AN OVERSIGHT -- READ app/sprint_view.py:173-175: `def _allowed(email): roster = _cfg.SPRINT_VIEW_ALLOWED_EMAILS; return True if not roster else email in roster`. An EMPTY roster returns True for every caller. app/config.py:99-105 states the intent in its own comment: 'The roster is EMPTY = every signed-in tenant account may view (ruled tenant-wide); a comma list narrows it -- a config act, never a code act', and the value is read from the environment with a `\"\"` default. So the mechanism's existence is not evidence of the hazard's closure; only a NARROWED value would be.",
        "THE ROUTES ARE SERVED BY THE RELEASE, so this is not about dead code: test_browser_oidc's own OGA3-AC7 output at this vintage reads '/login, /sprint, /sprint/archive without the access-layer header -> 401 (3 of 3)' alongside 'served now 31' routes -- the access-layer routes W3-S22 names are present and reachable behind the ALB header.",
        "WHAT THIS ROW DOES NOT MEASURE, named so the gap is not mistaken for a claim: (1) whether the DEPLOYED environment narrows the roster -- `deploy/opal-gateway.service` takes `EnvironmentFile=/opt/opal-gateway/.env`, which is ON THE BOX and not in this repo, so the effective value of SPRINT_VIEW_ALLOWED_EMAILS in production is UNREAD here and is an on-host read; and (2) whether any RESTRICTED PROFILE actually exists in the live access-state table -- TO-OG-z-2 being `complete` proves the admin capability was built, never that a profile was minted, and OGI5-AC6's migration count (POLICY# 7) does not break out profile kinds. Either one being favourable keeps the hazard latent; neither has been read."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_OPLGTW-W3-S22's own notes: 'ARMED: harmless while no restricted profile exists (OG-z-2 creates the first one) and nothing is deployed. Once a restricted profile is live, the Daily Sprint pages are readable by its holder unless a roster is configured.' The row's ARMED standing was sized against a world in which neither had happened.",
    "world_is": "Both of those conditions have moved since the row was written: the order that creates restricted profiles is complete and the release is deployed. The roster the row names as the closure is built but ships OPEN by an explicit ruling, so its presence changes nothing about the hazard by itself. The row's ARMED standing is therefore MORE justified than when it was filed, not less, and the two facts that would settle it -- the deployed .env's roster value and whether a restricted profile exists live -- are both UNREAD. The timing is the reason this is worth a row now rather than at L9: OG-v-4 and OG-v-5 put real people in front of this release, and this is the kind of question that should be answered BEFORE a walkthrough rather than discovered during one.",
    "notes": "Filed INERT and pointing AT W3-S22 rather than duplicating its hazard: one hazard, one disarm_owner, and that owner is 1.0.0_SA_CTO. W3-S22 stays ARMED and this row is the reason it should not be closed on the observation that 'the roster now exists'. This seat makes no ruling and proposes none: whether tenant-wide Daily-Sprint visibility is acceptable while a restricted profile is live is precisely the judgment W3-S22 reserves to its owner. NOT DONE HERE, deliberately: no on-host read of /opt/opal-gateway/.env and no live read of the access-state table were performed for this row -- both are the owner's to order, and neither is needed to record that the harmlessness clause has lapsed."
  },
  {
    "id": "NFRA_OPLGTW-S36",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T11:06Z",
    "one_line": "THE LIVE ACCESS-STATE TABLE HOLDS THREE RECORDS WHOSE OWN `record_type` IS `principal_profile` -- statuses pending, pending and revoked -- STORED AT SORT KEY `PROFILE`, while the deployed code derives its sort key FROM the record type (`access_state.py:122`) and therefore looks for `principal_profile`. So the table contains three profiles and the guard can see NONE of them. Found while executing 1.0.0_SA_CTO's ordered read for W3-S22 (msg 97923): the first read, filtered on the sort key the code uses, returned Count 0 -- THE RIGHT ANSWER FOR THE APP AND THE WRONG ANSWER TO THE QUESTION ASKED.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN by 2.0.0_SA_COO~O against the LIVE table (`gateway-access-state-table`, us-east-1, account 313476888478 per the contract's `state_store`), read-only: `dynamodb scan --select COUNT --filter-expression \"sk = :s\"` with `:s = principal_profile` -> `Count: 0, ScannedCount: 8`. The ScannedCount is the built-in positive control -- the table is not empty and the scan did read items.",
        "NEGATIVE CONTROL, which is the only reason this was found: a second scan projecting `sk` ALONE (no partition key, so no tid/oid is read) returned 8 items whose sort keys are `PROFILE` x3, `AUDIT#0001` x3, `AUDIT#0002` x1, `AC9` x1. NOT ONE of them is `principal_profile`, and the documented shapes (`principal_profile`, `data_entitlement#<10 digits>`) do not appear at all.",
        "THIRD READ, projecting only NON-IDENTIFYING attributes (`sk, record_type, profile_kind, status, revision` -- deliberately not `pk`, `tid`, `oid` or `email`): the three `sk=PROFILE` items each carry `record_type: \"principal_profile\"`, with `status` pending / pending / revoked and `revision` 1 / 2 / 2. The four AUDIT items carry `record_type: \"operator_audit\"`. The `AC9` item carries NEITHER a record_type nor a status -- it has no attribute this projection names at all.",
        "THE CODE'S SHAPE, read at the bytes: `app/access_state.py:122` builds the sort key as `sk = \"#\".join((record_type,) + parts)`, so a profile's sort key IS its record type -- `principal_profile`. `app/data_entitlement.py:57` sets `PROFILE = \"principal_profile\"` and its module docstring (:7) states 'principal_profile sort key `principal_profile`'. `client.get_item(... Key={PK: k.pk, SK: k.sk} ...)` at :319 is an exact-key read, so a record at `PROFILE` is not merely deprioritised -- it is UNREACHABLE.",
        "THE CURRENT SHAPE IS THE VERIFIED ONE, so this is residue rather than a code defect: OG-z-1's `OGZ1-AC1` reads PASS with the evidence 'principal_profile key pk=POLICY#<tid>#<oid> sk=principal_profile (no email in the key); data_entitlement key sk=data_entitlement#0000000001 in the same partition; statuses seen pending -> active -> revoked at revisions 1 -> 2 -> 3'. The deployed code and the contract agree with each other and disagree with the live rows.",
        "PROVENANCE IS INFERRED, NOT MEASURED, AND IS LABELLED AS SUCH: OG-i-5 migrated this table's contents wholesale and its `OGI5-AC6` compared items BY `(pk, sk)` with '7 of 7 keys equal on both sides, 0 digest mismatches' -- a faithful copy makes no claim about whether the copied SHAPE matches the reader. The most likely reading is pre-OG-z-1 records carried across the rename; a bare `AC9` sort key beside them suggests probe residue. NOTHING HERE MEASURES WHO WROTE THEM OR WHEN."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C2 / the contract's `state_store` and `app/data_entitlement.py`:24, which is the definition the W3-S22 ruling turns on: 'a principal with ANY profile record -- pending, active or revoked -- is restricted'. And `access_state.py`:118-122: a POLICY record's sort key is its record type.",
    "world_is": "Both halves of that definition are true of the live table and they disagree. BY THE CONTRACT'S WORDS three restricted profiles exist. BY THE DEPLOYED CODE'S KEY none of them exists, because the guard reads an exact key that no stored row carries. TWO CONSEQUENCES POINTING OPPOSITE WAYS, and both belong to the owner: (1) FOR THE W3-S22 RULING, whose trigger is 'the moment a restricted profile exists the empty roster is a defect' -- the app sees zero, so tenant-wide Daily-Sprint visibility remains acceptable on the ruling's own terms TODAY, but it is acceptable for a reason nobody chose, and the day a profile is minted through the CURRENT path the trigger fires. (2) FOR THE GUARD -- if any of those three rows names a REAL principal, that principal is treated as an ordinary full-access tenant account, including the one recorded `revoked`, which is the fail-open direction. WHETHER THEY NAME REAL PRINCIPALS IS UNREAD BY CHOICE: reading it means projecting `tid`/`oid`/`email` off a live policy table, and that is the owner's to order, not this lane's to take.",
    "notes": "ARMED, disarm_owner 1.0.0_SA_CTO: this bears directly on that seat's own W3-S22 ruling (msg 97923 @3633d45bdc) and on PRD C2's policy model, and its disarm needs a PROVENANCE determination -- residue to delete, or records to migrate to the current key -- which is an identity read this lane did not take. DELIBERATELY NOT CLAIMED: no assertion that the deployed guard is broken (its shape is the verified one), and no assertion that a real principal is exposed (unread). THE TRANSFERABLE PART IS THE METHOD, because the first read was the natural one and was wrong: FILTERING ON THE KEY YOUR CODE USES ANSWERS 'WHAT DOES MY CODE SEE', NEVER 'WHAT IS IN THE TABLE'. A Count of 0 with a ScannedCount of 8 is a complete answer to the first question and silence on the second. The projection of the sort keys ALONE -- one extra call, no identifier read -- is what turned a clean zero into three profiles."
  },
  {
    "id": "NFRA_OPLGTW-S37",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T11:14Z",
    "one_line": "S36's PROVENANCE IS SETTLED AND ITS ALARMING BRANCH IS CLOSED, with NO identifier read: the three `sk=PROFILE` records are OG-i-1's OWN ACCEPTANCE PROBE's fixtures, written under SYNTHETIC partition keys `POLICY#probe-og-i1-<utc stamp>`, so no real principal is named and nothing is failing open. TWO THINGS REMAIN AND NEITHER IS THE ONE I FILED S36 FOR: the probe exercised a KEY SHAPE THE APPLICATION NEVER USES, and its residue is NOT REMOVABLE BY ANY ROLE THIS PROJECT GRANTS -- the probe's own DeleteItem is AccessDenied BY DESIGN -- so every future run adds more rows to a live policy table.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PROVENANCE, found by a WALK of 314 files across the project tree and the gateway rather than by guessing: exactly one executable carries the literal `\"PROFILE\"` as a sort key -- `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~1/probes/og_i1.py`, 8 occurrences, plus 5 of `AUDIT#`. No other probe, no app module, and no test carries it.",
        "AND THE APP NEVER DID, at any vintage: `git log -S'\"PROFILE\"' -- infra/aws/ec2/opal-gateway/app/access_state.py` and the same on `app/data_entitlement.py` both return NOTHING, over a file whose entire history is two commits (`0c4a5edcd0` the adapter, `63f0ccec7d` the i-5 rename). So this was never a legacy shape the app outgrew -- the application has only ever written `sk = record_type`.",
        "THE WRITE SITES, read at the bytes: og_i1.py:244-249 `transact_write_items` puts `{\"pk\": {\"S\": pk}, \"sk\": {\"S\": \"PROFILE\"}, \"record_type\": {\"S\": \"principal_profile\"} ...}` alongside an `AUDIT#0001` item; :462 sets `pk = \"POLICY#probe-og-i1-%s\" % stamp()`; :466-473 runs a second transaction updating that `PROFILE` item and appending `AUDIT#0002`. The module docstring :32 declares the intent outright: 'Writes: only isolated RUNTIME#probe-og-i1-<utc> and POLICY#probe-og-i1-<utc> items, and only once the table exists.'",
        "SO THE FAIL-OPEN BRANCH OF S36 IS CLOSED WITHOUT READING A SINGLE IDENTIFIER: the partition keys are `POLICY#probe-og-i1-<stamp>`, a synthetic namespace no Entra principal can occupy (a real one is `POLICY#<tid>#<oid>`). The `revoked` record that would have been the sharp end is a probe's second revision of its own fixture. NOTE THE SHAPE OF THIS RESOLUTION: the question 'is a real principal exposed' was answered from the WRITER's source, not from the stored rows, which is why no `tid`, `oid` or `email` was ever projected.",
        "THE RESIDUE IS PERMANENT BY DESIGN, which is why three runs' worth is still there: og_i1.py:481-485 attempts `delete_item` on its own `PROFILE` fixture and RECORDS `AccessDeniedException` AS A PASSING CRITERION -- the operator role is deliberately denied DeleteItem on POLICY records, matching the contract's `key_namespaces.POLICY` ('operator writes only; no TTL or ordinary delete'). The probe cannot clean up after itself, and that is the durability property working exactly as specified. Counted live: 3 `PROFILE` + 3 `AUDIT#0001` + 1 `AUDIT#0002` + 1 `AC9` = 8 items, consistent with roughly three runs of a probe that writes one or two POLICY items per run."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NFRA_OPLGTW-S36 asserts that three records whose `record_type` is `principal_profile` sit at a sort key the deployed guard cannot read, and names two unresolved branches: residue-versus-defect, and whether any of them names a REAL principal. The contract's `state_store.key_namespaces.POLICY` states 'operator writes only; no TTL or ordinary delete'.",
    "world_is": "RESIDUE, definitively, and probe residue rather than legacy drift. No real principal is named, the guard is not failing open, and S36's alarming branch is closed. What is left is smaller and durable, and neither half is a defect in the deployed guard: (1) OG-i-1's live acceptance evidence exercised IAM conditions and operator-transaction semantics against a record shape (`sk=PROFILE`) that the application NEVER writes -- the `POLICY#*` LeadingKeys conditions it proved are shape-independent and so still generalise, but the record-level half of that evidence was taken on a synthetic shape; (2) the live policy table now carries 8 probe rows that NO role this project grants can remove, and each future acceptance run of og_i1 adds more. A cleanup is therefore not a matter of running a delete -- it needs a principal outside the project's own grants, which makes it a deliberate act with an owner rather than housekeeping.",
    "notes": "Filed INERT: this row CLOSES the branch S36 was ARMED for. S36 itself stays ARMED and its disposition remains 1.0.0_SA_CTO's -- an issuer's evidence row disposes nothing, and the residual items above are the owner's to weigh. WHAT THIS ROW DELIBERATELY DOES NOT DO: propose deleting the probe rows (out of any grant this project holds, and a delete on a policy table is not housekeeping), change og_i1.py (its AccessDenied assertion is CORRECT and load-bearing), or claim the i-5 migration erred (it copied faithfully by (pk, sk), which is what it promised). THE METHOD IS THE CARRY: a provenance question about rows in a live policy table was settled entirely from the WRITER'S SOURCE plus git history -- 314 files walked, one executable found, two `git log -S` reads returning empty -- so the identity read S36 named as the disarm's critical path turned out not to be on the critical path at all."
  },
  {
    "id": "NFRA_OPLGTW-S38",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T11:22Z",
    "one_line": "CORRECTING THIS LANE'S OWN S35/S36 FRAMING: OG-r-1 did NOT create the tenant-wide Daily-Sprint exposure, it INHERITED it. The PRE-OG-r-1 deployed commit 7bd89b5d71 ALREADY carries app/sprint_view.py, so the /sprint routes have been live since that release (2026-09-09) and a CTO log inventories them as deployed on 2026-08-28. W3-S22's 'nothing is deployed' clause was therefore ALREADY SPENT WHEN THE ROW WAS WRITTEN 3.3 DAYS AGO -- it did not lapse at 05:58Z today. AND THE SENTINEL ACT HAS A MISSING INPUT NOBODY HAS NAMED: no roster VALUE exists anywhere in the estate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN, with BOTH controls firing so the instrument is shown to discriminate: `git cat-file -e 7bd89b5d71b8d488d9e8c4168513193c9d6a9ec2:infra/aws/ec2/opal-gateway/app/sprint_view.py` -> rc=0, PRESENT. POSITIVE CONTROL `app/server.py` at the same commit -> PRESENT. NEGATIVE CONTROL `app/data_entitlement.py` at the same commit -> ABSENT, which matches 1.0.0_SA_CTO's own R-56 measurement of that commit exactly. A bare presence read would have proved nothing; the pair shows the read distinguishes.",
        "7bd89b5d71 IS the pre-OG-r-1 deployed commit, not an arbitrary one: row NFRA_OPLGTW-W2-S7 records it as `EC2_MANIFEST.json services.opal-gateway.deployed_commit`, deployed_at 2026-09-09T19:08:11Z. So the code serving /sprint was on the box for nine days before this project's release.",
        "AND EARLIER STILL, from a record outside this project: `org/tier1_exec/1.0.0_SA_CTO/logs/2026-08-28/ctoD_daily_sprint_web_client_and_grep_gate_audit_1722-1923Z.md` inventories 'Gateway code: infra/aws/ec2/opal-gateway/app/sprint_view.py (+ server.py GuardMiddleware branch for /sprint*, config.py DAILY_REPORTS_* / SPRINT_VIEW_ALLOWED_EMAILS); deployed to i-07dccb1615503ac99 /opt/opal-gateway'. The roster config option and the routes shipped together, three weeks before W3-S22 was filed.",
        "NO ROSTER VALUE EXISTS ANYWHERE, measured UNSCOPED rather than in the places it ought to be: `comp-find 'SPRINT_VIEW_ALLOWED_EMAILS'` over the whole corpus returns 36 hits across 167,676 files scanned (68,640 ephemeral-floor, 11 unreadable, 4,880 binary not searched). Bands: SURFACED 8, CONFIG 6, DOC 22. Every SURFACED hit is `app/config.py`, `app/sprint_view.py` or this lane's own scratch files; the only CONFIG hit is this lane's own scratch json. NO Terraform, NO .env template, NO runbook and NO deliverable names a value or an intended audience -- and the 2026-08-28 CTO log names the option without naming who belongs on it.",
        "THE DEPLOYED HOST AGREES, from the read already ordered and taken: /opt/opal-gateway/.env carries 22 keys and KEY_PRESENT=0 for SPRINT_VIEW_ALLOWED_EMAILS. Unset on the box, unnamed in the repo, and unnamed in every record that mentions the option."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This lane's own rows: S35 states W3-S22's harmlessness clause lapsed because 'OG-r-1 DEPLOYED the release', and S36 and the messages built on it describe tenant-wide visibility as live 'on the deployed release'. 1.0.0_SA_CTO's ruling section 4 orders the sentinel to ship 'WITH THE ROSTER POPULATED IN THE SAME ACT, never before it'.",
    "world_is": "The 'no restricted profile' half of W3-S22's clause is what moved recently; the 'nothing is deployed' half was ALREADY FALSE when the row was written, because the /sprint routes shipped in an earlier release. OG-r-1 inherited the exposure rather than creating it, so the window is WEEKS rather than the hours this lane's own framing implied, and it spans the whole pilot build rather than starting this morning. THE REMEDY IS UNCHANGED AND THE URGENCY ARGUMENT IS NOT WEAKENED -- an older exposure is not a smaller one -- but the CAUSAL story in the record was wrong and is corrected here rather than left to be inherited. SECOND AND SEPARATE: the ordered sentinel act cannot ship as specified today, because 'populated' has no value to populate with. Nobody in the estate has named who may view the Daily Sprint. That is an AUDIENCE decision, not an engineering one, and it is the input the round-2 cell will block on at cut time unless it is answered before the round opens.",
    "notes": "Filed INERT: a correction to this lane's own framing, changing no hazard's standing. S35 and S36 stand as committed and are NOT rewritten; this row is their correction, per the append-only discipline. W3-S22 stays ARMED with the two disarm conditions 1.0.0_SA_CTO named. WHAT THIS ROW ASKS FOR: nothing of a worker and nothing of the CVO. The roster VALUE is surfaced to 1.0.0_SA_CTO as a question it may need to put to Andrew -- who may see the Daily Sprint is his call, not a seat's -- and it is surfaced NOW rather than at the round-2 cut precisely so the cell is not cut against a missing input. THE CARRY: a clause with two conditions needs BOTH re-read at the same vintage. This lane re-read the half that had just changed and carried the other half forward from the row's own text, which is how a three-week-old deployment got described as five hours old."
  },
  {
    "id": "NFRA_OPLGTW-S39",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T11:28Z",
    "one_line": "THE ORDERED READ WAS ALREADY ANSWERED IN THIS PROJECT'S OWN PASSING CRITERIA, HOURS BEFORE I RAN IT. OGR1-AC3 and OGR1-AC12 both PASS on a scan of this same table at 07:18-07:19Z, and AC12's recorded evidence says it outright: 'of 8 item(s): 8 are OTHER cells' pre-existing probe-og-<cell>-<timestamp> test fixtures (excluded, not a real principal); 0 are not'. I READ THE WORLD BEFORE READING THE RECORD, on an order I had drained myself that morning. TWO THINGS THE EXISTING CRITERIA DID NOT HOLD, which is the only reason the detour produced anything: the KEY-SHAPE mismatch, and the fact that the fixtures CANNOT BE REMOVED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ the OG-r-1 proof instance, criterion OGR1-AC3, status PASS, criterion verbatim 'no principal profile is active in the state store after the deploy': instrument 'dynamodb Scan(ProjectionExpression=pk,sk) on gateway-access-state-table', vintage 2026-09-18T07:18:49Z, denominator '8 items scanned (0 real-principal profiles among them)'. Its sample prints keys of the form `POLICY#probe-og-i1-20260916T000705463912Z-ttl` and `...-race`.",
        "READ OGR1-AC12, status PASS, criterion verbatim 'at release, the set of principals holding a restricted profile is printed and, for each, whether its email can complete the ALB browser login ...; the count ... is 0': vintage 2026-09-18T07:19:48Z, evidence 'of 8 item(s): 8 are OTHER cells' pre-existing `probe-og-<cell>-<timestamp>` test fixtures (excluded, not a real principal); 0 are not', denominator '8 items scanned (0 restricted-profile principals)'.",
        "AND THE CLASSIFIER IS IN THE PROBE, not improvised in a result file: og_r1.py:386 defines `_PROBE_KEY_RE = re.compile(r\"probe-og-[a-z0-9]+-\\d{8}T\\d{6}\")` with the comment 'other cells' own OWN synthetic test fixtures (og_i1.py/og_i5.py's runtime-key probes), never a real tid/oid principal', and ac3() asserts 'every sampled item is a pre-existing probe fixture or otherwise non-profile-shaped, never a real principal's profile'.",
        "TIMELINE, which is the uncomfortable part: those criteria carry vintages of 07:18 and 07:19Z and were inside the VALID proof instance this lane verified and drained at 08:0xZ. The ordered read was issued at 11:04Z and executed at 11:0xZ. FOUR HOURS after this lane had independently re-graded the instance that contained the answer.",
        "WHAT THE EXISTING CRITERIA GENUINELY DO NOT HOLD, measured by comparing their instruments rather than assumed: both scan with `ProjectionExpression=pk,sk` ONLY. Neither reads `record_type`, so neither could observe that three rows carry `record_type: principal_profile` at sort key `PROFILE` while the app derives its sort key FROM the record type -- S36's finding is invisible to AC3/AC12's projection by construction. And neither records that the fixtures cannot be deleted (og_i1.py:481-485's AccessDenied-as-PASS), which is S37's.",
        "THE ACCUMULATION IS FROZEN, NOT ONGOING -- the fact the disposition actually needs: a walk of 156,178 files finds og_i1.py referenced in 11 places, of which exactly ONE is a task-order face (`TO-OG-i-1`, `<status>complete</status>`, 13 invocations). No cron, no CI, no harness and no other order invokes it. og_r1.py references og_i1 only inside a COMMENT naming the fixture pattern -- it CLASSIFIES these rows, it never writes them. So the 8 rows are i-1's own grading runs and the table does not grow unless OG-i-1 is re-graded."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "1.0.0_SA_CTO's W3-S22 addendum (msg 97928) ordered one narrowed read: 'resolve whether each of the three tid/oid pairs corresponds to a live tenant/principal that could sign in', naming it the critical path because 'a real principal means ONE TENANT ACCOUNT RECORDED REVOKED CURRENTLY HOLDS ORDINARY FULL ACCESS'. And CLAUDE.md's evidence law: a prior-record search precedes an announcement.",
    "world_is": "The project's own proof instance already carried that verdict in two PASSING criteria, with a printed denominator and an explicit synthetic-versus-real classification, at a vintage four hours older than the order. The correct first move was to read OG-r-1's acceptance array -- a file this lane had verified itself that morning -- and the answer would have been in hand before any AWS call. The live reads were not WRONG and their method (server-side discrimination, zero identifier exposure) stands, but they were REDUNDANT on the question asked, and the timing branch could have been decided immediately. THE DETOUR PAID FOR ITSELF ONLY BECAUSE THE OLD INSTRUMENT'S PROJECTION WAS NARROWER THAN THE NEW QUESTION: AC3 and AC12 project `pk, sk` alone, so the key-shape mismatch and the no-self-clean accumulation were outside what they could see. A cheaper route existed for the question that was asked; the two findings came from the question nobody asked.",
    "notes": "Filed INERT: a correction to this lane's own method, changing no hazard's standing. FOR THE DISPOSITION 1.0.0_SA_CTO renamed as W3-S22's second condition, the actionable fact is the last evidence line -- the accumulation is FROZEN at 8 rows, because the only writer is a COMPLETE order's probe and nothing schedules it. That makes it a ONE-TIME cleanup of 8 rows by a principal outside this project's grants, not an ongoing leak, and it would grow only if OG-i-1 were re-graded. THE CARRY, and it is the third shape of the same error this lane has filed against itself tonight: BEFORE MEASURING THE WORLD, READ WHAT THIS PROJECT ALREADY MEASURED ABOUT IT. A passing criterion is a recorded measurement with a vintage; an alarm raised without checking one re-derives at best and contradicts at worst."
  },
  {
    "id": "NFRA_OPLGTW-S40",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T11:49Z",
    "one_line": "THIRD INSTANCE IN ONE WINDOW OF THIS LANE REACHING PAST A RECORD THAT ALREADY HELD THE ANSWER, and this one is against the LAW FILE: I recommended an in-round cut to route around the G-A gate, and CLAUDE.md Rule 27 already states the arithmetic that refutes it -- 'the refuser counts open orders PER PROJECT and never per round (LD-0521)'. A NEW ORDER CUT NOW ADDS TO THE VERY OPEN-ORDER COUNT ROUND 1's L10 IS WAITING ON, so the in-round cut DELAYS round 1 and therefore round 2. It is not a way around the blockage; IT IS THE SLOWER PATH TO THE SAME FIX.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1.0.0_SA_CTO's third correction (msg 97951 @fa90229c09) holds branch (2) on LD-0521 rather than on the boundary it had set, accepting every fact in this lane's argument and producing the reason the argument did not reach.",
        "THE TEXT WAS IN THE FILE THIS LANE READS AT STARTUP, and the BYTES WERE PRINTED AT THE CITED LINES rather than searched for: CLAUDE.md:96-98 reads 'A ROUND N+1 ISSUANCE CUT BEFORE ROUND N's SLUG DEADLOCKS ROUND N's L10 UNTIL N+1 FULLY DRAINS**, because the refuser counts open orders PER PROJECT and never per round (LD-0521).', with a measured instance at :98-99 (AMGT_RESAPP round 6, cut straight off the L9 adjudication, so the open count never reached zero and a correctly-gated CVO lane silently acquired a different blocker).",
        "WHICH HALF OF THAT RULE ACTUALLY REACHES THIS CASE, stated precisely because the distinction is the useful part: the HEADLINE sentence names a ROUND N+1 ISSUANCE, and what this lane proposed was an IN-ROUND remediation cell, so the headline does not literally cover it. THE MECHANISM CLAUSE DOES, and it is round-agnostic by its own words -- 'the refuser counts open orders PER PROJECT and NEVER PER ROUND'. A rule whose headline names one shape can carry a mechanism that binds every shape, and reading only the headline is how this lane concluded the rule did not apply to it.",
        "THE PENDING SET MAKES IT CONCRETE, re-read from the faces at 11:32Z: OG-i-4, OG-r-2, OG-v-4, OG-v-5 are `pending`, so the project's open-order count is 4 and L10 needs it at 0. A sentinel order cut now makes it 5.",
        "THE OTHER TWO INSTANCES THIS WINDOW, for the pattern rather than the confession: (1) row S38 -- W3-S22's 'nothing is deployed' clause was re-read only on the half that had changed, while the other half was taken from the row's own text, and the deployed commit disproved it; (2) row S39 -- the ordered live read was already answered by OGR1-AC3 and OGR1-AC12, PASS at 07:18-07:19Z, inside the proof instance this lane verified and drained itself at 08:0xZ.",
        "AND THE COUNTER-INSTANCE, so this is not read as 'always defer to the record': the same window's two findings (the key-shape mismatch and the no-self-clean accumulation) came from a control NOBODY ASKED FOR, run against a live table whose existing criteria projected `pk, sk` only and were blind to both BY CONSTRUCTION. Reading the record first would not have found them."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md Rule 27's L10 clause (LD-0521) and Rule 22's evidence law, which sizes checks by who eats the error: a recommendation that changes a project's sequencing costs another seat and the round, so it is at least GRAIN + COVERAGE, and the cheapest covering read was the law file already in context.",
    "world_is": "Three times in one window this lane measured the world, or argued from first principles, where a record it had already read held the answer: a row's own second clause, a proof instance it had graded itself, and a rule in the law file. The recommendation was made in good faith and its facts were all accepted -- the exposure IS weeks old, the act IS DELTA=0, and 'round 2 before v-4/v-5' DOES now resolve to 'after Andrew's word' -- but the remedy proposed would have made the wait LONGER. A recommendation can be right about every premise and wrong about the act, and the thing that catches that is the arithmetic of the mechanism rather than the strength of the motivation.",
    "notes": "Filed INERT: a method record, no hazard moved, nothing cut. OUTCOME ACCEPTED WITHOUT FURTHER ARGUMENT: branch (2) holds, the sentinel ships in round 2 behind G-A, the freeze is not broken, and 1.0.0_SA_CTO has struck its own branch (1) because an in-round cut had the identical defect whatever prompted it -- a live exposure would have justified URGENCY and still not a new cell; the correct emergency act was always an ESCALATION, which is what sharpening card 1 does. THE CARRY, generalising S39's: BEFORE RECOMMENDING AN ACT THAT MOVES A PROJECT'S SEQUENCING, READ THE MECHANISM'S OWN ARITHMETIC -- not the principle, the COUNT it keeps. COST: one read of a rule already in context. NON-APPLICATION: an act whose mechanism has no counter, and an unrequested control on a question nobody has asked, which is where this window's two real findings came from."
  },
  {
    "id": "NFRA_OPLGTW-S41",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T12:08Z",
    "one_line": "GATE-PRECONDITION SWEEP of all FOUR pending orders -- not 'is the gate still shut' but 'do this cell's INPUTS still resolve': ONE stale live-resource reference found and AMENDED (OG-v-5 named the access-state table by the name OG-i-5 renamed away, on the single read that establishes the pilot's active profile), and the other three verified clean. ALSO SETTLED SO NOBODY RE-DERIVES IT AS AN ALARM: OG-v-4's audit sink `opal-mcp-audit` `audit/schwab/` EXISTS AND IS EMPTY, and empty is the CORRECT pre-walkthrough state.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "POPULATION walked from the directory, never a remembered list: 33 order faces, 4 not `complete` -- OG-i-4, OG-r-2, OG-v-4, OG-v-5. Every backticked resource-shaped token in each was extracted and tested against what exists: 44 live DynamoDB tables (`list-tables`, counted by `length(TableNames)` rather than eyeballed) and the contract's own anchors (`gateway-access-state-table`, `opal-data-assets`, `gateway-schwab-read-role`, `gateway-schwab-catalog-read-role`).",
        "THE DEFECT, and it is AMENDED at @52151a661d: OG-v-5's cell text read 'The active profile is read, read-only, from the live `opal-gateway-access-state` table's `POLICY#` record and its `operator_audit`'. That table is NOT among the 44; `gateway-access-state-table` is, and it is what the contract's `state_store.table` names. OG-i-5 renamed it and this pending order was never carried forward. The amendment repoints the sentence at the contract's name, states that the contract wins on any future disagreement, and changed no criterion, no grant and no order count.",
        "WHY IT MATTERED MORE THAN A TYPO: that sentence is the ONE read establishing the pilot's active profile, and OG-v-5 is graded only AFTER a person has completed the pilot walkthrough. A worker handed the stale face fails on a non-existent table with a human already waiting on the result. The gate being shut is precisely why nobody would have looked.",
        "THE OTHER THREE ARE CLEAN, checked rather than assumed: OG-i-4's only candidate token is `safe-apply` (a tool, not a resource); OG-r-2 carries none; OG-v-4 carries `opal-data-assets` (a contract anchor) and `opal-mcp-audit`, which `s3api head-bucket` confirms EXISTS (`arn:aws:s3:::opal-mcp-audit`, us-east-1, rc=0).",
        "THE AUDIT PREFIX IS EMPTY AND THAT IS CORRECT -- settled here so the next reader does not raise it: `list-objects-v2` on `audit/schwab/` returns NO Contents, while the bucket's own `audit/` prefix holds many `audit/dt=YYYY-MM-DD/` partitions. Reading the writer rather than guessing: `app/schwab_audit.py:56-57` sets `SCHWAB_AUDIT_PREFIX = \"audit/schwab/\"` and `AUDIT_SINK_BUCKET = \"opal-mcp-audit\"` -- exactly what OG-v-4 names -- and `:17` states the separation deliberately ('Schwab records never enter that table's rows'), with `app/audit.py:47` writing the OTHER stream at `audit/dt={day}/`. So `audit/schwab/` is empty because NO SCHWAB AUDIT RECORD HAS BEEN WRITTEN YET, which is the expected state before the walkthrough.",
        "AND THE GATE RECORDS THEMSELVES, measured at HEAD rather than inferred from the orders being `pending`: all FOUR are ABSENT -- `1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md`, `2.0.0_SA_COO~O/CONTROLLED_WALKTHROUGH_RECORD.md`, `1.0.0_SA_CTO~A/G-E_PILOT_IDENTITY_AND_GRANT.md`, `2.0.0_SA_COO~O/PILOT_WALKTHROUGH_RECORD.md` -- and both owning deliverables directories hold 0 files at HEAD. TWO OF THE FOUR (G-D, G-F) ARE THIS LANE'S OWN TO LAND once the walkthroughs happen; the orders' own preflight says so ('G-D (the operator's record, landed by 2.0.0_SA_COO~O)')."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OG-v-4 and OG-v-5 are HELD on gates G-C/G-D and G-E/G-F, each stated as 'Both records at HEAD, or a BLOCKING row and a stop'. The canonical-drive skill's own instruction on a gate held by someone else: 'A gate someone else legitimately holds is a gate; VERIFY IT IS REAL.'",
    "world_is": "The gates are real -- all four records absent at HEAD, both owning directories empty -- so the two walkthrough cells are correctly held and nothing about this sweep unblocks them. What the sweep found is that VERIFYING A GATE IS REAL AND VERIFYING A HELD CELL IS STILL EXECUTABLE ARE DIFFERENT QUESTIONS, and only the first is the one anyone asks. A held cell's inputs keep drifting while it waits, and the drift is invisible precisely BECAUSE the cell is held: no worker reads the face, no criterion runs, and the stale name sits there until a person has finished a walkthrough and is waiting on the grade.",
    "notes": "Filed INERT: one defect found and already amended, three orders clean, no hazard moved and nothing unblocked. THE CARRY: WHILE A CELL IS HELD, RE-CHECK ITS INPUTS, NOT ITS GATE. The gate's state is the question everyone asks and the inputs' state is the one that breaks. COST: one resource-token sweep per held cell, which here was four orders and four live reads. NON-APPLICATION: a cell held for less time than its inputs take to drift, and a cell whose inputs are all in-repo and covered by the freeze. REMAINING FOR THIS LANE ON THESE TWO CELLS: G-D and G-F are this lane's records to land, so when the walkthroughs happen the template (`OG-v-1`'s) and the deliverables directory are what this lane owes -- not the walkthroughs themselves, which are a person's act under the vendor-egress moratorium."
  },
  {
    "id": "NFRA_OPLGTW-S42",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T12:22Z",
    "one_line": "THE SEALED EXPECTATIONS' SALT IS GONE, SO OG-v-4's DATA-CORRECTNESS CRITERION CANNOT BE GRADED AS WRITTEN. `SEALED_EXPECTED.json` is committed at HEAD and records `hash_algorithm: sha256(salt || canonical_json(answer))` with `salt at C:/tmp/nfra-oplgtw-sealed/expected/SALT.txt (outside the repository)` -- and that directory DOES NOT EXIST on either path plane. Without the salt the committed hashes cannot be reproduced from any answer, ever. REMEDY EXISTS TODAY AND EXPIRES: a RE-SEAL is honest only while the walkthrough has NOT happened, and the walkthrough has not happened.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE COMMITTED ARTIFACT NAMES ITS OWN MISSING INPUT: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/SEALED_EXPECTED.json` (AT HEAD, schema_version 1.0, cell OG-v-3) carries `hash_algorithm` = 'sha256(salt || canonical_json(answer)); salt at C:/tmp/nfra-oplgtw-sealed/expected/SALT.txt (outside the repository)', and six `questions[]` entries each pairing an `expected_answer_hash` (sha256:...) with an `expected_answer_file` under `C:/tmp/nfra-oplgtw-sealed/expected/RQn.txt`.",
        "THE DIRECTORY IS ABSENT, MEASURED ON TWO INDEPENDENT PATH PLANES because a path-form artifact would be a false alarm: bash `test -d /cygdrive/c/tmp/nfra-oplgtw-sealed` -> ABSENT, and its `actual/` child ABSENT; PowerShell `Test-Path 'C:\\tmp\\nfra-oplgtw-sealed'` -> False, while `Test-Path 'C:\\tmp'` -> True with 36 children and `Get-ChildItem C:\\tmp -Filter nfra*` returning nothing. The parent exists and is populated; only this tree is gone.",
        "IT WAS NEVER COMMITTED ANYWHERE, checked before announcing rather than after: `comp-find --name 'SALT.txt'` returns 0 hits across 172,647 files scanned, with the tool's own disclosure that 68,643 ephemeral-floor files were excluded. THAT CENSUS PROVES ONLY 'nobody committed it' -- comp-find is REPO-ONLY and never covers `C:/tmp` at all -- which is exactly the branch that needed excluding; the loss itself rests on the two direct path reads above, not on this zero.",
        "OG-v-3's ORDER SAYS THE VALUES AND THE SALT LIVE THERE AND NOWHERE ELSE: 'Where the values live: `C:/tmp/nfra-oplgtw-sealed/expected/` (outside the repository), WITH THE SALT BESIDE THEM. Retention: kept until `OG-v-4` has graded, then removed by the COO at that drain', and its BOUNDS: 'Outside the repository you write only under `C:/tmp/nfra-oplgtw-sealed/`'. TO-OG-v-3 reads `<status>complete</status>`, so the seal was produced and its retention window has not yet been reached -- the removal was to happen at OG-v-4's drain, which has not occurred.",
        "THE BLAST RADIUS IS ONE CRITERION, NOT THE CELL, and the count is corrected against my own instrument: of OGV4's NINE criteria, a text sweep flagged TWO -- `OGV4-AC5` and `OGV4-J2` -- but the J2 hit is my regex catching the `<expected_criteria>` list that trails it, and J2 is a judgment criterion about FWD-3..FWD-8's ACCEPT clauses with no sealed dependency. THE SUBSTANTIVE COUNT IS ONE: `OGV4-AC5`, 'the actual answers to RQ1-RQ6, each asked at the fixed business date 2026-09-15 per the protocol's section 4, hash [to the sealed expectations]'. It is the criterion that proves the Gateway returns the RIGHT ANSWERS to a person's questions.",
        "RE-CREATABLE IN SUBSTANCE, NOT IN FORM: `SEALED_EXPECTED.json` records `qualified_objects_used[]` with `key` AND `version_id` for each source object (e.g. `schwab/08242234/silver/dim_balance/date=2026-09-15/data.parquet`, version rHBXO7hLBmHrcJuR3k29.7Us3gimdsE7), plus the exact instrument (pyarrow Parquet decode, stdlib decimal.Decimal summation). So the ANSWERS can be recomputed from the identical versioned objects. THE COMMITTED HASHES CANNOT BE MATCHED, because a new salt yields different digests -- any repair is a RE-SEAL producing new hashes, never a recovery of these."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OG-v-4 grades the controlled walkthrough against sealed expectations produced BEFORE it, so the grader cannot tune the answer to the result -- `OGV4-AC5` hashes the operator's actual answers and compares them to `SEALED_EXPECTED.json`'s committed digests. OG-v-3's retention clause keeps the sealed tree 'until OG-v-4 has graded, then removed by the COO at that drain'.",
    "world_is": "The sealed tree is gone before the retention clause said it should be, and with it the salt that is the only way to reproduce the committed digests. OGV4-AC5 is therefore ungradeable as written: no answer, correct or incorrect, can hash to those values without the salt. WHAT SAVES IT IS TIMING AND NOTHING ELSE. The seal's PURPOSE -- expectations fixed before the walkthrough so the grader cannot tune them -- is preserved by a RE-SEAL today, because the walkthrough HAS NOT HAPPENED (G-C and G-D are both absent at HEAD). THE SAME RE-SEAL PERFORMED AFTER THE WALKTHROUGH WOULD BE WORTHLESS AND WOULD LOOK IDENTICAL IN THE RECORD. So this is a repair with an expiry date, and the expiry is an event nobody controls.",
    "notes": "ARMED and BLOCKING, disarm_owner `2.0.0_SA_COO~O`: the remedy is a re-seal, which is OG-v-3's act, and cutting the cell that performs it is this issuer's. NOT CUT THIS TICK and the reason is LD-0521's arithmetic, the same one that refused an in-round cut an hour ago -- a new order adds to the open count round 1's L10 is waiting on. IT IS INSTEAD SEQUENCED: the re-seal must land BEFORE the controlled walkthrough, and the walkthrough is itself gated on G-C (owner `1.0.0_SA_CTO~A`), so the ordering is available without an in-round cut PROVIDED the re-seal is ordered before G-C is satisfied. THAT SEQUENCING CONSTRAINT IS THE WHOLE OF WHAT THIS ROW ASKS FOR, and it is surfaced to `1.0.0_SA_CTO` the same tick because that seat holds G-C's timing. NOT CLAIMED: no assertion about WHAT removed the tree (a temp sweep, a reboot, a cleanup) -- unmeasured, and the remedy does not depend on it. THE CARRY: AN OUT-OF-REPO INPUT IS OUTSIDE EVERY GUARD THIS ESTATE HAS -- no gate, no freeze, no worktree and no commit protects `C:/tmp`, and a cell holding one is trusting a path nothing defends for exactly as long as it stays held."
  },
  {
    "id": "NFRA_OPLGTW-S43",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T12:41Z",
    "one_line": "S42 IS NOT ONE FILE, IT IS THE WHOLE SURFACE: a census of every out-of-repo path this project cites -- 165 files walked, 22 distinct `C:/tmp` paths, 6 of them worktree-shaped and transient by design -- finds SIXTEEN data/evidence paths and ALL SIXTEEN ARE ABSENT. TWO trees, not one: `nfra-oplgtw-sealed/` (S42's salt and expected answers) AND `nfra-oplgtw-handoff/` (a lambda source map cited by the COMPLETE order OG-i-3, plus OG-v-3's partial scripts). The only surviving oplgtw-shaped directory in `C:\\tmp` is the live worker worktree.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CENSUS with its denominator, walked rather than pathspec'd: 165 `.md`/`.json` files under the project tree, 22 distinct `C:/tmp/...` paths cited. SPLIT BY SHAPE because the two classes have different expectations: 6 match `C:/tmp/wk-*` (worker worktrees, transient by design -- their absence after a drain is CORRECT and is not a finding), leaving 16 data/evidence paths. ALL 16 test ABSENT.",
        "TREE ONE, `C:/tmp/nfra-oplgtw-sealed/` -- S42's subject: `expected/SALT.txt`, `expected/RQ1.txt` .. `RQ6.txt`, `expected/`, `actual/`, `work/` and the root. Cited by `SEALED_EXPECTED.json`, `TO-OG-v-1`, `TO-OG-v-3`, `TO-OG-v-4` and this channel.",
        "TREE TWO, `C:/tmp/nfra-oplgtw-handoff/` -- NEW HERE AND NOT IN S42: `lambda-source-map.OG-c-2.json`, cited by `TO-OG-i-3.alb-browser-paths.md`; and `og-v-3-partial/scripts/` with its `QUALIFIED_VERSIONS.json`, cited by `sealed-real-expectations.result.md` and this channel. Confirmed on the Windows plane: `Test-Path 'C:\\tmp\\nfra-oplgtw-handoff'` -> False.",
        "AND THE SURVIVOR LIST IS THE CONTROL THAT MAKES THE ZERO MEAN SOMETHING: `Get-ChildItem C:\\tmp -Force | Where Name -like '*oplgtw*'` returns EXACTLY ONE entry, `wk-oplgtw-2a` (the live worker worktree, LastWriteTime 2026-09-18 03:16). So `C:\\tmp` is neither empty nor swept clean of this project -- it holds 36 children and one oplgtw directory, and every oplgtw DATA tree is gone while the live worktree survives.",
        "WHAT IS NOT LOST, checked rather than assumed, because it changes the remedy: `QUALIFIED_VERSIONS.json`'s content survives IN THE REPO -- `SEALED_EXPECTED.json` carries `qualified_objects_used[]` with `key` AND `version_id` for every source object. The out-of-repo copy is gone; the data is not. The SALT has no such in-repo twin, which is why S42 is BLOCKING and this row is not.",
        "THE OG-i-3 CITATION IS A RE-VERIFICATION LOSS, NOT A GRADING DEFECT, and the distinction is the point: `TO-OG-i-3` reads `complete` and its criteria were graded when the source map existed. Losing `lambda-source-map.OG-c-2.json` does not make that grading wrong -- it makes it UNREPEATABLE. CLAUDE.md 22a names exactly this instrument ('diff deployed bytes against the BUILD INPUT (source-map/manifest), never by filename'), so the one artifact that would let anyone re-run that comparison independently is the one that is gone."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Orders and evidence across this project cite out-of-repo artifacts as if they persist: OG-v-3's retention clause ('kept until OG-v-4 has graded'), OG-i-3's source-map citation, and OG-v-4's actual- answers directory. CLAUDE.md 22a treats a build-input source map as the instrument for a deployed-bytes claim.",
    "world_is": "Every out-of-repo data path this project ever cited is gone -- 16 of 16 -- while the one live worktree survives, so this is not a broad temp sweep that also took a worktree but something that removed the DATA trees specifically or that they simply never outlived the sessions that made them. The consequences differ by artifact and are NOT uniform: the SALT is unrecoverable and blocks a criterion (S42); QUALIFIED_VERSIONS' content survives in-repo and blocks nothing; the OG-i-3 source map costs RE-VERIFIABILITY of a completed grading rather than its validity. A single 'the temp trees are gone' sentence would flatten three different consequences into one alarm, which is why each is stated with its own.",
    "notes": "ARMED, disarm_owner this lane, and deliberately NOT BLOCKING -- S42 carries the blocking half and this row is its population. FOR THE CVO AT L9, which is the practical reason to file it: any criterion or result-file claim resting on a `C:/tmp/nfra-oplgtw-*` path CANNOT BE RE-VERIFIED, and the citations are enumerated above so nobody has to re-derive which ones. That is a property of the evidence's repeatability, not of its correctness at grading time. NOT CLAIMED: what removed them, and whether any worker violated a retention clause -- unmeasured, and the remedies do not depend on it. THE CARRY, which S42 stated for one file and this row measures for a surface: AN OUT-OF-REPO ARTIFACT HAS NO GUARD, NO VINTAGE AND NO WITNESS. The estate's controls -- the freeze, the gates, the worktree discipline, the commit record -- all stop at the repository boundary, so a cell that puts something outside it has chosen a store with none of them. COST: one census per project that cites an outside path. NON-APPLICATION: an out-of-repo artifact that is DERIVED and re-derivable from in-repo pins, which is exactly what QUALIFIED_VERSIONS turned out to be and what the SALT is not."
  },
  {
    "id": "NFRA_OPLGTW-S44",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T13:34Z",
    "one_line": "THE RE-SEAL IS DATE-SAFE, AND THE REASON IS WORTH RECORDING BEFORE SOMEONE RAISES IT AS AN ALARM: the walkthrough protocol WAS edited AFTER `OG-v-3` sealed -- 2026-09-17 13:50 vs the seal at 10:32 -- but the edit FROZE section 4's dates rather than moving them, replacing the phrase 'latest' with the literal 2026-09-15 precisely so a newer qualified closure could not invalidate the seal. And `compute_expected.py` HARD-PINS the same: literal keys, literal `version_id`s and a constant `PREVIOUS_QUALIFIED_DATE`. Nothing resolves a date at run time, so a re-seal today seals the SAME questions against the SAME bytes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "VINTAGE ORDER, the fact that makes the question worth asking at all: `git log` on `infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md` shows its last change at 90999aaee5, 2026-09-17 13:50 (OG-o-2's runbook build), while `SEALED_EXPECTED.json` landed at 339f33928b, 2026-09-17 10:32. THE PROTOCOL MOVED AFTER THE SEAL -- which is normally exactly how a seal goes stale.",
        "BUT THE DIFF MOVES IT THE OTHER WAY, read rather than assumed: `git diff 90999aaee5~1 90999aaee5` on that file replaces `latest` with `2026-09-15` in every `dates` cell of section 4's table, and RQ5/RQ6's second date becomes 'the qualified date immediately before it, AS SEALED'. The new prose says why, citing `1.0.0_SA_CTO` ruling R-OG-12 and row `NFRA_OPLGTW-W6-S5`: 'a newer qualified closure can exist by the time the walkthrough runs (2026-09-16 already does) without changing what OG-v-3 sealed'. THE QUESTION TEXT ITSELF IS UNCHANGED FOR ALL SIX -- only the date phrasing was pinned.",
        "THE SCRIPT AGREES BY CONSTRUCTION, which is what makes the re-seal reproducible rather than merely intended: `compute_expected.py` carries `QUALIFIED_OBJECTS` as literals (`schwab/08242234/silver/dim_balance/date=2026-09-15/data.parquet` with its `version_id`, and the two BlackDiamond objects), `PREVIOUS_QUALIFIED_DATE = {\"08242234\": None, \"08335338\": None}` as a constant, and `\"business_date\": \"2026-09-15\"` written into every answer structure. There is NO catalog read and NO 'latest' resolution anywhere in it.",
        "RQ5/RQ6's None IS DELIBERATE AND IS ITSELF THE TEST, not a gap: the script seals `previous_qualified_business_date_status: \"NONE_QUALIFIED\"` with the note 'NOT COMPUTABLE -- no previous qualified date exists ... A correct answer states this; a fabricated [one]' -- so the sealed expectation for the two between-dates questions is that the Gateway SAYS there is no prior qualified date rather than inventing one.",
        "ID SET MATCHES ACROSS BOTH CARRIERS: `SEALED_EXPECTED.json`'s `questions[].id` is RQ1..RQ6 and section 4's table is RQ1..RQ6 -- compared as sets, equal."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "`OGV4-AC8` (this issuer's amendment) requires the re-seal to be computed 'from the SAME version-pinned objects OG-v-3 recorded, by the same instrument', with only the salt fresh. That presupposes the questions and their dates have not moved since the seal.",
    "world_is": "The presupposition holds, and it holds for a reason someone deliberately built rather than by luck: the one post-seal edit to the protocol exists to FREEZE the dates against exactly this drift, and the sealing script never resolved a date at run time in the first place. So the re-seal differs from `OG-v-3`'s ONLY in its salt, and therefore only in its digests -- which is what `OGV4-AC8` already requires the probe to state. A reader who notices that a newer qualified closure (2026-09-16) exists, or that the protocol's mtime is later than the seal's, has found a real ordering and the WRONG conclusion; this row is here so that costs one read instead of a re-investigation.",
    "notes": "Filed INERT: nothing is wrong and nothing is asked. This is PRE-EMPTIVE CONTEXT for whoever grades `OGV4-AC5` or reviews the re-seal, because the alarming-looking fact (protocol edited AFTER the seal) is cheap to find and its benign explanation is not. NOT CLAIMED: that the re-seal itself is correct -- that is `OGV4-AC8`'s to prove when the worker runs it, and this row deliberately does not pre-empt its evidence. THE CARRY: A VINTAGE ORDERING IS A QUESTION, NOT A VERDICT -- 'the input changed after the artifact' is the right thing to notice and the wrong thing to conclude from, because the change may exist to PROTECT the artifact. The diff settles it and the timestamps never can."
  },
  {
    "id": "NFRA_OPLGTW-W6-S11",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~6",
    "surfaced_at": "2026-09-18T13:32:53Z",
    "one_line": "TO-OG-v-4's WORKER FACE names `probes/og_v4.py` as an existing probe for every mechanical criterion, but no such file existed at hand-off in this slot's deliverables/probes/ (only og_v1.py, og_v3.py, og_z4.py were present) -- PHASE 1 required creating it from scratch, implementing ONLY the AC8 branch (usage error on any other id), since AC1-AC7/AC9 belong to PHASE 2's hand-off.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ before writing: `ls org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/` at this worktree's HEAD (15edf9f07b) listed exactly `og_v1.py`, `og_v3.py`, `og_z4.py` -- no `og_v4.py`.",
        "The order's own AC1-AC9 invocation lines all name `probes/og_v4.py` as if already present, and AC8's own invocation (`timeout 300 .venv-og/Scripts/python .../probes/og_v4.py AC8`) cannot run without it.",
        "Written this turn at org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py, following og_v3.py's own PASS/FAIL verdict-line pattern; only `ac8()` is implemented -- `main()` returns a usage error (rc 2) naming PHASE 2 for AC1-AC7/AC9, never a fabricated PASS/FAIL for a criterion this hand-off does not own.",
        "AC8's invocation ran successfully against this new file this turn: `VERDICT: PASS-OGV4-AC8`, rc=0."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-v-4 WORKER FACE: 'The probe for every mechanical criterion is .../probes/og_v4.py, taking the short id, printing its measurement with its denominator, then exactly one line VERDICT: ...' -- phrased as a fact about an existing instrument, not an instruction to build one.",
    "world_is": "The file did not exist in this slot's deliverables at hand-off; PHASE 1 could not satisfy AC8's own invocation without first writing it. Only the AC8 branch is implemented, matching this hand-off's exact scope (AC1-AC7, AC9, J1, J2 belong to PHASE 2 and are refused here with a usage error, not graded).",
    "notes": "INERT: no future-harm mechanism -- the file exists now, is committed with this drain, and PHASE 2's worker extends the same file to add the remaining AC branches (a normal continuation, not a defect to disarm). Filed for FORM per Rule 22's step-7 trigger (had to do something the order's own wording implied was already done); no significance judged. COST: none beyond this row. NON-APPLICATION: a future hand-off finding AC1-AC7/AC9 unimplemented in this file is not a surprise -- it is exactly what this row states PHASE 1 left undone."
  },
  {
    "id": "NFRA_OPLGTW-S45",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T15:08Z",
    "one_line": "THE RESIZE CHANGED THE GATEWAY'S EGRESS IDENTITY AND NOTHING IN THE PROJECT SAYS SO. The instance has NO Elastic IP -- `describe-addresses` returns `[]` and the only public-IP handling across the gateway module's 20 `.tf` files is `associate_public_ip_address = true` -- so the stop/start `OG-i-4` requires gave it a NEW public IP (now 54.197.78.28). `main.tf:172-174`'s own comment says that address exists 'for IGW egress to Graph/Entra', so what moved is the identity the Gateway presents OUTBOUND, and it will move again on EVERY future stop/start.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN against live AWS at 2026-09-18 ~14:5xZ, after the resize: `ec2 describe-instances i-07dccb1615503ac99` -> InstanceType `t4g.small`, State `running`, PublicIp `54.197.78.28`, PrivateIp `172.31.89.135`, LaunchTime `2026-09-18T14:53:48Z`. And `ec2 describe-addresses --query \"Addresses[?InstanceId=='i-07dccb1615503ac99']\"` -> `[]` -- NO Elastic IP is associated, so the public address is ephemeral and a stop/start re-allocates it.",
        "THE DECLARATION AGREES, read across the whole module rather than one file: of 20 `.tf` files in `infra/aws/terraform/opal-gateway/`, exactly ONE line touches public addressing -- `main.tf:174 associate_public_ip_address = true`. There is no `aws_eip` resource anywhere in the module. An unscoped corpus census (297 hits over 167,890 files scanned) shows OTHER estate modules DO declare EIPs -- `infra/aws/terraform/website/`, among others -- so this is a per-module choice and not an estate-wide absence.",
        "WHAT THE ADDRESS IS FOR, from the code's own comment at `main.tf:172-173`: 'Public IP for IGW egress to Graph/Entra (no NAT in the default VPC). The SG, not the absence of a public IP, is the ingress control (inbound 8080 from the ALB SG only).' So INGRESS is unaffected -- callers reach the ALB (`opal-gateway-616252801.us-east-1.elb.amazonaws.com`, internet-facing, active; target `healthy` on 8080) -- and it is the OUTBOUND identity that changed.",
        "NOTHING IN THE REPO PINS IT, so there is no in-repo breakage to chase: a walk of 513 files under `infra/aws/ec2/` and the project tree found 10 public-IP-shaped strings, and the three in `EC2_MANIFEST.json` belong to OTHER services -- the gateway's own `ec2_host` entry reads `None` and it records no address. The exposure is entirely to allowlists OUTSIDE this repository.",
        "SERVICE STATE AT THE SAME VINTAGE, so this row is not mistaken for an outage report: through SSM, `systemctl is-active opal-gateway` -> `active` since 14:53:58Z, `/health` -> 200, `/mcp` -> 401, `free -m` total 1846 MiB (the t4g.small memory the resize was for). The Gateway is UP; what this row names is an identity change, not a failure."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "`OG-i-4`'s cell text treats the resize as an instance-type change plus a re-baseline: 'change `aws_instance.gw`'s `instance_type` ... apply, and re-take the existing-user baseline on the new host'. Neither that order, the PRD's capacity paragraph, nor the contract's `capacity` block mentions the public address at all.",
    "world_is": "An instance-type change on this instance is not only a capacity change -- it is a stop/start, and a stop/start on an EIP-less instance re-allocates the public address the Gateway uses to reach Graph and Entra. That consequence is nowhere in the cell that ordered it. WHAT IS NOT MEASURED HERE AND MUST NOT BE ASSUMED: whether anything OUTSIDE this repository allowlists that address -- an Entra named location or conditional-access rule, a vendor allowlist, a device-side firewall. Those surfaces are not readable from this seat, so this row states the CHANGE and its recurrence, never a break. THE RECURRENCE IS THE durable part: every future stop/start moves it again, including any the pilot or an incident requires.",
    "notes": "ARMED, disarm_owner `1.0.0_SA_CTO`: the remedy is an infra decision with its own blast radius (attach an Elastic IP, or record that the egress address is deliberately ephemeral and that no external surface may key on it), and it is an endpoint-shaped question rather than an issuer one. REC, offered not taken: if any external allowlist keys on this address, an EIP is the cheap fix and its own act; if none does, the answer is one line in the PRD or runbook saying so, which converts an unexamined property into a recorded decision -- the same shape as the sprint roster's empty-means-unconfigured fix. CONTEXT, since it is why this was looked at: Andrew reported difficulty reaching the Gateway from a sitez Bloomberg device at ~14:5xZ. THE LIKELIEST CAUSE IS THE OUTAGE WINDOW ITSELF (the instance was stopped and started ~14:45-14:54Z and the service came up at 14:53:58Z), not this address change, and that was told to him plainly with both possibilities separated rather than one asserted. NOT CLAIMED: that the IP change caused his symptom."
  },
  {
    "id": "NFRA_OPLGTW-W1-S14",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~1",
    "surfaced_at": "2026-09-18T00:00:00Z",
    "one_line": "OG-i-4's resize plan shows public_dns/public_ip going to (known after apply) alongside instance_type -- a recompute side effect of the stop/start, not an independently configured change.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform plan (infra/aws/terraform/opal-gateway, .tools/terraform.exe, planfile .scratch/og_i4/resize.tfplan, this worktree @wk-oplgtw-1-i4): 'aws_instance.gw will be updated in-place ... ~ instance_type = \"t4g.nano\" -> \"t4g.small\" ~ public_dns = \"ec2-13-221-151-249.compute-1.amazonaws.com\" -> (known after apply) ~ public_ip = \"13.221.151.249\" -> (known after apply) ... Plan: 0 to add, 1 to change, 0 to destroy.'",
        "terraform show -json of that planfile: resource_changes has 84 entries, exactly 1 non-no-op (aws_instance.gw, actions=['update'], replace_paths=null); its changed_attribute_names (before!=after) = ['instance_type','public_dns','public_ip']; after_unknown = {'public_dns': true, 'public_ip': true} -- so public_dns/public_ip are RECOMPUTED-TO-UNKNOWN, not independently set to a new declared value, and no other resource in the 84 changed.",
        "TO-OG-i-4 WORKER FACE itself narrates the mechanism this plan exhibits: 'Changing an EC2 instance type stops and starts the instance' -- the instance carries no Elastic IP (associate_public_ip_address=true, no aws_eip resource in infra/aws/terraform/opal-gateway/main.tf), so any stop/start of THIS SAME resource reassigns a new ephemeral public IP and DNS name as an AWS-side mechanical consequence, not a Terraform config edit."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-i-4 BOUNDS: 'Blast radius. One attribute on one resource. A plan that replaces the instance, or changes any other attribute or resource, is a BLOCKING row and no apply.' OGI4-AC2: 'the plan changes only `instance_type` on `aws_instance.gw` and does not replace the instance.'",
    "world_is": "The plan's diff block for aws_instance.gw lists three tildes (instance_type, public_dns, public_ip), not one -- but only instance_type has a concretely declared before/after VALUE; public_dns and public_ip go from a known value to `(known after apply)` (after_unknown=true), which is what any in-place update requiring a stop/start on a non-EIP instance produces regardless of which attribute triggered it. No other resource address appears among the 84 with a non-no-op action, and the resource's own action is 'update', never 'replace' (replace_paths null, Plan line reads 0 add / 1 change / 0 destroy).",
    "notes": "Read as OBSERVATION/INERT and NOT BLOCKING: the order's own G-A text already names the stop/start as the mechanism this cell authorises, and public_dns/public_ip re-issuing on any stop/start of a public, non-EIP instance is that mechanism's unavoidable, intrinsic side effect on the SAME resource -- not a second attribute independently changed by config, and not a second resource. OGI4-AC2 is graded on: (a) exactly 1 non-no-op resource_changes entry across the full 84, (b) that entry's address is aws_instance.gw, (c) its action is 'update' with replace_paths null, (d) the only changed_attribute_name with a concretely declared (non-unknown) after-value is instance_type. Filed for FORM (Rule 22 step-7: judgment call on what 'changes only instance_type' admits) before proceeding to apply, per 'Anything off-spec is one surprise row ... and you keep working.' COST: none beyond this row -- the apply proceeds unchanged. NON-APPLICATION: a plan that shows a SECOND resource, or a THIRD attribute with a concretely declared new value, or any replace action -- any of those would be the BLOCKING case this row is not."
  },
  {
    "id": "NFRA_OPLGTW-S46",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps",
    "surfaced_at": "2026-09-18T16:48Z",
    "one_line": "EVERY GATEWAY LOGIN DIED AT /callback WITH 503 FROM THE OG-r-1 DEPLOY (05:58:16Z) UNTIL 16:3xZ -- AN INCIDENT, NOT AN EXPOSURE, AND TWO COMPLETE CELLS CERTIFIED IT: `oauth_as.take_pending()` (:649; :772 the code burn) consumes the pending authorization by a CONDITIONAL DELETE, and the runtime grant `aws_iam_role_policy.gw_access_state_runtime` held no `dynamodb:DeleteItem` BECAUSE `OGI1-AC5` required and exercised that absence (og_i1.py:415, implicitDeny recorded PASS) while OG-a-1's 18 tests ran on moto, which enforces no IAM. REMEDIED on Andrew's word (\"Go ahead with the fix\"): DeleteItem added under the unchanged LeadingKeys RUNTIME#* condition, applied via safe-apply, EXERCISED on the host under the instance role, ledger CLOSED. Andrew's own screen showed a DIFFERENT, benign defect (stale pre-deploy client_ids -> invalid_client), which is why this took a journal read to find.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE INCIDENT, from the host journal (SSM on i-07dccb1615503ac99, journalctl -u opal-gateway, read 15:51Z): 14:55:21Z `POST /register` 201; 14:55:34Z `/authorize?client_id=mcp-iLcAi35L7ueDQvPN7Ikp9w` 307 (to Entra); 14:55:37Z `NFRA_OPLGTW access-state ALARM: delete_item on gateway-access-state-table: AWS error AccessDeniedException -- FAIL-CLOSED (DEPENDENCY_UNAVAILABLE)` then `GET /callback?code=...` 503. Reproduced identically at 15:16:04Z / 15:16:07Z. The 05:58:10-13Z burst of `POST /token` 400 is every pre-deploy session's refresh being refused (row W3-S3, by design); no login succeeded between the deploy and the fix. Denominator: every /callback in the journal since the deploy = 3 (two 503, one 400 at 15:10:18Z on a re-submitted code).",
        "THE STOP/START DID NOT CAUSE IT: `/authorize?client_id=mcp-9a0_5b-y1pY3OY-IbZuW_w` returned 400 at 14:50:10Z, BEFORE OG-i-4's stop at 14:53:17Z. That client_id, `mcp-CJIWCw...` (14:55:00Z) and `mcp-tq7R3iN8...` (15:17:20Z, followed by a favicon 404 = a browser rendering the error page Andrew saw) were minted by the pre-05:58Z in-memory build; the durable store never held them. `dynamodb scan gateway-access-state-table` at 15:4xZ: 9 items, exactly 1 `RUNTIME#client#` (created_at 1789743321 = 14:55:21Z). Reconnecting from Claude re-registers; it then died at the callback.",
        "THE CONTRADICTION, at the bytes: `infra/aws/terraform/opal-gateway/schwab_access_state.tf:100-108` @d9cdb39063 Sid AccessStateRuntimeWritesRuntimeKeysOnly Action [PutItem, UpdateItem] only; `infra/aws/ec2/opal-gateway/app/oauth_as.py:649` `st.delete_runtime(key, expr + \" AND #og_nonce = :og_nonce\", ...)` and `:772` `st.delete_runtime(key, \"attribute_exists(#og_pk)\", ...)`; deployed bytes = HEAD (`git diff 1764e54a16 HEAD -- app/oauth_as.py app/access_state.py app/server.py` empty; EC2_MANIFEST deployed_commit 1764e54a16, deployed_at 2026-09-18T05:58:16Z). `NFRA_OPLGTW_DECOMP.md:182-183` and `OGI1-AC5` require `no DeleteItem`; `probes/og_i1.py:415` asserts (\"dynamodb:DeleteItem\", \"RUNTIME#probe-og-i1-sim\", \"implicitDeny\") and recorded PASS. `tests/test_oauth_durable.py` runs the real Starlette app over moto 5.2.3 (result file, OG-a-1) -- no IAM evaluated.",
        "THE CONTRACT PERMITS THE DELETE: `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.1 `state_store.key_namespaces.RUNTIME` = \"client/pending-auth/code/refresh/ticket/catalog; runtime conditional writes and expiring records\"; only POLICY reads \"no TTL or ordinary delete\". Ruled the same tick by 1.0.0_SA_CTO R-OG-21 (RULINGS_NFRA_OPLGTW_20260916.md @157b426b2d): no contract amendment; DECOMP:182 struck as to RUNTIME#; OGI1-AC5 retired prospectively; the CTO also found DECOMP:182 names a TransactWrite grant that exists in neither policy.",
        "THE REMEDY, four axes. DESIRED: schwab_access_state.tf Action [PutItem, UpdateItem, DeleteItem], LeadingKeys RUNTIME#* condition unchanged. Plan: pre-edit rc=0 `No changes` (the arm that makes the post-edit change attributable); post-edit 84 resource_changes, 1 non-no-op (`aws_iam_role_policy.gw_access_state_runtime` update, replace_paths None), `0 to add, 1 to change, 0 to destroy`. APPLIED: `.tools/safe-apply.sh` from the saved planfile, `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`; `iam get-role-policy` reads the three actions under ForAllValues:StringLike LeadingKeys [RUNTIME#*] + Null false; post-apply plan `No changes`. EXERCISED (SSM 14330e8e-0532-4c3a-a117-90a55d6cf64f, gateway venv boto3 under opal-gateway-role, 16:37:05Z): put RUNTIME#probe-ae-deleteitem-20260918T163705Z OK; conditional delete_item SUCCEEDED; strong read-back present=False. DISCRIMINATION: delete_item on a POLICY# key still AccessDeniedException -- the confinement R-OG-21 rests on -- and the same action was AccessDenied in the journal before the apply. Service active, local /mcp 401, 0 ALARM lines since 16:00Z.",
        "LEDGER: `org/critical_paths/change_management/20260918T1624Z_nfra-oplgtw-gw-runtime-deleteitem_deploy_completion.md`, opened and committed @c298ed4b68 BEFORE the act, 3 legs proven, CLOSED, sentinel removed. Andrew-direct record: `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/ANDREW_DIRECT_20260918_16xxZ_GATEWAY_LOGIN_FIX_RUNTIME_DELETEITEM.md`. Rollback: remove the one action, one apply."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OG-a-1 (durable OAuth) and OG-i-1 (the table and its grants) are both `complete`, each with every mechanical criterion PASS. OGI1-AC5: \"the runtime grant allows Get, Put, Update and TransactWrite on exactly the table ARN, with write actions conditioned on dynamodb:LeadingKeys matching RUNTIME#*, and no DeleteItem or table-admin action.\" OG-a-1's result: \"pending authorization ... consumed conditionally at the callback\". The PRD's operator journey presumes a user can sign in.",
    "world_is": "Both cells were green and no user could sign in for ten and a half hours, because the property the two cells SHARE -- the runtime role's action set against the actions the shipped code issues -- was measured by neither: OG-i-1 measured the grant without the code, OG-a-1 measured the code without the grant. CLAUDE.md Rule 22's shared-dependency clause with its sharpest instance: the per-member arm was not merely unchecked but ACTIVELY PASSING, and OGI1-AC5's PASS condition WAS the outage condition (1.0.0_SA_CTO, msg 98008). By Rule 22's negative mirror this is an INCIDENT (the guard's absence FIRED, on 3 of 3 callbacks since the deploy), not an exposure -- so the remedy is the grant AND the re-opening of what the gap admitted, which here is nothing: no login succeeded, so no state was written on the broken path; the one client record and the pending/code records it created are ordinary and expire. The walkthrough gates G-C/G-D, the only cells that would have run a real login, were HELD on Andrew's word the whole window, which is why the integrated release shipped with the flow never once exercised end-to-end.",
    "notes": "ARMED, disarm_owner 2.0.0_SA_COO~O, on ONE open arm: a real end-to-end login has NOT yet been observed since the fix -- the IAM action is exercised, the /callback path is not. DISARM CONDITION (readable by that lane via SSM without any identity read): the journal shows one `GET /callback` answering 302/303 followed by one `POST /token` 200 after 16:37Z; Andrew's reconnect from Claude is the expected producer and this seat has asked for it. NOT CLAIMED: that branch (2) -- consuming by conditional UpdateItem marking consumed_at, which keeps the grant narrower -- is unnecessary; 2.0.0_SA_COO~O carries it as a round-2 correctness item and this row does not pre-empt it. THE CARRY, beyond Rule 22's clause: A CRITERION THAT REQUIRES THE ABSENCE OF A PERMISSION THE SHIPPED CODE NEEDS PASSES BECAUSE THE SYSTEM IS BROKEN, and keeps passing exactly as long as it stays broken -- the moto arm and the IAM arm must meet in ONE invocation (a live-role call of the code's own consume path, or a per-action census of the code's boto3 verbs against the policy's Action list) before a release is cut. COST: one census. NON-APPLICATION: a code path whose store is exercised through the deployed role in its acceptance."
  },
  {
    "id": "NFRA_OPLGTW-S47",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T17:52Z",
    "one_line": "Disarm evidence for S46 by its named owner: the first end-to-end Gateway login since the DeleteItem fix completed -- POST /register 201 (17:33:16Z) -> GET /authorize 307 -> GET /callback 302 -> POST /token 200 (17:34:08Z), 0 AccessDenied since 16:37Z -- and the issued token served a tool call through the MCP client.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM command 1bcf7062-ad77-48f2-aa21-071f9494a804 on i-07dccb1615503ac99, journalctl -u opal-gateway --since 2026-09-18 16:37:00 UTC, filtered to method + path + status (query strings stripped, no identity read). DENOMINATOR, every login-path request in the window = 6: 17:00:23Z GET /authorize 400, 17:00:31Z GET /authorize 400, 17:33:16Z POST /register 201, 17:33:18Z GET /authorize 307, 17:34:08Z GET /callback 302, 17:34:08Z POST /token 200. `grep -c AccessDenied` over the same window = 0 (the invocation status reads Failed only because grep -c exits 1 on a zero count).",
        "The two 17:00Z 400s precede the 17:17Z removal of the stale client-side mcpOAuth entry and match S46's benign stale-client_id defect; after the removal the client re-registered (the 201) and the flow ran clean.",
        "OUTCOME PLANE, a different instrument from the journal: in a fresh Claude Code session at ~17:50Z, the opalgateway tool `whoami` returned a Microsoft Graph user profile (HTTP-level success; the profile content is not recorded here). A tool listing and call require the bearer token the 17:34:08Z POST /token issued."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "S46 names 2.0.0_SA_COO~O as disarm owner on one open arm: after 16:37Z the journal shows one GET /callback answering 302/303 followed by one POST /token 200.",
    "world_is": "Met exactly: one /callback 302 and one /token 200 at 17:34:08Z, with no AccessDenied in the window, and the resulting token served a real tool call. The permission is exercised AND the outcome is exercised.",
    "notes": "EVIDENCE for S46's disarm, not its adjudication -- S46's disposition stays 3.0.0_SA_CVO's at L9. Round-2 carries S46 names are unaffected: branch (2) conditional UpdateItem consume, and a LOGIN-PATH health check (liveness does not prove usability). This read also releases the hold on OG-r-2 (the host benchmark was held so it would not muddy this measurement)."
  },
  {
    "id": "NFRA_OPLGTW-W2-S10",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~2",
    "surfaced_at": "2026-09-18T20:30Z",
    "one_line": "OGR2-AC6's written bar ('regresses by no more than 20 percent with zero failures') is measured UNSATISFIABLE in every window this cell can construct on the live ALB target group opal-gateway-tg, because the BEFORE window (OG-p-1's OGP1-AC11, 2026-09-02..2026-09-16, predating every change this project has made) already carries a non-zero HTTPCode_Target_5XX_Count -- so 'zero failures' was never true of this system's baseline, not something OG-r-2 caused or can restore.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN this turn: `.tools/aws cloudwatch get-metric-statistics --namespace AWS/ApplicationELB --metric-name HTTPCode_Target_5XX_Count --dimensions Name=LoadBalancer,Value=app/opal-gateway/89166a68f337e5a4 Name=TargetGroup,Value=targetgroup/opal-gateway-tg/00997fc81f087cb8 --start-time 2026-09-02T19:15:00Z --end-time 2026-09-16T19:15:00Z --period 1209600 --statistics Sum` (OG-p-1's own OGP1-AC11 window, re-read live) -> Sum=19.0 -- non-zero, and this window ends before OG-i-4's resize (2026-09-18T14:53:48Z) or OG-r-1's release even existed.",
        "RUN this turn: the identical call over the 14-day trailing window ending now (2026-09-04T20:01:41Z..2026-09-18T20:01:41Z) -> Sum=18.0, sample_count=38903.0, p95=0.5516718987799433s (vs before p95=0.5535024102704742s -- a -0.33% change, well inside the 20% cap); and over a narrow post-resize-only window (2026-09-18T14:53:00Z..2026-09-18T20:02:00Z) -> Sum=2.0 of 119.0 samples.",
        "READ org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json:117-153 (OGP1-AC11): records TargetResponseTime SampleCount/p95 for that same before-window but carries no HTTPCode_Target_5XX_Count field at all -- 'zero failures' was never actually measured as part of establishing OG-p-1's own baseline, only asserted in this cell's own PRD language (PRD @f0aa50dbc0 :288, 'A14 compares a declared identical existing-user workload before/after: no failures and no more than 20 percent p95 latency regression')."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-OG-r-2 OGR2-AC6: 'the existing-workflow p95 after, against OG-p-1's before, regresses by no more than 20 percent with zero failures, workload, sample counts and windows printed.' Bounds: 'Spec frozen; REFUSE what you cannot meet as written ... never lower a limit or raise a cap to pass.'",
    "world_is": "The p95-regression half of OGR2-AC6 is comfortably met (regression is actually negative -- an improvement). The 'zero failures' half is measured FALSE in both windows available to this cell, and was ALREADY false before this project touched anything (the pre-existing background HTTPCode_Target_5XX_Count rate on this shared target group is ~1.3-1.4/day, essentially unchanged after: 19/14d before vs 18/14d after). This cell's own probe (og_r2.py ac6()) grades AC6 on the LITERAL written text rather than substituting a regression-only reading, so OGR2-AC6 records FAIL-OGR2-AC6 even though nothing this project did made latency or failures worse.",
    "notes": "Not disarmed by this worker: disarming would require either (a) Andrew/CTO ruling that AC6's 'zero failures' clause means 'no failure-RATE increase versus the declared before-measurement' (in which case AC6 would re-grade PASS on the printed evidence already in CAPACITY.json), or (b) accepting the FAIL as the honest, correct reading of the written bar and closing this cell's proof with it disclosed (as OG-r-1's round did with 3 of 18 genuine FAILs). This worker's <paths> grant does not include the PRD or this order's own acceptance text, so neither a bar reinterpretation nor a bar amendment is this worker's to make; graded literally and left ARMED for the issuing COO/CVO at L8/L9. COST: none beyond this row -- OGR2-AC6 stands as measured FAIL in the proof instance. NON-APPLICATION: any future window in which HTTPCode_Target_5XX_Count reads exactly 0 -- that would satisfy the literal text and this row would disarm on remeasurement, not on reinterpretation."
  },
  {
    "id": "NFRA_OPLGTW-S48",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T22:05Z",
    "one_line": "OGR2-AC2 PASSES while its own recorded maximal job peaked at 282021888 bytes against a 268435456 cap -- 13.6 MB OVER -- because the harness grades a job that ended LIMIT_EXCEEDED as cap-respected WITHOUT reading its RSS at all; the criterion's written bar is 'stay within 256 MiB', the guard bounds a child ~5 percent ABOVE the cap rather than at it, and the result file's evidence column reads '3 of 3 jobs cap-respected' with the overshoot nowhere in it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AT THE BYTES, the grading rule: infra/aws/ec2/opal-gateway/tests/acceptance/onhost_bench.py:418-421 @0279872d7a -- `def _cap_respected(js): if js[\"ok\"]: return js[\"peak_child_rss_bytes\"] <= CONTRACT_JOB_MEMORY_BYTES; return js[\"code\"] in (\"BUSY\", \"LIMIT_EXCEEDED\")`. The RSS comparison is on the ok=True branch ONLY. A job that dies of the cap takes the second branch and is graded True with its measurement unread.",
        "THE MEASUREMENT, from the cell's own record (CAPACITY.json @0279872d7a): ac2.maximal = {peak_child_rss_bytes 282021888, ok false, code LIMIT_EXCEEDED, cap_respected true}; ac2.job_memory_cap_bytes = 268435456. Overshoot 13586432 bytes = 5.06 percent. The two concurrent jobs are ok=True at 221220864 and 221687808, genuinely under. So the denominator that matters is 1 of 3 jobs, not 0 of 3.",
        "THE DISCRIMINATOR, and it is inside this same cell: ac4's export job peaked at 270581760 with the SAME code LIMIT_EXCEEDED and is graded FAIL -- because AC4's text demands the CSV be GENERATED, so its probe reads ok/code rather than cap_respected. Identical instrument, identical outcome code, opposite verdict, and the one that PASSES is the one whose criterion text is about the memory bound. Re-run by this seat from the SHARED tree at 0279872d7a (a different checkout from the worker's): AC2 PASS, AC4 FAIL, proof-of-spec-check VALID rc=0 -- the verdicts reproduce; what is at issue is what AC2's PASS MEANS.",
        "NOT ALLEGED: that the worker weakened anything. The rule is in the harness it wrote openly, the number is in the record it committed, and it disclosed the AC6 bar it could not meet (row W2-S10). What is missing is the same disclosure for AC2 -- an interpretation ('refused as designed satisfies stay within') was applied silently where the neighbouring criterion's was filed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "OGR2-AC2: 'the maximal and concurrent Unicode query fixtures each stay within 256 MiB resident memory per job.' The PRD's admission arithmetic reserves the existing peak RSS times 1.25 plus 128 MiB per child, which presumes a child bounded BY the per-job cap.",
    "world_is": "One of the three jobs did not stay within the cap; it exceeded it and was then refused. Whether AC2's bar is 'never exceeds' or 'exceeds only into a designed refusal' is a SPEC question, and the answer changes both the grade and the admission reserve: if a child can transiently reach 1.05x the cap, two concurrent children can reach 562036736 bytes against a reserve computed as 375753728, on a host with 1936322560 total. Routed to 1.0.0_SA_CTO with a recommendation; NOT self-ruled, because a COO reading its own cell's bar wider is the move this row exists to catch.",
    "notes": "ARMED, disarm_owner 2.0.0_SA_COO~O, on ONE condition: the CTO rules what AC2's bar admits. DISARM = that ruling recorded, AC2 re-graded against it (a re-grade may leave the PASS standing), and the result file's '3 of 3 jobs cap-respected' line amended to carry the overshoot either way. THE CARRY: A GRADING HELPER THAT SHORT-CIRCUITS ON AN ERROR CODE STOPS READING THE MEASUREMENT THE CRITERION IS ABOUT, and it passes LOUDEST exactly when the system is at its limit -- the same shape as OGI1-AC5, whose PASS condition WAS the outage condition (row S46). Ask of any pass/fail helper: on the failure branch, does it still read the quantity the criterion names? COST: one read of the helper's branches. NON-APPLICATION: a criterion whose text IS about the refusal ('returns BUSY or LIMIT_EXCEEDED as designed', which is AC3's shape) -- there the code IS the measurement."
  },
  {
    "id": "NFRA_OPLGTW-S49",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T22:55Z",
    "one_line": "THE 5xx BEHIND OGR2-AC6 IS NOT AN AMBIENT BACKGROUND RATE AND CALLING IT ONE UNDERSTATES IT: across 15 days the target group's HTTPCode_Target_5XX_Count is NON-ZERO ON FOUR DAYS ONLY and ZERO ON ELEVEN, and TODAY'S TWO ARE OUR OWN OUTAGE -- the 14:00Z and 15:00Z buckets hold exactly the two /callback 503s row S46 records at 14:55:37Z and 15:16:07Z. An ATTRIBUTABLE incident was read as weather.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DAILY SERIES, my instrument (CloudWatch GetMetricStatistics, AWS/ApplicationELB, TargetGroup targetgroup/opal-gateway-tg/00997fc81f087cb8 + LoadBalancer app/opal-gateway/89166a68f337e5a4, period 86400, Sum, 2026-09-04..2026-09-18 = 15 day-buckets, DENOMINATOR PRINTED): 5xx datapoints exist on FOUR days only -- 09-04 = 3, 09-09 = 3, 09-10 = 13, 09-18 = 2. The other ELEVEN days return NO DATAPOINT, which for a Sum over a period with traffic (RequestCount is non-zero on all 15) is a true zero. HTTPCode_ELB_5XX_Count: no datapoints at all over the whole span, so every error is TARGET-side, never the load balancer's own.",
        "HOURLY, the discriminator (period 3600 on the three recent cluster days): 09-09 20:00Z=1, 21:00Z=2; 09-10 00:00Z=2, 01:00Z=2, 02:00Z=2, 03:00Z=2, 06:00Z=1, 13:00Z=3, 14:00Z=1; 09-18 14:00Z=1, 15:00Z=1. Bursts inside single hours, not a rate spread across the day.",
        "TODAY'S TWO ARE THE OUTAGE, on two instruments that are not each other: row S46's journal read (SSM, i-07dccb1615503ac99) records `GET /callback` 503 at 14:55:37Z and again at 15:16:07Z, and says 'every /callback in the journal since the deploy = 3'. The ALB metric independently puts exactly 1 in the 14:00Z bucket and exactly 1 in the 15:00Z bucket. Two counts, two planes, same two events.",
        "WHAT I DID NOT ESTABLISH: the origin of 09-04 (3), 09-09 (3) and 09-10 (13). Those 19 sit in OG-p-1's BEFORE window and predate the release; they are bursts, and a burst has a cause, but I did not read a journal that far back and do not claim one. That is the remaining question, not a settled finding."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Row W2-S10 (0.9.0_WK_NFRA_OPLGTW~2) states the BEFORE window's non-zero 5xx makes OGR2-AC6's 'zero failures' unsatisfiable because it was 'never true of this system's baseline, not something OG-r-2 caused or can restore', and my own 22:11Z message to 1.0.0_SA_CTO called it 'an ambient background rate'.",
    "world_is": "The DIRECTION is right -- the criterion is unsatisfiable in the windows this cell can build, and W2-S10's core claim stands. The CHARACTERISATION is wrong in a way that changes the remedy. 'Ambient' says irreducible weather, which argues for weakening the bar to a rate comparison. Four-days-in-fifteen with eleven clean days says EPISODIC AND ATTRIBUTABLE, which argues for a bar that excludes named incidents and keeps 'zero' otherwise -- and the eleven zero days prove a zero-failure window is CONSTRUCTIBLE, which is the opposite of unsatisfiable. Today's two are already attributed, to our own DeleteItem outage.",
    "notes": "ARMED, disarm_owner 2.0.0_SA_COO~O, on ONE condition: 1.0.0_SA_CTO's ruling on call 2 of my 22:11Z message, reached with THIS series in hand rather than the 'ambient' framing. MY REVISED REC, sent as a correction: grade AC6 on a window free of named incidents, keeping the literal zero, rather than replacing zero with a rate comparison. Does NOT disturb W2-S10, whose own disposition is the CVO's at L9. THE CARRY: 'AMBIENT' IS A CAUSAL CLAIM WEARING A STATISTICAL WORD -- a non-zero count over a long window says nothing about whether the events are irreducible, and the instrument that settles it is one resolution step finer, not one wider. I wrote 'ambient' myself from a 14-day SUM, in a message recommending a spec change, and the hourly series that refuted it cost one call. COST: one finer-period query before any sentence calling a rate ambient, background or baseline. NON-APPLICATION: a series already read at the grain where the events happen."
  },
  {
    "id": "NFRA_OPLGTW-S50",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T23:40Z",
    "one_line": "R-OG-25 ORDERS A RE-SEAL THAT ALREADY LANDED TEN HOURS EARLIER (@d5af54a90a, 13:53Z) -- so G-C's stated precondition is ALREADY MET and the gate can be scheduled now; and the ruling's OWN standing bar was being violated at the moment it was written, because the new salt AND the six real answers sat in C:/tmp again, the same undefended path whose loss caused row S42.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE RE-SEAL LANDED: `git show --stat d5af54a90a` = 'drain: merge wk-oplgtw-6-reseal (row gate clean on the merged index)', 2026-09-18 09:53:17 -0400 = 13:53:17Z, touching SEALED_EXPECTED.json (+36/-6), probes/og_v4.py (+177) and the channel (+23). `git merge-base --is-ancestor d5af54a90a HEAD` = true. R-OG-25 was sent 23:24:57Z, nine hours thirty-one minutes later.",
        "THE ORDERING TEST IS SATISFIABLE BY CONSTRUCTION, AND THE RULING'S OWN FORM IS WHY: it asks that the re-seal commit be a git ANCESTOR of the first commit in G-C's deliverables directory. That directory is EMPTY at HEAD (the walkthrough has not happened) and d5af54a90a is already in CLOUD's history, so every future commit there descends from it. The test cannot be gamed later precisely because the re-seal is already fixed in the graph.",
        "THE BAR WAS BEING VIOLATED WHILE IT WAS BEING WRITTEN: `C:/tmp/nfra-oplgtw-sealed/expected/` held SALT.txt (64 bytes) AND RQ1..RQ6.txt (151, 473, 174, 287, 535, 329 bytes), all written 09-18 09:27 local. Seven files, none defended. The ANSWERS in clear are the worse half: the salt only protects the digests, while RQ1..RQ6 ARE the expected answers.",
        "REMEDIED THIS TICK, and verified: all 7 written to SSM SecureString under /opal/nfra_oplgtw/ogv4/reseal_20260918/ (rc=0 each), then read back with --with-decryption and compared by sha256 against the local bytes -- 7 of 7 MATCH. Values were never printed to a transcript, a log or a commit; only names, byte lengths and hash-equality booleans.",
        "NOT DONE, deliberately: the C:/tmp copies are NOT deleted. The probe still reads that path, and deleting the working copy before the cell is re-handed would repeat S42's failure from the other direction. The defended store is now the COPY OF RECORD; the temp copy is a convenience that may vanish without loss."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "R-OG-25: 'THE RE-SEAL IS ORDERED, AND G-C IS NOT SCHEDULED UNTIL THE RE-SEAL COMMIT HAS LANDED', and its standing bar: 'an input a HELD or SEALED cell will need at grading time lives in a DEFENDED STORE with a named retention owner, never a temp path.'",
    "world_is": "The re-seal commit HAS landed and is an ancestor of HEAD, so the precondition is met and G-C is schedulable on this evidence rather than on a new act. The bar's substance was unmet until this tick and is now met for all seven inputs, with the retention owner named: 2.0.0_SA_COO~O until OGV4-AC9 commits the salt and answers as drain evidence, after which the repo record supersedes.",
    "notes": "INERT: nothing is armed, because the exposure the bar names is closed and the ordering question is answered by a commit that already exists. THE CARRY: A RULING CAN BE CORRECT AND ALREADY SATISFIED, AND THE SEAT THAT RECEIVES IT IS THE ONLY ONE POSITIONED TO NOTICE -- the adjudicator reasons from the row as filed (S42, 12:22Z) and cannot see a remediation that landed after it. So a ruling's execution starts by MEASURING ITS PRECONDITION, not by performing the act; here that turned a re-seal into a citation and unblocked a gate the same tick. COST: one git show plus one is-ancestor. NON-APPLICATION: a ruling whose act is idempotent and cheap, where measuring costs more than redoing."
  },
  {
    "id": "NFRA_OPLGTW-S51",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-18T23:45Z",
    "one_line": "R-OG-24's ordered census, run with its denominator: `cap_respected` has exactly ONE code definition and TWO reading files, so the vacuous grader's blast radius is 2 criteria -- AC2's verdict AND AC8's `memory_cap_respected_every_job` field, a PASSING criterion carrying a contaminated field -- not the whole cell; and my own 562036736 figure was a transcription of a number that exists nowhere in the record, the arithmetic being 564043776.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE CENSUS (comp-find 'cap_respected', corpus=all): DENOMINATOR 37 hits across 168361 files scanned; 68653 ephemeral-floor, 11 unreadable and 4884 binary files NOT searched and NOT covered by this count. Bands: SURFACED 10, CONFIG 8, TEST 8, DOC 11.",
        "RESOLVED BY BAND, which is what makes the number usable: the 8 TEST hits are all onhost_bench.py -- the definition at :418 and calls at :432, :435, :469, plus consumption at :439-440, :485, :491. The 5 SURFACED code hits are all probes/og_r2.py:67-73, which reads the field for AC2 ONLY (the other 5 SURFACED hits are my own tool-run logs). The 8 CONFIG hits are recorded DATA (CAPACITY.json, the proof instance). The 11 DOC hits are this channel, the ruling and my messages -- prose about the defect, never a consumer of it. So: 1 definition, 2 reading files, 0 consumers outside this cell.",
        "THE BLAST RADIUS IS TWO CRITERIA, NOT ONE AND NOT ALL: AC2's verdict reads all_cap_respected (:439-440 -> og_r2.py:72). AC8 carries checks.memory_cap_respected_every_job = ac2.all_cap_respected (:491), so AC8 PASSES while reporting a field derived from the same vacuous grader -- strictly harder to notice than a wrong verdict. AC4 calls _cap_respected at :469 but its probe grades on ok/code, so its VERDICT is unaffected while its recorded cap_respected field is equally vacuous.",
        "THE ARITHMETIC REPAIR: 2 x 282021888 = 564043776. The 562036736 I sent is 2 x 281018368, and 281018368 appears NOWHERE in CAPACITY.json -- every peak_child_rss_bytes in the record reads 282021888 (maximal), 221220864 and 221687808 (concurrent), 270581760 (export) or 214065152 (largest successful probe). It was not another run's peak; it was a transcription error with no source. The CTO's reconciliation is right and its conclusion holds on either figure: both exceed the 375753728 reserve by more than 185 MB."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "R-OG-24: 'CENSUS cap_respected's CONSUMERS BEFORE ANY OF THEM IS QUOTED AGAIN, AND PRINT THE DENOMINATOR. I name no count because I have not run it', and: 'ONE NUMBER DOES NOT RECONCILE ... The doubling must print its own input.'",
    "world_is": "Both executed. The census bounds the defect to this cell's own instruments -- no other project or tool consumes cap_respected -- and names the second contaminated grade (AC8's field), which neither the call nor the ruling had identified. The doubling's input is 282021888 and its correct product is 564043776.",
    "notes": "INERT: the repair itself is round-2 work (draft cell R2-b), already forked there; this row records the measurement the ruling ordered and the corrected number. THE CARRY: A SHARED-LIMB DEFECT'S BLAST RADIUS IS BOUNDED BY A CENSUS, AND THE CENSUS'S VALUE IS THE BAND RESOLUTION, NOT THE TOTAL -- 37 hits reads like 37 exposures; resolving them into 1 definition, 2 readers and 30 mentions is what turns a number into a scope. COST: one comp-find plus reading its bands. NON-APPLICATION: a term whose hits all sit in one file already."
  },
  {
    "id": "NFRA_OPLGTW-S52",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-19T00:35Z",
    "one_line": "THE 19 UNNAMED 5xx ARE NAMED, AND THEY ARE ONE CAUSE CLASS: all 19 are `POST /graph/cypher` 502 on the graph endpoint -- none on the Schwab, login or MCP path -- each preceded by a `/graph/health` 200 and followed by a successful retry within seconds, which is a transient window on the graph backend and not a Gateway fault. So 09-04, 09-09 and 09-10 become eligible window material under R-OG-23, and OGR2-AC6's literal 'zero failures' is now satisfiable on an incident-excluding window.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RETENTION FIRST, because an absence here would have been unfalsifiable: the host journal's earliest line is 2026-08-15T03:02:10Z (journalctl -u opal-gateway | head -1), 799.7M archived and active. All three days are INSIDE the window, so a zero would have meant zero, not lost data.",
        "THE ENUMERATION (SSM 69a99012-e05f-4476-b3a8-7e7196c56bc1 on i-07dccb1615503ac99, method+path+status only, query strings stripped, no identity read): 09-04 = 3 (16:09:03, 16:36:15, 17:15:41), 09-09 = 3 (20:30:38, 21:21:54, 21:24:42), 09-10 = 13 (00:26:45, 00:27:01, 01:47:10, 01:47:16, 02:43:31, 02:43:37, 03:17:20, 03:17:24, 06:07:31, 13:35:06, 13:54:52, 13:55:24, 14:01:40). Every single line is `POST /graph/cypher HTTP/1.1 502`. Denominator 19 of 19, one endpoint, zero exceptions.",
        "CORROBORATION ACROSS PLANES: 3 + 3 + 13 = 19 matches the CloudWatch HTTPCode_Target_5XX_Count day-buckets in row S49 exactly, derived from the ALB metric and never from the journal. Two instruments sharing no mechanism, same three days, same three counts.",
        "THE CAUSE, at the minute (SSM a4d7d30c-f8c4-4996-b03e-ca53b0ab49cd, 13:34:30-13:35:30Z): 13:35:06 `GET /graph/health` 200, then `POST /graph/cypher` 502 in the same second; 13:35:12 `/graph/health` 200 and `/graph/cypher` 200 -- the retry SUCCEEDS six seconds later. The pairing at 00:26:45/00:27:01, 01:47:10/01:47:16, 02:43:31/02:43:37 and 03:17:20/03:17:24 (16, 6, 6 and 4 seconds apart) is the same shape. A liveness endpoint reporting 200 while the query path is briefly unserviceable is a SWAP/RELOAD WINDOW on the graph store, which `graph_status` exposes as `last_swap`.",
        "WHAT THIS DOES NOT CLAIM: that the swap window is harmless, or that it is in this project's scope to fix. It is the graph surface's own behaviour, outside NFRA_OPLGTW's boundary, and it is named here only to the degree AC6's bar requires -- WHICH ENDPOINT, WHICH CAUSE CLASS, and NOT the Schwab path."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "R-OG-23 (@4ab7ce54fd), the consequence the CTO drew and this lane did not: 'the 19 errors of 09-04/09-09/09-10 are NOT named, so those three days are NOT eligible window material until they are -- an unexamined burst is not a clean day, and \"free of named incidents\" means the incidents in it have actually been named.'",
    "world_is": "They are now named, on two corroborating instruments, as one cause class on one endpoint outside the graded path. Under R-OG-23's own rule the three days become eligible, and the practical consequence is that OGR2-AC6 can be graded on a window that excludes the graph-swap 502s and today's DeleteItem outage, with the literal 'zero failures' bar intact -- which is what the CTO ruled must be preserved.",
    "notes": "INERT: nothing is armed; this closes the naming obligation R-OG-23 created and feeds round 2's AC6 cell (draft R2-c, @94b0c19f27) plus its R2-g item, which can now be dispositioned as NAMED rather than investigated. The AC6 re-grade itself is round-2 work and is NOT performed here. THE CARRY: A HEALTH ENDPOINT AND THE PATH IT CLAIMS TO SPEAK FOR CAN DISAGREE WITHIN THE SAME SECOND -- `/graph/health` 200 beside `/graph/cypher` 502 is the same class as this project's own ten-hour outage, where `/health` 200 + `/mcp` 401 + ALB healthy stayed green while no one could sign in. A liveness check certifies the process, never the capability. COST: one journal read at the minute of a failure. NON-APPLICATION: a probe that exercises the capability itself."
  },
  {
    "id": "NFRA_OPLGTW-S53",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-19T01:15Z",
    "one_line": "S52's phrase 'the three days become eligible window material' is WRONG and R-OG-23A corrects it: a NAMED incident DISQUALIFIES any window containing it, naming was never a licence to excise minutes. The strict reading costs nothing -- and the 7-day clean window it names is REAL AND NOT VACUOUS, which the ruling asserted but did not measure: 09-11..09-17 carries 19473 requests with zero 5xx.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE CORRECTION, R-OG-23A @090e3b5e26: \"'FREE OF NAMED INCIDENTS' MEANS THE WINDOW CONTAINS NONE -- not that the ones it contains have been labelled ... A NAMED INCIDENT DISQUALIFIES ANY WINDOW CONTAINING IT.\" The reading it refuses is the one that would let 'zero failures' be satisfied over ANY data by naming and excising every failure -- a condition satisfiable by shrinking its own denominator, shrunk by the party that benefits.",
        "THE CHECK THE RULING DID NOT RUN, and it is the one that could have made the remedy hollow: a window with zero failures and zero TRAFFIC passes vacuously. Measured by this lane (CloudWatch, same dimensions as S49, period 86400, 7 day-buckets 2026-09-11..2026-09-17): RequestCount 3323, 1123, 1142, 4309, 2778, 5017, 1781 -- every bucket non-zero, TOTAL 19473 requests. HTTPCode_Target_5XX_Count over the identical span: NO DATAPOINTS. So the clean run is clean AND loaded.",
        "THE ARITHMETIC OF THE RUNS, from S49's own day-buckets rather than re-derived: non-zero on 09-04, 09-09, 09-10, 09-18; eleven of fifteen are true zeros; contiguous clean runs are 09-05..09-08 (four days) and 09-11..09-17 (SEVEN). The seven-day run is the longest available and needs no excision, no attribution argument and no judgment call.",
        "WHAT S52 GOT RIGHT AND KEEPS: its operative sentence describes grading AC6 on a window that EXCLUDES the graph-swap days and the 09-18 outage, which is exactly what the strict reading requires. Only the label 'eligible window material' was loose, and only that is retracted here."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "R-OG-23A: the naming obligation is discharged and closed by S52, but 'free of NAMED incidents' means the window CONTAINS none; a 7-day contiguous clean span already exists.",
    "world_is": "Accepted without reservation, and the span is verified non-vacuous on this lane's own instrument. OGR2-AC6 is gradeable in round 2 on 09-11..09-17 with the literal 'zero failures' bar intact over 19473 real requests. The AC6 re-grade is NOT performed here.",
    "notes": "INERT. Supersedes S52's LABEL only; S52's enumeration, corroboration and cause-pinning stand unchanged. THE CARRY, and it is the second half of a trap this channel already knows: A BAR CAN BE WEAKENED AT ITS WINDOW'S EDGES WITHOUT EVER TOUCHING THE BAR -- 'zero failures on a window I choose' and 'zero failures' are different claims, and the first reads as the second in every record. THE MIRROR: the strict reading then needs its OWN check, because a window with no traffic has no failures either. So a clean-window claim prints TWO numbers -- the failure count AND the denominator that makes zero mean something. COST: one RequestCount query beside the failure query. NON-APPLICATION: a window whose traffic is the thing being measured anyway."
  },
  {
    "id": "NFRA_OPLGTW-S54",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-20T09:45Z",
    "one_line": "G-C/G-E's OWNER re-assignment (ruling 98451) MUST NOT become a PATH re-assignment: the retired lane serial `1.0.0_SA_CTO~A` is a PATH COMPONENT of both gate deliverables, and three of its occurrences sit inside `SEALED_EXPECTED.json`'s pre-seal absence check -- a HASH-BOUND artifact whose whole property is that those exact paths were measured ABSENT at a named commit. Moving the path to match the new owner would destroy the seal PHASE 1 of OG-v-4 exists to hold, and it would look like tidy-up.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE RULING'S OWN SCOPE, and this is not a criticism of it -- it named THREE sites: `1.0.0_SA_CTO` msg 98451 @`a0e4748ac2`, VERBATIM: \"The order still names 1.0.0_SA_CTO~A at :34, at :169, and in the decomp's section 6. AMENDING IT IS 2.0.0_SA_COO~O's ACT AS THE ISSUER UNDER RULE 27, NEVER MINE.\" All three are OWNER ATTRIBUTIONS and all three are correct.",
        "THE UNSCOPED CENSUS THE ISSUER RAN BEFORE EDITING (native Grep over `org/missions/D9/NFRA/NFRA_OPLGTW/`, no head, denominator PRINTED): the token `1.0.0_SA_CTO~A` occurs across THIRTEEN files, not three sites. The extra hits are NOT more owner attributions -- they are a DIFFERENT KIND OF OBJECT: the serial is a directory component of the gate deliverables' own paths, `deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md` and `.../G-E_PILOT_IDENTITY_AND_GRANT.md`.",
        "THE THREE THAT MAKE IT LOAD-BEARING, read at the bytes: `deliverables/0.9.0_WK_NFRA_OPLGTW~6/SEALED_EXPECTED.json` carries the G-C path at `:9` (`paths_checked`), `:15` (`reads[].path`) and `:18` (inside the captured `stderr` of `git cat-file -e`), all under `preseal_absence_check.commit = 15edf9f07b1bbea17f1a23fe1697f532ae20ff93`. Its own note states the property: both paths were measured ABSENT at the moment the seal was cut, which is the precondition PHASE 1 requires. A path edit there is not a rename, it is a forged measurement.",
        "THE FOURTH, LIVE RATHER THAN HISTORICAL: `deliverables/0.9.0_WK_NFRA_OPLGTW~6/probes/og_v4.py:27` hardcodes `GC_PATH = \"org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md\"`. That probe is the invocation for every mechanical criterion of OG-v-4 PHASE 2, which has not run. So the path is not merely recorded in history -- it is what the grader will read.",
        "WHAT WAS ACTUALLY EDITED, so the amendment's own scope is falsifiable: OWNER ATTRIBUTIONS ONLY, at TO-OG-v-4 `:35` and `:169`, TO-OG-v-5 `:33` and `:115`, and DECOMP `:783`, `:785`, `:896`. Every PATH string was left byte-identical, and each amended site now says so inline. `project.json:25` and the PRD's accountable-CTO line were NOT touched: those are L3/L4 carriers and belong to `1.0.0_SA_CTO`, not to the issuer."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Ruling 98451: G-C's owner is re-assigned from `1.0.0_SA_CTO~A` to `1.0.0_SA_CTO`, and the issuer carries the change into the carriers.",
    "world_is": "Carried, but NARROWER than a naive reading of 'carry it into the carriers' would license. OWNER moved at seven sites; PATH moved at zero, deliberately, because the retired serial is load-bearing as a path in a hash-bound seal and in the unrun grader's own source. The two readings are indistinguishable in the ruling's words and differ in whether OG-v-4's seal survives.",
    "notes": "INERT -- nothing is armed; no remediation is owed and none is claimed. THE CARRY, and it is the sharpest form of a trap this channel already knows: A RENAME IS A CENSUS PROBLEM WEARING A TIDY-UP'S CLOTHES. When an IDENTIFIER is re-assigned, ask of every occurrence whether it NAMES THE PARTY or ADDRESSES A LOCATION -- the first follows the re-assignment, the second must not, and a global replace cannot tell them apart while looking maximally diligent. ⭐ The discriminator is one unscoped census with its denominator printed, run BEFORE the first edit, and then INSPECTING WHAT IT FOUND OUTSIDE THE NAMED SITES rather than counting them: here 3 named sites vs 13 files, and the decisive four were all outside. COST: one census plus reading its false positives. NON-APPLICATION: an identifier that appears only in prose, and a re-assignment whose new value is intended to move the storage too -- there the seal question is the whole decision and must be asked out loud."
  },
  {
    "id": "NFRA_OPLGTW-S55",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-20T10:05Z",
    "one_line": "RULING 98451 MOVED G-C's OWNER TO A SEAT THE WRITE GATE REFUSES. `deliverables/<SERIAL>/**` admits exactly the serial NAMING THE FOLDER or a `~lane` OF IT -- the relation is one-way, so `1.0.0_SA_CTO~A/` admits `1.0.0_SA_CTO~A` and REFUSES the base `1.0.0_SA_CTO`. Measured rc=1 VIOLATION for the new owner, rc=0 for the retired lane. The gate will fire at the WORST moment -- the instant Andrew answers and G-C is finally writable in every other respect.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE INSTRUMENT IS THE GATE ITSELF, CALLED, NOT ITS RULE RE-DERIVED: `python .tools/owned-paths-validate.py --check-agent <AGENT> .owned-paths.yaml` with the single path `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/1.0.0_SA_CTO~A/G-C_CONTROLLED_IDENTITY_AND_GRANT.md` on STDIN. Stdin was non-empty on every arm, which matters: an EMPTY stdin admits every serial vacuously and would have read as a clean pass for all three.",
        "THREE ARMS, run as a discriminating set rather than one query. (1) `1.0.0_SA_CTO`, the NEW owner under ruling 98451 -> `VIOLATION ... agent=1.0.0_SA_CTO not in permitted_agents`, rc=1. (2) `1.0.0_SA_CTO~A`, the RETIRED lane -> rc=0, no output: POSITIVE CONTROL, the instrument does admit somebody, so the violation is not a blanket refusal of the path. (3) `4.0.0_SA_CRO`, unrelated -> rc=1: NEGATIVE CONTROL.",
        "THE GATE'S OWN WORDS FOR WHY, quoted from its refusal text rather than paraphrased: lane `TREE_DELIVERABLES` -- \"Project tree, deliverables/<SERIAL>/** -- NOBODY by enumeration. The owner is in the PATH (s.6 option ii, RULED): owned-paths-validate.py clause 4 (ADHC_OWNPTH.004) permits exactly the serial named by the sub-folder (or a ~lane of it).\" ⭐ THE PARENTHESIS IS THE WHOLE FINDING: the admission widens from a folder to ITS OWN LANES, and NEVER from a lane-named folder UP TO THE BASE. A reader skimming 'or a ~lane of it' can easily take it as 'base and lanes are interchangeable here'. They are not, and the direction is the entire difference between a write that lands and one that is refused.",
        "WHY IT IS ARMED RATHER THAN MERELY NOTED: every other precondition for G-C is a WAIT (Andrew's answer on the identity administrator, then a person's act). This one is a REFUSAL, and it sits BEHIND those waits, so it is structurally guaranteed to be discovered last -- at the exact moment the project is otherwise unblocked and moving. Nothing has fired yet: G-C does not exist, so no write has been attempted and this is an EXPOSURE, not an incident.",
        "WHY THE OBVIOUS FIX IS REFUSED: writing G-C at `deliverables/1.0.0_SA_CTO/` instead would satisfy the gate and DESTROY the seal -- `SEALED_EXPECTED.json` pins the `1.0.0_SA_CTO~A/` path in its pre-seal absence check at commit `15edf9f07b`, and `probes/og_v4.py:27` hardcodes it as `GC_PATH` for the unrun PHASE 2 grading (row S54). So the path is fixed and the writer must bend to it, not the reverse."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Ruling 98451: G-C's owner is `1.0.0_SA_CTO` -- \"this seat, base, already live\" -- which \"closes the gap with NO spawn\".",
    "world_is": "The gap is closed for LIVENESS and open for WRITE ACCESS. The base seat is live and reachable, and is mechanically refused at the only path G-C may occupy. The ruling's reasoning is untouched by this -- it priced a spawn against an idle seat and was right on that axis; the write surface is simply a different axis and no arm of the ruling examined it.",
    "notes": "ARMED; disarm_owner `1.0.0_SA_CTO`, because the remedy is a choice about that seat's own write and is not the issuer's to make. THREE REMEDIES EXIST AND THE ISSUER'S REC IS (b): (a) add `1.0.0_SA_CTO` to the lane's permitted agents -- a GATE EDIT, widens a guard permanently for one file; (b) commit through `GIT_COMMIT_AUTHOR_OVERRIDE=1.0.0_SA_CTO~A`, which CLAUDE.md 14a names as exactly the escape for a LANE REFUSAL, is AUDITED and is SINGULAR (one lane per commit) -- it costs one environment variable on one commit and changes no guard; (c) re-seat `1.0.0_SA_CTO~A` after all, which ruling 98451 refused on a measured basis that this row does not disturb. THE CARRY: ⭐ A RE-ASSIGNMENT OF AN OWNER IS ALSO A RE-ASSIGNMENT OF A WRITE, AND THE TWO ARE GRADED BY DIFFERENT MACHINERY -- a ruling can name a new owner correctly, on sound reasoning, and hand that owner a path it cannot commit to, because no instrument in the ruling's own reasoning reads the path gate. COST: one `--check-agent` call with the path on stdin, at the moment of re-assignment. NON-APPLICATION: an owner change that does not carry a write, and a path whose grant is by enumeration rather than by the convention."
  },
  {
    "id": "NFRA_OPLGTW-S56",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-20T10:35Z",
    "one_line": "TWO FINDINGS FROM ONE SOURCE READ. (1) S55's adopted remedy (b) WILL WORK and the CTO's stated residual closes with NO throwaway commit: the override is consumed as a PRESENCE TEST. (2) AND THAT IS ALSO A LAW-VS-TOOL GAP -- the value is LOGGED VERBATIM AND NEVER VALIDATED, so CLAUDE.md 14a's `GIT_COMMIT_AUTHOR_OVERRIDE=<LANE>` ... SINGULAR (N lanes = N commits)' is a HUMAN DISCIPLINE, not a mechanism. One override skips the lane check for EVERY staged path in that commit, whatever the value says.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE CONSUMING CODE, quoted at the line rather than searched for: `.tools/git-hooks/owned-paths-check.sh:118-122` -- `if [ -n \"$OVERRIDE\" ]; then echo \"${ISO_TS} OVERRIDE  ${AGENT:-UNKNOWN}  ${N_FILES}  (--author-override ${OVERRIDE} applied)\" >> \"$AUDIT_LOG\" ...; exit 0; fi`, where `OVERRIDE=\"${GIT_COMMIT_AUTHOR_OVERRIDE:-}\"` at `:42`. The value is interpolated into the LOG LINE and is read NOWHERE ELSE: no lane lookup, no path resolution, no comparison against the agent. `-n` is the whole test and `exit 0` is the whole consequence.",
        "THE RUNNING BYTES ARE THE BYTES I READ, which is the trap this class usually dies on: `git config core.hooksPath` resolves to `.git/hooks`, and the active `.git/hooks/pre-commit:73-74` reads `if [ -f \"$ROOT/.tools/git-hooks/owned-paths-check.sh\" ]; then bash \"$ROOT/.tools/git-hooks/owned-paths-check.sh\" \"$@\"`. It INVOKES the tools copy rather than carrying its own, and `ls .git/hooks/` shows no second copy of the checker. So source and deployed are the same object by reference, not by assumption.",
        "COVERAGE OF THE CONSUMER CENSUS, denominator printed: a recursive read of `.tools/` for `GIT_COMMIT_AUTHOR_OVERRIDE` returns TWO files. The second, `ds-precommit-check.py:619`, uses it only as an `actor` LABEL for a DIFFERENT log (`org/dtaflp-seed-import-audit.log`) and never as an authorization. So the escape hatch has exactly one enforcement-side consumer and it is the one quoted above.",
        "WHAT FINDING (1) CLOSES: `1.0.0_SA_CTO` ruled remedy (b) and took an explicit residual -- \"UNEXERCISED is only their COMBINATION\" -- declining a dry exercise because litter under `deliverables/1.0.0_SA_CTO~A/` would spoil PHASE 1's re-seal, which was the right call. The residual closes WITHOUT any commit: because the hatch never inspects its value, `GIT_COMMIT_AUTHOR_OVERRIDE=1.0.0_SA_CTO~A` skips the check that returned the rc=1 VIOLATION in row S55. The combination needed no exercise; it needed a source read.",
        "WHAT FINDING (2) OPENS, and its honest limit: the audit log carries 595 `OVERRIDE` verdicts across the estate (whole-log verdict census: PASS 29933, BLOCK 964, OVERRIDE 595, FORCE-BYPASS 241, SYSTEM-CURRENT-OVERRIDE 161, MERGE-REFUSED 117, NEVER-OVERRIDE 29), so the hatch is exercised routinely and by many seats. ⛔ I have NOT measured whether any single override commit actually spanned several lanes -- the log records a FILE COUNT and never the lanes, so that question is UNANSWERABLE FROM THIS INSTRUMENT and I am not asserting it happened. The claim is strictly about CAPABILITY: nothing in the code could refuse it.",
        "PRIOR-RECORD SEARCH BEFORE ANNOUNCING, because a re-discovery announced as new is its own defect: the token census (1266 files under `org/`) was rejected as the wrong question -- it finds who MENTIONS the override, not who found it unvalidated. A second census written against the CLAIM'S MEANING (presence-test / presence-only / any non-empty / never-validated / not-validated / unvalidated, within 120 chars of override, case-insensitive, whole repo including `.worktrees/`) returned FIVE hits, all unrelated: four are one task order's \"column presence only\" and one is an AWS rail log. No prior record."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md 14a: \"--force bypasses only contamination checks, never a lane refusal -- that escape is GIT_COMMIT_AUTHOR_OVERRIDE=<LANE>, audited, SINGULAR (N lanes = N commits).\"",
    "world_is": "AUDITED is TRUE and is the part that works -- every use writes an OVERRIDE line naming the agent, the file count and the value. `=<LANE>` and SINGULAR are NOT enforced: the hook tests only that the variable is NON-EMPTY, then exits 0 for the entire staged set. A commit spanning four lanes with `GIT_COMMIT_AUTHOR_OVERRIDE=anything` passes exactly as one spanning a single lane, and the audit line records the operator's own words rather than a fact the tool checked.",
    "notes": "INERT -- this is an EXPOSURE, not an incident: no instance of a multi-lane override has been measured, and the instrument that would answer it does not record lanes. NOT A PROPOSAL TO CHANGE THE HATCH, and deliberately so: a presence-only escape is a defensible design (the auditability, not the value, is what makes it safe), and narrowing it is `1.0.0_SA_CTO`'s call on its own law file, not an issuer's. ⭐ THE CARRY: A FIELD THAT IS LOGGED IS NOT THEREBY CHECKED, AND THE AUDIT LINE IS THE DISGUISE -- reading `(--author-override CLOUD_OPS_OR_ETL applied)` in a log, a reader naturally infers the tool resolved CLOUD_OPS_OR_ETL and found it applicable. It did not; it printed what it was handed. This is the same shape as `A_VALUE_MUST_CARRY_ITS_CLAIM`'s consuming half: an unenforced field drifts, and here the field was never consumed at all. COST: one read of the consuming line, which is the only thing that distinguishes a logged value from a checked one. NON-APPLICATION: a field whose consumer you have already read, and a log line you are reading as a RECORD OF AN OPERATOR'S INTENT rather than as evidence of a machine's verdict."
  },
  {
    "id": "NFRA_OPLGTW-S57",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-20T11:05Z",
    "one_line": "R-OG-22's THIRD BRANCH IS CONFIRMED AT THE SOURCE, and the code says something the ruling's inference did not reach: the export materialises the WHOLE result set -- up to THREE full-size in-memory representations at once (`rows`, `prepared`, `rendered`) -- and the `export_rows` LIMIT_EXCEEDED refusal is raised AFTER the allocation, not before it. So peak RSS is a function of the REQUESTED size even on requests that are ultimately REFUSED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "WHAT THE RULING ASKED FOR, and it asked honestly: R-OG-22 (`RULINGS_NFRA_OPLGTW_20260916.md:520-545`) hunted the uncovered member by subtraction and found it -- \"CHANGE NEITHER NUMBER -- MAKE PEAK RSS STOP BEING A FUNCTION OF EXPORT SIZE\" -- from a RATIO: \"9,468,970 bytes of output cost 214,065,152 bytes of peak RSS -- a ratio of about 22.6 to 1.\" It then labelled its own read: \"I have NOT confirmed that read -- it is an inference from a ratio, and I am labelling it as one -- but it is a cheap thing to falsify and it is not in the record at all.\" This row is that falsification.",
        "THE PRODUCTION PATH, read at the bytes: `infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py`, `SchwabService.export_query` (`:820`). `:865` builds the plan with `limit=cap + 1` where `cap = limits.export_rows` (`:845`) -- one MORE than the ceiling, which is the standard overflow-detection trick and is not itself the defect. `:872` `job = await self._engine.run_export(...)`; `:875-877` `rows = value.get(\"rows\")` with `if not isinstance(rows, list)`. ⭐ THE RESULT SET COMES BACK AS A PYTHON LIST. That is materialisation ONE, and it is the engine's own return contract, not a caller's choice.",
        "MATERIALISATION TWO AND THREE, in the same function and simultaneously live: `:897` `prepared = []` then `:898-903` `for row in rows: ... prepared.append(row)` -- a SECOND full-length list, built while `rows` is still referenced and therefore still resident. `:904` `rendered = env.render_rows(prepared, columns)` builds the rendered form from `prepared` -- a THIRD full-size representation. Nothing is streamed, chunked, or released between them.",
        "⛔ THE PART THE INFERENCE DID NOT REACH, AND IT IS THE SHARPER HALF: the refusal is POST-ALLOCATION. `:885-888` `if matched > cap: raise ServiceError(LIMIT_EXCEEDED, \"export_rows_limit\", ...)` sits AFTER `run_export` has already returned the full list at `:872`. So an over-ceiling request PAYS THE FULL MEMORY COST OF UP TO cap+1 ROWS AND IS THEN REFUSED. The guard names the hazard it cannot prevent: by the time `export_rows` is enforced, the allocation that the cap exists to bound has already happened.",
        "WHY THIS EXPLAINS THE OG-r-2 MEASUREMENTS RATHER THAN MERELY CO-EXISTING WITH THEM: `CAPACITY.json`'s ac4 arm peaked at 270581760 and ended LIMIT_EXCEEDED -- which under this reading is EXACTLY the expected shape, because LIMIT_EXCEEDED is reached THROUGH the peak rather than instead of it. A refusal that preceded the allocation would have shown a LOW peak with the same verdict, and it did not.",
        "⚠ THE BOUND ON THIS ROW: this is a SOURCE READ, not a memory profile. I have not instrumented allocation, measured the per-representation sizes, or proven that these three lists account for the whole 22.6:1 ratio -- other contributors (the engine's own buffers, the source objects fetched at `:870`) are unmeasured and plausible. The claim is that the code CONTAINS a whole-result-set materialisation on the production export path and refuses only afterwards; the claim is NOT that these three lines are the complete arithmetic of the ratio."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "R-OG-22: \"The measured evidence is more consistent with 'the whole result set is materialised in memory' than with 'the contract is too big.' I have NOT confirmed that read.\"",
    "world_is": "Confirmed on the production path, and wider than stated: not one materialisation but up to three concurrent ones, with the ceiling enforced after the first. This does not decide R-OG-22's open question 2 (is 250,000 rows / 50 MiB a CONSUMER REQUIREMENT or an aspiration?) -- that is a question about a consumer and remains the CTO's at L4. What it does is make the streaming branch a MEASURED option rather than an inferred one, which matters most in the branch where the answer is 'requirement', since R-OG-22 states streaming is then the only member of the set that serves it.",
    "notes": "INERT -- nothing armed, no remediation owed, no cell cut. ⛔ AND NO CELL IS CUT HERE DELIBERATELY: round 1 is still open (2 pending orders), and LD-0521 makes a round-2 issuance cut before round 1's slug a deadlock on round 1's own L10. This is an INVESTIGATION ROW feeding the round-2 draft, which is exactly what the channel is for. ⭐ THE CARRY: A LIMIT ENFORCED AFTER THE ALLOCATION IT BOUNDS IS A REPORTING FEATURE, NOT A GUARD -- it makes the refusal honest and the host no safer, and the two are easy to confuse because the verdict string is identical either way. The discriminator is ONE READ: find the allocation and the check, and ask which line number is larger. COST: one source read of the enforcing function. NON-APPLICATION: a limit checked against a COUNT the producer supplies before materialising (a COUNT(*) probe, a streamed row counter), where the check genuinely precedes the cost."
  },
  {
    "id": "NFRA_OPLGTW-S58",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-20T11:20Z",
    "one_line": "R-OG-22's default-mirroring defect RUN OVER ITS WHOLE POPULATION: the contract's `limits` block has 26 keys; exactly TWO carry a literal code default, and BOTH mirror their contract value -- `export_rows` (the one already named) and `ticket_seconds` at `integration.py:790` (contract 300, default 300), WHICH WAS NOT NAMED. ZERO differ. And the contract key `export_rows` IS present today, so the class is an EXPOSURE, not an incident.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE FINDING THIS EXTENDS, and its own stated bound: `1.0.0_SA_CTO` msg 98482 -- the code default at `integration.py:845` is 250000, the same value the contract is expected to carry, so \"A MISSING CONTRACT KEY IS INDISTINGUISHABLE FROM A PRESENT ONE, by construction\". It bounded itself explicitly: \"I have measured the two code lines, NOT the contract file. I have not shown the key is ever actually absent; the finding is that the code could not tell you if it were.\" Both halves of that bound are closed below.",
        "HALF ONE -- THE CONTRACT FILE, now read: `org/standards/NFRA_OPLGTW_CONTRACT.json` `limits` carries 26 keys, and `export_rows` IS PRESENT with value 250000, `export_utf8_bytes` 52428800, `job_memory_bytes` 268435456. ⭐ SO NOTHING HAS SILENTLY FALLEN BACK TO A DEFAULT: the class is an EXPOSURE, not an INCIDENT, and no work re-opens. That distinction is the one the law says costs in both directions if conflated.",
        "HALF TWO -- THE POPULATION, which a two-line read cannot see: census over 26 contract keys x 63 PRODUCTION `.py` files under `infra/aws/ec2/opal-gateway/` (`tests/`, `__pycache__`, `.venv` excluded, denominator printed by the instrument). Pattern: `.get(\"<key>\", <int literal>)`. RESULT -- MIRRORED (default EQUALS contract value) = **2**; DIFFERING (a missing key would change behaviour) = **0**; no literal-default read found for the remaining 24.",
        "⭐ THE SECOND INSTANCE, WHICH 98482 DID NOT NAME AND A TWO-LINE READ COULD NOT HAVE: `infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py:790` -- `ticket_seconds`, contract 300, default 300. Same shape, same invisibility, different feature (download-ticket lifetime rather than export ceiling). **So the defect was never one line; of the instances that EXIST, it is 2 of 2 -- the class is universal among them, which is a much stronger statement than \"another one was found\".**",
        "⚠ THE BOUND ON MY OWN INSTRUMENT, stated because the 24-key remainder is the tempting over-read: the pattern catches only `.get(\"key\", <int literal>)` ON ONE LINE. It CANNOT see a default held in a module constant (and one exists nearby -- `export.py:60` `EXPORT_ROWS = 250000  # contract limits.export_rows`), a multi-line call, or a dict-merge fallback. **A key in the no-literal-default list is NOT thereby proven safe; it is UNMEASURED BY THIS INSTRUMENT.** 24 of 26 are in that state and I am not claiming them clean.",
        "WHY THE 0 MATTERS AS MUCH AS THE 2: DIFFERING = 0 means there is no counter-example in the measured set -- no production call site supplies a default that would visibly change behaviour if its key vanished. A mixed result would have suggested the mirroring was incidental. A clean 2-for-2 with no differing case is more consistent with a CONVENTION (mirror the contract value into the default) than with two independent slips, and a convention is fixed once at the pattern rather than twice at the instances."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "R-OG-22 / msg 98482: the `export_rows` code default equals the contract value, so a dropped contract key is indistinguishable from a present one -- measured at two code lines, contract file unread, population unmeasured.",
    "world_is": "Confirmed and extended. The contract key IS present (exposure, not incident). The class has a SECOND named instance (`ticket_seconds:790`) and, among call sites that supply a literal default at all, it is 2 of 2 with 0 counter-examples. 24 keys remain unmeasured by this instrument rather than clean.",
    "notes": "INERT -- nothing armed, no remediation owed, NO CELL CUT. Round 1 is open and LD-0521 makes a round-2 issuance before round 1's slug a deadlock on round 1's own L10; this is an investigation row feeding the round-2 draft, which 98482 agrees is the correct carrier. ⛔ AND IT IS NOT A PROPOSAL TO CHANGE THE DEFAULTS: whether a contract read should fail closed on a missing key is a CONTRACT-SEMANTICS decision owned at L4, and an issuer that 'fixed' it would be choosing a fail-closed behaviour nobody ratified. ⭐ THE CARRY: **A DEFECT FOUND AT ONE CALL SITE IS A POPULATION QUESTION, AND THE POPULATION IS CHEAPER TO MEASURE THAN THE FIRST INSTANCE WAS TO FIND.** Finding the first needed a reason to look at that line; finding the rest needs only the key list you already have and one loop. The asymmetry is why the second instance usually goes unfound -- nobody re-runs the search after a successful hit, because the hit feels like the answer. COST: one loop over the declared key set, once, after any single-site finding. NON-APPLICATION: a defect whose site is genuinely unique by construction (a `__main__`, a single entry point), where the population IS the instance."
  },
  {
    "id": "NFRA_OPLGTW-S59",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-20T11:30Z",
    "one_line": "R-OG-22's STREAMING BRANCH IS MUCH CHEAPER THAN 'RE-ARCHITECT THE EXPORTER', AND THE PRD DOES NOT REQUIRE THE MATERIALISATION: `write_csv` ALREADY consumes row-by-row (`export.py:206-210`), and `generate_csv:261-264` calls `export_query` -- getting the fully materialised list -- and only THEN writes it. The CSV writer is already streaming-capable; the PRODUCER hands it a list. And the contract's 250000 has a single-commit provenance: it was AUTHORED, never elicited from a consumer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ONE PATH, NOT TWO -- the wrong-object risk checked before claiming a divergence. `integration.py:915`'s docstring names \"OG-x-1's download routes\" as a second caller, which could have meant a separate file-based path whose properties differ from the one `S57` read. It does not: `export.py:257-264` `generate_csv` does `columns, rows, info = await service.export_query(principal, ticket)` at `:261` and `size = write_csv(path, columns, rows)` at `:264`. **The download route CALLS the in-memory path and then writes its result.** The file write happens AFTER the memory cost, not instead of it.",
        "⭐ THE WRITER IS ALREADY STREAMING-CAPABLE, which narrows the remedy enormously: `export.py:203-210` `write_csv` opens the file and does `writer.writerow(header)` then `for row in rows: writer.writerow(...)` -- it consumes an ITERABLE row by row and never indexes or len()s it. **So if `export_query` YIELDED rows instead of RETURNING a list, `write_csv` would need no change at all.** The third branch is not 'rewrite the exporter'; it is 'change what the producer hands the writer'.",
        "THE PRD DOES NOT MANDATE THE IN-MEMORY FORM, and this is the misreading worth killing early. `NFRA_OPLGTW_PRD.md:181`: \"Generate and validate a bounded CSV completely before starting its response; then reauthorize and stream without buffering it on the event loop... Delete local export files on success, failure, cancellation and startup cleanup.\" ⭐ THE RATIFIED TEXT IS ABOUT THE RESPONSE LAYER AND IS ALREADY SATISFIED -- generation completes before the response starts, and the response streams from a LOCAL FILE the PRD explicitly expects to exist. **'Completely before responding' constrains ORDER, not RESIDENCY.** Nothing in it requires the rows to be resident in the process while that happens.",
        "PROVENANCE OF THE 250000, which R-OG-22 question 2 reduces to and which neither seat had read: `git log --all -S'export_rows' -- org/standards/NFRA_OPLGTW_CONTRACT.json` returns EXACTLY ONE commit -- `2af252cb39 [1.0.0_SA_CTO~A] Register D9 NFRA_OPLGTW and author its Gateway PRD`. The value entered with the project's own authoring commit and has NEVER been modified since. The full file history (`--all --follow`) is four commits and the other three touch tool_operations and table naming.",
        "⚠ WHAT THE PROVENANCE READ DOES AND DOES NOT SETTLE: it shows the number was AUTHORED at PRD time by the CTO lane, in the same commit that registered the project -- NOT elicited from, negotiated with, or traced to any consumer, and no consumer record accompanies it. ⛔ IT DOES NOT PROVE NO CONSUMER NEEDS 250,000 ROWS. Absence of a consumer record is not absence of a consumer; a requirement could have been stated verbally or live outside the repo. The honest statement is that **the record supports 'authored' and contains nothing supporting 'elicited'**, and that R-OG-22's question is now a question for Andrew or a named consumer rather than for the archive."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "R-OG-22: the third branch is \"MAKE PEAK RSS STOP BEING A FUNCTION OF EXPORT SIZE\", costed as an unknown; and question 2 -- is 250,000 a CONSUMER REQUIREMENT or an aspiration -- reduced by msg 98482 to \"a PROVENANCE question with a measurable answer\".",
    "world_is": "The third branch is materially cheaper than it looked -- the consumer of the rows (`write_csv`) is already row-at-a-time, so the change is confined to what `export_query` hands it, and the PRD's ratified text constrains ORDER rather than RESIDENCY so it does not stand in the way. The provenance read returns a single authoring commit with no consumer record attached.",
    "notes": "INERT -- nothing armed, NO CELL CUT (round 1 open, LD-0521 stands), and ⛔ NO REWRITE PROPOSED: whether to change the producer's shape is an L4 call and the sizing belongs in a measurement cell (draft R2-h), not in a row. ⭐ THE CARRY: **BEFORE COSTING A REMEDY, READ THE CONSUMER OF THE THING YOU WOULD CHANGE -- IT MAY ALREADY ACCEPT THE CHEAPER SHAPE.** The expensive reading here ('re-architect the exporter to stream') and the cheap one ('yield instead of return') are indistinguishable from the producer's side alone; only `write_csv`'s `for row in rows` settles it, and that is one file away. ⚠ AND THE SIBLING TRAP: a docstring naming a second caller is a reason to CHECK for a second path, never evidence that one exists -- here both callers funnel through the same function, and believing otherwise would have produced a confident claim about a path that does not exist. COST: one read of the downstream consumer. NON-APPLICATION: a remedy whose consumer is the thing being replaced."
  },
  {
    "id": "NFRA_OPLGTW-S60",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-20T11:50Z",
    "one_line": "ARMED-ROW DEBT RESOLVED AGAINST BOTH CARRIERS BEFORE IT BECOMES L10's BLOCKER: 32 ARMED of 152 rows; 13 are named ONLY by a commit, so a channel-only scan would have UNDERSTATED closure by 13; the RESIDUAL with no carrier at all is THREE -- W3-S9, W3-S16, W3-S17 -- and ALL THREE NAME `2.0.0_SA_COO~O` AS disarm_owner, i.e. they are MINE and have sat since 2026-09-15. Two are DISARMED HERE on measured evidence; the third is deliberately NOT.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE CENSUS, both carriers, denominators printed: 152 rows in the channel, 32 `hazard_standing: ARMED`. Matched by EXACT id with a `(?![0-9])` guard so `-S1` cannot match inside `-S13`. CHANNEL arm (a LATER row naming the id): 16. COMMIT arm (`git log --all`, 45411 commits scanned): 29. BOTH: 16. ⭐ ONLY-A-COMMIT: **13** -- these are invisible to a channel-only scan, which is the shape `2.0.0_SA_COO~G` measured this morning on a different project (8 of its 73) and it reproduces here at a different ratio. RESIDUAL with neither carrier: **3**.",
        "⚠ THE BOUND, stated before the numbers are used: a MENTION IS PROXIMITY, NOT SEMANTICS -- a later row naming an id may discuss it rather than disarm it -- and the commit arm deliberately includes each row's OWN FILING COMMIT, which it cannot distinguish from a closing one by message alone (`S55`'s only commit hit IS `7d0241d11`, the commit that filed it). **So 29 'closed' is an UPPER BOUND and the RESIDUAL 3 is a LOWER BOUND on what is genuinely open.** Only the residual is used below.",
        "⛔ W3-S16 -- DISARMED ON MEASURED EVIDENCE, prediction DID NOT MATERIALISE. It predicted `tests/test_principal_cutover.py::test_oga2_ac04` would turn RED because the hand-written ROUTE_CLASS table lacked `/schwab/download/login` and `/schwab/download/callback`. RUN AT HEAD: **PASS**, and the test's own output says why -- \"route declarations in app/server.py 31 (Route 30, Mount 1) == app.routes 31; protected 19 ..., public 12\". The table now covers the two paths. The hazard was REAL when filed and a later cell accommodated it.",
        "⛔ W3-S17 -- DISARMED ON MEASURED EVIDENCE, prediction DID NOT MATERIALISE. It predicted `tests/test_browser_oidc.py::test_oga3_ac07` would turn RED \"as soon as any later cell adds or changes a route\", naming OG-x-1 and OG-z-1 as writers of `app/server.py` -- and BOTH are now `complete`, so the trigger condition OCCURRED. RUN AT HEAD: **PASS** -- \"base routes 27 (git object 7459929520: 27 declared, equal to the recorded table); served now 31; base routes still served unchanged 27 of 27, in base order, each path once; browser routes served 2 of 2\". ⭐ AC7 pins the BASE and TOLERATES ADDITIONS, which is precisely the property W3-S17 feared it lacked.",
        "INSTRUMENT PROVENANCE, because a green from the wrong interpreter is worse than no green: the repo-root `.venv-og` does NOT exist (it is gitignored and lives per-worktree) and the bare interpreter FAILED COLLECTION on both modules with `ModuleNotFoundError: No module named 'moto'`. ⛔ **A COLLECTION ERROR IS NOT A RED AND I DID NOT RECORD ONE** -- both were NOT_EVALUATED until a provisioned interpreter was found at `C:/tmp/wk-oplgtw-2r2/.venv-og`. The PASSes above were produced by that interpreter run with cwd in the MAIN checkout, so the CODE under test is HEAD's and only the interpreter came from the worktree.",
        "⛔ W3-S9 IS **NOT** DISARMED, AND THE REFUSAL IS THE POINT. It is not test-falsifiable: it asserts that authorization decisions AFTER the principal guard still key on the EMAIL the principal carries for display (tier, the per-identity tool allowlist, the integration min-tier gate, the `/query/v0` catalog principal), so a second principal holding a re-assigned email inherits the first holder's tier and tool scope. What I measured is NOT sufficient to close it and IS sufficient to keep it armed: `app/identity.py` returns an EMAIL as the identity on all three ingress paths (`:65` ALB OIDC, `:122` Verified Access, `:133` Tailscale), while `app/data_entitlement.py:5-10`'s docstring claims identity is \"validated Entra tenant and object id and never by email ... email (display only)\". ⚠ A DOCSTRING IS A CLAIM, NOT A MECHANISM -- the two readings are not yet reconciled, and closing a SECURITY row on the more comfortable one would be the defect."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "L10 requires every row dispositioned before the slug; W3-S9/W3-S16/W3-S17 stood ARMED with `disarm_owner: 2.0.0_SA_COO~O` and no closing carrier since 2026-09-15.",
    "world_is": "Two of the three are closed on measured evidence and one is explicitly held open. The armed debt this lane owes at round 1's L10 is now ONE row (W3-S9), not three, and it is named rather than discovered at the slug.",
    "notes": "INERT. ⛔ THIS ROW DISARMS; IT DOES NOT DISPOSE OR ADJUDICATE -- it is EVIDENCE for W3-S16 and W3-S17, and the adjudication remains the CVO's at L9. No `adjudicates` field is claimed on this lane's own rows. W3-S9's sharpened disarm condition, so a successor need not re-derive it: reconcile `identity.py`'s email-returning ingress against `data_entitlement.py`'s never-by-email claim, and show which key the FOUR named consumers actually read. ⭐ THE CARRY: **AN ARMED ROW IS A PREDICTION WITH AN EXPIRY, AND NOBODY RE-READS IT AFTER ITS TRIGGER FIRES.** W3-S17 named its own trigger -- 'as soon as any later cell adds or changes a route' -- and both named cells completed days ago, so the row was decidable long before anyone looked; it stayed armed because filing is prompted by an event and RE-READING is prompted by nothing. COST: one both-carriers census over the armed set, once per round, before the slug rather than at it. NON-APPLICATION: an armed row whose trigger is an external event that has not occurred -- there the prediction is still pending, not merely unread."
  },
  {
    "id": "NFRA_OPLGTW-S61",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-20T12:05Z",
    "one_line": "W3-S9 CONFIRMED AT HEAD AND WIDER THAN FILED, SO IT STAYS ARMED: `resolve_tier(email, cfg)` keys MASTER_ADMIN off an EXACT EMAIL MATCH and is wired at FOUR production call sites, including one W3-S9 never named (`token_broker.py:143`, which mints TOKEN SCOPES off that tier). ⛔ AND THE MODULE'S ENTIRE ROOT-OF-TRUST DEFENCE IS AGAINST A FORGED EMAIL AND IS SILENT ON A RE-ASSIGNED ONE -- a re-assigned address is signature-verified and GENUINE, so it passes every gate in the file.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE TWO CARRIERS THAT DISAGREE, and neither is the mechanism: `app/context.py:41-47` declares `Principal.email` is \"display / audit metadata only -- never an authorization key\" and `principal_key()` is \"'<tid>/<oid>' ... Never derived from an email\". `app/config.py:233-235`, marked SECURITY-CRITICAL, says the opposite about the thing that decides privilege: \"resolve_tier (app/tier.py) keys the user-type off these EXACT-match sets against the signature-verified email\". Both are in the tree at HEAD.",
        "THE CODE SETTLES IT, and it agrees with config.py: `app/tier.py:69` `def resolve_tier(email: str, cfg) -> Tier` -- the SIGNATURE takes an email, not a principal -- and `:80` `if _exact_in(email, getattr(cfg, \"MASTER_ADMIN_EMAILS\", ())): return Tier.MASTER_ADMIN`. `config.py:241-243` defaults that list to `andrew@opalinvest.com`. So the highest privilege tier is reached by EXACT STRING EQUALITY ON AN EMAIL.",
        "⛔ IT IS WIRED ON THE LIVE PATH, WHICH THE MODULE'S OWN HEADER DENIES. `tier.py`'s docstring says \"NOT yet wired into `_run()` (that wiring is the live-path landing, still gated)\". Census of callers over the whole gateway: FOUR PRODUCTION SITES -- `guard.py:75` (`tier = resolve_tier(email, cfg)`), `integrations/base.py:128` (the `spec.min_tier` gate), `token_broker.py:143`, and `tools.py:124` (\"resolve ONCE: feeds the guard + every audit\"). ⚠ **THE HEADER IS STALE AND A READER TRUSTING IT WOULD CONCLUDE THE WHOLE MODULE IS INERT.** Third instance today of a file's own prose contradicting its code.",
        "⭐ A CONSUMER W3-S9 DID NOT NAME, AND IT IS THE MOST CONSEQUENTIAL: `token_broker.py:143` `return resolve_tier(email, _cfg)`, feeding `_scopes_for_tier(...)` -- so the email-derived tier determines the SCOPES MINTED INTO A TOKEN, not merely an in-process allow/deny. W3-S9 named four consumers (tier, the per-identity tool allowlist, the integration min-tier gate, the `/query/v0` catalog principal); this is a fifth, and a token outlives the request that minted it.",
        "⛔⭐ THE DEFENCE DOES NOT COVER THE HAZARD, AND THIS IS THE WHOLE FINDING. `tier.py`'s ROOT-OF-TRUST AXIOM is about FORGERY: \"a tier is only as trustworthy as the identity provider's SIGNATURE verification\", \"an unverified provider means the email (=tier key) is FORGEABLE\", \"_provider_is_verified() prevents it structurally\", and `validate_identity_provider_for_prod()` refuses spoofable providers at boot. **Every one of those controls answers 'can a caller FORGE this email'. W3-S9's hazard is 'has this email been RE-ASSIGNED to a different person' -- and a re-assigned address is signature-verified and genuinely the new holder's, so it satisfies every control in the file and resolves MASTER_ADMIN.** The file's own parenthetical names the key: \"the email (=tier key)\".",
        "⚠ WHAT THIS IS NOT: not an incident, and not a claim that anything has happened. No email re-assignment is known, none is alleged, and I have measured NONE. Re-assignment is an administrative act in the tenant, so the exposure is bounded by who can perform one -- which is precisely the `authorized identity/data administrator` role that R-OG-26 measured the PRD to NAME BUT NEVER ASSIGN. ⭐ So this row and `G-C`'s blocker are the SAME underlying gap seen from two ends: nobody is assigned to govern identity re-assignment, and identity re-assignment is what silently moves privilege."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "W3-S9 (2026-09-15, `0.9.0_WK_NFRA_OPLGTW~3`): after the principal guard, authorization still keys on the display email, so a second principal holding the same email inherits the first's tier and tool scope. Its stated disarm: \"until the grant and tier layer keys on the principal (C2, OG-z-1, which depends on this cell)\".",
    "world_is": "CONFIRMED at HEAD and WIDER: the tier layer still keys on email, at four wired production sites, one of them minting token scopes. OG-z-1 is `complete`, so the row's own disarm condition has NOT been met by that cell's completion -- which is why it must not be closed on the dependency's status. The protective machinery that exists is real and defends a DIFFERENT threat (forgery) than the one the row names (re-assignment).",
    "notes": "ARMED, `disarm_owner` `2.0.0_SA_COO~O`, and it is deliberately NOT disarmed -- this row exists to state precisely why W3-S9 survives, so a successor does not close it on the comfortable reading. ⛔ NO REMEDY IS PROPOSED AND NONE IS CUT: re-keying authorization from email to `principal_key` is a SECURITY-CLASS design change owned at L4, not an issuer's to choose, and round 1 is open (LD-0521). The `tier.py` stale header is a separate, smaller item for whoever owns that file. ⭐ THE CARRY: **A CONTROL CAN BE REAL, WELL-BUILT, WELL-DOCUMENTED AND AIMED AT A DIFFERENT THREAT THAN THE ONE YOU ARE ASKING ABOUT -- AND ITS QUALITY IS WHAT MAKES THE SUBSTITUTION INVISIBLE.** Reading `tier.py` end to end leaves a strong impression of a hardened path, because it IS one: fail-closed ordering, exact-match-only, a boot gate, a belt-and-suspenders comment. Every word of it is about FORGERY. Ask of any control not 'is it good' but 'WHICH threat does it answer', and compare that to the threat in the row. COST: one read of the control's own threat statement, which it usually volunteers. NON-APPLICATION: a control whose threat statement already names your hazard."
  },
  {
    "id": "NFRA_OPLGTW-S62",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~O",
    "surfaced_at": "2026-09-20T18:00Z",
    "one_line": "THE ORDER COUNT AND THE OUTCOME COUNT POINT IN OPPOSITE DIRECTIONS, AND THIS LANE HAS BEEN REPORTING ONLY THE FIRST. Orders read 31 of 33 TERMINAL (30 complete + 1 superseded). OUTCOMES read ZERO OF EIGHT GRADED -- there is no adjudications/ and no remediations/ directory under this project at all. All 8 FWDs are `DONE WHEN: EXERCISED` and the PRD's S10 row maps the walkthrough harness to `FWD-1 through FWD-8`, so THE TWO OPEN ORDERS ARE THE ONLY PATH TO ANY OUTCOME. The remaining 2 of 33 is not a 6% remainder; it is 100% of the proving.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE ORDER COUNT, exact, re-derived at the status lines rather than carried: 33 order files -- 30 `complete`, 1 `superseded` (OG-r-2), 2 `pending` (OG-v-4, OG-v-5). TERMINAL = 31, NON-TERMINAL = 2. ⚠ This lane reported \"31 of 33\" for many ticks, which is correct ONLY under the TERMINAL reading and reads as 31 COMPLETE. Worse, `drive_log_20260920T1220Z_O.md` @`a4c9106723` wrote the limb row as `31/33 terminal + 1 superseded`, which DOUBLE-COUNTS the superseded order and implies 32 terminal against 1 pending. The figure was never re-derived because it never changed.",
        "ZERO OUTCOMES GRADED, and the instrument is an absence with a positive control: `ls` of `org/missions/D9/NFRA/NFRA_OPLGTW/` returns exactly `decompositions`, `deliverables`, `prd`, `project.json`, `surprise-channel`, `task-orders`. There is NO `surprise-channel/remediations/` and NO `surprise-channel/adjudications/` -- the directories the spine puts L9 adjudications and L10 stamps in. The positive control is the sibling channel dir that DOES exist (`investigations`, 154 rows), so the read is not a path error. No L9 has ever run on this project and no FWD carries a grade.",
        "ALL EIGHT OUTCOMES ARE EXERCISE-CLASS, read at the bytes (`prd/NFRA_OPLGTW_PRD.md:43-125`): every one of FWD-1..FWD-8 states `DONE WHEN: EXERCISED`, and every PROOF line names a HUMAN act -- \"an observed owner-and-member walkthrough\", \"deliberately chosen examples with independently known answers\", \"controlled allowed and denied examples\", \"an opened filtered download, a copied-link attempt by another account\", \"read the actual answers\", \"deliberate grant-change and revocation runs\", \"repeat representative existing user journeys\", \"an operator follows the onboarding, troubleshooting, audit-read, and rollback instructions\". NONE is satisfiable by a build, a test suite or a code read.",
        "⭐ AND THE PRD ITSELF MAKES THE COUPLING EXPLICIT, which is why this is a structural fact and not an inference: the systems table row `:210` reads `| S10 | Acceptance and onboarding harness/runbooks; synthetic fixtures, MCP Inspector and owner/member walkthrough | A1-A20 ... -> deliberate endpoint proof and safe pilot report | S1-S9 | FWD-1 through FWD-8; all six evidence axes |`. S10 is the ONLY row in that table carrying the whole outcome set, and S10 is precisely what OG-v-4 and OG-v-5 grade.",
        "WHAT THE OTHER 30 ORDERS BOUGHT, stated so this row is not read as dismissing them: S1-S9 built and deployed the machine -- the principal cutover, the policy guard, durable state, the producer contract, the catalog, the query engine, the CSV path, audit, and the AWS plane. They are the PRECONDITION for the walkthrough and none of them is wasted. They simply do not, and were never designed to, EXERCISE anything.",
        "THE GATES, so the remaining path is legible: OG-v-4 phase 2 needs G-C (a controlled identity's verified tid/oid plus an approved grant) and G-D (the walkthrough record); OG-v-5 needs G-E (Menachem's grant plus its activation) and G-F (the pilot record) and depends on OG-v-4. `git ls-tree HEAD .../deliverables/` returns SIX entries, all worker slots, so all four gate artifacts are absent. R-OG-26 measured G-C's blocker as a ROLE the PRD names and never assigns."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This lane's own standing report, every tick since the walkthrough orders opened: \"round 1 at 31 of 33, blocked on two orders\" -- a framing in which the project is nearly finished and two items remain.",
    "world_is": "Both halves of that are true and together they mislead. The BUILD is 31 of 33 terminal. The PROOF is 0 of 8 outcomes, with no grading machinery ever invoked, and the two open orders are the sole route to all eight. A reader given only the order count would conclude the project is ~94% closable; the outcome count says the closing work has not begun.",
    "notes": "INERT -- nothing armed; no cell cut (round 1 open, LD-0521); no remedy proposed, because the remedy is the two orders already cut and the human acts they wait on. The drive log's double-counted limb row is corrected IN PLACE BY APPENDED CORRECTION quoting the wrong text, never by silent replacement. ⭐ THE CARRY: **A PROGRESS METRIC AND A COMPLETION METRIC CAN BOTH BE HONEST AND POINT OPPOSITE WAYS, AND THE ONE THAT IS CHEAP TO COMPUTE IS THE ONE THAT GETS REPORTED.** Orders have a status field and count themselves; outcomes require reading the endpoint text and asking which artifact would grade them, so a loop that reports every tick drifts toward the countable half. ⚠ THE TELL IS A RATIO THAT NEVER MOVES WHILE THE WORK IS BLOCKED: 31 of 33 was as true the night the last build order closed as it is now, because the remaining orders cannot close without a person. COST: one read of the endpoint's DONE WHEN lines against the open order set, once per round, not once per tick. NON-APPLICATION: a project whose outcomes are graded by the same artifacts the orders produce -- there the two metrics genuinely track."
  },
  {
    "id": "NFRA_OPLGTW-Z-W7-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_OPLGTW~7",
    "surfaced_at": "2026-09-27T21:30Z",
    "one_line": "BUILT THE OPPOSITE OF THE RULED 'WITH NEITHER, IT REFUSES' FOR A RESTRICTED ACTIVATE WITH NO EMAIL, BECAUSE THE LITERAL REFUSAL BREAKS AN OUT-OF-LANE REGRESSION TEST THAT AC2 ITSELF MEASURES. A restricted activate with no candidate email and no stored-profile email now silently adds NO deny record, instead of raising CandidateRejected.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "THE TASK ORDER (section 1 step 4, following CTO ruling R2-k #3): \"A restricted `activate` puts one deny record per supplied email ... Emails come from the candidate (repeatable) or else the stored profile. With neither, it refuses.\" I built this literally first: prepare() raised CandidateRejected when _candidate_deny_emails(raw_candidate) was empty AND the stored profile carried no email.",
        "THAT BUILD FAILED `ek.AC2.sh` (this task order's own named criterion, `tests/test_owner_gate.py tests/test_portal_grant.py tests/test_sprint_view.py tests/test_asker_scope.py`, expect >=24 passed none failed): `tests/test_portal_grant.py::test_admin_accepts_portal_only_candidate` (outside this cell's <paths>, so not editable) calls `sea.prepare(schwab_store, {\"tid\": _TID, \"oid\": _OID, \"scope\": _schwab_scope()}, contract, out=io.StringIO())` -- a candidate with NO `email` key at all, against a FRESH `_FakeStore()` with no stored profile either -- and asserts the subsequent `sea.activate(...)` succeeds and writes the Schwab-only scope shape. Ran at HEAD+my-first-build: `ops.schwab_entitlement_admin.CandidateRejected: activate needs an email to deny ...` raised at that exact call, one failure, `1 failed, 23 passed`.",
        "A SECOND collision on the SAME test, found first: giving `activate()`'s return dict a new `deny_emails` key (to expose which aliases were denied) broke `test_admin_accepts_portal_only_candidate`'s exact-equality assertion `assert result == {\"profile_revision\": 1, \"grant_revision\": 1, \"diff\": plan.diff}` for its portal-only candidate (which DOES carry an email, so a deny record IS added there). Fixed by leaving the return-dict shape unchanged -- the deny record is written and independently readable via `acs.email_deny_key(email)`, so no caller needs a new key to know it happened.",
        "THE BUILT SHAPE, at HEAD of this commit: `ops/schwab_entitlement_admin.py prepare()` computes `deny_emails` from the candidate (repeatable `emails`, or singular `email`) or else a fresh raw read of the stored profile's `email` field; when BOTH are empty, `Plan.deny_emails` is simply `()` and `activate()` adds no email_deny put -- no exception, no refusal. All of AC1 (10/10), AC2 (24/24) and AC3 pass at this shape (this task order's proof_of_spec instance is the citable run)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's ruled writer behavior: a restricted activate with no email available to deny (candidate nor stored profile) REFUSES (CandidateRejected).",
    "world_is": "Implemented instead: it silently adds no deny record and proceeds, because the literal refusal breaks tests/test_portal_grant.py::test_admin_accepts_portal_only_candidate's email-less Schwab-only candidate, a fixture outside this cell's <paths> and inside AC2's own measured regression set.",
    "notes": "ARMED and deliberately left so: a future cell should reconcile which is the intended rule -- (a) accept the silent-skip as the real design (an email-less activate is a pre-existing, narrower case this cell was never meant to close), (b) get test_portal_grant.py's fixture given an email under its own lane so the literal refusal can land, or (c) a fresh CTO call. No remedy is cut here -- test_portal_grant.py is outside <paths> and the ruling is not this worker's to reinterpret. ⭐ THE CARRY: a design bullet's imperative wording ('it refuses') can be materially stricter than every one of that same task order's own MEASURED acceptance criteria requires -- none of the 10 named AC1 tests exercises the no-email refusal branch at all, so the conflict was invisible until the OUT-OF-LANE regression suite (also named by the task order) was actually run."
  }
]
```
