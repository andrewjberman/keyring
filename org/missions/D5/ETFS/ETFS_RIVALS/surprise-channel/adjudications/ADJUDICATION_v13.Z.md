# ETFS_RIVALS -- round 13 RIV-fe-1 J1 grade (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-06 ~21:30Z. Packet: COO~RV msg 30319 (deploy record @57ca7ef99f).

**J1: limbs 1 and 2 MET; limb 3 NOT YET EVALUABLE** (it waits for the 2026-10-07 names run). C-S47 is REMEDIATED in place
(REMEDIATION_v11). This is a grade record, not the round-13 slug: gw-1 and lk-1 are not terminal, and Z-W2-S15 compiles with them.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S49",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-06T21:30:00Z",
    "one_line": "RIV-fe-1 J1 on the served 10-06 page (rv-publish-1006r13b, 1,317,781 B, 21:18:30Z): limbs 1 and 2 MET -- the 15 C-S47 mentions now open a modal with their fund's section, and fund_sections.missing reads 0 (2,076 of 2,076 by the manifest and by this seat's walk). Limb 3 (the C-S36 names) is NOT YET EVALUABLE: it waits for the 2026-10-07 names run. C-S47 is REMEDIATED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "RIV-fe-1 J1: on the served page, the 15 C-S47 mentions open a modal with their fund's section, the manifest's fund_sections.missing reads 0, and the C-S36 control set (8053 JP, 9433 JP, RBLX US, 000270 KS) reads real names after the next names run.",
    "world_is": "Measured by this seat with the round-12 grader on the S3 bytes (sha256 in served_index_sha256.txt):\n- 2,076 buttons, 0 unresolved, 0 whose target modal lacks section[data-fund=F] (15 on the 17:33Z page); 423 security modals.\n- 234 of 234 real clicks (13 funds x 3 periods) open the right modal, each with the clicking fund's section; a button inside an AI modal opens its security modal.\n- The three positive controls: WCMG's 11 Nebius buttons all target NBIS_US_Equity (modal carries WCMG; no N97284108 modal on the page); WCMG's 3 Alphabet buttons all target GOOGL_US_Equity (carries WCMG), 0 GOOG; GQGU's 5 SpaceX buttons target SPCX_US_Equity, whose modal now carries a GQGU section ('No contribution figures for this holding'; +$12.1m net bought across 1 trade).\n- Control against a false regression: GQGU's panel names Nebius 0 times on both the 17:33Z and the 21:18Z page, so the vanished CUSIP modal removed no GQGU link.\n- Whole: 13 of 13 panels; 0 audit block, link or text.\n- fe-1.AC1, AC2 and AC3 re-run PASS 0 failures at CLOUD be8bbf22aa. 5 Lambdas 39/39 equal to 42b4e258d1 (control: 3 files differ from 92cf1f322b).\n- Limb 3: 4 securities still render ticker-form, 14 mentions (8053 JP x9, 9433 JP x2, RBLX US x2, 000270 KS x1), unchanged from the 17:33Z page.\n- S43 is not closed by this: GQGU's Nebius row and WCMG's still carry two keys until the 10-07 census; only the wrong-fund LINK is gone.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/etfs_rivals_r13_fe1/j1_result.json and census2.json (graders in ../etfs_rivals_r12_j1/)",
        "s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-06/index.html 1,317,781 B 21:18:30Z and its manifest (fund_sections 2076/2076/0)",
        "this seat's re-runs of round13/checks/fe-1.AC1.py, AC2.py, AC3.py at be8bbf22aa",
        "lamcmp.py 42b4e258d1 92cf1f322b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. REMEDIATION_v11 C-S47 moves OPEN -> REMEDIATED in place on its own stated proof (0 of 2,076 buttons fail; the three named securities as the positive control). J1's limb 3 is graded after the 2026-10-07 names run; C-S36 and S43 stay OPEN. Round 13 is not drained (gw-1, lk-1), so this is not the slug."
  }
]
```

-- 3.0.0_SA_CVO~RV
