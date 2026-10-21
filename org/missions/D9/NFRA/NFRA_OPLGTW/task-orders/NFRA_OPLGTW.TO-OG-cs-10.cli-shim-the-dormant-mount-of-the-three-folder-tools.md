# NFRA_OPLGTW task order -- `OG-cs-10` -- the dormant mount: the three folder tools as an integration, registered and classified, switched off until a release enables it (cli-shim workstream, wave 4; PRD v3.19 FWD-23)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP_CLISHIM.round48.md</decomp_doc>
<owned_cells>OG-cs-10</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cs-10</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~187</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the integration names the role and the secret the reader IAM text (`OG-cs-6`) creates, and builds no client at import or construction.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is PRD v3.19 FWD-23 (ADMITTED), applied as code that is DORMANT: the integration id `folders` is in no `ENABLED_INTEGRATIONS` list, so merging it adds ZERO tools to the live surface. Enabling it is the release order (`OG-cs-9`), never-widen gated.
EGRESS CLASS, declared: NONE (nothing is called until enabled; the S3 client is built on first use).
</preflight>

## 1. THE CELL -- `OG-cs-10` (decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md`, workstream CLISHIM-D, wave 4)

WHY. `app/folder_tools.py` (drained from `OG-cs-2`: `list_folder`, `describe_object`, `async query_object`) takes every dependency as an argument. This cell mounts it as a gateway INTEGRATION named `folders` in the way the gateway's existing integrations are mounted, DORMANT: the registry knows the id, `ENABLED_INTEGRATIONS` does not list it, so no tool appears on the live MCP surface until a release enables it. All paths below are under `infra/aws/ec2/opal-gateway/`. READ first, and copy the shapes of: `app/integrations/schwab/integration.py` (`SPEC`, `_admit`, `_call`, `class SchwabIntegration(Integration)` with `register(mcp)`; lines 60-135 and 1172-1247), `app/integrations/schwab/envelope.py` (how a dict becomes a `CallToolResult`, `error_result`), `app/integrations/schwab/aws_roles.py` (the assumed-role session and `RoleConfig`; reuse its refreshing session, do not write a second one), `app/integrations/registry.py` (`register_factory` and the dormant lines), `app/integrations/base.py` (`run_integration_tool`, which audits every outcome, applies the identity-scope floor and the person record's narrowing, and `validate_integration_spec`), `app/data_entitlement.py` lines 95-230 (the tool classification sets), `app/folder_tools.py` and `app/folder_grant.py`.

THE FILES (exact names):

