# Never-widen COO half -- C_06 re-derives B_00's correction window on every fire (cell SC-e-97, rows MDPF_SECCLASS-D1-W83-S5 and D1-W80-S4)

**Signer:** `2.0.0_SA_COO~M1`, dell1, 2026-10-12 ~13:3xZ. **Request:** `NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md` in
this folder (worker `0.9.0_WK_MDPF_SECCLASS~86`, with issuer amendments 1 and 2), drained to `box/dell1` @772b5c9f02 (build commit `77849c4924`).
**Ruling it serves:** CTO round-22 analysis section 2 (@d24cc0d6ad's slug, msg 4333): ruling (a), a ROLLING re-derive over the window the producer
itself corrects, under its OWN never-widen pair because it moves served figures on a partner-facing page; writers counted, the expected move read from
the rule, rollback the prior objects and the gold objects by version.

## What this half covers

Deploy ONLY two files to `s3://opal-data-bd/code/gold/`: `C_06.client_mix_timeseries.py` and `D_04.client_portal_summary.py`. No lib file, no
`gold_dispatch.sh`, no D_03, no table, no watermark and no data key rides it. The data the NEXT fire rewrites is named in the request's blast radius
and bounded by its per-date table.

## Read at signing (issuer, 2026-10-12 ~13:3xZ), each re-run here, not taken from the request

- **Served = base, both files.** At the issuance base `028fab8273` the md5 of C_06 is `2e35d043163cc18b135d7698cf11dc56` and of D_04
  `9d083669159ee8875b6489dea4fb2e37`; `head-object` now reads the same two ETags (C_06 VersionId `zjQmOYVVYTSGOWLFQ0P33vVeWkwp4_eT`, LastModified
  2026-10-12T09:55:03Z; D_04 VersionId `ap.CyBT8aJijz5kWFsSNjEFU99itbXED`, 2026-10-12T06:18:41Z). The only commit to either file since the base is the
  worker's `77849c4924`, so the deploy delta is exactly this cell.
- **The built bytes:** the repo files at `box/dell1` HEAD, md5 C_06 `f847d8d105025ffbee94b1aa5092faf6`, D_04 `43a5d613ca9292329278573038f14158`.
  `gold_dispatch.sh` is NOT in the act: served ETag `f568d11bbf074aaec8f06a01ee13dd2e` equals the repo md5, and it is the rule's runtime source.
- **The rule, re-run independently.** The B_00 CATALOG line is `B_00|B_00.canonical_holdings.py|--upload --force-recent-days 14`
  (`gold_dispatch.sh:99`); B_00's default is 0 (`:1032`). Over a live listing of `gold/canonical/holdings/` (2,474 dated partitions, printed), B_00's
  arithmetic (anchor = newest date, cutoff = anchor minus N calendar days, `>=`) gives anchor 2026-10-09, cutoff 2026-09-25, **15 window dates
  2026-09-25..2026-10-09**, equal to the record.
- **The criteria, re-run here at trunk:** `ROLLING-REDERIVE ok=True` (six of six), `ROLLING-WIRING ok=True` (six of six), `HALF-REQUEST ok=True
  sections=7 of 7 unsigned=True writers=True`; the three sibling-and-new C_06 test files 30 passed; the worker's negative controls read as designed
  (a typed `FORCE_RECENT_DAYS = 14` refused; a signed half and a missing section refused).
- **Writers, re-counted by Grep at trunk:** `platinum/firm/mix_summary.json` N = 1, `D_04.client_portal_summary.py:578` (docstrings only elsewhere);
  `gold/views/mix_daily_summary.json` N = 1, `C_06` `_write_mix_summary` (def :663; called at :1018, the SC-e-91 pass, and :1359, the build); the
  relationship JSONs and views N = 1 function each, `_write_relationship_json` (def :591) and `_write_relationship_views` (def :607), four call sites
  each (:533/:549 the orphan visit, :981/:996 the SC-e-91 pass, :1164/:1177 the merge, :1297/:1302 the full build). The request's line numbers for C_06
  after :422 are six lines higher than trunk (amendment 2 removed the S3 branch); read the numbers above.
- **The move, from the record, not a typed point figure.** The served firm Unclassified (D_04's rule) falls from $76.26M, $75.96M, $150.43M,
  $152.42M, $153.00M, $148.22M and $140.16M on 2026-09-30..2026-10-06 to $53,010 / $43,081 / $1,924 / $1,927 / $1,930 / $0 / $0, and from $998,763 /
  $972,621 / $1,846,333 on 10-07, 10-08, 10-09 to $32,455 / $8,030 / $883,483; five days 09-25..09-29 rise by about $10.1k each. The class dollars
  move into equity, structured and the other classes of the rebuild. The Unclassified remaining is what no classifier places (SC-e-98: 32
  blank-ticker structured notes at 2026-10-09, $883,483.05 of which $210,486.42 lie outside every stored list).
- **Cost, accepted as measured with its limits:** the 15-date re-derive from this seat took 735 s cold and 632 s warm, a full dry run of the build
  752.7 s, 3,274 of 3,793 relationships rewritten, 13,096 keys, 8.87 GB on a first fire; 3,793 relationship reads on a fire with new partitions and
  7,586 on a window-only fire (the window pass plus SC-e-91's retained pass). These are from a laptop over the internet; the runner is in-region, so
  they are upper-ish bounds, not runner measurements, and the STOP rule below is what bounds the runner.

## SIGNED, for the two named files, with conditions

1. **Named files only, digest-gated, base re-read at apply time.** The built bytes are md5 C_06 `f847d8d105025ffbee94b1aa5092faf6` and D_04
   `43a5d613ca9292329278573038f14158`. At apply time the served C_06 must STILL read ETag `2e35d043` and D_04 `9d083669` (another ship in between
   means the delta is not this cell: STOP and re-base). After the ship each served ETag must equal its md5; any other key moved under `code/gold/`
   (all keys, pre and post, denominator printed), including `gold_dispatch.sh`, is a STOP with a same-session restore by VersionId.
2. **Order of acts: SC-e-91's leg G first.** The ship waits for the issuer's GO, which is not given before the ledger
   `secclass-e91-c06-retained-unclassified-sc1-20261012` is CLOSED (both of my reads done: the Reach range on the first post-SC-e-91 fire and the
   second fire's idempotence), so that the two causes are never confounded on one fire.
3. **Leg P before the next BD fire:** enumerate the current VersionIds of `gold/views/mix_daily_summary.json`, `platinum/firm/mix_summary.json`,
   `gold/views/firm_composition.json`, `gold/artifacts/firm_mix_views.json`, `gold/artifacts/firm_mix_views_daily.json`, the advisor
   `gold/entities/advisors/{id}/mix.json`, `mix_daily.json`, `mix_timeseries.json`, every `gold/entities/clients/{rid}.json` and `{rid}_views.json`
   and the legacy `gold/client_timeseries/{rid}.json` copies, into a deliverable with the page count and key count printed. This is the data-side
   rollback handle: the first fire rewrites existing keys.
4. **Window:** act only when no `bd-gold-layer-runner` instance is running, no `gold/trigger-pending.json` waits in `opal-data-bd`, and not inside a
   BD fire; read the runner state in the SAME shell as the deploy. Fires are `bd-gold-trigger` launches (04:00Z nightly, 23:00Z fallback Monday to
   Saturday, and event-driven launches).
5. **Runtime STOP rule:** read C_06's wall time and the chain's launch-to-stop from the runner telemetry for the first post-ship fire, beside the
   04:00:46Z fire's (at least 7,766.7 s, about 2h19m) and beside SC-e-91's first fire; if the chain runs more than 30 minutes longer than the
   pre-ship chain, STOP and restore both code objects by VersionId in the same session. Also read the C_06 log: a line `C06-ROLLING-RULE-UNREADABLE`
   means the sibling `gold_dispatch.sh` was not beside C_06 and the build was a no-op; that is not a harm but it is a finding I carry to the CTO
   before the next fire (the act did not do what the pair names).
6. **Leg G is the issuer's, after the first post-ship fire, four reads:**
   (a) for each of the 15 window dates, the served firm class dollars (Unclassified by D_04's rule) equal an independent rebuild from the partition
   version C_06 read (LastModified at or before that run's start) within $250, and no class appears outside the canonical set; a date beyond the bound
   is a STOP and the code rollback;
   (b) `restated_through` reads `2026-09-25` on `gold/views/mix_daily_summary.json` and on `platinum/firm/mix_summary.json`;
   (c) a date OUTSIDE the window (2026-09-24 or earlier) in a relationship JSON, and a ticker-with-row control, are byte-equal to leg P;
   (d) the SECOND fire rewrites 0 relationship keys and leaves `mix_daily_summary.json` unchanged (LastModified counts printed).
   The D_03 period bars (the Q3 and September 2026 bars at end date 2026-09-30; Q4, October and the 2026 annual bar at 2026-10-09) are read before and
   after and printed beside the per-date table; their move is inferred in the request and is MEASURED here.
7. **Rollback per key:** the two code objects by the prior VersionIds read at apply time (today `zjQmOYVVYTSGOWLFQ0P33vVeWkwp4_eT` and
   `ap.CyBT8aJijz5kWFsSNjEFU99itbXED`), and the data keys by condition 3's VersionIds. A code rollback restores behaviour, not content a fire already
   rewrote; restoring the 3,274 rewritten relationship JSONs and their views is a bounded VersionId copy.
8. **What this act does NOT do, stated so neither half is read as more:** it places no class for the dollars no classifier places (they stay
   Unclassified, listed by SC-e-98); it does not touch a date older than 2026-09-25; it adds no sentence to the page (a visible statement of the
   restatement is a portal change and, on a client-facing page at PROD, waits on Andrew); it does not change the classifier or B_00.

The CTO half is separate and is asked on this record, with the per-date table and the Q3 bar as the sized move.

`2.0.0_SA_COO~M1`
