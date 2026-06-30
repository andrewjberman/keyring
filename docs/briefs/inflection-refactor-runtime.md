# Refactor SPEC-4: Inflection — RUNTIME (cleanup / single-runner / auth / validation)

**Author:** 3.0.0_SA_CVO (Andrew-direct refactor planning, ADVI_BREAKS unified-flow) | **Date:** 2026-06-30
**Upstream:** SPEC-1 bronze, SPEC-2 silver, SPEC-3 gold. **Status:** DRAFT → CTO PRD. The final spec of the batch.

---

## 0. Governing principles (Andrew-locked)

1. **ONE inf-pipeline runner — the unified EC2 — and NOTHING else.** Decommission every other runner/trigger/lambda so there is zero confusion about what produces inf data (§1).
2. **Auth must be robust + observable.** Document exactly how we authenticate and how the token/cookie refreshes; alarm BEFORE a lapse goes dark, not after (§2).
3. **OTP is a first-class mechanism, not an afterthought.** Orion does phone/SMS OTP; build a reliable path to satisfy it (modeled on the Black Diamond manual-OTP approach) so a forced re-auth never silently darkens the pipeline (§3).
4. **End-to-end validation gates** prove the single runner delivers fresh, correct, complete data every day (§4).

## 1. The single runner — KEEP / DECOMMISSION inventory

