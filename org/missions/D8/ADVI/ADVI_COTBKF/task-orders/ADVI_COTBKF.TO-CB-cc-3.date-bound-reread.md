# TO ADVI_COTBKF.TO-CB-cc-3.date-bound-reread -- round 81 CB-cc-3: every cell window and built partition range of this project against the earliest client record and the 2012-01-01 floor: which bounds move (nothing is deleted)

<to_id>ADVI_COTBKF.TO-CB-cc-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~160</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>81</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-cc-3` (`decompositions/ADVI_COTBKF_DECOMP.round81.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ of the project's own decompositions, task orders, PRD and local data copies against a law. You change no code and no record of any other seat. Nothing is deleted, narrowed, re-run, built or fetched.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_81_20261013.md` whole, section 2 ruling 3 and section 3 item 3, word for word: "a client account's history starts at its earliest record in the system, and nothing
earlier is read, built or served; nothing before 2012-01-01 under any account; a non-client need takes 365 days before the point of the need. The decomposition's date bounds are re-read against this. A cell whose window begins earlier is narrowed at its
next cut, not re-run." and "each cell window and each built partition range in the decomposition, against the earliest client record and the 2012 floor. Report which bounds move. Nothing is deleted here." The law itself, read from the tree once it
is there (`git show origin/box/dell1:org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_141xZ_BACKFILL_FLOOR_2012_AND_EARLIEST_CLIENT_RECORD.md`, record @82c7c92449; if that ref does not resolve in your tree, say so and quote nothing from it). Then the PRD
`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` (its ENDPOINT, THREAD and every ADDENDUM) and the project's request file `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF-TIER2-15-FUNDS-AS-TRADED-20261012.request.json` (non-security fields only).

**Your item.**

1. **The inventory of windows.** From the PRD, `decompositions/ADVI_COTBKF_DECOMP*.md` (the base and rounds 2 to 81), the open task orders (`python .tools/to-check.py --all --project ADVI_COTBKF`) and the deliverables' manifests, list every DATE WINDOW this project reads, builds or serves: the
   back-fill's own range, each cell's window, each built partition range (the 47 early holdings partitions 2026-04-22 to 2026-06-07; the minted tables' range; the price store's range; the dell1 request window 2020-07-06 to 2026-06-22), and each
   non-client need's window. One row each: `where` (file and line), `kind` (client, non_client, build_range, served_range), `start`, `end`. The denominator of every search (files scanned) is printed beside the count.
2. **The earliest client record.** From the custodian's trades `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/trade_year=*/*.parquet` and the local silver copies the project reads (list the folders you used): the earliest record date over the whole firm; and the COUNT of accounts whose earliest record is
   before 2012-01-01, in 2012 to 2019, in 2020, and after 2020. Counts and dates only; an account is never named and never keyed by id.
3. **The re-read.** For each window of item 1: is its start earlier than the earliest client record of what it reads, or before 2012-01-01, or (for a non-client need) earlier than 365 days before the need? Write `moves` true or false, the `new_start` the law gives, and the rule
   that moves it (`client_earliest_record`, `floor_2012`, `non_client_365`). A window whose start the law cannot set from what is on disk is `not_established`, with the record looked in.
4. **What is built that sits before its bound.** For each built partition range or minted table whose range begins before its law bound, say so with the first date and the count of days before the bound. Nothing is deleted or rebuilt; the narrowing happens at the next cut.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~160/DATE_BOUNDS.json` and a short `.md`. Top-level keys, exactly: `law` (`{"floor", "non_client_days", "record_cited", "resolved_in_tree"}`), `earliest_client_record` (`{"date", "source", "accounts_before_2012", "accounts_2012_to_2019",
   "accounts_in_2020", "accounts_after_2020"}`), `windows` (a list: `{"where", "kind", "start", "end", "moves", "new_start", "rule"}`), `windows_total`, `windows_moving`, `built_before_bound` (a list), `searches` (a list: `{"term", "scope", "files_scanned", "hits"}`), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB81cc3-AC1" cell_refs="CB-cc-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~160/DATE_BOUNDS.json',encoding='utf-8'));w=d['windows'];print('DATE-BOUNDS windows=%d total=%s moving=%s with_a_rule=%d built_before_bound=%d earliest=%s floor=%s'%(len(w),d['windows_total'],d['windows_moving'],sum(1 for x in w if x['rule']),len(d['built_before_bound']),d['earliest_client_record']['date'],d['law']['floor']))"</invocation><expect>DATE-BOUNDS windows=</expect></criterion>
`CB81cc3-AC1` -- every window is listed with its start, end and whether the law moves it; the earliest client record and the account counts are in the record. The issuer reads which bounds move.

<criterion id="CB81cc3-AC2" cell_refs="CB-cc-3" judgment="true"/>
`CB81cc3-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the inventory is complete against its denominator (every decomposition and open order was read); the law is quoted from its record or marked unresolved; a bound is marked moving only by the law's rule;
a bound the disk cannot set is `not_established`; nothing was deleted, narrowed, rebuilt or re-run; no account id or amount appears.

<expected_criteria>CB81cc3-AC1,CB81cc3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry, and no other seat's record.** Everything is local; no AWS call. The commands you run beyond python and git are `python .tools/to-check.py`, `git show` of one ref (a read), and the estate's search tools (`comp-find`, the native Grep tool on a named path).
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`. **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D2-W160-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`),
  APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round81.md</decomp_doc> (round 81), cell `CB-cc-3`.
<owned_cells>CB-cc-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB81cc3-AC1, CB81cc3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~160/ADVI_COTBKF.TO-CB-cc-3.date-bound-reread.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB81cc3-AC1,CB81cc3-AC2` BEFORE the flip. Mechanical: CB81cc3-AC1. A judgment criterion is recorded with status `UNVERIFIABLE-BY-INSTRUMENT` and a `status_reason` that begins `PENDING-ADJUDICATION`, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** whether the law's record resolved in your tree and what it says, quoted; the earliest client record and the account counts by period; the windows and which move, each with its rule; what is built before its bound; every search with its denominator; the `DATE-BOUNDS` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of the project's own records and local copies; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the inventory is checked against a printed denominator (every decomposition and open order); the law is quoted, not paraphrased; a bound moves only by the law's rule; BLIND: a window held only in a seat's message or in a record of another project that this project reads.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-81 analysis @ab1112493b (msg 7078), section 2 ruling 3, section 3 item 3; Andrew-direct 2026-10-13 ~14:1xZ (record @82c7c92449); `3.0.0_SA_CVO` REMEDIATION_v49 @7aceb5d4a1.
