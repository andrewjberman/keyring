# TO ADVI_COTBKF.TO-CB-cc-1.minted-table-consumers -- round 81 CB-cc-1: every consumer of the minted table, found through the dependency graph and then each consumer's own code; and whether the build series after 2026-06-05 feeds anything served

<to_id>ADVI_COTBKF.TO-CB-cc-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~158</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>81</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-cc-1` (`decompositions/ADVI_COTBKF_DECOMP.round81.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ of the dependency graph and of code and configuration in the tree. You change no code. Nothing is built, served, corrected or fetched.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_81_20261013.md` whole (about 60 lines): section 2 rulings 1 and 5, word for word:
"A read of EVERY consumer of the minted table finds none. Use the dependency graph first (CLAUDE.md rule 20), then each consumer's own code or config. A consumer with a page means a
person sees these prices." and "The build series after 2026-06-05 (row: one-day steps on APH, CTVA and KLAC) is read under item 1: does that range feed anything served? If not, it is held;
it is not a defect until it is served." And section 3 item 1: "Graph query, then each consumer's code. Report: consumers, each with whether it serves a page and which dates it reads. 0
consumers needs a positive control: the graph names a known consumer of a sibling table." Then the row in the channel
`ADVI_COTBKF-D2-W155-S1` (the served price errors) and the never-widen record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R27_FWD3_SERVE_COO_HALF.md`.

**What "the minted table" is:** the three tables the builder `commonwealth_fwd3_serve.py` mints: `daily_returns`, `account_day_value`, `month_grades`. Their S3 targets, from the never-widen record:
`s3://opal-data-assets/commonwealth/cottonwood/silver/daily_returns/date=2026-06-23/`, `.../account_day_value/date=2026-06-23/`, `.../month_grades/date=2026-06-23/`. The local copy the earlier
rounds read: `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/` (read only; the file `COO_REFERENCE_fwd3_manifest.json` beside `.scratch/advi_cotbkf/` names the tables and their row counts).

**Your item.**

1. **Is the table served at all?** One read-only listing per prefix above (at most the first 5 keys, `--max-items 5`, through the `.tools/aws` shim): the object count seen for each of the three. State the
   listing's own limit beside the count, so a short listing is not read as a total. Any object found: its key, size and last-modified time.
2. **The graph first** (CLAUDE.md rule 20): pick the call from `org/modules/graph/graph-call-manifest.yaml` (the entries that answer "who reads this S3 path / this table"), QUERY it, never rebuild, and
   print the graph's provenance header and age before you quote an answer. Ask it about each of the three prefixes and about each of the three table names. Quote each call and its output size.
3. **The positive control, before any zero is believed.** Run the SAME graph calls on a sibling table whose consumers are known and name at least one it finds: the cot price store key
   `s3://opal-data-cot/silver/prices/canonical_prices.parquet` (its builder is `data/cot/scripts/gold/build_canonical_prices_v2.py`), or another sibling you name with the reason it is known. If the control
   returns nothing, the graph is blind to that kind of consumer and you say so; a zero on the minted table is then `not_established`, never "none".
4. **Then each consumer's own code or config, found by the estate's tools** (a recursive shell search of the repository is denied by a hook; use `comp-find`, `comp-estate`, `comp-which`, or the native Grep tool on
   a named path): for the three table names and the three prefixes, over the code, the portal, Lambda handlers and infrastructure files. For EVERY hit that reads the minted table: its path and line, what it reads,
   whether it serves a page (a portal route, a Lambda behind a route, a report that goes to a person) and which dates it reads. A hit that only WRITES it (the builder) is listed apart as a writer, not a consumer. The
   denominator of every search (files scanned) is printed beside its hit count; `0 hit(s) across 0 file(s)` is out-of-corpus, not absence (`comp-find --hidden`).
