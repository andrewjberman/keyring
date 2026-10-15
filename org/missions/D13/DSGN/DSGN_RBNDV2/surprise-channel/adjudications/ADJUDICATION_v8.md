# DSGN_RBNDV2: CVO L8/L9 at the round-7 close (2026-10-15)

<sweep_watermark>2026-10-15T18:15Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~RB` msg 109480 (record `deliverables/2.0.0_SA_COO~RB/ROUND7_CLOSE_RUN_20261015.md` @a7c43dbf9f).

**Result: RB7Z1-AC3 MET. W22-S1..S3 dismissed. The candidate is local only; its push and the client-facing approval are Andrew's.**

Instrument. This seat's own reads in the portal repository:
- `git rev-parse` of the three refs;
- `git ls-remote --heads origin cand/laptop/dsgn-rbndv2-light`;
- a per-file `git diff --quiet` of the 89 feature files between the feature branch and the candidate;
- `tsc -p tsconfig.app.json --noEmit` in a detached scratch checkout of the candidate (`ajb_wk/cand-check-cvo`), using a temporary junction to the integration worktree's `node_modules`.

The junction was removed with `rmdir`, so the link alone went and its target was untouched: 317 entries before and after. The scratch checkout was then removed. This seat
did not switch the shared dev server on port 5174 to the candidate. The walk half rests on the COO's walk and on the byte identity below.

```json
[
 {
  "id": "DSGN_RBNDV2-C-S22",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T18:44Z",
  "one_line": "L9 round 7: RB7Z1-AC3 MET. The candidate cand/laptop/dsgn-rbndv2-light (c8181090) sits 39 commits over PROD 33ad65ee with PROD as its ancestor; it typechecks clean (rc=0); the 89 feature files are byte-identical to feature/dsgn-rbndv2-light (0 differ); the record prints 0 conflicts; the branch is absent from origin.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "RB7Z1-AC3: the real typecheck on the candidate adds no error over PROD's own baseline; the conflicts (if any) and their resolutions are printed in the record; one Market Overview walk on the candidate build reads the same as on the feature branch.",
  "world_is": "Typecheck: tsc -p tsconfig.app.json --noEmit in a checkout of c8181090 reads rc=0 with no error lines, so it adds no error over any baseline. Conflicts: the record prints 0 conflicts, 0 empty and 0 skipped cherry-picks of 39. Identity: all 89 files of ad7c100b..feature/dsgn-rbndv2-light compare equal between 3509eae8 and c8181090. The candidate's only other content is PROD's own 10 commits ahead of DEV. Walk: the COO's walk of the candidate build reads the same values as this seat's round-6 walk of the feature branch (unboxed topic rows, 'Source: Global News.', a dark needle, white tooltip text). Given the byte identity of every feature file, this seat accepts that walk without moving the shared server. Remote: ls-remote prints 0 heads for the branch.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git -C portal rev-parse --short cand/laptop/dsgn-rbndv2-light feature/dsgn-rbndv2-light origin/PROD -> c8181090, 3509eae8, 33ad65ee; rev-list --count origin/PROD..cand -> 39; merge-base --is-ancestor origin/PROD cand -> true",
    "git -C portal ls-remote --heads origin cand/laptop/dsgn-rbndv2-light -> 0 lines",
    "per-file git diff --quiet over the 89 files of ad7c100b..feature/dsgn-rbndv2-light -> differing=0",
    "node node_modules/typescript/bin/tsc -p tsconfig.app.json --noEmit in a detached checkout of c8181090 -> rc=0 (2026-10-15 ~18:4xZ)",
    "org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ROUND7_CLOSE_RUN_20261015.md @a7c43dbf9f"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard. The candidate's push, through portal-merge-forward.sh and a client-facing approval row, waits on Andrew's word; Market Overview is a client-facing page."
 },
 {
  "id": "DSGN_RBNDV2-C-S23",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T18:44Z",
  "one_line": "W22-S1 (39 commits, not about 45), W22-S2 (the scratch PROD worktree got its own bun install) and W22-S3 (a 'Filename too long' removal, later cleared by wk-provision.sh remove) are dismissed INERT.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["DSGN_RBNDV2-W22-S1", "DSGN_RBNDV2-W22-S2", "DSGN_RBNDV2-W22-S3"],
  "spec_asserts": "TO-RV-z-1 as written.",
  "world_is": "Build notes. The COO's record states that the prod-baseline directory was removed with the merged worker worktree, and that the shared node_modules is intact. This seat's read of that folder after its own scratch use shows its usual entry count.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md rows W22-S1..S3"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Build notes; nothing stranded."
 }
]
```

-- 3.0.0_SA_CVO~L
