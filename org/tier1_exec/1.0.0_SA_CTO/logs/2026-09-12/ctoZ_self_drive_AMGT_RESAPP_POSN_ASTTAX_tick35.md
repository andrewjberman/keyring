# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 35

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-12T23:45Z**
(`date -u`.) Tick 34's log is `@1a66969c0a`. **Three substantive deltas, and the largest is a
RETRACTION of a claim this seat printed in four consecutive logs.**

---

## 1. AMGT_RESAPP ROUND 7 CLOSED AT L7 DURING THIS TICK -- 43 OF 43 TERMINAL

`rf-4` closed against amendment 1 (`8ec7756a49`, drained `a8659e8baa`) and `rf-5` closed
(`bb80780c83`, drained `1effa7ac68`). `2.0.0_SA_COO~ZZZ` handed the L8 packet
(`ledger/ROUND7_PACKET.md @6a50ce1832`) to `3.0.0_SA_CVO~Z` the same tick and cut nothing next,
citing LD-0521 by name. **The next limb is L9; the slug after it is what this seat answers.**

Re-measured here independently rather than taken on report -- `_open_tos_for_project` at HEAD
`d359728e66`: **AMGT_RESAPP 0 of 43**, POSN_ASTTAX 4 of 15, `ZZZZ_NOSUCH` 0 of 0. Same numbers, a
different instrument from the COO's, so corroboration and not a re-run.

⛔ **AND NOT FROM `to-check`, WHICH STILL PRINTS "6 ACTIVE" AT THIS SAME HEAD.** Its count has now
held at 6 while the true value went 4 -> 2 -> 1 -> 0. A seat sizing round 7 off that tool reads a
round that never progressed.

**The two constraints that bind the round-7 analysis are unchanged and still recorded:** no
round-7 artifact may claim the portal half is delivered on SITEZ (carrier `Z-S34`); and the
criterion-defect class is stated ONCE at class grain, not as six repairs.

## 2. THE RETRACTION -- FOUR TICKS OF "D4 open_tos" WAS THIS SEAT'S OWN WRONG DOMAIN

`AMGT_RESAPP-Z-S42` **`@0e8b5e941d`**. `directives-check.py:83 open_tos()` does not count orders.
Its docstring, VERBATIM: *"project -> open-TO count, parsed from to-check.py --all (its
denominator, not ours)."* It shells out to `to-check --all`, regex-parses each `Project: <CODE>
(<n> ACTIVE)` line, and `:183` sums it over **the directive's MEMBERS**. So the register reprints
to-check's number one consumer layer up.

| | domain | to-check | gate | verdict |
|---|---|---|---|---|
| **D4** | SIX members | 0+2+0+0+0+4 = **6** | 0+2+0+0+0+4 = **6** | **CORRECT, and always was** |
| **D5** | ONE member (AMGT_RESAPP) | **6** | **0** | **WRONG, and never flagged** |

⛔ **TICKS 31-34 PRINTED "D4 open_tos=6 vs measured 4, UNDETERMINED". THE "MEASURED 4" WAS
`POSN_ASTTAX` ALONE -- a six-member sum compared against one project.** That is Rule 24's own
postulate failing on the seat that has cited it all session: *choosing the domain is itself a
claim, falsified before the comparison runs.* One read of `:183` closes it on tick 31.

⭐ **THE PART WORTH CARRYING: the wrong domain did not merely produce a false positive -- IT
CONSUMED THE ATTENTION THAT WOULD HAVE FOUND THE TRUE ONE, sitting in the same printed table, for
four ticks.** And it survived precisely BECAUSE it was carried honestly as UNDETERMINED rather than
acted on. A carried uncertainty is not a safe place to park a comparison; it is an unexamined claim
with a label on it.

Blast radius is still REPORTING and enforcement was re-measured clean -- but the reporting surface
is one layer wider than `Z-S36` states: it reaches the artifact seats read to resolve scope.
`directives-check.py` has no defect of its own; it faithfully reprints what it is given.

## 3. Z-S16 DISARMED ON A LIVE REMOTE READ; Z-S21 STAYS ARMED AND IS NOW MEASURED

`AMGT_RESAPP-Z-S43` **`@5a54fa6560`**. Z-S16's own FIRST arm fired without any act by any seat:
*"either the IRPT chain lands on DEV (making the base ordinary)."* It landed.

```
git ls-remote --heads origin  (portal/)   refs/heads/DEV = 5b959f63ca   <- the exact commit the row
                                          called "DEV plus nineteen un-merged commits"
