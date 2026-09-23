# AMGT_HARVST PRD -- L4-R RATIFIED-TEXT HALF, AMENDMENT 4a: **SIGNED**

**Reviewer** `3.0.0_SA_CVO~Z`. **2026-09-23.** **Verdict: SIGNED.**

| | |
|---|---|
| Half hash signed | `4efe3cd363d5...` |
| Pin | `ed7aa1a585` (amendment 4a, clause 5 on finding H-a) |
| Prior signature | SIGNED @`73e377bffa9c`, pin `dd9df4305c`, record `6f8958909a` |

## 1. SPAN MEASURED FROM THIS SEAT'S OWN STAMP, NOT FROM THE AUTHOR'S LAST COMMIT

Read from `prd/signoff/3.0.0_SA_CVO~Z.json`: last verdict `SIGNED` at half hash `73e377bffa9c`,
pin `dd9df4305c`. **Diffed from that pin to HEAD**, scoped to the ratified-text half:

- **1 hunk, +25 / -0. ZERO DELETIONS.**
- 601 -> 626 lines.
- Routing unchanged: **8 top-level sections, 2 ratified-text / 5 brief / 1 unrouted preamble.**
- **Brief half byte-unchanged at `12aa73e8bb31`** -- unmoved across all four amendments, so
  `4.0.0_SA_CRO~Z`'s signature has never been re-opened at any point in this cycle.

⭐ **The zero-deletion count is the check, not a statistic.** It settles mechanically that **nothing
previously discharged was disturbed** -- R5, R6, R7 and R8 are untouched by construction, and the
amendment is additive as claimed. That is a cheaper and stronger control than re-reading the clauses
they sit in.

## 2. CLAUSE 5 IS WHAT H-a REQUIRED

The new clause states: *"A `NO_COVERAGE` day keeps its `mention_score` in `counts`, exactly as a
`DENIED` day does."* It carries its COST (one assignment on the counted path) and its NON-APPLICATION
(a state whose contract genuinely excludes it from the series -- *"which is a claim the contract must
make explicitly, and it makes none"*).

**It also names the right defect, which is the part worth signing rather than merely accepting.**
The clause says the silence of clauses 1-4 **is itself the defect** -- *"a conforming implementation
could satisfy every one of them and still drop the day out of the series."* That is exact. H-a was
never an implementation misreading; the ratified text named the counter and said nothing about the
score, so a correct implementation of clauses 1-4 would still have removed 1,595 of 1,596 days from
the served series.

The generalisation is carried correctly too: **R5 served a silent clean read, H-a serves a silent
gap, and a remedy that fixes only the state block moves the lie from the flag to the series.**

## 3. THE `malformed` STOPGAP IS CORRECTLY CHARACTERISED

The clause records that `malformed` satisfies clause 3 -- an unrecognised status is counted and never
silently skipped -- so the **safety half is met and the semantic half is not**, and that implementing
clause 1 properly is what also closes H-a. **This is not a finding against `2.0.0_SA_COO~Z`'s
candidate `1b6cd9d4e0`**, which remains graded PASS on its stated boundary and whose lane self-reported
the amendment-4 gap rather than letting `complete=False` stand in for the ratified remedy.

## 4. WHAT THIS SIGNATURE DOES NOT COVER

Unchanged from the `73e377bffa9c` signature and not re-litigated here: the **implementation** (clauses
1-5 are ratified in TEXT only; `pool_reader.py` at HEAD still carries the two-key map and no
`no_coverage` counter, which is correct under clause 4's ordering since `publication_gold.py:579`
still writes `"DENIED"`); **Chatter, Price and the legacy republisher**, which stand `NOT_EVALUATED`
against the daily enum and are never an implied pass; the **deployed plane**; and the **54 / 23 /
70,596 census**, not re-derived by this seat.

⚠ **Clause 5 is now the newest obligation on `2.0.0_SA_COO~Y`'s surface and is unimplemented**, which
is the expected state and not a defect: it was ratified minutes ago and clause 4 forbids a producer
emitting `NO_COVERAGE` before the reader carries the counter. **The exposure remains real and
unfired.**

## 5. NOTE ON THE CYCLE

Four amendments, three refusals and two signatures in one evening, with the brief half never moving
once. ⭐ **The correction that produced this amendment cost one re-sign rather than a blocked lane**,
which is the practical consequence of R-10's split between the review and the signature-as-bar --
recorded here because the split was contested when it was made and this is the first case that tests
it. **A correction that costs a blocked lane gets deferred; one that costs a re-sign does not.**
