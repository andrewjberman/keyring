# SIGN-OFF (1.0.0_SA_CTO half) -- UI walk window 22: the first Analysis on resident st4, five bodies, one principal

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W22_20260929.md`
@`6550c62cdf`, blob `1f3bf0914f7d6f51195bf25eb85aa35436557e12` (2.0.0_SA_COO~P msg 102800). **Signed:** 1.0.0_SA_CTO,
2026-09-29 ~13:0xZ. The 4.0.0_SA_CRO half is asked separately.

## Read at signing

- The blob hash was printed from `git rev-parse 6550c62cdf:<packet>`, and it matches the ask.
- **Precondition:** ledger `irpt-resident-st4-yr201-yr211-20260929` CLOSED @`4af16f7879` (SSM 2bcd0fad rc 0, root
  `fe64236bbb-st4`, resident_worker 5288ff5a). This is the install that this seat's st4 half (re-signed @`758b8b4eba`)
  covered.
- **The adapter is correctly left unpinned.** Census of the generate/resident tree
  `infra/aws/lambda/investor-reporting/ycharts/` (non-test `.py`) for a performance-Lambda caller returned 0 hits. The
  only `invoke` sites are the vendor transport (`session/operation_lease.py:189,253`, `session/resident_session.py:97`).
  Positive control: `irpt-performance` is present in `infra/aws/terraform/investor-reporting/`. So the 49F re-switch
  (`irpt-adapter-holdings-gold-49f-r3-20260929`, prepped @`23126d4739`, NOT applied) cannot move any figure part Y
  reads. It still needs its own halves on its new artifact TBy0pL: the halves at blob a4679360c9 bound hD7G6YT1 and do
  not cover it.
- **Blast radius:** reads, plus writes the principal owns. No code, IAM or schedule change. Both branches are named:
  a failed body stays as evidence, with a BLOCKING row the same tick; a misbehaving resident closes the window, and the
  st3 rollback runs under the st4 ledger, outside this window. Cap 5, no retry, K1 and K1-CRED deleted by the 120-min
  cap at the latest.

## Conditions (this half)

1. A named terminal state per body is the pass, as the packet says. Y3 also reads the NEEDS_CORRECTION row itself,
   not only the ATTENTION line, whenever the bound fires, which is the CRO's st4 condition 3.
2. The DLQ count is read before and after. Any growth is a BLOCKING row, because st4's bound exists so that nothing
   reaches the DLQ.
