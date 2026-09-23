# AMGT_CORPUS task order -- `CRPS-c-3` -- ROUND 1: the typed per-report record in silver (class, fund, sector as written, period, author, size), every field cited or absent-with-reason; K5 answered (how a report's PERIOD is determined, and how many carry one); and the query that returns one name's reports in period order

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-c-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=7 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: RUN at L5 -- 214 roles on the DESIRED plane; BLIND to this box's credential, measured by the chain's earlier puts.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, continued from `CRPS-c-2`. Work ONLY in your worktree.
- **First act:** print `git rev-parse --abbrev-ref HEAD`, and test that `lib/research/corpus/extract.py` exists. If it is
  absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~1;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. NEVER TOUCH THE LIBRARY:** read bronze and the extractions
  from the store.

## 1. THE CELL, inlined in full -- `CRPS-c-3` (manifest row R3, outcome FWD-2)

**FWD-2, verbatim:** *"Every stored report says which security and which period it belongs to, and the ones that cannot
be placed are named. DONE WHEN EXERCISED -- a query by security key returns that name's reports in period order; and
the run prints, as a denominator, how many files resolved, how many did not, and the reason for each that did not."*

**Manifest R3:** *"typed per-report record (class, fund, sector as the team wrote it, period, author, size) | harvest /
silver / research-report, by security key."* **The decomposition's ruling 2:** the security key is a COLUMN. The partition
is the ONE silver writer's own `date=` fetch-date partition (`lib/research/harvest/store.py` `silver_append`, under
`AMGT_RESAPP`'s `C-SILVER-PARQUET`). This project adds no second silver writer.

**`C-CITED-OR-ABSENT`:** *"A field the corpus does not state is `null` with an explicit `absent` reason. Nothing in this
project infers, defaults or fills."*

**K5, verbatim:** *"period resolution -- how a report's PERIOD is determined (filename, header, or content) and how many
of the 351 carry one -- FWD-2's ordering depends on it."* (The decomposition's ruling 3 places K5 in this cell.)

**THE CLASSES, measured by the brief's scan** (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922/RESEARCH_CORPUS_SCAN_20260922.md`
s.1, read-only). This is the report-class enum the decomposition authors: `A | B | C | D | OTHER`.
- **A, the research pack / research note (initiation):** a header block (Ticker, Name, Sector, Location, Currency...),
  a RECOMMENDATION with a fund and a position size, INVESTMENT THESIS, RISKS AND CONSIDERATIONS, MANAGEMENT, and chart
  pages. Filenames often say "Research Pack" or "Research Note".
- **B, the earnings update (quarterly):** `RECOMMENDATION: MAINTAIN x% POSITION IN <fund>`, Headline results or Qn
  Summary, Guidance, Broker commentary, PERFORMANCE VS FUND, TRADING HISTORY.
- **C, the word-capped short form:** section headers carrying word budgets, for example `Company Overview (250)` and
  `Investment Thesis 250`.
- **D, the stock-move update:** a single page on a price move, "Investment thesis unchanged".
- **OTHER:** everything else, which is the subtraction's remainder. That covers company source documents (releases,
  10-Ks, RNS, transcripts, presentations), workbooks, PNG charts, HTML, and blank templates still carrying
  `[PASTE EXCEL OUTPUT]`.
- Every record carries `class_evidence`: the heading, phrase or filename token that decided it. A class you cannot
  evidence is `OTHER` with the reason, never a guess.

**Funds as the corpus writes them:** IDVZ, PFOE, DIVZ. A fund is a field of the REPORT, not of the security.

**RULED -- what you build:**
1. **`lib/research/corpus/typed.py`:**
   - `record(bronze_doc, extraction, backlog_row)` returns one silver row: `security_key`, `report_id`, `bronze_key`,
     `extract_key`, `fetched_at` (tz-aware UTC; the writer requires it), `file_ext`, `source_relpath`, `size_bytes`,
     `words_or_pages`, `report_class` with `class_evidence`, `fund` with `fund_evidence` or `fund_absent_reason`,
     `sector_as_written` with evidence or absent reason, `period` (an ISO date, or a `YYYY-Qn` / `FYyyyy` label) with
     `period_source` in `filename | header | content` and `period_evidence`, or `period_absent_reason`, and `author`
     with evidence or absent reason. Evidence is the literal matched text (at most 200 chars) plus where it was found.
   - **Period resolution order, stated and measured:** the filename date first (`YYYY MM DD`, `YYYYMMDD`, `YYYY-MM-DD`,
     `Qn YYYY`, `nQyy`, `FYyy`, and any other form you MEASURE in the corpus, named in the code), then the header block,
     then content. Record which source won.
   - `python -m lib.research.corpus.typed --write` builds a row for EVERY bronze object and writes them with
     `store.silver_append("amgt", "research-report", rows, ("security_key", "report_id"), <run_stamp>)`. It prints:
     `silver_rows <n> of <n> bronze`, `class A <a> B <b> C <c> D <d> OTHER <o>`, `fund <per fund> absent <n>`, the K5
     line `k5 period carried <p> of <n> by filename <f> header <h> content <c> absent <x>`, and the FWD-2 denominator
     `backlog files <n> = resolved_files <r> + unresolved_files <u>`, followed by one `unresolved <folder> | <reason>`
     line per unresolved folder, the reason read from `CRPS-c-4`'s stored backlog document, never re-worded.
   - `reports_for(security_key)` reads silver (`store.silver_latest`) and returns that name's rows ordered by period
     ascending. Rows with no period come LAST and are counted separately.
   - `python -m lib.research.corpus.typed --reports-for-first-multi` picks the first security key (sorted) with at least
     two reports that carry a period, prints `security_key <key> reports <n> dated <d>`, then one line per report
     (`<period> <class> <relpath>`), then `period_order_ok True` if and only if the dated rows are non-decreasing.
   - `python -m lib.research.corpus.typed --census` re-reads silver and prints `silver_rows <n> of <n> bronze` and the
     K5 line from the STORED rows (the read-back).
