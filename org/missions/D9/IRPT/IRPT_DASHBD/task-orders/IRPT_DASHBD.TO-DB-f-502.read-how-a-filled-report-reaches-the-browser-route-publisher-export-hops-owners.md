# TO IRPT_DASHBD.TO-DB-f-502 -- the SERVE-PATH READ: how a filled performance report could reach the browser from gold today (the read route, the platinum publisher, any report object, the export render path), the hops still missing with an owner and a risk class each, and the route to propose; a read, nothing written

<to_id>IRPT_DASHBD.TO-DB-f-502</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~502</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>114</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, the four-workstream ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md`; overlap rule 3: F-SHIP reads the filled document and never builds one) | **Rows:** IRPT_DASHBD-D2-W502-S<k> | **Decomp cell:** `DB-f-502` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R114_F.md`) | **outcome_ref:** FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-502` (branch `wk-IRPT_DASHBD-502`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~502/`. Never push; never commit the workspace `portal` gitlink (you have no portal work). This is a READ of repository files and git history: no AWS call of any kind, no network, no vendor call, no secret read. Any real client, household or account id and any client figure is never written in the repo, a row or your report.

**Why.** FWD-21 asks for one household at each firm rendered from Opal gold on DEV, on the Performance tab and as the export. The report components exist, and a sibling cell (`DB-f-501`) is mounting them in the tab behind a reader that asks a PROPOSED route for a client's filled report. Nothing yet shows how a filled report would be PUBLISHED and SERVED. What exists, measured by the issuer at the cut: the served read route `irpt-reporting-read` (owner IRPT_BCKEND workstream `~P2`) serves a per-account `manifest` and `series` and a per-client `summary` as files the dashboard publisher wrote to platinum; a text search of `lib/research/api` for the route's paths found nothing, so the route is NOT in that tree; the only producers of a filled report are the private sample builders (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~175/build_sample_inflection_r110.py` and its siblings) and the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (`document.filled_report`). The export is rendered by a server host from a frozen series version (`performance_source`, IRPT_BCKEND.TO-IB-pr-301), per `portal/src/pages/InvestorReporting/export/resolveBundle.ts` and `tabs/reporting/ReportingTab.tsx` (`buildDashboardExportTarget`). This cell finds where each of those lives, says what is missing and who owns each missing hop.

**The cell (`DB-f-502`).**
1. **Find the route.** Locate the code of the served read route for the reporting files: the handler that answers `/api/scoped/investor-reporting/reporting/{account_id}/{manifest|series}` and `/reporting/client/{client_id}/summary`. Use `comp-find --files '<term>' <folder> --limit 20` with the terms `irpt-reporting-read`, `reporting/client` and `summary`, and `comp-which "which code serves the investor reporting manifest and series routes"`; read the file you find. Record its path, the line that decides the path template, the path template, and which files it serves. Never `head` a census; print the denominator the tool gives.
2. **Find the publisher.** Locate the code that WRITES the platinum `manifest`, `series` and client `summary` objects (the dashboard publisher; the issuer's lead is `data/assets/scripts/` under `irpt_reporting`; use `comp-find`). Record its path and the line that writes one object kind, and in words how it addresses its objects (through `lib/opal_naming.py address()`, or otherwise) and how often it runs (a schedule, an event, or by hand: say which and cite the file; if you cannot tell, say `absent` with the reason).
3. **Is there a report object?** Answer two booleans with words: does any code publish a FILLED REPORT object to platinum (`exists_in_platinum`), and does any code that could produce one exist beyond the private sample builders (`producer_exists`). A producer that exists only as a sample builder writing to a private folder is `producer_exists` false.
4. **The export path.** Read how the export is rendered today and say in words where the document is built (in the browser, or on a server host), what it reads (the retained report, or the series by `performance_source`), and whether anything in it reads a filled report today (`reads_report_today`). Record the file and the line that decides it.
5. **The hops.** List the hops that would carry ONE household's filled report from gold to BOTH the tab and the export, in order, each with: `hop` (1, 2, 3 ...), `what` (words), `owner` (a serial or workstream that owns the write surface: for example `2.0.0_SA_COO~D2` for the contract and the sample builder, `2.0.0_SA_COO~P2` for the read route and the platinum publisher, `2.0.0_SA_COO~F2` for the portal, an AE seat for a deploy; name an owner from the files, never a guess: where none can be named write the word `UNOWNED`), `risk` (`LOCAL`, `SERVED` or `WORLD` by the issuer's rule: a code or test change is LOCAL; a served data path or a PROD promotion is SERVED; a deploy, a grant, a key or a schedule is WORLD), and `exists_today` (true or false). At least 4 hops; the first hop is the builder of the filled report from gold and the last is the portal.
6. **The proposed route.** Say whether the summary route's shape (`/reporting/client/{client_id}/summary`) can carry a sibling `/reporting/client/{client_id}/report` with the same scope check (the viewer must cover every account the document names), citing the code line that does the summary's scope check; give the `path_template` you would propose and the words of what the route owner must add.
7. **Record** `RD_REPORT_SERVE_PATH_R114.json` in your folder with EXACTLY these fields: `as_of` (ISO date of the read); `route` {`file`, `line`, `path_template`, `serves` (list of words), `claim`}; `publisher` {`file`, `line`, `words`, `claim`}; `report_object` {`exists_in_platinum`, `producer_exists`, `words`, `claim`}; `hops` (the list of step 5); `export_path` {`file`, `line`, `words`, `reads_report_today`, `claim`}; `proposed_route` {`path_template`, `words`}; `reads` {`s3_reads` 0, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}; and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. Every `claim` is one of `measured` (you read the line), `inferred`, `held`, `absent` (not found, with the reason in `words`/`serves`; an unfound item is `absent`, never invented). A `file` is an existing repo path with an INTEGER `line` whose text holds the thing the record says it holds (the checker reads that line: the route line must hold `manifest`, `series`, `summary` or `reporting`; the publisher line `manifest`, `series`, `summary` or `platinum`; the export line `export`, `bundle`, `render`, `performance_source` or `print`). No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage` or `path_template` field.

<criterion id="DBF114-2-AC1" cell_refs="DB-f-502"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r114/p114_ship.py" . DBF114-2-AC1</invocation><expect>DBF114-2-AC1 PASS</expect></criterion>
`DBF114-2-AC1` -- `RD_REPORT_SERVE_PATH_R114.json` has exactly the form of step 7; each cited file exists and each cited line holds the token class its field names; `hops` has at least 4 entries numbered from 1, each with an owner, a risk class in the set and a boolean `exists_today`; `report_object` carries both booleans and words; every claim is in the four-word set; the reads block is all zero, the four flags are false and no run of 8 or more digits stands outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DBF114-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every code file, the contract, the portal, the routes, the publisher, the issuer's check.
- **A READ.** Nothing is deployed, applied, published, pushed or changed outside your folder; no AWS call (the route and the publisher are read from their code, not from the cloud); no network. Where only the cloud could answer a question, the answer is `absent` with that reason, never a guess.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a thing is not found, the record says `absent` and what you searched; a zero is never read as "does not exist" without the tool's printed denominator beside it. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W502-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~502/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-502.read-how-a-filled-report-reaches-the-browser-route-publisher-export-hops-owners.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R114_F.md</decomp_doc> round 114, workstream ~F2, cell `DB-f-502`.
<owned_cells>DB-f-502</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF114-2-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~502/IRPT_DASHBD.TO-DB-f-502.read-how-a-filled-report-reaches-the-browser-route-publisher-export-hops-owners.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF114-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the route's file, line and path template; the publisher's file, line and cadence in words; the two booleans of the report object; where the export document is built and whether it reads a filled report; the hops in order with owner, risk and `exists_today`; the proposed route; anything you saw off-task (as row ids). No real id and no client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the cell reads the route's code.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; a cadence is read from code.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DBF114-2-AC1 FAILS at base (no record) and the record form is exercised by the checker's self-test.
lane: the <paths> block IS the grant.
</preflight>
