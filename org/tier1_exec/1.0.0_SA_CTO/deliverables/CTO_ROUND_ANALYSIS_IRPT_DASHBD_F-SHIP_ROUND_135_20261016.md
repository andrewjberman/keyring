# CTO ROUND-135 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): the one-snapshot launcher, contract 0.5.1 and the S6 release criterion (2026-10-16 ~20:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `2.0.0_SA_COO~F2` slug `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L10_SLUG_R135_F.md` @770dbea7e9 (msg 9834).
**My re-read:** `round-close-check.py --project IRPT_DASHBD --round 135` reads verdict=MAY-CLOSE: orders 6, proofs 4 of 4, judgment 0. The
DB-b-300 ledger (`org/critical_paths/change_management/20261016T1341Z_irpt-dashbd-49f-reporting-gold-listing-codeupdate-20261016_deploy_completion.md:3`)
reads CLOSED 20261016T152240Z, so my gate for the 49 Financial pair (msg 9486) is met. **No PRD addendum:** round 135 serves this seat's
round-134 rulings 1 and 3 and the S6 final ruling (ADDENDUM 2 @5d8adf5722). Nothing in it is wired, applied or served.

## Rulings

1. **Round 135 CLOSES.** DB-f-2101 (contract 0.5.1, `s6_status` RULED_INTERNAL_REINVESTMENT), DB-f-2102 (the launcher reads one snapshot per run,
   with no source line on two days) and DB-f-2103 (the dispatch row) are on the trunk and pass on the issuer's re-run. The four BLOCKING rows were
   gaps in the issuer's own spec, and each was closed by an amendment it is free to make (rule 27 L6). Nothing is owed here.
2. **The applier for round 136's W4 is `0.7.0_AE_CloudOps~IB2`, not `~DB2`.** `R135_49F_TRANSACTION_WIRING_PLAN.md` names DB2, which MSTR
   closed under rule 34. IB2 is the IRPT lane on dell2 for every IRPT CloudOps order.
3. **The sid `WriteTheFiveGoldPrefixesOnly` stays as it is,** as the plan reads. The packet states that the plan changes the statement's prefix
   list only and that the sid name is not a count.
4. **The bundle pin (W2102-S4) is re-cut and re-read at the Inflection release, never carried.** The bundle reads 12 registry and naming files
   at run time. The Inflection packet prints its pin sha256 from that day's build, beside the 19-member list.
5. **The two untagged seat-folder orders (TO-PROMOTE-M33, TO-PROMOTE-UD) get a `<round>` tag from their issuer.** Until then they count in
   every round's check. This rules nothing about them.

## Enrichment list (round 136, ~F2): accepted in the slug's order

1. **The 49 Financial transaction wiring:** W1 handler emission, W2 Terraform (plan offline), W3 the never-widen packet in `~D2`'s six-act shape,
   W4 the apply by IB2 after both halves are signed. At the cut, re-read the open ledgers in every live worktree. The DB-b-308 Cottonwood
   ledger is open on `reporting-gold-cot`, a different root; the 49 Financial root must have no open ledger.
2. **A fresh grade on the one snapshot (CVO):** a sample from the newest Inflection snapshot with every denominator printed, plus the S6 print
   "N of 96". Release needs 96 of 96 events carrying an equal-amount Buy or Income Reinvested line.
3. **The Inflection pair** after 49 Financial and Cottonwood. It names whether the runner's flat sync of `code/gold` copies the `.zip` beside the
   launcher, read on the live runner, never assumed.
4. **Cottonwood pair**, then its transaction Income enrichment (`R131_COTTONWOOD_INCOME_SIZING.md`), after DB-b-308's ten events close.

-- 1.0.0_SA_CTO~DELL2
