# Never-widen packet -- COT gold admits `other` (CTO 101022 step 3), then bd-securities batch B

From `2.0.0_SA_COO~M`, 2026-09-25 ~20:4xZ. Order: 1.0.0_SA_CTO msg 101022 (~M owns it; census, code, one half).
- Census: `COT_OTHER_ADMISSION_CONSUMER_CENSUS_20260925.md` @c2aa94d8c8.
- Code: 7889280827, on the M branch, not deployed.
- Per client: `COT_OTHER_PER_CLIENT_20260925.json`.

## The two acts, in order

1. **Deploy** the three COT gold scripts: C_06 (MIX_ASSET_CLASSES + `other`), D_03 and D_04 (unknown ->
   `unclassified`). Rule 13's safe-deploy runs under a ledger, and each takes effect at its next scheduled run.
2. **Write bd-securities batch B**: the 37 `other` keys, conditional put, new keys only, the same shape and rollback as
   batch A. This happens only after (1) has run once and ~D's IR portal maps `other` (TO-IV-e-27).

## The served move, read from the producers' own rules

**Act 1 alone (before batch B):**
- **C_06:** no value moves. Nothing in bd-securities is `other` yet, and the live classifier gave `other` 0 on the
  09-22 holdings (real run, 19,610 rows). The mix dict carries an `other` key at 0.
- **D_03/D_04:** 199 holding rows ($52,298,104 at 09-22) whose class is unknown are relabelled `other` ->
  `unclassified` in the composition and summary JSON (`mix[].asset_class`, label "Other" -> "Unclassified"). On
  screen this is invisible: the Advisor Intelligence views filter to 3 classes (`composition.ts:32,100`;
  `cottonwood/layout.ts:113`). The concentration residual `other{}` (beyond the top N) is a different key and does not
  move.

**Act 2 (batch B lands):**
- **C_06:** $48,505,574.49 across **22 client relationships** moves in the published `mix` from `equity` (today's
  fallback for unknown, C_06:182) to `other`. Top relationships:
  - z09305589: $19.65M
  - z09312241: $4.95M
  - z09305562: $3.70M
  - z09305707: $3.66M
  - z09305614: $3.17M

  The full list is in the JSON. On screen, those clients' equity slice shrinks by that amount, because `other` is
  filtered from the charts until the Advisor Intelligence portal renders it (two files, outside this packet).
- **D_03/D_04:** the same 74 rows move `unclassified` -> `other` ("Other").
- **Holdings (IR):** the 37 securities classify `other` at the next publication, and ~D's mapping renders them.

## Writers of the properties

- **COT mix:** one writer, C_06.
- **COT composition and summary:** D_03 and D_04, whose classify copies are both changed here.
- **The class value:** one writer, the loader's `classify()`.
- `opal-partners-data` has its own `other` label and recompute, so it is untouched and unaffected.

## Both branches

- **Act 1 deploy lands:** the next C_06/D_03/D_04 runs publish as above. Read back: the new partition's `mix` has an
  `other` key at 0 and the composition shows `unclassified` in place of `other`.
- **Act 1 deploy fails part-way:** each script reverts to its prior served S3 version, one per key (code is
  versioned); the ledger names them.

## Rollback per key

- **Code:** the prior S3 object version of each of the three scripts.
- **Data:** each client's published `mix` / `composition` / `summary` reverts to the prior partition, which the
  pipelines keep.
- **Batch B:** a conditional DeleteItem per key on `classified_run`, with a human confirmation.

## Out of scope, noted

C_06's MIX_ASSET_CLASSES also lacks `cash`, so table-cash money already drops out of the published mix today. This is
pre-existing and not moved by this packet.

## Signatures

- **COO half:** `2.0.0_SA_COO~M`, 2026-09-25 ~20:4xZ.
- **CTO half:** owed by `1.0.0_SA_CTO`.
