# Drive log -- 2.0.0_SA_COO~ZI -- 2026-10-09 10:0xZ-11:2xZ -- host opal_bloomberg

**archetype:** COORDINATE

Loop: `/canonical-drive NFRA_IAMROLES202609` every 10m, cron 40356b22 (ANDREW_DIRECT_20261009_073xZ).

| tick (UTC) | limb | round | TOs t/T | act |
|---|---|---|---|---|
| 10:02 | L7 | 5 | 2/4 | 09Z drive log @5b7b6ad512 |
| 10:05 | L7 | 5 | 2/4 | the v-2/v-4 GO (32648) read OFFER-EXHAUSTED; re-sent (32652) |
| 10:15 | L7 | 5 | 2/4 | lane working v-2 (plan @59112aafed) |
| ~10:2x | L7 | 5 | 2/4 | v-2 ten-row carrier @8909011839, after an issuer check (exactly 10 row first-lines, rows=16 unowned=0) |
| 10:34 | L7 | 5 | 2/4 | v-4 started: ledger iamroles-fwd5-narrowing OPEN @f07f3dcc87; the in-flight edit equals the signed patch |
| 10:44 | L7 | 5 | 2/4 | v-4 APPLIED @e02476796b (~10:36Z, before the 13:02Z run). Issuer's own live read: DescribeSecret implicitDeny, GetSecretValue allowed, ReadAuthBundle Action = [GetSecretValue] |
| 11:04 | L7 | 5 | 2/4 | nudge: v-2 proof + flip |
| ~11:1x | L7 | 5 | 3/4 | v-2 COMPLETE @38b456ff1c, issuer-verified on the COMMITTED blob (VALID; rows=16 unowned=0 at HEAD; 10 roles in the plan; one author) |

## State at close of hour

- FWD-4: 16 of 16 rows carry a named owner and a reason on the committed table. The CVO grades the APPLIED bar.
- FWD-5: the narrowing is live and verified. `MATCHES-PREDICTION` is withheld until the first 13:02Z run after the apply is read
  from 13:30Z against F1-F4. The ledger leg OBS is open.
- A lesson the lane surfaced, kept for the round's analysis: v-2 AC1 reads the file on DISK, so uncommitted bytes satisfy it. The
  lane ran a committed-blob control (unowned=10) and withheld its proof until the carrier landed.

Push state: the lane reports both of its commits on origin @04124013f9 (its ls-remote read); this seat's commits: box-sync carries them.
