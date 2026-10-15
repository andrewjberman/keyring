# NFRA_CTLPLN -- ROUND-16 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~08:1xZ)

**On:**
- the issuer's drain end `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND16.md` (3 of 3 complete, MAY-CLOSE);
- the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v21.md` @c7d0865d79 (MAY-CLOSE; W100-S1 graduates ARMED to
  this seat).

**PRD:** unchanged.

## 1. What round 16 moved

- **The own-commit test exists** (CT-af-1). `worktree_gc.py` prints `UNSTARTED=`, and a branch still at its issuance commit,
  clean or dirty, is never removed. It is the mechanical form of my round-15 ruling 1.
- **round-close-check counts by the decomposition's round** (CT-af-2). The round-15 instrument note is cured.
- **The placement-refusal branch unstages every path** (CT-af-3; W99-S1 closed).
- **Every worker committed early,** with 4 to 5 own commits per branch. The new face line works.

## 2. Rulings

1. **W100-S1 (ARMED), RULED (c), sent to the issuer at 07:04Z:** a merged worktree with uncommitted changes is still removed,
   per Andrew's standing word. Before removal, its uncommitted state (tracked changes plus untracked non-ignored files) is
   committed to a new branch `preserve/<branch>-<stamp>` and the sha printed.
   - The two verbs agree: `--check-removable` reports such a worktree `REMOVABLE-AFTER-PRESERVE`, and `--go` preserves, then
     removes.
   - Done when both verbs agree on one planted dirty merged tree, and that tree's file is readable at the preserve sha (the
     CVO's done-when).
2. **W100-S2 (`--check-removable` too strict): gitignored paths are not "dirt".** `.comp-graph/`, `.scratch/` and similar test
   leftovers are ignored by design. The test reads `git status --porcelain`, which excludes ignored files, exactly as my
   round-15 definition said. The extra refusal on ignored non-cache paths is removed. The preserve step also excludes ignored
   paths.
3. **The sparse worker checkout** (my message ~07:05Z): each full worker worktree costs 3.6G, and the laptop fell to 6G free
   twice. Workers cut a sparse checkout of the order's `<paths>` plus `.tools/` and `lib/` by default.

## 3. ENRICHMENT LIST for round 17 (one issuance)

1. One cell for rulings 1 and 2 together in `worktree_gc.py`: the preserve step, `REMOVABLE-AFTER-PRESERVE`, and porcelain-only
   dirt.
   - Proof: a planted dirty merged tree, where both verbs agree and the file is read back at the preserve sha.
   - Then ONE real `--go` on the real repository against a real merged worktree. It was never run there before; the round-16
     packet says so.
2. The sparse worker checkout (ruling 3). Proof: one real cell green in a sparse worktree, with sizes printed.
3. Carried, with owners as before: S9125 (dell1), S9119, S9103, S9120, S9122, Z-S3, W12-S1, W89-S3.
