# /self-drive AMGT_RESAPP & POSN_ASTTAX -- tick 40

**seat:** `1.0.0_SA_CTO~Z` · **state:** ARMED · **device:** sitez · **2026-09-13T02:10:34Z**
Tick 39's log is `@6d8dec3f83` (amendment `@67034521da`). **The obligation `Z-S57` named is done as
a READING; its recording is HELD on a peer's uncommitted append to the shared channel.**

---

## 1. THE SEVEN THAT WERE NEVER IN THE SET -- READ

`Z-S57` recorded that this seat's reader admitted only `[` blocks, so AMGT_RESAPP's count was 17
when it is 24, and `Z-S52`'s "the twelve are read" ran over a short denominator. The seven missing
ids are now read.

**All seven live in `ADJUDICATION_v5.md` -- the one file the old reader choked on -- and every one
is the CVO's GRADUATED TWIN of a row this seat had already dispositioned.** That is the reassuring
shape rather than seven unknown obligations, and it is stated as a measurement, not a relief.

| twin | of | standing after reading it in full |
|---|---|---|
| `Z-C-S39` | `Z-S16` | **DISCHARGED on its base half** -- `Z-S43` measured `refs/heads/DEV` IS `5b959f63` on the live remote, so the promotion-base coupling is gone. Its *"later authorized integration"* half is the same freeze item as `Z-S21`/`Z-C-S47` and is NOT double-counted. |
| `Z-C-S42` | `Z-S19` | **DISCHARGED.** Its own text: the preservation risk was *"loss of the sole object store"*, `S21` records the successful fetch, and *"resolve the separate integration hold"* points elsewhere. |
| `Z-C-S51` | `Z-S22` | **DISCHARGED tonight** `@2981c4bd72`. Its residual is quoted verbatim -- *"the new skill prose and 21672 repeat that killing the process destroys 189 KB ... Correct that causal claim while retaining the output-plane probe"* -- and both halves were honoured. |
| `Z-C-S24` | `Z-S6` | **LIVE.** `evaluate()` still falls back to `prd_version` when `half_hash` is absent. Andrew's ~21:1xZ approval covers `--expect-half-hash` ONLY and does not reach it. |
| `Z-C-S47` | `Z-S21` | **LIVE**, portal-freeze-sequenced. Same object, same hold. |
| `Z-C-S37` | `Z-S14` | **LIVE** -- fixture-vs-deliverable identity. |
| `Z-C-S46` | `Z-W2-S10` | **LIVE** -- a handoff must carry path + commit + resource identifier. |

⚠ **STATED RATHER THAN GLOSSED:** `Z-C-S39`, `-S42`, `-S51`, `-S24` and `-S47` were read in FULL.
`Z-C-S37` and `Z-C-S46` were read at their `one_line`, which matches their originals' exactly, and
their standing is INHERITED from originals whose full text was read at `Z-S52`. That is a weaker
read and it is labelled as one.

**AMGT_RESAPP standing after this tick: 24 distinct ids -- 7 discharged tonight (`Z-S16`, `Z-S36`,
`Z-S42`, plus `Z-C-S78`, `Z-C-S90`, `Z-C-S39`, `Z-C-S42`, `Z-C-S51`), the rest live or inert per
`Z-S52`.**

## 2. THE RECORDING IS HELD, AND WHY

`2.0.0_SA_COO~ZZZ` has `AMGT_RESAPP-Z-S58` appended to the channel and **UNCOMMITTED** -- 29 lines,
complete, parsing at 116 rows. Appending mine on top would either race it or be swept into that
seat's commit under its author line, which is worse than losing it.
⛔ **This is the same class that reverted this seat's `Z-S42` write earlier tonight**, and the
remedy learned there is applied here: hold, do not write into a file a peer is mid-append on. The
row lands next tick.

## 3. OPEN CALLS / COMPLETION

```
OPEN CALLS IN SCOPE: 0 adjudicable · 3 RESERVED · NO PITCH (unchanged; CVO-confirmed at tick 31)
  CARRIED   portal DEV push · LIMB 6 widening · Bright Data proxy
  NOT-MINE  POSN round-3 four-of-fifteen · the half-hash mechanical-change carve-out (both MSTR's)
COMPLETION TEST: NOT DONE -- 0 of 2 complete (denominator: 2 projects, 2 of 14 live directives)
  AMGT_RESAPP  active/EXECUTING  REACHABLE  1 OPEN of 46 -- round 8, rg-2 remaining
  POSN_ASTTAX  active/EXECUTING  REACHABLE  4 OPEN of 15 -- round 4 not cut; L10 held on Andrew
  UNREACHABLE: 0     HELD-AT-STOP: not reached
```
`rg-1` (the consumer join) drained at `55c71e45d5` and `rg-2` was amended at `3981fe738c` with AC2
and AC4 routed to L9 as judgments. Round 8 is one order from its own L10.

**STILL OWED:** the held `Z-C-S39/S42/S51` disarm row, and POSN_ASTTAX's twenty-six read to a
standing each (`Z-S38` did the triage: 8 inert, 9 with no candidate disarm, 8 needing a paired read).

**Push state:** everything this seat has committed is PUBLISHED -- `origin/SITEZ` was `19bfdd3fc3 ==
local` at 02:05Z with `a3178cdb71` and `19bfdd3fc3` both ancestors and negative control `83cc87f29d`
firing. `HEAD:portal e85f6eb84f`, unmoved. No TO cut, no dispatch, no apply, no merge, no promote.

## Compiler Tools

The channel reader with all six columns -- files, blocks PRESENT/ADMITTED/SKIPPED, rows,
unparseable, read time -- admitting BOTH `[` and `{` blocks after `2.0.0_SA_COO~Z` located the
admission defect · a set difference against the ids named in `Z-S43`/`Z-S50`/`Z-S51`/`Z-S52` to
isolate the seven · a full read of five of the seven and a labelled `one_line`-only read of two ·
`_open_tos_for_project` with `ZZZZ_NOSUCH` · `git status --porcelain` + `git diff` on the channel
path to identify the peer's uncommitted append by id and author before deciding to hold ·
`safe-commit.sh -F`.
