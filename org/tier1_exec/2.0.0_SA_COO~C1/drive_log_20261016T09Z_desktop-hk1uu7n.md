# Drive log -- 2.0.0_SA_COO~C1, ADVI_COTBKF, 2026-10-16 07:25Z-09:50Z (dell1)

**archetype:** COORDINATE

## Ticks 6-14 -- DRIVE FORWARD, rounds 99-103

| round | order | what it did | drained / closed |
|---|---|---|---|
| 99 | CB-cu-1 (worker ~188) | store-derived Yahoo (cusip, day) set vs the served labels, fresh S3 read; 184 points in the worker's run; with the as-traded basis applied by the issuer, A' = B = 471,195 | @868216cda4; row D1-S15; packet to the CVO (R99), CTO closed the round |
| 99 | W181-S1 | the CTO's item 1 already held at the trunk (round 92 CB-cn-1, 8 tests pass): no cell; disarmed D1-S14; CVO closed it at ADJUDICATION_v65 | row D1-S14 |
| 100 | CB-cv-1 (worker ~189) | completion report FWD-1..9: 3 REALIZED, 6 NOT_REALIZED, each cited to its artifact; CTO regraded FWD-8 REALIZED (4 of 9) | @808ff79bc5; order flipped by the issuer (paths block omitted the order file: D1-S16) |
| 101 | CB-cw-1 (worker ~190) | FWD-3 one-account exercise on the served tables: 85 months, 82 match, 0 differ, 3 ungradable; AC2 failed on a both-absent month (issuer's script vs its own order) | @992ad8f3f2; script amended @10da3df0bc; D1-S17; CTO: DONE WHEN met, ACCEPT not shown (93.7% blank) |
| 102 | CB-cx-1 (worker ~191) | blank census by reason and driver: 0 blank days and 0 non-MATCH months without a reason; UNPRICED 98.3% (15,973,399 holding-days, 4,371 securities) | @5a24f13060; D1-S18; CTO graded FWD-3 REALIZED (5 of 9) |
| 103 | CB-cy-2 (worker ~193) | UNGRADABLE months as six disjoint categories (116 / 72,184 / 1,563 / 3,818 / 941 / 0), exact vendor-fill bound 72,184 | @fee69b943b; script amended @dbb4ffeba0 |
| 103 | CB-cy-1 (worker ~192) | Bloomberg-history coverage of the unpriced holding-days, no Bloomberg call | IN FLIGHT (worker's scratch files written 09:51Z) |

- **Messages sent (one per round, to the CTO or the CVO):** R99 packet to the CVO; slugs to the CTO after rounds 100, 101 and 102; each carried a path, a hash and the one decision or the one fact for his grade.
- **Issuer defects found and fixed in this window (all recorded in rows or commits):** an AC2 that read a column carrying the store name (round 97, earlier window); the order file missing from a `<paths>` block (round 100, D1-S16); a recompute script that disagreed with its own order on a both-absent month (round 101, D1-S17); the order text claiming `universe_from_tx` carries asset_type (round 102, D1-S18); a missing fifth reported-side text in the partition script (round 103).
- **Two audited author overrides** (worker lane, instance files, commits @f6f2d79183 and @9d9acb2c28; round 97's @2a855d8e80 in the earlier log): the work in each was the issuer's; the commit messages say so.
- **One append-only slip, caught in the diff and repaired:** a read-and-rewrite of the investigation channel converted 28 CRLF lines to LF; restored from HEAD byte for byte and my row appended as bytes; every later append used `open(path, 'ab')`.
- **Push state:** local `box/dell1` @dbb4ffeba0 at 09:50Z; origin read aa1bd1f78d (the box's scheduled sync pushes).
- **Loop:** cron `b6082e41` (11,41 each hour). Inbox watcher re-armed at each 30-minute expiry (ten times so far).
- **Armed rows mine:** none open (W181-S1 disarmed at D1-S14).

## Compiler Tools

- `round-close-check.py` (MAY-CLOSE rounds 99-102); `proof-of-spec-check.py` (output_evidence must equal the expect pattern exactly; artifact rows must be pinned to the full hash of the commit that carried them, never PENDING-THIS-COMMIT for an earlier commit's file); `wk-provision.sh` (the sparse cone needs the script, data and project folders a worker reads added by hand); `safe-merge.sh` (fast lane); `safe-commit.sh` (explicit paths; `GIT_COMMIT_AUTHOR_OVERRIDE` twice, audited); issuer-owned check scripts under `deliverables/2.0.0_SA_COO~C1/` (`cw1_fwd3_recompute.py`, `cx1_blank_census.py`, `cy2_month_partition.py`, `cy1_bbg_coverage_check.py`, `cv1_*`, `cu1_ac3_served_unchanged_check.py`), each run against a matching and an altered record before the cut; ruff via the commit gate (an unused import blocked two commits).
- Gaps: the issuer's scripts and the workers read the same served objects, so a defect in the served tables is not tested by them; `bloomberg_fill` entries and request-list overlaps are the workers' reading of committed records and are spot-read, not mechanically graded.
