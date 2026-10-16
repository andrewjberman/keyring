# TO IRPT_DASHBD.TO-DB-c-29 -- round 149: the 49 Financial FWD-10 coverage census (the two gold tables) and the labelled TEST READ of every published 49 Financial series through the page's own reader and performanceView; read-only S3; counts only; no identifier, key or value recorded; no portal edit

<to_id>IRPT_DASHBD.TO-DB-c-29</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~420</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md` Move 2 (msg 8741: "`~C2`: IRPT_DASHBD FWD-10 ... Cottonwood first ... Then 49F and Inflection") | **Rows:** IRPT_DASHBD-D2-W420-S<k> | **Decomp cell:** `DB-c-29` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 18) | **outcome_ref:** FWD-10 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-420`); run everything from its root unless a step says the portal. Its nested `portal/` is a PORTAL worktree (branch `wk-IRPT_DASHBD-420-portal`) cut from the portal commit `34a6baf8657bb166676dc3b8c3eec97ee8d3e585` (portal DEV), which holds the page's reader and the unreported-days sentence. You edit NO portal file and make NO portal commit. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~420/`; your files, rows and this order's evidence commit in the workspace repo with `.tools/safe-commit.sh` and your author line (`0.9.0_WK_IRPT_DASHBD~420 <0.9.0_WK_IRPT_DASHBD~420@opal.agent>`; never `--no-verify`). Never push. `node_modules` in the portal is a LINK to the main checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`.

**You make read-only AWS calls through python `boto3` and nothing else:** S3 `list_objects_v2` and `get_object`, region `us-east-1`, on exactly two things: (1) the date partitions of the two gold tables `account_return_daily` and `holdings_performance_daily`, whose prefixes you build with `lib/opal_naming.py` `address("irpt", "49financial", "gold", <table>, "date=2000-01-01")` cut at `<table>/` (list the partition folders; open no data file); (2) the published series prefix `address("irpt", "49financial", "platinum", "reporting", "account=X", "series.json.gz")` cut at `account=` (list it, and `get_object` only the `series.json.gz` objects). No put, delete, create, invoke, update or secret read; no Terraform. A read that is refused is recorded as refused (its words). **This is a TEST READ, not a serve or a production run.** The objects are real client series: you record COUNTS and DATES only. You never write, print, commit or put in any file an account id, an object key, a household id or a series value (an object key's account folder IS an account id: print no key, name no file after one, and print no raw listing). The downloaded objects go in ONE temporary folder OUTSIDE every repository (`mktemp -d`), under running-number file names, and you delete the files you downloaded (and that folder) when you are done.

**Why.** PRD FWD-10: "A person can always tell what they are looking at: where the data starts, which trading days the source did not report, and how current the data is." Round 145 measured Cottonwood. This cell measures 49 Financial the same way, so every sentence the page says about a 49 Financial account rests on a count: where its gold history starts, whether any trading day is absent from it, how current the published series are, and what the page prints for them today.

**The page's code (read it, do not edit it).** In the portal worktree: `src/pages/InvestorReporting/dashboard/seriesContract.ts` exports `readSeries(value)` (returns `{ ok: true, document }` or `{ ok: false, refusal }`); `src/pages/InvestorReporting/dashboard/DashboardPerformance.tsx` exports `performanceView(series, selection)` (pure; returns `notes`, the sentences) and the `WindowSelection` type. Round 148's worker wrote a harness for the Cottonwood publish; its two scripts are committed at `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~419/read_publish_r148.py` (download and python counts) and `.../page_read_r148.ts` (the page's side). Read them and COPY them into your folder as `read_publish_r149.py` and `page_read_r149.ts`, then change them to this prefix, these fields and these names (never edit the originals).

**The cell (`DB-c-29`).**
1. **The gold census.** For each of the two tables list the date partitions (`date=YYYY-MM-DD/` folders; a partition counts as present when its prefix holds at least one object, counted by a listing and no data read). With `lib/trading_calendar.py` (`trading_days_between(a, b)` is inclusive; run with plain `python`, NOT `-I`, because it needs the user site packages) compute for each table: `partitions`, `first_date`, `last_date`, `absent_trading_days` (the sorted list of every trading day between first and last inclusive with NO partition, `[]` when none) and `runs` (the maximal runs of consecutive absent trading days as `[{"start", "end", "trading_days"}]`, `[]` when none).
2. **The python truth of the published series.** List the series prefix (paginate until the listing ends), count the objects by kind (`series.json.gz`, `manifest.json`, anything else), download every `series.json.gz` into the temporary folder and, over those documents (gunzip, `json.loads`), compute and keep these EXACT key names: `objects_series`, `objects_manifest`, `objects_other`, `docs_total`, `docs_parse_ok`, `pair_present` (documents carrying BOTH `unreported_trading_days` and `unreported_trading_days_basis`), `pair_absent`, `nonempty_lists`, `total_listed_days`, `max_list_len`, `income_all_null_docs` (a non-empty `income` array null on every entry), `income_any_number_docs` (any entry a number), `income_claim_present_docs` (the key `income_claim` present), `history_scope_counts` (map of each `history_scope` value to its document count), `first_data_date_min` and `first_data_date_max` (the smallest and largest `first_data_date` as strings), `as_of_counts` (map of each `as_of` value to its document count), `day_quality_day_totals` (map of each value of the `day_quality` arrays to the TOTAL number of days across all documents) and `return_basis_day_totals` (the same for `return_basis`). Also keep, as an extra field `first_data_date_after_gold_first_day`, the number of documents whose `first_data_date` is later than `account_return_daily`'s `first_date` from step 1. Use a thread pool of at most 32 for the downloads.
3. **The page's side.** With a bun script (run it with `bun run` from the portal worktree so the portal's path aliases resolve) read the same downloaded documents: `readSeries(parsed)`; when `ok`, `performanceView(document, <the custom selection from document.first_data_date to document.as_of>)` inside `try`. Keep these counts, EXACT names: `read_ok`, `read_refused`, `performance_view_threw`, `accounts_printing_unreported_sentence` (documents whose notes hold a note containing `not reported by the source`), `sentences_total`, `sentence_n_mismatch` (documents where the number that sentence starts with differs from the length of the document's `unreported_trading_days`, or where a document with an empty or missing list printed one, or a document with a non-empty list printed none), `income_coerced_to_zero` (documents where the document `readSeries` returns holds a `0` at an income index where the raw document held `null`), and, informational: `accounts_printing_returns_from` (a note beginning `Returns from`), `accounts_printing_excluded_days_note` (a note containing `no measurable return`) and `accounts_printing_day_quality_note` (a note starting with a number and `day`/`days` and a colon). The script prints these counts as one JSON line and nothing else.
4. **Record** `FWD10_49F_CENSUS_R149.json` in your folder with exactly: `label` ("TEST READ -- not a serve, not a production run"), `read_utc` (`date -u +%FT%TZ`), `firm_scope` ("49financial"), `gold` (an object keyed by the two table names, each `{"partitions", "first_date", "last_date", "absent_trading_days", "runs"}`), `series_truth` (the step-2 object with its extra field), `page` (the step-3 counts), `reads` {`s3_list_calls`, `s3_get_calls`, `writes` 0, `invokes` 0}, `claim` "measured", `ids_recorded` false, `pushed` false, `deployed` false. Anything you cannot establish is `NOT_ESTABLISHED` with the reason, never guessed. Also write `FWD10_49F_CENSUS_R149.md` (at most 50 lines): in words, for each of the three FWD-10 questions (where the data starts, which trading days were not reported, how current), what a person looking at a 49 Financial account would need to be told, which of the page's words say it today (read the `performanceView` notes and `coverageWords.ts`), and anything that looks wrong to you, with no identifier or value. Then delete the downloaded files and their folder.

<criterion id="DBC150-1-AC1" cell_refs="DB-c-29"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r149/p150_bcw.py" . DBC150-1-AC1</invocation><expect>DBC150-1-AC1 PASS</expect></criterion>
`DBC150-1-AC1` -- the record's `gold` section equals a FRESH listing-and-calendar measurement the checker makes for both tables (partitions, first and last date, the exact absent trading days and the runs), and the record is labelled a TEST READ with claim `measured`. Base: FAIL (no record).

<criterion id="DBC150-1-AC2" cell_refs="DB-c-29"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r149/p150_bcw.py" . DBC150-1-AC2</invocation><expect>DBC150-1-AC2 PASS</expect></criterion>
`DBC150-1-AC2` -- the record's `series_truth` equals a FRESH read of the published series prefix, and the page-side counts agree: every document read with none refused or threw, the accounts printing the unreported-days sentence equal the documents with a non-empty list, no printed count differs from its list and no income was coerced to zero. Base: FAIL (no record).

<criterion id="DBC150-1-AC3" cell_refs="DB-c-29"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r149/p150_bcw.py" . DBC150-1-AC3</invocation><expect>DBC150-1-AC3 PASS</expect></criterion>
`DBC150-1-AC3` -- the hygiene: no account identifier token anywhere in the worker's folder, the record reports zero writes and invokes and `ids_recorded`, `pushed` and `deployed` false, no downloaded object is left in the folder, the note is at most 50 lines, and only the worker's folder, the channel and this order changed from the branch point. Base: FAIL (no record).

<expected_criteria>DBC150-1-AC1, DBC150-1-AC2, DBC150-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. The portal is read, never edited. Everything else is read, never edited, including the round-148 harness you copy.
- **Reads and writes.** Reads: repo files, `git show`, the portal worktree, and the read-only S3 calls named above. Writes: the files in `<paths>` and the temporary folder you delete. No AWS write, no invoke, no Terraform, no push, no vendor call, no secret read. The 49 Financial data is read for counts only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A page-side count you cannot produce (the script will not run) is `NOT_ESTABLISHED` with the error words and a row, never a guess.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W420-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES; no identifier or value in a row. Commit with `.tools/safe-commit.sh` (never `--no-verify`); run its gates in the background and wait for them. ASCII only in anything you write. Leave this order's `<status>` as it is; the issuer flips it. Name your proof instance exactly `IRPT_DASHBD.TO-DB-c-29.49-financial-fwd10-coverage-census-and-page-read.proof_of_spec.json`.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~420/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-29.49-financial-fwd10-coverage-census-and-page-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 18, cell `DB-c-29`.
<owned_cells>DB-c-29</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC150-1-AC1, DBC150-1-AC2, DBC150-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~420/IRPT_DASHBD.TO-DB-c-29.49-financial-fwd10-coverage-census-and-page-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC150-1-AC1,DBC150-1-AC2,DBC150-1-AC3` BEFORE you report (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the counts (gold first and last days and absent days per table; series documents; those printing each note; the as_of spread; the day-quality totals); the list and get call counts; row ids. No identifier, key or value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: read-only measurements and a record; nothing is created, planned, applied or written to any service.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: only S3 list and get calls on two named prefixes of the 49 Financial bucket; no grant is made or changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC150-1-AC1 and AC2 re-measure the S3 plane themselves and compare.
</preflight>
