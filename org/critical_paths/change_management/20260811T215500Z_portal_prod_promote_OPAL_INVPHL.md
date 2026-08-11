# DEPLOY-COMPLETION LEDGER — portal DEV -> PROD promote (OPAL_INVPHL)

**Opened:** 2026-08-11T215500Z
**Owner:** 0.4.0_DT_ClientPlatform (DT lane, `/prod-deploy`)
**Status:** ⛔ **BLOCKED AT LEG 1 — NOTHING BEGUN, NOTHING STRANDED**
**Authority:** Andrew-direct ~2148Z at the DT terminal, VERBATIM: *"i like it get this build
promoted to PROD"*, after he smoke-tested the build on localhost:5175 against the live backend.
COO clearance 215124Z (their 195948Z "do not promote" scope note SUPERSEDED by the later
sovereign word).

## Scope

| | |
|---|---|
| Promote | portal `DEV` -> `PROD` |
| Riders | **exactly 2 commits, both mine, both routine portal work** — `84f6b3e2` (OPAL_INVPHL TO-1 model modal), `335dd198` (TO-2 Philosophy page). `git log origin/PROD..HEAD` = 2; author census = 1 (0.4.0_DT_ClientPlatform). No served-key change, no data-shape change, no other seat's half-finished surface. This is what Andrew clicked through. |
| Pre-merge checks (COO 215124Z) | **BOTH PASS.** `/cma` -> `/philosophy` redirect confirmed IN THE COMMIT at `git show 335dd198:src/App.tsx:425` (outside `ProtectedRoute`, so a bookmarked `/cma` forwards rather than hitting deny-by-default). `firmAccess.ts` allowlist = 4 `/philosophy` entries in the commit — without which `/philosophy` is a dead page for all four partner firms. |
| Typecheck | `bun run typecheck` (`tsc -b --noEmit`) rc=0 |

## Legs (7) and their state

| # | Leg | State |
|---|---|---|
| 1 | push `origin DEV` | ⛔ **BLOCKED — gate refusal, see below** |
| 2 | re-assert local PROD from origin | not started |
| 3 | ephemeral worktree + `bun install` | not started |
| 4 | merge `DEV->PROD` `--no-ff` + parity gate | not started |
| 5 | push `origin PROD` -> CI deploy + tag | not started (**would hit the same gate**) |
| 6 | workspace gitlink bump + push `origin CLOUD` | not started (**would hit the same gate**) |
| 7 | worktree teardown + confirm main tree on DEV | not started |

**NOTHING HAS LANDED. NO LEG IS HALF-DONE.** Main `portal/` tree is on **DEV** and clean of
tracked modifications; local PROD untouched; no worktree created. This ledger is open per
CLAUDE.md NEVER#7 and COO 215124Z, and is closeable at zero cost if the promote is stood down.

## The blocker

`git push origin DEV` from `portal/` was **DENIED** by
`.tools/hooks/never-rules-gate.sh` GATE 5 (LD-0367 rule 2 / LD-0368, INTEGRATOR-ONLY
push/pull on a shared branch):

> BLOCKED ... only `0.0.0_AB_MSTR` (base) / `0.0.0_AB_MSTR~Z` (site-Z) may push or pull the
> shared branch; you are `0.4.0_DT_ClientPlatform`.

The gate's own scope comment (`:490`) lists shared branches as **CLOUD/DEV/PROD/main/master**,
so `DEV` is deliberately covered — this is the gate working, not an accident of my invocation.

⚠ **STRUCTURAL CONSEQUENCE, surfaced not worked around: THREE of the canonical `/prod-deploy`
legs push a shared branch** (DEV, PROD, CLOUD). Under this gate the DT lane that OWNS
`/prod-deploy` cannot execute it end to end without the integrator. That is a collision between
two live laws, not a judgement call for me, so it is routed rather than overridden.

⚠ **I did NOT use the audited `# never-override:` escape.** The gate's own text requires
coordinating with the integrator FIRST *because the override still republishes the tree* —
a push from a non-integrator seat publishes every other seat's local commits, which is the
exact harm LD-0367 exists to prevent and which I cannot see from here.

**Routed to `0.0.0_AB_MSTR` (integrator, LIVE at time of routing) 2026-08-11T~2155Z** to either
run the pushes or authorize the override. COO + Andrew informed in the same window.

## Close-out (to be completed)

| Field | Value |
|---|---|
| PROD commit | *pending* |
| Tag `portal-vX.Y.Z` (peel-verified) | *pending* |
| CI run id + `conclusion` | *pending* |
| Workspace pointer | *pending* |
| Main tree back on DEV | *pending (never left)* |
| Closed at | *pending* |
