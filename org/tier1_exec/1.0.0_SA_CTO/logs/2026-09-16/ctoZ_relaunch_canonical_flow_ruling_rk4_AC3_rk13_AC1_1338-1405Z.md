# `1.0.0_SA_CTO~Z` -- relaunch after the 07:56Z reboot, `/canonical-flow AMGT_RESAPP`, and ONE ruling (13:38-14:05Z)

**archetype:** MIXED (VALIDATE + COORDINATE + SCRIBE)
**Seat:** `1.0.0_SA_CTO~Z`, site-Z fabric, branch SITEZ. **Project:** AMGT_RESAPP (D5).
**Authority:** Andrew-direct ~13:33Z at the `0.0.0_AB_MSTR~Z` terminal, record @`933a40dab2` (relayed as msg 23435):
*"bring the tier 1 ~Z fleet back online and in their launch explain to them that there was a reboot and they need to pick
up /canonical-flow AMGT_RESAPP"*. Standing arm re-armed off `org/XXX.md` Step 1b-F (this lane's row): `/self-drive
AMGT_RESAPP` 30 min at `17,47`, cron id (then) `884c0211`; the tick IS the goal loop.

## Startup (org/XXX.md A-F), measured

| step | result |
|---|---|
| `/watcher` | registered LIVE (PID 28216); Monitor `bnl0hzahi` `running`; no legacy watcher; 0 crons at launch |
| A.1 serial file | written for this session id |
| A.2 audit-archive | rc=1, 14 findings, baseline `sitez/2026-09-16T043514Z`; same count as the 04:40Z session; NOT chased per A.2 |
| A.3 PATH | 104 of 104 comp-tools resolve bare; forwarder RAN |
| B.0 delivery ledger | 1 of 1 row since 07:56Z (23435) opened and acked |
| B.1 `to-check --all --assignee` | no open order addressed to this lane; `sequence-check`: AMGT_RESAPP not sequenced, 0 flags |
| D / E | owned-paths hook wired; `.agent_context` SERIAL set |

## CANONICAL FLOW -- 1.0.0_SA_CTO~Z on AMGT_RESAPP (2026-09-16 13:4x-14:0xZ)

```
LOCATE   home: org/missions/D5/AMGT/AMGT_RESAPP   placement: site-z (project.json fabric)   status: active
         brief docs/briefs/amgt-resapp-security-analysis-20260910.md@19ce7d5b4d   endpoint: PRD ENDPOINT section
         PRD prd/AMGT_RESAPP_PRD.md v0.10 @49aedcf88b -- ADMITTED (ratified-text SIGNED 3.0.0_SA_CVO~Z; brief SIGNED 4.0.0_SA_CRO~W; both current)
         decomp decompositions/AMGT_RESAPP_DECOMP.md @d658d713be (01:43Z); issuance 6e4327f77f (02:10Z); not moved since the cut
         TOs 13 open / 3 terminal (rk-9, rk-10, rk-11 complete; rk-1..8, rk-12..16 pending)
         proof instances 3 VALID at HEAD for the 3 completes (receiving-check ACCEPT x3, coverage UNCHECKED by that tool);
                         3 further instances at HEAD for OPEN orders rk-1 (~23), rk-2 (~24), rk-3 (~26): criteria REFUSED with grounds, orders open
         worker branches 1 unmerged at 13:4xZ (wk-amgt_resapp-12-25 @0a5064ded5) -> DRAINED by 2.0.0_SA_COO~Z @a8be8b7452 at 13:55Z; 0 unmerged now
         unfinished edits: INVESTIGATION_v1.md carried CONFLICT MARKERS at 13:5xZ and MERGE_HEAD=0a5064ded5 -> the COO's LIVE drain,
                           markers 0 and MERGE_HEAD absent on the second read; porcelain under the project 0 after the drain
                           (the two files 0.0.0_AB_MSTR~Z's record names, seed-etf-constituents.py and nerves-risk-edges.json,
                           are under NO round-12 order's <paths> and are not this project's residue)
         live-production probe (next limb owner 2.0.0_SA_COO~Z): commit a8be8b7452 at 13:55Z, 13 min after relaunch -> MOVING
         rows 264 investigation items, 84 armed (channel-wide), 10 open items; 266 rows in the file at HEAD after the drain
         slug REMEDIATION_v11 @5d3a04cab6 (drained @d87181423c)   answer ROUND_ANALYSIS.round11 @c708914c50 (+ addenda 1db70c8e87, 06378dd3bd)
         round-12 slug ABSENT (correct: 13 orders open)
         dep_stage (claimed): EXECUTING
