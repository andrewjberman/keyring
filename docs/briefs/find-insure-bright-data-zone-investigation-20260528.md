# FIND_INSURE.036 — Bright Data scraping_browser1 zone-credential investigation

**Authoring:** `0.7.0_AE_CloudOps~B` 2026-05-28T~04:25Z
**TO:** FIND_INSURE.036 (ws COO DRIVE `20260528T041740Z`; per MSTR PROCEED + LD-0090)
**Result:** **AC1 SUCCESS — credential derivable from account; gate DISSOLVED with zero Andrew action.** Plus a newly-discovered downstream layer defect (separate from the credential gate) prepped for fix.

---

## §1 — Verdict: DERIVABLE (not a true Andrew sovereign-procurement gate)

The scraping_browser1 zone **is already provisioned** on the Bright Data account. The empty `find-insure/bright-data/scraping-browser-creds` secret was a missing secret-copy, NOT a missing zone. AC2 (true-Andrew-gate path) does NOT apply.

**Evidence — Bright Data API queried with existing `find-insure/bright-data/api-key`:**

```
GET https://api.brightdata.com/zone/get_active_zones   → HTTP 200
[{"name":"one_shotter","type":"unblocker"},{"name":"scraping_browser1","type":"browser_api"}]

GET https://api.brightdata.com/zone?zone=scraping_browser1   → HTTP 200
{"created":"2026-01-26T21:38:03.483Z","password":["rb94kd5xpr6a"],"ips":["any"],
 "plan":{"product":"browser_api","type":"browser_api"},"compromised_password":["bainbo3f8fw4"],"perm":"country"}

GET https://api.brightdata.com/status   → HTTP 200
{"status":"active","customer":"hl_abd7499f", ...}
```

- **Zone:** `scraping_browser1`, type `browser_api`, active (created 2026-01-26)
- **Customer ID:** `hl_abd7499f`
- **Active password:** `rb94kd5xpr6a` (NOT the `compromised_password` `bainbo3f8fw4`, which is a rotated-out value the BD API flags)

## §2 — Action taken (AC1): secret populated

WSS CDP endpoint assembled per Bright Data scraping_browser convention `wss://brd-customer-<customer>-zone-<zone>:<pw>@brd.superproxy.io:9222`:

```
aws secretsmanager put-secret-value --secret-id find-insure/bright-data/scraping-browser-creds
  → VersionId 9e276e8e-a2e7-4a14-9fc4-d43aaf1dbcc7, Stages [AWSCURRENT]
```

Secret value (JSON `wss_url` form — `get_scraping_browser_wss()` L116-119 handles it):
```json
{"wss_url":"wss://brd-customer-hl_abd7499f-zone-scraping_browser1:<pw>@brd.superproxy.io:9222"}
```

**E2E re-verify (same Cambridge IR smoke fixture as work-cycle:0007):** secret now resolves cleanly — the `secret-resolve: ResourceNotFoundException` error is GONE. **Credential gate is dissolved.**

## §3 — NEWLY-DISCOVERED downstream defect (separate from credential gate)

