# TO MDPF_DEMQUE.TO-DQ-t59 -- round 9 DQ-t-59: a `porting_verdict` column on the Yahoo store index (never-widen pair B, signed): UNVERIFIED until the porting test passes, fail closed
<to_id>MDPF_DEMQUE.TO-DQ-t59</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~51</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>PORTINGVERDICT</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-59` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 22) |
**outcome_ref:** C-PRICES, C-YAHOO, FWD-8 | **depends_on:** DQ-t-49, DQ-t-51, DQ-t-58 (merged; this worktree is provisioned AFTER t-58 lands)

---

## WORKER FACE

### THE CELL

Andrew-direct 2026-10-13: a Yahoo-sourced client price reads UNVERIFIED until it passes the porting test (returns, five sha256-drawn intervals, within 10 bps of Bloomberg `TOT_RETURN_INDEX_GROSS_DVDS`; `porting_test.compare` returns `PASS`, `FAIL`, `NO_BLOOMBERG` or `UNTESTABLE` per CUSIP).
Nothing in the served store says so today. This cell adds the label. It changes a served file, so it carries a signed **never-widen pair**; read both halves first and obey them: [COO half](file:///C:/dev/ajb_workspace/org/missions/D8/MDPF/MDPF_DEMQUE/ledger/NEVER_WIDEN_R9_YAHOO_B_COO_HALF.md),
[CTO half](file:///C:/dev/ajb_workspace/org/missions/D8/MDPF/MDPF_DEMQUE/ledger/NEVER_WIDEN_R9_YAHOO_B_CTO_HALF.md) (repo-relative `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/NEVER_WIDEN_R9_YAHOO_B_{COO,CTO}_HALF.md`).
**The shape is a separate column, NOT a value of `claim`:** a new value in that enum needs the TAXONOMY LAW record. **Only the two index keys move** (`index/index.parquet`, `index/index.csv`); no `cusip=<C>/` key is touched. **This cell writes nothing to S3.**

**Build** (read `price_store.py` `INDEX_COLS`, `index`, `write_index`, `main`; `porting_test.py` `compare`; `test_demque_store.py`; import, do not copy):
1. **`INDEX_COLS`** gains `porting_verdict` as the LAST column (the nine old columns keep their order).
2. **Verdicts file.** `price_store.verdicts_path()` returns `<OPAL_DEMQUE_HOME or ~/.opal/demque>/porting_verdicts.json` (derived exactly as `run_daily_draw.sh` derives its state home; nothing typed). Format: `{"<CUSIP>": {"verdict": "PASS"|"FAIL"|"UNTESTABLE"|"NO_BLOOMBERG", ...other keys ignored}}`.
3. **`index(root, verdicts=None)`** fills `porting_verdict` per CUSIP: `PASS`, `FAIL` and `UNTESTABLE` as read; `NO_BLOOMBERG`, a CUSIP with no row, and any other value read `UNVERIFIED` (a NO_BLOOMBERG is never a pass). **Fail closed:** a verdicts file that is absent reads `UNVERIFIED` for every name; one that is unreadable or malformed
   (not JSON, not an object, a row that is not an object) also reads `UNVERIFIED` for every name and the function reports `verdicts_source = "unreadable"` (`"absent"` / `"read"` otherwise). It never writes `PASS` on a read it could not complete. `write_index(root)` passes `verdicts_path()`; its two `put`s are unchanged.
4. **`price_store.py --index-preview [--verdicts PATH]`** (a NEW mode of `main`, read only, NO `put`): builds the index as `write_index` would and prints ONE JSON line `{"columns", "rows", "porting_verdict": {value: count}, "verdicts_source", "sample_cusips": [first three CUSIPs ascending], "old_columns_digest": sha256 hex of the nine old columns as CSV text}`.
   `--index-preview` must NOT fall through to the old positional root argument (the old `main` takes `argv[0]` as a root; guard it).
5. **A named test file** `test_demque_porting_verdict.py` (pytest; a local store directory, no network) with exactly these names:
   `test_the_index_gains_a_porting_verdict_column_defaulting_to_unverified_for_every_name_when_no_verdicts_file_exists`,
   `test_a_verdicts_file_sets_pass_fail_untestable_per_name_and_a_name_without_a_row_or_with_no_bloomberg_stays_unverified`,
   `test_a_malformed_or_unreadable_verdicts_file_writes_unverified_for_every_name_and_never_pass`.
   `test_demque_store.py:64` pins the column list: update that assertion to the new list and nothing else; every other importer's tests keep passing unedited (run the whole folder).

### ACCEPTANCE

<criterion id="DQ9-t59-AC1" cell_refs="DQ-t-59"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t59_tests.py</invocation><expect>VERDICT-OK</expect></criterion>
<criterion id="DQ9-t59-AC2" cell_refs="DQ-t-59"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t59_real.py</invocation><expect>VERDICT-REAL-OK</expect></criterion>
`DQ9-t59-AC1` -- the three named tests. `DQ9-t59-AC2` -- on the REAL index (S3 read only, `--index-preview`): the nine old columns plus `porting_verdict` last, every name `UNVERIFIED` with no file, PASS 1 / FAIL 1 / the rest UNVERIFIED with a file naming three real CUSIPs (the third `NO_BLOOMBERG`),
a broken file fails closed, the old columns are byte-identical across runs. Report the whole folder `pytest data/mdpf/scripts/demque` once and the three arm lines verbatim.

<expected_criteria>DQ9-t59-AC1,DQ9-t59-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `VERDICT-BAD no file ...test_demque_porting_verdict.py`; `VERDICT-REAL-BAD arm1 ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **NO write to S3, any store key, the queue, the ledger, the actuals or the pacer; `price_store.py` is never run without `--index-preview` against the real root, and `write_index` is never run against S3; no AWS write; no deploy; no timer; no Yahoo or Bloomberg call.** Build no alarm, monitor or notification.
- **Do not write the verdicts file for the real store** and do not run the porting-test comparator: the file is written after the Bloomberg draw, by a later cell. Tests build their own temp files.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W51-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the
  investigation file below. Do NOT merge `box/dell1` (it is blocked by a foreign row); the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/price_store.py
data/mdpf/scripts/demque/test_demque_porting_verdict.py
data/mdpf/scripts/demque/test_demque_store.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-59`.
<owned_cells>DQ-t-59</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t59-AC1, DQ9-t59-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~51/MDPF_DEMQUE.TO-DQ-t59.porting-verdict-column.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t59-AC1,DQ9-t59-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the three arm lines, how the verdicts path is derived, what each unreadable case prints, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the 22:30 ET scheduled task runs the same script; no schedule changes.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write by this cell; the runtime write set is the two index keys the run already writes.
comp-adversary: DECLARED-NOT-APPLICABLE the signed pair names the 2 keys, the single writer (write_index), the consumers and the fail-closed branches.
risk: SERVED -- adds a column to the served index. Never-widen pair B: COO half `7cf77ad224`, CTO half signed 2026-10-13 ~22:0xZ (msg 5251). The first night the new index is written is a WORLD act; the issuer reads the index before the next.
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct 2026-10-13 (porting test; Yahoo client prices UNVERIFIED until pass); CTO msg 5251; decomposition round 9.
