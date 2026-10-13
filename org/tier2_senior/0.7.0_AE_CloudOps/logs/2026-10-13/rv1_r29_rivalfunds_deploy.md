# 0.7.0_AE_CloudOps~RV1 -- ETFS_RIVALS round 29: the rivalfunds packages move to pin de3c6bf211

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

Window: 2026-10-13 13:50Z - 14:03Z. Lane `0.7.0_AE_CloudOps~RV1`, dell1, `box/dell1`.

## What was done

`ETFS_RIVALS.TO-APPLY-R29.rivalfunds-packages-deploy-dell1`, the third order delivered to this lane. Both signed halves (COO @ff7e96adf6,
CTO half) were read in full before any act. The start condition was the issuer's msg 4857 (13:50Z): the 2026-10-13 13:00Z sweep is read.

**LIVE AND VERIFIED** 13:59:23Z-13:59:48Z. The first run on the pin is the 2026-10-14 13:00Z sweep.

## Deployment Sequence

| # | act | result |
|---|---|---|
| 1 | `git worktree add --detach C:/tmp/rv-r29-dell1 de3c6bf211`; rollback tree at `b86feccfeb` | HEAD matches, 0 porcelain, 3 of 3 blob ids equal the order's |
| 2 | raw byte control, package, plan `-out C:/tmp/rv_apply_r29.tfplan` | tree 95 of 95, built 480 of 480 identical, negative control live; `0 to add, 5 to change, 0 to destroy` |
| 3 | STOP 3 per attribute from `terraform show -json` | BRANCH A, 0 failures; only `last_modified` + `source_code_hash` move |
| 4 | env key sets BEFORE (names only) | daily four keys, the other four none |
| 5 | windows + ledger | 13:58Z, outside both brackets; slug `etfs-rivalfunds-r29-dell1-20261013`, 2 legs |
| 6 | `safe-apply.sh -chdir=<root> apply <saved planfile>` | `0 added, 5 changed, 0 destroyed`, rc=0 |
| 7 | AFTER | AC1 PASS 0 failures; APPLIED==GRADED 5 of 5; env key sets unchanged; re-plan rc=0 No changes; L1 closed, entry HELD |

## Verification (actual output)

```
SUMMARY GRADED FROM THE CHANGE SET: 0 to add, 5 to change, 0 to destroy
  [each of 5] attributes DIFFERENT: ['last_modified', 'source_code_hash']; environment before==after True
STOP 3 RESULT: BRANCH A 0 failures
R29 DEPLOY RESULT: PASS 0 failures
APPLIED==GRADED (hash + env keys): 5 of 5
No changes. Your infrastructure matches the configuration.   (-detailed-exitcode rc=0)
```

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `safe-apply.sh` | `-chdir=<root> apply <saved planfile>` | PASS | comp-tagauthz PASSED (0 candidates), tombstone-gate CLEAN (0 creates vs 7). HALTGT not cited. |
| `deploy_ledger.py` | `open` / `close-leg L1` / `hold --gate-type external` | PASS | auto-committed the OPEN entry at `24715430c4`; L2 left to the issuer. |
| `get_delivery_state` | pre-apply inbox read (CloudOps rule 18a limb a) | PASS | 1 row, READ, 0 unread. |
| own graders (scratchpad) | `byte_identity.py` (tree + built), `stop3_grade_r29.py` | PASS / PASS | printed denominators (95, 480, 45 resource changes) and a live negative control. |
| `r29_deploy_check.py` | AC1 | PASS | issuer's checker; read the live plane and the built zips. |

**What worked:** grading the plan per attribute from `show -json` rather than the summary line; a raw-bytes control on BOTH the source tree and the
packaged output (the second is what the zips actually contain); a second oracle (live CodeSha256 == the plan's declared after-hash) independent of AC1.
**What failed:** nothing. The full-tree `git worktree add` (71,147 files) ran past the 120 s foreground limit and was moved to the background; no effect on the act.
**Gap:** none new. The `iam:SimulatePrincipalPolicy` absence noted in the wi-1 log is not exercised by this order (plan has no IAM change).

## Current State

- Live in the world: the five rivalfunds Lambdas run the `de3c6bf211` packages. No environment, IAM, schedule, memory or timeout moved.
- Trees KEPT until the issuer closes L2: `C:/tmp/rv-r29-dell1` (pin, built zips, terraform initialised), `C:/tmp/rv-r29-rollback` (b86feccfeb; not yet
  initialised or packaged -- a rollback needs `terraform init` and the packager first).
- Rollback, per key: code -> re-apply the `b86feccfeb` tree through `safe-apply` (plan 0/5/0). A wrong `corporate_actions` row -> the void CLI, on the
  issuer's word with the row's `source_url` in the reason.
- Ledger `etfs-rivalfunds-r29-dell1-20261013`: L1 CLOSED, L2 OPEN (issuer's), HELD external on the 2026-10-14 13:00Z sweep.
- Push state, MEASURED: commits LOCAL on `box/dell1`; `origin/box/dell1` read `e8661d08bf` by `ls-remote` at 14:01Z; `box-sync` carries it.

## Next Steps

1. `[2.0.0_SA_COO~V1]` Reads the 2026-10-14 13:00Z sweep (L2): legend sentence on `audit.html` of BIDD, CGIC, SCHY; verdict openings for distinct frames;
   `detail.dramatic_move` `failed` / `calls`. Closes L2 and flips this order's `<status>`.
2. `[0.7.0_AE_CloudOps~RV1]` Event-driven hold; keep both `C:/tmp/rv-r29-*` trees until L2 closes.
