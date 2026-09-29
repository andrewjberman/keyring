# DSGN_AMGTV1 -- ROUND 3 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~11:5xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26585, READ-acked, subject *"L10 SLUG DSGN_AMGTV1 round 3 @aea6d112d0"*,
citing `surprise-channel/adjudications/ADJUDICATION_v5.md`. Issuer packet: `deliverables/2.0.0_SA_COO~D/round3/DRAIN_END_READ.md`
@`3e92ffcb6b` (msg 26582).

**Round 3 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

5 of 5 orders terminal. The CVO's L9 verdicts:
- **r-3: MET, on its own harness runs.** The parity harness reads the page's data and card windows (sets 4 of 4 exact). Deleting one
  absence fails it (`rc=1`, `missing=1`). `Z-S297` is closed.
- **r-2: TRUE sentence on every walked name** ("not served on this page yet"). This fixes round 2's false one. The INTU team-case
  arm waits on AMGT_RESAPP's `vv-4` re-land (r48 cell 1, now unblocked).
- **r-4: MET on the face.** r-5: MET on band and money, with SAP GY in EUR. The chart caption is UNGRADED: no walked name serves a chart.
- **r-1: PARTIAL**, on one residual, "WALMEX\* MM" (see decision 2).

## 2. THE CVO'S DECISIONS

1. **`Z-S3`: `walk.mjs` reports 0 findings on a sign-in page -- RULED: fix it before the next walk is graded.** The walk harness
   must FAIL when any step lands on the sign-in page, and its positive control is a deliberately signed-out run that fails. Until
   then, a walk's zero is an unproven reading. Cell 1.
2. **"Extend the ticker cleanup from `/` to any key metacharacter" -- RULED: NO, and my round-1 ruling 3 is reversed.**
   `BP/ LN` and `WALMEX* MM` are the Bloomberg tickers themselves. The `/` and the `*` are part of what a PM types into a terminal,
   not artifacts of our key. FWD-2's ACCEPT forbids "a code the PM would have to look up", and a ticker in its own exchange form
   is not one. **The page shows the ticker as Bloomberg writes it:** only the key's own encoding (`_`, the `_Equity` suffix) is
   removed, and `BP/ LN` returns. Once AMGT_RESAPP serves the company name (r48 cell 2), the name leads and the ticker is
   secondary. Cell 2 (a small revert of round 2's slash strip, with arms for `BP/ LN` and `WALMEX* MM`).

## 3. FWD GRADES

- **`FWD-4`: REALIZED.** Its bar is a walk on names in more than one currency. The header's four cards each lead with one figure
  and open a window (rounds 1-2). Every money figure is in the company's own currency, graded on VLO and INTU (USD, e-3 PASS
  round 2) and on SAP GY (EUR: `Price EUR 184.18`, `Enterprise value EUR 226B`, r-5 MET this round).
- **`FWD-9`: REALIZED** (round 2), standing.
- **`FWD-1`:** NOT REALIZED -- hop 3 (AMGT_RESAPP r48 cell 2).
- **`FWD-6`:** the INTU arm waits on the `vv-4` re-land.
- **`FWD-7`, `FWD-10`, `FWD-11`:** faces met or nearly, with residuals in s.4.
- **`FWD-2`:** needs the served name and classification.
- **`FWD-3`, `FWD-5`, `FWD-8`:** not yet cut.
- **2 of 11 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~D` cuts for round 4 in ONE issuance

| # | cell | outcome | note |
|---|---|---|---|
| 1 | **The walk harness fails on the sign-in page** | the round's instrument (`Z-S3`) | a positive control: a signed-out run FAILS; lands before the round's walk is graded |
| 2 | **Tickers as Bloomberg writes them** | FWD-2 | decision 2; `BP/ LN` and `WALMEX* MM` shown whole |
| 3 | **Status words off the Model face** | FWD-11 | "REFUSED --" x20, "ABSENT --", "Base case: SERVED --", "PEERS V / DIVERGENCE D not read" become plain sentences; the census gains a status-word class |
| 4 | **Exec Management: the last dark band and its raw "Read detail"** | FWD-7, FWD-11 | `roster_status`, `source_accession` and the like behind the detail read as words |
| 5 | **Posture evidence** | FWD-10 | the comparable's missing sources said once; the raw figure codes in cites (`OPER_MARGIN FY2025 ... PERCENT`) read as words |
| 6 | **The history view** | FWD-3 | ten or more names without a knot of lines, as ruled at F1 (@`ac5433b35b`); the first cut of this outcome |

**The round's one real run:** the signed-in walk on VLO, INTU and SAP GY, graded only after cell 1 lands. **Fan-out:** 6, cap 8.
**NOT cells:**
- "$1,234" inside INTU's drafted prose. C-PRESENTATION-ONLY forbids rewriting served prose, so this is the drafter's, if anyone's.
- The chart caption. No name serves a chart, so it is re-read when one does.

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)
- Remove the merged worker worktrees, if he wishes [CLAUDE.md Agent Autonomy: recursive deletion].

## Compiler Tools
The CVO's harness runs and PNG judgments (v5), and the COO's DRAIN_END_READ s.4, taken as measurements; FWD-4's DONE WHEN and FWD-2's
ACCEPT read at the PRD's ENDPOINT section.
