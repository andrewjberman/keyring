# ETFS_RIVALS -- round 8 remediations (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-05 ~17:00Z. Graduated at round 8's L9 (`adjudications/ADJUDICATION_v8.Z.md`).

Round 8 is drained and applied:
- 11 of 11 orders are terminal;
- LIVE at b166e04416;
- the ledger is CLOSED 6/6.

This slug covers the whole project and carries no sweep watermark. Five items graduate: S24 (ARMED), S25, S29 (a CTO call),
C-S35 and C-S36. The slug goes to `1.0.0_SA_CTO~Z` with the review
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R8_REVIEW_20261005.md`. W1-S46 (REMEDIATION_v7) is REMEDIATED in place.

```json
[
  {
    "id": "ETFS_RIVALS-Z-S24",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Bloomberg's daily capacity on the Terminal is a shared, finite budget. The D12/D13 backfill can spend all of it overnight, and every BQL and refdata consumer on the Terminal then fails for the rest of the day: the 07:00 ET vehicle leg, the OPAL_BBGTML models pull, and the enrichment that fed the empty G4 (S25). Nothing in the backfill plan or in READ_HERE.md bounds that spend.",
    "evidence": [
      "investigation rows ETFS_RIVALS-Z-S24, S25",
      "10-05 12:33:12Z capture: '#N/A Daily Capacity, request is blocked.' for 9 of 9 funds",
      "round8/BACKFILL_D12_PLAN.md (no capacity clause)"
    ],
    "remedy": "A capacity-aware backfill: a per-day slice budget that leaves the production pulls their share, and a stop on the first capacity error rather than a retry. Record the limit in integrations/bloomberg/READ_HERE.md. Proof: the first backfill night after the change is followed by a 07:00 ET vehicle pull with no capacity error, read from that pull's capture.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v8"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~RV",
      "at": null
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-S25",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Enrichment writes whatever the vendor returns as the newest G4 revision, so a capacity-blocked pull landed 601 rows with 0 prices, 0 GICS and 0 names as the 10-02 G4, which every reader then took as current. The restore (remedy 2) is done; the guard (remedy 3) is not built.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S25",
      "round8/NEVER_WIDEN_HALF_COO_G4_1002_REPUT.md @988544c80c"
    ],
    "remedy": "Enrichment refuses to land a G4 revision whose fields are all errors or all empty: it keeps the prior revision and records the refusal. Proof: a planted all-error vendor response leaves the served G4 key unchanged and records the refusal.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-S29",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "D12 Step B's import chain re-derives G5 for every fund on 189 dates with current code, so a step scoped to new names would rewrite every other fund's served trade schedule. Step B is held at the CTO's stop condition.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S29 (6a9aa4fa9e)",
      "CTO~Z msg 29594 (Step B condition)"
    ],
    "remedy": "A CTO call between (A) accepting a G5 replay of all funds as part of Step B, under a never-widen sign-off that names that blast radius, and (B) a round-9 cell in which the trade schedule rebuilds only the named funds and carries every other fund's G5 forward unchanged.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-C-S35",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "fc-1's linker leaves most security names in the AI text as plain text: 395 mentions of 43 names that have a modal, against 253 linked, on the served r8b page. Four names are linked in one account and plain in another. One name shared by two keys (Taiwan Semiconductor Manufacturing Co Ltd: 2330_TT_Equity and TSM_US_Equity) is left as an unlinked span. The rankings, trend and trade log are fully linked.",
    "evidence": [
      "adjudications/ADJUDICATION_v8.Z.md ETFS_RIVALS-Z-C-S35",
      "this seat's playwright measure over the served r8b page"
    ],
    "remedy": "Every whole-word occurrence of a page display name in the AI faces and dialogs becomes the security's button. An ambiguous name links to the key the account's citation names, or reads with both identifiers. Proof: the served page's count of plain AI-text mentions of a modal-bearing name reads 0. The latest-holdings table's 334 plain mentions are a scope call for the issuer.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v8",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v8"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-C-S36",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "22 holdings on the served page are still named by their raw Bloomberg ticker form ('ATD CN Equity', 'MSCI US Equity', '8053 JP Equity'), on the face and in their modal headings. The LONG_COMP_NAME names expected with the 2026-10-05 vehicle run did not reach them, and no round-8 cell carried ui-5's residue.",
    "evidence": [
      "adjudications/ADJUDICATION_v7.Z.md ETFS_RIVALS-Z-C-S28",
      "adjudications/ADJUDICATION_v8.Z.md ETFS_RIVALS-Z-C-S36"
    ],
    "remedy": "Find why the names hookup misses these 22 keys (vehicle coverage, Bloomberg capacity on 10-05, or the name map's key space) and name them in words. Proof: the served page's count of holdings named by a '<id> XX Equity' form reads 0, or each remaining one is named with its reason.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v8"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~RV
