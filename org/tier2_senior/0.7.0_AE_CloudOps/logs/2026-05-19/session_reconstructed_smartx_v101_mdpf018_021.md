# AE 0.7.0 Session Log -- 2026-05-19 -- smartx-pipeline-v1.0.1 + MDPF_ASSETS.018 P1 + .021 SSM doc

**Agent:** 0.7.0_AE_CloudOps
**Status:** RECONSTRUCTED 2026-05-20 from git + AWS ground truth. The 2026-05-19
session(s) ended mid-closeout without writing a contemporaneous log -- this log
of record is rebuilt on 2026-05-20 from commit history, tag annotations, S3
telemetry, and live AWS state, at COO~B's request as part of the MDPF closeout.
It is evidence-faithful but not a contemporaneous narrative; where 5/19 intent
is not recoverable from artifacts it is marked as such.

---

## TL;DR

2026-05-19 was the CEO-direct MDPF methodology-pivot day (broader-1b + Cohort-0-IN
+ 2b-OUT; DS Base 225df40bc). AE 0.7.0 shipped three coordinated infra changes off
that pivot, plus a separate news-pipeline lane. The MDPF/smartx work was committed
and (for smartx + .021 TF) applied, but .018 and .021 were left at TO status
`pending` -- not RAVC2'd, not closed, no session log. The 2026-05-20 session
reconstructs and completes the closeout.

## 1. smartx-pipeline-v1.0.1 -- Opt-A neutralize non_model_append (COMPLETE 5/19)

CEO-direct methodology pivot: DS Base's `build_legacy_compat_emit.py` (225df40bc)
becomes sole source-of-truth for `non_model_assets.json`; the smartx-ingestion
`append_non_model_today` step is neutralized to a no-op early-return.

| Step | Evidence |
|------|----------|
| Source edit | `de03b497a` 09:11 (append_non_model_today -> Schwab-confirmed), then `0aa31c41c` 13:06 (v1.0.1 NEUTRALIZE step) |
| record-deploy | `52a62406a` 13:09 (recommitted with agent author) |
| Tag | `smartx-pipeline-v1.0.1` -> `52a62406a` |
| Apply | 0 add / 1 change / 0 destroy; 0-diff verified (per tag annotation) |
| Live verify | CodeSha256 `a2EM0JyzUXxQkRKnsQ6LePJS1B0b5lUkZQI9CJU1vLo=` match; smoke -- non_model_assets.json sha256 IDENTICAL pre/post-invoke, appended=false, no Lambda write |

Status: COMPLETE + tagged 5/19. Dead-Lambda cleanup (the now-no-op step) is the
follow-on SXIN_PRODCT.001 Phase 2.

## 2. MDPF_ASSETS.018 Phase 1 -- WS-C feeder into chain Stage 1 (COMMITTED 5/19)

Commit `cd8500aad` 14:30 -- `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh`:
WS-C Inflection feeder (`gold/build_mdpf_wsc_inflection_feeder.py`) added to Stage 1
parallel alongside WS-B/WS-D.1/WS-D.2. Stage-1 failure of any feeder -> chain FAIL
LOUD (no partial emit). This is the CTO-ratified Option-A fix for the 5/19 Cohort 0
race ($17.80M understated when the chain read an empty Inflection partition).

Deployed to S3 5/19 14:30:17-14:30:20: `code/mdpf-daily-dispatch.sh` (8255 B) +
`code/scripts/gold/build_mdpf_wsc_inflection_feeder.py` (23417 B).

Status 5/19: Phase 1 committed + S3-deployed. Phases 2-5 not done; TO left
`pending`. (See 2026-05-20 log: Phase 2 found to be a stale premise.)

## 3. MDPF_ASSETS.021 -- legacy-emit-on-demand SSM RunDocument (PARTIAL 5/19)

Interim daily-fire bridge for `build_legacy_compat_emit.py` until SXIN_PRODCT.001
productionizes the schedule.

| Step | Evidence |
|------|----------|
| TF authored | `316a5681f` 14:34 -- `legacy-emit-ssm.tf` (SSM doc `mdpf-legacy-emit-on-demand` + standalone `MDPFLegacyEmitInvoker` policy) |
| Fix 1 | `d57a80d1f` 14:39 -- SSM doc: drop `--date` arg (script CLI is `--upload`/`--dry-run` only) |
| Fix 2 | `3d99f1dd1` 14:42 -- runner IAM: add `json/portfolios/*` RW + ListBucket prefix (AC1 dry-run surfaced gap) |
| Apply | legacy-emit-ssm.tf applied 5/19 -- SSM doc + policy live in AWS (confirmed 5/20: `terraform plan` 0-diff, doc Active DocVersion 2) |
| AC1 invocations | 4 SSM-doc invocations 5/19 18:37-18:45Z -- **ALL FAILED** (exit 1) |

**Open defect at 5/19 session end:** all 4 invocations failed. Root cause (diagnosed
2026-05-20): `mdpf-daily-runner-ec2-role` had no `opal-data-inf` statement;
`build_legacy_compat_emit.py:list_inf_dates()` paginates `opal-data-inf/gold/eclipse/`
-> AccessDenied on `s3:ListBucket`. The 5/19 `3d99f1dd1` IAM fix addressed the
`json/portfolios/*` gap (a real, different gap) but not the `opal-data-inf` one.
Fixed 2026-05-20 -- see that session's log (mdpf-pipeline-v1.0.1 / `9944deb75`).

Status 5/19: TF applied, SSM doc live, but invocation non-functional. TO left
`pending`.

## 4. news-pipeline -- separate same-day lane (FYI)

Same day, separate lane: news-v2.9.8 / v2.9.9 / v2.9.10 (ADHC_CRYPCT.001 crypto
rip-out + backfill_from_layer2 crypto-bypass hotfix) -- commits `60ff5d267`/
`4beb59a4a`, `815791d85`/`f26252a23`, `1c9072cef`/`b13c88b2e`. Each has an
upload-artifacts + record-deploy commit pair. Not part of the MDPF closeout;
noted here only for 5/19 completeness. If that lane also lacks a session log,
that is a separate audit-trail item.

## Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| comp-* | reconstruction only | N/A this reconstructed log -- 5/19 comp-tool runs (if any) are not recoverable from artifacts. The 2026-05-20 closeout session runs the applicable comp checks (comp-iam scope review on the runner IAM addition). |

## Current State (as of 5/19 session end -- reconstructed)

| Item | 5/19 end state |
|------|----------------|
| smartx-pipeline-v1.0.1 | COMPLETE + tagged |
| MDPF_ASSETS.018 | Phase 1 committed + S3-deployed; TO `pending` |
| MDPF_ASSETS.021 | TF applied, SSM doc live but invocation FAILING (opal-data-inf IAM gap); TO `pending` |
| news-v2.9.8/9/10 | deployed + record-deploy committed (separate lane) |

## Next Steps (carried into 2026-05-20)

1. Diagnose + fix the .021 SSM-doc invocation failure.
2. Verify .018 Phase 1 + resolve the Phase-2 cron premise.
3. RAVC2 + close .018 and .021; tag mdpf-pipeline closeout.
4. Write this log of record (done 5/20).
