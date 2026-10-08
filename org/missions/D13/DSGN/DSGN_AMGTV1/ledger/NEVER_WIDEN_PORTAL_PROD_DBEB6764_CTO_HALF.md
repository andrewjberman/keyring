# CTO never-widen half -- portal PROD promote, b06863fe -> dbeb6764 (44 commits, 71 files)

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-08 ~18:3xZ. **Ask:** `2.0.0_SA_COO~D` msg 31947.
**COO half:** `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round52/prod-promote/NEVER_WIDEN_HALF_COO_PORTAL_PROD_DBEB6764.md`
@454754ec7d, read whole. **Andrew's word:** "recs approved" at `2.0.0_SA_COO~D`'s terminal ~15:5xZ, record @7eb9750741.

## VERDICT: SIGNED for the merge of `dbeb6764` into PROD and its push, pinned to that sha. The pin is ruled right.

**The pin.** `dbeb6764`, not DEV's head `1cbc56a7`. The nine AMGT_CORPUS commits past it were not in the range the four owners
confirmed, and Andrew's PROD word was given on that range. They ride the next promote, on their own word.

## What this seat read at signing (in `C:/tmp/wk-crps-r40-4/portal` after a fetch)

| read | result |
|---|---|
| origin PROD | `b06863fe` |
| `git rev-list --count b06863fe..dbeb6764` | 44 |
| `git diff --name-only b06863fe dbeb6764` | 71 files |
| the marker `data-research-coverage` under `src` | 0 files at `b06863fe`, 1 at `dbeb6764` |
| `deploy.yml` at the pin | on push to PROD; `deploy` needs `build`; `aws s3 sync ... --delete` |
| **is `b06863fe` an ancestor of `dbeb6764`?** | **NO** (rc 1; positive control `dbeb6764` -> `1cbc56a7` rc 0). PROD holds 5 commits DEV does not |
| those 5 commits | each is a DEV->PROD merge (`b06863fe`, `ab3191d0`, `f8c94759`, `ce6f0721`, `c69b4747`) whose tree equals its DEV parent (0 files differ), and every DEV parent is an ancestor of `dbeb6764` |

## A correction to the COO half, and why it does not change the act

The COO half's sentence "`b06863fe` is an ancestor of `dbeb6764`, so nothing on PROD today is outside the range" is false as
written: PROD carries five merge commits of its own. Its conclusion holds by the second read above: each of the five carries only
DEV content already inside `dbeb6764`. So after the merge PROD's tree is `dbeb6764`'s, and nothing served today is lost. The COO
half is corrected in place by its author; the act does not wait on that edit.

## Accepted as the COO half states it

The owners' table (44 of 44: site Z 11, dell1 11, dell2 22, the laptop none). N = 1 writer, `deploy.yml`. Both branches and
the rollback by `git revert -m 1` pushed to PROD, never a force push and never a delete by hand. The `--delete` in the sync is
the standing writer's own rule, run on every promote; it removes the assets the new build does not produce, under Andrew's word
for this promote.

## C1 -- the served read names the page, not only the bundle

After the deploy: the served index read and the marker present, as the COO half says; and Security Analysis opened once on PROD
for one name (BP/ LN): the officers start with the chief executive, and the one statement of inputs is drawn. FWD-1's signed-in
walk stays Andrew's.

-- 1.0.0_SA_CTO~Z
