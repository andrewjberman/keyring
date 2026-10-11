# CTO ROUND-9 ANALYSIS -- IRPT_YCDGEN -- answering the round-8 L10 slug (2026-10-11 ~08:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/remediations/REMEDIATION_v7.md`
@aa9286f7af (3.0.0_SA_CVO msg 4452), on `deliverables/2.0.0_SA_COO~G2/r8/ROUND8_DRAIN_END_READ_20261011.md` @a6bd47170b.
**Prior:** `CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_8_20261011.md` with Addenda 8.1 to 8.3. **No PRD addendum.**

## 1. Where the project stands

**FWD-1 is NOT MET and has still not been run as written.** Round 8 was all reads, and they changed what is known:

- Of the retained test report's 257 sections, 6 carry a value.
- 96 read `NOT_IN_THIS_VERSION`, a true stated reason.
- 155 read `INPUT_MISSING`. That one reason covers two causes: 70 sections have no rule at all, and 85 are fed from the
  characteristics store, which held no row for that request's 10 securities.
- The store holds 172 securities. Cottonwood held 826 on 2026-05-06; 72 have a store row, 8.7% by count. Weights are unread.

So the thread's missing hop is not the generator. It is the data the generator reads: FWD-8 and FWD-14. Round 9 is still a
thread round, and it is mostly measurement before any request for data is sized.

## 2. Ruling on the row

| row | ruling |
|---|---|
| **D2-W10-S7** (OBSERVATION, INERT; owner this seat): the portal's wire generator cannot render `OwnedAnalysisRequest.schema.json` since `persist_inputs.report_index` was added as two empty schemas | **The contract moves: the two members get a type.** An empty schema in a contract admits anything, so it states nothing, and a generator that refuses it is right to. The schema is IRPT_ANLREQ workstream Y's file: 2.0.0_SA_COO~Y2 types the two members in its next cell, and DSGN_IRPTV1's uncut id `iv-e-26` (wire regeneration) closes on that by regenerating. The portal generator is not changed. |

The three ARMED rows (D2-S38, S16, D2-W7-S1) stay with 2.0.0_SA_COO~G2 as the slug states them.

## 3. ENRICHMENT LIST for round 9 (ONE issuance, in this order)

1. **The stated reason is made true.** The order already written (round 8 AMENDMENT 2 @f81e3e72b4, two checks failing at
   base): `opal_producer.closed_reason` stops folding causes. No rule reads `NOT_IN_THIS_VERSION`; a rule whose store has no
   row reads that the security is not covered. Proof: the census re-run on a regenerated report.
2. **Coverage by weight.** The 72 of 826 is a count. One read of Cottonwood's positions (counts and percentages only leave
   it; no account, no dollar figure): what share of held VALUE the 72 covered securities carry, and the uncovered 754 grouped
   by kind (the 120 five-letter symbols ending in X, the 253 with no symbol, the rest), each with its share of value.
3. **The request is sized, not sent.** From item 2: the shortest list of securities that takes value coverage to a stated
   level, ordered by weight. The list is a deliverable. **Nothing is asked of Bloomberg in round 9**: a Bloomberg pull goes
   only through its queue, and whoever cuts that request reads `integrations/bloomberg/READ_HERE.md` first. Kinds the store's
   source does not describe (funds, if so) are named as needing another source Opal already holds, which is item 4's read.
4. **The 70 rule-less elements, listed.** By input (`bond_maturity` 17 first), each with whether Opal already keeps data that
   could feed it and where. Read-only. This is FWD-14's work list.
5. **Carried cells a and b**: the portal's status call read for `REQ-5e4149d2` once IRPT_ANLREQ's reader release is live
   (D2-S38); the generation hop read from TCKT_VNEXT's run 3 trace (S16). Neither orders a run of its own.

Items 2 and 4 are independent and read-only. Item 3 follows item 2. Each build order carries at most three mechanical
criteria. Served reads are batched into one window (this seat's msg 4392).

## 4. The sitting

Not asked. The bar stands (Addendum 8.2): on a seat-measured Overview for Cottonwood-shaped holdings, every reason the page
states is true, and Andrew is given the counts by class beforehand. On today's numbers a Cottonwood Overview would be mostly
"not covered", truthfully. Whether that is worth a sitting is decided on item 2's value share, by this seat, at the round-10
analysis.

## 5. Acts only Andrew can do

- **The FWD-1 sitting.** Citation: PRD FWD-1 ACCEPT, "Andrew, signed in as himself". Not asked.

## 6. What this analysis did not measure

It rests on the slug and the issuer's reads as filed. This seat read none of the positions file, the store, the census or the
generator. "8.7%" is 2.0.0_SA_COO~G2's count on one date (2026-05-06) against one store vintage (`bbg/2026-10-09`).

-- 1.0.0_SA_CTO~DELL2
