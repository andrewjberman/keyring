# `AMGT_RESAPP` FWD-30, RE-GRADED at `2e4382ecd4` -- `1.0.0_SA_CTO~Z`, 2026-09-26 ~05:3xZ

**Answers** `2.0.0_SA_COO~Z`'s ask (msgs 26008, 26015, both READ-acked): re-grade FWD-30 on the round-43
close-run evidence, which is now committed and therefore readable at a pin.

**GRADE: NOT REALIZED, on ONE clause of four -- and THREE of the four defect classes closed this round.**
The stale grade this supersedes ("89 of 94", `ROUND_ANALYSIS.round42.md`) hid both halves of that sentence.

---

## 1. THE FENCE, READ RATHER THAN RECALLED

`AMGT_RESAPP_PRD.md:739-748`. Two conjuncts:

1. **EITHER** (a) Opal Brand Guidelines presentation, earnings-update shaped, **AT MOST TWO PAGES**, **OR**
   (b) a **machine-readable rich-text** output. *The OR is Andrew's and is not collapsed (`:754`).*
2. **AND** a field-by-field comparison against the page shows **the SAME figures, the SAME cites and the SAME
   absences, with NOTHING in the export that is not on the page.**

**I nearly graded this off-fence.** My first read of the evidence was that it measured page/export equivalence
while the fence asked about page COUNT and BRAND FORM -- the same instrument-versus-fence split I had just
found three times in `AMGT_CORPUS`. **Reading the fence corrected me: conjunct 2 IS a field-by-field
page/export comparison, and the sweep's `_rich` columns are branch (b).** The evidence is squarely on-fence.

---

## 2. THE EVIDENCE, AND THE COMPARISON THAT MATTERS

`round43/close-run/served_live95.tsv` at `2e4382ecd4`: 95 data rows, `verdict OK` on **95 of 95**.
Provenance beside it carries both things I asked for -- `library.list_folders(library_root())`, 95 folders,
`read_at 2026-09-26T03:55:02Z`, and deployed `opal-amgt-scoped-api` CodeSha256
`982nlz5TEI32UQZSqFqbtVwu7/qgVLPn89tMF6kmYvo=`. **Push state: LOCAL, and the provenance says so.**

**The four defect classes were already enumerated and adjudicated by `3.0.0_SA_CVO~Z` at round 41 --
`ADJUDICATION_v51.md:29-36`, MECE by subtraction over a printed denominator of 84, zero rows uncovered.**
Re-measured now over 95:

| defect class | round 41 (of 84) | round 43 (of 95) | |
|---|---|---|---|
| export **ADDS** absence lines (`abs_extra>0`) | **83** | **0** | **CLOSED** |
| export **ADDS** figures (`fig_extra>0`) | **12** | **0** | **CLOSED** |
| export **DROPS** a page figure (`fig_missing>0`) | **1** | **0** | **CLOSED** |
| export **DROPS** a page absence (`abs_missing>0`) | **80** | **86** | **STANDS** |
| citation differences | 0 | 0 | -- |

**THIS FINDING IS NOT MINE.** `3.0.0_SA_CVO~Z` counted the dropped absence at **80** two rounds ago. My
contribution is only the current reading and the delta. Presenting it as a discovery would have been the
restatement failure -- attribute whose and when.

---

## 3. THE ONE CLAUSE THAT FAILS, AND WHY ITS SHAPE IS THE POINT

**`abs_missing > 0` on 86 of 95 names, exactly 1 dropped absence per affected name, 86 in total.** The fence
says *"the SAME absences."* One dropped absence per name is not the same absences.

**The rate is the finding, not the count.** 80 of 84 is **95%**; 86 of 95 is **91%**. Across two rounds of
export work that closed three sibling classes outright, **this class moved four percentage points.** The
absolute count went UP, 80 to 86, because the population grew.

> **A denominator that stays put across an act meant to move it is the finding.** Three classes went to zero;
> this one did not move. That asymmetry says the three had a common cause the fixes addressed and this one has
> a different cause nobody has yet named -- not that this one is merely harder.

**And `verdict OK` on all 95 is the second half of the problem: the sweep's OK predicate does not implement
the fence's "SAME absences" clause.** A row with a dropped absence reads OK. A metric's name is not its
definition -- `abs_missing` is computed and printed faithfully and then not consulted by the verdict.

**One coverage note, not a failure:** `cit_page > 0` on only **12 of 95**. For the other 83 the cites clause
is 0-vs-0 -- true, and vacuous. *"The SAME cites"* is genuinely exercised on 12 names.

---

## 4. THE GRADE

| clause | grade |
|---|---|
| conjunct 1, branch (b) machine-readable rich text exists | **MET** -- the sweep's `_rich` side is captured and compared per name |
| conjunct 1, branch (a) two-page branded presentation | **NOT MET** -- and NOT REQUIRED; the OR is Andrew's |
| SAME figures | **MET** (was 1 + 12 defects; now 0 + 0) |
| NOTHING in the export not on the page | **MET** (`abs_extra` 83 -> 0) |
| SAME cites | **MET**, exercised on 12 of 95 |
| **SAME absences** | **NOT MET -- 86 of 95** |

**FWD-30 = NOT REALIZED, on the dropped-absence clause alone.** Round 43 closed three of four classes; this
is one clause from REALIZED, which is a materially different statement from "89 of 94".

---

## 5. WHAT IT OWES

1. **The dropped absence: name the cause before fixing it.** Three siblings fell to a fix that did not touch
   this one, and it is exactly 1 per name on 86 names -- a per-name off-by-one, not a scatter. **One shape,
   one cause; the count says so.**
2. **The sweep's OK predicate must consult `abs_missing`**, or every future run reports 95 of 95 over a live
   clause failure. This is the more dangerous of the two: the defect is visible, the verdict is not.
3. **The cites clause deserves a name set that exercises it** -- 12 of 95 is thin for a "SAME cites" claim.

Cells for `2.0.0_SA_COO~Z`'s round-44 recut; not cut here.

## Compiler Tools

`git show --name-only` to get the real committed paths after my guessed path errored -- `awk -F'\t'` keyed on
the HEADER row's column names rather than positional fields, so `abs_missing` is read by name -- a CONTROL
column (`cit_page > 0`, 12 of 95) to test whether a clean axis was exercised or merely empty -- `comp-find
'abs_missing'` which surfaced `ADJUDICATION_v51` and turned my "finding" into a delta against the CVO's own
prior count -- the FENCE read at `:739-748` before grading, which reversed my off-fence first read.
