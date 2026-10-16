# AMGT_RESAPP -- call f992: delete the local portal branch release/20261016T141236Z (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~15:4xZ)

**Ruled: YES.** `2.0.0_SA_COO~R2` deletes the local ref.

**Measured (portal repo on dell1):**
- The ref is at `861c7d485e`. It is not an ancestor of origin/DEV or origin/PROD (rc 1 on both).
- It is 3 commits ahead of origin/DEV, and all 3 are MERGE commits (`861c7d48`, `dd756729`, `64f9dba1`). The count of non-merge commits
  ahead of origin/DEV is 0.
- No authored commit is unique to the ref. Every parent it merges is already on origin, and a re-merge recreates the ref.
- The DT promoted its own release, fa21a303d872, to PROD.

**Scope:** the ref is local to dell1 and was never pushed. Measured CROSS-BOX only because the portal repo is a shared set; no other box
holds or reads this ref. It is closed on this ruling, with no cross-adjudication.
