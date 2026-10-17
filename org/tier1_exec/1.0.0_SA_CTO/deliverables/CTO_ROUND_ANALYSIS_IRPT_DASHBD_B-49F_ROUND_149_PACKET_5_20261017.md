# CTO ROUND-149 PACKET-5 ANALYSIS -- IRPT_DASHBD workstream B-49F (~D2): Cottonwood rewrite and republish, the minted account id (2026-10-17 ~00:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v148 (tally corrected in v149)
(`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v148.md` @e4fcb3a160, msg 23:42Z).
- **(a) PASS:** the 308 gold and the 315 served series match the signed packets on the CVO's own reads (844/798 per day; 102/826/657/659,
  value 0).
- **(b) FAIL:** the minted account ids contradict contract 0.5.4:157 and the :126 order rule, and no claim travels with them.
- **Mechanical:** 27 PASS, 6 FAIL (4 by supersession, and 2 where p180 and p181 were amended to DB-b-316's targets).
- **Ledgers:** the three ledgers read OPEN at HEAD, because the closures are uncommitted.

**No PRD addendum:** the contract file is the carrier.

## Rulings

1. **(a) stands as PASS.** The 49 Financial addendum countersign landed late; it is noted, and nothing it covered moved before it.
2. **(b) Minting is the policy; the contract catches up in ONE drain with the producer (`~D2`).** Contract 0.5.5:
   - `account_id` is the issued opaque (minted) id, the same form as `IRPT_DASHBD_CLIENT_SUMMARY_CONTRACT.json:71`.
   - A new field `account_id_form`, value `minted`, travels on every account entry, so a consumer can reject a raw id by field. No
     custodian-form id leaves the function.
   - The :126 order rule is restated as "ascending by `account_id`", the minted id, which is stable.
   - The schema hash moves, and the portal mirror follows in the same round.
   - W247-S1 closes on that drain.
3. **The three ledger closures are committed now** by their writer (IB2, or `~D2` where it closed them). HEAD must read CLOSED (CLAUDE.md
   NEVER-2). Until then, this seat treats those deploys as open for any act on the same functions.
4. **The stale FAILs:** DB-b-316 has now landed (1f525845; `~C2`'s whole-suite gate is clean). `~D2` re-runs p180 and p181 at 1f525845 for
   orders 313 and 314 and refreshes 312's proof instance, so the gate stops refusing on stale lines.

## Enrichment list (next B-49F round, ~D2)

1. Contract 0.5.5 plus the producer, in one drain, with the portal mirror.
2. The ledger-closure commits, and the refreshed proofs for 312, 313 and 314.
3. After Andrew's smoke of 1f525845 and his word on row f1bb: the DEV merge-forward.
4. The Cottonwood filled report, which follows the Cottonwood transaction cells (XA-3c21).

-- 1.0.0_SA_CTO~DELL2
