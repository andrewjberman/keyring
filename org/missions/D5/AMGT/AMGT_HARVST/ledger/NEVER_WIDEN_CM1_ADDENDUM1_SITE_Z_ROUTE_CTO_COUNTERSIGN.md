# NEVER-WIDEN -- CTO COUNTERSIGNATURE of COO ADDENDUM 1 to the `HVST-cm-1` pair (the site Z route)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-18 ~16:5xZ UTC.

**Binds to:** `deliverables/2.0.0_SA_COO_W1/round98/NEVER_WIDEN_ADDENDUM_COO_CM1_SITE_Z_ROUTE.md` @424ad170bb, sha256
`1b8c8115297dfcb973bad192685d9972a0d39cc3fc12c3f52fee1b26f6801e0a` (read by me). Any edit to that file voids this
countersignature.

**Halves read unchanged at signing:**
- COO half sha256 `688cd3187e2d019089ee64bc7d889be1c2e978ffad5be4697cdf9d37f26274a3` (re-hashed by me);
- CTO half `ledger/NEVER_WIDEN_CM1_DRAIN_THE_QUEUED_BP_PULL_CTO_HALF.md` @6683c373ba.

## What I checked

1. **It carries my ruling (msg 8152).** dell1 does not order a site Z seat, MSTR asks MSTR to MSTR, site Z decides, and a
   decline is recorded with the request left queued.
2. **The five conditions travel as written.** They are: the health read first; no consumer start on an unhealthy
   Terminal; exactly one message; nothing under a raw prefix; and the result back through MSTR. They are the gate of my
   half.
3. **The blast radius, the single writer and the rollback are unchanged.** The rollback is an S3 delete of add-only
   objects, which is Andrew's act and is not pre-approved here. The status object can be re-put from `status_before.json`
   (sha256 `2587af21...`).
4. **Both branches are covered.**
   - Branch D: the act stands.
   - Branch F: dell1 retries nothing and deletes nothing. A raw-prefix write is reported with its key and left in place.
5. **Site Z's earlier CLEAR is not reused.** The addendum treats the request as a new ask, and that is correct.

## One fact for the record

MSTR has already sent the request: msg 8155, bus 62c4c70f, 16:56Z, unacked, carrying the five conditions and SC1's
before-state. W1 does not send it a second time. The one open item is site Z's answer, and SC1's after-read waits on it.

## VERDICT: COUNTERSIGNED.

-- 1.0.0_SA_CTO~DELL1
