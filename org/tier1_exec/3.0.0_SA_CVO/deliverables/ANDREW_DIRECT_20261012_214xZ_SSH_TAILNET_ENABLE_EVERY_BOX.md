# ANDREW-DIRECT 2026-10-12 ~21:4xZ -- SSH over the tailnet on every box (FWD-27; disarms W61-S1)

Recorded by `3.0.0_SA_CVO~L` (laptop) at the `3.0.0_SA_CVO~L` terminal. Andrew's words, verbatim:
- "I am at my desk and can run the necessary elevated panels at all devices to allow for ssh. what do you need run at this device + the other dells and sitez as well as \"rc\""
- "have MSTR send this to each box's manager with instruction that i will be there to run escalated"
- "dont put command and key in commit, needs to be taildropped only"

## Rule

The SSH enable command lines and the public key are never committed and never sent on the broker or the bus. They reach each
box ONLY by Taildrop, as one file from the laptop. This record names the procedure, not the key.

## What each box's manager does

Andrew will be at each box to run the ELEVATED step himself; no agent session is elevated. The manager:
1. updates the box's `ajb_workspace` checkout so `.tools/ssh-tailnet-enable.ps1` is present (5f4c551c4c is on every
   `origin/box/*`);
2. confirms the user variable `AGENTBUS_DEVICE` names the box;
3. takes the Taildropped file (`tailscale file get`) and has its STEP 1 line ready for Andrew;
4. after Andrew's run, reports the receipt line (SSH-ENABLE ... and the RECEIPT path). The receipt prints only the key's
   fingerprint, never the key.

STEP 2 (switching password login off) follows only after `3.0.0_SA_CVO~L` confirms a key login from the laptop to that box. It
is in the same Taildropped file.

"rc" is not a box in `org/devices/DEVICES.json` (laptop, sitez, dell1, dell2). It is OPEN until Andrew names it.
