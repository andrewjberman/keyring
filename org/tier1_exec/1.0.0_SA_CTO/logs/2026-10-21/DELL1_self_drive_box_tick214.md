# DELL1 self-drive box -- ticks 213-214, 2026-10-21 ~01:18-01:49Z (delta: all six Fidelity files landed; round 3 issued; co-7 addendum 2 countersigned and the failed-start ruling; Andrew-direct backfill word)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 01:49Z. Acked since tick 212: 8891, 8904, 8909, 8912, 8916, 8919, 8924, 8930.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool.

## Acts and rulings
- **NFRA_FIDUPL, ALL SIX files landed for 20261019** (P1 8909; read by me): account 3,794,367 B, balance 1,221,776, position
  30,334,785, prices 646,731, security 656,599, transact 602,207, run record `run-20261021T012004Z.json`, outcome ALL_LANDED, re-landed
  from the box's copies after the per-file date fix (FU-s-4 REPAIR 1 @a71eb71abb0) with no new sign-in. FU-s-13 whole-root apply
  complete @aeebf2f65e5 (1 added, 2 changed; the per-G list secret `fidelity/alongside/perg-list` exists with no version).
  - **Ruled** (01:05Z): the secret's value is the switcher's list as the box's probe reads it, put by the CloudOps lane with a
    `measured` claim; `tmp/cotbooks/` is the comparison; nobody types a G number.
  - **Ruled** (01:22Z): the thread's order: switcher read + secret, daily logout, schedule addendum (CloudOps applies), backfill
    cells cut in parallel.
- **Andrew-direct via ms** (bus 02abe551 01:27Z, MSTR 8912; CRO 8916): the backfill's earliest date is found EMPIRICALLY by exports at
  progressively earlier dates until the channel refuses or returns empty; nothing waits on Andrew's two inputs; report per file type
  to the ms inbox. Recorded @b979ff17e9 (`ANDREW_DIRECT_20261021_012xZ_FIDUPL_BACKFILL_EMPIRICAL_EARLIEST_DATE_NO_WAIT_ON_ANDREW.md`).
  Ownership ruled: P1 runs (CRO method @877f50fce8), CRO~FIDELITY compiles, MSTR carries. The one conditional Andrew act: a
  back-dated export profile, only if the wizard's date field cannot be automated on the first run.
- **Round 3 issued** (P1 8919, @6bd116284f + @0b37a83d8d), seven cells FT-s-1..7. GO as cut; FT-s-6's schedule ON bound to a
  never-widen addendum I countersign (secret version, seed keys, rule expressions, first fire read); P1 amended it so @845e8d758ab.
  Since: FT-s-5 complete @cdfdc9dbf34 (box role may put the per-G secret only, 0/1/0 apply), FT-s-4 complete @bbea5c0468e (backfill
  runner), FT-s-1 drained @ac1fb3cd67f (switcher_list.py).
- **AMGT_HARVST co-7 addendum 2** (W1 8904): countersigned @368c6df8c6 with the start span bound to 01:30Z-03:59Z, read from the
  producer's own rule (`gold_refresh.py:140-142` as_of = previous trading day of the NEW YORK date; `publication_gold.py:547`
  partitions by as_of; New York is UTC-4, the day turns at 04:00Z; W1's span ran to 05:00Z).
- **co-7 stage 5** (W1 8924): task 3f57aad6 FAILED TO START (CannotPullContainerError, "schema1 conversion ... not found"); I read
  describe-tasks, ECR (one image, the digest present) and the three gold prefixes (24/26/10, newest keys unchanged). Ruled: not the
  one write run; SC1 may probe the pull and run ONE run-task again before 03:59Z; a second failed start is a new push, digest and
  addendum 1. Ruling @cb877ea56b. SC1 filed row D1-S70 @92eac31e166.
- **Seats:** the deaf-seat fix held (MSTR 8883); NFRA1 healed at its 00:30Z expiry, SC1 hears by its own poller; `/unstick` fixed
  @2138a1f383; row S28 @a377a9ef590.

## Scope state
- **NFRA_FIDUPL:** FT-s-2, FT-s-3, FT-s-6, FT-s-7, FU-s-11, FU-x-1 pending (6 of 9 round-3-era orders open). 13 objects under
  `fidelity/alongside/bronze/` (6 data for 20261019, 7 run records). The 3 fetch rules are DISABLED.
- **AMGT_HARVST:** round 100, co-7 stage 5, the write run's second start pending before 03:59Z.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a back-dated Fidelity export profile, only if the wizard's step-1 date field cannot be automated (CRO 8916).

## Compiler Tools
- `list-objects-v2`, `s3 cp` of run records (counts, sizes, dates only).
- `ecs describe-tasks`, `ecr describe-images`, the gold prefix counts (`# rail-checked`).
- `sha256sum` and `git show <pin>:<path>` (addendum 2); `Read` of `gold_refresh.py` and `publication_gold.py`.
