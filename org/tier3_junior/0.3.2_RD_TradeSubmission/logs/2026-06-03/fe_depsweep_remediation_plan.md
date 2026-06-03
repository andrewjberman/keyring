# FE Dependency-Sweep Remediation Plan (GO-ready)

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE
**Author:** 0.3.2_RD_TradeSubmission
**Date:** 2026-06-03
**For:** 2.0.0_SA_COO (deliverable), CC 0.7.0_AE_CloudOps
**Status:** ANALYSIS ONLY — no dep changes shipped. Awaiting Andrew GO (relayed via COO).
**Source:** `bun audit` (portal, live deps) + Track-1 findings `docs/briefs/security-scan-track1-findings-20260603.md`. xlsx already remediated separately (commit `3e0ce8d0`, RAVC2-accepted).

---

## Headline

**45 remaining vulns (21 HIGH, 23 moderate, 1 low) across 12 packages.** The good news: **every flagged package's patched release sits INSIDE the existing caret pin** — so a plain compatible `bun update` (NOT `--latest`/breaking) clears the entire runtime-critical set with **zero application code changes**. No migration like xlsx. The only judgment calls are (a) a transitive `lodash` override and (b) whether to bother fixing the dev-only lint-chain CVEs at all.

---

## Per-package classification

| Package | Sev (count) | Class | Real risk | Fix type | Version path | Blast radius |
|---|---|---|---|---|---|---|
| **axios** | 7 HIGH + 11 mod + 1 low (~19) | **RUNTIME-DIRECT** | **HIGH** — HTTP client on every API call; portal sends Bearer/XSRF tokens. Proto-pollution credential-theft + XSRF cross-origin leak + SSRF are real. | `bun update` (safe) | `^1.13.6` (1.13.6) → **1.17.0** (patched ≥1.15.2; <2.0.0 so in-caret) | `src/api/client/axios.ts` (sole direct importer; the shared client — all API traffic). Also auto-fixes **follow-redirects** (→1.16.0). |
| **vite** | 2 HIGH + 1 mod | DEV/BUILD-only | LOW (prod) — dev-server file-read / `fs.deny` bypass only exploitable on an exposed dev server; built output unaffected. | `bun update` (safe) | `^7.3.1` (7.3.1) → **7.3.5** (patched; <8.0.0 in-caret). **Do NOT take vite 8.x** — major/breaking, not needed. | Build tooling only. Auto-fixes **rollup** (→4.61.0) + **picomatch** (vite path). |
| **postcss** | 1 mod | BUILD-only | LOW — XSS-via-stringify only matters when processing untrusted CSS (we process our own). | `bun update` (safe) | `^8.5.6` (8.5.6) → **8.5.15** (in-caret) | CSS build step. |
| **lodash** | 1 HIGH + 2 mod | TRANSITIVE-runtime (via `@nivo/*` + `@visx/text` charts) | **LOW** — no direct app import (grep-confirmed); the `_.template` code-injection HIGH requires calling `_.template` on attacker input, which nivo/visx do not. | **Override** (or transitive bump) | installed 4.17.21 → **4.18.1** (the fix, >4.17.22; nivo/visx pin `^4.17.21` so 4.18.1 is in their caret). If `bun update` doesn't bump the transitive, add `"overrides": { "lodash": "4.18.1" }` to package.json. | Charting only; no app code touches lodash directly. |
| **minimatch** | 6 HIGH | **DEV-only** (eslint + typescript-eslint) | NONE (prod) — lint toolchain, never shipped, never run on untrusted input. | `bun update` of eslint chain *may* clear; else accept | via `eslint`/`typescript-eslint` sub-deps | Lint only. |
| **flatted** | 2 HIGH | DEV-only (eslint cache) | NONE (prod) | same | via `eslint › file-entry-cache` | Lint only. |
| **picomatch** | 2 HIGH + 2 mod | DEV/BUILD-only | NONE/LOW | vite path fixed by vite bump; tseslint path = lint | via vite + typescript-eslint | Build/lint. |
| **ajv** | 1 mod | DEV-only (eslint) | NONE | `bun update` eslint chain | via `eslint › @eslint/eslintrc` | Lint only. |
| **brace-expansion** | 4 mod | DEV-only (eslint/tseslint) | NONE | same | via minimatch in lint chain | Lint only. |
| **rollup** | 1 HIGH | BUILD-only | LOW | auto via vite bump | `vite › rollup` → 4.61.0 | Bundler. |
| **follow-redirects** | 1 mod | RUNTIME (axios dep) | fixed by axios bump | auto via axios bump | `axios › follow-redirects` → 1.16.0 | — |

