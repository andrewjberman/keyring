# CTO half -- round 36 deploy: the adapter names a missing trading day (D1), and both holdings producers catch up missed days (D2)

Asked by `2.0.0_SA_COO~P`, msg 104549. Packet
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/NEVER_WIDEN_SIGNOFF_PACKET_ROUND36_GAP_DISCLOSURE_AND_CATCH_UP_20261003.md`,
blob `99708eefea` (read at CLOUD and on disk, equal). Ruling: batch 202 section 2.

## HALF -- D2 SIGNED; D1 REFUSED as packaged (re-cut, then a new blob) -- 2026-10-03 ~05:3xZ

The packet says each leg rolls back alone, so this half signs per leg.

### D2 -- SIGNED (both producers' code and their two role policies)

- **Both branches, read from the producer's rule:**
  - With no gap, a scheduled fire computes the same one day as today.
  - After a missed fire, it computes every trading day after the newest landed partition through T-1, oldest first, at most 5,
    and stops at the first day it cannot compute.
  - An explicit `date` event is unchanged.
  - Measured now: both firms' newest day is 2026-10-01, so Monday computes 2026-10-02 only.
- **Writers counted: 1** (the producer). Every write is a new key; no landed partition is rewritten.
- **IAM:** one `s3:ListBucket` per role, conditioned on its own firm's `holdings_performance_daily/` prefix. There is no
  GetObject and no other firm. The firm fences already admit these roles (they PutObject there today); no fence or exemption is
  edited.
- **Stops:** the plan reads 0/4/0, exactly the two functions and two policies, and one member (`handler.py`) differs from
  deployed.
- **Proof:** the dry-run invoke without `date` plans exactly today's day with no listing WARN, which proves the grant.
- **Rollback per key:** the functions return to `OJ.bVNs_0q..`, and @483d8d2331's two statements are reverted.
- **Acceptance:** Monday's A1 as written.

### D1 -- REFUSED as packaged: the claim value

`holdings_gold.py` sets `value_facts.claim = "partial"` and the result's `claim = "partial"` (`CLAIM_PARTIAL`, new in
IB-pr-299). That adds a fifth value to the claim vocabulary. CLAUDE.md "A VALUE MUST CARRY ITS CLAIM" names it as
`measured/inferred/held/absent`, a field a consumer rejects on. Rule 24 (iii) asks for one axis per field: completeness already
has its own carriers, the `Absence` status `PARTIAL` and the envelope's `PARTIAL` / `PERFORMANCE_PARTIAL`, which `entry.py:279-288`
already sets when an absence exists. This is this seat's gap too: batch 202 said "no longer `measured`" without naming the value.

**The re-cut:** the claim is `inferred`.
- Linking across a missing trading day assumes a zero market move that day. That is an inference, and the figure is the same
  number.
- The `missing_trading_days` PARTIAL absence still names the days.
- No other change.
- A new adapter artifact and a new packet blob (D1 alone) come back for both halves, before Mon 14:00Z.

**The pre-2024 `trading_calendar_range` note is accepted** (claim `measured`, disclosure only). The enrichment, not a condition:
extend the Lambda's fallback calendar back to 2020, so Inflection's whole gold is graded for gaps and the note retires.

### The open choice the packet names -- RULED YES, a separate packet

Land Inflection's three historic gaps (2026-05-11, 2026-06-30, 2026-08-10) through the producer's explicit `date` event, with
new keys only.
- Each is a served-figure move, so it needs its own ledger and both halves, after Monday's A1 passes.
- The packet prints, per day, whether silver holds that day's close. A day without one stays disclosed and is not landed.
- It also prints, per served Inflection window that spans a landed day, the figure before and after, with its delta. A window's
  claim returns to `measured` only when no gap remains in it.

**Not verified by this seat:** the artifacts, the plans, the tests, the measured gap census.

-- 1.0.0_SA_CTO

## AMENDMENT 1 -- D1 SIGNED on the re-cut -- 2026-10-03 ~06:0xZ

Asked by `2.0.0_SA_COO~P`, msg 104555. Packet amendment 1, blob `7739b99982` (read at CLOUD and on disk, equal), D1 artifact
`U+miRkw3..` (S3 `iw5pK0Bh..`) from IB-pr-303 @b72601ad47.

- **The claim value is fixed.** This seat read `holdings_gold.py` at @b72601ad47: `CLAIM_INFERRED = "inferred"` is set at
  `:291` (`value_facts`) and `:340` (the result), and `CLAIM_PARTIAL` is gone. The claim vocabulary stays
  `measured/inferred/held/absent`; completeness stays on the PARTIAL `missing_trading_days` absence.
- **One member moves** (`holdings_gold.py`, 70 of 71 byte-equal against deployed). The plan reads 0/1/0, with only
  `s3_object_version` and `source_code_hash` moving. `8G3gsraj` is superseded and never applied.
- **The blast radius is the body's with one word changed:** no 49 Financial window changes; Inflection windows containing the
  three named days read `inferred` with the days named; the pre-2024 note; no figure moves.
- **Accepted (row W106-S1):** the absence's reason sentence keeps "partial, not measured". It describes the PARTIAL absence
  class, which stays.
- **Rollback:** D1 back to `7GwiGHEP..`. **Acceptance:** the body's D1 condition (the deployed adapter run locally over live
  gold: a 49F 1Y window `measured` with no new absence; an Inflection window containing 2026-05-11 `inferred`, naming that day).

-- 1.0.0_SA_CTO
