# TO IRPT_DASHBD.TO-DB-c-3 -- the READERS of the three COTTONWOOD gold tables (`account_dim`, `account_return_daily`, `holdings_performance_daily`) and the FALLBACK CALENDAR's equality with the package for 2026-06-23 to 2026-10-13; a read; counts and words only; nothing written

<to_id>IRPT_DASHBD.TO-DB-c-3</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~402</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>114</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (B-CW is this workstream); the two items `deliverables/0.9.0_WK_IRPT_DASHBD~166/COTTONWOOD_RESUME_PACKET.md` section 8 left unestablished | **Rows:** IRPT_DASHBD-D2-W402-S<k> | **Decomp cell:** `DB-c-3` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 1) | **outcome_ref:** FWD-11, FWD-15 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-402`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~402/`. Never push. Counts, paths and words only in the repo, a row or your report; an account number, a client or household id, a name or a figure is never recorded.

**Why.** Whether a Cottonwood account page can show a return depends on which served code reads which Cottonwood gold table; the resume packet recorded "no reader found" for `account_return_daily` but could not grade it, because `comp-pipescript postdeps` refused the producer's id in all four trees. And the packet's calendar for the catch-up range is the fallback, whose equality with the package was not run. This cell settles both from the repo.

**The cell (`DB-c-3`).**
1. **Readers.** For EACH of `account_dim`, `account_return_daily`, `holdings_performance_daily`: find the served or scheduled CODE that READS the table from the Cottonwood gold (the Lambda handlers under `infra/aws/lambda/investor-reporting/`, the portal API under `lib/research/api/`, the gold scripts under `data/assets/scripts/gold/`). Use `comp-find '<table>' <one named folder> --files --limit 20` per named folder (the rail denies a blind repo search) and read each candidate file. A READER is a file that opens the table's gold prefix for reading. A writer, a checker, a record and a test are NOT readers; list them separately in `non_readers` (a count and the paths, not an explanation). Record per table `readers` ([{`file`, `line_words`}]: the repo path and a short phrase for how it reads), `reader_count`, `claim` ("measured" if you read every candidate file, else "inferred" with the unread folders named in `none_words`), and `none_words` (words; required when `reader_count` is 0: say which folders you searched and what the denominator was).
2. **Calendar.** `lib/tests/test_nyse_fallback_equals_package.py` compares the generated NYSE fallback to `pandas_market_calendars`. Try to run it with `python -I` from the repo root. `calendar.ran` is true only if the comparison ran; then `compared_days` and `mismatches` are the integers it reports. If the package is absent on this box (it was on 2026-10-14), `ran` is false and `not_runnable_reason` states that in words. In either case record `range` as `["2026-06-23","2026-10-13"]`, `source` as the string `lib.trading_calendar.calendar_source()` returns, and `fallback_years` (the first and last year the fallback covers, from `FALLBACK_FIRST_YEAR` and `FALLBACK_LAST_YEAR`). Do NOT install a package.
3. **Record** `READERS_AND_CALENDAR_R114.json` in your folder with exactly: `claim` ("measured"); `tables` {the three table names, each {`readers`, `reader_count`, `non_readers` {`count`, `paths`}, `claim`, `none_words`}}; `calendar` {`ran`, `compared_days`, `mismatches`, `not_runnable_reason`, `range`, `source`, `fallback_years`}; `basis_words` (words: which folders you searched and read); `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `aws_writes` 0}; `pushed` false; `deployed` false.

<criterion id="DBC114-3-AC1" cell_refs="DB-c-3"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r114/p114_bcw.py" . DBC114-3-AC1</invocation><expect>DBC114-3-AC1 PASS</expect></criterion>
`DBC114-3-AC1` -- the record names exactly the three tables; each recorded reader file exists in the repo and names its table; a table with zero readers carries `none_words` and a claim of absent or inferred; `reader_count` equals the list; when the calendar comparison did not run the package is in fact absent now and a reason is given; the range is the stated one; no write is recorded. Base: FAIL (no record).

<expected_criteria>DBC114-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files; `comp-find` per named folder; the calendar test. Writes: the record in your folder. No AWS call is needed or allowed, no install, no deploy, no push, no vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W402-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~402/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-3.cottonwood-gold-table-readers-and-fallback-calendar-equality.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 1, cell `DB-c-3`.
<owned_cells>DB-c-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC114-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~402/IRPT_DASHBD.TO-DB-c-3.cottonwood-gold-table-readers-and-fallback-calendar-equality.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC114-3-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; per table the reader count and the reader files; whether the calendar comparison ran and its result or reason; row ids. No account number, client or household id, name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read record; nothing is wired, changed or deleted.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC114-3-AC1 FAILS at base (no record) and its file-exists and package-absent arms are exercised on the worker's record.
</preflight>
