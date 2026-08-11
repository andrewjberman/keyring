# ANDREW-DIRECT — THE BUILD ORDER OF OPERATIONS (five phases, sequential)

**Channel:** Andrew-direct at the 1.0.0_SA_CTO terminal, 2026-08-11 ~0810Z.
**Recorded by:** 1.0.0_SA_CTO same turn. **Broadcast:** COO + CVO + CRO base + CRO~A + MSTR.

## VERBATIM

> "Something that is crucial for this operation I believe is the order of operations. I think the
> first thing we need to do is update the scripting, and testing that the scripts compile properly
> stage by stage. Then we need to assess the eventbridge timing and event-based timing for each
> pipeline to make sure that nothing is wrongly-timed + we very likely want to shift all of this
> to the morning. Third, we want to assess the repoints and make sure that the runners are calling
> the right silver files (in opal-data-assets, not in their firm buckets) and exporting gold
> parquets to the opal-data-assets/portal/ buckets. Then we want to make sure that the frontend
> publishers are pulling from the correct locations. Then we need to systematically decommission
> all legacy paths once the portal is verified to be taking in data in correctly and displaying
> what it should be."

## THE FIVE PHASES (the build decomposition's governing sequence)

| # | Phase | Content | Composes with |
|---|---|---|---|
| P1 | **SCRIPTS** | Update the scripting per the ratified A/B/C/D specs; STAGE-BY-STAGE compile verification (the commit-gate's py_compile + per-group acceptance batteries are the mechanical support) | the five-spec set; EXTRACT-side admission |
| P2 | **TIMING** | Assess EventBridge + event-based timing PER PIPELINE — nothing wrongly-timed; **converge the whole flow to THE MORNING** (his standing morning-trigger vision made a phase). Output = the per-pipeline timing map + the ruled morning floor values | Group W (the A1-A5 tables + both-namespace dispatch census); the silver-completeness trigger requirement |
| P3 | **REPOINTS** | Runners READ silver from `opal-data-assets` ({vendor}/{firm}/silver) — NOT firm buckets; runners EXPORT gold PARQUET to `opal-data-assets/portal/gold/{product}/{scope}` | the M-row repoint map (CRO decom spec) + the X-acts in flight (the mdpf pilot's phase 3, already GO'd — they continue) |
| P4 | **PUBLISHERS** | Frontend/platinum publishers pull from the CORRECT locations (parquet gold, per the three requirements) | D-group publishers + the frozen-shape census; the wo2 one-ordered-act |
| P5 | **DECOMMISSION** | SYSTEMATIC legacy-path teardown — **GATED on the portal verified taking data in correctly AND displaying what it should** | the 19-channel disposition map; migrate-before-kill; never-widen where a served key moves (none should); CVO cert-of-built as the verification instrument |

## COMPOSITION NOTES

- Each phase GATES the next (his "then... then... then" is sequential, not thematic). In-flight
  mdpf cutover acts (X-iii/X-ii-a etc.) are the pilot's phase-3-class work already GO'd — they
  CONTINUE; the five-phase order governs the build decomposition from here.
- P2's "shift all of this to the morning" is a DIRECTIVE, not a preference: the timing assessment
  proposes morning-converged floor values, ruled at review (Group W's floors were already
  proposed-ex-ante pending the measured distributions — the morning constraint now bounds them).
- P5's gate is a VERIFICATION event (portal in-taking + displaying correctly), never a date — and
  the verifier is the cert-of-built chain, not a self-report.
