# SIGN-OFF (1.0.0_SA_CTO half) -- UI walk window 25: the S218 step-2 one-body read, one principal

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W25_20260930.md` @`90aebc3952`, blob prefix `f3273476`
(2.0.0_SA_COO~P msg 103126). The blob prefix was printed here from `git hash-object` on the file and matches the ask.
**Signed:** 1.0.0_SA_CTO, 2026-09-30 ~03:3xZ. The 4.0.0_SA_CRO half is asked separately by ~P.

## Read at signing
- **Per-use word:** Andrew's "yeah Yes run it" at the ~P terminal (~03:02Z), record `ANDREW_DIRECT_20260930_030xZ_S218_STEP2_ONE_BODY_YCHARTS_WINDOW_YES.md` @d821060b8b, scope
  the one window as armed, no retry, no second window. I read the record's opening; the packet cites it verbatim.
- **Precondition:** ledger `irpt-resident-st5-yr231-20260930` CLOSED @12dd4b35a5 (root `fe64236bbb-st5`); this seat's st5 half is @9fa83724fe. The packet states the resident has
  handled 0 jobs since install.
- **The act:** one login, one vendor session, one Overview job for cottonwood (the W15 CSV), cap 1, 60 minutes, on a cold resident. Every arm is a write the principal owns plus reads;
  no code, IAM, schedule or resident restart; nothing served for another user moves.
- **Both branches:** a body that fails leaves the REQ as evidence and files a BLOCKING row the same tick with no retry; a misbehaving resident closes the window and its rollback to st4
  is a separate act under the st5 ledger. A named terminal state (READY, or ATTENTION with its code) is a pass; a hang past the cap is not.

## Conditions (each a stop)
1. **Solo, provably:** `irpt-generation` read 0/0 immediately before the K5 and no non-principal job in flight; if other work is live the read waits. (W24 condition 2, carried.)
2. **Pins re-read at create** and written in the ledger (the three Lambda versions, the resident root and worker sha, queue 0/0, DLQ baseline 1 visible / 0 in flight). Any difference, a non-empty queue,
   or another job in flight: the window does not open.
3. **Credoff before the vendor call:** K1-CRED deleted and read back as ParameterNotFound before K4; the password is never printed.
4. **DLQ read before and after.** Any growth over the baseline is a BLOCKING row the same tick. (W22 condition, carried.)
5. **Cap 1, no replay:** a challenged vendor mutation is never replayed; the window closes at 60 minutes at the latest.
6. **Teardown and censuses:** K1 and K1-CRED gone at the cap at the latest (a consistent read finds no item); the users census and `walk_window_census.py` before and after, both printed.
7. **Proof discipline:** the pass is a named terminal state read from the case trace and the resident journal; do not report the eviction-vs-pre-job-rejection diagnosis as settled unless the journal lines say so.

## Not covered
A second body, a retry, any deploy in the window, any change to the resident, and any use of Andrew's word beyond this one window.
