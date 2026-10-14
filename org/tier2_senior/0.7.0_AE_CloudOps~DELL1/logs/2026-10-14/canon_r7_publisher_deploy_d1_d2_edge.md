# MDPF_CANON round 7: the publisher serves the category-views history leaf -- 0.7.0_AE_CloudOps~DELL1

**Date:** 2026-10-14 (UTC; ~16:23Z - 16:4xZ)
**Task Order:** ADHOC.canon-r7-publisher-deploy (risk WORLD)
**Status:** COMPLETE
**archetype:** DEPLOY
**Branch:** box/dell1

## Objective

Rebuild the `opal-assets-mdpf-portal-publisher` package at pin `9592daf75c7469d212242cd63850c735f6f53238`, upload it to the
artifact key, set `MDPF_PUBLISHER_COMMIT` in the same targeted apply, run the function once on demand, and read the edge.
The gold lambda, the gold package and the runner tree are not touched.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| r7_cn_j_1.py / pytest | unit, seam, real; tests (C1, C2) | PASS | 6/6, 8/8, 6/6 arms; 19 passed |
| build_package.py | --pin 9592daf75c, --out scratch | PASS | 14 members; the artifact-type axis unchanged |
| own zip, plan and print graders | built zip vs git show pin; show -json per attribute | PASS | every attribute compared by value |
| safe-apply.sh | saved planfile, -target module.mdpf_publisher | PASS | 16:32:42Z-16:33:33Z |
| deploy_ledger.py | open, close-leg x6, close | PASS | CLOSED 6 of 6 |
| r7_history_readback.py (issuer's, read-only) | read, on the D2 output | 8 of 9 | H9 SKIP: it matches the ledger by filename tokens |
| comp-rail | none denied on this order's reads | -- | native Grep and named-resource reads |

**What worked:** the before print equalled the order's expectations field for field, so the drift table had a verified
premise; saving the prior artifact's exact bytes by hash before the upload made the rollback a copy, not a rebuild.
**What failed:** nothing in the act. My own cross-check "pointer history_rows equals the manifest's" read False, which was
my check being too strict: the pointer carries only `content_sha256` and `served_sha256` per leaf by design; both equal.
**Gap found:** (1) the issuer's H9 finds the ledger by filename tokens and the order's own slug has none of them, so H9
reads SKIP; the script is the issuer's. (2) The builder's sidecar `runtime` says python3.12 while the function runs python3.11;
pre-existing, unchanged. (3) The edge answers 401 without a session, so the route's authenticated behaviour is not measured here.

## Work Completed

1. **GO and preconditions** (msg 5647): 2a-2g measured, including the edge read (30 behaviours, no leaf named; the deployed
   router rewrites by prefix; 6 WAF rules, none naming a leaf) and the sentinel read across 33 worktrees (57 distinct).
2. **Ledger** opened 16:26Z with 6 legs; L1 closed with the before print, the rollback copy by hash and the drift table.
3. **Drift table at the pin:** 9 differing members (the cell plus the pair's eight), all inside section 1a; no ninth.
4. **D1** 16:29Z-16:33Z: built from the pin; checks of the zip; upload (new version `KjRaDaow...`); the `.tf` edit
   (`0e4390c914`); targeted plan 0/1/0; applied through `safe-apply`; read back; re-plan clean.
5. **D2** 16:34Z: one invoke, 200, `published=18`, four history rows `published`; 18 leaves same data; pointer gained `history_rows`.
6. **D3** 16:36Z: the unauthenticated GET of each leaf answered 401, recorded, sub-leg stopped.
7. **L6** after print; the committed sidecar updated to this build's; ledger CLOSED.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Updated the committed sidecar after the deploy | it is an order `<paths>` entry and the next drift table reads it |
| Did not authenticate to get past the 401 | the order says record and stop that sub-leg; a borrowed credential is not mine to mint |
| Ran the issuer's readback once, read-only | the CTO's condition 2(a) names H8; supporting evidence only, the grade stays the issuer's |

## Open Items

- The first-run acceptance is the issuer's read on the 2026-10-15 13:50Z scheduled run at the earliest.
- `C:/tmp/r7-pub/` (built zip, prior zip, plans, invoke response) is local scratch and is not committed; the prior zip is the rollback copy.
