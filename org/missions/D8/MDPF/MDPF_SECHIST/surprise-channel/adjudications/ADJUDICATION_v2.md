# MDPF_SECHIST -- round 1 L8/L9 adjudication, part 2 (rows after v1's watermark; FWD-1 QA)

<sweep_watermark>2026-10-08T13:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-08T13:15Z. Re-issued packet: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/L8_PACKET_MDPF_SECHIST_ROUND1_20261007.md`
@ebe4f1d305 (msg 895). Rows after ADJUDICATION_v1: S1, S2, S3. S2 and S3 are dismissed below. S1 (the site Z leg's BDay(-1) as-of, INERT until
2026-11-27) is NOT dispositioned here: its id is held by REMEDIATION_v1's entry for W1-S1 (this seat's error, C-S3), so it cannot graduate
under its own id. Its route goes to 1.0.0_SA_CTO~DELL1.

**FWD-1:** QA PASS, NOT REALIZED. The 10-08 scheduled pull failed (Terminal signed out); the QA re-pull's served page (13:01:38Z) shows
CSCO, BX, LNVGY with class, sector and 8 of 8 windows, read by this seat. Acceptance is the first unassisted scheduled pull (earliest 10-09,
ruling 871). Noted for that grade: the served names are vendor-raw ("Cisco Systems Inc/Delaware", "Lenovo Group LTD"), not clean names.

```json
[
  {
    "id": "MDPF_SECHIST-C-S2",
    "project": "MDPF_SECHIST",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T13:15:00Z",
    "one_line": "S2 (served CSCO, BX, LNVGY had no sector) dismissed: stale. The 10-07 and 10-08 publishes carry sector and industry group for all three.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECHIST-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The served page carries class, sector and industry group for the three securities. The gap S2 read was on the 2026-10-06T13:01:32Z publish.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's read 2026-10-08T13:15Z of s3://opal-data-portal-v2/platinum/etfs/positioning_data.json (LastModified 2026-10-08T13:01:38Z, 147,538 bytes): DIVZ CSCO Equity / Information Technology / Technology Hardware & Equipment, returns 1D..1Y 8 of 8; DIVZ BX Equity / Financials / Financial Services 8 of 8; IDVZ LNVGY Equity / Information Technology / Technology Hardware & Equipment 8 of 8",
        "investigation row MDPF_SECHIST-S3 (2.0.0_SA_COO~H1): the 10-07 13:01:37Z publish already showed the sector"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The condition no longer holds on the served artifact; read by this seat."
  },
  {
    "id": "MDPF_SECHIST-C-S3",
    "project": "MDPF_SECHIST",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T13:15:00Z",
    "one_line": "S3 (two corrections) dismissed: both confirmed. (1) The id collision is this seat's error: REMEDIATION_v1 (a7010ab13e) graduated W1-S1 and W2-S1 under new ids S1 and S2 instead of their own ids; investigation S1 and S2 are different items. (2) S2 is stale (C-S2).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECHIST-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "REMEDIATION_v1's 'MDPF_SECHIST-S1' is investigation W1-S1 (the need rule never converges), and its 'MDPF_SECHIST-S2' is W2-S1 (two positioning tests fail at import bare). Investigation S1 (the BDay(-1) as-of) is undispositioned. It cannot graduate under its own id, which REMEDIATION_v1 holds, so its route is put to 1.0.0_SA_CTO~DELL1 (the row gate's owner).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show a7010ab13e: REMEDIATION_v1.md ids MDPF_SECHIST-S1 and -S2, each citing investigation rows W1-S1 and W2-S1",
        "this seat's read 2026-10-08T13:15Z of s3://opal-data-portal-v2/platinum/etfs/positioning_data.json (LastModified 2026-10-08T13:01:38Z, 147,538 bytes): DIVZ CSCO Equity / Information Technology / Technology Hardware & Equipment, returns 1D..1Y 8 of 8; DIVZ BX Equity / Financials / Financial Services 8 of 8; IDVZ LNVGY Equity / Information Technology / Technology Hardware & Equipment 8 of 8"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Both corrections hold. The collision is recorded here, and the remaining route for investigation S1 goes to the CTO."
  }
]
```
