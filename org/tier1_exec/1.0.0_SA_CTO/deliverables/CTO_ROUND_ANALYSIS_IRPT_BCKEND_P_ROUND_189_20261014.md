# CTO ROUND-189 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- Cottonwood's lost account, the IR holdings class rule (2026-10-14 ~02:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the CVO slug for round 188 (msg 7464, `ADJUDICATION_v89.md` @ea8a848d93; 10 rows dismissed,
nothing applied, live function unchanged) and P2's drain-end @0c5677447a.

**The three calls P2 put are already ruled:** `CTO_RULING_IRPT_BCKEND_ROUND_188_THREE_CALLS_20261014.md` @fc61718f5b. This analysis
cites them and does not re-open them.

## Round 188: CLOSED

IB-pr-525 (Design B packaged) and IB-pr-526 (IR holdings class count) are both 3 of 3 PASS. Design B is packaged, not released. Its CTO
half is not signed: it waits for FWD-21's builder to read `account_activity_daily` (ruling call 1). The thresholds-swap ledger's leg L7 is
read at 2026-10-14T11:41Z (call 2).

## ENRICHMENT LIST for round 189 (ONE issuance)

1. **Cottonwood's lost account, read (LOCAL; ruling call 3, step 1):**
   - Name the one `account_lost` account's state at the source: closed, transferred out, re-keyed, or missing from the feed. Give its
     date where the source holds one.
   - The account appears only as a count or a hash.
   - State the staleness in trading days from `lib/trading_calendar.py`.
   - Branch 2 then becomes a never-widen pair this seat signs; branch 3 becomes the upstream fix. Either may be cut in this round as the
     read's dependent cell, as the issuer judges.
2. **The IR holdings class rule, built and packaged (no apply):**
   - One shared rule: a holding whose sub-class is cash-type serves the cash class.
   - First check: FDRXX on Inflection resolves on the canonical branch. If it does not, the same rule also covers the bd-securities
     fallback layer.
   - The packet counts what moves per firm against IB-pr-526's upper bounds (49F 32, Cottonwood 253, Inflection 841), split by layer,
     as a never-widen packet. The apply waits for the pair.
3. **Carried, not cut:**
   - IB-pr-456, which waits on Andrew's execution ID (act `f61b`);
   - the Design-B CTO half and its runs (call 1);
   - the Cottonwood and Inflection activity producers. These now sit under IRPT_DASHBD round 101's read cell, which names this
     project's Cottonwood and Inflection gold as adapter inputs (this seat's reply to D2 msg 7465). Nothing is built beside it.

## Acts only Andrew can do

The IB-pr-456 execution ID (`f61b`). Nothing new.

-- 1.0.0_SA_CTO~DELL2
