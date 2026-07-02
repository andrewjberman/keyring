# NFRA_TOOLHEALTH TH-B skeleton LANDED + emitter whitelist-extend + emit-unwired finding

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT (primary), DIAGNOSE, COORDINATE

## Summary
MSTR spawned base 0.8.0_AE_CloudComp for NFRA_TOOLHEALTH.TH-B. Cold-start clean, then built + landed +
got-accepted the TH-B 2-live-axis skeleton (the fused per-tool 3-axis health query), added the Phase-B
config-wire, and -- while grounding the separate emitter whitelist-extend deploy path -- surfaced a
source-confirmed silent-staleness finding (the tool_activity nightly emit is UNWIRED). 3 commits, all
pushed to CLOUD.

## What happened (window: session start 2026-07-02 ~19:00Z -> now)

### Cold-start
/watcher (registered LIVE PID 6980; persistent inbox Monitor brq8f6mtx; inbox pulled). /cloud-ops loaded.
Read the TH-B GO from COO~B + the TO + PRD + project JSON. Grounded the 3 live substrate sources (Rule 22).

### TH-B Phase-A skeleton -- LANDED + ACCEPTED (commit 64c89d675)
`org/modules/graph/comp_tool_health.py` (+ `.tools/comp-tool-health` shim, gitignored). ONE query ->
per comp-tool `{used, rail_consistent, effective, verdict in KEEP|FIX|PROMOTE|RETIRE}` + the PRD-SS3
taxonomy, over the LIVE COMPLEARN substrate (REUSED comp_learns_score.load_corpus + comp_route un-forked;
COMPLEARN stays closed).
- USED = tool_activity (rolling-log + telemetry) freq/recency/by-role + the RESULT-column mean OUTCOME
  value (the value-anchored signal, NOT raw count -- SS5 gate).
- RAIL_CONSISTENT = comproute-routing.jsonl route-wins (chosen-over-raw) + router-confidence annotation.
  HONESTY CATCH: my first draft over-flagged 20 tools FIX by treating router disambiguation-heaviness as
  per-tool bypass; I caught + fixed it (router hedging is the router's nature on ambiguous queries, NOT a
  tool bypass) -> FIX now comes from the value gate (known-low outcome), sparse + real.
- EFFECTIVE = pending TH-A; classify_full() is the one-line join seam.
- Live run: 50 tools, FIX?=3 (comp-drift 0.49/comp-constants 0.43/comp-tooltip 0.58, value-grounded),
  RETIRE?=4, KEEP?=43. --self-test 13/13 (incl. the load-bearing effective-alone-flips-KEEP<->FIX +
  zero usage-Goodhart + preventive-gate temper). --goodhart-audit proves NOT a usage proxy.
- COO~B ACCEPTED (builder deliverable); TH-V (CVO~B) is the formal acceptance gate (MSTR spawn requested).
- LANDING BLOCKER (resolved): owned-paths enumeration gap -- base 0.8.0_AE_CloudComp absent from the
  ANY_EXEC_OR_AE lane (only ~A-~E enumerated). Routed the exact 1-line fix to COO~B (SoD); COO~B landed
  the grant (.owned-paths.yaml, base added after line 524) -> committed.

### TH-B Phase-B config-wire (commit 6b641ff05)
`--effective-feed <json>` + `load_effective_feed()` -- makes the TH-A join a CONFIG wire, not a code
change. self-test now 13/13: added phaseB.effective_feed_flips_live_keep_to_fix (demonstrates the flip
END-TO-END on a REAL live tool: comp-pipescript eff=False -> FIX final / eff=True -> KEEP final). This
proves acceptance #2 machinery on live data; TH-A just supplies real probe values.

### Emitter whitelist-extend (commit d44cfcfd6) -- CTO arch-GO'd, INERT-until-wired
`infra/aws/globgrph/tool_activity_emit.py`: RAIL_ACTIONS += ROUTE-POSTERIOR + ROUTE-POSTERIOR-DISAMBIG.
The whitelist predated the COMPROUTE DR2 posterior router, dropping ~317 routing rows (~17% of route
signal) from the catalog + comp_learns_score + COMPROUTE telemetry. Validated (local emit): source=rail
2814 -> 3138 (+324 recovers the ~317 == the 2 tokens account for the full gap). CTO arch-GO (5/5 criteria);
(a) light-confirm cleared (no RAIL_ACTIONS enumerate/filter consumer breaks). COO~B ruled it a separate
forward-only fix I own (globgrph lane), NOT a COMPLEARN reopen.

