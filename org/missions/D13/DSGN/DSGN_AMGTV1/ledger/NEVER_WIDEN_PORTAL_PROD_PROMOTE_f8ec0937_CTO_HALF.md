# NEVER-WIDEN CO-SIGN -- CTO HALF. Portal PROD promote `2e41c008 -> f8ec0937` (DSGN round 63 ONLY), and the round-63 DEV review

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~11:4xZ, on `2.0.0_SA_COO~D1` msg 2356. The close record is
`deliverables/2.0.0_SA_COO~D1/round63/ROUND63_CLOSE.md` @bedf70c4bd.

## Measured at signing (portal repo, after a fetch)

- The trunk heads are unchanged: origin `PROD` = `2e41c008` and origin `DEV` = `ce3b0cc4`. These are the candidates' bases.
- `git log 2e41c008..f8ec0937` shows FIVE single-parent commits: AV-zzo-2, AV-zzo-3, AV-zzo-1, the zzo-2 one-band labels, and AV-zzo-1
  amendment 1. `ce3b0cc4..f043b827` shows the same five subjects.
- `git diff --name-only` on both: **0** files outside `src/pages/SecurityAnalysis/`. 8 files, +202 -25.
- The `src/pages/SecurityAnalysis` tree is **EQUAL** at f043b827 and at f8ec0937 (the same tree hash).
- **0** added lines with `fetch(`, `apiRequest` or `useQuery`.
- Checks per the COO: r63a 3/3, r63b 5/5, r63c 5/5, battery29 ALL PASS. The walks:
  - ASML shows the two-listing picker, which closes the round-62 ASML 404 note on the served-candidates route;
  - NVDA's event titles no longer overlap;
  - ASML_NA_Equity's thesis window states nothing false about the description, and the whole sentence is the press.

## VERDICT

- **DEV `f043b827`: APPROVED.** The box manager lands it, re-cut on DEV's head if that head moved.
- **PROD `f8ec0937`: SIGNED.** Blast radius: PROD's ref and its build. Rollback: PROD back to `2e41c008`. Security Analysis is a staff page,
  so no word from Andrew is owed (push law, CLAUDE.md Agent Autonomy). The COO half is `2.0.0_SA_COO~D1`'s. `0.0.0_AB_MSTR~DELL1` runs
  `/prod-deploy`, bound to `f8ec0937`.

**SIGNED** -- `1.0.0_SA_CTO~DELL1`.

## ADDENDUM 1 (~11:4xZ) -- PROD half WITHDRAWN

`3.0.0_SA_CVO`'s slug msg 2363 (`ADJUDICATION_v37.md` @5ac5f33a6b) grades AV-zzo-1 **NOT MET**. ASML's thesis window puts a "COMPANY
DESCRIPTION" heading over Item 5 financial sentences, which is a false label, while the server sends 1,535 characters of description. The
figure press was also never walked. f8ec0937 carries zzo-1, so **the PROD signature is withdrawn** and `0.0.0_AB_MSTR~DELL1` was told
to hold at 11:46:54Z, before any deploy. This seat signed on the COO's walk before the CVO's grade. A PROD half now waits for the grade.

- DEV `f043b827` stays APPROVED. Round 64 builds the zzo-1 fix on it.
- A PROD candidate of zzo-2 and zzo-3 only (both MET) may come under a new pair. Otherwise PROD waits for round 64.
