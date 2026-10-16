# TO IRPT_DASHBD.TO-DB-c-23 -- WHAT THE PAGE SAYS ABOUT COVERAGE TODAY (FWD-10, round 145): for the four ACCEPT cases and the eight coverage members, the code path from the data to the sentence on screen (or its absence), read from the repo and the portal, with file and line evidence; no write, no run

<to_id>IRPT_DASHBD.TO-DB-c-23</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~415</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>145</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** Andrew's go through the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md` Move 2 (msg 8741: `~C2`: IRPT_DASHBD FWD-10, Cottonwood first; write surface "the coverage readers and `MethodAndSources` (surface row S07), the coverage vocabulary") | **Rows:** IRPT_DASHBD-D2-W415-S<k> | **Decomp cell:** `DB-c-23` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 14) | **outcome_ref:** FWD-10, FWD-8 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-415`); run everything from its root; its nested `portal/` is a portal worktree cut from the portal DEV head named in your prompt. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~415/`. Never push. **You read files only: no AWS call, no run of any build, no portal dev server, no network.** No client value is read or written.

**Why (the outcome).** PRD FWD-10 (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`, read the FWD-10 block, the constraints C-COVERAGE and C-HONESTY and surface row S07 first): "A person can always tell what they are looking at: where the data starts, which days could not be measured, when a figure is a fallback, and how current the data is." ACCEPT: "a partial-history account, a day that could not be measured, a fallback day and a window before the news data starts are each explained on screen in a sentence; no state is hidden inside an average." Before any build, you read what the page and its readers say today for each, so the build cells are cut on facts.

**What to read.** The portal page and its readers: `portal/src/pages/InvestorReporting/tabs/reporting/MethodAndSources.tsx` (its lines 32-63 are named in the PRD as the wrong label) and the files in the same `tabs/reporting/` folder and the page's data hooks and readers that carry or show a `coverage`, `status`, absent-day or fallback state (find them by reading the imports of the page and of `MethodAndSources.tsx`, a named file at a time); the backend side that produces the state the page receives: `infra/aws/lambda/investor-reporting/performance/holdings_gold.py` (the label constants near line 259), `data/assets/scripts/gold/irpt_reporting/filled_report_values.py` and the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` where they name coverage, absent kinds or fallback; and the closed vocabulary in the PRD (C-COVERAGE: `FULL`, `PARTIAL_HISTORY`, `NO_LOTS`, `FLOW_UNRECONCILED`, `UNCLASSIFIED_HOLDINGS`, `SOURCE_LAG`, `FEE_RAIL_UNUSED`, `MISSING_HISTORY`).

**The cell (`DB-c-23`).** Write ONE record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~415/COTTONWOOD_SCREEN_COVERAGE_READ_R145.json` and ONE short note `.../COTTONWOOD_SCREEN_COVERAGE_READ_R145.md` (under 50 lines). The record carries:
1. `cases`: an object keyed by `partial_history_account`, `day_not_measured`, `fallback_day`, `window_before_news_data`, each `{"verdict", "words", "evidence"}` where `verdict` is one of `EXPLAINED` (the page shows a sentence for it where the number is), `NOT_EXPLAINED` (the state reaches the page or its reader but no sentence is shown), `NOT_REACHED` (the state is not carried to the page at all), `WRONG_LABEL` (the page says something false about it) or `NOT_ESTABLISHED`; `words` says in two or three sentences what the page does today; `evidence` is a non-empty list of `{"file", "line", "text"}` with `file` a repo-relative path (a `portal/...` path is the nested portal worktree), `line` the 1-based line number, and `text` an exact substring (at least 12 characters) of that line or of one of the two lines either side of it.
2. `label`: `{"wrong_label_present" (true when `MethodAndSources.tsx` still contains the text `Time-weighted, net of fees`), "file", "line", "text", "words" (what the PRD's C-LABEL says the label must say instead, one sentence from the PRD)}`.
3. `members`: an object keyed by the eight C-COVERAGE members, each `{"produced_by" (file and line where the backend or contract assigns it, or null), "sentence_on_screen" (the file and line where the page maps it to a sentence, or null), "words"}`.
4. `cottonwood_specific`: `{"adapter_reads_coverage" (true or false: does `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_report_reader.py` or `cottonwood_account_dim.py` produce a `coverage` value (the account_dim adapter assigns `FULL`, `UNCLASSIFIED_HOLDINGS` or `PARTIAL_HISTORY`), "evidence" (the same `{file, line, text}` form), "words"}`.
5. `reads`: `{"files_read" (a count), "writes": 0, "aws_calls": 0, "runs": 0}`; `claim` = `"inferred"` (the verdicts are readings of code, not runs); `pushed` = false; `deployed` = false.
Anything you cannot establish from the files is `NOT_ESTABLISHED` with the reason, never guessed.

**Do NOT**: run any code, test or build; call AWS or the network; edit any file outside your folder, the channel and your order (the portal worktree is read only).

<criterion id="DBC145-2-AC1" cell_refs="DB-c-23"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r145/p145_bcw.py" . DBC145-2-AC1</invocation><expect>DBC145-2-AC1 PASS</expect></criterion>
`DBC145-2-AC1` -- the four cases and the label: each case carries a verdict from the closed set and a non-empty evidence list whose every `{file, line, text}` the checker re-reads (the file exists and the text appears on the cited line or within two lines of it); the label's `wrong_label_present` equals a fresh search of `MethodAndSources.tsx` for `Time-weighted, net of fees`. Base: FAIL (no record).

<criterion id="DBC145-2-AC2" cell_refs="DB-c-23"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r145/p145_bcw.py" . DBC145-2-AC2</invocation><expect>DBC145-2-AC2 PASS</expect></criterion>
`DBC145-2-AC2` -- the members, the Cottonwood adapter and the bounds: all eight members are present with words; every non-null `produced_by` and `sentence_on_screen` location the checker re-reads exists; the adapter's `adapter_reads_coverage` equals a fresh search of the two Cottonwood adapter files for a `coverage` assignment; the record carries zero writes, AWS calls and runs; only the worker's folder, the channel and its order changed. Base: FAIL (no record).

<expected_criteria>DBC145-2-AC1, DBC145-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo and portal files, `git show`. Writes: the files in `<paths>`. No AWS call, no run, no network, no push.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A state the page does not explain is a finding, never a fix.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W415-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh` (never `--no-verify`); run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~415/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-23.what-the-page-says-about-coverage-today-the-four-fwd10-cases-read-from-the-code.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 14, cell `DB-c-23`.
<owned_cells>DB-c-23</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC145-2-AC1, DBC145-2-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~415/IRPT_DASHBD.TO-DB-c-23.what-the-page-says-about-coverage-today-the-four-fwd10-cases-read-from-the-code.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC145-2-AC1,DBC145-2-AC2` BEFORE the flip (set the order's status to complete only when both PASS); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the two criteria's last lines; the four case verdicts; whether the wrong label is present; how many of the eight members have a sentence on screen; whether the Cottonwood adapter produces coverage; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: file reads and a record; nothing is created, planned, applied, run or written.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched; the page is read from its source.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the checker re-reads every cited line itself.
</preflight>
