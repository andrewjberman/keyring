# DSGN_AMGTV1 round 22 -- CTO review of the portal candidate `a730d8ce` (product files), `1.0.0_SA_CTO~Z`, 2026-10-02 ~07:5xZ

**Asked by:** `2.0.0_SA_COO~D` msg 28291. Round-22 close: `deliverables/2.0.0_SA_COO~D/round22/ROUND22_CLOSE.md` @863ff402ec.

## What I read

- **Base:** `3ca6c53a` is an ancestor of `a730d8ce`. The candidate diff from `3ca6c53a` is **9 files, +101/-36, all under
  `src/pages/SecurityAnalysis/`**. 0 files fall outside it.
- **The code:**
  - `reasonWords.ts` adds ONE guard (`hasCodeShapedToken`, `guardedReason`). It matches field codes, security keys, file names,
    the state words ABSENT / UNMAPPED, and UPPER_SNAKE state codes. A served string carrying one prints the plain fallback
    sentence, and the served text rides a `data-` attribute.
  - `ExecManagementTab.tsx` prints "Contact enrichment was skipped for this company", followed by the served reason only when
    it is code-free.
  - `PostureTab.tsx` passes the claim through the guard.
  - `cscTable.ts` drops the code from the reason words, and the code stays in `code`.
  - The Peers subject row fills Price, EV and P/E from the header.
  - **Producer strings are not rewritten.** The guard only withholds them, which matches ruling 1 of the round-21 analysis.
- **COO~D's checks:** 3 round checks, 14 of 14 harnesses, `tsc` 0. On the signed-in walk 20261002T072805Z, the Peers subject rows
  carry the header values (BA 196.80), and VLO Exec and BA Posture carry no code.

**Verdict: APPROVED as a DEV candidate.**

## Two facts for the push and the promote

1. **Remote DEV has moved.** `git ls-remote` reads DEV `c4e0d744`, and that is NOT an ancestor of `a730d8ce`. The DEV landing is a
   merge of `a730d8ce` onto `c4e0d744`; the files are disjoint, but it is not a fast-forward. `2.0.0_SA_COO~D` prepares that
   merge locally and re-runs `tsc` and the 14 harnesses on it, so that the push becomes a fast-forward.
2. **A merge-forward PROD promote carries more than DSGN.** PROD `b3a1d8a6` -> remote DEV `c4e0d744` is 10 non-merge commits and
   40 files:
   - 30 files under `src/pages/InvestorReporting`;
   - 8 under `src/pages/AdvisorIntelligence`;
   - `src/lib/chartColors.ts` and `src/components/holdings`.
   They come from FAST-lease commits on DEV (DSGN_IRPTV1 items 63-69, IRPT_DASHBD, MDPF_SECCLASS). Under CVO verdict 27503, a
   payload beyond Security Analysis is Andrew's to name.

## Acts only Andrew can do (cited)

1. **The DEV push of the merged candidate.** `0.0.0_AB_MSTR` pushes trunks on his word.
2. **The PROD promote, and its payload.** Either the merge-forward of DEV (Security Analysis + the 40 other files above), or a
   Security-Analysis-only payload he names (CVO verdict 27503). Rollback is `b3a1d8a6`.
