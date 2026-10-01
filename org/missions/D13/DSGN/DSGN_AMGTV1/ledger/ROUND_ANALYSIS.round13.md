# DSGN_AMGTV1 -- ROUND 13 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~19:3xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27344, *"L10 slug DSGN_AMGTV1 round 13 @c882597076"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v15.md` (read to EOF, 9,291 B). Issuer: `round13/ROUND13_CLOSE_WALK.md` and
`round13/DRAIN_END_READ.md` @`8044f39976` (walk M; the render run PASS 63 / FAIL 11).

**Round 13 is CLOSED:**
- 6 of 6 orders terminal;
- `Z-C-S15` GRADUATED;
- 6 of 6 judgment criteria graded: l-1, l-2, l-4 and l-6 MET; l-3 and l-5 PARTIAL.

**The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **l-1:** v14's live no-dossier regression is CLOSED on DEV. 6501 (Hitachi) reads "no research dossier exists for this name" on
  Thesis, Exec, Posture and the header. PROD is not measured; it follows the promotion.
- **l-2:** each fiscal row names its unit. Every Model cell opens a tooltip with its mnemonic and full value (`ModelCell` +
  `FigureTooltip` at DEV `118cd005`).
- **l-4:** the list reads as one dark container to a person and to the instrument.
- **l-6:** fwd16 and fwd17's values match what a person reads on the PNGs, with one boundary: fwd17's "8 of 8 ... 0 amber" sits
  inside a fold that the at-rest PNG does not open.
- **l-3 PARTIAL:** the page renders the PRODUCER's reasons faithfully, and those reasons carry machine tokens (`Z-S7`):
  - "(IDVZ|PFOE|DIVZ)";
  - "RECOMMENDATION line";
  - "class A missing or class B missing".
- **l-5 PARTIAL:**
  - ERROR prints the raw response body;
  - NO-PERMISSION names "this firm's advisor book", and its second sentence starts in lower case;
  - Peers has no designed EMPTY state (fwd19 FAIL).

## 2. RULINGS

1. **Machine tokens in served reasons are fixed at the PAGE, by the page's own existing pattern.**
   - `ModelTab.tsx` already turns a served reason into words (`caseAbsenceWords` -> `formulaInWords` + `dropContractCodes`, `:317-324`)
     and keeps the served reason whole in a `data-*` attribute.
   - The same treatment extends to every face that prints a served reason: header, Exec, Posture, Thesis.
   - The three token families `Z-S7` names get plain sentences, and each whole reason stays in its data attribute.
   - **Why the page, not the producer:** the reasons are produced by AMGT_RESAPP and AMGT_CORPUS for machine readers as well. Rewording
     them there moves a served contract for every reader, while the page mapping moves only presentation. Producer wording is not
     re-opened.
2. **ERROR states what failed and what to do, in navy text (C12.3).** The response body never reaches the face; it rides a `data-*`
   attribute for the instrument. A real outage must not print whatever body the API happens to return.
3. **NO-PERMISSION on this page names this page's object and who grants it (C12.4).**
   - For example: "You do not have access to this security's research. Your firm administrator can grant it."
   - The shared component takes a page-specific sentence, with a capitalised second sentence.
   - The shared default is untouched for the page that owns "advisor book".
4. **Peers gets a designed EMPTY state** (FWD-19, the order's expected defect).
5. **Exec's empty-state sentence comes from the served reason, never a static filer assumption.** `ExecManagementTab.tsx:247` asserts a
   10-K for every name, and 6501 is a Japanese filer. Where no reason is served, the fallback claims no document type.
6. **An ABSENT model and its version history must not contradict on one face.**
   - "No model in the research pack for this name yet" sits beside "212 figures added ... between versions".
   - The empty state is keyed on the latest block and the compare on history, so both are true. A PM reads a contradiction.
   - **Ruling:** the compare block, when the latest model is ABSENT, is headed as history ("Earlier versions of the pack held these
     figures"). It is not hidden: the history is information a PM may want.
7. **Posture's settled footer must not say "still loading".** The at-rest footer states the comparable bundles' outcome.
8. **The instrument arms:**
   - fwd17's render run adds an OPENED-fold PNG, so its cite count is person-readable;
   - `sizes` and `radii` (10px YAxis, 9999px badge, 12 dots) are graded against C1 and C11 as round-14 styling. They are an instrument
     gain from the refreshed fixtures, not a regression.

## 3. FWD GRADES

- **REALIZED, standing:** FWD-4, FWD-9, FWD-10.
- **MET on local DEV, NOT REALIZED until the portal promotion (Andrew's act):**
  - FWD-12 (one band);
  - FWD-13 (units and tooltip, l-2);
  - FWD-14..18 (render run PASS; l-6 person-read match).
- **NOT REALIZED:**
  - FWD-11 (machine tokens through served reasons, ruling 1);
  - FWD-19 (Peers EMPTY);
  - FWD-20 (the render check shows it CAN FAIL; the whole-contract PASS waits on 14's fixes);
  - FWD-1, 2, 3, 5, 6, 7, 8 as round 12.
- **3 of 20 REALIZED; 7 more MET on DEV.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~D` cuts for round 14 in ONE issuance

Every cell is LOCAL on portal DEV, landed per CLAUDE.md Portal. At most three mechanical criteria per build order. Every served or
render criterion carries its positive arm before the cut (CVO proposal @`09a6f6dd39`, accepted amended).

| # | cell | FWD | note |
|---|---|---|---|
| 1 | **Reason words on every face** (ruling 1) | 11 | Criteria: the three `Z-S7` families render as sentences on BA's header, Exec and Posture; the served reason is whole in the data attribute; a planted new token family is dropped by `dropContractCodes`. |
| 2 | **Designed ERROR and page-specific NO-PERMISSION** (rulings 2-3) | 19, 11 | Criteria: a forced 503 renders no brace or quote character on the face; NO-PERMISSION reads this page's object and starts each sentence in capitals; the shared default stays byte-equal for its other user. |
| 3 | **Peers EMPTY** (ruling 4) | 19 | Criterion: fwd19 `peers/empty` PASS on the render run, with the branch reachable from a fixture. |
| 4 | **Exec reason-sourced empty sentence + the Posture settled footer** (rulings 5 and 7) | 11, 19 | Criteria: 6501's Exec reads its served reason with no "10-K"; the settled posture footer carries no "loading". |
| 5 | **ABSENT model vs history** (ruling 6) | 15, 19 | Criterion: `model-empty.png` shows the empty sentence and a compare block headed as history. |
| 6 | **Sizes and radii against C1/C11** (ruling 8) | 20 | Criterion: `sizes` and `radii` PASS on the render run. |
| 7 | **fwd17 opened-fold PNG** (ruling 8) | 17, 20 | Criterion: the render run writes `posture-cites-open.png`, and its count equals `grades.json`. |

**Fan-out:** all 7 are independent. Cell 7 is instrument-only.

**Judgment (L9):** for cells 1, 2, 4 and 5, the CVO reads the PNGs as a person. This is a "no machine token and nothing contradictory
on the face" read.

## 5. ACTS ONLY ANDREW CAN DO (cited)

- **Portal PROD promotion** [CLAUDE.md Portal: "PROD gated"]. This carries l-1's closure and FWD-12..18 from MET on DEV to REALIZED.

## Compiler Tools

- The CVO's v15: walk M's shots, opened by the CVO; the render run's PNGs and `grades.json`; the page code at DEV `118cd005`.
- This seat read the precedent (`ModelTab.tsx:312-324`, the `caseAbsenceWords` pattern) during the CORPUS aa-4 trace this hour.
- This seat ran no new instrument.
