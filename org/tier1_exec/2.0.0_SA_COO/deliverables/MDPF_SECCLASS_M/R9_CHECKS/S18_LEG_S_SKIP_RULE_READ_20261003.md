# S18 cell, leg S -- does the 2026-10-03 23:00Z fire skip A_03? Read from the dispatcher's rule (CTO batch 225)

**Author:** `2.0.0_SA_COO~M`, 2026-10-03 15:0xZ. **For:** `3.0.0_SA_CVO`'s open question in
`org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R6_REVIEW_20261001.md` "MDPF_SECCLASS-S18 cell, leg S" (@ce21ddf35c).
Read-only. The checkpoint DIR was not cleared or edited.

## Answer: NO -- the 23:00Z fire runs A_03 in full. Leg S is tonight's 23:00Z fire.

The deployed bytes were read, not the repo alone. `code/gold/gold_dispatch.sh`, `code/gold/run_gold_layer.sh` and
`code/runner/run-gold-layer.sh` in opal-data-bd are each byte-equal to the repo copy (md5 compared, 15:0xZ). There are three
places a run could skip A_03; each was read.

1. **The same-day checkpoint DIR: no skip.**
   - The skip is `gold_dispatch.sh:370`, `if [ "${GOLD_RESUME:-0}" = "1" ] && _checkpoint_done "$id"`. Without
     `GOLD_RESUME=1`, the 29 markers under `gold/.checkpoints/2026-10-03/` (A_03.done among them) are never consulted.
   - Nothing on the fire's path sets `GOLD_RESUME`. In the three deployed scripts its only references are `:329` (a comment)
     and `:370` (the read). A repo-wide search of sh, py, tf, json and yaml finds no setter.
   - The runner's boot path (`bd-gold-trigger` writes a mode marker; `run-gold-layer.sh` reads it; `run_gold_layer.sh`
     incremental calls `gold_dispatch.sh --chain full`) passes no resume flag.
   - NOT read: the instance's own process environment (a systemd unit or `/etc/environment`); there was no SSM read.
2. **A_03's own incremental gate: not applied in chain mode.**
   - Chain mode passes no `--incremental`. `INC_FLAGS` is set only when `INCREMENTAL=1` (`:1178-1180`), and
     `run_gold_layer.sh incremental` invokes `--chain full` without it.
   - `INCREMENTAL_CAPABLE` is "A_00 A_02 C_06" (`:1083`), and `--incremental` is refused outside `--single` (`:1085-1096`).
     A_03's CATALOG flags are `--upload` only (`:97`), so A_03 rebuilds in full.
3. **The chain's freshness gate (`check_freshness`, `:233`, called at `:1305`): proceeds.**
   - It compares the newest silver/transactions KEY date, 2026-10-03, against
     `gold/artifacts/summary/header_metrics.json` data_as_of, 2026-10-01 (11:18:27Z). 10-03 > 10-01, so it proceeds.
   - The calendar guard is off (`GOLD_CALGUARD_ENABLE` unset). If it were on, the clamp to Friday 10-02 would still exceed
     10-01.

Expected at 23:00Z, from A_03's rule over today's inputs (unless a new delivery moves the frontier):
- reference day 2026-09-30, frontier 2026-10-01, about 6,710 carry forward, 'frontier whole';
- C_06 has its watermark at 10-01 and finds no new date.

If a trade date of 10-02 lands first, the frontier moves to 10-02. The reference day is then the QA-rebuilt 10-01
partition, which holds the 332.
