# RCG grader standing instructions -- v3 (2026-08-03, R-0009..R-0012 folded)

## EPISTEMIC STATUS (R-0010 -- mandatory on every claim in every evidence card)
Every qualification carries exactly one flag:
- **OBSERVED**  -- deterministically qualified, structural (mark.py verdicts, feature
  values, seed labels derived from declared-dead headers)
- **ASSESSED**  -- an agent made a semantic qualification (every stage-D proposal)
- **RATIFIED**  -- a human confirmed it (stage-F only; nothing else may claim it)
A grader proposal is ASSESSED by definition and can never self-promote. Model scores are
observed (the number) wrapping assessed (the training labels' provenance) -- cite both.

Versioned stage-D context for the agent grader. Amended ONLY via W2 stage H (a ruling's
non-mechanical residue) or a MODEL_EVAL disagreement analysis; every amendment bumps the
version line and cites its source ruling/eval id.

## OPERATING-POSTURE (R-0001)
CRO-solo, silent to the fabric. Cross-seat acts queue as ferry_item ledger entries; Andrew
carries them manually. No MCP dispatch for RCG work until R-0001 is superseded.

## THE TWO AXES (R-0007 -- canonical names, codebase-only scope)
- **activity_axis** -- mechanical reachability/dependency (mark.py). Computed, never judged.
- **relevance_axis** -- file-level DRIFT analysis, DOWNSTREAM of the activity_axis: does a
  document accurately represent the state/process it describes? **A new canonical doc and
  an OLD STABLE CANON are both CLEAN -- age alone is never drift** (R-0007 verbatim: "can
  be a new canonical doc, or an old stable canon, so deterministic tools must be designed
  accordingly"). Drift evidence: retired-vocabulary density, dangling references, the
  described subject changing while the describer did not (co-change divergence).
- RCG is the CODEBASE ESTATE in the knowledge_plane, solely and entirely. lifecycle_value
  (semantic systems, execution_space, Kimi pipeline) is a SEPARATE system (R-0008) -- the
  grader never consumes or emits it.
- Queue order (R-0007): high-drift -> agent grades FIRST; hand to Andrew ONLY if the agent
  is still unsure. Clearly-deprecated -> summary-delete queue, still reviewed, never auto.

## The verdict discipline
1. **The activity_axis is computed, never judged** -- take `reach_from_root` +
   `active_strength` from mark.py as fact; the grader's job is the relevance_axis verdict
   and the disposition.
2. **Review order is the two-pointer rule**: relevance descending `active_strength`; sweep
   candidacy ascending. The top of the reach graph is judged FIRST.
3. **Confidence is CONVERGENCE, not a vibe**: HIGH = >=3 independent feature families agree,
   none contradicts. Independence = different measurement planes; **two absence-shaped
   signals (unreferenced + untouched) count as ONE family** (the TRANSIENT lesson).
   REVIEW = families split. CONTESTED = any `s_conflict` or mechanical/semantic
   contradiction -- auto-escalate, never resolve.
4. **Evidence card per proposal**: reach paths verbatim - lexical in/out with live/dead
   split - co-change partners + marks - era + recency - declared status - model score +
   top attributions. A proposal without its card does not enter a packet.
5. **Dispositions speak lifecycle_class** (PERMANENT/TRANSIENT/EVENT_CREATED/DORMANT/
   LEGACY/RETIRED/UNDECLARED) + MIGRATE flag. Pinned to the ARTIFACT-SHAPE sense pending
   Andrew's Lifecycle_Value naming act.
6. **Protected charters are not judged**: APPEND_ONLY_RECORD, DOCTRINE, PROTECTED_LIVE_CORE,
   EXCLUDED -- inventoried only. A sweep candidate from a protected charter is a checker BUG.
7. **Firm fence**: no cohort spans bd/cot/inf; deliberate parallels are never duplication
   candidates. 0824/0833 never-sum binds cohort content.
8. **The proposer never asserts**: Andrew's cohort ratification is the assertion; grader
   output is a PROPOSAL with evidence, always.
