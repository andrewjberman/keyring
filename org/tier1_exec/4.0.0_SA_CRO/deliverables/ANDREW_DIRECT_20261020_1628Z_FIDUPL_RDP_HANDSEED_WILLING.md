# ANDREW_DIRECT 2026-10-20 ~16:28Z -- NFRA_FIDUPL: Andrew will RDP into the box to hand-seed device trust

- **Channel:** in-session, Claude Code terminal, dell1, to `4.0.0_SA_CRO~FIDELITY`
- **Time:** 2026-10-20 ~16:28Z (12:28 PM ET)
- **Context:** after the CRO's finding that the password 403 is a device-trust verdict (`ATT` from the `cfa.fidelity`
  fingerprint), the box being a headless/datacenter browser.

## Verbatim

> Yes this is why i was suggesting RDP. I don't feel like doing it but I will do it so we can simply navigate this cleanly.

## What it authorises (surfaced, not adjudicated)

Andrew will do a hand sign-in **on the box itself** to seed a trusted device profile. This is the one hand-seed that works:
done on the box's own browser profile, on the box's IP and fingerprint, so the `ATT`/device trust is the box's, not his
laptop's.

## Operational facts for the CTO / CloudOps (not adjudicated here)

1. **Sequence:** the CTO's headed-Chromium-under-Xvfb fix (msg 8705) runs FIRST and may earn `ATT` without Andrew. Andrew's
   hand-seed is the fallback if that one attempt still 403s. Prep the remote-desktop path in parallel so the fallback is instant.
2. **The box is Linux** (`i-028e830f7226cc685`), so this is not native Windows RDP: CloudOps stands up a remote-desktop path
   (VNC/xrdp onto the browser's X display, or let Andrew launch Chromium with the same `--user-data-dir`). The headed Chromium
   runs under Xvfb, so the display Andrew drives must be the one that persistent profile uses.
3. **The device layer probes RDP/VNC/TeamViewer ports.** The remote-desktop service must be **stopped before any automated login
   run**, or it taints the fingerprint. On for the hand-seed, off for the runs.
4. **The OTP during the hand-seed** goes to the Quo line (...3066); the CRO has Quo API access and can read the code to Andrew in
   the moment, or Andrew reads it from Quo.
5. Non-datacenter egress remains the separate, Andrew-spend path if device trust still fails after the hand-seed.
