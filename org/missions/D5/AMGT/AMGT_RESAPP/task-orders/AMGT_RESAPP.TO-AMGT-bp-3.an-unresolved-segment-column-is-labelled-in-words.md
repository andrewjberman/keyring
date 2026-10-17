# AMGT_RESAPP task order -- `AMGT-bp-3` -- A SEGMENT-TABLE COLUMN WHOSE YEAR IS NOT RESOLVED IS LABELLED IN WORDS, NOT `Period 5` (A CODE CHANGE ON THE SERVED PATH, WITH TESTS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bp-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~489</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bp-3.an-unresolved-segment-column-is-labelled-in-words</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- python code and tests only; nothing scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call: the tests build their inputs in memory and read committed fixture files.
comp-adversary: RUN at the cut -- the three existing segment test files read `43 passed` at the base (read here); the new test file `lib/research/api/tests/test_segment_unresolved_label.py` does not exist at the base, so `python -m pytest` naming it exits 4 (`file or directory not found`) and AC1 and AC2 both read FAIL there as expected. The worker runs both with the new test file written but the product code unchanged before any product edit (step 3): U1 and U4 must fail.
EGRESS CLASS, declared: NONE -- no network, no AWS call, no S3 read; pytest with in-memory inputs. The change is a CODE change only: nothing is deployed by this order (a later order redeploys the scoped API).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-489` (branch `wk-AMGT_RESAPP-489`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-489`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE CELL -- `AMGT-bp-3` (round 109, decomposition s.118)

On the Security Analysis page, RIO LN's Thesis tab prints a segment-revenue column headed `Period 5`. The CTO's ruling: "the label comes from the period's real name". This cell changes the SERVED label of a column whose year is not resolved. It is a python change under `lib/research/api/`; it deploys nothing.

**How the label is made today (read at the base).** `lib/research/api/segment_table.py` reads the stored Bloomberg segment table: every row carries `Period 1 Value` to `Period 5 Value` and NO period name. `lib/research/api/segment_served.py` `_serve` calls `segment_period.label_periods(_column_sums(rows), revenue, currency)`, which names a column `Fiscal year <Y>` only when its top-level sum ties to the company's stored reported revenue for year `Y`; every other column is served as `{"period": n, "label": "Period n", "fiscal_year": None, "top_level_sum": <sum or None>, "note": <reason>}`. Measured on RIO LN (the served body is committed, fixture below): columns 1 and 2 have no figure (sum null); column 3 is `Fiscal year 2023` (sum 54041.0); column 4 is `Fiscal year 2022` (55554.0); column 5 is `Period 5` (sum 106861.0, note `The rows of this column do not add up to the company's reported revenue for any year we hold, so the year is not stated.`). The portal (`SegmentTable.tsx`) prints the served `label` as the column head and, for a dropped (no-figure) column, `<label> is not shown: <note>`.

**The change.**
1. **Look first for a real name.** Read `segment_period.py` and `segment_served.py` and decide, from what the STORED data holds (the stored revenue by fiscal year, the column sums, the units), whether a column that does not tie can be named truthfully (for example a stored unit or scale mismatch that makes one year tie when the columns are rescaled by the units the table states). If, and only if, a stored value names it with the same tolerance the code already applies to the other columns, name it `Fiscal year <Y>` exactly as a tied column is named. Do NOT guess a year from position (the column after the last named one is NOT evidence) and do NOT widen the tie tolerance. State in your report what you tried and what you found.
2. **Otherwise label it in words.** A column that carries at least one figure (its `top_level_sum` is not null) and whose year is not resolved is labelled `Year not stated (column <n>)`, with `<n>` its `period` number, in place of `Period <n>`. `fiscal_year` stays `None`, `top_level_sum` and `note` are unchanged. A column with NO figure keeps today's label `Period <n>` (the portal drops it and its footer line is unchanged). A tied column keeps `Fiscal year <Y>`.
3. **Nothing else moves.** `period_note`, `currency`, `units`, `rows`, `operating_income_rows` and every other key of the served block are byte-for-byte as today; the label string of an unresolved figure-bearing column is the ONLY value that changes. Update only the existing assertions that pinned the old label on a figure-bearing column, and list each one you changed in your report (file, test name, old, new); an assertion you cannot justify is a BLOCKING row, not an edit.

**Fixture.** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round109_prep/fixtures/RIO_LN_segment_slice_live.json` (the live served `segment_table` and `segment_breakdown` of RIO LN, read 2026-10-17, unedited). Use its `segment_table.periods` and `rows` as the expected shape and build the test inputs from the table's own numbers (read the helpers in `lib/research/api/tests/test_segment_served.py` as your model: they construct the stored rows as `Period <i> Value` columns and a stored revenue set).

