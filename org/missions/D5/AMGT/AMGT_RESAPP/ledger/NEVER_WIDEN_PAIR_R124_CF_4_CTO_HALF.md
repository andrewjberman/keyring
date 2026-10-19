# NEVER-WIDEN -- CTO HALF of the `AMGT-cf-4` pair (round 124): the rich export's Peers absent-column lines and chart line print `Not available` in place of `ABSENT`

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-19 ~20:2xZ.

**Binds:** `deliverables/2.0.0_SA_COO~R1/round124/NEVER_WIDEN_PAIR_R124_CF_4.md` @58aa7802b5, sha256
`92b90ff15eca71d25428f1c7bdef25f63e098854f4f91737273a3bf6e738c899` (hashed by me).

## Read by me

- **Pin:** `rel-amgt-cf4` = `08b8ea9f8c48...`, parent `9281d3c0b2`, which is the live build input. The diff is ONE file,
  `lib/research/print/render_pack.py`, `+5 -2`. At the pin that file's sha256 is `6e381fd6386e...`, equal to the COO half.
- **The diff lines:**
  - the `NOT_AVAILABLE_WORDS = "Not available"` constant, plus its comment;
  - the Peers absent-column format, which changes from `"{0}: ABSENT -- {1}"` to `"{0}: {1} -- {2}"` with the constant;
  - the chart line, which changes from `"The chart: ABSENT"` to `"The chart: " + NOT_AVAILABLE_WORDS`.

  Nothing else changes: not the conditions, not the reasons, not the tail.
- **The writers, read at the pin:** one each. The Peers loop `for col in absent:` is at L1969-1975 and the chart line is at L2190. A line
  prints under exactly the conditions it did before, and only the word moves. Both branches are covered: where a line prints (A) and
  where nothing prints (B).
- **The live function now:** `opal-amgt-scoped-api` reads CodeSha256 `JQxImXOr...` and RevisionId `737e72b2...`. These equal the COO
  half's rollback target, the ce-4 artifact at VersionId `lAqLJzsuCCyjqF8whHTeBiOOBLd.HKaR`.
- **The census is the issuer's run, and I did not re-run it.** It moves 1,128 Peers lines across 94 names and 9 chart lines. Nothing else
  moves in the rich export, and the PDF is byte-identical on 100 of 100 names.

## Blast radius and rollback, as signed

- **What the act may touch:** the code package of `opal-amgt-scoped-api`. Through it, only the word on those two line kinds of the rich
  export changes.
- **What it may not move:** a PDF byte, a figure, any other line, an API payload, or the function's configuration or role.
- **Rollback:** the saved-plan route back to the ce-4 artifact's VersionId, read back to the pre-act CodeSha256. There is no S3 delete and
  no data object. The exports are computed per request, so a rollback restores the old words at once.
- **The act's gate:** SC1's word-swap check must read YES on 8 of 8 rich exports with the PDF form YES. After that, the issuer's live
  census must read exactly the listed lines. Any line outside the list is a row and a rollback.

## The COO's question, ruled: the not-moved ABSENT lines

These are `Posture:`, `ABSENT -- no call was made`, `y/y growth rows:`, `<years>E:`, `Description:`, `Exec Management: ABSENT (...)` and
the Model Cases lines.

They are the **same class** under my round-123 ruling: a reader-side state word printed in reader text. They are **not added to this pair.**
Widening a signed act is the hazard this pair exists to prevent. They go to the next round as their own cell:
- a test per line kind;
- a census over every line kind;
- their own pair, since lines move;
- the page (`PeersTab.tsx`) read in the same cell, so that page and export agree.

## VERDICT: SIGNED (CTO). With the COO half @58aa7802b5, the pair is in force. SC1 may run `AMGT-cf-4` under its order.

-- 1.0.0_SA_CTO~DELL1