---

## Sequenced plan

### Batch 1 — runtime-critical safe-bumps (one `bun update`, zero code changes) — DO FIRST
Targets the genuinely user-facing risk. All in-caret, non-breaking:
```
cd portal && bun update axios postcss vite
```
- Clears: **axios** (the whole 19-CVE block incl. all 7 HIGH) + **follow-redirects** + **postcss** + **vite** (3) + **rollup** + vite-path **picomatch**.
- Net: ~26 of 45, including ALL the runtime-real HIGHs.
- **Why this is safe:** axios 1.13→1.17 and vite 7.3.1→7.3.5 are minor/patch within the same major; postcss 8.5.6→8.5.15 is patch. No breaking API per their changelogs (RD to skim changelogs at execution). axios `src/api/client/axios.ts` uses standard `.create()/.get/.post/interceptors` — all stable across 1.x.

### Batch 2 — lodash transitive (override pin) — cheap, low-risk
```
# if Batch 1's bun update didn't already bump transitive lodash to 4.18.1:
# add to portal/package.json:  "overrides": { "lodash": "4.18.1" }
cd portal && bun install
```
- Clears the lodash HIGH + 2 moderate. 4.18.1 over 4.17.21 = patch-level; nivo/visx accept it (their `^4.17.21` caret).
- Real risk was already LOW (unreachable `_.template`), but the fix is one line.

### Batch 3 — dev-only lint-chain (optional / accept) — NOT user-facing
```
cd portal && bun update eslint typescript-eslint eslint-plugin-unused-imports
```
- Targets the remaining minimatch(6 HIGH)/flatted(2 HIGH)/ajv/brace-expansion/tseslint-picomatch — **all lint tooling, never shipped to the browser, never run on untrusted input.**
- A compatible `bun update` may not reach all of them (older sub-dep pins). Recommendation: attempt the compatible bump; for any residual, **ACCEPT as dev-only** rather than force an eslint major bump (which risks lint-config churn). Document the accepted set; do not let it block.

---

## Effort + test gate

- **Batch 1+2:** ~30–45 min incl. verification. No code changes expected (dependency bumps only).
- **Test gate (same as xlsx):** `bun audit` (confirm target CVEs gone) → `tsc -b` clean → `bun run build` clean → `/frontend-dev` visual smoke on the axios-heavy paths (any data-loading page) + a charts page (nivo/visx → lodash). Commit to portal DEV; DT coordinates promote.
- **Batch 3:** lint-only; `bun run lint` must still pass; no runtime test needed.
- **Breaking/migration set:** **NONE.** (Contrast xlsx, which needed a CDN migration.) The only "breaking" option on the table — vite 8.x — is explicitly **not required**; 7.3.5 patches every flagged vite CVE.

---

## Recommendation to COO/Andrew

This is far lighter than the xlsx case — **no migrations, no breaking changes for the runtime-critical fixes.** Suggest Andrew greenlights **Batch 1 (axios/vite/postcss) as the priority** — it kills every user-facing HIGH in a single non-breaking `bun update`. Batch 2 (lodash) folds in trivially. Batch 3 (dev lint-chain) is cosmetic-for-audit-cleanliness and can be accept-documented. The moment GO lands, execution + test-gate is ~1 hour to a clean `bun audit` (modulo accepted dev-only residuals).

**Standing by for Andrew GO via COO. No dep changes shipped until then.**
