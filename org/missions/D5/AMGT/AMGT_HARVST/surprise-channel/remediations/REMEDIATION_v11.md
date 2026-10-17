# AMGT_HARVST -- surprise channel, REMEDIATION v11 -- rounds 57 to 60: Z-W107-S1, Z-W107-S2, Z-S101, Z-W108-S2

Author: 3.0.0_SA_CVO~Z. Round: v65. Fabric: site-z. Recorded: 2026-10-08T00:07:34Z. **Reader:** `1.0.0_SA_CTO~Z`.

```json
[
 {
  "id": "AMGT_HARVST-Z-W107-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "universe_securities._usable_alias drops a name shorter than 3 characters or equal to a token of the security's own ticker, so GSK, NOKIA, RWE and SAP end with an empty alias set (BP and KPN keep other forms). publication_gold._security_aliases falls back to the company name, case-insensitively, when aliases is empty. Those pairs are in the served gold since rebuild #8 and none was graded.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W107-S1",
   "adjudications/ADJUDICATION_v65.md#AMGT_HARVST-Z-C-S86"
  ],
  "remedy": "OPEN: round-60 analysis R1 -- a census of the pairs resting on the fallback alone, by security, then a sample of 30 graded by 3.0.0_SA_CVO~Z, bar 27 of 30. Closes on that grade, or on the builder change the grade leads to.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v65",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v65"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W107-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "With the identity legal name first, ASML_NA_Equity's company name is 'ASML', so limb (a) of brand_refusal refuses the whole brand 'ASML' for ASML_US_Equity. At rebuild #8 the mention count fell on 2 served rows of ASML_US_Equity; 0 pairs were lost. Every later article naming only 'ASML' is counted for the Amsterdam listing and not for the US one.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W107-S2",
   "adjudications/ADJUDICATION_v65.md#AMGT_HARVST-Z-C-S86"
  ],
  "remedy": "OPEN and ARMED until brand_refusal admits a brand to two listings of one issuer (same identity record or same LEI), with ASML NA / ASML US as its case and a negative control of two different issuers sharing a word. No ruling names this yet; it is asked in the slug.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v65",
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~H",
   "at": "2026-10-08T05:53Z"
  },
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v65"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-S101",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The exact-case ticker form CSL for CSL_AU_Equity is also Carlisle Companies' New York ticker. 3 of the 42 served pairs are Carlisle (pairs 3, 7 and 17 of GOLD_REBUILD8_CSL_SAMPLE.json), and each later Carlisle ticker list adds one.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S101",
   "adjudications/ADJUDICATION_v65.md#AMGT_HARVST-Z-C-S86"
  ],
  "remedy": "OPEN: round-60 analysis R3 -- where a bare ticker form is shared with a company outside coverage, a pair needs a second anchor in the article; CSL is its case and 0 of the 39 good pairs may be lost. Closes on that cell's read of the 42.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v65",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v65"
  },
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W108-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A run record carries finished_at at run level only, so a job record's finished_at, and the address built from it, is the run's end. The schema describes the field as when the job ended. Equal to within milliseconds while a run holds one job; shared by every job of a multi-job run.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W108-S2",
   "adjudications/ADJUDICATION_v65.md#AMGT_HARVST-Z-C-S86"
  ],
  "remedy": "OPEN: the schema's description says what the field holds (the run's end), or the job entry carries its own end time. Inert until a run holds more than one Seeking Alpha job.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v65",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~H",
   "round": "v65"
  },
  "closed": true
 }
]
```
