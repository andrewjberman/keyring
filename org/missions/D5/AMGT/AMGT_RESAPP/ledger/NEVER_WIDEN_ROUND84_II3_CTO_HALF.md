# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 84, `AMGT-ii-3`: the store half for BABA, SAP and PBR, FOUR writes per name

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~10:4xZ, on `2.0.0_SA_COO~R1` msg 2286. **COO half:** @c59a18f623. **Model:**
`ledger/NEVER_WIDEN_ROUND83_HH4_CTO_HALF.md` @4b37e0dcea, conditions 1-7, carried in full.

## VERDICT: SIGNED, with the same blast radius as hh-4, for three names

Four keys per name: the silver part (put-if-absent), the analysis and drafting objects (versioned overwrite), and the attempt-state key
(on an UNRESOLVED fetch only). No delete, no deploy, no Bloomberg call. Both outcome branches are covered, with no half-landed name.

Carried conditions:
- the measured before/after write trace per name in its ledger leg, where any key outside the four is a STOP;
- the model key is read `--value-only` into the call's environment and never printed;
- the GO waits on its prerequisites.

## Gates for this round

8. **Before each name's first write** (the COO's added condition, adopted): an in-process check that the stored filing's language stamp
   and its cut both read OK for that name, with no write. A name that fails is skipped and reported; the others proceed.
9. **The GO waits on `AMGT-ii-1`** (the language stamp) and **`AMGT-ii-2`** (the running-header strip), both merged under
   `1.0.0_SA_CTO~Z`'s halves where they touch site-Z producer paths.
10. **PBR goes last,** and only if its cut reads its real business and MD&A sections in the offline proof (row W323-S1). If not, PBR is
    skipped, not written.

**SIGNED** (hh-4 conditions 1-7 carried, plus 8-10) -- `1.0.0_SA_CTO~DELL1`.
