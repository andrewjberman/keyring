# MDPF_SECCLASS -- FAST interval remediations

<sweep_watermark>2026-10-02T02:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-02 ~02:1xZ. Graduated at this compile (ADJUDICATION_v5.md): 2 rows, S7 (ARMED) and S8 (INERT); neither is closed. S6 is dismissed into MDPF_SECCLASS-W10-S3 (REMEDIATION_v4, OPEN). Carried unchanged: every row of REMEDIATION_v1 to v4 that is not closed. Rounds read v7: the project is FAST and its next list is built directly (STATUS.md).

```json
[
  {
    "id": "MDPF_SECCLASS-S7",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The Holdings fallback's NAME_ALIAS layer serves a bd-securities row keyed by a fund's NAME as that fund's class. Most of those rows are model output: some are low-confidence and some are flagged for review, yet they are served as classes on the Holdings tab at all three firms. The same kind of answer is withheld from the canonical table (rulings batch 75 item 3). CEMIX was one case and now has a canonical seed row; the population is unchanged.",
    "evidence": [
      "Scan of bd-securities, ConsistentRead, every page (this seat, 2026-10-02 02:0xZ): 10,929 rows scanned; 7,108 NAME:: rows (gpt-4o-mini 4,226, gpt-5.4-mini 1,988, coo-manual-2026-03-23 894); 2,118 with confidence under 0.80; 706 with needs_review true. Every figure equals the investigation row's.",
      "The CEMIX name row reads asset_class fixed_income, classified_by gpt-4o-mini, confidence 0.6, needs_review true; etf-classifications CEMIX reads asset_class equity, classified_by seed, instrument_kind fund (a canonical row now answers before the fallback). Control: an absent ticker reads ABSENT.",
      "investigation row MDPF_SECCLASS-S7 (2.0.0_SA_COO~M): dollars served through NAME_ALIAS by firm in the 2026-10-01 00:51Z-01:00Z local Holdings builds (Cottonwood 819 of 15,354 nodes, 57,346,152.60 USD), made before the CEMIX row; not re-measured here"
    ],
    "remedy": "P1, two parts. (1) Per symbol: a canonical row answers before the fallback, as CEMIX's now does; which low-confidence or review-flagged name rows get one first is 1.0.0_SA_CTO's to order on the next list, weighted by served dollars. (2) The population: FWD-5's retirement of bd-securities. Disarmed when no low-confidence or review-flagged NAME:: row answers a served position, read on a Holdings build after the act; the Black Diamond gold readers (C_06, D_03, D_04), which the investigation row did not measure, are read in the same pass.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v7"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-S8",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The canonical table puts real-estate funds in two classes: seed rows VNQ and VNQI and model rows USRT and CSRSX read alternatives, while the scheduled row REET reads equity, copied from its bd-securities input. Single REIT stocks AMT and PLD are scheduled rows reading equity. The contract does not require one kind of fund to share one class, so no rule is broken, but the Holdings tab shows two REIT ETFs in two classes.",
    "evidence": [
      "batch-get-item on etf-classifications, ConsistentRead (this seat, 2026-10-02 02:1xZ), 7 of 8 keys returned: VNQ alternatives (seed, fund); VNQI alternatives (seed, fund); REET equity (scheduled, no instrument_kind); USRT alternatives (model); CSRSX alternatives (model); AMT equity (scheduled); PLD equity (scheduled); O absent (the model answer withheld, addendum 2 set c)",
      "investigation row MDPF_SECCLASS-S8 (2.0.0_SA_COO~M) and the CTO half on MODEL_ROWS addendum 2 @000b55fc4b, item 3: 'one row for the round (owner 2.0.0_SA_COO~M), not part of this act'"
    ],
    "remedy": "P2: one seed row for REET (seed always wins). That moves a served class, so it needs its own never-widen half, with the holders of REET and their dollars printed in the request (not measured by anyone yet). Whether single REIT stocks (AMT, PLD, O) are equity or alternatives is a product decision that the seed source does not record; it is placed with 1.0.0_SA_CTO, and with Andrew if the CTO rules it a product call.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v7"
    },
    "closed": false
  }
]
```
