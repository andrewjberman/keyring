# Drive log 2.0.0_SA_COO~M1 -- 2026-10-17 01Z-02Z (times from `date -u`)

| time | project | limb | what |
|---|---|---|---|
| 01:27Z-01:50Z | MDPF_SECCLASS | EXECUTING (r27), dated wait | Session restart on dell1: registered, watcher re-armed, `/canonical-drive` 30m cron armed at :17,:47 per `org/ref/LIVE_ARMS.md`. Tick 1: runner i-01003b035d2988dfb stopped (23:00:11Z launch), `gold/trigger-pending.json` 404, 0 open calls. Leg G read ahead of the 01:45Z plan (read-only): `SEED22-LEGG ok=False window_dates=15 moved=15 bad=15 tol=250`; row D1-S45 @ddc416b0a5. Tick 2 (01:48Z): byte-identical re-read; versions of `mix_daily_summary.json` bracket one fire (pre 3BY8Etw3... 2026-10-16T05:25:26Z, latest 87CvfcFp... 2026-10-17T00:22:27Z); lots partition unreadable for 13 of 15 dates; row D1-S46 @22b86a9af0. TO-SC-e108b GO NOT given (its hold 2). |
| 02:18Z | MDPF_SECCLASS | EXECUTING (r27), dated wait | Tick 3: state unchanged (runner stopped, trigger-pending absent, 0 OPEN calls, inbox empty, lease FULL). No act owed before the 04:00Z chain writes a third version. |

## Owed next
1. After the 04:00Z chain stops (about 05:30Z), same-shell runner and trigger-pending reads, then `seed22_legg_read.py read --pre-version-id 3BY8Etw3LetRaRFcOofjaAT98PSfp4Z3` against the new latest version.
2. The cash to fixed_income shift of about 36k to 39k per date (D1-S45/S46) is unnamed; it needs a per-security diff of the pre and latest C_06 outputs (surprise-channel owner: the CVO's adjudication). The GO for `MDPF_SECCLASS.TO-SC-e108b` (addressed to `0.7.0_AE_CloudOps~DELL1`, staged) waits on leg G reading as seeded.
3. Round-27 L8 packet (draft @0b8cd2890f, NOT SENT) and round 28 (CTO round-27 analysis; FWD-12 sector writer apply carried).

## Compiler Tools
- Run: `seed22_legg_read.py read` (twice), `aws s3api list-object-versions`, `unblock.py tick`, `drive-mode.py read`, `open-calls.py list`, `comp-find --files`.
- Failed: `comp-surprise` as `python .tools/comp-surprise` (it is a bash script; run it with bash); two Bash calls with `| head`/`| tail` after a comp-find were denied by the rail (R6), re-run without the pipe.
- Gap: `seed22_legg_read.py` prints no per-security detail, so a firm-level class delta cannot be traced to a name without a separate diff.
