# NFRA_MCPORTAL task order -- `MP-pe-1` -- WORKSTREAM PE ROUND 1: the gateway breakdown groups each tool by its source, with no Microsoft 365 default

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pe-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pe-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~31</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request handler; read when opened (PRD C8).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the handler reads files already shipped in the gateway artifact.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (no declaration, a malformed one, a two-bucket tool, a tool with an integration spec that is also declared).
EGRESS CLASS, declared: none. Every read in a test is a planted file or a fake.
</preflight>

## 1. THE CELL -- `MP-pe-1` (workstream PE round 1, decomposition sections PE.0 to PE.2)

Your worktree is `C:/tmp/mp-pe-31` (branch `wk-NFRA_MCPORTAL-pe-31`). Work and commit only there.

**The defect.** Andrew reads the gateway's tools on a page, `GET /api/admin/gateway/breakdown`, built in `infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py`
(read the whole file first, and `tests/test_admin_gateway_breakdown.py`). In `_compute`, the loop that puts each tool into a channel sends every tool with no
integration spec into a channel named "Microsoft 365" (the `else` branch, and the forced `M365_ID` channel). That files the 13 harvest tools, the etfs tools,
and the news and portal tools under Microsoft 365, which is false: only tools that call Microsoft Graph belong there. A human reading the page is told something
wrong. Fix the grouping so the page tells the truth, and make it ready for a per-tool source declaration that another project is adding to the catalog.

THE RULE, per tool, the FIRST that holds (`registry._ACTIVE_BY_TOOL`, the catalog file `app/refs/DATA_CATALOG.yaml`, and `graph_scope_map.TOOL_GRAPH_SCOPES`
already exist; read how `_compute` and `_catalog_read_tool_rows` use them):
1. The tool has an integration spec: its integration channel, exactly as today (kind `integration`). A declaration NEVER moves such a tool.
2. Else the tool's row in the catalog's top-level `tool_index:` list (the row whose `tool:` equals the tool name) carries `source_group`: an object
   `{id, name, kind}` or a list of such objects, where `kind` equals the string `bucket` and `id` and `name` are non-empty strings. The tool joins ONE group per
   element: group `id` = the element's `id` (the bucket name, for example `opal-data-harvest`), group `name` = its `name`, `kind` = `bucket`, `auth` = `per tool`,
   `min_tier` = `per tool`. A tool with several elements is listed in each of those groups.
3. Else the tool is a key of `graph_scope_map.TOOL_GRAPH_SCOPES`: the existing Microsoft 365 group (`id` `m365`, `kind` `native`, `auth` `delegated`, `min_tier`
   `per tool`), and ONLY such tools.
4. Else the tool joins the group `{id: "undeclared", name: "No source declared", kind: "undeclared", auth: "per tool", min_tier: "per tool"}`. This group exists
   only when at least one tool lands in it. A tool is NEVER placed in Microsoft 365 by default.
5. A `source_group` that is not an object or a list of objects each having a non-empty string `id` and `name` and `kind` equal to `bucket` is treated as NOT
   declared: rule 3 or 4 then applies. One bad element makes the whole declaration not declared (never a partial read).

Build:
1. A small helper, for example `_declared_source_groups()`, that reads the catalog once per `_compute` and returns `tool -> list of {id, name}` for the validly
   declared tools, in the style of `_catalog_read_tool_rows` (same file handle path and encoding). Reuse the YAML path constant the file already has.
2. Replace the grouping branch in `_compute` with the rule above. Keep the forced Microsoft 365 channel (`chans.setdefault(M365_ID, ...)`) as it is.
3. The response gains a top-level string `grouping_basis`: one sentence naming the four rules in this order (integration, declared bucket, Graph scope,
   otherwise undeclared) and ending exactly `N tool(s) declare no source.` where N is the number of DISTINCT tools that landed in the undeclared group (N may be 0).
4. `channels[].kind` now takes `integration`, `native`, `bucket`, `undeclared`. Output order of `channels`: all `bucket` groups sorted by `id`; then
   `integration` groups sorted by `id`; then `native` (`m365`); then `undeclared`. (Today it is `m365` first, then sorted ids: change the final loop.)
5. Everything else about a channel keeps its meaning: `tools[]` (sorted by name), `indexes`, `holders` and `holders_basis` computed by the existing chain from
   each group's own tool list (a tool in two groups appears in both groups' holder rows), `rating` read by group id (a group id with no row reads `unrated`).
   Do not change `_admits`, the holder evaluation, the grant-store scan, or the kill-switch handling.

