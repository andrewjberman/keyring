# L4-R BRIEF-HALF REVIEW — DSGN_REBRND PRD v0.1 @9769e40c6f

**Reviewer:** `2.0.0_SA_COO~D`, designated brief-half signer on the project row
(Andrew-direct 2026-09-11 ~08:0xZ, relayed by `1.0.0_SA_CTO` msg 95914, ACKed).
**Half under review:** CELL CANDIDATES · PATHS · FIXTURES AND EVIDENCE · BRIEF COVERAGE ·
L2 FINDINGS CARRIED · SURFACE MANIFEST.
**Reviewed against:** `docs/briefs/portal-visual-elevation-brief-20260911.md` @`bed01b226a`,
which this same lane authored as `0.1.1_RD_MarketPerformance`.

## VERDICT: REFUSE

One omission, in the SURFACE MANIFEST, and it is not a defect of care — it is a sovereign ruling
the CTO could not have known, given to this lane directly after the PRD was written. Everything
else in the half verified sound, and the verification is below so the correction is a one-line
edit rather than a re-review.

---

## THE REFUSAL

**Section:** SURFACE MANIFEST, its preamble sentence — *"The portal is a submodule on `DEV`:
workers commit in their own portal worktrees inside their workspace worktrees, `2.0.0_SA_COO~D`
drains them, any active DEV-push freeze is respected, and a shared branch is pushed only by
`0.0.0_AB_MSTR` on Andrew's word (brief V.5)."*

**What is missing:** the whole project is confined to a FEATURE BRANCH. Andrew-direct 2026-09-11
at this lane's terminal, VERBATIM:

> *"you are going to reregister as 2.0.0_SA_COO~D. Congratulations you just got promoted. You are
> going to be the driver of this project. The only thing I ask is that you keep it all on a feature
> branch so if it goes to hell we haven't fucked our entire shit up, understand?"*

**Why this is a refusal and not a carried note.** The preamble already binds every cell with three
rulings (light canvas; the charts keep their colour; nothing third-party vendored). **This is a
fourth ruling of exactly that class** — it governs the write path of all 13 cells. As the half
reads today, a worker follows it to `DEV`, which is the branch Andrew ruled this work must stay
off. A reviewer's private record does not travel; **the PRD is what the workers read.** Correcting
the document is cheap; correcting 13 cells' drain target afterwards is not.

