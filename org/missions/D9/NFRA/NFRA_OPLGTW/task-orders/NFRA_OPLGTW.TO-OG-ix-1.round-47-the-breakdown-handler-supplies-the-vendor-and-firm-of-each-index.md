# NFRA_OPLGTW task order -- `OG-ix-1` -- the gateway breakdown handler supplies the (vendor, firm) of each index: `index_pairs` on every tool of the two segmented buckets (round 47; round-46 analysis item 7; NFRA_MCPORTAL's interface GWZ1.1; P1 handler half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ix-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ix-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~171</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code and test change; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the handler reads the catalog file it already reads.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-46 analysis (`org/missions/D9/NFRA/NFRA_OPLGTW/ledger/ROUND_ANALYSIS.round46.md` @ad17495429), rank 7: "the breakdown handler's `index_pairs` (P1, the handler half), so that `2.0.0_SA_COO~MP` can cut the page filter".
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ix-1` (decomposition addendum R3-T.124, round 47, workstream ENRICH-R47-A)

WHY. The owner-only page `/api/admin/gateway` (NFRA_MCPORTAL) shows, per channel, the tools and their catalog indexes; in a vendor/firm segment of the two data buckets it should list only the indexes that belong to that segment, but the handler gives it only `tool.indexes` (a flat list), so every index of a tool shows under every segment the tool serves. NFRA_MCPORTAL's page cells (`MP-z-7`, `MP-z-8`) are built and waiting for this field. Their interface, verbatim (GWZ1.1): *"Each tool object in the breakdown may carry `index_pairs: [{ "index": <name>, "vendor": <segment vendor key>, "firm": <segment firm key> }, ...]`, one entry per (index, pair) the index serves, in the server's own order. The keys are the same strings a `segments[]` entry carries. If a tool has NO `index_pairs` key (an older payload), the page keeps listing `tool.indexes` unchanged. An EMPTY `index_pairs` means the tool has no index for any pair."*

READ FIRST: `infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py` (the `_catalog_read_tool_rows` function about line 98, `SEGMENTED_BUCKETS` and `UNRESOLVED` about lines 164-165, `_segment_fields_for`, and `_compute` about lines 324-365 where each tool's `entry` is built and appended to its channel); the catalog `app/refs/DATA_CATALOG.yaml` (a silver row looks like `entity: ...`, `read_tool: client_resolve_account`, `bucket: opal-data-assets`, `prefix: blackdiamond/49f/silver/dim_account_xref/`); `tests/test_admin_gateway_breakdown.py` (the fakes and `test_real_server_tool_inventory`).

DO, in `infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py` ONLY (plus the new test file):

1. **A catalog reader for the index rows** (new function, read once per `_compute`, using the same `CATALOG_YAML` and the same walk as `_catalog_read_tool_rows`): index id -> `{"bucket", "prefix"}` for every mapping anywhere in the catalog that carries a string `bucket` and a string `prefix` and an id (`entity`, else `key`, else `index`, as `_catalog_read_tool_rows` reads it); the first row for an id wins.
2. **The pair rule.** For an index id: if its catalog row exists, its `bucket` is `opal-data-assets` or `opal-data-bd` (`SEGMENTED_BUCKETS`) and its `prefix` has at least two non-empty path components, the pair is `(first component, second component)` as `vendor` and `firm`; in every other case (no row, another bucket, a short prefix) the pair is `("unresolved", "unresolved")` (the module's `UNRESOLVED`). Never invent a name and never reject a new value.
3. **In `_compute`, for a tool placed in a channel whose id is in `SEGMENTED_BUCKETS`** (the same `if home["kind"] == "bucket" and home["id"] in SEGMENTED_BUCKETS` branch that sets `chan["pairs"]`), the tool entry appended to THAT channel carries `index_pairs`: a list with one `{"index": <id>, "vendor": ..., "firm": ...}` per id of the entry's own `indexes`, in the same order as `indexes`. A tool in any other channel (Microsoft 365, an integration, an undeclared or non-segmented bucket) carries NO `index_pairs` key. A tool in two channels, one segmented and one not, carries it only in the segmented one. The response stays JSON-serialisable; every existing key and value of the body is unchanged.
4. **The new test file `tests/test_og_ix1.py`** with at least these tests (names fixed), built on the fakes and fixtures of `tests/test_admin_gateway_breakdown.py` (import them or copy the few lines; plant a catalog with `_plant_catalog`): `test_ogix1_pairs_from_prefix`, `test_ogix1_unresolved_cases` (no row; a row in another bucket; a one-component prefix), `test_ogix1_order_follows_indexes`, `test_ogix1_other_channels_have_no_key`, `test_ogix1_tool_in_two_channels`.

## 2. BOUNDS

- Write only `app/admin_gateway_breakdown.py`, `tests/test_og_ix1.py`, `W/` and, if a row is needed, the channel. NO other product file (`admin_api.py`, `admin_people.py` and the page are not touched), no release, no deploy, no Terraform, no AWS call, no `EC2_MANIFEST.json` edit (the `mcportal_commit` pin of the release is the applier's, item 18 of the round list).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number, email address or client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_gateway_breakdown.py
infra/aws/ec2/opal-gateway/tests/test_og_ix1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~171/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W171-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ix-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/ix1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)segmented channels hold tools: ok.*every tool in a segmented channel carries an index_pairs list: ok.*every element is exactly \{index, vendor, firm\}: ok.*one for one, in the same order: ok.*first two components of the catalog row's prefix \(else unresolved\): ok.*some pair resolves to a real vendor and firm: ok.*tools in other channels carry no index_pairs key: ok.*the body serialises: ok.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ix-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r47/checks/ix1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)new file tests/test_og_ix1.py: [1-9]\d* passed, 0 failed.*neighbours \(\d+\): [1-9]\d* passed, failed names \[\].*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the real tool inventory and the real catalog, graded against an independent read of the catalog YAML. `AC2`: your test file and the four existing files for the breakdown, the people view and the route.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ix-1.round-47-the-breakdown-handler-supplies-the-vendor-and-firm-of-each-index.proof_of_spec.json`. Validate it after your last commit with `python3 -I .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` (`python3`, not `python`: ruling msg 35901). Flip the ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 47, workstream ENRICH-R47-A, `<risk>WORLD</risk>` is the gateway-path floor. Source: the CTO's round-46 analysis (msg 36165) rank 7; the page half is `2.0.0_SA_COO~MP`'s (cells `MP-z-7`, `MP-z-8`, drained and inert until this handler is live and a bundle release pins `mcportal_commit` `21ad40432cae0d09c5ab9d806307944baaf45cb9`).
- READINGS DISCLOSED TO THE CTO: (1) the pair of an index is read from the first two components of its catalog row's prefix, not from the tool's `serves` list: a tool that serves two pairs has indexes under both, and the prefix is the only place an index names its own pair. (2) Only tools placed in `opal-data-assets` or `opal-data-bd` carry the key, because only those channels have segments; the page keeps listing `tool.indexes` for every other tool, as GWZ1.1 says. (3) An index whose row is absent or outside the two buckets reads `unresolved`, the module's existing word, so the page can show it under the unresolved segment.
- Pre-cut: `AC1` base FAIL as expected (5 tool entries sit in the segmented channels and none carries the key); the real inventory and catalog run offline in about 3 seconds. `AC2` base FAIL as expected (no test file). The four neighbour files pass at the base (49 tests).

<status>pending</status>
<round>47</round>
<workstream>ENRICH-R47-A</workstream>
<slot>~171</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
