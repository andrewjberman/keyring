# TO MDPF_DEMQUE.TO-DQ-t67 -- round 9 DQ-t-67: the Yahoo backfill requests for the inactive-only names that have a symbol, built in chunks and priced (read only; the issuer places them)
<to_id>MDPF_DEMQUE.TO-DQ-t67</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~59</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>INACTIVEREQ</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-67` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 29) |
**outcome_ref:** C-PRICES, C-YAHOO, C-QUOTE, FWD-8 | **depends_on:** DQ-t-64, DQ-t-65 (merged)

---

## WORKER FACE

### THE CELL

Andrew-direct 2026-10-15 (CTO msgs 6105, 6114): inactive accounts may take Yahoo. `inactive_set.py --census --out PATH` (DQ-t-64/65, merged) writes the names file `{"names": [{cusip, symbol, priority}, ...]}` of the securities no V2 active account holds: 1,705 names, 1,071 of them with a symbol. **This cell builds the Yahoo history requests that will draw those 1,071 names.** One Yahoo vendor request is one symbol whatever the window, and the shared pacer allows 380 a day, so the names go in several request FILES of at most 300 names each, ordered by rank across the files; the draw takes them in file order within the tier. It makes no vendor call, draws nothing and writes only the `--out-dir` it is given: the issuer places the files in the queue after the never-widen pair is signed.

**Build** (read `inactive_set.py` `names_doc`; `extend_frontier.py` `_request`, `NEED_CLASS`, `TIER`, `FIELDS`, `_window_start`; `demand_queue.py` `validate`, `quote`, `_rank_key`; `daily_draw.py` `_closed_frontier`; `lib/trading_calendar.py`; import, do not copy; all under data/mdpf/scripts/demque/):
1. **A NEW module `data/mdpf/scripts/demque/inactive_request.py`**:
   - `build(names, frontier, chunk=300) -> list` (pure): from the names list, drop every entry with a null or blank `symbol` (count them), order the rest by `priority` (`P1`, `P2`, `P3`) then `cusip` ascending, give each kept entry `rank` = its 1-based position in that order, cut the ordered list into consecutive chunks of at most `chunk`, and return one request dict per chunk: `request_id` `YAHOO-INACTIVE-BACKFILL-NN` (`NN` two digits from `01`), `tier` 2, `reason` "Andrew-direct 2026-10-15: inactive accounts take Yahoo; securities no V2 active account holds", `page` "price store (C-PRICES, inactive-only names)", `securities` `[{cusip, symbol, rank}]`, `fields` `["close"]`, `start` `"2012-01-01"`, `end` the frontier as an ISO date, `need_class` `"client"`, `window_start` `"2012-01-01"`. Each request passes `demand_queue.validate`.
   - **`python data/mdpf/scripts/demque/inactive_request.py --build --names PATH --out-dir DIR [--chunk N]`**: reads the names file, takes the frontier from `daily_draw._closed_frontier(datetime.now(timezone.utc))`, writes one `YAHOO-INACTIVE-BACKFILL-NN.json` per request into `DIR` (`sort_keys=True`, indent 1, trailing newline; the directory is created), and prints ONE JSON line of integers: `names_in`, `with_symbol`, `without_symbol`, `requests`, `securities_total`, `max_chunk`, `cells` (the sum of `dq.quote(req, 0, 400, today)["cells"]["yahoo"]` over the requests), `nights` (the ceil of `with_symbol` over 380). Two builds on one names file the same day are byte-identical. No account number and no key naming an account appears. A `DIR` that already holds a `YAHOO-INACTIVE-BACKFILL-*.json` is REFUSED (nothing written).
2. **Tests** in a NEW `test_demque_inactive_request.py` (pytest; stub names, no network) with exactly these names:
   `test_the_backfill_requests_chunk_the_symbolled_names_in_rank_order_and_every_name_appears_once`,
   `test_every_request_validates_and_carries_the_floor_start_the_frontier_end_and_the_client_need_class`,
   `test_a_name_without_a_symbol_is_left_out_and_counted`.
3. **Report the real build line verbatim**, with the folder count (`pytest data/mdpf/scripts/demque` once). Write the real files only under `.scratch/`.

### ACCEPTANCE

<criterion id="DQ9-t67-AC1" cell_refs="DQ-t-67"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t67_tests.py</invocation><expect>REQUEST-OK</expect></criterion>
<criterion id="DQ9-t67-AC2" cell_refs="DQ-t-67"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t67_real.py</invocation><expect>REQUEST-REAL-OK</expect></criterion>
`DQ9-t67-AC1` -- the three named tests. `DQ9-t67-AC2` -- on the REAL inputs (S3 and the V2 set read only): the build line's counts add up, `requests` is the ceil of `with_symbol` over 300, every file validates with tier 2, need class client, start 2012-01-01 and a trading-day end on or before today, the union of the requests is exactly the symbolled names each once, none is in V2, no account key, two builds are byte-identical.
The check runs the census once and the build twice (about 60 s in all): invoke it under `timeout 260`.

<expected_criteria>DQ9-t67-AC1,DQ9-t67-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `REQUEST-BAD no file ...test_demque_inactive_request.py`; `REQUEST-REAL-BAD inactive_request.py rc=2 ... No such file`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO vendor call, no write to S3, any ledger, the queue, the price store or any pacer state; do NOT write into `org/missions/.../requests/` or into `~/.opal/demque`**; no AWS write; no deploy; no timer. Never print an account number. Build no alarm, monitor or notification. Edit NO existing script: `inactive_request.py` imports them.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W59-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) appended at the end of your own branch's copy of the investigation file below. Do NOT merge `box/dell1` (it is blocked by a foreign row); the issuer unions at the drain.

<paths>
data/mdpf/scripts/demque/inactive_request.py
data/mdpf/scripts/demque/test_demque_inactive_request.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-67`.
<owned_cells>DQ-t-67</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t67-AC1, DQ9-t67-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~59/MDPF_DEMQUE.TO-DQ-t67.inactive-yahoo-backfill-requests.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t67-AC1,DQ9-t67-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the real build line verbatim, the folder count, commits (never an account number).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE a request builder over S3 reads; no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a builder; nothing is drawn or placed.
risk: LOCAL -- code and tests; the placement of the files into the queue is the issuer's later act, under the never-widen pair.
direct_act: false -- a worker order.
</preflight>

Source: Andrew-direct 2026-10-15 via CTO msgs 6105, 6114; the DQ-t-64/65 census (1,071 symbolled of 1,705); decomposition round 9, amendment 29.
