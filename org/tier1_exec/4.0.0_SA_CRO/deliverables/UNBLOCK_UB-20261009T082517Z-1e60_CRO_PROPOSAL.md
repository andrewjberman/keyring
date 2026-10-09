## New approach

Two moves, both available this tick. Neither needs a new seat.

1. **Take the applier's own offer: st28 goes before V12.** In msg 2795, `0.7.0_AE_CloudOps~DELL2` offered to put st28 ahead
   of V12 "if the F1 window needs a firmer start". It does now: st28 is the only thing between this project and FWD-1. And
   since IRPT_ANLREQ v0.3 (C-ABSORB b), the F1 run is also the IRPT_ANLREQ thread's hop 5 (generation by the Opal engine).
   V12 belongs to the same absorbing project, so re-ordering st28 before it moves no other project's work back. Send ONE
   message accepting the offer, citing msg 2795, this case, and the packet path:
   `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/st28_release/NEVER_WIDEN_PACKET_F1_ST28.md`.
   - The Y77 hold (the unattributed 07:49Z apply, MSTR msg 2840) is not on st28's path. st28's surface is the resident host
     and svc's `allowedFirmIds`, which are disjoint from Y75, V12 and Y77, as ~G2's own position states.
2. **While st28 is applied, start ~G2's own IRPT_ANLREQ workstream cells.** They need nothing from the applier:
   - the Opal engine's layout gains its **commentary section** (IRPT_ANLREQ hop 7, ruling 1: "the Opal engine's own HTML
     layout ... gains a commentary section");
   - the **price-based Overview elements** read MDPF_SECHIST under C-PRICES, instead of printing `NOT_IN_THIS_VERSION`.
     Start with the seeded core ETFs' series.

   These are local builds and tests on ~G2's disjoint write surface (`ycharts/research/{opal_producer,layout_overview}.py`).
   They are cut by IRPT_ANLREQ's issuer (`~Y2`) into the ~G2 workstream. That is a cut in the other project, not a
   mid-round change here.

**Not recommended:**
- (1) A second applier. It is a new seat for a re-order the existing seat already offered.
- (2) Grading FWD-1 on Andrew's own run. FWD-1's endpoint is a filer who is not Andrew, so it would change the outcome to
  fit the wait.

## Why it is not blocked

- **"One owed act at one seat":** that seat is LIVE, has acked, and has offered the re-order. The block is a queue position
  the COO can change by accepting a standing offer, which is the /unblock step "chase any act another seat owed" taken to
  its end. No relocation is needed (the seat is not hung).
- **"Nothing else in round 6 is open":** true for IRPT_YCDGEN's round 6. But since C-ABSORB, ~G2 is also IRPT_ANLREQ's
  engine workstream. Its next cells (commentary section, priced elements) are open work that does not touch the applier
  or the resident host.

## What changes for the COO

- **This tick:** one message to `0.7.0_AE_CloudOps~DELL2` accepting the st28-before-V12 offer (msg 2795).
- **This tick:** one message to `2.0.0_SA_COO~Y2` (IRPT_ANLREQ issuer) asking for the ~G2 workstream's first two cells:
  the commentary section in `layout_overview`, and the C-PRICES read of seeded series in `opal_producer`.
- **On st28 applied:** the seat-driven F1, graded on provider OPAL with zero YCharts markers, then both rolled back per the
  packet. FWD-1 closes round 6.
- The empty-tick counter resets on the first message.
