# Session log — MDPF_INFACTUAL.001 inflection ETF actual-holdings feeder
**archetype:** IMPLEMENT

**Agent:** 0.4.0_DS_ClientPlatform~A · **Date:** 2026-07-29 (00:22–00:45Z window)
**TO:** `MDPF_INFACTUAL.001.inflection-etf-actual-holdings-not-target-weight.md` @991a04d761 + COO
Amendment 1 (~0024Z Andrew-direct, dual-source parity tracking).

## What happened

1. **Startup:** /watcher armed (Monitor task btjfuxs3c), registered `~A`, XXX.md steps A.1–E clean
   (93/93 comp-tools resolve). GO arrived 00:22Z mid-startup; RAVC-acked and executed.
2. **Source caveats resolved by enumeration** (not construction): orion silver = 4 tables;
   `fact_assets` + `fact_positions` both 2,283 partitions (floor 2020-04-28, newest 07-28),
   byte-identical on calculation columns; **fact_assets picked, CTO-ratified**. Eclipse silver =
   4 tables, ALL portfolio/model-metadata grain, **zero ticker/isin/cusip columns** → Amendment 1's
   Eclipse parity leg NOT BUILDABLE as stated; STOPped per amendment, reported, no synthesis from
   weights. COO accepted; carrying to Andrew as blocked amendment.
3. **Directional deviation investigated before acceptance:** measured vs estimate = DIVZ +0.71%,
   IDVZ −18.5%, PFDE −20.2%, PFOE −20.4% (total −13.1%) — outside the briefed −1..−3%. Join
   verified on 4 axes; COO retracted the envelope (49F-population mis-import, his own flag);
   population discriminator run: orion $203.3mm/943 accts vs model_aua $142.1mm/556 accts,
   containment 549/556 + 7 synthetic $0.00 ids = 100% of model value inside custody feed →
   **real drift, gate CLEARED** (COO 00:36Z), envelope re-based by CTO (this measurement = the
   inflection baseline).
4. **Population declared** (COO one-level-deeper ruling): 49F sibling sums the WHOLE RPS custody
   book (read at source, :131-155) → my whole-book sum MATCHES; PURPOSE declared in-module + in
   artifact parquet metadata; CTO condition-(a) disclosure (coarse `rps_actual` label vs true
   `orion_assets` source) in module + artifact metadata + deliverable.
5. **Built** `data/mdpf/scripts/feeders/wsc_inflection_held_etf.py` (pure-add mirror of
   `wsd_partner_held_etf.py`; fail-loud on missing partition — NO silent target_weight fallback;
   zero-value guard; roll-forward provenance in `rps_date_used`).
6. **Exercised acceptance:** feeder rc=0; local-fixture aggregator runs with/without the artifact
   (fixture-parity control vs s3 run: IDENTICAL etf_decomposition); FULL-AXIS diff = 34 leaf paths,
   all named, no unexplained mover, headline unchanged; identity2 verify PASS; s3 dry-run rc=0
   reconciliation PASS; sentinel-1 activation-day move +4.9% << 50% threshold.
7. **DORMANT landing:** no S3 upload (deploy freeze; activation = CTO gate); commit-no-push.
   Deliverable: `deliverables/MDPF_INFACTUAL_001_inflection_actual_holdings_feeder_20260729.md`.

## Compiler Tools

| Tool | Result | Notes |
|---|---|---|
| `comp-pipescript io mdpf_aggregate_aua.py` | ran; READS/WRITES "(none detected)" + WARN dynamic-key | **Gap:** the aggregator's S3 I/O is fully dynamic; manifest blind here. Manual body read substituted (mandated by the WARN itself). |
| `comp-grep "partner_held_etf"` | 47 hits across 10 files | Located feeder + consumer + handoff design; §3 premise confirmed at source (`:1052-1055`, `:227-245`). |
| `comp-validate wsc_inflection_held_etf.py --artifact <parquet>` | **NOT a known artifact-id** (NO_CONFIG class) | mdpf feeder class is outside the 21-script validate config (sibling equally unconfigured). Reported UNVALIDATED-by-instrument; did NOT signal SAFE on it; validation = exercised acceptance chain. **Gap flagged:** feeder-class validate configs don't exist. |
| `comp-blast wsc_inflection_held_etf` | see post-commit note in report | Phase-3, run after commit. |

Rail overrides: 3 `# rail-checked` raw `aws s3 ls` enumerations (TO-mandated prefix enumeration —
existence/partition questions, not freshness/routing; logged to the rail audit).

## Open items / handoffs

- **CTO:** activation GO (artifact upload + AE chain wiring, post-fires); basis-label edit riding
  the cutover producer spec (R7); Eclipse parity leg blocked-at-Andrew (COO carrying).
- **COO:** push (I committed, did not push — push-operator process).

---

# Addendum: Andrew-direct 49F ETFS backfill (same session, ~0106-0125Z)
**archetype:** IMPLEMENT

