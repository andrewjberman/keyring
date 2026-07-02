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

## 7. Prereqs already resolved (stand regardless)
S3→box code-deploy IAM path (SchwabOpsCodeRead, applied+verified, tag canonical-schwab-ec2-v1.0.0) · console-session task pattern · daily-bridge design · the parity/completeness discipline. Only "how the box gets a complete set" changed: GUI-download → SDD REST.
