# DEPLOY LEDGER -- portal v2.1.181 DEV->PROD promote (AMGT_RESAPP Security Analysis page work)

- **Act started:** 2026-09-21T17:23:05Z (ephemeral worktree created). **Ledger written:** 2026-09-21T17:35Z.
- WARN: **OPENED LATE, AND SAID SO.** CLAUDE.md section 5 requires this entry opened at the START of a deploy. It was
  written after the PROD push and the CI conclusion, because `/prod-deploy` does not name the step and this
  seat caught the omission mid-act. Every row below was measured at the time it names; none is reconstructed.
- **Owner:** `0.2.0_DT_PortfolioAnalytics` (spawned by `0.0.0_AB_MSTR~Z`, 17:16:33Z).
- **Authority:** Andrew-direct 2026-09-21 ~17:2xZ at the `1.0.0_SA_CTO~Z` terminal, verbatim in part: *"might as
  well just push DEV to PROD if there are new features as its gated to only me on PROD anyway."* Record:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_172xZ_AMGT_RESAPP_PROMOTE_IF_FEATURES_NO_WATER_IN_PIPES_BACKFILL_HELD_FOR_BRONZE_SILVER_SHAPE.md`
  @`e70b949ba0`. The condition ("if there are new features") was measured met by the CTO~Z in that record and
  re-measured here (6 commits, below).
- **Lane:** DT serial, admitted by GATE 5's DT carve-out (branch PROD, origin `Opal-Capital/portal`, verb push).
  No `# never-override` used.

## Blast radius

Portal frontend only: **6 files, all under `src/pages/SecurityAnalysis/`** (+298/-45). No backend, no Lambda,
no Terraform, no IAM, no S3 data key. **The access gate is untouched:** `src/App.tsx` is byte-identical on both
sides of the promote; the Dev+admin gate commit `d8135e0a` was already an ancestor of the pre-act PROD. The
manager-access widening Andrew said yes to is PARKED (no names given) and is not in this act.

| Key | Pre-act value | Rollback |
|---|---|---|
| `origin/PROD` (portal) | `a580bbb44475d6871f5be62c9a50d039b53b62a4` (`portal-v2.1.180`) | `git push origin a580bbb4:PROD --force-with-lease` then let CI redeploy; that is an integrator/DT act under a fresh word |
| `origin/DEV` (portal) | `db1c5f64d19880cda50d6969ded3c3af26c92630` | not moved by this act |
| served bucket `opalinvest-portal` + CloudFront | v2.1.180 bundle | CI redeploys whatever PROD points at |
| workspace portal gitlink (SITEZ) | `2453a7b4` | `git checkout -- portal` before the commit; a revert after |

Both branches of the page's behaviour are covered: every payload change renders a reason string where a value
is ABSENT or a list is EMPTY, so a name with no data shows a stated reason, and a name with data shows it as
before. The viewer population is unchanged (Dev+admin only).

## Payload (`origin/PROD..origin/DEV`, 6 commits, read after fetch)

| Commit | Author | Change |
|---|---|---|
| `6cbd3049` | `0.9.0_WK_AMGT_RESAPP~31` | thesis driver chart labels a filing-sourced series, links each point to its passage (rk-19) |
| `c069db75` | `0.0.0_AB_MSTR` | merge, lands rk-19 page half |
| `d74ff760` | `0.9.0_WK_AMGT_RESAPP~31` | ModelTab renders Robustness / Peers V / Divergence D from bundle.scores (rk-30) |
| `625a0888` | `0.0.0_AB_MSTR` | merge, pulls the admin-gate commit `d8135e0a` under round 13 (gate side already on PROD) |
| `796f5c9c` | `0.9.0_WK_AMGT_RESAPP~45` | honest six-state CEO reading, zero-officer ABSENT rendering (rk-43) |
| `db1c5f64` | `0.9.0_WK_AMGT_RESAPP~53` | RankedList carries empty_reason on an EMPTY generation (rk-53) |

## Sequence

