# AE 0.7.0 Session Log -- 2026-05-20 -- MDPF closeout: .021 IAM fix + .018 verification

**Agent:** 0.7.0_AE_CloudOps
**Trigger:** Andrew boot ("0.7.0_AE_CloudOps")
**Status:** IN PROGRESS -- resuming 5/19 MDPF mid-flight closeout.

---

## TL;DR

Fresh session. 5/19 work (smartx-v1.0.1, MDPF_ASSETS.018 P1, .021 SSM doc) was
committed/applied but never closed -- no 5/19 log, TOs at `pending`. Reconstructed
5/19 ground truth from git + AWS (see `logs/2026-05-19/session_reconstructed_*`,
written this session at COO~B's request). Found + fixed the open .021 defect
(SSM-doc invocation AccessDenied'd on opal-data-inf); shipped mdpf-pipeline-v1.0.1.
Surfaced a .018 Phase-2 stale-premise issue to COO~B for adjudication. Verifying
on today's 15:00Z chain fire.

## 1. Startup

register_agent (PID 19388) + inbox-watch (PATH wrapper, tracked) + comp-context.
check_inbox + get_agent_status: GO for TRSB_LEDGER.009 (COO~B) -- ACK'd, queued
behind the MDPF closeout. 5 pending TOs from the 5/19 dispatch (.018/.021/
SXIN_PRODCT.001/ADHC_DSFLOW.007/ADVI_INFALM.001) + TRSB_LEDGER.009.

git fetch origin CLOUD: local==origin. UTC 14:22Z. Reconstructed that I had
shipped substantial 5/19 work with no log -- the stuck-mid-closeout failure mode.

## 2. MDPF_ASSETS.021 -- root-caused + fixed the SSM-doc failure

All 4 5/19 SSM-doc invocations failed (exit 1). Pulled the run log:
`build_legacy_compat_emit.py:list_inf_dates()` line 150 paginates
`opal-data-inf/gold/eclipse/` -> `AccessDenied` on `s3:ListBucket` -- the
`mdpf-daily-runner-ec2-role` had NO `opal-data-inf` statement. The 5/19
`3d99f1dd1` IAM fix had closed a different gap (`json/portfolios/*`), not this one.

Fix: two prefix-scoped statements in `mdpf-pipeline/iam.tf` --
`InfEclipseReadLegacyEmit` (`s3:GetObject` on `gold/eclipse/*` + `silver/eclipse/*`)
and `InfEclipseListScoped` (`s3:ListBucket` on `opal-data-inf` with `s3:prefix`
condition). Mirrors the existing `BdReadWSD2WSE`/`BdListScoped` least-privilege
pattern; no bucket-wide grant. Added `inf_bucket` local to `main.tf`.

The same grant also covers the WS-C feeder, which (post .018 Phase 1) runs in
chain Stage 1 and reads the identical `opal-data-inf` eclipse prefixes -- without
this, today's 15:00Z chain WS-C step would have AccessDenied'd.

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source | `9944deb75` fix(mdpf-pipeline): runner role opal-data-inf eclipse read |
| 2 | terraform plan | 0 add / 1 change / 0 destroy (aws_iam_role_policy.mdpf_runner in-place) |
| 3 | terraform apply | 0 added / 1 changed / 0 destroyed |
| 4 | 0-diff plan | No changes. Infrastructure matches the configuration. |
| 5 | Tag + push | `mdpf-pipeline-v1.0.1`; pushed CLOUD + --follow-tags |
| 6 | record-terraform-deploy | FAILED -- known git-cwd issue (cloud-ops skill notes it); no source-map drift produced; surfaced here per protocol |

## 3. MDPF_ASSETS.018 -- Phase-2 premise issue surfaced to COO~B

Phase 1 (WS-C feeder into chain Stage 1) committed `cd8500aad` 5/19 + S3-deployed.
Phase 2 directs a cron shift 11:02Z->11:30Z, but `aws events list-rules` shows the
only mdpf rule is `mdpf-daily-refresh-trigger @ cron(0 15 ? * MON-FRI *)` (15:00 UTC
-- the schedule I codified 5/18 in mdpf-pipeline-v1.0.0). No 11:02Z cron exists.
Phase 1 already removes the WS-C race structurally; a cron shift adds nothing.
Re-routed to COO~B (MDPF = ~B lane) -- recommended closing .018 on Phase 1 +
15:00Z natural-fire verification, Phase 2/AC3 marked N/A. Awaiting concurrence.

## Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| comp-iam (manual review) | runner IAM addition | Two new statements are prefix-scoped (`gold/eclipse/*`, `silver/eclipse/*`), `s3:prefix`-conditioned on ListBucket -- no bucket-wide `*`. Consistent with the module's CTO-ratified least-privilege discipline. comp-iam service not run as a graph tool (mdpf-pipeline runner role is not a comp-graph node; consistent with prior-session finding that mdpf-pipeline infra is outside the comp-graph). |

## Current State

| Item | Status |
|------|--------|
| 5/19 log of record | WRITTEN (logs/2026-05-19/session_reconstructed_*) |
| MDPF_ASSETS.021 IAM fix | SHIPPED -- mdpf-pipeline-v1.0.1 / 9944deb75; SSM-doc invocation verification PENDING |
| MDPF_ASSETS.018 | Phase 1 done+deployed; Phase-2 premise w/ COO~B; verification PENDING (15:00Z fire) |
| TRSB_LEDGER.009 | GO received; queued |

## Next Steps

1. Monitor today's 15:00Z mdpf chain fire -- verify .018 Phase 1 (WS-C in Stage 1
   populates Inflection partition; Cohort 0 ~$91M) + the IAM fix's WS-C path.
2. Verify .021 SSM-doc invocation now succeeds (post-IAM-fix); telemetry artifact.
3. RAVC2 .021 + .018 (latter pending COO~B Phase-2 call).
4. Then SXIN_PRODCT.001 -> ADHC_DSFLOW.007 -> ADVI_INFALM.001 -> TRSB_LEDGER.009.
