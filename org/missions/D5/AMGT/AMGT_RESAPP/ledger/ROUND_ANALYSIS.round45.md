# AMGT_RESAPP -- ROUND 45 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-28 ~21:1xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26211, READ-acked, subject *"L10 SLUG AMGT_RESAPP round 45
@6841a976e4"*, citing `surprise-channel/adjudications/ADJUDICATION_v55.md` @`6841a976e4` (LOCAL at receipt).
First analysis after the site-Z reboot and the S19 history rewrite; every hash below is POST-rewrite.

**Round 45 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE SLUG MEASURED, AND WHAT I TAKE FROM IT

| limb | reading (the CVO's, re-measured by it, not adopted from the packet) |
|---|---|
| L7 | 4 of 4 terminal on the LAST `<status>` tag; project-wide 0 of 234 orders pending or staged |
| L8 | 633 items over 68 files, `unknown: []`; 10 gating rows: 3 GRADUATED on the CVO's own re-runs (`Z-S236`, `Z-S251`, `W130-S1`), 7 CARRIED with reasons; 6 rows since round 44, of which the packet listed 4 |
| L9 | `tt-3` AC2 PASSES (a) 3/3, (b) 3/3 on FRESH captures, (c) 3/3 as written -- with a methodology finding the band cannot see |

**Round 44's two gaps are closed on the right grounds.** The round-44 analysis asked for (1) a sample chosen against
the criterion's full clause set and (2) a served value observed crossing to the render. `tt-3` chose RKT / AMD / GOOGL
against clauses a/b/c; the CVO read each render's Base case line byte-equal to the served `base_line`, on captures
dated 18:50-18:52Z. Clause (b) is no longer bound to round 43's fixture.

**`Z-S268`'s graduation is re-grounded, not re-decided.** `Z-S289` showed round 44's "95 of 95" never tested
`abs_missing`. The CVO re-read `round45/close-run/served.tsv`: 95 rows, OK 95, `abs_missing` / `fig_missing` /
`cit_missing` 0 on all 95. The falsifier moved on the served plane (86 -> 0), and the planted pre-fix exports still
read NOT OK (2 of 2).

---

## 2. THE DECISION THE SLUG HANDS ME -- THE BASE-CASE BASIS

**The finding.** Base case = `BEST_EPS (FY1) x median(PE_RATIO)`. `consensus_eps` carries no `basis` field, while every
`fiscal_year_figures` row beside it does. `PE_RATIO` tracks GAAP (AMD 2023: 229.06 against GAAP-implied 278 and
adjusted-implied 55.6). `BEST_EPS` behaves as adjusted (INFERRED from magnitude). On the CVO's same-basis proxy
(INFERRED, not the producer's rule) AMD reads ~0.66 of `px_last`, not 1.035. **AMD was sampled for clause (c) because
it sat near 1; that nearness is produced by the mismatch, and the `[0.33, 3.0]` band passes it either way.**

**My ruling splits it along the line of whose call it is:**

1. **MECHANICAL -- mine, and a round-46 cell.** `consensus_eps` carries `basis`, as its siblings do, so a consumer can
   refuse a mismatched pair (A VALUE MUST CARRY ITS CLAIM). Adding a field to a served object moves served output:
   the cell carries a never-widen pair (issuer + CTO) naming the one added key per firm scope; DELTA on existing keys
   must read 0.
2. **METHODOLOGY -- NOT mine.** Whether the multiple is taken on the same basis as the EPS (adjusted/adjusted, or
   GAAP/GAAP), or the case keeps its current construction and states it, is a case-methodology choice. The served
   page already routes case methodology to Andrew ("to be discussed with Andrew"). **It goes to Andrew as one card;
   no cell changes the formula until he answers.**
3. **ORACLE.** The ratio band is not a plausibility oracle for this formula. Round 46's judgment criterion on the Base
   case names the BASIS of each input beside the ratio, so a grader can see a mismatch the band hides.

**GOOGL's FY1 `BEST_EPS`** (1.75x its last adjusted year) stays UNGRADED by name. It rides the next authorised
Bloomberg use; this analysis makes no new vendor ask.

---

## 3. FWD GRADES

- **`FWD-30`: its `DONE WHEN` comparison is MET on the served export** -- 95 of 95 names, the same figures, cites and
  absences, nothing extra (cases 285/285, missing 0, extra 0). **I do not grade it REALIZED yet**, for two measured
  reasons: the page side of that comparison is portal DEV only (every page fix from rounds 40-45 is unpromoted), and
  `tt-2`'s limb 7 branches 1 and 2 had ZERO members in the live 95 (UNEXERCISED, not passed). The round-46 full pass
  grades it with the rest.
- **`FWD-24`** stays the open half of `FWD-12` limb 3 (the team's cited cases, 34 of 95 dossiers).
- **Every other FWD** is graded by round 46's full pass; no grade here is carried forward from memory.

**Rule 27's close condition is not met, so this analysis ends in an enrichment list.**

---

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~Z` recuts for round 46 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **The full `FWD-1`..`FWD-31` outcome pass, as one cell** | as planned (packet s.5 item 1; model `TO-CRPS-i-5`). Carries the round's JUDGMENT criterion, and that criterion names each Base-case input's basis beside its ratio (s.2 item 3) |
| 2 | **The export-compare harness loads a header that mounts HARVST's `TimelinePanel`** (`Z-S292`) | must land BEFORE cell 1 reads the page once `92a2576254` publishes (Andrew's ruling 3 pre-authorises that DEV push on two measured conditions; `0.0.0_AB_MSTR~Z` measures them) |
| 3 | **`consensus_eps` carries `basis`** | SERVED; never-widen pair; one added key; DELTA 0 on existing keys (s.2 item 1) |
| 4 | **Served values print as values, not raw float repr** (`537.6961078500001 USD`) | round 43's second defect, still visible; same never-widen pair as 3 if it touches the served object |
| 5 | **`FWD-24` cited cases** and the stale "methodology to be discussed" served reason | the reason text changes only after Andrew's answer on s.2 item 2 |

**NOT cells:**
- The order template's gitlink instruction (`Z-S290`) is the ISSUER's own template; the issuer amends it at the recut
  and states so in the issuance commit. `Z-W163-S1` stays disarmed by the measured condition until then.
- The portal PROD promote is gated (DEV only without Andrew's word); it is named here because `FWD-30` waits on it.
- The 7 carried rows keep their owners as the CVO named them (`Z-S237` safe-commit detached-HEAD limb; `Z-S255`
  portal hooks, `0.0.0_AB_MSTR~Z`; `Z-S248` another owner; `Z-S238` not authorised; `Z-W158-S1` + `Z-S276` two arms).

**Fan-out** from the chains: 2 precedes 1 (cell 1 reads the page through the harness); 3 and 4 share a write surface
and a sign-off, so they are one cell or a strict pair; 5's reason-text half waits on Andrew. Cap 8 not pressed.

## 5. WHAT THIS ANALYSIS DOES NOT DO

It does not close the project, does not choose the Base-case methodology, and adds or changes no outcome, so it
re-opens no L4-R half (the ENDPOINT hash is unmoved).

## Compiler Tools

The CVO's L8 census (`_latest_dispositions`, 633 items, `unknown: []`) and L9 render read taken as the measurement,
because it re-ran each instrument rather than adopting the packet; `FWD-30`'s `DONE WHEN` read at
`prd/AMGT_RESAPP_PRD.md:765-774` to grade the served comparison against the text, not the packet's summary;
`prd-signoff.py status AMGT_RESAPP` read ADMITTED at v0.28 (both halves current) before stating that nothing here
re-opens a half.
