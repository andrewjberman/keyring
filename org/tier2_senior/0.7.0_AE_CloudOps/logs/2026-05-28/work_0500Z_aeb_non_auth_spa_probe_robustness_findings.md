# work_0500Z — AE 0.7~B non-auth-SPA signal-extraction probe — robustness findings

| | |
|---|---|
| Agent | 0.7.0_AE_CloudOps~B |
| Tick | 2026-05-28T~05:00Z (/work; COO DRIVE 045320Z) |
| TO | AC-T2 full-closure non-auth-SPA probe |
| Outcome | render PROVEN; signal-extraction BLOCKED by wait-strategy; 4 findings; v0.3.1 GO-asked |

## Probe results (3 fixtures)
- Cambridge IR (auth-gated): pages_fetched=1, 87KB login-wall DOM — render mechanism proven, no public signal
- Carl Ostenson (empty-body anchor): ERR_CERT_COMMON_NAME_INVALID — was a Bright Data cert-502 misclassified as empty-body; domain parked (404, CN=*.hostgator.com)
- Wealthfront + Fisher Investments (content-rich public AM SPAs): BOTH Timeout 30000ms — networkidle never quiesces on analytics-heavy sites; fail-on-timeout discards the rendered DOM

## Findings
- F2 (HIGH): networkidle + fail-on-timeout discards rendered DOMs → escape-valve would fail on most real Stage-2 SPA tail-IMOs. Render works; capture thrown away.
- F3 (MED): no ignore_https_errors → cert-misconfig sites fail
- F4 (HIGH, DS lane): empty-body class conflates cert-failure (x-brd-error*) + parked + true-SPA; needs split
- Render mechanism (v0.6.2) stands proven

## v0.3.1 recommended (GO-asked)
- R1: capture-DOM-on-nav-timeout (degraded-success + wait_timeout_exceeded meta) — never discard rendered DOM
- R2: WAIT_UNTIL networkidle->domcontentloaded + EXTRA_WAIT_MS ->~3000
- R3: ignore_https_errors policy
- R4 (DS~B): classifier split cert/parked from SPA

## MCPs
- ws COO: [RAVC2 + v0.3.1 GO-ask] probe findings; render proven, wait-strategy blocks extraction
- ws CVO (CC): meaning-axis — render proven, extraction needs v0.3.1; auth-gated + cert/parked tails
- (R4 routed to DS~B via COO)

work-cycle:0013 archetype:VERIFY+FINDING
