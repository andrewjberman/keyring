# Drive log -- 2.0.0_SA_COO~P -- 2026-10-03 18:3xZ-20:1xZ: B2, B3, leg V and two defects found by the walk

## The P-2 window (ledger `irpt-p2-window-20261003`)

- **B2:** PROD 98a98e70fb, portal-v2.1.197 (MSTR 104689). This seat measured is-ancestor for B1's commits.
- **B3:** applied 18:44:32Z. Live adapter NU6YVERL. The live zip reads 49F not composed and carries PathARetiredForFirm. B3
  closed; ledger @f60ed456af.
- **V, half 1:** the CVO reproduced the FWD-8 pair on served gold (0.4738 / -0.4998 / 0.0264 pp). FWD-8 is REALIZED
  (@89c0fbfa46). This closes S22, W1-S18, W1-S19, W2-S3 and W5-S2.
- **V, half 2:** ~D's signed-in walk on PROD code (msg 104700). Tab PASS, print PASS. Export FAIL with
  DEPENDENCY_UNAVAILABLE. The page still calls PATH A and gets OBJECT_NOT_COVERED.

## Defect 1 -- row S307 (@3376d7b446)

**The trace,** read from the export, edge, authorizer and read-Lambda logs at the same second:
- the edge V3 accepted the render-delegate token;
- the API Gateway authorizer V2 refused it as a "non-render route";
- RENDER_ROUTE_CLAIMS held three routes, and IB-pr-304 had widened only V3.

**The fix:**
- CTO batch 226: fix forward, no window rollback.
- Round 42 IB-pr-307 issued @6850506b19. Worker ~110 (node_modules copied locally; the test imports a bun bundle). 9 of 9
  tests; the human path is byte-unchanged. Drained @79db37c149.
- Packet @5c92c0a. CTO half batch 227, with one added stop.

**The act** (ledger `irpt-authorizer-series-render-20261003`):
- N1: 401 on 4 of 4 before and after.
- D1: built gQp2IooA.
- D2: applied 19:52:32Z.
- Stop: ~D's signed-in GETs answered 200 twice.
- P2: a foreign-account render token was refused 403 at V2's new entry.
- P1: the export was ACCEPTED and frozen (receipt exr_07fe19290b7846e39a6afa0a; series version H1BKI, sha256, as_of
  2026-10-01).

## Defect 2 -- row S308 (@cd24c46d57), owner ~D

- Render command 8f095a01 FAILED: "This print URL names no selection".
- The served `PrintEntry-lFovSTi6.js` reads account and version, but its performance check G(e) still requires selection.
  PATH B's print query sends account, start, end and version.
- ~D was told. The fix is: accept the PATH B query, land on DEV, then MSTR promotes.
- Asked of the CTO: close the authorizer ledger on S, P2 and the freeze, and carry the READY-receipt arm to leg V?

## Held

E3 (the one Black Diamond population pull) stays held per Andrew-direct 17:3xZ.
