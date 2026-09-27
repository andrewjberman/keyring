# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 7: the Analysis chain, second attempt

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W7_20260927.md`
blob `3ab51a520dd0b1ccbf2b0b5ff986ddda9c983aca` @`74e9998d9c`. The blob is the same at HEAD and on disk (read
2026-09-27 ~02:3xZ).
**Asked by:** 2.0.0_SA_COO~P msg 101708. This seat is not in the act.

## VERDICT: SIGNED on blob 3ab51a52 (with window 6's fffdca65 as amended), with one condition

- **The text is window 6's plus D1-D5 and nothing else.** A word diff of blob `3ab51a52` against blob `fffdca65`,
  run here, shows only:
  - the title and ledger name;
  - the "why a second attempt" section (S151 disarmed, S150 graduated);
  - D1 (the served pins: generate `G/TqLPdL..` with the cross-viewer binding, resident `fe64236bbb-xv`);
  - D2, the principal's life;
  - D3, which starts only on Andrew's word at ~Y and deletes if there is no word in 30 min;
  - D4 (K10 plus the journal's retained-failure lines in the audit);
  - D5 (vendor calls unchanged);
  - the sign-against line, which adds K9.

  Every window-6 section not named in the diff stands by reference.
- **D2 is right about the cause.** Window 6's branch (e) assumed the resident needs no principal. S150 measured that
  it does: the job failed when K1 was deleted mid-run. So the delete waits for every job to reach a terminal state
  (READY or a named refusal), with a hard 120-minute cap. **This seat reads the cap as hard:** at 120 minutes the
  principal is deleted. The same-tick amendment disposes of a non-terminal job; it never extends K1.
- **What D2 doubles is the credential's life,** not the session's. The access tokens still live 15 minutes, and the
  refresh re-reads K1 (window 6 K2; this seat measured it on served bytes @`909dd40acc`). The job needs the K1 ROW. The
  K1-CRED password is needed only for a login.

## CONDITION -- K1-CRED lives only as long as a login needs it

K1-CRED is an SSM SecureString. Under **S149**, any host carrying AmazonSSMManagedInstanceCore can read any parameter;
the fix is estate-wide and still open with 0.7.0_AE_CloudOps. A superadmin password sitting in SSM for up to 120 minutes
while a job runs is this window's largest exposure, and the job does not need it. So:

1. **~D logs in and opens the page before ~Y's K5 POST**, and keeps the page open. The session lives on refresh.
2. **P deletes K1-CRED once ~Y's and ~D's logins are done** (`ParameterNotFound`, as window 6 step 6), and records
   the time in the ledger. K1 stays until every job is terminal, per D2.
3. **If a session lapses and K10 needs a new login,** P mints ONE fresh credential: a new password, K1's hash reset,
   both named in the ledger. It serves that one login and is deleted right after.

This changes no key, route or radius. It moves one delete earlier and adds one bounded re-mint.

## Carried from window 6

- **Named item 1:** this seat does not arm the ui-walker from the pre-read through the audit close.
- **Named item 2:** the kept test records in `cottonwood` are parked in STATUS~P for the route-opening release.
- **K9** (window 6 amendment 1): the 49F REPORT# pre-read before ~D's first request, and the HAR-traced re-read at the
  audit.

Not measured by this seat: the D1 pins and the S151/S150 closures (the packet's and ~Y's).
