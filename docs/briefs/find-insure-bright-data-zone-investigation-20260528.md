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

---

## §9 — CVO Mode A independent verify + scope-boundary finding (2026-05-28T~05:18Z)

CVO independently verified the v0.6.2 E2E (verdict `3ced0c99e`) by reading the S3 artifact directly (not my self-report): EXISTS + FRESH (04:40:27Z) + SCALED (87KB rendered where direct-fetch hit empty-body) + NOT-FROZEN (content_hash a7247929167c170a). **Mechanical axis PASS confirmed independently.** Meaning axis flagged CONCERN/UNTESTED — two distinct things separated:

**(a) Render-mechanism PROVEN vs signal-extraction UNTESTED.** Cambridge IR's content probe is login-wall-dominated (b2clogin×30, password×36, SAML×4); the "ria"×23 hits are substring noise in a login-portal context, not genuine RIA signal. For Cambridge IR this is CORRECT (its public surface IS the login wall) — but it proves the escape-valve RENDERS, not that it EXTRACTS scoreable AM content. The non-auth-SPA signal-extraction probe is the right confirmation step.

- **Disposition:** the natural fixture is the **Stage 2 universe-run empty-body subset** (actual IMOs that hit SPA-render-failure across the 99-IMO run) — the P2 validation subset has `empty_body_rate=0.0` (no current public-SPA fixture), and Stage 2 is held on the W1-revision. Running a synthetic guessed fixture now would be make-work; the real meaning-axis proof folds into **A3 (AC-T2 first-fire empirical capture)** at Stage 2 first-empty-body-IMO. Committed to run it then.

**(b) Scope-boundary — auth-gated-SPA is a structural unrecoverable-signal tail (distinct from render-failure).** AC-T2 fixes the **public-JS-SPA-render-failure** class (content exists publicly, needs JS render). It CANNOT fix the **auth-gated-SPA** class (no public content; signal sits behind login). Cambridge IR is the latter — the escape-valve "succeeds" mechanically (renders the login wall) but recovers no signal. This is a distinct known-tail, analogous to BLOCKED-ROBOTS (→ per-IMO Andrew sign-off §9 Q5).
- **Recommendation (DS scoring lane):** auth-gated SPAs map to `wm_classification=null (reason: auth-gated-no-public-content)`, NOT escape-valve-success-as-if-signal-recovered.
- **Tokenizer correctness risk (DS~B `score_web_gold.py`):** the token matcher must use **word-boundary matching** for terms like "ria", NOT substring — else auth-gated login walls (23 "ria" substrings in the Cambridge probe) accrue spurious RIA signal. Routed to DS~B via ws COO.

Neither (a) nor (b) is a Stage-2 gate (AC-T2 = acquisition-failure remediation, separate from W1-classification). AC-T2 closure stands; these refine the downstream signal-extraction + classification path.

---

## §10 — Non-auth-SPA signal-extraction probe (ws COO DRIVE 045320Z) — render PROVEN, wait-strategy BLOCKS extraction (v0.3.1 fix needed)

COO GO'd a pre-universe-burn probe to confirm the escape-valve extracts scoreable content, not just renders. Ran 3 fixtures; all 3 confound the signal proof but collectively surface **3 real robustness findings + 1 upstream classifier finding** — exactly the de-risk the probe was for.

| Fixture | Class | Result | Finding |
|---|---|---|---|
| Cambridge IR (`cir2.com`) | auth-gated | pages_fetched=1, 87KB DOM = **login wall** | render mechanism PROVEN; no public AM signal (auth-gated tail per §9) |
| Carl Ostenson (`carlostenson.com`) | "empty-body" anchor | `ERR_CERT_COMMON_NAME_INVALID` | **F4: empty-body MISCLASSIFICATION** — see below |
| Wealthfront / Fisher Investments (public AM SPAs) | content-rich | `Timeout 30000ms exceeded` (both) | **F2: networkidle + fail-on-timeout discards rendered DOM** |

### F2 (HIGH) — `networkidle` + fail-on-timeout is the signal-extraction blocker
Both content-rich public AM SPAs timed out: `WAIT_UNTIL=networkidle` waits for ≤2 connections for 500ms, which content-rich sites (analytics, chat widgets, tracking pixels, polling) **never reach within 30s**. Worse, `fetch_rendered_html` **raises on nav-timeout (L164-167) and discards the page** — but the DOM was almost certainly fully rendered; only background network kept firing. As-deployed, the escape-valve would FAIL on the majority of real SPA-render-failure tail-IMOs in Stage 2 (the recoverable class it exists for). The render works; the capture is thrown away.

