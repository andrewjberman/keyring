# TO ADVI_COTBKF.TO-CB-cd-2.route-read -- round 82 CB-cd-2: is the second hop LIVE: the served minted objects read, and the route ARD -> gold account_return_daily -> reporting-publish -> dashboard followed through code AND deployed configuration, to say whether any person can see these prices

<to_id>ADVI_COTBKF.TO-CB-cd-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~162</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>82</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-cd-2` (`decompositions/ADVI_COTBKF_DECOMP.round82.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ of code, of deployed configuration (describe and get of NAMED resources only) and of three served objects. You change no code. Nothing is built, served, corrected or fetched from a vendor.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_82_20261013.md` whole, section 2 ruling 1 and section 3 item 2, word for word: "W155-S1 disarms on a READ, not a correction, if the read shows no person can see these prices. The CVO's remedy offers exactly that: 'a read that the second hop reaches no page'.
So the cell reads whether the route ARD -> gold `account_return_daily` -> reporting-publish -> dashboard is LIVE, from code and from the deployed config. Not live: W155-S1 disarms. Live: this seat cuts the correction under a never-widen pair." and "The route read for W155-S1: the served minted objects are read, not the scratch copy."
Then the round-81 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~158/CONSUMER_READ.json` (the two code readers, the second hop in code, the sentence "Planned, not applied" at `infra/aws/lambda/ci/lambda-source-map.json:6485`), the stage record `deliverables/0.9.0_WK_ADVI_COTBKF~159/STAGE_READ.json`
and the channel rows `ADVI_COTBKF-D2-W155-S1`, `-D2-W158-S2` and `-D2-W158-S3`.

**The route, as round 81 found it in code (you re-read every hop yourself and cite file and line; do not copy):** the ARD adapter `data/assets/scripts/silver/commonwealth_account_return_daily.py` (reads the three minted tables at `:221-226`), its output into gold `account_return_daily`, then `infra/aws/lambda/investor-reporting/reporting-publish/handler.py`, then
`portal/src/pages/InvestorReporting/dashboard/seriesContract.ts:4` and the dashboard page that renders it.

**Your item.**

1. **The served objects, read.** Of each of the three minted objects, ONE `get-object` (the prefixes are `s3://opal-data-assets/commonwealth/cottonwood/silver/{daily_returns,account_day_value,month_grades}/date=2026-06-23/`; each holds one object, 1,651,055 / 54,246,028 / 421,751 bytes, last modified 2026-10-09T12:41Z, per round 81; list with `--max-items 5` to get the key first): the key, the size, the row count, the date range, the
   columns, and for APH, CTVA and HON on the days `deliverables/0.9.0_WK_ADVI_COTBKF~159/STAGE_READ.json` chose: the served close and the ratio to the vendor Close and to the price paid (counts of accounts as a COUNT; never an account value). Say whether the served objects agree with the scratch copy `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/` on those rows.
2. **The route, hop by hop, from code:** for each hop, the file and line that reads the previous hop's output (the object key or table name), and the line that writes its own. A hop whose input name does not match the previous hop's output name is a BREAK; say so.
3. **The route, hop by hop, from DEPLOYED configuration (named resources only):** (a) does the gold `account_return_daily` object exist for this firm (one `head-object` or a one-key listing of the key the adapter writes, from the code); (b) is the `reporting-publish` Lambda deployed (`lambda get-function-configuration` of the one function name the code or `lambda-source-map.json` names; its last-modified and its environment variable NAMES, not values);
   (c) is a read route to it registered (the API Gateway route or CloudFront behaviour the infrastructure files name; one `get` of that named resource, or the Terraform that creates it and whether it is applied: say how you know it is applied or not); (d) does the dashboard page call that route in the portal's `DEV` and `PROD` source (read the files, do not run the portal); (e) the sentence at `lambda-source-map.json:6485` read in place with its neighbours: what does "Planned, not applied" refer to.
