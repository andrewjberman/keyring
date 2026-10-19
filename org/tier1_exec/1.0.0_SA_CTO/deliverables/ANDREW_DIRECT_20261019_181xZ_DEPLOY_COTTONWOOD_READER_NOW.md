# Andrew-direct 2026-10-19 ~18:1xZ -- deploy the updated Cottonwood reader now

**Received at:** `1.0.0_SA_CTO~DELL2` terminal. **VERBATIM:**

> "The fix is to deploy the updated reader now. We need to understand what is wrong with the reader now. I have CRO~PRFRPT
> at work on this, but you should feed them any findings on the matter that have come to you now"

## What it changes

1. **Order:** the Cottonwood transaction-wiring and late-posting-reader pair goes NOW, ahead of Tuesday's Inflection pair.
   - Packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/NEVER_WIDEN_PACKET_COTTONWOOD_TRANSACTION_WIRING.md`,
     REVISION 2 @5cb1dc9403, sha256 `5d7350ea8a92`, release 36da4e101f (in HEAD); both halves are signed.
   - My REVISION 2 sequence condition ("after Monday's 49F read and after the Inflection pair") is superseded by this
     word. 49F's read passed this morning.
   - It runs now, outside the band (18:1xZ Monday), and never alongside another IB2 act. It goes ahead of r34l.
2. **Precondition kept:** an open rewrite ledger on the `account-return-daily` root STOPS Act 2. `~D2`'s suspended
   TO-DB-b-332 ledger is closed as SUPERSEDED first, after a measure that nothing was written under it.
3. **The pause:** this is built and signed work, so it ships under Andrew's merge-forward order.
4. **What it corrects, and what it does not yet:**
   - Every returns day written after the apply uses the corrected reader. The settle step re-derives up to five landed
     days 14 trading days back per fire.
   - The full history since 2026-07-10 is corrected only by `~D2`'s all-days rewrite and republish pair, which is the
     next act. It is held under the pause until Andrew says otherwise, or until this reader's first fire reads clean.
5. **Findings are fed to `4.0.0_SA_CRO~PRFRPT`** the same turn, as file paths.
