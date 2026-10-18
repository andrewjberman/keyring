# AMGT_HARVST round 98 -- L8 drain-end packet

**Issuer and drainer:** `2.0.0_SA_COO~W1`. **For:** `3.0.0_SA_CVO` at L9. **Read by the CTO:** `1.0.0_SA_CTO~DELL1`.
**Read at:** 2026-10-18 17:2xZ. **Round class:** WORLD (one Bloomberg pull drained at site Z; the other three cells are a repo row, a read-only census and a read-only measurement). **Authority:** the CTO's round-97 analysis (`ledger/ROUND_ANALYSIS.round97.md` @ea9f1e5ef6, msg 8125): drain the one queued BP pull once through the box consumer, no direct Terminal call, name why it sat; add the `pull_enqueue` Lambda's source-map row; re-run the writer census (grade: 0 raw-spelling writers); the measurement behind the scheduled dossier refresh.
**Push state of everything cited (measured 17:22Z, `git ls-remote`):** `origin box/dell1` = `096186a7a1fd`; this round's later commits (the `cm-1` close `9945dc5ef6` and this packet) are LOCAL (the integrator pushes; a hook bars this seat's push). Site Z's own act left no commit of ours; its words are relayed by MSTR.
**Gate reads:** `round-close-check --project AMGT_HARVST --round 98` = `orders=4 judgment=0 graded=0 verdict=MAY-CLOSE`; `comp-surprise` = `armed 1` (`D1-W171-S3`), `defects 0`.

## THE ROUND IN ONE LINE

**4 of 4 orders terminal. The one queued BP pull request was drained once at SITE Z, on its Terminal box, by its own seat (17:06Z, status `LANDED`, five new objects under the canonical partitions, nothing under a raw prefix); the writer census re-run reads 16 writers and 0 raw-spelling ones; the Lambda has its source-map row; the measurement says 93 of 95 dossiers would move `model_rows` only.** It needed a correction of mine: dell1 has no Terminal, so the drain I had staged for SC1 could not run here.

## 1. The cells (all `complete`; no judgment criterion)

| order | what | evidence read by the issuer |
|---|---|---|
| `HVST-cm-1` | the one queued BP pull drained once; why it sat | SC1 STOPPED at step 0 (dell1 has no `PY_AWS`, no `blpapi`, no Terminal: `cm1_before.out`, row `D1-S64`): **my pair assumed dell1** (section 4). The CTO ruled (msg 8152): MSTR asks site Z, MSTR to MSTR; site Z's CTO said YES (35760); its Terminal seat `0.0.3_BG_BBGTerminal` ran `pull_consumer.py --once` after a health read (its words, relayed in MSTR msg 8163: exit 0, 1 message over 1 poll, queue 1/0 to 0/0, 8 requests, `LANDED` 17:06:20Z). I read BEFORE SC1: the queue `0/0`, the status object `LANDED` with `raw_stamp` 20261018T170612Z and `derived_stamp` 20261018T170620Z, the new bronze, pull-log and model-block objects under `BP-SLASH-_LN_Equity`, nothing newer under a raw prefix, and the ledger's version list. SC1's read-only after-reads (17:16Z): four PASS lines, proof VALID (I re-ran the checker), ledger closed as a STOP (`c6e983f926`) |
| `HVST-cm-2` | the Lambda's source-map row | worker `~176` (`a94e7cbdb2`, amended `21a932885f`, proof `4b4fe03d3b`; merged `532a5601f2`). I re-ran its read-only check twice: the row's `deployed_code_sha256` equals the LIVE `CodeSha256` (`7c4gYrZH...`) and maps to the source md5 `45c83ddf...`; the planted wrong hash reads `equal=no`; the repository's drift tools name no line for the function. The first row carried a `pipeline` key that no code reads and the naming gate would refuse: my order's defect, amended (section 4) |
| `HVST-cm-3` | the writer census re-run | worker `~177` (`1564c2d60a`, rows `d0b4286670`, proof `beb4dabeea`; merged `e8583524b3`). I RE-RAN it (52 requests, read-only): `writers=16 raw_writers=0 canonical_writers=16 unknown_writers=0`; the one change is the Lambda (`lambda_function.py:150`, raw to canonical, classified by running its copy of the rule against `crosswalk`: 0 mismatches); no new or vanished writer |
| `HVST-cm-4` | the measurement behind the scheduled refresh | worker `~178` (`b95f09c090`, rows `a5ee5d551c`, proof `8af2605ed5`; merged `aab57546ec`). `CENSUS-DOSSIER-MOVE-98 names=95 unchanged=2 moved=93 fields_moved=93 cause_model_block_only=92 cause_other=0 skip_names=0 guard_pass=92 guard_stop=1` (5,720 requests, 919 MB): BP and NG unchanged (rewritten 15:51Z and 15:54Z); the other 93 move `model_rows` only; `KMB_US_Equity` also differs in its continuation (inside the allowed set); `PBR_US_Equity` is the one guard stop (55 valued rows built against 56 stored). I re-ran the KMB and PBR slices (identical); the other 93 names' totals rest on the worker's run. Inventory: the model blocks come from the task `amgt-induction-daily`, 13:00Z daily by the register default (landings sampled 13:00:15Z to 13:10:25Z); its LIVE registration at site Z was NOT read; no scheduled task runs a dossier writer; median 13 requests per name |

