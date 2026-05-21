# YALP_MDSRC.C1 Phase 0 — YCharts Credential Pipeline: Confirmations + Build Architecture

| Field | Value |
|---|---|
| Task Order | YALP_MDSRC.C1 (ae-ycharts-credential-pipeline) |
| Agent | 0.7.0_AE_CloudOps |
| Date | 2026-05-21 |
| Build spec | docs/briefs/mdsrc-ycharts-internal-api-20260520.md §3 (A3 P2, af5102dd3) |
| Status | Phase 0 COMPLETE — build cleared to proceed (live-capture stage seat-gated) |

---

## 1. Secret decision (TO Phase-0 requirement: reuse/rename vs new — do not duplicate)

Two DISTINCT credential artifacts — not a duplication:

- **`ycharts/credentials`** (EXISTS, `infra/aws/terraform/inf-pipeline/secrets.tf:65`) —
  the YCharts **login** credentials `{username, password}`. TF manages the
  secret resource; the value is placed out-of-band via `put-secret-value`
  (mirrors the `orion/credentials` pattern — the credential never lands in
  TF state). This is the INPUT to a (re-)login. **C1 reuses it read-only** —
  the capture Lambda reads it to log in. C1 does NOT move or re-manage it
  (it stays in inf-pipeline; `System: InflectionPipeline`).

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

No blocker. The secret architecture is decided (reuse `ycharts/credentials`
read-only; stand up `ycharts/session/current`). The seat is understood
(build now; live-capture gated on the `~A`/A4 handoff). The capture runtime is
decided (container-image Lambda, real Node). Build proceeds.
