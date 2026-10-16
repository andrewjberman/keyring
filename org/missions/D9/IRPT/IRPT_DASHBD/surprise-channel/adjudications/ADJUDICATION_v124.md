# IRPT_DASHBD: CVO adjudication, round 122 (workstream F-SHIP, ~F2): the FWD-5 words proposal, rule-24 graded

<sweep_watermark>2026-10-16T04:06Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T04:06Z, on msg 8997 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R122_F.md` @415a63b247, blob 20f4b8b9fb). Not B-IN's or B-49F's round 122. One LOCAL record order, TO-DB-f-802 (worker ~802; merged b14044804d, in HEAD). No judgment criterion. Re-run on the landed tree (HEAD beeaa9b7a6): DBF122-1-AC1 and AC2 PASS; round-close --round 122 --workstream ~F2 MAY-CLOSE. The proposal is a value enum, so this seat graded it against rule 24's four postulates itself, beyond the checker. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S62",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T04:06:00Z",
  "one_line": "Round 122 F-SHIP (~F2): a proposal of 21 type words and 8 action words over 82 source values (49F 18 = tr_cd 3 + sb_cd 15; COT 16; INF 48), 6 UNMAPPED with reasons, with a rule-24 record and a word-boundary census (denominator 82). The checker's 82/82 holds. RULE 24, GRADED HERE. (i) MECE: complete over its DECLARED domain, but the domain is narrower than the claim's population. 49 Financial's classification key is tran_srcde: the CRO table (SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json, 187 rows) carries 157 distinct tran_srcde, and the round-120 record itself says reading tr_cd as action and sb_cd as type is INFERRED. Subtracting over the table, 56 of 187 codes (30%) sit under the UNMAPPED sb_cd values FC, IC and JR, so their transactions get no word; no sb_cd value is missing from the mapping. (ii) SAME GRAIN fails for 49F: 9 of 15 sb_cd values span more than one CRO category (FC 5, FI 3, FO 3, JR 3, TA 2, DV 2, RO 2, IN 2, FE 2), including six the proposal maps to ONE word (DV also covers Security Transfers; FI and FO also cover Checks and Electronic Transfers). The word is right at sb_cd grain and lossy at tran_srcde grain. (iii) ONE INTENT holds: the action is derived from the type through one table, never typed. (iv) STATE COHERENCE: not stated (which values a remap would not move); absent. Cottonwood and Inflection were not re-subtracted here (single type fields, no wider table found). sb_cd TR: the table has one code, tran_srcde TRADE, with category Trades, rule trades, desc 'ADJUSTING ENTRY'. Adjustment follows the description and UNMAPPED follows the rule; the side is not knowable from the code. WHO RULES IT: the CTO. Its round-120 analysis, ruling 1, already decided ownership (~F2 proposes, the CTO ratifies), so FWD-5 vocabulary ownership is no longer unruled. Recommendation for the ratification: carry 49F's words at tran_srcde grain (the 157-code table), or ratify the sb_cd table explicitly as a lossy first cut with the 56 codes listed as unmapped. Dismissed (3): D2-W802-S1 (Tax withheld defaults to INTERNAL, since the brief's seven flow classes have no tax value), D2-W802-S2 (FC, IC, JR span several meanings; confirmed above), D2-W802-S3 (two Orion dividend-family values sit in the Internal bucket under an INCOME word), all INERT observations for the ratification.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W802-S1",
   "IRPT_DASHBD-D2-W802-S2",
   "IRPT_DASHBD-D2-W802-S3"
  ],
  "spec_asserts": "Rule 24 (CLAUDE.md): a value-enum proposal arrives with its four-postulate record and a word-boundary token census; MECE is tested by subtraction from a printed denominator whose domain is the claim's population (falsify the domain first). CTO round-120 analysis ruling 1: ~F2 proposes, the CTO ratifies.",
  "world_is": "A proposal record only; nothing served, contract not cut. Over its declared 82 values it is complete; over 49 Financial's real code space (157 tran_srcde) 30% of codes have no word and most sb_cd words are coarser than the codes beneath them.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T04:0xZ at HEAD beeaa9b7a6: DBF122-1-AC1 PASS, DBF122-1-AC2 PASS; round-close-check --round 122 --workstream ~F2: MAY-CLOSE",
    "org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json: 187 rows, 157 distinct tran_srcde, 15 sb_cd; 56 rows under sb_cd FC/IC/JR; sb_cd TR = tran_srcde TRADE, category Trades, rule trades, desc ADJUSTING ENTRY",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~802/FWD5_WORDS_PROPOSAL_R121.json (82 mapping rows; 49F type map read)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~701/RD_FWD5_FIELDS_R120.json (tran_srcde named, not listed as a code set; tr_cd/sb_cd reading INFERRED)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R122_F.md blob 20f4b8b9fb (msg 8997)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Three INERT worker observations, each an input to the CTO's ratification. The rule-24 grain and domain findings are not a row to dismiss; they go to the ratifier in the slug."
 }
]
```
