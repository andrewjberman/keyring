# IRPT_ANLREQ PRD v0.18 -- L4-R review, ratified-text half (every unpriceable holding files for C-SWAP)

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-15 ~21:5xZ. **Delivery:** msg 8694. **PRD:**
`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @c0993a9bbe. **Compared against:** v0.16 @a4af0e5bba (signed) and v0.17
@ab6de45efb. This seat's msg 8691 noted that v0.17 changed no table row.
**Authority:** `ANDREW_DIRECT_20261015_214xZ_J4_PROD_FIRM_CHOOSER_WORKS_TICKER_SWAP_MISSING.md`, read with his 10-15 ~14:xxZ "swaps are not up
to the filer". His PROD filing was refused with "Name a similar ticker ... (a proxy)", and nothing filed.

**Verdict: SIGN.** v0.17's rule is now in the CONTRACTS table. No other ratified line moved.

- **C-FILING-HINT** now covers every holding Opal cannot price as given, `TICKER_DATA_NOT_ENTITLED` included. Such a holding:
  - files UNRESOLVED;
  - shows the filer informational words ("... The analysis will use a similar security in its place and the report will say which.");
  - is never met with a request for a proxy, because `NAME_PROXY` is retired from every filer-facing finding.

  Until r33 lands in `irpt-ycharts-generate`, such a holding is refused as today, and the form says so in words.
- **C-SWAP step (2)** takes every UNRESOLVED holding into the backend pass, and the filer is never asked for a replacement. A
  `NOT_ENTITLED` security that Yahoo or YCharts can price is KEPT at step (2), and only an unpriceable one goes on to replacement. The
  report names the replacement (step 5).
- **Agreement.** The two rows agree with each other, with C-PRICES and with FWD-2 and FWD-7. The ENDPOINT is unchanged.

-- 3.0.0_SA_CVO~DELL2
