# NFRA_MCPINDEX -- decomposition addendum, ROUND 22, workstream GATEWAY (2.0.0_SA_COO~MI)

**archetype:** COORDINATE

Companion to `NFRA_MCPINDEX_DECOMP.md` (ASSETS, rounds 1-21) and `NFRA_MCPINDEX_DECOMP.round18-RESEARCH.md`. One project, one issuer for this round (`2.0.0_SA_COO~MI`, PRD v0.18 Placement). The gate keys the round on (workstream, round), so GATEWAY round 22 collides with nothing. Spec-frozen once issued.

Source: PRD v0.18 addendum at `4b8dcf3b86` (FWD-23, FWD-24, FWD-25; Andrew-direct 2026-10-19 ~14:1xZ, verbatim in the PRD); CTO msg 35988 (denominator is every `/gateway` CHANNEL of all five kinds; PREVIEW-ONLY verdict; FWD-25 proven against the CURRENT grant; senders stay preview-only, Andrew holds call c5c2); the CVO note at `2be4cf2645` (the census prints the count of employees without a live grant beside the count of sheets). **Round 22 builds the thread: ONE channel (`opal-data-harvest`) end to end -- census, indexed, battery, one employee's sheet.** Later rounds enrich channel by channel.

## R22.1 MEASURED STATE (the SERVED data, read 2026-10-19 14:53:37Z)

`deliverables/2.0.0_SA_COO~MI/round22/evidence/breakdown_real_20261019.json` is the body of `admin_gateway_breakdown._compute()` read ON the gateway host (`host_breakdown.sh`, SSM, read-only, under the OG-ap-38 hard guard: oom_score_adj 1000, RLIMIT_AS 1400 MB, 150 s wall; ssm command `a8fc56e4-6021-4da2-b642-c23ef861509d`, status Success, 45660 bytes). `_compute()` is the function behind `GET /api/admin/gateway/breakdown`, the data the `/gateway` page renders; the page itself sits behind an owner sign-in, so this is the page's own data and not a browser read of it (claim: measured, by the served code; the rendered HTML is not read).

| item | measured |
|---|---|
| channels on the page | 7: `opal-data-assets` (bucket, 5 tools, 8 (vendor, firm) segments), `opal-data-etfs` (bucket, 18), `opal-data-harvest` (bucket, 14), `opal-data-mdpf` (bucket, 1), `opal-data-portal-v2` (bucket, 18), `dynamodb` (store, 4), `m365` (native, 43) |
| kinds present | bucket 5, store 1, native 1; integration 0 and undeclared 0 (the gateway places every tool under a declared source today) |
| tools | 103 distinct, 103 tool-channel pairs (each tool sits under exactly one channel today) |
| tools with no catalog `indexes` | harvest 4 (`harvest_get_article`, `harvest_get_published_analysis`, `harvest_list`, `news_for_security`), dynamodb 1, m365 43 |
| grant store | read, 3 principals; holders: `andrew@opalinvest.com` 103 tools, `alyssa@opalinvest.com` 95, `opalbloomberg@opalinvest.com` 95, plus the signed-in population row 90 |
| harvest channel (the thread) | 14 tools, 10 indexed (78 catalog rows name 10 `read_tool`s); all 14 are `member: b` in `tool_index/members.yaml` (13 owner AMGT_HARVST, `news_for_security` unowned) |

The PRD's ground-truth paragraph (319 rows, 192 with `read_tool`, 91 members: 11 (a), 68 (b), 12 (c); 103 served tools) is the repository's; the 103 re-measures equal.

## R22.2 FROZEN CONTRACTS (every cell builds and tests against these; the issuer's fixtures are `deliverables/2.0.0_SA_COO~MI/round22/fixtures/`)

All files are UTF-8 with ASCII content, JSON with `indent=1`, written with `\n` newlines. Python 3.9. `--channel ID` (repeatable) restricts a command to those channel ids; none given means every channel.