1. NEW `app/integrations/folders/__init__.py` (empty or one docstring) and NEW `app/integrations/folders/integration.py` with: `INTEGRATION_ID = "folders"`; `TOOL_NAMES = ("folder_list", "folder_describe", "folder_query")`; `SPEC = IntegrationSpec(id="folders", display_name=..., description=..., auth_kind=AuthKind.ASSUMED_ROLE, tool_prefix="folder_", read_only=True, min_tier="read_only", hosts=<the three bucket S3 hosts and sts.amazonaws.com>, tool_classifications=<a SAFE row for each tool, the shape the Schwab spec uses>)`; `class FoldersIntegration(Integration)` with `spec = SPEC`, `__init__(self, deps_factory=None)` (the factory is stored and NEVER called at construction), `deps(self)` (calls the factory once, on first use, and caches the object), `async dispatch(self, principal, rec, is_master_admin, is_opal, tool, args) -> dict`, `register(self, mcp) -> list[str]`, and the admitted call path `_call` below.
2. `dispatch`: `tool` not in `TOOL_NAMES` answers `{"error": ..., "code": "unknown_tool"}`; a missing, non-str or empty `path`, and for `folder_query` a `request` that is not a dict, answer `{"error": ..., "code": "INVALID_REQUEST"}` BEFORE any dependency is built and before any S3 call; then `deps()` (an exception answers `{"error": ..., "code": "UNAVAILABLE"}`, never raises); then `folder_list(path, start_after="")` -> `folder_tools.list_folder(principal, rec, is_master_admin, is_opal, deps.s3, path, start_after)`, `folder_describe(path)` -> `describe_object(...)`, `folder_query(path, request, cursor="")` -> `await query_object(principal, rec, is_master_admin, is_opal, deps.s3, deps.engine, deps.codec, path, request, cursor)`. `list_folder` and `describe_object` are synchronous S3 work: run them with `asyncio.to_thread`. `deps` is any object with attributes `s3`, `engine`, `codec`. No function raises.
3. The DEFAULT deps factory (used when `deps_factory` is None; built on the first call, never at import): `s3` is a boto3 S3 client from an assumed-role session for role `gateway-folder-read-role` (account id from `sts.get_caller_identity()`; the ExternalId from the Secrets Manager secret `opal/mcp/opal-gateway-folder-reader-external-id`, JSON field `external_id`); reuse `aws_roles`' refreshing session (credentials renew before expiry). `engine = ExecutionEngine()`, `codec = CursorCodec()` (a per-process random key: a cursor does not outlive a gateway restart; that is disclosed, not hidden).
4. `_call(self, tool, **kwargs)`: copy the Schwab `_call`: the admission chokepoint FIRST (`run_integration_tool` as `_admit` does, which audits, applies the floor and the person record's `tools_deny`/`channels_deny`), then the principal from `get_current_principal()`, `rec = data_entitlement.person_access(principal)` (any exception answers an `UNAVAILABLE` error result: fail closed), `is_master_admin = data_entitlement._tier_of(principal) is Tier.MASTER_ADMIN`, `is_opal` by the same `_is_opal_user(email)` test `app/integrations/base.py` uses, then `dispatch`; turn the dict into a `CallToolResult` with the Schwab envelope helper (an answer carrying `"code"` and `"error"` is an error result, anything else a success).
5. `register(self, mcp)`: three async functions `folder_list(path: str, start_after: str = "")`, `folder_describe(path: str)`, `folder_query(path: str, request: dict, cursor: str = "")`, each with a docstring that tells a caller what it does (list a served bucket or folder, one level, `bronze` and `raw` folders never shown; describe one parquet object's columns, five sensitive column classes dropped by name; run one bounded read-only query over a table folder, a page of at most 500 rows with a `next_cursor`), registered with `mcp.tool(name=fn.__name__)(fn)`; returns `list(TOOL_NAMES)`.
6. `app/integrations/registry.py`: ONE new dormant block after the `blackdiamond` line, in the style of its neighbours: a comment that says it is DORMANT (`folders` is in no default `ENABLED_INTEGRATIONS`, so the line adds zero tools until a release enables it), `from .folders.integration import FoldersIntegration` and `register_factory("folders", FoldersIntegration)`. Nothing else in that file changes.
7. `app/data_entitlement.py`: a new set `FOLDER_TOOLS = frozenset({"folder_list", "folder_describe", "folder_query"})` placed with the other tool-name sets, with a comment (read class, legacy, Opal principals only; NOT in `DATA_GRANT_TOOLS` and NOT in `TIER_ADMITTED_TOOLS`: the folder strings in the person's record are the gate, applied by `folder_tools`, not the tool name), and `FOLDER_TOOLS` added to the union that builds `TOOL_CLASSES` as `CLASS_LEGACY`. Nothing else in that file changes.

## 2. TESTS

NEW `tests/test_cs10_folders_mount.py`, at least EIGHT tests, offline, `os.environ.setdefault("MOCK_GRAPH", "1")` before any app import: the spec fields and SAFE rows; `register` against a fake `mcp` registers exactly the three names in order and returns them; `dispatch` for each tool equals the `folder_tools` function's answer on a fake S3 (admin and granted person); a refused path makes zero S3 calls through every tool; bad inputs (non-str path, missing path, non-dict request, unknown tool) answer a dict with a code, zero S3 calls, no raise; the factory is not called at construction and a raising factory answers `UNAVAILABLE`; `registry.available_ids()` holds `folders` and `register_enabled(fake_mcp, [])` registers nothing while `register_enabled(fake_mcp, ["folders"])` reports exactly the three tools with no `error`, `violations`, `unclassified` or `composed_path_refused` key; `FOLDER_TOOLS` is classified legacy and is in neither `DATA_GRANT_TOOLS` nor `TIER_ADMITTED_TOOLS`. If an existing pin test fails ONLY because the registry now holds a dormant id or the classified set grew (`tests/test_entitlement_admin.py`, `tests/test_tool_classification_composition.py`), change that ONE pin line to include the new names by name, with a comment citing this order, and say which line in your report; touch no other test.

## 3. BOUNDS

- Write only the files named in section 4 and, if a row is needed, the channel. No other product file, no route, no `deploy-to-ec2.sh` (the enablement is the release's), no `ENABLED_INTEGRATIONS` edit, no AWS call, no deploy.
- Counts and hashes only: no e-mail address, account number, ExternalId or token in any file (test data uses `example.invalid` addresses and made-up values).
- Never: push, `git stash`, rebase, `checkout --` or `clean`.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 4. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/integrations/folders/__init__.py
infra/aws/ec2/opal-gateway/app/integrations/folders/integration.py
infra/aws/ec2/opal-gateway/app/integrations/registry.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/tests/test_cs10_folders_mount.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
infra/aws/ec2/opal-gateway/tests/test_tool_classification_composition.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~187/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W187-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 5. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cs-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs10.AC1.sh; echo "exit=$?"</invocation><expect>(?s)the spec: id folders, prefix folder_, read_only True, auth ASSUMED_ROLE, min_tier read_only, SAFE rows True: ok.*register\(\) registers exactly the three tools in order and returns them .*: ok.*dispatch answers what folder_tools answers for an admin: .*: ok.*dispatch answers what folder_tools answers for a granted person: .*: ok.*dispatch query runs on the real engine from deps .*: ok.*a refused path makes ZERO S3 calls through every tool \(0\): ok.*bad inputs answer a dict with a code, zero S3 calls, no raise .*: ok.*construction never calls the factory and a raising factory answers UNAVAILABLE .*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cs-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs10.AC2.sh; echo "exit=$?"</invocation><expect>(?s)the registry holds folders and its spec validates \(violations \[\]\): ok.*FOLDER_TOOLS is exactly the three names, each classified .*: ok.*register_enabled with no ids registers nothing and folders is not enabled by default .*: ok.*enabling folders reports exactly the three tools and nothing refused .*: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-cs-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/clishim/checks/cs_foot.sh org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cs-10.cli-shim-the-dormant-mount-of-the-three-folder-tools.md app/integrations/folders/__init__.py,app/integrations/folders/integration.py,app/integrations/registry.py,app/data_entitlement.py,tests/test_cs10_folders_mount.py,tests/test_entitlement_admin.py?,tests/test_tool_classification_composition.py? tests/test_cs10_folders_mount.py 8 tests/test_entitlement_admin.py tests/test_tool_classification_composition.py tests/test_og_ad1.py tests/test_data_entitlement_guard.py tests/test_blackdiamond.py tests/test_portal_index.py tests/test_cs2_folder_tools.py; echo "exit=$?"</invocation><expect>(?s)files that differ from HEAD under the gateway folder: .*: ok.*tests/test_cs10_folders_mount\.py: (?:[89]|[1-9]\d+) test functions.*: ok.*new file tests/test_cs10_folders_mount\.py: (?:[89]|[1-9]\d+) passed, 0 failed.*neighbours \(7\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1` (the integration, with the real engine) and `AC2` (the registry and the classification, the dormant switch) are graded by issuer-written probes independent of your tests. `AC3`: the footprint is the named files (the two pin tests optional), your tests pass and the seven neighbours pass.

## 6. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cs-10.cli-shim-the-dormant-mount-of-the-three-folder-tools.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order org/missions/D9/NFRA/NFRA_OPLGTW/task-orders/NFRA_OPLGTW.TO-OG-cs-10.cli-shim-the-dormant-mount-of-the-three-folder-tools.md` (`python3`, not `python`: ruling msg 35901). Report once; the `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Workstream CLISHIM-D, wave 4, decomposition `NFRA_OPLGTW_DECOMP_CLISHIM.round48.md` (amendment A1). Source: PRD v3.19 FWD-23; the mounting pattern is the gateway's own (`schwab`, `blackdiamond`). Staged: spawn after OG-cs-2 and OG-cs-6 are drained (this cell imports `app/folder_tools.py`).
- Widening, plainly: none by this order (dormant: zero tools until `ENABLED_INTEGRATIONS` lists `folders`). The release order enables it, applies the reader IAM text and carries the never-widen halves.
- DISCLOSED READINGS: (1) the classification is legacy and Opal-principals-only; a person reads a folder only where their record's `channels_allow` covers it (`folder_decision`), so a profiled non-master person with no folder string reads nothing; (2) `tools_allow` in a person's record widens the identity-scope floor for these tools exactly as for any served tool (`person_widens`), and `tools_deny` narrows; (3) a cursor does not survive a gateway restart; (4) the per-firm client grant (`OG-cs-7`) is NOT mounted here: mounting it on the `client_*` tools narrows today's access and waits on the CTO's ruling on the namespace string.
- Pre-cut: `AC1` and `AC2` base FAIL as expected (`app.integrations.folders` absent). Armed on a SCRATCH copy of the gateway app (shared tree untouched; `folder_tools` stood in by a scratch reference): `AC1` reads OK on all eight arms and `AC2` OK on all four.

<status>pending</status>
<round>48</round>
<workstream>CLISHIM-D</workstream>
<slot>~187</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
