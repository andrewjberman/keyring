# /self-drive AMGT_RESAPP -- tick 27 (covers ticks 26-27), `1.0.0_SA_CTO~Z`

**state: ARMED** · cadence 30m · device **sitez** · arming record
`ANDREW_DIRECT_20260923_193xZ_SELF_DRIVE_AMGT_ALL_THREE_CLOSER_LOOPS.md` @`a8a62f4f5c`
(that commit's subject misdescribes it; the file is correct -- annotated in `RULINGS.md`, not edited).

## SCOPE + SEQUENCE

`AMGT_RESAPP` -> directive D5 / macro AMGT. `sequence-check` @`55903c6259`, enforcement **TRACK**:
`AMGT_RESAPP` and `AMGT_CORPUS` both **UNPLACED** -- register projects the sequence does not list, so
their directive's rules govern and no `WAITING`/`HELD` cap applies. No `DRIFT`, no `OUT-OF-SEQUENCE`.
Device guard: scope is site Z, driver is site Z. PASS.

## COMPLETION TEST -- NOT DONE, 0 of 2 projects complete

| project | status | dep_stage | orders (denominator) |
|---|---|---|---|
| `AMGT_RESAPP` | `active` | EXECUTING | **201** = 186 complete + 8 superseded + 6 pending + 1 withdrawn |
| `AMGT_CORPUS` | `active` | EXECUTING | **17** = 15 complete + 2 pending |

Read from `org/projects/<CODE>.json`, never declared. Pending on RESAPP fell 10 -> 6 this tick as
`2.0.0_SA_COO~Z`'s round-37 wave-1 drains landed (rl-2 `973dc1cf5d`, rl-3 `a8aa8bff17`, rl-4 in flight).

⛔ **AND THE ORDER-COUNT INSTRUMENT WAS BROKEN THIS TICK BEFORE IT WAS FIXED.** A regex
`<status>\s*([^<\n]+)` matched the FIRST `<status>` in each file, which in most task orders sits inside
CRITERION PROSE describing how to flip it ("flip `<status>` to `complete`"). It returned **19 distinct
values**, most of them backtick fragments. The anchored form `^<status>...</status>$` returns 4.
⭐ **THE SUM CHECK WOULD NOT HAVE CAUGHT IT: the broken parse ALSO summed to 201**, because every file
contributed exactly one garbage value. **The discriminator is the SIZE OF THE VALUE SET against the
enum the field allows** -- 19 observed where ~5 are legal means free text was matched. Same discipline
R-39 (2) rules into the grade table: one controlled token, or the count is unreadable.

## OPEN CALLS IN SCOPE -- 0 adjudicable, 1 RESERVED, no pitch sent

**⚠ THE ALL-RESERVED TELL FIRED (1 of 1) AND THE CITATION TEST WAS RE-RUN,** per the skill's own
instruction. It survives: the citation is a NEVER-class law line naming the decision class, not a
"carried to Andrew once" hook. With n=1 the tell carries little weight and is recorded rather than acted on.

```
+-- CALL 1 of 1 -- RESERVED ------------------------------------------+
  **Does `rk-49` (Lusha) proceed?**
  An AMGT_RESAPP order held on a vendor word. It is one of the FOUR named
  exceptions in the close condition, and the only one Andrew alone can clear.
  ----------------------------------------------------------------------
  **REC --** no rec is offered; the class is his. The order moves on no
  measurement this seat can take.
  **CITATION --** CLAUDE.md, Agent Autonomy: *"NEVER call an external vendor
  API without Andrew's explicit per-use word -- availability is not
  authorization."* Decision class named: vendor egress.
+----------------------------------------------------------------------+
```
No pitch to `3.0.0_SA_CVO~Z` this tick: the reservation was already surfaced once and re-pitching a
standing citation every 30 minutes is noise, not adjudication.

## ACTS TAKEN THIS TICK -- the driver's own lane only

| act | hash | note |
|---|---|---|
| **R-39** -- the close condition's `N of 49` is not machine-readable | `54b277a086` | three failed measurements recorded with their instruments |
| **R-39a** -- WITHDRAWS R-39's attempt 3 | `5c19c11ed8` | the CORPUS L10 analysis exists; a glob wrong on TWO axes |
| **R-40** -- WITHDRAWS precondition (2) as verified | `5c19c11ed8` | shares that commit, whose subject names only R-39a |
| **R-40 delivery annotation** | `f0cd3b7417` | the broadcast named the wrong seat for an open merge |
| **`GRADE_TABLE_49.md`** -- 49 rows, both carriers named | `f31e029fbe` | makes `N of 49` measurable; extraction-only, cannot go stale |

Broadcasts: msgs 25356-25359 (ruling batch), 25362-25365 (attribution correction), 25366-25369
(grade table). **12 of 12 DELIVERED, 0 queued, 0 refused.** Inbox: 12 messages READ-acked
(25303, 25309, 25325, 25329, 25335, 25340, 25341, 25343, 25344, 25352, 25355, 25360). Watcher re-armed
on `[WATCHER-EXPIRED]` in the same turn it fired (task `b8jjyowej`).

## THE FINDING OF THE TICK -- eight instruments, one family

Counting the order-status parser above, **eight measurements this tick were a real instrument aimed
ONE LEVEL OFF THE CLAIM**, each returning a confident result with a real printed denominator:

1. a per-FILE co-occurrence join read as a per-ROW claim;
2. `NOT REALIZED` (spaced) matched as `REALIZED` -- **the grade INVERTED**, and in the flattering direction;
3. a glob wrong on DOMAIN and NAME simultaneously, so fixing either alone still returned zero;
4. precondition (2) graded on a STRING CENSUS when the claim was about a CALL PATH;
5. `MERGE_HEAD` read as naming the merging actor when it names the merged-FROM branch;
6. the hypothesis that the latest analysis per project carries current state (round 36 names ONE id of 30);
7. the order-status parser matching criterion prose;
8. and the sum-to-denominator check that would have certified (7) as clean.

⛔ **FOUR OF THE EIGHT WERE CAUGHT BY A PEER'S CITATION, NOT BY ANY CONTROL THIS SEAT RAN**
(`2.0.0_SA_COO~X` twice, `0.0.0_AB_MSTR~Z` and `2.0.0_SA_COO~Z` once each). ⭐ **AND A RULING ABOUT
MEASUREMENT ERROR IS NOT PROTECTED FROM MEASUREMENT ERROR BY ITS SUBJECT** -- R-39a is a defect inside
R-39, committed four minutes after it.

## WHAT IS GATED, NAMED RATHER THAN LEFT PENDING (Rule 29)

| owed | owner | gate |
|---|---|---|
| L10 analysis, round 37 | this seat | wave-1 drains, 3 of 7 landed |
| `AMGT_CORPUS` round-2 analysis | this seat | round 2 EXECUTING, 2 orders pending |
| preconditions (3) + (4) | `2.0.0_SA_COO~Z` | accepted into one closer cell; build starts post-drain |
| F2, F3, the 37 heading renames | this seat | PARKED per R-33/R-34, ride the first post-drain edit |
| CVO read of THE FIFTEEN amendments | `3.0.0_SA_CVO~Z` | routed; does not wait on a drain |
| 6 calls at Andrew | Andrew | sovereign; `rk-49`/Lusha is the only close-condition exception |

**Induction re-fire preconditions: FOUR. (1) MET. (2) re-graded NOT MET. (3) and (4) OPEN.**
Nothing unblocked remains in this seat's lane this tick.

## Compiler Tools

`sequence-check.py` · `agentbus-sqs.sh device` · `safe-commit.sh` · python (anchored status census,
word-boundary token census, unscoped 42,116-file carrier census) · `check_inbox` / `ack_messages` /
`send_message` / `heartbeat` · Monitor (watcher re-arm).

**Push state: LOCAL on all five commits** (`ls-remote` UNREAD this tick). `0.0.0_AB_MSTR~Z` pushes on
its cadence and will not push while a drain is open.
