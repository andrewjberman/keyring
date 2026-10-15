# NFRA_MCPORTAL task order -- `MP-pf-3` -- WORKSTREAM PF ROUND 2: the breakdown reads `serves` and accepts the `store` source kind

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pf-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pf-3</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~31</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request handler; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the handler reads a catalog file and calls no new AWS API.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (a tool serving two pairs, a missing `serves`, an empty store id).
EGRESS CLASS, declared: none. No AWS call and no network call.
</preflight>

## 1. THE CELL -- `MP-pf-3` (workstream PF round 2, decomposition section PF.7)

You work on your existing branch `wk-NFRA_MCPORTAL-pe-31` in the worktree `C:/tmp/mp-pe-31`; it has been brought up to the shared branch head, so your merged `MP-pe-1` and `MP-pf-1` work is already in
`infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py`. This order file on your branch is your grant. Work only in `infra/aws/ec2/opal-gateway/`. No deploy, no AWS call, no network call, no push.

Two changes, both in `admin_gateway_breakdown.py` (keep inside the grouping loop, the final assembly loop and the helpers `_declared_source_groups` and `_segment_fields_for`):

**A. The tool-level pair is a LIST called `serves`** (the CTO's ruling replacing the single `vendor` and `firm` fields you read in `MP-pf-1`). Each `tool_index` entry whose tool reads opal-data-assets or opal-data-bd MAY carry
`serves`: a list of objects `{"vendor": <str>, "firm": <str>}`, the distinct pairs of the catalog rows that name the tool as `read_tool`. Change what `_segment_fields_for` returns and how the assembly uses it:
1. For a tool in the `opal-data-assets` or `opal-data-bd` bucket group, read `serves` from its `tool_index` entry (the same entry `source_group` comes from). Each element that is an object has its `vendor` and `firm` read as in `MP-pf-1` (a missing, non-string or empty-after-strip value reads as `unresolved`); an element that is not an object is skipped; duplicate pairs collapse to one.
2. If `serves` is absent, not a list, or yields no pair, the tool has the single pair (`unresolved`, `unresolved`).
3. A tool is listed under EVERY pair it serves: in the channel's `segments` the tool name appears in each pair's `tools` list. The channel's `tools[]` still lists the tool once.
4. Everything else in `MP-pf-1`'s contract stands: segment keys `vendor`, `firm`, `tools`; ordering by vendor ascending (`unresolved` last), then named firms, `multi`, `none`, `unresolved`; no `segments` key on any other channel.
The six tests of `MP-pf-1` keep their names and meaning but now plant `serves` where they planted `vendor` and `firm` fields: rewrite them in place (this is the one existing-assertions change this order allows; name each in your report). Where one of them planted a single pair, plant a one-element `serves`.

**B. `source_group.kind` takes a third value, `store`.** The catalog writes `{id, name, kind}` with `kind` `bucket` for an S3 bucket, `graph` for the Microsoft tools and `store` for any other source (YCharts, the Kuzu graph, a tool that reads only gateway state, DynamoDB).
Your `MP-pe-1` rule 5 treats any kind other than `bucket` and `graph` as malformed, so a `store` tool would read as undeclared. Change it: an element with a non-empty string `id` and `name` and `kind` equal to `store` is valid, and the tool joins a group
`{"id": <id>, "name": <name>, "kind": "store", "auth": "per tool", "min_tier": "per tool"}` (one group per distinct `id`; a tool with several elements is listed in each, as for buckets). `channels[].kind` gains the value `store`.
The channel order becomes: all `bucket` groups by id, then all `store` groups by id, then `integration` by id, then `native` (`m365`), then `undeclared`. `grouping_basis` keeps its sentence (add nothing). The People view keeps working through the shared placement function; do not edit `admin_people.py` (the shared function carries the change).

**Tests**, by these exact names, in `tests/test_admin_gateway_breakdown.py` (reuse the file's way of planting a registry and a catalog):
- `test_declared_store_kind_makes_a_store_group`: a tool with `source_group: {id: ycharts, name: Ycharts, kind: store}` is in a channel with `id` `ycharts`, `name` `Ycharts`, `kind` `store`;
- `test_store_declaration_is_not_malformed`: that tool is NOT in the `undeclared` channel, while a `store` element with an empty `id` is still malformed (the tool reads undeclared);
- `test_groups_are_ordered_bucket_store_integration_native_undeclared`: the channel order of rule B, ids sorted within a kind;
- `test_tool_serving_two_pairs_is_listed_in_each_segment`: an assets tool whose `serves` holds two different pairs is in both segments' `tools`, once in each, and once in the channel's `tools[]`;
- `test_missing_serves_reads_unresolved_pair`: an assets tool with no `serves` (and one with `serves: []`, and one with `serves: "x"`) is in one segment with vendor `unresolved` and firm `unresolved`.
The whole gateway admin suite must keep passing (AC2).

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Make no deploy and no AWS call. Do not edit any other `app/` module (the People view reuses the shared placement function and must keep working: that is AC2).
2. Another project edits `app/admin_gateway_breakdown.py` near its tool-name reading code. Keep your change inside the places named above so it merges cleanly.
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never re-type a rule to make a test pass.
4. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md 14a). If you cannot meet a criterion as written, REFUSE it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py
infra/aws/ec2/opal-gateway/tests/test_admin_gateway_breakdown.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~31/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other `infra/aws/ec2/opal-gateway/app/` module, `app/refs/DATA_CATALOG.yaml`, and
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W31-S<k>` (the next free k for W31).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pf-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/pf3.AC1.sh; echo "exit=$?"</invocation><expect>named tests PASSED 5 of 5.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pf-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/pf3.AC2.sh; echo "exit=$?"</invocation><expect>failed=0; seam test failures=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~31/NFRA_MCPORTAL.TO-MP-pf-3.handler-reads-serves-and-store-kind.proof_of_spec.json`, run `proof-of-spec-check.py` on it, and report once with:
- the two check outputs;
- the commit hash;
- every existing assertion you changed (file, test, old, new);
- from a real run of `_compute()` against the repository's own registry and catalog (no plant): the channels and whether any carries `segments`;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut from PF.7 (decomposition amendment ~22:0xZ): the CTO's ruling msg 34591 (`serves` list) and my reading of NFRA_MCPINDEX TO-MX-c-21 item 3 (`kind` `store`). pf3.AC1 dry-run at the base: FAIL as expected (named tests PASSED 0 of 5);
pf3.AC2 is a bound (109 passed at the base). The release is 2.0.0_SA_COO~O's act, batched with MP-pe-1 and MP-pf-1.

<status>pending</status>
<round>2</round>
<workstream>PF</workstream>
<slot>~31</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