MEASURED limb: L7 -- highest conforming output: the round-12 issuance 6e4327f77f + three VALID instances at HEAD
         claimed vs measured: AGREE
CLASS    IN-PROGRESS: the COO drained the one orphan branch 13 min after relaunch and is landing ISSUER AMENDMENT 3 (msg 23439);
         ORPHAN-WORKTREE: CLEARED at a8be8b7452; UNFINISHED-EDITS: none under the project after the drain
ROLE     1.0.0_SA_CTO~Z owns L2-L4, the L10 read, the close, and (Step 1b-F) adjudication of open calls; next limb L7 is NOT MINE -> 2.0.0_SA_COO~Z
ACT      no L10 act owed (no round-12 slug); ONE adjudicable call received at 14:00Z (msg 23439) and RULED below;
         my five reassigned remedy rows (S102, W18-S19, W20-S9, W20-S11, W22-S7) are SETTLED in the ratified text and the
         round-11 analysis (C-ROUND12-THESIS-ASOF; C-ROUND12-COMPARABLE-COVERAGE; A3.1; A3.2; S108/S110) and wait on the CVO's L9 flip
```

## Correction to the relaunch record, measured at HEAD

`0.0.0_AB_MSTR~Z`'s record @`933a40dab2` s.3 says this lane's rulings 23427 and 23432 "stand unactioned by the seats they
name". **Measured false:** ISSUER AMENDMENT 1 @`6f433fc2a8` (06:58Z) touched **16** rk-* orders and ISSUER AMENDMENT 2
@`66ea4e4f7a` (07:49Z) touched **7**, both by `2.0.0_SA_COO~Z` before the reboot; `2.0.0_SA_COO~Z` reported the same in
23439 s.3 from its own read. Two seats, two instruments (`git show --name-only` here; the COO's own commit record there).
No act is owed on either ruling. The record's "no MERGE_HEAD" was also true when written and false by 13:5xZ, because the
COO had begun the drain -- a snapshot, not an error.

## THE RULING -- rk-4 AC3 and rk-13 AC1 (msg 23439 s.1), as adjudicator under Step 1b-F

**The call.** rk-4 AC3 expects `empty_subjects` "materially BELOW 23" and `populated` "materially ABOVE 10" over the 33
`peers/v1` objects; rk-13 AC1 carries the same "populated materially ABOVE 10". Measured by TWO instruments -- worker
`~25`'s row `AMGT_RESAPP-Z-W25-S2` and `2.0.0_SA_COO~Z`'s own read in 23439 -- **23 of 23 empties trace to a MISSING
`model_block_<key>.json`** for a non-US coverage name (4 blocks in the pool: BA, BABA, SAP, NVDA); **0 of 23** to an
identity join; 0 of 23 lack a `security_key`. The model-block pull is **CARD 1 at Andrew** (RESERVED: the budgeted
Bloomberg sign-in; CTO rec YES, standing).

**RULED: (a) -- re-cut both bars to the property each cell CAN move, with the CARD-1 half CARRIED, never dropped.**

*Why it is my call and not an issuer repair:* the repair test I set at 23434 is *same property, right object*. The
"populated" property has **TWO WRITERS** -- the identity join (cell C's) and the model-block landing (CARD 1's) -- and a
bar that reads their SUM cannot discriminate cell C's work from CARD 1's absence: it reads 23 on a perfect identity join
and 23 on a broken one. Re-cutting to "empties caused by identity" changes the PROPERTY the criterion asserts, which the
test reserves to this seat. It is Rule 5's *count the writers of the named property* applied at a criterion, and the
count is 2.

*Why not (b):* holding chain C on a reserved card turns a card into a stall on the round -- Rule 27's *no FWD is a wait*.
The card stays at Andrew, restated once in the round-12 L10 analysis, and nothing else waits on it.

**THREE CONDITIONS, binding on the re-cut (ISSUER AMENDMENT 3 or its successor):**

1. **The reason census must DISCRIMINATE.** `reason = no landed model block` is a MEASURED read of key absence under
   `s3://opal-data-harvest/derived/model_block/` (trailing slash; the sibling `model_block_fye/` excluded), never a label
   carried inside the peer object. The instance plants ONE mutant -- a subject WITH a landed block and an empty
   `members` list -- and the identity-defect count must read 1 on it and 0 on the live store. Printed denominators:
   `peer_objects`, `empty`, `empty_by_reason` (both branches), `blocks_in_pool`.
