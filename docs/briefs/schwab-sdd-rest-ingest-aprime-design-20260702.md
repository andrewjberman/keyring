# Schwab SDD REST Ingest — A-PRIME DESIGN (arch-gate draft; NO live REST call until CTO-signed)

**Author:** 0.6.2_AE_PartnerETL (lead) | **Date:** 2026-07-02 | **Project:** ADVI_SCHWABAUTO (finish-the-box)
**Status:** DESIGN for CTO ARCH-GATE. Andrew-ratified mechanism. **ROE: mechanism-not-values; NO live SDDServices call until CTO arch-signs this design.**
**RAVC:** CTO (arch-gate the REST-ingest + session-auth-replay) + MSTR (auth-replay confirm + milestones) + COO. Reuse coordinated with 0.6.0 (bd REST-pull) + 0.7.0 (OAuth-gateway + liveness alarm).

## 1. Mechanism (Andrew-ratified 2026-07-02)
Andrew: *"it's already authenticated on that machine so you absolutely should use the rest backend on automation."*
The SI2 desktop app is a GUI wrapper over a REST backend (`REST_SI2Desktop = https://si2.schwabinstitutional.com/fileservices/SDDServices/`; auth = OAuth via the Schwab **LMS SSO gateway** `sws-gateway.schwab.com`, `LMS_ClientId=SDD`, `LMS_Redirect=sdd.schwab.com`, + Windows Credential Manager). **RIDE the box's STANDING authenticated SI2 session → call SDDServices REST directly** (list + download by date/type/master), no re-login/MFA/OTP/GUI. Same live-session-REST pattern as 0.6.0's bd `.bd.identity` fix. This SUPERSEDES the unviable GUI-driver AND Option-B sole-client (no sovereign gate). *Why the pivot: Rule-22a exercise proved the SI2 GUI is UIAutomation-opaque for data entry; the non-GUI + auth spikes found this robust path.*

