# Andrew-direct 2026-10-12 ~01:5xZ -- execute the tailnet SSH setup (LD-0644), COO~C if available

VERBATIM: "I also want that tailnet port set up so that we can ssh into the various devices as well as rdp, when you have
available capacity, we should make sure that gets executed, perhaps COO~C can handle it if they are available."

Order of record: `org/tier0/ledger/LD-0644.md`. Plan: `LD0644_ROLLOUT_PLAN_CLUSTER_REMOTE_ACCESS_TAILNET_20261011.md` (sections
3 and 7). Wave 1 result (section 7): all four boxes' agent sessions read `elevated=False`; sshd runs only on the laptop (its :22
rule any-address); RDP already tailnet-scoped on all four.

## Placement

NFRA_CTLPLN (laptop fabric; remote access across the four devices is control-plane scope). The CTO adds the outcome as an L10
addendum to the PRD: **FWD-27 -- `ssh <user>@<tailnet-ip> hostname` answers from the laptop for sitez, dell1, dell2 and the
laptop itself, key-auth only, port 22 admitted from 100.64.0.0/10 only, RDP unchanged.** `2.0.0_SA_COO~C` cuts it in its
issuance (one cell per box plus one packaging cell), ahead of E1-E8 if it chooses.

## The elevation fact, stated once

`Add-WindowsCapability`, `Set-Service`, `New-NetFirewallRule` and the `administrators_authorized_keys` ACL need an ELEVATED
session. Every agent session on every box is unelevated (measured), and an agent cannot answer a UAC prompt. So each box's enable
run is ONE elevated PowerShell launched by a person: Andrew, over the RDP that already works, right-click "Run as administrator",
one line. The cell's job is to make that line trivial and its result self-verifying:

1. Packaging cell (COO~C, laptop): `.tools/ssh-tailnet-enable.ps1` -- idempotent; runs section 3 A-D of the plan; takes
   `-PublicKey <path or string>`; refuses to turn password auth off until a key is present; prints BEFORE/AFTER of the service,
   the two firewall rules and the key file; writes its receipt to `org/devices/state/<device>/ssh_enable_<stamp>.json` (device
   from `AGENTBUS_DEVICE`, never hardcoded). Rollback block in the same file (`-Rollback`). Tested on the laptop first (the laptop
   needs only B and D): Andrew runs it elevated once here; the probe from a second shell is the proof.
2. Per-box cells (one each: sitez, dell1, dell2): the box's manager places the script and the public key on the box, prints the
   one elevated line for Andrew, and after his run verifies `:22` OPEN over the tailnet from the laptop plus one
   `ssh -o BatchMode=yes ... hostname` answer, and commits the receipt.
3. Keys: Andrew's public key(s) (his own and `muse`'s) are the input to every cell; they are pasted to the laptop manager, never
   a private key.

If COO~C finds an elevated path the fabric already owns (a scheduled task registered to run as SYSTEM), it does NOT use it
without Andrew's express word: that is privilege escalation by an agent and is listed as an option, not taken.

## What Andrew does, in total

Paste the public key(s); run one elevated line on the laptop; then one elevated line on each of sitez, dell1, dell2 (RDP in,
elevated PowerShell, the line the manager printed). Tailscale ACL (plan section 5) in the admin console at his convenience;
without it, today's any-to-any tailnet policy already admits the SSH.
