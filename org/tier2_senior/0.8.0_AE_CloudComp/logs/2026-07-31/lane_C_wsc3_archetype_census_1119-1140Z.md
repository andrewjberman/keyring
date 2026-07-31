# 0.8.0_AE_CloudComp~C -- NFRA_VELOCITY WS-C3: archetype census + pattern inventory

**archetype:** VALIDATE
**secondary_archetypes:** EXPLORE, SCRIBE
**Window:** 2026-07-31 ~1119Z -> ~1140Z (site Z). Lane `~C`, logged to the base folder (no `~C`
agent folder exists).
**TO:** `NFRA_VELOCITY_CORE.WS-C3.archetype-census-and-pattern-inventory` @d9131fdd7
**Status:** DELIVERED @29b5ccacc. **CTO~Z GATE: PASS** (all three load-bearing claims independently
re-derived to the digit). CVO~Z verify next. Item 8 = this log.

## Summary

Built the archetype census and pattern inventory for P2. The headline result is that **the TO's own
axis does not resolve**: "per-plane" names two different vocabularies, and the graph's own `layer`
property disagrees with itself between nodes and edges. Published on the measurable axis with the
inconsistency stated, and ROUTED the vocabulary decision rather than picking one -- CTO~Z accepted
it as WS-C1 round 2 and is carrying it.

## Deliverable

`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_VELOCITY_WSC3_ARCHETYPE_CENSUS.md` @29b5ccacc
(+272). TO flip @d9cb1e6a1. Both pushed; repo 0/0 at close.

## Findings

1. **"PER-PLANE" IS NOT WELL-DEFINED.** `type_tuple.plane.enum` (source/projection/desired/applied/
   live/mixed/graph-cache) and the graph `layer` property are two axes sharing one name. **And
   `layer` is internally inconsistent: NODES carry a `portal` plane -- the LARGEST at 11338/20473 =
   55.4% -- and EDGES CARRY NONE.** `RENDERS` (2447) and `PROP_PASSES` (1382), the exact edges
   `c1_frontend_adapter` calls "the FRONTEND mass", are labelled `aws` while their endpoints are
   labelled `portal`. **A per-plane edge census therefore reports the frontend as cloud.** Routed,
   not resolved: picking an axis is a vocabulary decision.
2. **40% OF EDGE MASS CANNOT CARRY A MOTIF.** `ms` + `semctl` = 16535 edges (40.4% of 40912) across
   THREE distinct edge types, all containment/ownership -- no flow, no control, no transform. A hard
   ceiling on any motif census. CTO~Z had not seen this one and is folding it into the tick-29 record.
3. **"REGISTERED TOOLS" IS FIVE POPULATIONS**, all from ONE `comp-manifest-check` run: 87
   tracked+committed / 69 tools_index / 18 excluded / 70 entries-tools / 90 coverage-map. Against
   PRD "~96" and `ls` 94 -- seven numbers for one concept. Ratio published against every denominator.
4. **THE DEMAND SIGNAL IS DEVICE-LOCAL, LIVE, AND 92.7% UNATTRIBUTED.** `comp-which-rail.log` read
   187 (PRD) -> 261 (CTO~Z) -> 330 (me ~1120Z) -> **399 (me ~1135Z, same session)**. Per-device is
   necessary but NOT sufficient -- it needs a VINTAGE, because the log is append-only-live. Only 29
   of 399 lines carry a serial, so the tool-gap list was ranked on a structural criterion instead.
5. **I IMPEACHED MY OWN CONFIRMING RESULT.** The compression ratio (16 patterns / 69..96 tools =
   0.23..0.17) CONFIRMED the PRD's "far smaller" prediction by 4-6x. Flagged anyway: the pattern
   count comes from two CURATED CATALOGUES, and a catalogue is curated to be small -- **the ratio
   would land near this value whether or not the estate is redundant, so it is not evidence about
   the hypothesis.** An independent enumeration of observed motifs is the real test; routed.
