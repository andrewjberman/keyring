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

## ROUND 23 -- candidate `41eeda55` (supersedes `419ef41d`), reviewed 2026-10-02 ~09:0xZ on COO~D msg 28345

- **Ancestry,** read by this seat: remote DEV `8df9e3d3` (ls-remote 09:0xZ) and `419ef41d` are both ancestors of `41eeda55`, so the DEV
  push is a fast-forward. `8df9e3d3..41eeda55` is 10 files, +152/-54, and **0 outside `src/pages/SecurityAnalysis/`**.
- **The code** (`419ef41d..41eeda55`, 6 SecurityAnalysis files):
  - `cscTable.ts` / `PeersTab.tsx`: the absent-column reasons are now reader sentences ("This column is not reported for each of
    these peers."), with no "registry" and no "R-1".
  - `ExecManagementTab.tsx`: `filingWords()` names the filing by form and date ONLY when the served provenance carries the SAME
    accession; otherwise it reads "the company's filing". The accession rides `data-exec-source-accession`.
  - `posture.harness.cjs`: the stub is repaired (Z-W69-S1).
- **Battery,** per COO~D: 8 checks 3/3, 14 of 14 harnesses, `tsc` 0. Walk 20261002T084927Z: VLO Exec reads "the 10-K filed
  February 25th, 2026", and A3 is REALIZED (0 of 94 bars by ticker, with B1 live).
- **Verdict: APPROVED as the one DEV candidate.**
- **Z-S14:** VLO's Lusha line repeats itself, because AV-z-1's lead-in precedes B2's plain served reason. **Ruling:** when the served
  reason is code-free, print it alone, as one sentence. This is a one-line direct act folded into the candidate if it can be
  re-merged and walked by 11:30Z. Otherwise `41eeda55` ships as is, because the repetition is cosmetic.
- **PROD payload, updated:** PROD `b3a1d8a6` -> `41eeda55` is 50 files. 10 are SecurityAnalysis, and **40 are outside it**, from 11
  FAST commits on DEV (DSGN_IRPTV1 items 63-71, IRPT_DASHBD, MDPF_SECCLASS). Under CVO verdict 27503 that payload is Andrew's to
  name.

## ROUNDS 24-26 -- candidate `0ab75973` (supersedes `41eeda55`), reviewed 2026-10-02 ~10:2xZ on COO~D msg 28389

- **Content** (`41eeda55..0ab75973`, SecurityAnalysis only):
  - `reasonWords.ts` maps each served absent reason (exact text) to a CLASS, and each class to ONE reader clause. An unknown
    reason reads `unmapped`, with a generic clause, so it never prints a code. The served text rides `data-absent-column-reason`.
  - The Exec Lusha line is printed once (Z-S14).
  - The posture check is renamed, and a zero-resolved plant is added.
- **Battery,** per COO~D: 12 checks 3/3, 14 of 14 harnesses, `tsc` 0. Walk 20261002T101105Z: VLO Peers 12 of 12 reasons classed,
  0 generic; the Exec Lusha line said once; the SERP sentence gone (B5 live).
- **Verdict: APPROVED, the SecurityAnalysis content of `0ab75973`.**
- **A brittleness, carried, not blocking:** the class map keys on the producer's exact sentence, so a reworded served reason
  falls to `unmapped` (generic clause, never a code). The durable form is a reason CLASS served by RESAPP beside the text. It
  goes to the RESAPP round-62 list.
- **Remote DEV keeps moving.** `ls-remote` 10:2xZ reads `243f17b1` (one more laptop FAST commit, 0 SecurityAnalysis files), so
  `0ab75973` is not a fast-forward. **Ruling: stop chasing DEV.** The DEV landing is done AT PUSH TIME, on Andrew's word:
  - merge the approved candidate onto the CURRENT remote DEV head;
  - confirm the merge brings 0 SecurityAnalysis changes from the DEV side, and that the candidate side's diff equals this
    reviewed content;
  - re-run `tsc` and the 14 harnesses;
  - fast-forward push.
  The content approval carries; only the base moves.
