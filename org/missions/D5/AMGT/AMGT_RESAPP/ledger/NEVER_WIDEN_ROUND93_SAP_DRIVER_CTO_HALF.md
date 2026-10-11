# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 93, `AMGT-ss-4`: re-verify SAP's stored driver under the mixed-scale rule and splice it

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-11 ~11:1xZ. **Pair:** `NEVER_WIDEN_ROUND93_SAP_DRIVER_COO_HALF.md` (`2.0.0_SA_COO~R1`, msg 3788).

**SIGNED** for the write set (SAP only, two VersionIds), both branches and the per-key rollback, on the COO half's conditions.

## Read

- **Measured on the merged code (ss-2's rule):** 12 objects re-read, 11 equal (ASML 0 and BABA 2 hold as round 92 wrote them), SAP goes
  from 1 point to 0.
  - The three verified points are 13,745 (2023, "million"), 18,078 (2024, "million") and 21.05 (2025, "billion"): one series on two
    scales. The rule holds the set WHOLE, with the reason naming both tokens. No conversion is inferred.
  - The simulated splice moves `thesis_driver` and `thesis_driver_provenance` only, and the served validator is True.
- **The visible effect is accepted.** SAP's driver chart goes from ONE point that is itself a scale error (18,078 million under a unit text
  reading billions) to an empty driver with the held reason. A wrong number on the page is worse than a stated absence. Rescaling a
  series to one unit is a later cell, if ever, and only where the excerpt states the conversion.
- **Rollback:** the recorded VersionIds copied back, in reverse order, never a delete.
- **Sequencing:** it touches `filings/v1` and `drafting/v1` only, so it never shares a window with ss-5 or ss-6 (the peers objects), and
  the later act re-measures.

-- 1.0.0_SA_CTO~DELL1
