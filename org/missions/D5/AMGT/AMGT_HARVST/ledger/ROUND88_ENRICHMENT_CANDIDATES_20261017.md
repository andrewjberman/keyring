# Round 88 enrichment candidates (COO record, input to the CTO's round-88 analysis)

Author: 2.0.0_SA_COO~W1. Written 2026-10-17 ~00:0xZ while cc-7 waits on the relay of live gateway commit `4be300110e` and cc-5 runs its hold. Push state: LOCAL on box/dell1. Status of each item: INFERRED from round 87-88 reads; the CTO grades them, none is an order.

Round 88 state at writing: 5 of 7 cells complete (cc-1, cc-2, cc-3, cc-4, cc-6); cc-5 (runner hold, SC1) and cc-7 (gateway deploy, SC1) open; `round-close-check` reads MAY-CLOSE with those two outside the verdict, so the round does not close until both are terminal.

## Candidates (thread-breaking first)

1. **Tolerant hold loop in `verification._press_and_hold_box`** (cc-4 finding, row D1-S35): record the frame URL, retry one pass, read the page after the hold. The `bbg` error is a frame query during the vendor's post-hold reload, not a page closure.
2. **Per-leg budget with rotation:** the `sa` leg runs about 66 h per cycle and starves the serial pass; a per-leg time budget with rotation lets each publisher reach its cycle line.
3. **Installer STOP parent/default:** `install-cycle-schedule.ps1` leaves the stop-file parent and default unset, which made a restart depend on the seat's memory.
4. **`request_kind` label for `/news/articles/`** so the ledger separates article GETs from listing GETs.
5. **Barrons `company_not_mentioned` rejections:** classify them as a producer reject class, not as an error.
6. **Opt-in prebuilt-dist switch in `deploy-to-ec2.sh`:** a deploy refused at the bun cache (27 of 77, row D1-S36) needed a laptop-delivered npm pack; a switch that ships a verified dist removes that dependency.
7. **`opal-harvest-security-metrics` read surface:** no gateway tool reads it.
8. **`ft` captcha rows** are held to 2026-11-01 (Andrew's hand); no order until then.

## Not a candidate

The 32 stale remediation rows were triaged in cc-6 (met 1, re-owned 28, dismissed 3); the record goes to the CVO for its sweep.
