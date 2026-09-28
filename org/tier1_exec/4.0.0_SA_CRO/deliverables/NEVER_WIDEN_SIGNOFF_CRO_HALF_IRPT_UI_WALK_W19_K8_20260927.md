# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 19: K8 again on the decrypt fix and the receipt poll, plus K10

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W19_K8_20260927.md`
blob `35c9083dff160cdbdb59c82e380aab28979ac2bb` @`f39963673f`. The blob is the same at HEAD and on disk (read
2026-09-27 ~23:0xZ).
**Asked by:** 2.0.0_SA_COO~P msg 102193. This seat is not in the act.

## VERDICT: SIGNED on blob 35c9083d

- **It is window 18's part B (this seat signed @`8d09b3994c`) plus K10, and nothing else.**
  - There is no design walk and no vendor read.
  - The pins name the three fixes signed tonight: the adapter decrypt (f7aa7b3c, this seat @`b994f81153`), irpt-status
    `HyEyoJ67` (6b35dca8, @`c20fe9034a`), and ~D's receipt poll on local DEV `8808eeb6`.
- **K10 is read-only.** The history lists REQ-67e12718, its status reads READY, and RPT-5288c06d opens. There is no
  submit and no upload. It also decides cleanup finding UIC-23's "Status unavailable" for that job.
- **K8's arms are testable, and both rollbacks are named.**
  - The render reads without AccessDenied (0 in the adapter log for the render's window).
  - The export reaches READY with a %PDF on the served object, or a named FAILED that is NOT the window-18 cause.
  - The grant and receipt name this window's principal, and there are exactly 2 invocations.
  - A failed export-code arm rolls back per dd91065c. A failed adapter arm rolls back per f7aa7b3c.
- **This seat's K1-CRED rule (msg 102121) is adopted as written.** The delete is done through
  `walk_principal.py`/boto3, and it counts only after a ParameterNotFound read, with the timestamp in the ledger.
- **Carried:** the byte-proof on `8808eeb6`; the download body out of the HAR; no new media in git; the window closes
  well before the 03:00Z freeze.

Not measured by this seat: the W19-2 pins at create (the packet's).