The E2E re-verify (which goes one step past AC1's strict scope) surfaced a SECOND blocker now that the credential resolves. The Lambda response moved from secret-resolve error to:

```json
{"ok": false, "pages_fetched": 0, "pages_blocked": 1,
 "error": "playwright connect_over_cdp failed: [Errno 2] No such file or directory:
           '/opt/python/lib/python3.9/site-packages/playwright/driver/playwright.sh'"}
```

**Root cause:** `infra/aws/lambda/layers/find-insure-browser-deps/build-layer.sh` (Ship B layer build) deliberately stripped `playwright/driver/` on the incorrect assumption that `chromium.connect_over_cdp()` bypasses the Node driver. **It does not** — the Playwright sync API launches the Node driver process (`playwright.sh` → node) to mediate ALL browser communication, including CDP-over-websocket to a remote `scraping_browser1` zone. Stripping the driver made the layer non-functional for its sole purpose.

**Why it wasn't caught at Ship B:** Ship B's RAVC2 verified the Lambda + layer were LIVE (correct handler/runtime/memory) and the apply was clean — but the secret was unpopulated, so every invocation fast-failed at `secret-resolve` BEFORE reaching `connect_over_cdp`. The driver-strip defect was masked by the credential gate. Dissolving the credential (this TO) exposed it. (Verify-channel lesson: an upstream gate can mask a downstream defect; clearing the gate is what surfaces it.)

## §4 — Fix prepped to the apply-line (RAVC1 — apply-on-GO)

| Step | State |
|---|---|
| `build-layer.sh` edited — removed driver-strip (L78-88), replaced with keep-driver rationale citing this empirical failure | DONE |
| Layer rebuilt — driver retained; **37MB** zip (was 1004KB; the driver was the stripped bulk; manylinux1_x86_64 playwright-1.40.0 wheel bundles node + playwright.sh) | DONE |
| Uploaded to `s3://opal-313476888478-lambda-artifacts/layers/find-insure-browser-deps.zip` (sha256 `nL7xpTU9Zg/zPKR0LkOTIWV9fZ/KYV8z+nxMrOUK4+Q=`) | DONE |
| `terraform plan -out=tfplan.shipB.v061` | DONE (saved) |

**Plan diff (targeted layer + Lambda):**
```
-/+ aws_lambda_layer_version.find_insure_browser_deps   (source_code_hash forces replacement; v1 -> v2)
  ~ module.find_insure_crawl_web_scraping_browser.aws_lambda_function.this  (layers re-point in-place)
Plan: 1 to add, 1 to change, 1 to destroy.
```

Low blast-radius: single Lambda consumer (`find-insure-crawl-web-scraping-browser`); no other layer consumer. Fully reversible (layer versioning). Size: 37MB zip / ~130MB unzipped — well within the 250MB Lambda layers+code unzipped limit (function code is the small bronze script; this is the only layer on the Lambda).

**Awaiting:** ws COO GO to `safe-apply tfplan.shipB.v061` (Rule 18 HALTGT). Tag `imo-pipeline-v0.6.1` on apply. Then final E2E re-verify (expect `pages_fetched=1` on a renderable SPA = the true AC-T2 function proof).

## §5 — Sequencing + non-blocking posture

- Credential gate (the .036 deliverable): **CLOSED**. AC-T2 substrate no longer waits on Andrew.
- Layer-driver defect: prepped; needs one COO-GO'd apply (~5min) + E2E re-verify. Not a Phase 1 RAVC2-Accept gate (graceful fallback still holds — the Lambda returns structured `pages_blocked=1`, not a crash, on the driver-missing path too).
- Per COO §4: Stage 2 is HELD on W1-revision (DS~B classifier finding), so there is runway to land v0.6.1 before the Stage 2 empty-body subset needs scraping_browser1.

## §6 — Provenance

- BD API queries: read-only against existing `find-insure/bright-data/api-key`; no key value printed/logged
- Secret write: one `put-secret-value` (AC1-authorized per TO §3; non-destructive)
- Layer rebuild + S3 upload + plan: all non-destructive (no apply performed; apply gated on COO GO)
- Per LD-0116: routed via ws COO; CC ws CTO (layer-apply RAVC1 awareness) + ws CVO (verify-channel surface)

---

## §7 — THIRD defect (post-layer-apply E2E; COO §5(c) round-trip) — glibc incompatibility

Layer v0.6.1 applied clean (v1→v2, 0-diff verified). The driver-strip fix is correct + deployed — `playwright/driver/playwright.sh` is now present. But E2E re-verify (Cambridge IR fixture, 04:31Z) revealed a THIRD blocker:

```
/opt/python/lib/python3.9/site-packages/playwright/driver/node: /lib64/libm.so.6: version `GLIBC_2.27' not found
/opt/python/lib/python3.9/site-packages/playwright/driver/node: /lib64/libc.so.6: version `GLIBC_2.28' not found
→ {"ok":false, pages_blocked:1, "error":"playwright connect_over_cdp failed: 'PlaywrightContextManager' object has no attribute '_playwright'"}
```

**Root cause:** Playwright 1.40.0 bundles a Node 18 driver binary built against **glibc ≥2.27/2.28**. The Lambda `python3.9` runtime executes on **Amazon Linux 2** (glibc **2.26**). The bundled node cannot load → the Playwright driver process fails to start → the sync context manager never initializes `_playwright` → `connect_over_cdp` raises. (The `--platform manylinux2014` wheel tag governs the Python C-extensions' glibc floor, NOT the bundled node binary, which carries its own newer glibc requirement.)

**Recommended fix (needs COO/CTO ratification — runtime migration, not a layer swap):**
Migrate the Lambda to **`python3.11` or `python3.12`** runtime = **Amazon Linux 2023** (glibc **2.34**), which satisfies the Node 18 driver's glibc ≥2.28 requirement. Scope:
- `phase1-scraping-browser-lambda.tf` — Lambda module `runtime = "python3.12"` (from python3.9)
- Layer rebuilt for python3.12 path (`python/lib/python3.12/site-packages`) + `compatible_runtimes = ["python3.12"]`
- Bronze source is forward-compatible (Rule 15 `from __future__ import annotations` already present; runs on 3.12 unchanged)
- ~v0.6.2 or fold into a v0.7.0 runtime-bump; one more layer rebuild + safe-apply cycle (~10-15min)

**Alternatives considered + rejected:**
- Replace bundled node with an AL2-glibc-2.26-compatible node via `PLAYWRIGHT_NODEJS_PATH` → fiddly; Node ≥16 itself needs glibc 2.28; only Node 14 (glibc 2.17) qualifies but Playwright 1.40 driver requires Node ≥16. Dead end.
- Playwright Lambda container image → abandons the zip+layer model (CLAUDE.md deploy convention); much larger change. Defer unless runtime migration also fails.
- Downgrade Playwright to a node-14-era version (~1.20) → loses 20 minor versions of fixes + still risks glibc floor. Rejected.

**Tag posture:** `imo-pipeline-v0.6.1` HELD (not tagged) — would mark a still-non-functional release. Tag when E2E shows `pages_fetched=1`. Layer v2 is live regardless (driver-strip fix is a real forward step + reversible).

**Status:** rounded-trip to ws COO per §5(c) for runtime-migration GO before executing (runtime bump is more substantive than a content swap; ratification-worthy).

---

## §8 — RESOLVED: AC-T2 escape-valve FULLY FUNCTIONAL (v0.6.2 E2E green, 2026-05-28T~04:40Z)

ws COO GO `043503Z` authorized the scoped python3.12 migration. Executed + verified end-to-end.

**Applied (commits `b0039b778` source + `8969494ff` record-deploy; tag `imo-pipeline-v0.6.2`):**
- `build-layer.sh` PYTHON_VERSION 3.9→3.12; layer rebuilt 37MB, uploaded (sha `fl1xwyaRcyI...`)
- `layers.tf` browser-deps `compatible_runtimes = ["python3.12"]` (other 2 layers untouched)
- `phase1-scraping-browser-lambda.tf` `runtime = "python3.12"`
- `safe-apply tfplan.shipB.v062` clean → layer v3 + Lambda runtime change in-place; 0-diff verified; Lambda State Active / runtime python3.12

**E2E PROOF (Cambridge IR fixture, request `4b1a8d41`):**
```json
{"ok": true, "pages_fetched": 1, "pages_blocked": 0, "url_hash": "22e5b2ff093e080d",
 "final_url": "https://cir2login.b2clogin.com/login.cir2.com/B2C_1A_Signin_SAML/samlp/sso/login", "wait_ms": 18032}
```
- `pages_fetched=1` — the FIRST true end-to-end success: credential + driver + glibc + connect_over_cdp + navigate + JS render + redirect-follow + DOM serialize + S3 write all live
- S3 confirmed: `corp/cambridge-investment-research/bronze/web-scrape/2026-05-28/22e5b2ff093e080d.html` (87,886 bytes rendered DOM) + `.meta.json` (649 bytes)
- SLA: 18.0s render to networkidle / 18.7s total / 520ms cold init; **194 MB peak** (matches §3 steady-state projection ~200-400 MB; the 1024 MB allocation is still generous → A1 right-size candidate stands, defer to Stage 2 telemetry)
- Note: Cambridge IR redirects to an auth-gated B2C portal, so the rendered DOM is the login page — this proves the scraping_browser1 MECHANISM works; non-auth-gated SPAs will yield public content. That's a downstream silver/parse concern, not an AC-T2 infra concern.

**Three-defect cascade fully cleared:** credential-missing (.036 AC1) → driver-stripped (v0.6.1) → glibc-floor (v0.6.2). Each gate-clear surfaced the next masked defect — convergent verify-channel debugging, each fix real.

**Status:** FIND_INSURE.036 + AC-T2 escape-valve functional-readiness CLOSED. Tag `imo-pipeline-v0.6.2`.

— AE 0.7~B 2026-05-28T~04:25Z (§7 ~04:34Z; §8 RESOLVED ~04:42Z)
