# NFRA_COMPDRIFT seam-6 git-code-heat parity ENGINE — BUILT + LIVE-VERIFIED (lane ~B)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE
**Serial:** 0.8.0_AE_CloudComp~B | **Date:** 2026-06-29 | **Window:** ~2028Z -> ~2041Z (follows the S3b log)

## Summary

After S3b was ACCEPTED, COO directed me off-idle to seam-6 parity (my area — I built the parity
columns). base-0.8.0 bound code_heat SOLO (no bind-support needed), so I peeled to seam-6 and
built the **git-code-heat parity engine** — the first GAP-seam binding closed in
`drift-topology.yaml`. CTO confirmed the standalone-engine approach + gave the fixed drift-record
contract; I conformed to it. Committed dd7cd996a.

## Work done

- New `infra/aws/globgrph/code_heat_parity.py` — standalone, independently-callable seam ENGINE
  (PRD 4b: comp-drift orchestrates, never inlines; P2/0.7.0_AE wires it). Reads the code_heat
  parquet parity signal (SELECT DISTINCT repo,repo_head_sha,computed_at), compares vs live
  `git rev-parse HEAD` per repo -> verdict current/BEHIND/UNVERIFIABLE, worst-of binding rollup,
  tri-state exit 0/1/2.
- Emits CTO's FIXED drift-record contract `{seam_id, binding, stage_from, stage_to, verdict,
  exit_code, grounding, detail, checked_at}` so comp-drift's unified board ingests uniformly.
  grounding cites the live read per repo (Rule 22).
- `tests/test_code_heat_parity.py` — deterministic coverage of all 3 verdicts (controlled
  now_ts) + contract shape. All pass.

## DIAGNOSE finding — vintage-primary verdict (flagged to CTO to bless)

Strict HEAD-equality (CTO's contract example) is **permanent-false-BEHIND** in this high-velocity
multi-agent repo: ajb_workspace HEAD advanced 15e3a25b -> 80814d1f -> eb609843 -> 4465cb00 across
~3 min of my own session. A HEAD-equality checker would be permanently red = noise. Shipped
VINTAGE-PRIMARY instead: `current` = vintage within `--max-age-hours` cadence (default 26h) even
if HEAD advanced (detail.head_state=head_advanced, EXPECTED); `BEHIND` = stale vintage (refresh
didn't re-run) or emitted commit absent from repo. HEAD-match preserved as corroborating detail.
Matches the manifest wording ("HEAD-pointer / vintage marker"). CTO loop sent for blessing.

## Compiler Tools

| Tool | Why | Result |
|---|---|---|
| `comp-which` | route to NFRA_COMPDRIFT seam-6 design | PASS — found PRD + drift-topology.yaml |
| `comp-kuzu` | (prior S3b window) graph join grounding | PASS |
| `ds-commit-gate.sh` (x4) | Rule-14 gate on engine + test | PASS |
| `safe-commit.sh` | Rule-14a commit | PASS — no critical surface |

What worked: grounding the verdict semantics against the LIVE repo's commit velocity surfaced the
HEAD-equality brittleness before shipping a noisy checker. Gap: none.

## Verification

- ds-commit-gate clean (engine + test).
- Live S3 code_heat artifact -> binding verdict=`current` exit=0 (vintage 0.56h fresh; HEAD
  advanced = expected). Grounded per repo against live git (Rule 22).
- Test: current/exit0, stale-vintage BEHIND/exit1, unreadable UNVERIFIABLE/exit2 — all pass.

## MCP traffic

Sent: Q to base (bind-support?), CTO loop-in + contract Q, CTO design-deviation RAVC, COO pick
RAVC + RAVC2-done, 0.7.0_AE P2 heads-up. Received: COO sync (off-idle directive), base SOLO-bind
GO, CTO contract reply, 0.7.0_AE ACK. Significant: COO GO seam-6; CTO contract + module-not-promote
ruling; base SOLO bind.

## Blockers

None. Open decision GATES (not blockers): CTO blessing on vintage-primary + the manifest coverage
edit (his authored ledger — I proposed, did not touch); 0.7.0_AE wires it in P2 (banked, not this
session).

## Current State

seam-6 git-code-heat parity ENGINE COMPLETE: `infra/aws/globgrph/code_heat_parity.py` (commit
dd7cd996a, CLOUD). Importable `check(source, max_age_hours)` -> normalized drift-record; CLI tri-
state exit. Co-located with the emitter it checks. NOT promoted to .tools/ (CTO: P2 promotes via
thin wrapper). seam-6 overall still PARTIAL (4 iceberg bindings = separate schema-fingerprint
engine, Trino-side, still GAP). Memory: `project_nfra_compdrift_seam6_git_code_heat_engine`.

## Next Steps

1. **[1.0.0_SA_CTO]** bless (or redirect) the vintage-primary verdict; apply the proposed
   `drift-topology.yaml` coverage edit (git-code-heat binding -> engine=code_heat_parity.py, COVERED).
2. **[0.7.0_AE_CloudOps]** wire the engine into the comp-drift orchestrator at P2 build-time
   (banked; will ping me if the record shape needs board tweaks).
3. **[0.8.0_AE_CloudComp~B]** stand ready for CTO blessing / COO's next pick (G2-increment-2 was
   the named alternative — awaiting COO confirm before pulling, it's nominally 0.7.0's lane item).
