# Drive log -- 2.0.0_SA_COO~MP (sitez) -- 2026-10-14 17Z-20Z -- NFRA_MCPORTAL

## Closed decision 1: PC round 1 closed and graded; round 2 issued in ONE commit

| act | commit / msg |
|---|---|
| MP-pc-6 drained (worker ~24), AC1 re-run PASS on the merged tree, pointers re-read; rows Z-W24-S1..S3 ruled in the merge message | @33741bf311, complete @669a3e7f1d |
| PC round 1 drain packet to 3.0.0_SA_CVO~Z (one judgment criterion, MP-pc-4 AC2); READ in under a minute | @b53cc655ee, msg 34158 |
| CTO round-1 analysis in hand: recut R1 + F2 + U2 in one issuance (msg 34162); Andrew's finish-then-close word (msg 34168): "get as much done as possible ... close them out or at least put them on hold" | analysis @771fadb53b |
| Decomposition v10 (PC round 2): 8 cells, 5 chains; 12 checks dry-run at the base, three run-file checks exercised green and red | issuance @9af1cee1ab, `fanout: 5 of 5 chains, cap 8` |
| Workers ~25 ~26 ~27 ~28 ~29 spawned (haiku, effort high) in C:/tmp/mp-pd-25..29 | 18:2xZ |

## Closed decision 2: four round-2 cells drained; two amended by the issuer

| act | commit |
|---|---|
| MP-pd-1 (R1): the People view read under the OPERATOR role, 1 of 1 principal, 5 of 5 tools equal. Row Z-W25-S1 (Query denied to the operator role) ruled not a blocker: GetItem under the same role read it | @9771f6af91 |
| MP-pd-2 (F2 writer): `set_person_access`, 12 new tests, suite 36 passed. Row Z-W26-S1 (the store returns revision as Decimal) fixed in the writer by the worker | @dc132db72a |
| MP-pd-3 (F2 gateway handler): AMENDED by the issuer (A1): my cut left an exact-key-set test unchanged against the added `principal` key, so AC2 could not pass; the worker's BLOCKING row was my defect. Re-seated, 4 of 4 | amend @7484bf5fca, merged @75248b6d2e |
| MP-pd-5 (U2 script): 7 of 7 named tests plus the real subprocess invocation; the issuer read the 174-line script before releasing MP-pd-6 | @e327ca0703 |
| Statuses flipped complete for pd-1, pd-2, pd-3, pd-5 after the issuer re-ran 7 of 7 checks on the merged tree, py_compile on 4 files, and the gateway admin suite (93 passed) | @35199152d7 |
| MP-pd-4 (F2 page): AMENDED (A1): the gateway answers a REFUSED verdict as HTTP 409 and the page threw on it; the contract had left the mapping unstated. Re-seated worker has committed mcportal f7760a6; its report is pending | amend @87b2ded2cf |
| MP-pd-6 (U2 enable) GO: G-ENABLE held; worker re-seated in slot ~29 with the backup-outside-the-repo and rollback-on-a-copy steps | @88dbfe0e28 |

Process facts worth keeping: (1) a worker order is amended by committing the order to the trunk and putting that file on the worker's branch; a finished subagent cannot be resumed here, so the slot is re-seated with its prior commits named as inherited state;
(2) `safe-merge.sh` conflicts on the shared surprise-channel file at every concurrent drain, and the resolver that always works is to keep ours whole and append the branch's new fenced blocks (scratch helper, not committed);
(3) `safe-merge.sh` refuses while a peer has anything staged, and a retry a few seconds later passes.

## Carried state

- Gates: MP-pd-7 (F2 release, `0.7.0_AE_CloudOps~MQ`) waits on NFRA_OPLGTW OG-cp-1 being RELEASED (its order is not yet issued by `2.0.0_SA_COO~O`); MP-pd-8 (close run) waits on Andrew's sitting on the People page.
- After MP-pd-4 drains, the mcportal commits need a fast-forward to origin DEV by `0.0.0_AB_MSTR~Z` (only MSTR pushes) before the release can name them.
- The FWD-22 transport and panel are NOT in this round (decomposition PD.8 item 3); to state to the CTO at the drain-end message.
- Calls at Andrew unchanged: 21d9, def4.
