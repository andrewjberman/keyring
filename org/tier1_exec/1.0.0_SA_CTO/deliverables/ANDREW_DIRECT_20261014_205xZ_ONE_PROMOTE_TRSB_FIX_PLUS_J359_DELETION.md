# Andrew-direct 2026-10-14 ~20:5xZ (dell1, `1.0.0_SA_CTO~DELL1` terminal) -- one promote: the TRSB Excel fix plus the J359 footnote deletion, ASAP

## VERBATIM

> "I want this on PROD asap so i can test it: [the CRO~DELLX status of `cand/dell1/trsb-history-excel-download`] . I understand there is
> some work being done currently on MDPF with COO~D1. That cannot hold up the TRSB fix, so we need to get the TRSB fix merged into DEV and
> promoted. we have an 0.4.0_DT agent live on this fabric who can handle it."

> "Also if there is any lingering work (e.g. the disclosure about methodology deletion from J359 that has not made it to PROD yet, that
> should be folded in to the promote that caries the TRSB fix."

## What it decides (verbatim scope)

- **ONE chosen-set PROD release by dell1's one promote DT (`0.4.0_DT_ClientPlatform~H1`), as soon as possible.** It carries:
  - `cand/dell1/trsb-history-excel-download` @`040b152f`: Opal-internal, row `dell1-20261014T204814Z-c2b9` APPROVED by Andrew. It is already in DEV at `bbad56e3`.
  - `cand/dell1/satellite-returns-method` @`714f8e48c8`: client-facing, row `dell1-20261014T202134Z-fbdf` APPROVED by Andrew ("go ahead with the deletion",
    `2.0.0_SA_COO~J1` record @50234ae112). It is merged forward to DEV first.
- **MDPF_CANON work in flight (`2.0.0_SA_COO~D1`, Variant 1 round) does NOT ride and does NOT hold this release.**
- Lingering approved work: the two above are the only approved, unpromoted dell1 rows read at ~20:55Z. Nothing else on dell1 is approved and unpromoted.

-- 1.0.0_SA_CTO~DELL1
