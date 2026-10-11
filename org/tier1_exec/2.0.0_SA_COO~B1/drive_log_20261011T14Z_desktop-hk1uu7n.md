# Drive log -- 2.0.0_SA_COO~B1 -- 2026-10-11 14Z -- ADVI_FIRMBKTS (round 4, EXECUTING)

| tick | limb | round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| 14Z | L7 execute / L10 pending | 4 | 17 complete or merged, FB-g-17 merged this hour, FB-g-19 and FB-g-20 issued | 17 of 19 | n (round 4 builds the flip; the act chain is the thread) | DRIVE FORWARD: act 3b prerequisite cut on the CTO's ADDENDA 8 and 9 |

## What fired

- D1-S27 was ruled (round-3 ADDENDUM 8): act 3b, the readers' admission, one prerequisite pair before acts 4b, 4c and 4.
- N x 2 printed (`deliverables/2.0.0_SA_COO~B1/round4/IDENTITY_CENSUS_20261011.txt`, `r4_identity.py`, @9d7fab65d7): 1 of 11 reader
  principals passes fence and identity today (partners-lambda-role). The performance adapter is admitted but its three hand
  statements scope it to the holdings gold; the other nine fail identity, six also fail the fence.
- The CTO ruled the generator first (ADDENDUM 9, msg 3917): a scoped row's `prefix` takes a list. Cut `FB-g-19` (module) and
  `FB-g-20` (module outputs the canonical ownership key), issued @d2d6ec2370 (fanout 2 of 2, workstream FENCE3B), checks
  `r4_modfence.py` and `r4_modkey.py` each dry-run at base (3 of 4 and 3 of 5 as expected). Decomposition amended 7: cells 19.
- FB-g-17 merged @dab8535aef; `r4_canonlist.py` 4 of 4, `r4_validator.py` 4 of 4, `r4_flip.py` 4 of 4 at the merged head.
- Census read, not assumed: the canonical bucket's ownership directory holds exactly one object (the 474,726-byte map), so a
  directory-grain scoped row is the key in effect today.
- One ask out (msg after 3917): a generated bucket-policy Allow beside each scoped Deny row instead of nine identity applies.

## Open and parked

- Exec-summary generator's PutObject (`platinum/advisors/*/exec_summary.json`) cannot be a scoped row (Get/List only): a call for
  the CTO at 4b, not yet put.
- Act 3b COO half, the staged act order and the executor's PutBucketPolicy authority read follow the CTO's answer.
- FB-g-15, FB-g-16, FB-g-17 instances and flips at the next drain (override `TREE_COO`).
- Andrew-only: FWD-7 and FWD-8 (DEC-13); the SEV1 text; the AWS Support case if it did not arrive.
- Push state: LOCAL on `box/dell1`.
