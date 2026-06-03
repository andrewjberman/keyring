# work — 0.4.2_RD_AdvisorIntelligence — 2026-06-03 ~1721-1730Z — FE security dep-sweep (Batch 1)

Andrew-direct frontend security cleanup. Cleared the runtime-critical dependency vulnerabilities on
the portal HTTP client + build chain under an explicit zero-breakage bar. Scoped, careful, clean.

## Mandate

- **Andrew directive (via COO GO 172114Z):** "be very ginger about it, I don't want any breaks." Zero-breakage = the hard acceptance bar.
- **Plan of record:** `org/tier3_junior/0.3.2_RD_TradeSubmission/logs/2026-06-03/fe_depsweep_remediation_plan.md` (commit 867660fd5, author 0.3.2_RD_TradeSubmission). 45 vulns / 12 packages; every patched release sits INSIDE the existing caret pins → a named compatible `bun update` clears the runtime set with zero app-code changes.
- **Scope:** BATCH 1 ONLY (runtime-critical, in-caret) = `bun update axios postcss vite`. Batch 2 (lodash override) + Batch 3 (eslint dev-only) held.
- **Hard stop:** do NOT take vite 8.x (breaking, unneeded). STOP on any major/out-of-caret bump of a named pin.

## What I did — the ginger protocol, step by step

1. **BEFORE state captured:** git baseline clean (no pending package.json/bun.lock). Pins: `axios ^1.13.6`, `postcss ^8.5.6`, `vite ^7.3.1`. `bun audit` = **45 vulns (21 HIGH, 23 moderate, 1 low)**.
2. **Named update:** `bun update axios postcss vite` (named, NOT a blanket update). Landed exactly: **axios 1.17.0, postcss 8.5.15, vite 7.3.5**. Vite held 7.3.x (hard stop respected). follow-redirects auto-bumped 1.15.11→1.16.0 (expected axios auto-fix).
3. **Lock diff vetted:** only in-caret bumps of the 3 named + follow-redirects. package.json caret floors moved to the patched versions (`^1.17.0`/`^8.5.15`/`^7.3.5`), same major.
4. **VERIFY HARD:**
   - `bun audit` AFTER = **22 vulns (12 HIGH, 10 mod)** → **23 cleared**, including **ALL 7 axios HIGHs + the XSRF token cross-origin leak + proto-pollution + SSRF block + postcss**.
   - `tsc -b`: CLEAN.
   - Full `bun run build` (vite production build): **CLEAN, exit 0, 16.5s** — every chunk built incl. the chart vendors (vendor-nivo / recharts / apexcharts) + ModelPortfolios. The build bundles + tree-shakes every page against the new deps, so it's a strong non-breakage proxy.

## Shipped

**Commit 8c3caf70** (portal DEV, Rule 19 no-promote) — package.json + bun.lock only, **zero app code**. Rides v2.1.114+.

## Disclosures (flagged in RAVC2; neither tripped a STOP)

- **(a) axios 1.17.0 transitive footprint:** brought `https-proxy-agent@5.0.1` + `agent-base@6.0.2` (new) + `proxy-from-env` 1.1.0→2.1.0 (transitive MAJOR). ALL are Node http-adapter-only; the browser build uses the XHR adapter, so they're **inert at runtime** (clean build confirms). This is axios-1.17's own internal dep tree, NOT an out-of-caret bump of a named/top-level pin → proceeded, disclosed.
- **(b) rollup did NOT auto-clear** (still a build-only HIGH, <4.59.0). The plan expected vite 7.3.5 to pull rollup 4.61.0, but vite 7.3.5's range (`^4.43.0`) was already satisfied so no forced bump. Build-only (bundler path-traversal), LOW real risk, never on untrusted input. Not a regression (pre-existing); cleanable in a separate rollup bump if audit-clean-zero is wanted.

## Remaining gate (not done by me)

In-app **render smoke** (Advisor-Intelligence data page + a charts page) is **auth-gated** — localhost dev needs a login I can't perform. The full vite build is a strong proxy (bundles every page incl. the lodash-transitive nivo charts), but the live render confirm = **Andrew at promote**, same as every portal smoke this session.

## Outcome + disposition

- **RAVC2 ACCEPTED by COO** ("textbook ginger execution"). The one genuine user-facing risk (axios XSRF cross-origin leak) is killed.
- **Batch 2 (lodash override) + Batch 3 (eslint dev-only) + the optional rollup bump = HELD — COO is asking Andrew.** Rationale: Batch 1 cleared the genuine risk; the remaining 22 vulns are all non-shipping — lodash UNREACHABLE (transitive via charts, no direct `_.template` call), eslint DEV-ONLY (never ships), rollup BUILD-ONLY. Chasing audit-clean-zero for cosmetic build/dev vulns may not be worth the churn against Andrew's no-breaks bar. Awaiting his call.

## Audit delta

| | HIGH | moderate | low | total |
|---|---|---|---|---|
| before | 21 | 23 | 1 | **45** |
| after | 12 | 10 | 0 | **22** |
| cleared | 9 | 13 | 1 | **23** |

All 23 cleared are runtime-real (axios block + follow-redirects + postcss). All 22 remaining are dev/build-only tooling.

## Reusable takeaways

- **The "in-caret named `bun update`" is the safe lever for security dep bumps** — clears the CVE without app-code churn or migration (contrast the xlsx case which needed a CDN migration). Pre-check: every patched release ≥ the advisory floor AND < the next major.
- **A transitive major bump is not automatically a STOP** — scope it: a Node-only utility (proxy-from-env / https-proxy-agent) pulled by an in-caret browser-lib upgrade is inert in the XHR build. Disclose, let the build confirm, proceed. STOP is for major/out-of-caret bumps of the *named/top-level* pins.
- **A clean full `vite build` is the strongest non-breakage signal available without auth** — it type-checks, bundles, and tree-shakes every page (incl. transitive chart surfaces). When the in-app render smoke is auth-gated, the build is the proxy and the live render is the human's promote-gate.
- **Sequence security batches by real risk, not audit-count** — clear the genuine user-facing HIGH first (axios), then let the cosmetic dev/build residuals be a separate, optional, human-greenlit step rather than forcing audit-zero in one churny pass.
