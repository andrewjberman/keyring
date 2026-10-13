# TO MDPF_DEMQUE.TO-DQ-t51 -- round 9 DQ-t-51: the porting test always draws 5 intervals; a length that does not fit is replaced by a drawn length that does; a window under 10 trading days is UNTESTABLE
<to_id>MDPF_DEMQUE.TO-DQ-t51</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~43</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>PORTINTERVALS</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-51` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 15) |
**outcome_ref:** C-QUOTE, C-ROUTE, FWD-6 | **depends_on:** DQ-t-49 (merged @567a058ddb)

---

## WORKER FACE

### THE CELL

CTO ruling msg 4976 on `DQ-t-49` (Andrew said "several" intervals; the 5 stays): **always 5 intervals.** In a short held window each fixed length (1 month, 1 quarter, 1 year) that
does not fit becomes a sha256-drawn length that fits inside the window. Overlap is allowed; the minimum interval is **5 trading days**; every interval must still be within 10 bps.
A window under **10 trading days** cannot hold 5 distinct intervals, so that security stays on Bloomberg as **UNTESTABLE**: a reason, never a FAIL. As built at `567a058ddb`, 182 of 326
securities had fewer than 5 intervals and could never pass; this cell removes that. **No vendor call; nothing drawn.**

**Build** (edit `data/mdpf/scripts/demque/porting_test.py` and its test file; read it at HEAD first, with `lib/trading_calendar.py`):
1. **Interval draw.** For each security, with `N` the number of trading days in its held window `[valid_from, valid_to]`: if `N < 10` the security is UNTESTABLE (no interval, no request
   entry). Otherwise draw exactly 5 intervals, k 0 to 4, from the same `hashlib.sha256(("%s|%d" % (cusip, k)).encode()).digest()` as today: k 0, 1, 2 try 1 month, 1 quarter, 1 year; a length that
   does not fit inside the window (in trading days) is REPLACED by a length drawn from the digest between 5 and `N - 1` trading days (a salted second digest if the first has been used, so
   the replacement is deterministic); k 3, 4 draw a length between 5 and `min(250, N - 1)`. Each interval's start is drawn inside the window so the end also falls inside it; endpoints
   are trading days; overlap is allowed; no interval is shorter than 5 trading days; none starts before the first held date.
2. **Output.** The request as before, plus `"untestable": [{"cusip", "reason": "window under 10 trading days"}, ...]` (CUSIPs and a reason only). The `--build` line becomes
   `{"securities", "testable", "untestable", "intervals_total", "cells", "max_cells_per_security", "need_class", "window_start"}` with `securities` = testable + untestable. A repeated
   endpoint date within a security is one cell (cells count distinct single-day entries). Two runs write byte-identical files.
3. **Comparator.** `compare(...)` keeps its rule (PASS only if every interval is within 10 bps); it never returns PASS for fewer than the security's 5 intervals, and a security listed
   untestable is never given a verdict by it. Add a verdict value `UNTESTABLE` the caller uses for the listed securities.
4. NEW `test_demque_porting_intervals.py` (pytest; stub frames, no network, no S3) with exactly these names:
   `test_a_fixed_length_that_does_not_fit_is_replaced_by_a_sha256_drawn_length_that_fits_so_every_testable_security_has_five_intervals`,
   `test_a_window_under_ten_trading_days_is_untestable_with_a_reason_and_never_a_fail`,
   `test_every_interval_is_at_least_five_trading_days_and_overlap_is_allowed`.
   The existing `test_demque_porting_test.py` tests that pin the old shorter-window behaviour are updated to the new rule and nothing else.

### ACCEPTANCE

<criterion id="DQ9-t51-AC1" cell_refs="DQ-t-51"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t51_tests.py</invocation><expect>INT-OK</expect></criterion>
<criterion id="DQ9-t51-AC2" cell_refs="DQ-t-51"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t51_real.py</invocation><expect>INT-REAL-OK</expect></criterion>
`DQ9-t51-AC1` -- the three named tests. `DQ9-t51-AC2` -- on the REAL index: every testable security has exactly 5 intervals, the cells stay within 10 a security, the UNTESTABLE ones are
listed with the reason, the file is deterministic and valid. Report the count of UNTESTABLE securities, the new cell count and the whole folder `pytest data/mdpf/scripts/demque` once.

<expected_criteria>DQ9-t51-AC1,DQ9-t51-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `INT-BAD no file ...`; `INT-REAL-BAD arms=ints,count,five,cap,untestable_listed`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO Yahoo call, NO Bloomberg call, no write to S3, the ledger, the queue or any pacer state, no AWS write, no deploy, no timer.**
- **Account ids never enter a committed file.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `MDPF_DEMQUE-D1-W43-S<k>`, `fabric` `dell1`, `surfaced_at` =
  `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a check. Rows are APPEND-ONLY. Merge `box/dell1` into your branch (a merge,
  never a rebase; the worker rule against merges does not bind a merge the order directs) before you append rows.

<paths>
data/mdpf/scripts/demque/porting_test.py
data/mdpf/scripts/demque/test_demque_porting_intervals.py
data/mdpf/scripts/demque/test_demque_porting_test.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-51`.
<owned_cells>DQ-t-51</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t51-AC1, DQ9-t51-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~43/MDPF_DEMQUE.TO-DQ-t51.porting-test-always-five-intervals.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t51-AC1,DQ9-t51-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the `--build` line verbatim, the UNTESTABLE count, the new cell count against 2,497, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE a request builder and a pure comparator; nothing is drawn or served.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: CTO ruling msg 4976 (Andrew's porting test, "several" intervals); TO-DQ-t49 merged @567a058ddb; decomposition round 9.
