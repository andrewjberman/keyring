# NFRA_MCPINDEX -- decomposition addendum, ROUND 24, workstream GATEWAY (2.0.0_SA_COO~MI)

**archetype:** COORDINATE

Companion to `NFRA_MCPINDEX_DECOMP.round23-GATEWAY.md`. One issuer, one round, ONE issuance (workstream GATEWAY, round 24). Spec-frozen once issued.

Source: the CTO's round-23 analysis `ledger/ROUND_ANALYSIS.round23.md` (`1.0.0_SA_CTO~Z`, 2026-10-20 ~12:3xZ), PRD v0.19 @7c42c0c743, and the round-23 evidence under `deliverables/2.0.0_SA_COO~MI/round23/evidence/`. Round 23 closed at 19 of 19 orders, MAY-CLOSE; its drain left FWD-23 at 13 MISROUTED tools and 36 member-(b) refusals, FWD-24 at PASS 38, EMPTY-CORRECT 4, FAIL 85, FWD-25 at one sheet of 17.

Nothing in this round touches the gateway, a grant, the live `DATA_CATALOG.yaml`, or sends anything. Every worker cell writes local files; the live reads, the battery runs, the catalog and members edits and the SharePoint write are the issuer's drain acts (R24.5).

## R24.1 INPUTS (all under `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/`, read-only to workers)

- `round22/evidence/GATEWAY_SURFACE_CENSUS_20261019_v2.json` -- the census (14 channels, 127 tools).
- `round23/evidence/BATTERY_GRADED_20261019.json` -- the graded battery (`tools[]` with `tool`, `verdict`, `fail_class`, `cases`); `cases_all_20261019.json` and `results_all_20261019.json` beside it.
- `round23/evidence/ROUTING_TABLE_20261019.json` -- `gateway_routing_table/1`, tools with `source_set`, `pairs` (`row`, `verdict` ROUTED|MISROUTED|UNRESOLVED), `verdict`, `class`.
- `round23/evidence/COVERAGE_after_apply_20261019.json` -- `index_coverage/1`, `refusals[]` (`class` tool_member_b, `channel`, `subject` = the tool, `detail` = the named owner).
- the source sets `deliverables/0.9.0_WK_NFRA_MCPINDEX~71..~76/source_sets_*.json` (`source_sets/1`: per tool, sources with `kind`, `bucket`, `prefix`, `vendor`, `cite`).
- the catalog `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` and `workflows/atom_decomposition/tool_index/members.yaml` (read-only).
- `workflows/gateway_battery/` -- the merged scripts (`routing_table.py`, `tool_battery.py`, `index_coverage.py`, `partition_windows.py`, `cheatsheet.py`) and `tests/`.

## R24.2 THE CELLS (one per class of the analysis; seven independent chains)

| cell | analysis item | class | deliverable | slot |
|---|---|---|---|---|
| `MX-w-1` | 1 source_unchecked (35) | code | `workflows/gateway_battery/source_compare.py` + `tests/test_source_compare.py` | ~77 |
| `MX-w-2` | 2 not_run (32) | data | `deliverables/0.9.0_WK_NFRA_MCPINDEX~78/not_run_plan.json` | ~78 |
| `MX-w-3` | 3 misrouted link (10) | data | `deliverables/0.9.0_WK_NFRA_MCPINDEX~79/link_fixes.json` | ~79 |
| `MX-w-4` | 4 the 7 remaining FAILs | data | `deliverables/0.9.0_WK_NFRA_MCPINDEX~80/fail_attribution.json` | ~80 |
| `MX-w-5` | 5 coverage (36 member b) | data | `deliverables/0.9.0_WK_NFRA_MCPINDEX~81/coverage_rows.json` | ~81 |
| `MX-w-6` | 6 generated serves | code | edit `workflows/gateway_battery/routing_table.py` + `tests/test_routing_serves.py` | ~82 |
| `MX-w-7` | 7 FWD-25 sheets | code | edit `workflows/gateway_battery/cheatsheet.py` + `tests/test_cheatsheet_batch.py` | ~83 |

Item 8 (re-run the battery and the routing script on opal-data-assets after batch16 is live, 2026-10-21 06:00Z) is time-gated and is the issuer's drain act, not a cell. Write sets are disjoint: no two cells write the same file; nobody edits `members.yaml`, the catalog rows, `emit_catalog_v02.py` or `app/`.

## R24.3 FROZEN CONTRACTS

