# AMENDMENT 1 to commit `0f95e82c20` -- 2026-08-30, `2.0.0_SA_COO~X`

**That commit carries the D11 19:18Z drive log under the commit message of a DIFFERENT tick.**

| | |
|---|---|
| file committed | `org/tier1_exec/2.0.0_SA_COO~X/drive_log_20260830T1918Z.md` (the `/drive D11` paired tick) |
| message attached | the one written for `87b3410813`, the `/drive NFRA_C3MATERIALIZE` **18:59Z** tick |

**The file is right; the message is about a different tick.** No claim inside the 19:18Z log is affected.

## Mechanism

I passed a stale scratchpad message-file path to `safe-commit`. The wrapper did exactly what it is
documented to do -- it commits the files you NAME with the message you NAME, and returns `rc=0` either
way. Its own `[msg-verify]` line printed the subject it had just committed: **the instrument that would
have caught this, had I read it as a CHECK rather than as a receipt.**

⛔ **The shape is the one corrected all session, one surface over: a LABEL THAT DOES NOT MATCH THE OBJECT
IT NAMES.** Today: a denominator calling a pending task order a certified record; a numerator saying
"certified" over an unchecked predicate; a stale sha256 in a commit message; now a commit message naming
the wrong tick. The instance changes, the class does not -- **produce the artifact correctly, then
attach a label not re-derived from it.** The generalisation applies to my own commits, not only to my
cutters.

## Why an amendment and not a rewrite

CLOUD is a shared branch and the standing rule prefers a new commit over amending an existing one. The
wrong message stays in the record; this corrects it rather than erasing it. A reader arriving at
`0f95e82c20` by any path -- log listing, cursor-by-author, bisect -- should read that file as the
**D11 19:18Z paired tick**.

## What the 19:18Z log records

Tick-top (clause LIVE, register predicate re-resolved to `NFRA_SUBSTRATECARDING` + `NFRA_C3MATERIALIZE`);
the empty-and-legal ledger limb (21 rows, 20 with `unblocks`, **0 unconsumed**); the three certification
STOPs and the four-component repair; concurrence with reading **(a)** of Andrew's naming law; and the
carding lane regaining a living owner.

**Placement MEASURED:** origin/CLOUD `89edf8efc1`; `0f95e82c20`, `3b2e4cf294` and this amendment LOCAL.
