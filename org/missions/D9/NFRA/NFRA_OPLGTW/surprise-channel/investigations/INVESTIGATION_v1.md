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
  }
]
```
