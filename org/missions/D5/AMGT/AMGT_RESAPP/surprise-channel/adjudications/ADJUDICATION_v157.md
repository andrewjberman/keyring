# AMGT_RESAPP -- round 118 L8/L9 (dell1)

<sweep_watermark>2026-10-18T11:33:58Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T11:33:58Z, on 2.0.0_SA_COO~R1 msg 8017 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round118/DRAIN_END_PACKET.md @7e80977875 (sha256 43934556c6471f69...)). Swept: 9 dell1 rows never named, 7 dismissed and 2 graduated (1 ARMED). Clocks advanced in place: REMEDIATION_v57 W512-S2, W512-S3, W512-S4 (DISARMED at 2026-10-18T11:14:27Z, the AMGT-by-5 apply, and REMEDIATED), W513-S1; REMEDIATION_v56 C-S189, W511-S9. The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S193",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T11:33:58Z",
    "one_line": "ROUND 118 L9: the CTO's rich-export grade MET on the three live rich exports. 0 storage paths, 0 order ids and 0 vendor-error lines; RIO LN withholds market cap, net debt and enterprise value with the page's words and prints no amount; served reasons print in plain words. The three PDFs are byte-identical to the round-117 PDFs graded MET. Round 118 is MAY-CLOSE with all orders complete. Clocks: REMEDIATION_v57 W512-S2/S3/S4 disarmed and remediated, W513-S1 remediated; REMEDIATION_v56 C-S189 and W511-S9 remediated.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W515-S1",
      "AMGT_RESAPP-D1-W515-S4",
      "AMGT_RESAPP-D1-W515-S5",
      "AMGT_RESAPP-D1-W515-S6",
      "AMGT_RESAPP-D1-W516-S1",
      "AMGT_RESAPP-D1-W516-S2",
      "AMGT_RESAPP-D1-W516-S3"
    ],
    "spec_asserts": "The CTO's round-117 analysis for R1 (ledger/ROUND_ANALYSIS.round117.R1.md @e351115a7e, msg 7987): the rich export takes the pack's rules in full (plain sentences, withheld figures per W513-S1, guarded readers per W511-S9); W512-S2 and W512-S3 disarmed by one reason mapper; a C-S189 census across all names.",
    "world_is": "READ BY THIS SEAT 2026-10-18 ~11:3xZ. The packet hash was verified. PDFs: sha256 of the three round-118 PDFs equals round 117's (RIO LN 4dcc0ac6ec4c, ICT PM d69276f5cfa5, GOOGL US b9d4e388f090), so ADJUDICATION_v155's grade stands for them. RICH EXPORTS (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round118/packs/*_rich_export.md, 767, 749 and 728 lines). 's3://' 0, 0 and 0. 'AMGT-xx-n' 0, 0 and 0. No vendor or Python error text: the lines an error pattern matched are field names (RETURN_ON_TANGIBLE_ASSETS, FREE_CASH_FLOW_PER_SH) and decimals containing '403'. RIO LN Header rows: CUR_MKT_CAP, NET_DEBT and CURR_ENTP_VAL read '<label>: Bloomberg does not confirm this figure's currency' with no amount. ICT PM NET_DEBT reads the same. GOOGL US prints its amounts. Absence lines read in words ('Posture: ABSENT -- no positioning view is on file for this name'; the CEO reading 'the object could not be read'), not codes. C-S189 census (the issuer's round118/CS189_CENSUS.md): 101 distinct names; 73 serve last_stated_position and 73 print it in the Summary; 0 are served but unprinted, which meets the census half. W512-S2: render_pack.py now prints one Positioning sentence for posture=None and ABSENT, and live TSM US prints 'No positioning view is on file for this name.' W512-S3: the CEO-profile site goes through _plain_reason (render_pack.py:943). A unit control feeds an s3 path and a vendor error (test_by1_reason_mapper.py:50-74, 258). Live TSM US prints 'CEO public profile: no public profile is on file yet.', and HD US prints a plain sentence about its web search. W512-S4 and W513-S1: the RIO LN export carries no path and no amount for the withheld figures. W511-S9: the rich route's readers are guarded, proven by unit controls (no live fault was forced). The issuer's all-names leak scan of the live packs reads 101 clean of 101. RESIDUALS. (a) Graduated as C-S195: the rich export's CEO public-profile reading reads 'the object could not be read' on 8 of 8 captured names, while the same build's PDF prints HD US's served reading. (b) Graduated, W515-S3: the export's measured money rows print no currency code. ICT PM's market cap reads '1735465117699.9998 ABSOLUTE (full currency units)'. (c) The export keeps its Mnemonic column, field codes inside the Rendered cell and unrounded floats; it declares itself 'Machine-readable rich-text export'. (d) The RIO LN export prints the Posture absence line twice (lines 758-759). DISMISSED (INERT). W515-S1: a posture basis claim is analyst text and prints as written. W515-S4: no export path calls the case function. W515-S5: the order's bound conflict is named, and the region governed. W515-S6: a figure's own code in the export is graded as legitimate. W516-S1 to S3: by-4's producer-location and census facts, read for the CTO's fund-currency question.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round118/packs/RIO_LN_Equity_rich_export.md, ICT_PM_Equity_rich_export.md, GOOGL_US_Equity_rich_export.md, and the three PDFs (sha256 compared to round117/packs/)",
        "C:/dev/ui-walk-evidence/r118-rich-issuer-after/ and r118-packs-issuer-after/ (issuer's live captures, 8 names; client data stays local)",
        "lib/research/print/render_pack.py:943,1514-1521,1701-1705 and lib/research/print/tests/test_by1_reason_mapper.py at HEAD (read by this seat)",
        "python .tools/round-close-check.py --project AMGT_RESAPP --round 118 (this seat)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round118/DRAIN_END_PACKET.md @7e80977875 (sha256 43934556c6471f69...)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (rich-export grade MET) and INERT worker rows that are resolved, named, or read for the CTO."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S194",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T11:33:58Z",
    "one_line": "Graduated to REMEDIATION_v58 (3): W515-S2 (ARMED, latent: the Appendix prints a served source and basis definition raw), W515-S3 (the export's measured money rows print no currency code), and this seat's finding C-S195 (the rich export says the CEO public-profile reading could not be read on 8 of 8 names).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W515-S2",
      "AMGT_RESAPP-D1-W515-S3"
    ],
    "spec_asserts": "Spine L10: an item that still bears on a later act graduates with an owner and a close condition; every ARMED row is dispositioned before the slug.",
    "world_is": "See C-S193. W515-S2 stays ARMED under disarm_owner 2.0.0_SA_COO~R1; the 101-name live leak scan reads it latent (no served source carries a path today).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudication row AMGT_RESAPP-D1-C-S193 (this file)",
        "investigation rows AMGT_RESAPP-D1-W515-S2, AMGT_RESAPP-D1-W515-S3"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation rows W515-S2, W515-S3 and C-S195 in REMEDIATION_v58."
  }
]
```

-- 3.0.0_SA_CVO
