# TO IRPT_DASHBD.TO-DB-c-27 -- round 148: the labelled TEST READ of the real Cottonwood series publish through the page's own reader and performanceView; read-only S3; counts only; no value, key or identifier is recorded; no portal edit

<to_id>IRPT_DASHBD.TO-DB-c-27</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~419</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>148</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's condition on the Cottonwood publish pair (msg 9022: "your cell (a) may read the prefix after Act 4, labelled as a test read") and `~D2` msg 9108 (the Cottonwood series are published at `irpt/cottonwood/platinum/reporting/`, 939 accounts, 1,878 objects) | **Rows:** IRPT_DASHBD-D2-W419-S<k> | **Decomp cell:** `DB-c-27` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 17) | **outcome_ref:** FWD-10 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-419`); run everything from its root unless a step says the portal. Its nested `portal/` is a PORTAL worktree (branch `wk-IRPT_DASHBD-419-portal`) cut from the portal commit `dd417a1055e5754182391e79cb941aeab07abfbe`, which holds the page's reader and the unreported-days sentence you test. You edit NO portal file and make NO portal commit. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~419/`; your files, rows and this order's evidence commit in the workspace repo with `.tools/safe-commit.sh` and your author line (`0.9.0_WK_IRPT_DASHBD~419 <0.9.0_WK_IRPT_DASHBD~419@opal.agent>`; never `--no-verify`). Never push. `node_modules` in the portal is a LINK to the main checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`.

