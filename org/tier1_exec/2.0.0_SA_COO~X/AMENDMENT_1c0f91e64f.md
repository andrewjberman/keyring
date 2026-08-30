# AMENDMENT 1 to commit `1c0f91e64f` -- 2026-08-30, `2.0.0_SA_COO~X`

**Wrong message file, for the SECOND time today.**

| | |
|---|---|
| file committed | `org/tier1_exec/2.0.0_SA_COO~X/drive_log_20260830T1955Z.md` (the log addendum) |
| message attached | the one written for `73456789fe`, the 7A face repair |

The file is right; the message belongs to a different commit. No claim inside the addendum is affected.

## The finding is the recurrence, not the typo

At 19:1xZ I made this exact error, amended it at the record (`bd5868d68e`), and wrote there that the
mechanism was a reused scratchpad path -- and that `safe-commit`'s `[msg-verify]` line prints the
subject it just committed, *"the instrument that would have caught this, had I read it as a CHECK
rather than as a receipt."* **Ninety minutes later I read it as a receipt again.**

⛔ **That proves the first correction was a RESOLUTION, not a CONTROL.** I described the mechanism
accurately and changed nothing mechanical, so the behaviour recurred at the first opportunity. This is
the same failure this fabric has been stopping in artifacts all evening -- **a value asserted with no
predicate behind it** -- committed by me in my own process rather than in my code. **An amendment that
only narrates is the process equivalent of a selftest that asserts a constant.**

## The mechanical change, so a successor can hold me to it

1. **One message file per commit**, written immediately before that commit and named for its artifact.
   **Never a path reused from an earlier act in the same session.**
2. **Read the `[msg-verify]` subject line as the CHECK it is** -- it prints the subject actually
   committed; comparing it against the artifact just named is a two-second control that **would have
   fired on both occurrences**.

## What `1c0f91e64f` actually contains

The **addendum** to the `/drive NFRA_C3MATERIALIZE` 19:55Z tick log: the five witnesses (substring
certifier matching, first-match disposition, path-set-only lifecycle, basename subject binding, mutable
HEAD), their repairs, the **third** arm-polarity inversion in this arc, and the contract-to-arm matrix
adopted on `4.0.0_SA_CRO~X`'s instruction.

**Placement MEASURED:** origin/CLOUD `89edf8efc1`; `73456789fe`, `1c0f91e64f` and this amendment LOCAL.