### DIAGNOSE -- the tool_activity emit is UNWIRED (source-confirmed silent-staleness)
While grounding the emitter deploy path: the served warehouse parquet is 2d+ stale (2026-06-30 21:01 =
~E's local seed emit). SOURCE-CONFIRMED mechanism (CTO's definitive-check ask): Dockerfile CMD =
derive_runner.py only + tool_activity_emit.py NOT in the COPY set (not in the image) + no EventBridge
rule + no runbook -> no path runs the emit. tool_activity.tf comments assert a "nightly re-emit
(EventBridge->Fargate)" that does not exist (declarative drift). Same fail-silent class as the ETL
freezes. CTO ruled: fold the emit-wiring WITH the whitelist deploy + materialize the claimed emit.
DESIGN FORK surfaced + routed to CTO: the emitter reads 5 sources, 3 GITIGNORED/local-only (comp-which-
rail.log, comproute-routing.jsonl, agent_telemetry/*.jsonl) -> NO cloud-only runner can emit the full
catalog; the seed ran locally for exactly this reason. Options A(local-scheduled, rec)/B(sync-to-S3 +
GHA)/C(split) routed to CTO for the model ruling.

## Compiler Tools
| Tool | Command | Result |
|---|---|---|
| comp-which | comp-which "where is the tool_activity catalog + rail routing log queried" | PARTIAL (hedged near-tie -> read source directly; a coverage-gap datapoint) |
| ds-commit-gate | ds-commit-gate.sh comp_tool_health.py / tool_activity_emit.py | PASS (py_compile+AST+ruff py39, both files, each commit) |
| safe-commit | safe-commit.sh (x4: TH-B, Phase-B, whitelist; grant-blocked then unblocked) | PASS (owned-paths gate caught the base enumeration gap -- feature) |
| comp-surface-check | auto via safe-commit (all commits) | PASS (no critical surface touched) |

**What worked:** reusing comp_learns_score.load_corpus + comp_route un-forked gave the whole live
substrate free; the owned-paths gate correctly caught the base enumeration gap (SoD -> COO~B).
**What failed:** comp-which hedged on the tool_activity-catalog query (near-tie comp-dups/comp-platinum,
neither relevant) -> a genuine coverage-gap (this exact intent has no rich tool; noted, not chased).
**Gap found:** tool_activity_emit RAIL_ACTIONS whitelist drift (posterior-router actions dropped) -- FIXED
(d44cfcfd6); and the deeper emit-UNWIRED finding (nightly emit never materialized) -- routed to CTO.

## Blockers
None assumption-blocked. Three forward paths at REAL, freshly-fired external gates, each stated:
(1) emit-wiring model ruling -- CTO (RAVC in flight, design fork presented); (2) TH-V honesty verify --
CVO~B (COO~B requested MSTR spawn); (3) Phase-B full EFFECTIVE join -- TH-A (COMPPROOF-B1 resuming per
c77f5558a). Whitelist code committed but INERT until the emit-wiring lands (by design; folded per CTO).

## Current State
- comp_tool_health.py (org/modules/graph/, 700 lines) = the fused query. Invoke: `python
  org/modules/graph/comp_tool_health.py [--verdict|--tool|--json|--goodhart-audit|--self-test|
  --effective-feed <json>]`. Reads live logs via comp_learns_score.load_corpus (NOT the stale parquet).
- tool_activity_emit.py RAIL_ACTIONS extended (d44cfcfd6), inert until an emit runs.
- HEAD synced at push time; my 3 commits: 64c89d675, 6b641ff05, d44cfcfd6.
- Served parquet s3://opal-313476888478-globgrph/warehouse/tool_activity/ = 2026-06-30 (stale; emit unwired).

## Next Steps
1. **[1.0.0_SA_CTO]** rule the emit-wiring model (A local-scheduled / B sync+GHA / C split) -> I execute
   the coordinated deploy (whitelist d44cfcfd6 effective on first emit + the wiring), change-mgmt-ledgered,
   finish-in-session, verify the served parquet advances past 06-30.
2. **[3.0.0_SA_CVO~B]** TH-V: exercise comp-tool-health --self-test / --goodhart-audit / --json (the
   honesty acceptance gate).
3. **[0.8.0_AE_CloudComp / me]** on TH-A landing: pass its EFFECTIVE feed via --effective-feed -> full
   4-verdict + the real-tool FIX demo (acceptance #2 complete). Config-wire already built.
4. **[2.0.0_SA_COO~B]** the DE TSGRAPH dynamic SERVED_FROM bundle (heads-up received) awaits your formal
   dispatch to my lane (infra/aws/globgrph) -- on-deck.