1. **AVGCAP July measured** (COO item 2, before fix): 49F = 3 written/31 covered days, $521.9mm;
   AC6 source_as_of_worstcase fires AS SPECIFIED but is structurally blind to dead TAILS
   (worst-case-OLDEST = month-start on any healthy-front month); June SHIPPED mid-month
   (generated 06-25) partial=false on 17/30 days — surfaced to COO for the Andrew-level call.
2. **Source corrected by enumeration**: CTO spec's fact_rps_s2 = S2 account-summary (no ticker);
   position grain = fact_rps (S1). Reported + proceeded.
3. **Reproduction STOP-control**: 28/28 per-ETF values exact to the cent vs all 7 existing
   burst artifacts — monolith fact_rps ≡ bd-tree silver rps on this quantity. Burst files left.
4. **Root cause grounded**: producer NEVER SCHEDULED BY DESIGN — TF single commit 349c91e35b
   says "NO event trigger (S-D2 monthly batch, rides next Schwab batch)"; 0 event rules in
   full TF history. "Never started," not "stopped."
5. **Backfill executed**: `data/etfs/scripts/backfill/backfill_49f_daily_from_monolith_rps.py`,
   window 2026-07-07..07-27 (15 enumerated partitions; 07-03 holiday + weekends resolved),
   15/15 uploaded + listing/md5 verified. source_as_of = partition identity. Clock answer:
   first ETF-carrying partition = data floor 2024-05-24 (DIVZ $39.1mm).
6. **July basis after backfill** (dry-run, NOT uploaded — re-run proposal pending):
   49F written 3d -> 18d, total $521,948,667.35 -> $527,329,468.85 (+$5.38mm; the carry was UNDER).

Compiler tools: comp-glob (located producer TF/code), comp-grep (avgcap engine), enumerations
rail-checked. comp-pipescript io not applicable (new backfill script, S3-dynamic; manual body
review is the record above).

---

# Addendum 2: etf_decomposition consumer trace (COO item 1, ~0126-0132Z)
**archetype:** TRACE

Render-backwards map, denominators stated per claim:
- DDB/emitter path (rendered): opal-assets-daily-emitter reads etf_decomposition at exactly 2
  sites, both extract ONLY ticker + etf_total_net_assets (NAV passthrough); held values are
  measured opal-data-etfs artifacts ("NEVER mdpf etf_decomposition target_weight" ratified
  in-code). Estimate-free.
- Served timeseries (fetched, NOT rendered): aggregate_aua_timeseries.json etf_decomposition
  block (433 dates, live through 07-28) embeds the estimate in held_total/public_residual;
  portal types it (MdpfEtfSeries) but 0/404 src files consume the fields. Ships to browser,
  displayed nowhere.
- OWNTS per-ticker artifacts: consume held_by_partner, are themselves consumed by NOTHING
  (0/1,055 portal files; repo = producer+runbook+PRD only).
- Load-bearing exception named: identity_2 (over-attribution gate) is computed FROM the
  decomposition and gates the platinum write — deletion would delete the gate.
Verdict: no rendered surface displays the estimated inflection held value. Reported to COO
(cc CTO) 013150Z. Open mechanism note (INFERRED, labeled): how the timeseries etf block
advances despite the dim producer not naming the key — pin before any deletion decision.

AE~A seam closed: writer design @5dd48c5eba adopted my compute_slice as the one computation;
import-surface question answered (pandas/boto3/stdlib, import-safe, client-injected).

---

# Addendum 3: cottonwood daily-continuity census (Andrew-direct ~0320Z, ~0330-0345Z)
**archetype:** VALIDATE

Full chain walked read-only: monolith bronze (8 feeds, both conventions) / silver (14 tables) / gold DDB
(4,678-item scan, 6 cohorts) / gold-mdpf accrual (canonical portal/gold/mdpf per Andrew's live correction
mid-census — root gold/mdpf_revamp flagged as duplicate write target) / platinum per-firm + global fold /
ETFS baseline / parallel opal-data-cot tree. Calendar = lib/trading_calendar.py.
VERDICT: cottonwood IS pulled daily (both trees at-frontier at declared cadences); all downstream breaks map
to G7 (values end 07-22, carry covers to 07-27) + 4c (DDB rows missing 07-23..24; accrual born 07-28);
fact_holdings known-unknown RESOLVED HEALTHY (advanced to 07-27). No fourth live break; three bounded
residuals named UNKNOWN/CTO-routed: 06-24..25 two-day outage (both trees, healed), ETFS in-span gaps
(06-23/24 + 07-20; floor said 31/31, measured 30), duplicate gold write target.
Two instrument errors caught in-flight and corrected before reporting: date= / .gz filename parsing
(silver/bronze false-EMPTY), and a partners{}-dict assumption on the global-slice schema (false 0-slot
histogram). Deliverable: deliverables/COTTONWOOD_DAILY_CONTINUITY_CENSUS_20260729.md.
Compiler tools: comp-grep/comp-glob for layer discovery; raw enumerations rail-checked per census mandate;
DDB data-plane scan operational (off-rail per graph-presence principle).
