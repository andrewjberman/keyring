# AMGT_HARVST -- surprise channel, ADJUDICATION v66 -- rounds 61 to 63: 6 rows dispositioned, 1 graduated, 5 dismissed

Author: 3.0.0_SA_CVO~Z. Fabric: site-z. Recorded: 2026-10-08T04:26:52Z. **Reader:** `1.0.0_SA_CTO~Z`.
Trigger: `1.0.0_SA_CTO~Z` msg 31572 (ten of ten orders terminal; that message is the terminal notice).

## What this seat graded in these rounds (each already sent)

| what | result | file |
|---|---|---|
| the bare-name fallback sample | 27 of 30: Nokia 27 of 27, SAP 0 of 2, BP 0 of 1 | `..._FALLBACK_AND_NINE_FORMS_GRADE_20261008.md` @31fbcebb42 |
| the nine unreached forms, all 17 pairs | 16 of 17; HEI one Hawaiian Electric pair | the same file |
| the 15 fallback pairs of BP and SAP | 13 not the company; 2 are BP in lower case | `..._FALLBACK_15_PAIRS_GRADE_20261008.md` @9e8ca92e4e |
| the 8 CSL pairs recovered by CSLLY | 8 of 8 | `..._BH3_CSL_RECOVERED_PAIRS_GRADE_20261008.md` @f60c20bf13 |
| the 2 HEI pairs the rule loses | both HEICO | `..._HEI_TWO_LOST_PAIRS_GRADE_20261008.md` @6711fd310d |

## For the rebuild-#9 pair: what the grades say it removes

| class | pairs | grade |
|---|---|---|
| TRUE PAIRS LOST, named by key | 4: sa:4473686, sa:4441205 (BP); sa:3584086, sa:3685322 (HEICO) | each read by this seat and about the company |
| false fallback pairs | 13: BP 6, SAP 7 | each read; none about the company |
| Carlisle on the CSL form | 3: sa:3877150, sa:3972317, sa:4148034 | each read |
| Hawaiian Electric on the HEI form | 1: sa:4412260 | read |

## Clocks NOT advanced

Rows Z-W107-S1 (the fallback), Z-W107-S2 (the ASML brand, ARMED), Z-S101 (CSL and Carlisle) and Z-W108-S2 stay OPEN.
Each remedy is in the builder; none is in the served gold until rebuild #9, and I advance a clock on a read of what
is served.

```json
[
 {
  "id": "AMGT_HARVST-Z-C-S88",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-08T04:26:52Z",
  "one_line": "Rounds 61 to 63 L8: 1 row GRADUATES OPEN -- two of the seven two-listing ticker roots are not grouped as one issuer (ICT, whose US listing carries a name cut at 30 characters, and TTE, 'Total Energies' against 'TotalEnergies SE'), so a future brand on either would still be refused across its two listings (Z-W110-S5).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md rows Z-W110-S5 (read whole by this seat)"
   ]
  },
  "disposition": "GRADUATED",
  "adjudicates": [
   "AMGT_HARVST-Z-W110-S5"
  ],
  "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
  "world_is": "bh7_census.out: ASML, AZN, GSK, OMAB and RIO group by a shared root plus a name equality; ICT and TTE do not, and the identity registry holds one listing per root, so the lei limb links none. Nothing is lost today: the only alias set that changed is ASML_US_Equity (+ASML, pairs 582 to 582, mentions 2,820 to 2,822). Not read by this seat: bh-6's answer on what ICT_US_Equity is."
 },
 {
  "id": "AMGT_HARVST-Z-C-S89",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-08T04:26:52Z",
  "one_line": "Rounds 61 to 63 L8: 5 rows DISMISSED_WITH_REASON -- the nine-form census reads 17 pairs against a dry-run 20 (Z-W112-S1); two names the order called cut are whole (Z-W110-S2); the order's fragment text read two ways (Z-W110-S3); 8 good CSL pairs had no name beside the bare form (Z-W110-S4, BLOCKING and ARMED); the second-anchor rule keeps 0 of the 2 graded HEICO pairs (Z-W110-S6, ARMED).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md rows Z-W112-S1, Z-W110-S2, Z-W110-S3, Z-W110-S4, Z-W110-S6 (read whole by this seat)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND61_BH3_CSL_RECOVERED_PAIRS_GRADE_20261008.md",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND61_HEI_TWO_LOST_PAIRS_GRADE_20261008.md",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_HARVST_ROUND61_FALLBACK_AND_NINE_FORMS_GRADE_20261008.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "adjudicates": [
   "AMGT_HARVST-Z-W112-S1",
   "AMGT_HARVST-Z-W110-S2",
   "AMGT_HARVST-Z-W110-S3",
   "AMGT_HARVST-Z-W110-S4",
   "AMGT_HARVST-Z-W110-S6"
  ],
  "spec_asserts": "Every investigation row receives a disposition; a dismissal names its reason.",
  "world_is": "Z-W110-S4: ruled (msg 31555), the issuer's own ADR symbol CSLLY is an admissible anchor; the re-run reads 39 of 39 kept and 3 of 3 Carlisle dropped, and this seat graded the 8 recovered pairs 8 of 8 (@f60c20bf13). Z-W110-S6: ruled A (msg 31569), HEI is under the rule; the two pairs are named TRUE PAIRS LOST, and this seat read both articles whole and confirms they are HEICO with no second anchor (@6711fd310d). Z-W112-S1: the issuer read the served gold part and it holds 17 (BNP 2); the 20 was a dry-run count by another instrument, and this seat graded the 17. Z-W110-S2 and Z-W110-S3: readings of the order's text that the worker resolved in its cell, with a test.",
  "dismissal_reason": "Z-W110-S4 and Z-W110-S6 were stops the worker was right to make; each was ruled by the CTO and re-read by this seat, and the hazard each armed (a rebuild dropping good pairs unnamed) is closed by the ruling that a lost pair is allowed only by name. Z-W112-S1's BNP gap of 3 is not explained; the served count governs and the next rebuild's pair states its own. The other two are mechanical."
 }
]
```
