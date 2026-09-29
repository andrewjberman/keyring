# ANDREW-DIRECT 2026-09-29 ~20:4xZ -- open calls answered: push YES, G-C blocked on IT, remove the 34 YES

**Channel:** Andrew, in the 1.0.0_SA_CTO~O Claude Code session (site Z), 2026-09-29 ~16:4x ET, answering this seat's
`/open-calls` (3 cards, 20:43Z).
**Recorded by:** 1.0.0_SA_CTO~O, same turn, before the acts.

## Verbatim

> "yes to call 1. call 2 need to talk to IT, so blocked externally there. call 3 yes"

## What each answer binds (verbatim scope, nothing wider)

| call | his word | act | who acts |
|---|---|---|---|
| 1. Release the site Z push to origin CLOUD | "yes" | push site Z CLOUD to origin as a pull-merge (never a rebase); then MX-t-10's 41ba3f747f reaches laptop CLOUD | 0.0.0_AB_MSTR~Z (the only site-Z seat that pushes a shared branch) |
| 2. G-C test identity (new unprivileged M365 user) | "need to talk to IT, so blocked externally there" | no act; G-C is BLOCKED-EXTERNAL on Opal IT. OG-g-1, then OG-v-7, and MCPINDEX G5 stay held | 2.0.0_SA_COO~O records it in NFRA_OPLGTW's blocking |
| 3. Remove the 34 NFRA worktree checkouts | "yes" | remove the checkouts listed below; every branch is kept; `.scratch/` is archived first; portal junctions are unlinked first | each project's own seat, for its own set |

### The 34 (the list put to him at 20:43Z, `POST_CRASH_ASSESSMENT_CTO_O_OPALAI_MCPORTAL_20260929.md` @18badb8d01)

- **NFRA_OPLGTW (2.0.0_SA_COO~O), 11:** the 10 in its msg 26641 table, plus `C:/tmp/wk-oplgtw-14` (msg 26693).
- **NFRA_MCPINDEX (2.0.0_SA_COO~MI), 13:** the DISPOSE 13 in its msg 26635 table (`POST_CRASH_ASSESSMENT_NFRA_MCPINDEX_20260929.md`).
  `wk-mcpindex-r4-15` is NOT covered; it stays as MX-t-10's candidate.
- **NFRA_OPALAI / NFRA_MCPORTAL / own (1.0.0_SA_CTO~O), 10:**
  - OPALAI: `C:/tmp/oa-10`, `oa-15`, `oa-10-rb2`, `oa-10-rel`, `oa-10-rel2`, `oa-10-sw-rb2`, `oa-10-sw-rel`, `oa-10-sw-rel2`.
  - MCPORTAL: `C:/tmp/mp3-1`.
  - Own: `Desktop/cto_o_tflocal`.

NOT covered: every branch; `wk-mcpindex-r4-15`; `C:/tmp/oa-s45-redrain` (2.0.0_SA_COO~AI's re-drain checkout, which
was not on the list); every other worktree.

## Result (as of ~21:4xZ)

**Call 1, push.** 0.0.0_AB_MSTR~Z pull-merged and pushed portal DEV (origin/DEV = ac8265668d, ls-remote read). It did
NOT push workspace CLOUD: a fresh merge-tree of CLOUD against origin/CLOUD (1024 ahead / 633 behind) reads 5 conflicts
(`.claude/skills/ui-walk/walk.mjs`, `4.0.0_SA_CRO/RECON_REGISTER.md`, three `2.0.0_SA_COO~D` drive logs written on both
devices). MSTR~Z took them to Andrew (msg 26703). 41ba3f747f stays local, and MX-t-10 stays held.

**Call 2, G-C.** Relayed to 2.0.0_SA_COO~O to record in NFRA_OPLGTW's blocking as BLOCKED-EXTERNAL on Opal IT.

**Call 3, removals.**
- **1.0.0_SA_CTO~O's set: 10 of 10 removed.**
  - Pre-act re-measure: unique commits and tracked edits matched tick 1. The two tracked edits were
    `cto_o_tflocal/.tools/naming-gate.py`, byte-identical to CLOUD (f3e10beb8c), and `oa-10`'s gateway `audit.jsonl`,
    5 lines of local test output with test identities.
  - `.scratch/` archived: oa-10 414=414, oa-15 6=6 plus `.scratch_msg1/2`, mp3-1 9=9.
  - Reparse points: 1 in 10 trees, `mp3-1/portal/node_modules` (junction into the main portal/node_modules). It was
    unlinked with `cmd /c rmdir` before the remove. Main node_modules read 263 entries before, after the unlink and after
    all removals, with vite and react present.
  - `git worktree remove --force` returned rc=0 on all 10 and every directory is gone. All 10 branches still resolve.
    `git worktree prune` and `git -C portal worktree prune` were run.
- **2.0.0_SA_COO~O's set: 11 of 11 removed** (msg 26720): 4 junctions unlinked first, main node_modules
  263 before and after, all 8 branches kept, and the 3 detached HEADs contained in kept branches.
- **2.0.0_SA_COO~MI's set: 13 of 13 removed** (msg 26727, record @76043d5c0b): 0 junctions (control fired), `.scratch`
  archived with counts equal, 20 branch tips unchanged, and wk-mcpindex-r4-15 kept.
- **Call 3 DONE: 34 of 34 removed** (~21:48Z), every branch kept. The only NFRA checkout left in the four projects is
  wk-mcpindex-r4-15 (MX-t-10's candidate).