**Do this in order.** (1) `cd C:/dev/wk-resapp-489` and read the files named above. (2) Write the new test file `lib/research/api/tests/test_segment_unresolved_label.py` FIRST. It must hold at least these 4 tests, each named for what it checks: U1 a table shaped like RIO LN's (column 3 and 4 tied, column 5 figure-bearing and untied, columns 1 and 2 empty) serves column 5 with label `Year not stated (column 5)`, `fiscal_year` None, `top_level_sum` 106861.0, and the same `note` as before; U2 the columns 1 and 2 keep `Period 1` and `Period 2`, columns 3 and 4 keep `Fiscal year 2023` and `Fiscal year 2022`; U3 the difference control: serving the same inputs through the UNEDITED label rule (kept in the test as a small copy of the old rule) differs from the new serve in exactly the one label of column 5, every other key of the block equal; U4 a table with NO tied column and two figure-bearing untied columns labels them `Year not stated (column <n>)` with their own numbers (two distinct labels). If step 1's look finds a real name (change item 1), add a test for it and say so. (3) With the new test file written and the product code UNCHANGED, run AC1 and AC2 ONCE: both must read failures (AC1 shows `failed` with U1 and U4 among them; AC2 exits non-zero with U1 and U4 failed); record both runs. (4) Then make the product edit, only in `lib/research/api/segment_served.py` and, only if step 1 needs it, `lib/research/api/segment_period.py`. (5) Run AC1 and AC2. (6) Commit in your worktree via `.tools/safe-commit.sh` with the author line below (`-F` a message file written with the Write tool; `--` the changed paths). Every `.py` edit passes `.tools/commit-gate.sh` (py_compile, ds-precommit, ruff py39); a gate refusal is a BLOCKING row, never an override.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W<slot>-S<k>` (a seat order's rows: `AMGT_RESAPP-D1-S<k>`), `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Python only, under `lib/research/api/`: the two product files and the five test files named in `<paths>`; no other product file, no portal file, no AWS call, no `pip install`.
2. Never deploy, never invoke the live function, never write S3; the served shape of every block other than the one label is unchanged.
3. Do not widen the tie tolerance and do not name a year the stored data does not name.

## 3. SURFACES

<paths>
lib/research/api/segment_served.py
lib/research/api/segment_period.py
lib/research/api/tests/test_segment_served.py
lib/research/api/tests/test_segment_period.py
lib/research/api/tests/test_segment_table.py
lib/research/api/tests/test_segment_unresolved_label.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~489/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bp-3"><invocation>cd C:/dev/wk-resapp-489 &amp;&amp; timeout 120 python -m pytest lib/research/api/tests/test_segment_served.py lib/research/api/tests/test_segment_period.py lib/research/api/tests/test_segment_table.py lib/research/api/tests/test_segment_unresolved_label.py -q --color=no -p no:cacheprovider 2>&amp;1 | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>a line `<N> passed` with N at least 47 (the base's 43 across the first three files plus at least four new tests) and no `failed` or `error`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bp-3"><invocation>cd C:/dev/wk-resapp-489 &amp;&amp; timeout 120 python -m pytest lib/research/api/tests/test_segment_unresolved_label.py -q --color=no -p no:cacheprovider -k "U1 or U2 or U3 or U4" 2>&amp;1 | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>a line `4 passed` (the four named tests U1 to U4; more only if step 1 adds one) and no `failed`; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~489 <0.9.0_WK_AMGT_RESAPP~489@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~489/AMGT_RESAPP.TO-AMGT-bp-3.an-unresolved-segment-column-is-labelled-in-words.proof_of_spec.json` (this order's own name is short on purpose, so the canonical path opens on this box) with `to_id` equal to the `<to_id>` line above, character for character, and `decomp_ref` from the order's own `<decomp_ref>` block; record each criterion's `expect` as an ordered regex of the printed lines when the prose has regex-active characters. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` from `C:/dev/wk-resapp-489` on the committed bytes and report its verdict line.

Report once:
- the branch name and its head commit;
- what step 1's look found (a real name, or none) and why;
- the unchanged-tree run of AC1 and AC2 and the runs after;
- AC1's and AC2's output lines;
- every existing assertion you changed (file, test, old, new);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 7490 and `ROUND_ANALYSIS.round108.md` item 2 ("RIO LN Thesis column label `Period 5`: the label comes from the period's real name"). Measured by the issuer at the cut: the label is SERVED (`lib/research/api/segment_served.py`, `"Period %s" % n`), not a portal string, and the stored segment source (`segment_table.py`) carries no period name, only `Period N Value` columns; a column is named only by reconciling its sum to stored reported revenue (`segment_period.label_periods`). So the CTO's wording cannot be met by reading a name that is not stored: s.118 (b) makes the cell look for a stored name once and otherwise label the column in words as a column whose year is not stated, which is the honest state of the data. This is a SERVED-path change; the redeploy of `opal-amgt-scoped-api` carrying it is the placed cell `AMGT-bp-6` (a CloudOps act behind a never-widen pair on the one AMGT CloudOps lane, CLAUDE.md rule 34), cut when this order is complete. The portal needs no edit: `SegmentTable.tsx` prints the served label. Base measured at the cut: `43 passed` across `test_segment_served.py`, `test_segment_period.py` and `test_segment_table.py` (pytest 9.1.1, 2026-10-17 ~12:0xZ); `test_segment_served.py` lines 110 and 174 assert `label == "Period %d"` on columns that may carry no figure or a figure, so the worker reads each and lists its changes.

<status>pending</status>
<round>109</round>
<slot>0.9.0_WK_AMGT_RESAPP~489</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