**You make read-only AWS calls through python `boto3` and nothing else:** S3 `list_objects_v2` and `get_object` on the ONE prefix `s3://opal-data-cottonwood/irpt/cottonwood/platinum/reporting/` (region `us-east-1`). No put, delete, create, invoke, update or secret read; no Terraform. A read that is refused is recorded as refused (its words). **This is a TEST READ, not a serve or a production run.** The objects are real client series: you record COUNTS only. You never write, print, commit or put in any file an account id, an object key, a household id or a series value (the key's account folder IS an account id: do not print a key, and do not name a file after one). The downloaded objects go in ONE temporary folder OUTSIDE every repository (`mktemp -d`), under a file name that is a running number, and you delete the files you downloaded (and that folder) when you are done.

**Why.** PRD FWD-10 cell (a) prints the trading days the source did not report. It was built and graded against fixtures made by the contract's writer (round 147). The Cottonwood series are now published. The CTO allowed one labelled test read of them through the page's own code, to see that the page reads every real document and prints its sentence, before any account's screen does.

**The page's code (read it, do not edit it).** In the portal worktree: `src/pages/InvestorReporting/dashboard/seriesContract.ts` exports `readSeries(value)` (returns `{ ok: true, document }` or `{ ok: false, refusal }`); `src/pages/InvestorReporting/dashboard/DashboardPerformance.tsx` exports `performanceView(series, selection)` (pure; returns `notes`, the sentences) and the `WindowSelection` type (a custom selection is a start and end date; read the type for its exact shape). The round-147 test `src/pages/InvestorReporting/__tests__/irpt-dashbd/fwd10-unreported-days.test.tsx` shows how both are called. The sentence this cell reads for is `<N> trading day(s) not reported by the source: <dates>.`

**The cell (`DB-c-27`).**
1. **Download.** With a python script in your folder (`read_publish_r148.py`; it prints counts only, never a key), list the prefix (paginate until the listing ends), and download every `series.json.gz` and `manifest.json` into the temporary folder as `<n>.series.json.gz` and `<n>.manifest.json`, `<n>` a running number. Count your list calls and get calls.
2. **The python truth.** Over the downloaded series documents (gunzip, `json.loads`), compute and keep: `objects_series`, `objects_manifest`, `objects_other` (the listing's objects that are neither), `docs_total`, `docs_parse_ok`, `pair_present` (documents carrying BOTH `unreported_trading_days` and `unreported_trading_days_basis`), `pair_absent`, `nonempty_lists` (pair present and the list non-empty), `total_listed_days` (the sum of the list lengths), `max_list_len`, `income_all_null_docs` (a non-empty `income` array that is null on every entry), `income_any_number_docs` (any entry a number), `income_claim_present_docs` (the document has the key `income_claim`), `history_scope_counts` (a map of each `history_scope` value to its document count) and, over the manifests, `calendar_source_counts` (a map of each `calendar_source` value, `"ABSENT"` when the key is missing, to its count). These must be the exact key names; the checker re-measures the same fields.
3. **The page's side.** With a bun script in your folder (`page_read_r148.ts`; run it with `bun run` from the portal worktree so the portal's path aliases resolve; it imports `readSeries`, `performanceView` and the `WindowSelection` type from the portal worktree by relative path) read the same downloaded series documents. For each: `readSeries(parsed)`; when `ok`, `performanceView(document, { custom selection from document.first_data_date to document.as_of })` inside `try`; from the returned `notes` take those that contain `not reported by the source`. Keep these counts: `read_ok`, `read_refused`, `performance_view_threw`, `accounts_printing_sentence` (documents whose notes hold exactly one such sentence), `sentences_total`, `sentence_n_mismatch` (documents where the number the sentence starts with differs from the length of that document's `unreported_trading_days`, or where a document with an empty or missing list printed a sentence, or where a document with a non-empty list printed none), `income_coerced_to_zero` (documents where the document `readSeries` returns holds a `0` at an income index where the raw document held `null`). The script prints these counts as one JSON line and nothing else.
4. **Record** `TEST_READ_R148.json` in your folder with exactly: `label` ("TEST READ -- not a serve, not a production run"), `read_utc` (`date -u +%FT%TZ`), `prefix` ("irpt/cottonwood/platinum/reporting/"), `python_truth` (the step-2 object), `page` (the step-3 counts), `reads` {`s3_list_calls`, `s3_get_calls`, `writes` 0, `invokes` 0}, `claim` "measured", `ids_recorded` false, `pushed` false, `deployed` false. Anything you cannot establish is `NOT_ESTABLISHED` with the reason, never guessed. Also write `TEST_READ_R148.md` (under 30 lines): in words, what the page does with the real publish (how many accounts print the sentence, the longest list, what the income and the history scope read as) and anything that looks wrong to you, with no identifier or value. Then delete the downloaded files and their folder.

<criterion id="DBC149-1-AC1" cell_refs="DB-c-27"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r148/p149_bcw.py" . DBC149-1-AC1</invocation><expect>DBC149-1-AC1 PASS</expect></criterion>
`DBC149-1-AC1` -- the record's `python_truth` equals a FRESH read-only measurement the checker makes over the same prefix, and the page-side counts agree: `read_ok` equals the documents read with none refused, none threw, the accounts printing the sentence equal the accounts with a non-empty list, no printed count differs from its list's length and no income was coerced to zero. Base: FAIL (no record).

<criterion id="DBC149-1-AC2" cell_refs="DB-c-27"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r148/p149_bcw.py" . DBC149-1-AC2</invocation><expect>DBC149-1-AC2 PASS</expect></criterion>
`DBC149-1-AC2` -- the hygiene: no account identifier token anywhere in the worker's folder, the record reports zero writes and invokes and `ids_recorded`, `pushed` and `deployed` false, no downloaded object is left in the folder, and only the worker's folder, the channel and this order changed from the branch point. Base: FAIL (no record).

<expected_criteria>DBC149-1-AC1, DBC149-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. The portal is read, never edited. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files, `git show`, the portal worktree, and the read-only S3 calls named above. Writes: the files in `<paths>` and the temporary folder you delete. No AWS write, no invoke, no Terraform, no push, no vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A page-side count you cannot produce (the script will not run) is `NOT_ESTABLISHED` with the error words and a row, never a guess.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W419-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES; no identifier or value in a row. Commit with `.tools/safe-commit.sh` (never `--no-verify`); run its gates in the background and wait for them. ASCII only in anything you write. Leave this order's `<status>` as it is; the issuer flips it.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~419/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-27.test-read-of-the-published-cottonwood-series-through-the-page.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 17, cell `DB-c-27`.
<owned_cells>DB-c-27</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC149-1-AC1, DBC149-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~419/IRPT_DASHBD.TO-DB-c-27.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC149-1-AC1,DBC149-1-AC2` BEFORE you report (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the counts (documents, accounts printing the sentence, longest list, income and history-scope readings); the list and get call counts; row ids. No identifier, key or value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: read-only measurements and a record; nothing is created, planned, applied or written to any service.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: only S3 list and get calls on one prefix; no grant is made or changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC149-1-AC1 re-measures the S3 plane itself and compares.
</preflight>
