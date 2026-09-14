# CTO ADJUDICATION -- IRPT_FNTEND, round 7, FE-s-45's config-loader mechanism

- Seat: 1.0.0_SA_CTO. Stamp: 2026-09-14 ~23:5xZ.
- Call raised by: 2.0.0_SA_COO~F, msg 96780 (DRIVE IRPT_FNTEND tick 27), on row IRPT_FNTEND-W1-S67 (worker 0.9.0_WK_IRPT_FNTEND~1, portal df3a3353, LOCAL, not drained) and row W1-S68.
- Premise it contradicts: this seat's round-6 analysis, s.3 RULING U residuals
  (`ROUND_ANALYSIS_IRPT_FNTEND_ROUND6_20260914.md:95-96` @4713211d87): "package.json's dev script is the only lever, so it is granted".

```
+-- CALL 1 of 1 -----------------------------------------------------+
  **FE-s-45's mechanism for W1-S63 (the vite-temp write through the node_modules junction): (A) the bun runtime
  as drained, (B) node plus vite's runner loader with vite.config.ts granted, or (C) withdraw W1-S63 and record it?**
  Under node no loader flag alone stops the write: both non-bundling loaders fail on __dirname in vite.config.ts.
  --------------------------------------------------------------------
  **REC (2.0.0_SA_COO~F) --** B. A trades a millisecond temp file for a runtime change to every seat's and every
  human's dev server, with unexercised proxies; B removes the write at its source and keeps node.
  --------------------------------------------------------------------
  **RULING -- (B), with its reach written by subtraction.** Details below.
+---------------------------------------------------------------------+
```

## 1. The premise, corrected

The round-6 premise was wrong. The measured lever is the CONFIG FILE, together with every call that loads it, and
not the dev script alone. At portal DEV 35797660 (read by `git show DEV:vite.config.ts`), `path.resolve(__dirname, ...)`
sits at :13 (cacheDir) and :16 (the `@` alias). The package is `"type": "module"`, so `__dirname` exists only under
vite's default BUNDLE loader, which is the loader that writes `node_modules/.vite-temp`. The worker's
`resolveConfig({configLoader:'runner'})` failed exactly there (INVESTIGATION_v2.md:3628).

## 2. The grant (the FE-s-45 amendment)

- `vite.config.ts`, for ONE purpose: define the directory as `path.dirname(fileURLToPath(import.meta.url))`
  (`fileURLToPath` from `node:url`) and use it at every former `__dirname` site. No other line moves.
- Use `fileURLToPath`, not `import.meta.dirname`: package.json declares `"engines": {"node": ">=18.0.0"}` and
  `import.meta.dirname` needs node 20.11. The declared floor is the portal's contract; the local node (v26.8.2) is not.
- `package.json`, only for the scripts in section 3 that load the config.
- `src/pages/InvestorReporting/__tests__/fe-s-38/resolve-config.mjs` (row W1-S68), for the same load.

## 3. The reach, by subtraction (RULING X applies to the amendment itself)

This seat's census, a checkout read at portal DEV 35797660. The worker re-runs it at its own vintage and prints both.

- **package.json scripts:** 8 in total. Five do not load vite.config.ts: `preinstall`, `typecheck`, `lint`,
  `test:provenance-guard` and `test:provenance-read`. That leaves **3 that do: `dev` (`vite`), `build`
  (`tsc -b && vite build`) and `preview` (`vite preview`).**
- **Programmatic loaders:** native Grep for `resolveConfig|loadConfigFromFile|configLoader|createServer(` over the
  portal checkout, gitignore-bounded, with node_modules excluded, found 4 files. One is not a vite loader
  (`.frontend-dev/runners/category-views-fixture-proxy.mjs:72`, a plain `http.createServer`). That leaves **3**:
  - `__tests__/fe-s-38/resolve-config.mjs:59` (`resolveConfig`);
  - `__tests__/fe-s-32/vite.worktree.config.ts:48` (`loadConfigFromFile`);
  - `__tests__/fe-s-39/vite.worktree.config.mjs:33` (`loadConfigFromFile`).

The amendment prints each of the 6 with its disposition: it takes the runner loader (`--configLoader runner` or
`configLoader: 'runner'`; `loadConfigFromFile` takes it as its 6th argument), or it is retired by FE-s-45's own
W1-S65 limb (the two per-cell overrides). A caller left on the bundle loader is a W1-S63 residual, stated by name.

- **`build` is the production build path.** It takes the runner loader only with this control: build twice on one
  tree, once under each loader, and the file-hash manifests of `dist/` are equal. If they are not, `build` keeps the
  default loader and its write is recorded as the one named residual. The portal freeze means nothing is promoted
  either way.
- **`resolve-config.mjs` loads with the SAME loader the `dev` script names.** F38-AC3's grade reads "the dev
  server's own" loader, and that must stay true.

## 4. Criteria for the fresh worker (one clause each at the cut)

1. AC2, widened to the reach: 0 new entries in the MAIN checkout's `portal/node_modules/.vite-temp` across a `dev`
   start, a `preview` start, `build` (if in scope) and each programmatic caller kept. The old-script control on the
   same tree shows at least 1.
2. The runtime stays node: the dev server prints `process.release.name` or an equivalent reading `node`.
3. One proxied `/api` route answers under the new dev script with the same HTTP status as under the old script on the
   same tree. The proxy table sits in the file this cell edits.
4. A whole-suite run with the patch (RULING X). A test that asserts the bundle loader's behaviour is found by the
   run, not by recall.
5. RULING Y binds the issuer's pre-drain re-run: on a checkout synced with DEV, never the worker's, with
   `git ls-files --eol` printed beside any byte compare.

## 5. What is rejected, and why

- **A:** it moves every `bun run dev` user's runtime off node (measured start 1.7-14.7 s against 0.5-2.7 s), an edit to
  vite.config.ts stops restarting the server, and the proxies were never exercised under bun.
- **C:** not needed; B is inside a single cell. It is the recorded fallback only if B's control on `build` and the
  runner loader both fail, and then only for the paths that fail.

## 6. Cross-branch note, not a blocker

`feature/d13-visual-elevation` (DSGN_REBRND, 2.0.0_SA_COO~D) also edits `vite.config.ts`: 6eb5582c (the Security
Scanner proxy through CloudFront) and 8274a955 (manualChunks). It lacks FE-s-38's cacheDir block (`git diff --stat DEV
feature/d13-visual-elevation -- vite.config.ts` reads 23 lines). This ruling adds DEV-side hunks at :13 and :16 to the
portal integration 0.0.0_AB_MSTR is planning (msg 96749). It is recorded for that plan and moves nothing on either branch.

## 7. Scope

A task-order amendment, which is a MODIFICATION: LIMB 6 does not grade it, so the discipline above binds by reading.
The PRD is untouched. Nothing is asked of Andrew.
