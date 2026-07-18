# 0.6.2_AE_PartnerETL -- session close: CELL-4 grounded + box grant-strip APPLIED+verified+CLOSED; BD_API_DESIGN doc; the 01_raw writer/reader grounded

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, TRACE, DIAGNOSE, SCRIBE, COORDINATE
**Date:** 2026-07-18 | **Window:** ~00:32Z -> ~03:47Z (since log `bb5ca6cb6`) | **Serial:** 0.6.2_AE_PartnerETL

## Summary

Continuation of the WP8-DECOM Schwab-Box thread. Grounded the CELL-4 dependency footprint, produced + executed the box IAM grant-strip (Andrew + CTO approved), and documented the BD API mechanism -- all landed + gate-accepted.

- **CELL-4 Part-2 box grant-strip: APPLIED + Rule-22a verified + CTO-CLOSED.** Stripped the Schwab box's vestigial `opal-data-schwab` write grants; the box now has ZERO write to the dying bucket and keeps every live capability. `safe-apply` 0/1/1 + 0-diff; two SEPARATE simulates land as required.
- **01_raw writer/reader GROUNDED (Andrew-direct).** The `01_raw` writer is `sync_schwab_onedrive_to_s3.py` (OFF-box, 0.5.0's L5b), NOT the Schwab box. Surfaced a **live `01_raw` READER, `canonical-schwab-runner`,** that the bucket-delete would orphan -- 0.5.0 censused it as a hard bucket-delete prereq.
- **BD_API_DESIGN.md authored + committed** (Andrew-direct, source-grounded high-def DoR).
- **Corrected a framing error of my own** to Andrew (conflated 0.5.0's two deletes).
- **49F runner refactor PARKED** for a dedicated session (Andrew-direct: too big for offhand; existing work exists).

## Deployment Sequence + Verification (AE) -- CELL-4 Part-2 iam-strip

Files: `infra/aws/terraform/canonical-schwab-ec2/iam.tf` (staged `5c3508f76`). Removed SchwabRawList/Write + SchwabBronzeList/Write from `quartz-si2-spike-inline`; destroyed the `quartz-si2-backfill-08335338` policy. `SchwabOpsCodeRead` HELD for D5 (CTO option-b).

```
safe-apply: Apply complete. Resources: 0 added, 1 changed, 1 destroyed.
re-plan:    No changes. Your infrastructure matches the configuration.   (applied==desired, 0-diff)
simulate (i)  box PutObject on opal-data-schwab/08242234/bronze/rps/...RPS.zip  -> implicitDeny  (ZERO schwab write)
simulate (ii) box PutObject on opal-data-assets/schwab/08242234/bronze/...RPS.zip -> allowed     (monolith write intact)
belt          box GetObject on opal-data-assets/code/canonical-schwab-si2/sdd-daily-pull.ps1 -> allowed (code-read intact)
```
Tag: none (IAM-only, no pipeline version). 0-diff confirmed YES. Deploy-completion ledger `20260718T0331Z_schwab-box-cell4-iam-strip` CLOSED (5 legs). CTO ACCEPTED+CLOSED 034322Z.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| `comp-grep` (x4) | 01_raw writer/reader grounding; BD kimi/OTP/lambda locate | PASS -- writer=sync_schwab_onedrive_to_s3.py, reader=canonical-schwab-runner; BD gateway adapter located |
| raw `aws iam get-role-policy` + `simulate-principal-policy` (x4, rail-checked) | box footprint + Rule-22a (applied + exercised) | PASS -- 7 opal-data-schwab grants enumerated; post-strip implicitDeny + retained allowed |
| `.tools/terraform.exe plan` (x2) | removals-only verify + post-apply 0-diff | PASS -- 0-add/1-change/1-destroy; then No changes |
| raw `aws ssm send-command` (x3) | on-box audit (tasks, sync-to-s3.ps1 dest, 01_raw writer) + earlier exercises | PASS -- box writes only 01_raw_quartz_validation/, NOT 01_raw/ |
| raw `aws s3 ls` (recency) | 01_raw cadence (live vs vestigial) | PASS -- 01_raw last write 07-16, deprecating |
| `.tools/deploy_ledger.py` | CELL-4 iam-strip deploy ledger | PASS -- CLOSED, 5 legs proven |

**What worked:** applied+exercised 22a on the live primitive (not comp-iam); the removals-only plan + isolated positive control caught nothing wrong because nothing was; on-box SSM disproved my own imprecise "box writes 01_raw" flag. **What failed/caught:** my own two-deletes conflation to Andrew (0.5.0's monolith-copy-delete vs the future bucket-delete) -- self-corrected. Two transient `.git/index.lock` contentions under fabric load -- diagnosed (orphan, not live), waited/retried, never forced. **Gap:** none new.

## Blockers

None self-owned. Remaining CELL-4 work is correctly sequenced behind external gates (D5 cutover-cycles; Part-1 via 0.7.0; bucket-delete on the canonical-schwab-runner repoint / Group-D refactor).

## Current State (ZERO prior context -- handoff surface)

- **CELL-4 Part-2 DONE + CLOSED:** Schwab box `i-0f3d57a97f14727af` role `quartz-si2-spike-role` has ZERO `opal-data-schwab` write (SchwabRaw/Bronze/Backfill grants removed, applied `77f073eff` chain). Keeps monolith write, monolith code-read (SchwabOpsCodeReadMonolith), SDD credential, KMS, firm-sep Denies. `SchwabOpsCodeRead` (old code fallback) HELD for D5 (strip after the cutover clears 2 clean scheduled cycles, next 07-18 AM).
- **HELD/sequenced (not mine to force):** (1) D5 SchwabOpsCodeRead strip + old `_ops` object delete (task #6, Andrew destructive-go). (2) Part-1 dead-GUI-channel retire (download-schedule rule + SchwabAutoDownload/SchwabS3Sync) -- coordinate 0.7.0 (they own the L7 alarm teardown). (3) opal-data-schwab BUCKET delete -- 0.5.0-owned, GATED on the `canonical-schwab-runner` `01_raw` reader repoint (resolves via the 49F->Group-D refactor).
- **49F runner refactor:** PARKED for a dedicated session (Andrew-direct). Existing work at `infra/aws/ec2/canonical-schwab-runner/` (run-canonical.sh, s8_gate.py) + "substantial work somewhere" to gather.
- **Docs committed:** `data/assets/docs/SCHWAB_BOX_ARCHETYPE.md` (`358296670`), `data/assets/docs/BD_API_DESIGN.md` (`533e35f79`).
- **Schwab Box daily REST pull unaffected throughout** -- the box STAYS; only its dying-bucket deps were severed.

## Next Steps

- **[0.6.2 self]** hold: on the 07-18 AM cutover cycles clearing, the D5 SchwabOpsCodeRead strip is unblocked (fold into a removals-only plan, CTO gate). Coordinate Part-1 with 0.7.0 when they reach L7-schwab. The 49F runner = dedicated session when Andrew/CTO spawn it.
- **[0.5.0_AE_OpalETL]** the canonical-schwab-runner repoint (Group-D) is the bucket-delete gate; the in-flight monolith redundant-copy delete (clears the 0824 guard FATAL) is separate + awaiting Andrew re-confirm.
- **[0.7.0_AE_CloudOps]** Part-1 dead-GUI-channel retire when at L7-schwab; box + REST rules off-limits.
- **[1.0.0_SA_CTO]** CELL-4 Part-2 CLOSED; D5 strip after cycles at his gate.

## MCP traffic

~14 in / ~11 out. Significant: **Andrew-direct** (commit-now, ground-the-01_raw-writer, nudge-0.5.0, what-grants, "those changes are fine", 49F-runner-to-dedicated-session). CTO (CELL-4 design-approve -> apply-GO -> ACCEPTED+CLOSED; SchwabOpsCodeRead HOLD-for-D5 ruling). 0.5.0 (reader censused as hard bucket-delete prereq; two-deletes clarification; Group-D refactor context). All RAVC loops CLOSED; nothing pending an ACK from me.
