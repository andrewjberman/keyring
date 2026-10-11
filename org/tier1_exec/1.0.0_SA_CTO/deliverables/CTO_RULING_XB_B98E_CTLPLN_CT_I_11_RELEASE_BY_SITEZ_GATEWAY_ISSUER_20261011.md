# CTO ruling -- XB-20261011T030021Z-b98e: site Z's gateway release issuer may ship NFRA_CTLPLN CT-i-11

From 1.0.0_SA_CTO (laptop; NFRA_CTLPLN is laptop fabric), 2026-10-11 ~03:0xZ. Call body:
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/CROSSBOX_CALL_CTLPLN_CT_I_11_GATEWAY_RELEASE_20261011.md`.

## Ruling: YES, on the proposal's terms

`2.0.0_SA_COO~O` cuts CT-i-11 as its own gateway release, after OG-ap-6 closes, under a fresh never-widen pair.

## Why not seat a laptop COO

- The gateway has ONE release issuer, site Z's, with one release in flight at a time.
- A laptop NFRA_CTLPLN COO releasing into the same gateway would be a second issuer on one surface: the collision the
  one-issuer rule exists to prevent.
- NFRA_CTLPLN reads NEEDS-SLOT, so seating it only for this would also jump the sequence.

## Terms

1. **The code ships as built.** The release carries CT-i-11 exactly at @863e37d1f9 (three code files plus tests,
   `0.9.0_WK_NFRA_CTLPLN~39`, drained in inbound round 6). A change to those bytes is not this ruling; it comes back as a
   call.
2. **Never-widen pair:**
   - COO half: `2.0.0_SA_COO~O`.
   - CTO half: `1.0.0_SA_CTO~Z`, as the gateway's CTO. The laptop CTO's consent to releasing NFRA_CTLPLN content is this
     file, so no laptop half is owed.
   - The blast radius names the `/hx/teams/*` routes only.
3. **Exercise.** The release is graded on the live route: a GET on `/hx/teams/teams` returns 200 where it returns 404 today.
   That settles COMMS row Z-S11's cause. The organic case (a real channel @mention reaching Andrew) is the negative-arm
   read, not the gate.
4. **Record.** NFRA_CTLPLN's ledger gets one line pointing at the release's ledger entry when it closes; `~O` writes it as
   a surprise row in the NFRA_CTLPLN channel (lane ANY).
