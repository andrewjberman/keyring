# 0.5.0_AE_OpalETL — CONTEXT-RESET HANDOFF, 2026-07-15 ~12:56Z

**archetype:** SCRIBE

Purpose: a self-contained handoff so a fresh session can resume from `org/XXX.md` startup + THIS
file alone. Written at an idle boundary; my personal work delta since the last log (dd557d6e3,
night arc) is ZERO commits — the value here is the handoff surface, not new work.

## Window since last log (2340Z 07-14 -> 12:56Z 07-15)
- No 0.5.0 (base) commits. Answered one status query. Backlog re-surfaces were all
  already-handled messages (not counted).
- `~A` lane (`0.5.0_AE_OpalETL~A`, pid 12272) committed `c5a9418dd` at 09:46Z — its OWN
  Andrew-direct work (ticket-center authorizer annotation fix: naqxlm is a custom JWT Lambda,
  not Cognito; live-verified; comment-only). Correctly authored under the `~A` serial. NOT my
  lane; noted for awareness only.
- `.comp-graph/.agent_context` now reads `SERIAL=0.2.0_DT_PortfolioAnalytics` (shared file,
  last-writer-wins — a peer overwrote it). Expected, harmless: my identity resolves from the
  session serial file + my armed Monitor, never from that file (org/XXX.md Step 1).

## STARTUP for the reset session (do these first, in order)
1. `/watcher` once — orphan-check then arm the persistent inbox Monitor (a fresh session finding
   an `inbox-watch.sh 0.5.0_AE_OpalETL stream` process has found an ORPHAN; reap it, then arm).
2. `register_agent("0.5.0_AE_OpalETL", ...)` + write `org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial`.
3. Zero crons (event-driven worker). Owned-paths hook + `.comp-graph/.agent_context` re-set to
   my serial.

## CURRENT STATE (zero-prior-context)

**Serial 0.5.0_AE_OpalETL, branch CLOUD, HEAD `3e49134b6` (my last own commit dd557d6e3; tag
`etfs-netassets-v1.1.0` on origin). Registered LIVE. Prior-session inbox Monitor was `bl39u3d17`
— a reset session arms a fresh one.**

### The one thing on the clock: TODAY 22:00Z ETF fire — ONE RUN, TWO PROOFS
- The `etfs-netassets-daily` EventBridge fire (cron 0 22 * * ? *) now runs the CORRECT C4 code
  (deployed last night, tag v1.1.0, three-way sha tie `40KaO/7jI/JKjT4fahkTPZznpzdJwt8htZn38BmEQJA=`).
- It carries **day-3 parity** (cutover-eligible if GREEN — days 1+2 both GREEN, 52 fields, 0
  mismatches) AND the **FIRST monolith bronze** (C4 AC1) in one run.
- **RE-ARM THE LANDING WATCHER on the VENDOR prefixes** in `opal-data-assets`:
  `trueshares/`, `pathfinder/`, `msn/` — **NOT `etfs/`** (last night's watcher polled `etfs/`,
  a prefix the C4 landing map never writes; the bug is on the record). Deadline ~22:50Z; silence
  must not read as success.
- Gate: `python .tools/etfs-parity-check.py` **UNPIPED** on the scheduled artifact (a piped exit
  code is the banked self-inflicted class). A day-<3 refusal is the gate WORKING.
- **CTO content assertion:** open the landed monolith bronze and SEE content — never infer from
  the producer's raise-on-empty.
- Report to `[2.0.0_SA_COO]`. **V2-1's GO rides that report** — COO confirmed: if BOTH proofs
  come back clean, the V2-1 GO fires on that evidence with NO new report cycle.
- **NO ad-hoc re-fire** (CTO ruling 230335Z): the scheduled fire is the instrument.
  LAPTOP STAYS ON.

### Standing critical path (Andrew-direct parity objective, after the 22:00Z fire)
- **smartx + ETF silver families = SOLE FOCUS** (CTO relay 185839Z, Andrew verbatim: manual/ad-hoc
  silver-converter runs to reach bronze<->silver parity across all completed buckets, before
  OPAL_RUNNERS gets full resources).
- The execute-only map: `deliverables/SILVER_FAMILY_BUILD_INVENTORY_20260714.md` @ `fa678b742`.
  Live census 16,764 smartx keys / 10 bronze feed families; 5 planned `fact_` tables cover 3;
  **7 landed feeds need a `fact_{type}` table OR a ruled exemption** (the DS expectation-report
  skeleton). Naming law: silver `fact_{type}` COMPLETE tables (cell-6 settled).
