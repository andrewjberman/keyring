# Drive log 2026-10-20 12Z, 2.0.0_SA_COO~O, NFRA_OPLGTW round 47 (host opal_bloomberg)

- 12:05Z: grant orders `OG-gv-1`, `OG-gm-1`, `OG-gc-1` committed STAGED (`983573280e`, ENRICH-R47-F/G/H, decomp A5-A7); Phase A GOs sent to `0.7.0_AE_CloudOps~NFRA1` (one message per order).
- 12:17Z: NFRA1 reports `OG-rl-17` C1 not computable (the audit lake has one end timestamp per call, no start or duration); proxy: 13 calls ended in one second. Asked the CTO to rule.
- 12:27Z: CTO ruled C1 (msg 36195): the measured peak is at least 13, so `MAX_INFLIGHT` moves to 26, `QUEUE_WAIT_S` stays 20.0, new `release_sha`, all three halves re-sign, window 2026-10-21 06:00Z kept. Round 48: a call start or duration field in the audit record.
- 12:45Z: `OG-mg-4` cut (`1ed22ed869`, ENRICH-R47-I, decomp A8), worker `~174` spawned. `OG-rl-17` text and checks `mg3.AC1`, `rl17.AC2` moved to 26.
- 12:49Z: NFRA1 Phase A findings ruled (row Z-S434, `e79820bfb6`): `Z-S431` Andrew's download operation unchanged (gv-1 continues); `Z-S432` the `client_*` tools cannot be admitted by a `person_access` record (gc-1 closes on facts; CTO ruled the per-firm client grant a round-48 cell, msg 36202); `Z-S433` Menachem has no verified identity record (gm-1 superseded for round 47, re-cuts in round 48).
- Open: worker `~174` (committed `72bc4026fb`, proof pending); NFRA1 on gv-1 ask and gc-1 AC1; `OG-rl-17` re-cut and re-sign after `OG-mg-4` drains; `OG-rl-18` after `OG-rl-17` CLOSED.
- All commits are LOCAL on `box/sitez` (push state: ls-remote not read).
