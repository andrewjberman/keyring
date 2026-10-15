# TO MDPF_DEMQUE.TO-DQ-t65 -- round 9 DQ-t-65: the inactive-only set takes its symbols from Cottonwood's own transactions (the estate already carries them), read only
<to_id>MDPF_DEMQUE.TO-DQ-t65</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~57</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>INACTIVESYMBOLS</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-65` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 28) |
**outcome_ref:** C-PRICES, C-YAHOO, C-PRIORITY, FWD-8 | **depends_on:** DQ-t-64 (merged)

---

## WORKER FACE

### THE CELL

`DQ-t-64` built `data/mdpf/scripts/demque/inactive_set.py`, the census of the securities no V2 active Cottonwood account holds (1,705). It found only 14 with a symbol, because its `symbol_of` read only the stored price index and the request files. Cottonwood's own silver transactions (`commonwealth/cottonwood/silver/transactions`, the frame `rank.load_transactions` reads with six columns) also carry a `Symbol` column, and a pre-measure counts 1,071 of the 1,705 with a non-blank one. **This cell adds that third source. It makes no vendor call and draws nothing; it edits only `inactive_set.py` and adds one test file.**

**Build** (read `inactive_set.py` in full: `_norm`, `_symbol`, `census`, `_real`, `main`; `rank.py` `load_transactions`, `_s3`, `_split`, `DAY` and the `address("commonwealth", "cottonwood", "silver", "transactions", DAY)` call; import, do not copy):
1. **`tx_symbols(frame) -> dict`** (pure): from a frame with columns `Cusip` and `Symbol`, the map `cusip -> symbol` where `cusip` is the trimmed, non-blank `Cusip` and `symbol` is that CUSIP's MOST FREQUENT non-blank `Symbol` after trimming and upper-casing; a tie takes the first in ascending string order; a blank, null, `nan` or `none` Symbol is never counted; a CUSIP with no non-blank Symbol is absent.
2. **`merge_symbols(index_syms, request_syms, tx_syms) -> (dict, set)`** (pure): precedence is the stored index first, then the request files, then the transactions; the second value is the set of CUSIPs whose symbol came ONLY from `tx_syms`.
3. **`census(...)` gains a trailing optional argument `tx_only=()`** and the dict gains the integer key `tx_symbol_only`: the count of inactive-only CUSIPs that are in `tx_only` and have a symbol. Every existing key, identity and call keeps its meaning (the DQ-t-64 tests pass unedited).
4. **`_real()` and `main`** read the transactions' `Cusip` and `Symbol` columns only (a NEW loader function `load_tx_symbol_frame(s3=None)` in `inactive_set.py`, the same address and paging as `rank.load_transactions`, `columns=["Cusip", "Symbol"]`), build `tx_syms`, merge, and pass `tx_only`. Output stays deterministic (two runs byte-identical); no account number and no key naming an account appears. Edit NO other script.
5. **Tests** in a NEW `test_demque_inactive_symbols.py` (pytest; small stub frames, no network) with exactly these names:
   `test_a_transaction_symbol_is_the_modal_non_blank_symbol_per_cusip_and_a_tie_takes_the_first_ascending`,
   `test_the_symbol_precedence_is_the_index_then_the_request_files_then_the_transactions`,
   `test_the_census_counts_the_names_whose_symbol_came_only_from_the_transactions`.
6. **Report the real census line verbatim**, with the folder count (`pytest data/mdpf/scripts/demque` once).

### ACCEPTANCE

<criterion id="DQ9-t65-AC1" cell_refs="DQ-t-65"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t65_tests.py</invocation><expect>SYMBOLS-OK</expect></criterion>
<criterion id="DQ9-t65-AC2" cell_refs="DQ-t-65"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t65_real.py</invocation><expect>SYMBOLS-REAL-OK</expect></criterion>
`DQ9-t65-AC1` -- the three named tests. `DQ9-t65-AC2` -- on the REAL inputs (S3 and the V2 active set read only): every DQ-t-64 identity still holds, `tx_symbol_only` is above 0 and at most `with_symbol`, `with_symbol` is between 1,000 and `inactive_only`, the names file's non-null symbols number exactly `with_symbol`, no CUSIP of it is in V2, no account key, two runs are byte-identical.
The check runs the census twice (about 40 s each): invoke it under `timeout 260`.

<expected_criteria>DQ9-t65-AC1,DQ9-t65-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `SYMBOLS-BAD no file ...test_demque_inactive_symbols.py`; `SYMBOLS-REAL-BAD a census key is missing or not an integer`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO vendor call, no write to S3, any ledger, the queue, the price store or any pacer state; do NOT write into `org/missions/.../requests/`**; no AWS write; no deploy; no timer. Never print an account number (the loader reads `Cusip` and `Symbol` only and never the account column). Build no alarm, monitor or notification.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W57-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1` (it is blocked by a foreign row); the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/inactive_set.py
data/mdpf/scripts/demque/test_demque_inactive_symbols.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-65`.
<owned_cells>DQ-t-65</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t65-AC1, DQ9-t65-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~57/MDPF_DEMQUE.TO-DQ-t65.inactive-symbols-from-transactions.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t65-AC1,DQ9-t65-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the real census line verbatim, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE a measurement over S3 reads; no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a read-only census; nothing is drawn or served.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: CTO msg 6114 (the non-Bloomberg resolver is the next cell; P2 names count as inactive for Yahoo, ruling amendment 1 @bed1cdb778); the DQ-t-64 census; decomposition round 9, amendment 28.
