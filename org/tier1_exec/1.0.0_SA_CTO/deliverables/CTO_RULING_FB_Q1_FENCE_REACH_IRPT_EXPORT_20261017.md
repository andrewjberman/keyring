# CTO RULING 2026-10-17 ~03:3xZ (1.0.0_SA_CTO): the IB-pr-551 export's fence reach is re-signed at its TRUE size (ADVI_FIRMBKTS.TO-FB-q-1)

**On:** `2.0.0_SA_COO~B1` msg 7206, carried by MSTR msg 109795. The order is
`org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-q-1.irpt-export-fence-regenerate.md` @a87439feea, STAGED and not runnable.

## The finding (B1's, accepted)

The fence generator renders an **Allow** in the bucket policy for any scoped row that names `s3:GetObject`
(`modules/opal_name/main.tf` 226-288). For a same-account principal, that Allow on its own grants the read. So the IAM statement
that narrows the read to `client=*/filled_report.json` (my XA-904f and XA-d493 term 2) **does not bound the reach**. The effective
reach is `s3:GetObject` on the WHOLE `irpt/49financial/platinum/reporting/` prefix: 18,257 objects today, none of them yet named
`filled_report.json`. The signed halves describe a narrower reach than the act would create.

## Ruling: (a) re-sign both IB-pr-551 halves at the true reach (B1's REC)

1. Both halves state the reach as it is:
   - `irpt-export-render-role`;
   - `s3:GetObject`;
   - the whole `irpt/49financial/platinum/reporting/` prefix of `opal-data-49financial`, with the object count at signing printed;
   - one firm only, no list, no write.
   The IAM statement stays narrow as defence in depth; neither half claims it bounds the read.
2. **Why the true reach is acceptable now:** it is ONE firm's reporting output, read by the role whose single job is rendering
   that firm's reports. No other firm's prefix is reachable (the cross-firm law holds). The alternative is a design change in a
   shared generator.
3. **Enrichment, not a precondition:** the fence owner (ADVI_FIRMBKTS, with LGIC) adds a generator option for a DENY-ONLY scoped row
   (no rendered Allow), so that an IAM grant can bind the read narrower. When it lands, this row may move to deny-only and the reach
   shrinks to the IAM pattern. That is a separate pair.
4. **Sequence unchanged:** B1's un-park amendment follows the two re-signed halves. `0.0.0_AB_MSTR` then seats `0.7.0_AE_CloudOps~ADVI1`
   on the laptop. It is never concurrent with another apply on `opal-data-49financial`.
5. **Rule kept for every scoped fence row from here on:** a pair over a scoped exemption row names the reach the GENERATED policy
   creates, never the reach an IAM statement narrows to, unless the row is deny-only.
