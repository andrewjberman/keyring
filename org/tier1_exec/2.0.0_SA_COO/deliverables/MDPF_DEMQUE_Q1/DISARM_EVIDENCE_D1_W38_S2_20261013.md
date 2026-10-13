# Disarm evidence: MDPF_DEMQUE-D1-W38-S2 (2.0.0_SA_COO~Q1 as disarm owner, 2026-10-13)

**Hazard (row, worker `~38`):** `redraw_stale --apply` reset pacer entries BEFORE the need-class refusal and then enqueued nothing, leaving the pacer reset with no request.

**Fix, merged @6f6a61123b (t-45):** `redraw_stale.request()` declares `need_class` client and `window_start` (floored at 2012-01-01) and validates before any write; `main` validates
BEFORE `reset_pacer`. A new test (`test_a_refused_request_resets_no_pacer_entry`) proves a refused request resets no entry.

**Measured at HEAD after the merge (shared tree, read only):** `demand_queue.py --check-declared ~/.opal/demque/queue` printed `{"accepted": 7, "checked": 7, "refused": []}`; the same over
`requests/` printed `{"accepted": 2, "checked": 2, "refused": []}`; folder `pytest data/mdpf/scripts/demque` read 164 passed, 0 failed. `redraw_stale --apply` was NOT run.

**Disarm:** the hazard's order of operations is removed in code, covered by a test that failed before the fix and passes after it. -- 2.0.0_SA_COO~Q1
