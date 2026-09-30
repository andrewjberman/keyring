# AMGT_CORPUS -- ROUND 7 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-28 ~23:4xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26283, READ-acked, subject *"L10 SLUG AMGT_CORPUS round 7
@ad5b98b64b"*, citing `surprise-channel/adjudications/ADJUDICATION_v10.md`. Issuer: `2.0.0_SA_COO~X`, packet
`deliverables/2.0.0_SA_COO~X/ROUND7_DRAIN_END_PACKET.md` @`ed8debee79`.

**Round 7 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE SLUG MEASURED

| limb | reading (re-measured by the CVO, not adopted) |
|---|---|
| L7 | 5 of 5 terminal on the LAST `<status>` tag; 1 judgment criterion (`i-3` AC4) |
| L8 | 80 items, `unknown: []`, 32 UNDER_INVESTIGATION. `Z-S45` GRADUATED: `/2` served on 95 of 95, `stale_pick 0` (the round-6 split of 49 / 46 is gone). `Z-W5-S2` GRADUATED. 8 BLOCKING/ARMED CARRIED with reasons |
| L9 | `i-3` AC4 **NOT MET** on the workbook half: 0 of 42 computable selections inside [0.5, 2.0]; the served half UNGRADED (no team number to read it beside) |

**The round delivered its act.** The continuation method `/2` is the one every reader serves, and the dossier rewrite
landed on 95 of 95 under closed change entries.

**The slug confirms the routed defect on the served plane:** `read_dossier("AZN_LN_Equity")` serves
`cases.base = {"value": "Base Case", "citation": {"passage": "Base Case", "locator": 0}}`. The case value is its own
heading, cited to itself. **`FWD-12` limb 3's data half is NOT MET**, as ruled at msg 26235; the worker's literal `met`
is not adopted.

---

## 2. THE DECISION THE SLUG HANDS ME -- WHERE "THE TEAM'S OWN CASES" COME FROM

**The findings.** (A) The workbook route fails on its own evidence: the one-pager's F-column "Base Case" block is a 2D
layout whose selected cells are yields and ratios, one label 65 rows from its value, 0 of 42 plausible. (B) Worse, the
value `0.22414202074587247` sits as a "Base Case" candidate in **15 different companies' workbooks (32 slots)**: the
template's own cell, left unedited. A reader keyed on that block would serve one number as fifteen companies' Base case.

**`FWD-12` does not name a source.** Its `DONE WHEN` asks that *"the team's Upside/Base/Downside cases render as the
team's, cited"* (`prd/AMGT_CORPUS_PRD.md:405-406`). The team writes its cases in two places: the research pack's prose
(the section the dossier already locates, then serves as a heading) and the workbook one-pager. **The choice between them
is an implementation choice under an unchanged outcome, so it is mine.**

**RULING.**
1. **Prose first.** Round 8 extracts the text UNDER the case heading (`lib/research/corpus/dossier.py:701-704`), which is
   the team's own written case, cited to its passage. The census reports, per name and per case, body-with-content /
   heading-only / absent, with the 95 denominator. This is the cheapest route to the team's own words, and it fixes the
   defect RESAPP routed here (its Z-S293).
2. **The workbook route is NOT re-cut in round 8.** It returns only if the prose census leaves names with no written
   case, and then under a hard rule:
3. **CROSS-NAME REPEAT REJECTION (binding on any future workbook reader).** A candidate value that appears verbatim in
   the workbooks of two or more DIFFERENT names is template residue and is never selected; the reader prints how many
   candidates the rule removed. The `0.22414202074587247` family is the positive control.

`i-3` AC4's workbook half therefore stands NOT MET and is not re-graded until a workbook cell exists.

---

## 3. SMALLER RULINGS

- **`FWD-9` and a planted control.** The fifth unresolved site is `key_glob_census.py:199`, i-4's own planted control. A
  control that writes inside the censused tree will be read as an unresolved write in the next census. **Ruling:** a
  planted control writes OUTSIDE the censused tree. That needs no census schema change. The other four sites
  (`induction_run.py` deliverables-dir writes) are resolved by origin in the round-8 cell.
- **`Z-W2-S11`'s example contradicts its producer** (Finding B: the row says 8306_JP's column K is empty below K43; the
  producer selected `K45 = 2108.7834` on the same workbook). The grade does not rest on it. The owner, `2.0.0_SA_COO~X`,
  appends a correction row; this is not a cell.
- **Stray temp dirs** (`%TEMP%\amgt_corpus_ro_copy_*`, ~308 MB for the newest, plus ~45 census dirs) are outside the
  repo. Removing them is recursive deletion and waits on Andrew's word; nothing in the loop depends on it.

---

## 4. FWD GRADES

- **`FWD-12`: NOT REALIZED.** Rows and labels stand; limb 3 (the team's cases) is NOT MET on the served plane.
- **`FWD-9`: NOT REALIZED** on 5 unresolved sites, one of them a planted control (s.3).
- The remaining outcomes stand as `i-5`'s nineteen-outcome evidence pass records them
  (`deliverables/0.9.0_WK_AMGT_CORPUS~5/FWD_EVIDENCE_ROUND7.md`); no grade here is carried from memory.

**Rule 27's close condition is not met, so this analysis ends in an enrichment list.**

---

## 5. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 8 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **Case BODY extraction** (s.2 ruling 1) | `dossier.py:701-704` carries the text under the heading; the census prints body/heading-only/absent per case over 95; then the dossier rewrite under a never-widen pair (SERVED output moves). Carries the round's JUDGMENT: *does each served case read as the team's own written case for that name?* Run the rewrite concurrently in the producer (packet item 5), not through an issuer-side driver |
| 2 | **`FWD-9`'s five sites** | the planted control moves outside the censused tree (s.3); the four `induction_run.py` writes resolved by origin; the census reads rc 0 |
| 3 | **The derive's stamp selection (`Z-S47`)** | unblocks the 6861_JP and CSL_AU re-mints still carried on `Z-W2-S10` |
| 4 | **`read_dossier` prefers the current method version** | named by the round-7 CTO half as a round-8 input |

**NOT cells:** the workbook reader (s.2 ruling 2), the `Z-W2-S11` correction row (the issuer's), the temp-dir removal
(Andrew's word).

**Fan-out** from the chains: cell 1 is independent and SERVED; 3 precedes any re-mint; 2 and 4 are LOCAL and
independent. Cap 8 not pressed.

## 6. WHAT THIS ANALYSIS DOES NOT DO

It does not close the project and adds or changes no outcome, so it re-opens no L4-R half (the ENDPOINT hash is
unmoved).

## Compiler Tools

The CVO's direct `read_dossier("AZN_LN_Equity")` read taken as the served-plane measurement; `FWD-12` read at
`prd/AMGT_CORPUS_PRD.md:401-410` to confirm the outcome names no source before ruling on one; the packet's section 6
read to EOF so its five enrichment candidates are each dispositioned above (4 cells, 1 folded into cell 1).
