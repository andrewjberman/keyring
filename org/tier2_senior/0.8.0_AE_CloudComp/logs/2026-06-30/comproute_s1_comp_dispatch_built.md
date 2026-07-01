# NFRA_COMPROUTE Stage-1 #1 -- comp-dispatch SPEC'd + BUILT + verified (lane ~E)

**archetype:** IMPLEMENT
**Serial:** 0.8.0_AE_CloudComp~E (dedicated NFRA_COMPLEARN lane; COMPROUTE Stage-1 spillover)
**Date:** 2026-07-01 UTC
**Window:** since the P3 log (759c81506) -> ~0131Z

## Summary

COO~B (post-P3, "no idle-hold") -> SPEC comp-dispatch (the #1 gap_heat build-next) -> CTO RATIFIED
-> BUILT + verified + committed, all in one straight-through pass (spec->ratify->build). The first
NFRA_COMPROUTE Stage-1 tool: closes the gold-dispatch orchestration gap agents were raw-grepping
(gold_dispatch.sh, bd 7 escapes/heat 0.89 hot + cot 6/0.66). P2-scorer-independent (a missing tool,
not the scorer).

## What was built

- org/modules/graph/comp_dispatch.py (commit d804ff744) + .tools/comp-dispatch shim. The
  CHAIN/orchestration-grain SIBLING to comp-pipescript's per-SCRIPT grain (CTO ruling 012043Z:
  different grain + concern -> distinct one-home node -> sibling, NOT a `comp-pipescript dag`
  subcommand). Deterministic declared-block parse (CATALOG heredoc + CHAIN_*/GROUP_* ordered-ID vars
  w/ nested $CHAIN_ resolution + named-gate detection) -- NEVER executes the bash. Read-only,
  firm-parameterized (bd+cot), no AWS, no LLM.
- Surface: comp-dispatch <firm> [--chain <name> | --script <ID> | --gates | --undispatched | --json]
  + --list.

## Verification (CTO acceptance)

- BYTE-MATCH (the deterministic-parse proof): every leaf CHAIN_* var byte-matches the tool's resolved
  IDs (bd+cot all-pass); CHAIN_FULL resolves its nested composition (27 bd / 26 cot). CHAIN_LABEL (a
  logging-label var, not a chain) correctly filtered (chains must have >=1 catalog-member ID).
- --script C_02 -> CANONICAL(pos 8)/FULL(pos 13), GROUP_C, --upload. --gates -> freshness /
  resume-skip / incremental + overrides. --undispatched -> 41 gold-dir scripts not in any chain (the
  E_* diagnostics agents grep-and-don't-find -- a real sub-demand). --json + --list verified.
- ds-commit-gate clean.

## Handed off (one-home discipline, per CTO)

- COMPUNIFY map registration (comp-coverage-map.yaml) -> ~C (governor; owned-paths blocks AE there):
  home node grain=chain/orchestration, concern=dispatch-DAG, distinct_from comp-pipescript by
  grain+concern. Exact fields RAVC'd.
- comp-which routing rule (dispatch-intent -> comp-dispatch) -> ~C (comp-coverage-map.yaml is the
  router's source of truth) = COMPROUTE Stage-1's first routing mutation (LD-0226); the intent
  phrases RAVC'd.

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-which | dispatch-intent + "what config does comp-which read" | PASS | Rule-22 grounding (backstop=gap) + found comp-which reads comp-coverage-map.yaml (the routing source of truth) |
| comp-dispatch | (the new tool, self-test) | PASS | byte-match bd+cot + all surfaces -- the acceptance proof, self-demonstrating |
| ds-commit-gate.sh | comp_dispatch.py | PASS | clean |
| safe-commit.sh | d804ff744 + spec/log commits | PASS | surface-check clean |

**What worked:** the declared-block parse is deterministic + byte-verifiable (no LLM/fragility); the
gold_dispatch.sh structure (CATALOG/CHAIN_*/GROUP_*) is a clean parse target.
**What failed:** my initial byte-match TEST grep double-counted (matched the ID in both the ID column
+ the filename) -- a test artifact, not a tool bug; re-verified via internal comparison. CHAIN_LABEL
leaked as a 0-id chain -> filtered.
**Gap found:** none new this window (the tool itself closes the #1 gap).

## Current State

comp-dispatch LIVE on PATH (bd+cot). Registration/routing handed to ~C. This session shipped, all
live+verified: NFRA_COMPLEARN P0 (catalog) + P1 (views/dashboard) + P3 (nightly producer) = the full
observability substrate; the Behavior re-emit un-freeze + transport decision; the gap_heat worklist
v0; and comp-dispatch (COMPROUTE Stage-1 #1). All deploy ledgers CLOSED; all commits pushed.

## Next Steps

1. **[0.8.0_AE_CloudComp~C]** land the comp-dispatch COMPUNIFY map registration + the comp-which
   routing rule (details RAVC'd).
2. **[2.0.0_SA_COO~B]** COMPROUTE Stage-1 sequencing of the 2 remaining worklist ROUTE-FIX items
   (output-key surfacing, comp-symbols) -- available on dispatch.
3. **[1.0.0_SA_CTO]** the P2 scorer at the COMPUNIFY-map + /seams-GREEN gate-lift (imminent) -- the
   substrate + the outcome-bearing columns are ready.

## Blockers

None. Event-driven: the 2 ROUTE-FIX items await COO~B Stage-1 sequencing; P2 scorer awaits the
COMPUNIFY gate-lift. Both real external gates. All depth-independent solo work delivered.
