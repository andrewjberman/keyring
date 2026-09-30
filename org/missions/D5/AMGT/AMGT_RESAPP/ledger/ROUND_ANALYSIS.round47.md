# AMGT_RESAPP -- ROUND 47 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~10:5xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26571, READ-acked, subject *"L10 SLUG AMGT_RESAPP round 47 @556a5a37f8"*,
citing `surprise-channel/adjudications/ADJUDICATION_v57.md`. Issuer packet: the round-47 drain-end @`c02010a3b0`.

**Round 47 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **FWD-30's instruments work again:** `vv-3` and `vv-5` read the redesigned page, with 182/182 figures and 0 wrong-way checks.
- **`vv-1` and `vv-2` are merged and VALID but NOT served.** `vv-1` is the basis-true formula plus the "Historical-multiple
  reference" label; `vv-2` is the team's cases on the scoped API. Both were measured live during `vv-4`'s window (formula 70 of 70;
  `team_cases` on 95 of 95, 28 x 3 SERVED), then rolled back under both halves. The gate refused the hyphen grant (`Z-S298`),
  and the CVO's verdict (26550) was "finish in-session or roll back". The CVO verified the rollback on the APPLIED plane (round-46
  code live, `research-dossier` implicitDeny, control allowed).
- **The re-land path is in motion:** AMGT_CORPUS round 12 moves the dossier to the builder's `research_dossier/` prefix (pair
  signed both halves, act running).

## 2. THE CVO'S DECISION -- FWD-30's harness has two writers -- RULED: one writer per artifact

- **`exportCompare.harness.cjs` (the page-side parity harness) has ONE writer: DSGN_AMGTV1.** DSGN owns the page's presentation, and
  its round-3 cell 3 (issued @`d1c583a705`, from this seat's `W4-S1` (a) ruling @`06d51bce50`) re-keys the harness on data attributes
  and opens the card windows. **That cell closes `Z-S297`,** so no RESAPP round-48 item is cut for it. RESAPP consumes the harness and
  reads its verdict.
- **`lib/research/print/render_pack.py` (the export) has ONE writer: AMGT_RESAPP.** The export's wording change (`W4-S1` (b)) is
  RESAPP's.
- If either project needs the other's artifact to change, it asks through the owning project's round, never by a direct edit.

## 3. FWD GRADES

- **`FWD-30`: NOT REALIZED.** The instruments are restored, but the export still prints vendor mnemonics where the page prints
  words, and the harness cannot yet see the card-window cites.
- **`FWD-12` (render half) and the team's cases on the page:** unserved since the rollback; they re-land in round 48.
- The others stand as `ROUND_ANALYSIS.round46.md` left them.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~Z` cuts for round 48 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **Re-land `vv-4` on the canonical prefix** | after AMGT_CORPUS r12 lands: the grant typed `amgt/harvest/gold/research_dossier/` (builder output) and `team_cases` read there. A fresh never-widen pair re-measures formula 70, label 95, and `team_cases` against the NEW prefix. STOP limb 6 on timeline output is kept |
| 2 | **The served company name and classification on list rows** (DSGN_AMGTV1 FWD-1 hop 3; C-ASKS row 1) | joined server-side from `etf-classifications`; POSN's writer moves the AMGT rows under a never-widen pair that names both branches |
| 3 | **The export's wording from ONE source** (`W4-S1` (b)) | Model line names and the formula text come from one shared definition, read by both the page and `render_pack`; the export's bytes move under a pair |

**Fan-out:** 3 cells. Cell 1 waits on AMGT_CORPUS r12's close, and cells 2 and 3 are independent of it. **NOT cells:** `Z-S297`
(DSGN_AMGTV1 round 3 cell 3).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)
- An R20 acknowledgment for the existing `amgt/harvest/gold/research-dossier/` prefix [CLAUDE.md Rule 30]. It only shortens the wait,
  because cell 1 re-lands without it once AMGT_CORPUS r12 closes.

## Compiler Tools
The CVO's APPLIED-plane rollback read (v57) taken as the measurement; this seat's r12 before-state (boto3) and the vv-4 halves as
the reference for cell 1's expected outcome.
