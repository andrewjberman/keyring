# 4.0.0_SA_CRO -- the #2/#4 field-2 walk (both CONFIRMED) + the memory content-staleness census (~20%, twice-measured) (2026-08-06 12:50Z -> 13:50Z)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, SCRIBE

## Window

Fresh session, 12:50Z -> 13:50Z. 2 workspace commits + 1 memory-repo commit. Prior log:
`logs/2026-08-06/canonical_render_class0_and_rcg_ferry_2205-0435Z.md` @8bcc4389f.

## What happened

**0. Startup clean.** Predecessor registration was a leftover (recorded PID 29072 dead in both
process tables -- discriminated by PID per the watcher doctrine, no identity conflict); re-registered
PID 36516, Monitor b5jhlmi6b armed + TaskOutput-confirmed, zero crons, PATH 96/97 + exercise PASS,
audit-archive-invoker rc=0. One stale ~SWEEP lane FYI (the 08-04 B-0001 staging notice) archived --
its subject landed 2 days ago.

**1. The #2/#4 field-2 rows WALKED -- both CONFIRM the reasoned mapping. @54b6ae2c7.**
Discharges the canonical's own hold ("do not build on the #2/#4 rows until someone walks them").
- **#2 GRAIN SHIFT -> "not traversed"**, on D-7: the self-route gate's population is
  sorted(tools_index) keys -- 72 tool-grain members vs 324 live subcommand-grain members, zero of
  which can enter. Mutant exercise (in-process, PURE -- never invoked the live router, because the
  harness's own header documents gate runs polluting the rail log it measures): growing the
  subcommand surface both ways it grows in life left the universe and all 72 tested queries
  byte-identical.
- **The sharpening: TRIGGER-GRAIN IS NOT VERDICT-GRAIN.** The gate FIRES on a subcommand edit
  (manifest_check_cli.py:699-701 diffs tools_index keys) and still verifies the tool-grain property.
  A gate that visibly runs on your edit reads as coverage of your edit. Handed to CTO for routing
  (gate owner 0.8.0_AE_CloudComp); not mine to take.
- **#4 VOCABULARY POVERTY -> "coerced to nearest sayable"**, on auth_api_gw
  (extract_routes.py @b9f80e6dae): 3/3 authorizer references in the file are a field, a comment, and
  the origin-type assignment at :1053 -- zero code consults an authorizer, so bool gets the nearest
  sayable True. Cost measured (MACHINEFLAG R1 false-secure, P1). The widened-vocabulary remedy
  already exists one field over in the same dataclass (:177-181 UNDETERMINED-not-absent).
Walk record: `deliverables/FIELD2_ROWS_2_AND_4_WALKED_20260806.md`.

**2. MEMORY CONTENT-STALENESS: measured, twice, ~20%.** Discharges the 08-05 OPEN+UNMEASURED item.
- **Deep sample:** seeded RNG (seed=20260806, printed), 30 of 1,010 files, every file read, live
  checks where cheap (F6 marker verified IN S3 updated today; COO~B NOT REGISTERED; all 7 lane-split
  subject projects `complete`). Verdict: 20 TRUE / 4 true-with-stale-tails / 3 PARTIAL-STALE /
  3 STALE. 6/30 = 20%, CI 8-39%.
- **Mechanical pass:** 868 path citations across 402 citing files tested; 80 files (19.9%) hold
  unresolvable cites (upper bound; false-positive modes named: script-relative lib/ paths,
  illustrative tokens). Different derivation, same rate -- a real convergence, not an echo.
- **The worst two specimens are exactly the predicted hazard class:** the 270s-cadence blanket
  (2026-04-27) contradicting the entire loop-retirement arc, and "CTO~B is GONE" while CTO~B
  committed this morning.
- **The COO~B lane-split file is a live specimen of the RETIREMENT shape** my FIVE_SHAPES audit
  named as candidate-sixth on reasoning alone -- the census is the incident that hypothesis lacked.
- **6 files annotated** with dated, additive, provenance-preserving UPDATE notes (memory repo
  @69ff771; no rewrites, no scope adjudication -- the 270s note explicitly surfaces-not-rules).
- **SECURITY FLAG, routed not self-remediated:** one memory embeds a plaintext portal credential
  (opal-users-v2 test login). Memory repo is local-only/no-remote (mitigating). Scrub/rotate/accept
  is Andrew's call; added to open-calls.
Census: `deliverables/MEMORY_CONTENT_STALENESS_CENSUS_20260806.md`.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-grep | auth_api_gw estate-wide; D-7 + self_route_verdicts consumer census | PASS | found the specimen files + the gate wiring chain; denominators printed by the tool |
| comp-glob | locating the ambiguous lib/*.py cites | PASS | killed a false dangling-cite class (script-relative paths) |
| comp-which | A.3 exercise probe | PASS | forwarder ran (banner produced) |
| comp-surface-check / comp-pulse | via safe-commit x2 | PASS | risk-reflex CLEAN, 1,659 danger nodes, denominator printed |
| python (as instrument) | manifest mutant exercise; memory census scans | PASS | the mutant is the load-bearing run: universe + queries byte-identical under subcommand growth |

**What worked:** exercising the gate's population invariant WITHOUT the live router -- the harness's
own header warns the gate pollutes the rail log it measures; the pure in-process form proves the same
invariant with zero pollution. And drawing the memory sample before reading any file.
**What failed:** my first dangling-cite instrument had two false-positive modes I only found by
spot-checking its output (regex truncation, script-relative paths) -- the triage layer is the
instrument; the raw pass is not. Disclosed in the census. Also one probe artifact: NFRA_COMPAWS.json
read failed on my locale-default cp1252 decode -- my probe's defect, not the file's; disclosed.
**Gap found:** volatile facts (seat state, "currently says", project phase) get banked without
in-line dates and rot silently -- the self-dating norm is proposed in the census as the zero-cost
standing control.

## Files Modified

@54b6ae2c7 (doctrine amendment + field-2 walk record), plus this log's commit. Memory repo:
@69ff771 (6 annotations). Scratchpad artifacts (not committed): dangling-cite maps, sample list.

## MCP traffic

OUT: walk-complete notice to [3.0.0_SA_CVO] (with the trigger-grain sharpening for their instrument
doctrine); canonical-amendment FYI + the routing-gate design question to [1.0.0_SA_CTO]. IN: none
(no inbox events this window).

## Blockers

**None.** Everything open is Andrew-paced or at an owning lane.

## Current State (zero-context handoff)

Section 9 of `INTENT_DENOMINATOR_SYNCHRONIZATION.md` is now FULLY EXERCISED -- the #2/#4
do-not-build hold is lifted, both rows confirmed on estate specimens. Memory staleness is MEASURED:
~20% (two convergent instruments), 6 worst files annotated @69ff771, full-corpus walk PROPOSED (a
funding/staffing decision, not mine to dispatch). RCG unchanged: ferry 9/14, 5 A-units at
0.6.0_AE_PartnerETL, the 1,552-file bundle at 0.7.0_AE_CloudOps behind their INF work.

## Next Steps

1. **[Andrew]** open-calls now carries FIVE: v6 band-172 - seeking-alpha trio - RCN-0005 - memory/
   remote decision - NEW: the embedded-credential scrub/rotate/accept call.
2. **[1.0.0_SA_CTO]** the routing-gate grain design question (route or decline; mechanism handed
   over) + the M13 naming inversion still with CTO~Z.
3. **[4.0.0_SA_CRO]** event-driven: RCG ferry closes as AE lanes answer; full-corpus memory walk if
   funded; field-2 rows now buildable-on for anyone who needs them.
