# 0.5.0_AE_OpalETL -- smartx planned family 5/5 LIVE + D2 leg-2 closed + ETF design filed (14:17-15:15Z)

**archetype:** MIXED (IMPLEMENT + VALIDATE + COORDINATE)

## Window summary

Fresh session post context-reset (handoff 485e3efb8). One 58-minute arc: startup -> 22:00Z
watcher armed -> the whole smartx planned silver family landed against pre-filed expectations.

1. **STARTUP + ORPHAN REAP:** /watcher found the predecessor's watcher pair (348052/348110)
   holding my inbox. Identity probe FIRST (dual-COO-collision discipline): broker LIVE @ PID
   26332 = the detached python poller (started 07-14), NOT a peer session -> orphan confirmed,
   killed both, fresh Monitor bh695mg0v armed. LD-0290 serial file written. The ~A lane's
   watcher left untouched (not mine).
2. **22:00Z LANDING WATCHER ARMED (task b2o9w222h):** polls the VENDOR prefixes
   (trueshares/ pathfinder/ msn/ in opal-data-assets -- NOT etfs/, last night's wrong-axis bug)
   for /20260715/ keys from 21:56Z, 60s cadence, LOUD DEADLINE-MISS at 22:50Z. Instrument
   positive-controlled against smartx/ monolith keys (same grammar) before arming. Live Lambda
   env grounded first: BRONZE_BUCKET=opal-data-assets, BRONZE_GRAMMAR=monolith,
   SILVER_ROOT=_cloudprobe/, CodeSha256 ties v1.1.0 three-way sha.
3. **SMARTX FAMILY BUILD (Andrew-direct critical path; CTO board "families = 0.5.0 today"):**
   - Coordination: RAVC-REQ to DS for the expectation skeleton; DS delivered part-1 (43bbc0385,
     atom) + part-1b (6663a320a, model tables, PINNED all-22-objects) same window. CTO family
     review PASS + THREE RULINGS (145610Z): (a1) model_id DROPPED from model_aum contract
     (payload carries no identity field -- measured 11/11); (b) model_name +
     opened_date_friendly KEPT (Rule 17); (c) empty-series hole CONFIRMED with a binding
     discriminator AC.
   - Code @ 5ae372e99: naming-law fact_ constants + silver_keys rename (5 tables off constants);
     parse_model_aum + parse_model_allocations + discriminating-dedup frames + pinned pyarrow
     schemas. Suite 13->35 cases.
   - Code @ 7f76de167: ruling-(c) discriminator (lawful [] ONLY on perf==[] AND totalAum==0 AND
     enterprise==null; ANY funding signal RAISES; fixed vocabulary MODEL_AUM_HOLE_UNFUNDED) +
     3 mutants killed (funded-but-empty, partial-signal, missing-totalAum). Suite 39/39.
     CTO verified at source + accepted 150145Z.
   - **ATOM RUN (scratchpad driver, v28 discipline):** fact_allocation_positions 107,309 rows +
     fact_allocation_valuation 9,540 rows @ date=2026-07-15. Every DS check green: valuation
     rows==distinct==objects==9,540 [hard]; positions IN band (DS extrapolated ~110,330 from a
     2.1% sample; exact 107,309); zero-position 20.7% (sampled ~19%); strict subset 7,563<9,540.
     DS later independently re-read ALL 9,540 objects: their total == 107,309 TO THE ROW (two
     instruments agree).
   - **MODEL RUN:** fact_model_aum_daily 4,278 rows (EXACT DS pin; EXACTLY the 3 named
     empty-series-unfunded holes 53ba340c/920c1026/e32a9399) + fact_model_allocation_roster
     9,540 rows (status split open 7,125/close 2,381/workingClose 34 EXACT; identity nulls 0).
     CROSS-FEED INVARIANT (DS part-1b) wired refuse-on-miss and TIED: valuation-landed ==
     roster == 9,540, symmetric diff 0.
   - Discipline both runs: grammar probes listing-verified pre-write; denominators enumerated at
     run time; write_parquet ListObjectsV2 key+Size+ETag (13c); BEHAVIORAL 22a read-back from
     LANDED S3 bytes; manifests in smartx/platform/meta/pulls/20260715/.
   - **DEDUP-SEMANTICS FINDING (latent, at CTO):** to_frames dedups positions on the NATURAL KEY
     keep-last; DS expectation says exact-duplicate-only. Measured ALL 9,540 objects: 0 dupes
     either class -> outputs identical TODAY, divergence latent. A future two-lots-one-ticker
     delivery would be silently collapsed. My drivers refuse on conflicting dupes; the durable
     to_frames ruling is at CTO with DS's independent grounding + concurring recommendation
     (exact-row dedup + conflict-RAISE, the model_aum precedent).
4. **D2 LEG-2 CLOSED @ 257ac3085 (CTO validated + RAVC-closed 145732Z):** fresh-CRS join
   re-measured on the ruled substrate (V2-8 fact_acc date=2026-07-14, both masters) -- 99.43%
   (5,592/5,624, same denominator as the 20260508 measure; was 96.4% on the stale lossy staging
   table; 173/205 of the old residual joined = the stale-vintage explanation HELD). Residual 32
   pinned to classes: 19 = master-0833 identity (RECORDED, never summed) $21.0M; 13 = neither
   master $8.2M (9-digit class INFERRED non-Schwab custody, honestly open). D2 has ONE open leg
   (feed-8, at CTO's consolidated Andrew ask).
5. **ETF FAMILY DESIGN FILED @ 9efe4ae0e** (inventory sec D, alongside day-3): 5 proposed fact_
   tables off the C4 landing map; the load-bearing line = tier-adjudication/carry-forward/
   staleness_days/consolidated series are GOLD, not silver; per-fund-at-silver per ruling 15;
   msn sparsity law (tier-3 fallback absence is normal -- never point comp-freshness at it flat);
   schemas PIN on tonight's landed bytes; Q1-Q3 routed to CTO/DS. Push raced DS's part-1b commit
   (transient ref-lock); resolved by pull-merge per NEVER#7, landed clean.
6. **Portal freeze ACK'd** (COO 143744Z, POSN_BMKVIZ promote window) -- no portal work in lane.

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-grep | trueshares/msn landing-map hunts; fact_allocation_account_map estate census | PASS -- found the C4 producer + all driver/ruling record sites |
| comp-glob | C5 plan / ingestion-architecture / expectation-report locates | PASS |
| comp-to | OPAL_ASSETS.C5 session TO context | PASS (race-free per-session file) |
| commit-gate + surface-check + risk-reflex | via safe-commit x4 | PASS all; risk-reflex denominators printed (1239 danger nodes) |
| raw aws (operational) | get-function-configuration (env ground), ListObjectsV2 landings/censuses, s3 cp samples | monolith acceptance instrument per ruling; comp-tool gap for monolith remains filed (07-14) |

What worked: the pre-fire expectation-report pattern end-to-end -- DS's independent census caught
my stale 9,525 denominator BEFORE the run, and their pins made every landing binary-checkable.
What failed: nothing this window. Gap: monolith opal-data-assets still has no comp-tool coverage
(filed 07-14, ~Z/0.8.0 pending) -- every landing verify is rail-checked raw listing.

## MCP traffic

~14 handled. Significant: DS skeleton REQ/part-1/part-1b/closes (4 loops CLOSED); CTO family
review PASS + 3 rulings + (c)-accept + D2 validate + atom/model evidence (all loops CLOSED);
COO portal-freeze ACK. Zero open loops at log time.

## Files Modified

See commit messages: 5ae372e99, 257ac3085, 7f76de167, 9efe4ae0e. Plus
SILVER_FAMILY_BUILD_INVENTORY_20260714.md status header (5/5 live; rides this log commit).
Scratchpad (session, uncommitted by design per v28 precedent): atom_first_conversion.py,
model_first_conversion.py, etf_landing_watch_20260715.sh.

## Blockers

None. Every open item is event-gated: 22:00Z fire (watcher armed), DS part-2 (their queue),
CTO rulings (7-feed wave + to_frames dedup), feed-8 (Andrew ask).

## Current State (zero-prior-context handoff)

**Branch CLOUD pushed through 9efe4ae0e. Monitors: bh695mg0v (inbox), b2o9w222h (22:00Z landing
watch, vendor prefixes, deadline alarm 22:50Z). Session TO context: OPAL_ASSETS.C5.**
- **SMARTX PLANNED FAMILY 5/5 LIVE SILVER** (platform scope, date= partitions, manifests in
  smartx/platform/meta/pulls/20260715/): account_map 7,141 @ 07-14; positions 107,309 +
  valuation 9,540 + model_aum_daily 4,278 + roster 9,540 @ 07-15.
- **TONIGHT 22:00Z (the clock):** scheduled etfs-netassets-daily fire = day-3 parity + FIRST
  monolith ETF bronze in ONE run. At landing: python .tools/etfs-parity-check.py UNPIPED on the
  scheduled artifact; OPEN the landed bronze and SEE content; report both verdicts to
  [2.0.0_SA_COO] (V2-1 GO rides clean BOTH). NO ad-hoc re-fire. LAPTOP STAYS ON. C4 TO flips
  complete only on the populated-vendor-prefix listing from THIS fire.
- **Open at others:** [1.0.0_SA_CTO] to_frames dedup ruling (latent) + 7-feed rulings (on DS
  part-2) + feed-8/1,066-class/4-Global Andrew ask + ETF design Q1/Q2; [0.4.0_DS] part-2
  skeleton + ETF converter authoring (their board) + ETF design Q3; [2.0.0_SA_COO] portal-freeze
  release relay (holds dbfe8c3a9's companion portal commits, predecessor session's item).
- ETF design: ETF_SILVER_FAMILY_DESIGN_20260715.md @ 9efe4ae0e -- schemas pin on tonight's
  landed bytes; nothing compresses the parity window (cutover order unchanged).
- D2: ONE open leg (feed-8). MDPF_BASISSWITCH untouched (sovereign-excluded). Draft silver
  objects untouched (LEAVE-AND-QUEUE).

## Next Steps

1. [self, 22:00Z] read the landing watcher -> unpiped parity gate + open monolith bronze content
   -> report to [2.0.0_SA_COO]; then pin ETF schemas on the landed bytes (design sec 5.2).
2. [self, on CTO's to_frames ruling] apply the dedup-semantics fix if ruled (exact-row +
   conflict-RAISE) -- small silver.py edit, suite extension, no re-run needed (today's output
   proven identical under both semantics).
3. [self, on DS part-2 + CTO rulings] the 7-feed table-or-exemption build wave.
4. [1.0.0_SA_CTO] holds: dedup ruling, 7-feed rulings, ETF design Q1/Q2, feed-8 Andrew ask.
5. [0.4.0_DS_ClientPlatform] part-2 skeleton; ETF converter authoring post-first-bronze (Q3).