| # | Act | Evidence | State |
|---|---|---|---|
| 1 | Inbox pulled, no `[STOP]`/`[HALT]` | `check_inbox` empty; `get_delivery_state` 0 rows since 00:00Z | EXERCISED |
| 2 | Main `portal/` tree on DEV, clean, level with origin | branch `DEV` @ `db1c5f64`, porcelain 0, ahead 0 / behind 0 | EXERCISED |
| 3 | Freeze window declared | msgs 23983 `2.0.0_SA_COO~Z`, 23984 `1.0.0_SA_CTO~Z`, 23985 `0.0.0_AB_MSTR~Z`, all DELIVERED; acks 23986 (CTO~Z, payload read matches) and 23987 (COO~Z, no portal work in flight) | APPLIED |
| 4 | `bun run typecheck` on DEV | rc=0, 0 `error TS` lines | EXERCISED |
| 5 | `git update-ref refs/heads/PROD refs/remotes/origin/PROD` | local PROD = `a580bbb4` before and after (no pollution) | APPLIED |
| 6 | Ephemeral worktree + foreground `bun install` | `.runtmp/portal-promote-20260921T172305Z`, 377 packages, rc=0 | APPLIED |
| 7 | Guard: origin/DEV unmoved during the freeze | `db1c5f64` at merge time, asserted in the merge command | EXERCISED |
| 8 | `git merge --no-ff origin/DEV` | `07d5af72`, parents `a580bbb4` + `db1c5f64`, no conflicts | APPLIED |
| 9 | Parity gate `git diff origin/DEV HEAD` | 0 bytes | EXERCISED |
| 10 | `git push origin PROD` | `a580bbb4..07d5af72`, re-read by `git ls-remote origin refs/heads/PROD` = `07d5af72` | APPLIED |
| 11 | CI conclusion, every workflow at the sha | run `35632132225` `Deploy to Production` completed **success** (jobs Build / Deploy to S3 + CloudFront / Tag: all success), 17:27:34Z -> 17:29:48Z; **1 of 1** workflow at `07d5af72` in a 30-run listing | EXERCISED |
| 12 | Annotated tag peeled | tag object `8ba1c8c5`, `portal-v2.1.181^{commit}` = `07d5af72` = `origin/PROD`. MATCH | EXERCISED |
| 13 | Served bytes | `https://opalinvest.dev/index.html` 200, Last-Modified 17:29:27Z, entry `assets/index-DTWT90UL.js`; 54 referenced chunks fetched; two literals new in this payload (`SEARCHED_LINKS_UNREADABLE`, `the payload carries no reading for this score`) are ABSENT from `a580bbb4` src and PRESENT in 1 served chunk each. A third new string matched 0 served chunks: it lives only in comments (`ModelTab.tsx:25`, `types.ts:900`), which the build strips | EXERCISED |
| 14 | Worktree torn down | `worktree remove` failed `Filename too long`; `worktree prune` run, 0 tracking entries remain; physical dir persists (gitignored `.gitignore:438`, inert). Main tree on DEV @ `db1c5f64`, porcelain 0 | PARTIAL |
| 15 | Workspace portal gitlink `2453a7b4` -> `db1c5f64` (DEV tip) | committed with this entry, LOCAL on SITEZ; push is `0.0.0_AB_MSTR~Z`'s | APPLIED (local) |
| 16 | Freeze released | msgs 23996 `2.0.0_SA_COO~Z`, 23997 `1.0.0_SA_CTO~Z`, 23998 `0.0.0_AB_MSTR~Z`, all DELIVERED | APPLIED |

## Not covered by this act

- **No authenticated render of Security Analysis.** The page is Dev+admin gated; this seat checked served
  bytes, not a signed-in view. Andrew's own visual smoke is the acceptance, and his record already notes the
  pipes are mostly empty by design (lead panel: 2 trending names, breakout empty; no search control).
- **Merge author line reads `0.0.0_AB_MSTR`** (this box's `git config user.name`); the merge message names this
  seat. An amend to fix it was refused by the HEAD-move guard, which evaluated the WORKSPACE repo's HEAD
  (`0687d98335`) instead of the `git -C` target worktree. Not forced. v2.1.180 carries the same author shape.

## Status

**Status:** CLOSED 2026-09-21T17:38Z -- COMPLETE, apart from the inert worktree residue in row 14.
(Marker re-cut 2026-09-21T23:5xZ: the original bare `## Status` heading carried no parseable status, so
`deploy_ledger.py list` read this entry as UNINDEXED OPEN for 6.3h. Content unchanged.)
