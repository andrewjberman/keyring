# Deploy-completion ledger — ETFS reporter renderer (canonical averaging + CSV grids)

**Opened:** 2026-07-07T15:25Z | **Closed:** 2026-07-07T15:27Z (single-leg, same session)
**Agent:** 3.0.0_SA_CVO (Andrew-direct in-session; renderer is 0.4.0_DE lane — DE notified via MCP)
**Change:** `data/etfs/scripts/presentation/render_month_end.py` — commit `5b9c6d46e` (CLOUD, pushed)

## Legs (all closed)

1. **Code committed + pushed:** `5b9c6d46e` — `_month_cap` + `_carried_daily` (complete-month cap fix + month-boundary seed) + `write_month_csvs` (per-firm `opaletfs_{firm}_{YYYYMM}.csv`, Date row + DIVZ/IDVZ/PFDE/PFOE rows, carried values) wired into `main()` incl. `--s3-out` upload. ds-commit-gate PASS.
2. **Artifact deployed:** `aws s3 cp` → `s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py`. Pre-overwrite check: prior S3 ETag `3b81440a8c66b2e8b911c4a91899fab8` == pre-edit git HEAD md5 (byte-identical — no foreign deploy clobbered). Post-deploy verify: S3 ETag `d618e3b9931bde32c2d672363f8587ff` == committed local md5, 36,767 bytes both sides.
3. **Consumer unchanged by design:** the `etfs-reports-orchestrator` Lambda pulls this artifact fresh via SSM on every run (`_render_command`); no Lambda code/TF change needed. Lambda env confirmed live (`REPORTS_ARTIFACT_PREFIX` matches the deployed key).
4. **Exercised (F5):** the changed code path itself rendered Apr/May/Jun decks + 9 CSVs against the CVO-verified daily series — all marquis figures match the triple-checked blessed numbers; 36/36 CSV row-mean == deck-average asserts PASS.

## Residual (not stranded — routed)

- Production `daily/{partner}/` slices + `monthly/*.json` for Apr–Jun remain unbackfilled (DS lane, flagged in the Andrew report; renderer self-heals for July+ on the normal 1st-of-month run).
- SES email attaches PDF only; attaching CSVs would need an orchestrator Lambda change (TF cycle) — optional follow-up, not part of this deploy.

**Status:** CLOSED — no half-landed legs (4/4 legs closed, exercised F5). Format-corrected by 2.0.0_SA_COO 2026-07-07T15:31Z so the deploy-ledger gate parser recognizes this as terminal — content unchanged, this was a marker-format gap, not an actual half-landed deploy.
