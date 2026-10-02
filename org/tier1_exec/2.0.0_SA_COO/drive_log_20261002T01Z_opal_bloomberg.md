# drive log 2.0.0_SA_COO~H -- 2026-10-02 01Z-04Z, session wind-down (opal_bloomberg)

## tick 41 -- 01:14Z: DRIVE FORWARD -- bbg drain slower than projected (286 uploaded, 543 left at ~60 per upload: the retry_at backoff gated each item <= 1 h) -> issuer reset retry_at=0 on the 543 pending/JSONDecodeError bbg rows (live runtime db, one UPDATE) so the next job-end upload takes them all. wsj job since 22:29Z still fetching (01:14Z); sa upload since 23:52Z.

## tick 41 CORRECTION: the retry_at reset was a NO-OP -- all 542 rows were already past due at 01:14Z (max retry_at < now). Measured: the 01:03Z upload took 273 bbg articles in one pass (receipt 280 uploaded incl. 8 listings, 1 SilverRowError); 558 were not yet due AT 01:03Z and are due now, so the next job-end upload takes them with or without the reset.

## tick 42 -- 01:45Z: NO-OP -- bbg outbox draining (342 uploaded, 487 left; ~60 per 30 min -> ~06Z, inside the 10:00Z gold #4 bound); sa upload since 00:02Z still writing (WAL 01:46Z); wsj job ended 01:34Z (66 done). FT secret updated per Andrew-direct (new version e7cace73, value never written to a file); FT sign-ins still held to 06:00Z, NopeCHA path not to be used without Andrew's word.

## tick 43 -- 02:14Z: NO-OP -- bbg outbox 383 uploaded / 446 left (~40 per 30 min -> ~07:45Z, inside the 10:00Z bound); bbg job since 01:03Z; sa upload since 00:02Z; wsj 69/323.

## 02:2xZ: ANDREW-DIRECT (verbatim): 'yeah give FT a shot ill look at it personally' -- the 06:00Z FT hold is lifted for ONE attempt now; headed Chrome so Andrew can watch; NopeCHA/Kimi path barred (no vendor word); a captcha waits for Andrew's own hand (recorded as human-hand, not a limb-2 pass).

## tick 44 -- 02:45Z: NO-OP -- ~92 FT attempt 3 in flight: an ft job ran 02:41:10-02:41:23Z from the old saved session file, status error, 0 fetches (worker still running; no new commit yet). bbg outbox 421 up / 408 left; wsj 73/335.

## tick 45 -- 03:14Z: FT attempt 3 -- ~92 progress 636e639b78: headed ft sign-in SUCCEEDED; the ft job running from 02:56Z with keep-alive page loads every ~3 min (200s through 03:12Z); 18 min so far, past attempt 2's 90 s death. bbg outbox 453 up / 376 left; sa 29/4100; wsj 79/337.

## 03:2xZ: MSTR 28167 (disk at limit, Andrew /cleanup) acked -- removed my drained worktrees wk-hvst-r32-90 and -91 (0 unmerged commits, 0 tracked changes each; untracked only .scratch + throwaway r34 test Chrome profiles): C: 4.5 GB -> see df. wk-hvst-r32-92 KEPT (live sa runtime + the running FT attempt). Future cells: sparse-cone worktrees only.

## tick 46 -- 03:44Z: FT attempt 3 -- session ALIVE ~48 min after the sign-in (keep-alive page loads logged_in true throughout; 90 ft 200s since 02:56Z, 0 renewals). Job 2 02:56-03:15Z: 49 fetched, 2 stored, 4 locked, ended a NON-auth error (message not recorded; ~92 added an error-capture wrapper). Job 3 running from 03:30Z (28 fetched so far). bbg outbox 484 up / 345 left; disk 34 GB free.

## 04:0xZ: WIND-DOWN (Andrew-direct via MSTR 28178, acked): ai-2 worker stopped (its ft job 3 had ended; ft chrome 0); STOP files set for sa/bbg/wsj drivers + the load monitor (wsj + monitor exited; sa + bbg end after their current job/upload); /canonical-drive cron 079d5acb deleted. OPEN for resume: (1) gold #4 NOT run -- bbg outbox 506 uploaded / 323 pending (+1 SilverRowError, row W91-S19); CTO 28084: run #4 after the drain, else without it before Fri 13:00Z; (2) ai-4 AC2 owes the issuer grade after the drain + status flip; (3) ai-2 open: FT attempt 3 held the session ~48 min with keep-alive (0 renewals); ~92 has UNCOMMITTED ai2_ft_longevity.json + ai2_run_log.txt (worker lane) in wk-hvst-r32-92; a stale worker.lock may remain in the main runtime; (4) round 36 L8 packet not yet compiled; (5) env-var credentials change offered to Andrew, unanswered. Totals: sa 30 names/4,198; bbg 61/830; wsj 80/346; ft 3/62 (+ attempt-3 jobs).