2. **rk-13 AC1 becomes an identity, both sides printed:** `populated == count(subjects with a landed block AND a
   resolved identity)`, plus `total_members` nonzero in the SAME grain as the pre-census (the W20-S1 clause stands), **plus
   the W25-S3 re-arm condition as its own clause**: the self-match residual is RE-MEASURED before the batch writes
   `peers/v1` objects for the newly resolved holdings (W25-S3's own `disarm_owner` text names rk-13; it is not optional).
3. **The CARD-1 partition is CARRIED as data, twice:** one line in the amendment commit's issuance data -- *population
   outcome for the N names with no landed block: HELD on CARD 1* -- and the same partition in the round-12 L8 packet, so
   L9 dispositions W25-S2 against it and the L10 analysis grades the peers/comparable outcomes REALIZED for the
   keyed-with-block population and HELD for the rest. The outcome set is not narrowed; its population is partitioned and
   the held half is named -- the goal's HELD-AT-STOP form applied to one outcome.

**Not ruled:** the dispositions of W25-S1/S2/S3/S4 (L9, `3.0.0_SA_CVO~Z`); no ratified text moves; no order's grammar
beyond the two bars named.

**RAVC on 23439 s.2 (the retraction):** ACCEPTED. Pinning the AC1 baseline by VersionId and fixing the `holdings`/`holding`
filter assert the same property against the right object; the AC2 repair carries its own discriminator (23 -> 0 on clean
code, 2 of 2 on a planted mutant). ⭐ The COO's dry run read the worker's own output as the pre-cell world -- a fresh
instance of the drain-ref inversion (`a-bar-anchored-on-a-drain-ref-inverts-once-the-ref-contains-the-branch`), at the
S3 object level: **pin the baseline by VersionId, never by "the object at the prefix"**.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-which` (A.3) | PASS | 104 of 104; forwarder RAN |
| `comp-surprise --project AMGT_RESAPP --json` | 3.1 MB | 264 items, 84 armed, 10 open; parsed in python, no pipe receiver |
| `receiving-check.py` x3 (rk-9/10/11 instances, `--governing-order`) | ACCEPT x3 | first call bound nothing -- my glob dropped the slug; re-run on the real paths |
| `prd-signoff.py status AMGT_RESAPP` | ADMITTED, both halves current | nothing owed at L4-R |
| `sequence-check.py --project AMGT_RESAPP` | not sequenced | 0 flags |
| `git branch --no-merged HEAD` / `git worktree list` / MERGE_HEAD + marker count, read TWICE | 1 -> 0 unmerged; markers present -> 0 | the change between reads is the live-drain discriminator |
| `audit-archive-invoker.py` | 14 findings | not chased (A.2) |

**Gap found:** none in the tools. The `comp-surprise` rail refused `| tail`; the JSON flag plus a python read is the
right shape and costs nothing.

## Owed next

`2.0.0_SA_COO~Z`: amendment 3 under the three conditions, then fresh slots for chains A-D. `3.0.0_SA_CVO~Z`: L8 on the
next completions. This seat: the `17,47` tick; the round-12 slug when it is cut. Cards at Andrew unchanged (CARD 1
model-block pull, CARD 2 filings batch; the SITEZ push and the merge leg are `0.0.0_AB_MSTR~Z`'s on his word).

Push state: **LOCAL on SITEZ**. LD-0522 puts the push with `0.0.0_AB_MSTR~Z`; none requested.
