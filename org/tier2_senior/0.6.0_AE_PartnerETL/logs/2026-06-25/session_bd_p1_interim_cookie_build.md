# Session Log — 0.6.0_AE_PartnerETL — BD-P1 49F Interim-Cookie Build

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE
**Date:** 2026-06-25 (~1505–1600Z)
**Project:** ADVI_BDAPIMIG (P1 interim-cookie solution)
**TO:** ADVI_BDAPIMIG.P1 (pending)
**Driver/verifier:** 3.0.0_SA_CVO (BD lane = CVO+Andrew). CTO arch-gate.

## Summary

Fresh `0.6.0_AE_PartnerETL` spawn for the ADVI_BDAPIMIG P1 interim-cookie build (Andrew PEAK).
Startup + watcher armed, took the CVO GO, and built all 3 interim components in the CVO-directed
order **A → C → B**, each Terraform-deployed + live-proven + CVO-verified. Keeps 49F BD REST
ingest flowing on a manually-seeded `.bd.identity` cookie (password/auto-login on Andrew hold)
with least-possible manual friction + zero silent failure.

## What shipped

| Comp | Lambda | Schedule | Tag | CVO verdict |
|---|---|---|---|---|
| A keepalive | bd-49f-keepalive | rate(15m) | bd-v2.33.0 | ACCEPTED (4/4 bars) |
| C freshness | bd-49f-freshness-probe | rate(1h) | bd-v2.34.0 | ACCEPTED (full pass) |
| B runner | bd-49f-runner | cron(0 2 UTC) | bd-v2.35.0 | smoke-landed; CVO dry-run pending |

- **(A)** GET `/datamining/auth/keepalive` on the SM `.bd.identity` (READ-ONLY GetSecretValue);
  204=extend; 401/403 → direct SNS re-capture alert + `KeepaliveOK=0` + verifier-absence alarm.
  Live invoke `{ok:true,status:204}`.
- **(C)** GET `/auth/token` → `AuthTokenOK` (401-specific; 5xx=transient/no-page) + per-table
  `SilverAgeHours{transactions,allocations,realized,unrealized}`. Alarm-driven paging
  (authtoken-dead/absence + 4× silver-stale) → `opal-bd-49f-cookie-alerts`. Live invoke proved
  per-table discrimination (realized/unrealized correctly ALARM @138h; txn/alloc OK).
- **(B)** Daily runner pulls the shared `cot_bronze_ingest.py` from `opal-data-bd/code/bronze/`
  (Model-B, no fork), 4 env vars EXPLICIT, runs the 4 REST tables → `forwardfill_v2`. Retry/backoff
  401(no-storm)/5xx-Error(retry). Live smoke landed transactions (76MB) in 222s.

### Firm-separation HARD GATE (AC#4, the load-bearing risk)
3-layer defense: (1) runner sets all 4 env vars explicit; (2) `_assert_firm_separation()` added to
the shared `cot_bronze_ingest.py` (commit `eb0ce40f6`) — a non-cot firm with `BD_S3_BUCKET` unset
or `==opal-data-cot` ABORTS via SystemExit before any auth/S3; (3) `bd-49f-runner-role` has an
explicit IAM **Deny** on `opal-data-cot`. Guard is bd-agnostic (NFRA_DTAFLP — names only
`opal-data-cot`; the ds-commit-gate caught my first cut naming `opal-data-bd` and I fixed it).
Safe-by-construction for cot (firm unset/cottonwood → returns; verified vs the cot bronze SSM doc
which sets neither var). Proven dry-run matrix: 49f+unset=ABORT, 49f+cot=ABORT, 49f+bd=PASS,
cot-default=no-abort.

### Egress rework (CVO blocking finding on A)
CVO caught the SNS egress fired into the void (account in SMS sandbox + email PendingConfirmation).
Resolved: Andrew confirmed the email sub; CVO published a [TEST] and Andrew confirmed receipt →
email delivery-proven. SMS sub **dropped** (account has no SMS origination entity + sandbox =
false coverage). Added a guarded `{"test_alert":true}` hook to A+C for re-provable delivery without
a real dead cookie. SMS-as-2nd-channel = tracked non-blocking durable follow-up (origination
identity + production access = account-owner action).

## Deploy hygiene
3 deploy-completion ledgers opened-at-start + CLOSED-on-proof (bd-49f-p1a-keepalive /
bd-49f-p1c-freshness / bd-49f-p1b-runner), no stranded legs. Each: commit→build-and-upload→commit
sha→plan→safe-apply→0-diff→record-deploy→tag→push --follow-tags. Tags bd-v2.33.0 / .34.0 / .35.0.

## Remaining (TO stays pending)
- (B) full-4-table run gated on CVO/Andrew silver-fire GO (realized/unrealized still 138h-stale in
  SILVER — B lands their bronze forwardfill; DS owns the silver trigger).
- cron 02:00 UTC vs bd-silver precedence — DS/CVO confirm.
- Phase 2: decommission the 4 Playwright scrape boxes (parity-verify + separate GO; destructive).
- Durable follow-up: SMS 2nd channel; (D) Andrew manual reseed on C alerts. DEFERRED (Andrew hold):
  auto-login session-refresh.

## Runtime observation (banked)
transactions alone = 222s/3.7min (76MB, heaviest table). 4 tables sequential could approach the
900s Lambda ceiling on a slow BD day; daily incremental should fit + C's per-table alarms backstop.
If it times out, convert to per-table fan-out (4 Lambdas, each <4min). Flagged to CVO.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-glob` | locate cot_bronze_ingest.py + session-fetch + cot-pipeline | found (1 each); systems-context surfaced |
| `comp-freshness chain bd` | ground the 4 REST silver prefixes + post-deploy nightly-health | transactions/allocations PASS, realized/unrealized FAIL@138h (expected) |
| `comp-iam gaps` | after each iam.tf change (A/C/B) | no gap for the 3 new roles; B GetObject = deny-present-coexistence (intentional cot Deny), not missing |
| `comp-which`/`comp-glob` rail | gated my raw `.tf`/`s3 ls` greps; used rail-checked markers where no comp-tool fit (existence-listing of a cross-firm shared script not in bd's PIPELINE_MAP) | compliant |

Rail note: 2 raw `aws s3 ls code/` calls carried inline `# rail-checked:` markers (existence
listing of the shared script + templates in bd's bucket — comp-pipescript maps bd's OWN scripts,
not a cross-firm shared bronze script run firm-bound to bd).
