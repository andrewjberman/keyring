# 0.6.2_AE_PartnerETL — work log 2026-06-26 (session ~22:12Z->23:4xZ)

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, DIAGNOSE, VALIDATE, COORDINATE

## Session: startup + cot nightly pre-flight confirm (DS) + device-trust re-inject SHIP + BD long-term-token analysis + device-registration email reconcile

### Context
Fresh spawn (PID 32576) as Cottonwood's AE. /watcher armed persistent Monitor (task bgrb2x7t3); registered live. One inbox message at launch: DS (0.4.0) welcome + ask to confirm tonight's cot nightly runs two freshly-deployed COTMVP producer changes (D_03 composition_artifacts snapshot-first, D_04 client_portal_summary clients_tab), gated on the 02:00 UTC scheduled nightly (NEVER#4 no ad-hoc).

### 1. cot nightly pre-flight confirm (DS request) — GO delivered
- **(b) code staged CONFIRMED:** `comp-pipescript deployed --firm cot` -> D_03.composition_artifacts.py + D_04.client_portal_summary.py both MATCH at s3://opal-data-cot/code/gold/ (runner pulls there). Side-flag: cot_silver_merge.py STALE -> DS confirmed it's deliberately-HELD retry-net WIP (atomic pair-commit w/ 0.7.0 TF ~tomorrow-AM, CTO deploy-seq GO); hands-off tonight.
- **(a) nightly armed CONFIRMED:** eventbridge.tf cot-bd-session-daily = cron(0 2 UTC) ENABLED; full event-driven chain (session SSM Success -> bronze _BRONZE_COMPLETE.json -> silver silver_complete.json -> gold) all ENABLED.
- **(c) baseline captured:** gold/views/firm_composition.json + gold/artifacts/firm_mix_views.json ABSENT pre-run (expected — old D_03 hard-exited on empty holdings_lots). Today's 06-26 chain already ran midday (silver 09:45, gold ~11:12) on OLD code -> targets absent. Armed background verifier `bmayp5xj0` (exits on artifact-landing OR 05:30 UTC deadline -> no silent no-fire).
- **Reliability caveat surfaced:** bronze partitions 06-17..06-23, GAP 06-24/06-25, then off-schedule midday 06-26 -> aligns w/ 0.7.0's 06-25 cot-box->t3.large + debug-screenshot deploy. BD OIDC session-fetch ENTRY is the flaky stage.

### 2. Device-trust re-inject — SHIPPED (Andrew-direct)
Root cause (grounded): the auto-login .js (bd_49f_auto_login.js, 0.6.0's canonical) CAPTURES the bd_DeviceRegistration cookie to blackdiamond/cot/session AND has L3 re-inject code (reads process.env.BD_DEVICE_REGISTRATION), but **nothing exported that env** -> L3 was a no-op every run -> full OTP procural nightly. SM confirmed bd_device_registration present, captured_at 2026-06-26T15:44:01Z.
- **Fix:** infra/aws/ec2/bd-cot-auto-login/run-bd-auto-login.sh now sources bd_device_registration from blackdiamond/cot/session and exports BD_DEVICE_REGISTRATION before node. FAIL-SAFE (absent/SM-miss -> unset -> today's full-OTP behavior, no regression). No IAM change (box role already has GetSecretValue on session-*). cot-only, firm-sep clean.
- **Deploy (ledger cot-device-trust-reinject, all 4 legs CLOSED):** L1 git 61dc06e5d pushed CLOUD; L2 S3 ec2/bd-cot-auto-login/run-bd-auto-login.sh 3258B (md5 a10ac98a...); L3 box bake SSM 37cd0a62 -> BOX_MD5==committed; L4 dry-verify on box -> BD_DEVICE_REGISTRATION_WOULD_BE_SET len=28 (no login triggered). Box started briefly then STOPPED back to overnight-stopped. Coordinated 0.7.0 (CLEAR, complementary to their /otp/fetch) + FYI 0.6.0.

### 3. BD long-term-token analysis (Andrew Q: "why not just grab the token?")
Grounded via docs/briefs/cot-har-auth-api-first-analysis-20260608.md + live probes:
- **6h TTL claim FALSIFIED:** was a CVO-log inference, not measured. `.bd.identity` is opaque (not JWT), all 8 cookies session-scoped (expires=-1), no expires_at in bundle. Lambda session-check probe @23:08Z -> session_live=TRUE at +7.4h (past "6h"). TTL is server-side, unknown ceiling; idsrv = likely sliding session.
- **Long-term token path EXISTS but gated:** discovery doc (login.bdreporting.com/.well-known/openid-configuration) advertises password + refresh_token + client_credentials grants + offline_access. BUT dummy-cred ROPC probe -> HTTP 400 invalid_client (fails at CLIENT-auth layer; token_endpoint_auth_methods = client_secret_basic/post, no "none"). => direct-token grants need a CONFIDENTIAL client (client_id+secret) only Black Diamond can provision. Web client (BlackDiamond_Web, public/PKCE) + BFF pattern (refresh token held server-side) means no self-serve. Did NOT spend a real-cred attempt (same wall, lockout risk avoided). Andrew decision: stay on existing cookie-login strategy.

### 4. Device Registration Email reconcile (Andrew)
BD sends "Device Registration Email" (noreply@bdreporting.com) per login-that-registers-a-device. Three found: 06-24 22:32Z, 06-26 15:29Z, 06-26 15:43:40Z. The 15:43:40Z one = 21s before the 15:44:01Z SM token capture -> THE login that registered our EC2 (benign, our automation, as Andrew expected). KEY: repeated reg-emails + repeated OTPs = device-trust OTP-skip NOT active pre-fix (confirms the unwired re-inject). Tonight's run is the clean test: success = NO new OTP + NO new Device Registration Email after ~02:00Z.

## Compiler Tools
| Tool | Why | Result |
|---|---|---|
| comp-pipescript deployed --firm cot | AE min — verify D_03/D_04 code-MATCH at cot S3 (gate b) | PASS — both MATCH; flagged cot_silver_merge STALE (DS-confirmed held WIP) |
| comp-iam service cot-exporter | confirm box role SM access before wiring SM-read into wrapper | PASS — GetSecretValue+PutSecretValue on blackdiamond/cot/session-* already present, no IAM change |
| comp-freshness (chain/--list) | attempted cot served-artifact freshness | GAP — comp-freshness models bd+inf only; cot (NFRA_DTAFLP separate firm) not covered -> fell back to rail-checked aws s3 ls |
| comp-grep / comp-glob | locate auto-login system files + eventbridge schedule | PASS — found bd-cot-auto-login dir, eventbridge cron(0 2), ssm docs |
| comp-which | route "cot bd session token fetcher" | PARTIAL — collided on "registration" (broker); fell back to comp-glob/grep |

**What worked:** comp-pipescript deployed --firm cot gave the decisive code-MATCH gate with firm attribution; comp-iam confirmed no IAM change needed before the deploy. **Gap:** comp-freshness has no cot coverage (bd+inf only) — cot served-artifact freshness has no comp-tool; logged rail-checked aws s3 ls. Heavy operational aws (s3/ssm/lambda/secretsmanager) + m365 email reconcile were off-rail by design (no comp-tool drives a live SM/SSM/OIDC/email probe).

## Blockers
None. Device-trust re-inject SHIPPED + verified on box. Long-term-token = blocked on BD provisioning a confidential API client (vendor action, Andrew-owned; decision = stay on cookie-login for now). cot nightly = scheduled external gate (02:00 UTC), auto-verifier armed.

## Current State (handoff)
- **Device-trust re-inject LIVE on box:** /opt/bd-cot-auto-login/run-bd-auto-login.sh (committed 61dc06e5d, baked md5 a10ac98a...) sources bd_device_registration from blackdiamond/cot/session -> exports BD_DEVICE_REGISTRATION -> .js L3 injects pre-login. Box i-0643a5bee8a8feabf STOPPED (nightly Lambda starts it at 02:00 UTC).
- **Background verifier bmayp5xj0** running: polls firm_composition.json + firm_mix_views.json; fires SUCCESS on landing or TIMEOUT at ~05:30 UTC.
- **Tonight's 02:00 UTC nightly tests BOTH:** (1) DS D_03/D_04 artifact delivery, (2) device-trust OTP-skip (success = no new OTP/Device-Registration email post-02:00Z).
- **BD auth facts banked:** session opaque/server-TTL (alive >7.4h, ceiling unknown); direct-token grants need a BD-issued confidential client (invalid_client wall); BFF keeps refresh token server-side.

## Next Steps
- **[0.6.2 self]** On bmayp5xj0 fire (~03:00-05:30 UTC): verify D_03/D_04 artifacts + pull session-fetch log (s3://opal-data-cot/logs/cot-exporter/session-fetch/) + check mailbox for new OTP/Device-Registration email -> report device-trust OTP-skip verdict to DS + Andrew.
- **[0.4.0_DS]** awaiting the post-nightly delivery verdict (verifier relays).
- **[Andrew]** optional: request a BD/SS&C confidential API client (client_credentials) for the durable no-login path — only vendor action that unlocks the long-term token.

## MCP traffic
~6 messages: DS welcome (acted), 2x DS pre-flight ACK/close + 1 DS hands-off-silver ack, 0.7.0 coordination (CLEAR reply), 0.6.0 FYI.
