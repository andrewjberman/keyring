# ANDREW-DIRECT 2026-10-05 ~12:5xZ -- three calls: site-Z no standby; /yearinreview owner-only; DSGN r37+r38 DEV push

- **Channel:** the site-Z terminal of `0.0.0_AB_MSTR~Z` (session 701d71e1-0145-49b8-9bad-582fbd5d8b4b), typed by Andrew.
- **Time:** 2026-10-05 ~12:5xZ (08:5x ET).
- **Recorded by:** `0.0.0_AB_MSTR~Z`, same turn.

## The three calls he answered (this seat's cards)

1. "Standby on site Z: set it to never sleep on AC power? I recommend yes." The site-Z power plan sent the box into
   Modern Standby after 600 s idle on AC (STANDBYIDLE and VIDEOIDLE AC = 0x258). That caused the 2026-10-05 05:14-08:32
   local stall and his RDP failure.
2. "/yearinreview: visible to every signed-in Opal account (my recommendation), or only you?" (`2.0.0_SA_COO~O` msg 29458,
   release r17b.)
3. "DSGN rounds 37+38: push to DEV once the fix lands? I recommend yes." (`1.0.0_SA_CTO~Z` msgs 29491 and 29550; the
   required CardFooter fix is owed by `2.0.0_SA_COO~D`.)

## Verbatim

Andrew: "regarding your 3 decisions: 1.) Yes. This is the intention of the mson script, but maybe it glitched out, if
there is a more stable solution that would be ideal. 2.) Visible to me only. Eventually will be visible to select managers
at my discretion. 3.) Yes, recommendation approved."

## Scope as read (surfaced, not adjudicated)

1. Site Z never enters standby on AC: the plan's standby and display idle timeouts on AC become 0 (never). The persistent
   power-plan setting is the more stable path, because it does not depend on a running script. No file, task or Run
   key named "mson" was found on site Z (repo name census 0 hits; Startup folders, Run keys and root scheduled tasks read).
2. /yearinreview is OWNER-ONLY, like /sprint. Later it extends to managers Andrew selects, at his discretion.
   `2.0.0_SA_COO~O` changes the kit before r17b deploys.
3. The DSGN r37+r38 portal stack goes to DEV once `2.0.0_SA_COO~D`'s required fix lands and `1.0.0_SA_CTO~Z` confirms it,
   merged onto current DEV. DEV only.
