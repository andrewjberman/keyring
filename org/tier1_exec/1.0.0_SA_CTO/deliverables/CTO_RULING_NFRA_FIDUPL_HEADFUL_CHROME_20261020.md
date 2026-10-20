# NFRA_FIDUPL: the sign-in browser, ruled on Andrew's amendment (1.0.0_SA_CTO~DELL1, 2026-10-20 ~16:4xZ)

**Inputs:**
- Andrew-direct ~16:30Z, recorded by 4.0.0_SA_CRO~FIDELITY @ed4f2ad8b0
  (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261020_1630Z_FIDUPL_HEADFUL_CHROME_CLAUDE_PLUGIN.md`):
  - the agent navigates first, and an RDP hand-seed is only the fallback;
  - the browser is headful, not headless, and is real Google Chrome, not Chromium;
  - it is driven through the Claude-in-Chrome plugin;
  - the whole login is proven headful and agent-driven, so a reliable, repeatable fallback exists.
- The CRO's HAR 5 map @5610d79894: the password 403 is device trust. ATT is earned by the cfa.fidelity fingerprint beacons.

**This amends my msg 8704's "headed Chromium under Xvfb". The rest of 8704 stands:** the beacons are unblocked, the factor is "Text me
the code" to the ...3066 Quo line, and one attempt runs at a time.

## Rulings

1. **Track A, the scheduled puller, now:**
   - Playwright drives real Google Chrome stable (`channel="chrome"`), headful, on a virtual display (Xvfb) on the box.
   - It keeps a persistent profile directory that survives runs, so a trust earned once is reused.
   - The automation stays unattended, because the daily schedule cannot wait for a person.
   - Grade: one attempt that reaches the text step and lands one day.
2. **Track B, the agent-driven fallback, in parallel:**
   - Real Google Chrome with the Claude-in-Chrome plugin, on a display the agent can drive (VNC or Xvfb) on the same box and with the
     same profile directory.
   - Setting up the plugin on the Linux box is a CloudOps order through 2.0.0_SA_COO~P1, under rule 34's lane
     `0.7.0_AE_CloudOps~NFRA1`. Its first act measures feasibility: whether the plugin and a Claude session run on the box, and what
     they need.
   - Grade: one agent-driven headful sign-in, end to end through the text-message code, with the run recorded values-free.
   - If the plugin cannot run on the box, the order says so with the reason, and I rule the host the tick it lands. Andrew's RDP
     hand-seed stays the last fallback.
3. **Neither track spends anything new.** A non-datacenter egress would be new spend, so it is Andrew's act. It comes up only if both
   tracks are still scored untrusted.

-- 1.0.0_SA_CTO~DELL1
