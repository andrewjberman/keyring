# CTO ROUND-32 ANALYSIS -- DSGN_IRPTV1 -- answering the round-31 L10 slug (2026-10-12 ~23:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/remediations/REMEDIATION_v11.md`
@9ac0c902f4 (3.0.0_SA_CVO msg 6667): 4 rows OPEN, ARMED 0. **No PRD addendum.**

## 1. Rulings on this seat's two rows

| row | ruling |
|---|---|
| **D2-W69-S1** (should a last-four pick start Performance on the matched account?) | **Yes, on the matched account, by the producer's entry kind** (round-31 analysis section 2a, row D2-S28 routed to IRPT_BCKEND ~P @25c688b1e2): a query matching an account's tail returns that ACCOUNT entry; the page's account-row start (S24) does the rest. The page does not infer an account from a tail. |
| **D2-W70-S2** (may a vendor view carry the vendor's name in its source line?) | **Not now; the view keeps adding no provider (IV-e-101 arm (c) stands), and the line keeps "Source: a vendor's report."** Naming a third-party vendor on a page a partner-firm login opens is a vendor-relationship and branding decision (licensing terms unread here; IRPT_YCDGEN is building Opal-branded generation from the same data). It goes to Andrew as a carried call. If he says yes, the view gains one `vendor` member from the wire's provider and the line names it. |

## 2. ENRICHMENT LIST for round 32 (ONE issuance)

1. **D2-W69-S2** (the issuer's): one read of the holdings producer for the ACCOUNT node id equal to the account id on served
   answers; if not equal on any, map node ref to account id before the focus post.
2. **D2-W70-S4** (the issuer's): the unsupported-card reason on an UNCERTIFIED vendor report is worded like the face's one
   validation sentence, with no producer token.
3. D2-W60-S1 and D2-S21 close when candidate `cf52fdbf` lands on DEV (approved @25c688b1e2; the box manager lands it).

## 3. Acts only Andrew can do

- **NEW, carried (nothing blocked):** may a client-facing Investor Reporting view name YCharts as the source of a vendor report?
  REC: not now.
- PROD of every candidate rides his held promote `e7f2`.

-- 1.0.0_SA_CTO~DELL2
