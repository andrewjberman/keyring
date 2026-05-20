# ADHC_HALTGT.003 — safe-apply.sh terraform checkpoint

**Date:** 2026-05-20
**Agent:** 0.5.0_AE_OpalETL~B
**TO:** `org/tier2_senior/0.5.0_AE_OpalETL~B/task_orders/ADHC_HALTGT.003.ae-safe-apply-terraform-checkpoint.md`
**Commit:** `<filled at commit>`

---

## Current State

- **ADHC_HALTGT.003: COMPLETE.** `.tools/safe-apply.sh` shipped — the PRIMARY HALTGT
  net, gating `terraform apply` at the last reversible moment. Part of the COO~B batch
  GO; next in sequence: .004.

## What shipped

`.tools/safe-apply.sh` — a thin HALTGT-gated wrapper around `terraform apply`:
- Runs the `.001` checkpoint (`.tools/halt-gate-check.sh`, sourced) FIRST.
- Checkpoint blocks (STOP-class, or routine without `HALT_ACK=1`) -> exits non-zero,
  terraform is **never** invoked.
- Checkpoint passes -> `exec`s the terraform binary with every argument passed through
  unchanged; terraform's exit code propagates transparently.
- Gates `apply` only — refuses (exit 2) if no `apply` subcommand is in the args, so
  `plan` and other non-destructive subcommands are never gated (do_not compliance).
- `SAFE_APPLY_TERRAFORM` env override for the terraform binary (used by the anchor test).
- Git Bash 3.6.7-safe; ASCII only.

Usage: `safe-apply.sh [-chdir=DIR] apply [apply-args...]` — args passed exactly as to
the terraform binary, including the `apply` word. This explicit-passthrough form avoids
fragile global-vs-subcommand arg-position parsing and keeps the wrapper a true thin front.

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| Phase 1 — read `.tools/halt-gate-check.sh` + `safe-commit.sh` + `safe-deploy.sh` | OK | `.001` sourceable interface + exit-code contract clear; house wrapper style (arg passthrough, exit-code propagation via `exec`) established. comp-* N/A — `.tools/` shell not graph-modeled (PRD section 5). |
| Phase 2 — `shellcheck .tools/safe-apply.sh` | **NOT RUN — shellcheck not installed** in this Git Bash env. Substitute: `bash -n` clean. `# shellcheck source=/dev/null` directive on the source line. Self-audited: vars quoted, no banned utilities, exit code propagated via `exec` (not swallowed). Same env gap flagged in .001/.002. |
| Phase 3 — anchor test (`.runtmp/haltgt003_anchor_test.sh`, stub terraform via `SAFE_APPLY_TERRAFORM`, sandboxed inbox, `</dev/null`) | **11/11 PASS** | See transcript. |

## Verification — Phase 3 anchor test (11/11 PASS)

```text
== Case 1: STOP-class -> apply NEVER runs ==
  PASS: safe-apply exits 2 (STOP block)   PASS: terraform stub NEVER invoked   PASS: STOP surfaced
== Case 2: empty inbox -> apply runs, args passthrough, exit code propagated ==
  PASS: terraform exit code propagated (stub exits 7)   PASS: terraform stub invoked
  PASS: arg passthrough intact ("-chdir=infra/aws/terraform/x apply -auto-approve")
== Case 3: routine message -> blocks; HALT_ACK=1 -> apply runs ==
  PASS: routine(no ack) blocks, apply not run   PASS: apply not run on routine block
  PASS: HALT_ACK=1 -> apply runs (exit 7)
== Case 4: no 'apply' subcommand -> refused (apply-only wrapper) ==
  PASS: non-apply (plan) refused, exit 2   PASS: terraform not run for refused invocation
RESULT: 11 passed, 0 failed
```

The anchor test uses a stub terraform (records its args, exits 7) so the real binary
never runs. Case 1 proves the primary-net guarantee: a STOP-class message blocks the
wrapper and terraform apply is never invoked. Case 2 proves transparent passthrough +
exit-code propagation. Case 3 proves the non-interactive `HALT_ACK=1` re-invocation path.

## Next Steps

- `[2.0.0_SA_COO~B]` RAVC2 validation; routes to CTO~B. shellcheck-absent flag carries over.
- `[0.5.0_AE_OpalETL~B]` Proceed to ADHC_HALTGT.004 — CLAUDE.md rule mandating safe-apply
  + memory entry. Note: CLAUDE.md is BASE_EXEC lane, memory/ is CTO-lane — .004 will be
  drafted in the drafts/ lane and routed to CTO~B for canonical-apply.
