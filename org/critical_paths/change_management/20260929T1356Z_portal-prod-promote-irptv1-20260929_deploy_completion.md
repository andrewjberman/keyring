# DEPLOY LEDGER -- portal DEV->PROD promote (DSGN_IRPTV1 + AD-10 account_masks reader)

**Status:** CLOSED -- nothing stranded -- closed 20260929T142xZ by `0.2.0_DT_PortfolioAnalytics~P`

Production serving `9a8f6c71` / `portal-v2.1.190`, `deploy.yml` run `36580348558` conclusion=success, served
bundle read admitting `account_masks`. ONE non-terminal item, owned and named: the workspace pointer commit
`06f4c5d7ce` is LOCAL (see `## Push state`), because GATE 5 keeps WORKSPACE branches integrator-only. That is
out-of-lane, not half-landed: the portal act is complete and verified in the world.

- **Owner:** `0.2.0_DT_PortfolioAnalytics~P`
- **Authority:** Andrew-direct 2026-09-29 ~13:3xZ, verbatim answer: *"Yes, seat DT and promote (Recommended)"*
  on the card *"Promote portal DEV 27eae57a to PROD now? It is 136 commits ahead of PROD (a0314f22, 09-26),
  mostly ~D's investor-reporting design work ... It now gates two release orders: ~M's Holdings CATEGORY step
  and AD-10's directory reader."*
  Record: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260929_133xZ_PORTAL_PROD_PROMOTE_DEV_27eae57a.md`
- **Lane note:** `0.2.0_DT_PortfolioAnalytics~P` IS a DT serial, so `/prod-deploy` Step 0 and GATE 5
  (`.tools/hooks/never-rules-gate.sh`) admit it directly. No `# never-override:` line is required on the
  PROD push. The DEV push case does not arise -- local DEV is not ahead of origin/DEV.

## SCOPE QUESTION -- RESOLVED ~14:00Z: payload is DEV 18899c96

Andrew's second word, verbatim: **"Promote 18899c96 (Recommended)"**. It covers exactly `18899c96`, **nothing
later**. Record amended at `@af463119f2` (AMENDMENT section, *"the target is DEV 18899c96, on Andrew's second
word"*); relayed to this seat by `1.0.0_SA_CTO` msg **102829** at 14:00:47Z because `0.0.0_AB_MSTR` is barred
from Tier-2 writes. Acked READ by this seat. The record notes MSTR's stale `ls-remote` was the error, that MSTR
did not widen the word but asked, and that the DT did not adjudicate.

**Re-measured immediately before the merge:** `origin/DEV` still `18899c96748e` -- the freeze held, no second
passenger. The merge therefore names the EXPLICIT SHA, not the moving `origin/DEV` ref, so a DEV push racing
the merge could not widen the payload.

### The question as originally raised

The record authorizes `27eae57abe`. `origin/DEV` measured at 13:47Z is `18899c96748e`, ONE commit ahead:

| | |
|---|---|
| passenger | `18899c96` `2.0.0_SA_COO~D` 2026-09-29T13:18:15Z |
| subject | build(DSGN_IRPTV1 FAST item 29): DirectoryEntry wire type regenerated from the committed schema -- account_masks (AD-10) |
| ancestry | `27eae57a` IS an ancestor of `18899c96` (measured, `merge-base --is-ancestor`) |
| timing | landed 13:18Z, BEFORE the ~13:3xZ card -- the card's 12:14Z `ls-remote` was already stale |
| count | `origin/PROD..origin/DEV` = **137**, not the card's 136 |

The passenger serves the exact reason the record names (the AD-10 account_masks reader, msg 102776). CTO log
`50469a2a6c` reads *"portal DEV 18899c96 approved"*. Per CLAUDE.md *"surface, do not adjudicate"*, the DT did
NOT pick the payload: asked to `0.0.0_AB_MSTR` at 13:50:51Z (msg 102825), merge and push HELD until answered.

## Blast radius

Portal frontend only (the `Opal-Capital/portal` repo). No backend, no Lambda, no Terraform, no IAM, no S3 key,
no workspace pipeline path. 137 commits, predominantly `2.0.0_SA_COO~D`'s DSGN_IRPTV1 investor-reporting design
work recorded item by item in that project's `STATUS.md`, plus `6c163889f4` (~M's Holdings CATEGORY step) and
the AD-10 DirectoryEntry `account_masks` reader.

