# ANDREW-DIRECT 2026-10-16 ~04:0xZ -- NFRA_WFSPINE: store it in a bucket called opal-data-trino

**Channel:** the `1.0.0_SA_CTO~DELL1` terminal, while the NFRA_WFSPINE PRD (L4) was being written. **Recorded by:** `1.0.0_SA_CTO~DELL1`, same
turn.

## Verbatim

> "I think all of this should be stored in a bucket called opal-data-trino also, using LGIC_NAMING conventions otherwise."

## What it settles (scope as worded)

- **The spine's data lives in a bucket named `opal-data-trino`:** the raw audit events, the derived views and the coverage record. The bucket
  name is his.
- **Everything else follows the LGIC naming conventions:** keys and prefixes under the bucket, and the names of the other resources, come from
  `lib/opal_naming` builder output. If the builder refuses the bucket because no registry row admits it, the row is added under
  `infra/logic/registry/`, and this word is the acknowledgement that the R20 rule asks for. A refusal is never answered with a hand-typed key.
- **Read as the spine's data.** "all of this" is read in the context it was spoken in: the NFRA_WFSPINE PRD. It does not move any other
  project's data into this bucket; a wider reading would be asked first.

-- 1.0.0_SA_CTO~DELL1
