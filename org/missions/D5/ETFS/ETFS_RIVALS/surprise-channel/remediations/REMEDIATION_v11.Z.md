# ETFS_RIVALS -- rounds 11 and 12 remediations (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-06 ~18:30Z. Graduated at the round-11/12 L9 (`adjudications/ADJUDICATION_v11.Z.md`).

Round 11 is drained and applied (2 of 2 complete); round 12's RIV-au-1 is applied (5 Lambdas 39/39 at 50a2248fe9; the 10-06
republish serves). Round 12's BBGLEG (eb-1, pk-1) compiles at its own drain-end.

Two items graduate: C-S47 and S43 (C-S47 adjudicates it; S43's own row carries its remedy, pk-1). In place, REMEDIATION_v9 C-S38 moves OPEN -> REMEDIATED on dr-1. Still OPEN:
- S24: the backfill-night proof;
- C-S36: nm-3 (4 securities, 14 mentions still ticker-form on the 10-06 republish);
- W6-S2: the served replay honoured its precondition (G1 staged from 2025-12-01), but the planted mid-scope proof is not built.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S47",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A security mention links to the modal of the listing its NAME resolves to, not the listing the linking fund holds or traded. 15 of 2,073 mentions on the served 10-06 page (Nebius in WCMG x8, Alphabet Cl C in WCMG x2, SpaceX in GQGU x5) open a modal with no section for that fund. Nebius is S43's key split; Alphabet is a share-class name crossing to the other listing; SpaceX is a fresh entry whose modal gets no section because the fund has no contribution row yet.",
    "evidence": [
      "adjudications/ADJUDICATION_v11.Z.md ETFS_RIVALS-Z-C-S47",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r12_j1/census2.json (nfs)",
      "investigation row ETFS_RIVALS-Z-S43"
    ],
    "remedy": "A mention inside fund F's panel links to the key F holds or traded for that security (F's own row key first, then the name map); a fund with a trade but no contribution row still gets its modal section (the trade line). Nebius also needs pk-1 (PARSEKYABLE_DES join) so one modal carries both funds. Proof on a served page: for every data-sec button in panel F, the target modal has section[data-fund=F]; 0 of N fail, with the three named securities as the positive control.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v11",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v11"
    },
    "closed": true
  },
  {
    "id": "ETFS_RIVALS-Z-S43",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "RIV-ok-1's CUSIP/ISIN join cannot merge WCMG's Nebius row (Bloomberg key, no CUSIP/ISIN) with GQGU's CUSIP-only row, so Nebius keeps two keys and two modals. On the served 10-06 page, WCMG's 8 Nebius mentions open GQGU's CUSIP modal (C-S47).",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S43",
      "adjudications/ADJUDICATION_v11.Z.md ETFS_RIVALS-Z-C-S47",
      "deliverables/2.0.0_SA_COO~RV/round12_prep/pk-1.AC1.draft.py (FAIL 2 at base, control PASS)"
    ],
    "remedy": "CTO ruling (A) @982e914b1d: the G4 reference request asks PARSEKYABLE_DES for identifier-keyed securities and the one-key join reads it (RIV-pk-1). Proof: pk-1.AC1 PASS, then on a served page WCMG's and GQGU's Nebius mentions open one modal carrying both funds.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v11",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v11"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~RV
