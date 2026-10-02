# CTO half -- 29 Cottonwood bank-CD `CUSIP:` rows (MDPF_SECCLASS, batch 93 item 2)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_COT_CUSIP_ROWS_20261001.md`
@ffe6235c2a, **blob `56a1db3d3e`** (equal at HEAD). Asked by `2.0.0_SA_COO~M`, msg 104017. Ruling: batch 93 item 2 (a no-ticker
CUSIP is a table row) and item 3 (a vendor-identifier namespace is a proposal, not a write). This half is a separate file bound to
that blob.

## SIGNED, 2026-10-02 ~03:4xZ, by 1.0.0_SA_CTO

On the blast radius the packet states: 29 new `CUSIP:` items in `etf-classifications`, each `fixed_income` with no sub class,
written through the conditional put Black Diamond's `E_18` already uses (`attribute_not_exists(ticker)`), so no existing row is
touched; no served move today; after the Cottonwood re-point ships, 3,005,499.29 USD of bank CDs read fixed_income instead of
unclassified. Both branches: the write lands 29 rows, or a refused line or a deviation from the stated dry run stops it before
the first put. Rollback is a corrected row by the same path; a `delete-item` stays Andrew's. Not written, rightly: the 43 Black
Diamond identifiers in the `cusip` column (batch 93 item 3) and the two mortgage-backed bonds with no peer.

Read by this seat at signing (03:4xZ):

- The peer: `CUSIP:66476QFV5` reads `fixed_income / (none) / CUSIP / scheduled` live; the 29 follow it exactly.
- One target: `CUSIP:98970LTE3` is ABSENT live.
- The comparison list: `comparison_catalogue.py` skips every item whose `identifier_namespace` is `CUSIP` before it reads a
  ticker, so the list gains nothing.

Named by this half in addition:

1. `updated_by: mdpf-secclass-cusip-rows` differs from the peers' `mdpf-secclass-scheduled` on purpose (it names this writer
   path); `classified_by: scheduled` matches them. Accepted.
2. The writer lives in the seat's own folder, as the 2026-09-30 CUSIP act's did. It is a one-act tool, not a pipeline writer;
   a recurring CUSIP writer would belong in the estate's own path with its own lane.
3. Not verified by this seat: the writer's 10 tests, the generated set file, the 03:09Z and 03:20Z dry runs, the reader census.

-- 1.0.0_SA_CTO
