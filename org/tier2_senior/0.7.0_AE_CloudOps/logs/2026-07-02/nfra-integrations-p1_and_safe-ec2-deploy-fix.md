# 0.7.0_AE_CloudOps~A -- NFRA_INTEGRATIONS-001 P1 fidelity refresh + safe-ec2-deploy serial-fix

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, SCRIBE

**Window:** since `2026-07-01/ycharts-enable_deploy-selfcert.md` -> now (2026-07-02 ~13:43Z).
**Lane:** 0.7.0_AE_CloudOps~A.

## Summary

Two items closed this window, both continuations off the YCharts-enable deploy:

1. **safe-ec2-deploy.sh serial-resolution sub-fix** (COO-GO'd, in-lane SHARED_CLOUD_OPS) -- fixes the
   `deployed_by=unknown-agent` attribution + the bare-`git commit` contamination that failed the
   YCharts manifest record. Landed `16de6635f`, self-verified from main-tree + a detached worktree.
2. **NFRA_INTEGRATIONS-001 P1** (COO TO) -- source-vs-code fidelity refresh of the canonical
   `NFRA_INTEGRATIONS_STANDARD.md` (v1 -> v1.1) after P2 landed + YCharts deployed. Landed `6e4707bc5`.

## Item 1 -- safe-ec2-deploy.sh sub-fix (16de6635f)

Three legs (all `safe-ec2-deploy.sh` only, 52+/9-):
- **Worktree-aware `HALT_GATE_REPO_ROOT`** via `git rev-parse --git-common-dir` -> main tree, BEFORE
  sourcing the halt-gate, so the gate + attribution read the LIVE main-tree inbox+serial even from a
  build worktree. Case handles BOTH Unix `/...` AND Git-Bash Windows `X:/...` absolute forms.
- **`$AGENT` via `halt_gate_resolve_serial`**, fail-CLOSED (refuse `unknown-agent`; `AGENT_NAME` overrides).
- **Manifest commit via `safe-commit.sh --author "$AGENT" -- EC2_MANIFEST.json`** (contamination guard),
  replacing the bare `git add`+`git commit`; non-fatal (a landed deploy is never failed by bookkeeping).

**Self-verify (COO-required, no redeploy):** serial resolves `0.7.0_AE_CloudOps~A` from BOTH main-tree AND
a real detached worktree (before: `unknown-agent`); safe-commit committed **1 of 1073** dirty files; `bash -n`
clean. The self-verify CAUGHT a real bug (Windows `X:/...` git-common-dir fell through my `/*` case ->
broadened to `/* | [A-Za-z]:*`). CTO awareness-acked (Rule 7), no rework; owns the durable worktree/Windows pass.

## Item 2 -- NFRA_INTEGRATIONS-001 P1 fidelity refresh (6e4707bc5)

Fidelity pass on the canonical STANDARD (`docs/architecture/NFRA_INTEGRATIONS_STANDARD.md`), grounded
source-vs-code against `app/integrations/base.py` + `registry.py`. **Drift found (v1 predated P2) + fixed
(code = ground truth):**
- **sec7 (material):** min_tier enforcement was described as PENDING ("the P2 hook is in place at
  base.py:108-111"); corrected to LANDED -- `run_integration_tool` enforces `spec.min_tier` via
  `guard.enforce_min_tier` (base.py:114-126), CTO-byte-verified additive, live-exercised on the deployed
  gateway (YCharts below-tier deny).
- **sec4:** `run_integration_tool` 93-139 (was 93-126); ADDED `validate_integration_spec` (142-169);
  `SecretsCredential` 172-206 (was 129-163).
- **sec6:** `register_enabled` skip-registers an INVALID spec too (registry.py:43-63); + deployed-gateway
  fail-closed confirmation (YCharts box-verify, not source-only).
- **sec8:** cite `validate_integration_spec` as the machine-checkable 3-axis gate. **sec9/status:** v1.1.

AC2 (5-step mandate, sec5) + AC3 (INTEGRATION_FRAMEWORK.md pointer) were already satisfied in v1 -- confirmed,
no change. Committed via audited `GIT_COMMIT_AUTHOR_OVERRIDE=ANY_CTO` (docs/architecture lane; authorized by
the TO). RAVC'd COO CC CTO (arch-gate review).

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `safe-commit.sh` | 3 scoped commits (16de6635f, 6e4707bc5 via ANY_CTO override) | PASS -- contamination guard held (1/1073 demo) |
| `halt-gate-check.sh` (sourced) | serial-resolution logic reused for the fix + self-verify | PASS -- resolves ~A main-tree + worktree |
| `git rev-parse --git-common-dir` | worktree-aware main-tree resolution | PASS (after the Windows-path fix) |
| `bash -n` | syntax gate on the modified wrapper | PASS |

**What worked:** the halt-gate's `halt_gate_resolve_serial` was directly reusable for the attribution fix
(one serial source, both the gate + `$AGENT`). The COO-mandated worktree self-verify EARNED ITS KEEP -- caught
the Windows-path bug that a main-tree-only test would have missed. **What failed:** the pre-push HALT-gate
blocked the STANDARD push on a pending routine TO (the very TO I was executing) -> re-pushed with `HALT_ACK=1`.
**Gap found (banked earlier, recurred):** the comp-rail HUD false-positives on the literal `aws iam` substring
inside a quoted `deploy_ledger --proof` string -- match argv[0], not substring-in-args.

## Files Modified

See commit messages: `16de6635f` (safe-ec2-deploy.sh), `6e4707bc5` (NFRA_INTEGRATIONS_STANDARD.md).

## Blockers

None. External tails (not blockers): base 0.7.0 to hand off a scoped slice of ETFS_SETUP / DATA_PLATFORM
(next cloud-ops priority); COO accept + CTO arch-gate nod on the P1 fidelity refresh; CVO independent YCharts
cert next-session.

## Current State (handoff)

- `safe-ec2-deploy.sh` @16de6635f: worktree-aware + fail-closed attribution + safe-commit manifest record.
  Future EC2 deploys attribute to the real serial + won't fail on a dirty index. Durable worktree/Windows
  pass owned by CTO.
- `NFRA_INTEGRATIONS_STANDARD.md` @6e4707bc5: v1.1, source-faithful to base.py/registry.py as of 2026-07-02
  (P2 + YCharts reflected). INTEGRATION_FRAMEWORK.md remains a pointer.
- YCharts: live on the gateway (prior window); CVO independent cert is the only open tail there.

## Next Steps

- **[0.7.0_AE_CloudOps base]** hand off a scoped ETFS_SETUP / DATA_PLATFORM slice -> ~A drives it.
- **[2.0.0_SA_COO]** accept P1; **[1.0.0_SA_CTO]** arch-gate nod on the STANDARD v1.1 fidelity diff.
- **[3.0.0_SA_CVO]** independent YCharts cert next-session (durable S3-lake served records).
