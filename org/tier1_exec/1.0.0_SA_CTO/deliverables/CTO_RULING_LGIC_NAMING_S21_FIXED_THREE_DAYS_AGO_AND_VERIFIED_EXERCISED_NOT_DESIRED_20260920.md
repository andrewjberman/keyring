# CTO RULING -- `LGIC_NAMING-S21`: the defect was **real**, was fixed **three days ago by a worker**, and is now verified **EXERCISED** rather than merely present

**Seat:** `1.0.0_SA_CTO`, the row's `disarm_owner` and the gate's named owner. **Date:** 2026-09-20 · laptop · CLOUD
**Row:** `LGIC_NAMING-S21` (ARMED). **Subject:** `.tools/proof-of-spec-check.py`, the `surprises` limb.

---

## 1. THE ROW'S CLAIM, AND IT WAS CORRECT

> *"`proof-of-spec-check` resolves a cited surprise row by globbing the MAIN checkout (`_channel_row_ids` uses
> `WORKSPACE`), not the checkout being graded. An instance whose row is committed on a SIDE BRANCH reads INVALID
> with 'the row must be committed before the instance cites it', although the row is committed and present in
> the graded tree."*

**A FALSE `INVALID` on a worker's own proof** -- the worst direction for this limb, because the worker did
everything right and the instrument said otherwise.

## 2. IT IS FIXED, AND NOT BY THIS SEAT

`git log -S'_instance_checkout_root'`: landed **@`b918930306`, 2026-09-17T09:31:51-04:00**, by
**`0.9.0_WK_LGIC_ENFORCE~3`** under `EN-i-3-r3`. The mechanism, read at HEAD:

- `_instance_checkout_root(inst_path)` (`:1132-1160`) walks **up from the instance's own path to the nearest
  `.git` entry** -- *"a dir for a normal clone, a file for a linked worktree -- `.exists()` covers both"* --
  and falls back to `WORKSPACE` when `inst_path` is None or no `.git` is found.
- `surprises_check` (`:1231`): `row_ids, files_scanned = _channel_row_ids(code, _instance_checkout_root(inst_path))`.
- ⭐ **The walk-up is the RIGHT design and a prefix test would have been WRONG here:** this box currently
  carries **16 worktrees, five of them NESTED INSIDE the main checkout** under `.worktrees/`. A path under the
  main checkout can therefore belong to a *different* checkout, so "is this path mine?" is not answerable by
  prefix. The walk-to-nearest-`.git` answers it correctly by construction.

## 3. ⛔ THE SELF-TEST ALONE WOULD NOT HAVE BEEN ENOUGH, AND SAYING SO IS THE POINT

`python .tools/proof-of-spec-check.py --self-test` -> **`RESULT: 45 of 45 arm(s) behaved`** at HEAD. The
script even documents an uninjected arm (`:2010`) *"left uninjected so `_instance_checkout_root` +
`_channel_row_ids` actually run."*

⚠ **But that arm runs in the SAME checkout as the script.** It exercises the WIRING and the **FALLBACK**; it
can never exercise the **FIX**, because the fix only differs from the old behaviour when the instance lives
somewhere else. **A 45-of-45 pass is consistent with the defect still being live.**

**So I ran the real function, three arms, on real checkouts:**

| arm | input | returned | reads |
|---|---|---|---|
| 1 | `None` | `…\ajb_workspace` | fallback, as documented |
| 2 | a path in the MAIN checkout | `…\ajb_workspace` | correct, and **indistinguishable from the old behaviour** |
| 3 | **a path in a LINKED worktree** (`C:\tmp\verify-m1`, `.git` present) | **`C:\tmp\verify-m1`** | **the graded checkout, NOT `WORKSPACE` -- DISCRIMINATES** |

⭐ **Arms 1 and 2 would both have passed BEFORE the fix. Only arm 3 separates fixed from broken** -- *two arms
show a fix works; only three show the guard is load-bearing.* **STATE: EXERCISED, not DESIRED.**

## 4. ⭐ THE FINDING THAT IS NOT ABOUT THIS GATE

**The row sat ARMED for three days after its own defect was repaired.** The fix landed 09-17; the row is
disarmed 09-20. Nothing was blocked and nothing was wrong -- **the remedy simply arrived before anyone asked
whether it had.**

> ⛔ **A ROW CAN BE SATISFIED BY WORK THAT LANDED BEFORE ANYONE WENT LOOKING, AND NOTHING IN THE ROW MOVES WHEN
> THAT HAPPENS.** Its `hazard_standing` is written by the filer and changed only by a later act, so an armed
> row is evidence about **when someone last looked**, never about the world. **COST: one read of the named
> file before assuming a row describes HEAD.** **NON-APPLICATION:** a row whose remedy is owned by the seat
> reading it, where "has anyone done this" and "have I done this" coincide.

That is the same shape as tonight's counting sequence one level over: **an armed-row census measures the
channel's attention, not the estate's state** -- which is why `3.0.0_SA_CVO`'s six and every figure I published
are upper bounds and nothing more (`S140`).

## 5. DISPOSITION

- **`LGIC_NAMING-S21`'s condition is MET at HEAD, verified on the live function with a discriminating arm.
  This seat -- its `disarm_owner` -- DISARMS it.** ⚠ The clock move is `3.0.0_SA_CVO`'s under R-19.
- **NOT CLAIMED:** that every `surprises`-limb defect is closed; only this one. The `files_scanned`
  denominator, the ANNOUNCE/ENFORCE split and the `SURPRISE_ID_RE` shape are untouched and ungraded here.
- **NOT DONE:** no edit to `proof-of-spec-check.py`; the fix is a worker's and it stands as landed. `S22`'s
  stop-on-first-raise finding is a different instrument and is not moved by this.

## 6. INSTRUMENTS

`git log -S'_instance_checkout_root'` for provenance; **bytes PRINTED at `:1132-1160` and `:1212-1231`**, not
grepped; `--self-test` run at HEAD (45/45, and its insufficiency stated rather than cited as proof);
`git worktree list --porcelain` (16 worktrees, 5 nested); **the real `_instance_checkout_root` invoked three
times through a module load of the script itself**, with the third arm on a genuine linked worktree whose
`.git` entry was confirmed present.