6. **VINTAGE DRIFT, 4 of 11.** Rule bank D1/D2 `graph_evidence` (stamped @2026-07-23) vs live
   @07-31: `WRITES` 562->551, `READS` 712->703, `TRIGGERS` 145->149, `EMITS_TO` 144->145; 7
   unchanged. **NOT a defect** -- the figures were stamped, which is the only reason drift is
   detectable. Evidence the vintaging practice pays.
7. **A HYPOTHESIS OF MINE, FALSIFIED.** I suspected my own comp-* calls were inflating the rail
   count. Measured: **1 line of 399 carries my serial.** FALSE. Recorded rather than shipping a
   contamination caveat the data does not support.

## Compiler Tools

| Tool | Invocation | Expect | Result | Note |
|---|---|---|---|---|
| `comp-kuzu` | per-plane edge-type census | frequency by plane w/ denominator | **PASS** | 56 rows, 40912 edges, reconciles to the DB's own count |
| `comp-kuzu` | per-plane node-label census | node population by plane | **PASS** | 5 planes, 20473 nodes; surfaced the node/edge plane inconsistency |
| `comp-manifest-check` | `completeness` | authoritative tool count | **PASS (finding)** | returned FIVE denominators, not one -- finding 3 |
| `comp-which-rail.log` | line + verdict census | demand signal | **PARTIAL** | device-local, live-growing, 92.7% unattributed -- finding 4 |
| `safe-commit.sh` | x2 (TO flip, deliverable) | clean commit | **PASS** | surface-check OK, risk-reflex CLEAN (measured, 1484 danger nodes) |
| `git ls-files` / `check-ignore` | rail-log tracking status | tracked vs ignored | **PASS** | UNTRACKED, `.gitignore:68`; positive control `CLAUDE.md` reads TRACKED |

**What worked:** reconciling every total against the instrument's own denominator. That is the only
reason finding 8 below surfaced.

**What failed (mine):** **my verification parse used `[A-Z_]+` for edge-type names, which silently
drops every type containing a digit.** It lost `READS_S3` (323) and `WRITES_S3` (275) = exactly the
598 shortfall against the DB's 40912, **and would have had me "correct" a correct hand-computed
figure downward.** Caught only because the total did not reconcile. This is the fifth instrument
defect of mine this session and, like the other four, a control caught it rather than care.

**Gap found:** `comp-kuzu` exceeds a 120s foreground timeout routinely on this box and backgrounds.
The hazard is that a backgrounded completion reads as a null result unless the agent returns for the
output file -- **a tool's non-return is a MISSING OBSERVATION, never a measurement.** Same gap as
logged in the 0245-0450Z window; no tool change proposed. This window I read every backgrounded
output.

## Blockers

None. Finding 1 is ROUTED, not blocked -- the census shipped on the measurable axis with the
inconsistency stated.

## Current State

- WS-C3 delivered @29b5ccacc, **CTO~Z gate PASS**, CVO~Z verify pending.
- **The `layer`-axis decision is CTO~Z's (WS-C1 round 2). I must NOT start it** -- explicit.
- `watchdog-observe` ranks LAST in the tool-gap list DELIBERATELY (building a monitor is moratorium
  work, unauthorised by this TO). CTO~Z confirmed explicitly so the ranking is not read as a build
  queue.
- Rule bank NOT touched this window. Three items routed to CTO~Z in the deliverable's S.8.
- Held-out fence intact: shaping corpus published in S.0; `ADVI_PERFORMANCE` / `MDPF_GLOBAL` appear
  exactly once, in the not-drawn-on declaration.
- **UNREAD BY ME:** CVO~Z's fence ruling @82b2efb4a ("a GATE WITH NO OWNER") landed after my commit.
  Flagged to CTO~Z; will re-check this deliverable against it if it changes what a rail author owes.

## Next Steps

- **[3.0.0_SA_CVO~Z]** verifies WS-C3 within its exposure bindings (the census is measurement and so
  is verifiable; the axis question is vocabulary and is not theirs to rule).
- **[1.0.0_SA_CTO~Z]** carries the `layer`-axis decision as WS-C1 round 2, and the independent
  motif enumeration that would make the compression ratio load-bearing.
- **[0.8.0_AE_CloudComp~C]** IDLE-BUT-WARM after this log. Nothing else in CORE without CTO~Z's word.
