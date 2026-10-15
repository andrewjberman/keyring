# TO MDPF_DEMQUE.TO-DQ-t64 -- round 9 DQ-t-64: the INACTIVE-ONLY set, the securities no active Cottonwood account holds, measured and quoted for the Yahoo leg (read only)
<to_id>MDPF_DEMQUE.TO-DQ-t64</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~56</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>INACTIVESET</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-64` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 27) |
**outcome_ref:** C-PRICES, C-YAHOO, C-PRIORITY, FWD-8 | **depends_on:** DQ-t-57, DQ-t-60 (merged)

---

## WORKER FACE

### THE CELL

Andrew-direct 2026-10-15, relayed by the CTO (msg 6105): "Active accounts should get BBG pricing exclusively, inactive accounts are fine with yahoo finance." The Yahoo leg is to be pointed at the securities held ONLY by accounts outside the V2 active set. Nothing yet says how many those are, how many have a symbol, or what one pass costs against the Yahoo request cap. **This cell measures that. It makes no vendor call and draws nothing; it changes no existing file.**

**Build** (read `active_set.py` `load`; `priority_gate.py` `load_inputs`; `rank.py` `rank` and `_stats`; `p1_coverage.py` `request_symbols` and `classify`; `extend_frontier.py` `_landed`, `DAILY_CAP`, `TIER2_RESERVE`, `_request_cap`; `price_store.py` `s3_root`, `index`; import, do not copy):
1. **A NEW module `data/mdpf/scripts/demque/inactive_set.py`** with these functions (pure; no IO inside them):
   - `inactive_cusips(tx_df, active) -> list`: the distinct, non-blank values of `tx_df["Cusip"]` that are not in `active` (a mapping or set of CUSIPs), sorted ascending. A blank or null `Cusip` is never held.
   - `census(tx_df, crosswalk_df, active, symbol_of, stored, request_cap) -> (dict, names)`: `names` is the list of `{"cusip", "symbol", "priority"}` over `inactive_cusips`, sorted by cusip; `symbol` is `symbol_of.get(cusip)` (a string or `None`); `priority` is `rank.rank`'s class (`P1`, `P2` or `P3`). The dict holds these integer keys: `held_total` (distinct non-blank CUSIPs in `tx_df`), `active_held` (those in `active`), `inactive_only`, `class_p1`, `class_p2`, `class_p3` (counted over the inactive set), `with_symbol`, `no_symbol`, `inactive_stored` (inactive CUSIPs in `stored`), `inactive_unstored`, `active_stored` (CUSIPs in `stored` that ARE held by an active account), `requests_one_pass` (equals `with_symbol`: one vendor request per symbol), `request_cap`, `nights_at_cap` (`ceil(with_symbol / request_cap)`, 0 when `with_symbol` is 0).
2. **`python data/mdpf/scripts/demque/inactive_set.py --census --out PATH`**: reads the real inputs (`priority_gate.load_inputs()` for the crosswalk and the transactions; `active_set.load()` for `active`; `symbol_of` = the stored index's `yahoo_symbol` per CUSIP, overlaid by `p1_coverage.request_symbols` over every `*.json` in `org/missions/D8/MDPF/MDPF_DEMQUE/requests/` (look at its signature: it takes request file paths); `stored` = the CUSIPs of `price_store.index(price_store.s3_root())`; `request_cap` = `extend_frontier._request_cap()`), prints the census dict as ONE JSON line, and writes `{"names": [...]}` to `--out`. **Deterministic**: two runs write byte-identical files (`sort_keys=True`, a fixed indent, a trailing newline). **No account number, and no key that names an account, appears in the line or the file.**
3. **Tests** in a NEW `test_demque_inactive_set.py` (pytest; small stub frames, no network) with exactly these names:
   `test_the_inactive_set_is_the_held_cusips_not_in_the_active_set_and_a_blank_cusip_is_never_held`,
   `test_the_census_adds_up_classes_symbols_and_stored_against_the_inactive_total`,
   `test_nights_at_cap_is_the_ceiling_of_symbols_over_the_request_cap`.
4. **Report the real census line verbatim**, with the folder count (`pytest data/mdpf/scripts/demque` once). If no importable resolver gives you a symbol for a stored or requested CUSIP the way step 2 says, stop with a BLOCKING row; do not invent a symbol source.

### ACCEPTANCE

<criterion id="DQ9-t64-AC1" cell_refs="DQ-t-64"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t64_tests.py</invocation><expect>INACTIVE-OK</expect></criterion>
<criterion id="DQ9-t64-AC2" cell_refs="DQ-t-64"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t64_real.py</invocation><expect>INACTIVE-REAL-OK</expect></criterion>
`DQ9-t64-AC1` -- the three named tests. `DQ9-t64-AC2` -- on the REAL inputs (S3 and the V2 active set read only): the census identities hold (`held_total == active_held + inactive_only`; the three classes, `with_symbol + no_symbol` and `inactive_stored + inactive_unstored` each add to `inactive_only`; `requests_one_pass == with_symbol`; `request_cap == 380`; `nights_at_cap == ceil(with_symbol / 380)`), the names file holds exactly `inactive_only` unique sorted entries none of which is in V2, it carries no account key, two runs are byte-identical.
The check runs the census twice (about 100 s each): invoke it under `timeout 260`.

<expected_criteria>DQ9-t64-AC1,DQ9-t64-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `INACTIVE-BAD no file ...test_demque_inactive_set.py`; `INACTIVE-REAL-BAD census rc=2 ... inactive_set.py ... No such file`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO vendor call, no write to S3, any ledger, the queue, the price store or any pacer state; do NOT write into `org/missions/.../requests/`**; no AWS write; no deploy; no timer. Never print an account number (the census reads the transactions to count holders and classes; its output holds CUSIPs, symbols, classes and counts only). Build no alarm, monitor or notification. Edit NO existing script: `inactive_set.py` imports them.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W56-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1` (it is blocked by a foreign row); the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/inactive_set.py
data/mdpf/scripts/demque/test_demque_inactive_set.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-64`.
<owned_cells>DQ-t-64</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t64-AC1, DQ9-t64-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~56/MDPF_DEMQUE.TO-DQ-t64.inactive-only-yahoo-set.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t64-AC1,DQ9-t64-AC2` BEFORE the flip.
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

Source: Andrew-direct 2026-10-15 via CTO msg 6105 and the ruling `org/missions/D8/ADVI/ADVI_COTBKF/ledger/CTO_RULING_DELL1_UNPARK_ACCELERATE_20261015.md` @f984c02191 items 3 and 4; decomposition round 9, amendment 27.
