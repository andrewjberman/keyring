# work_2352Z_post_main_cycles — /work cron cycles post-main-session

**Serial:** 0.7.0_AE_CloudOps
**Date:** 2026-05-28 ~23:20Z-23:52Z
**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, COORDINATE

Continuation after work_2305Z_main_session.md. Three /work cron ticks.

---

## Cycle 1 (~23:20Z)

**TO queue flip:** cloudops-canonical-user-provisioning-and-cloud-audit.md pending→complete
(37d0096cd). Previously completed Phases 1-3 but status hadn't been flipped.

**S2 backfill root-cause (COO dispatch):**
COO flagged 3 auto-stops as a pattern requiring root-cause, not blind 4th restart.

Root cause: mdpf-daily-runner EC2 user-data runs mdpf-daily-dispatch.sh on every start.
Dispatch finds no chain work (daily run already done, EventBridge DISABLED) → hits
"Auto-shutdown in 2 minutes (no work to do)" branch → `sudo shutdown -h +2` → kills
nohup backfill after ~2-9 minutes per start.

Fix: on 4th EC2 start, immediately sent SSM `sudo shutdown -c` → SHUTDOWN_CANCELLED.
Re-dispatched: r4 PID 2190, `/tmp/mdpf_backfill_r4.log`, 300 HH loaded, [1/252] processing.
Verified: only backfill process running, no chain/dispatch competing.

COO ACK: "nailed it — that's why root-causing beat a 4th blind restart."

**Watcher:** AUTO-RESPAWN-INTERRUPT-LOST → kill + relaunch (bgot6cb7l).

**LD-0131 L1 MSTR acceptance relayed by COO:**
MSTR ledgered COMPLETE, RV-0021 F-002 closed. Fixture at .tools/ accepted.
"clean close, thank you." — MSTR via COO relay.

---

## Cycle 2 (~23:42Z)

**Audit follow-ups (COO dispatch — F1 priority, F2/F7, domain reconcile):**

F1 (MEDIUM → ADVISORY):
- /api/scoped/security-scanner/* routes: verified all 4 have authorization_type=CUSTOM
  + portal_jwt authorizer in TF (routes.tf:375-400). JWT required at API GW level.
- Missing auth-validator-edge is defense-in-depth gap only — NOT open exposure.
- The security-scanner Lambda (data_refresh) serves firm-specific financial data
  (universe/scanner percentile data, presigned upload URLs for FactSet Excel).
- VERDICT: document as advisory; no remediation required.

F2 (LOW → CLOSED):
- /json-tiered/* → json-tiered/market-overview/ in S3: RSI details
  (commodities/equities/fixedIncome) + market summary. Public market metrics.
- No firm-specific data, no PII. No auth needed. CLOSED.

F7 (LOW → CLOSED):
- security-sweep-comprehensive EventBridge rule found: State=ENABLED,
  Schedule=cron(0 12 * * ? *) (daily at 12:00 UTC). Active and scheduled. CLOSED.

F6 (MEDIUM → ESCALATED then CLOSED by Andrew direct):
- Inflection users have 3 email domains: inflection.com, inflectionwealth.com, inflectionwealthmgmt.com
- Escalated to CTO per COO routing. CTO routed for Andrew decision.
- Andrew: "the only real user for inflection is peter@inflectionwealth.com, that is their domain"
- See Cycle 3.

**RAVC2-ACCEPT** from COO: "Fast + thorough. F1/F2/F7 closed clean, F6 correctly escalated."

---

## Cycle 3 (Andrew direct ~23:48Z) — F6 domain reconcile

Andrew direct: inflectionwealth.com is the canonical domain.

Changes applied:
- `portal/src/lib/firmAccess.ts` (portal/DEV commit 4d08170c):
  FIRM_EMAIL_DOMAINS['inflection'] = 'inflectionwealthmgmt.com' → 'inflectionwealth.com'
- `users/scripts/create_user_v2.py`: email_domain + comment updated
- `FIRM#inflection/META` DynamoDB: domain field updated live via aws dynamodb update-item
- `docs/reference/user-provisioning-firm-scope-profiles-20260528.md`: discrepancy note replaced

Commits: 6962a88a8 (script + portal pointer), f2ee8c806 (doc) → CLOUD.
COO notified. F6 FULLY CLOSED.

---

## Compiler Tools

| Tool | Result |
|---|---|
| comp-routes behaviors (F1) | /api/scoped/security-scanner/* has no CF auth-edge — verified API GW authorizer present instead |
| comp-routes auth-map | Confirmed F2 json-tiered content (market-overview, public-safe) |
| DynamoDB update-item | FIRM#inflection/META.domain = inflectionwealth.com |

---

## Monitor items remaining

- S2 backfill r4 (PID 2190, ~04:21Z ETA): signal DS~B on completion → timeseries rebuild
- Long-term TF fix (MDPF_NO_SHUTDOWN=1 in user-data): COO tracking as follow-on TO
