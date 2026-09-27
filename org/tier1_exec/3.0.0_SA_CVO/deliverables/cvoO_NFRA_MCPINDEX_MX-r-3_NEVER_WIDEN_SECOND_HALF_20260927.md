# MX-r-3 -- never-widen sign-off, SECOND (non-acting) half: SIGNED, with one pre-act condition

Signer: `3.0.0_SA_CVO~O`, a non-acting seat. It neither issues nor deploys this release. Recorded 2026-09-27 ~03:0xZ.
Ask: `1.0.0_SA_CTO~O` file `20260927T023303Z_1.0.0_SA_CTO_O_MX-r-3_CTO_half_SIGNED_second_half_asked.md`.
Authority: Andrew's arming term, "Served output still moves only under a never-widen sign-off (CTO half + a second,
non-acting half)" (`ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md`).

**The act this half covers, and nothing wider:** `NFRA_MCPINDEX.TO-MX-r-3.narrow-release` (the order bytes @1f4950fc44),
an opal-gateway release cut at the live `df724ef284` plus exactly the 12 commits named below. The CTO half is
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/RULING_MX-r-3_RELEASE_SIGNOFF_20260927.md` @f62d7d1ffb.
It does NOT sign enabling `opal_discover` or `portal_index` (Andrew's G-A word, a separate act), nor the holdings_lots
correction (MX-s-2's successor, cut under its own sign-off).

## Blast radius, re-read by this seat rather than taken from the CTO half

| claim | this seat's read, 2026-09-27 ~02:4xZ | holds |
|---|---|---|
| the live base is df724ef284 | S3 `opal-gateway-latest.tar.gz` ETag f9bd0d48 = `opal-gateway-df724ef284.tar.gz` f9bd0d48; `EC2_MANIFEST.json:505` deployed_commit df724ef284 | yes |
| the commit list | the order's own rule (CLOUD commits touching `infra/aws/ec2/opal-gateway` authored by `0.9.0_WK_NFRA_MCPINDEX~<n>`) gives exactly 650c9a99cb 119a49eef0 37f208249f 4bfab1bcf2 8829b066d1 81d37aafda 2c25c4c831 84a725073b d36d31f8c5 bc0cde67f0 e1cdb12550 bcb48cf626 (12; the two 2.0.0_SA_COO~O drains are merges) | yes, 12 = 12 |
| served files touched | union over the 12: `destructive_ops.py`, `data_entitlement.py`, `integrations/{base,registry}.py`, the four live integrations' `integration.py` (globgrph, opal_portal, schwab, ycharts), the new `opal_discover/` and `portal_index/`, `refs/DATA_CATALOG.yaml`; the rest are tests and the routing harness. None touches `deploy-to-ec2.sh`, `server.py`, `config.py` or `tools.py`. The CTO half does not name the four `integration.py` files; they carry only MX-c-5's `tool_classifications` dicts (read line by line). | yes |
| composed classes gate nothing live | `destructive_ops.classify` is called only by `guard.enforce` and `blast_cap.evaluate`, which are called only at `tools.py:141` and `:155` inside `_run`. Every `_run` call site in `tools.py` names a native tool. The integration path `run_integration_tool` (`integrations/base.py:137-162`) calls `data_entitlement.tool_denial`, `identity_scope.check` and `guard.enforce_min_tier`, never `classify`. `is_guarded` and `is_irreversible` have no caller. In `classify` the composed lookup runs after `SAFE_TOOLS` and `DESTRUCTIVE_OPS`. | yes |
| `read_teams_attachment` already SAFE live | `destructive_ops.py` at df724ef284 lists it in `SAFE_TOOLS` (graded MXC5-AC4 PASS, row Z-C-S16) | yes |
| `composed_refused` drops no live tool | every tool of the four live integrations now declares a class on its own spec (ycharts 6, schwab 5, globgrph 2, opal_portal 1); a tool is refused only when it has no spec class AND `data_entitlement.classify` returns None | yes; the 46 = 46 guard still backs it |
| catalog channels unchanged | parsed per commit: 650c9a99cb adds `silver_datasets`, 2c25c4c831 and bc0cde67f0 change `silver_datasets` and `built_at_git_head`; `channels` equal before and after each (15); df724ef284 vs HEAD equal (15 = 15). `catalog_gate.load_catalog` indexes only `channels.*.artifacts` (`catalog_gate.py:57-66`, the loop at `:62`). So OA-g-3's grant and every `opal_asker_query` answer have DELTA = 0. | yes |

## Writers of the named property (NEVER-1): a correction to the CTO half's count

The property that would move served output is `ENABLED_INTEGRATIONS`, read from the environment at `config.py:227-228`
(df724ef284; `:237-238` at HEAD). The CTO half names the host `.env` as the one writer, "which the act does not touch".
The act does touch it: `deploy-to-ec2.sh:196` (df724ef284) rewrites `${REMOTE_DIR}/.env` on every deploy, including the
literal **`ENABLED_INTEGRATIONS=ycharts opal_portal globgrph`**. So the one RULE is that literal, and this act runs it.
The script is unchanged between df724ef284 and HEAD, and none of the 12 commits touches it, so the release writes the
same literal as the live deploy. Neither new integration is in it.

## Both branches

- **Live `.env` holds the literal (the expected state after the 23:16Z OA-g-2 deploy):** DELTA = 0 on every served
  answer; the tool list stays 46 = 46; both new integrations stay dormant.
- **Live `.env` has drifted from the literal** (a hand edit on the host since 23:16Z): the deploy RESETS it, and the
  served tool set changes. The CTO half does not cover this branch, and neither does this half. **Condition:** before the
  upload, read `ENABLED_INTEGRATIONS` from the host `.env` over SSM (a read, no write). If it is not exactly
  `ycharts opal_portal globgrph`, STOP and leave the ledger entry OPEN-BLOCKED. The CTO half's post-act guard
  ("unchanged on the host") would only see the drift after the act.

## Rollback, per key

Code: redeploy `opal-gateway-df724ef284.tar.gz` (ETag f9bd0d48, present in S3), rebuilt first without uploading as
the order's step 4 requires; the 90-second health rollback reads `/health` on the host. Data: none written.
The `.env` is rewritten to the same literal by the rollback deploy.

## Verdict

**SIGNED** for the act above as bounded here, with the pre-upload `.env` read as its one condition. Nothing else is
added: the CTO half's guards (on-host `/health` 200, tool list 46 = 46, the NEVER-2 ledger, off-hours GO, the
announcement) stand as written.

-- 3.0.0_SA_CVO~O
