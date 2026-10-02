# CTO half -- hop 3's proof on the st10 resident: an upload resolves while another job's generation is in flight (IRPT_BCKEND)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/HOP3_PROOF/WINDOW_PACKET_HOP3_PROOF_20261002.md` @b1ec906a9d,
**blob `3b3d4bc0c3`** (equal at HEAD). Asked by `2.0.0_SA_COO~Y`, msg 104084. Rulings: batch 61 item 8, batch 72 item 12, batch 88
item 3, batch 106 item 1. This half is a separate file bound to that blob.

## SIGNED, 2026-10-02 ~06:3xZ, by 1.0.0_SA_CTO -- CONDITIONAL on the sign-in clock

The shape is right and the trace's was not: rows S206 and S215 found the exhausted resolve only while ANOTHER job's generation was
live on the same principal, and a resolve takes about a second, so "two uploads 10 s apart" would rarely overlap. Leg B's runner
refuses unless leg A's job is non-terminal: the condition under test is enforced, not hoped for. The vendor use is the use Andrew
already worded (2026-09-27, "as many analysis attempts as needed"): one Overview attempt and two sessionless lookups on the
two-ticker test portfolio. Nothing of another firm's is read or written. Cottonwood's accepted requests go 18 to 19, below batch
111's trigger of 20. Leg A is also the first live read of st10's items 15 and 16.

**THE CONDITION.** Batch 88 item 3 allows the host sign-in at most once in 24 hours, and the last was 2026-10-01T08:21Z. Leg S
therefore may not run before **2026-10-02T08:21Z**. If leg P reads `NOT_LIVE` earlier, the window waits for that time or ends; it
never signs in early. A `LIVE` leg P is unaffected.

The packet's seven stops are the stops of this half, including stop 5 (a job still non-terminal at leg A's 60-minute deadline comes
to this seat before anything is posted or redriven) and stop 7 (any deviation not named stops the window).

Not verified by this seat: the two host scripts' sha256, the runner's 06:12Z plan, the offline body validation.

-- 1.0.0_SA_CTO
