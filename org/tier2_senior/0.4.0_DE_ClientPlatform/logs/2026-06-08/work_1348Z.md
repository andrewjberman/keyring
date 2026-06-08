# 0.4.0_DE_ClientPlatform — Session Log 2026-06-08 (~1330Z–1350Z)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE

**Role:** Tier-2 DE COO bring-up per LD-0165 — /frontend-dev visual-smoke gate for two near-close
projects (MDLP_DISTFIX distribution surfaces + MDPF_COUNTS Account Trend count toggles) + confirm
the MDPF Global-COUNT-path FE re-point live-build status. Andrew chose /frontend-dev for these gates.

**Outcome (one line):** Cleared the 6/05 JWT auth wall (real-token login via vite proxy) and
VISUAL-GATED both Model-Portfolios halves GREEN on live data (6/08 11:30Z): DISTFIX bell curve
dust-floored $1K (P10 $7.99K, no $8.42 dust) + MDPF_COUNTS Count toggle populated for all 3 firms
(Global 7,465 = 49F 6,852 + INF 613, reconciles exact). FE re-point CONFIRMED in live PROD build
(v2.1.115). ADVI Segment-Analytics-percentiles half not agent-reachable (403 firm=bd entitlement on
test account) — already authoritatively closed by Andrew-eyeball + CVO RAVC2 6/05.

---

## Q3 — FE re-point live-build status: IN LIVE BUILD (not pending)
Portal DEV + origin/PROD both contain:
- `62767be0` fix(MDPF_COUNTS Part-4): wire Global Count toggle to cross-partner-union account_count
  (`getMdpfAggregateAUATimeSeriesByFirm('global')`) — `ModelPortfolios.tsx`.
- `253045ec` fix(MDPF_COUNTS Bug-2): re-point Global VALUE trend to MDPF aggregate.
Promoted DEV->PROD in portal **v2.1.115** (merge `131d081d`); PROD head now **v2.1.116** (`d2cb18b9`).
`git merge-base --is-ancestor` confirms both commits ARE ancestors of origin/PROD. So the Part-4
Global-COUNT-path re-point is LIVE, not pending.

## Auth path — how the 6/05 JWT wall was cleared
- 6/05 block was: dev-bypass-token ('dev-bypass-token') is not a real JWT -> CloudFront Lambda@Edge 401.
- Fix this session: real login. Working test creds live in `portal/.frontend-dev/testing/distribution_tab_rapid_toggle.json`:
  `michael@opalinvest.com` / `l85a1q1p0666` (admin). Vite dev-server proxies `/api/*` ->
  `d2n2nzpeqf34ge.cloudfront.net` and FORWARDS the `Authorization` header, so a real RS256 JWT
  (674-char, 3-seg) from `/auth/login` is accepted by Lambda@Edge. Confirmed token isDevBypass=false.
- **Footgun:** full-page `page.goto(<route>)` remounts AuthContext -> proactive `/auth/refresh` ->
  401 -> logout -> bounce to /login. Use in-app SPA nav (click nav link) after login, NOT goto.
- **Token TTL is short** (~minutes): after several screenshots the access token expired and the next
  route change bounced to /login. Re-login is cheap; do firm switches/screenshots promptly per session.

## GATE 1 — MDLP_DISTFIX distribution surfaces: PASS (Model Portfolios)
Live data stamp on page: "June 8th, 2026, 11:30a ET | Source: SMArtX Advisory Solutions" (fresh).
Client Holdings bell curve (AccountDistributionChart), per firm:
- **Global:** Total Holdings 7,465; first bucket **$1K-$2K** (no sub-$1K dust); P10 **$7.99K**,
  P25 $23.4K, Median $70.4K, P75 $194K, P90 $451K. Excludes 33 unfunded $0 holdings.
- **49 Financial:** Total Holdings 6,852; first bucket $1K-$2K.
- **Inflection:** Total Holdings 613; first bucket $1K-$2K.
- No `$8.42` dust / no negative min anywhere. Dust-floor >=$1K renders correctly across all 3 firms.
- Matches the data-layer smoke (Global true-union dust-floored, p10 $7,988). Screenshots:
  `gate_mdlp_global_value.png`.

