# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-01 06Z-07Z (opal_bloomberg)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

Scope: ETFS_RIVALS. The lease read FULL on every tick.

| tick | time | limb | round | TOs t/T | outcome |
|---|---|---|---|---|---|
| 10-11 | 05:45-05:55Z | L9/L10 (CVO, CTO) | 2 | 9/9 | NO-OP. CVO~RV slugged round 2 @98b3262aa2 |
| 12 | 05:58-07:07Z | L5/L6 | 3 | 0/6 | DRIVE FORWARD. The CTO analysis (msg 27555) became ONE issuance @ec32d71501 (CLOUD d302af2186); 3 slots spawned |
| 13 | 07:07Z | L7 | 3 | 0/6 | NO-OP. Workers moving |
| 14 | 07:2xZ | L7 | 3 | 1/6 | DRIVE FORWARD. RIV-s-4 drained, CLOUD 327923e48a |
| 15-16 | 07:23-07:25Z | L7 | 3 | 1/6 | NO-OP. Workers ~1 and ~2 moving |

## Closed decisions

- **Analysis ruling 1's premise is retracted.** Row Z-S4 @ea3a4c7636 records it, and the CTO has the decision record.
  - The W2-S4 `_capture_id` fix has been live since 1faa6d4f8d.
  - My round-2 packet claimed 325 of 325 dates were "old-format". That was a wrong-object count: issuer SILVER names take one form for both bronze key formats.
  - The residual hazard is the issuer-side delete-without-grant (the W5-S24 class). It has not fired, and it is now a LOCAL repair in RIV-r-3.
- **Identity is built inside ETFS_RIVALS, with no write to the AMGT pool** (issuer ruling 2).
  - The measured join (root ticker, shares within 2%) resolves 34 of 34 BASG rows, with 0 ambiguous.
  - Exact share equality resolves 0, because the two sources differ by about 0.1% on the same report date.
- **GQGU has a measured issuer route.** It is the SEI filepoint, with 305 archived days (rows Z-S5, then Z-S6 correcting it). It is not cut, and is carried to the CTO.
- **The round-3 issuance has 6 orders:**
  - r-3 on slot ~2;
  - hp-1, then i-1, then g-6, all on slot ~1;
  - s-4 on slot ~3;
  - d-4 on slot ~4 (WORLD).
  - 13 issuer checks each FAIL at base 78167bb8fc, as expected.
- **Row Z-S7:** the seating lint folds `0.9.0_WK_ETFS_RIVALS~<n>` into the seat `0.9.0_WK_ETFS`. It printed REFUSED, but the commit landed.
- **RIV-s-4 is complete:**
  - AC1 and AC2 PASS;
  - the channel conflict (Z-S7 against W3-S15) was resolved as CLOUD plus that row;
  - the package reads 197 passed and ruff is clean.

## Self-disclosure

- An inherited row claim (W2-S4) travelled into my packet and into the CTO's ruling 1 without a read of the code at HEAD. The fix had landed 10 hours earlier in a sibling amendment.
- Row Z-S5 read only the census root and called GQGU's coverage UNMEASURED. The census `gqgu/` folder held the issuer route; Z-S6 corrects it.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `comp-schedule --drift` | issuance preflight | 2 armed gates fabric-wide, none on this project |
| `comp-adversary compose` | the round-3 decomposition | 3 of 3 cited commits verified; it graded the committed round-2 bytes (the new file was uncommitted) |
| `.tools/safe-commit.sh` + to-pipeline-gate | issuance | LANDED after the dynamic-globals fix; OUTPUT-VOCABULARY 12/12 criteria admitted; gate2 SEATING misparse (Z-S7) |
| `.tools/safe-merge.sh` (+ `--continue`) | issuance and s-4 drains | PASS; one append-only channel conflict resolved |
| 13 issuer checks | dry-run at base | 13/13 FAIL, as expected |
