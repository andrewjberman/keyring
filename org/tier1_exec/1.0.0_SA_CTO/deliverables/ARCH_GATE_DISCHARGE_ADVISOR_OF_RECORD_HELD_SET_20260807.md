# DISCHARGE — the `arch-gate (live CTO)` condition on the advisor-of-record held set

**Author:** `1.0.0_SA_CTO` (base, the seat the condition names) · **2026-08-07**
**Authority:** Andrew-direct, base CTO terminal 2026-08-07 ~1645Z, answering `/open-calls`:

> **VERBATIM: *"All your recs are approved, proceed"*** — approving, on this item, the recommendation
> *"(b) [the arch-gate half accreted], with the never-widen half retained. I am the beneficiary of this
> answer, which is exactly why I will not rule on it myself."*

---

## THE RULING, in one line

**The `arch-gate (live CTO)` / `CTO~B clean-review` condition on the advisor-of-record daily fold is
DISCHARGED. The `NEVER#2` never-widen sign-off condition is RETAINED, untouched, and still binds.**

## What was held

17 files carrying 18 `DEPLOY-SERVE-HELD` sentinels — **one coherent workstream**, the advisor-of-record
daily fold:

| n | sentinel |
|---|---|
| 12 | `# DEPLOY-SERVE-HELD: advisor-of-record daily fold pending arch-gate (live CTO) + NEVER#2 sign-off` |
| 5 | `# DEPLOY-SERVE-HELD: advisor-of-record daily fold pending CTO~B clean-review + NEVER#2 sign-off` |
| 1 | `# DEPLOY-SERVE-HELD -- and READ WHY, because the reason CHANGED and the sentinel did not:` |

## Why this needed a sovereign answer rather than my own

**Twelve of them were held on my own seat and I did not know they existed.** I was reinstantiated with
fresh context on the morning of 2026-08-07; the sentinels landed 2026-07-12 (`223a71982b`) and
2026-08-05 (`1ae1ac882b`). The other five were held on `1.0.0_SA_CTO~B`, whose session Andrew closed.

That is the harm mechanism of his 2026-08-06 no-gates ruling, verbatim:

> *"an agent-manufactured approval step is INVISIBLE TO ANDREW — work he believes is moving sits held
> on an approver he does not know exists, and the hold surfaces only when he trips over it."*

**Neither approver could have discharged it: one had no knowledge of it, the other was not running.**
A hold in that state is not a decision anyone is making — it is a decision nobody can make.

**And I refused to rule on it myself for a specific reason: I am the beneficiary.** A seat adjudicating
whether its own approval requirement was ever authorized is the same defect the ruling names, run in the
opposite direction. So it went to Andrew as a call, with the recommendation stated.

## What is RETAINED — read this before assuming anything is free to move

⛔ **`NEVER#2` never-widen sign-off STILL BINDS on every one of these files.** It is **pre-existing
mechanical enforcement**, which Andrew's 2026-08-06 ruling explicitly preserves (*"pre-existing
MECHANICAL enforcement STANDS — the landed gate layer is not touched by this rule"*). Served output does
not move without it.

**So the practical effect of this discharge is narrower than "the files are released":**

| condition | state |
|---|---|
| arch-gate (live CTO) | **DISCHARGED** — accreted, never authorized by Andrew |
| CTO~B clean-review | **DISCHARGED** — same class, same ruling |
| NEVER#2 never-widen sign-off | **RETAINED — still required, unchanged** |

A file in this set becomes deployable when the never-widen sign-off is satisfied, **not** on the
strength of this document.

## How it was discovered — worth keeping, because nothing was pointed at it

`3.0.0_SA_CVO` flagged three of these files as STALE-and-undeployed while working an unrelated axis of
the INF investigation. I asked for the discrimination before routing it, and **the finding inverted**:
the files are held deliberately, and STALE is what a working hold looks like from outside. CVO retracted
their own finding inside the hour.

**The instrument property underneath it, which is the durable part:** `comp-pipescript deployed` has a
verdict space of MATCH / STALE / MISSING and **no concept of a hold**. A deliberately-held file that was
subsequently edited is byte-indistinguishable in its output from a file someone forgot to deploy. Both
print `STALE`. The tool is not wrong — its domain is (local hash vs S3 hash) and it answers that
correctly. It simply cannot carry the disposition, and the reader supplies the wrong one.

*No tool change is proposed. The sentinel is already in the file and greppable; the fix is a reading
discipline, not machinery. A tool that started modelling intent would need to be told about every
future kind of intent.*

**Only 3 of ~17 held files read STALE** — the difference between those and the ~14 reading MATCH is
solely whether anyone edited the file after the hold landed. So the tool's signal here is
*edit-since-hold*, not *neglect*, and nothing in the estate was pointed at the set as a set.

## ⚠ RESIDUE — one sentinel this discharge does NOT resolve

`data/inf/scripts/silver/convert_transactions_to_silver.py:94`:

> `# DEPLOY-SERVE-HELD -- and READ WHY, because the reason CHANGED and the sentinel did not:`

Someone had already noticed that a hold's **stated reason went stale while the sentinel stayed.** That is
a hold nobody can discharge, because nobody can any longer say what discharging it would mean — and it
sat inside a set that has now outlived both of its approvers. **This discharge does not touch it**: it is
not the arch-gate condition, it is an unknown condition. Surfaced, not adjudicated; it needs whoever
wrote it, or a fresh decision.

## Execution — what happens to the sentinel text

The files live in DS lanes (`data/inf/scripts/**`, `data/inf/manual_api/**`) — **not mine to edit.** The
discharge is this ruling, not a text edit at my seat. The owning lane strikes the discharged clause and
retains the `NEVER#2` clause on next touch. **Nobody is gated on doing so**, and a sentinel still
carrying the discharged clause is stale text, not a live hold — this document is the authority, and it
is cited by hash.

---

**Grounding:** sentinel census by `comp-find 'DEPLOY-SERVE-HELD' data/ --all` (19 hits / 957 files
scanned; 18 sentinels across 17 files, the 19th a reference to the mechanism) · sentinel provenance
`223a71982b` (2026-07-12, *"7 held files, second firebreak, switch OFF, inert"*) and `1ae1ac882b`
(`0.4.0_DS_ClientPlatform`, 2026-08-05T22:54:11Z, *"re-hold(INF): restore the DEPLOY-SERVE-HELD
sentinels… exactly as CTO/COO conditioned"*) · discrimination measured by `3.0.0_SA_CVO` (worktree
md5 == HEAD md5, clean porcelain, both commits ancestors of origin/CLOUD).
**Not established:** who authored the arch-gate condition originally, or whether it was ever
represented to Andrew. I did not trace it, and the ruling does not depend on it — the call was whether
it is authorized NOW, and it is not.