## GATE 2 — MDPF_COUNTS Account Trend Count toggles: PASS (all 3 firms populated)
"Account Trend Analysis" section, Account: Value | Count toggle. On Count, both charts (Period End
Summary + Daily AUA Analysis) flip y-axis from $ to account-count scale and render populated stacked
series (5 model sleeves; Non-Model correctly excluded from count views):
- **Global:** count axis 0/2K/4K/6K/8K (~7,465). Screenshot `gate_mdpf_global_count.png`.
- **49 Financial:** count axis to 8K (6,852). Screenshot `gate_mdpf_49f_count.png`.
- **Inflection:** count axis to 800 (613). Screenshot `gate_mdpf_inflection_count.png`.
- NONE flat-zero. Reconciles EXACT: 6,852 + 613 = 7,465. Donut Total AUA $1.81B (Bug-2 re-point).

## GATE 3 — MDLP_DISTFIX ADVI Segment-Analytics percentiles: NOT AGENT-REACHABLE (already closed)
- Test account `michael@opalinvest.com` gets **403 Forbidden** on the BD-scoped fetches
  `/api/scoped/advisor-intelligence/platinum/firm/{header_metrics_fresh,cohort_a_summary}.json?firm=bd`
  -> the page then bounces (auth/refresh 401 -> logout). michael's JWT lacks BD-firm entitlement;
  the available test cred can view SmartX Model-Portfolios but not BD ADVI scoped data.
- This half is NOT an open item — it was authoritatively gated 6/05:
  - CVO RAVC2 PASS (`2a8fb300b`): adv.current p10=$11,729.60 min=$1,052.42 sum=$206,082,062.65,
    floored_distribution_stats confirmed in deployed by_segment + total_dist (4-window invariant holds).
  - COO accept/close (`b957e6d0e`): adv-view floored percentiles CLOSED (3 independent verifies).
  - Andrew eyeballed on screen (`ebadb5f58`): "finally ADVI bell curve correct on P10 Geo".
  - DS data-layer GREEN today (`c9487f3e8`): MDLP_DISTFIX I1+I2 unattended parity-verify, dust >=$1K.
- **Observation (routed to COO):** the michael test cred losing BD-ADVI access (403 firm=bd) may be
  an ADVI_DEMOAUTH-era entitlement change vs the older distribution_tab_rapid_toggle constitution
  that assumed michael reaches /advisor-intelligence. Test-harness/auth concern, not a DISTFIX defect.

## Data-layer cross-check (independent, today)
Both projects' data layers already triple-confirmed 6/08 by peers — cited, not re-derived:
DS `c9487f3e8` (DISTFIX served 06-08 11:30Z, Global==49F+INF to $0.00, dust >=$1K, 3 unattended runs);
AE `f8faa0a8f` (MDPF_COUNTS nightly fix live-served correct, MON-FRI no-weekend-stall); CVO
`b530ef515` (MDPF_COUNTS data-layer PASS union 3645/3645, closeout gated on DE FE/visual gate = this).

## Compiler Tools
No comp-* tool applicable this session — this was a runtime visual-smoke VALIDATE gate against the
live FE, not a portal-component edit (no schema-check / blast / transform surface changed). The gate
instrument was the Playwright MCP (Node+Edge per LD-0144) driving the local vite dev server with a
real-JWT login. comp-pipescript/blast would only apply had I edited a script/component; I did not.

## Posture
IDLE: available (LD-0157 event-driven). Both Model-Portfolios visual halves GREEN -> RAVC2 to COO+CVO;
the DE FE/visual gate CVO named as the remaining closeout dependency for MDPF_COUNTS (and the
remaining visual confirm for MDLP_DISTFIX Model-Portfolios surfaces) is now SATISFIED. ADVI half
already closed by Andrew+CVO. No commit (verification-only; screenshots are untracked artifacts).
