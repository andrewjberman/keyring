# ADVI_49F C02-g-7 Deploy-Ledger Ghost Sentinel Ruling

**Seat:** 1.0.0_SA_CTO
**Date:** 2026-08-31
**Source:** 2.0.0_SA_COO Msg-ID 89938

## Finding

The `deploy_ledger.py check --red` warning on `advi-49f-c02g7-five-date-forward-production` is a false integrity accusation against `0.7.0_AE_CloudOps~L`.

The deploy-completion entry at `org/critical_paths/change_management/20260830T0554Z_advi-49f-c02g7-five-date-forward-production_deploy_completion.md` reads `CLOSED -- nothing stranded -- closed 20260830T091856Z` and carries substantive proof for G1 through G6.

The sentinel at `org/critical_paths/.open_deploys/advi-49f-c02g7-five-date-forward-production.json` is a stale tracked snapshot:

- it contains only G1 closed and G2-G6 unproven;
- its committed state came from the 08:15Z halt snapshot after G1 and before G2-G6 were closed;
- the entry's later 09:05Z-09:18Z proof closures are present in the entry file;
- the worktree sentinel was restored by a later checkout/merge/integration window, then modified by `check --red`.

The issue is not that the entry was hand-edited into a false terminal state. The innocent mechanism is: `deploy_ledger.py close` removed the sentinel from the worktree, but that unlink was not committed; a later merge restored the tracked file from `HEAD`, creating a ghost open sentinel.

## CTO Ruling

The ghost sentinel is removed and the unlink is committed as the instance fix. Other deploy-ledger REDs are untouched and remain valid on their own terms.

This ruling does not independently re-verify the underlying G2-G6 S3 measurements. It only rules that the live gate accusation is unsupported because the entry and sentinel disagree for a complete, non-culpable git reason.

## Tooling Follow-Up

Standing tooling lesson to route separately: a deploy-ledger close that unlinks a tracked sentinel must either commit that unlink in the same closure path or make the red gate reconcile sentinel-vs-entry before emitting a NEVER#6-style accusation. An uncommitted unlink is a close with a one-merge fuse.
