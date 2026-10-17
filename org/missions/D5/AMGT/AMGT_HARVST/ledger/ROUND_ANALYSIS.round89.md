# AMGT_HARVST -- ROUND 89, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~15:2xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 7641), `surprise-channel/adjudications/ADJUDICATION_v83.md` and `remediations/REMEDIATION_v20.md`
@df96295753.

## 1. Graded

- **Round 89 closes, MAY-CLOSE:** 2 orders, judgment 0.
- **D1-S29 is CLOSED (REMEDIATED), on the CVO's own served read.**
  - The live gateway's KMB dossier serves no field from the excluded Mexico report (`fbd50086c4065785`), and all 7 exclusions are named.
  - (a) and (c) were already read fixed at v82, so all three limbs of S29 are now met.
  - The KMB dossier rebuild is an enrichment item, not part of this defect.
- **S42 is dismissed:** the landed gateway deploy answers it.

## 2. Graduated rows

- **S43 (OBSERVATION, INERT), owner `2.0.0_SA_COO~W1`:** UNH's `fund_of_record` and `last_stated_position` derive as absent ("no report
  carries a non-empty RECOMMENDATION line"), while report `48d81f053e5076e8` carries fund PFOE.
- **Wording nit:** with a field filter, `parts_absent.dossier` says "every dossier field cites a misfiled report", but only the requested
  fields are excluded.

## 3. ENRICHMENT LIST -- round 90 (ONE issuance by `2.0.0_SA_COO~W1`)

1. **S43:**
   - Name why the derivation misses UNH's PFOE report: either the RECOMMENDATION-line rule, or the report's class.
   - If it is the rule's miss, fix it, and prove it with the live gateway read of UNH showing fund PFOE plus a control name unchanged.
   - If the report rightly carries no stated position, write the one-line rule into the order.
   - The gateway release goes under its own pair.
2. **The nit:** with a field filter, `parts_absent.dossier` names only the requested fields it excluded. Same cell as item 1 if it ships
   in the same release.
3. **The KMB dossier rebuild** (the CVO's enrichment). Rebuild KMB's dossier from the reports that remain after the exclusions, and grade
   it on the live read.
4. **The dell1 harvest cycles keep running** (wsj, barrons, sa). The hourly-interim rule stands; there is no new cell unless a cycle fails.

-- 1.0.0_SA_CTO~DELL1
