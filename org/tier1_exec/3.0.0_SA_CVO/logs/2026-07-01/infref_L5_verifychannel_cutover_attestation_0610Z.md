# CVO L5 co-sign + verify-channel + CUTOVER attestation — ADVI_INFREF (3rd tri-validation leg)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

**Serial:** 3.0.0_SA_CVO | **Date:** 2026-07-01 | **Window:** ~06:07-06:11Z
**Gate:** ADVI_INFREF atomic cutover — post-swap L5 + live verify-channel + CVO closure-attestation (Andrew-direct tri-validation: AE + DS~A + CVO). Swap: 0.6.1 additive cp platinum/_rebuild/20260630T234458Z/ -> platinum/, landed 06:07:28Z, on my L3-GREEN (c5a4fc883).

## VERDICT: cutover L5 = GREEN + verify-channel = GREEN. CUTOVER ACTIVATION attested. (PROJECT CLOSE = separate, rides the multi-day tail — see scope.)

Grounded on the actual post-swap SERVED state + a live Lambda re-invoke — never 0.6.1's swap self-report.

### L5 — atomic swap correctness (my independent co-sign; CTO co-signs separately)
- **Served is now the rebuild content:** served platinum/firm/header_metrics.json LastModified 06:07:28Z, **generated_at = 2026-07-01T05:35:01Z** (the rebuild run — advanced from the pre-swap nightly's 06-30T17:16Z). total_aua $202,125,678.08, client_count 307, as_of 06-30. The swap actually replaced served with the rebuilt canonical.
- **Never-widen CONFIRMED:** sampled legacy orphan clients/100/detail.json still 27-Apr-2026 18:10Z (preserved, not deleted); current clients/101/detail.json refreshed to 06:07:00Z. Additive cp (not sync --delete) — the 691 stale orphans preserved, only the 307 current overwritten. Matches the never-widen requirement.
- **Post-swap served == parity baseline:** $202,125,678.08 to the cent (== my L3 baseline == CTO's value-parity anchor).

### verify-channel (surface-level, the 4-check on the SERVED artifact + live render)
- **EXISTS:** served header_metrics.json present post-swap.
- **FRESH:** mtime 06:07:28Z, generated_at = the rebuild run (not stale).
- **SCALED:** total_aua $202,125,678.08 — correct magnitude (not zero/garbage/short), 307 clients.
- **NOT-FROZEN:** generated_at advanced from the prior nightly (06-30T17:16Z) to the rebuild (07-01T05:35Z) — served is the NEW content, not stuck.
- **LIVE value-parity (deployed guard, re-invoked post-swap):** opal-inf-value-parity dry-run -> exit=0, FRESH, "served 202125678.08 matches inf current_value.sum[2026-06-30] to the cent (diff 0.0000) -- served equals the source." The live guard confirms the newly-served number == the Orion source, post-cutover.
- **Render path:** the served key is the SAME one the daily nightly updates (pre-swap generated_at = yesterday's nightly), so the portal renders it via the daily-proven cache cadence (cache-control-injector on origin-response governs edge TTL). The rebuilt number propagates to the portal exactly as every daily update does.

### CVO CUTOVER ATTESTATION (3rd tri-validation leg — SCOPED)
I attest, grounded on live served state: **the ADVI_INFREF atomic cutover is ACTIVE and the served surface correctly delivers the rebuilt canonical numbers to the cent.** L3 (rebuild==served) GREEN + L5 (swap correctness + never-widen + served==parity) GREEN + verify-channel (served fresh/usable/value-parity-live) GREEN.

**This attests the CUTOVER ACTIVATION, NOT the PROJECT CLOSE.** Per CTO's ledger framing (060943Z), full ADVI_INFREF close is a multi-day tail gated on legs I have NOT verified and explicitly HOLD:
- **L1** (pull-stage parity: staged --stage pull == served pull + bash -n 57-script set) — lands on the new single-runner's FIRST NIGHTLY (~tomorrow); c5a4fc883 was compute-only, does NOT satisfy it.
- **L4** (incremental == rebuild reference-parity) — the incremental artifact isn't built yet; separate downstream verdict.
- **L6** (temporal-stability, ~tomorrow) + **L7** (cron-delete after L6).
My tri-validation CLOSURE-attestation (project-complete) is owed LATER, when L1/L4/L6/L7 land and all three parties attest. Tonight's attestation is bounded to the cutover activation.

### Residuals
- **[P2] CDN edge-curl not performed (auth wall):** every /api/scoped/* platinum behavior is [AUTH]-gated; I could not directly curl the edge. Render is grounded via the daily-cadence proof + live value-parity on the origin. BELT-AND-SUSPENDERS RECOMMENDATION (DT/AE): a CloudFront invalidation of platinum/firm/* + the 307 refreshed clients/ paths guarantees IMMEDIATE edge freshness rather than waiting on TTL expiry. Not gating (cadence proves eventual freshness).
- **[P2] _meta cleanup pending (0.6.1):** platinum/firm/_meta/reconciliation_summary_holdings_* present in served — internal reconciliation artifacts, NOT portal-rendered, benign; 0.6.1 cleans post-swap. Independently confirmed they are not in the portal's rendered surface (under _meta/ subprefix, not a firm view).
- **[P2] upstream April-orphan question:** why ~690 households went stale in the normal pipeline after 2026-04-27 — separate pre-existing issue, non-gating, COO tracking.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp-routes behaviors` | ground the platinum CDN serving/cache behavior for verify-channel edge | PASS — confirmed [AUTH]-gated scoped behaviors + cache-control-injector on origin-response |
| `comp-which` (inf CDN) | route | backstop → comp-platinum/comp-pii/comp-routes |

What worked: re-invoking the LIVE deployed value-parity guard against the newly-served header post-swap is the strongest verify-channel evidence — it confirms served==source to the cent on the actual cutover artifact, not a self-report. Auth-gated edge blocked a direct curl (bounded residual, mitigated by daily-cadence). No comp-tool invokes a Lambda / diffs post-swap served, so those ran rail-checked.

— 3.0.0_SA_CVO
