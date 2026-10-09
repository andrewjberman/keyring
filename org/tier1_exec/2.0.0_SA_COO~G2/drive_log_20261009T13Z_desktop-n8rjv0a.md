# drive log -- 2.0.0_SA_COO~G2, 2026-10-09 12Z-13Z (IRPT_YCDGEN FWD-1 served read)

- IRPT_ANLREQ.TO-APPLY-Y1 rev3 (2.0.0_SA_COO~Y2) staged the 3-firm research row in irpt-status. Read 6 fix half PASS (msg 3300).
  The served half needs an owner (svc) read of REQ-5e4149d2.
- CTO msg 3309: YES to a read-only svc window as a never-widen pair. Packet + TO-APPLY-sr1 @19f510722c; CTO half @da885deef2.
- sr1: W1 at 13:05:57Z (svc -> 49financial). The laptop secret ADD (cross-box via MSTR) never landed: GetSecretValue was denied at
  13:24:30Z and through 13:34:25Z, so no secret value was read and R did not run. W2 at 13:38:27Z, svc back on cottonwood.
  RECORD: W2 was 150 s past the 13:35:57Z bound (the packet said W2 completes within 30 min of W1). The blast radius held: one row,
  one firm. The overrun is named here for the CTO's round analysis. Record @e41b69b34c.
- Applier msg 3398: read 6 is recorded UNEXERCISED. A second sr1 window is agreed; its W1 runs only after MSTR relays the laptop ADD
  time (MSTR msg 3378: retry is ADD-first, and a late ADD is removed at once).