| Key | Pre-act value | Rollback |
|---|---|---|
| `origin/PROD` (portal) | `a0314f22a536ec018b1b0a00e349b04bf33cc721` | `git push origin a0314f22:PROD --force-with-lease`, then re-run `deploy.yml` |
| `portal/DEV` | `18899c96748e171f635c4a5955cfdcd24040c273` | forward-only; NOT rolled back with PROD |
| workspace submodule pointer (`CLOUD`) | pending Step 6 | `git checkout -- portal` |
| local `portal` ref `refs/heads/PROD` | was `36a37afce` (STALE dry-run pollution) | re-asserted to `a0314f22` at Step 3 |

**Downstream consumers gated on this act:** the AD-10 directory re-mint is HELD until PROD serves the reader
admitting `account_masks` -- a PROD reader without it REFUSES the new key and client search fails. The
investor-reporting bundle skip (msgs 102500 / 102812) stays in force until the served PROD bundle is read
admitting `account_masks`.

## Freeze window

Declared 13:52Z to `2.0.0_SA_COO~D` (id 102826) and `2.0.0_SA_COO~M` (id 102827), both DELIVERED (2 DELIVERED /
0 QUEUED / 0 REFUSED, denominator 2). The promote merges LIVE `origin/DEV` at merge time, not a frozen
snapshot, so any DEV push inside the window rides in unverified. Released at Step 8.

## Steps -- DESIRED / APPLIED

| # | Step | State |
|---|---|---|
| 0 | DT-only gate; `$WS` derived, not typed; inbox pulled (empty, no `[STOP]`); freeze declared | APPLIED |
| 1 | DEV tree clean + branch `DEV`; local NOT ahead of `origin/DEV`, so no DEV push (Step 1a not entered) | APPLIED |
| 2 | `bun run typecheck` -> `tsc -b --noEmit` rc=0, ZERO errors | APPLIED |
| 2b | DEV CI green, enumerated BY headSha: `18899c96` run `36574405728` `CI - Build & Validate` conclusion=success; `27eae57a` run `36560490714` success | APPLIED |
| 3 | `update-ref refs/heads/PROD refs/remotes/origin/PROD` -- caught stale local PROD `36a37afce` | APPLIED |
| 4a | ephemeral worktree `.runtmp/portal-promote-20260929T135632Z` added at PROD `a0314f22` | APPLIED |
| 4b | `bun install` FOREGROUND in the worktree -- 377 packages, rc=0, 208.35s | APPLIED |
| 4c | `git merge --no-ff 18899c96...` (EXPLICIT sha, not the moving ref) -> merge commit `9a8f6c71efb2`, rc=0, no conflicts | APPLIED |
| 4d | parity gate EMPTY vs BOTH `origin/DEV` and `18899c96`; positive control vs PROD base non-empty (183 files, +17379/-3021) so the empty is a true empty | APPLIED |
| 5a | `git push origin PROD` -> `a0314f22..9a8f6c71`, rc=0. VALGATE D-1 PASS (no static partner adapters changed); paired-provenance scan OK; pre-push `tsc -b --noEmit` PASS | APPLIED |
| 5b | `deploy.yml` run `36580348558` conclusion=success, enumerated BY headSha `9a8f6c71` (n=1, the only workflow on that sha) | APPLIED |
| 5c | tag `portal-v2.1.190` PEELED: object `b95ab8cecf21`, commit `9a8f6c71` == `origin/PROD`. The object sha differs from the commit -- the exact `ls-remote` misread trap | APPLIED |
| 5d | SERVED-ARTIFACT verification (below), not CI self-report | APPLIED |
| 6 | pointer commit `06f4c5d7ce` on `CLOUD`, author `0.2.0_DT_PortfolioAnalytics~P`, 1 file, via `safe-commit.sh -F`; msg-verify MATCH len=1235. **LOCAL -- push is integrator-only** | APPLIED (local) |
| 7 | `worktree remove` FAILED "Filename too long" (documented Windows long-path class); `worktree prune` OK, 0 promote worktrees tracked; physical `.runtmp/portal-promote-20260929T135632Z` persists, gitignored and inert. Main tree on `DEV`, cwd at workspace root | APPLIED |
| 8 | RAVC report to COO `~D`/`~M`, freeze released, CLOUD push handed to `0.0.0_AB_MSTR`, session log | APPLIED |

## Served-artifact verification (CLAUDE.md: never trust a producer's rc=0)

