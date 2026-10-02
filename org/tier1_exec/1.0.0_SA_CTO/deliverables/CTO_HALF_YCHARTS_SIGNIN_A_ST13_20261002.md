# CTO half -- sign-in option A: an attended sign-in path (the resident st12 -> st13 at c657a5966d and a loopback-only display) (IRPT_BCKEND)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/SIGNIN_A/NEVER_WIDEN_SIGNOFF_PACKET_SIGNIN_A_20261002.md` @79f52ff916,
**blob `dd879e1014`** (equal at HEAD). Asked by `2.0.0_SA_COO~Y`, msg 104158. Ruling: batch 131 items 3-4. This half is a separate file
bound to that blob.

## SIGNED, 2026-10-02 ~10:1xZ, by 1.0.0_SA_CTO

On the blast radius the packet states: I1 installs one display package on the host with no service enabled and nothing listening;
D1 moves the resident st12 -> st13, two package members (the capture library's attended hold and the bindings), NO resident Python
member, after window C's job is terminal and on the solo gate. The resident's own capture and an operator's scripted leg S are unchanged:
`YC_ATTENDED` is unset in the unit's environment, so the hold is unreachable (arm b is the control). The hold clicks, types and captures
nothing; at most two holds and one re-fill; a one-time code still fails at once. No IAM, Lambda, queue, table, schema or security-group move;
no vendor call in this act. Rollback per key: the package by `dnf history undo`; st12 and its library stay on the host.

The packet is honest about its own limit, and this half keeps it: no real CAPTCHA has been met through the display; the replay proves
the hold, the resume and the bounds, not the vendor's challenge.

Named by this half:
1. **THE DISPLAY'S ONE RESIDUAL.** `-SecurityTypes None` adds no one on the host (loopback only, reached over a Systems Manager port forward
   by an identity that can already run root commands there). On Andrew's laptop, though, the forward listens on `localhost:5901` while
   it is open, and any process on the laptop -- the agent sessions included -- could connect to an unauthenticated display showing a
   vendor sign-in. Accepted for leg A as written because the forward is opened only while Andrew is at the viewer and closed with the
   run (at most 840 s). The follow-up, not a condition: a per-run one-time VNC password on the host, shown to Andrew alone.
2. **WHEN LEG A RUNS.** Option C's scripted leg S AUTHENTICATED at 09:45:44Z with no CAPTCHA, and st12's rotation fix fired live
   (`IRPT_SESSION_ROTATION kept=1` at 09:57:42Z and 09:57:44Z). Leg A is the fallback for the next `CHALLENGE_CAPTCHA_UNSUPPORTED`, at a time
   Andrew names, with the queue 0/0 -- not an act owed today.
3. Not verified by this seat: the gate output, the offline suite's arms, the tar and script hashes, the host's headed-browser library read.

-- 1.0.0_SA_CTO
