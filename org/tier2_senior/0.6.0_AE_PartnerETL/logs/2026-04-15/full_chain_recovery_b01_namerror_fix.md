# Session Log — Full A→D rerun, B_01 NameError patch + recovery, CF invalidation

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-15
**Result:** Full A→D rerun closed CHAIN-COMPLETE 19:35:06 UTC. AE-owned B_01 patch under Andrew GO override. RF01 + D_04 distribution + C_08 spot-checks all PASS. CF EVTSA9VEHNZVH invalidated.

---

## Phase Overview

| Phase | Action | Outcome |
|---|---|---|
| 1 | Startup, MCP register, inbox catchup | COO GO on full A→D acked; tactical 3-bond audit confirmed absent from PROD |
| 2 | Group D dry-fire (D_02 + D_04) on QA runner | RF01 spot-check PASS; signaled COO+CTO+Andrew |
| 3 | Full A→D fire on QA i-0090b823a4a0997e3 | Launcher SSM `disown` failure -> nohup process detached BEFORE failure detected; refire created duplicate chain |
| 4 | Detect + kill duplicate chain (PIDs 9282/9289/9320) | Only 17:27 chain remained; no S3 race |
| 5 | Group A clean (S_00 + A_00..A_04, 12m22s) | A_03 dominant at 565s |
| 6 | B_01 NameError `cusip_to_name` at 17:43 UTC | Chain died; QA auto-stopped |
| 7 | Diagnose: scoping bug in DS-base freeze-window commit (8eda12a3) | `cusip_to_name` defined in `_build_rps_context` but absent from returned ctx dict; referenced in `_build_rps_synthetic_lots` line 666 |
| 8 | Andrew GO-NOW: AE owns the patch | 2-line surgical fix; py_compile OK; commit 17e75359 |
| 9 | Push CLOUD + upload to S3 | etag `43a8f0d85d9d4026532115f71dd923f7` |
| 10 | EC2 capacity bounce (~4 min) | Restart succeeded; SSM online 18:05:58 UTC |
| 11 | Partial chain B_01→D_04 fire | 18:07:36 UTC; helper script `_partial_chain_b01.sh` wraps `gold_dispatch.sh --single $id` per script with fail-fast |
| 12 | Chain ran B_01..D_04 sequentially | Closed 19:35:06 UTC; auto-shutdown |
| 13 | Spot-checks: RF01 nna_max, D_04 distribution, C_08 fee_eff | All PASS |
| 14 | CF invalidation EVTSA9VEHNZVH `/*` | ID IEU8CK2CTAR6YLN1J6JI26UB3H |
| 15 | gold_dispatch.sh flag audit (Andrew request) | 8 real bugs + 6 logic traps; COO staged `gold-dispatcher-hygiene-cleanup` TO HARD-GATED on chain close |

