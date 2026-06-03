# xlsx/SheetJS CDN-swap — HIGH CVE remediation (TradeSubmission fileParser)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DEPLOY

**Date:** 2026-06-03
**Agent:** 0.3.2_RD_TradeSubmission
**Source:** Andrew-direct, routed via 0.7.0_AE_CloudOps (Track-1 security scan `1f512f69d`, findings `docs/briefs/security-scan-track1-findings-20260603.md`)
**Commit:** portal DEV `3e0ce8d0`

## Task

Remediate 2 HIGH CVEs in `xlsx`/SheetJS pinned at `^0.18.5` (frozen-vulnerable community
npm build — SheetJS stopped publishing to npm; patches live CDN-only):
- GHSA-4r6h-8v6p-xvw6 — Prototype Pollution
- GHSA-5pgg-2g8v-p4x9 — ReDoS

Live attack surface: `portal/src/pages/TradeSubmission/services/fileParser.ts` calls
`XLSX.read()` on USER-UPLOADED `.xlsx` files (TradeSubmission upload). Lowest-impact fix
requested: repoint the dependency from npm to the SheetJS CDN patched build.

## What I did

- Confirmed sole consumer: `grep` across `portal/src` → only `fileParser.ts` imports `xlsx`.
- Confirmed current patched stable = **0.20.3** (CDN tarball HTTP 200; docs page corroborates).
- Swap: `bun remove xlsx` then `bun add https://cdn.sheetjs.com/xlsx-0.20.3/xlsx-0.20.3.tgz`.
  - `bun add` alone hit a `DependencyLoop` error against the old `^0.18.5` semver pin —
    resolved by removing first, then adding the tarball. (Note for next time.)
- Result: `package.json` `"xlsx"` → CDN tarball URL; `bun.lock` relocked. **Zero source
  changes** — `fileParser.ts` untouched (import + API identical). git diff = 2 files.

## Verification

| Check | Result |
|-------|--------|
| `bun audit` — xlsx advisories | Both GHSA-4r6h + GHSA-5pgg **GONE** (PASS). Unrelated picomatch/vite CVE remains (out of scope). |
| API-parity (executed fileParser's exact call chain on 0.20.3 build, real `.xlsx` bytes) | **PASS** — `XLSX.read(data,{type:'array'})` / `SheetNames`+`Sheets` / `XLSX.utils.sheet_to_json(ws,{header:1})` / `XLSX.SSF.parse_date_code(serial)`. Serial 45658 → `2025-01-01`; cash/`curncy` row skipped; 2 securities parsed. Script: `.runtmp/xlsx_api_parity_test.cjs`. |
| `tsc -b --noEmit` | clean (exit 0) |
| `vite` production build (`bun run build`) | clean (exit 0, 29s) — Rollup bundles new xlsx ESM into `index.esm` chunk = browser-bundling proven (this is the promote path) |
| Browser visual smoke (`/frontend-dev` upload-render) | **NOT RUN** — shared Playwright/Edge MCP locked by another agent's session (`Browser is already in use … use --isolated`); declined to disrupt. Residual UI risk ~nil for a no-code dep swap that bundles cleanly + parse-logic proven byte-for-byte. Proposed: covered by DT promote smoke / Andrew localhost check, or I run it when the browser frees. |

**Key risk caught proactively:** `fileParser.ts:169` uses `XLSX.SSF.parse_date_code` —
beyond the `read`+`sheet_to_json` AE flagged. Verified `SSF` survives the 0.18→0.20 bump
(object + function present at runtime; types `export const SSF: any`). No API drift.

## Compiler Tools

Portal-component comp-* tools (`comp-transform schema-check` / `ternary-audit`) were **not
the applicable gate** here: this is a service-layer dependency-source swap with no portal
component schema/prop change and no rendered-field delta — those tools key on component
field/ternary surfaces, which are unchanged. The correct verification axis for a dependency
swap was `bun audit` (CVE delta) + executed API-parity against the new build + tsc + vite
production build, all run above. No comp-tool gap found.

## Handoff / status

- RAVC2 → AE (`0.7.0_AE_CloudOps`), CC COO (`2.0.0_SA_COO`).
- Promote: portal DEV→PROD needs DT coordination (RD does not push PROD).
- Open: literal browser visual smoke pending shared-MCP availability.