**W1 SOURCE COMPARE** `python workflows/gateway_battery/source_compare.py --census F --routing F --results F --cases F --out F [--fake F]`. Writes `gateway_source_compare/1`: `{"schema","tools":[{"tool","case_ids":[...],"source":{"kind","bucket","prefix"}|null,"instrument":str,"answer_as_of":str|null,"source_dates":[sorted date strings seen under the source],"agrees":true|false|null,"reason":str}],"counts":{"tools","agrees","disagrees","unreadable"}}`, tools sorted by name, one entry per census tool that has at least one RESULT with `status` ok. Source choice: the tool's `source_set` entry of kind `s3` whose bucket/prefix overlaps (one prefix starts with the other) an `answer_source` string of the result; else the first `s3` source of the set in file order; no `s3` source -> `source` is the first source of the set and `agrees` null with a `reason` that names its kind ("store", "integration" or "graph") and says it is not read here. For an `s3` source the instrument lists keys under bucket+prefix (list only, never a get) by importing the listing helper of `partition_windows.py`; `source_dates` are the `YYYY-MM-DD` / `date=YYYY-MM-DD` / `YYYYMMDD` tokens found in the listed keys. `agrees` is true when the result's `as_of` date is among `source_dates`, false when `source_dates` is non-empty and it is not, and null with reason when the result has no `as_of` or the listing has no date token ("undated"), or the listing is empty. `--fake` is a JSON `{"<bucket>|<prefix>": [page, ...]}` of key lists in place of S3 (the format `partition_windows.py --fake` already reads). Same input, same bytes. A tool in the results that is not in the census, or a missing routing entry, exits 2. Stdout `SOURCE tools=T agrees=A disagrees=D unreadable=U`; exit 0 iff `D` is 0.

**W2 NOT-RUN PLAN** `not_run_plan.json`, schema `gateway_not_run_plan/1`: `{"schema","plans":[{"tool","plan":"run"|"preview-only"|"c","case_ids":[existing case ids still to run],"new_cases":[full case objects of `gateway_battery_cases/1`],"test_send":null|{"case_id","to":"tester mailbox"|"tester chat"},"reason":str,"cite":"<path>:<line>"}]}`. One entry for each tool graded `not_run` in `BATTERY_GRADED_20261019.json`, exactly those tools, once each. Rules: `run` lists every planned case of the tool (from `cases_all_20261019.json`) that has no result in `results_all_20261019.json`, plus `new_cases` for a case whose input was a placeholder, with a real input read from the catalog rows or the gateway code (no `<...>` token in any argument, no email address, no account number); a sender tool (census `write_class` a real class, or `opal_data_refresh_upload`, or `schwab_prepare_download`) is never `run`: it is `preview-only` with its preview case ids and, if the CTO's rule applies (open call c5c2: ONE real message to the tester's own mailbox or chat), a `test_send` naming the one case; a tool that cannot run without a write elsewhere is `preview-only` and says which write; `c` gives the reason the tool reads no data row, with a `cite` that exists. Every `reason` is ASCII, at least eight words.

**W3 LINK FIXES** `link_fixes.json`, schema `gateway_link_fixes/1`: `{"schema","fixes":[{"tool","remove":[row ids],"add":[row ids],"keep":[{"row","reason"}],"basis":str,"cite":"<path>:<line>"}]}`. One entry for each tool the routing table grades `MISROUTED` with class `link` (10 tools), exactly those. Every MISROUTED pair of the tool is in `remove` or in `keep` (with a reason that names the source that justifies leaving the link); `remove` and `keep` hold only that tool's MISROUTED pairs; `add` holds only catalog rows (entities of `silver_datasets`, `portal_datasets`, `harvest_datasets`) that overlap an `s3` source of the tool's source set and that the tool does not already link. After applying the fixes to the tool's linked rows, every remaining pair is ROUTED against the tool's source set by the link rule of `routing_table.py` (same bucket; one prefix starts with the other).

**W4 FAIL ATTRIBUTION** `fail_attribution.json`, schema `gateway_fail_attribution/1`: `{"schema","items":[{"tool","fail_class","cause":"code"|"catalog"|"battery"|"data","owner":str,"evidence":str,"fix":str}]}`. One item for each of the 7 tools graded `tool_error` (3), `source_disagrees` (2), `unexpected_empty` (1) or `route_unproven` (1) in `BATTERY_GRADED_20261019.json`, exactly those; `fail_class` equals the graded class. `evidence` is `<path>:<line>` of a file in the repository or `<results file>#<case_id>`, and must resolve (the file exists, the line exists, or the case id is in the file). A `code` cause names `2.0.0_SA_COO~O` as owner; a `catalog` cause names `2.0.0_SA_COO~MI`; a `battery` or `data` cause names the producing project code. `fix` is at least eight ASCII words.

