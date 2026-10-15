# ANDREW DIRECT -- WSJ and Barron's ops run on this device (2026-10-15 ~16:0xZ, dell1 terminal, 2.0.0_SA_COO~W1 session)

**Channel:** the `2.0.0_SA_COO~W1` terminal on dell1. Received after the lane's empty tick on parked AMGT_HARVST
(the park: CTO round-85 analysis msg 5592, on `ANDREW_DIRECT_20261013_211xZ_DELL1_SEAT_ALLOCATION_AND_YCHARTS_TO_CRO_DELL1.md`).

**Andrew, verbatim:**

> We can run the WSJ and Barron's ops on this device. You shouldnt need me to sign in because you have scripts for that, but if you need me to do it for whatever reason to get the long term trust token or etc, open a Chromium and I will handle it.

## What it sets (read from the text, scope not widened)

1. WSJ and Barron's harvest operations may run on dell1 (this device). Until now they ran on site Z (`~ZW`), where the refresh failed
   (`SignInRefused: 401 under --no-sign-in: no refresh`, row Z-S121).
2. The lane tries the existing sign-in scripts first. Only if a script cannot obtain the long-term trust token does the lane open a
   Chromium on dell1 and Andrew signs in there.
3. It does not say whether AMGT_HARVST un-parks as a project. That is the CTO's call; this record is the carrier.

-- recorded by 2.0.0_SA_COO~W1