## 2. Ingest design (cloning 0.6.0's cot_bronze_ingest.py — reuse-not-rederive)
**2.1 CAPTURE (decoupled 2-process; ingest NEVER touches the live app directly):**
- A box-side CAPTURER reads the live SDD auth material (Windows Cred Manager / the app's in-memory OAuth token) → writes a JSON blob to Secrets Manager `schwab/sdd/session`: `{sdd_cookies:[FULL JAR], oauth_access_token, refresh_token, captured_at, expires_at}`.
- **FULL-AUTH-JAR (0.6.0 gotcha, cot_bronze_ingest.py:167-181):** grab the WHOLE SDD auth context (all cookies + the OAuth bearer), NOT just the token — a partial jar silently 401s only on the write/execute path (worst place to discover it).
- **STEAL F1 (hung-socket 30s timeout on the capture) + F2 (SM-persist failure → rc=1 LOUD)** — the two silent-death modes of this pattern.

**2.2 REST INGEST (`schwab_sdd_ingest.py`, cloning run()/ingest_table()/_window_for()/emit_bronze_sentinel()):**
- `load_schwab_session()` reads SM → auth headers on every SDDServices call. LIST files (by date/type/master 08242234) → DOWNLOAD the expected set (incl the MDPF-critical RPS) → land `s3://opal-data-schwab/01_raw_quartz_validation/` (validation prefix; repoint stays N=5-held). Idempotent (`_already_landed` head_object skip). Emit a bronze-complete sentinel → the silver-merge S3-event wire (clone `bd-silver-merge.tf` + `s3-notifications.tf` BronzeCompleteSilverMerge).
- **CONTENTION-FREE:** a direct REST fetch by date/type doesn't consume the GUI "new files" flag → both clients (box REST + Andrew's manual desktop) co-run, no starvation. (Resolves the root-cause contention WITHOUT Andrew's manual-pull cessation.)

**2.3 OAUTH-REFRESH ADVANTAGE (schwab > bd — 0.6.0):** SDD is real OAuth (client_id=SDD, refresh_token via sws-gateway). On 401 → REFRESH the access_token + retry ONCE before re-driving full SSO; persist `expires_at`, pre-emptive refresh ~T-5min. Do NOT inherit bd's wholesale re-mint (bd had no refresh; we do).

## 3. Firm-separation (2-layer, fail-closed — 0.6.0's pattern, schwab-scoped; NEVER#1 binding)
- **APP-GUARD:** `_assert_firm_separation()` reads `os.environ` DIRECTLY (no module default → detects UNSET). Require `SCHWAB_S3_BUCKET=opal-data-schwab` EXPLICIT; ABORT if unset OR == any other firm's bucket (opal-data-bd / opal-data-cot).
- **IAM EXPLICIT-DENY:** on the schwab box/ingest role, `Deny s3:* on other firms' buckets` (clone 0.6.0's `bd-silver-merge.tf:75-83` DenyCotPlane → add `DenyBdPlane` + `DenyCotPlane` for the schwab role).
- **AUTH FIRM-SEP (Andrew-binding):** reuse the bd TECHNIQUE only; the schwab auth (creds/session/token/box/secrets) is entirely separate, `schwab/*` SM-scoped, NEVER bd's.

## 4. Session-liveness fail-LOUD alarm (WS-4-class — 0.7.0's bd pattern; the standing-auth is a single-point-of-freshness)
- **ACTIVE PROBE (primary):** a keepalive Lambda `rate(15m)` → a lightweight AUTHENTICATED SDDServices probe → 401/403 = session dead → DIRECT SNS to the pager topic. READ-ONLY on the session secret (no version churn) + publishes STRAIGHT to SNS (delivery-INDEPENDENT of the session it watches — a drop can't kill its own pager).
- **ABSENCE BELTS** (`treat_missing_data=breaching`): authtoken-absence (verifier died) + keepalive-absence (probe stopped) + `schwab-silver-stale-{table}` (ingest output didn't land = downstream freshness).
- **PENDINGCONFIRMATION SAFEGUARD (0.7.0 live-caught gotcha — critical):** an SNS topic with 0 CONFIRMED subs = silent-freeze (the exact class the alarm exists to catch). (a) deploy-check ASSERTS `SubscriptionArn != "PendingConfirmation"` (a real ARN) — a created-but-unconfirmed sub is a FALSE-GREEN → FAIL the deploy. (b) use an AUTO-CONFIRMING delivery (Lambda→pager/Slack or a pre-confirmed ops channel), NOT a personal-email sub that silently expires in 3 days.
- **SEQUENCE:** liveness alarm FIRST (a drop MUST page), THEN the headless re-mint as automated recovery.

## 5. Fallback: headless SI2-session re-mint (0.7.0's bd auto-login technique — only if riding the standing session proves insufficient long-term)
Headless Playwright+Chromium driving the LMS-gateway OAuth flow (CV Kimi-VL + the DOM-fallback classifier, INCLUDING the F1/F2 hardening) + a pluggable OTP/MFA seam → fresh session → SM. **PRE-BUILD GROUND:** does Schwab block AWS-datacenter egress (bd forces resi-proxy always-on)? Check before committing the re-mint transport. Riding the standing session (Andrew's directive) is primary; this is the drop-recovery fallback.

## 6. Guardrails (binding) + build sequence
- CTO ARCH-GATE this design + the auth-replay mechanism BEFORE any live SDDServices call (ROE: mechanism-not-values until gated).
- prod bd→schwab REPOINT stays Caution-B N=5-gated (MSTR-settled: respect N=5, no acceleration). This ingest lands the VALIDATION prefix; the repoint is a separate sovereign step.
- Ledger every box-state change (NO-HALF-DEPLOYS). Firm-sep binding throughout.
- **SEQUENCE:** (0) CTO arch-gate → (1) capturer (SM blob, full jar, F1/F2) → (2) **liveness alarm FIRST** → (3) ingest (`schwab_sdd_ingest.py`, list/download/land-validation/sentinel, firm-sep 2-layer, OAuth-refresh) → (4) bronze→silver wire → (5) exercise-confirm: prove a REST fetch of a KNOWN date (the missing 06-30 RPS = prove-and-recover) lands via REST → RAVC CTO+MSTR → (6) daily-cycle wiring. Repoint remains N=5+never-widen+Andrew-gated (LEG-5, untouched).

## 6b. CTO ARCH-GATE CONDITIONS (approved da995bf56 2026-07-02T231837Z — BOUND into the build)
- **Exercise-confirm gates reliance:** a LIVE SDD REST fetch of the missing 06-30 RPS (prove-and-recover) must PASS before ANY production ingest. NO live SDD REST call until CTO has SEEN the capturer + the alarm.
- **SM blob:** KMS-encrypted + scoped `schwab/sdd/session`.
- **Firm-sep UNCONDITIONALLY fail-closed:** app-guard ABORTs if `SCHWAB_S3_BUCKET` unset OR cross-firm (no default, no proceed-on-unset); IAM DenyPlane explicitly Denies bd AND cot AND inf buckets.
- **SDD surface least-privilege:** only list-by-date/type/master + download, scoped to 08242234; no broader SDD API.
- **Liveness alarm → the OPS CHANNEL** (Andrew's this-session ruling; COO names it), NOT personal email. PendingConfirmation safeguard kept. Alarm built + verified-DELIVERING (confirmed-sub) BEFORE any standing-session/re-mint reliance.

## 6c. FOLDED SCOPE — CVO schwab-dependency baseline (COO 231431Z; CVO verifies at arch-gate)
- **ULT (grounded verdict 2026-07-02):** `schwab/silver/ult` is LIVE-CONSUMED (14 gold + 2 lambda consumers; gated freshness input `warn_age_hours=36`, scripts:[B_02.canonical_lots]), NOT dormant. 85d-frozen = the ult silver converter isn't run daily (uln/rld are via /49-schwab-conv; ult is not). Impact = bounded served-QUALITY staleness (B_02 lot-cost-basis 85d-stale; NOT gross AUA — WARN-gate + fallback profile masks it). **A-prime re-point MUST wire `convert_schwab_lots_to_silver.py ult` (mode 3) into the daily cycle** (raw CRS*.ULT is box-fed) → silver/ult un-freezes.
- **Two-namespace consolidation:** `opal-data-schwab/silver/RPS|ULN` (uppercase, box-fed SI2 raw) vs `opal-data-bd/schwab/silver/rps|uln|rld|ult` (lowercase, bd silver) → the re-point consolidates onto the box-fed path. Fold into the re-point design; CVO verifies.

## 7. Prereqs already resolved (stand regardless)
S3→box code-deploy IAM path (SchwabOpsCodeRead, applied+verified, tag canonical-schwab-ec2-v1.0.0) · console-session task pattern · daily-bridge design · the parity/completeness discipline. Only "how the box gets a complete set" changed: GUI-download → SDD REST.

## 8. PREREQ-A LIVE-GROUNDED + firm-sep DenyPlane draft (0.6.2, 2026-07-06 — for the CTO IAM gate)

**PREREQ-A (S3→box code-deploy path) = RESOLVED, live-confirmed 2026-07-06** (Rule 22a, IAM grounded
on live `get-role-policy`, NOT the comp-iam DESIRED view — the role is not TF-managed so DESIRED can't
see it). SI2 box `i-0f3d57a97f14727af` (`quartz-si2-spike`, running) → instance-profile
`quartz-si2-spike-profile` → role `quartz-si2-spike-role`, inline `quartz-si2-spike-inline` grants:
- `s3:GetObject` on `opal-data-schwab/_ops/canonical-schwab-si2/*`  ← the code-deploy path EXISTS.
- `s3:ListBucket` on `opal-data-schwab`; `s3:PutObject` on `01_raw/*` + `01_raw_quartz_validation/*`.
- `secretsmanager:{GetSecretValue,PutSecretValue}` on `schwab/*`  ← covers the capturer's
  `schwab/sdd/session` write + the ingest's read (§2.1/§2.2). (§6b least-privilege refinement: could
  scope to `schwab/sdd/*`, non-blocking.)

The ADVI_SCHWABAUTO TO's "grants ONLY ListBucket+PutObject, NO GetObject" premise is STALE (07-02;
GetObject added since, matching §7). **No GetObject TF to author — that would be redundant.**

**REAL OPEN IAM (arch-gate §6b requires; NOT present today):** the explicit firm-sep DenyPlane. The
role is Allow-only/schwab-scoped (no cross-firm Allow ⇒ no leak today), but §6b mandates the explicit
Deny belt. Draft (clone of `infra/aws/terraform/bd-pipeline/bd-silver-merge.tf:74-83` `DenyCotPlane`,
extended to bd+cot+inf — A/B-agnostic, identical statements whichever role it attaches to):

```hcl
# FIRM-SEP belt (NEVER#1): the schwab ingest role can NEVER touch another firm's plane. Explicit Deny wins.
{ Sid = "DenyBdPlane",  Effect = "Deny", Action = ["s3:*"],
  Resource = ["arn:aws:s3:::opal-data-bd",  "arn:aws:s3:::opal-data-bd/*"]  },
{ Sid = "DenyCotPlane", Effect = "Deny", Action = ["s3:*"],
  Resource = ["arn:aws:s3:::opal-data-cot", "arn:aws:s3:::opal-data-cot/*"] },
{ Sid = "DenyInfPlane", Effect = "Deny", Action = ["s3:*"],
  Resource = ["arn:aws:s3:::opal-data-inf", "arn:aws:s3:::opal-data-inf/*"] }
```

**GROUNDING CORRECTION (0.6.2, 2026-07-06 — supersedes an earlier wrong claim in this section + the
now-deleted DenyPlane .tf.draft + CTO 135619Z Gate-1's "Option A import" premise):** I earlier claimed
`quartz-si2-spike-role` is HAND-MADE / non-TF (→ needs an "Option A vs B" import). That was WRONG, from
two errors both falsified by grounding on `terraform state` + `plan`:
1. comp-iam `service canonical-schwab` missed it because its `tf_resource` is `schwab_si2` (query matched
   the `canonical-schwab-*` name prefix). The role IS TF-managed in `infra/aws/terraform/canonical-schwab-ec2/iam.tf`
   (0.6.0's DATA_SSOTMG.CUTOVER-1), ALREADY IMPORTED (`terraform state list` shows `aws_iam_role.schwab_si2`,
   `schwab_si2_inline`, the instance-profile + the SSM attachment all in state).
2. My "live has no Sids / no ListBucket prefix-condition" (the supposed live-vs-TF drift) was a JMESPATH
   PROJECTION ARTIFACT — `get-role-policy --query 'Statement[].{Effect,Action,Resource}'` dropped the
   Sid+Condition fields. They ARE present live. Proof: `terraform plan` (pre-edit) = "No changes.
   Your infrastructure matches the configuration." The module is CLEAN.

**CORRECTED GATE-1 (no import, no A/B):** the §6b DenyPlane is a 3-statement ADDITION to the existing
`aws_iam_role_policy.schwab_si2_inline` in `iam.tf` (append the DenyBd/Cot/Inf statements above, verbatim).
PROVEN zero-churn (added the 3, ran plan, restored iam.tf pristine): `Plan: 0 to add, 1 to change, 0 to
destroy` — the ONLY change is `schwab_si2_inline` gaining the 3 Deny statements; every existing Allow
(SchwabRawList/Write/OpsCodeRead/Secrets) UNCHANGED. Never-widen-safe (a Deny only narrows). CROSS-DOMAIN:
`iam.tf` is 0.6.0's file (CUTOVER-1) — coordinate the addition with 0.6.0. **No apply until CTO re-confirms
the corrected approach + 0.6.0 nods; then commit + safe-apply (HALT-gated) + ledger + post-apply confirm
the DenyPlane on live get-role-policy (without projecting fields away). No live SDD REST call regardless
until CTO has seen the capturer + the liveness alarm (§6b).**

## 9. GATE-3 RECON RESULT (0.6.2, 2026-07-07 — CTO ROE-nod'd: read-only, location/key/format, no
session perturbation, SSM S3->box console-session pattern N/A here since this was direct read-only
SSM against the running box, no schtasks/interactive-session touch)

**Objective:** locate the live SDD auth material (§2.1's "Windows Cred Manager / the app's in-memory
OAuth token") so the Gate-2 capturer knows exactly what to read.

**FINDING — Windows Credential Manager is NOT the location.** `cmdkey /list` on the box (Administrator
console, the account SI2 runs as) shows exactly one generic entry (`WindowsLive:target=virtualapp/didlogical`,
unrelated — a Windows/MSA artifact, not Schwab). The §2.1 design language anticipating Cred Manager was
a reasonable guess pre-recon; it's wrong. **Rescope the capturer away from Cred Manager entirely.**

**ACTUAL LOCATION — SI2Desktop.Container embeds a WebView2 (Chromium) control** and the LMS-gateway SSO
flow (`sws-gateway.schwab.com`) runs inside it. Standard Chromium profile at:
```
C:\Users\Administrator\AppData\Local\Apps\2.0\AJ358CTY.E5K\BP9BJTJZ.6BX\
  schw..tion_2227d0d3394dbd7e_001a.0004_3c191691c3bd481c\
  Schwab.SI.SI2Desktop.Container.exe.WebView2\EBWebView\Default\
```
Two concrete capturer targets identified (existence/format only — contents NOT read, staying inside the
ROE bound; no live-session-material access before CTO sees the capturer per §6b):
1. **`Cookies`** (SQLite, ~20KB, last-write tracks live app activity) — the standard Chromium cookie jar;
   this is the §2.1 "FULL-AUTH-JAR" target (all cookies, not just one token). Chromium cookies are
   DPAPI-encrypted at rest under the OS user profile — the capturer will need to decrypt in-process
   (as the same Windows user SI2 runs as, via `CryptUnprotectData`/the Chromium `os_crypt` key in
   `Local State`), not just copy the file.
2. **`Local Storage\leveldb\*.log`** (leveldb KV store, actively written — newest entry 6/29 5:49:48PM
   PM, same session window as the Cookies file) — the likely OAuth access_token/refresh_token
   persistence point (standard pattern for browser-hosted OAuth SPA flows, e.g. MSAL.js/oidc-client
   using localStorage). `Session Storage` also has a fresh entry (5:52:14PM) — check both; sessionStorage
   is ephemeral-per-tab so Local Storage is the more durable candidate for what survives a capturer
   read between app restarts.
3. `Login Data` (Chromium saved-passwords store) also present but likely irrelevant — SI2 auth is SSO,
   not a saved-password autofill; not pursuing unless the other two prove insufficient.

**NOT pursued (deliberately, ROE-bound):** did not open/query the Cookies SQLite DB, did not read the
leveldb log contents, did not attempt DPAPI decryption. This recon establishes WHERE + WHAT FORMAT, not
the actual live session material — that's Gate-2 capturer-build territory, gated on CTO seeing the
capturer + liveness alarm per §6b.

**Gate-2 capturer implication:** the capturer needs (a) SQLite read + DPAPI/os_crypt decrypt for
`Cookies`, (b) a leveldb reader (or shell out to a small Go/Python leveldb lib) for `Local Storage`,
run as/impersonating the same Windows Administrator console-session user SI2 runs as (DPAPI keys are
per-user). This is a different (more standard, well-precedented — Chromium cookie/localStorage
extraction is a common, well-documented pattern) build than the Cred-Manager assumption in §2.1 — likely
SIMPLER, since there are mature libraries for both SQLite-Chromium-cookie and leveldb reads, vs. the
undocumented Cred Manager blob format that would have been needed otherwise.
