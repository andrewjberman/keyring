# ANDREW-DIRECT 2026-09-22 ~13:5xZ -- AMGT_RESAPP: a single-sample trial, Lenovo through the ENTIRE pipeline

**Where:** the `1.0.0_SA_CTO~Z` terminal (site Z).

**Extends:**
- @`78106b9cea` ("I will deliver a list which will be our starting backfill list"). This is its first member, and the
  trial the structure is built on.
- @`6f1a72e4be` (composite FIGI for research; the data quota binds).

## VERBATIM

> "Let's try one sample first, let's run Lenovo through the entire pipeline. Let's do every single thing for Lenovo
> and use that as the trial."

## WHAT IT RULES (the narrow reading, stated as such)

1. **The trial scope is ONE security: Lenovo Group, `992_HK_Equity`** (Hong Kong listing; reports in USD; fiscal year
   ends 31 March). Nothing else is pulled or run under this word.
2. **"The entire pipeline" / "every single thing"** means every channel in the field map @`3a0b3cadaa`, for every page
   component in scope: Lead Panel, Thesis, Exec Mgmt, Peers and Model. Posture stays out, per @`78106b9cea`.
   The trial runs each layer: identity/key -> bronze -> silver -> the served page.
3. **Vendor egress: this seat reads the word as the explicit per-use word, for Lenovo only, for one pass per channel.**
   The caps are this seat's, stated so Andrew can object:

   | channel | cap |
   |---|---|
   | Bloomberg Terminal | one unique security; the pipeline's existing field sets plus the identity fields (FIGI family, ISIN, SEDOL, LEI) |
   | HKEX / issuer site | the battery crawl, at most 40 pages |
   | Seeking Alpha | the ADR line only, at most 10 calls |
   | Lusha | at most 10 credits |
   | Bright Data SERP | at most 3 queries |
   | Bright Data social | at most 1 dataset job of the smallest size |
   | Publications harvester | 1 run for Lenovo |

   A channel whose cost is not knowable in advance runs only with its cost printed first.
4. **The backfill holds** (@`2a192b6e07`, @`5c20841dd1`) are MET FOR LENOVO ONLY by this word. His list is Lenovo, the
   key is composite FIGI for research, and the channel inventory is the field map. They stand for every other security.
5. **The trial is the design basis.** What Lenovo breaks sets the structure: key, fiscal-year pairing,
   currency/units, language, and per-component contracts.

## WHAT EXISTS FOR LENOVO TODAY (measured, `opal-data-harvest`, 19 of 1,780 objects)

| present | missing |
|---|---|
| Bloomberg refdata + histdata bronze (09-16) | identity (no FIGI) |
| 3 served model blocks | bestdata (no forecasts) |
| peers/v1 (5 versions) | exec officers |
| scores | management/v1 (no Exec Mgmt page data at all) |
| posture | any filing (the `filing_attempt` reads UNRESOLVED-SOURCE; Lenovo is not an SEC filer) |
| | Seeking Alpha |
| | Lusha |
| | SERP |
| | publications |
| | social |

## ACTS

- This record, committed; broadcast the same turn.
- `1.0.0_SA_CTO~Z` writes the trial into the PRD (v0.22) as the validation scope, with the order, the caps and the
  preconditions, for L4-R sign-off. `2.0.0_SA_COO~Z` then cuts the trial round. The preconditions are:
  - the identity pull first;
  - the fiscal-year join wired;
  - the Z-S221 language fix before any non-US filing analysis;
  - currency (a USD reporter listed in HKD).

-- `1.0.0_SA_CTO~Z`
