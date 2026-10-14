# NFRA_DEVPLN -- a second feature reached portal DEV through the route, organically, from another box (issuer read, 2026-10-14 ~00:30Z)

Not a cell and not a grade: a measured record for the CTO's and CVO's grade reads of FWD-1, FWD-4 and FWD-7. Read by `2.0.0_SA_COO~DV` from origin, on the laptop, with the tools the project built.

## What happened

At ~20:20 local (see the commit) a worker `0.9.0_WK_AMGT_RESAPP~423` landed `cand/dell1/amgt-sa-header-money-and-dash-reasons` on portal DEV: merge commit `5e40e541`, first parent `24877b67` (the laptop feature's merge), second parent `624e2533f665bf786e41594adba17b82c447aa7d`. Neither this project's workers nor the issuer touched it.

## The reads (all from the laptop; dell1 is a foreign box)

| read | result |
|---|---|
| merge body, last lines | `Feature: cand/dell1/amgt-sa-header-money-and-dash-reasons` and `Approved-By: 1.0.0_SA_CTO~DELL1 @dell1-20261014T001511Z-633a` |
| `python .tools/open-calls.py approval-status --branch cand/dell1/amgt-sa-header-money-and-dash-reasons` | `NOTE: dell1 list read from cluster written_at=2026-10-14T00:17:47Z` then `state=APPROVED valid=yes row=dell1-20261014T001511Z-633a by=1.0.0_SA_CTO~DELL1 head_sha=624e2533f665 commits=1 class=opal-internal box=dell1 pages=Security Analysis` |
| the row's bound head equals the merge's second parent | `624e2533f665` on both sides |
| `python .tools/portal-hooks/dev_push_payload_gate.py --portal portal --remote-ref refs/heads/DEV --remote-sha 24877b67 --local-sha 5e40e541` | `PASS 5e40e54119 route=A` then `DEV-PUSH-GATE result=ADMITTED reason=- commits=1` |
| `python .tools/portal-dev-approval-read.py --portal portal` | `first_parent_commits=5 approved=2 unapproved=3` (the three unapproved are the dell2 ANLREQ merges that predate the route) |

## What it shows, and what it does not

- The approval route ran from a box other than the laptop: an `opal-internal` feature approved by that box's CTO lane (`_SA_CTO` closer, class rule `valid=yes`), landed with both trailers. That is FWD-7's class line operating on organic work, and FWD-4's per-commit read naming the feature and approver for each approved commit.
- Three round-2/4/5 tools composed on real data: the cluster-first read found a row on dell1's list that the laptop's working-tree copy does not hold (`DP-e-2`); the payload limb admitted the push as route A against that row's bound head (`DP-f-1`); the per-commit read listed it (`DP-c-1`).
- It does NOT show the client-facing case. This feature is Opal-internal (Security Analysis, staff-only). FWD-1's client-facing close still waits on Andrew ruling the dell2 rows (`3635`, `8500`, `7b45`, `fde0`).
- Not measured here: which route the worker took to push (the script versus a typed push). The merge is a two-parent merge with both trailers and a valid row either way. The payload limb is not installed on any box, so it did not gate this push.

## Addendum ~01:30Z -- the second feature also reached PROD, as a chosen-set promote, with no word from the project

`origin/PROD` moved from `10e7664d` (the laptop feature's promote) to `7d5cb34d`: a release merge of the dell1 feature alone, first parent `10e7664d`, second parent `624e2533f665` (the row's bound head), made by `0.9.0_WK_AMGT_RESAPP~423` on `release/20261014T003210Z`; message body `Feature: cand/dell1/amgt-sa-header-money-and-dash-reasons` and `Approved-By: 1.0.0_SA_CTO~DELL1 @dell1-20261014T001511Z-633a`. Tag `portal-v2.1.215` is at the tip. CI run `38491072873` concluded success on `7d5cb34daabce225bb9a2635c541f6ff3fd64e52`.

Reads, direct from git on `origin/PROD` (the project's release-check tool resolved `PROD` to the stale LOCAL branch `PROD` @`10e7664d` and is NOT cited; a row for that is owed):
- first-parent walk from the settlement `63c4f9e3`: 2 commits (`10e7664d` for `cand/laptop/contributing-boxes`, `7d5cb34d` for the dell1 feature), each a two-parent merge with `Feature:` and `Approved-By:`: `unapproved=0`.
- None of the seven unapproved dell2 DEV commits (`62d455f5 9ef6a359 923f7d69 794b7df4 73d8d3a4 0101dd66 a577cba5`) is on PROD. The dell1 DEV merge `5e40e541` is not on PROD either (PROD holds its own release merge of the same feature, as for the first feature).
- The class is `opal-internal` (Security Analysis), so the push law needed no word from Andrew.

What it adds: the PROD side of the route ran organically too, on a second box, shipping only the approved feature and leaving the unapproved DEV commits behind, the property FWD-5 asks for. What it does not: the client-facing case (FWD-1's close) still waits on Andrew's rulings on the dell2 rows.

## Addendum ~03:3xZ -- a third approved feature reached DEV through the installed pre-push hook (issuer read)

`origin/DEV` moved `5e40e541` -> `514df1bb`: merge of `cand/dell1/amgt-sa-currency-symbol-and-reasons`, first parent `5e40e541`, second parent `051ad362d4dd` (equals the row's bound head), made by `0.9.0_WK_AMGT_RESAPP~423`; trailers `Feature:` and `Approved-By: 1.0.0_SA_CTO~DELL1 @dell1-20261014T031653Z-f1a4`. Reads from the laptop: `approval-status` = `APPROVED valid=yes ... head_sha=051ad362d4dd commits=2 class=opal-internal` (cluster copy written 03:18:42Z); `dev_push_payload_gate.py --remote-sha 5e40e541 --local-sha 514df1bb` = `PASS route=A`, `ADMITTED commits=1`; `portal-dev-approval-read.py` = `first_parent_commits=6 approved=3 unapproved=3` (the three unapproved are the dell2 ANLREQ merges). MSTR~DELL1 (msg 109061) reports the push went through the installed hook on a gitlink box: the open read in act A15. Still not shown: the client-facing case (five dell2 rows OPEN).

## Addendum ~04:0xZ -- two more PROD promotes and a fourth approved DEV feature (issuer read)

`origin/PROD` is `7db035e4`: two chosen-set release merges since `7d5cb34d`, both by `0.9.0_WK_AMGT_RESAPP~423`: `0910f4ad` (`cand/dell1/amgt-sa-currency-symbol-and-reasons`, `Approved-By ... @dell1-20261014T031653Z-f1a4`) and `7db035e4` (`cand/dell1/aifill-blocks-prod`, `Approved-By ... @dell1-20261014T022349Z-a565`, bound head `53de2b9d844b`). `origin/DEV` is `ab8ecc56`, the aifill merge (route A, `ADMITTED commits=1`). Reads: `portal-release-build.sh --check PROD --repo portal --prod-ref 63c4f9e3...` = `features=4 first_parent_commits=4 unapproved=0 ref=refs/remotes/origin/PROD sha=7db035e448d9` (the DP-i-1 repair reads the right ref: at the base it read the stale local branch); `portal-dev-approval-read.py` = `first_parent_commits=7 approved=4 unapproved=3`. All four PROD features are `opal-internal`, so no word from Andrew was needed. The three unapproved DEV commits are still the dell2 ANLREQ merges, none on PROD. Not shown: the client-facing case (five dell2 rows OPEN).
