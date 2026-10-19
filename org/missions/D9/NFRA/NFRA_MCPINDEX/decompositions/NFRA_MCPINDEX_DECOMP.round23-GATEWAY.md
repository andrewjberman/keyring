# NFRA_MCPINDEX -- decomposition addendum, ROUND 23, workstream GATEWAY (2.0.0_SA_COO~MI)

**archetype:** COORDINATE

Companion to `NFRA_MCPINDEX_DECOMP.round22-GATEWAY.md`. One issuer, one round (PRD v0.18 Placement). Spec-frozen once issued.

**AMENDED AGAIN ~17:2xZ for PRD v0.19 as ADMITTED @7c42c0c743 (CTO msg 36016; CVO @48390bb520), which supersedes @f59634ebe3: the routing arm is graded per (tool, linked row) pair against a SOURCE SET traced from the code, with an intent check against the declared scope and the defect classes link, code and display; the routing table is emitted by ONE re-runnable script with planted negatives; FWD-24 records `route: response-cited | code-cited`. The ~17:1xZ amendment below stands except where this paragraph and R23.2 say otherwise: `MX-h-6` is re-specified and the new workstream GATEWAY-TRACE adds `MX-r-1` (the emitter) and `MX-s-1..6` (the source sets by channel group). The CVO's non-blocking note, a third planted case for the display class, is in `MX-r-1`.**

**AMENDED ~17:1xZ for PRD v0.19 @f59634ebe3 (CTO msg 36006; Andrew-direct ~16:2xZ, CRO~Z record @634d368d98): the order is opal-data-assets and its vendor/firm segments FIRST, then the integration channels (Schwab, Black Diamond, YCharts and the rest), then the others; FWD-23 gains a ROUTING arm and FWD-24 gains the FAIL class `misrouted`. The amendment adds `MX-h-6`, the `expect_source` requirement to the case cells, R23.2 deltas and R23.4 ruling 9; `MX-h-1..5` and `MX-k-1..6` otherwise stand.**

Source: the CTO's round-22 analysis `ledger/ROUND_ANALYSIS.round22.md` @44e6950a24 (msg 35997: E1 harvest to member (a); E2 the other channels to (a) or (c); E3 the battery across every channel, senders PREVIEW-ONLY under open call c5c2; E4 the sheets), PRD v0.18 @4b8dcf3b86, and **the corrected census** (below): the analysis was written on my round-22 census, which undercounted; the correction is `deliverables/2.0.0_SA_COO~MI/round22/evidence/CORRECTION_CENSUS_V1_UNDERCOUNT_20261019.md` (msg to the CTO 16:04Z). Round 23 is cut on the corrected numbers, so the E2 list gains the seven integration channels.

## R23.1 MEASURED STATE (the corrected census, read 2026-10-19 16:02:52Z on the gateway host, ssm `0b455a1e-c194-416d-94cd-e508236dea03`)

`round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json`: 14 channels, 127 tools, 8 (vendor, firm) segments. Coverage over the whole census (`COVERAGE_ALL_20261019_v2.json`): 195 refusals.

| channel (kind) | tools | member b | b with a catalog index | b with NO index |
|---|---|---|---|---|
| opal-data-assets (bucket) | 5 | 5 | 5 | 0 |
| opal-data-etfs (bucket) | 18 | 18 | 18 | 0 |
| opal-data-harvest (bucket) | 14 | 14 | 10 | 4 |
| opal-data-mdpf (bucket) | 1 | 1 | 1 | 0 |
| opal-data-portal-v2 (bucket) | 18 | 17 | 17 | 0 |
| dynamodb (store) | 4 | 4 | 3 | 1 |
| blackdiamond, portal_index (integration) | 1, 6 | 0 | 0 | 0 |
| globgrph (integration) | 2 | 1 | 0 | 1 |
| opal_discover (integration) | 2 | 2 | 2 | 0 |
| opal_portal (integration) | 2 | 1 | 0 | 1 |
| schwab (integration) | 5 | 1 | 0 | 1 |
| ycharts (integration) | 6 | 5 | 0 | 5 |
| m365 (native) | 43 | 35 | 0 | 35 |
| total | 127 | 104 | 56 | 48 |

