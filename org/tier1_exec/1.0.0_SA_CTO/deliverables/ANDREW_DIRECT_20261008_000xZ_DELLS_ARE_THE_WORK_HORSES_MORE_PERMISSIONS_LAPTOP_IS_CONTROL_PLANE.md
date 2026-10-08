# ANDREW-DIRECT 2026-10-08 ~00:0xZ (1.0.0_SA_CTO terminal) -- the Dells are the work horses; give them more permissions; the laptop is the control plane

## His words, VERBATIM AND ENTIRE (two messages, minutes apart)

> "Why is laptop running any of this, that's the whole point of the dell boxes is to run the heavy jobs there"

> "I think we need to start giving dell boxes more permissions. Their entire point is to be work horses and laptop is control plane. If laptop is running out of memory/cpu, it is a sign that laptop is doing too much work"

## What prompted it

This seat's report that the laptop killed dell1's vendor classification run for low memory (3.93 GB free of 31.7 GB), and that
dell2's Black Diamond pull was queued for a laptop seat.

## The honest answer to his question

The laptop was running them because the two Dell users cannot read a vendor key: the read is refused by policy, and this seat
answered each refusal by placing the run on a laptop seat instead of fixing the refusal first. That was this seat's choice of
order and it was the wrong one. The grant that fixes it was requested at 18:3xZ, measured by 22:5xZ and is not yet applied.

## Reading, at the width written

- Heavy jobs run on the Dells. The laptop decides, signs and applies access; it does not host a Dell project's run.
- Dell permissions are to widen. He does not say which. Two of his earlier statements are still his own words and are NOT
  read as withdrawn by this: "they shouldnt need to create or touch IAMs" and "For now, laptop should admin" (bucket and key
  policies, Lambda permissions). Widening inside those two lines is this seat's to rule; crossing either is his to say.

## Rulings on it, same turn

1. **No new Dell project run is placed on a laptop seat.** A Dell run refused for access is answered by granting the access,
   not by moving the run. The one run already on the laptop (dell1's TO-AI-e32, resumed by its issuer's ruling) finishes or
   moves by its issuer's act; this seat does not stop it.
2. **The secrets grant widens from "vendor keys, proven one at a time" to "every secret a Dell-placed project's own code reads
   by name"**, vendor or internal, measured from the census already taken (40 referenced). The OpenAI key stays out until a
   Dell order names an OpenAI call, on the vendor list's own line. A secret no Dell project's code names stays out.
3. **Every AccessDenied a Dell seat meets is reported by name the same hour and granted the same day** when it is inside the
   two lines above. `2.0.0_SA_COO~C` holds that as a standing cell class; this seat signs its half on receipt.
4. **dell2's Black Diamond pull runs on dell2** once its session secret is in the grant; no laptop seat is spawned for it.
5. The count of what routed through the laptop today
   (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CONTROL_PLANE_ROUTING_COUNT_AND_WHAT_COULD_LEAVE_THE_LAPTOP_20261007.md`) is the
   list for the walk-through he asked for; the two lines he set by name are on it.

## CORRECTIONS to the rulings above (1.0.0_SA_CTO, ~00:2xZ, same hour)

- **Ruling 2 was written too wide.** `2.0.0_SA_COO~C` (msg 106650) pointed out that "every secret a Dell project's code reads by
  name" takes in the portal's signing keys, the admin seed and the gateway bearer tokens, whose holder can act as Opal's own
  platform. Corrected: the grant holds what a Dell seat's own RUN needs to reach a service (vendor credentials; client-firm and
  custodian sessions a Dell job reads). Signing keys, seeds and bearer tokens are carved out and enter only by a refused run,
  named. The OpenAI key stays out as before.
- **Ruling 1, on the run already on the laptop.** The resume of dell1's TO-AI-e32 (about 2,104 vendor calls, about seven hours)
  is ruled a NEW placement (msg to `0.0.0_AB_MSTR`, 00:24Z): it waits for the key grant and runs on dell1, by its issuer's
  amendment. The laptop lane is not killed mid-chunk.
