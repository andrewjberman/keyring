# /self-drive ~O fabric -- ticks 86-87 (1.0.0_SA_CTO~O, 2026-09-27 21:45Z-22:48Z)

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d.

- **Design ruled (@1973056c51):** MX-s-4 step 1.2, the BD asset-dim REST pull, is designed as ONE cell.
  - A bd-tree bronze module; nothing goes in cot's tree.
  - `assetClass` (dim 1) and `segment` (dim 1138) are qt3/qt4 holding dims (`field_dictionary.md:310-311`, `:574-575`).
  - One ledgered discovery read covers super-class; if it is absent, the value is NULL with the claim `absent`.
  - The pull is unioned with the frozen 04-14 dim, both counts stated.
  - Measured: `bronze/fees/` is current through 2026-09-25, so the fees downloader is a dead path.
  - COO~O closed MX-s-4 on step 2 (A5, @81c13ee0f9). The design goes to a new cut after the freeze.
- **OG-s-1 LANDED:** /sprint is owner-only live.
  - opal-gateway serves `6a98a0553a` (complete @2487a23c33, ledger closed @c0d45da58d).
  - All 12 CTO-half guards held; sp.AC3 PASS on CLOUD @4619ac12ee.
- **W3-S22 DISARMED** by row NFRA_OPLGTW-Z-S7 (@2f60185fb7).
  - /sprint* is closed.
  - /login and /callback are reachable but inert: a restricted profile reaches no Graph tool, and the email-deny guard
    is live for any named person.
  - /login retirement goes to the round-2 enrichment list.
- **Z-S29 redaction:** routed directly to live `0.7.0_AE_CloudOps~I` (file 20260927T224452Z), and MSTR~Z was told.
  AE~I also confirmed the safe-ec2-deploy CR-strip patch is already on origin (765093b0e3).

**Cards at Andrew:**
- (1) the purge add-on for the Z-S29 literal, before about 02:30Z;
- (2) rotate the BD and SmartX passwords;
- (3) the switchover sitting.

**Completion test:** NOT DONE. 0 of 4 projects are complete.
**Freeze:** 03:00Z, with a 02:45Z cutoff. This seat's paths hold 0 uncommitted tracked files.

state: ARMED
