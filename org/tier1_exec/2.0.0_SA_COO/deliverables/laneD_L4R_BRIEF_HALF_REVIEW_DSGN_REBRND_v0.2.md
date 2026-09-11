# L4-R BRIEF-HALF RE-REVIEW — DSGN_REBRND PRD v0.2 @8ad762f7bf (half hash 5c71da53ce)

**Reviewer:** `2.0.0_SA_COO~D`, designated brief-half signer (Andrew-direct @`2daf4d8b85`).
**Supersedes:** `laneD_L4R_BRIEF_HALF_REVIEW_DSGN_REBRND_v0.1.md`@`b5a959bb82` (REFUSED, stamped
@`45fc3f539b`).
**Scope:** the WHOLE half re-read, not the refused line. The half's bytes moved everywhere —
`3.0.0_SA_COO~D`'s refusal plus `3.0.0_SA_CVO`'s whole-PRD review @`638c8085b6` both landed — so
the v0.1 verifications were re-run against the new bytes rather than carried forward.

## VERDICT: SIGN

---

## 1 — The refusal is CURED, in both places it needed to land

The SURFACE MANIFEST preamble now reads, verbatim in the document workers will read:

> *"The portal is a submodule on `DEV`, but **no cell of this project writes to `DEV` or to
> `CLOUD`**. Andrew-direct 2026-09-11 at the `2.0.0_SA_COO~D` terminal, verbatim: 'keep it all on a
> feature branch so if it goes to hell we haven't fucked our entire shit up.' All work lands on
> `feature/d13-visual-elevation` in BOTH repos … `2.0.0_SA_COO~D` drains them onto that branch and
> nowhere else … Promotion of the feature branch into `DEV` is a separate act on Andrew's word and
> is NOT commissioned by this PRD."*

Three things make this a cure rather than an acknowledgement:

1. **The preamble now names FOUR binding rulings**, the feature branch being the fourth, so it sits
   at the same level as light-canvas / charts-keep-colour / nothing-vendored rather than in a
   footnote. A cell author reading only the preamble is bound.
2. **"and nowhere else"** closes the drain target. The v0.1 text was silent, not wrong, and silence
   is what would have routed 13 cells to `DEV`.
3. **Promotion is explicitly NOT commissioned.** That was not in the suggested wording; it is the
   CTO's addition and it is the better half of the fix — it stops a worker from reading "get it
   onto DEV eventually" into the scope.

Both worktrees are named by path and both exist. `PROVENANCE AND AMENDMENT HISTORY` carries the
ruling with its channel and this lane's review by pin.

## 2 — The routed question is answered inside the PRD

R7 now reads *"the RD draft on `feature/d13-visual-elevation` at portal `10236236` is INPUT, never
authority."* That is correct on both halves: the location is right, and the authority statement is
the one that matters — an RD draft written before L4 cannot bind a ratified contract.

## 3 — N1: the count correction is right, and the error is MINE

`3.0.0_SA_CVO` found that Appendix A's accounting was wrong. Verified independently by parsing the
brief's own table rather than reading either document's prose:

| | |
|---|---|
| Appendix A rows | 23 |
| rows whose outcome column is `-` | **2** — A15, A22 |
| rows bearing an outcome | **21** |
| the brief's SUMMARY SENTENCE claims | "20 bear on an outcome; 3 are cleanup" |

**The brief's prose contradicts the brief's own table, and the table is the authority.** A21 is the
row in dispute: its outcome column reads `O11` and the summary silently counted it as cleanup. The
v0.1 PRD had hedged this ("A15 and A22 *and A21's cosmetic half*"); v0.2 resolves it to 21/2 and
states the contradiction in the open. Both are improvements and the second is correct.

**DECISION — the brief is NOT amended now, deliberately.** The PRD pins `brief_ref` at
`bed01b226a`; the quoted prose is accurate AT THAT PIN, so the citation is sound. Editing the brief
during its own sign-off would move a pinned L1 input mid-L4-R for a prose fix the PRD has already
adjudicated correctly — and the brief moving after L2 is exactly what forced the FWD-10/FWD-11
append. **Recorded as an open defect in this lane's own artifact**, to be corrected the next time
the brief is legitimately re-pinned, not before. If `1.0.0_SA_CTO` would rather re-point
`brief_ref`, this lane will make the edit on request.

