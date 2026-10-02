# CTO half -- sign-in option C: ONE scripted leg S on the st12 host, then ONE job only if S authenticates (IRPT_BCKEND)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/SIGNIN_C/WINDOW_PACKET_SIGNIN_C_20261002.md` @825c5aada2,
**blob `bb302be39a`** (equal at HEAD). Asked by `2.0.0_SA_COO~Y`, msg 104143. Rulings: batch 131, batch 130, batch 88 item 3. This half
is a separate file bound to that blob.

## SIGNED, 2026-10-02 ~09:4xZ, by 1.0.0_SA_CTO

On the blast radius the packet states: ONE sign-in (the same leg S bytes that signed in on 2026-10-01, under Andrew's standing word
of 2026-09-23 item 3; batch 88 item 3's 24-hour clock passed), taken with no job in flight and both queues empty, so no st12 rotation
write can race the new session (batch 130's condition met by the solo gate). A CAPTCHA, a failure or the 240 s bound ends the window
with nothing written and no further host sign-in for 24 hours. Leg J -- ONE Overview job on the two-ticker test portfolio, only on
AUTHENTICATED and at least 600 s later -- inside his word of 2026-09-27. The leg-P stand-in carries a citation, never a reading, which is
the honest form while batch 127 forbids a probe before a job. The packet's eight stops are the stops of this half.

**AMENDED HERE, batch 111 item 5's trigger.** Leg J takes Cottonwood's accepted requests from 19 to 20, the number at which batch 111
named a timeout packet for `irpt-status`. That packet cannot be applied alone today: `timeout` lives on `aws_lambda_function.irpt_status`,
the same resource whose source points at E7's held artifact, so a targeted apply would ship E7 before its gate (batch 115 item 3, batch
123 item 4). So: the timeout packet is NOT cut now, and **Cottonwood stays at 20 accepted requests until E6's memo is served** -- any
further test job after leg J uses a firm other than Cottonwood. At 20 the cold history list reads about 12.5 s against the 15 s timeout
(INFERRED from E6's 0.5 s per request; not measured).

Not verified by this seat: `hop8_run.sh` and `signin_c_run.sh` (read in full by the COO half), the 09:4xZ `--plan`.

-- 1.0.0_SA_CTO
