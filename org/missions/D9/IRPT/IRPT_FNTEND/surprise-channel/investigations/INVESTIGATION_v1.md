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
  }
]
```
