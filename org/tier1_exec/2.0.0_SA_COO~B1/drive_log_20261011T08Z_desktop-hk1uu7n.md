# /canonical-drive log -- 2.0.0_SA_COO~B1 (dell1), ADVI_FIRMBKTS round 3 window, 2026-10-11 08Z

**archetype:** COORDINATE

Loop: none armed. Same session as the 07Z log.

| UTC | limb | project/round | TOs t/T | act fired |
|---|---|---|---|---|
| 07:5xZ-08:1xZ | L7 | ADVI_FIRMBKTS 3 | 7/11 | act 1 re-addressed off-box: CTO ADDENDUM 2 (Dell deny stands), TO-FB-f-8 amendment 6 (`7bc01f770a`), crossbox ORDER XB-20261011T080600Z-ba12 to fresh laptop lane `~FBL` (delivered, seated); Dell entry closed SUPERSEDED |
| 08:0xZ-08:3xZ | L7 | ADVI_FIRMBKTS 3 | 7/11 | FB-f-9 phase A2 (rotation source, write sentinel) merged `628d9f241b`; carrier ruled (ADDENDUM 4); E_01/E_24 measured (row D1-S14); FB-f-10 DELTA_TOOL written; read-site hazard (35 rows) raised, CTO ADDENDUM 5, phase A3 cut and worker `~20` spawned (`56c2234580`) |

## Rulings by the issuer in this stretch

- D1-S13/amendment 5: the comp-iam line of TO-FB-f-8 corrected (the simulation grain at `*` was mine); step 2a replaced by
  the executor's measure (a refresh-only reconcile moves nothing).
- D1-W19-S7/S8: the rotation's copy source and D_00f's sentinel are code, not executor acts: cut as dormant phase A2.
- D1-W19-S9: an environment condition for the phase B pair (no runner overrides `BD_S3_BUCKET`), not a code change.
- D1-S14: E_01 is retired from the served-writer census on the module's own rule (3 of 3 objects, newest 2026-04-07);
  E_24 reads dead by ADDENDUM 4's test (0 of 4,010 SendCommand events in 45 days), one residual StartSession; the CTO rules.

## Defects in this tick's row, stated

- My comp-iam read was at resource `*` where a deny names the functions: the apply was refused 403 and a worker-grade
  executor spent a window on it. The read is now resource-scoped on the order's own step 0b.
- ADDENDUM 2 condition 2 ("only writes move") was the CTO's, but the census that produced it was mine: it enumerated
  writers and not the readers of their outputs. The reader census (`r3_reads.py`, 127 sites) is the repair.
- The phase A census classed E_01 under a served class by script, not by key: the key is outside every served prefix.

## Left open

- Act 1 (`TO-FB-f-8`): the laptop actor `~FBL` runs steps 0b, 0c, 1-7; the CTO reads at `Deployed`.
- Act 2 phase B: needs `FB-f-8` complete, phase A3 merged (worker `~20`), the pair with the read/list/delete sites in its
  blast radius, the gold_dispatch.sh export read-back, E_01/E_24 ruled, and QA not inheriting `canonical`.
- Act 3 (`FB-f-10`): DELTA_TOOL written; expect about 49,000 overwrites (destination versioning Enabled).
- Act 4 (`FB-f-11`): its F6 deploy changes the same protected router, so it routes to the laptop identity too.
- Push state: LOCAL on `box/dell1` except the commits MSTR pushed at the ORDER commit.

## Compiler Tools

| tool | result |
|---|---|
| `r3_rotation.py` (issuer, new) | base 1 of 3, reference edit 3 of 3, merged 3 of 3 |
| `r3_reads.py` (issuer, new) | base 127 sites: ROUTED 22, NOT-SERVED 36, EXEMPT 0, UNROUTED 69 |
| `r3_f7_delta.py` (issuer, new) | selftest 6 of 6; live read-only plan: absent 0, equal 52,910, differs 0, versioning Enabled |
| `proof-of-spec-check.py` | CHECKER-SCOPE refusal when run from the shared checkout against a worktree instance; VALID from the worktree and on the merged tree |
| `wk-provision.sh remove` | the portal worktree blocks a bare `git worktree remove`: removal goes through the tool |
| `comp-rail` | denied a piped census and an unscoped `find`; named-file reads and native Grep were free |
