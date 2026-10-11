# MDPF_SECCLASS stale worker worktrees -- owner assessment (2.0.0_SA_COO~M1, dell1, 2026-10-11 ~03:4xZ)

**On:** `0.0.0_AB_MSTR~DELL1` msg 3423 (worktree_gc ESCALATE, 7 worktrees plus `wk-secclass-42`). **Owner:** this seat (the workers' issuer).
**Method (measured, `box/dell1` @d29944d19a):** for each branch, every file it changed against its merge base is classed by blob
equality with `box/dell1`: LANDED (same blob), SUPERSEDED (box/dell1 moved the file since, past the branch's version), or UNLANDED
(box/dell1 still holds the merge-base blob, so the branch's change never reached it). Patch-id `git cherry` is not the test: these
branches were drained by conflict-resolved merges, so equal content shows as unequal patches.

| worktree | branch (last commit) | round / cell | files | landed | superseded | unlanded | what the unlanded files are |
|---|---|---|---|---|---|---|---|
| `wk-secclass-44` | `wk-MDPF_SECCLASS-44` (10-07) | r9 SC-e-44 (producer non-old-list input) | 29 | 6 | 12 | 11 | E_18 callers + tests (BD, COT), a v2_portal shared test, the e44 proof |
| `wk-secclass-47` | `wk-MDPF_SECCLASS-47` (10-07) | r9 SC-e-47 | 37 | 7 | 18 | 12 | the same E_18 set plus the e47 records |
| `wk-secclass-48` | `wk-MDPF_SECCLASS-48` (10-07) | r9 SC-e-66 (silver union columns) | 6 | 2 | 3 | 1 | the e66 proof instance only |
| `wk-secclass-54` | `wk-MDPF_SECCLASS-54` (10-07) | r10 SC-e-53 (attribution categories) | 4 | 0 | 2 | 2 | the e53 order file and its proof instance |
| `wk-secclass-r8-27` | `wk-MDPF_SECCLASS-27` (10-07) | r8 SC-e-27 (name aliases / classify BD securities) | 19 | 0 | 5 | 14 | `scripts/classification/*`, B_01b, gold_dispatch.sh |
| `wk-secclass-r9-34` | `wk-MDPF_SECCLASS-34` (10-07) | r9 SC-e-44 (an earlier slot) | 8 | 0 | 2 | 6 | the e44 order, half request, dry-run, proof |
| `wk-secclass-r9-38` | `wk-MDPF_SECCLASS-38` (10-07) | r10 SC-e-55/56/57 | 18 | 9 | 4 | 5 | proof instances and order files for e55, e56, e57 |
| `wk-secclass-42` | `secclass-r10-held-38` (10-07) | r10 held line (e55-e62) | 41 | 23 | 11 | 7 | proof instances and order files for e55-e62 |

**Reading.**
- **Product code in the unlanded set** is only in the two oldest lines: the E_18 callers and tests (r9 e44/e47) and the r8 classification
  scripts (e27). The measured basis for "superseded" is the SUPERSEDED column (box/dell1 changed the
  same files after the branch's merge base); that the E_18 and classification-script changes are no longer wanted is this seat's reading
  from the later rounds, not a measured fact, and it is the one a human word should confirm before anything is dropped.
- **Everything else unlanded is a record:** order files and proof-of-spec instances the worker wrote on its own branch. The order text
  and the outcomes are on `box/dell1` through the issuances and ledger entries; the instances are the worker's self-report.
- **No worktree has tracked content dirty beyond the nested `portal` gitlink; each holds untracked `.scratch/` scaffolding** (disposable
  by the order's own bound).

**Disposition proposed, and why it is not done here.** Nothing is deleted by this seat: each branch holds commits no other ref carries,
and removing a ref that is not contained in a trunk is destructive git (CLAUDE.md, Agent Autonomy). Proposed, on a human word:
1. tag each branch tip `archive/MDPF_SECCLASS/<branch>` (keeps every commit reachable, adds a ref only);
2. `git worktree remove` each directory (never `--force`);
3. delete the branch names, which then loses nothing.
If the human word is that some line should land instead, the two product-code lines (e44/e47 E_18, e27 classification) are the only
candidates and each would need its own pair; this seat recommends not landing them.