**THE runner (KEEP):** `inf_gold_layer_runner` EC2 (i-0ed5afded2ebd4ed4) — becomes the sole pull→silver→gold machine (Inflection's small book fits one machine).

| Resource | Disposition |
|---|---|
| `inf_gold_layer_runner` EC2 | **KEEP** — the one unified runner |
| `inf_exporter` EC2 (i-081ae6aafb394fb1a) | **KEEP (auth box)** — the Playwright JWT/OTP sign-in box `[DECISION: fold onto the unified runner, or keep as the isolated auth box?]` |
| `inf_bronze_runner` EC2 (i-083ad9ae297f88e9f) | **DECOMMISSION** — Eclipse pull moves onto the unified runner |
| `inf_gold_qa_runner` EC2 (i-04373615f03fbf9a9) | **DECOMMISSION** `[DECISION: or retain for QA/PROD-parity?]` |
| 9 cron pull λ (`inf-api-reps`, `inf-accounts-v2-daily`, `inf-unified-account-dim-daily`, `inf-api-assets-v2`, `inf-api-positions`, `inf-tax-daily`, `inf-api-txn`, `inf-billing-daily`, `inf-performance-daily`) | **DECOMMISSION** — pull moves to the unified EC2 (bronze SPEC-1 R1) |
| `inf-bronze-trigger`, `inf-assets-trigger` λ | **DECOMMISSION** — no bronze-runner; one trigger path remains |
| `inf-silver-chain`, `inf-nna-partition-checker` λ | **ASSESS/DECOMMISSION** — fold into the single chain if redundant |
| `inf-etf-ownership-daily` λ | **ASSESS** — standalone data λ; fold or keep per use |
| `inf-client-detail` λ | **DECOMMISSION** — deployed STUB, no API Gateway wired (CVO ground-truth) |
| `inf-gold-trigger` λ | **KEEP** — the single runner's trigger (one chain dispatch) |
| `inf-jwt-trigger`, `inf-otp-relay` λ | **KEEP + HARDEN** — the auth/OTP mechanism (§2/§3) |
| `inf-ec2-launch-monitor`, `inf-ec2-retry-launch` λ | **KEEP** — adapt to the single runner |

**No second producer of any inf artifact may remain** — the single-writer principle (TO-2) generalized to the whole pipeline. Acceptance: a sweep finds exactly one runner, one trigger path, one writer per S3 key.

## 2. Auth — current mechanism (grounded) + robustness

**Current (grounded — `inf-jwt-trigger` + D3 §3.1):**
- `inf-jwt-trigger` λ, mode `jwt-extract` (08:13 ET daily) → SSM doc `opal-inf-jwt-fetch` on `inf-exporter` EC2 → **Playwright headless sign-in as Andrew** on `api.cloud.orionadvisor.com` → captures the `Authorization: Session <jwt>` header → writes **SM `orion/jwt/current`** (HS512, ~10h TTL) + S3 mirror `orion/jwt/current.json`.
- Then exchanges the Orion JWT for the Eclipse JWT via `GET /v1/admin/Token` → **SM `orion/eclipse_jwt/current`** (HS256). Poll: 300s / 15s.
- **Device-remember cookie** persisted in the browser profile (`s3://opal-data-inf/orion/browser-profile/state.json`) → steady-state runs are **OTP-free (~30–90d cookie TTL)**.
- Header contract: `Authorization: Session <jwt>` (literal `Session `, NOT `Bearer`); required `App/AppPath/BrowserSessionId/Origin/Referer` headers; download-fetch also accepts `?Authorization=<jwt>` query param.

**Robustness gaps to close:**
- **Silent cookie-expiry = the 49F-class dark risk.** When the ~30–90d device cookie expires (or Orion forces re-auth), the next sign-in needs an OTP; if not satisfied, the pipeline goes dark. → **Proactively monitor cookie age + JWT freshness; alarm BEFORE expiry** (e.g. at T-7d), not after a failed run.
- **JWT-refresh failure must be LOUD.** A failed `jwt-extract` must fire an alarm + block-with-signal (not a silent stale JWT). Tie to the existing `inf-otp-alert` SNS.
- **Eclipse roster dependency (D3 §5.1):** the Eclipse JWT needs Andrew on firmId 209900; de-listing → `422 No Firm Associated`. Record the Eclipse-admin contact; alarm on 422.

## 3. OTP mechanism (the phone/SMS OTP — make it robust)

**Current:** `inf-otp-relay` λ (Function-URL HTML form, token-gated via SM `inf/otp-relay/token`) — Andrew enters the SMS/phone OTP code → writes `s3://opal-data-inf/otp/state.json`; an EventBridge rule on that object resumes the sign-in. (Lambda lives outside `infra/aws/lambda/inf-pipeline/` — confirm location at impl.)

**Harden (the Black-Diamond-style manual-OTP mechanism Andrew flagged for the final step):**
- **Proactive prompt:** when a re-auth needs an OTP, fire `inf-otp-alert` SNS to Andrew (push/SMS/email) with the relay link — don't wait for him to notice a dark pipeline.
- **A reliable, durable relay form** (the BD-manual-OTP analog): a token-gated Function-URL where Andrew enters the phone OTP on demand; the sign-in resumes within the JWT-fetch window.
- **Cookie-refresh discipline:** maximize the device-remember cookie lifetime; re-persist it each successful sign-in; monitor its age (§2).
- `[DECISION]` whether to keep the dedicated `inf-exporter` auth box or fold the Playwright sign-in onto the unified runner (auth-box isolation vs single-machine simplicity).
- Goal: a forced re-auth is a **bounded, alerted, human-in-the-loop-with-a-clear-path** event — never a silent multi-day outage (the 49F lesson).

## 4. Validation — end-to-end gates (prove the single runner delivers)

- **Freshness:** `gold/meta/pipeline-complete.json` advances every run; current-day `holdings_{run_date}` exists (SPEC-3 AC1).
- **Value-parity (no tolerance):** served `total.aua` == current-day `positions_mv` == Orion **to the cent** — the TO-6 alarm (CVO-co-verified) on every served firm-header.
- **Completeness:** each bronze dim carries the full endpoint field-set; silver field-set ⊇ bronze (SPEC-1 AC4 / SPEC-2 AC4).
- **Single-writer sweep:** exactly one writer per served key; one runner, one trigger path (§1).
- **Auth health:** JWT fresh (<10h), cookie age < expiry-alarm threshold, Eclipse JWT valid (no 422).
- **Parity gate (cutover):** refactored output == pre-refactor output, several clean days, before the old runners are torn down.

## 5. Retroactive / decommission sequence

- **RT-R1 — stand up the unified runner** (SPEC-1/2/3 land on `inf_gold_layer_runner`: pull all dims → silver → gold, full + incremental-with-current-day-B_00).
- **RT-R2 — parallel-run + parity** (new single runner alongside the legacy lambdas/runners; confirm parity several days — never-widen).
- **RT-R3 — decommission** (in order): the 9 cron pull λ + their EventBridge rules → `inf-bronze-runner` EC2 + `inf-bronze-trigger`/`inf-assets-trigger` → the stub/redundant λ → `inf_gold_qa_runner` (if not retained). Each via the deploy-ledger; never-widen on shared roles.
- **RT-R4 — harden auth/OTP** (§2/§3): cookie-age alarm, loud JWT-fail, the robust OTP relay. **This is the FINAL step** (Andrew-flagged in SPEC-1 §7).
- **RT-R5 — single-writer/single-runner sweep** confirms no orphan producer remains.

## 6. Acceptance criteria (machine-checkable → PRD/TO)

- AC1: exactly ONE inf-pipeline runner (the unified EC2); a resource sweep finds no other active producer/trigger; the decommissioned EC2s are stopped + their EventBridge rules removed.
- AC2: one writer per inf S3 served key (no second producer).
- AC3: auth — SM `orion/jwt/current` < 10h old on every run; device-cookie age monitored with a pre-expiry alarm; JWT-refresh failure fires `inf-otp-alert` (loud, not silent).
- AC4: OTP — a forced re-auth produces an Andrew alert + a working relay path; resolved within the JWT-fetch window; no silent dark.
- AC5: validation gates (§4) all green for several consecutive clean days before legacy teardown (parity-gated cutover).
- AC6: Eclipse-roster + 422 alarmed; Eclipse-admin contact recorded.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| read inf-jwt-trigger lambda + D3 §3.1 | the grounded auth/JWT/OTP/cookie-refresh flow | PASS (rail-checked) |
| ls inf-pipeline lambda dirs + TF aws_instance | the KEEP/DECOMMISSION resource inventory | PASS |
| inflection-bronze/gold audits + pipescript advi-inf | the resource roles (runners/triggers/stub) | PASS |

— 3.0.0_SA_CVO
