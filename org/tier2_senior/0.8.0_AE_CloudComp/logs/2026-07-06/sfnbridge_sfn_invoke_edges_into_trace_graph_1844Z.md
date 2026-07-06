# SFNBRIDGE: SFN->Lambda invoke edges bridged into trace_graph (comp-blast blast-radius completeness)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

## Summary
Built NFRA_GRAPHUNI.SFNBRIDGE (Andrew + COO GO) -- a SEV1 comp-blast/comp-iam surface change that closes
a false-negative in the blast-radius graph: trace_graph modelled NO Step Functions, so comp-blast on an
SFN-orchestrated Lambda missed its orchestrator. Build complete + self-verified LIVE; the formal cert
(AC-3) is the async ~A oracle re-diff + CVO~B cert (both holiday-dormant). Design fully CTO-confirmed
(dual-edge). commit 3a7a6cce2.

## What happened

### Grounding (Phase-1) -- deep, because it's SEV1
- The certified walker: comp_aws_cli._sfn_task_invokes(def_str) -> [(state, target_arn)], pure Python
  (comp_aws_cli imports boto3 lazily inside _boto only -> reusable in the static build, no AWS dep).
- trace_graph: NODE/EDGE dataclasses, build_graph() orchestrates static extract passes (each reads the
  repo, zero API). comp-blast on a LAMBDA is DOWNSTREAM-ONLY (forward-edge-following); upstream only for
  function-grain or --direction.
- Definition source: aws_sfn_state_machine "yang_pipeline" (name YangDataPipeline) with
  `definition = file("${path.module}/yang-pipeline-definition.json")` -- a STATIC co-located file (no
  interpolation; = the deployed definition), so a static parse matches live. Only SFN in the estate.
- BEFORE-state exercised: comp-blast YangDataPipeline = NOT-FOUND (rc 3); comp-blast yang-generate-valuation
  --direction both = no STATE_MACHINE. Gap confirmed. comp-surface-check baseline clean.

### The 26-vs-27 reconciliation (Rule-22 grounding, flagged for cert)
Running the certified walker on the definition = 27 Task-state invokes but 26 UNIQUE (SM,Lambda) targets
(yang-generate-allocation-summary is invoked by 2 states). The definition is UNCHANGED since ~A's 07-01
census (git-confirmed) -> the oracle's "26" is unique targets. comp-aws's raw E() does NOT dedup (would
emit 27). Decision: bridge 26 UNIQUE dependency edges = the oracle + the correct blast grain (a Lambda's
blast radius includes its SM once). Flagged for ~A's re-diff.

### The build
extract_sfn.py (Pass 7): static-parse aws_sfn_state_machine -> resolve the file()/jsonencode definition ->
reuse _sfn_task_invokes UN-rewritten -> dedup to unique (SM,Lambda) -> emit DUAL-direction edges:
  STATE_MACHINE -[SFN_INVOKES]->   LAMBDA         (blast(SM) shows its Lambdas + comp-iam invoke view)
  LAMBDA        -[SFN_INVOKED_BY]-> STATE_MACHINE  (blast(Lambda) surfaces the SM -- the SFNBRIDGE goal)
Dual because blast(Lambda) is downstream-only, so surfacing the SM needs the reverse edge -- mirrors the
estate's CALLS/CALLED_BY convention (the "same as Lambda->Lambda" the TO cites). Bounded to invoke edges;
deep SFN stays in comp-aws. Wired as Pass 7 in trace_graph.build_graph (after the Lambda passes).

### AFTER-state (Phase-3, Rule-22 against the BUILT cache)
- Built cache: 26 SFN_INVOKES + 26 SFN_INVOKED_BY, 1 STATE_MACHINE node (sfn:YangDataPipeline).
- comp-blast YangDataPipeline: NOT-FOUND -> RESOLVES + shows the orchestrated Lambdas.
- comp-blast yang-generate-valuation: -> STATE_MACHINE(1) YangDataPipeline in its blast radius (the goal).
- comp-surface-check CLEAN before + after (no SEV1 regression).
- CTO CONFIRMED the dual-edge (his single SM->L spec was incomplete; my CALLS/CALLED_BY mirror correct).

## Compiler Tools
| Tool | Command | Result |
|---|---|---|
| comp-surface-check | check --file trace_graph.py/extract_sfn.py (before+after) | CLEAN both (no critical surface) |
| comp-blast | YangDataPipeline; yang-generate-valuation (before->after) | NOT-FOUND->resolves; SM now in blast radius |
| comp-build | rebuild graph with Pass 7 | 1857 nodes (+1 STATE_MACHINE); 26+26 SFN edges in cache |
| _sfn_task_invokes (reused) | on yang-pipeline-definition.json | 27 state-invokes / 26 unique targets (oracle reconcile) |
| ds-commit-gate | extract_sfn.py + trace_graph.py | PASS (incl. my own log-open-lint block-mode = clean) |

**What worked:** grounding the edge DIRECTION against how blast actually traverses (downstream-only for a
Lambda) caught that the TO's single SM->L spec would fail its own goal -> dual-edge; reusing the certified
walker un-rewritten kept it low-risk + additive. **What failed:** two safe-commit timeouts (surface-check
graph-load slow / lock contention) -- the commit landed each time, only the push lagged; re-pushed. **Gap
found:** the 26-vs-27 counting-grain (flagged for ~A's cert re-diff) -- a definition-unchanged reconcile,
not drift.

## Blockers
None on me. AC-3 formal cert is async-gated on the dormant owners (~A oracle re-diff + CVO~B cert); COO
dispatches on their post-holiday spin-up. TO = pending-cert, NOT blocked-on-me. CTO design-confirmed.

## Current State
- SFNBRIDGE build LIVE + self-verified (3a7a6cce2). trace_graph now models SFN invoke edges.
- All GO'd work closed today: TH-A (CVO-validated), utf-8-log lint (block-mode, CTO-closed), SFNBRIDGE (build).
- HEAD 3a7a6cce2 synced to origin/CLOUD.

## Next Steps
1. **[2.0.0_SA_COO]** dispatch ~A's 26-invoke oracle re-diff + CVO~B cert on owner-return (SFNBRIDGE AC-3).
2. **[me]** on cert-return: close SFNBRIDGE. TH-C stays parked on the DRV-flip/D1-GREEN (external).
3. **[me]** surface a next-ready in-lane slice to COO (lint-integration is ALREADY block-mode-complete).
