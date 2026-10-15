# TO MDPF_DEMQUE.TO-DQ-t68 -- round 9 DQ-t-68: a `use_class` column on the Yahoo store index: NOT_FOR_ACTIVE for a V2-held name, INACTIVE_USE for every other, fail closed
<to_id>MDPF_DEMQUE.TO-DQ-t68</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~60</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>USECLASS</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-68` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 29) |
**outcome_ref:** C-PRICES, C-YAHOO, FWD-8 | **depends_on:** DQ-t-59 (merged: the `porting_verdict` column this one sits beside)

---

## WORKER FACE

### THE CELL

Andrew-direct 2026-10-15 (CTO msgs 6105, 6114; ruling amendment 1 @bed1cdb778): a Yahoo price may serve an inactive account and never an active one; "Yahoo prices already stored for active-set names stay and are labelled not-for-active". **Active means the V2 set** (`active_set.py`). This cell adds the label to the store's index as its OWN column, `use_class`, beside `porting_verdict` and not as a value of it or of `claim`: `porting_verdict` grades whether a price matches Bloomberg, `use_class` grades who may use it, and one column carries one intent (TAXONOMY LAW iii). Values (a closed pair, MECE over the index rows by V2 membership): **`NOT_FOR_ACTIVE`** (the row's CUSIP is in V2) and **`INACTIVE_USE`** (it is not). **Fail closed:** when the V2 set cannot be read, EVERY row reads `NOT_FOR_ACTIVE`; the column never writes `INACTIVE_USE` on a read it could not complete.
It changes a served file, so it carries the never-widen pair `ledger/NEVER_WIDEN_R9_INACTIVE_YAHOO_{COO,CTO}_HALF.md`; the issuer merges it only after both halves are signed. **This cell writes nothing to S3.**

**Build** (read `price_store.py` `INDEX_COLS`, `index`, `write_index`, `main`, `verdicts_path`, and the DQ-t-59 tests `test_demque_porting_verdict.py`; `active_set.py` `load`; import, do not copy; all under data/mdpf/scripts/demque/):
1. **`INDEX_COLS`** gains `use_class` as the LAST column (the ten old columns keep their order).
2. **`index(root, verdicts=None, active=None)`** fills `use_class` per CUSIP: `NOT_FOR_ACTIVE` when the CUSIP is in `active` (a set or mapping), else `INACTIVE_USE`; **`active=None` means the V2 set was not supplied or could not be read, and every row reads `NOT_FOR_ACTIVE`**. A caller that passes an empty set reads every row `INACTIVE_USE` (an empty set is a successful read).
3. **`write_index(root)`** loads `active_set.load()` itself inside a `try` that catches `Exception` and `SystemExit`: success passes the key set, failure passes `None` and prints one line naming the failure type (never a path of an account, never an account key). Its two `put`s are unchanged.
4. **`price_store.py --index-preview [--verdicts PATH] [--active-set-path PATH]`** (the DQ-t-59 mode): the one JSON line gains `use_class` ({value: count}) and `active_source` (`"read"` when `active_set.load(path)` succeeded, `"unreadable"` otherwise; `--active-set-path` is passed to `active_set.load(path=...)`), and `columns` ends `[..., "porting_verdict", "use_class"]`. `old_columns_digest` is still the sha256 of the ten OLD columns as CSV text (so it equals the DQ-t-59 value).
5. **Tests** in a NEW `test_demque_use_class.py` (pytest; a local store directory, no network) with exactly these names:
   `test_the_index_gains_a_use_class_column_last_and_a_v2_held_name_reads_not_for_active_while_any_other_name_reads_inactive_use`,
   `test_an_unreadable_or_absent_active_set_writes_not_for_active_for_every_name_and_never_inactive_use`,
   `test_the_use_class_column_is_independent_of_the_porting_verdict_column`.
   `test_demque_store.py:64` and `test_demque_porting_verdict.py` pin the column list: update those assertions to the eleven-column list and nothing else; every other importer's tests keep passing unedited (run the whole folder).
6. **Report** the folder count (`pytest data/mdpf/scripts/demque` once) and the real `--index-preview` line verbatim.

### ACCEPTANCE

<criterion id="DQ9-t68-AC1" cell_refs="DQ-t-68"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t68_tests.py</invocation><expect>USECLASS-OK</expect></criterion>
<criterion id="DQ9-t68-AC2" cell_refs="DQ-t-68"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t68_real.py</invocation><expect>USECLASS-REAL-OK</expect></criterion>
`DQ9-t68-AC1` -- the three named tests. `DQ9-t68-AC2` -- on the REAL index (S3 read only via `--index-preview`): eleven columns ending `porting_verdict`, `use_class`; `NOT_FOR_ACTIVE` equals the number of index CUSIPs in V2 and `INACTIVE_USE` the rest (counted independently by the check); `active_source` reads `read`; the old-columns digest is the same across two runs; an unreadable active-set path prints `unreadable` and every row `NOT_FOR_ACTIVE`.
The check runs the preview three times (about 20 s each): invoke it under `timeout 260`.

<expected_criteria>DQ9-t68-AC1,DQ9-t68-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `USECLASS-BAD no file ...test_demque_use_class.py`; `USECLASS-REAL-BAD columns do not end in porting_verdict, use_class with 11 columns`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **NO write to S3, any store key, the queue, the ledger, the actuals or the pacer; `price_store.py` is never run without `--index-preview` against the real root, and `write_index` is never run against S3; no AWS write; no deploy; no timer; no Yahoo or Bloomberg call.** Never print an account number. Build no alarm, monitor or notification. **Do not merge anything**; the issuer merges after the pair is signed.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W60-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1` (it is blocked by a foreign row); the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/price_store.py
data/mdpf/scripts/demque/test_demque_use_class.py
data/mdpf/scripts/demque/test_demque_store.py
data/mdpf/scripts/demque/test_demque_porting_verdict.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-68`.
<owned_cells>DQ-t-68</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t68-AC1, DQ9-t68-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~60/MDPF_DEMQUE.TO-DQ-t68.use-class-column.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t68-AC1,DQ9-t68-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the real preview line verbatim, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no new AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE a column graded by tests and a read-only preview.
risk: SERVED -- the code changes the two served index keys at the next `write_index`; the never-widen pair `ledger/NEVER_WIDEN_R9_INACTIVE_YAHOO_{COO,CTO}_HALF.md` covers it and gates the MERGE.
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct 2026-10-15 via CTO msgs 6105, 6114 and ruling items 4 and amendment 1 (its own column); decomposition round 9, amendment 29.
