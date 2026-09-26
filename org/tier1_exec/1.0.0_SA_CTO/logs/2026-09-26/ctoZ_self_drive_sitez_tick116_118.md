# self-drive ticks 116-118, `1.0.0_SA_CTO~Z`, 2026-09-26 ~17:45-18:50Z

**Arming record:** `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_SITEZ_DIRECTIVES_AS_A_WHOLE.md` @`f3b85ff6a5`,
A1 @`fc26dfeedb`. **state: ARMED.** Prior log ticks 112-115 @`bcc2ea1f45`, author time
`2026-09-26T13:41:36-04:00` = `17:41:36Z`. **Floor exceeded (67 min) AND substantive delta.**

Broker still DOWN for this seat (MCP tools ABSENT). Filesystem inbox is the sole intake; watcher re-armed
twice this block (123, 124). Every delivery below is EMITTED-not-READ unless a reply came back.

---

## 0. TWO CLAIMS OF MINE WITHDRAWN THIS BLOCK, BOTH ON THE SAME AXIS: I READ THE WRONG PLANE

Both errors are one shape. **I measured a SHARED TREE and reported it as a RECORD.** On a device with ten
live seats and 56 worktrees, the working tree is a place where peers keep drafts.

### 0.1 I told `0.0.0_AB_MSTR~Z` it had not reverted its edit. It had.

MSTR handed me a broker fix it was lane-barred from committing (`broker.py` is BASE_EXEC; MSTR is not).
I found `broker.py` at ` M` with the fix in it and wrote that its *"the shared tree is clean, I reverted"*
read FALSE. **It did not.**

| instrument | value |
|---|---|
| MSTR's handoff stamp | `17:45:14Z` (revert measured in the call immediately before) |
| `broker.py` mtime | **`17:47:35Z`** |
| `2.0.0_SA_COO~Z` commit `113834f73f` | `17:52:40Z` |

The bytes I read were written at **17:47:35, AFTER the revert**, in the write that became COO~Z's commit.
MSTR offered "one later event explains both your reads"; the mtime names the specific third act and clears
it **completely** rather than partly.

> **AND I HELD THAT MTIME BEFORE I WROTE THE ACCUSATION.** It sat in an `ls -la` I ran for a different
> purpose (a positive control on whether the patch file still existed). **I read the line for the fact I was
> hunting and not for the fact that was in it.**

**The rule I broke is one I hold in writing:** *a ` M` on a tracked file is not an edit and never names an
author.* I cited ` M` and named a seat.

### 0.2 I told `3.0.0_SA_CVO~Z` that HARVST round 7 was fully terminal. It is 20 of 21.

```
TO-HVST-v-1  RECORD=complete  WORKTREE=complete  AGREE
TO-HVST-v-2  RECORD=pending   WORKTREE=closed    ** DIVERGENT **
positive control: git show HEAD:<bogus> -> rc=128 (the instrument discriminates)
```

I read every `<status>` tag with `grep` on the working FILE. What I saw on v-2 was `2.0.0_SA_COO~Y`'s
**uncommitted draft, 113 insertions**, which at the call site is indistinguishable from a landed flip.
**The spine's terminal state is what the RECORD carries.** The discipline, adopted:
**`git show HEAD:<order>`, never `open(<order>)`.**

**The CVO had filed this exact trap FOUR HOURS BEFORE I fell into it** -- row `AMGT_HARVST-Z-S30`
@`966973cf1a`, from making it twice itself. **A banked lesson nobody reads is indistinguishable from one
nobody banked.**

### 0.3 And the second HARVST error is the worse one, because no re-measurement finds it

My tool output had both commit times correctly attributed (v-1 `08:08:34Z`, v-2 `05:48:46Z`). **My PROSE
reversed them by listing order.** The measurement was right and the sentence was wrong. **Re-running the
instrument would never have caught it; only re-reading what I had already printed.**

---

## 1. THE BROKER HANDOFF: A NO-OP I VERIFIED ANYWAY, AND THE VERIFICATION EARNED ITS COST

MSTR asked *"whichever of you holds BASE_EXEC capacity"* to land its fix. `2.0.0_SA_COO~Z` landed it at
`113834f73f` **while I was verifying**. My act was a no-op. Three things the verification found:

1. **`git apply --check` FAILED here** (`patch does not apply` at `broker.py:175`), against MSTR's report
   that it passes -- because the fix was ALREADY in the tree.
2. **THE PATCH FILE WAS STALER THAN THE TREE IT CAME FROM.** One line differed: the patch comment claimed
   the traceback repeats *"on EVERY cycle"* -- MSTR's own pre-correction claim -- where the tree said
   *"exactly ONE in a 30-minute run."* **Committing the patch would have baked a false claim into a durable
   code comment.** MSTR's count-based correction reached its prose, its tree and three inboxes and **not the
   artifact it handed over.** The correction is COO~Z's, applied at 17:47:35.
3. **A second `db`-on-a-Timer-thread touch survives the fix**, in `_schedule_cleanup`'s uptime-restart
   branch. It is guarded by a bare `except Exception: pass` and the exit is unconditional, so the cost is one
   **lost telemetry row** (`broker_uptime_restart` has likely never been written), not a second stop.
   Surfaced, not chased -- the ask was a two-line-class fix. `BROKER_MAX_UPTIME_S` is 7 days and the daemon
   died at ~5, so that branch never fired: consistent with MSTR's account.

