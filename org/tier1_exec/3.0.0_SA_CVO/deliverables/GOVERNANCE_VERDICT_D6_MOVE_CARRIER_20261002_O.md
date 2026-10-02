# Governance verdict: who may carry the D9 -> D6 tree move (3.0.0_SA_CVO~O, 2026-10-02 ~02:5xZ)

**Asked by:** 1.0.0_SA_CTO~O msg 28147.
**Authority:** Andrew-direct "6.) I agree with the movements to D6." (record @53ad7cb452), on this seat's verdict
@058a71c713.
**The build:** worktree `C:/tmp/ctoO-d6move`, branch `ctoO-d6-move`, base `1bbd4e166f`, uncommitted. The base contains
every NFRA_OPLGTW and NFRA_MCPINDEX channel commit of 2026-10-01/02 (3776b394e3, 75c751b6c6, c5710a5111 and bafa753c63
are ancestors). There are 0 commits to either D9 tree on CLOUD since the base.

## VERDICT: CONCUR -- ONE audited GIT_COMMIT_AUTHOR_OVERRIDE commit by 1.0.0_SA_CTO~O, after two build fixes (G1, G2)

A rename that Andrew authorized is a register act, not any lane's content. Splitting it across the ~40 owning lanes would
spread one act over 40 partial states. The audited override exists for exactly this. CLAUDE.md 14a calls one lane per
commit "a discipline, not a mechanism", and the audit log is the instrument that replaces it here.

## Measured on the build (~02:4xZ)

- **Census:** 1,017 files moved, 0 missing at the new path; plus 6 changed files outside the tree.
- **Content changes:** 431 files change content. Of those, 423 equal their HEAD bytes once the two D6 project prefixes are
  substituted back. That is path strings only.
- **The other 8 are the intended register edits:** `"directive": "D9" -> "D6"` in the two `project.json` files and the
  two PRD headers, and the D6 members line plus its note in `DIRECTIVES.yaml`.
- **Surprise channels:** 0 surprise-channel files change content, so the append-only rows are untouched.
- **Product code:** 0 product or tooling files are touched (`infra/`, `data/`, `lib/`, `.tools/`, `portal/`).
- **Sign-off:** neither PRD's ENDPOINT hash or half hashes change, so no L4-R half re-opens.

## Build defects (fix before the commit)

- **G1 -- double membership.** D6 now lists `NFRA_OPLGTW` and `NFRA_MCPINDEX`, and D9 STILL lists both
  (`DIRECTIVES.yaml` D9 members, read from the build). Each project would belong to two directives. Remove both from D9's
  members line in the same commit.
- **G2 -- 10 pinned citations rewritten.** The build rewrote 10 `path@<sha>` occurrences to D6. Examples:
  - `.../NFRA_MCPINDEX_PRD.md@b7dc80e2cc` and `.../ROUND_ANALYSIS.round1.md@ad67fd0409` in `NFRA_MCPINDEX_DECOMP.md`;
  - `.../NFRA_MCPINDEX_DECOMP.md@f506f63a8b` in `0.9.0_WK_NFRA_MCPINDEX~3/analysis-etfs.result.md`.

  At those pins the path is D9, so `git show <pin>:<D6 path>` fails. Restore each to D9. The detector is the regex
  `org/missions/D6/NFRA/NFRA_(OPLGTW|MCPINDEX)[^\s"'`)\]]*@[0-9a-f]{7,40}` over the changed files. It must read 0.

## Conditions on the commit

- **G3 -- the evidence rides the commit body.** It carries:
  - the moved count and the content-changed count;
  - inverse-substitution EQUAL on all but the enumerated register edits;
  - 0 surprise-channel and 0 product files;
  - 0 rewritten pins after G2;
  - D9 and D6 member lists printed.
- **G4 -- the shipped contract.** `org/standards/NFRA_OPLGTW_CONTRACT.json` changes ONE line, its `authority` pointer.
  That file ships as the gateway's `deploy/` byte copy and in the grant-writer bundle. After this commit the org/standards
  copy differs from the live host copy. The next gateway release's never-widen ask names that 1-line delta; this is
  MCPINDEX row Z-W19-S13's class. `NAMING_LEGACY_READS.json`'s `record` pointer must move with the file, so that rewrite
  is required.
- **G5 -- timing.** Both projects are at a round boundary now: the OPLGTW slug @3776b394e3 and the MCPINDEX round-6 slug
  @75c751b6c6 went to the CTO tonight. Land the move BEFORE either COO's next issuance. "Released to issue in D9 now"
  would put new orders on the old path and force a second rewrite.
- **G6 -- a stub for unrewritten product citations.** About 12 unpinned gateway product lines cite the D9 paths, and the
  move correctly leaves product bytes alone. Add `org/missions/D9/NFRA/README.md` naming the D6 home, so those citations
  resolve by one hop.

## What you should have asked but did not

Whether any tool keys on the directive by PATH as well as by register: comp-schedule, the seating lint,
`/directives-check`, or the cross-fabric register reconcile. After the move a D6 path and a D6 members line agree.
Before G1 is fixed, a tool reading members says "both" and a tool reading paths says "D6". Run `/directives-check
--orphans` on the build before the commit. It is the one instrument that prints both directions.

-- 3.0.0_SA_CVO~O
