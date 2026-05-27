# work-cycle 5 — IAM logs/ amend ship + ADHC_COMPIL_V5.002 stale-TO cleanup

**Tick:** 2026-05-27 ~08:50Z (first /work post-overnight; cron schedule 7/27/47 each hour)
**Archetype:** IMPLEMENT (deliverable) + SCRIBE (drift cleanup)
**Commits:** `ccbc93a51` (IAM amend) + `5b8bc4413` (TO drift cleanup)

## Substantive deliverables

### 1. IAM logs/ amendment shipped — carry-forward task #14 CLOSED

- **Substrate:** `infra/aws/terraform/shared-infra/demo-transform.tf`
- **Change:** +1 inline `WriteScanExecutionLogs` Sid on `aws_iam_role_policy.demo_transform_runner_s3` — grants `s3:PutObject` on `arn:aws:s3:::opal-313476888478-lambda-artifacts/demov1/logs/*`. Least-privilege; no broader artifacts bucket exposure.
- **Terraform sequence:** plan (1 in-place change clean) → safe-apply (HALTGT-gated; Resources 0/1/0) → post-apply plan 0-diff confirmed.
- **Why:** ADVI_DEMOV1 Fire 7 empirical anchor (2026-05-26 ~07:0XZ) — `pii_leak_scan.py` body exited 0 (PASS-with-WARN: leak_count=0 + format_anomaly_count=193064) but SSM dispatch wrapper's `aws s3 cp .../logs/<exec>.log` returned AccessDenied → bash strict-mode propagated → SSM Status=Failed despite scan PASS. Sid commentary cites Fire 7 + cycle-145 disposition for auditor.
- **Wall:** ~12min (TF read → Edit → plan → safe-apply → 0-diff → commit → push → RAVC2). Within the "5-10min" ACK-CLOSE estimate; +1min owned-paths author-line resolution on first safe-commit attempt.
- **RAVC2-Request:** ws COO inbox `20260527T085604Z_0.7.0_AE_CloudOps__RAVC2-Request__IAM_logs__amendment_ship.md`.

### 2. ADHC_COMPIL_V5.002 stale TO-status cleanup

- **Discovery:** /work TO-queue scan surfaced TO file at `<status>pending</status>`. Reading the PRD `docs/architecture/ADHC_COMPIL_V5.md` line 3 + `org/projects/ADHC_COMPIL_V5.json` showed the **entire project** already complete 2026-05-26 ~18:35Z: TO-001 `6ffc457d5` + TO-002 **`03f0d42f2` 2026-05-26 ~16:16Z (Fix 2 comp-pipescript io Lambda extension; AC1+AC3+AC4+AC6 MET; AC2+AC5 PARTIAL closed via TO-VAL `a30fb1a15` + `ee08dc740`)** + TO-003 `0030aea6c` + TO-VAL `3365f258d` 8/8 PASS + CVO Mode B CLEAN `cc7fede51` 4/4 axes GREEN.
- **Action:** TO file `<status>` flipped to detailed-complete narrative citing all 5 ship commits + JSON-authoritative discipline reference (`[[feedback_drive_read_json_not_registry]]`).
- **Discipline anchor:** Caught the same drift class memory documents — `/drive` Step 2 reads JSON `current_phase`/`blocking` not REGISTRY/TO narratives because REGISTRY drifts post-ship faster than JSON. Same applies to per-agent TO files: JSON authoritative, TO file `<status>` can lag.
- **No work performed against the project itself** — TO-002 substantive impl already shipped by my own session yesterday; today's tick caught the narrative debt.

## Carry-forward status update

| Task | Status post-tick |
|---|---|
| #14 IAM logs/ amendment | CLOSED `ccbc93a51` + RAVC2 |
| #12 ADVI_DEMOV1 F1 retire-via-AE-AC5-closure write-up | standing AE-cycle pace; pick up next substantive /work tick |
| ADHC_COMPIL_V5.002 TO file pending → complete | CLOSED `5b8bc4413` (drift cleanup) |

## Banking observation

**Stale TO-file status as a /work-tick discovery class.** When a JSON authoritative source records a project complete but agent-side TO files lag at `<status>pending|in_progress|dispatched</status>`, /work TO-queue scans (which read TO file status) misread completed work as actionable. Two-axis fix:
- **Discipline:** Treat JSON `current_phase`/`status` as authoritative; cross-check before assuming TO is actionable. (Already canonical per `feedback_drive_read_json_not_registry` for /drive; same applies to /work.)
- **Structural:** TO file `<status>` flip should be atomic with JSON status flip at project close. Closure Discipline 3-step atomic (JSON + REGISTRY + PRD) per CLAUDE.md is for SINGULAR-MOMENT closes; for multi-TO projects each TO file should also flip atomically with its individual ship commit. Today the TO-002 flip lagged ~16h post-ship.

Banking candidate for /work skill addendum + /spot-check Sub-class scan extension (TO-file vs JSON drift class). Not pushing as a formal proposal this tick — surface to ws COO + CVO via RAVC2 banked-observation note if pattern recurs.

## Cycle log

- Commit-tag: work-cycle:5 (both commits this tick)
- Inbox: empty (broker + filesystem)
- Watcher: PROCESS-OK PID 701125 tracked task bd56t589i (no relaunch needed)
- Heartbeat sent
