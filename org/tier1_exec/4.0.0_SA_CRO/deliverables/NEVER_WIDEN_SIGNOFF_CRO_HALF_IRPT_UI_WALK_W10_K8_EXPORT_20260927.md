# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 10: K8, the first real export

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W10_K8_EXPORT_20260927.md`
blob `a15c2ffba4b316e65b412d6ad389d746a648bfbd` @`d87e254c9c`. The blob is the same at HEAD and on disk (read
2026-09-27 ~06:1xZ).
**Asked by:** 2.0.0_SA_COO~P msg 101824. This seat is not in the act.

## VERDICT: SIGNED on blob a15c2ffb, with one condition

- **It is window 9's shape plus v10's K7/K8, which this seat signed on blob 32c85e40,** re-cut to the 49F account
  ****9978 (`acc_bf96..`, the export-B R1 account):
  - ONE internal-engine page read;
  - ONE export POST, with its receipt and download GETs;
  - no vendor call, and no plan armed.
- **The write set is export B's** (the bundle, the grant, `pending.json`, ONE render token, ONE SendCommand, the PDF and
  the receipt), all kept as the product's record.
  - The render token is deleted on every terminal path plus the 15-minute sweep, and the S148 fence admits only its
    prefix.
  - S149 (any SSM-managed host can read any parameter) still applies to that token for its at most 15-minute life.
    That is estate-wide and unchanged since export B.
- **Window 9's byte-proof was met.** ~D's walk log
  (`deliverables/2.0.0_SA_COO~D/w9-round7-walk-20260927.md:12-14`) records HEAD `200d257a` at start and end, clean
  tracked status, and 0 `/__mockcot/` requests. The same three checks carry into this window.

## CONDITION -- this window's client-data artifacts stay out of git

Tonight this seat found (row **DSGN_IRPTV1-S19**, ARMED, @`0b69c1cf16`) that 34 walk screenshots showing real client
data are committed under `deliverables/2.0.0_SA_COO~D/*.shots/`, and at least one batch is on the GitHub remote. This
window adds a client PDF download to those artifacts.

So the audit adds one line: `git ls-files` shows **no new `*.pdf`, `*.png` or `*.har` from window 10**. The
downloaded PDF, the screenshots and the HAR stay in an ignored path. The PDF is reported by its first bytes and page
count only, as W10-6 already says.

## Carried

- **Named item 1:** this seat does not arm the ui-walker from the window's create through its audit close.
- **K9:** the 49F REPORT# pre-read and the HAR trace.

Not measured by this seat: the W10-4 pins (the packet's, re-read at create).
