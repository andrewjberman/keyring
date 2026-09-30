# AMGT_CORPUS -- ROUND 19 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~02:5xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 26858, subject *"L10 slug AMGT_CORPUS round 19 @15d57857ad"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v22.md`.

**Round 19 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **`u-2`:** the CLI uses the producer's header path. The CVO's replay reads **214 of 214** (it was 209). `Z-W2-S14` GRADUATED.
- **`u-1`:** the unit/sign readers honour a per-security non-MEASURED status, including the pre-exception shape (the issuer's
  call, AGREED).
  - Hitachi BEST_SALES reads UNRESOLVED/UNRESOLVED; the control 8035 reads MILLIONS/POSITIVE.
  - The served block agrees with the fixed reader (FY1 11962163.4, UNRESOLVED on both). So round-18 ruling 1's branch holds:
    the served block stands, and no re-derive is owed.
  - `Z-W2-S13` GRADUATED.
- **`u-3` (the `r-1` re-sign) is held on AMGT_RESAPP r51 cell 1**, which is issued first in that round (the RESAPP round-50
  analysis @debbec1907).

## 2. RULINGS

1. **The 3.9 floor (`_ensure_unit_map`'s `Path.write_text(..., newline="\n")`, a keyword added in 3.10): CELL 1.**
   - Use `open(path, "w", encoding="utf-8", newline="\n")`.
   - The code states a 3.9 floor, and ruff's py39 target cannot see a stdlib keyword added later. So the AC runs the function
     under a 3.9 interpreter if one is installed. Otherwise it runs an AST check that no `write_text`/`read_text` call in
     `lib/research/corpus/` passes `newline=`, with the file count printed.
2. **The six render outcomes (FWD-10, 11, 12, 15, 16, 18): CELL 2, the re-grade round-14 ruling 7 promised "once that lands".**
   - It has landed: `/thesis` at `pVa+sgzj` passes pillars, management, fund/position and terms. The CVO read ML_FP at 5 of 5
     pillar leads.
   - Each outcome's DONE WHEN is an analyst READING the page (PRD `:318`-`:490`). So the cell grades both halves:
     - a served census over the 96 names, per outcome, with its denominator;
     - a walk on 5174 at the current portal DEV of the named validation pages, one per outcome.
   - The CTO grades from both at the next analysis. A served half met with the page unrendered is NOT REALIZED, and the page
     ask then goes to DSGN_AMGTV1.
3. **`u-3`: CELL 3, dependent, unchanged.**

## 3. FWD GRADES

- 13 of 19 REALIZED, unchanged.
- The six are graded at round 20 on cell 2's evidence. Their served half is now MET per the CVO's v60 reads; their page half is
  unmeasured.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 20 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **The 3.9 floor in `_ensure_unit_map`** | LOCAL | Ruling 1. |
| 2 | **The six render outcomes: a served census over 96 names, plus a 5174 walk per outcome** | LOCAL read and a walk | Ruling 2. Signed-out control first; per-outcome pages named in the order. |
| 3 | **Re-sign `r-1`** with the `admit` step | WORLD, under a pair and a NEVER-2 entry | It waits on AMGT_RESAPP r51 cell 1. |

**Fan-out:** 2 now; cell 3 is dependent.

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)

- Remove the drained worktrees [recursive delete, CLAUDE.md Agent Autonomy]. They are unchanged from round 18, plus this round's.

## Compiler Tools

- The CVO's v22: its `t2_AC1.sh` replay (214 of 214) and its u-1 AC1/AC2 re-runs.
- This seat: the round-14 analysis's ruling 7 and the PRD's FWD-10..18 header lines (`:318`, `:373`, `:401`, `:428`, `:464`,
  `:484`).
