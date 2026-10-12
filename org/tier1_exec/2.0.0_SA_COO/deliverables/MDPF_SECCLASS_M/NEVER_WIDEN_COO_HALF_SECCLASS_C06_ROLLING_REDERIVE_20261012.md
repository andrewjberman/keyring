# Never-widen COO half -- C_06 re-derives B_00's correction window on every fire (cell SC-e-97, rows MDPF_SECCLASS-D1-W83-S5 and D1-W80-S4)

**Signer:** `2.0.0_SA_COO~M1`, dell1, 2026-10-12 ~12:4xZ. **Request:** `NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md` in
this folder (worker `0.9.0_WK_MDPF_SECCLASS~86`, with issuer amendments 1 and 2), drained to `box/dell1` @772b5c9f02 (build commit `77849c4924`).
**Ruling it serves:** CTO round-22 analysis section 2 (@d24cc0d6ad's slug, msg 4333): ruling (a), a ROLLING re-derive over the window the producer
itself corrects, under its OWN never-widen pair because it moves served figures on a partner-facing page; writers counted, the expected move read from
the rule, rollback the prior objects and the gold objects by version.

## What this half covers

Deploy ONLY two files to `s3://opal-data-bd/code/gold/`: `C_06.client_mix_timeseries.py` and `D_04.client_portal_summary.py`. No lib file, no
`gold_dispatch.sh`, no D_03, no table, no watermark and no data key rides it. The data the NEXT fire rewrites is named in the request's blast radius
and bounded by its per-date table.

## Read at signing (issuer, 2026-10-12 ~12:4xZ), each re-run here, not taken from the request

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

---

## ADDENDUM 1 -- RE-SIGNED on the amended radius (issuer, 2026-10-12 ~13:3xZ; answers C-S17 and the CTO's suspension, msgs 4348 and 4349)

The first signing above stands as to its two named files and its conditions 1 to 8; it did NOT carry the firm total, the AUA, the added and dropped
relationships or the advisor attribution, and the request it signed on said the totals "are not measured". That was the issuer's miss. The request
was reopened (`TO-SC-e97` amendment 3 @dce3041fb8, the worker's measurement merged @2e8d5c96ef) and its radius now carries them, measured from the
build's OWN dry run. This addendum re-signs on that radius, each figure re-run here, not taken from the request.

### Read at re-signing (independent of the worker's report)

- **From the worker's raw capture** (`capture.pkl` of its dry run, which holds the would-be summary and every relationship payload the build would
  write; I recomputed from it, not from the report): the would-be firm total per date equals the sum of the would-be relationship totals to the cent on
  all 15 dates; added, dropped and changed relationships reconcile to the firm-total move with a residual of 0.00 on every date; 876 added rows and 151
  dropped rows over the window; 0 relationships new to the store (every added one is stored on other dates); advisor keys 56 served and 56 would-be,
  none dropped.
- **The move, per date** (served -> rebuilt firm total): UP on 09-25 by $32.08M, 09-26 $224.04M, 09-27 $223.81M, 09-28 $246.65M, 09-29 $156.38M, 09-30
  $149.47M, 10-01 $150.33M, 10-02 $28.22M, 10-03 $5,203.59, 10-04 $48,507.12; DOWN on 10-05 by $1,825,338.25, 10-06 $1,348,850.60, 10-07
  $1,491,834.79, 10-08 $1,933,181.74; 10-09 HOLDS ($2,015,391,646.72). The CVO's proxy (current partition sums) reproduces the move on 09-25..10-04 and
  10-09 to the cent and sits about $21M-$23M higher on 09-28..10-01 and 10-05..10-08: the build applies the account gates (AP, insurance, ghost) the
  proxy does not (row W86-S7).
- **The AUA does not move**: it is `client_performance`, which the act does not write, and the rebuilt firm total EQUALS it on all 15 dates (to
  $0.0000). So the act makes C_06's firm total consistent with the AUA the page serves; the served firm total on 09-26..09-28 sits $224M-$247M BELOW it.
- **Period bars**: the four bars' (and the 2026 annual's) TOTALS do not move (each is the AUA at its end date); the classes do: Q3 and September 2026
  (end 09-30) Unclassified $82,444,446.18 -> $52,957.36 (-$82.39M), structured $28.41M -> $115.96M (+$87.55M), fixed income -$16.84M, equity
  +$7.25M, cash +$2.33M, alternatives +$1.73M, commodities +$0.37M; Q4, October and 2026 (end 10-09) Unclassified $1,846,332.73 -> $883,413.33
  (-$962,919.40), equity +$876,265.04, fixed income +$86,654.36. The after figures exclude SC-e-91's retained pass on window dates (row W86-S9).
- **Advisors**: no advisor key is dropped (56 and 56), the last five served versions each carry the same 56 keys, so the base code did not drop any
  (D1-W80-S3 measured: not a defect of this act). But **502 of 840 advisor-days move** and ATTRIBUTION moves: the build reads the CURRENT
  `rel_architect` lookup, the served map carries an earlier attribution; the largest single moves are Tim Rodgers on 09-28 +$79.3M (served $60.8M ->
  $140.1M) and Luke Heiligenthal on 09-29 -$52.6M (served $64.2M -> $11.5M), about $55M of window-day history moving between advisors. This is a served
  restatement of advisor history by the producer's own rule, and it is named here so that neither half signs it unseen.
- **The ten largest added and dropped relationships per date** are by opaque relationship id and dollars in the request; the full tables are
  committed beside it in `R23_RADIUS/` (this folder): `added_dropped_by_date.csv`, `added_dropped_top10.csv`, `advisor_window_table.csv`,
  `aua_vs_firm_by_date.csv`, `bars.json`, `d04_unclassified_by_date.csv`, `advisor_key_sets_v1_v5.json`. No client name and no account id is in them.
- **Criteria re-run at trunk @2e8d5c96ef**: `ROLLING-REDERIVE ok=True`, `ROLLING-WIRING ok=True`, `HALF-REQUEST ok=True sections=11 of 11 ... totals=True
  added_dropped=True bars=True`.

### SIGNED again, for the same two files, with the first signing's conditions 1 to 8 AND these

9. **Leg G, the totals (closes C-S17):** for each of the 15 window days, the served `firm[date].total` of `gold/views/mix_daily_summary.json` equals
   the rebuilt firm total stated in the request within $1.00 (the totals are sums of `total_mv`, with no six-place rounding in them), and equals the
   AUA of that date; the Q3, September, Q4, October and 2026 bars' TOTALS read unchanged. A day beyond $1.00 is a STOP and the code rollback.
10. **Leg G, the advisors:** the served advisor map carries the same 56 keys; each advisor-day of the window equals the request's stated rebuilt total
    (`R23_RADIUS/advisor_window_table.csv`) within $250 (SC-e-91's retained pass runs after the window pass on the first fire and the worker could not
    measure it; any residual beyond $250 is printed and judged, not waved). The attribution moves are printed beside the table and are the CTO's to
    have seen BEFORE the ship (condition 11).
11. **The CTO re-signs or refuses on THIS radius first.** The ship is not given a GO on this half alone; it needs the CTO's half re-signed at the
    bytes of the request @2e8d5c96ef (or later, with its change stated), the attribution move named in his reading.
12. **Order of acts** is unchanged from condition 2: SC-e-91's leg G first.

`2.0.0_SA_COO~M1`
