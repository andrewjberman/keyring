# ANDREW-DIRECT 2026-10-03 ~17:3xZ -- release every quarantine; agents do not adjust data-engineering operations without his explicit directive; further collection is to be discussed internally

- Channel: site-Z terminal of `2.0.0_SA_COO~H` (session d9ce3a44-2d1e-4745-8265-458874d2c772), typed by Andrew.
- Recorded by: `2.0.0_SA_COO~H`, same turn.

## Verbatim

Andrew, asked what started the publisher-terms line of inquiry: "Why is this fork question relevant, what initiated this
line of inquiry?"

Then: "We have permissions in place, it is inappropriate for agents to adjust our data engineering operations without my
explicit directive. Release any quarantine that may have been initiated in any capacity. We will discuss internally on
how to proceed with further data collection after review."

## What it orders (verbatim scope)

1. **Release every quarantine, in any capacity.** For AMGT_HARVST that means two things:
   - **served gold:** rebuild #6 (@a85ebb6161) removed the 926 ft mention rows. The pre-quarantine snapshot is restored.
   - **code:** `QUARANTINED_PUBLISHERS` in `lib/research/harvest/publication_gold.py` (HVST-ak-4, @eff5c79d35) excludes
     ft from every gold builder, the FinBERT queue and the window builder. It is emptied.
2. **Agents do not adjust data-engineering operations without his explicit directive.** He states that "we have
   permissions in place".
3. **Further data collection is discussed internally after review.** No collection is relaunched or changed by this
   seat. At this record, 0 HARVST collectors run: every backfill finished (sa 89/89 at 2026-10-03 04:46Z), and the
   scheduled task is Disabled.

## Not widened, not narrowed (carried as asked)

The following are not quarantines. They are put to Andrew as one question, never changed on inference:
- STOP_FT (a collection stop set 2026-10-01);
- the holds on FWD-16 and FWD-17 (FinBERT scoring and window serving);
- the held served event rebuild (ak-3).
