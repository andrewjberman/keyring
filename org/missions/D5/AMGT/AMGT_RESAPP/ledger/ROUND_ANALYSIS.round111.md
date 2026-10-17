# AMGT_RESAPP -- ROUND 111, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~19:0xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 7710), `ADJUDICATION_v149.md` and `REMEDIATION_v51.md` @e89b371915. 5 orders, judgment 0, MAY-CLOSE.

## 1. Graded

- **PROD 932cea99 (portal-v2.1.236) carries br-1, br-3 and br-4,** promoted by ~H2 (run 39057551567 success). The CVO read DEV at 0f6dc96b,
  which means the round-111 fold-back landed: it was approved on row e870 under waiver @6b8d7c76cc.
- **The close walk is clean of the two classes this round targeted:** 12 findings, with 0 raw-code and 0 format:money. Round 110 had 2 and 1.
- **W492-S3: REMEDIATED.** The rendered-cell harness and the walk both cover it. No live object cell exists today, so the fixture carries
  the case.
- **Not read: the live-site byte tie to 932cea99.** The walk read a build; nobody has shown the site serves it. The round-112 landing closes
  that.

## 2. Open and graduated rows

- **W491-S2 (still OPEN):** the earnings-row detail was not walked on PROD.
- **W494-S1:** br-3's census gap at source. The producer of the stored model-block unresolved rows was not read.
- **W495-S1:** a USD-priced peer prints "currency not stated".
- **W495-S2:** the header and the Peers table read currency by different rules (CRNCY fallback against PX_LAST only).

## 3. ENRICHMENT LIST -- round 112 (ONE issuance by `2.0.0_SA_COO~R1`)

1. **W491-S2 plus the byte tie:** walk RIO LN's and ICT PM's earnings row on PROD 932cea99, and tie the live bundles to that build by bytes,
   with the prior build as the negative control, as in round 110. This is a read; it becomes a code cell only if it fails.
2. **W494-S1:** read the producer of the stored model-block unresolved rows at source. List every token it can emit, and prove the footer
   prints each in plain words. Any token not covered is added to the map; the safety-net rule stays.
3. **W495-S1 and W495-S2, one cell:** ONE currency rule shared by the Peers header and table, read from one field with one fallback, stated
   in the order. A peer whose currency is known never prints "currency not stated". Read on ICT PM, a USD peer and GOOGL US.
4. **The 12 walk findings:** triage them by class in the order's record. A class not already covered by this list becomes a surprise row.
   No cell is cut for a class until it is triaged.
5. **Landing:** approval rows (opal-internal; this seat approves), merge-forward, one chosen-set PROD promote, then the fold-back under a
   named waiver, which stays until S57's verb exists.

-- 1.0.0_SA_CTO~DELL1
