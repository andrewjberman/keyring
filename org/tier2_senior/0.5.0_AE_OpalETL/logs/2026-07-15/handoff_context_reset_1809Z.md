# 0.5.0_AE_OpalETL -- CONTEXT-RESET HANDOFF, 2026-07-15 18:09Z (fire T-minus ~1h50m)

**archetype:** SCRIBE

Purpose: self-contained resume surface -- a fresh session resumes from org/XXX.md startup + THIS
file alone. Written at Andrew's reinstantiation request. Prior log 18 minutes ago (3a1e71aae);
the delta since is folded into Current State below.

## Window since last log (17:52 -> 18:09Z)

1. **DS FILED ALL SIX part-2 pins @ a289cc2fe** (SMARTX_PART2_EXPECTATION_REPORT_20260715.md) --
   two-instrument agreement on EVERY overlapping denominator (7,066 / 511 / 91 / 164 / 6,456 /
   1,058). Their three deltas triaged + DS RAVC-CLOSED (180303Z): (1) detail bools -- committed
   schema already pins NINE (my '8' was prose; artifact wins); (2) sweep presence biconditionals
   -> run-1 FLEET measurement first, frame RAISE folds only after fleet confirmation
   (assert-later ladder); (3) R3 containment = a MATRIX not a subset -- model-open-outside-map
   REPORTS loud, write stays lawful.
2. **Envelope-count refuse-gate landed @ 33ed38e0f** (attestation-tie; DS pin): sweep /
   nonzerosleeve / holdings / changerequests parsers refuse count!=len(data). Mutant killed.
   Suite prints 68 OK (the commit message says 67 -- my third prose count slip today; the suite
   is the truth; noted here, not churned into an immutable message).
3. **Run-1 sweep driver STAGED** (scratchpad, below) -- every DS pin wired as a gate; DOES NOT
   RUN until CTO's per-family GO.

## STARTUP for the reset session (in order)

1. `/watcher` -- **TWO orphan bash children survive this session's end; REAP BOTH before arming**
   (own-serial scope; identity-probe first per the dual-COO doctrine):
   - `bash .../org/mcp/inbox-watch.sh 0.5.0_AE_OpalETL stream` (was wrapper 864898 / child
     864955) -- the inbox thief class; kill, then arm the fresh Monitor.
   - `bash .../scratchpad/etf_landing_watch_20260715.sh` (was wrapper 876382 / child 876463) --
     NOT an inbox thief, but its 22:50Z DEADLINE-MISS alarm fires into a DEAD PIPE; kill it and
     RE-ARM YOUR OWN (step 3). `ps -ef | grep -E "inbox-watch.sh 0.5.0|etf_landing_watch"`.
2. `register_agent("0.5.0_AE_OpalETL", ...)` + write org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial
   + owned-paths hook + `.comp-graph/.agent_context` + `comp-to OPAL_ASSETS.C5.smartx-holdings-activity-etl`.
   Zero crons (event-driven worker).
3. **RE-ARM THE LANDING WATCH (deadline-critical, do before anything else after registration):**
   Monitor tool, persistent:true, command:
   `bash "/c/Users/ANDREW~1/AppData/Local/Temp/claude/C--Users-AndrewBerman-Desktop-ajb-workspace/17c57e5a-0149-4046-ae44-c2536b762cc3/scratchpad/etf_landing_watch_20260715.sh"`
   (the script persists at that OLD-session path; it polls vendor prefixes from 21:56Z every 60s,
   emits LANDED/CORE-LANDED lines, LOUD DEADLINE-MISS at 22:50Z, exits on core-landed).

## THE CLOCK: 22:00Z scheduled fire = ONE RUN, TWO PROOFS (WS-A1/A2). LAPTOP STAYS ON.

- etfs-netassets-daily (cron 0 22 * * ? *), artifact v1.1.0 verified live (sha 40KaO/7j...,
  BRONZE_BUCKET=opal-data-assets, BRONZE_GRAMMAR=monolith, SILVER_ROOT=_cloudprobe/).
- Landing map (vendor prefixes, NOT etfs/): trueshares/{DIVZ,IDVZ}/bronze/netassets/20260715/,
  pathfinder/filepoint/bronze/{holdings,dailynav}/20260715/, msn/{TICKER}/bronze/netassets/...
  (msn = tier-3 fallback; ABSENCE IS NORMAL -- investigate only if trueshares also missed).
- AT LANDING, in order:
  1. `python "/c/Users/ANDREW~1/AppData/Local/Temp/claude/C--Users-AndrewBerman-Desktop-ajb-workspace/17c57e5a-0149-4046-ae44-c2536b762cc3/scratchpad/etf_postfire_report.py"`
     (dry-run exercised; emits C4 AC1 listing evidence + content assertions incl. TS_PATTERNS on
     landed HTML + CSV headers/rows + the Q2 conservation denominators + msn key unions).
  2. `python .tools/etfs-parity-check.py` **UNPIPED**. Days 1+2 GREEN already; expected-if-clean
     TONIGHT = 3/3 CUTOVER-READY exit 0 (a refusal tonight = a FINDING: day-3 mismatch or
     missing artifact). Pre-exercised 15:16Z (correct 2/3 refusal).
  3. OPEN the landed bronze and SEE content (CTO content assertion; the harness in step 1 does
     this) -- never infer from the producer's raise-on-empty.
  4. REPORT both verdicts to [2.0.0_SA_COO] -- V2-1's GO rides clean BOTH (WS-A2). NO ad-hoc
     re-fire (CTO ruling 230335Z). C4 TO flips complete ONLY on the populated vendor-prefix
     listing from THIS fire (WS-A1).
  5. Then: ETF schema pins off the harness field reports (design sec 5.2) ->
     [0.4.0_DS_ClientPlatform] picks up converter authoring from the same bronze (their tree).
