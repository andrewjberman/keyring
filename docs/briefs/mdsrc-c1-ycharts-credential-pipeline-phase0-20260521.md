# YALP_MDSRC.C1 Phase 0 — YCharts Credential Pipeline: Confirmations + Build Architecture

| Field | Value |
|---|---|
| Task Order | YALP_MDSRC.C1 (ae-ycharts-credential-pipeline) |
| Agent | 0.7.0_AE_CloudOps |
| Date | 2026-05-21 |
| Build spec | docs/briefs/mdsrc-ycharts-internal-api-20260520.md §3 (A3 P2, af5102dd3) |
| Status | Phase 0 COMPLETE — CREDENTIAL BLOCKER surfaced (see §6); path-invariant build proceeding |

---

> **§6 UPDATE (2026-05-21, post-COO-expedite):** an empirical check of
> `ycharts/credentials` corrected §1 below — it holds a captured **cookie
> bundle**, NOT `{username, password}`. That blocks an automated fresh login.
> See §6. The §1 text is left with a correction note rather than rewritten,
> to preserve the audit trail.

## 1. Secret decision (TO Phase-0 requirement: reuse/rename vs new — do not duplicate)

Two DISTINCT credential artifacts — not a duplication:

- **`ycharts/credentials`** (EXISTS, `infra/aws/terraform/inf-pipeline/secrets.tf:65`) —
  ~~the YCharts **login** credentials `{username, password}`~~ **CORRECTED (§6):
  the secret holds only a `cookies` key — a captured cookie-bundle string, no
  username/password.** TF manages the secret resource; the value is placed
  out-of-band via `put-secret-value` (mirrors the `orion/credentials` pattern
  — the credential never lands in TF state). C1 reads it; it stays in
  inf-pipeline (`System: InflectionPipeline`). The §1 assumption that it held
  login creds came from the inf-pipeline `secrets.tf` comment (which describes
  the secret's *intended* `{username, password}` shape); the value actually
  placed is a cookie bundle — see §6.

- **`ycharts/session/current`** (NEW — C1 stands it up) — the captured
  **session cookie bundle** `{ycsessionid, csrftoken, aws-waf-token, AWSALB}`
  (A3 P2 §3.1). Distinct content, distinct lifecycle (refreshed pre-emptively
  ~every 72h, ahead of the ~96h `aws-waf-token` TTL), distinct producer (the
  capture Lambda) and consumer (C2's pull + the freshness probe). It is the
  OUTPUT of capture.

Decision: **NOT a duplicate** — login creds vs session bundle are different
artifacts. C1 stands up `ycharts/session/current` per the TO's stated option.
Same out-of-band-value pattern: TF manages the resource; the capture Lambda
writes the value via `PutSecretValue` (never a TF `secret_version`).

## 2. Seat status (TO Phase-0 requirement: confirm seat free / coordinate)

- A3 (0.1.0_DS_MarketIntelligence) is COMPLETE (all 4 phases) — it is no
  longer holding the YCharts seat. The TO's "do not evict A3's session"
  concern is discharged: A3 is done.
- A4 (the granularity/depth sweep) IS in flight — `0.7.0_AE_CloudOps~A`
  holds the single YCharts seat for the A4 entity sweep.
- Per the COO C1-GO: C1's seat-using stage (a LIVE capture/refresh run) is at
  least one full deploy-cycle out. The C1 BUILD — TF module, Lambda code, the
  secret resource, IAM, the alarm — needs NO seat. Only a live capture RUN
  evicts a session. So: build the full pipeline now; gate only the live
  first-capture on `~A` releasing the A4 seat. Coordinate the handoff directly
  with `~A` (MCP) when the build reaches that stage; escalate to COO only on a
  genuine same-window unsequenceable conflict.

## 3. Capture runtime (TO + A3 P2 constraint: real Node, never bun)

A1 proved Playwright `launch()`/`connectOverCDP()` HANG under `bun` on the
workspace host. The production capture must run on a real Node runtime.
Decision: **container-image Lambda** (Node + headless Chromium —
`@sparticuz/chromium` + `puppeteer-core`). Rationale: keeps the capture in the
Terraform-only Lambda deploy discipline (Rule 1) rather than standing up a
capture EC2 (its own manifest/SSM machinery for one periodic job); a
container-image Lambda is the established pattern for headless Chromium on AWS
and runs a genuine Node runtime (not bun). ECR repo + Dockerfile are part of
the C1 build.

## 4. Build architecture (the C1 deliverable)

New TF module `infra/aws/terraform/ycharts-pipeline/`:

1. **`ycharts/session/current` secret** — resource only; value written by the
   capture Lambda via `PutSecretValue`.
2. **Capture/refresh Lambda** (container image, Node + headless Chromium) —
   reads `ycharts/credentials`, logs into YCharts, navigates to an app page to
   clear the AWS WAF JS-challenge and mint `aws-waf-token` (A3 P2 §3.3),
   extracts the cookie bundle, writes `ycharts/session/current`. Triggered by
   (a) an EventBridge ~72h pre-emptive schedule and (b) on-demand on a 403.
3. **Freshness-probe Lambda** (lightweight, Python + requests) — one
   authenticated GET against an endpoint representative of the C2 pull set;
   classifies 200 vs 403; on 403 reads the body to distinguish hard eviction
   (`"concurrent sign in"`) from a partial/disturbed session
   (`"signed out"`) (A3 P2 §3.4); invokes the capture Lambda on failure.
4. **CloudWatch alarm** — on the probe's failure metric: a dead/evicted
   session surfaces fast.
5. **IAM** (least-privilege, resource-scoped):
   - capture Lambda: `GetSecretValue` on `ycharts/credentials` +
     `PutSecretValue` on `ycharts/session/current`.
   - probe Lambda: `GetSecretValue` on `ycharts/session/current` +
     `lambda:InvokeFunction` on the capture Lambda.

Deploy: Terraform-only (Rule 1) via the standard cycle (commit -> plan ->
safe-apply -> 0-diff -> tag -> push --follow-tags -> record-deploy). ECR image
build is part of the cycle (build/push image -> TF references the image URI).

## 5. Phase 0 verdict

~~No blocker.~~ **Superseded by §6.** The secret architecture, the seat
status, and the capture runtime are all decided as stated — but §6 (added
after the COO Phase-0 expedite) surfaces a credential-availability blocker on
the *fresh-session* capability. The path-invariant pieces build; the capture
Lambda + the live general_data.json test are blocked on the §6 decision.

## 6. CREDENTIAL BLOCKER — fresh-session capability (2026-05-21, post-expedite)

COO expedited a Phase-0 diagnostic: capture a FRESH YCharts session and do one
GET to `/charts/general_data.json` — 200 vs 403 settles whether 36 A4 entities
(29 MSCI + 7 Bloomberg-bond indices) are a recoverable degraded-session issue
or a permanent account-entitlement gap.

**The blocker.** An empirical check of `ycharts/credentials` (key names +
value-classes only, never values) found it holds exactly ONE key — `cookies`,
a ~1428-char captured-cookie-bundle string. There is NO `username`/`password`.
Therefore C1 **cannot perform an automated fresh login** — and the existing
(degraded) cookie bundle just reproduces ~A's 403. A genuinely fresh session
cannot be established autonomously.

This also forks C1 itself: the capture/refresh Lambda was scoped as "automated
headless login -> fresh cookie bundle." Without login credentials, the capture
Lambda cannot renew `ycsessionid` (it could only re-mint the `aws-waf-token`
via headless app-page navigation). `ycsessionid` is what general_data.json's
403 "You are signed out" implicates.

**Two paths (COO/Andrew call, surfaced to COO 2026-05-21T14:17Z):**
- **(A)** Andrew places YCharts `username`+`password` into `ycharts/credentials`
  -> C1 builds the automated-login capture as the TO scopes it; the
  general_data.json verdict drops out of C1's first capture; fully automated.
- **(B)** No credentials -> C1 is an ATTENDED-refresh model: a human logs in
  and places a fresh cookie bundle in the secret; C1 automates only the
  freshness probe + `aws-waf-token` re-mint + the eviction alarm. The
  general_data.json test then needs one attended login.

**Evidence lean (not the definitive test):** the 403 body "You are signed out.
Please sign in again." is A3 P2 §3.4's *disturbed-session* signature; an
entitlement block typically reads "feature not available / upgrade," not
"signed out." That leans toward (A) — a fresh session probably DOES restore
general_data.json — but the fresh-session GET remains the only definitive test.

**Recommendation: path (A).** It is the TO-as-written (fully automated
capture/refresh), it makes the capture Lambda viable, and it produces the
36-entity verdict cleanly.

**Build status under the blocker:** path-invariant pieces proceed —
the `ycharts-pipeline` module skeleton + the `ycharts/session/current` secret
(`8d4a27a8a`) and the freshness-probe Lambda (`188be4686`) are committed. The
capture Lambda + its Terraform + the live test are held for the §6 routing.
