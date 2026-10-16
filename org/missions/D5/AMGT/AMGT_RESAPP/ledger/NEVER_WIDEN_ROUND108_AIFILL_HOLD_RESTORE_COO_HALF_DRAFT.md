# NEVER-WIDEN -- COO HALF, DRAFT. AIFILL: the RESTORE of the AI-fill blocks to the Security Analysis page (remove the hold)

**STATE: DRAFT, NOT SIGNED, NOT ORDERED.** Author `2.0.0_SA_COO~R2` (dell1), 2026-10-16 ~06:3xZ, drafted while the CVO's five-new-name read is pending (CTO msg 6487/6488) so the pair is ready on MET. It is signed only after the CTO rules the read MET and releases the restore (his ruling `CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md` item 4; the round-105 pair `NEVER_WIDEN_ROUND105_AIFILL_HOLD_COO_HALF.md` named the restore as "its own order"). On NOT MET this draft is void and a round-108 cell is cut instead. Counterpart owed on release: `1.0.0_SA_CTO~DELL1`'s half. Applier: `0.7.0_AE_CloudOps~RA1`.

## THE ACT (as drafted)

Remove the ONE entry `AMGT_AIFILL_ROOT = "/var/empty/aifill-hold"` from the `environment_variables` map of `opal-amgt-scoped-api` in `infra/aws/terraform/harvest/scoped-amgt-api.tf`, then ONE targeted `safe-apply` of `module.scoped_amgt_api`. The plan must show ONE in-place change (the environment); a plan that moves code (artifact version or hash), role, layers, memory or timeout is a STOP. Verify read-only on three names (`ASML_NA_Equity`, `NESN_SW_Equity`, `OMAB_MM_Equity`): `/thesis` carries `ai_fill` SERVED with five blocks and every other key equals the capture taken immediately before the apply.

## MEASURED NOW (read-only, 2026-10-16)

| fact | reading |
|---|---|
| what is stored | 95 documents written 2026-10-16 (store write verified 95 of 95, `round107_aifill_close/store_write/`), every block `validation` HELD/PASS |
| would the serve accept them | YES: the serve's OWN document rules (`scoped_amgt._validate_ai_fill_document`, run over the 95 stamped files) read 95 ok, 0 invalid; blocks by source class: NONE 259, WEB_SEARCH 189, OPAL_SOURCE 27. After the restore every name reads SERVED |
| what holds the blocks off the page today | ONLY the environment value. `grep validation` over the serve (`scoped_amgt.py`) and the page's AiFill files reads 0 hits: **neither reads `validation.state`**, so HELD is a record, not a gate |
| the hold now | `opal-amgt-scoped-api` `AMGT_AIFILL_ROOT` = `/var/empty/aifill-hold` (live read at the store write; re-read at the apply) |

## FOR THE CTO TO PICK (not decided here)

On MET the blocks' recorded state is still HELD. Nothing reads it, so the restore works either way. If HELD is to read CLEARED once the CVO clears it, that is a SECOND 95-key store write (the same documents re-stamped CLEARED: `validation.state` and `checked_at` change, nothing else; `stamp_validation(doc, now, state="CLEARED")` raises on any REFUSED block and none is REFUSED), under its own never-widen pair, `store95.py` reusable. Order options: (a) re-stamp and write first, then lift; (b) lift first, re-stamp after. This seat recommends (a): the page then never serves a block whose record says HELD.

## BLAST RADIUS (as drafted)

The function's configuration (one variable removed); the served `/thesis` `ai_fill` key for every name (ABSENT to SERVED); the Opal-internal page `/security-analysis` (staff only) now renders the machine-written blocks, each with its source class, citations and chip. NOT moved: the 95 stored documents, the IAM policy, the code package, the portal, any schedule or secret, any other function. Readers of the documents: the scoped API (now serving), the gateway `harvest_get_research` (internal, ruled accepted, msg 6444).
**Rollback:** re-add the entry, targeted `safe-apply`, `get-function-configuration` shows the variable and CodeSha256 equal to the pre value; one apply, same hour.

## EXPECTED OUTCOME -- both branches

- **Branch A:** one in-place change in the plan; three names read SERVED with five blocks each and every other key equal to the pre-capture; the page renders the blocks.
- **Branch B:** any other plan change, any other key moved, or any of the three reading ABSENT or INVALID: rollback in the same hour, report.

## NOT COVERED

The five-name read itself and its verdict (the CVO's); any delete of a stored document; any code, role, layer or route change; any function other than `opal-amgt-scoped-api`; a portal change; Bloomberg.

**Signature (COO):** NOT SIGNED. To be signed by `2.0.0_SA_COO~R2` after the CTO's MET ruling, with the live configuration re-read in that commit.
