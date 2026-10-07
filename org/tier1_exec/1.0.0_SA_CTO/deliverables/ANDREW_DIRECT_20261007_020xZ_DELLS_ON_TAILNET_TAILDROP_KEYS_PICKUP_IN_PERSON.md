# ANDREW-DIRECT 2026-10-07 ~02:0xZ -- dell1 and dell2 are on the tailnet; the AWS keys go by Taildrop; he picks them up in person

**Channel:** typed at the `1.0.0_SA_CTO` terminal (laptop). **Recorded by:** `1.0.0_SA_CTO`, same turn.

## Verbatim

"Both dells are on tailscale already, they are on tailnet as dell1 and dell2. i would recommend doing the taildrop. once its done, let me know
and i can go to each server in person and write in the terminal to pick up the credentials"

## Measured by this seat, ~02:0xZ, from the laptop

- `tailscale status`: dell1 100.79.95.44 (windows), dell2 100.104.84.87 (windows), account Andrew@. `tailscale ping`: both pong (4 ms, 6 ms).
- Port 3389 answers on both over the tailnet (`Test-NetConnection`). Whether each Dell's Remote Desktop rules are scoped to the tailnet only
  (the setup document's section C) is NOT measured from here; it is read on each box.

## Rulings

1. **Key delivery: Taildrop**, his choice. After site Z applies NFRA_CTLPLN's IAM (C-IDENTITY), site Z creates ONE access key per Dell user
   (`cloudops-dell1-agent-user`, `cloudops-dell2-agent-user`), writes each to a file, sends it with `tailscale file cp <file> dell1:` (likewise
   dell2), deletes its own copy and reads back that it is gone. The key never enters Terraform, git, the bus or any message.
2. **Pickup:** Andrew, at each Dell, runs `tailscale file get <folder>`, imports the key with `aws configure --profile <user>`, then deletes the
   file. The steps reach him from this seat when both sends are done.

-- 1.0.0_SA_CTO
