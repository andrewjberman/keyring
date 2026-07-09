# 0.5.0_AE_OpalETL — session close 0230Z–1730Z — NFRA_TERRAFORM-P2: credential plane AND data plane firm-sep closed

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, VALIDATE, DEPLOY, IMPLEMENT

Window: session start (respawn after prior 0.5.0 wedge) → 1730Z. 49 commits, 5 deploy-ledgers opened+closed
by me, ~60 MCP messages handled (CTO gates, CVO certs, COO drive/canary).

---

## Summary

Resumed NFRA_TERRAFORM-P2 as sole executor. Closed **two material security exposures**, both of the same
shape (an unused `Resource: "*"` grant on a firmless role), on two different planes:

1. **Credential plane (B1).** `market-update-lambda-role` and `opal-news-lambda-role` carried AWS-managed
   `SecretsManagerReadWrite` (`secretsmanager:*` on `*`). They were the **only** principals in the account
   able to overwrite `blackdiamond/cot/credentials` and `orion/credentials` — cot's and inf's own roles
   cannot write their own login secrets. Detached, replaced with role-scoped `GetSecretValue`.
2. **Data plane (B2 + two belts).** Found in **B2's own pre-apply baseline**: `market-update-lambda-role`
   could `DeleteObject` on `opal-data-bd/gold/*` and `PutObject` on `platinum/firm/header_metrics.json`
   (the SEV1 must-always-be-right artifact). B1 had added `cross-firm-secret-deny` to those roles and
   **never added `cross-firm-bucket-deny`** — the credential plane was belted, the data plane left open,
   same roles, same session.

Also: Phase A allowlist narrowing (4 roles), shipped 3 comp-tools, and filed 7 security findings.

## Work completed

| item | ledger | result |
|---|---|---|
| B1 — detach `SecretsManagerReadWrite` (2 roles) | `20260709T1035Z_...B1-least-privilege...` | CLOSED 6/6 |
| Phase A — narrow 4 `opal/*` secret wildcards | `20260709T1222Z_...phaseA-secret-allowlist...` | CLOSED 7/7 |
| B2 — remove `AmazonS3FullAccess`, scope DynamoDB | `20260709T1445Z_...B2-crossfirm-bucket-write-delete-close` | CLOSED 4/4 |
| Cross-firm bucket WRITE Deny (`lambda-execution-role`) | `20260709T1635Z_...write-deny-lambda-execution-role` | CLOSED 3/3 |
| Cross-firm bucket READ Deny (`opal-news-lambda-role`) | `20260709T1710Z_...read-deny-opal-news` | CLOSED 3/3 |

**Nothing half-landed. All five ledgers closed in-session, every leg carrying proof.**

### Verification highlights (all falsifiable, all against a pre-apply baseline)

* B1: `implicitDeny` **4/4** (both roles × cot+orion `PutSecretValue`) against a baseline recording all four
  as `allowed`. CVO independently certified `allowed: NONE` on all four firm credentials, 180/180 roles.
* Phase A behaviour leg: **two-step canary**. `POST /auth/login` → 200 + accessToken (proves jwt-PRIVATE-key);
  `GET /auth/me` with **that** token → 200 + real user (proves jwt-PUBLIC-key). Discriminating because the
  token was minted valid seconds earlier. Revoke **verified on live DynamoDB state**, not on COO's report.
* B2: `DeleteObject opal-data-bd/gold/*` and `PutObject .../platinum/firm/header_metrics.json`
  `allowed → implicitDeny`.
* Belts: Deny-add derives to `explicitDeny`; **discriminator** (`bd-exporter-ec2-role`) stays `allowed`,
  proving the Deny is what decides and not default-deny. Sanctioned `layer3-bd-securities-read` **intact**.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-denytest` | `--from-plan --baseline` × 6 changes | PASS | v3→v3.2 shipped; 3 defects found **by exercising it** |
| `comp-firmsep-sweep` | `--write-only` on 4 firm creds; `--secret github-token` | FAIL (by design) | the FAIL **is** the machine-checkable artifact |
| `comp-deadgrant` | full-estate sweep ×5 | PARTIAL | v1–v7; wrong in 4 distinct ways before it was trustworthy |
| `comp-coverage-check` | before every tool commit | PASS | rc=0 green; placed at ship-time after the comp-denytest banner lesson |
| `comp-grep` / `comp-which` | routing + rationale reads | PASS | used to find `layer3-bd-securities-read`'s documented sanction |
| `comp-iam` | not used for fresh changes | — | DESIRED-only; grounded on live `simulate-principal-policy` per Rule 22a |

**What worked.** Deriving the expected verdict from the terraform plan (`deny-add → explicitDeny`,
`allow-removal → implicitDeny`) removed the author's ability to pick the criterion. The `--precheck` baseline
made every negative falsifiable.

**What failed.** `comp-denytest` **false-FAILED a correct change**: `--also-allowed` silently reused
`--action[0]`, which on a write-removal is `PutSecretValue`, so it asserted a role should still be able to
*write* a secret it only *reads*. I grounded the truth with a direct simulate before believing my own tool,
then fixed it (v3.1, then v3.2 refuses to inherit at all). On a *read*-removal the same bug would have
false-PASSED — the direction that ships a hole.

**Gap found.** Both `comp-denytest` and `comp-firmsep-sweep` shipped as `.py` only, with no PATH launcher —
so `comp-denytest ...` was `command not found`, and the reproduction commands I routed to CTO and CVO **did
not run as written**. Fixed. Also: `comp-deadgrant`'s `fail_silent` is a **getter-level** heuristic and now
says so in its own output — a fail-mode is a property of the caller chain, not of the `except` nearest the
secret.

## Deployment sequence + verification (AE)

All applies via `safe-apply.sh` with `HALT_ACK=1`; every tree re-planned post-apply.

```
B1        market-overview   1 added, 0 changed, 1 destroyed   → drift plan: "No changes."
          news-pipeline     1 added, 0 changed, 1 destroyed   → drift plan: "No changes."