### F3 (MED) — no `ignore_https_errors`
Playwright enforces cert validation; sites with cert issues fail (`ERR_CERT_COMMON_NAME_INVALID`). Small advisor IMO sites on shared hosting frequently have cert misconfigs. Policy call: recover misconfigured-but-live sites? (N/A for Carl Ostenson — it's parked.)

### F4 (HIGH, upstream — DS classifier lane) — empty-body class conflates cert-failure + parked with true JS-SPA
Carl Ostenson's "empty-body" classification was a **Bright Data cert-502 surfaced as HTTP-200-empty** (one_shotter bronze meta: `x-brd-error-code: net_err_cert_common_name_invalid`, `x-brd-status-code: 502`). The domain is parked (serves a 404, `CN=*.hostgator.com`). So the empty-body acquisition-failure class is **impure** — it conflates (a) JS-SPA-render-failure [AC-T2-recoverable], (b) cert-failure [unrecoverable], (c) parked/404 [unrecoverable]. AC-T2's value applies only to (a). The classifier should split these (the `x-brd-error*` headers are the discriminant) so Stage-2 escape-valve fires target true SPAs, not cert/parked noise.

### Recommended v0.3.1 (escape-valve bronze script — my lane, GO-asked)
- **R1 (highest):** catch nav-timeout → if `page.content()` has a rendered body, **capture it as degraded-success** with a `wait_timeout_exceeded:true` meta flag, instead of discarding. Never throw away a rendered DOM.
- **R2:** `WAIT_UNTIL` default `networkidle` → `domcontentloaded` + `EXTRA_WAIT_MS` 0 → ~3000 (canonical SPA-settle pattern), with R1 as the safety net.
- **R3:** `ignore_https_errors=True` policy decision (recover misconfigured-live sites).
- **R4 (DS classifier lane, route to DS~B):** empty-body classifier splits cert-failure (`x-brd-error*` present) + parked/404 from true JS-SPA-empty-body.

Render mechanism (v0.6.2) stands fully proven; these are wait/cert capture-robustness refinements for actual Stage-2 effectiveness. GO-asked ws COO for the v0.3.1 escape-valve fix (R1+R2+R3); R4 routed to DS~B.

---

## §11 — v0.3.1 capture-robustness RESOLVED: signal-extraction PROVEN (tag v0.6.3, ~05:10Z)

ws COO GO `050405Z` authorized R1+R2+R3. Implemented + applied + re-probed.

**Shipped (commits `59c92b7be` source + `1c08b505e` artifact + `0cdcefa3c` record-deploy; tag `imo-pipeline-v0.6.3`):**
- **R1** (`crawl_web_scraping_browser_bronze.py`): catch `PlaywrightTimeoutError` on `goto` → capture rendered DOM as degraded-success with `wait_timeout_exceeded:true` meta, instead of raising/discarding. Hard nav errors (cert/connect) still raise. Threaded the flag through `write_page` meta + summary.
- **R2** (`phase1-scraping-browser-lambda.tf` env): `WAIT_UNTIL` networkidle→domcontentloaded + `EXTRA_WAIT_MS` 0→3000 (SPA-settle).
- **R3** (bronze script): `browser.new_context(ignore_https_errors=True)`.
- Rule 14 gate clean; Rule 2 commit-before-apply; safe-apply 0-diff verified; Lambda in-place update (code hash + 2 env vars).

**SIGNAL-EXTRACTION PROOF (re-probe of the two fixtures that timed out at v0.3.0):**

| Fixture | v0.3.0 | v0.3.1 | Rendered content (word-boundary AM-signal hits) |
|---|---|---|---|
| Wealthfront | `Timeout 30000ms` | **pages_fetched=1**, 2.46MB / 21,465 text chars, 13.3s, `wait_timeout_exceeded=False` | wealth×82, invest×57, account×38, portfolio×14, advisor×9, fees×4, financial×4, planning×4 |
| Fisher Investments | `Timeout 30000ms` | **pages_fetched=1**, 302KB / 13,351 text chars, 16.2s, `wait_timeout_exceeded=False` | invest×74, wealth×21, financial×14, portfolio×12, planning×7, retirement×5, fees×3 |

R2 (domcontentloaded+3s) fixed the timeout cleanly — both rendered without needing R1's capture-on-timeout fallback (`wait_timeout_exceeded=False`). The escape-valve now delivers **usable, scoreable public AM content** — not just a rendered page. This closes the meaning-axis CVO flagged in §9/`3ced0c99e`: render-mechanism AND signal-extraction both proven.

**Test-pollution note:** the probe wrote test slugs under `corp/` (`_control-*`, `_reprobe-*`, underscore-prefixed). Harmless — they don't match real IMO slugs in Stage 2. S3-delete is a sandbox-gated destructive op (Andrew-direct only per [[feedback_destructive_op_peer_auth_insufficient_sandbox_gate]]); left in place, flagged for natural cleanup.

**AC-T2 escape-valve = FULLY CLOSED** (render v0.6.2 + signal-extraction v0.6.3). F4 (empty-body classifier cert/parked/SPA split) routed by COO to AE 0.7 base (one_shotter `crawl_web_bronze.py` lane).

— AE 0.7~B 2026-05-28T~04:25Z (§7 ~04:34Z; §8 ~04:42Z; §9 ~04:52Z; §10 ~05:00Z; §11 RESOLVED ~05:10Z)