4. **The verdict, one of:** `route_live` (every hop deployed, a route registered, the page calls it), `route_not_live` (at least one hop is absent in deployment and you name which and the evidence), or `not_established` (say which hop could not be read and why). A `route_not_live` needs the absent hop proven absent by a read that would have found it (a positive control: the same read on a hop known to exist).
5. **The page question, answered plainly:** can a person (a partner-firm or client login, or Opal staff) see a price served from the minted tables today? `yes` (name the page and login class), `no` (the hop that breaks it), or `not_established`.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~162/ROUTE_READ.json` and a short `.md`. Top-level keys, exactly: `objects` (a list of 3: `{"key", "bytes", "rows", "first_date", "last_date", "columns"}`), `agrees_with_scratch` (true, false or `not_established`), `rows_read` (a list: `{"ticker", "day", "served_close", "ratio_to_vendor", "ratio_to_price_paid"}`),
   `hops` (a list: `{"hop", "reads_file_line", "writes_file_line", "name_matches_previous", "deployed", "evidence"}`), `planned_not_applied_reading`, `positive_control` (`{"hop", "found"}`), `route_verdict`, `a_person_can_see_these_prices`, `page_or_break`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB82cd2-AC1" cell_refs="CB-cd-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~162/ROUTE_READ.json',encoding='utf-8'));print('ROUTE-READ objects=%d rows_read=%d hops=%d hops_with_deployment_evidence=%d verdict=%s person_can_see=%s control_found=%s'%(len(d['objects']),len(d['rows_read']),len(d['hops']),sum(1 for h in d['hops'] if h['evidence']),d['route_verdict'],d['a_person_can_see_these_prices'],d['positive_control']['found']))"</invocation><expect>ROUTE-READ objects=3</expect></criterion>
`CB82cd2-AC1` -- the three served objects are read, every hop of the route carries its evidence, and the verdict, the page answer and the positive control are in the record. The issuer reads whether the row disarms or the correction is the next cell.

<criterion id="CB82cd2-AC2" cell_refs="CB-cd-2" judgment="true"/>
`CB82cd2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the served objects, not the scratch copy, are the evidence; every hop is read in code AND in deployment; `route_not_live` is claimed only for a hop proven absent by a read that has a positive control; "Planned, not applied" is read in place with its neighbours, not taken as the answer; the page answer follows
from the hops and not from the sentence; nothing was built, served or corrected.

<expected_criteria>CB82cd2-AC1,CB82cd2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest, registry, graph or infrastructure.**
- **AWS: READ-ONLY, through the `.tools/aws` shim, of NAMED resources only:** `list-objects-v2 --max-items 5` on the three prefixes and one `get-object` per minted object; one `head-object` or one-key listing for the gold object; `lambda get-function-configuration` of the one function; one `get` of the one named route resource. No other listing, no write, no delete, no serve. If a read is refused, record the exact error; do not try another role.
- **Another firm's data is never opened.** No account id and no account's value: counts, tickers, dates, prices and ratios only.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`. **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull).
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- Searches go through the estate's tools (`comp-find`, `comp-estate`, the native Grep on a named path); a recursive shell search of the repository is denied by a hook and is not retried another way. The graph is queried, never rebuilt.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D2-W162-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`),
  APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round82.md</decomp_doc> (round 82), cell `CB-cd-2`.
<owned_cells>CB-cd-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB82cd2-AC1, CB82cd2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~162/ADVI_COTBKF.TO-CB-cd-2.route-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB82cd2-AC1,CB82cd2-AC2` BEFORE the flip. Mechanical: CB82cd2-AC1. A judgment criterion is recorded with status `UNVERIFIABLE-BY-INSTRUMENT` and a `status_reason` that begins `PENDING-ADJUDICATION`, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. You flip your own order `<status>` to `complete` in the commit that carries the proof instance, as the earlier rounds' workers did.
</proof_of_spec>

**REPORT:** FIRST, if `a_person_can_see_these_prices` is `yes`: the page, the login class and the dates of the prices shown. Then: the three objects (key, bytes, rows, dates); whether they agree with the scratch copy; the rows read for APH, CTVA and HON; each hop with its code lines and its deployment evidence; the reading of "Planned, not applied"; the verdict and the positive control; every remote read made; the `ROUTE-READ` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of code, named resources and three served objects; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: read-only calls on Opal data and named resources under the existing role, as the bounds list them; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the served objects, not the scratch copy; every hop read in code AND in deployment; a hop is "absent" only by a read with a positive control; "Planned, not applied" is read with its neighbours; BLIND: a route built outside the tree (a console-made behaviour or Lambda) and a consumer in the portal repo's branch not checked out here.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-82 analysis @ea59dfcdec (msg 7196), section 2 ruling 1, section 3 item 2; `3.0.0_SA_CVO` REMEDIATION_v50 @43b340c673 (row D2-W155-S1's remedy).
