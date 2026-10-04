# /self-drive AMGT_FRIDAY -- tick 1 after the SentinelOne crash (1.0.0_SA_CTO~Z, 2026-10-04 ~20:0xZ -> ~20:1xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141` (hourly at :13 local). Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. It was committed before this tick. Previous log: tick 44 @29e44bd234, under the 2026-10-02 record.

## Session before the arm

- **Relaunch:** `/watcher` armed and registered; startup per org/XXX.md. Unread msg 29186 (OFFER-EXHAUSTED) was read and acked.
- **Crash assessment** for `0.0.0_AB_MSTR~Z` (msg 29191): `deliverables/CTO_Z_FABRIC_STATE_20261004_19xxZ_SENTINELONE_CRASH.md`
  @bbfd37b595. It covered 28 worktrees, 10 seats in the pre-crash telemetry window, and found 0 open deploys in this fabric.
- **NFRA_SPRINTWIN** (outside this scope): CVO~Z signed the ratified-text half @43b01c88f8 (msg 29196). This seat landed the
  CONTRACTS amendments v0.2 @1f344f57f4 (window_end, an 8-day look-back, the union of every census file in the window, and the COO
  half on `2.0.0_SA_COO~H`). Relayed in msgs 29197-29199.
- **Re-arm:** Andrew, ~19:4xZ, "2.) Yes" to "Restart the AMGT drive loops?" (msg 29200, record @3166fec43e).

## Measurements (tick 1)

- **Device:** sitez (`agentbus-sqs.sh device`).
- **Scope:** `directives-check --json` reads 15 live directives. D5 (SITEZ) holds AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP and
  ETFS_RIVALS, with 118 open TOs directive-wide. D13 (LAPTOP) holds DSGN_AMGTV1 with 1 open TO. D13's device mismatch is carried
  from the prior arms, because Andrew named the project.
- **Sequence:** `sequence-check --project` reads all 5 UNPLACED (the file lists 0 projects), with 0 flags.
- **Inbox:** 0 unread at the tick start. Since then 29208 and 29209 arrived; both were read and acked.
- **Active commitments:** 0 lines in 0 of 27 ledgers (24h).

## Calls closed and acts

| msg / source | item | ruling | act |
|---|---|---|---|
| row `AMGT_HARVST-Z-S82` (COO~H, "the CTO's scope call") | 19,967 of 31,042 served gold mention rows are pre-2026 | **KEEP in gold; CLIP the served events and timeline at STORE_START** under a pair (driver's rec; the windows' existing bound is the precedent) | msg 29207 to COO~H; COO~H recorded row Z-S83 @7a88db8538 (msg 29209) |
| 29208 CVO~Z slug, HARVST r44 (ADJUDICATION_v56 @876c7d30e1) | L10 owed | **Round 44 CLOSED.** FWD-5 REALIZED. FWD-7 NOT re-ruled under C-HV-RANK-DECLARED-SET and moved to the collection partition. FWD-2 and FWD-12(c) repairs cut for round 45, with the Z-S82 clip. | analysis @ed9efe80ea; project.json phase/blocking refreshed; msg to COO~H 20:09Z |

No design forks went to CRO~Z and no governance forks went to CVO~Z this tick. No ETFS_RIVALS call is open: round 8 drained to
CLOUD @1b2d733c6d, and Z-S20 is the issuer's own stop into cell RIV-lg-1.

## Scope state (register read, denominator 5)

| project | status | dep_stage | where it stands (since the relaunch) |
|---|---|---|---|
| AMGT_CORPUS | active | EXECUTING | r35 ak-4: map leg written @74e00624b0; NEVER-2 entry `amgt-corpus-r35-ak4` OPEN @b2cea29ed9 (COO~X, in flight) |
| AMGT_HARVST | active | EXECUTING | r44 CLOSED; r45 owed by COO~H |
| AMGT_RESAPP | active | EXECUTING | r67 aq-1/2/3 drained (fa22ce3149, aac5a586d1, e5ea575b16); aq-4 and aq-5 open with COO~Z |
| DSGN_AMGTV1 | active | EXECUTING | r34 closed; next round on the 7 reopened outcomes (COO~D); 055ba370 unpushed |
| ETFS_RIVALS | active | EXECUTING | round-8 prep on CLOUD; cut after the 2026-10-05 grades (COO~RV) |

**Completion test: NOT DONE.** 0 of 5 complete; all 5 REACHABLE.

**Stale documents named (not edited here):** `AMGT_RESAPP` `blocking` (round-46 text) and `ETFS_RIVALS` `blocking` (round-2 text)
trail their projects. Owners: COO~Z and COO~RV, at their next status write.

## Acts only Andrew can do (each cited)

1. His word on further data collection: HARVST's 9 collection outcomes, FWD-7 among them. The hold is "We will discuss internally
   on how to proceed with further data collection after review" (2026-10-03 ~17:3xZ).
2. The DSGN portal 055ba370 DEV push. MSTR pushes a product-file candidate on his word (CLAUDE.md Portal); his ~19:4xZ answer left it
   unanswered.
3. DSGN FWD-1 and ETFS_RIVALS FWD-1 signed-in reads (his login).
4. The rivalfunds OpenAI project key (his console).

## Compiler Tools

- `directives-check.py --json` (15 live; scope resolved), `sequence-check.py --project` x5 (all UNPLACED, rc 0),
  `active-commitments.py` (0 lines), `prd-signoff.py status NFRA_SPRINTWIN` (ADMITTED; current by ENDPOINT hash).
- Telemetry window scan (10 serials, 18:25-18:58Z), `git worktree list --porcelain` census (28 trees), and an open-deploy union
  across trees with `--full-history` close tracing.
- What worked: `--full-history --diff-filter=D` traced two branch-only AMGT entries to their CLOUD closes, where default history
  simplification had printed "none".
- What failed: one commit hit the peer's `index.lock` (rc=1); the retry landed. One commit was refused during a peer's drain
  merge; it waited, then landed.