git rev-list --count origin/DEV..5b959f63 = 0     is-ancestor -> YES
POSITIVE CONTROL, same breath, object known NOT on DEV:
git rev-list --count origin/DEV..e6057f26 = 2     is-ancestor -> NO    <- instrument discriminates
```
A LIST READ -- not a fetch, not a push, not a promote. **NOT claimed: that the row was wrong when
filed.** DEV may have advanced between its 09-11 19:55Z filing and this read, and a remote branch's
push time is not recoverable from a clone. The innocent reading is taken.

**`Z-S21` STAYS ARMED, and the freeze's cost is now a number.** The round-6 Lead Panel `e6057f26`
EXISTS, contained by exactly TWO LOCAL branches (`wk-amgt_resapp-5-8-portal`,
`wk-amgt_resapp-7-2-portal`) and by **ZERO remote refs** -- against the control that the recorded
gitlink `e85f6eb84f` IS contained by `remotes/origin/DEV`. Two anchors, so one `git branch -D` no
longer makes it unreachable; but **the round-6 deliverable exists ON THIS DEVICE ONLY.** Its
remaining arms are a promote (frozen) or a conscious carry accepting device-local durability for a
round deliverable. **This seat is not taking the second silently.** It is an instance behind the
portal card already CARRIED at Andrew with a YES rec, and it is NOT re-carded.

## 4. TWO THINGS DELIBERATELY NOT DONE

**The spaced-key asymmetry was reached here independently and NOT filed.** This seat censused it at
CRITERION grain -- 1 of 23 criteria across 6 of 6 orders carry the space form, and it is `rf-4` AC1
-- agreeing with `2.0.0_SA_COO~ZZZ`'s 1-of-6 order-grain sweep. That seat filed it first at `Z-S41`
and amended `rf-4` at `f5461c6884`. Re-filing is repetition; it is recorded here as an agreeing
second instrument and nothing more.

⚠ **AND A WRITE OF THIS SEAT'S TO THE SHARED CHANNEL WAS SILENTLY REVERTED, WHICH IS WORTH THE
PARAGRAPH.** An append of `Z-S42` landed while `2.0.0_SA_COO~ZZZ`'s drain was replacing the same
file; the verify-after-write threw a `JSONDecodeError` because it read the peer MID-WRITE. Full
three-plane check afterward -- HEAD, index and worktree all at 90 rows, identical id sets, no
duplicates, **no peer row lost** -- and nothing of this seat's had survived. **The write succeeded
and left no trace, and the only reason it was noticed is that the failing verify happened to fire.
On an append-only shared file under a live drain the oracle is `git show HEAD:<path>` AFTER the
commit, never the worktree after the write.** Both rows above were re-verified that way, each with
a `Z-S99` negative control.

## 5. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 3 RESERVED · NO PITCH (unchanged; CVO-confirmed at tick 31 and
                     nothing has changed their citations. Re-pitching is repetition, and Andrew's
                     02:22Z priority ruling names that traffic.)
  CARRIED   portal DEV push (now with the device-local measurement behind it) · LIMB 6 widening ·
            Bright Data proxy
  NOT-MINE  POSN round-3 four-of-fifteen · the half-hash mechanical-change carve-out (both MSTR's)
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 projects, 2 of 14 live directives)
  AMGT_RESAPP  active/EXECUTING  REACHABLE  0 OPEN of 43 -- round 7 TERMINAL, at L9 with the CVO
  POSN_ASTTAX  active/EXECUTING  REACHABLE  4 OPEN of 15 [S2-1,S3-1,T6-1,T7-1]; round 4 not cut
  UNREACHABLE: 0     HELD-AT-STOP: not reached
  (counts from _open_tos_for_project with its negative control -- NOT from to-check, per Z-S36/Z-S42)
```
The D4 line that ran in ticks 31-34 is **struck, not carried**: see section 2.

**One input sent, no adjudication asked for:** msg 22017/22018 to `3.0.0_SA_CVO~Z` (L9 owner) with
`2.0.0_SA_COO~ZZZ` copied -- this seat's four ARMED rows disposed or refused each on a measurement,
plus the property that `hazard_standing` is IMMUTABLE AT SURFACING so a field census reads 35 ARMED
of 92 and OVERSTATES the live set by roughly 40%. **The screen offered with it names its own
demonstrated false positive** (it flags `Z-S21` because `Z-S43` mentions that id beside the word
DISARM, while `Z-S43` says in terms that `Z-S21` stays ARMED) -- one known false positive in 15,
found only because this seat knew that row's answer, so it is offered as a candidate list to read
rather than a count to trust.

**Push state:** this seat's `0e8b5e941d` and `5a54fa6560` are LOCAL -- neither is an ancestor of
`origin/SITEZ 0c59581cd8` (ls-remote). Local HEAD `d359728e66`, 9 ahead, 0 behind; the tip moved
four times during this tick. `HEAD:portal e85f6eb84f`, unmoved. No TO cut, no dispatch, no apply,
no merge, no promote.

## Compiler Tools

`_open_tos_for_project` loaded directly from `surprise-row-gate.py` with a `ZZZZ_NOSUCH` negative
control · `directives-check.py --json` for MEMBERSHIP only (never its `open_tos`, per Z-S42) ·
`to-check.py --all` run ONLY as the subject of the Z-S36 disarm test, never as a state read · a
python `<criterion>` parser over the six round-7 order files for the key census · `git ls-remote
--heads origin` in `portal/` plus `rev-list --count` / `merge-base --is-ancestor` with a firing
positive control · `git show HEAD:<path>` as the post-commit oracle · `git log --all --author` for
the worker plane · `date -u` · `safe-commit.sh -F` with the message file written by a non-shell
writer.
