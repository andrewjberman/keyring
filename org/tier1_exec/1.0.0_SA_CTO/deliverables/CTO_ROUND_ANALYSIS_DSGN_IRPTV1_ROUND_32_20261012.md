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

## 2a. After the drain (2026-10-13 ~00:2xZ; 2.0.0_SA_COO~D2 msg 6684, record `ROUND_32_REAL_RUN_20261013.md` @f43d788041)

- **Portal candidate `wk-DSGN_IRPTV1-73-portal` @64980b4d: APPROVED for DEV.** Read by this seat: a fast-forward of `origin/DEV`
  cf52fdbf; 4 files, +127/-7; the one product change is `NativeSections.tsx` `unsupportedReason`, which now reads as one plain
  sentence with no producer status word (W70-S4), and a report with no verdict gets its own sentence. PROD rides `e7f2`.
- **The 49F node link (W69-S2): YES, the producer adds it.** The live 49F builder mints ACCOUNT node ids from the Schwab key and the
  directory uses `dim_account`; the producer refuses unequal accounts, so nothing wrong shows today, but the page has no account id
  per node. The producer adds an `account_id` member on each ACCOUNT node (additive, the directory's id), so the page maps node to
  account without guessing. It is the same producer link the last-four route (row D2-S28) needs, so it rides that cell at
  IRPT_BCKEND ~P under one pair (an added served member). The page then posts the account id, not the node ref.

## 3. Acts only Andrew can do

- **NEW, carried (nothing blocked):** may a client-facing Investor Reporting view name YCharts as the source of a vendor report?
  REC: not now.
- PROD of every candidate rides his held promote `e7f2`.

-- 1.0.0_SA_CTO~DELL2
