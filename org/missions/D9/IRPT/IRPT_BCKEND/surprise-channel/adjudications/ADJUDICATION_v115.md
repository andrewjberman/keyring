# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PD, the split-adjusted holdings price return: the READ)

<sweep_watermark>2026-10-15T12:16Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T12:16Z, on msg 8264 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PD_DRAIN_END_20261015.md` @8cf9a4519e). One order, IB-pr-572 (risk SERVED, read-only), complete, merged @af479072d6, issued @a8b2b72549 on the CTO's ruling @9913bf3ed4. Re-run here at HEAD: IB211-1-AC1..AC3 PASS (exit 0). `round-close-check --round 1 --workstream "~PD"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE. **Nothing built:** the merge changes only the worker's record, criteria output, proof instance and the channel; `holdings_performance.py` last changed 718716fb60 (2026-10-02).

**(1) The defect at `holdings_performance.py:816`, bytes printed at HEAD.** `git show HEAD:data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py`, lines 815-816 read `g0.loc[earning, "_contrib"] = (g0.loc[earning, "_v"]` / `* (g0.loc[earning, "_p1"] / g0.loc[earning, "_p0"] - 1.0))`. Line 816 is the price-ratio factor, with neither price split-adjusted. The packet's description (`v * (p1 / p0 - 1)`) matches the bytes.

**(2) The ruled key: the two lanes agree on its meaning, and both show it is one firm's schema.** The ruling is `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_ICRO_VUG_STOCK_SPLIT_NONFLOW_SPLIT_ADJUST_HOLDINGS_RETURN_20261015.md` @9913bf3ed4, item 4: classify by `(tran_srcde, tr_cd, sb_cd)`, never `tr_cd|sb_cd` alone. IRPT_DASHBD v89 (DISCLOSURE 1) records ~D2's rounds 121-123 keyed without `tran_srcde`, so the 04-21 `IC|RO` rows read as in-kind receipts instead of the `STK` "STOCK SPLIT" they are. ~PD reads the same triple the same way: `tran_srcde=STK` plus the STOCK SPLIT text marks the split (1,348 STK rows on 49F, all STOCK SPLIT; W415-S4). The lanes agree. Both, and the ruling, rest on the 49 Financial (Schwab) transaction schema. ~PD measures that Cottonwood's and Inflection's feeds carry none of the three columns (W415-S1, BLOCKING, ARMED, owner `~P2`). So ruling item 4's "No served producer is affected: the producers already key on all three" holds for 49 Financial only, and "every reader" cannot apply to the other two firms until each declares its split key.

**(3) 17 of 75 at 2 percent, confirmed from the record.** `split_source.49financial`: 76 split security-days, 75 measurable, 1 ratio absent, 58 agree, 17 disagree. The tolerance is stated in the record: agreement when `|r x close(t)/close(t-1) - 1| <= 0.02`, "stated here and not tuned". The denominator is 75 measurable security-days on 49 Financial alone, not all firms.

**(4) 985 against 920: different populations, so the CTO's count is NOT shown contradicted.** The 920 is the ruling's (@9913bf3ed4 items 3 and 5): account-days on 2026-04-21 the guard GRADED (`GRADED_DISAGREED` / `NOT_MEASURABLE`). The 985 is distinct accounts holding one of five split securities at t-1 on that day (`delta_projection` statement), a holder count with no grading filter. The read says it "does not reproduce" 920, which is true, but it never counted the graded set, so it neither confirms nor contradicts it. The same goes for the CRO's 840 (quantity exactly x6.0) against the read's 846 (6-for-1 holders with no same-day activity): different filters. Two record-hygiene defects follow from this: the field holding 985 is named `graded_disagreed_on_2026_04_21`, which mislabels a holder count as the graded set; and `account_days_affected` gives cottonwood 0 and inflection 0 where the statement says these are unmeasured, not zeros. Under the claim rule those should read absent/null. Neither is used by anything built.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S23",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T12:16:00Z",
  "one_line": "Round 1 ~PD. holdings_performance.py:816 (bytes printed at HEAD) multiplies by p1/p0 - 1 with no split adjustment. The ruled key (tran_srcde, tr_cd, sb_cd) means the same to ~PD and to ~D2's v89 disclosure (STK + STOCK SPLIT marks a split; IC|RO alone misreads it), and exists on 49 Financial's transactions only; Cottonwood and Inflection carry none of the three (W415-S1, BLOCKING, held). 17 of 75 measurable 49F split security-days disagree with the close ratio at |..|<=0.02 (record). 985 (holders at t-1) vs the ruling's 920 (graded account-days) are different sets: not a contradiction. Record hygiene: 985 sits in a field named graded_disagreed; Cottonwood/Inflection read 0 where unmeasured. IB211-1-AC1..AC3 PASS; nothing built. Dismissed (5): D2-W415-S2, -S3, -S4, -S5, -S6 (readings). Held: D2-W415-S1, D2-S195.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W415-S2",
   "IRPT_BCKEND-D2-W415-S3",
   "IRPT_BCKEND-D2-W415-S4",
   "IRPT_BCKEND-D2-W415-S5",
   "IRPT_BCKEND-D2-W415-S6"
  ],
  "spec_asserts": "CLAUDE.md rule 27 L4-R: a citation is verified by printing the bytes at the cited line; section 4: a value carries its claim (an unmeasured count is not 0); CTO ruling @9913bf3ed4 item 4: every reader classifies by (tran_srcde, tr_cd, sb_cd).",
  "world_is": "The split defect is confirmed in the bytes; nothing is built. The build cannot be cut as ruled for Cottonwood and Inflection: their feeds have no tran_srcde, tr_cd or sb_cd, so each needs a declared split key (Cottonwood names splits in text types). The pair also needs the CTO's word on which ratio governs when the custodian ratio and the close ratio disagree (17 of 75), and the DELTA is a lower bound (49F 1,291 account-days) until the other two firms are keyed.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T12:1xZ of the invocations in IB-pr-572: IB211-1-AC1..3 PASS, exit 0",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 1 --workstream ~PD: orders=1 proof_ok=1 judgment=0 verdict=MAY-CLOSE",
    "git show HEAD:data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py lines 812-818 printed (cat -A); line 816 the p1/p0 factor; file last changed 718716fb60 2026-10-02",
    "git diff --name-only af479072d6^1 af479072d6: worker record, criteria output, proof instance, INVESTIGATION_v1.md",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_ICRO_VUG_STOCK_SPLIT_NONFLOW_SPLIT_ADJUST_HOLDINGS_RETURN_20261015.md @9913bf3ed4 lines 5, 19-30 (840 accounts x6.0; 920 graded account-days; item 4 the triple key)",
    "org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v89.md @f10b69c083 DISCLOSURE 1 (keyed without tran_srcde)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~415/IB211-1_split_adjust_read.json: split_source.49financial 75/58/17/1; tolerance 0.02 stated; delta_projection 1291, graded_disagreed_on_2026_04_21=985 (statement: holders at t-1), cottonwood 0 and inflection 0 with claim absent on split_source",
    "investigation rows D2-W415-S1..S6, D2-S195",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PD_DRAIN_END_20261015.md @8cf9a4519e (msg 8264)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Five readings. The build-blocking key gap (W415-S1) and the issuer's disposition row are held with ~P2 for the CTO's answer on per-firm keys and the governing ratio."
 }
]
```
