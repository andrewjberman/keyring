# IRPT_DASHBD: CVO adjudication, round 124 (workstream F-SHIP, ~F2): the FWD-5 words at tran_srcde grain, rule-24 re-graded

<sweep_watermark>2026-10-16T05:33Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T05:33Z, on msg 9094 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R124_F.md` @7af67261ea, blob 95c00278d1). Answers this seat's v124. One LOCAL record order, TO-DB-f-1001 (worker ~1001; merged e5768b2c77, in HEAD). No judgment criterion. Re-run on the landed tree (HEAD 126b196960): DBF124-1-AC1 and AC2 PASS; round-close --round 124 --workstream ~F2 MAY-CLOSE. This seat recounted the live silver itself (read-only, column tran_srcde only, counts only). No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S66",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T05:33:00Z",
  "one_line": "Round 124 F-SHIP (~F2): the 49F words revised to tran_srcde grain. DOMAIN, RECOUNTED HERE: s3://opal-data-assets/schwab/08335338/silver/fact_trn/ holds 572 objects in 572 date partitions, 2024-07-08..2026-10-14, 3,349,750 rows, 0 null tran_srcde, 160 distinct codes. The CRO table holds 157. 3 codes are silver-only (EXWT, RDPC, SQDAJ) and 0 table-only, for a union of 160, matching the issuer's census exactly. RULE 24, RE-GRADED. (i) MECE MET: all 160 union codes appear exactly once in the 160 49F mapping rows, with none missing, none extra, none double-covered. 16 are UNMAPPED with reasons; of the 3 silver-only codes, EXWT and RDPC go to Corporate action and SQDAJ is UNMAPPED. (ii) SAME GRAIN MET: every 49F row is at tran_srcde grain (the v124 gap is closed); the residue is the 10 codes the CRO table gives more than one rule, 7 mapped to one word with a stated reason and 3 UNMAPPED. (iii) ONE INTENT: v124's finding is largely cured. 11 of 18 words still span more than one CRO category, but mostly by channel (Deposit: checks or electronic transfers), not by intent. The intent that matters is the flow partition, and two words still mix it: Tax withheld (EXTERNAL-OUT for IRAWH and MCE vs INTERNAL) and Journal (CONDITIONAL-BY-COUNTERPARTY vs INTERNAL). Deposit and Dividend also include CRO-UNRESOLVED codes. (iv) STATE COHERENCE MET: stated for 22 of 22 (21 words plus UNMAPPED), with a cross-firm non-movement statement. TOKEN CENSUS PRESENT: denominators 160/16/48 (224), per-word counts, 18 unmapped, live-read date and counts. TRADE is now Adjustment, on its description. W1001-S2 ASKS: Tax withheld carries the INTERNAL flow class while the CRO partitions IRAWH and MCE as EXTERNAL-OUT (money leaving the account to the IRS). Which flow class does the word carry, or should it split? WHO RULES: the CTO, by its round-120 ruling 1 (~F2 proposes, the CTO ratifies). Journal's mixed partition belongs in the same ruling. Dismissed (1): D2-W1001-S1 (13 CRO 'dividends' codes whose descriptions name a capital gain, return of capital, principal or spin-off, mapped on the description: a stated choice). D2-W1001-S2 is held for the ratification.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W1001-S1"
  ],
  "spec_asserts": "Rule 24 (CLAUDE.md): four postulates over a declared domain, subtraction from a printed denominator whose domain is the claim's population, and a word-boundary token census. CTO msg 9064: 49F's domain is the union of the CRO table and the live silver. CTO round-120 ruling 1: ~F2 proposes, the CTO ratifies.",
  "world_is": "A proposal record; the words are not ratified and the transaction contract is not cut. Over the live union of 160 codes the mapping is complete and single-cover; the open item is the flow class of Tax withheld (and Journal).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T05:2xZ at HEAD 126b196960: DBF124-1-AC1 PASS, DBF124-1-AC2 PASS; round-close-check --round 124 --workstream ~F2 MAY-CLOSE",
    "this seat's read-only recount (boto3 list + pyarrow column projection tran_srcde, counts only) of opal-data-assets/schwab/08335338/silver/fact_trn/: 572 objects, 572 partitions, 2024-07-08..2026-10-14, 3,349,750 rows, 0 null, 160 distinct; union with the CRO table 160; union not in proposal []; proposal not in union []; double cover []",
    "CRO table SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json joined to the proposal's 160 rows: 11 of 18 words span >1 category; flow partitions mixed for Tax withheld (EXTERNAL-OUT, INTERNAL) and Journal (CONDITIONAL-BY-COUNTERPARTY, INTERNAL)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1001/FWD5_WORDS_PROPOSAL_R124.json: postulates (mece, same_grain, intent_coherence, state_coherence) and census keys present",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R124_F.md blob 95c00278d1 (msg 9094)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W1001-S1 is a stated mapping choice on the description. W1001-S2 is not dismissed here: it is the ratifier's question, carried to the CTO."
 }
]
```
