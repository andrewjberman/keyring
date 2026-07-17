# 0.8.0_AE_CloudComp~D — KUZUSPLIT P0 close + COMPSIMILAR PH1 grounding/route (session)

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, COORDINATE
**Serial:** 0.8.0_AE_CloudComp~D (globgrph-platform build lane) · **Date:** 2026-07-17 · **Window:** session start (~2046Z) -> ~2140Z

## Summary
New lane ~D came online (Andrew ~D staffing, LD-0305) as the build lane for the two globgrph-platform
projects. Drove NFRA_KUZUSPLIT P0 (instrument) to CLOSE with exercised numbers, then COMPSIMILAR PH1 to its
arch gate. Both lanes now at real external gates (CTO rulings), no stalls.

## Work done
1. **Startup** — /watcher (registered LIVE PID 22212, persistent Monitor `bsc0hl27e`, LD-0290 serial written),
   /cloud-ops loaded. ACK'd COO GO 203150Z (KUZUSPLIT GO LIVE) + 205139Z (COMPSIMILAR PH1 GO) + the ADOPT-base
   amendment + base's handoff.
2. **NFRA_KUZUSPLIT P0 INSTRUMENT — CLOSED (@b0c94d9ff).** All six measurements EXERCISED (Rule 22a), run into
   scratch `--db` paths so the shared canonical was never disturbed:
   - M1 full reload = **482.26s** (PRD guessed ~356s -> real +35%). M2 incremental = **5.20s** (0-delta warm).
   - M3 AC-1 ambush: forced a faithful large delta (copied canonical, flipped all 20,429 node snapshot_ts) ->
     `rc=2 "delta 20429 >= 4000 and >= 25% of head (full-derive overwrite)"` in 4.85s -> current code falls to
     full 482s => **~487s per-worker morning ambush** = the number that justifies the split + the §4 hard gate.
   - M4 rate = ~1 full/day/box on active days (empirical: comp-kuzu on 4 distinct days 07-14->17); SHARP finding:
     NO persistent fallback-log sink (events -> ephemeral stderr) -> the "UNSURFACED" gap, feeds P3.
   - M5 shared-warm CONFIRMED (needs_refresh=False,current -> peers ride warm shared canonical @~0).
   - M6 habit = the involuntary post-nightly comp-kuzu ambush, NOT hand-run comp-aws derive (derive=0 vs
     comp-kuzu=64 in telemetry). Not ambiguous in the sizing-relevant direction.
   - Deliverable committed + pushed; reported P0-complete to COO (his trigger to sequence P1). COO RAVC VALIDATED
     ("exemplary", "482s real vs 356s guess"), sequenced P1 to CTO code arch-gate + flagged the carve-out.
3. **NFRA_COMPSIMILAR PH1 — grounded + specced + routed (@758632bc6).** ADOPTED base's summary_corpus.py (did NOT
   rebuild; --self-test PASS 4/4). Mandate phase-1 grounding DONE: resource_summaries ABSENT (net-new), graph_nodes
   has no summary field. Authored the table DDL (cse_store precedent: Nessie catalog, append-only ARN-keyed,
   latest-version-wins, one marker-HEAD, no freshness-twin, taxonomy-conformant) + the KUZUSPLIT coupling
   reconciliation (summary = editorial OVERLAY re-applied in BOTH comp-kuzu-full AND -inc after every graph delta
   = ONE overlay-over-two-graph-modes refresh path). Surfaced the ONE arch fork (write path: Nessie-in-VPC rec vs
   the TO's Glue IAM hint) to CTO for the plan-gate.

## Compiler Tools
| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-kuzu | `--json MATCH (n:CloudNode) RETURN n.*` | PASS | grounded graph_nodes schema (no summary field); auto-fired a live small-delta incremental (stayed incremental, corroborates P0) |
| comp-manifest-check | (P0/P1 mandate, not yet due) | N/A | binds when the two comp-kuzu-{full,inc} executables land (P1) |
| kuzu_nessie_load / kuzu_incremental_refresh | timed subprocess exercises (M1/M2/M3) | PASS | the P0 measurement instruments themselves |

**What worked:** exercising the real path (Rule 22a) surfaced the +35% cost error the PRD carried; the forced-large-
delta mutation faithfully tripped the exact "full-derive overwrite" branch.
**What failed:** none.
**Gap found:** no persistent local-refresh/fallback log sink exists (M4) -> P3 should add `last mode + behind-by-N +
last-full-at` to `comp-graph status`.

## MCP traffic
~7 messages. Significant: COO GO 203150Z (KUZUSPLIT GO LIVE) + 205139Z (COMPSIMILAR PH1 GO) + ADOPT amendment;
base handoff (adopt summary_corpus.py); my ACK+P0-plan (COO RAVC VALIDATED) -> P0-complete report (COO VALIDATED,
sequenced P1) -> COMPSIMILAR write-path arch-fork routed to CTO (213522Z) + FYI COO.

## Files Modified
see commit messages: f51c33ec2 (TO flip staged->pending), b0c94d9ff (P0 sizing-basis deliverable), 758632bc6
(COMPSIMILAR PH1 table-DDL + projection design).

## Blockers
NONE (no assumption-blocks). Both lanes are at REAL external gates, stated plainly:
- KUZUSPLIT P1 (command split) -> CTO code arch-gate; COO carries the GO on gate-clear.
- COMPSIMILAR store-writer/TF -> CTO write-path ruling (Nessie-in-VPC vs Glue); projection -> KUZUSPLIT P1.
These are the legal-defer exception (hard external gate), not a coast. Monitor `bsc0hl27e` live for CTO/COO replies.

## Current State
- ~D LIVE (PID 22212), Monitor `bsc0hl27e` armed, serial file written.
- KUZUSPLIT: P0 CLOSED @b0c94d9ff (deliverable at .../deliverables/KUZUSPLIT_P0_INSTRUMENT_SIZING_BASIS_20260717.md).
  P1 pending CTO arch-gate. Design fully fixed by ratified PRD + Andrew O-1 (comp-kuzu-inc = serve-labeled-stale,
  never full). Code touches infra/aws/globgrph + .tools/comp-kuzu-{full,inc} + org/modules/graph (latter needs the
  GRANTOR-LANDED carve-out at P1-open).
- COMPSIMILAR: PH1 design @758632bc6 (.../deliverables/comp_similar_phase1/PH1_TABLE_DDL_AND_PROJECTION_DESIGN_20260717.md).
  Engine adopted (base's summary_corpus.py, PASS 4/4). Table code will live in infra/aws/globgrph (AE-writable, no
  carve-out for this slice). Apply held for CTO plan-gate.

## Next Steps
1. **[1.0.0_SA_CTO]** rule the COMPSIMILAR write-path fork (Nessie-in-VPC rec vs Glue) at the plan-gate; arch-gate
   the KUZUSPLIT P1 code + grant the project-scoped GRANTOR-LANDED carve-out.
2. **[2.0.0_SA_COO]** carries the KUZUSPLIT P1 GO the moment CTO gates the code.
3. **[me, on CTO write-path ruling]** IAM simulate the exact ARN -> author resource_summaries_store.py (cse
   template) + TF -> route the held plan for CTO's plan-gate (no apply before it).
4. **[me, on KUZUSPLIT P1 GO]** build the command split (kuzu_cli.py mode flag + two wrappers + serve-labeled-stale
   branch) + the COMPSIMILAR overlay projection together (ONE refresh path); comp-manifest-check green; docs same-wave.