2. **`lib/research/corpus/tests/test_typed.py`**, offline, under the poison:
   - each class A-D decided from a minimal fixture extraction, and OTHER for a `[PASTE EXCEL OUTPUT]` template;
   - **ABSENT, NEVER DEFAULTED:** a report stating no fund gives `fund` None and a non-empty `fund_absent_reason`;
   - **PERIOD ORDER:** `reports_for` over a stub with three periods out of order returns them ascending, with an undated
     row last;
   - **ORDER CHECK CAN FAIL:** the order checker over a deliberately unsorted list returns False.

**What this cell does NOT do:** no continuation, template, fund form or typecast (cells c-6 to c-9), no library read, and
no change to any earlier module.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @3c09ae6ce8, chain A, cell 4 of 7 on this slot. When it drains VALID, three sibling workers
spawn on your silver (`CRPS-c-7` sector templates, `CRPS-c-8` fund forms) while you continue to `CRPS-c-6`. **The row
shape is their input: document it at the top of `typed.py`.**

## 3. SURFACES

<paths>
lib/research/corpus/typed.py
lib/research/corpus/tests/test_typed.py
org/missions/D5/AMGT/AMGT_CORPUS/cards/K5_period_resolution.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-3.typed-per-report-record-and-period.md
</paths>

**READ-ONLY:** every earlier `lib/research/corpus/` module, `lib/research/harvest/store.py`, `lib/opal_naming.py`, and
the scan file. Scratch in `.scratch/c3/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **NO S3 DELETE OF ANY KIND** (issuer amendment on row `AMGT_CORPUS-Z-S4`): a wrong object you wrote is superseded by a
  NEW key (bump `method_version`), never deleted. An S3 delete is a human-confirmed act on this estate.
- **Pure ASCII source, LF, Python 3.9-compatible.**
- **S3:** writes ONLY through `store.silver_append`, which is never-overwrite and skips unchanged rows by construction.
- **Run `--write` as a BUILD STEP before the criteria.**
- **The K5 card** answers K5 in plain words (how the period is determined, how many carry one by each source), quoting
  your printed K5 line, and names every filename date form you found.
- **Surprise rows:** `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner` `2.0.0_SA_COO~X`. **REFUSE a criterion you cannot satisfy as
  written**, and report it with your measurement.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 120`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-c-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_typed.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-c-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.typed --census 2>&1 | tail -4</invocation><expect>(?s)silver_rows (\d+) of \1 bronze.*k5 period carried \d+ of \d+ by filename \d+ header \d+ content \d+ absent \d+</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-c-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.typed --reports-for-first-multi 2>&1 | tail -30</invocation><expect>(?s)security_key \S+ reports \d+ dated \d+.*period_order_ok True</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-c-3" judgment="true"/>
  <criterion id="AC5" cell_refs="CRPS-c-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC6" cell_refs="CRPS-c-3"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/c3/hyg.py</invocation><expect>(?s)outside_allowed \[\].*changed_files \d+.*bad 0</expect></criterion>
</proof_of_spec>

- **AC4 (JUDGMENT, the CVO's):** your `--write` run's FWD-2 denominator block (the `backlog files` line and every
  `unresolved <folder> | <reason>` line), plus the K5 card. Record them verbatim, with NO verdict.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-c-3.typed-per-report-record-and-period.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6 --governing-order <this order>` returns rc 0.
3. Flip to `complete` only if every mechanical criterion passes. Commit with `--only`.
4. Report ONCE: the class line, the fund line, the K5 line, the FWD-2 denominator line, and the security key AC3 picked.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the class enum's four postulates are in the decomposition's s.2 (OTHER is the subtraction's
remainder). R3's partition-versus-column reconciliation (ruling 2) is reported to the CTO in the drain-end read.

<status>pending</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
