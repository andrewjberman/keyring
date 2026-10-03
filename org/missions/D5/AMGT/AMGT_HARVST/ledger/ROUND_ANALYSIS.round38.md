# AMGT_HARVST -- ROUND 38 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-02 ~23:3xZ

**Input:** CVO slug msg 28797, `surprise-channel/adjudications/ADJUDICATION_v50.md` @8f911c0199 (precondition MET).

## 1. WHAT THE ROUND DELIVERED

- **The ft quarantine is served** (gold rebuild #6, STRICT; pair COO @42aedf5638 / CTO @5eb4e11b3d; act @a85ebb6161).
  - CVO~Z read it from S3: 23,691 -> 22,765 rows, ft 926 -> 0, the other four publishers unchanged, tone columns NULL.
  - BA 07-28 now serves 3 sa rows.
- **ak-1** (the FinBERT module, fixed sentences only) and **ak-2** (code, planted tone) merged with no served write. FWD-16 and FWD-17
  are HELD on the publisher-terms card.
- **The reconciliation** (CVO~Z REMEDIATION_v5 @41be202aa5, on the row-gate fix @9734005635) took ARMED from 49 to 10. This round
  takes it from 10 to 2:
  - 8 were advanced on COO~H's evidence (7 fix commits on HEAD, 2 claims read);
  - **Z-S11 is FIXED in the checker** (@9edfeae04d: invocations compared in their decoded, runnable form);
  - Z-W91-S10 goes to round 39.

**Round 38 is CLOSED.**

## 2. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **Z-S67: FinBERT keyed to silver's `record_hash`, which hashes `run_stamp`** | **Key the score to a CONTENT hash of the exact text scored.** PRD v0.17 amends FWD-16; the CVO re-sign is owed. | Otherwise every re-silvering re-scores an unchanged article, which contradicts FWD-16's "an unchanged one never is". It is fixed now, while FWD-16 is held, so it cannot resume wrong. |
| 2 | **Z-S11** | **DISARMED** by @9edfeae04d. | Owned by this seat as the checker's owner. |
| 3 | **What is HELD, and why** | FWD-16, FWD-17 and the event rebuild (ak-3) stay HELD on `CARD_HARVST_PUBLISHER_TERMS_20261002.md` @8d20bc24c8, open at Andrew. No round-39 cell processes publisher text. | The five publishers' terms, read verbatim. |

## 3. ENRICHMENT LIST (round 39, ONE issuance by `2.0.0_SA_COO~H`)

1. **Z-W91-S10:** a LOCAL cell, as placed.
2. **The FWD-16 content-hash key** (ruling 1): the code change and its plant (an unchanged article re-silvered keeps its key; a
   changed body gets a new one). It is built but NOT run on publisher text while the card is open.
3. **Nothing else is cuttable** until Andrew answers the card, or the FT licence quote, which would re-open the ft limb.
