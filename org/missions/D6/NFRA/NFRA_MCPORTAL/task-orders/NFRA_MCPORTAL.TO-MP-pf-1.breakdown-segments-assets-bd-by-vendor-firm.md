# NFRA_MCPORTAL task order -- `MP-pf-1` -- WORKSTREAM PF ROUND 1: the breakdown segments an opal-data-assets / opal-data-bd bucket by (vendor, firm)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pf-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pf-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~31</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request handler; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the handler reads a catalog file and calls no new AWS API.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (a missing field, a firm that mixes, a tool in two buckets).
EGRESS CLASS, declared: none. No AWS call and no network call.
</preflight>

## 1. THE CELL -- `MP-pf-1` (workstream PF round 1, decomposition section PF.1)

You work on your existing branch `wk-NFRA_MCPORTAL-pe-31` in the worktree `C:/tmp/mp-pe-31`, AFTER the issuer has merged your `MP-pe-1` work (this order file arrives on your branch as your grant; your
`MP-pe-1` commits `90996f1825` and the commits that follow it are inherited state: the single placement function and `source_group` reading are already in `app/admin_gateway_breakdown.py`).
Work only in `infra/aws/ec2/opal-gateway/`. No deploy, no AWS call, no network call, no push.

**What this is for.** The `/gateway` page must show each AWS bucket as a clear segment and, inside `opal-data-assets` and `opal-data-bd`, each (vendor, firm) pair as a sub-segment (Andrew's word, carried in the PRD).
The segmentation key is CONTRACT C-GROUP: the catalog's `tool_index` rows carry `bucket` (which is `source_group.id`) and, on opal-data-assets and opal-data-bd rows, `vendor` and `firm`. The catalog carries them only
after a later catalog release; until then no row has them and every tool reads `unresolved`. The handler reads the fields and never re-derives them.

Build, in `infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py` (keep the change inside the grouping loop, the final assembly loop and one new helper):
1. When a tool joins a group of kind `bucket` whose `id` is `opal-data-assets` or `opal-data-bd`, read two more fields from the tool's `tool_index` row, the same row `source_group` comes from: `vendor` and `firm`. A field
   that is missing, not a string, or empty (after strip) reads as the literal string `unresolved`. The handler does NOT check the values against any list (a new value is an addendum to the contract, not a local rejection).
2. That channel gains `segments`: a list of `{"vendor": <str>, "firm": <str>, "tools": [<tool name>, ...]}`, one entry per distinct (vendor, firm) pair among the channel's tools, each tool name listed once, `tools` sorted by name.
   A tool in two buckets is placed per bucket by its own `source_group` element; its `vendor` and `firm` are the row's, and they matter only in the two buckets above.
3. Order of `segments`: `vendor` ascending, with the vendor `unresolved` last; inside a vendor the named firms ascending, then `multi`, then `none`, then `unresolved`.
4. A channel that is not `opal-data-assets` or `opal-data-bd` carries NO `segments` key (absent, not empty). `channels[].tools[]`, `indexes`, `holders`, `holders_basis`, `rating`, `grouping_basis` and the channel order keep
   their meaning. The People view is unchanged.

**Tests**, by these exact names, in `infra/aws/ec2/opal-gateway/tests/test_admin_gateway_breakdown.py` (reuse that file's way of planting a registry, a catalog file and a graph-scope map):
- `test_assets_bucket_splits_into_vendor_firm_segments`: two assets tools with different (vendor, firm) give two segments, each with its tool; a channel `segments` entry has exactly the keys `vendor`, `firm`, `tools`;
- `test_multi_none_and_unresolved_firms_are_own_segments`: firms `multi`, `none` and `unresolved` each become their own segment and are never folded into a named firm;
- `test_missing_vendor_or_firm_reads_unresolved`: a row with no `vendor`, a row with `firm: 7`, and a row with `firm: "  "` read `unresolved`;
- `test_bucket_without_vendor_firm_fields_has_no_segments`: a tool declared in `opal-data-harvest` (even with vendor and firm fields on its row) gives a channel with no `segments` key;
- `test_segments_order_named_firms_before_multi_none_unresolved`: the order of rule 3, including the vendor `unresolved` last;
- `test_tool_in_two_buckets_is_segmented_only_where_it_is_assets_or_bd`: a tool declared in `opal-data-harvest` and `opal-data-assets` appears in the harvest channel with no segments and in one assets segment.
The existing tests of the gateway admin suite must keep passing (AC2). If an existing assertion pins a channel's keys exactly and this contract adds `segments`, change only that assertion and name it (file, test, old, new) in your report.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Make no deploy and no AWS call. Do not edit any other `app/` module.
2. Another project edits `app/admin_gateway_breakdown.py` near its tool-name reading code. Keep your change inside the grouping loop, the final assembly loop, and one new helper, so it merges cleanly.
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
  <criterion id="AC1" cell_refs="MP-pf-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/pf1.AC1.sh; echo "exit=$?"</invocation><expect>named tests PASSED 6 of 6.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pf-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/pf1.AC2.sh; echo "exit=$?"</invocation><expect>failed=0; seam test failures=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~31/NFRA_MCPORTAL.TO-MP-pf-1.breakdown-segments-assets-bd-by-vendor-firm.proof_of_spec.json`.
Report once, with:
- the two check outputs;
- the commit hash;
- every existing assertion you had to change (file, test, old, new), or none;
- from a real run of `_compute()` against the repository's own registry and catalog (no plant): the channels and whether any carries `segments` (expected: none until the catalog carries C-GROUP);
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PF issuance (decomposition v12) from PRD v0.9 @532d1e68bb and the CTO's GO (msg 34553). It follows MP-pe-1 on worker ~31's queue because both write
`admin_gateway_breakdown.py`. AC2 reads 103 or more passed because MP-pe-1 leaves 103 and the six tests add. Dry-run at the base (the shared tree, before MP-pe-1 merged): AC1 FAIL as expected (0 of 6 named
tests), AC2 FAIL as expected (93 passed, below 103). The release is 2.0.0_SA_COO~O's act, batched with MP-pe-1; the catalog fields arrive with MCPINDEX's first C-GROUP release.

<status>pending</status>
<round>1</round>
<workstream>PF</workstream>
<slot>~31</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