**Suggested correction** (CTO's wording to choose; this lane will sign the corrected bytes):

> The portal is a submodule on `DEV`, but **no cell of this project writes to `DEV` or to `CLOUD`.**
> Andrew-direct 2026-09-11: *"keep it all on a feature branch so if it goes to hell we haven't
> fucked our entire shit up."* All work lands on `feature/d13-visual-elevation` in BOTH repos.
> Workers commit in their own portal worktrees inside their workspace worktrees, branched from
> `feature/d13-visual-elevation`; `2.0.0_SA_COO~D` drains them onto that branch and nowhere else.
> Any active DEV-push freeze is respected, and a shared branch is pushed only by `0.0.0_AB_MSTR`
> on Andrew's word (brief V.5). Promotion of the feature branch into `DEV` is a separate act on
> Andrew's word and is NOT commissioned by this PRD.

**Already built and reachable, so the correction describes something real, not a plan:**

| | |
|---|---|
| workspace worktree | `.worktrees/d13-visual-elevation` on `feature/d13-visual-elevation` |
| portal worktree | `.worktrees/d13-visual-elevation/portal`, same branch, `node_modules` junctioned and verified (react resolves) |
| portal `DEV` | restored to `787015e8` for `2.0.0_SA_COO~F`'s live IRPT_FNTEND round; nothing of this project remains in that tree or its index |

---

## ANSWERING THE ONE FACT THE CTO ROUTED TO THIS LANE

The message asked where `portal/DESIGN.md` lives, since it is absent from the workspace's portal
checkout at `787015e8`.

**It is on `feature/d13-visual-elevation` in the portal repo at commit `10236236`**, reachable at
`.worktrees/d13-visual-elevation/portal/DESIGN.md`. It is absent from `787015e8` **deliberately**:
it was authored on portal `DEV`, stacked on `2.0.0_SA_COO~F`'s IRPT_FNTEND drain, and this lane
moved it off by branch-pointer so their live round was not disturbed — their working tree and index
were left byte-identical to how they were found.

**R7's treatment of it is exactly right and needs no change:** input where the lane can reach it,
**authority nowhere.** It is an RD draft; only the L4-ratified contract carries authority.

---

## WHAT VERIFIED SOUND — instruments named, not read for plausibility

| # | Claim under review | Instrument | Result |
|---|---|---|---|
| V1 | BRIEF COVERAGE denominator is 32 sections | independent heading count of the brief at `bed01b226a` (`^## ` + `^### `) | **10 + 22 = 32.** Exact. Derived, not copied from the PRD. |
| V2 | 23 of 23 Appendix A defects mapped, 0 unmapped | set-difference of the brief's `A\d+` rows against the PRD's defect map, **both directions** | **0 missing, 0 extra.** |
| V3 | Lato's licence closes brief V.1 | read `docs/research/investor_reporting_export_20260910/FONT_LICENSE.txt` | Real. *"Reserved Font Name \"Lato\""*, *"SIL Open Font License, Version 1.1"*. **V.1 is genuinely closed** — this lane wrote V.1 as an open gap and it is now shut by a file already in the estate. |
| V4 | The 9 cited `index.css` lines exist at portal `787015e8` | `git show 787015e8:src/index.css` + `sed -n` per line, **plus a negative control at line 999** | All 9 byte-match their claim; control blank. GRAIN sound. |
| V5 | `ADHC_DESIGN` does not collide (L2 finding 2) | read `org/projects/ADHC_DESIGN.json` | `status: complete`, CLOSED 2026-04-21. Correct. **This closes brief VII.1**, which this lane declared as its own largest gap. |
| V6 | `docs/architecture/D13_DESIGN_PRD.md` absent (L2 finding 4) | file test | Absent. Finding correct, and correctly routed to `0.0.0_AB_MSTR` rather than absorbed. |
| V7 | `portal/src/lib/modelPortfolioColors.ts` reused, not replaced (R8) | file test | Present. |
| V8 | Fixtures exist for R10/R11 | `portal/.frontend-dev/testing/` listing | Populated. |

**On FWD renumbering:** FWD-10 ← O9 (density), FWD-11 ← O10 (empty states), FWD-9 re-sourced O9 → O11.
Checked against this lane's own renumber of the brief, where the original O9 (Andrew's side-by-side)
became O11. **Coherent — FWD ids were appended and never reused**, which is the rule.

---

## OBLIGATIONS THIS LANE ACCEPTS AT L5 (not refusal grounds — recorded so they are not lost)

1. **Compound acceptance clauses.** R1 (5 conjuncts), R3 (7), R7 (6), R9 (3+) are conjoined.
   Rule 27 refuses a compound criterion **at the cut**, and the cut is this lane's. The PRD labels
   them `acceptance clause draft` and hands the split to L5 explicitly. They will be split, one
   clause per criterion, each with its invocation and expectation.
2. **Two acceptance clauses need a HUMAN and no worker can produce one.** R12 — *"one person who
   has never seen the portal is walked from opalinvest.com into a portal route"*; R7 — *"one page
   is rejected by clause number **with the author's agreement** on record"*. At L5 each is re-cut
   into an on-demand act a seat can take (the render pair; the clause-cited rejection) plus a
   JUDGMENT criterion graded at L9 and never self-graded.
3. **FWD-9 is the one genuine wait.** R13 grades on Andrew's word. The pack-exists half is
   on-demand and will be cut that way; the grade half is his and is expressly qualified in the PRD
   (*"the grade is HIS"*). Its qualification sits in the ENDPOINT section — **the CVO's half** — so
   this lane flags it across the boundary rather than ruling on it.
4. **R13's competitor capture is egress** and needs Andrew's per-use word. The PRD says so; no cell
   will be issued that assumes it.

## WHAT THIS REVIEW DOES NOT COVER

ENDPOINT and CONTRACTS are the ratified-text half and belong to `3.0.0_SA_CVO`. This lane read
CONTRACTS while reviewing PATHS and raises nothing against it, but **that is not a sign-off on it**
and must not be read as one.
