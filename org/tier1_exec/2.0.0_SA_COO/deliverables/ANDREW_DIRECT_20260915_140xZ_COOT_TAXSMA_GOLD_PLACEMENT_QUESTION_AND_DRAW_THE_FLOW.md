# ANDREW-DIRECT 2026-09-15 ~14:0xZ -- MDPF_TAXSMA: "shouldn't need TAXSMA in gold" + "/draw the intended design flow"

**Channel:** the `2.0.0_SA_COO~T` terminal, mid-turn, while that seat was drafting the MDPF_TAXSMA L5 decomposition
(PRD v0.2 ADMITTED @60c722fe64). Both messages arrived before 2026-09-15T14:04:12Z. Recorded by `2.0.0_SA_COO~T`.

## VERBATIM

1. *"Shouldnt need TAXSMA in gold, that should be entirely retrievable from silver 0833 schwab, maybe gold is just an intermediary published location in opal-data-mdpf or something"*
2. *"What is the intended design flow? /draw it"*
3. *"dont take my word for it, just /draw, maybe im mistaken or you have better framing"*

Message 3 settles the class: this is a question put to the seat for its own framing, NOT a ruling.

## What it touches (measured, not adjudicated)

- The ratified PRD's CONTRACTS rows "Gold history and corrections" and "Canonical naming and tenancy", and surface
  S05 (`taxsma_assets`), whose home is CTO disposition 96960 (R7: firm-attributable Gold/state in the firm bucket),
  carried in `org/tier1_exec/1.0.0_SA_CTO/deliverables/TAXSMA_D8_PIPELINE_20260915/GOVERNING_CONTRACTS.md`.
- `lib/opal_naming.address()` at HEAD @3f42aff4af resolves `taxsma_assets` to
  `s3://opal-data-49financial/mdpf/49financial/gold/taxsma_assets/date=<K>/data.parquet` and Global category Gold to
  `s3://opal-data-mdpf/...`. The firm bucket exists (`s3api head-bucket opal-data-49financial` rc=0 at ~14:0xZ, with
  `opal-data-assets` as the positive control).

## Status

**OPEN QUESTION, NOT A RULING.** The sentence is phrased as a question ("Shouldnt need", "maybe"). This seat answers
it on the merits at the terminal and does NOT change the PRD, which is `1.0.0_SA_CTO~A`'s (L4) under
`1.0.0_SA_CTO`'s disposition 96960. If Andrew rules a change, it is a PRD addendum by its owner and re-enters L5
through the notifier. Until then the decomposition proceeds on the ratified v0.2, and the cells on the Gold-placement
surface (S05, and the S06/S07/S08/S13 grants and reads that key on its address) are marked as the ones his answer
would move.

Broadcast: `1.0.0_SA_CTO`, `1.0.0_SA_CTO~A`, `0.0.0_AB_MSTR`, same turn.
