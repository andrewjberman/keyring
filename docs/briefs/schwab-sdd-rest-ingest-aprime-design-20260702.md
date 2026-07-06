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

**STRUCTURAL DECISION for the CTO (my README bar — I do not decide IAM-management-model unilaterally):**
`quartz-si2-spike-role` + `-profile` are HAND-MADE, NOT Terraform-managed (comp-iam `service
canonical-schwab` surfaces only `canonical-schwab-{runner,automation-start,events-invoke-ssm}` roles;
the spike role is absent). Per CLAUDE.md "Terraform manages EC2 infra," landing the DenyPlane in TF
means either **(A, recommended)** import/adopt `quartz-si2-spike-role` into the `canonical-schwab-ec2`
module + add the DenyPlane there (clean productionization), or **(B)** a NEW TF-managed `schwab-ingest`
role the REST ingest assumes, leaving the spike role for SI2-download only. Statements are identical
either way; only the attachment target differs. **Staged-for-gate; no apply until CTO arch-signs +
COO/CTO RAVC (arch-gate binding, §6a/§6b). No live SDD REST call regardless until CTO has seen the
capturer + the liveness alarm (§6b).**