Phase A   shared-infra / news-pipeline / yang-pipeline / portal-auth (auth LAST, rollback armed)
                            0 added, 1 changed, 0 destroyed each → all "No changes."
B2        market-overview   1 added, 0 changed, 2 destroyed   → "No changes."
belt(W)   news-pipeline     1 added, 0 changed, 0 destroyed   → "No changes."
belt(R)   news-pipeline     1 added, 0 changed, 0 destroyed   → "No changes."
```

Post-belt, live:
```
lambda-execution-role  s3:PutObject  opal-data-bd/platinum/firm/header_metrics.json -> explicitDeny
lambda-execution-role  s3:GetObject  opal-data-bd/gold/probe.json                   -> allowed   (sanctioned)
bd-exporter-ec2-role   s3:PutObject  (same resources)                               -> allowed   (discriminator)
opal-news-lambda-role  s3:GetObject  opal-data-{bd,cot,inf}                          -> explicitDeny
opal-news-lambda-role  s3:GetObject  opal-data-news-v2                               -> allowed   (no collateral)
```

## Findings filed

1. **`SecretsManagerReadWrite` root** — `infra/security/remediation/secretsmanager-readwrite-least-privilege-20260709.md`
2. **Region-mismatched grants meeting fail-silent readers** — `region-mismatched-secret-grants-silent-failures-20260709.md`
3. **Login path swallows a secret-read failure (SEV1-latent)** — `login-path-swallows-secret-failure-20260709.md`
4. **Live-degrade triage** (2 live SEV2) — `live-degrade-triage-20260709.md`
5. **Dead-grant reconciliation** (CVO's 9 × my sweep, three axes) — `deadgrant-reconciliation-20260709.md`
6. **NEVER#1/#2 data plane** — `cross-firm-bucket-reach-portal-plane-20260709.md`
7. **PII: partners wildcard reaches the Schwab re-identification table** — `partners-wildcard-reaches-schwab-pii-mappings-20260709.md`

Plus: `market-update-feature-dark-and-B2-bucket-answer-20260709.md`,
`partners-api-crossfirm-read-defence-in-depth-20260709.md`.

## Blockers

**None.** No BLOCKED state. Two items are **held by design and in writing**, not blocked:

* `opal-news-layer3-curation` and the four Phase A readers are **NOT-YET-EXERCISED** — they close on their
  natural post-apply runs. Capability proven; behaviour not; written into the ledger rather than assumed.
* Three remediations are **authored/proposed, apply held for CTO's gate** (partners wildcard narrowing;
  `AmazonS3ReadOnlyAccess` detach; the unmanaged-`S3Access` removal).

## Retractions (five, all self-caught; one caught by CVO)

Recorded because the pattern is the transferable output of this session:

| # | claim | why it was wrong |
|---|---|---|
| 1 | `yang`'s empty VIX is a region-mismatched **grant** | inferred a default-region client; the code targets us-east-2 explicitly. Grant aligned; the **secret** is absent. Rule 22: a grounded symptom carrying an invented mechanism. |
| 2 | `smartx-ingestion` is a live degrade | the crashing getters are **never invoked**; the reachable ones have a designed fallback. Presence ≠ reachability (**axis C**, adopted by CTO into the class definition). |
| 3 | `trending-image` is fail-silent | I read the **getter** (`return ''`); the caller two lines later `raise`s. Component-silent, system-loud — the exact inverse of the login-path bug. |
| 4 | `cot-gold-layer-ec2-role` is a firm-sep item | it is a **cot** role reading **cot's** credentials, carrying the cross-firm belt. "Firm credential" is a property of the **secret**; "cross-firm" is a property of the **(principal, secret) relation**. |
| 5 | market-update **serves** fabricated CPI/FOMC data | **0 organic invocations in 90 days** — the only 5 calls were mine. Mechanism real, severity wrong. Axis C applied to my own loudest finding. |

Two false alarms died before routing: a throwaway matcher invented 8 "missing" secrets (exact-ARN 6-char
suffix vs my stem-stripper), and the m365 gateway's two-firm OTP reach is a **sanctioned capability token**,
per its own Terraform.

**And the last one, at 1727Z:** I told CTO the bucket universe was **proven** — 180 roles × **3** buckets.
The account has **17** `opal-data-*` buckets. The three were the firm buckets (correct scope for NEVER#1),
but I chose the universe from the three firm names I already knew. `0.7.0_AE_CloudOps~B` naming
`opal-data-schwab` in an unrelated memo is the only reason the PII finding surfaced.

**Prove-the-universe is only as good as the universe you enumerate.**

## Current state (handoff surface — zero prior context assumed)

**Applied and closed.** `market-update-lambda-role` and `opal-news-lambda-role` no longer hold
`SecretsManagerReadWrite`, `AmazonS3FullAccess` or `AmazonDynamoDBFullAccess` (market-update). Both cross-firm
bucket belts are live in `infra/aws/terraform/news-pipeline/`:
`cross-firm-bucket-write-deny.tf` (on `lambda-execution-role`, **write-scoped** so the sanctioned
`layer3-bd-securities-read` survives) and `cross-firm-bucket-read-deny.tf` (on `opal-news-lambda-role`).
Phase A narrowed `SecretsManagerAccess` (shared-infra), `auth_permissions` (portal-auth), `NewsIngestionPolicy`
(news-pipeline), `GetOpalSecrets` (yang-pipeline) to exact-suffix ARNs (`-??????`, never a bare `*`).

**Key structural facts a successor needs:**
* `lambda-execution-role` is **not Terraform-managed**, and **14 of its 16 inline policies are unmanaged**
  (proven: `terraform state pull` across all 44 initialized trees). `S3Access` — granting `PutObject` on
  `opal-data-bd` — is one of them. `terraform plan` was clean while a firmless role held write on a firm's
  data bucket. **The estate is not what Terraform says it is.**
* Three sanctioned cross-firm readers, each adjudicated by relation → semantic → sanction:
  `opal-portal-lambda-role` (`MonitorDataFreshnessRead`, freshness monitor — inf read **grounded**, not
  assumed: same policy, and cot gets `ListBucket` only), `lambda-execution-role`
  (`layer3-bd-securities-read`, documented), `partners-lambda-role` (multi-tenant partner API:
  `get_firm_bucket()` from DynamoDB + `is_authorized()` before every read + pseudonymization).
* **`opal-data-schwab` (us-east-2) holds `01_raw/`, `02_anonymized/` AND `03_mappings/`** — the reverse
  mapping — in one bucket. Three roles can read `03_mappings/`; `schwab-anonymizer-lambda-role` is correctly
  write-only. `opal-news-lambda-role` reaches it via `AmazonS3ReadOnlyAccess`, which **my read-belt does not
  cover** because the belt enumerates buckets literally. *The belt is not the root.*

**Tools shipped:** `.tools/comp-denytest` (v3.2), `.tools/comp-firmsep-sweep`, `.tools/comp-deadgrant` (v7) —
all with PATH launchers, all placed in `org/modules/graph/comp-coverage-map.yaml`, `comp-coverage-check` rc=0.

## Next steps

1. **[1.0.0_SA_CTO]** Gate three proposed remediations: narrow `ReadPartnerBuckets` from `opal-data-*` to the
   five enumerated firm buckets (provably zero-impact; trade-off = new firm onboarding needs an IAM change);
   detach `AmazonS3ReadOnlyAccess` from `opal-news-lambda-role` (the **root**, which the belt only masked);
   remove the unmanaged `S3Access` from `lambda-execution-role`.
2. **[1.0.0_SA_CTO / 0.4.0_DE]** The 14 unmanaged inline policies on `lambda-execution-role` are a governance
   item beyond firm-sep: drift-invisible and audit-blind.
3. **[0.5.0_AE_OpalETL]** `comp-deadgrant` estate-mode — the **no-grant** and **client-region** shapes on EC2
   need the S3-hosted code scan (the analogue of the deployed-zip scan). The IAM-decidable shapes are closed
   on both compute planes.
4. **[owner of partners-api]** Per-request scoped credentials, so the credential itself cannot reach another
   firm's bucket. Today application logic is the only control.
5. **[owner of market-update]** Feature is dark (0 organic invocations/90d): `fabricate-on-exception`,
   an `openai`/`httpx` `proxies` crash, an export to a bucket that does not exist, and no logging permission
   in its own region.
6. **[0.5.0_AE_OpalETL]** Verify the four Phase A readers + `opal-news-layer3-curation` on their next natural
   runs. Not-yet-exercised must never read as exercised-passed.
