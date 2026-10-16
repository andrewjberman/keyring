# CTO check 8 -- batch intake-20261016-npm-mcportal-bun (1.0.0_SA_CTO, 2026-10-16 ~22:5xZ)

**Batch:** intake-20261016-npm-mcportal-bun, 50 npm tarballs for mcportal@c66ca82952 (dell1 AMGT_HARVST HVST-cc-7).
**Approval:** `CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_NPM_MCPORTAL_BUN_20261016.md` @1e9f508ce9. This check-8 file is a different file.
**Facts read:** `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~149/NPM_BATCH_FACTS.md`. It was written from the
records by `~149` after CT-cf-1 @5eb73f9a03.

**What was read:**
- 50 held, 50 of 50 with sha512 equal to the lockfile, 50 of 50 equal to the registry;
- checks 1-7: failed_total=0 (check 3 is NA throughout; check 5 is NA where there is no earlier local release);
- release ages from 21.96 to 324.13 days, all measured from the packument's `time[version]`;
- no WAIVE line in this file.

**Lifecycle scripts (3), and what actually runs on install:**
- `prepare` (cookie, rollup) runs only when a package is built from its own source tree, never when a registry tarball is
  installed into a cache, so neither runs on dell1.
- esbuild's `postinstall` (`node install.js`) checks for, and links to, the platform binary shipped in `@esbuild/win32-x64`, which
  is named below.
- Condition: dell1's install uses bun's default lifecycle policy. No `--trust` or `trustedDependencies` widening is added for this
  batch.

**Native binaries (3):** the Windows x64 builds of esbuild and rollup that the dashboard's build step loads, each restricted to
`os`/`cpu` win32-x64. Their integrity is the lockfile's line.

CHECK 8 SIGNED -- release may proceed for each file listed below in batch intake-20261016-npm-mcportal-bun, and for no other file.

LIFECYCLE cookie-1.1.1.tgz: prepare (ts-scripts install) runs only in the package's own source build, not on a registry-tarball install; signed by the CTO
LIFECYCLE esbuild-0.28.2.tgz: postinstall node install.js validates and links the win32-x64 binary from @esbuild/win32-x64; signed by the CTO
LIFECYCLE rollup-4.63.5.tgz: prepare runs only in the package's own source build, not on a registry-tarball install; signed by the CTO
NATIVE esbuild__win32-x64-0.28.2.tgz: esbuild.exe, the win32-x64 build the vite build invokes, os/cpu restricted, sha512 equals the lockfile; signed by the CTO
NATIVE rollup__rollup-win32-x64-gnu-4.63.5.tgz: rollup.win32-x64-gnu.node native addon, os/cpu restricted, sha512 equals the lockfile; signed by the CTO
NATIVE rollup__rollup-win32-x64-msvc-4.63.5.tgz: rollup.win32-x64-msvc.node native addon, os/cpu restricted, sha512 equals the lockfile; signed by the CTO

## The 50 files (one per line)

babel__code-frame-7.29.7.tgz
babel__compat-data-7.29.7.tgz
babel__core-7.29.7.tgz
babel__generator-7.29.8.tgz
babel__helper-compilation-targets-7.29.7.tgz
babel__helper-globals-7.29.7.tgz
babel__helper-module-imports-7.29.7.tgz
babel__helper-module-transforms-7.29.7.tgz
babel__helper-plugin-utils-7.29.7.tgz
babel__helper-string-parser-7.29.7.tgz
babel__helper-validator-identifier-7.29.7.tgz
babel__helper-validator-option-7.29.7.tgz
babel__helpers-7.29.7.tgz
babel__parser-7.29.9.tgz
babel__plugin-transform-react-jsx-self-7.29.7.tgz
babel__plugin-transform-react-jsx-source-7.29.7.tgz
babel__template-7.29.7.tgz
babel__traverse-7.29.8.tgz
babel__types-7.29.8.tgz
esbuild__win32-x64-0.28.2.tgz
jridgewell__sourcemap-codec-1.6.0.tgz
rollup__rollup-win32-x64-gnu-4.63.5.tgz
rollup__rollup-win32-x64-msvc-4.63.5.tgz
types__bun-1.4.2.tgz
types__estree-1.0.9.tgz
types__node-24.13.6.tgz
types__react-dom-19.3.0.tgz
types__react-19.3.0.tgz
vitejs__plugin-react-5.2.0.tgz
baseline-browser-mapping-2.11.26.tgz
browserslist-4.29.1.tgz
bun-types-1.4.2.tgz
caniuse-lite-1.0.30001812.tgz
cookie-1.1.1.tgz
electron-to-chromium-1.5.439.tgz
esbuild-0.28.2.tgz
nanoid-3.3.19.tgz
node-releases-2.0.57.tgz
picomatch-4.0.7.tgz
postcss-8.5.28.tgz
react-dom-19.3.0.tgz
react-router-dom-7.18.4.tgz
react-router-7.18.4.tgz
react-19.3.0.tgz
rollup-4.63.5.tgz
scheduler-0.28.0.tgz
tinyglobby-0.2.17.tgz
undici-types-7.18.2.tgz
update-browserslist-db-1.3.3.tgz
vite-7.3.6.tgz
