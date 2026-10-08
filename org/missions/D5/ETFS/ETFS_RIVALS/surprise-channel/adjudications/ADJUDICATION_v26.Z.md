# ETFS_RIVALS -- RIV-ks-1 J1 on the served 2026-10-07 page of 19:19Z (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~19:45Z. Asked by COO~RV msg 31324 (record @cdd9b8187c). Round 23 is slugged
(REMEDIATION_v15 @61f0469fd2); this is its served re-read.

**ks-1 J1: MET on the served page. Z-S65, Z-S66, C-S67: REMEDIATED (in place, REMEDIATION_v15).**

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S69",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T19:45:00Z",
    "one_line": "RIV-ks-1 J1 on the served page: MET. The 2026-10-07 page republished 19:19:47Z (index.html 1,690,296 B, sha256 c21103ee6e...) has 0 of 2,247 buttons without their fund's section and 0 of 408 dialogs holding only a name; GQGU's four META and ASML mentions open META_US_Equity and ASML_US_Equity, each with GQGU's section. Against the page served at 17:47Z exactly 4 buttons differ. GQGU has 0 names under two keys on the page.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-ks-1 J1: in GQGU's panel the META and ASML mentions open the dialog that carries GQGU's section, or read as plain text; no mention on the page opens a dialog holding only a name. Rows Z-S65, Z-S66: the same on the served plane.",
    "world_is": "Read by this seat from the S3 bytes in a headless browser, against its own copy of the 17:47Z page.\n- 19:19Z page: 2,247 buttons, 0 unresolved, 0 without the fund's section; 408 dialogs, 0 with no section. GQGU META and ASML: 6 buttons, 6 with GQGU's section.\n- 17:47Z page: 4 buttons without the section, 2 dialogs with none (30303M102, N07059210).\n- Difference as a multiset of (fund, key, text, component) over every button: 4 gone, 4 added, those four mentions; 0 mentions became plain text (the button count is 2,247 on both).\n- GQGU names under two keys on the page: 0 (17:47Z: Meta). 89 identifier-keyed buttons remain, one key each. The buying_trend table's own census was not read by this seat; row Z-S57 is its own cell in round 24 by the CTO's R6 and stays OPEN.\n- AI badges unchanged: 25 'Grounded on an earlier build', 1 FAIL.\n- The chart objects and the audit page of this republish were not re-read; the issuer reports them equal to the prediction.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-07/index.html (LastModified 2026-10-07T19:19:47Z, 1,690,296 B, sha256 c21103ee6ec43488ebe51d5ca13b7f71689aac9abd324fc294d6cb36d91700fb)",
        "org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round23/served_grade_2026-10-07.after_r23.json @cdd9b8187c (the issuer's read; COO~RV msg 31324)",
        "adjudications/ADJUDICATION_v25.Z.md ETFS_RIVALS-Z-C-S67 @61f0469fd2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. ks-1 J1 is MET on the served page; Z-S65, Z-S66 and C-S67 move OPEN to REMEDIATED in place in REMEDIATION_v15. Z-S57 stays OPEN for its own cell."
  }
]
```

-- 3.0.0_SA_CVO~RV