---

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| 7 | grep + Read on B_01 source | locate `cusip_to_name` definition + reference | bug confirmed at line 666 (in `_build_rps_synthetic_lots`); cusip_to_name local to `_build_rps_context` (line 484) and missing from return dict (line 537-547) |
| 8 | py_compile | `python -m py_compile B_01.holdings_lots.py` | PY_COMPILE_OK |
| 9 | aws s3api head-object | etag verify post-upload | `43a8f0d85d9d4026532115f71dd923f7` matched runner-side md5 |
| 11 | aws s3 sync (runner) | sync code/gold/ to /tmp/gold_layer_scripts/ | 53 scripts; B_01 md5 confirmed |
| 13 | python json inspector (local) | structural spot-checks on platinum/advisors/* + firm/* | All gates PASS |

WP-3 pre-flight `comp-pipescript io silver/transactions` not applicable (silver layer; tool only accepts gold IDs); `comp-iam service bd-transactions-trigger` returns "lambda not registered in IAM corpus" (corpus only knows EC2 `bd-gold-runner`); `comp-blast silver/transactions` deferred to WP-3 execution slot.

---

## Commits

| Commit | Author | Subject |
|---|---|---|
| `17e75359` | 0.6.0_AE_PartnerETL | fix(B_01): thread cusip_to_name through rps_context dict (unblock full chain) |

Rule deviation: AE owned a gold-script fix normally owned by 0.4.0_DS_ClientPlatform (per `feedback_ds_commits_ae_deploys.md`). Per Andrew explicit GO 2026-04-15 ("just fix it") under rerun-deadline pressure. COO ACK + logged as narrow exception.

---

## AWS State

| Resource | Action | State |
|---|---|---|
| EC2 i-0090b823a4a0997e3 (bd-gold-qa-runner) | start (capacity-retry) -> chain run -> auto-shutdown | stopped post-CHAIN-COMPLETE |
| S3 `s3://opal-data-bd/code/gold/B_01.holdings_lots.py` | upload | etag `43a8f0d85d9d4026532115f71dd923f7` |
| S3 `s3://opal-data-bd/code/gold/_partial_chain_b01.sh` | upload (one-off helper) | live |
| S3 `s3://opal-data-bd/gold/logs/partial_b01_20260415_180736.log` | uploaded by helper | 1.46 MB |
| S3 `s3://opal-data-bd/gold/logs/chain_full_20260415_172741.log` | uploaded by gold_dispatch (failed chain) | 19 KB (B_01 traceback) |
| S3 `s3://opal-data-bd/platinum/**` | refreshed by D_*, 20,493 files | live |
| CloudFront EVTSA9VEHNZVH (opalinvest.dev) | invalidate `/*` | InProgress, ID IEU8CK2CTAR6YLN1J6JI26UB3H |

---

## Wall Times

| | wall |
|---|---|
| S_00 + Group A (17:27 chain) | 12m22s |
| Group B (B_01 22m42s, B_01b 3s, B_00 4m45s, B_02 2m40s, B_03 2m13s) | 32m23s |
| Group C (C_00..C_08, C_06 6m44s) | 16m32s |
| Group D (D_00 29s, D_00b 3m35s, D_00c 54s, D_01 3m42s, D_02 22m, D_03 ~0s, D_04 7m51s) | 38m35s |
| Partial chain wall (B_01->D_04) | 1h 27m 30s |
| End-to-end incl. recovery (17:27 fire -> 19:35 close) | ~2h 7m |

---

## Spot-check Evidence

**Firm headline (gold/artifacts/summary/* + dashboard):**
- generated_at: 2026-04-15T19:27:15Z
- data_as_of: 2026-04-13 (silver/allocations watermark)
- total_aua: $1,633,503,725.44
- 2,814 clients / 5,960 accounts / 378 advisor books

**RF01 nna_max gate** (`book.rfs.decomposition_max.nna == book.rfs.nna_max`, ±$0.01):

| Advisor | total_aua | nna_max | decomp.nna | gate |
|---|---|---|---|---|
| alex_bright | $239,584,927 | $604,199.36 | $604,199.36 | $0.00 PASS |
| collin_plotts | $164,972,176 | $3,288,762.02 | $3,288,762.02 | $0.00 PASS |
| kyle_sims | $297,701,075 | $2,457,322.57 | $2,457,322.57 | $0.00 PASS |

**D_04 distribution.total tie-out** (`distribution.total.total == book.total_aua`):

| Advisor | book.total_aua | distribution.total.total | match |
|---|---|---|---|
| alex_bright | $239,584,927 | $239,584,927.20 | PASS (cent rounding) |
| collin_plotts | $164,972,176 | $164,972,175.57 | PASS (cent rounding) |

**C_08 advisor_fee_efficiency.json**: schema healthy (advisors / as_of_date / regression / windows), 526,936 bytes. Cross-check against advisor summary book totals deferred to ~C.

---

## Incidents / Lessons

- **`disown` not in sh:** First full-chain SSM launcher used `nohup ... & disown` but SSM script.sh runs in dash. nohup detached the chain BEFORE disown failed, so the chain went live but the launcher reported "Failed". Refire created a duplicate chain. Detected via ps before A_03 race; killed cleanly. Future helper scripts: prefer `bash -c "nohup ... &"` or just `nohup ... &` without disown.
- **Shell expansion bug in inline SSM heredoc:** First refire helper used `for id in $IDS; do bash gold_dispatch.sh --single $id ...` inside a `bash -c "..."` — outer double-quotes expanded `$id` and `$(date)` at parent level. `--single` got empty string. Fix: write a proper helper script, upload to S3, invoke it from SSM. Done at phase 11 with `_partial_chain_b01.sh`.
- **D_02 + D_04 longer than historical:** D_02 ~22m (vs 4-7 historical), D_04 ~7m51s (vs 3-7 historical). RSS climbed 14 GB on D_02 during 5b relationship timeseries. No failures; output structurally clean. Worth flagging to ~A as a perf regression candidate.
- **gold_dispatch.sh flag audit surfaced 8 real bugs + 6 logic traps.** COO authored `gold-dispatcher-hygiene-cleanup.md` TO, HARD-GATED on chain close. Will flip pending + execute post-validator settle. Andrew picks: `--incremental` restricted to `--single A_00|C_06` only (option a, tighten first, expand as follow-up).

---

## Open / Followups

- **WP-3 (BDPL_CNPRCS) CUSIP backfill:** staged TO; pre-flight compiler runs documented (with `silver/transactions` mismatch caveat). Flip pending + execute post-W7 verification tonight.
- **W7 (BDPL_ASTDIM):** verify natural EventBridge fire of `bd-asset-dim-trigger` at 22:00 UTC tonight. If clean: forwardfill_v2/assets/ has 2026-04-15 xlsx, silver/assets/2026-04-15.parquet present, CW + S3 logs clean. Then MCP COMPLETE -> COO; closes W1.
- **WP-10b:** wire `diag_gold_silver_recon.py` (cff234b5) into nightly post-gold_dispatch + CloudWatch JSON ingest + FAIL alert. 3 clean nights = acceptance.
- **gold-dispatcher-hygiene-cleanup TO:** flip pending after validator settle; execute then commit.
- **CF E2LPCXXBLDGWXY (no-alias portal-v2):** Andrew didn't request invalidation; staging/internal use only. Skipped.
- **C_08 deep validation:** ~C owns the cross-check between fee_eff.advisors[*].book_aua and platinum/advisors/{name}/summary.json:book.total_aua. Surfaced to COO in evidence message.

---

## Next Steps

- **[0.6.0_AE]** Tonight 22:10 UTC: W7 verification + MCP COMPLETE to COO (closes W1).
- **[0.6.0_AE]** Post-W7: flip WP-3 to pending; execute CUSIP backfill into silver/transactions.
- **[0.6.0_AE]** Post-validator settle: flip gold-dispatcher-hygiene-cleanup TO pending; execute.
- **[0.4.0_DS_*]** Resume validators on CN-P1 + RA-P1 + DS-A distribution + DS-C B9 + B1-rerun closeout per COO's standing post-chain loop.
