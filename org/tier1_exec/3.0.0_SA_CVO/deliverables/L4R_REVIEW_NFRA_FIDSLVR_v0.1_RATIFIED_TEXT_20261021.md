# L4-R review -- NFRA_FIDSLVR PRD v0.1 @e5a9015a3f, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-21 ~16:0xZ. Delivered by 1.0.0_SA_CTO~DELL1 msgs 9128 and 9129 (acked). Half hash
`23567774d28c`. Brief half: SIGNED (auto, CRO-written brief).

**Read:** `org/missions/D8/NFRA/NFRA_FIDSLVR/prd/NFRA_FIDSLVR_PRD.md` @e5a9015a3f, whole (202 lines); the L2 record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_FIDSLVR_20261021.md` at the same commit;
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261021_1520Z_FIDUPL_ALL_FACT_TABLES.md`;
`infra/aws/lambda/opal-assets/opal-assets-silver-schwab/schwab_schemas.py` (the ULN and ULT specs); `python .tools/open-calls.py list`.

## Verdict: REFUSE (three grounds)

- **Ground 1 -- the ENDPOINT has no ratified pin.** Open call `dell1-20261021T154821Z-cc75` ("Confirm the NFRA_FIDSLVR DONE WHEN lines
  FWD-1..FWD-7") reads `[OPEN]`. The PRD's own endpoint status says it "goes to L4-R after it".
- **Ground 2 -- the ENDPOINT is not verbatim to the L2 record.** A script compared the two fenced blocks at e5a9015a3f: DIFFER. The PRD
  makes two changes:
  - it moves FWD-6 before FWD-7 (the record has FWD-7 first);
  - it cuts FWD-7's SOURCE from `Andrew-direct ~15:35Z ("use the G Number from Fidelity and the Master Account Number from Schwab ... in
    some mapping config ... rather than rely on downstream data vendor inputs")` to `Andrew-direct ~15:35Z`, which drops Andrew's quoted
    words.

  Re-paste the record's block exactly. If the order or the source line should change, change it in the L2 record, so that Andrew confirms
  one text.
- **Ground 3 -- an operative constraint is missing from FWD-2.**
  - Andrew, VERBATIM at ~15:20Z: "yes we definitely want ALL fact tables, open tax lots, realized gain/loss, unrealized gain/loss, we need
    absolutely everything."
  - FWD-2's DONE WHEN lists "accounts, positions, balances, securities and prices, transactions, open lots, realized gain/loss". **Unrealized
    gain/loss is absent**, in both the record and the PRD.
  - The Schwab twins exist (`schwab_schemas.py` carries `('ULN'` and `('ULT'` specs). Decision 4 even rules the unrealized grain.
  - Add unrealized gain/loss to FWD-2's list in the L2 record before Andrew confirms, so he confirms the line his words asked for.

## Checks that pass

- **No waits:** every DONE WHEN is driven on demand (FWD-1, 4, 5 and 7 EXERCISED on demand; FWD-2, 3 and 6 APPLIED reads).
- **FWD-1 has a positive control:** the same reader is run against Schwab for the same date.
- **C-SCHEMA imports the Schwab pin from one source, never a copy, and never alters the Schwab silver.** This is consistent with Andrew's
  "formulated the exact same way".
- **C-GOLD:** gold is by configuration, with no master table presumed; this is Andrew's ~15:38Z word. Its home is per firm by R7. Unattributed
  accounts are listed and placed in no firm. This is consistent with the NFRA_FIDUPL verdicts @bc07810172 and @6e5e420536.
- **C-NATIVE-ID and FWD-7:** attribution comes from the custodian's own id, never from a vendor; this is Andrew's ~15:35Z word.
- **C-NAMES:** each address and name is quoted as builder output, measured.

## Nit, not a ground

- C-EXT's sidecar name pattern `fidx_<fact_table>` is a typed convention. Under C-NAMES and rule 30 it should be builder output, or a
  registry row, at the map cell. The contract already routes the proposal through a Rule 24 record, so name the builder there too.

## Re-delivery

Re-deliver after Andrew confirms. If the confirmed ENDPOINT is the record's block re-pasted verbatim and FWD-2 names unrealized gain/loss,
this half is signed on that delivery, with only the changed lines re-read.

-- 3.0.0_SA_CVO~DELL1
