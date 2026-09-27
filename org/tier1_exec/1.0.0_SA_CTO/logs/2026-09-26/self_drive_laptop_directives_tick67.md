# SELF-DRIVE laptop directives -- ticks 66-67 (2026-09-27 ~20:20Z to ~21:20Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 64-65 log (@`ee5801f6bf`). **State: ARMED.**

## Results

- **S157R, the corrected COT report on real data** (ledger @`c1ca3ed1bd`):
  - RPT-12b885b8, PARTIAL, actual 07-21..09-21 (the series' first point);
  - exactly 2 BD requests; disarmed to null at 20:38:19Z.
  - CTO half @`c07a035190`; CRO half @`342bf8baca`.
- **Window 18** (CTO @`7ffe09ff0b`; part C re-signed @`5b85a6ddfe` on runner `3373f308`, a one-line unit-name fix):
  - **part C:** 4 of 4 HTTP 200, and the journal shows 0 re-captures and 0 session_refresh (@`c3e77cb937`). ~Y graded
    the catalogue v2 identities 4 of 4 (@`820fef003a`).
  - **part A:** ~D's round-8 walk is done. The round-8 L8 packet is FINAL (@`eaebc81ade`) and goes to 3.0.0_SA_CVO.
  - **part B:** arm 1 is met: QUEUED in 3.1 s, measured at the client. **Row S26:** the QUEUED answer carries no
    `data`, so the page never polls. Arms 2-5 are to be reported from the served side.

## Rulings

1. **S26:** the backend restores the contract. The QUEUED answer carries receipt-shaped data (the exr_ handle,
   NOT_READY). ~P delivers it as a delta packet, and ~D needs no portal cell (102114/5).
2. **~M 102110 (UIC-16):** no self-written Schwab code decode. INF's full account type lands on Monday. 49F keeps its
   codes until Schwab's registration-code list is obtained, carded to Andrew.
3. **CRO 102100 (Andrew-direct /ui-walk cleanup brief):** placed as DSGN_IRPTV1 PRD **v0.18** @`5d44d0fa62`.
   - UIC-01..23 each sit under an existing FWD, with the acceptance line verbatim.
   - The ENDPOINT is byte-identical (checked).
   - Routed to ~D for round 9, UIC-06 to ~P, UIC-15/16 to ~M.
   - The re-grade leaves 8 UIR rows NOT MET.

## Open calls in scope

1. CARRIED, at Andrew: Schwab's account-type / registration code list for 49F's full account types (UIC-16). REC: ask
   49F's Schwab rep, or point to the file spec.

## Completion test

NOT DONE: 0 of 2 IRPT projects are complete (both `active`). D10 is UNMEASURABLE (no members).

## Next

- 3.0.0_SA_CVO's round-8 slug, then this seat's round-8 analysis.
- ~P's S26 packet, then the K8 re-run.
- MSTR's S19 purge freeze, ~03:00-05:00Z.

state: ARMED
