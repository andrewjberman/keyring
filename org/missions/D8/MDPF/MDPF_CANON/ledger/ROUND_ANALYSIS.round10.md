# MDPF_CANON -- ROUND 10, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~14:0xZ)

**Answers:** the CVO's L10 slug (msg 6729; `surprise-channel/adjudications/ADJUDICATION_v19.md` @dec32ed773). Round 10 is MAY-CLOSE, with
both orders complete.

## 1. Round 10 closes

- **CN-r-1 AC4 is MET on the first fire.** The CVO re-ran the readback at pin b6352de8f8: 11 of 11.
  - The partition and the oracle hold.
  - `carried_dates` holds the 9 no-total dates plus 0 leg gaps, and `meta.trend_groups` is intact.
- **The limit is accepted as stated:** today had no leg gap, so the carry rule ran on its negative arm only. The positive arm rests on the
  merge-time oracle (CN-p-1 arms O3-O5).
  - On real data, Dividend and Growth are never missing.
  - Where `sma_additive_aua` is missing, the served Total excludes it (amendment 1 to round 9), so the leg stays absent by rule.
  - A live positive arm has no real date to run on, and inventing a served gap to prove it would move served output for a test.
- **Record nit:** the packet's section-4 command names a non-commit pin (`b6352de843f3...`). C1/D1 correct it to b6352de8f8 in the packet
  at the next edit.

## 2. ENRICHMENT LIST -- round 11 (`2.0.0_SA_COO~D1`, ONE issuance)

These are PRD v2.23's heads, with D1's split read at HEAD (@ba8dca3ec2).

1. **CN-s-4a, the Variant 2 band repair (D1-S29, ARMED).** Non-internal Global viewers no longer double-count the carried Models band on the
   9 carried dates.
   - One criterion: the Variant 2 render's Total equals the served Total on all 9 dates.
   - It is client-facing on PROD, and it rides the next portal promote on Andrew's word: "it should get added on to the next prod promote of
     the portal" (`ANDREW_DIRECT_20261015_162xZ_DEMO_GLOBAL_TREND_USES_VARIANT1_NEXT_PROMOTE.md`).
2. **CN-s-4b, the demo session on Variant 1.** The flag plus the three internal gates and the edge firm gate D1 named, so the demo sees what
   the global view sees (the same record). It ships in the same promote.
3. **FWD-9 head (f), the Cottonwood Trend upgrade,** on the CRO spec; and **head (g), Muni as "Opal Municipal Bonds"**. D1 cuts each as a cell
   once its spec input is on file, or states which input is missing.
4. **D1-S29** disarms on item 1's PROD read. The other open rows carry on the CVO's clock.

A build order carries at most three mechanical criteria.

-- 1.0.0_SA_CTO~DELL1
