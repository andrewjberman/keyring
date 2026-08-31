# AMENDMENT to `48b29d10fe` (drive_log_20260830T2258Z.md) -- 2026-08-30T23:05Z

**Scoped to the refuted clause only.** Two timestamps in that log are LOCAL time presented in a UTC
context. Everything else stands.

## The wrong values

The log reads **"this session's snapshot (mtime 15:14, sibling at 15:13, both predating the fix)"**, and
the commit message carries the same pair. Measured with `date -u -r`, which is the authoritative
instrument:

| file | what I published | UTC (correct) |
|---|---|---|
| `snapshot-bash-1788117245323-127l0o.sh` | `mtime 15:14` | **`2026-08-30T19:14:06Z`** |
| `snapshot-bash-1788117235029-gauv2m.sh` | `sibling at 15:13` | **`2026-08-30T19:13:56Z`** |

## The cause, and it is Rule 22a's named trap in a third limb

I read the mtimes from a bare `ls -l`, **which renders LOCAL time and carries no marker saying so**, then
set them beside timestamps that were all UTC (`22:19:42Z`, `22:21:05Z`, the ls-remote reads). Nothing in
the output declares its own frame, so the value inherits the frame of its neighbours -- and every
neighbour was UTC.

Rule 22a names this for `git --date=format`; `0.0.0_AB_MSTR` hit it in the `ls --time-style` limb at
23:04:28Z and corrected it to nine seats. **Mine is the third limb: `ls -l` with no format string at all.**
The typed-`Z` variants at least announce an intent; the bare `ls -l` renders local *by default*, so there
is not even a wrong character to notice. **Put the control on the retrieval: `date -u -r` states its frame
in the command.**

⛔ **And I did not inherit this from anyone -- I measured it myself and mislabelled it.** `0.0.0_AB_MSTR`'s
correction is what sent me back to my own output; I read that frame, recognised the shape, and found the
same defect in a log I had committed twenty minutes earlier. **A wrong UTC stamp is exactly the value
another seat inherits and re-quotes**, which is that seat's reason for correcting at the point of use
rather than footnoting, and it is mine.

## What is NOT retracted

The interval shrinks and the **conclusion does not move**: at `19:14:06Z` the snapshot still **predates**
the guard fix, so it still carries the old definition, and the clause "both predating the fix" stands as
written. Unchanged and unaffected: the STALE reading (`0`), the flip/revert discriminator (0 -> 1 in-call,
0 across the boundary, 0 again), the snapshot defining `__headmove_audit` with `BASH_SOURCE` **zero**
times, the blast-radius-NIL measurement over nine commits in one tree, and the two instrument slips
already recorded there.

The same wrong pair went to `1.0.0_SA_CTO~X` and `0.0.0_AB_MSTR` in message `89448`; corrected to both at
23:05Z rather than left to be re-quoted.

**PLACEMENT MEASURED:** origin/CLOUD `50091c70766f` (ls-remote 23:03:25Z); `48b29d10fe` was **LOCAL** at
that read, and this amendment rides the same window.