- Cutover order (do not compress): 3d parity -> SILVER_ROOT="" -> verify live write -> disable
  legacy.

## OPEN LOOPS -- NONE. THE WAVE IS EXECUTE-READY (batch GO in hand)

- **ADDENDUM 18:11Z -- CTO BATCH GO RECEIVED (181013Z), the loop closed as this handoff
  committed.** One batch authorization for ALL SIX in pinned order (sweep -> nonzerosleeve ->
  detail -> holdings -> performance -> changerequests), each DS pin a REFUSE GATE, v28
  discipline. **STOP CONDITION: any pin-miss/refuse-gate/containment surprise HALTS the wave at
  that family pending CTO's read -- never continue past a refusal.** Per-family evidence lands
  as each converts (landed read-back + manifest cite); NO per-family ack needed -- the batch GO
  covers the sequence. Delta triage approved as stated (biconditionals measure-first;
  containment = named-finding-never-refuse; cadence manifested honestly). Fire window law:
  anything in flight at 22:00Z queues behind the fire; the wave resumes after.
- **Reset session runs the wave FIRST (before 21:56Z), starting with the staged driver:**
  `python "/c/Users/ANDREW~1/AppData/Local/Temp/claude/C--Users-AndrewBerman-Desktop-ajb-workspace/17c57e5a-0149-4046-ae44-c2536b762cc3/scratchpad/part2_run1_sweep_conversion.py"`
  (sweep, partition 2026-07-14; ~3 min). Then author drivers 2-6 off run-1's template (~15 min
  each; same gates from the DS pin sections). The wave was NOT started pre-reset deliberately --
  no conversion stranded mid-write by the session kill.

## CURRENT STATE (zero-prior-context)

**Branch CLOUD pushed through 33ed38e0f. P0 = OPAL_CONSOLIDATION (lane: WS-A1/A2 fire, WS-A3
part-2 wave, WS-A4 ETF build, WS-C5 post-parity). TO context: OPAL_ASSETS.C5.**
- **smartx silver:** 5 planned tables LIVE (map 7,141 @ 07-14; positions 107,309 + valuation
  9,540 + model_aum 4,278 + roster 9,540 @ 07-15; manifests in smartx/platform/meta/pulls/).
  6 part-2 families LIBRARY-COMPLETE + review-PASSED (@ 6ce907696 + 33ed38e0f; suite 68 OK;
  THE GRAIN LAW + attestation-tie folded @ b3df964aa) -- runs await CTO GO only.
- **ETF:** design FULLY RULED (ETF_SILVER_FAMILY_DESIGN_20260715.md @ e8ecfab0a; Q1 both-store +
  null-not-drop, Q2 per-fund + CONSERVATION AC, Q3 two tables, msn sparsity law). Schemas pin on
  tonight's landed bytes. Post-fire harness staged (above).
- **yaliu = SmartX account of record** (Andrew S2, lock ff6ae74d8; doc sec 7c @ 2b0187c94):
  opal7 = feeds 1-7; yaliu-bundle in SM verified w/ full 22a battery incl. negative control.
  Feed-8 build (task) = behind a DS expectation skeleton, off the parity path.
- **D2:** wrapper CLOSED @ a7adebf39 (feed-8 re-parented to WS-B1); fresh-CRS 99.43% closed.
- **Cadence facts (R4):** sweep/detail/nonzerosleeve are 20260714-latest = ad-hoc-pull feeds,
  latest-available, NOT stale; new basenames (nonzerosleeve.json/detail.json/
  allocation_accounts.json) need TF event rules via [0.7.0_AE_CloudOps] when families wire.
- **Standing holds untouched:** INF chain/Door 5-6, stamp order, 0824/0833 never-summed,
  MDPF_BASISSWITCH sovereign-held, bronze-raw 17a, vendor egress (ORION/SMARTX lifted, rest held).
- ~A lane note: commits under the base author line from the ~A session (822474a03 OPAL_TAXSMA,
  dbfe8c3a9, c5a9418dd) are the sovereign delegate's own work, not this lane's.

## Compiler Tools

This 17-minute window: test suite x2 (68 OK), safe-commit gates x1 -- all PASS. (Full-window
tool tables live in the two prior logs today; gap unchanged: monolith + SM comp-tool coverage.)

## MCP traffic

4 this window: DS pins-filed -> my triage -> DS RAVC-CLOSE; CTO GO request (OPEN). Plus this
handoff. All other loops closed.

## Next Steps

1. [reset session, FIRST] startup steps above -- REAP BOTH ORPHANS, re-arm inbox Monitor +
   landing watch. Deadline-critical: the landing watch must be live before 21:56Z.
2. [reset session, 22:00Z] the fire sequence above -> COO report -> ETF schema pins.
3. [reset session, on CTO GO] part-2 run 1 (staged driver) -> families 2-6 in pinned order.
4. [1.0.0_SA_CTO] holds: the per-family GO. [0.4.0_DS_ClientPlatform]: event-driven on my fire
   announcement; feed-8 skeleton when it suits them.
