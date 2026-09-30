# DSGN_IRPTV1 post-crash relaunch: state from artifacts, residue, FAST item 36 (W2-07) -- 2.0.0_SA_COO~D

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE, DEPLOY

**Date:** 2026-09-30 13:05Z to 14:2xZ
**Task Order:** DSGN_IRPTV1 under a FAST lease (/closer-drive), post-crash relaunch (MSTR brief
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAUNCH_BRIEF_20260930_130xZ_POST_CRASH.md`); no numbered TO
**Status:** IN PROGRESS (items 36 + 37 on origin DEV 1d7b8feb; next item W2-19)

---

## Objective

Relaunch after the 07:52Z reboot: assess this lane's state from commits and logs, clean up residue, continue
`/canonical-drive` on DSGN_IRPTV1 (the lease reads FAST, so the tick body is `/closer-drive`).

## Work Done

1. **Startup:** registered `2.0.0_SA_COO~D` (PID 23724), /watcher armed (b8s9nhnf2 -> buipslyyw -> bavqpmkwj, script
   pid 12096), CTO 103204 (annex 17c) acked, delivery ledger 2 of 2 READ, zero crons, session serial file written,
   owned-paths hook already wired, comp-tools 104 of 104 on PATH.
2. **State from artifacts:** last commits 2c8d4ad08b / c45edc420e / 42bb20c39d; portal DEV 44fd5f42 = origin; 84 of 84
   DSGN_IRPTV1 task orders terminal; no `.open_deploys/` entry names this seat (14 scanned); no `index.lock`; no worker
   worktree of this lane; 0 ARMED / 0 OPEN surprise rows by disposition (231 rows). Lease read FAST (presence-extended;
   `org/mcp/presence/laptop.last`).
3. **Residue:** 5174 dead after the reboot -> restarted detached (`bun run dev:live --port 5174`, pid 25396; a first
   start on 5173 was stopped). STATUS.md stale at item 35 -> overwritten (AF-1 5c7eead8 and AF-2 44fd5f42 recorded).
4. **FAST item 36 (W2-07):** after Generate the ISSUED request opens in the page's own dialog (status in words, report
   sections when READY) and "Your analysis requests" re-lists from the first page. `requestToOpenAfterSubmit`
   (composer.ts), `onSubmitted` (GenerateComposer), `openRequest` (OwnedRequestHistory), wired in AnalysisTab.
   Portal `a20b5a60`, pushed to origin DEV 13:58Z under the lease (VALGATE pre-push passed).
5. **DEV CI read + FAST item 37:** CI run 36725618787 (a20b5a60) FAILURE at Run ESLint, as every DEV push since 620ea953.
   Local `bun run lint` reproduces six errors in three files; the four in this lane's surface (iv-e-106 no-control-regex,
   iv-e-116 no-regex-spaces) are fixed at portal `1d7b8feb` (origin DEV 14:19Z; lint 6 -> 2 errors). The two remaining
   are `SecurityAnalysis/components/HeaderBrief.tsx:47-48`, a literal 0x08 byte inside two regexes since the site-Z
   worker commit cb25695b -- outside this lease's surface; row DSGN_IRPTV1-S41 names DSGN_AMGTV1's seat as the owner.
6. **CTO 103252 read and acked:** IRPT_DASHBD PRD v0.1 @2cb022f549, workstream F is this seat's; C-LEASE + ruling 6.7 read.
   F's round-1 cell (the Performance chart reading `series`) is a closer-drive item HERE once ~P lands the series
   contract; measured absent at 14:1xZ, so it is parked in STATUS.md's next-list at position 0.

## Compiler Tools

| Tool | Command | Result | Notes |
|---|---|---|---|
| comp-read | `.tools/drive-mode.py --for "presence"`; `IRPT_DASHBD_PRD.md --for "C-LEASE ..."` | PASS | presence rule + C-LEASE located |
| comp-surprise | `--project DSGN_IRPTV1 --json` (to a scratch file) | PASS | 231 rows; state is `disposition`, not `state` |
| comp-find (rail) | two pipe-receiver denials, re-run with native flags | PASS | `--width` / file output instead of a pipe |
| typecheck | `bun run typecheck` | PASS | rc=0 at a20b5a60 |
| eslint | four touched files | PASS | 0 errors, 14 pre-existing warnings |
| bun test | `iv-e-116.generate-journey.test.tsx` | PASS | GENERATE-JOURNEY-OK |
| IR suite | `timeout 590 bun test ./src/pages/InvestorReporting` x2 | PARTIAL | 920 pass / 18 known fail (five + S40's 13) once the regenerated `contracts/wire/*` were restored; iv-e-116 green |
| real run | `.runtmp/w2-07-generate-journey-driver.mjs 5174` (fixture plane) | PASS | GENERATE-JOURNEY-REAL-OK; shot read |
| gh | `gh run list/view` | READ | DEV CI "Run ESLint" step FAILURE on every DEV push since 09-29 21:06Z |

**What worked:** the fixture-plane driver recipe (auth stub + CORS + longest-key route match) extended with the five
journey routes and the AD-11 search stub; `safe-commit.sh` from the portal dir with explicit paths.
**What failed:** the first 5174 start came up on 5173 (`dev:live` defaults to 5173; `--port 5174` is required); the
first hand-typed submission envelope was refused (ENVELOPE_STATUS) -- the fixture's own status block passes.
**Gap found:** an IR suite run rewrites `contracts/wire/*` on disk (gen-wire tests): 23 files EOL churn, two carry the
ComparisonCatalogue wire (row S40, ~Y's). Restore to HEAD after each run; never commit them from this lane.

## Deployment Sequence + Verification

- Portal DEV: `a20b5a60` (13:58:47Z) then `1d7b8feb` (14:19:15Z) pushed by the lease seat; `git ls-remote origin refs/heads/DEV` read `1d7b8feb3172`.
- CI run 36725618787 for a20b5a60: "Lint, Type Check & Build" FAILURE at "Run ESLint" (the same step has failed on
  every DEV push since 620ea953 on 09-29 21:06Z); reproduced locally, four of six errors fixed at 1d7b8feb, the two
  out-of-surface ones are row S41's; the run for 1d7b8feb stays red until that pair lands.
- No PROD change. No AWS change.

## MCP Traffic (significant)

CTO 103204 (annex 17c law edit) acked; CTO 103252 (IRPT_DASHBD L4 landed, F is ~D's; read C-LEASE + 6.7) acked. No sends.

## Blockers

None on this lane. Parked: IRPT_DASHBD F round-1 chart (un-parks on ~P's series contract + served file); W2-04/05
(~Y catalog read); W2-12/14 (~M class release under CTO 103168); W2-13 industry (served field); W2-15 (CTO F7-AC4);
W2-06 words (CTO seat decision); S40 portal half (~Y).

## Current State

- portal PROD ba8e971f (v2.1.191); origin DEV a20b5a60 (item 36 on AF-2 44fd5f42). 5174 serves the main checkout.
- STATUS.md overwritten @ this session (pins, claims, next-list, parked lines, limits).
- Workspace: this log, `drive_log_20260930T13Z_andrew.md`, STATUS.md and `deliverables/2.0.0_SA_COO~D/item36/`
  committed LOCAL on CLOUD (hash in the drive log); push is 0.0.0_AB_MSTR's.

## Next Steps

- [DSGN_AMGTV1, site-Z 2.0.0_SA_COO~D] HeaderBrief.tsx:47-48 two-byte fix (row S41) -> DEV CI green again.
- [this lane] FAST item 37: W2-19 (one source line from `sourceVendorKeys`, served coordinate as the fallback in words).
- [Andrew] Re-smoke DEV a20b5a60 on 5174; PROD promote call; FCASH fold scope.
- [2.0.0_SA_COO~P] `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` + a served `series.json.gz` -> un-parks F's chart item here.
