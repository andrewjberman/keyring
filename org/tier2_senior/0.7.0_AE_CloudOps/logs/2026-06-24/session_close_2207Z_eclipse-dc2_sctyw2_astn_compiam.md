# Session Close 2207Z -- Eclipse DC2 FORK-B, SCTY.W2 remediation, ASTN_WSJFT, comp-iam Conditions

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DEPLOY, DIAGNOSE, COORDINATE

Serial: 0.7.0_AE_CloudOps (base). Window: since `session_oplmcp07-ac2_and_oplmcp05-r8_audit-lake.md`
-> 2026-06-24T22:07Z. ~45 commits, very high MCP traffic (continuous CTO/COO/CVO RAVC across 6
workstreams). Long multi-compaction session; this close covers the full window from the commit record.

## Workstreams (chronological-ish)

### 1. M365 gateway connect (OPLMCP, my lane) -- WORKING end-to-end
Andrew connected green for the first time + read live Outlook through it. The connect path had 4
config gaps surfaced (each hidden behind the prior): scope Read-vs-ReadWrite exactness (Sites.Read.All
was IT's actual consent, not ReadWrite -- 0.5.0 aligned 36f4a4d51; I landed the EC2_MANIFEST record
`0b1ac073a`), the /mcp trailing-slash redirect, the 421 host-allowlist. All config gaps, not arch.
I'm the MSTR-onboarding contact for per-user write-gating (blocklist.py enforce()).

### 2. SCTY.W2 own-attack-surface self-assessment + remediation (Andrew-direct via CVO)
- Self-assessment `89c3b6fa7`: read-only posture review vs the reverse-skill methodology catalog. 1
  CRITICAL (committed BD vendor cred, 4 files -- SEC-1, HELD per Andrew), 7 HIGH, MEDIUMs. HARD-SAFETY
  held (nothing executed, all content inert-data, read-only, zero changes, no secrets reproduced).
- Remediations (P1/P2, CVO-co-verified): SEC-2 `17655c193` (remove leaked-cred debug .mjs + scrub
  settings.local.json), SEC-3 `a1c1cbd02` (demo pw -> env), M365-1 `bdb82af6e` (loopback exact-host
  parse), M365-2 `e996f956b` (config.validate boot-guard vs unverified IDENTITY_PROVIDER), PORTAL-1
  `efdb9a8de`+`40512cf6b` (attach orphaned WAF to portal CF -> /auth/login rate-limited, ledger CLOSED).
- AWS-IMDS-1 `76d1d7ba1`+`b31e0a6c3` (bd-pipeline leg CLOSED): IMDSv2 enforced on all 7 bd EC2
  (http_tokens=required, hop-limit=1), safe-apply 0/7/0 in-place, live-verified. Remaining legs:
  inf/cot/mdpf/smartx per-firm-tree.
