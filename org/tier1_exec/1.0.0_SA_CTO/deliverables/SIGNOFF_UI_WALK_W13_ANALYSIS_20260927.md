# CTO half -- UI walk WINDOW 13: the Analysis chain, fifth attempt, on resident cw (packet blob 49ee40b0) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~13:5xZ. **Request:** 2.0.0_SA_COO~P msg 101899.

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W13_ANALYSIS_20260927.md`
@`eea3452029`, blob `49ee40b0`. Read at HEAD: `git hash-object` equals `git rev-parse eea3452029:<path>`.

**The base text:** window 11, blob `9ee0c7c5` (CTO half @`1e5b0a08af`), re-hashed at HEAD.

## What was read

- The file was diffed against window 11. It carries W11-2's start condition (Andrew's "as many analysis attempts as
  needed" @`460e2ae8cb`; ONE upload and ONE Overview, no retry), W11-3's bounds, D2, and every signing condition:
  - CTO 101875: bounds counted from the resident journal, AWSPREVIOUS kept, an overrun is a BLOCKING row;
  - CRO 101877: the running re-capture total is printed.
- **The served code:** resident `fe64236bbb-cw` since 13:51:07Z carries ~Y's two window-11 fixes (backend
  `b6739556ea`):
  - `capture_env`, which strips PYTHON*;
  - the saved-portfolio read-back.
  - The census against wf shows the 3 patched members plus bindings; the queue was 0/0; rollback to wf is kept
    (@`45c9ac981e`), on the terms set at CTO 101897.
- **The one added vendor call:** ONE `GET /model_portfolios/fixed/{id}` after `available`, as named at CTO 101897. It
  is a read, the research worker's proven one.
- Window 13 is created only after window 12 closes: one principal at a time.

## Named item

None new. Window 11's conditions carry unchanged.

**CTO half: SIGNED on blob 49ee40b0.** The CRO half is separate.
