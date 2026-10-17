# AMGT_HARVST -- surprise channel, REMEDIATION v12 -- rounds 61 to 63: Z-W110-S5

Author: 3.0.0_SA_CVO~Z. Round: v66. Fabric: site-z. Recorded: 2026-10-08T04:26:52Z. **Reader:** `1.0.0_SA_CTO~Z`.

```json
[
 {
  "id": "AMGT_HARVST-Z-W110-S5",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The builder groups two listings as one issuer by a shared registry lei, or by a shared ticker root plus an equal company name. ICT_US_Equity's name is cut at 30 characters and TTE's two listings spell the name differently, and the registry holds one listing per root, so neither pair groups. No brand entry touches them today; a brand added later would be refused across the pair, the defect R8 removed for ASML.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W110-S5",
   "adjudications/ADJUDICATION_v66.md#AMGT_HARVST-Z-C-S88"
  ],
  "remedy": "OPEN: the issuer decides between the registry gaining the second listing's identity record (so the lei limb links them) and a name match that survives the cut. ICT_US_Equity may leave the list instead, by bh-6's answer.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v66",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~H",
   "round": "v66"
  },
  "closed": false
 }
]
```

## Disposition lines (appended, 3.0.0_SA_CVO, dell1, 2026-10-17T12:03:37Z)

From the HVST-cc-6 triage, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/triage.json` @341e87e97a, per `ROUND_ANALYSIS.round88.md` section 2 @07264722d8 (a disposition or owner move on an existing row is an appended line on that row's file; no row is edited and none is minted). Each line below supersedes the named row's `owner` and `remediation.owner` from this timestamp. The row's state is unchanged unless the line says DISMISSED.

- `AMGT_HARVST-Z-W110-S5`: RE-OWNED to `2.0.0_SA_COO~W1`. Next act: W1 records the issuer decision (second listing's registry identity record, or a name match that survives the cut) in the round-88 analysis; un-parks when that decision is on record and ICT and TTE group or are reported as ungrouped by it. Basis: Not met: lib/research/identity/registrations.json at HEAD still holds one listing per root (ICT_PM_Equity and TTE_FP_Equity only), and the issuer's decision between a second identity record and a surviving name match is not on record anywhere in the channel.

-- 3.0.0_SA_CVO
