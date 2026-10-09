# 2.0.0_SA_COO~MP drive log -- 2026-10-09 00Z-04Z -- /canonical-drive NFRA_MCPORTAL 30m (:22/:52)

| tick | time | limb | round | TOs t/T | act fired |
|---|---|---|---|---|---|
| 4-6 | 23:38Z-00:29Z | L8 | 4 | 2/2 | NUDGE once: packet msg 32122 read OFFER-EXHAUSTED at 3.0.0_SA_CVO~Z; READ at 23:43Z; then NO-OP while queued |
| 7 | ~01:0xZ | L8->L10 | 3+4 | 20/20 | RULE: the CVO compile read the L10 precondition NOT MET (MP-c-1/v-1 staged) -> superseded both @39ea2d5e3e on the round-2 precedent; `<to_id>` on every order @5e59e66320; project close MAY-CLOSE |
| 8 | ~01:3xZ-02:0xZ | L6 | 5 | 0/5 | DRIVE FORWARD: CTO analysis @460bc0af2f -> round 5 ONE issuance @44fa181d43; the seating lint moved the applier to a fresh lane 0.7.0_AE_CloudOps~MP (spawned, LIVE ~80 s); GO sent; row Z-S20 disarms four round-1 rows @835b1c0c02 |
| 9-12 | 02:10Z-03:28Z | L7 | 5 | 0/5 | NO-OP (applier working; a screen peek at 02:29Z confirmed it, no keys sent). Andrew asked at ~03:1xZ: G-REL ask to 2.0.0_SA_COO~O, owed since round 4's drain and not yet sent, now sent -> (b), r29 drain ~12:00-14:00Z (msg 32304). RULE on Z-S21: the policy name was refused at apply and pinned by AC1 -> amendment 1 @807220a352, builder name gateway-mcportal-fabric-read-policy |
| 13 | ~03:4xZ-04:1xZ | L7 drain | 5 | 1/5 | DRIVE FORWARD: MP-x-3 drained @edf50ff4d3 (policy LIVE; issuer re-run AC1-3 PASS); the flip was refused because the proof instance was INVALID (11 schema violations) -> ruling re-sent citing the order (the first send was refused by LD-0529) -> fix 42ed038fea drained @bee68a57eb; flipped complete @93052772a7 |
| 14 | ~04:2xZ | EMPTY -> /next-calls --drive | 5 | 1/5 | WHILE BLOCKED (MP-x-4 on r29): read-only host probe of the handler: cold 21.3 s, warm 0.8 s, 3,004 records; told the applier (information only); removed the nested mcportal worktree (branch kept at d60b4e0) |

## Decisions

- **Rounds 3-4 closed at the project grain** by superseding the two Andrew-gated orders, which never ran. They are re-cut
  unchanged in round 5 (MP-c-2, MP-v-2). Andrew's hold on Alyssa's close run until r29 is untouched.
- **Applier lane:** `0.7.0_AE_CloudOps~MP`, a fresh lane, because `~Z` held three other projects (rule 27 seating).
- **Z-S21:** builder-output policy name (option (a)). Option (c), the commit naming limb RAISEing a name the apply limb
  then refuses, stays on the row for the gate's owner.
- **Two worker worktrees (`C:/tmp/mp-r4-5`, `C:/tmp/mp-r4-6`) are left in place.** Their branches are merged, and only
  untracked `.scratch/` files remain. A forced removal is a recursive delete, which needs Andrew's word.

## Waiting on

- G-REL: NFRA_OPLGTW r29 drained (2.0.0_SA_COO~O; deploy >=11:00Z, drain ~12:00-14:00Z). Then MP-x-4 starts at
  0.7.0_AE_CloudOps~MP.
- G-SEE (after MP-x-4), G-CLOSE (r29 + Alyssa's sitting), G-2ND (after MP-x-4): Andrew.

## Compiler Tools

- `round-close-check`: per round and project-wide REFUSED -> MAY-CLOSE after the `<to_id>` and supersede fixes.
- `to-pipeline-gate`:
  - the round-5 issuance was admitted;
  - the MP-x-3 flip was refused on an INVALID instance, then admitted.
- `to-decomp-ref-lint` seating (ANNOUNCE) refused `0.7.0_AE_CloudOps~Z` for MP-x-3/x-4.
- `proof-of-spec-check`: INVALID with 11 violations, then VALID.
- `missions-tree-index` `check` and `derive --write`: 0 violations after each stage change.
- `mstr-spawn` pre-flight: 1pt 0 of 12, markers 0, concurrency 4/20, and 1d clean.
- `unstick --peek`: one peek, no keys sent.
- SSM host probe: read-only, scratch dir removed.
