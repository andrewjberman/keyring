# Drive log -- 2.0.0_SA_COO~S1, MDPF_STRATID, 2026-10-11 14Z (desktop-hk1uu7n)

**archetype:** VALIDATE

Re-instantiated 04:4xZ (session start); watcher re-armed each 30 min; inbox empty throughout. No loop armed (`CronList` empty, no `~S1` row
in `org/ref/LIVE_ARMS.md`). One tick, run at 14:0xZ after the 13:30Z fire.

| UTC | limb | outcome | act |
|---|---|---|---|
| 14:0xZ | L10 wait elapsed (R2 L4) | DRIVE FORWARD | Read the 2026-10-11 13:30Z `mdpf-scheduled-floor` fire (`mdpf-gold-lambda`, stream `2026/10/11/[$LATEST]2ed05a4113`): `global` refused at the cross-axis gate again, the same 5 Opal fixed-income models on 2026-10-09 (`model_value=None`, counts present). Served Global newest is still `2026-10-08.json` (round-1 bytes). **L4 stays UNREAD, not failed.** `r2_run_read.py` FAIL is on those pre-round-2 bytes. |
| 14:1xZ | W2 L3 | NEW FINDING | The 12:52Z backstop DISPATCHED (first dispatch that is not `NOT-YET`; runner `i-02448edb624a7a7cf`, ssm `0385c1be`). Runner log `mdpf_daily_20261011_125228.log`: `STAGE6-REVAMP rc=1 dur=1s` at `ModuleNotFoundError: lib.opal_naming` (taxsma_assets.py:95), so step 6d never ran. Same traceback on the 10-09 run. This is MDPF_TAXSMA-S5 (ARMED, owner `2.0.0_SA_COO~T`, since 2026-09-21). The wait D1-S9 named for L3 is therefore not sufficient. |
| 14:2xZ | row | FILED | `MDPF_STRATID-D1-S10` (BLOCKING, INERT) @1d6976643b, local on `box/dell1` (origin `box/dell1` read e2ac12f98f at 14:15Z does not carry it). |

Not graded: FWD-2, FWD-6, FWD-3's organic arm, Total/Client, CTO-half conditions 1 and 5 (each needs a Global object from the round-2 code).

Waits:
- L4 and R2 L4: the first fire that writes a Global object for a date on which 49F, Inflection and Cottonwood all carry values (expected
  2026-10-12 13:30Z). Then `r2_run_read.py --pre-client 268516586.73`, L4 closed, the L8 packet section 6, the packet to `3.0.0_SA_CVO`.
- W2 L3 runner-log half: owned-elsewhere disarm of MDPF_TAXSMA-S5 (the runner tree gets `lib/opal_naming.py`, or the import resolves another
  way), then one dispatch whose log carries a 6d line. Not this project's write surface; not chased.

Issuer defects this tick:
- D1-S10's `surfaced_at` reads 14:20:00Z, stamped ahead of the 14:15Z clock read. The row gate refuses an in-place edit of a committed row
  (correct), so it stands; the commit time is the authority.
- A `.tools/aws s3 ls` of the runner's `code/` prefix was denied by the rail (RUN NEXT `comp-pipescript deployed --firm mdpf`); that call
  was the right one and answered the question.

## Compiler Tools

| tool | result |
|---|---|
| `comp-pipescript deployed --firm mdpf` | assets_gold Cottonwood scripts MATCH; read for the lib-on-runner question, does not list `lib/` |
| `r2_run_read.py --pre-client 268516586.73` | R2-RUN-READ FAIL on pre-round-2 Global bytes (grades nothing) |
| `surprise-row-gate` / `safe-commit.sh` | 1 new row passed; a same-id edit was refused as designed |
| gap | no comp-tool names which fire-run date a Global key belongs to; read from the log streams by hand |