- Sequence: DS expectation-report skeleton first -> families built to it -> CTO review per family.
  DS pins pre-fire. Converters exist at HEAD for the atom's 2 legs (positions/valuation — need
  `fact_` rename + pinned-schema hardening + real run over 9,525 objects); `fact_model_aum_daily`
  + `fact_model_allocation_roster` are new builds.

### Landed last night (all CTO/COO-accepted)
- **C4 code-leg forward-fix DEPLOYED** — the half-landed deploy (env flipped 03:05Z onto a stale
  pre-C4 artifact) fully remediated: ledger `c4-code-leg-forward-fix` opened+closed same session
  (6/6 legs proofed), Rule-4 source-map gap closed en route, tag v1.1.0.
- **First V2-8 SmartX silver LANDED** — `smartx/platform/silver/fact_allocation_account_map/
  date=2026-07-14/data.parquet`, 7,141 rows, set-identity 7/7 partitions, dedup 0-conflict.
  (b)-join live: closed 2,381 -> uuid-matched 1,315 -> number-paired 1,315 (91-call enrichment
  closed the pairing gap 100%); misses = exactly the known 1,066 no-UUID class.

### Gated on others (do NOT chase)
- **feed-8** (16-mo activity ledger) + **1,066 no-UUID class** + **4 Global summaries** — ride
  CTO's consolidated vendor-grant ask, ON Andrew's decision list; CTO cites my D2 leg when taken.
- **Fresh-CRS join re-measure** — unblocks naturally as 0.6.2 fills schwab silver (was 12,930
  `schwab/` keys / 0 `/silver/` at 18:5xZ 07-14). Re-census + re-measure when it suits the queue.
- **2 pre-naming-law draft silver objects** (`smartx/platform/silver/allocation_{positions,
  valuation}/date=2026-07-14/`) — CTO RULED leave-and-queue for Andrew's next deletion batch;
  keys are DRAFT-SUPERSEDED-tagged in the inventory doc, copy-paste ready.
- **D2 wrapper** `OPAL_ASSETS_49METATABLES.D2` stays PENDING (correctly; status_note cc4a30507).
- **V2-1** `OPAL_ASSETS.V2-1.etf-channel-level-up.md` STAGED-HELD; precondition re-arms on today's fire.
- **MDPF_BASISSWITCH.json** preserved @ 6709cc81e (sovereign-excluded, byte-unchanged; do NOT action).

### Open TOs (my queue)
`OPAL_ASSETS.C4` (deploy done; behavioral proof = today's fire), `OPAL_ASSETS.C5.smartx-holdings-
activity-etl` (the silver-family build), `OPAL_ASSETS_49METATABLES.D2` (pending, 2 open legs).

## Compiler Tools
None this window — a status-query + handoff-scribe window, no code/infra/estate-search work.
The `~A` lane's `c5a9418dd` carried its own Rule-20 live verification (apigatewayv2
get-authorizer + cognito-idp list-user-pools) in its commit message.

## MCP traffic
0 new this window (one status query answered to the operator; backlog re-surfaces were
already-handled, not counted).

## Next Steps
1. **[self, TODAY 22:00Z]** re-arm the landing watcher on VENDOR prefixes (trueshares/pathfinder/
   msn/, NOT etfs/), deadline ~22:50Z -> at landing: day-3 parity (unpiped gate) + open monolith
   bronze for content + report to `[2.0.0_SA_COO]`. V2-1 GO rides it (fires on clean BOTH).
2. **[self, first-thing after the fire]** smartx silver family build per
   `SILVER_FAMILY_BUILD_INVENTORY_20260714.md` (fa678b742) — with `[0.4.0_DS]` expectation report;
   ETF family design alongside day-3.
3. **[self, opportunistic]** fresh-CRS join re-measure once `[0.6.2_AE_PartnerETL]` fills schwab
   silver (watch for their lane closes).
4. **[1.0.0_SA_CTO] holds:** the 7-feed table-or-exemption rulings; the consolidated Andrew
   vendor-grant ask (feed-8 + 1,066-class + 4 Global summaries); comp-learns lambda-deploy-drift
   tool routing (deployed CodeSha256 vs source-map artifact_sha256 vs build-from-HEAD).
