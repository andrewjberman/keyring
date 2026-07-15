# 0.5.0_AE_OpalETL -- 22:00Z fire close: PARITY 3/3 CUTOVER-READY + scheduled leg confirmed (21:15-22:05Z)

**archetype:** VALIDATE

## The name-map endgame (Andrew, my terminal, all verbatim on the record)

- ~21:2xZ: BOTH SMAs CONFIRMED ("these are the two SMAs i was looking for") @ 3ad8d50fa.
- ~21:3xZ: TAX LABEL SEVERED ("I wouldnt call Pathfinder a Tax SMA, just an SMA, we will
  figure out the tax stuff later") @ 981797593 -- DS corrective sent BEFORE their expectations
  baked my provisional label.
- ~21:3x-4xZ: THREAD WRAPPED ("Don't care about Opal Equity Growth for now... just make sure
  that we're properly pulling all of these in our smartx bronze" + "specifically in the
  opal-data-assets/smartx/ bronze") @ ae80ccf4c. Equity Growth PARKED; the ruled verification
  ran GREEN: ALL 7 confirmed models x ALL 5 model-tier feeds present @
  opal-data-assets smartx/model/{rmid}/bronze/{feed}/20260715/ (listing instrument; sizes
  internally consistent -- model_allocations scales with book, LTC 1,316KB/3,195 allocs vs
  SMAs 25-42KB/40-45).

## THE 22:00Z FIRE -- one run, three verdicts, all GREEN

1. **PARITY 3/3 CUTOVER-READY**: 07-13 + 07-14 + 07-15 each GREEN 52 fields / 0 mismatches
   (unpiped; textual verdict cited). Step 1 of the 4-step cutover order complete; steps 2-4
   (SILVER_ROOT="" safe-apply -> verify LIVE write -> disable legacy) await dispatch; LAPTOP
   STAYS ON. Channel caveat carried: numerator leg only, LD-0292 ($528mm partner_held_etf,
   different feeder) stays OPEN. V2-1 GO precondition MET per COO 183555Z auto-fire clause.
2. **SCHEDULED-TRIGGER LEG CONFIRMED**: EventBridge fired on schedule; 4/4 vendor-prefix keys
   REFRESHED 22:00:10Z, caught by watcher v2's LastModified>=21:55Z discriminator. INSTRUMENT
   VINDICATION on the record: refreshed trueshares bytes carry ETags IDENTICAL to the manual
   fire's (issuer page unrepublished since 12:37) -- existence AND ETag oracles were both
   structurally blind tonight; LastModified was the ONLY discriminating instrument. Harness on
   refreshed bytes: TS_PATTERNS 8/8 both funds, as_of Jul 14 (T-1 correct), headers ==
   expected, Q2 conservation ties (85+23=108; dailynav 2/2).
3. **msn SILENT post-strike**: 0 keys both fires; no FINDING; CTO's code-strike can sequence
   at his artifact-swap gate.

Both remaining S1 cert cells (day-3 parity; scheduled trigger) close on this evidence.
Verdicts delivered to COO (220317Z) + CTO (220319Z).

## Compiler Tools

None this window -- vendor-API probes + landed-parquet reads + the parity/harness instruments;
no comp-tool covers the SmartX/ETF monolith surfaces (standing gap, fourth consecutive log).

## Open at close

- [CTO dispatch] ETF cutover steps 2-4; msn code-strike at his artifact-swap gate.
- [Andrew, parked] Tax SMA (deferred by ruling) - Opal Equity Growth (parked).
- [days] MSTR LCLRPO data/smartx disposition (incl. smartx-model-monthly-pull portal-consumer
  check).
- Laptop stays ON until cutover step 4.