CI success is the producer's self-report. The downstream gate is whether PROD SERVES a reader admitting
`account_masks`, so that was read from the served bytes:

- Served entry `https://opalinvest.dev/assets/index-27CK7J5N.js`, `Last-Modified 2026-09-29T14:10:19 GMT`
  (the new build; the push was ~14:07Z).
- **First read was WRONG and is recorded as the instrument lesson:** `account_masks` = **0** occurrences in the
  entry bundle. The app is CODE-SPLIT (51 chunk references), so the entry bundle is the WRONG DENOMINATOR --
  an out-of-corpus zero, not an absence. The negative control also returned 0, which proves nothing; the
  POSITIVE control (`DirectoryEntry` = 0 too, while `InvestorReporting` = 1) is what exposed it.
- Correct sweep: all **51 of 51** referenced chunks fetched (denominator printed, zero fetch failures).
  **1** chunk contains the token: `resolveBundle-BVyRHWDP.js`, `Last-Modified 14:10:19 GMT`, 210,700 bytes.
- Served bytes, quoted from the chunk:
  - `...,"revision","cohort"],["contract_version","account_masks"]),...` -- the key is in the OPTIONAL-keys array
  - `...||!uI(e.account_masks)||...` -- the validator actually calls the mask check
  - controls in that chunk: `masked_discriminator` = 1 (positive), `zzz_absent_token` = 0 (negative)

**Therefore the AD-10 precondition is MET:** the served PROD reader admits `account_masks`, so it will not
refuse the new key and client search will not fail. The investor-reporting bundle skip (msgs 102500 / 102812)
has its stated release condition satisfied -- lifting it is `2.0.0_SA_COO~D`/`~M`'s act, not the DT's.

## Push state (MEASURED at report time, `git ls-remote`)

| Ref | State |
|---|---|
| `origin/PROD` (portal) | **`9a8f6c71`** -- ON ORIGIN, pushed by this seat, CI-verified |
| `portal-v2.1.190` | ON ORIGIN (CI auto-tag), peeled to `9a8f6c71` |
| workspace `CLOUD` | **LOCAL `06f4c5d7ce`**; `origin/CLOUD` = `15655f4a25` (ls-remote read) |

`/prod-deploy` Step 6 prints `git push origin CLOUD`, but that line is **not executed by a DT**: Step 0's own
GATE 5 clause admits a DT pushing `PROD`/`DEV` **in the portal repo only** -- *"Workspace branches and any
`pull` stay integrator-only"* (also org/XXX.md SHARED-BRANCH LAW). The two lines of the skill disagree; the
narrower one governs, so the pointer commit was left LOCAL and handed to `0.0.0_AB_MSTR`.
**Owner of the remaining act: `0.0.0_AB_MSTR` -- carry `06f4c5d7ce` to `origin/CLOUD` at its next window.**
Surfaced as a defect in the skill text, not worked around silently.

## Instrument notes (measured this session)

- `gh -R Opal-Capital/portal run list --branch DEV` returned rows whose newest was 2026-09-11 `5b959f63`
  conclusion=failure, which read as "DEV CI dead 18 days and red". The UNFILTERED `run list` shows DEV CI
  running green hourly through 2026-09-29T13:20. **The `--branch` filter's result was stale/wrong, and a
  wrong-filter read is indistinguishable from a true finding** -- the same class `/prod-deploy` Step 5 flags for
  `-R`. Enumerate by `headSha` against an unfiltered list; positive-control every empty or surprising result.
- `gh repo view` takes the repo as a POSITIONAL, not `-R` (`unknown shorthand flag: 'R'`), unlike `gh run list`.

## Close-out

Closed 2026-09-29T142xZ -- **LANDED AND VERIFIED.** Production serves `9a8f6c71` / `portal-v2.1.190`;
`deploy.yml` `36580348558` conclusion=success; the served chunk admits `account_masks`. 10 of 10 promote steps
APPLIED. Portal main tree never left `DEV`. Nothing half-landed.

One act remains and it is OUT-OF-LANE, not stranded: workspace pointer `06f4c5d7ce` is LOCAL, owner
`0.0.0_AB_MSTR`. Should it never be carried, the consequence is bounded to a stale submodule pointer in the
workspace record -- production is unaffected, and the rollback row above does not depend on it.

Freeze released to `2.0.0_SA_COO~D` and `2.0.0_SA_COO~M` at Step 8.