**W5 COVERAGE ROWS** `coverage_rows.json`, schema `gateway_coverage_rows/1`: `{"schema","items":[{"tool","owner","disposition":"row"|"c","row":null|{"entity","bucket","prefix","vendor","firm"},"reason":str,"cite":"<path>:<line>"}]}`. One item for each refusal of `COVERAGE_after_apply_20261019.json` (36 tools, class tool_member_b), exactly those; `owner` equals the refusal's `detail`. `row`: a catalog row the tool reads, `entity` unique (not an entity of the catalog and not repeated), `bucket` and `prefix` overlapping an `s3` source of the tool's source set, `vendor` one of the catalog's vendors plus opal, ycharts, microsoft, bloomberg, other; `firm` a string. `c`: the tool reads no data a row can describe, `reason` and an existing `cite`.

**W6 SERVES** In `routing_table.py`, `--serves-out` writes the TRACED set: a catalog row contributes its (vendor, firm) to a tool only when some `s3` source of the tool matches the row by bucket and prefix (the link rule) AND the row's `vendor` equals the source's `vendor`. A source that matches rows of a vendor it does not carry (a coarse or empty prefix over a bucket) contributes nothing for them. The unresolved pair rule (a non-matching source contributes (the source's vendor, `unresolved`)) is unchanged. `added` and `removed` are computed as before, so `removed` is non-empty when the catalog claims a pair the trace does not reach. Round-23 behavior of `ROUTING` (counts, verdicts, classes, the three `--plant` modes) is byte-identical on the round-23 fixtures and the live table.

**W7 SHEETS BATCH** `python workflows/gateway_battery/cheatsheet.py gen-all ... --out-dir D` writes one sheet per roster person and one examples JSON beside it, prints `SHEETS people=P written=W legacy=L placeholder=H`, writes only under `--out-dir`, never delivers, sends or uploads, and gives byte-identical files on two runs. A person with a live profile gets the tools the installed decision admits (as `gen` does); a person with NO profile is on the LEGACY path and gets the legacy admit set; a person with no recorded role gets the placeholder relevance line; no person without a profile is listed a `client_*`, Schwab or Black Diamond tool. **AMENDED at the cut (fork finding on the real inputs; the order's section 1 is the exact specification and wins where it differs):** the roster file is a plain list of emails, so roles and the placeholder flag come from a `--relevance` file the issuer builds from the CRO map; the legacy admit set is read from the `--tier-decisions` file (`round23/evidence/TIER_DECISIONS_20261019.json`) and not hard-coded (the CRO map shows the legacy path also reads MDPF and the person's own Microsoft 365 tools); sheets narrow by relevance buckets (Andrew's yes on calls 5ccb and 8cdf), with the m365 and other buckets kept for every person.

## R24.4 RULINGS (issuer, 2.0.0_SA_COO~MI)

1. Cell ids `MX-w-1..7` (the letter w is unused); slots ~77..~83; fan-out `7 of 7 chains, cap 8`.
2. Every cell is `<risk>LOCAL</risk>` with at most three mechanical criteria; the checks are `deliverables/2.0.0_SA_COO~MI/round24/checks/w_check.py` plus one `.sh` per criterion, base dry-run FAIL, scratch reference passes.
3. W3 and W5 produce JSON the issuer applies at the drain through the existing members/catalog writers (R24.5); a worker never edits `members.yaml` or the catalog.
4. W7 reads the legacy admit set from the tier-decisions evidence; the issuer confirms it against `app/` at the drain before any sheet is written to the folder.
5. The routing note of the analysis binds every message of this round: slugs and decisions go to `1.0.0_SA_CTO~Z`.

## R24.5 THE ISSUER'S REAL RUN AT THE DRAIN (not worker cells)

1. W3, W5: apply the merged JSON to `members.yaml` (links, rows, (c) reasons) in ONE commit; coverage over the 14 channels; routing re-run with the new links.
2. W1: run `source_compare.py` live (list-only) over the merged results; the 35 `source_unchecked` tools take their verdict from it.
3. W2: run the planned cases with at most two gateway calls at a time (battery concurrency rule of the analysis); the one test send per sender tool only if the plan names it and Andrew's c5c2 yes stands; grade again.
4. W4: each `code` item goes to `2.0.0_SA_COO~O` as a defect row; each `catalog` item is fixed in step 1.
5. W6: regenerate `GATEWAY_SERVES`; write it into the catalog only once it removes a pair (a separate sign-off if the catalog is served output).
6. W7: generate the 17 sheets into the default folder named in PRD v0.18; sending a sheet is held for Andrew's word.
7. After batch16 is live (2026-10-21 06:00Z): re-run the battery and the routing script on opal-data-assets.
8. `round-close-check --round 24`, then the L10 slug to `1.0.0_SA_CTO~Z`.

## R24.6 WHAT THIS CUT DOES NOT CLAIM

It does not change a grant or a tool, send anything, deliver a sheet, or realize FWD-23, FWD-24 or FWD-25 by itself. The live runs and the numbers come from the drain.
