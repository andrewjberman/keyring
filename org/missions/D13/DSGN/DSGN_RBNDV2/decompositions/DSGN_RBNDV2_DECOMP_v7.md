# DSGN_RBNDV2 -- DECOMPOSITION (L5) -- ROUND 7, THE LOCAL CANDIDATE REHEARSAL (PRD v0.1)

```json
{
 "project": "DSGN_RBNDV2",
 "directive": "D13",
 "macro": "DSGN",
 "fabric": "laptop",
 "decomp_version": "v7",
 "step": 5,
 "prd_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/prd/DSGN_RBNDV2_PRD.md@e71a48e4b0 (v0.1, RATIFIED; both halves signed)",
 "round_analysis_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/ledger/ROUND_ANALYSIS.round6.md@bd082e180c (1.0.0_SA_CTO; CTO msg 109469)",
 "author": "2.0.0_SA_COO~RB",
 "round": 7,
 "rectangle": "the CTO's round-6 enrichment item 1: a LOCAL candidate rehearsal, cut from the last PROD with the feature branch's commits, the conflicts printed, the real typecheck and one walk, NOTHING pushed; item 2 (Andrew's next page and call 002b) is cut only on his words",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "portal_base": "feature/dsgn-rbndv2-light @3509eae8 (local, no upstream, never pushed)",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~RB`. **Input:** the CTO's round-6 analysis (msg 109469) over the CVO's L9 grades (`ADJUDICATION_v7.md`, two of two MET) and its ruling on `W19-S2`: C-BRANCH governs while building, `portal/CONTRIBUTING-BOXES.md` governs at the merge forward, on Andrew's push word. **Frozen at the cut.**

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

Denominator: the CTO's two round-7 items. Item 1 PLACED as `RV-z-1`. Item 2 (Andrew's next page's comments and the answer to `002b`) HELD with its condition (his words); FWD-4 (heat maps) HELD (his answer, owed at this terminal). Remainder after subtraction: item 2 and FWD-4, held.

**Measured at the cut (git reads in the portal repository):** `origin/PROD` is `33ad65ee` (a release merge); `origin/DEV` is `ad7c100b`, the commit the feature branch was cut from; DEV is 26 commits ahead of PROD and PROD is 10 ahead of DEV; the feature branch changes 89 files, and `git diff --name-only origin/PROD ad7c100b` (22 files) lists none of them, so a replay is expected to be clean; the rehearsal measures it rather than assuming it. A check file written by the issuer (`ledger/check_rehearsal.py`) is the mechanical criterion; at the base (no candidate branch) it prints `REHEARSAL-FAIL`.

## 2. THE CELL -- 1 (round 7)

| cell | what it builds | serves | writes | risk | class |
|---|---|---|---|---|---|
| `RV-z-1` | a local branch `cand/laptop/dsgn-rbndv2-light` cut from `origin/PROD` with the feature branch's non-merge commits cherry-picked in order, every conflict printed with its resolution, the typecheck before (PROD) and after (candidate) compared, the design tests run, a record written; nothing pushed | FWD-1, FWD-5 | a local git branch; its own deliverables folder | LOCAL | worker |

## 3. PLACEMENT, EDGES, BATTERY

One cell, one chain, one worktree (disk is at 87 percent used). The COO's own acts at the drain: the real `tsc -p tsconfig.app.json --noEmit` on the candidate, and one Market Overview walk on the candidate build (the dev server on port 5174 is switched from the integration checkout to the candidate checkout for the walk and switched back; dev builds stay on 5174 only). comp-iam, comp-schedule: not applicable. comp-adversary: no other open order writes a portal ref. Nothing is pushed, `portal-merge-forward.sh` is not run, no remote ref is created.

## 4. RULE 24 FOUR-POSTULATE RECORD

(i) MECE over the CTO's list by subtraction (section 1). (ii) One grain: a rehearsal of one replay. (iii) One intent: measure the replay before Andrew's push word. (iv) State coherence: the cell moves a local branch only; it leaves the feature branch, every remote ref and every source file other than through the cherry-picks.

## 5. FINDINGS FOR THE CTO (at the cut)

- The feature branch carries about 45 non-merge commits over `ad7c100b`; the candidate replays them by cherry-pick so the candidate carries the commits themselves (with `-x` provenance), as `CONTRIBUTING-BOXES.md` expects, rather than a squashed tree.
- PROD is ahead of DEV by 10 commits: the candidate is cut from PROD's tip, so those 10 are in it and the typecheck baseline is PROD's own.