**Tests**, by these exact names, in `tests/test_admin_gateway_breakdown.py` (reuse that file's way of planting a registry, a catalog file and a graph-scope map):
- `test_no_tool_lands_in_microsoft_365_without_a_graph_scope`: a planted native tool with no spec, no declaration and no Graph scope is NOT in `m365`; a planted
  tool with a Graph scope IS.
- `test_declared_source_group_names_the_bucket_group`: a `tool_index` row with `source_group: {id: opal-data-harvest, name: opal-data-harvest, kind: bucket}`
  puts the tool in a channel with that `id` and `name` and kind `bucket`.
- `test_tool_declaring_two_buckets_appears_in_each`: a list of two elements lists the tool in both groups.
- `test_undeclared_tool_lands_in_no_source_declared`: no declaration and no Graph scope gives `id` `undeclared`, `name` `No source declared`, `kind` `undeclared`.
- `test_integration_spec_still_wins_over_a_declaration`: a tool with an integration spec that is ALSO declared stays in its integration channel.
- `test_malformed_declaration_reads_undeclared`: a `source_group` with a missing `id`, or with `kind` not `bucket`, or a list with one bad element, is treated as not declared.
- `test_grouping_basis_states_the_undeclared_count`: `grouping_basis` ends `N tool(s) declare no source.` with the true N for the planted world, including 0.
- `test_groups_are_ordered_bucket_integration_native_undeclared`: the `channels` order is bucket, integration, native, undeclared, ids sorted within a kind.
The existing tests of `test_admin_gateway_breakdown.py` and `tests/test_admin_people.py` must keep passing. If an existing assertion pins a channel id, kind, count or order
that THIS contract changes, change only that assertion to the new truth and name each such change (file, test, old, new) in your report. Change nothing else there.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Make no deploy and no AWS call. Do not edit any other `app/` module (the People view reuses this module's
   helpers and must keep working: that is AC2).
2. Another project edits `app/admin_gateway_breakdown.py` near its tool-name reading code. Keep your change inside `_compute`'s grouping loop, the final assembly
   loop, and one new helper, so it merges cleanly.
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never re-type a rule to make a test pass.
4. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md 14a). If you cannot meet a criterion as
   written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py
infra/aws/ec2/opal-gateway/tests/test_admin_gateway_breakdown.py
infra/aws/ec2/opal-gateway/tests/test_admin_people.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~31/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other `infra/aws/ec2/opal-gateway/app/` module, `app/refs/DATA_CATALOG.yaml`, and
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W31-S<k>` (the next free k for W31).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pe-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/pe1.AC1.sh; echo "exit=$?"</invocation><expect>breakdown grouping tests: 0 failed; named tests PASSED 8 of 8 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pe-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/pe1.AC2.sh; echo "exit=$?"</invocation><expect>admin suite: passed=101 or more failed=0; seam test failures=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~31/NFRA_MCPORTAL.TO-MP-pe-1.breakdown-groups-by-source.proof_of_spec.json`.
Report once, with:
- the two check outputs;
- the commit hash;
- every existing assertion you had to change (file, test, old, new), or none;
- from a real run of `_compute()` against the repository's own registry and catalog (no plant): the group ids with their tool counts, so the issuer can see
  how many tools fall to `m365`, to `undeclared`, and to each integration;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PE round-1 issuance (decomposition v11) from Andrew's 2026-10-15 ~16:3xZ word (record @5025c60ba1) and 2.0.0_SA_COO~O msgs 34496
and 34503. The declaration field is NFRA_MCPINDEX's (msg 34513; carrier MX-c-21 after MX-r-14, about 19:00Z), so today no tool is declared: the fix on its own
turns the false "Microsoft 365" list into a true Microsoft 365 group plus a "No source declared" group. Checks dry-run at the base 2026-10-15: AC1 FAIL (0 of 8 named
tests, 10 existing tests pass); AC2 PASS at base as a bound (93 passed, 0 failed). AC2's expect line says 101 because the eight new tests are added to the 93. The
release is 2.0.0_SA_COO~O's act with MI's catalog; mcportal bundle commits are pushed by 0.0.0_AB_MSTR~Z.

<status>pending</status>
<round>1</round>
<workstream>PE</workstream>
<slot>~31</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