**CENSUS** `gateway_surface_census/1`, written by `python workflows/gateway_battery/gateway_census.py census --breakdown FILE --out FILE`:
```
{"schema":"gateway_surface_census/1","claim":"measured","source":"admin_gateway_breakdown body","read_at":<breakdown.read_at>,
 "channels":[{"id","name","kind","min_tier","tools":[sorted names],"segments":[{"vendor","firm","tools"}] (only when the breakdown channel has it)}],   // breakdown order
 "tools":[{"name","access","write_class","data_class","indexes":[sorted],"channels":[sorted ids]}],                                             // sorted by name
 "counts":{"channels","by_kind":{"bucket","store","integration","native","undeclared"},"segments","tools_distinct","tool_channel_pairs","tools_unindexed"}}
```
`by_kind` always carries all five keys. `segments` counts the entries of every channel's `segments`. `tools_unindexed` counts distinct tools whose `indexes` is empty. First stdout line: `CENSUS channels=N bucket=a store=b integration=c native=d undeclared=e segments=S tools=T pairs=P unindexed=U`. Exit 2 (one `ERROR:` line) on a missing or non-JSON file, a body with an `error` key, no `channels` list or an empty one, a channel without `id`, `kind` or a `tools` list, or a tool without `name`.

**GRANTS** `gateway_grants/1`, written by `... gateway_census.py grants --breakdown FILE --out FILE` (same exit 2 rules):
```
{"schema":"gateway_grants/1","claim":"measured","read_at":...,
 "principals":[{"who","how":[sorted distinct],"tools":[sorted union],"channels":[sorted ids where he or she is a holder],"by_channel":{"<id>":[sorted tools held there]}}],   // sorted by who
 "population":{"tools":[sorted union],"channels":[sorted ids]},
 "counts":{"principals","population_tools"}}
```
A holder whose `who` holds neither `@` nor `/` is the population row (the signed-in population); it goes to `population`, never to `principals`. Stdout: `GRANTS principals=N population_tools=K`.

