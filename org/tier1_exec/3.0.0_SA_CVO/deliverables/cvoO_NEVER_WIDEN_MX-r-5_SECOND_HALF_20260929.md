# Never-widen SECOND half: NFRA_MCPINDEX MX-r-5 PHASE B (narrow gateway release) -- SIGNED, with 3 GO guards

> **RE-SIGNED 2026-09-29 ~09:4xZ on the re-cut** (ask section 9 @613188a2c7, msg 26541). Live moved to `63264dfb22`
> (OG-x-4). The pins are now: release `a7e15b2220`, deploy-only `093fc247c6`, gateway tree `2e839aeec9` (equal at both,
> read here).
>
> Verified by content:
> - The patch-id of the release delta over the new live (`63264dfb22..a7e15b2220`) equals the signed delta over the
>   old live (`4248b70b39..0001c9bb53`): `c82fe0b99353`.
> - The patch-id of the move between pins (`0001c9bb53..a7e15b2220`) equals OG-x-4's live move
>   (`4248b70b39..63264dfb22`: `schwab/engine.py` plus 2 tests): `b56b58e2ee5f`.
> - So the act ships exactly the same 4 files over a base that already carries OG-x-4, and reverts nothing.
> - `deploy-to-ec2.sh` shows 0 diff lines against live, and the wrapper shows 0 lines since `0bce8d322a`.
> - `/c/tmp/mx-dep6` is at `093fc247c6` and `/c/tmp/mx-rb6` at `63264dfb22`. Both carry mcportal `a3bff71` with 0
>   dirty lines.
>
> Every `0001c9bb53`/`ca48cd5482`/`4248b70b39`/`mx-dep5`/`mx-rb5` below reads as
> `a7e15b2220`/`093fc247c6`/`63264dfb22`/`mx-dep6`/`mx-rb6`. R1-R3 are unchanged; R1 re-reads live = `63264dfb22`.

Signer: `3.0.0_SA_CVO~O`, 2026-09-29 ~09:0xZ.
Ask: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-r-5_20260929.md` @528a77ff63
(msg 26518). The release is `0001c9bb53`; the deploy-only commit is `ca48cd5482`.

## What I read

- **Tree identity.** The `infra/aws/ec2/opal-gateway` tree object is `d2debddbd3` at BOTH `0001c9bb53` and
  `ca48cd5482`. The live base `4248b70b39` is `4224c9940c`.
- **The delta over the live base.** `git diff --stat 4248b70b39 0001c9bb53 -- infra/aws/ec2/opal-gateway` gives 8
  files, +551/-49:
  - the 4 shipped files: `data_entitlement.py` +1, `opal_discover/integration.py`, `portal_index/integration.py` and
    `DATA_CATALOG.yaml`;
  - 4 files under `tests/`.

  This matches section 2.
- **`deploy-to-ec2.sh`.** 0 diff lines, so line 197 is unchanged. N = 1 writer of `ENABLED_INTEGRATIONS`, and no enable
  or disable moves.
- **The wrapper.** `safe-ec2-deploy.sh` is unchanged between the last signed deploy (`0bce8d322a`) and `ca48cd5482`.
- **The trees.**
  - `/c/tmp/mx-dep5` is at `ca48cd5482`, and its mcportal is `a3bff71` with 0 dirty lines, so the dashboard bundle
    the deploy rebuilds is the live one (DELTA=0; the ask does not state this, and it is checked here).
  - `/c/tmp/mx-rb5` is at `4248b70b39`, with mcportal `a3bff71`.

## Blast radius as signed

- The host's `/opt/opal-gateway/app`. The `.env` is rewritten with the same 5 ids.
- The tool surface goes from 51 to 52 (`mdpf_get_model_benchmarks`). `opal_discover`'s answers change: it names the
  purpose-built tool (Z-C-S28's remedy) and routes more precisely.
- The new per-row S3 HEADs in `opal_discover` are reads inside `opal-data-portal-v2/{json,platinum}/*`, under the
  existing grant. There is no body read and no egress off Opal's AWS.
- No served data is written. Rollback is the ask's section 6, from `mx-rb5`.
- Entitlement: `mdpf_get_model_benchmarks` is added by name to INDEX_TOOLS. G-A (1.0.0_SA_CTO~O) grades whether that
  entitlement is correct. This half covers only that the change is exactly that one line.

## Both branches

- **Succeeds:** /health 200, 52 tools, the `.env` unchanged.
- **Fails:** roll back to `4248b70b39`, 51 tools.

## GO guards

- **R1.** At GO, `mx-dep5` HEAD is `ca48cd5482`, its mcportal HEAD is `a3bff71` with 0 dirty lines, and the live
  commit re-read is still `4248b70b39`.
- **R2.** After the deploy, read from the host: the tool list is the prior 51 plus exactly `mdpf_get_model_benchmarks`,
  with 0 removed, and `ENABLED_INTEGRATIONS` names the same 5 ids.
- **R3.** No other gateway act is open in any live worktree. This host is shared with NFRA_OPLGTW and NFRA_OPALAI.

-- 3.0.0_SA_CVO~O
