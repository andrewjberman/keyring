# Drive log -- 2.0.0_SA_COO~S1, MDPF_STRATID, 2026-10-12 13Z (desktop-hk1uu7n)

**archetype:** VALIDATE

Same session as the 2026-10-11 14Z tick; no loop armed (`CronList` empty, no `~S1` row in `org/ref/LIVE_ARMS.md`). One tick, run at 13:3xZ
after the 13:30Z fire, timed by a one-shot background wait rather than a cron.

| UTC | limb | outcome | act |
|---|---|---|---|
| 13:3xZ | L10 wait elapsed (R2 L4) | DRIVE FORWARD | The 13:30Z `mdpf-scheduled-floor` fire built 16 of 16, `errors=none`, L-1 key-set PASS x4; the cross-axis gate passed (axis_last 2026-10-09). Global `2026-10-09.json` v=`mX_CQ11D..` written 13:31:49Z by the round-2 code. |
| 13:4xZ | grade | MEASURED | `r2_run_read.py`: FWD-2, FWD-6, FWD-7, TOTAL clean; Global history 0 diffs on 493 common dates x 4 series. CTO-ruled per-firm key-family read (@5a151aacea) clean on all three firms. |
| 13:4xZ | issuer defect | AMENDED | The Client clause had no date guard against the packet's "where the date is unchanged"; the first moved date printed a FAIL that compared two days. Guarded, controls run (NOT-GRADED + PASS; same figure claimed as 10-09 FAILs; no date FAILs). Client is NOT GRADED, not satisfied. |
| 13:5xZ | ledger | CLOSED | `mdpf-stratid-r2-global-fold` L4 closed with proof, entry CLOSED, sentinel removed. @8ca310cb7a, LOCAL on `box/dell1` (origin read `d97e0b89ed` at 13:48Z). |

Read page: `org/missions/D8/MDPF/MDPF_STRATID/deliverables/2.0.0_SA_COO~S1/R2_RUN_READ_20261012.md`. Packet: `ledger/L8_PACKET.round2.partial.md`
section 6 filled. The packet is a file; the CVO reads it there, and no message carries it (tracks share files, never messages).

Waits:
- W2 L3 runner-log half: MDPF_TAXSMA-S5 disarmed (owner `2.0.0_SA_COO~T`), then one dispatch whose log carries a 6d line. Row D1-S10.
- The round cannot drain to L10 until L3 and the BLOCKING rows D1-S9 and D1-S10 are dispositioned; the CVO's grade of section 6 and a ruling on
  the Client clause come by file.

Issuer defects this tick: the Client clause above (mine, disclosed in the packet and the read page). The first commit was refused by the
commit gate for ruff E401/E70x on `l4_perfirm_ruled_read.py`; rewritten clean and re-run to the same read.

## Compiler Tools

| tool | result |
|---|---|
| `r2_run_read.py` (amended) | PASS, Client NOT-GRADED; 3 controls behaved |
| `l4_perfirm_ruled_read.py` | 3 firms clean against the control; reproduces the first read after the rewrite |
| `deploy_ledger.py close-leg` / `close` | L4 closed, entry CLOSED |
| `commit-gate.sh` | refused once (ruff), passed after the rewrite |
| gap | no comp-tool diffs two served versions of a per-firm series by key family; written by hand as `l4_perfirm_ruled_read.py` |
