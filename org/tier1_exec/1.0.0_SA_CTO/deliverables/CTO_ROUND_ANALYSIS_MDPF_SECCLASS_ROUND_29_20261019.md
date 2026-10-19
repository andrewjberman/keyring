# MDPF_SECCLASS -- ROUND 29, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-19 ~15:0xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 8325), `ADJUDICATION_v30.md` @3c7ff3bb3a. MAY-CLOSE, 26 orders. 7 rows swept: 4 dismissed and
3 graduated to REMEDIATION_v19. `round-close-check` lists TO-DEPLOY-e57e61 as not complete, outside the verdict.

## 1. Graded (round-28 enrichment list, `CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_28_20261018.md`)

1. **(a) E_18's fire line: MET.** On the CVO's own read of two chain logs, the 10-19 04:03Z fire prints all 14 held-out tickers by
   name. **D1-S42 is DISARMED** (row C-S37). Its remediation stays OPEN because the 14 are still unclassified, which is S55, ruled
   below.
   **(b) 10-16 absent from the 00:24Z version: EXPLAINED.** It is S54, dismissed: A_03's window ends at the newest silver transactions
   date, and the row appears from the next 04:00Z fire. That is schedule order, not a defect.
2. **LCFYX to fixed_income:** shipped under my half @ae5763dab8. No row contests it.
3. **S52, the held-out display: MET.** It shipped under my half @554d3d227f, and the held-out names now print.
4. **The partners-data repoint: NOT LANDED.** It waits on Andrew's word, because the apply is client-facing. W104-S2 (ARMED) is
   inlined in it: the classifier returns the table's asset_class verbatim, a wider set than the pre-read said. FWD-12 (the sector
   writer) carries behind it.
5. **D_03 / C_06:** carried. The slug grades nothing on them.

## 2. Graduated (REMEDIATION_v19)

- W104-S2: ARMED, as in item 4.
- S53: the served TOTAL runs $31.6k to $32.2k below canonical on Monday-to-Thursday dates only. The cause is unread.
- S55: the 14 held-out tickers.
- **TO-DEPLOY-e57e61** is not complete. M1 either closes it, or names what it waits on, in the round-30 issuance.

## 3. The CVO's question, ruled

**S55: should the April name-to-ticker table still gate candidacy when a ticker is absent from etf-classifications?**

**RULING: no.**
- The April table's job is resolution: name to real ticker. A real ticker that is absent from the canonical classification table is
  exactly what the classifier exists to classify. Holding it out makes it permanently unclassified, with nobody owning it.
- **What changes:** a name that the table resolves to a real ticker absent from etf-classifications enters candidacy through the
  classifier's normal path and its normal refusal rule. Each written row carries `resolved_via = april_table` as its claim field, so a
  consumer can reject on it.
- **What does not change:** a name the table cannot resolve stays unresolved and printed. The table never writes a class itself.
- The 14 are not all one kind; WTM, for one, is a stock. The classifier's own rule decides each one. A refusal is printed with its
  reason, never silently skipped.

## 4. ENRICHMENT LIST -- round 30 (ONE issuance by `2.0.0_SA_COO~M1`); one served change per fire, in this order

1. **S55: the 14 enter candidacy** as ruled.
   - It goes under its own never-widen pair: etf-classifications gains rows, which is a served move.
   - The blast radius is the 14 tickers and nothing else.
   - The pair reads both branches from the classifier's rule, written and refused.
   - Proof is the next fire's E_18 line: the 14 read as written or refused-with-reason, and 0 held out.
2. **S53: a read cell**, no writes. It names the step and the dates behind the $32k Monday-to-Thursday gap, read against
   `lib/trading_calendar.py` and the producer's own rule. The cause becomes its own row.
3. **TO-DEPLOY-e57e61:** closed, or its wait named.
4. **Carried:**
   - the partners-data repoint, with W104-S2 inlined, waiting on Andrew's word for the client-facing apply;
   - FWD-12 behind it;
   - D_03 / C_06.

## ACTS ONLY ANDREW CAN DO

- **The partners-data repoint apply.** Citation: a client-facing change, which needs his word.

-- 1.0.0_SA_CTO~DELL1
