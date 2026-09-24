# DEPLOY LEDGER -- portal v2.1.179 DEV->PROD promote (POSN_AGGFIX + Andrew's two post-smoke items)

**Status:** CLOSED -- nothing stranded -- closed 20260916T012xZ

⛔ **FIELD ADDED 2026-09-24T05:5xZ BY THE ENTRY'S OWN OWNER (`1.0.0_SA_CTO~Z`). NO STATE CHANGED AND NO ACT WAS
PERFORMED -- this entry has been CLOSED IN ITS OWN TEXT since 2026-09-16T01:2xZ** (see `## Close-out`:
*"Closed 2026-09-16T01:2xZ -- LANDED AND VERIFIED ... Nothing half-landed"*, production serving `ff542d0a` /
`portal-v2.1.179`, CI `conclusion=success`, 10 of 10 steps APPLIED). ⛔ **BUT THE CLOSURE WAS PROSE UNDER A
HEADING RATHER THAN THIS FIELD, SO `.tools/deploy_ledger.py check --red` COULD NOT SEE IT AND HAS CLASSED THIS
ENTRY `BYPASS: UNINDEXED OPEN LEDGER` FOR 8.2 DAYS** -- *"no `**Status:**` and no close-date marker (open or
malformed)"* -- delivering a RED gate-bypass alert to the COO inbox on a **PROD promote**, the single class where a
false "half-landed" reading is most expensive. ⭐ **THE ENTRY READ CORRECTLY TO EVERY HUMAN AND WAS INVISIBLE TO
EVERY MACHINE, WHICH IS WHY 8 DAYS PASSED**: the author verified the world, wrote a careful close-out, and
re-reading what they wrote would never have surfaced the defect, because what they wrote was true.
**Cost of the fix: one line. Cost of the omission: 8 days of a false RED on a production deploy.**
- **Owner:** `1.0.0_SA_CTO~Z`
- **Authority:** Andrew-direct 2026-09-15, verbatim: *"I visually smoked the branch before the reboot
  and it looks good. The only thing I'd change is that the frontend toggle should read 'AGG' not
  'AGGREGATE'. Other than that though, everything looks good ... make that one targeted change, and
  get the PROD portal promote complete."* Plus, same session: *"a date field snuck into the
  'Portfolio Composition' title bar on the 'Positioning' page ... That date should not be in the
  header there; it is already in the footer. Please rectify that as well leading into the promote."*
- **Lane note:** `1.0.0_SA_CTO~Z` is NOT a DT serial. Admitted by `/prod-deploy` Step 0's
  explicitly-Andrew-directed clause; GATE 5 does not admit an Andrew-directed non-DT on its own, so
  the DEV push carried `# never-override: Andrew-direct 2026-09-15` on the same command (audited).
  Precedent at this same seat: `6cb3d0f6` (v2.1.176, Andrew-direct 2026-09-02).

## Blast radius

Portal frontend only. **Positioning page**, Holdings tab. No backend, no Lambda, no Terraform, no
IAM, no S3 key. The matching edge leg (`POSN_AGGFIX.TO-C1-1`, `aggregate_gate.mjs`) lives in the
WORKSPACE repo and is **NOT** carried by this promote.

| Key | Pre-act value | Rollback |
|---|---|---|
| `origin/PROD` (portal) | `edf85ce503aad961b84b5ea3b2074eb84d416a16` | `git push origin edf85ce5:PROD --force-with-lease` then re-run CI |
| `portal/DEV` | `acdb02e917f510a834c00ef33f8d4343d351f8eb` | advanced to `be8cf218` -- forward-only, not rolled back with PROD |
| workspace submodule pointer | pending Step 6 | `git checkout -- portal` |

**BOTH BRANCHES OF THE PRODUCER'S RULE ARE COVERED.** The aggregate is viewer-scoped: it renders
only when the family rolls up, the viewer passes the page's internal predicate, AND the served file
reports `status: OK` with a non-empty `current_holdings.AGG.holdings`. If the served key is absent,
stale or empty, `mergeOpalAggregate` returns the input object itself and the page renders the five
books exactly as it does on `edf85ce5` today -- i.e. the **negative branch is the current production
behaviour**, not a new failure state. No client-facing viewer gains a surface either way.

## Sequence

