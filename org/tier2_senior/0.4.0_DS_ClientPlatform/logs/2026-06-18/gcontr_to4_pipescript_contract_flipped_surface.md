# NFRA_GCONTR.TO-4 -- pipescript --contract / --flipped value-layer surface

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Window
2026-06-18 ~1619-1628Z. Picked up off COO /drive capacity-check (GO 162024Z) -- productive use of
the pre-nightly window while the NNA/cot fixes are event-gated on tonight's nightly.

## Current State (zero-context handoff)
TO-4 COMPLETE + deployed. Added the VALUE-layer read surface to pipescript
(`org/modules/graph/pipescript_cli.py`, DS-owned, owned-paths 0096b5cbb -> same-tool lane,
commit-direct). Reads delegate to `contract_engine.py` (the canonical graph_contracts reader +
Q1/Q2 drift/flip logic) -- the CLI is the human surface, not a re-implementation.

- **`pipescript --contract <surface>`** (commit 0c8f73eae): declared contract (canonical_writer /
  canonical_producer / source_of_truth / period_defs / forbidden_writers / ratified_by / ratified_at)
  + observed writers on the WRITES edges into the contracted bucket(s) (latest snapshot), flagging
  drift (non-canonical or forbidden). Uncontracted -> LOUD `unreviewed` (exit 2), never silently clean.
- **`pipescript --flipped --since <snap>`** (same commit): per-surface writer-flip since <snap> via
  `contract_engine.run_contract_check(base_ref=since, current_ref=latest, window)` -> tag SANCTIONED /
  UNSANCTIONED / WATCH / CLEAN; then enumerate every `critical-surfaces.yaml` SEV1/SEV2 surface with NO
  contract row as uncontracted = LOUD unreviewed. Exit 2 on any UNSANCTIONED or uncontracted-critical
  (the CLI's own non-advisory signal; distinct from comp-surface-check's v1 advisory gate).
- Wired into `main()` argv dispatcher; module docstring usage updated; ASCII-only output (`_a()`),
  exit-code propagation via `return cmd_*()`.

Gate (TO-4 cross_domain): ground-truthed against the LIVE 3-row graph_contracts table (NOT TO-3's
`<status>` field, which is owed only its runtime value-check). SEV1 model_portfolios.benchmark row is
live + ratified -> TO-4's hard gate satisfied.

## Files Modified
`org/modules/graph/pipescript_cli.py` (+188 / commit 0c8f73eae); TO status staged->complete (3011fe9a6).

## FINDING surfaced by the tool (routed CVO/TO-3 + CC COO -- NOT a CLI bug)
`--flipped` tags model_portfolios.benchmark = WATCH, not UNSANCTIONED (the TO/molecule expected the
BMKAUD UNSANCTIONED catch). Reason: contract forbidden_writers (smartx-ingestion-role,
smartx-model-monthly-pull) do NOT exact-match the live edge via_role names (smartx-ingestion-lambda-role,
smartx-model-monthly-pull-role; note the missing -lambda-role/-role suffix). q2_join does exact set
membership -> 0 forbidden_hits -> WATCH. The smartx roles ARE writing into the benchmark bucket; the
never-widen tripwire is name-mismatched and may be INERT on live data (comp-surface-check shares the
engine -> same blind spot). CVO (contract-semantics owner) to confirm: intended-forbidden (then
forbidden_writers needs exact IAM names / contract_engine needs alias-normalization -> tripwire
currently inert) vs genuinely-distinct roles (then WATCH is correct). The CLI is faithful either way;
NOT hacked to force UNSANCTIONED. This is the false-clean-on-the-value-layer surface doing its job.

## Compiler Tools
| `<run>` (TO mandate) | Result | Observed vs `<expect>` |
|---|---|---|
| Phase-1: `pipescript --list` + sample `pipescript portfolio-management` | PASS | named-thread census renders; sample traversal works -> baseline reference recorded |
| Phase-1: `pipescript --gate-b` (pre-change baseline) | PASS | 25/25 named threads + gate-c 169 res/0 double-claimed |
| Phase-2: `.tools/ds-commit-gate.sh pipescript_cli.py` | PASS | exit 0 (py_compile + AST + ruff FA) |
| Phase-3: `pipescript --gate-b` (post-change regression) | PASS | 25/25 STILL pass -> --contract/--flipped ADDITIVE, non-regressive |
| Phase-3: `pipescript --contract model_portfolios.benchmark` | PASS | declared yang-pipeline-lambda-role + period_defs + ratified_by=Andrew + observed writers; exit 0 |
| Phase-3: `pipescript --contract model_portfolios.headline` | PASS | uncontracted-LOUD SEV1 (authored-but-not-loaded); exit 2 |
| Phase-3: `pipescript --flipped --since 20260617` | PASS | benchmark/peers/aum WATCH + headline/advisor_intelligence uncontracted-LOUD; exit 2; FINDING above |

- **What worked:** delegating all graph_contracts reads + Q1/Q2 logic to contract_engine.py -> the CLI
  is a thin faithful surface; mirrored surface_check_cli's call pattern (load_contracts ->
  contract_for_surface -> load_graph_snapshot -> run_contract_check/writes_into). Verified READY
  against the LIVE table, not TO-3 status.
- **What failed:** nothing in the CLI. The benchmark WATCH-not-UNSANCTIONED is a contract-DATA finding
  (above), surfaced by the tool as designed.
- **Gap found:** the BMKAUD never-widen tripwire is name-mismatched/possibly-inert on live data
  (forbidden_writers vs live via_role names) -> routed to CVO/TO-3.

## Blockers
None. TO-4 complete + deployed; RAVC2 to COO (CC CTO) + finding to CVO. Close-gate = COO RAVC + CVO
finding-disposition.

## Next Steps
1. **[2.0.0_SA_COO]** RAVC the deployed CLI (commits 0c8f73eae/3011fe9a6).
2. **[3.0.0_SA_CVO]** Disposition the forbidden_writers name-mismatch finding (intended-forbidden ->
   fix TO-3 contract data / contract_engine normalization; or distinct-roles -> WATCH correct, no-op).
3. **[self, event-driven]** Back to the NNA/cot nightly verifies (tomorrow-AM, separate threads).
