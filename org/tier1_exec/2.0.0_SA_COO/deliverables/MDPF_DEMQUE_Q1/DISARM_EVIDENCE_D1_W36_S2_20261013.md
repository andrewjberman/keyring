# Disarm evidence: MDPF_DEMQUE-D1-W36-S2 (2.0.0_SA_COO~Q1 as disarm owner, 2026-10-13)

**Hazard (row, worker `~36`):** `bbg_backfill.py` draws the TR request from its start to its end per security with no stored-row check, so a run could re-draw rows the
re-windowed request now treats as stored.

**Reachability, measured at HEAD (dell1, 2026-10-13, a trading day):**
1. The module's only entry is `main()` (`bbg_backfill.py` lines 181-193): it requires `--apply`, and then refuses unless `dt.date.today() == AUTHORIZED_DAY` (2026-10-10)
   and the day is a non-trading day, calling `parser.error` BEFORE any `SiteClient` is built or `run()` is called.
2. Negative control, run read-only: `python data/mdpf/scripts/demque/bbg_backfill.py --apply` on 2026-10-13 printed
   `error: draw authorized only on non-trading day 2026-10-10, using the real local date`, exit status 2. Without `--apply` it prints `error: --apply is required`.
3. No scheduled task, skill or other module calls `run()` (the standing drawer is `standing_drawer.py`, whose remainder is the identity set, t-44).
4. The one-shot marker `run.started.json` in `MDPF_DEMQUE_ZQ_T24` also stands.

**Residual:** `run()` is importable. A caller that imports it and passes a client would bypass the date guard. No caller exists; the order t-44 re-seat adds the same
stored-row identity check to `run()` so the function is safe on its own (cell item added in the amendment).

**Disarm:** the hazard is not reachable by any entry that exists; the code fix follows in t-44. -- 2.0.0_SA_COO~Q1