## 4 — The CVO's other four changes, checked against the brief

| change | checked | finding |
|---|---|---|
| **C2** R5/R6 accent budget by ROLE — one PERSISTENT primary action; the transient focus ring and text selection share the accent and are not counted | against brief O4, III.3, IV.2 (accent ≤1.0 %) | **Resolves a real contradiction I had left.** O4 says one accent per view; O5 demands a visible accent focus ring. Both cannot hold under a naive count. Role-splitting persistent vs transient is the right cut, and R5 now walks the counterexample (primary visible + secondary focused + text selected) on all three routes. |
| **C3** R10 density graded on spacing and a designed end state, with a sparse-populated negative control, never a fold quota | against brief O9, Part II | **Better than my own outcome.** O9 as I wrote it invites a fold quota, which would push a cell toward adding panels — and information architecture is explicitly out of scope in Part II. The negative control (one short row, panels intact) is what makes the criterion falsifiable without widening scope. |
| **C5** R3 grades the DEFAULT LIGHT MODE and exercises light → dark → light | against brief III.7, V.3 | Correct. III.7 says dark mode is a choice, not residue; grading only the light default would have left the retained toggle unexercised. |
| **C6** NEW cell **R14** — affected-surface inventory, denominator = route count, one read render per touched route/state, keyboard walk per touched interactive surface | against brief VII.2 | **This is the strongest addition in v0.2 and it repairs a gap I declared and did not close.** VII.2 admits three of twenty-six routes were rendered. R14 converts that admission into a denominator-bearing obligation, and it retains `UI_VERIFICATION.md`'s render-LOOK-then-commit rule by name rather than inventing a second mechanism (brief IV.7). Named in PATHS, FIXTURES and SURFACE MANIFEST — verified in all three. |

## 5 — v0.1 verifications RE-RUN at the new bytes (not carried forward)

| # | Claim | Instrument | Result |
|---|---|---|---|
| W1 | coverage denominator 32 | heading count re-derived from the brief | **32.** Match. |
| W2 | 23 of 23 defects mapped | set-difference **both directions** | 0 missing, 0 extra. |
| W3 | every cell reachable from the coverage map | cell-id extraction vs the BRIEF COVERAGE section | 14 cells (R1–R14), **0 orphans**. |
| W4 | FWD ids intact | id extraction | FWD-1…FWD-11, contiguous, none reused. |
| W5 | R14's artifact named where it must be | per-section containment test | present in PATHS, FIXTURES **and** SURFACE MANIFEST. |

V3–V8 of the v0.1 review (Lato's OFL text, the nine `index.css` lines at portal `787015e8` with a
negative control, `ADHC_DESIGN` closed, the absent D13 directive doc, `modelPortfolioColors.ts`,
the fixtures directory) were verified against artifacts **outside** this PRD, which have not moved;
they stand unchanged and are not re-asserted here as though re-measured.

## 6 — The four L5 obligations

`1.0.0_SA_CTO` records them as read and agreed, with no PRD change needed. **Concurred** — they are
cut-time obligations, not document defects, and they remain this lane's:

1. Compound acceptance clauses split one-per-criterion at the cut (Rule 27 refuses a compound
   criterion at the cut, and the cut is this lane's). v0.2 made R3, R5, R6 and R10 **longer**, so
   this obligation grew rather than shrank — noted deliberately.
2. R12's walked person and R7's "author's agreement" re-cut into an on-demand act plus a JUDGMENT
   criterion graded at L9, never self-graded.
3. FWD-9's grade half stays Andrew's; the pack-exists half is cut as the on-demand act.
4. No cell assumes the competitor capture; it is egress needing his per-use word.

## 7 — What this signature does NOT cover

ENDPOINT and CONTRACTS are the ratified-text half and are `3.0.0_SA_CVO`'s. This lane read CONTRACTS
while checking PATHS and raises nothing, **but that is not a sign-off on it.** At the time of this
stamp the ratified-text half reads STALE and is owed by that seat; `to-pipeline-gate.py` LIMB 6
holds L6 until both halves read SIGNED, which is correct and this lane does not ask for relief
from it.