- Change-briefings `5d9f96d6f`+`e3dd5f3b9`: commit-by-commit remediation record for fabric-wide
  distribution; WITHDREW the bd-exporter TerminateInstances role-scope item (grounded ALREADY
  tag-scoped -- the broad framing was comp-iam's condition-blind view -> seeded workstream #6).

### 3. ASTN_WSJFT pipeline (S1-S4, ASTN_WSJFT macro)
- S1 `2644d523d`+`4d1339872`: opal-data-astn bucket + least-priv EC2 scraper role (SES pinned to
  opalinvest.dev). S2 `e0f7c24fb`+`90683814e`: AL2023 t3.medium SSM-managed scraper host (IMDSv2,
  encrypted, ephemeral-IP), manifest-registered. S3 FT `ba5afa030` (EC2-own-IP CF-403-blocked ->
  residential proxy required) + WSJ `62b7e3cad` (PROVEN: 18 articles via Web Unlocker -> S3). S4
  SES `5cbf7b71a`+`d7d214230` (FromAddress Condition fix -> EC2_SES_OK self-test). Go-live to
  austin@/cron = Andrew's separate gate-3.

### 4. Orion crawl DC1 BFS phase-2 (DATA_PLATFORM, lead) -- complete + certified
- BFS seam `bc9f3c38a` (discoverLinks, locators-only) + structural no-arbitrary-JS guard. The guard
  CAUGHT a real hole: vendored stealth/humanize.ts had 8 page.evaluate (active in prior certified
  runs) -> 0.5.0 rewrote evaluate-free (bf522fdba); I made the guard RECURSIVE `9c98518aa` +
  standalone pre-deploy gate `52fc3b37c` (W1 control, whole-src incl stealth/). BFS run `a95ddacaa`
  clean (0 new screens -- Orion is a hash-router, href-BFS no-op; Orion-class drill-grounding deferred).
  CVO/CTO/COO all PASS; the halt-property was certified-proven-live earlier in the session.

### 5. Eclipse vendor-2 DC2 (DATA_PLATFORM, lead) -- FORK-B SOLVED (the milestone)
- FORK-A `e463029ef` (Vendor union), FORK-C `c9ebd36ed` (SM read-source for the Eclipse JWT +
  least-priv IAM), the crawl path `df219bf61`. CTO isolation-PASS + CVO ROE-PASS; first crawl
  shell-only (header-auth insufficient) -> FORK-B = browser-session branch.
- FORK-B(b): the out-of-band Eclipse SESSION PARKER (`509a62357`->`4f56f641b`->`c7bc11945`). 5
  screenshot-diagnosed iterations: streamlined remembered-device login (autonomous, no OTP) ->
  authed Orion Connect -> Eclipse SSO authorize-login -> authed Eclipse dashboard (screenshot:
  Inflection Eclipse, 18 models/856 accts) -> PARKED eclipse/browser-profile/state.json. The crawl
  rides it read-only. Isolation held end-to-end; VERIFY-AFTER Orion crawl CLEAN (73 eps, no bump).
- Eclipse /v1 hash-route capture `59bd12805`: still shell-only -- the SPA renders shell not authed
  riding storageState (likely sessionStorage, which Playwright storageState doesn't capture).
  CTO-DEFERRED (220218Z): ground cookie-vs-sessionStorage first; if sessionStorage -> a vetted
  data-only injector (session-ride class), NOT now (ASTN-priority).

### 6. bd A_01 incremental flip (Andrew-direct via DS) -- deployed + verified
`316202d69`+`40268e2bb`: gold_dispatch.sh A_01 full->incremental (1 token, bd-only). AE-grounded the
safety basis myself (10-night parity, identical=True, bd argparse/cache confirmed) before deploying;
S3-deployed + re-pull byte-identical; deploy-completion ledger opened+closed. DS verifies served-SCD
unchanged on the next bd nightly -> then I retire the GLDINC shadow.

### 7. NFRA_COMPAWS.IAM-CONDITIONS (Andrew-direct, my comp-iam lane) -- investigated, proposed
comp-iam false-reads tag-scoped (Resource:* + Condition) grants as broad (it omits Condition).
Investigated: anchor = bd-exporter TerminateInstances (iam.tf:445-453, Resource:* + Condition
ec2:ResourceTag/ManagedBy). Mechanism: static census (cmpaws-iam-axis-census-20260603.json) bakes
overperm_flags ignoring Condition; iam_cli reconcile HAS the TF condition. Proposed a condition-aware
broad-classifier to CTO for arch-gate (key Q: which Condition keys count as scoping). Awaiting CTO.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-iam (iam_cli.py/extract_iam.py source) | trace the broad-vs-scoped FP for IAM-CONDITIONS | PASS -- root-caused (static census omits Condition) |
| no-arbitrary-js-guard (built) | structural observe-only enforcement, whole-src | PASS -- caught the humanize.ts evaluate hole |
| safe-apply (HALT-gate) | IMDS-1 (7 bd EC2), PORTAL-1 WAF, ASTN IAM, Eclipse/crawl IAM | PASS -- all in-place, 0-recreate, 0-diff post |
| comp-iam (the tool itself) | (the FP under repair) | the FP IS the workstream-6 fix target |

What worked: source-grounding IAM at the TF (Rule 22) caught comp-iam's condition-blind FP before it
drove a wrong scope-down (stopped ~B). The structural no-arbitrary-JS guard caught a live hole two
manual reviews + the live runs missed. What failed: comp-iam omits Condition (the IAM-CONDITIONS bug).
Gap found: Playwright storageState() doesn't capture sessionStorage -> the Eclipse authed-render-in-crawl
frontier (CTO-deferred, vetted-injector path).

## Blockers
None hard. Gated/awaiting (not blocked): comp-iam IAM-CONDITIONS impl awaits CTO's scoping-key
arch-gate; Eclipse /v1 CTO-deferred (ASTN-priority); ASTN go-live = Andrew gate-3; bd A_01 GLDINC
retire = DS next-nightly verdict.

## Current State (handoff)
- **Eclipse DC2**: FORK-B SOLVED. Parker = `infra/aws/ec2/inf-exporter/src/stepwise/eclipse_session_parker.ts`
  (runs on inf-exporter box i-081ae6aafb394fb1a, off-peak). Parked artifact = s3://opal-data-inf/
  eclipse/browser-profile/state.json (authed, 8 cookies). Crawl = runEclipseCrawlLive rides it +
  FORK-C JWT. Crawl instance i-010f195f1798b40ad STOPPED. /v1 capture = CTO-deferred (sessionStorage).
- **comp-iam IAM-CONDITIONS**: investigated; fix proposed to CTO (org/modules/graph/iam_cli.py reconcile,
  condition-aware broad-classifier). Awaiting CTO scoping-key ruling.
- **bd A_01**: deployed (gold_dispatch.sh:80 --incremental on s3://opal-data-bd/code/gold/). DS verifies
  next nightly. Then I retire the GLDINC A_01 shadow.
- **SCTY.W2**: bd IMDS-1 closed; inf/cot/mdpf/smartx IMDS legs remain. SEC-1 (BD cred) HELD per Andrew.
- All instances stopped; nothing half-landed; inf-pipeline fmt-churn cleaned (~B IMDS-1 unblocked).

## Next Steps
- [1.0.0_SA_CTO] arch-gate the comp-iam condition-scoping-key allow-list -> I implement IAM-CONDITIONS + RAVC.
- [0.4.0_DS_ClientPlatform] bd A_01 served-SCD-unchanged verdict on next nightly -> [0.7.0_AE_CloudOps] retire GLDINC shadow.
- [0.7.0_AE_CloudOps] Eclipse /v1: ground cookie-vs-sessionStorage when scoped (CTO-deferred); remaining IMDS legs (inf/cot/mdpf/smartx).
- [Andrew] ASTN_WSJFT go-live gate-3 (austin@/cron); SEC-1 BD-cred rotation decision.
