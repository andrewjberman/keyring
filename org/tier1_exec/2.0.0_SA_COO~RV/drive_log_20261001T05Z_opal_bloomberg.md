# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-01 05Z (opal_bloomberg)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

Scope: ETFS_RIVALS. The lease read FULL on every tick.

| tick | time | limb | round | TOs t/T | outcome |
|---|---|---|---|---|---|
| 7 | 04:55-05:26Z | L7 -> L8 | 2 | 9/9 | DRIVE FORWARD. d-3 was closed and drained, the served page was read, and the packet went to the CVO |
| 8 | 05:27Z | L8/L9 (CVO) | 2 | 9/9 | NO-OP. Packet msg 27541 was READ by 3.0.0_SA_CVO~RV at 05:26:41Z |
| 9 | 05:35Z | L8/L9 (CVO) | 2 | 9/9 | NO-OP. Waiting on the CVO's L9 and L10 slug; no CVO artifact yet |

## Closed decisions
- **TO-RIV-d-3 flipped complete @8ad2033519.**
  - The issuer re-ran d-3.AC1, AC2, AC3 and b-1.AC3 live; all PASS 0 failures.
  - Row W5-S26 is disarmed by the issuer's test fix. Its record is row Z-S3.
  - The package reads 189 passed, 2 skipped.
- **Drain to CLOUD @caafc907e7.**
  - The shared index carried other seats' staged paths twice, so `safe-merge` refused the main tree.
  - The graded merge of CLOUD into `wk-rivals2-5r` ran under `safe-merge` in the worktree, followed by `git merge --ff-only` on CLOUD.
- **Drain-end packet @d152231e55** (`round2/DRAIN_END_READ_ROUND2.md`).
  - W2-S4 stays ARMED. Issuer silver holds 325 of 325 dates in the old-format id, so a re-capture of a landed BASG date keeps the old rows.
  - It is carried to round 3 as the first cell.

## Instrument note
This session launched with `OPAL_AGENT_SERIAL=2.0.0_SA_CVO~RV`, the mistyped serial; Andrew chose 2.0.0_SA_COO~RV. The row
gate therefore read the committer as `2.0.0_SA_CVO` and refused this seat's own row as foreign. Every commit now exports the
corrected serial.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `.tools/safe-commit.sh` | d-3 close and the packet | LANDED after the surfaced_at format fix and the serial env fix |
| `.tools/safe-merge.sh` | CLOUD into the worker branch, twice | PASS: row gate and corpus clean on the merged index |
| `aws s3 ls` (rail-checked) | W2-S4 exposure census | 325 dates: 325 old-format, 0 new-format |
| `aws s3 cp` | the served page and manifest at close | read: grouped, 6 of 13 updated, freshness FAIL on 4 PFOE rivals |