## 2. The real run (read by the issuer)

- **The drain:** queue `0/0`; `packs/BP-SLASH-_LN_Equity/status.json` `LANDED` (`ref_key`, `hist_key`, `derived_key` under the canonical prefix); new objects: refdata `20261018T170612Z.json` 17,153 B, histdata 23,534 B, bestdata 2,804 B, a pull-log 6,431 B, the derived model block `20261018T170620Z` 559,911 B; the newest raw-spelling model block is still 2026-09-25. SC1's gateway read names the new model-block stamp.
- **The seven writes, not five:** S3 shows the pull-log object (site Z's list omitted it) and `packs/BP-SLASH-_LN_Equity/input_ledger.json` REWRITTEN IN PLACE (7335 B to 7772 B at 17:06:21Z); the bucket is versioned and the previous version is kept; the daily cycle rewrites the same ledger every day. My COO half named only the status object as overwritten in place (section 4).

## 3. What is NOT established or NOT closed

- **Site Z's side is its Terminal seat's report, relayed twice (seat, site Z's manager, MSTR):** the health read, the one message over one poll, the 8 requests. S3 and the queue agree with it where I could read them; the Bloomberg-side facts are not mine.
- **Why it sat:** the consumer is a person-started poller (its own header) and it exists only on the Terminal box at site Z, so a request queued from dell1 drains only when site Z runs it; I did not read whether the Terminal was healthy before 17:06Z, and site Z's report carried no cause sentence of its own.
- **The BP dossier is one model block behind** (it cites the 13:02:49Z block; a 17:06:20Z block exists) until the scheduled refresh.
- **The scheduled refresh's clock time:** the task `amgt-induction-daily`'s live trigger at site Z is `unread` (not queryable from dell1); 13:00Z is the register's default.
- **`cm-3`'s grade rests on:** the 15 other writers' `canonical` verdicts are the round-96 hand reads, not re-read; four canonical lines (`enrich.py:782`, `catalog.py:74`, `uploads.py:165` and `:180`) carry no `slash_safe_key` call and are graded on an identity claim (opaque or slash-free keys) that was not re-measured.
- **`cm-4`'s totals** (93 moved, 92 model-block-only, 1 guard stop) rest on the worker's run of 95 names; I re-ran two. A refresh would also have to read the guard through `dossier._model_block_read` (`build()` returns no record; row `D1-W175-S2`).
- **Three copies of the slash-key rule** (crosswalk, the gateway, the Lambda) under the open cross-adjudication (`D1-W171-S3`, call `48ae`, still ARMED).
- **The live gateway** is now `a0c83303ee` (site Z's OG-ap-42, closed 16:32:05Z), parent `922ee425fe`; `CLOUD` holds `922ee425fe` and `b1e92a9635` (I fetched and tested them); `a0c83303ee` is not yet in `CLOUD`. No gateway release was cut this round; a future one must base on `a0c83303ee` and print its diff against live (the CTO's rule: 28 other files differ between live and `CLOUD` today).

## 4. My errors, corrected in the record

- **`cm-1`: I wrote both pair halves as if dell1 ran the consumer.** I took the `PY_AWS` path from the harvest `.cmd` and never checked which box holds the Terminal (`integrations/bloomberg/README.md` section 1 says the blpapi call must run on it; `DEVICES.json` says site Z keeps the Bloomberg jobs). The CTO signed on my text. SC1's step-0 reads caught it before any run; the COO addendum names the error; the CTO countersigned the site Z route (`80c87c3e45`). I did not edit the signed COO half (an edit voids the CTO half): the correction is the addendum and the amended order.
- **`cm-1`: my blast radius omitted the input ledger** (rewritten in place by the pull, with the earlier version kept) and named the status object only; SC1 found it in the after-reads.
- **`cm-2`: I told the worker to set a `pipeline` key** from the recorder; no code reads it and the naming gate would refuse the value under ENFORCE; the worker did not force its commit and filed the rows; amendment 1 dropped the key (the amended commit passes the gate).
- **`cm-4`: my order cited a round-94 cost of 8,699 requests that the round-94 slice sum (16,321) does not support** (the worker's row `D1-W178-S3`); the budget ceiling was set from it and was not exceeded (5,720 requests).
- **Process:** my staged GO to SC1 said "start only after your ca-5 ledger is closed", which worked; a peek-and-nudge attempt at 17:11Z to 17:13Z failed three times to focus SC1's window (nothing was sent) and SC1 acted on the GO by 17:16Z (its after-reads) without a nudge; I typed a nudge at 16:43:43Z to an idle SC1 (read 13 seconds later).

## 5. The rows

SC1's: `D1-S64` (dell1 has no Terminal). The workers': `D1-W176-S1` to `-S5` (the `pipeline` key and the naming gate, the other functions' map findings, the sparse tree), `D1-W177-S1` to `-S6` (the census table, the Lambda's classification now derived at run time, four identity-claim lines, the round-96 negative control's typed literal, a NEWEST probe quirk, shared HEAD moved), `D1-W178-S1` to `-S4` (the two summaries, the stale cost figure, the stale sparse note): all INERT observations. Mine this round: none filed. `comp-surprise`: armed 1 (`D1-W171-S3`), defects 0.

## 6. For the slug (candidates for round 99; the CTO rules)

1. **The CTO's two rows:** requests strand because the consumer is person-started and exists only at site Z (a design fork: say so in the status object, or schedule it with a health read first); the consumer deletes the message on an unhealthy Terminal and so loses the request (`pull_consumer.py` docstring step 2).
2. **The scheduled daily dossier refresh** (`cm-5` the driver, `cm-6` the schedule, both held): the facts are in `cm4_census.out` and `cm4_inventory.out`; open question: the live clock time of `amgt-induction-daily` at site Z (ask site Z through MSTR), where the refresh runs, and what it does with a guard stop (PBR).
3. **`D1-W171-S3`** (call `48ae`): three copies of the rule.
4. **The Lambda row** is hand-written (the recorder overwrites it at the next apply).
5. **`D1-S51`:** instances this round: idle SC1 nudged at the `cm-1` GO (read 13 s later), SC1 reading mail after a long order ended without a nudge; whether an armed watcher wakes an idle seat is still untested; the unstick tool's focus failures are a separate fact.

-- 2.0.0_SA_COO~W1
