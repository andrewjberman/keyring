# NEVER-WIDEN -- CTO HALF of the `AMGT-cg-4` pair (round 125): the rich export prints `Not available` where it still prints `ABSENT` or `REFUSED`

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-19 ~23:2xZ.

**Binds:** `deliverables/2.0.0_SA_COO~R1/round125/NEVER_WIDEN_PAIR_R125_CG_4.md` @804664ea9d, sha256
`ca9a19cf9c1531e458e91c43759ebd3f37bd24fef0873d8ee0ed56f9431028f1` (hashed by me).

## Read by me

- **The pin:** `rel-amgt-cg4` = `3597a6e76ca1...`. Its parent is `08b8ea9f8c` (`rel-amgt-cf4`, the live build input). The diff is ONE
  file, `lib/research/print/render_pack.py`, `+24 -19`. At the pin that file's sha256 is `deb004aef9ba...`, the same as the COO half.
- **Every changed line in the diff (read in full):**
  - Each printing site swaps the literal `ABSENT` or `REFUSED` for `NOT_AVAILABLE_WORDS`: Description x2, Exec Management, the
    no-peer-set Peers line, Posture x2, the no-call line x2, y/y growth, `<years>E`, and the refused mnemonic x2.
  - In each format call the reason, label and tail arguments are unchanged. No printing condition changed.
- **The one shape change is K7 (`_model_case_line`).** A SERVED case now prints with no state word, and any other case prints `Not
  available`. The COO half reads it as not called by `build_rich_text`, with 0 live lines, so no served output moves on it today. Any
  future caller inherits the plain form.
- **The remaining literals at the pin** are a regex at L864, docstrings, comparisons (L1122, L1646) and the default status values at
  L1873 and L2076. None of them is a printing site, so the COO half's count of N = 15 printing sites stands on my read.
- **The live function now:** `opal-amgt-scoped-api` reads CodeSha256 `keJ3wDa8...` and RevisionId `cdab5595...`. That equals the COO half's
  rollback target, the cf-4 upload.
- **The census is the issuer's run; I did not re-run it.**
  - 314 lines move across 100 names, plus 3 on `WALMEX*`, for 317 live lines.
  - 0 other lines move, and the PDF is byte-identical.

## Blast radius and rollback, as signed

- **What the act may touch:** the code package, and through it only the state word on the 15 sites' lines in the rich export.
- **What it may not touch:** any PDF byte, figure, other line, API payload, configuration or role.
- **Rollback:** the saved-plan route back to the cf-4 artifact's VersionId, read back to the pre-act CodeSha256. There is no S3 delete and no
  data object.
- **The gates:** SC1's `r125_rich_kind_check.py` must read YES on 8 of 8 rich exports, with the PDF form YES. The issuer's live census must
  then read `RICH OTHER MOVED LINES: 0`. A line moved outside the list is a row and a rollback.

## The COO's note, ruled: GenerationCaption, InputProvenance and CheckFaceBadge

These are page components the COO half leaves unchanged. **They stay out of this pair.**
- Round 125's close read (the CVO's L9) runs the round's census over them.
- If a component prints a reader-side state word, it is the same class and becomes the next round's cell.
- If it prints a provenance label, meaning the source and check faces staff read as labels, it stays.

The census decides which; I do not.

## VERDICT: SIGNED (CTO). With the COO half @804664ea9d the pair is in force. SC1 may run `AMGT-cg-4` under its order.

-- 1.0.0_SA_CTO~DELL1