| # | Act | Evidence | State |
|---|---|---|---|
| 1 | Merge `wk-aggfix-1-3-portal` (worker-local, unpushed, branched off PROD) forward onto current DEV | `a4ef8853`, no conflicts | APPLIED |
| 2 | Andrew's two change items | `be8cf218`, 1 file, +10/-3 | APPLIED |
| 3 | `bun run typecheck` on the merged content | rc=0, 0 `error TS` lines | EXERCISED |
| 4 | Push `portal/DEV` | `acdb02e9..be8cf218` | APPLIED |
| 5 | Freeze window declared | msg 23316 `2.0.0_SA_COO~Z`, 23317 `0.0.0_AB_MSTR~Z` | APPLIED |
| 6 | `git update-ref refs/heads/PROD refs/remotes/origin/PROD` | local PROD = `edf85ce5` | APPLIED |
| 7 | Main `portal/` tree returned to DEV (was DETACHED at PROD -- Rule 19 violation found at start) | branch `DEV` @ `be8cf218`, clean | APPLIED |
| 8 | Merge DEV->PROD in ephemeral worktree `.runtmp/portal-promote-20260916T010633Z` | `ff542d0a` | APPLIED |
| 9 | Parity gate `git diff origin/DEV HEAD` | EMPTY (0 bytes) | EXERCISED |
| 10 | `git push origin PROD` | `edf85ce5..ff542d0a`, re-read from `git ls-remote origin refs/heads/PROD` | APPLIED |
| 11 | CI conclusion, enumerated by headSha across ALL workflows | run `35043067158` `Deploy to Production` status=completed **conclusion=success**; 1 of 1 workflow at `ff542d0a` out of a 30-run listing | EXERCISED |
| 12 | Annotated tag peeled (`rev-parse <tag>^{commit}`) vs PROD head | tag object `c17905e2c8`, `portal-v2.1.179^{commit}` = `ff542d0a` = `origin/PROD`. MATCH | EXERCISED |
| 13 | Workspace submodule pointer updated | `e85f6eb8` -> `be8cf218` (portal DEV tip) | APPLIED |
| 14 | Worktree torn down, main tree confirmed on DEV | main `portal/` on branch DEV @ `be8cf218`, `status --porcelain` empty. Worktree dirs NOT deleted -- see residue below | PARTIAL |
| 15 | FREEZE CLOSED posted | msg to `2.0.0_SA_COO~Z` + `0.0.0_AB_MSTR~Z` | APPLIED |

## Independent corroboration (different instrument)

`0.0.0_AB_MSTR~Z` (msg 23321) verified step (b) **at the remote**, not from this seat's report:
`origin/DEV be8cf218` / `origin/PROD edf85ce5` unmoved at that moment; `PROD..DEV` = 7 files,
379 insertions, **46 deletions**; drain tip `3ec1f83c` IS an ancestor of `origin/DEV`; the merge's
tree effect versus the drain is the 2 CI files ONLY. That seat first inferred from commit
author/committer lines that a different seat had pushed DEV, and withdrew the inference before
sending it: `org/git-author-override-audit.log` carries
`2026-09-16T01:03:38Z NEVER-OVERRIDE serial=1.0.0_SA_CTO~Z rule=PUSHPULL_AUTHORITY cmd=git push origin HEAD:DEV`.
**A commit's author/committer is not an oracle for who moved a ref**; the push-authority audit log is.

## Findings surfaced, NOT chased

1. **The main `portal/` tree was in DETACHED HEAD at `origin/PROD`** at session start -- a standing
   Rule 19 / `/prod-deploy` invariant-1 violation predating this session. Corrected (step 7).
2. **The POSN_AGGFIX portal work had never reached DEV.** It existed only as
   `wk-aggfix-1-3-portal` in worker worktree `C:/tmp/wk-aggfix-1-3/portal`, unpushed, branched off
   `origin/PROD` rather than `origin/DEV`. Round 1 was reported L7 TERMINAL (7/7 drained,
   `dep_stage ROUND_CLOSE`) with this leg unpublished. Surfaced to `2.0.0_SA_COO~Z` and
   `0.0.0_AB_MSTR~Z` in the freeze message; **not** adjudicated here.
3. Nine stale portal worktrees under `C:/tmp/` from completed workers. Not chased.
4. **Round 1's L8 compile / L9 adjudication / L10 slug were never run**, and the 28-row surprise
   channel carries no CVO watermark with all 28 rows at UNDER_INVESTIGATION (`2.0.0_SA_COO~Z`
   msg 23318). Andrew's ~01:0xZ "mark it complete" is an R6 close on the ENDPOINT outcomes and is a
   DIFFERENT question from the channel adjudication. **Not adjudicated here** -- surfaced to
   `3.0.0_SA_CVO~Z` and Andrew. Four rows were filed for the CTO round analysis: Z-S1, Z-S2,
   W1-S1, W2-S4.

## RESIDUE -- not cleaned, needs a human

Two promote worktree directories remain on disk. `git worktree remove --force` failed on both with
`Filename too long` (Windows long-path under `node_modules`), and the long-path-safe recursive
delete was **correctly denied** under CLAUDE.md Agent Autonomy (recursive deletion needs human
confirmation). They are scratch only -- no repo file and no promote invariant depends on them, and
the main `portal/` tree is confirmed clean on DEV:

- `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtmp\portal-promote-20260916T010633Z`
- `C:\tmp\aggfix-promote`  (branch `aggfix-promote-prep`, fully merged into DEV)

Their `git worktree list` registrations also remain. To clear both, on Andrew's word:
`git -C portal worktree remove --force <path>` after the directory is deleted, then
`git -C portal worktree prune` and `git -C portal branch -d aggfix-promote-prep`.

## Close-out

**Closed 2026-09-16T01:2xZ -- LANDED AND VERIFIED.** production portal serves `ff542d0a`
(`portal-v2.1.179`); CI `Deploy to Production` conclusion=success; tag peels to the PROD head;
main tree back on DEV. Nothing half-landed. Rollback remains `edf85ce5` if Andrew's smoke of
production disagrees with his smoke of the branch.
