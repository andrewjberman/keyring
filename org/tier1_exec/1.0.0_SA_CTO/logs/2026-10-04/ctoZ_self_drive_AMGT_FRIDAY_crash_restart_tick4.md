# /self-drive AMGT_FRIDAY -- tick 4 after the SentinelOne crash (1.0.0_SA_CTO~Z, 2026-10-04 ~21:2xZ -> ~22:2xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: ticks 2-3 @5019202c20.

## Andrew's word in the window

- `/open-calls` at this terminal ~21:3xZ: "No open sovereign calls at this lane."
- **The DSGN round-35 DEV push:** carded at this terminal ~21:4xZ. Andrew gave the word at the MSTR~Z terminal ("push 35a723bf to
  DEV", record @8f3b66b0ee). Portal DEV is now `35a723bf` with CI success (run 37237977735); PROD is untouched at `c69b4747`
  (msgs 29264, 29270).

## Calls closed, halves signed, analyses (since tick 3)

| item | ruling / act | commit |
|---|---|---|
| CVO~Z REMEDIATION_v1 (msg 29249) | CORPUS ARMED 39 -> 0, so the round-35 L10 precondition is now met by the instrument. Z-W4-S4 (`induction_request.py` writes on `--pick`) goes to the round-36 analysis. | -- |
| DSGN r35 review ask (msg 29252) | portal `d60a0f90` APPROVED for DEV under 4 conditions. Re-merged as `35a723bf` (msg 29261) and pushed on Andrew's word. PROD waits on RESAPP aq-5. | 98209ce86a |
| SPRINTWIN Addendum A (msg 29254) | CTO half EXTENDED to the 10-04 served re-run. Seam [10-03 22:15Z, 22:16Z) = 0 commits (control 40); A1-A4 cover both invoke-time branches. COO~H extended too (@7fa231405f). | cd417a0586, a647b1dcdf |
| CORPUS r36 al-5 (msg 29265) | CTO half SIGNED, 4 conditions. Base `aoQ+WrefJ` read live; content diff 1 file. It starts after aq-5's entry closes. | 95d297d418 |
| SPRINTWIN round-1 slug (msg 29272) | **Round 1 CLOSED, FWD-1 REALIZED** (386 = 336 + 2 + 48). **PRD v0.3:** the census is one object per run, never overwritten. Round-2 list sent to CRO~Z. | 94a34c849d |
| CORPUS al-2 portal `fb1f3cbb` (msg 29275) | **REWORK.** It is 155 commits behind DEV and the trial merge CONFLICTS in `ModelTab.tsx` with DSGN AV-zg-5/AV-zi-1. Merge DEV in and keep DSGN's order. COO~D is told ModelTab has a second writer. | 934205909b |
| RESAPP row Z-S346 (AE~A @ebf6eda0cb) | **No aq-5 rollback.** c24 reads 74 before and after; a rollback cures nothing and reverts c23/c25/c26. The forward-fix is aq-6, one read-only `chatter_window` prefix grant under a new pair, and the CTO half signs on receipt. | 14aa3c9200 |

No design forks went to CRO~Z and no governance forks went to CVO~Z.

## Scope state (register read 22:18Z, denominator 5)

| project | status | dep_stage | where it stands |
|---|---|---|---|
| AMGT_CORPUS | active | EXECUTING | r36: al-1, al-2 and al-3 drained; al-2 portal in REWORK; al-5 redeploy signed and waiting on aq-5 |
| AMGT_HARVST | active | EXECUTING | r45: ar-1 drained @38fc65b7bf; collection runs follow FWD-12 DONE (Andrew's word) |
| AMGT_RESAPP | active | EXECUTING | r67 aq-5: code LANDED; c24 waits on aq-6 (Z-S346) |
| DSGN_AMGTV1 | active | EXECUTING | r35 on DEV `35a723bf`; round 36 next |
| ETFS_RIVALS | active | EXECUTING | r8 workstream A issued; workstream B in prep (@7cc969288b) |

Open TOs, directive-wide: D5 127, D13 2. Sequence: 5 UNPLACED. Active commitments: 0.

**Completion test: NOT DONE.** 0 of 5 complete; all 5 REACHABLE.

## Acts only Andrew can do (each cited)

1. The DEV push of the next portal product-file candidates (CLAUDE.md Portal): CORPUS al-2 after its rework, and DSGN round 36.
2. The DSGN and ETFS_RIVALS FWD-1 signed-in reads (his login).
3. The rivalfunds OpenAI project key: deferred by his word.

## Compiler Tools

- `directives-check.py --json`, `sequence-check.py --project` x5, `active-commitments.py`, `prd-signoff.py status`,
  `aws lambda get-function-configuration`, `git merge-tree --write-tree` (the trial merge that exposed the ModelTab conflict
  without touching any tree), `lib.opal_naming.address()` (the per-run census key).
- What failed: a heredoc-embedded Python regex broke on the harness's backslash unescaping. It was redone as a script file in the
  scratchpad.
