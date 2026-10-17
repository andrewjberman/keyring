# Drive log 2026-10-17 03Z -- 2.0.0_SA_COO~D2 (IRPT_DASHBD workstream B-49F + contract; DSGN_IRPTV1 second project, no order of mine)

Claim words: MEASURED = read from a file or the live account; INFERRED = from code, not run. Counts and hashes only.

## Cottonwood Performance read path (CTO ruling A, msg 10134), round 150

| cell | order | worker | state at 03:4xZ |
|---|---|---|---|
| C0 read-only trace | TO-DB-b-318 | IB2 | complete (record verified by p184) |
| C1 forward code | TO-DB-b-319 | ~253 | LANDED on the trunk at 3eb27c60c0; p185 AC1..3 PASS on the issuer's reads from the main-tree checker; 7 files, 0 deletions; worktree and branch removed |
| C2 Terraform | TO-DB-b-320 | ~254 | running; AC1, AC2, AC3 PASS on its tree after my p186 repair |
| C3 function-map | TO-DB-b-321 | ~255 | running; reference run builds both entries to one hash (32 members) |
| C4 never-widen pair | to be cut | - | packet drafted and committed as DRAFT (06c74f2782); halves bind to final bytes after C2/C3 |
| C5 real run | page owner ~C2 | - | after C4 |
| C6 ownership map from the dell1 match sheet | to be cut | - | newer pair on this box outside the repo; behind C5 (Andrew-direct, CTO msg 10215, 10227) |

## Defects of the issuer's own, found by the workers and repaired (each reported as a BLOCKING row by the worker)

- p185 AC1 diffed against an old pin, so files other lanes had landed read as "outside the agreed set", and it refused the worker's own folder: re-based to the worker branch point (8d31127ce6), selftest green on a fresh reference tree and red on 5 mutants.
- The reference test file failed the commit gate (ruff F841, one unused local): fixed at fc8d52804c.
- The proof validator compares the recorded invocation to the order text: the three criteria of TO-DB-b-319 now run the main-tree checker by absolute path (2d2dc06faf). Correction to that commit's message: GATE (viii) DID grade the modification (1 of 1 modified order already declares placeholders); the message said no limb graded it.
- p186 AC2 counted the nested portal checkout (a gitlink the provisioner leaves modified) as a changed file: excluded from the working-tree half (f2846b8c4a); a worker commit of it is still refused.

## Rulings (inside this decomposition, the issuer's)

- No ownership-map grant is added to the Cottonwood role beyond the object-scoped read: an absent map reads as an empty map under both wire shapes (loaders.py 241-303) and a Global staff caller takes the firm population (resolve.py 445-451). INFERRED, not run; the pair's probe is the first execution.
- Both read-function entries move together or neither does (p187 AC1 and AC2).

## Waiting on

Workers ~254 (refreshing its proof after the repair) and ~255; IB2 to land the function-map port of the Cottonwood publish entry (e8cf39af23, asked); Andrew's smoke of the Performance tab (row dell2-20261017T003553Z-f1bb, HELD, no change to that branch).

Push state: LOCAL (box/dell2 is MSTR's to push).