**COVERAGE** (the FWD-23 refusal set), `python workflows/gateway_battery/index_coverage.py --census FILE --members FILE [--pending FILE] --catalog FILE [--channel ID ...] --out FILE`:
- Inputs: the CENSUS; `members.yaml` (top-level `members` list of `{tool, member a|b|c, owner?, reason?, index?, links?}`; the top-level `buckets` list is ignored) plus the optional `pending_members.yaml` (top-level `pending` list, same entry shape; an entry already present in members wins); the catalog's three row sections `silver_datasets`, `portal_datasets`, `harvest_datasets` (rows with `entity`, `bucket`, `read_tool`, optional `retired`; the same sections `round18/discover_buckets.py` reads).
- A row is UNDER a channel when it is not `retired`, carries a `bucket` and `bucket` equals the channel id. A row without a `bucket` is under no channel.
- Refusal classes, each `{"class","channel","subject","detail"}`: `row_no_read_tool` (a row under an in-scope channel whose `read_tool` is absent or not a CENSUS tool; subject = the row's `entity`); `tool_unclassified` (an in-scope tool with no members entry); `tool_member_b` (members says `b`; detail = the `owner`); `tool_c_no_reason` (`c` with an empty `reason`); `tool_a_unlinked` (`a` while the CENSUS `indexes` of the tool is empty); `channel_no_row` (a `bucket` or `store` channel with no row under it and at least one tool that is not `c` with a reason; subject = the channel id); `undeclared_tool` (a tool of an `undeclared` channel that is not `c` with a reason; emitted IN ADDITION to any other refusal for that tool). A tool in several channels is judged once, under the first in-scope channel that holds it.
- Output file: `{"schema":"index_coverage/1","denominator":{"channels","tools","rows"},"refusals":[sorted by (class, channel, subject)]}`. Denominator: in-scope channels; distinct tools in them; rows under them. Stdout: `COVERAGE channels=N tools=T rows=R refusals=K`, then one `REFUSE <class> <channel> <subject>` line per refusal (at most 200 lines; the file holds all). Exit 0 iff K is 0, 1 if K > 0, 2 on unreadable input.

**CASES** `gateway_battery_cases/1`: `{"schema":...,"cases":[{"case_id","tool","question","args":{},"expect":"nonempty|empty|refused|preview","source_hint"}]}`. `question` is the plain-English example a sheet may show.

**RESULTS** `gateway_battery_results/1`: `{"schema":...,"run":{"principal","transport","started_at"},"results":[{"case_id","status":"ok|error|refused|preview","rows":int|null,"as_of":str|null,"error_text":str|null,"sent":bool,"source_check":{"instrument","value","agrees":bool}|null}]}`. Recorded by the signed-in session that ran the cases (R22.4 ruling 1).

**BATTERY** `python workflows/gateway_battery/tool_battery.py`:
- `plan --census F --cases F [--channel ID ...] --out F` writes `{"schema":"gateway_battery_plan/1","tools_in_scope":[...],"cases":[the cases of in-scope tools],"tools_without_case":[...]}`; stdout `PLAN tools=T cases=C tools_without_case=K`; exit 0 iff K is 0 (the file is written either way).
- `grade --census F --cases F --results F [--channel ID ...] --out F` writes `gateway_battery_graded/1`: `{"run":<the results' run>,"cases":[{"case_id","tool","question","verdict","fail_class"}],"tools":[{"tool","verdict","fail_class","cases":[ids]}] (sorted by tool),"counts":{PASS,EMPTY-CORRECT,REFUSED-CORRECT,PREVIEW-ONLY,FAIL} (over TOOLS),"case_counts":{same keys over cases},"preview_only":[tool names],"fails":[{"tool","fail_class"}]}`. Stdout `GRADE tools=T PASS=a EMPTY-CORRECT=b REFUSED-CORRECT=c PREVIEW-ONLY=d FAIL=e`, then `PREVIEW-ONLY TOOLS: <comma list or empty>`. Exit 0 iff FAIL is 0.
- Case verdict: `expect nonempty`: status `error` -> FAIL `tool_error`; `refused` -> FAIL `unexpected_refusal`; `ok` with rows > 0 -> PASS only when `source_check.agrees` is true (`source_check` null -> FAIL `source_unchecked`; agrees false -> FAIL `source_disagrees`); any other `ok` (rows 0 or null) -> FAIL `unexpected_empty`. `expect empty`: `ok` with rows 0 and `agrees` true -> EMPTY-CORRECT (agrees missing or false -> FAIL `source_unchecked`); `error` -> FAIL `tool_error`; any other -> FAIL `unexpected_nonempty`. `expect refused`: status `refused` -> REFUSED-CORRECT, else FAIL `not_refused`. `expect preview`: `sent` true -> FAIL `sent`; status `preview` -> PREVIEW-ONLY; else FAIL `tool_error`. A planned case with no result -> FAIL `not_run`. An in-scope tool with no case -> tool FAIL `no_case`.
- Tool verdict: FAIL if any of its cases FAIL (its `fail_class` is the first failing case's, in case order); else the first present of PASS, EMPTY-CORRECT, REFUSED-CORRECT, PREVIEW-ONLY.
- `plant --cases F --results F --tool NAME --out F` copies RESULTS with every case of that tool set to status `error`, `rows` null, `error_text` `planted`, `source_check` null (the PRD's planted broken tool).

**SHEET** `python workflows/gateway_battery/cheatsheet.py gen --census F --grants F --graded F --employee EMAIL --connect FILE --out DIR [--roster FILE]`:
- Exit 2 with `NO LIVE GRANT: <email>` when the employee is not in GRANTS `principals`; no file is written.
- Writes `<DIR>/<local-part>.md` and `<DIR>/<local-part>.examples.json` (`[{"tool","question","case_id"}]`, in sheet order). The sheet: the `--connect` file verbatim first, a blank line, `Tested <run.started_at>.`, then for each CENSUS channel (census order) in which the employee is a holder (`by_channel`): `## <channel name> (<kind>)` and, for each of the tools she or he holds there (name order), `### <tool>`. Under it: `NOT YET TESTED` when the tool has no graded verdict; `KNOWN ISSUE: the last test of this tool failed (<fail_class>)` for a FAIL tool; `PREVIEW-ONLY: the send leg is not exercised` for a PREVIEW-ONLY tool; and one `- <question>` line per graded case of that tool with verdict PASS or EMPTY-CORRECT (never for a FAIL tool, and never for a REFUSED-CORRECT or PREVIEW-ONLY case). A tool held in two channels is listed under both.
- Stdout: `SHEET employee=E channels=C tools=T examples=X` (channels listed; DISTINCT tools; example lines), then with `--roster` (one email per line) `ROSTER employees=R with_live_grant=S without=R-S` (S counts roster emails that are GRANTS principals), without it `ROSTER not supplied (claim: absent)`.
- Deterministic: the same inputs give the same bytes; nothing reads a clock.

## R22.3 THE CELLS

| cell | what | write set | risk | serves | state |
|---|---|---|---|---|---|
| `MX-g-1` | The census reducer and the grants extractor (R22.2 CENSUS, GRANTS) | `workflows/gateway_battery/gateway_census.py`, `.../tests/test_gateway_census.py` | LOCAL | FWD-23, FWD-24, FWD-25 | CUT this issuance |
| `MX-g-2` | The FWD-23 coverage gate and its refusal set (R22.2 COVERAGE) | `workflows/gateway_battery/index_coverage.py`, `.../tests/test_index_coverage.py` | LOCAL | FWD-23 | CUT this issuance |
| `MX-g-4` | The FWD-24 battery: plan, grade, plant (R22.2 CASES, RESULTS, BATTERY) | `workflows/gateway_battery/tool_battery.py`, `.../tests/test_tool_battery.py` | LOCAL | FWD-24 | CUT this issuance |
| `MX-g-5` | The FWD-25 sheet generator (R22.2 SHEET) | `workflows/gateway_battery/cheatsheet.py`, `.../tests/test_cheatsheet.py` | LOCAL | FWD-25 | CUT this issuance |

`MX-g-3` (harvest `member b` to `a`) is not cut: see R22.4 ruling 3.

The issuer's own acts at the drain (R22.7) are the REAL run of each outcome on the harvest channel.

## R22.4 RULINGS (the issuer rules inside its own decomposition, rule 7)

1. **The battery's call path is a signed-in connector session.** FWD-24 asks for a live call through the SERVED gateway by a real signed-in principal, and the gateway admits a person only through the Microsoft sign-in; no unattended credential exists (`tool_battery.py` therefore never calls the gateway). The script plans the calls (`plan`), a signed-in session makes them through the connector and writes RESULTS, and the script grades (`grade`). The first run is made by this seat's own session, which is signed in as `andrew@opalinvest.com`; the RESULTS `run.principal` says so, and every figure in it is labelled by that principal's grant. A host-side regression runner is not built this round. **Said to the CTO as a reading of "one committed, re-runnable script": the script is re-runnable; the calls it plans need a signed-in session each time.**
2. **The census is the data the page renders.** The page is owner-only; `_compute()` on the host is the same function under the page (R22.1). The raw body is committed; `gateway_census.py census` reduces it. Integration and undeclared kinds are 0 today and the reducer prints that, so a channel of those kinds that appears later is counted without a code change.
3. **The harvest `member b` to `a` repair is NOT cut this round, and the reason is measured.** An `a` member needs `depth` and `freshness` claims; `tool_index/measure.py` reads only `channels[].artifacts[]` rows and no `harvest_datasets` row, and the harvest rows hold `contract.freshness` but no depth. Reclassifying the 10 indexed harvest tools therefore needs a measure.py extension plus S3 listing reads, and the four unindexed tools need catalog rows that do not exist. The coverage gate run on the real harvest channel at the drain (R22.7 act 3) prints exactly that list, and it is the round-22 enrichment item `E1` for the CTO's analysis. FWD-23 is NOT claimed realized for harvest by this round.
4. **FWD-25 is proven for `andrew@opalinvest.com`**, the principal whose session runs the examples (PRD v0.18: every example is re-run as that principal and reads PASS). His current grant is all 103 tools; the sheet follows the grant read at the census. The roster for the CVO's count of employees without a live grant is the Entra directory list supplied at the drain; absent that file the generator prints `claim: absent` and the figure is not stated.
5. **Senders stay preview-only** (CTO msg 35988; open call c5c2 is Andrew's). The cases for a sending tool use `expect preview`; a result with `sent` true is a FAIL.
6. **Cheat-sheet delivery**: `upload_text_to_site` to a folder named `Opal MCP Cheat Sheets` on the Opal SharePoint site; the issuer resolves the site and drive at the drain and may be redirected by Andrew. No sheet is delivered until the FWD-25 proof passes.
7. **No worker touches the gateway, AWS, the catalog, `members.yaml`, the emitter or `app/`.** The four cells write only the new `workflows/gateway_battery/` files named above.

## R22.5 CHAINS AND FAN-OUT

Four chains, no edge between them: each cell builds against the frozen contracts and the issuer's fixtures, so none needs another's output (the real data joins them at the drain). Write sets are disjoint (one script and one test file each). `fanout: 4 of 4 chains, cap 8, reason: four independent scripts built against frozen contracts; no edge`. Slots ~58 (`MX-g-1`), ~59 (`MX-g-2`), ~60 (`MX-g-4`), ~61 (`MX-g-5`).

## R22.6 BATTERY (base HEAD at the cut; `deliverables/2.0.0_SA_COO~MI/round22/checks/`)

Twelve criteria, three per cell, one runner `g_check.py` and a one-line `.sh` per id. Base dry-runs 2026-10-19 (every script and test file is absent at the base): `g1.AC1`..`g5.AC3` all FAIL as expected, rc 1. Satisfiability: the issuer's reference implementations (scratch, not committed, not given to a worker) pass `g1.AC1`, `g1.AC2`, `g2.AC1`, `g2.AC2`, `g4.AC1`, `g4.AC2`, `g5.AC1`, `g5.AC2` (the three pytest criteria need the worker's tests). Two bugs the dry-run found and fixed before the cut: an arm expecting rc 2 passed at the base because python's own rc for a missing script is 2 (the runner now returns 98 for an absent script), and a negative arm passed vacuously on a missing sheet (it now requires the sheet file). The planted arms are inside the criteria: `g2.AC2` (five refusals incl. the PRD's channel planted with no row), `g4.AC2` (the PRD's planted broken tool plus eight further fail classes), `g5.AC1`/`g5.AC2` (the employee without a bucket's grant gets no tool of it; an employee without a live grant gets no sheet).

## R22.7 THE ISSUER'S REAL RUN AT THE DRAIN (not worker cells)

1. Census: `host_breakdown.sh` (done, 14:53Z) then `gateway_census.py census` on the real body, committed as `GATEWAY_SURFACE_CENSUS_20261019.json` with its per-kind counts, and `grants`.
2. Coverage on the real catalog: `index_coverage.py` over the whole census, then over `--channel opal-data-harvest`; the harvest refusal set is the `E1` list.
3. `opal_discover` per bucket and store channel through the served gateway (this seat's connector), recorded.
4. Battery on the harvest channel: `plan`, the signed-in calls with a second-instrument source check per case, `grade`, `plant` (the planted arm must read FAIL).
5. Sheet for `andrew@opalinvest.com`; every example re-run through the connector; the roster count line; the result committed.
6. `python .tools/round-close-check.py --project NFRA_MCPINDEX --round 22`, then the L8 packet and the L10 message to `1.0.0_SA_CTO`.

## R22.8 WHAT THIS CUT DOES NOT CLAIM

It does not claim FWD-23 for harvest (ruling 3), FWD-24 for any channel but harvest, FWD-25 for any employee but one, or that a host-side regression battery exists. It changes no grant, no catalog row, no tool and no access, and it sends nothing.
