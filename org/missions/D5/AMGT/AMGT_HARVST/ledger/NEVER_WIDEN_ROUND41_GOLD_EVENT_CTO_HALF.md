# AMGT_HARVST round 41 -- HVST-an-3 never-widen pair, CTO half (the served chatter_event rebuild)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-03 ~22:0xZ. **COO half:** `deliverables/2.0.0_SA_COO_H/round41/NEVER_WIDEN_HALF_COO_GOLD_EVENT.md`
@72f2c9be42 (msg 29036). **Authority:** Andrew ~20:3xZ card 2, "yes to all recommendations" (@9fe6e6f111).

## What I read

- **The rule, signed instead of a count:**
  - events > 0, with unique ids;
  - every `security_key` in the 212-name universe;
  - every `article_keys` entry a mention row of that security in the newest served snapshot (ORPHAN 0);
  - the builder's own lead rule, and `articles_total == len(article_keys)`;
  - HEADLINE MISMATCH 0.
- **The dry run over the current mention snapshot:** 8 served events on 6 securities -> 438 events on 63 securities, with every check
  at 0. This matches HVST-ak-3's census (438). The act runs AFTER an-2 over the larger snapshot, so it will build more.
- **The served set is REPLACED:** 4 of the 8 served events are not reproduced. They were built 09-30 over a 9,521-row table.
- **Writers:** 1 (`build_event` via `write_gold`, never-overwrite); no scheduled producer.

## Conditions

1. **Order:** an-3 runs only after an-2 is written and its post-act read is done.
2. The act's gate holds on the WRITTEN part, and its digest equals the dry run's. If it fails, ROLLBACK as the half states (the 8 re-put
   as a newer part; nothing deleted).
3. **Post-act read on what RESAPP serves:** the timeline route (FWD-37 c11) on its 3 names. Every served marker opens its day, the
   built event count is printed, and **the 4 dropped event_ids are named** with the reason the current rule does not reproduce them.
4. One act, once.

**CTO HALF: SIGNED** for HVST-an-3.
