# Session Log — gold_dispatch wait_phase gate hotfix

**Agent:** 0.6.0_AE_PartnerETL
**Date:** 2026-04-22
**Session start:** ~08:47 ET (startup investigation)
**Session type:** Unscheduled hotfix — discovered on startup

---

## Summary

On startup, S3 audit of overnight gold logs revealed three consecutive chain_full failures
at the same PHASE_D1 gate check. Root-caused, fixed, committed, uploaded, pushed in one session.

---

## Problem Discovery

Pulled S3 gold log list as part of startup state check. Found:

| Log | Size | Outcome |
|---|---|---|
| chain_full_20260421_220446.log | 1.8 MB | FATAL: gate artifact missing after PHASE_D1 |
| chain_full_20260421_230045.log | 1.8 MB | FATAL: gate artifact missing after PHASE_D1 |
| chain_full_20260422_040056.log | 1.8 MB | FATAL: gate artifact missing after PHASE_D1 |

All three failing at identical line: `FATAL: gate artifact missing after PHASE_D1: s3://opal-data-bd/gold/validation/aua_certification/`

D_00, D_00c, D_03 (PHASE_D1 scripts) all completed. D_00b, D_01, D_02, D_04 (PHASE_D2/D3/D4) never ran.

---

## Root Cause Analysis

**Faulty gate check (gold_dispatch.sh `wait_phase` function, line 306):**

```bash
# Old — broken:
if ! aws s3 ls "s3://$BD_S3_BUCKET/$gate_artifact" --recursive --max-items 1 &>/dev/null; then
```

`aws s3 ls` does not support `--max-items` in AWS CLI v1 (1.44.44 locally; runner likely also affected). The command exits 255 with `Unknown options: --max-items,1` unconditionally. Since `&>/dev/null` hides both stdout and stderr, the non-zero exit silently triggers the FATAL.

**Confirmed locally:**
```
aws s3 ls "s3://opal-data-bd/gold/validation/aua_certification/" --recursive --max-items 1
  → Unknown options: --max-items,1 | Exit: 255

aws s3 ls "s3://opal-data-bd/gold/validation/aua_certification/" --recursive
  → [24 objects listed] | Exit: 0
```

**Introduced in:** `e1e3b7c2` (2026-04-16, feat: parallel 14-phase dispatcher). Gate has been broken since that commit.

**C_02 was correctly writing the cert:** Log evidence shows `OK: s3://opal-data-bd/gold/validation/aua_certification/2026-04-20.json` at 23:30Z in the nightly log — written before PHASE_D1 starts. The artifact existed; the check mechanism was broken.

**Impact scope:** PHASE_D2 (D_00b, D_01), PHASE_D3 (D_02), PHASE_D4 (D_04) have not run in any full chain since 2026-04-16. Manual `--group D` foreground dispatches (which bypass the parallel dispatcher gate) covered the gap — explaining why portal users saw fresh data.

---

## Fix

**One-line change in `wait_phase` (gold_dispatch.sh line 306):**

```bash
# New — fixed:
if ! aws s3 ls "s3://$BD_S3_BUCKET/$gate_artifact" 2>/dev/null | grep -q .; then
```

- Drops `--max-items 1` and `--recursive` (non-recursive listing sufficient for direct-file prefixes)
- Pipes stdout through `grep -q .` which exits 1 (no match) when prefix empty, 0 when any output present
- Safe under `set -e`: command runs inside `if` condition; errexit is suppressed for if-conditions per bash spec
- Fixes both PHASE_D1 (`aua_certification/`) and PHASE_D2 (`role_aua/`) gates (same function)

**Bash syntax checked:** `bash -n data/black_diamond/scripts/gold/gold_dispatch.sh` → Syntax OK

---

## Deployment Sequence

| Step | Action | Result |
|---|---|---|
| 1 | Edit gold_dispatch.sh | Line 306 fixed |
| 2 | bash -n syntax check | OK |
| 3 | git commit --only (f201c75d) | fix(gold_dispatch): replace aws s3 ls --max-items 1 gate with grep -q pipe |
| 4 | aws s3 cp → s3://opal-data-bd/code/gold/gold_dispatch.sh | Upload OK |
| 5 | git push origin CLOUD | f201c75d pushed |
| 6 | MCP COO + CTO | Delivered |

**Deploy path:** runner syncs `code/gold/` at chain start via `sync_scripts`. Fix will be live on next chain run (tonight's 23:00Z nightly or manual dispatch).

---

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| Investigation | aws s3 ls | gate check direct test | Confirmed --max-items exits 255; without it exits 0 |
| Investigation | aws s3 ls | s3://opal-data-bd/gold/validation/aua_certification/ | 24 objects present (2026-03-11 → 2026-04-20) |
| Pre-commit | bash -n | gold_dispatch.sh | Syntax OK |
| Post-deploy | comp-pipescript | deployed gold_dispatch.sh | N/A — shell script not in Python corpus |

No Python files edited. Pre-commit py_compile gate not applicable (bash script).

---

## MCP Outbound

| To | Subject | Time |
|---|---|---|
| 2.0.0_SA_COO | HOTFIX SHIPPED: gold_dispatch gate fix f201c75d | 20260422T124744Z |
| 1.0.0_SA_CTO | HOTFIX f201c75d: gold_dispatch wait_phase gate fix | 20260422T124754Z |

---

## Current State

- Fix deployed to S3 and CLOUD branch (f201c75d)
- Both PROD and QA runners will pick up fixed gold_dispatch.sh on next chain start (S3 sync at boot)
- No manual SSM hot-patch needed (sync_scripts pulls from S3 at chain start)
- AE lane: idle, registered live (PID 5440)
- Inbox-watch running (task bhku8dgkr)

## Next Steps

1. **[0.6.0_AE]** Tonight's 23:00Z nightly will be first full end-to-end test of the fix. Monitor S3 logs for `Gate OK: gold/validation/aua_certification/` and full D-tier completion (D_00b, D_01, D_02, D_04 PERF entries in log).
2. **[0.6.0_AE]** On nightly completion: verify D_02 (advisor_client_detail) + D_04 (client_portal_summary) artifacts are fresh in S3.
3. **[1.0.0_SA_CTO / 2.0.0_SA_COO]** Assess whether HLOT2b + CHART-ALIGN validations that were blocked by D-tier gate are now unblocked by tonight's nightly.
4. **Carried forward:** SL-AE1 email draft on COO hold, Schwab-bucket-access TF drift, ADVI_STAUDT.OPB deferred.

## Incidents / Lessons

1. **Silent gate failure via exit code mismatch.** `aws s3 ls --max-items` silently exits 255 (stderr hidden by `&>/dev/null`). The FATAL message was visible in the log but the underlying AWS CLI error was not. Pre-ship gate testing should verify the gate command exits 0/1 as expected. Add gate-command test to the post-deploy checklist.

2. **--max-items is an `aws s3api` option, not `aws s3 ls`.** High-level S3 commands and API commands have different option surfaces. The fix (`grep -q .`) is CLI-version-agnostic.

3. **Group D foreground runs masked the regression for 6 days.** Because manual `--group D` bypasses the parallel dispatcher gate, D_02/D_04 outputs were kept fresh via those dispatches. This delayed detection. The regression was only visible on startup because I specifically checked what the overnight chains produced.
