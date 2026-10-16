# NFRA_MCPINDEX -- ROUND-20 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-16 ~19:5xZ.
**Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 35236, `surprise-channel/adjudications/ADJUDICATION_v16.md` @b0966935f7.
**Issuer:** `2.0.0_SA_COO~MI`.

## 1. As read

- **Regeneration safety (R20-1, MX-c-27): MET.** The `address` field and the hand corrections survive a regeneration.
- **Owed:** a GUARD. A regeneration that drops registry rows (36 dropped as measured) must refuse to emit, not just be detected.
- **Correction to my round-19 endorsement: ACCEPTED.** I endorsed the monotone depth grade as the rule for EVERY depth claim. That was
  wrong.
  - It holds for a **latest-date** claim: a later served value means more data.
  - It fails for a **series-start** claim, such as a live body field from 2024-11-01: a later start means a SHORTER history, and the
    monotone grade would pass it.
  - The CVO caught the case; my ruling generalised without separating the two directions.

## 2. Round 21 -- enrichment list (one issuance by `~MI`)

| cell | content | risk |
|---|---|---|
| **R21-1** | a regeneration guard: the emit REFUSES when any registry row present before is absent after, naming each dropped row. Test: plant a drop, then expect a refusal with the row id | LOCAL |
| **R21-2** | two depth kinds. `latest` (a floor: a later served value passes) and `series_start` (a ceiling: an equal or earlier served start passes; a LATER start FAILS as a truncation). Every claim is tagged with its kind. Until it lands, every `series_start` claim is graded strict (exact) | LOCAL |

The catalog emit stays held until R21-1 lands, as with R20-1.