Rows: 274 under a channel; 91 have no served `read_tool`, all in opal-data-assets and all carrying `gap_owner: NFRA_OPLGTW` already. The rows that name `schwab_query`, `mdpf_get_*` and `etfs_get_positioning` are served tools in the corrected census (the undercount had hidden them).

## R23.2 FROZEN CONTRACTS

All files ASCII, JSON `indent=1`, `\n` newlines, python 3.9. The CASES and RESULTS schemas are round 22's (R22.2); the COVERAGE contract is round 22's with the delta below.

**ROWS** (input to the measurer): `{"rows":[{"entity","bucket","prefix"}]}`; a row's `prefix` is the S3 key prefix of its table (the catalog row's `prefix` field).

**WINDOWS** `partition_windows/1`, written by `python workflows/gateway_battery/partition_windows.py --rows FILE --out FILE [--fake FILE] [--now UTC_STAMP]`:
```
{"schema":"partition_windows/1","read_at":<--now, else the UTC clock to the second, form YYYY-MM-DDTHH:MM:SSZ>,"claim":"measured",
 "rows":[{"entity","bucket","prefix","kind":"dated|undated|empty|error","partition_key","earliest","latest","partitions","error"?}]}
```
- Each row is listed with `list_objects_v2(Bucket, Prefix, Delimiter="/")`, every page (`ContinuationToken` while `IsTruncated`). The measurer calls `list_objects_v2` and nothing else: no object read, write, copy or delete.
- A first-level common prefix whose tail (after the row prefix) is `<key>=YYYY-MM-DD/` (a valid calendar date) is a date partition; `partition_key` is the first such `<key>`; `earliest` and `latest` are the minimum and maximum dates; `partitions` counts them. Other folders and bad dates are ignored.
- `dated`: at least one date partition. `undated`: entries came back but no date partition. `empty`: nothing under the prefix. `error`: the listing raised; `error` holds `<ExceptionName>: <text>`; the other fields are null and `partitions` is 0.
- `--fake FILE` replaces the S3 client with a fake that answers from `{"<bucket>|<prefix>": [page, page, ...]}` (a page is a `list_objects_v2` response dict, returned in order per call; a missing key raises `KeyError`, which reads as `error`). Without `--fake` the client is `boto3.client("s3")`. Tests and the criteria use `--fake`; only the issuer runs it live.
- Stdout `WINDOWS rows=N dated=a undated=b empty=c error=d`. Exit 0 iff `error` is 0, 1 otherwise (the file is written either way), 2 on an unreadable rows file, no `rows`, an empty list, or a row without `entity`, `bucket` or `prefix`. Same input and `--now` give the same bytes.

**DISPOSITION** `gateway_disposition/1`: `{"schema":"gateway_disposition/1","scope":<free text>,"tools":[{"tool","member":"b"|"c","owner"?,"reason"}]}`. It covers ONLY tools with no catalog index (an indexed tool is made `a` by the applier without a disposition). `c`: `reason` non-empty, no `owner`. `b`: `owner` (a project code or `unowned`) and `reason` (why no row exists and what would create one), both non-empty. A `reason` is ASCII, at least 40 characters, and ENDS with a source reference `[app/<file>.py:<line>]` naming a real line of the gateway source (`infra/aws/ec2/opal-gateway/app/`) where the tool's definition or the code it reaches sits.

