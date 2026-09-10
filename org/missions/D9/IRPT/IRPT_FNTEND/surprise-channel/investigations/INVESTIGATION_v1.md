# IRPT_FNTEND -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric). Append-only; rows below are minted by their own allocator (`.tools/surprise-row-gate.py` validates every NEW row).

```json
[
  {
    "id": "IRPT_FNTEND-W1-S1",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-10T21:40:00Z",
    "one_line": "F1-AC1 (portal typecheck rc=0) and F1-AC2..AC6 (bun tests under src/) could not both pass without ambient type declarations the order does not name: the portal tsconfig's types array excludes @types/node and bun-types is not installed, so every test file under src/ failed tsc with TS2307.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-1 names tests under portal/src/pages/InvestorReporting/__tests__/fe-s-1/ 'runnable by bun test' (F1-AC2..F1-AC6) AND a portal typecheck at rc=0 (F1-AC1), and grants no path outside <paths> -- portal/tsconfig.app.json is not in the grant.",
    "world_is": "portal/tsconfig.app.json sets \"types\": [\"vite/client\"] and \"include\": [\"src\"], so tsc -b --noEmit compiles the test files but loads neither bun-types (absent from node_modules entirely) nor @types/node (installed but excluded from the program). Measured: 7 errors, TS2307 on 'bun:test', 'node:fs' and 'node:url' plus 3 consequent TS7006. Resolved INSIDE the grant by two type-only ambient declaration files in the granted test folder -- __tests__/fe-s-1/bun-test.d.ts and __tests__/fe-s-1/node-builtins.d.ts -- rather than by editing the ungranted tsconfig. ARMED because the disarm is not the shim: if a later cell adds @types/node or bun-types to the tsconfig types array, node-builtins.d.ts's `interface Dirent` would merge against @types/node's `class Dirent` in the same ambient module, and the typecheck that is green today would break on an edit nobody would connect to this folder.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/tsconfig.app.json @5907cbca lines 'types': ['vite/client'] and 'include': ['src'] -- read at HEAD of the portal worktree branch wk-irpt_fntend-1-1-fe-s-1",
        "measured before the shims: bun run typecheck emitted TS2307 'Cannot find module node:fs' at fixtures.test.ts(11,43) and source-bounds.test.ts(15,30), TS2307 'node:url' at fixtures.test.ts(12,31) and source-bounds.test.ts(16,31), and TS7006 at fixtures.test.ts(30,14),(31,11) and source-bounds.test.ts(36,52)",
        "measured after: bun run typecheck rc=0, and a second non-incremental instrument ./node_modules/.bin/tsc --noEmit -p tsconfig.app.json rc=0 (tsc -b is cache-backed, so the build-mode green alone is not a state read)",
        "node_modules/bun-types and node_modules/@types/bun both absent (ls: No such file or directory); node_modules/@types/node present"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Both shim files are TYPE-ONLY and declare only the surface these tests call (bun:test's describe/test/expect/hooks; node:fs readdirSync/readFileSync; node:url fileURLToPath). Closing condition: an owner of portal/tsconfig.app.json decides between (a) keeping the local shims and recording that the types array must not gain @types/node or bun-types without deleting them, or (b) adding the packages to the tsconfig and deleting both shim files in the same commit. This worker cannot take either act: portal/tsconfig.app.json is not in TO-FE-s-1's <paths>."
  },
  {
    "id": "IRPT_FNTEND-W1-S2",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-10T21:42:00Z",
    "one_line": "The order's 'lists fixtures/ and asserts 31 files' cannot be a literal directory listing: the same order puts fixtures/index.ts and fixtures/smoke/default.json in that directory, so a literal listing returns 33 entries and the 31 is only reachable under a stated filter.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-1: fixtures.test.ts 'lists fixtures/ and asserts 31 files, printing FIXTURES: 31 of 31'; the same cell also requires 'A fixtures/index.ts manifest' and 'a smoke map ... at fixtures/smoke/default.json', both inside fixtures/.",
    "world_is": "A literal listing of portal/src/pages/InvestorReporting/fixtures/ returns 33 entries: 31 .json fixture files, index.ts, and the smoke/ directory. The denominator 31 is the count of .json files at depth 1, which is what the test computes and prints (readdirSync withFileTypes, filtered to isFile() and .json, no recursion). Recorded rather than resolved silently because a count whose filter is not stated is a number a later reader cannot reproduce -- and the same order supplies both the 31 and the two entries that break it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "measured: ls portal/src/pages/InvestorReporting/fixtures/*.json | wc -l = 31; the directory additionally holds index.ts and smoke/default.json",
        "portal/src/pages/InvestorReporting/__tests__/fe-s-1/fixtures.test.ts prints 'FIXTURES: 31 of 31' and separately asserts the manifest and the directory agree in BOTH directions (listed-but-absent = [] and present-but-unlisted = [])",
        "bun test src/pages/InvestorReporting/__tests__/fe-s-1/fixtures.test.ts -- 9 pass, 0 fail, rc=0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "No act taken beyond stating the filter in the test and here. If a later cell adds a non-fixture .json to fixtures/ (a config, a snapshot), the 31 breaks; the manifest-vs-directory two-way check is what would catch it, and it names the offending file rather than only disagreeing on a count."
  },
  {
      "id": "IRPT_FNTEND-S1",
      "project": "IRPT_FNTEND",
      "fabric": "laptop",
      "surfaced_by": "2.0.0_SA_COO~F",
      "surfaced_at": "2026-09-10T22:05:00Z",
      "one_line": "Disarm act for IRPT_FNTEND-W1-S1 assigned by its disarm_owner: TO-FE-s-2 (slot ~1, next in queue) is amended at the FE-s-1 drain to replace the shim's exported `interface Dirent` with an inline structural type and to prove it (F2-AC8, F2-AC9); the hazard is removed when FE-s-2 lands, and the row stays ARMED until the L9 remediation records DISARMED.",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
        "status": "GROUNDED",
        "evidence": [
          "portal/src/pages/InvestorReporting/__tests__/fe-s-1/node-builtins.d.ts@0322a04a4d (portal repo) -- declares `export interface Dirent` inside `declare module 'node:fs'`; the only name in the two shims that would merge against @types/node 24.11.0 (installed, excluded by tsconfig.app.json types: [\"vite/client\"])",
          "org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-2.route-shell-header-search.md -- amended this commit: the shim file added to <paths>, F2-AC8 (DIRENT_NAME=False) and F2-AC9 (fe-s-1 tests 0 fail) added, expected_criteria 9",
          "the alternative -- editing portal/tsconfig.app.json types -- was not taken: it changes what every portal file sees and is not this project's surface"
        ]
      },
      "spec_asserts": "IRPT_FNTEND-W1-S1: ARMED, disarm_owner 2.0.0_SA_COO~F; a later addition of @types/node to the tsconfig types array would break a green typecheck on an edit nobody would connect to the fe-s-1 folder.",
      "world_is": "The collision has exactly one carrier, the `Dirent` interface name; overload merging on readdirSync/readFileSync/fileURLToPath is legal under either state of the types array. Removing the name makes the shim safe whether or not @types/node is ever loaded. The act is granted to FE-s-2 and graded there; this row records the assignment so L9 can graduate W1-S1 and record the disarm.",
      "disposition": "UNDER_INVESTIGATION"
  },
  {
    "id": "IRPT_FNTEND-W1-S3",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-10T22:35:00Z",
    "one_line": "TO-FE-s-2 names PageThemeProvider as an export of portal/src/components/PageHeaderVariants.tsx; that file exports only PageHeaderCleanBadge, and PageThemeProvider is defined in portal/src/contexts/PageThemeContext.tsx, which is where this cell imports it from.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-FE-s-2 cell FE-s-2, Page shell: \"`PageThemeProvider` and `PageHeaderCleanBadge` from `portal/src/components/PageHeaderVariants.tsx`\".",
    "world_is": "portal/src/components/PageHeaderVariants.tsx is 63 lines and has exactly one export, `PageHeaderCleanBadge`. `PageThemeProvider` is defined at portal/src/contexts/PageThemeContext.tsx:12 and every one of the 15 portal pages that uses it imports it from '@/contexts/PageThemeContext' (comp-find '<PageThemeProvider': 29 hits, 21 SURFACED, across 1034 files scanned). The page shell therefore imports PageThemeProvider from @/contexts/PageThemeContext and PageHeaderCleanBadge from @/components/PageHeaderVariants -- the two named components, from the two real paths. No file outside the grant was written; both are import-only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/PageHeaderVariants.tsx (portal repo @6b614a5a) -- sole export `export const PageHeaderCleanBadge: FC<PageHeaderProps>`; no PageThemeProvider identifier in the file",
        "portal/src/contexts/PageThemeContext.tsx:12 @6b614a5a -- `export function PageThemeProvider({ children, accentColor })`",
        "comp-find '<PageThemeProvider' --limit 15: DENOMINATOR 29 hit(s) across 1034 file(s), including SecurityScanner.tsx:57, ModelPortfolios.tsx:1258 and Positioning.tsx:499, all of the form `<PageThemeProvider accentColor=...>` with the import from '@/contexts/PageThemeContext'",
        "portal typecheck after the import: bun run typecheck rc=0, and ./node_modules/.bin/tsc -b --noEmit --force rc=0 (the build-mode cache is shared through the node_modules junction, so the forced run is the state read)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Form only: the order names the right two components and one wrong path. Nothing about the cell changes -- the shell composes PageThemeProvider > PageHeaderCleanBadge exactly as SecurityScanner.tsx does. Recorded so a later reader of the order does not go looking for an export that is not there."
  },
  {
    "id": "IRPT_FNTEND-W1-S4",
    "project": "IRPT_FNTEND",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_IRPT_FNTEND~1",
    "surfaced_at": "2026-09-10T22:38:00Z",
    "one_line": "PageSurfaceControl's `as=\"dropdown\"` shape renders WHITE text on a TRANSPARENT background directly on the silver canvas -- measured on the component's OWN demo route as well as on this cell's header -- which is the exact state the colour law forbids, and the control is on this order's do-not-edit list.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~F",
    "spec_asserts": "TO-FE-s-2 requires the firm dropdown to be `PageSurfaceControl` with `as=\"dropdown\"`, lists PageSurfaceControl.tsx as IMPORTED, never edited, and binds the cell to the colour law: \"No light text (text-white*, text-{color}-300) or light button (bg-white/N) directly on the silver canvas\". F2-AC7 is graded at L9 on \"nothing light sits on the silver canvas\".",
    "world_is": "The dropdown branch's own classes say bg-[hsl(var(--primary))] text-white, but the COMPUTED style of the rendered <select> is background-color: rgba(0, 0, 0, 0) with color: rgb(255, 255, 255) on a body background of rgb(195, 202, 218) -- white on silver, roughly 1.35:1. The button and toggle-group branches of the SAME component compute background-color: rgb(96, 60, 226) with white text and are correct. The defect is the control's, not this cell's usage: it reproduces identically on /dev/page-surface-control, the component's own demo route, which this cell does not touch. The background-image (the white chevron data-URI) computes to `none` on the same element, i.e. BOTH bg-* utilities on that branch are absent from the computed style; the cn()/tailwind-merge conflict group for bg-* is the likely mechanism and is INFERRED, not measured. No remedy taken: PageSurfaceControl.tsx is outside this order's <paths> and on its reuse list.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DOM computed-style read (playwright, .scratch/psc-contrast.mjs) on /dev/page-surface-control: SELECT \"49 Financial...\" bg=rgba(0, 0, 0, 0) color=rgb(255, 255, 255) bgImage=none; BUTTON \"Apply filter\" bg=rgb(96, 60, 226) color=rgb(255, 255, 255); BUTTON \"1Y\" bg=rgb(96, 60, 226); CANVAS rgb(195, 202, 218) -- 9 controls read, 1 of 1 select affected",
        "same instrument on /investor-reporting with fe-s-2-default.json: SELECT \"Global (All)...\" bg=rgba(0, 0, 0, 0) color=rgb(255, 255, 255), canvas rgb(195, 202, 218) -- 4 controls read, identical values, so the two pages differ in content and agree on the control",
        "second instrument, the screenshot: fe-s-2_page_1440.png and .scratch/psc-demo.png both show a pale chip with white text where the demo page's own prose claims 'Contrast gate: WCAG AA >= 4.5:1 against silver page bg. White text on hsl(var(--primary)) indigo'",
        "portal/src/components/ui/PageSurfaceControl.tsx @6b614a5a -- the dropdown branch passes cn(controlVariants({variant,size}), 'pr-7 appearance-none bg-no-repeat bg-[right_0.5rem_center]', \"bg-[url(...)]\", className) to the <select>; the button branch passes cn(controlVariants({variant,size}), className) with no second bg-* utility"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "ARMED because it is not this page's bug: every page that puts this shape on the silver canvas ships an unreadable control, and the demo route that exists to certify the contrast shows the failure while asserting the pass. Disarm needs an owner of portal/src/components/ui/PageSurfaceControl.tsx (one line: give the <select> its background-color outside the conflicting bg-* group, then re-read the computed style). This cell renders the control exactly as the order specifies and does not work around it -- a local override here would hide the defect on the one page that measured it."
  }
]
```