5. **The build series after 2026-06-05** (the build's prices at `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet`, one-day steps on APH 2026-09-04, CTVA 2026-10-02, KLAC 2026-09-04; rows
   `ADVI_COTBKF-D2-W155-S4`): does that range, 2026-06-06 onward, feed anything that is served? Read it from the minted-table builder and from each consumer found in item 4: which dates the minted tables cover, whether any
   served path reads a build price dated after 2026-06-05, and say which. If none does, write that it is HELD, in those words, with the lines that show it.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~158/CONSUMER_READ.json` and a short `.md`. Top-level keys, exactly: `tables` (the three names), `prefixes` (a list of 3:
   `{"prefix", "objects_seen", "listing_limit", "keys"}`), `graph` (`{"provenance", "age", "calls": [{"call", "output_rows"}]}`), `positive_control` (`{"sibling", "found", "consumers_found"}`), `consumers` (a list: `{"name", "path",
   "line", "reads", "serves_page", "dates_read", "evidence"}`), `writers` (a list), `consumer_count` (an integer), `consumers_with_a_page` (an integer), `searches` (a list: `{"term", "scope", "files_scanned",
   "hits"}`), `build_after_2026_06_05_feeds_served` (true, false or `not_established`), `build_after_2026_06_05_reading`, `disarm_fact_a` (one of `no_consumer`, `consumers_found`, `not_established`), `headline`,
   `not_established`.

### ACCEPTANCE

<criterion id="CB81cc1-AC1" cell_refs="CB-cc-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~158/CONSUMER_READ.json',encoding='utf-8'));print('CONSUMER-READ tables=%d prefixes=%d graph_calls=%d control_found=%s consumers=%d with_a_page=%d searches=%d disarm_fact_a=%s build_after_feeds_served=%s'%(len(d['tables']),len(d['prefixes']),len(d['graph']['calls']),d['positive_control']['found'],d['consumer_count'],d['consumers_with_a_page'],len(d['searches']),d['disarm_fact_a'],d['build_after_2026_06_05_feeds_served']))"</invocation><expect>CONSUMER-READ tables=3 prefixes=3</expect></criterion>
`CB81cc1-AC1` -- the three tables and three prefixes are read; the graph's calls and the positive control are in the record; every consumer is listed with its page flag. The issuer reads the consumer count and the disarm fact.

<criterion id="CB81cc1-AC2" cell_refs="CB-cc-1" judgment="true"/>
`CB81cc1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the graph was queried before any code was read and its age was printed; a zero is claimed only with a positive control that found a known consumer; every search carries
its denominator; a writer is not counted as a consumer; `no_consumer` is written only where the control and the code reads support it, and `not_established` otherwise; nothing was built, served or corrected.

<expected_criteria>CB81cc1-AC1,CB81cc1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest, registry or graph.** QUERY the graph; never rebuild it.
- **AWS: READ-ONLY, one `list-objects-v2 --max-items 5` per prefix of the three above, through the `.tools/aws` shim; no get, no write, no delete, no other listing.** If a read is refused, record the exact error; do not try another role.
- **Another firm's data is never opened.** No account id and no account's value: counts, names, paths, lines and dates only.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`. **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull).
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D2-W158-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`),
  APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round81.md</decomp_doc> (round 81), cell `CB-cc-1`.
<owned_cells>CB-cc-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB81cc1-AC1, CB81cc1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~158/ADVI_COTBKF.TO-CB-cc-1.minted-table-consumers.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB81cc1-AC1,CB81cc1-AC2` BEFORE the flip. Mechanical: CB81cc1-AC1. A judgment criterion is recorded with status `UNVERIFIABLE-BY-INSTRUMENT` and a `status_reason` that begins `PENDING-ADJUDICATION`, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** FIRST, if it exists: a consumer that serves a page (name, path, line, dates read). Then: the object count per prefix with the listing's limit; the graph's provenance and age; each graph call and its output; the positive control and what it found; every consumer and writer with path, line, page flag and dates; every search with its denominator; the build-after-2026-06-05 reading; `disarm_fact_a`; every remote read made; the `CONSUMER-READ` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of the graph and of code in the tree; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: three read-only listings on Opal data under the existing role, as the bounds list them; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the graph is queried first and its age printed; a zero needs a positive control that finds a known consumer of a sibling table; a writer is not a consumer; BLIND: a consumer outside the tree (a console-built Lambda, a consumer on another box or in the portal repo's DEV branch not checked out here).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-81 analysis @ab1112493b (msg 7078), section 2 rulings 1 and 5, section 3 item 1; `3.0.0_SA_CVO` REMEDIATION_v49 @7aceb5d4a1.