**APPLY** `python workflows/gateway_battery/apply_disposition.py --census F --members F --windows F --dispositions F [F ...] --out F [--report F]`:
- Reads the census (`gateway_surface_census/1`), the members file text, the WINDOWS file and the disposition files. Writes the NEW members text to `--out` (never edits `--members` in place) and a report `{"changes":[{"tool","rule"}]}`.
- Only entries inside the top-level `members:` list are edited. The file also has a top-level `buckets:` list whose entries start `- tool:` too; they, the header comments, every comment line between entries and every entry it does not change stay byte for byte. Entry order is unchanged. A changed entry is replaced by its new block (same two-space indentation as the file's other entries).
- Rule `auto_a` (no disposition needed): a `member: b` entry whose census `indexes` is non-empty becomes `{tool, member: a, index: <first of the sorted indexes>, links: <sorted indexes>, history_depth, freshness}` plus the old entry's `bucket` and `bucket_source` if it had them (the old `owner` is dropped).
  - One linked row: `freshness` = the row's WINDOWS entry if `dated`: `{claim: measured, value: <latest>, basis: "s3://<row bucket>/", method: key-date, read_at: <windows read_at>}`; `history_depth` = `{claim: inferred, value: "<earliest>..<latest>", basis: "s3://<row bucket>/", source: "first-level partition listing of the row <entity>", method: partition-listing, read_at: <windows read_at>}`. If the row is not `dated` or has no WINDOWS entry, both are `{claim: absent, reason: <why: not dated at the first level, or no windows entry>}`.
  - Several linked rows: `freshness` = `{claim: absent, reason: "a multi-index tool: each linked row has its own freshness"}`; `history_depth` = `{claim: per-link, links: [one element per linked row in links order, each carrying "row": <entity> and the inferred or absent claim of that row as above]}`.
  - Every composed claim passes `validate_claim` of `workflows/atom_decomposition/emit_catalog_v02.py` (import it by path with importlib; it is a pure function; do not edit that file); a claim that fails is a bug in the applier, exit 2.
- Rule `disposed_b` / `disposed_c`: a tool named in a disposition. A `b` entry becomes `{tool, member: b, owner, reason}` and a `c` entry `{tool, member: c, reason}`, each plus the old `bucket` and `bucket_source` if present. A `member: b` entry named in no disposition and with no index is untouched.
- Refused with exit 2 and NO output file: a disposition tool the census does not serve; one that has census indexes (an indexed tool is never disposed); `member: a` or any member letter but b or c; a `c` with an empty reason; a `b` with no owner or no reason; the same tool in two dispositions or twice; an unreadable windows, census or disposition file.
- Stdout `APPLY auto_a=N disposed_b=B disposed_c=C untouched_b=U`. Same input gives the same bytes.

**CASES and RESULTS delta** (PRD v0.19, FWD-24 `misrouted`):
- A case MAY carry `"expect_source": "<string>"`: the bucket id, key prefix, store or integration source that the tool's OWN CODE reads for that case, taken from the catalog row's `bucket` and `prefix` or `key`, or from the code's `bucket_source` line, NEVER from the tool's name.
- A result MAY carry `"answer_source": ["<string>", ...]`: the source fields the response itself carries (its `source_keys` entries, bucket, prefix, or its integration or source field), copied as the signed-in session recorded them.

**SOURCE SETS** `gateway_source_sets/1` (the TRACE of what each tool's code can read; a data file written by a worker who read the code):
```
{"schema":"gateway_source_sets/1","scope":<free text>,"tools":[{"tool","vendors":[sorted distinct vendors of its sources],
  "sources":[{"kind":"s3"|"store"|"integration"|"graph","bucket"?,"prefix"?,"store"?,"integration"?,"graph"?,"vendor","cite":"app/<file>.py:<line>"}]}]}
```
- One entry per tool of the cell's scope, once. One source per dispatch branch the code can take (a multi-vendor `client_*` tool has one source per vendor branch).
- `s3` carries `bucket` (the bucket id, resolved from the constant or config key the code uses) and `prefix` (the key prefix that branch reads; the empty string only when it reads the whole bucket); `store` carries `store`; `integration` carries `integration`; `graph` carries `graph` (the Microsoft Graph endpoint family).
- `vendor` is the data's owner: the catalog's own vendor values (`schwab`, `blackdiamond`, `orion`, `eclipse`, `smartx`, `commonwealth`, `gateway`, `market`) or `opal` (Opal's own non-client data), `ycharts`, `microsoft`, `bloomberg`, `other`.
- `cite` is `app/<file>.py:<line>` of the line that names the source or the branch that selects it; the cited file must contain the bucket, store, integration or graph string. `bucket_source` in `members.yaml` and the tool's linked rows are index CLAIMS: the trace is checked against them and never copied from them; a disagreement is a surprise row.

**ROUTING TABLE** `gateway_routing_table/1`, emitted by `python workflows/gateway_battery/routing_table.py --census F --catalog F --sources F [F ...] --out F [--channel ID ...] [--plant link|code|display --tool NAME]`:
- Inputs: the CENSUS (channels, `segments`, each tool's `indexes`), the catalog (rows from `silver_datasets`, `portal_datasets` and `harvest_datasets` with `entity`, `bucket`, `prefix`, `vendor`; channel artifacts `channels[].artifacts[]` with `entity` and `key` take the catalog's top-level `bucket` and the `key` as their prefix), and one or more SOURCE SETS files (a source with no `cite` or no `kind` is refused, exit 2).
- Per census tool (all, or the `--channel` ones), an entry `{"tool","channel","declared_vendors":[sorted],"source_set":[the tool's sources],"pairs":[{"row","row_source":{"bucket","prefix"}|null,"verdict":"ROUTED"|"MISROUTED"|"UNRESOLVED","class":null|"link"}] (sorted by row),"verdict":"ROUTED"|"MISROUTED"|"UNTRACED","class":null|"link"|"code"|"display"}`, sorted by tool, plus `"counts"` (`tools`, `pairs`, `routed_pairs`, `link`, `code`, `display`, `untraced`, `unresolved`).
- **Link check**, per (tool, linked row) pair: the row's source is its `bucket` and `prefix`; the pair is `ROUTED` when some `s3` source of the tool has the same `bucket` and one of the two prefixes starts with the other; otherwise `MISROUTED` (class `link`). A linked id that names no catalog row is `UNRESOLVED` (counted, never a defect).
- **Intent check**, per tool: `declared_vendors` is the set of `vendor` values of the census `segments` entries that list the tool, plus the tool's channel id when that id is itself a vendor name (a vendor value of any catalog row, or `ycharts`). When `declared_vendors` is not empty, every vendor of the tool's sources must be in it, else the tool is `MISROUTED` (class `code`): it reads outside its declared scope. The tool's name is never consulted.
- **Display check**, per tool: every vendor of a census `segments` entry that lists the tool must be a vendor of the tool's sources, else `MISROUTED` (class `display`): the page lists it under a segment it does not serve.
- Tool verdict and class, in this order: `UNTRACED` when no source set names the tool; else `code` if the intent check fails; else `link` if any pair is `MISROUTED`; else `display` if the display check fails; else `ROUTED`.
- **Planted negatives**: `--plant KIND --tool NAME` applies ONE defect to that tool in memory (the real inputs are not changed) and writes the table for the planted state: `link` appends a catalog row, from a bucket that none of the tool's sources names, to the tool's linked rows; `code` appends an `s3` source with bucket `planted-bucket`, an empty prefix, cite `app/planted.py:1` and a vendor that none of the tool's sources has; `display` adds a `segments` entry listing the tool under a vendor that none of its sources has. It prints `PLANT kind=K tool=T verdict=MISROUTED class=K` and exits 0 when the table reads that tool `MISROUTED` of class K; it prints `PLANT-MISSED kind=K tool=T` and exits 3 otherwise; it exits 2 when the tool is not in the census.
- **SERVES (CTO ruling @473f5177a8, P2: `serves` is generated from the traced source set, never hand-edited):** `--serves-out FILE` also writes `gateway_serves/1`: `{"schema":"gateway_serves/1","tools":[{"tool","serves":[{"vendor","firm"}],"current":[{"vendor","firm"}],"added":[...],"removed":[...]}],"counts":{"tools","changed"}}`, one entry per tool that has a source set, sorted by tool, every list sorted by (vendor, firm).
  - `serves` (generated) is the set of (`vendor`, `firm`) of every catalog row (table rows only) that one of the tool's `s3` sources matches, by the same bucket and prefix rule as the link check; a source with no matching row contributes (the source's `vendor`, `unresolved`).
  - `current` is the `serves` list of the tool's row in the catalog's top-level `tool_index` list (a list of mappings with `vendor` and `firm`); no row or no `serves` is an empty list.
  - `added` is generated minus current, `removed` is current minus generated (the pairs the catalog claims that the code cannot reach: Schwab on a `client_*` tool is the CTO's first named case). `changed` counts the tools with either list non-empty. Stdout gains `SERVES tools=T changed=C` after the ROUTING line. The planted modes do not write `--serves-out`.
- Stdout without `--plant`: `ROUTING tools=T pairs=P routed_pairs=R misrouted_tools=M link=a code=b display=c untraced=u`. Exit 0 iff `M` and `u` are 0, 1 otherwise (the file is written either way), 2 on unreadable input. The same input gives the same bytes.

**CASES and RESULTS delta** (PRD v0.19, FWD-24 `route`):
- A case MAY carry `"expect_source": "<string>"`: the bucket id, key prefix, store or integration source that the tool's OWN CODE reads for that case (a hint taken from the code, never from the tool's name).
- A result MAY carry `"answer_source": ["<string>", ...]`: the source fields the response itself carries (its `source_keys` entries, bucket, prefix, or its integration or source field), copied as the signed-in session recorded them.

**BATTERY delta** (the round-22 `tool_battery.py` gains `route` and the misrouted class; without `--routing` everything is exactly as in round 22):
- `grade` gains an optional `--routing FILE` (a ROUTING TABLE). When given, a case that would otherwise be a PASS (`expect: nonempty`, `ok` with rows, `source_check.agrees` true) is also routed:
  - the result carries a non-empty `answer_source` list: the route is `response-cited`. An element MATCHES a source of the tool's routing entry when the source's `prefix` (if non-empty) is contained in the element, or, for a source with an empty prefix, its `bucket` is contained in the element, or its `store`, `integration` or `graph` string is. EVERY element must match some source of the tool's `source_set`; one element that matches none is FAIL `misrouted`;
  - the result carries no `answer_source` (missing or empty): the route is `code-cited`, and it is a PASS only when the routing table holds the tool with verdict `ROUTED`; otherwise FAIL `route_unproven`.
  - Each graded case then carries `"route": "response-cited" | "code-cited"` (the key is absent when `--routing` is not given, and for a case that did not reach the routing step the value is `null`).
- New subcommand `plant-route --cases F --results F --case CASE_ID --out F`: copies RESULTS with that case's `answer_source` replaced by the single element `planted/wrong/source/`; it exits 2 (`REFUSED:` on stderr, no output file) when the case is not in the cases file; stdout `PLANT-ROUTE case=<id>`. Grading the planted file with the routing table must read that tool FAIL `misrouted`.

**COVERAGE delta** (the round-22 gate `index_coverage.py` gains an EXPLAINED remainder; its contract otherwise stands):
- A row under an in-scope channel with no served `read_tool` and a non-empty STRING `gap_owner` (after strip) is not a `row_no_read_tool` refusal; it is an explained record `{class: row_explained_gap, channel, subject: <entity>, detail: <gap_owner>}`. A blank or non-string `gap_owner` stays a refusal.
- A `member: b` tool with a non-empty string `owner` AND a non-empty string `reason` (after strip) is not a `tool_member_b` refusal; it is an explained record `{class: tool_b_explained, channel, subject: <tool>, detail: <owner>}`. A `b` without a reason stays `tool_member_b`.
- Nothing else changes: an undeclared-channel tool that is not `c` with a reason still refuses `undeclared_tool` (an explained `b` there is also listed as explained).
- The output file gains `"explained": [sorted by (class, channel, subject, detail)]` and the denominator gains `"explained": N`. The stdout line becomes `COVERAGE channels=N tools=T rows=R refusals=K explained=E`. Exit 0 iff K is 0 (explained records never fail the run), 1 if K > 0, 2 unreadable input.
- The round-22 criteria `g2.AC1` and `g2.AC2` are updated to the new line and must keep passing; the existing tests of the file move with the line.

## R23.3 THE CELLS

| cell | what | write set | risk | serves | order |
|---|---|---|---|---|---|
| `MX-h-1` | The partition-window measurer (R23.2 WINDOWS) | `workflows/gateway_battery/partition_windows.py`, `.../tests/test_partition_windows.py` | LOCAL | FWD-23 (E1, E2) | worker ~62 |
| `MX-h-2` | The applier (R23.2 APPLY) | `.../apply_disposition.py`, `.../tests/test_apply_disposition.py` | LOCAL | FWD-23 (E1, E2) | ~63 |
| `MX-h-3` | The gate's explained remainder (R23.2 COVERAGE delta) | `.../index_coverage.py`, `.../tests/test_index_coverage.py`, `.../tests/test_index_coverage_explained.py` | LOCAL | FWD-23 | ~64 |
| `MX-h-4` | Dispositions for the 13 unindexed b tools outside m365 (harvest 4, dynamodb 1, globgrph 1, opal_portal 1, schwab 1, ycharts 5) | `deliverables/0.9.0_WK_NFRA_MCPINDEX~65/disposition_non_m365.json` | LOCAL | FWD-23 (E1, E2) | ~65 |
| `MX-h-5` | Dispositions for the 35 unindexed b tools of m365 | `deliverables/.../~66/disposition_m365.json` | LOCAL | FWD-23 (E2) | ~66 |
| `MX-k-1` | Battery cases, opal-data-etfs (18 tools) | `deliverables/.../~67/cases_etfs.json` | LOCAL | FWD-24 (E3) | ~67 |
| `MX-k-2` | Cases, opal-data-portal-v2, opal-data-mdpf, portal_index (25 tools) | `.../~68/cases_portal.json` | LOCAL | FWD-24 | ~68 |
| `MX-k-3` | Cases, opal-data-assets, schwab, blackdiamond (11 tools) | `.../~69/cases_assets.json` | LOCAL | FWD-24 | ~69 |
| `MX-k-4` | Cases, dynamodb, globgrph, opal_discover, opal_portal (10 tools) | `.../~65/cases_stores.json` (queued behind MX-h-4) | LOCAL | FWD-24 | ~65 |
| `MX-k-5` | Cases, ycharts (6 tools) | `.../~66/cases_ycharts.json` (queued behind MX-h-5) | LOCAL | FWD-24 | ~66 |
| `MX-k-6` | Cases, m365 (43 tools) | `.../~67/cases_m365.json` (queued behind MX-k-1) | LOCAL | FWD-24 | ~67 |
| `MX-h-6` | The battery's `--routing`, `route` record, `misrouted` and `route_unproven` classes and `plant-route` (R23.2 CASES and RESULTS delta, BATTERY delta); workstream GATEWAY-ROUTE | `workflows/gateway_battery/tool_battery.py`, `.../tests/test_tool_battery_route.py` | LOCAL | FWD-24 (v0.19) | ~62 (queued behind MX-h-1) |
| `MX-r-1` | The routing-table emitter with its three planted negatives (R23.2 ROUTING TABLE); workstream GATEWAY-TRACE | `workflows/gateway_battery/routing_table.py`, `.../tests/test_routing_table.py` | LOCAL | FWD-23 (v0.19) | ~70 |
| `MX-s-1` | Source sets (the trace of the code) for opal-data-assets, schwab, blackdiamond: 11 tools. FIRST in the order | `deliverables/.../~71/source_sets_assets.json` | LOCAL | FWD-23 | ~71 |
| `MX-s-2` | Source sets, opal-data-etfs (18 tools) | `.../~72/source_sets_etfs.json` | LOCAL | FWD-23 | ~72 |
| `MX-s-3` | Source sets, opal-data-portal-v2, opal-data-mdpf, portal_index (25 tools) | `.../~73/source_sets_portal.json` | LOCAL | FWD-23 | ~73 |
| `MX-s-4` | Source sets, opal-data-harvest and dynamodb (18 tools) | `.../~74/source_sets_harvest.json` | LOCAL | FWD-23 | ~74 |
| `MX-s-5` | Source sets, ycharts, globgrph, opal_discover, opal_portal (12 tools) | `.../~75/source_sets_integrations.json` | LOCAL | FWD-23 | ~75 |
| `MX-s-6` | Source sets, m365 (43 tools) | `.../~76/source_sets_m365.json` | LOCAL | FWD-23 | ~76 |

The issuer's own acts at the drain (R23.7) are the live runs. Harvest's 16 round-22 cases stand as its E3.

## R23.4 RULINGS (the issuer rules inside its own decomposition, rule 7)

1. **An indexed member b becomes a mechanically.** The applier, not a worker, moves the 56 b tools that already have a catalog index to `a`; their claims are composed from the measurer's listing, never typed. The judgment work is only the 48 tools with no index.
2. **Depth and freshness are said honestly.** A date partition read at the first level gives a measured freshness (single-row tools) and an inferred partition-listing depth window. A tool linked to several rows gets one depth element per row and an `absent` freshness with its reason. A row with no first-level date partition (a portal JSON object, a table partitioned by security) reads `absent` with the reason; **FWD-20 says `absent` only where no served artifact carries any date, so every `absent` the applier writes is FWD-20 debt, counted and listed at the drain, not a claim of "no date exists".**
3. **`c` for the Microsoft 365 reads is a stretch and is said so.** FWD-20 defines (c) as "not a data read". The 35 unindexed m365 tools read the caller's own mailbox, files, calendar or Teams, which is data but not Opal dataset data and has no catalog row by design. Their disposition is `c` with a reason that says exactly that, grounded in the source line. **Said to the CTO as a ruling that widens (c)'s plain meaning.**
4. **An explained remainder is allowed and counted.** A `b` with an owner and a reason, and a row with a `gap_owner`, are listed beside the refusals and never hidden. FWD-23 is realized only at zero refusals AND the explained list stated to the CTO; the explained `b` set is the honest remainder.
5. **REFUSED-CORRECT and the sheet admit check are the issuer's host programs** (as the CTO ruled, msg 35997): a read-only in-process call of the installed entitlement decision for a named principal and tool, written by this seat in the style of `host_breakdown.py`, under the OG-ap-38 guard. They are not worker cells.
6. **Senders stay PREVIEW-ONLY** (open call c5c2 is Andrew's). A sender is a tool whose census `write_class` is a real class (`write_comms`, `write_files`: 8 tools in the m365 channel) or `opal_data_refresh_upload` (the one mutating integration tool); every case of a sender is `expect: preview`. **A `write_class` of `UNCLASSIFIED` (22 integration tools: all the schwab, ycharts, portal_index, opal_discover, globgrph and opal_portal tools) means only that `destructive_ops` has no entry for the tool, which the census reports as `access: write`; it does not make the tool a sender.** Those tools are read from their definitions: a reader's cases must end their `source_hint` with the `[app/<file>.py:<line>]` of the definition that shows it only reads. The 22 unclassified integration tools are a finding for `2.0.0_SA_COO~O` (PRD C2: every tool is classified in `destructive_ops`).
7. **The m365 cases read the signed-in principal's own data only**, and a recorded result holds counts, never message text. A case that needs an id from an earlier answer says so with `depends_on`.
9. **The routing arm (PRD v0.19 as admitted) is one table and one battery, not three testers.** The FWD-23 routing table is EMITTED by `routing_table.py` (`MX-r-1`) from the census, the catalog and SOURCE SETS that workers TRACE from the deployed gateway code (`MX-s-1..6`); the PRD's "one committed, re-runnable script, not a second tester" is that emitter. `4.0.0_SA_CRO~Z`'s read-only audit (why the page shows Black Diamond on Schwab) is evidence and the seed of the defect rows, which arrive as surprise rows; the issuer classifies Andrew's case first, by measurement, as link, code or display. The FWD-24 half is the battery's own (`MX-h-6`: the `route` record and the `misrouted` and `route_unproven` classes). A source set is a worker's reading of the code: the trace is graded for form and for grounding (the cited line exists and its file names the source), and the issuer reads a sample and checks the live responses against it (a response that names a source the trace does not hold is a FAIL `misrouted`, which is the cross-check). Defect classes go where the PRD sends them: link to NFRA_MCPINDEX, code to `2.0.0_SA_COO~O`, display to `2.0.0_SA_COO~MP`.
10. **Order of the issuer's live runs (v0.19):** opal-data-assets and its eight vendor/firm segments first (windows, source sets, routing table, battery), then the seven integration channels (schwab, blackdiamond, ycharts, portal_index, opal_discover, globgrph, opal_portal), then the buckets etfs, portal-v2, mdpf, harvest, then dynamodb and m365. The worker cells run in parallel and are merged as they finish; only the live runs follow the order. `MX-s-1` (assets, schwab, blackdiamond) is spawned first.
8. **Workers touch only the files named.** The three code cells write the new and named scripts under `workflows/gateway_battery/`; the five data cells write one JSON file in their own deliverables folder; nobody edits `members.yaml`, the catalog rows, the emitter or `app/`. The issuer applies the dispositions through `apply_disposition.py` in ONE commit at the drain and reviews a sample of the reasons.

## R23.5 CHAINS AND FAN-OUT

Eleven independent chains (no edge: each cell is built against the frozen contracts and the issuer's fixtures or the real census; the real data joins them at the drain). Disjoint write sets. Eight slots at once; the last three orders queue on slots that finish early (the same worker continues, context intact). `fanout: 8 of 12 chains, cap 8, reason: cap; MX-k-4, MX-k-5, MX-k-6 and MX-h-6 queue behind MX-h-4, MX-h-5, MX-k-1 and MX-h-1`. Slots ~62..~69 (MX-h-6 was added at v0.19 as a twelfth chain, in order workstream `GATEWAY-ROUTE` because the gate allows ONE issuance per (workstream, round), as round 18 did with RESEARCH-LINKS; the eleven orders issued at c2ca511b36 stand, the four case cells that carry `expect_source` were amended before any spawn).

**Second issuance (v0.19 as admitted):** workstream `GATEWAY-TRACE`, `fanout: 7 of 7 chains, cap 8, reason: the emitter and the six trace cells are independent; slots ~70..~76`. The gate allows one issuance per (workstream, round); GATEWAY-TRACE carries the seven new orders, GATEWAY-ROUTE the re-specified MX-h-6.

## R23.6 BATTERY (base HEAD at the cut; `deliverables/2.0.0_SA_COO~MI/round23/checks/`)

`h_check.py` plus one `.sh` per id: h1.AC1-3, h2.AC1-3, h3.AC1-3, h6.AC1-3, r1.AC1-3 (fixtures under `fixtures/`), s1..s6.AC1-2 (the real census: scope, source shape, vendor vocabulary, cite and grounding), h4.AC1-2, h5.AC1-2 (the REAL census and members, so the check grades the disposition against live repository truth), k1..k6.AC1-2 (the REAL census: scope, sender safety, question quality, ids, and `expect_source` on every reader of a bucket, store, Schwab or Black Diamond channel). Base dry-runs 2026-10-19 ~16:5xZ: every id FAILs at the base (script or file absent). Satisfiability: the issuer's scratch reference implementations (not committed) pass h1.AC1-2, h2.AC1-2, h3.AC1-2, and generated reference files pass h4/h5/k1..k6 AC1-2. One reference bug the check caught before the cut: the members file's top-level `buckets:` list repeats `- tool:` lines, and an applier that edits by text span rewrote the wrong entry; `h2.AC1` plants that trap. The data checks prove form and grounding, not truth: **the issuer reads a sample of the dispositions at the drain** (R23.4 ruling 8).

## R23.7 THE ISSUER'S REAL RUN AT THE DRAIN (not worker cells)

1. Windows: build ROWS from the catalog rows under every channel and run `partition_windows.py` live (read-only listings).
2. Apply: `apply_disposition.py` over the real members with the merged dispositions; review; one commit; coverage over all 14 channels (`refusals` and `explained` stated).
3. Battery E3: run the cases of every channel through the signed-in connector (senders preview only); in-process REFUSED-CORRECT through the installed decision for a read_only and a standard principal; `grade` per channel; every FAIL goes to `2.0.0_SA_COO~O` as a defect cell.
4. E4: re-run the owner sheet's examples, generate the sheet for the first non-owner (the CTO seeds Adam Muller) with the in-process admit check, write it to the default folder, print the count of employees without a live profile beside the count of sheets.
5. `round-close-check`, then the L10 message to the CTO.

## R23.8 WHAT THIS CUT DOES NOT CLAIM

It does not change a grant or a tool, send anything, deliver a sheet to a person, or realize FWD-23, FWD-24 or FWD-25 by itself. The live runs and the numbers come from the drain.
