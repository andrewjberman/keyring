# 0.6.2_AE_PartnerETL — work log 2026-06-29 (Quartz/SI2 spike, Andrew-live)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, DEPLOY, COORDINATE

## Session: SCHWAB_SSOT.DERISK-1 — stand up SI2 Desktop on an EC2 Windows box + prove an unattended Schwab pull lands in S3 (Path A de-risk). COMPLETE + RAVC-ACCEPTED.

### Context
CTO's Schwab-SSOT migration de-risk #1 (COO-assigned). Path A = lift-and-shift SI2 Desktop (ClickOnce) onto an EC2 Windows box, one-time interactive enroll, then unattended AllNewFiles -> S3. Done live with Andrew at the keyboard for the one human step (enrollment). Prereq: read SCHWAB_SDD_DELIVERY_BRIEF.md (UA-authored) + consult UA 0.0.1.

### Provisioning (autonomous, my lane)
- EC2 i-0f3d57a97f14727af: Win Server 2022 Full Base (ami-0ab5e8edee718de14), t3.large, public IP 3.89.31.201. IAM role quartz-si2-spike-role (s3 PutObject scoped to opal-data-schwab/01_raw_quartz_validation/* + AES256, SM read schwab/*, SSM). SG sg-04ce8e1d981858f32 (RDP scoped to Andrew's IP only). Key pair for admin-pw decrypt.
- Per UA blueprint: WebView2 v149 installed (silent), auto-logon console session (in-process Quartz needs a live desktop), IE-ESC disabled. Schwab SDD creds stored schwab/sdd-credentials (Andrew-provided; acct 08242234).

### Enrollment (Andrew, one-time interactive via RDP)
- SI2 install: dfshim ClickOnce launch of https://si2.schwabinstitutional.com/sdd/Schwab.SI.SI2Desktop.Container.application (UA-confirmed URL; Edge 404'd on raw nav, dfshim/rundll32 worked -> dropped a desktop .bat since RDP paste was broken). Error 1923 "SDD Schedule Service" = ClickOnce-sandbox can't register a system service -> UA confirmed SKIPPABLE (in-process Quartz), Andrew clicked Ignore.
- Login + account-level MFA (6-digit TOTP, no QR/per-device seed). Device enrolled. DURABILITY PROVEN: close+reopen SI2 -> no re-login (steady-state OTP-free).
- June AllNewFiles -> 13 files / 720MB (CRS20260626.*) -> SSM `aws s3 sync` -> S3-VERIFIED in opal-data-schwab/01_raw_quartz_validation/ (segregated; AC#1 MILESTONE).

### Unattended pipeline (built, since no CLI/scheduler-service available)
UA static-confirmed: Container.exe is GUI-ONLY (zero argv parsing in any assembly) + the scheduler service isn't in the ClickOnce package (needs Schwab enterprise MSI). So unattended REQUIRES UI-automation. Built 3 scheduled tasks:
- **SchwabAutoDownload** (daily 12/16/20Z, Administrator-interactive): UIAutomation finds + clicks the 'Download all new files' Pane (SI2 renders controls as Panes not Buttons -> match by Name, click by clickable-point) + patient dismiss of the resulting 'OK' Pane popup. No-files flow TESTED (Andrew watched: click -> "no new files" -> OK auto-dismissed).
- **SchwabS3Sync** (30min, SYSTEM): aws s3 sync ...\08242234\ -> S3 (AES256). Verified rc=0.
- **SchwabKeepConsole** (5min, SYSTEM): tscon-to-console if Administrator session disconnected (UIAutomation needs an active desktop; can't run from session-0/SSM).
Box PERSISTENT (Andrew-direct) = effectively the working Schwab runtime.

### 5 PRD findings (AC#2)
1. MFA account-level (no per-device seed) -> re-enroll is Andrew-attended. 2. Error 1923/ClickOnce sandbox -> service uninstallable + GUI scheduler won't arm. 3. NO CLI trigger -> UI-automation structurally required. 4. CORRECTION: production box is MANUAL (no auto-schedule) -> built net-new capability. 5. In-process-Quartz session model -> SI2 must stay running in active console session.

### Acceptance
AC#1 (pull->S3) MET. AC#2 (findings) MET. AC#3 (reversibility) -- box reversible but Andrew opted persistence. AC#4 (RAVC COO+CTO) DONE -> COO RAVC-ACCEPT 183610Z. Path-C recommendation: Schwab enterprise-MSI ask (clean long-term) vs the UI-automation interim. COO-flagged cutover seam: validation-prefix vs build_canonical_daily.py 01_raw/ (held for Andrew).

## Compiler Tools
| Tool | Why | Result |
|---|---|---|
| (none applicable) | This was a net-new Windows-EC2 + interactive-GUI spike -- no gold script / pipeline-graph / IAM-TF surface that comp-* models. The estate's comp-tools cover the data pipelines (bd/inf/cot) + the graph/IAM/routes/freshness surfaces, none of which this Schwab-SI2-on-EC2 build touches. IAM was net-new CLI-created (not TF-modeled), so comp-iam (TF-DESIRED) had nothing to read; the milestone was ground-truthed directly on the S3 objects (NEVER#7) rather than comp-freshness (no Schwab coverage). |

**What worked:** UA's static-analysis grounding (install URL, no-CLI, service-not-required) prevented multiple dead-ends; grounding the milestone on the served S3 objects (not the box sync rc). **Gap:** none comp-tool-shaped; flagged that comp-freshness has no Schwab coverage (consistent with the 06-26 cot gap).

## Blockers
None. Follow-ups (not blockers): monitor first with-files run tomorrow 12:00Z; the cutover-prefix seam + Path-C MSI ask held for Andrew/CTO.

## Next Steps
- **[0.6.2 self]** monitor tomorrow 12:00Z first real with-files run (download + completion-popup path differs from empty) -> verify S3 landing -> RAVC COO; tune if needed.
- **[0.6.2 self]** 49f AC#3 silver verify on tonight's 21:53Z nightly (served artifact) -> RAVC COO.
- **[Andrew/CTO]** cutover-prefix decision (validation vs 01_raw/) + the Schwab enterprise-MSI (Path-C) ask.

## MCP traffic
RAVC to COO (accept) + CTO (PRD input); UA 0.0.1 consults x3 (feasibility, install-URL, 1923/no-CLI) -- decisive grounding throughout.
