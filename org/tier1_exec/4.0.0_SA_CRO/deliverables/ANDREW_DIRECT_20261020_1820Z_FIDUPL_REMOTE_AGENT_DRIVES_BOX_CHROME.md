# ANDREW_DIRECT 2026-10-20 ~18:20Z -- NFRA_FIDUPL: a remote Claude agent drives the box's Chrome; no Claude account on the box

- **Channel:** in-session, Claude Code terminal, dell1, to `4.0.0_SA_CRO~FIDELITY`
- **Time:** 2026-10-20 ~18:20Z (2:20 PM ET)
- **Bears on:** `TO-FU-s-11` (the Claude-in-Chrome fallback) and the CTO ruling @c618ca8c8c.

## Verbatim

> Is there a reason we can't send a claude agent from this device to run the RDP? Why do we need a claude account signed in on the
> device itself?

## The answer the CRO gave, for the record

The controller (the agent) and the browser are separable. Only the browser must live on the box.
- **Browser on the box is required** because the daily pull runs unattended on an always-on server, and device trust (the `ATT`
  token + the `cfa.fidelity` fingerprint + the egress IP) is earned per-machine. Signing in from dell1 would earn dell1's trust, which
  does not help the box's scheduled run, and the firm feed must not depend on Andrew's laptop being on.
- **The agent/account need NOT be on the box.** A Claude agent on dell1 (or this session) can drive the box's headful Chrome over the
  VNC/SSM tunnel by screenshots-and-clicks (computer-use). The browser stays on the box, so Fidelity sees the box's trusted device,
  while the controller sits remote. No Claude account or extension is installed on the box for that.

The build leaned to a plugin+account on the box only because the Claude-in-Chrome extension normally lives inside the Chrome it drives.
The remote-VNC drive avoids it.

## Steer to the CTO (surfaced, not adjudicated)

`TO-FU-s-11` becomes "a remote Claude agent drives the box's Chrome over the existing VNC/SSM tunnel" rather than "install the
Claude-in-Chrome plugin and sign a Claude account into Chrome on the box". To verify: whether the agent drives via (i) a VNC
computer-use session (screenshots + input, no plugin, no account on the box), or (ii) the Claude-in-Chrome extension pointed at the
box's Chrome from a remote session. (i) needs nothing installed on the box beyond the VNC that CloudOps already stood up
(`nfra-fidupl-vnc-20261020`). The scripted headful-Chrome path (Track A) is unchanged.
