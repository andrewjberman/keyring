# TCKT_MTADTA -- round 1 remediations (dell1)

<sweep_watermark>2026-10-16T07:43:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T07:43:20Z. Graduated at ADJUDICATION_v1 (C-S2): 6 rows.

```json
[
  {
    "id": "TCKT_MTADTA-D1-S5",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The collector role invokes the door by its own identity policy; C-ACCESS (1) says only group members may invoke.",
    "evidence": [
      "investigation row TCKT_MTADTA-D1-S5",
      "adjudication row TCKT_MTADTA-D1-C-S2 (ADJUDICATION_v1)"
    ],
    "remedy": "The PRD names the collector role as the one non-member invoker, with the ops it may call, or the collector writes another way, and the door refuses any other non-member caller. Close when: this seat reads the PRD row and the built root agreeing.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    }
  },
  {
    "id": "TCKT_MTADTA-D1-S2",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C-POPULATION resolves actors against object ids, which need a Graph permission that C-APP does not grant; round 1 resolves by the UPN fields only.",
    "evidence": [
      "investigation row TCKT_MTADTA-D1-S2",
      "adjudication row TCKT_MTADTA-D1-C-S2 (ADJUDICATION_v1)"
    ],
    "remedy": "The PRD says UPN-only resolution, or C-APP adds the one directory read with its cost stated. Close when: the PRD text and the collector agree.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "TCKT_MTADTA-D1-S4",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The bucket policy denies s3:ListBucket to all but the access role; the Terraform bucket refresh needs it, so later plans may 403.",
    "evidence": [
      "investigation row TCKT_MTADTA-D1-S4",
      "adjudication row TCKT_MTADTA-D1-C-S2 (ADJUDICATION_v1)"
    ],
    "remedy": "Before release act 1: an apply order that keeps the policy fixable (for example the applying identity admitted for ListBucket only, named in C-RESIDUAL), proven by a plan after the policy lands. Close when: this seat reads that plan.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    }
  },
  {
    "id": "TCKT_MTADTA-D1-W3-S2",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "collect.py, collector.tf and handler.py carry literal keys and names in place of builder output.",
    "evidence": [
      "investigation row TCKT_MTADTA-D1-W3-S2",
      "adjudication row TCKT_MTADTA-D1-C-S2 (ADJUDICATION_v1)"
    ],
    "remedy": "Replace them with lib/opal_naming output now that the registry rows exist. Close when: the naming gate passes them at the merged pin.",
    "owner": "2.0.0_SA_COO~S1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~S1",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~S1",
      "at": null
    }
  },
  {
    "id": "TCKT_MTADTA-D1-W3-S3",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "One coverage object per day, overwritten by each hourly fire, so an earlier fire's GAP is lost.",
    "evidence": [
      "investigation row TCKT_MTADTA-D1-W3-S3",
      "adjudication row TCKT_MTADTA-D1-C-S2 (ADJUDICATION_v1)"
    ],
    "remedy": "Coverage per fire (or cumulative), so a gap stays visible (FWD-9). Close when: a planted gap survives the next fire.",
    "owner": "2.0.0_SA_COO~S1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~S1",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~S1",
      "at": null
    }
  },
  {
    "id": "TCKT_MTADTA-D1-W3-S5",
    "project": "TCKT_MTADTA",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Fire counts are attributed to the window's end day because blob ids carry no time.",
    "evidence": [
      "investigation row TCKT_MTADTA-D1-W3-S5",
      "adjudication row TCKT_MTADTA-D1-C-S2 (ADJUDICATION_v1)"
    ],
    "remedy": "Attribute by each event's own time. Close when: a two-day window's counts split correctly on a planted case.",
    "owner": "2.0.0_SA_COO~S1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~S1",
      "round": "v1"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
