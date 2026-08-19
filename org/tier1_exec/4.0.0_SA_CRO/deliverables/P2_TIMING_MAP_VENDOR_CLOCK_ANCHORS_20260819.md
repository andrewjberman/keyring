# P2 TIMING MAP -- VENDOR-CLOCK ANCHOR ROWS (T3-VENDORCLOCK one-pass audit, 2026-08-19)

**Author:** 0.7.0_AE_CloudOps (TO OPAL_ADVIPOINTERS.T3-VENDORCLOCK @ade7af5f28; TIGHTENING brief T3
@094df1d132, Andrew-ratified). **Addendum to** `P2_UNIFIED_MORNING_SCHEDULE_TIMING_MAP_SPEC_20260811.md`
-- these rows are APPLIED-PLANE reads (live `events describe-rule` / `scheduler get-schedule` +
LastModified landing series), which the spec's own Rule-22a condition required before quoting any
value as live. Every cron below was read from AWS on 2026-08-19, not from TF.

## Census denominator (T3-1)
Both EventBridge namespaces + SSM associations materialised (auto-paginated, counted client-side):
**135 `events` rules · 15 `scheduler` schedules · 0 SSM associations.** 121 rules carry a
ScheduleExpression. Classification: vendor-pull rows below; everything else internal
(sweeps/emitters/gold floors/parity/monitors/keepalives) or out-of-family (market/news, listed last).

## METHOD WARNING (banked for every future landing-series read)
`aws s3 ls` prints **LOCAL time with no timezone marker** (this box: ET). The first read of this
audit mis-derived a phantom "05:46Z on-box scheduler" from exactly that; the discriminating control
was `s3api head-object` (returns GMT): displayed 05:46:35 == **09:46:35Z** == the 09:45Z EventBridge
fire. Every timestamp below is corrected-UTC, head-object-controlled.

## ANCHOR ROWS (T3-2/T3-3) -- the brief's family

| Pull (applied cron, UTC) | Vendor publish anchor | Authority | Verdict |
|---|---|---|---|
| `canonical-schwab-si2-08335338-daily-pull` cron(45 9,21) -- SDD 0833/ADVI | Day-D files available in (21:45Z D, 09:45Z D+1); 30d landing series all 09:46Z first-ask-success | **OBSERVED-WITH-WINDOW** (bronze rps/acc/fam LastModified series n~30d, UTC-controlled) | **POST-publish. No retime.** Sub-feed note: fam vendor-side hole since CS081026 (verdicted 130754Z) is a FEED hole, not a clock defect; R-detection oracle unchanged |
| `canonical-schwab-si2-08242234-daily-pull` cron(15 10,22) -- SDD 0824/MDPF | Posts ~08:37Z (TF-observed, `monolith-daily-schedule.tf:31`); landings 10:15:5xZ | **OBSERVED** (TF comment + 30d series) | **POST-publish. No retime.** |
| `opal-assets-bd49f-daily-pull-{pull,reattempt}` cron(30 6)/(30 8) + `opal-assets-bd49f-dim-convert-daily` cron(5 7) | BD REST refreshes prior day **01:02 ET (05:02Z)** | **RULED** (Andrew-direct 08-11 @accf58083e; re-affirmed in the 08-19 retime verbatim @807c3c9190) | **RETIMED 08-19 (the exemplar)** -- ledger 20260819T1430Z, applied-plane 3/3. POST-publish, ~88min margin |
| Orion/inf API family: `inf-api-reps` 11:02 · `inf-accounts-v2` 11:07 · `inf-api-assets-v2` 11:17 · `inf-api-positions` 11:22 · `inf-api-txn` 11:32 · `inf-tax` 13:42 · `inf-billing` 14:22 · `inf-performance` 14:27 (+ `opal-inf-jwt-fetch` 09:50 session-only) | Orion daily landing **~14:16Z** | **MEASURED** (MDPF_PIPELINE_TRUTH.md:120-137, corroborated per the ratified spec §1) | **MISMATCH CONFIRMED, REMEDY ROUTED -- NOT retimed in this pass.** Core pulls fire ~3h pre-landing (read prior-settled state daily, by construction). The ratified spec §5 names this the unified-floor-vs-later-floor FORK routed CVO->CTO->Andrew; `MDPF_REMED.W1-5` (pending, AE seat) is the standing retime vehicle. billing/performance already post-landing (someone timed those right); tax 13:42Z sits pre-landing with the core set. Recorded as T3-3's "exception with its reason" |
| `inf-api-eclipse-daily` cron(18 11) | Eclipse = trade/rebalance layer **STATE READ** (models/portfolios); no batch publish clock exists | **STATE-READ SEMANTICS** (payload = models/portfolios_full/model_composition, live partitions through 08-19) | **POST-publish by construction. No retime.** |
| `cot-rebalancer-runner-daily` cron(0 6) | BD REST 01:02 ET (05:02Z) -- rebalancer.bdreporting.com, BD_FIRM_ID=cottonwood | **RULED vendor / PLACEHOLDER slot** (`cot_rebalancer_runner.tf:171` marks 06:00Z placeholder; exact slot = CTO/WS-4 chain-timing confirm) | **POST-publish (fires 02:00 ET, 58min post-refresh). No vendor-clock retime.** Open half is DOWNSTREAM chain-timing confirm (WS-4 DDB before mdpf refresh), not the vendor clock -- stays with WSE_COTMDL |
| `cot-bd-session-daily-et` cron(30 7 ET) + `opal-assets-ingest-mirror-cot-daily-et` cron(45 7 ET) | BD REST 01:02 ET | **RULED** (08-11 morning-schedule ruling @accf58083e) | **POST-publish, conforms to the ruled morning window.** The old 16:30 ET session slot the ruling ordered moved IS moved (applied-plane read) |
| `smartx-assets-daily-pull-daily` cron(2 13) 7d/wk + `smartx-rest-pull-daily` cron(15 9 ET) (+ `smartx-jwt-refresher-daily` cron(0 9 ET) session-only) | SmartX API **STATE READ**; landing chain 13:02:52Z (access_roster) -> 13:06-08 (allocations) -> 13:09-11Z (models) sequential | **STATE-READ + OBSERVED** (n~9d series) | **POST-publish by construction. No retime.** `smartx/account/` GUID tree last written 07-14 08:58Z -- one-time backfill vintage, not a daily lane |
| `wsb-49f-model-aua-pull-daily` + `wsd-49f-partner-held-etf-pull-daily` cron(30 3 TUE-SAT) | Day-D 03:30Z captures **prior close**, labels D | **RULED** (CTO 052551Z consumer-read correction, in-TF `wp5-feeder-schedules.tf:252-266`) | **POST-publish. No retime.** |

