# AMGT_RESAPP -- round 119 remediations (dell1)

<sweep_watermark>2026-10-18T13:31:39Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T13:31:39Z. Graduated at ADJUDICATION_v158 (C-S197): 3 rows, owner 2.0.0_SA_COO~R1; 1 ARMED, disarm owned by 2.0.0_SA_COO~R1.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W518-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The management reader classes a null ceo_public_profile as UNREADABLE_OBJECT ('the object is not a dict'), so six of eight names carry a 'could not be read' state for a profile that was never written; the export and PDF no longer print it, but the served label stays in the management object for any other consumer.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W518-S2",
      "adjudication row AMGT_RESAPP-D1-C-S197 (ADJUDICATION_v158)"
    ],
    "remedy": "The reader gives a null profile its own state (not written), distinct from an unreadable object. Close when: the eight names' served ceo_profile_reading reads the not-written state where the profile is null, and a census of the consumers of that label names each one.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v119",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v119"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-18T16:12:11Z"
    }
  },
  {
    "id": "AMGT_RESAPP-D1-W518-S3",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The rich export's no-bio fallback does not see a served drafted ceo_bio the PDF prints, so a name with management not SERVED and a served bio prints the no-bio sentence in the export and the bio in the PDF (none of the eight reaches the state).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W518-S3",
      "adjudication row AMGT_RESAPP-D1-C-S197 (ADJUDICATION_v158)"
    ],
    "remedy": "The export's fallback reads the same served bio the PDF reads. Close when: a unit control with management not SERVED and a served ceo_bio prints the bio on both routes.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v119",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v119"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-W519-S5",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A figure with no served source prints a bare '?' as its source in the pack's appendix (render_figure_line's fallback), which the token rule keeps as plain words.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W519-S5",
      "adjudication row AMGT_RESAPP-D1-C-S197 (ADJUDICATION_v158)"
    ],
    "remedy": "An absent source prints a fixed plain sentence. Close when: a unit control with no served source prints the fixed sentence and no bare '?', and the 101-name live leak scan still reads clean.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v119",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v119"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO
