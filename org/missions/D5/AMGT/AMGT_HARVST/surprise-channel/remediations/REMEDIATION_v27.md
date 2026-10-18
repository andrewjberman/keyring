# AMGT_HARVST -- round 96 remediations (dell1)

<sweep_watermark>2026-10-18T14:31:23Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T14:31:23Z. C-S74 is the disarm row for W171-S4 and W171-S6 (the checker reads `disarms` on a new row). W173-S1 graduated at ADJUDICATION_v90 (C-S73), owner 2.0.0_SA_COO~W1.

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S74",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "W171-S4: the peers, posture, scores and filings tools kept the caller's spelling of a slash key while the prefixes held both spellings, so a raw and an encoded request read different sets. W171-S6: harvest_security_coverage differed across the spellings in its path-component templates. Release 922ee425fe (HVST-ck-3, 14:07:06Z) reads the union of the canonical and legacy raw prefix, canonical winning a name collision.",
    "evidence": [
      "adjudication row AMGT_HARVST-D1-C-S72 (ADJUDICATION_v90)",
      "investigation row AMGT_HARVST-D1-S61",
      "remediation rows AMGT_HARVST-D1-W171-S4, AMGT_HARVST-D1-W171-S6 (REMEDIATION_v26)",
      "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND96_L8_PACKET_20261018.md @4f9eefc804 (sha256 88f17277...)"
    ],
    "remedy": "None further for the readers: the union read is live, and a raw and an encoded request read the same objects on each tool. Close when: this seat's served read shows one record per name for both spellings, which is met (ADJUDICATION_v90 C-S72).",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v96",
    "disarms": [
      "AMGT_HARVST-D1-W171-S4",
      "AMGT_HARVST-D1-W171-S6"
    ],
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~W1",
      "at": "2026-10-18T14:07:06Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v96"
    },
    "closed": true
  },
  {
    "id": "AMGT_HARVST-D1-W173-S1",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The pull_enqueue Lambda (infra/aws/lambda/research/pull_enqueue/lambda_function.py:129) writes packs/{sec_key}/status.json with the raw security key, no slash_safe_key; its consumer reads the canonical spelling, so a slash ticker's REQUESTED status would be stranded. It is the only raw writer of 16.",
    "evidence": [
      "investigation rows AMGT_HARVST-D1-W173-S1, AMGT_HARVST-D1-W173-S3",
      "adjudication row AMGT_HARVST-D1-C-S73 (ADJUDICATION_v90)"
    ],
    "remedy": "The Lambda writes the canonical spelling: the slash-key rule is carried into its zip or the key is built from the crosswalk rule, deployed by Terraform only under its own pair. Close when: the writer census reads raw_writers=0, and a dry enqueue of BP/_LN_Equity writes packs/BP-SLASH-_LN_Equity/status.json.",
    "owner": "2.0.0_SA_COO~W1",
    "round": "v96",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~W1",
      "round": "v96"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