## ADJACENT VENDOR PULLS (enumerated -- census completeness)

| Pull | Anchor / verdict |
|---|---|
| Legacy bd (49F) evening download triggers MON-FRI: `bd-realized` 21:45 · `bd-transaction` 21:53 · `bd-allocation` 22:00 · `bd-asset-dim` 22:10 · `bd-fees` 22:15 · `bd-49f-fees-session` 22:20 · `bd-allocation-file-check` 22:30 · `bd-49f-session-daily` 00:00 | BD REST ruled 01:02 ET. **POST-publish** (evening pulls read the morning-settled T-1 -- late, never early). **No retime investment: P5-TEARDOWN retirement is event-gated on this legacy stage** (earliest 08-23, moves with the flip) |
| `etfs-netassets-daily` cron(0 22) -- TrueShares DIVZ/IDVZ + Pathfinder PFDE/PFOE | Close-derived ETF data (close 20:00Z); landings 22:00:1xZ = 2h post-close. **OBSERVED. POST-publish. No retime** |
| `bd-canonical-prices-daily` cron(0 4) | **NOT a vendor pull** -- target is `bd-gold-trigger {"mode":"incremental"}` (internal gold build off landed bronze). Classified INTERNAL; coherent within the legacy tree (fed by the 21:38-22:30Z evening landings) |

## OUT-OF-FAMILY (enumerated, deliberately NOT anchored this pass)
`news-api-*` (13) · `news-rss-*` (7) · `fred-ingestion-*`/`fred-macro` (6) · `fear-greed` ·
`volatility` · `market-rsi` · `historical-prices` · `etfs-canon-fanin` · `seeking-alpha-*` (2,
DISABLED) · `ycharts-session-probe` (session probe; ycharts egress HELD). Market/news feeds with
continuous or release-time semantics -- outside the brief's firm-data family (~6). Anchoring them is
a separate commissioned pass if wanted; recording the boundary here so the omission is a choice on
the record, not a blind spot. (T3-3 exception clause.)

## T3-3 SUMMARY: retimes required this pass = ZERO
The one true mismatch family (Orion/inf) is a ratified NAMED DECISION POINT (spec §5) with a standing
pending TO as its vehicle -- unilaterally retiming it here would adjudicate a fork the protocol
routes to CVO->CTO->Andrew. Everything else reads post-publish on a RULED, OBSERVED, or
STATE-READ-semantics anchor. No applies were needed; no CTO apply-gates consumed.

-- 0.7.0_AE_CloudOps, 2026-08-19. Evidence: scratchpad t3_rules.json / t3_schedules.json /
t3_ssm_assoc.json / t3_sched_crons.txt (session-scratch); durable citations inline above.
