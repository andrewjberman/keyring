# IRPT_BCKEND round 71 -- workstream ~Y decomposition (E11 repair: the staged report modules carry E9)

Issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~00:5xZ. Input: release 4 BRANCH B (`0.7.0_AE_CloudOps~DELL2` msg 1989, @241a51196f;
row `IRPT_BCKEND-D2-S16`).
- The import census on the release-4 bytes failed: `custody_submission: ImportError cannot import name CUSTODY_POLICY_REVISION from
  composition`. Live was rolled back to `Un0wVZqj...` (issuer re-read).
- **Cause:** `irpt-ycharts-generate` stages `reports/composition.py` and `reports/repository.py` at `3f29017cfc`, which predates E9
  (IB-pr-369, @2aa217ec58: `CUSTODY_POLICY_REVISION` and `additional_policy_revisions`). E11's tests passed because their sys.path
  resolves the repo copy. The build's import-closure gate checks module names, not imported names.

ONE issuance, one cell, no edges.

| item | cell | cut? |
|---|---|---|
| Re-pin the two staged rows `composition.py` and `repository.py` of `irpt-ycharts-generate` to `605c4cd4ac`, so the package carries E9; add a symbol-closure grade of the built zip | `IB-yr-711` | **CUT** |

**Riders (named for the release-5 pair, not graded here):** commits to those two files since `3f29017cfc` besides E9 are
`f60e6f1d2a` (`~G2`, YCD-l-6: the Opal PDF under its own policy row) and `b13bab7495` (`~P`, IB-pr-336: custody naming). Each owner
confirms its member at the pair.

| criterion | invocation | base reading |
|---|---|---|
| Y71-1-AC1 (the build carries E9 and only the named members change) | `python infra/aws/lambda/ci/release-census.py irpt-ycharts-generate --pin HEAD` | `changed_members=1` (custody_submission.py). Expected after: `changed_members=3`, exactly custody_submission, composition, repository |
| Y71-1-AC2 (every imported name resolves in the packaged module) | `bash org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r71/y71_ac2.sh` | `MISSING custody_submission.py:15 imports CUSTODY_POLICY_REVISION from composition`; `modules=62 pairs=273 missing=1`; `symbol_closure FAIL` |

Risk WORLD (the L6 gate floor on lambda-source-map.json). Nothing deploys here; release 5 follows under its own pair.

## Four-postulate record

(i) Domain: the two staged rows whose pinned blobs lack E9. (ii) One row each. (iii) One intent: the package carries E9, so E11
imports. (iv) Every other staged row and every deployed byte do not move.

fanout: 1 of 1 chains, cap 8, reason: one item. Worker slot `~221` (Y 220-229).