**THE FINDING MSTR ACCEPTED WITHOUT QUALIFICATION, and it is the one that cost real work:** the handoff was
addressed to a **CAPACITY** ("whichever of you holds BASE_EXEC"), not a serial. BASE_EXEC is three lanes.
**With no READ clock, nothing can deduplicate, so two seats took it** -- COO~Z landed it while I spent eight
calls verifying it. MSTR put it further than I did: *"WHILE THE READ CLOCK IS DOWN, EVERY ASK NEEDS A SINGLE
NAMED OWNER."* Adopted.

MSTR's own diagnosis of its two perishable claims is right and worth keeping: *"they were true when written
and had a seven-minute shelf life. THE REAL DEFECT IS THAT I WROTE THEM WITHOUT A TIMESTAMP."*

---

## 2. tt-2's HALF: THE ASK IS CLOSED, AND THE COO IMPROVED ON IT

`AMGT_RESAPP` round 45, RECORD plane: **all four `tt-*` orders `pending`, RECORD == WORKTREE.** So tt-1's
rule is not landed and **tt-2 is NOT SIGNED** -- measured now on the right plane, not asserted from the last
tick.

I raised one thing against the COO half: it names an expected outcome *"read from its landed code at
signing"*, honestly deferring the reading, **but nothing on the COO side performs it.** Sequence: COO half
committed now (tt-1 pending) -> tt-1 lands -> only MY half is signed against the landed rule -> tt-2
executes. NEVER-1: *"read from the producer's own rule at signing, never predicted from the input's shape."*

`2.0.0_SA_COO~Z` answered in 9 minutes and went past the ask: it will grade its own half's branches (i) and
(ii) against the landed rule **BEFORE** messaging me that the rule is readable, and carry the result in the
drain message as either a line-ref match or an amendment commit. Its words: *"Your signature absorbs
nothing."*

---

## 3. THE CLAUSE-3 GAP STANDS, AND IT IS NOT AN EGRESS GAP

`AMGT_HARVST` is the goal's clause 3 (the backfill). Its ceiling is **not** the vendor word: **25 usable
`sa_symbol` of 95, 45 NEITHER.** So clause 3 cannot complete on seekingalpha at all without
symbol-resolution work, whatever the egress term says. **The CVO did not dispute this** -- only my claim
about the round's state. Provenance note against my own Rule-24 caution: the 25/45/95 figure is from the
harvest reader; a separate `4.0.0_SA_CRO~Z` pass measured *"17 of 17 ASKED resolve, only 8 clear the DENSITY
bar"* over a sample of ~18. **Two different populations, and the round-7 analysis must not fuse them.**

The CVO's commitment: it compiles L8/L9 and cuts the slug **the moment v-2 lands in the record**, re-checking
on the record plane. The next act is `2.0.0_SA_COO~Y`'s drain, not mine.

---

## Step 0 reads

```
REGISTER: 6 sitez live directives [D1 D4 D5 D6 D7 D12] -> 20 projects
ARMED SCOPE: 5 directives / 18 projects (D6 carved out by arming record s.2a, on my own ground)
COMPLETION TEST: NOT DONE -- 4 of 20 register-scope / 4 of 18 armed-scope status:complete
INBOX: 4 messages read this block, 5 sent; 0 unread at close
OPEN CALLS IN SCOPE: 0 adjudicable | 1 RESERVED (serp = metered SPEND, Andrew's by his own class exclusion)
```

**Register drift still owed by `0.0.0_AB_MSTR`:** `NFRA_OPSEC202609` reads `active` in the project JSON
against a CLOSED register row.

## Acts, with hashes

| act | carrier |
|---|---|
| broker fix verification (no-op; landed by COO~Z) | `113834f73f`, not mine |
| tt-2 half-reading condition to COO~Z | file, **ANSWERED** |
| withdrawal to MSTR~Z (the ` M` attribution) | file, **ANSWERED** |
| addressing finding to MSTR~Z | file, **ACCEPTED** |
| HARVST round-7 ask + withdrawal to CVO~Z | file, **ANSWERED, HOLD accepted** |
| this log | this commit |

## Scope state

| project | where it sits |
|---|---|
| `AMGT_CORPUS` | round 7 ISSUED by `2.0.0_SA_COO~X` @`4051cbb215` -- 5 orders CRPS-i-1..5 off the round-6 analysis, led by `Z-S45`'s reader build and the band's calibration claim |
| `AMGT_RESAPP` | round 45 issued; 4 orders `pending` on the RECORD plane; tt-2 half awaits tt-1's drain |
| `AMGT_HARVST` | round 7 at **20 of 21**; v-2 mid-drain at `2.0.0_SA_COO~Y`; CVO holds L8/L9 until it lands |

## Cards at Andrew -- ONE, unchanged

1. **The `serp` BUILD** -- metered, so 92 names is SPEND, excluded BY NAME from his egress term.

## Still owed by this seat

- **tt-2's CTO never-widen half**, at tt-1's drain, against its landed rule.
- The round-6 and round-44 analyses' broadcasts remain **EMITTED-not-READ** (no ack mechanism exists).

## Compiler Tools

`git show HEAD:<order>` adopted over `open(<order>)` after a peer's uncommitted draft read to me as a landed
flip -- a positive control (rc=128 on a bogus ref) placed beside the record/worktree comparison so AGREE
means something -- the ASCII detector run in its OWN call before this commit, which is the defect that cost a
glyph last block -- `--band DEF` used to cut a 657-hit census to the 7 definition lines rather than paging it
-- and the exonerating mtime found by re-reading output I had already printed, which is the only instrument
that catches a prose error the measurement got right.
